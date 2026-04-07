from core.signal_core import normalize_signal, validate_signal
from core.iam_core import decide
from core.action_mapper import map_action


def safe_import(name):

    try:
        module = __import__(name, fromlist=["run"])
        return module.run
    except Exception as e:
        print("IMPORT FAILED:", name, "|", e)
        return None


def run(signal):

    print("\n=== SIGNAL RECEIVED ===")

    signal = normalize_signal(signal)

    if not validate_signal(signal):
        print("INVALID SIGNAL")
        return

    decision, score, priority = decide(signal, False)

    print("IAM:", decision, "| SCORE:", score)

    action = map_action(signal, decision)

    if not action:
        print("NO ACTION")
        return

    engine = action.get("engine")

    # 🔴 STRUCTURE SYSTEM
    if engine == "STRUCTURE":

        structure_run = safe_import("core.structure_manager")

        if not structure_run:
            print("STRUCTURE MANAGER MISSING → SIGNAL")
            return

        result = structure_run(signal)

        if result:
            print("STRUCTURE SUCCESS")
        else:
            print("STRUCTURE FAILED")

        return

    # 🔴 HEALTH SYSTEM
    if engine == "HEALTH":

        health_run = safe_import("core.health_manager")

        if not health_run:
            print("HEALTH MANAGER MISSING")
            return

        result = health_run(signal)

        print("HEALTH RESULT:", result)
        return
