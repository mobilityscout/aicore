import os
import json
import time

BASE = "/opt/aicore"

# =========================
# 🔴 REAL SYSTEM SCAN
# =========================

def scan_system():

    signals = []

    # 🔴 Struktur prüfen
    if not os.path.exists(BASE + "/state"):
        signals.append("missing: state system")

    if not os.path.exists(BASE + "/ui"):
        signals.append("missing: ui system")

    # 🔴 Dateien prüfen
    for root, dirs, files in os.walk(BASE):
        for f in files:

            if f.endswith(".log"):
                path = os.path.join(root, f)

                try:
                    with open(path) as fh:
                        content = fh.read().lower()

                        if "error" in content:
                            signals.append("error detected in logs")

                except:
                    pass

    return list(set(signals))


# =========================
# 🔴 IAM (STRUCTURE THINKING)
# =========================

def decide(signal):

    s = signal.lower()

    if "state" in s:
        return {"type": "BUILD_STRUCTURE", "target": "STATE_SYSTEM"}

    if "ui" in s:
        return {"type": "BUILD_STRUCTURE", "target": "UI_SYSTEM"}

    if "error" in s:
        return {"type": "SELF_HEAL"}

    return {"type": "IGNORE"}


# =========================
# 🔴 STRUCTURE MANAGEMENT
# =========================

def build_state():

    os.makedirs(BASE + "/state", exist_ok=True)

    with open(BASE + "/state/state.json", "w") as f:
        json.dump({"status": "ok"}, f)

    with open(BASE + "/state/api.py", "w") as f:
        f.write("def get_state():\n    return {'status': 'ok'}\n")

    return True


def build_ui():

    os.makedirs(BASE + "/ui", exist_ok=True)

    with open(BASE + "/ui/dashboard.py", "w") as f:
        f.write("def dashboard():\n    return 'ok'\n")

    return True


def structure_manager(action):

    target = action.get("target")

    if target == "STATE_SYSTEM":
        print("BUILD FULL STATE SYSTEM")
        return build_state()

    if target == "UI_SYSTEM":
        print("BUILD FULL UI SYSTEM")
        return build_ui()

    return False


# =========================
# 🔴 HEALTH / SELF HEAL
# =========================

def self_heal():

    print("SELF HEAL → scanning baseline")

    # hier später baseline + repair logic
    return True


# =========================
# 🔴 EXECUTION
# =========================

def execute(action):

    t = action.get("type")

    if t == "BUILD_STRUCTURE":
        return structure_manager(action)

    if t == "SELF_HEAL":
        return self_heal()

    return False


# =========================
# 🔴 MAIN LOOP (AUTONOM)
# =========================

def run():

    print("\n=== AUTONOMOUS SYSTEM START ===")

    while True:

        signals = scan_system()

        if not signals:
            print("SYSTEM STABLE")
            time.sleep(5)
            continue

        for s in signals:

            print("\nSIGNAL →", s)

            action = decide(s)

            print("ACTION →", action)

            result = execute(action)

            if result:
                print("RESULT → SUCCESS")
            else:
                print("RESULT → FAILED")

        time.sleep(5)
