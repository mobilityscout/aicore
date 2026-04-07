import requests, sys, time
from core.memory import write_short, write_mid
from core.health import decide

GREEN = "\033[92m"
RED   = "\033[91m"
YELLOW= "\033[93m"
RESET = "\033[0m"

def check(url):
    try:
        return requests.get(url, timeout=1).status_code
    except:
        return 404

def scan():
    return {
        "state": check("http://127.0.0.1:50000/state"),
        "tasks": check("http://127.0.0.1:50000/tasks"),
        "data":  check("http://127.0.0.1:50000/data")
    }

print("\n=== IAM BOOT (CLEAN) ===")

signal = scan()

# MEMORY
write_short(signal)
write_mid({"t": time.time(), "signal": signal})

# OUTPUT
error = None
for i,k in enumerate(["state","tasks","data"]):
    code = signal[k]
    if code == 200:
        print(f"[{i}] {k} → {GREEN}GREEN{RESET}")
    else:
        print(f"[{i}] {k} → {RED}RED ({code}){RESET}")
        error = k
        break

# HEALTH DECISION
decision = decide(signal, error)

print(f"\n=== HEALTH: {decision} ===")

if decision == "STABLE":
    print(f"{GREEN}SYSTEM STABLE → HARD STOP{RESET}")
    sys.exit(0)

if decision == "KNOWN_ERROR":
    print(f"{YELLOW}KNOWN ERROR → WAIT (no auto fix){RESET}")
    sys.exit(0)

if decision == "UNKNOWN_ERROR":
    print(f"{RED}UNKNOWN ERROR → STORED → IAM REQUIRED{RESET}")
    sys.exit(0)
