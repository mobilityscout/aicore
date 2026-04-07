def map_intent(text):

    t = text.lower()

    if "ui" in t:
        return "UI_SYSTEM"

    if "state" in t:
        return "STATE_SYSTEM"

    return None
