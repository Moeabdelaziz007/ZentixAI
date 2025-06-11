"""Compatibility package exposing core modules under the 'sss' namespace."""

 codex/convert-unittest-to-pytest
import importlib
import sys

sys.modules[__name__ + ".zero_system"] = importlib.import_module("zero_system")
sys.modules[__name__ + ".plugin_example"] = importlib.import_module("plugin_example")
=======
from importlib import import_module

zero_system = import_module("zero_system")
plugin_example = import_module("plugin_example")

__all__ = [
    "zero_system",
    "plugin_example",
]
 main
