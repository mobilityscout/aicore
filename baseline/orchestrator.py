from core.signal_core import normalize_signal, validate_signal
from core.iam_core import decide
from core.action_mapper import map_action

def execute(action, signal):

    if not action:
        return False

    return False


def run(signal):

    print("\n=== SIGNAL RECEIVED ===")

    signal = normalize_signal(signal)

    if not validate_signal(signal):
        print("INVALID SIGNAL")
        return

    decision, score, priority = decide(signal, False)

    print("IAM:", decision, "| SCORE:", score)

    action = map_action(signal, decision)

    result = execute(action, signal)

    if result:
        print("SUCCESS")
    else:
        print("FAILED")
