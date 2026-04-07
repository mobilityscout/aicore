from core.sandbox import create, copy_system
from core.repair_validator import validate


def evolve(tenant, system, builder):

    print("\n=== EVOLUTION ENGINE ===")

    # 🔴 1. SANDBOX
    sandbox = create()
    systems_path = copy_system(tenant, sandbox)

    print("SANDBOX:", sandbox)

    # 🔴 2. BUILD IN SANDBOX
    try:
        builder(systems_path)
    except Exception as e:
        print("SANDBOX BUILD FAIL:", e)
        return False

    # 🔴 3. VALIDATION
    ok = validate("BUILD", tenant)

    print("SANDBOX VALIDATION:", ok)

    return ok, sandbox
