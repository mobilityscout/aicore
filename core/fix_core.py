def run(signal):

    actions = []

    # Beispiel: fehlende endpoints
    if signal.get("tasks") == 404:
        actions.append("BUILD_TASKS")

    if signal.get("data") == 404:
        actions.append("BUILD_DATA")

    return actions
