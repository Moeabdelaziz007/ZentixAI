from importlib import import_module
from typing import Optional, Type
import math
from decimal import Decimal


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
    def get(cls, name: str) -> Optional["Plugin"]:
        return cls._plugins.get(name)

    @classmethod
    def clear(cls) -> None:
        cls._plugins.clear()


def load_plugins(*module_names: str) -> None:
    """Dynamically import modules and register all ``Plugin`` subclasses."""
    for module_name in module_names:
        module = import_module(module_name)
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if (
                isinstance(attr, type)
                and issubclass(attr, Plugin)
                and attr is not Plugin
            ):
                PluginRegistry.register(attr_name.lower(), attr())


class CalculatorPlugin(Plugin):
    """Simple plugin that adds two numbers with basic validation."""

    def execute(self, inputs: dict) -> dict:
        a = inputs.get("a")
        b = inputs.get("b")
        if a is None or b is None:
            raise ValueError("CalculatorPlugin requires 'a' and 'b'.")

        numeric_types = (int, float, Decimal)
        if not isinstance(a, numeric_types) or not isinstance(b, numeric_types):
            raise TypeError("CalculatorPlugin inputs must be numeric.")

        def check_finite(value, name):
            if isinstance(value, float):
                if math.isinf(value):
                    raise OverflowError(f"Input {name} is infinite.")
                if math.isnan(value):
                    raise ValueError(f"Input {name} is NaN.")
            elif isinstance(value, Decimal):
                if value.is_infinite():
                    raise OverflowError(f"Input {name} is infinite.")
                if value.is_nan():
                    raise ValueError(f"Input {name} is NaN.")

        check_finite(a, "a")
        check_finite(b, "b")

        if inputs.get("high_precision"):
            a = Decimal(str(a))
            b = Decimal(str(b))

        return {"result": a + b}


class Agent:
    """Agent that invokes registered plugins by name."""

    def execute_plugin(self, name: str, inputs: dict) -> dict:
        plugin = PluginRegistry.get(name)
        if not plugin:
            raise ValueError(f"No plugin named '{name}' registered.")
        return plugin.execute(inputs)


if __name__ == "__main__":
    PluginRegistry.register("calculator", CalculatorPlugin())
    agent = Agent()
    output = agent.execute_plugin("calculator", {"a": 5, "b": 3})
    print(output)
