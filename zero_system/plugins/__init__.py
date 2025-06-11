from __future__ import annotations

from importlib.util import spec_from_file_location, module_from_spec
from types import ModuleType
from pathlib import Path
from typing import List


def load_plugins(path: Path) -> List[ModuleType]:
    """Dynamically load all plugin modules in *path*.

    Each module must define a ``register`` function which will be called
    after the module is imported. Loaded modules are returned as a list.
    """
    modules: List[ModuleType] = []
    if not path.exists():
        return modules
    for file in path.glob("*.py"):
        if file.name == "__init__.py":
            continue
        spec = spec_from_file_location(file.stem, file)
        if spec and spec.loader:
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "register"):
                module.register()
            modules.append(module)
    return modules
