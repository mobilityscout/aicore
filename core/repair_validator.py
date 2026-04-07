def validate(action, tenant):

    # 🔴 einfache Basis (erweiterbar)
    try:
        if action == "BUILD":

            path = f"/opt/aicore/tenants/{tenant}/systems/ui_system.py"

            with open(path, "r") as f:
                content = f.read()

            if "def run" in content:
                return True

        return False

    except:
        return False
