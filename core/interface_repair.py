from core.error_parser import parse
from core.auto_module_builder import build as build_module


def repair(error):

    print("\n=== INTERFACE REPAIR ===")

    info = parse(error)

    print("PARSED:", info)

    # 🔴 FALL 1: fehlendes Modul
    if info["type"] == "MISSING_MODULE":

        module = info["module"]

        return build_module(module)

    # 🔴 FALL 2: fehlende Funktion
    if info["type"] == "MISSING_FUNCTION":

        func = info["function"]
        module = info["module"]

        path = f"/opt/aicore/core/{module}.py"

        wrapper = f"""

# AUTO-GENERATED FUNCTION FIX
def {func}(*args, **kwargs):
    print("AUTO-FIXED FUNCTION: {func}")
    return True
"""

        with open(path, "a") as f:
            f.write(wrapper)

        print("FUNCTION FIXED:", func)

        return True

    return False
