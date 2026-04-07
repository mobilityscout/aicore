import os
from core.tenant_registry import list_tenants
from core.structure_manager import build_state, build_ui

BASE = "/opt/aicore/tenants"


def enforce():

    print("\n=== GLOBAL STRUCTURE ENFORCEMENT ===")

    tenants = list_tenants()

    results = {}

    for t in tenants:

        path = os.path.join(BASE, t)

        results[t] = {
            "state": False,
            "ui": False
        }

        # 🔴 STATE prüfen
        if not os.path.exists(path + "/state"):
            print(t, "→ BUILD STATE")
            os.makedirs(path + "/state", exist_ok=True)
            build_state()
            results[t]["state"] = True
        else:
            results[t]["state"] = True

        # 🔴 UI prüfen
        if not os.path.exists(path + "/ui"):
            print(t, "→ BUILD UI")
            os.makedirs(path + "/ui", exist_ok=True)
            build_ui()
            results[t]["ui"] = True
        else:
            results[t]["ui"] = True

    return results
