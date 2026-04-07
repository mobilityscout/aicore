import os
import importlib.util
from core.tenant_registry import list_tenants

BASE = "/opt/aicore/tenants"


def check_python_file(path, func):

    try:
        spec = importlib.util.spec_from_file_location("mod", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        if hasattr(mod, func):
            getattr(mod, func)()
            return True

    except Exception as e:
        print("EXEC FAIL:", path, e)

    return False


def run():

    print("\n=== REAL SYSTEM TEST ===")

    tenants = list_tenants()

    total_checks = 0
    success = 0

    details = []

    for t in tenants:

        path = os.path.join(BASE, t)

        state_ok = False
        ui_ok = False

        # 🔴 STATE prüfen (funktional)
        state_file = path + "/state/api.py"

        if os.path.exists(state_file):
            if check_python_file(state_file, "get_state"):
                state_ok = True

        # 🔴 UI prüfen (funktional)
        ui_file = path + "/ui/dashboard.py"

        if os.path.exists(ui_file):
            if check_python_file(ui_file, "dashboard"):
                ui_ok = True

        total_checks += 2

        if state_ok:
            success += 1

        if ui_ok:
            success += 1

        details.append({
            "tenant": t,
            "state_exec": state_ok,
            "ui_exec": ui_ok
        })

    score = (success / total_checks) if total_checks > 0 else 1

    print("\nREAL PERFORMANCE:", round(score * 100, 2), "%")

    for d in details:
        print(d)

    return {
        "score": score,
        "details": details
    }
