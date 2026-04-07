from core.snapshot import create, restore
from core.repair_validator import validate


def repair(action, tenant, executor):

    print("\n=== REPAIR ENGINE ===")

    target = f"/opt/aicore/tenants/{tenant}"

    # 🔴 1. SNAPSHOT
    snap = create(target)

    # 🔴 2. APPLY REPAIR
    try:
        executor()
    except Exception as e:
        print("REPAIR FAILED:", e)
        restore(snap, target)
        return False

    # 🔴 3. VALIDATION
    ok = validate(action, tenant)
    print("VALIDATION:", ok)

    if not ok:
        restore(snap, target)
        return False

    print("REPAIR SUCCESS")
    return True
