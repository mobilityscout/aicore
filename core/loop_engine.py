import time
from core.entrypoint import run


def scan():

    # 🔴 einfache erste Selbstbeobachtung
    return [
        "error: missing state endpoint",
        "ui: dashboard missing"
    ]


def loop():

    print("\n=== ADAPTIVE LOOP START ===")

    while True:

        signals = scan()

        for s in signals:
            print("\nLOOP SIGNAL →", s)
            run(s)

        time.sleep(5)
