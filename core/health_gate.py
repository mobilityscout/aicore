def classify(signal):

    content = signal.get("content", "").lower()

    # 🔴 einfache Sicherheitsregeln (erweiterbar)

    if "rm -rf" in content:
        return "THREAT"

    if "exec(" in content:
        return "ANOMALY"

    if signal.get("type") == "unknown":
        return "UNKNOWN"

    return "OK"
