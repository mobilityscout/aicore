def decide(signal, _):

    raw = signal.get("raw", "").lower()

    # 🔴 STRUKTUR DENKEN

    if "missing state" in raw:
        return "BUILD_STRUCTURE:STATE_SYSTEM", 0.95, "HIGH"

    if "ui" in raw:
        return "BUILD_STRUCTURE:UI_SYSTEM", 0.9, "HIGH"

    if "error" in raw:
        return "SELF_HEAL", 0.7, "MEDIUM"

    return "IGNORE", 0.3, "LOW"
