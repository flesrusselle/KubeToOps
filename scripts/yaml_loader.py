"""
Lightweight YAML loader helper for KubeToOps.
Tries PyYAML (`import yaml`) first; if missing, provides a pure-Python fallback parser for catalog YAML files.
"""
import re


def load_yaml(filepath_or_stream):
    content = ""
    if hasattr(filepath_or_stream, "read"):
        content = filepath_or_stream.read()
    elif isinstance(filepath_or_stream, str):
        if "\n" in filepath_or_stream or filepath_or_stream.endswith(".yaml"):
            try:
                with open(filepath_or_stream, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                content = filepath_or_stream
        else:
            content = filepath_or_stream

    try:
        import yaml
        return yaml.safe_load(content)
    except ModuleNotFoundError:
        return _pure_python_yaml_parse(content)


def _pure_python_yaml_parse(content: str):
    """
    Pure Python parser for list-of-dicts YAML structure used in KubeToOps catalogs.
    """
    lines = content.splitlines()
    items = []
    current_item = None
    current_list_key = None
    current_sub_item = None

    for raw_line in lines:
        # Strip comments
        line_no_comment = raw_line.split(" #")[0]
        if not line_no_comment.strip() or line_no_comment.strip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = line_no_comment.strip()

        # Top-level item start `- id: "..."`
        if stripped.startswith("- "):
            if current_item is not None:
                if current_sub_item is not None and current_list_key:
                    current_item[current_list_key].append(current_sub_item)
                    current_sub_item = None
                items.append(current_item)

            current_item = {}
            current_list_key = None
            current_sub_item = None

            content_after_dash = stripped[2:].strip()
            if ":" in content_after_dash:
                k, v = content_after_dash.split(":", 1)
                current_item[k.strip()] = _parse_val(v.strip())
            continue

        if current_item is None:
            continue

        # Nested list item inside current_item (e.g., breakdown or tags)
        if indent >= 4 and stripped.startswith("- "):
            item_str = stripped[2:].strip()
            if ":" in item_str:
                if current_sub_item is not None and current_list_key:
                    current_item[current_list_key].append(current_sub_item)
                current_sub_item = {}
                k, v = item_str.split(":", 1)
                current_sub_item[k.strip()] = _parse_val(v.strip())
            else:
                if current_list_key and isinstance(current_item.get(current_list_key), list):
                    current_item[current_list_key].append(_parse_val(item_str))
            continue

        # Key-value pair inside current item or sub-item
        if ":" in stripped:
            k, v = stripped.split(":", 1)
            key = k.strip()
            val_str = v.strip()

            if indent >= 6 and current_sub_item is not None:
                current_sub_item[key] = _parse_val(val_str)
            elif indent >= 2:
                if not val_str:
                    # Indicates start of a nested list or dict
                    current_list_key = key
                    current_item[key] = []
                else:
                    current_item[key] = _parse_val(val_str)

    if current_sub_item is not None and current_list_key and current_item:
        current_item[current_list_key].append(current_sub_item)

    if current_item is not None:
        items.append(current_item)

    return items


def _parse_val(val_str: str):
    if not val_str:
        return ""
    if (val_str.startswith('"') and val_str.endswith('"')) or (val_str.startswith("'") and val_str.endswith("'")):
        return val_str[1:-1]
    if val_str.lower() == "true":
        return True
    if val_str.lower() == "false":
        return False
    return val_str
