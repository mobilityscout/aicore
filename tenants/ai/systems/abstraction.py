def abstract(entry):

    signal = entry.get("signal", "").lower()

    # 🔴 einfache Musterbildung (später erweiterbar)
    if "ui" in signal:
        return {
            "pattern": "UI_BUILD",
            "action": "BUILD"
        }

    if "error" in signal:
        return {
            "pattern": "ERROR_FIX",
            "action": "FIX"
        }

    return None
