def validate(system, tenant):

    try:
        if system == "UI_SYSTEM":

            path = f"/opt/aicore/tenants/{tenant}/systems/ui_system.py"

            with open(path, "r") as f:
                content = f.read()

            if "<html" in content.lower():
                return True

        return False

    except:
        return False
