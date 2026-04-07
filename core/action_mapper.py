def map_action(signal, decision):

    if decision.startswith("BUILD_STRUCTURE"):
        structure = decision.split(":")[1]
        return {"engine": "STRUCTURE", "structure": structure}

    if decision == "SELF_HEAL":
        return {"engine": "HEALTH"}

    return None
