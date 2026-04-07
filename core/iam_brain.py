import os

CORE = "/opt/aicore/core"

def module_exists(name):
    return os.path.exists(f"{CORE}/{name}.py")

def score_decision(context):

    score = 0.0

    if context.get("signal"):
        if all(v == 200 for v in context["signal"].values()):
            score += 0.2
        else:
            score += 0.5

    if context.get("module"):
        if module_exists(context["module"]):
            score += 0.2
        else:
            score += 0.4

    if context.get("type") == "known_error":
        score += 0.3

    return min(score, 1.0)

def priority(context):

    if context.get("signal"):
        if any(v == 500 for v in context["signal"].values()):
            return "CRITICAL"

        if any(v == 404 for v in context["signal"].values()):
            return "HIGH"

    return "LOW"

def decide(context):

    print("\n=== IAM BRAIN ===")

    s = score_decision(context)
    p = priority(context)

    print("SCORE:", s)
    print("PRIORITY:", p)

    signal = context.get("signal")
    module = context.get("module")

    # ------------------------
    # STABLE
    # ------------------------
    if signal and all(v == 200 for v in signal.values()):
        return {
            "decision": "IGNORE",
            "score": s,
            "priority": p
        }

    # ------------------------
    # MODULE CHECK
    # ------------------------
    if module:
        if not module_exists(module):
            return {
                "decision": "INSTALL",
                "module": module,
                "score": s,
                "priority": p
            }

        return {
            "decision": "FIX_USAGE",
            "module": module,
            "score": s,
            "priority": p
        }

    # ------------------------
    # DEFAULT
    # ------------------------
    return {
        "decision": "RESEARCH",
        "score": s,
        "priority": p
    }
