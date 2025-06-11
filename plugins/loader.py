import importlib
import pkgutil


def load_plugins(skills: dict) -> None:
    """Discover modules in the ``plugins`` package and call their ``register``.

    Each plugin module should expose a ``register(skills)`` function that
    receives the skills dictionary and registers its skill instances.
    """
    package = importlib.import_module("plugins")

    for finder, name, ispkg in pkgutil.iter_modules(package.__path__):
        if name == "loader":
            continue
        module = importlib.import_module(f"plugins.{name}")
        register = getattr(module, "register", None)
        if callable(register):
            register(skills)
