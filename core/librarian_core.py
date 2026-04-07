def transform(raw):

    # 1. Struktur erzwingen (Grundgesetz)
    structured = {
        "vertical": raw.get("dirs"),
        "horizontal": raw.get("files"),
        "risk": raw.get("risk"),
        "context": raw
    }

    # 2. Business Layer (dein Punkt!)
    plan = {
        "task": "ANALYZE_STRUCTURE",
        "allowed": True,
        "mode": "READ_ONLY_FIRST"
    }

    return {
        "structured": structured,
        "plan": plan
    }
