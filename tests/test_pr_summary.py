"""
Unit tests for KubeToOps PR Summary Generator & Timestamp Preservation (PHT).
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))
from update_pr_summary import render_pr_summary, parse_created_timestamp, MARKER


class TestPRSummary(unittest.TestCase):
    def test_pr_summary_contains_marker(self):
        summary = render_pr_summary()
        self.assertIn(MARKER, summary)
        self.assertIn("PHT", summary)
        self.assertIn("## Status", summary)
        self.assertIn("## Timeline", summary)
        self.assertIn("## Validation", summary)

    def test_parse_and_preserve_created_timestamp(self):
        original_created_time = "August 9, 2026 — 8:42 PM PHT"
        old_comment = f"""{MARKER}
# 🧭 KubeToOps Pull Request Summary

## Timeline

Created:  
{original_created_time}

Last updated:  
August 9, 2026 — 8:42 PM PHT
"""

        parsed_time = parse_created_timestamp(old_comment)
        self.assertEqual(parsed_time, original_created_time)

        # Generate new summary passing old comment
        new_summary = render_pr_summary(existing_comment=old_comment)

        # Check that Created time is preserved exactly
        self.assertIn(f"Created:  \n{original_created_time}", new_summary)


if __name__ == "__main__":
    unittest.main()
