"""
Unit tests for KubeToOps Diff-Based Release Preview Engine.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))
from generate_release_preview import generate_release_preview


class TestReleasePreview(unittest.TestCase):
    def test_generate_release_preview_categories(self):
        sample_files = [
            ("A", "docs/troubleshooting/crashloopbackoff.md"),
            ("M", "content/commands.yaml"),
            ("A", "scripts/generate_release_preview.py"),
            ("M", "SECURITY.md")
        ]

        preview = generate_release_preview(sample_files)

        self.assertIn("## 🚀 Release Preview", preview)
        self.assertIn("### Added", preview)
        self.assertIn("`docs/troubleshooting/crashloopbackoff.md`", preview)
        self.assertIn("### Changed", preview)
        self.assertIn("`content/commands.yaml`", preview)
        self.assertIn("### Documentation", preview)
        self.assertIn("### Security & Safeguards", preview)
        self.assertIn("### 💰 Cost Impact", preview)
        self.assertIn("No paid services or APIs are required", preview)

    def test_generate_release_preview_empty_sections(self):
        # Only changed file, no additions or removals
        sample_files = [("M", "README.md")]
        preview = generate_release_preview(sample_files)

        self.assertIn("### Changed", preview)
        self.assertNotIn("### Removed", preview)  # Should not display empty Removed section!


if __name__ == "__main__":
    unittest.main()
