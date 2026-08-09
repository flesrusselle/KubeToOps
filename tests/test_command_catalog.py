"""
Unit tests for KubeToOps Command and Tool Catalog schema validation.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))
from validate_commands import validate_commands, validate_tools


class TestCommandCatalog(unittest.TestCase):
    def test_validate_commands_catalog(self):
        commands_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../content/commands.yaml"))
        errors = validate_commands(commands_path)
        self.assertEqual(errors, [], f"Commands catalog validation failed with errors: {errors}")

    def test_validate_tools_catalog(self):
        tools_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../content/tools.yaml"))
        errors = validate_tools(tools_path)
        self.assertEqual(errors, [], f"Tools catalog validation failed with errors: {errors}")


if __name__ == "__main__":
    unittest.main()
