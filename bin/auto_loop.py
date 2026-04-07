import time, requests
from core.system_orchestrator import run

INTERVAL = 5
MAX_IDLE = 8

idle = 0
last = None

def scan():
    def c(u):
        try:
            return requests.get(u, timeout=1).status_code
        except:
            return 404

    return {
        "state": c("http://127.0.0.1:50000/state"),
        "tasks": c("http://127.0.0.1:50000/tasks"),
        "data":  c("http://127.0.0.1:50000/data")
    }

print("\n=== AUTO SYSTEM LIVE ===")

while True:

    s = scan()
    print("\nSIGNAL:", s)

    if s == last:
        idle += 1
        print(f"IDLE {idle}/{MAX_IDLE}")

        if idle >= MAX_IDLE:
            print("→ STAGNATION → LAYER")

            from core.layer_manager import new_layer
            new_layer(s)

            idle = 0

        time.sleep(INTERVAL)
        continue

    idle = 0
    last = s

    run(s)

    time.sleep(INTERVAL)
