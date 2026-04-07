from core.decision_scoring import score_decision


def decide(signal, known):

    fragments = signal.get("fragments", [])

    # 🔴 RULE BUILD TRIGGER
    if signal.get("rule_needed"):
        return "BUILD_RULE", 0.9, "HIGH"

    base_decision = "RESEARCH"

    if signal["type"] == "BOOT":
        base_decision = "INITIALIZE"

    elif known:
        base_decision = "FIX_USAGE"

    elif fragments:
        top = fragments[0]
        if top.get("confidence", 0) >= 0.8:
            base_decision = top.get("decision", "RESEARCH")

    elif signal["type"].startswith("error"):
        if signal["type"] == "error_syntax": return "FIX_CODE", 0.9, "HIGH"
    if signal["type"] == "error_import": return "FIX_CODE", 0.9, "HIGH"
    base_decision = "FIX"

    score, priority = score_decision(signal, base_decision)

    return base_decision, score, priority
