import importlib
from core.module_registry import get

def load(name):

    path = get(name)

    if not path:
        raise Exception(f"MODULE NOT REGISTERED: {name}")

    module = importlib.import_module(path)

    print("LOADED:", name)

    return module
