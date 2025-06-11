"""Simple plugin registry for external skills."""
import importlib.util
import os
from typing import Optional, Dict


class Plugin:
    """Base class for external skills."""

    def execute(self, inputs: dict) -> dict:
        raise NotImplementedError


class PluginRegistry:
    _plugins: Dict[str, Plugin] = {}

    @classmethod
    def register(cls, name: str, plugin: Plugin) -> None:
        cls._plugins[name] = plugin

    @classmethod
    def get(cls, name: str) -> Optional[Plugin]:
        return cls._plugins.get(name)

    @classmethod
    def load_plugins(cls, directory: str) -> None:
        if not os.path.isdir(directory):
            return
        for fname in os.listdir(directory):
            if not fname.endswith(".py") or fname.startswith("_"):
                continue
            path = os.path.join(directory, fname)
            spec = importlib.util.spec_from_file_location(fname[:-3], path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                # Modules can call PluginRegistry.register during import
                # No further action needed
