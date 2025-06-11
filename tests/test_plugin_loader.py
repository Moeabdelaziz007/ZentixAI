import importlib
import sys
from types import ModuleType

from plugin_example import PluginRegistry, load_plugins, Plugin


def test_load_plugins_registers_modules(tmp_path, monkeypatch):
    module_path = tmp_path / "my_plugin.py"
    module_path.write_text(
        """
from plugin_example import Plugin
class Custom(Plugin):
    def execute(self, inputs):
        return {"ok": True}
""",
        encoding="utf-8",
    )
    sys.path.insert(0, str(tmp_path))
    try:
        load_plugins("my_plugin")
        plugin = PluginRegistry.get("custom")
        assert plugin is not None
        assert plugin.execute({}) == {"ok": True}
    finally:
        sys.path.remove(str(tmp_path))
        PluginRegistry.clear()
