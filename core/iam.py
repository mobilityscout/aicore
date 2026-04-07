import os

def mem():
    try:
        return int(os.popen("free -m | awk '/Mem:/ {print $3}'").read())
    except:
        return 0

def decide(signal):

    m = mem()

    # --- RESOURCE LAW ---
    if m < 100:
        mode = "STOP"
    elif m < 500:
        mode = "SLOW"
    else:
        mode = "FULL"

    # --- DECISION ---
    actions = []

    if signal.get("tasks") == 404:
        actions.append("BUILD_TASKS")

    if signal.get("data") == 404:
        actions.append("BUILD_DATA")

    decision = "REPAIR" if actions else "OK"

    return {
        "mode": mode,
        "decision": decision,
        "actions": actions,
        "mem": m
    }
