import random

def generate_hypotheses(signal):

    # einfache Startlogik (später erweiterbar)
    base = signal["type"]

    if base == "ERROR":
        return [
            {"type": "ADD_ENDPOINT"},
            {"type": "INSTALL_PACKAGE", "name": "flask"},
            {"type": "RESTART_SERVICE"}
        ]

    return []


def select_next(hypotheses, tried):

    for h in hypotheses:
        key = str(h)

        if key not in tried:
            return h

    return None
