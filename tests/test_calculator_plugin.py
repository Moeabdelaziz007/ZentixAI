import os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import unittest

from sss.plugin_example import CalculatorPlugin


class TestCalculatorPlugin(unittest.TestCase):
    def test_addition(self):
        plugin = CalculatorPlugin()
        result = plugin.execute({"a": 5, "b": 3})
        self.assertEqual(result, {"result": 8})
