from zero_system import PluginRegistry
from plugin_example import CalculatorPlugin


def test_calculator_plugin():
    plugin = PluginRegistry.get("calculator")
    assert plugin is not None
    result = plugin.execute({"a": 2, "b": 3})
    assert result == {"result": 5}
