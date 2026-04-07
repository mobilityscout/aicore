def run(signal):

    s = signal.lower()

    if "no module named" in s:
        return {"type": "MISSING_MODULE"}

    if "importerror" in s:
        return {"type": "IMPORT_ERROR"}

    if "syntaxerror" in s:
        return {"type": "SYNTAX_ERROR"}

    if "error" in s:
        return {"type": "GENERAL_ERROR"}

    if "build" in s or "baue" in s:
        return {"type": "BUILD"}

    return {"type": "UNKNOWN"}
