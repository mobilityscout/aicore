from core.health_learning import find as learn_find


def get_strategies(signal):

    raw = signal.get("raw", "").lower()

    strategies = []

    if "missing state" in raw:
        strategies = [
            {"type": "ADD_ENDPOINT"},
            {"type": "CREATE_STATE"},
            {"type": "REBUILD_SERVICE"}
        ]

    learned = learn_find(raw)
    if learned:
        strategies.insert(0, {"type": learned})

    return strategies


def handle_failure(signal):

    print("\n=== HEALTH MANAGEMENT ===")

    strategies = get_strategies(signal)

    if not strategies:
        print("NO STRATEGIES AVAILABLE")
        return None

    # 🔴 nur erste Strategie zurückgeben (keine Ausführung!)
    return strategies[0]
