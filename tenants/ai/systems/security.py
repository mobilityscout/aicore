def is_sensitive(entry):

    signal = entry.get("signal", "").lower()

    # 🔴 primitive Filter (erweiterbar)
    forbidden = ["api key", "password", "secret"]

    for f in forbidden:
        if f in signal:
            return True

    return False
