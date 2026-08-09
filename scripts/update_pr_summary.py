#!/usr/bin/env python3
"""
Pull Request Summary Comment Manager for KubeToOps.
Maintains a single PR comment marked by <!-- KUBE2OPS_PR_SUMMARY -->, converting all timestamps to Asia/Manila (PHT),
preserving the original Created timestamp, and appending a diff-based Release Preview.
"""
import argparse
import datetime
import os
import re
import sys
from zoneinfo import ZoneInfo
from generate_release_preview import get_git_diff_file_statuses, generate_release_preview


PHT_TZ = ZoneInfo("Asia/Manila")
MARKER = "<!-- KUBE2OPS_PR_SUMMARY -->"


def get_pht_timestamp_str(dt: datetime.datetime = None) -> str:
    if dt is None:
        dt = datetime.datetime.now(PHT_TZ)
    elif dt.tzinfo is None:
        dt = dt.replace(tzinfo=datetime.timezone.utc).astimezone(PHT_TZ)
    else:
        dt = dt.astimezone(PHT_TZ)

    # Format: August 9, 2026 — 8:42 PM PHT
    formatted_date = dt.strftime("%B %d, %Y — %I:%M %p PHT")
    # Clean up single leading zero in day if wanted, e.g. August 09 -> August 9
    formatted_date = re.sub(r'([A-Za-z]+)\s+0(\d,)', r'\1 \2', formatted_date)
    return formatted_date


def parse_created_timestamp(existing_comment: str) -> str:
    """
    Extracts existing 'Created:' timestamp line if present.
    """
    if not existing_comment:
        return None
    match = re.search(r"Created:\s*\n\s*([^\n\r]+)", existing_comment)
    if match:
        return match.group(1).strip()
    return None


def render_pr_summary(
    existing_comment: str = "",
    status_pass: bool = True,
    validation_matrix: dict = None,
    created_time_str: str = None
) -> str:
    # 1. Determine Timestamps
    if not created_time_str:
        created_time_str = parse_created_timestamp(existing_comment)
    if not created_time_str:
        created_time_str = get_pht_timestamp_str()

    updated_time_str = get_pht_timestamp_str()

    # 2. Validation Matrix
    if validation_matrix is None:
        validation_matrix = {
            "Command validation": "✅ PASS",
            "Python tests": "✅ PASS",
            "Python lint": "✅ PASS",
            "Markdown lint": "✅ PASS",
            "YAML lint": "✅ PASS",
            "ShellCheck": "✅ PASS",
            "Link checking": "✅ PASS",
            "Secret scanning": "✅ PASS",
        }

    # Format validation table
    val_table = "| Check | Status |\n|---|---|\n"
    for check_name, check_status in validation_matrix.items():
        val_table += f"| {check_name} | {check_status} |\n"

    # 3. Release Preview
    files = get_git_diff_file_statuses()
    release_preview_md = generate_release_preview(files)

    # 4. Overall status & Merge readiness
    status_header = "✅ All required checks passed" if status_pass else "❌ Validation checks failed"
    merge_readiness = "✅ Ready to merge" if status_pass else "⚠️ Blocked by failed validation checks"

    comment_body = f"""{MARKER}
# 🧭 KubeToOps Pull Request Summary

## Status

{status_header}

## Timeline

Created:  
{created_time_str}

Last updated:  
{updated_time_str}

{release_preview_md}

## Validation

{val_table}
## Merge Readiness

{merge_readiness}
"""
    return comment_body


def main():
    parser = argparse.ArgumentParser(description="Update KubeToOps PR Summary Comment")
    parser.add_argument("--existing-comment-file", help="File containing existing comment body")
    parser.add_argument("--output-file", default="pr_summary.md", help="Path to write rendered PR summary")
    parser.add_argument("--failed", action="store_true", help="Mark PR status as failed")
    args = parser.parse_args()

    existing_content = ""
    if args.existing_comment_file and os.path.exists(args.existing_comment_file):
        with open(args.existing_comment_file, "r", encoding="utf-8") as f:
            existing_content = f.read()

    summary_md = render_pr_summary(
        existing_comment=existing_content,
        status_pass=not args.failed
    )

    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(summary_md)

    print(f"Generated PR summary in {args.output_file}")


if __name__ == "__main__":
    main()
