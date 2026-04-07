import os

CORE_PATH = "/opt/aicore/core"

def module_exists(name):
    return os.path.exists(f"{CORE_PATH}/{name}.py")

def decide(context):

    print("\n=== IAM DECISION ENGINE ===")

    error_type = context.get("type")
    module = context.get("module")
    signal = context.get("signal")

    # ------------------------
    # STABLE SYSTEM
    # ------------------------
    if signal and all(v == 200 for v in signal.values()):
        print("SYSTEM STABLE")
        return {
            "decision": "IGNORE",
            "reason": "no action required"
        }

    # ------------------------
    # MODULE CHECK
    # ------------------------
    if module:

        exists = module_exists(module)

        if not exists:
            print("MODULE NOT FOUND")
            return {
                "decision": "INSTALL",
                "module": module,
                "reason": "module missing"
            }

        # exists but error → usage problem
        print("MODULE EXISTS → USAGE ERROR")
        return {
            "decision": "FIX_USAGE",
            "module": module,
            "reason": "wrong execution context"
        }

    # ------------------------
    # UNKNOWN CASE
    # ------------------------
    print("UNKNOWN → RESEARCH")
    return {
        "decision": "RESEARCH",
        "reason": "no known pattern"
    }
