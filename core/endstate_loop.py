import time
from core.endstate_model import build_state_model
from core.endstate_evaluator import evaluate
from core.completion_engine import run as complete
from core.architecture_engine import detect_missing_capabilities
from core.expansion_engine import expand


def run():

    print("\n=== SELF-EXPANDING LOOP ===")

    for i in range(10):

        print("\n--- ITERATION", i, "---")

        state = build_state_model()

        scores, overall = evaluate(state)

        print("STATE:", state)
        print("OVERALL:", round(overall * 100, 2), "%")

        # 🔴 EXPANSION
        missing = detect_missing_capabilities(state)

        if missing:
            expand(missing)

        # 🔴 COMPLETION
        if overall < 1.0:
            complete(scores, state)

        if overall == 1.0 and not missing:
            print("\nSYSTEM FULLY EXPANDED + COMPLETE")
            return True

        time.sleep(2)

    print("\nSYSTEM PARTIAL")
    return False
