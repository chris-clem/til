# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a "Today I Learned" (TIL) repository for storing personal learning snippets and technical discoveries. Inspired by Simon Willison's TIL format.

## Repository Structure

- **Topic-based organization**: TILs are organized into directories by topic (e.g., `raycast/`, `git/`, `python/`)
- **Markdown format**: Each TIL is a standalone markdown file with a descriptive filename
- **Supporting assets**: Images and other assets are stored in subdirectories alongside the TIL (e.g., `raycast/rcsb-quicklink-pngs/`)
- **README.md**: Contains a chronological index of all TILs with dates and links

## Adding New TILs

When creating a new TIL entry:

1. **Create the directory** if it doesn't exist for the topic (e.g., `mkdir docker/`)
2. **Write the TIL** as a markdown file with a descriptive name (e.g., `docker/compose-networking.md`)
3. **Add images** in a subdirectory if needed (e.g., `docker/compose-networking-pngs/`)
4. **Update README.md**: Add an entry to the `## TILs` section following the format:
   ```markdown
   - YYYY-MM-DD: [Title](./topic/filename.md)
   ```
   Keep entries in reverse chronological order (newest first)

## TIL Writing Style

Based on the existing entry:
- Start with a clear, descriptive H1 title
- Use numbered steps for procedures
- Include screenshots/images inline where they add value
- Reference external resources with links
- Keep it concise and practical
- Focus on "how to" rather than theory
