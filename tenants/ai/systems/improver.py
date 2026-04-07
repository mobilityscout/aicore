def run(signal, decision, confidence):

    if confidence < 0.6:
        return {"action": "RETRY"}

    return decision
