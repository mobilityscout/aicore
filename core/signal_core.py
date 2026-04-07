def detect_type(raw):

    if isinstance(raw, dict):
        raw = raw.get("raw", "")

    raw_l = str(raw).lower()

    if "error" in raw_l:
        return "ERROR"

    if "ui" in raw_l:
        return "UI"

    if "api" in raw_l:
        return "API"

    return "UNKNOWN"


def normalize_signal(raw):

    if isinstance(raw, dict):

        return {
            "raw": raw.get("raw", ""),
            "type": raw.get("type") or detect_type(raw),
            "priority": raw.get("priority", "LOW"),
            "route": raw.get("route", None)
        }

    return {
        "raw": raw,
        "type": detect_type(raw),
        "priority": "LOW",
        "route": None
    }


def validate_signal(signal):

    if not signal.get("raw"):
        return False

    return True


def is_duplicate(signal):
    return False
