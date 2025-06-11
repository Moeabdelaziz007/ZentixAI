class Plugin:
    """Base class for all plugins."""

    def execute(self, inputs: dict) -> dict:
        raise NotImplementedError


class PluginRegistry:
    """Registry to keep track of available plugins."""

    _plugins = {}

    @classmethod
    def register(cls, name: str, plugin: "Plugin") -> None:
        cls._plugins[name] = plugin

    @classmethod
    def get(cls, name: str) -> "Plugin | None":
        return cls._plugins.get(name)


import math


class CalculatorPlugin(Plugin):
    """Simple plugin that adds two numbers with basic validation."""

    def execute(self, inputs: dict) -> dict:
        a = inputs.get("a")
        b = inputs.get("b")
        if a is None or b is None:
            raise ValueError("CalculatorPlugin requires 'a' and 'b'.")

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numeric.")

        result = a + b

        if isinstance(result, float) and math.isinf(result):
            raise OverflowError("Result is infinite")
        if isinstance(result, float) and math.isnan(result):
            raise ValueError("Result is NaN")

        return {"result": result}


class Agent:
    """Agent that invokes registered plugins by name."""

    def execute_plugin(self, name: str, inputs: dict) -> dict:
        plugin = PluginRegistry.get(name)
        if not plugin:
            raise ValueError(f"No plugin named '{name}' registered.")
        return plugin.execute(inputs)


if __name__ == "__main__":
    # Register the calculator plugin
    PluginRegistry.register("calculator", CalculatorPlugin())

    agent = Agent()
    output = agent.execute_plugin("calculator", {"a": 5, "b": 3})
    print(output)  # {'result': 8}
