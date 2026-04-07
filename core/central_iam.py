from core.signal_core import normalize_signal, validate_signal
from core.iam_core import decide
from core.iam_state import update


def run(signal_raw):

    signal = normalize_signal(signal_raw)

    if not validate_signal(signal):
        return None

    decision, score, priority = decide(signal, False)

    update(signal, decision, score, priority)

    print("\n=== CENTRAL IAM ===")
    print("DECISION:", decision, "| SCORE:", score, "| PRIORITY:", priority)

    return {
        "signal": signal,
        "decision": decision,
        "score": score,
        "priority": priority
    }
