import importlib.util

def validate(path, func):

    try:
        spec = importlib.util.spec_from_file_location("mod", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        getattr(mod, func)()
        return True

    except Exception as e:
        print("VALIDATION FAIL:", e)
        return False
