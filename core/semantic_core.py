def interpret(text):

    t = text.lower()

    result = {
        "intent": None,
        "target": None
    }

    # 🔴 INTENT ERKENNUNG
    if any(w in t for w in ["baue", "erstelle", "build"]):
        result["intent"] = "BUILD"

    elif any(w in t for w in ["fix", "repariere"]):
        result["intent"] = "FIX"

    # 🔴 ZIELSYSTEM
    if "ui" in t:
        result["target"] = "UI_SYSTEM"

    elif "state" in t:
        result["target"] = "STATE_SYSTEM"

    elif "scan" in t:
        result["target"] = "ADVANCED_SCAN_SYSTEM"

    return result
