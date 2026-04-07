import os, json
from core.context import get_root

LAYERS = ["L0","L1","L2","L3","L4","L5"]

def _state_file(run_path):
    return f"{run_path}/LAYER_STATE.json"

def init_state(run_path):
    path = _state_file(run_path)

    if os.path.exists(path):
        return json.load(open(path))

    state = {
        "current_layer": "L0",
        "approved_layers": [],
        "blocked_layers": [],
        "mode": "AUTO",
        "iam_locked": True
    }

    with open(path, "w") as f:
        json.dump(state, f)

    return state

def load_state(run_path):
    path = _state_file(run_path)
    if not os.path.exists(path):
        return init_state(run_path)
    return json.load(open(path))

def save_state(run_path, state):
    with open(_state_file(run_path), "w") as f:
        json.dump(state, f)

def next_layer(state):
    for l in LAYERS:
        if l not in state["approved_layers"]:
            return l
    return None

def approve_layer(run_path, layer):
    state = load_state(run_path)

    if layer not in state["approved_layers"]:
        state["approved_layers"].append(layer)

    nxt = next_layer(state)
    state["current_layer"] = nxt if nxt else "DONE"

    save_state(run_path, state)
    return state

def block_layer(run_path, layer):
    state = load_state(run_path)

    if layer not in state["blocked_layers"]:
        state["blocked_layers"].append(layer)

    state["current_layer"] = layer

    save_state(run_path, state)
    return state
