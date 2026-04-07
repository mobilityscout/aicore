def unify(signal):

    # 🔴 garantiert einheitliches Format

    return {
        "raw": signal.get("raw", ""),
        "type": signal.get("type", "UNKNOWN"),
        "priority": signal.get("priority", "LOW"),
        "route": signal.get("route", None),
        "context": {},
        "history": []
    }


def enrich(signal):

    raw = signal["raw"].lower()

    # 🔴 einfache "Abteilungen"

    signal["context"]["security"] = "safe" if "hack" not in raw else "risk"

    signal["context"]["domain"] = (
        "ui" if "ui" in raw else
        "api" if "api" in raw else
        "system"
    )

    signal["context"]["complexity"] = len(raw)

    return signal
