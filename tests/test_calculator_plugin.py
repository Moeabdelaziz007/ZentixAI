 codex/add-unit-tests-and-update-readme
import unittest
from plugin_example import CalculatorPlugin, PluginRegistry, Agent

class TestCalculatorPlugin(unittest.TestCase):
    def setUp(self):
        PluginRegistry._plugins.clear()
        PluginRegistry.register("calculator", CalculatorPlugin())
        self.agent = Agent()

    def test_addition(self):
        result = self.agent.execute_plugin("calculator", {"a": 5, "b": 3})
        self.assertEqual(result, {"result": 8})

if __name__ == "__main__":
    unittest.main()
=======
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
 main
