def map_action(signal, decision):

    if decision == "BUILD_UI":
        return {"engine": "BUILD_UI"}

    if decision == "BUILD_API":
        return {"engine": "BUILD_API"}

    if decision == "BUILD_DB":
        return {"engine": "BUILD_DB"}

    if decision == "FIX":
        return {"engine": "FIX"}

    return None
