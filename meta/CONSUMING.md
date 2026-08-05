---
pack: task-workflows
summary: Packaging-oriented entrypoint that explains how to use README.md with the metadata files under meta/.
tags: [entrypoint, routing, packaging, metadata]
---

# Consuming This Repo

This repository is meant to be loaded in small pieces.

Do not treat it like one giant prompt.

Use these files first:
- [asset-manifest.yaml](asset-manifest.yaml)
- [guide-index.yaml](guide-index.yaml)
- [../README.md](../README.md)

For tools and packaging flows, the practical entry point is `README.md` plus the `meta/` folder.

## Simple Consumer Flow

1. Read [../README.md](../README.md).
2. Decide the task type.
3. Use [guide-index.yaml](guide-index.yaml) to find the smallest relevant guides.
4. Use [asset-manifest.yaml](asset-manifest.yaml) to keep related files together when exporting or packaging.
5. Load only the selected files.

## Example

If the task is "debug a regression in a Python service":

1. Start with README.md to identify the task type.
2. Load the shared rules from the `core-rules` pack.
3. Load [../development/debugging.md](../development/debugging.md).
4. Load [../development/context-management.md](../development/context-management.md) only if memory or large context matters.
5. Do not load unrelated guides such as release audit or ML bootstrap.

That means the consumer should end up with a small bundle, not the entire repository.

## Example For Skill Seekers Or Similar Tools

If you are turning this repo into packaged AI context:

1. Index all files so they are searchable.
2. Preserve the pack names from [asset-manifest.yaml](asset-manifest.yaml).
3. Preserve the per-file summaries and tags from [guide-index.yaml](guide-index.yaml).
4. Retrieve by task and pack.
5. Package only the selected files into the final skill, rules file, or context payload.

Good:
- `core/shared-contract.md` + `development/debugging.md`

Bad:
- every guide in one default bundle

## Recommended Rule

Route first.
Package second.
Load last.