def generate(data):

    intent = data.get("intent")

    blueprint = []

    # 🔴 Beispiel: UI bauen
    if intent == "BUILD":

        blueprint = [
            {"step": 1, "action": "CHECK_UI"},
            {"step": 2, "action": "BUILD_UI"},
            {"step": 3, "action": "VALIDATE_UI"},
            {"step": 4, "action": "REGISTER_UI"}
        ]

    return blueprint
