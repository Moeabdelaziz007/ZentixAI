import importlib, sys

sys.modules[__name__ + ".zero_system"] = importlib.import_module('zero_system')
sys.modules[__name__ + ".plugin_example"] = importlib.import_module('plugin_example')
