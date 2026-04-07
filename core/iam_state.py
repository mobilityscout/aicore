STATE = {
    "last_signal": None,
    "decision": None,
    "score": None,
    "priority": None,
    "fragments": [],
    "timestamp": None
}


def update(signal, decision, score, priority):
    import time

    STATE["last_signal"] = signal.get("content")
    STATE["decision"] = decision
    STATE["score"] = score
    STATE["priority"] = priority
    STATE["fragments"] = signal.get("fragments", [])
    STATE["timestamp"] = time.time()


def get():
    return STATE
