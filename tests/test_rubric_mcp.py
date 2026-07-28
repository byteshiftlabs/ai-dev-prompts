"""Unit tests for rubric_mcp.py.

Covers the path-traversal guard, the guide-selection scoring, and the four
MCP tools, all read-only against the real repo content (no mocking of the
filesystem — the guides themselves are the fixture).
"""

from __future__ import annotations

import pytest

import rubric_mcp


# ---------------------------------------------------------------------------
# _safe_resolve
# ---------------------------------------------------------------------------


def test_safe_resolve_accepts_real_guide():
    resolved = rubric_mcp._safe_resolve("core/shared-contract.md")
    assert resolved == rubric_mcp.SHARED_CONTRACT_PATH
    assert resolved.exists()


@pytest.mark.parametrize(
    "path_str",
    [
        "../outside.md",
        "core/../../outside.md",
        "development/..",
    ],
)
def test_safe_resolve_rejects_dotdot(path_str):
    with pytest.raises(ValueError, match="Path traversal not allowed"):
        rubric_mcp._safe_resolve(path_str)


@pytest.mark.parametrize(
    "path_str",
    [
        "rubric_mcp.py",
        "README",
        "core/shared-contract.md.bak",
    ],
)
def test_safe_resolve_rejects_non_markdown(path_str):
    with pytest.raises(ValueError, match="Only .md files are readable"):
        rubric_mcp._safe_resolve(path_str)


def test_safe_resolve_rejects_absolute_path_outside_repo():
    # Path.__truediv__ discards the left side when the right side is
    # absolute, so REPO_ROOT / "/etc/passwd.md" resolves to /etc/passwd.md.
    # The final relative_to() check must still catch this.
    with pytest.raises(ValueError, match="Path outside repo root"):
        rubric_mcp._safe_resolve("/etc/passwd.md")


# ---------------------------------------------------------------------------
# get_index / get_guide / get_shared_contract
# ---------------------------------------------------------------------------


def test_get_index_has_entrypoints_and_guides():
    index = rubric_mcp.get_index()
    assert index["entrypoints"]
    assert index["guides"]
    for entry in rubric_mcp._all_guides(index):
        assert "path" in entry
        assert "summary" in entry


def test_get_guide_returns_real_content():
    content = rubric_mcp.get_guide("core/shared-contract.md")
    assert isinstance(content, str)
    assert "Shared Contract" in content


def test_get_guide_missing_file_returns_error_dict():
    result = rubric_mcp.get_guide("development/does-not-exist.md")
    assert result == {"error": "Guide not found: development/does-not-exist.md"}


def test_get_guide_rejects_traversal():
    result = rubric_mcp.get_guide("../outside.md")
    assert "error" in result
    assert "Path traversal" in result["error"]


def test_get_shared_contract_matches_file():
    assert rubric_mcp.get_shared_contract() == rubric_mcp.SHARED_CONTRACT_PATH.read_text(
        encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# select_guides
# ---------------------------------------------------------------------------


def test_select_guides_always_pins_shared_contract_first():
    result = rubric_mcp.select_guides(task="debug a regression")
    assert result["selected"][0]["path"] == "core/shared-contract.md"


def test_select_guides_pins_model_adapters_when_model_family_set():
    result = rubric_mcp.select_guides(task="debug a regression", model_family="gpt")
    paths = [entry["path"] for entry in result["selected"]]
    assert "development/model-adapters.md" in paths
    assert paths[1] == "development/model-adapters.md"


def test_select_guides_omits_model_adapters_when_model_family_empty():
    result = rubric_mcp.select_guides(task="debug a regression", model_family="")
    paths = [entry["path"] for entry in result["selected"]]
    assert "development/model-adapters.md" not in paths


def test_select_guides_no_duplicate_paths():
    result = rubric_mcp.select_guides(task="debug a regression, review the code")
    paths = [entry["path"] for entry in result["selected"]]
    assert len(paths) == len(set(paths))


def test_select_guides_debugging_task_matches_debugging_guide():
    result = rubric_mcp.select_guides(task="I need to debug a regression in a service")
    paths = [entry["path"] for entry in result["selected"]]
    assert "development/debugging.md" in paths


def test_select_guides_task_guides_sorted_by_descending_score():
    result = rubric_mcp.select_guides(task="review this pull request for correctness and scope")
    # Entries after the pinned ones (shared-contract, model-adapters) must be
    # in non-increasing score order.
    task_reasons = [
        entry["reason"]
        for entry in result["selected"]
        if entry["path"] not in ("core/shared-contract.md", "development/model-adapters.md")
    ]
    scores = [int(reason.split("score=")[1].split(",")[0]) for reason in task_reasons]
    assert scores == sorted(scores, reverse=True)


def test_select_guides_tag_match_scores_higher_than_no_match():
    result = rubric_mcp.select_guides(task="", tags=["debugging"])
    paths = [entry["path"] for entry in result["selected"]]
    assert "development/debugging.md" in paths


def test_select_guides_excluded_count_matches_unscored_entries():
    index = rubric_mcp._load_index()
    total_entries = len(rubric_mcp._all_guides(index))

    result = rubric_mcp.select_guides(task="")
    assert result["excluded_count"] <= total_entries
    assert result["excluded_count"] == total_entries - len(result["selected"])
