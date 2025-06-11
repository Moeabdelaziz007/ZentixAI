"""Example plugin that registers the CalculatorPlugin from plugin_example."""
from .. import plugin_example


def register() -> None:
    plugin_example.register()
