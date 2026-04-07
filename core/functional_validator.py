def validate_ui():

    try:
        import core.ui_system as ui

        result = ui.run()

        # 🔴 einfache Semantikprüfung
        if isinstance(result, str) and "<html" in result.lower():
            return True

        return False

    except Exception as e:
        print("UI VALIDATION ERROR:", e)
        return False


def validate_state():

    try:
        import core.state_system as s

        result = s.run()

        if isinstance(result, dict):
            return True

        return False

    except:
        return False


def validate(system):

    if system == "UI_SYSTEM":
        return validate_ui()

    if system == "STATE_SYSTEM":
        return validate_state()

    return True
