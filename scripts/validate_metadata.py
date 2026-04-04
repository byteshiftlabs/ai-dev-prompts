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


def expected_markdown_files() -> list[Path]:
    folders = [
        ROOT / "core",
        ROOT / "development",
        ROOT / "setup",
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

    expected = {path.relative_to(ROOT).as_posix() for path in expected_markdown_files()}
    indexed = set(indexed_paths)
    missing_from_index = sorted(expected - indexed)
    if missing_from_index:
        errors.append(
            "Guide index is missing markdown files: " + ", ".join(missing_from_index)
        )

    files_requiring_frontmatter = [
        path for path in expected_markdown_files() if path.relative_to(ROOT).as_posix() != "README.md"
    ]
    missing_frontmatter = [
        path.relative_to(ROOT).as_posix() for path in files_requiring_frontmatter if not has_frontmatter(path)
    ]
    if missing_frontmatter:
        errors.append(
            "Files missing frontmatter: " + ", ".join(sorted(missing_frontmatter))
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