#!/usr/bin/env bash
set -euo pipefail

echo "=================================================="
echo "   KubeToOps Master Repository Validation"
echo "=================================================="

FAILED=0

echo -n "1. Validating Command Catalog... "
if python3 scripts/validate_commands.py content/commands.yaml content/tools.yaml > /dev/null 2>&1; then
    echo "✅ PASS"
else
    echo "❌ FAIL"
    FAILED=1
fi

echo -n "2. Running Python Unit Tests... "
if command -v pytest &>/dev/null; then
    if pytest tests/ > /dev/null 2>&1; then
        echo "✅ PASS (pytest)"
    else
        echo "❌ FAIL (pytest)"
        FAILED=1
    fi
elif python3 -m unittest discover -s tests > /dev/null 2>&1; then
    echo "✅ PASS (unittest)"
else
    echo "❌ FAIL (unittest)"
    FAILED=1
fi

if command -v yamllint &>/dev/null; then
    echo -n "3. Running yamllint... "
    if yamllint content/*.yaml .github/**/*.yml > /dev/null 2>&1; then
        echo "✅ PASS"
    else
        echo "❌ FAIL"
        FAILED=1
    fi
else
    echo "3. Running yamllint... ⚠️ SKIPPED (yamllint not installed)"
fi

if command -v shellcheck &>/dev/null; then
    echo -n "4. Running ShellCheck... "
    if shellcheck scripts/*.sh > /dev/null 2>&1; then
        echo "✅ PASS"
    else
        echo "❌ FAIL"
        FAILED=1
    fi
else
    echo "4. Running ShellCheck... ⚠️ SKIPPED (shellcheck not installed)"
fi

echo "=================================================="
if [ $FAILED -eq 0 ]; then
    echo "✅ All local validation checks PASSED cleanly."
    exit 0
else
    echo "❌ Validation errors detected."
    exit 1
fi
