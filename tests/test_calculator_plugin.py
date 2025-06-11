 codex/convert-unittest-to-pytest
from sss.plugin_example import CalculatorPlugin


def test_addition():
    plugin = CalculatorPlugin()
    result = plugin.execute({'a': 5, 'b': 3})
    assert result == {'result': 8}

=======
import os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import unittest

from plugin_example import CalculatorPlugin


class TestCalculatorPlugin(unittest.TestCase):
    def test_addition(self):
        plugin = CalculatorPlugin()
        result = plugin.execute({"a": 5, "b": 3})
        self.assertEqual(result, {"result": 8})
 main
