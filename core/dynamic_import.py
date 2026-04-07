import importlib

def load(name):
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError as e:
        print("IMPORT FAIL:", name)
        raise e
