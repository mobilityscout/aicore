from core.module_registry import register

def integrate(module_name, path):

    print("\n=== INTEGRATION ===")

    register(module_name, path)

    print("INTEGRATED:", module_name)

    return True
