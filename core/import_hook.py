import builtins

_original_import = builtins.__import__

BLOCKED = {"nt", "msvcrt", "_winapi", "_wmi"}


def custom_import(name, globals=None, locals=None, fromlist=(), level=0):

    if name in BLOCKED:
        raise ModuleNotFoundError(name)

    if name.startswith("tenants.ai"):
        return _original_import(name, globals, locals, fromlist, level)

    try:
        return _original_import(name, globals, locals, fromlist, level)

    except ModuleNotFoundError:
        from core.dynamic_import import load
        return load(name)


def install():
    builtins.__import__ = custom_import
