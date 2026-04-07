def run(analysis):

    t = analysis.get("type")

    if t == "MISSING_MODULE":
        return {"action": "BUILD_MODULE"}

    if t == "IMPORT_ERROR":
        return {"action": "REPAIR_IMPORT"}

    if t == "SYNTAX_ERROR":
        return {"action": "REWRITE_FILE"}

    if t == "GENERAL_ERROR":
        return {"action": "INVESTIGATE"}

    if t == "BUILD":
        return {"action": "BUILD"}

    return {"action": "IGNORE"}
