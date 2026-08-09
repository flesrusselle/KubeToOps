#!/usr/bin/env bash
set -euo pipefail

echo "=================================================="
echo "  KubeToOps Environment Prerequisite Check"
echo "=================================================="

# Function to check binary existence
check_tool() {
    local tool_name="$1"
    local required="$2"

    if command -v "$tool_name" &>/dev/null; then
        local version_info
        version_info=$("$tool_name" --version 2>&1 | head -n 1 || echo "installed")
        echo -e "  [✔] $tool_name: $version_info"
    else
        if [ "$required" = "true" ]; then
            echo -e "  [✘] MISSING (REQUIRED): $tool_name"
        else
            echo -e "  [!] MISSING (OPTIONAL): $tool_name"
        fi
    fi
}

echo "Required Tools:"
check_tool "git" "true"
check_tool "python3" "true"

echo ""
echo "Recommended K8s Tools:"
check_tool "kubectl" "false"
check_tool "kubectx" "false"
check_tool "kubens" "false"
check_tool "k9s" "false"
check_tool "gh" "false"

echo ""
echo "Development & Linting Tools:"
check_tool "shellcheck" "false"
check_tool "yamllint" "false"

echo "=================================================="
echo "Check completed."
