import time
from core.system_test import run as test
from core.failure_extractor import extract
from core.entrypoint import run as process


def run():

    print("\n=== CLOSED SELF-HEAL LOOP ===")

    max_cycles = 10
    cycle = 0

    while cycle < max_cycles:

        print("\n--- CYCLE", cycle, "---")

        result = test()

        score = result.get("score", 0)

        if score == 1.0:
            print("\nSYSTEM FULLY OPERATIONAL (100%)")
            return True

        # 🔴 FAIL → SIGNAL
        signals = extract(result)

        if not signals:
            print("NO SIGNALS BUT NOT 100% → STOP")
            return False

        for s in signals:
            print("\nAUTO SIGNAL →", s)
            process(s)

        cycle += 1
        time.sleep(2)

    print("\nMAX CYCLES REACHED")
    return False
