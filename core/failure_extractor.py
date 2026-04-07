def extract(test_result):

    signals = []

    for d in test_result.get("details", []):

        if not d.get("state_exec"):
            signals.append("missing: state system")

        if not d.get("ui_exec"):
            signals.append("missing: ui system")

    return list(set(signals))
