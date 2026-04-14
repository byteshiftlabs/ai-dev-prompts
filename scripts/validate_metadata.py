#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "meta" / "asset-manifest.yaml"
GUIDE_INDEX = ROOT / "meta" / "guide-index.yaml"


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def extract_list_values(lines: list[str], key: str) -> list[str]:
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
    lines = read_lines(path)
    return len(lines) >= 3 and lines[0] == "---" and "---" in lines[1:15]


def markdown_lines_without_fences(path: Path) -> list[str]:
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
    if "#" in target:
        return target.split("#", 1)[0]
    return target


def find_missing_internal_links(path: Path) -> list[str]:
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
    folders = [
        ROOT / "core",
        ROOT / "development",
        ROOT / "setup",
        ROOT / "meta",
        ROOT / ".github" / "prompts",
        ROOT / ".github" / "agents",
    ]
    files = [ROOT / "README.md"]
    for folder in folders:
        files.extend(sorted(folder.glob("*.md")))
    return sorted(files)


def main() -> int:
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