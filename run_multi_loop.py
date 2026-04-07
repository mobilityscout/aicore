import time
from core.distributed_scan import run as scan
from core.brain_aggregator import aggregate
from core.entrypoint import run as process


def loop():

    print("\n=== MULTI-TENANT LOOP ===")

    while True:

        findings = scan()

        if not findings:
            print("NO GLOBAL FINDINGS")
            time.sleep(5)
            continue

        # 🔴 global denken
        aggregate(findings)

        # 🔴 lokal handeln
        for f in findings:

            signal = f["finding"].replace("_", " ").lower()

            print("\nTENANT:", f["tenant"], "→", signal)

            process(signal)

        time.sleep(5)


loop()
