#!/usr/bin/env python3
"""Checks that rubric's YAML catalogue still matches the files on disk.

The MCP server answers from meta/guide-index.yaml and meta/asset-manifest.yaml
rather than by scanning folders, so the catalogue is what consumers actually
see. Nothing stops it drifting from reality: move a guide and the catalogue
points at a dead path, add one and it stays invisible. Both fail silently.

Run by .github/workflows/validate-metadata.yml on every push and PR. Fails if:
  1. the catalogue references a file that does not exist
  2. a markdown guide exists but is not in the catalogue
  3. a guide is missing its YAML frontmatter
  4. a markdown file links to something that is not there

Deliberately parses the YAML by hand, line by line, so the check has no
third-party dependencies and CI needs nothing installed.
"""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "meta" / "asset-manifest.yaml"
GUIDE_INDEX = ROOT / "meta" / "guide-index.yaml"


def read_lines(path: Path) -> list[str]:
    """Read a text file and return its lines, newlines stripped."""
    return path.read_text(encoding="utf-8").splitlines()


def extract_list_values(lines: list[str], key: str) -> list[str]:
    """Pull every value for a given YAML key out of raw lines.

    Matches both "key: value" and "- key: value", so it catches the field
    whether it sits on its own or opens a list item. Used to collect every
    `path:` in the guide index.
    """
    values: list[str] = []
    prefix = f"{key}: "
    list_prefix = f"- {key}: "
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(prefix):
            values.append(stripped[len(prefix):].strip())
        elif stripped.startswith(list_prefix):
            values.append(stripped[len(list_prefix):].strip())
    return values


def extract_manifest_files(lines: list[str]) -> list[str]:
    """Collect every path listed under a `files:` block in the manifest.

    Tracks indentation to know where each block ends: a line indented deeper
    than the `files:` key is one of its entries, and the first line at or
    above that indent closes the block.
    """
    files: list[str] = []
    in_files_block = False
    file_indent = None

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))

        if stripped == "files:":
            in_files_block = True
            file_indent = indent
            continue

        if in_files_block:
            if stripped.startswith("- ") and indent > (file_indent or 0):
                files.append(stripped[2:].strip())
                continue
            if stripped and indent <= (file_indent or 0):
                in_files_block = False

    return files


def has_frontmatter(path: Path) -> bool:
    """True if the file opens with a YAML frontmatter block.

    Wants "---" on line 1 and a closing "---" within the next 15 lines.
    """
    lines = read_lines(path)
    return len(lines) >= 3 and lines[0] == "---" and "---" in lines[1:15]


def markdown_lines_without_fences(path: Path) -> list[str]:
    """Return the file's lines with fenced code blocks removed.

    Stops the link checker flagging example links inside ``` blocks, which
    are illustrations rather than real references.
    """
    lines: list[str] = []
    in_fence = False

    for line in read_lines(path):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        lines.append(line)

    return lines


def extract_markdown_link_targets(line: str) -> list[str]:
    """Return the targets of every [text](target) link on one line.

    Walks the string by hand instead of using a regex, and skips a "[...]"
    not followed by "(" so reference-style brackets are ignored.
    """
    targets: list[str] = []
    index = 0

    while True:
        open_bracket = line.find("[", index)
        if open_bracket == -1:
            return targets

        close_bracket = line.find("]", open_bracket + 1)
        if close_bracket == -1:
            return targets

        if close_bracket + 1 >= len(line) or line[close_bracket + 1] != "(":
            index = close_bracket + 1
            continue

        close_paren = line.find(")", close_bracket + 2)
        if close_paren == -1:
            return targets

        target = line[close_bracket + 2:close_paren].strip()
        if target:
            targets.append(target)

        index = close_paren + 1


def normalize_markdown_target(target: str) -> str:
    """Strip any #anchor, leaving just the file path.

    "guide.md#setup" becomes "guide.md" — the anchor is not checked, only
    that the file it points into exists.
    """
    if "#" in target:
        return target.split("#", 1)[0]
    return target


def find_missing_internal_links(path: Path) -> list[str]:
    """Return this file's links that point at something missing.

    Ignores external URLs, mailto:, absolute paths and bare anchors. Also
    reports links that resolve outside the repo, which usually means one
    too many "../".
    """
    missing: list[str] = []
    source = path.relative_to(ROOT).as_posix()

    for line in markdown_lines_without_fences(path):
        for raw_target in extract_markdown_link_targets(line):
            if "://" in raw_target or raw_target.startswith(("mailto:", "/", "#")):
                continue

            target = normalize_markdown_target(raw_target)
            if not target:
                continue

            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                missing.append(f"{source} -> {target} (outside repo)")
                continue

            if not resolved.exists():
                missing.append(f"{source} -> {target}")

    return missing


def expected_markdown_files() -> list[Path]:
    """List every markdown file that must appear in the guide index.

    The README plus all .md files in the content folders. Add a folder here
    when its guides should be catalogued.
    """
    folders = [
        ROOT / "core",
        ROOT / "development",
        ROOT / "setup",
        ROOT / "meta",
        ROOT / ".github" / "prompts",
    ]
    files = [ROOT / "README.md"]
    for folder in folders:
        files.extend(sorted(folder.glob("*.md")))
    return sorted(files)


def main() -> int:
    """Run all four checks and report. Returns 0 if clean, 1 if not.

    Collects every problem before printing, so one run shows the full list
    rather than stopping at the first failure.
    """
    errors: list[str] = []

    if not MANIFEST.exists():
        errors.append(f"Missing manifest: {MANIFEST}")
    if not GUIDE_INDEX.exists():
        errors.append(f"Missing guide index: {GUIDE_INDEX}")
    if errors:
        print("\n".join(errors))
        return 1

    manifest_lines = read_lines(MANIFEST)
    index_lines = read_lines(GUIDE_INDEX)

    manifest_files = extract_manifest_files(manifest_lines)
    indexed_paths = extract_list_values(index_lines, "path")

    for rel_path in manifest_files:
        if not (ROOT / rel_path).exists():
            errors.append(f"Manifest references missing file: {rel_path}")

    for rel_path in indexed_paths:
        if not (ROOT / rel_path).exists():
            errors.append(f"Guide index references missing file: {rel_path}")

    expected_files = expected_markdown_files()
    expected = {path.relative_to(ROOT).as_posix() for path in expected_files}
    indexed = set(indexed_paths)
    missing_from_index = sorted(expected - indexed)
    if missing_from_index:
        errors.append(
            "Guide index is missing markdown files: " + ", ".join(missing_from_index)
        )

    files_requiring_frontmatter = [
        path for path in expected_files if path.relative_to(ROOT).as_posix() != "README.md"
    ]
    missing_frontmatter = [
        path.relative_to(ROOT).as_posix() for path in files_requiring_frontmatter if not has_frontmatter(path)
    ]
    if missing_frontmatter:
        errors.append(
            "Files missing frontmatter: " + ", ".join(sorted(missing_frontmatter))
        )

    missing_links: list[str] = []
    for path in expected_files:
        missing_links.extend(find_missing_internal_links(path))
    if missing_links:
        errors.append(
            "Markdown files contain broken internal links: " + ", ".join(sorted(missing_links))
        )

    if errors:
        print("Metadata validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Metadata validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())