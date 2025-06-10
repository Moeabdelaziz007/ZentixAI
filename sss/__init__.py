"""Compatibility package exposing core modules under the 'sss' namespace."""

import importlib, sys

sys.modules[__name__ + ".zero_system"] = importlib.import_module('amrikyyai.zero_system')
sys.modules[__name__ + ".plugin_example"] = importlib.import_module('amrikyyai.plugin_example')
