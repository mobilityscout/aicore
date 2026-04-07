from core.write_system import write
from core.integration_engine import integrate


def build(module_name):

    print("\n=== AUTO MODULE BUILD ===")

    # 🔴 Pfad berechnen
    path = module_name.replace(".", "/")
    file_path = f"/opt/aicore/{path}.py"

    # 🔴 Minimaler funktionaler Code
    content = f"""
# AUTO-GENERATED MODULE: {module_name}

def run(*args, **kwargs):
    print("AUTO MODULE EXECUTED: {module_name}")
    return True
"""

    # 🔴 Schreiben
    write(file_path, content)

    # 🔴 Integration
    integrate(module_name.split(".")[-1], module_name)

    print("MODULE BUILT:", module_name)

    return True
