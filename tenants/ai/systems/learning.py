from tenants.ai.systems.memory import load

CONFIDENCE_THRESHOLD = 0.9


def find_pattern(signal, tenant):

    data = load()

    for entry in reversed(data.get("history", [])):

        # 🔴 KEIN CROSS TENANT LEARNING
        if entry.get("tenant") != tenant:
            continue

        if entry.get("signal") == signal and entry.get("confidence", 0) >= CONFIDENCE_THRESHOLD:
            return entry.get("decision")

    return None
