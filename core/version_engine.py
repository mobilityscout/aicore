import os, json, time

def layer_path(run_path, layer):
    p = f"{run_path}/{layer}"
    os.makedirs(p, exist_ok=True)
    return p

def state_file(run_path, layer):
    return f"{layer_path(run_path, layer)}/STATE.json"

def load_state(run_path, layer):
    sf = state_file(run_path, layer)
    if not os.path.exists(sf):
        return {
            "current_version": None,
            "versions": [],
            "status": None
        }
    return json.load(open(sf))

def save_state(run_path, layer, state):
    with open(state_file(run_path, layer), "w") as f:
        json.dump(state, f)

def next_version(state):
    return f"V{len(state['versions'])+1}"

def write_version(run_path, layer, data, status):

    state = load_state(run_path, layer)

    v = next_version(state)
    path = f"{layer_path(run_path, layer)}/{v}.json"

    payload = {
        "version": v,
        "time": time.time(),
        "status": status,
        "data": data
    }

    with open(path, "w") as f:
        json.dump(payload, f)

    state["current_version"] = v
    state["versions"].append(v)
    state["status"] = status

    save_state(run_path, layer, state)

    return payload
