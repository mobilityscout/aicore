def optimize(work, evaluation):

    score = evaluation["score"]

    # 🔴 schlecht → mehr Schritte / Checks
    if score < 2:
        work["steps"].append({
            "step": 99,
            "action": "EXTRA_VALIDATION"
        })

    # 🔴 gut → einfacher machen
    if score == 3 and len(work["steps"]) > 2:
        work["steps"] = work["steps"][:2]

    return work
