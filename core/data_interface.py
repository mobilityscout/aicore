def normalize(input_data):

    # 🔴 STRING (Chat)
    if isinstance(input_data, str):

        text = input_data.lower()

        if "baue" in text or "build" in text:
            return {
                "type": "COMMAND",
                "intent": "BUILD",
                "target": "UI_SYSTEM",
                "data": {},
                "context": {}
            }

        return {
            "type": "TEXT",
            "intent": "UNKNOWN",
            "data": {"text": input_data},
            "context": {}
        }

    # 🔴 DICT (API / JSON)
    if isinstance(input_data, dict):

        return {
            "type": "STRUCTURED",
            "intent": input_data.get("intent"),
            "data": input_data,
            "context": input_data.get("context", {})
        }

    return {
        "type": "UNKNOWN",
        "intent": None,
        "data": {},
        "context": {}
    }
