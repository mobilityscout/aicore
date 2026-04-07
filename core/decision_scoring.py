def score_decision(signal, decision):

    score = 0.5
    priority = "LOW"

    # 🔴 KNOWN SIGNALS
    if signal.get("known"):
        score = 0.95
        priority = "LOW"

    # 🔴 ERROR
    elif signal.get("type") == "ERROR":
        score = 0.85
        priority = "HIGH"

    # 🔴 CODE
    elif signal.get("type") == "CODE":
        score = 0.7
        priority = "MEDIUM"

    # 🔴 RESEARCH
    if decision == "RESEARCH":
        score = 0.4
        priority = "LOW"

    # 🔴 ESCALATION
    if decision == "ESCALATE":
        score = 1.0
        priority = "CRITICAL"

    return round(score, 2), priority
