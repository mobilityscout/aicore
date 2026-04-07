def generate(system, state):

    print("\n=== GENERATE BLUEPRINT:", system, "===")

    files = {}

    # 🔴 STATE SYSTEM
    if system == "STATE_SYSTEM":

        files["state/api.py"] = (
            "def get_state():\n"
            "    return {'status': 'ok'}\n"
        )

        files["state/model.json"] = '{"status":"ok"}'

    # 🔴 UI SYSTEM
    elif system == "UI_SYSTEM":

        files["ui/dashboard.py"] = (
            "def dashboard():\n"
            "    return 'dashboard ready'\n"
        )

    # 🔴 FALLBACK GENERATOR
    else:

        files[f"{system.lower()}/main.py"] = (
            "def run():\n"
            "    return 'auto-generated'\n"
        )

    return {
        "system": system,
        "files": files
    }
