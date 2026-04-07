def classify_signal(raw):

    raw_l = str(raw).lower()

    if "error" in raw_l:
        return "error"

    if "ui" in raw_l:
        return "ui"

    if "api" in raw_l:
        return "api"

    return "unknown"


def risk_level(raw):

    raw_l = str(raw).lower()

    if "rm -rf" in raw_l or "delete" in raw_l:
        return "CRITICAL"

    if "error" in raw_l:
        return "HIGH"

    return "LOW"


def route(signal_type):

    if signal_type == "error":
        return "FIX"

    if signal_type == "ui":
        return "BUILD_UI"

    if signal_type == "api":
        return "BUILD_API"

    return "IGNORE"


def process(raw_signal):

    print("\n=== GLOBAL GUARD ===")

    s_type = classify_signal(raw_signal)
    risk = risk_level(raw_signal)
    action = route(s_type)

    print("TYPE:", s_type)
    print("RISK:", risk)
    print("ROUTE:", action)

    return {
        "raw": raw_signal,
        "type": s_type,
        "risk": risk,
        "route": action
    }


def verify(result):

    print("\n=== GUARD VERIFY ===")

    if result:
        print("VERIFY: SUCCESS")
        return True

    print("VERIFY: FAILED → BLOCK")
    return False
