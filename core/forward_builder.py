from core.reverse_scan import reverse_find
from core.version_engine import write_version

LAYERS = ["L0","L1","L2","L3","L4","L5"]

def next_layer(layer):
    i = LAYERS.index(layer)
    return LAYERS[i+1] if i+1 < len(LAYERS) else None

def rebuild_chain(run_path):

    stable = reverse_find(run_path, LAYERS)
    if not stable:
        return {"status":"STOP"}

    current = stable["layer"]
    data = stable["data"]["data"]

    while True:
        nxt = next_layer(current)
        if not nxt:
            break

        new_data = {"from": current, "payload": data}

        write_version(run_path, nxt, new_data, "REPAIRING")
        write_version(run_path, nxt, new_data, "FINAL")

        current = nxt
        data = new_data

    return {"status":"REBUILT","start":stable["layer"],"end":current}
