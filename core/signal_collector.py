import time, os, json
from core.context import get_root

RUN_ID = str(int(time.time()))

SIGNALS = []

def collect(signal, strength, source):
    entry = {
        "time": time.time(),
        "run": RUN_ID,
        "signal": signal,
        "strength": strength,
        "source": source
    }

    SIGNALS.append(entry)

    base = get_root()
    os.makedirs(base + "/logs", exist_ok=True)

    # eigenes Logfile pro Reboot
    with open(f"{base}/logs/signal_{RUN_ID}.log", "a") as f:
        f.write(json.dumps(entry) + "\n")

    return entry

def get_signals():
    return SIGNALS
