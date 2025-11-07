# /// script
# requires-python = "==3.11.*"
# dependencies = [
#   "loguru",
# ]
# ///

"""Update README with latest TILs.

Usage:
uv run update_readme.py
"""

import subprocess
from datetime import datetime
from pathlib import Path

from loguru import logger

REPO_ROOT_DIR = Path(__file__).parent


def get_uncommitted_md_files() -> list[Path]:
    """Get list of uncommitted markdown files."""
    logger.info("Checking for uncommitted markdown files")

    result = subprocess.run(
        ["git", "status", "--porcelain"], capture_output=True, text=True, check=True
    )

    uncommitted_files = []
    for line in result.stdout.splitlines():
        # Parse git status output: ?? or M or A at the start
        if line.startswith(("??", " M", "M ", "A ")):
            is_dir_name = line.endswith("/")
            # Find md file in dir
            if is_dir_name:
                dir_name = line[3:-1].strip()
                md_file_paths = sorted((REPO_ROOT_DIR / dir_name).glob("*.md"))
                uncommitted_files.extend(md_file_paths)
            else:
                logger.warning(f"Uncommitted file is not in a directory: {line}")

    logger.debug(f"Found {len(uncommitted_files)} uncommitted markdown file(s)")
    return uncommitted_files


def extract_heading(filepath: Path) -> str | None:
    """Extract the first H1 heading from a markdown file."""
    logger.debug("Extracting heading")

    heading_line = filepath.read_text(encoding="utf-8").splitlines()[0]

    if not heading_line.startswith("# "):
        logger.warning("No H1 heading found")
        return None

    heading = heading_line[2:].strip()
    logger.debug(f"Extracted heading: {heading}")

    return heading


def add_til_to_readme(filepath: Path, heading: str):
    """Add TIL entry to README.md."""
    logger.debug("Adding TIL to README")

    readme_path = Path("README.md")
    readme_content = readme_path.read_text(encoding="utf-8")

    # Create the new entry
    today = datetime.now().strftime("%Y-%m-%d")
    relative_path = f"./{filepath.relative_to(REPO_ROOT_DIR)}"
    new_entry = f"- {today}: [{heading}]({relative_path})\n"

    # Add to end of readme and save
    readme_content += new_entry
    readme_path.write_text(readme_content, encoding="utf-8")


def main():
    logger.info("Updating README with latest TILs")

    # Check for uncommitted md files
    uncommitted_files = get_uncommitted_md_files()

    if not uncommitted_files:
        logger.info("No uncommitted markdown files found")
        return

    # For each uncommitted file, check their heading
    for filepath in uncommitted_files:
        heading = extract_heading(filepath)
        if heading:
            add_til_to_readme(filepath, heading)

    logger.success("README update complete")


if __name__ == "__main__":
    main()
