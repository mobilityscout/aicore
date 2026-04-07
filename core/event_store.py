import os, json, time, uuid, hashlib, fcntl
from core.context import base_path

LAST_EVENT = None

def append_event(signal_id, run_id, layer, etype, payload):
    global LAST_EVENT

    root = base_path()
    runtime = f"{root}/runtime"
    store = f"{root}/event-store/{signal_id}"

    os.makedirs(runtime, exist_ok=True)
    os.makedirs(store, exist_ok=True)

    hash_file = f"{runtime}/global_hash"

    if os.path.exists(hash_file):
        prev_hash = open(hash_file).read().strip()
    else:
        prev_hash = "GENESIS"

    event = {
        "event_id": str(uuid.uuid4()),
        "time": time.time(),
        "signal_id": signal_id,
        "run_id": run_id,
        "layer": layer,
        "type": etype,
        "payload": payload,
        "prev_hash": prev_hash
    }

    event["hash"] = hashlib.sha256(
        json.dumps(event, sort_keys=True).encode()
    ).hexdigest()

    file = f"{store}/events.log"

    with open(file, "a") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write(json.dumps(event)+"\n")
        f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)

    with open(hash_file, "w") as h:
        h.write(event["hash"])

    LAST_EVENT = event
    return event
