#!/usr/bin/env python3
"""
Command & Tool Catalog Validator for KubeToOps.
Ensures content/commands.yaml and content/tools.yaml strictly comply with project schemas.
"""
import os
import sys
import urllib.parse
import yaml

VALID_CATEGORIES = {
    "kubectl", "productivity", "contexts", "namespaces", "aliases",
    "plugins", "tools", "troubleshooting", "debugging", "yaml",
    "networking", "workloads", "security", "resource-utilization", "advanced"
}

VALID_DIFFICULTIES = {"beginner", "intermediate", "advanced"}
VALID_SAFETY = {"safe", "caution", "destructive"}
VALID_TEST_ENVS = {"safe-read", "safe-local", "requires-cluster", "destructive", "interactive"}


def is_valid_url(url: str) -> bool:
    if not isinstance(url, str) or not (url.startswith("http://") or url.startswith("https://")):
        return False
    parsed = urllib.parse.urlparse(url)
    return bool(parsed.netloc and parsed.scheme)


def validate_commands(commands_path: str) -> list:
    errors = []
    if not os.path.exists(commands_path):
        return [f"Commands catalog path '{commands_path}' does not exist."]

    try:
        with open(commands_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return [f"YAML syntax error in {commands_path}: {e}"]

    if not isinstance(data, list):
        return [f"Root structure of {commands_path} must be a list of commands."]

    seen_ids = set()
    for idx, cmd in enumerate(data):
        prefix = f"Command[{idx}]"
        if not isinstance(cmd, dict):
            errors.append(f"{prefix}: Item must be a dictionary.")
            continue

        cmd_id = cmd.get("id")
        if not cmd_id:
            errors.append(f"{prefix}: Missing required field 'id'.")
        else:
            if cmd_id in seen_ids:
                errors.append(f"{prefix}: Duplicate command ID '{cmd_id}'.")
            seen_ids.add(cmd_id)

        # Required fields check
        required_fields = ["title", "category", "difficulty", "command", "description", "why", "safety", "official_docs"]
        for field in required_fields:
            if not cmd.get(field):
                errors.append(f"{prefix} (ID: {cmd_id}): Missing required field '{field}'.")

        # Enum validations
        if cmd.get("category") and cmd["category"] not in VALID_CATEGORIES:
            errors.append(f"{prefix} (ID: {cmd_id}): Invalid category '{cmd['category']}'. Must be one of {VALID_CATEGORIES}")

        if cmd.get("difficulty") and cmd["difficulty"] not in VALID_DIFFICULTIES:
            errors.append(f"{prefix} (ID: {cmd_id}): Invalid difficulty '{cmd['difficulty']}'. Must be one of {VALID_DIFFICULTIES}")

        if cmd.get("safety") and cmd["safety"] not in VALID_SAFETY:
            errors.append(f"{prefix} (ID: {cmd_id}): Invalid safety '{cmd['safety']}'. Must be one of {VALID_SAFETY}")

        if cmd.get("test_environment") and cmd["test_environment"] not in VALID_TEST_ENVS:
            errors.append(f"{prefix} (ID: {cmd_id}): Invalid test_environment '{cmd['test_environment']}'. Must be one of {VALID_TEST_ENVS}")

        # URL validation
        if cmd.get("official_docs") and not is_valid_url(cmd["official_docs"]):
            errors.append(f"{prefix} (ID: {cmd_id}): Invalid official_docs URL '{cmd['official_docs']}'.")

    return errors


def validate_tools(tools_path: str) -> list:
    errors = []
    if not os.path.exists(tools_path):
        return [f"Tools catalog path '{tools_path}' does not exist."]

    try:
        with open(tools_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return [f"YAML syntax error in {tools_path}: {e}"]

    if not isinstance(data, list):
        return [f"Root structure of {tools_path} must be a list of tools."]

    seen_ids = set()
    for idx, tool in enumerate(data):
        prefix = f"Tool[{idx}]"
        if not isinstance(tool, dict):
            errors.append(f"{prefix}: Item must be a dictionary.")
            continue

        tool_id = tool.get("id")
        if not tool_id:
            errors.append(f"{prefix}: Missing required field 'id'.")
        else:
            if tool_id in seen_ids:
                errors.append(f"{prefix}: Duplicate tool ID '{tool_id}'.")
            seen_ids.add(tool_id)

        required_fields = ["name", "tagline", "category", "description", "why", "installation", "official_docs"]
        for field in required_fields:
            if not tool.get(field):
                errors.append(f"{prefix} (ID: {tool_id}): Missing required field '{field}'.")

        if tool.get("official_docs") and not is_valid_url(tool["official_docs"]):
            errors.append(f"{prefix} (ID: {tool_id}): Invalid official_docs URL '{tool['official_docs']}'.")

    return errors


def main():
    commands_path = sys.argv[1] if len(sys.argv) > 1 else "content/commands.yaml"
    tools_path = sys.argv[2] if len(sys.argv) > 2 else "content/tools.yaml"

    cmd_errors = validate_commands(commands_path)
    tool_errors = validate_tools(tools_path)

    all_errors = cmd_errors + tool_errors

    if all_errors:
        print("❌ Catalog Validation Failed:", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"✅ Catalog Validation Passed ({commands_path}, {tools_path})")


if __name__ == "__main__":
    main()
