def build(data):

    intent = data.get("intent")

    # 🔴 Beispiel: UI bauen
    if intent == "BUILD":

        return {
            "goal": "UI_SYSTEM",
            "execution_context": "SYSTEM",
            "steps": [
                {"step": 1, "action": "CHECK_UI"},
                {"step": 2, "action": "BUILD_UI"},
                {"step": 3, "action": "VALIDATE_UI"}
            ],
            "risks": [],
            "dependencies": []
        }

    return {}
