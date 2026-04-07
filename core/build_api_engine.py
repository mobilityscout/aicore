import os

API_FILE = "/opt/aicore/bin/live_ui.py"

TEMPLATE_API = """
@app.route("/api/status")
def api_status():
    return {"api": "ok"}
"""

def run(action, signal):

    print("BUILD_API → APPLY")

    if not os.path.exists(API_FILE):
        return False

    with open(API_FILE, "r") as f:
        code = f.read()

    if "/api/status" in code:
        print("API EXISTS → SKIP")
        return True

    with open(API_FILE, "a") as f:
        f.write("\n" + TEMPLATE_API + "\n")

    print("API ENDPOINT ADDED")
    return True
