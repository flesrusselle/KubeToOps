"""
Unit tests for KubeToOps Diff-Based Release Preview Engine.
"""
import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))
from generate_release_preview import generate_release_preview


def test_generate_release_preview_categories():
    sample_files = [
        ("A", "docs/troubleshooting/crashloopbackoff.md"),
        ("M", "content/commands.yaml"),
        ("A", "scripts/generate_release_preview.py"),
        ("M", "SECURITY.md")
    ]

    preview = generate_release_preview(sample_files)

    assert "## 🚀 Release Preview" in preview
    assert "### Added" in preview
    assert "`docs/troubleshooting/crashloopbackoff.md`" in preview
    assert "### Changed" in preview
    assert "`content/commands.yaml`" in preview
    assert "### Documentation" in preview
    assert "### Security & Safeguards" in preview
    assert "### 💰 Cost Impact" in preview
    assert "No paid services or APIs are required" in preview


def test_generate_release_preview_empty_sections():
    # Only changed file, no additions or removals
    sample_files = [("M", "README.md")]
    preview = generate_release_preview(sample_files)

    assert "### Changed" in preview
    assert "### Removed" not in preview  # Should not display empty Removed section!
