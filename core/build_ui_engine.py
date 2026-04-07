import os

UI_FILE = "/opt/aicore/bin/live_ui.py"

TEMPLATE_ROUTE = """
@app.route("/ui/dashboard")
def ui_dashboard():
    return {
        "dashboard": "active",
        "components": ["index", "tenants", "state", "iam"]
    }
"""

def run(action, signal):

    print("BUILD_UI → APPLY")

    if not os.path.exists(UI_FILE):
        print("UI FILE MISSING → FAIL")
        return False

    with open(UI_FILE, "r") as f:
        code = f.read()

    if "/ui/dashboard" in code:
        print("UI DASHBOARD EXISTS → SKIP")
        return True

    # 🔴 sichere Erweiterung am Ende
    with open(UI_FILE, "a") as f:
        f.write("\n" + TEMPLATE_ROUTE + "\n")

    print("UI DASHBOARD ADDED")
    return True
