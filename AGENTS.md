# Repository Guidelines

## Project Structure & Module Organization
Each topic lives in its own directory (`gcp/`, `skypilot/`, `python/`, `raycast/`, `windsurf/`, `datamol/`, `ghostty/`, etc.), and every TIL is a single Markdown file named with a short, dash-separated slug (for example, `gcp/manage-gcp-buckets.md`). The top-level `README.md` is the canonical index and is updated automatically from new TILs. Utility code and scripts belong at the repo root; the only current example is `update_readme.py`, which owns README maintenance logic and assumes the working directory is the repository root.

## Build, Test, and Development Commands
- `uv run update_readme.py` — scans untracked/modified directories, grabs the first H1 in each Markdown file, and appends a dated link to `README.md`.
- `pre-commit run --all-files` — executes the configured hook suite (syntax validation, trailing whitespace cleanup, Ruff lint/format) so that Markdown and Python snippets stay consistent before committing.
- `ruff check .` / `ruff format .` — run these directly when iterating on Python helpers; both tools are already pinned by the pre-commit config.

## Coding Style & Naming Conventions
Author Markdown in UTF-8 with Unix newlines and a single `# Title` heading at line 1. Keep entries succinct, prefer fenced code blocks for commands, and link to upstream docs when useful. Directory and file names should reflect the product or tooling area plus the action learned (`skypilot/useful-skypilot-commands.md`). Python helpers follow Ruff defaults: 4-space indentation, type hints, and descriptive snake_case identifiers. Let Ruff auto-format (`ruff format`) instead of manual spacing tweaks.

## Testing Guidelines
This repository does not ship runtime tests, but contributors should manually validate two behaviors: (1) `uv run update_readme.py` picks up the new TIL and adds the correct relative path, and (2) `pre-commit run --all-files` succeeds so that Markdown structure and Python scripts remain lint-clean. When adding automation, colocate lightweight unit tests beside the script (`tests/` sibling) and keep names aligned with the module under test (e.g., `tests/test_update_readme.py`).

## Commit & Pull Request Guidelines
Git history favors concise, imperative subjects (“Add Useful Datamol functions”). Follow that pattern, limit to ~72 characters, and include multi-line bodies only when context is required. Each pull request should describe the new TIL(s), note any script updates, and optionally link to references or screenshots that motivated the note. Highlight verification steps (commands above) so reviewers can reproduce the outcome quickly.

## Security & Configuration Notes
Never commit credentials or API outputs; `detect-private-key` in pre-commit will block obvious leaks, but manual review is still required. If a TIL references internal resources, sanitize hostnames or IDs before publishing. Keep the `requires-python` header in scripts aligned with the toolchain—in this repo we target Python 3.11 via `uv`.
