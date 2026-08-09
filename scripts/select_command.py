#!/usr/bin/env python3
"""
Deterministic Command Selection Engine for KubeToOps Command of the Day.
"""
import argparse
import datetime
import hashlib
import json
import os
import sys
import yaml


def load_commands(catalog_path: str) -> list:
    if not os.path.exists(catalog_path):
        raise FileNotFoundError(f"Command catalog not found at {catalog_path}")
    with open(catalog_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Command catalog must be a non-empty list.")
    return data


def load_history(history_path: str) -> list:
    if not os.path.exists(history_path):
        return []
    try:
        with open(history_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def select_command(catalog: list, history: list, date_str: str, target_id: str = None) -> dict:
    # 1. If explicit command_id requested, find and return it
    if target_id:
        for cmd in catalog:
            if cmd.get("id") == target_id:
                return cmd
        raise ValueError(f"Requested command ID '{target_id}' not found in catalog.")

    # 2. Get recent command IDs from history (last 30 entries)
    recent_ids = {entry.get("id") for entry in history[-30:] if isinstance(entry, dict) and "id" in entry}

    # 3. Filter eligible commands not in recent history
    eligible = [cmd for cmd in catalog if cmd.get("id") not in recent_ids]
    if not eligible:
        # If all commands have been used recently, fallback to entire catalog
        eligible = catalog

    # 4. Deterministic selection based on date string hash
    hash_digest = hashlib.sha256(date_str.encode("utf-8")).hexdigest()
    hash_int = int(hash_digest, 16)
    index = hash_int % len(eligible)

    return eligible[index]


def main():
    parser = argparse.ArgumentParser(description="Select Command of the Day for KubeToOps")
    parser.add_argument("--catalog", default="content/commands.yaml", help="Path to commands.yaml")
    parser.add_argument("--history", default="command-of-the-day/history.json", help="Path to history.json")
    parser.add_argument("--date", default=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"), help="Date string YYYY-MM-DD")
    parser.add_argument("--command-id", default=None, help="Explicit command ID to select")
    args = parser.parse_args()

    try:
        catalog = load_commands(args.catalog)
        history = load_history(args.history)
        selected = select_command(catalog, history, args.date, args.command_id)
        print(json.dumps(selected, indent=2))
    except Exception as e:
        print(f"Error selecting command: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
