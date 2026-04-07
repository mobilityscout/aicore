def evaluate(signal, decision):

    # 🔴 einfache Basislogik
    if decision.get("action") == "BUILD":
        return 0.8

    return 0.5
