import json
import time

STATE_FILE = "/opt/aicore/state.json"


def load_state():
    with open(STATE_FILE) as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def add_step(name):
    state = load_state()
    step = {
        "id": len(state["steps"]),
        "name": name,
        "status": "pending",
        "timestamp": time.time()
    }
    state["steps"].append(step)
    save_state(state)
    return step


def confirm_step():
    state = load_state()
    step = state["steps"][-1]
    step["status"] = "ok"
    step["confirmed_at"] = time.time()
    save_state(state)
    return step


def get_last_ok():
    state = load_state()
    for step in reversed(state["steps"]):
        if step["status"] == "ok":
            return step
    return None
