"""
rubric_mcp.py — Exposes the rubric prompt toolkit as an MCP server.

Four tools:
  get_index           — Full parsed meta/guide-index.yaml as JSON
  select_guides       — Minimal guide bundle for a task (router-first)
  get_guide           — Raw markdown content of a single guide
  get_shared_contract — Content of core/shared-contract.md directly
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml
from mcp.server.fastmcp import FastMCP

REPO_ROOT = Path(__file__).resolve().parent
INDEX_PATH = REPO_ROOT / "meta" / "guide-index.yaml"
SHARED_CONTRACT_PATH = REPO_ROOT / "core" / "shared-contract.md"
MODEL_ADAPTERS_PATH = "development/model-adapters.md"

mcp_server = FastMCP("rubric")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _load_index() -> dict[str, Any]:
    return yaml.safe_load(INDEX_PATH.read_text(encoding="utf-8"))


def _all_guides(index: dict[str, Any]) -> list[dict[str, Any]]:
    """Return every entry (entrypoints + guides) as a flat list."""
    entries: list[dict[str, Any]] = []
    entries.extend(index.get("entrypoints", []))
    entries.extend(index.get("guides", []))
    return entries


def _safe_resolve(path_str: str) -> Path:
    """
    Resolve a relative path against REPO_ROOT with security checks.

    Raises ValueError for:
    - paths containing '..' components
    - paths that resolve outside REPO_ROOT
    - non-.md files
    """
    if ".." in Path(path_str).parts:
        raise ValueError(f"Path traversal not allowed: {path_str!r}")
    if not path_str.endswith(".md"):
        raise ValueError(f"Only .md files are readable: {path_str!r}")
    resolved = (REPO_ROOT / path_str).resolve()
    # Ensure the resolved path is inside the repo
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError:
        raise ValueError(f"Path outside repo root: {path_str!r}")
    return resolved


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


@mcp_server.tool()
def get_index() -> dict[str, Any]:
    """
    Return the full parsed meta/guide-index.yaml as a JSON object.

    Use this as the initial discovery step. Inspect the index to understand
    which guides exist before calling select_guides or get_guide.
    """
    return _load_index()


@mcp_server.tool()
def select_guides(
    task: str,
    model_family: str = "claude",
    tags: list[str] | None = None,
) -> dict[str, Any]:
    """
    Return a minimal list of guide paths suited to a task.

    core/shared-contract.md is always included. If model_family is set,
    development/model-adapters.md is always included.

    Args:
        task: Plain-language description of what you are about to do.
        model_family: One of 'claude', 'gpt', 'gemini', 'llama', 'mistral', 'grok',
            'reasoning'. Defaults to 'claude'.
        tags: Optional hint tags to narrow selection (e.g. ['debugging', 'scope']).

    Returns a JSON object with:
        selected      — ordered list of {path, reason} dicts
        excluded_count — number of entries that scored 0
    """
    if tags is None:
        tags = []

    index = _load_index()
    all_entries = _all_guides(index)

    task_tokens = set(task.lower().split())

    scored: list[tuple[int, dict[str, Any]]] = []
    for entry in all_entries:
        score = 0

        # +2 per matching tag
        entry_tags = entry.get("tags", [])
        for tag in tags:
            if tag.lower() in [t.lower() for t in entry_tags]:
                score += 2

        # +1 if any task token appears in summary or load_when strings
        summary = (entry.get("summary") or "").lower()
        load_when_items = entry.get("load_when") or []
        load_when_text = " ".join(load_when_items).lower()
        combined_text = summary + " " + load_when_text

        for token in task_tokens:
            if len(token) > 2 and token in combined_text:
                score += 1
                break  # count once per entry

        if score > 0:
            scored.append((score, entry))

    # Build the ordered result
    # 1. shared-contract always first
    # 2. model-adapters second if model_family is set
    # 3. task guides sorted descending by score

    shared_contract_path = "core/shared-contract.md"
    adapter_path = MODEL_ADAPTERS_PATH if model_family else None

    pinned_paths = {shared_contract_path}
    if adapter_path:
        pinned_paths.add(adapter_path)

    # Exclude pinned paths from scored results to avoid duplicates
    task_guides = [
        (score, entry)
        for score, entry in scored
        if entry.get("path") not in pinned_paths
    ]
    task_guides.sort(key=lambda t: t[0], reverse=True)

    selected: list[dict[str, str]] = []

    selected.append({"path": shared_contract_path, "reason": "always included"})

    if adapter_path:
        selected.append(
            {"path": adapter_path, "reason": f"model_family={model_family}"}
        )

    for score, entry in task_guides:
        path = entry.get("path", "")
        matching_tags = [
            t for t in (entry.get("tags") or []) if t.lower() in [x.lower() for x in tags]
        ]
        tag_str = f", tags={matching_tags}" if matching_tags else ""
        selected.append({"path": path, "reason": f"score={score}{tag_str}"})

    # Count entries that scored 0 (not in scored) and weren't pinned
    scored_paths = {entry.get("path") for _, entry in scored}
    excluded_count = sum(
        1
        for entry in all_entries
        if entry.get("path") not in scored_paths
        and entry.get("path") not in pinned_paths
    )

    return {"selected": selected, "excluded_count": excluded_count}


@mcp_server.tool()
def get_guide(path: str) -> str | dict[str, str]:
    """
    Return the raw markdown content of a guide file.

    Args:
        path: Relative path from the repo root, e.g. 'development/debugging.md'

    The path must be a .md file inside the rubric repo. Path traversal ('..') is rejected.
    Returns an error dict if the file does not exist.
    """
    try:
        resolved = _safe_resolve(path)
    except ValueError as exc:
        return {"error": str(exc)}

    if not resolved.exists():
        return {"error": f"Guide not found: {path}"}

    return resolved.read_text(encoding="utf-8")


@mcp_server.tool()
def get_shared_contract() -> str:
    """
    Return the content of core/shared-contract.md directly.

    Convenience shortcut — call this immediately after select_guides to get
    the always-on baseline rules without a separate path lookup.
    """
    return SHARED_CONTRACT_PATH.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp_server.run(transport="stdio")
