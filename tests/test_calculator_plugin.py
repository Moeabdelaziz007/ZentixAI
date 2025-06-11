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
