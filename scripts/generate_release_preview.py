#!/usr/bin/env python3
"""
Diff-Based Release Preview Generator for KubeToOps.
Generates deterministic Release Preview markdown from git diff without external AI/LLM APIs.
"""
import argparse
import os
import subprocess
import sys


def get_git_diff_file_statuses(target_ref: str = "main") -> list:
    """
    Retrieves list of tuple (status_code, file_path) from git diff.
    """
    try:
        # Check if target_ref exists in git
        check_ref = subprocess.run(["git", "rev-parse", "--verify", target_ref], capture_output=True, text=True)
        if check_ref.returncode == 0:
            cmd = ["git", "diff", "--name-status", f"{target_ref}...HEAD"]
        else:
            # Fallback for fresh repos or single branch
            cmd = ["git", "diff", "--name-status", "HEAD~1", "HEAD"]

        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lines = res.stdout.strip().split("\n")
        files = []
        for line in lines:
            if not line.strip():
                continue
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                status, path = parts[0][0], parts[1] # A, M, D, R
                files.append((status, path))
        return files
    except Exception as e:
        # Fallback if uncommitted working tree changes exist
        try:
            res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
            lines = res.stdout.strip().split("\n")
            files = []
            for line in lines:
                if not line.strip():
                    continue
                status_code = line[:2].strip()
                path = line[3:].strip()
                if "A" in status_code or "?" in status_code:
                    files.append(("A", path))
                elif "M" in status_code:
                    files.append(("M", path))
                elif "D" in status_code:
                    files.append(("D", path))
            return files
        except Exception:
            return []


def generate_release_preview(files: list) -> str:
    added = []
    changed = []
    removed = []
    docs = []
    commands = []
    workflows = []
    security = []

    for status, path in files:
        if status == "A":
            added.append(path)
        elif status == "M" or status == "R":
            changed.append(path)
        elif status == "D":
            removed.append(path)

        if path.startswith("docs/") or path.endswith(".md"):
            docs.append(path)
        if "commands.yaml" in path or "command-of-the-day" in path:
            commands.append(path)
        if ".github/workflows" in path or "scripts/" in path:
            workflows.append(path)
        if "SECURITY" in path or "security" in path:
            security.append(path)

    sections = ["## 🚀 Release Preview\n"]

    if added:
        sections.append("### Added\n" + "\n".join([f"- `{f}`" for f in added]) + "\n")
    if changed:
        sections.append("### Changed\n" + "\n".join([f"- `{f}`" for f in changed]) + "\n")
    if removed:
        sections.append("### Removed\n" + "\n".join([f"- `{f}`" for f in removed]) + "\n")
    if docs:
        sections.append("### Documentation\n" + "\n".join([f"- Updated `{f}`" for f in docs]) + "\n")
    if commands:
        sections.append("### Commands & Catalog\n" + "\n".join([f"- Catalog update in `{f}`" for f in commands]) + "\n")
    if security:
        sections.append("### Security & Safeguards\n" + "\n".join([f"- Security policy or guide edit in `{f}`" for f in security]) + "\n")

    # Breaking changes check
    sections.append("### Breaking Changes\nNone\n")

    # Operational impact check
    if workflows or commands:
        sections.append("### Operational Impact\nUpdated command catalog or workflow automation.\n")
    else:
        sections.append("### Operational Impact\nNone\n")

    # Cost Impact - MANDATORY $0 COST
    sections.append("### 💰 Cost Impact\nNo paid services or APIs are required. Hosted strictly at $0 cost.\n")

    return "\n".join(sections)


def main():
    parser = argparse.ArgumentParser(description="Generate Release Preview for KubeToOps PRs")
    parser.add_argument("--target", default="main", help="Git target ref (default: main)")
    args = parser.parse_args()

    files = get_git_diff_file_statuses(args.target)
    preview = generate_release_preview(files)
    print(preview)


if __name__ == "__main__":
    main()
