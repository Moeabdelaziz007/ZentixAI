"""Example plugin using ZeroSystem plugin registry."""
from typing import Optional
from zero_system.plugins.registry import Plugin, PluginRegistry


class CalculatorPlugin(Plugin):
    """Simple plugin that adds two numbers."""

    def execute(self, inputs: dict) -> dict:
        a = inputs.get("a")
        b = inputs.get("b")
        if a is None or b is None:
            raise ValueError("CalculatorPlugin requires 'a' and 'b'.")
        return {"result": a + b}


# Register plugin on import
PluginRegistry.register("calculator", CalculatorPlugin())


class Agent:
    """Agent that invokes registered plugins by name."""

    def execute_plugin(self, name: str, inputs: dict) -> dict:
        plugin = PluginRegistry.get(name)
        if not plugin:
            raise ValueError(f"No plugin named '{name}' registered.")
        return plugin.execute(inputs)


if __name__ == "__main__":
    agent = Agent()
    print(agent.execute_plugin("calculator", {"a": 5, "b": 3}))
