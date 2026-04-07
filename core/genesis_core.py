import json, os, time, shutil

BASE = "/opt/aicore/db"
GENESIS_FILE = BASE + "/genesis.json"
LAYER_FILE = BASE + "/layers.json"
VERSIONS_DIR = BASE + "/versions"

def ensure():
    os.makedirs(VERSIONS_DIR, exist_ok=True)

def load_layers():
    return json.load(open(LAYER_FILE))

def lock_genesis():

    ensure()

    if os.path.exists(GENESIS_FILE):
        return {"status": "ALREADY_LOCKED"}

    layers = load_layers()

    if not layers:
        return {"status": "NO_LAYER"}

    genesis = layers[-1]

    # speichern als Genesis
    json.dump(genesis, open(GENESIS_FILE, "w"), indent=2)

    # Version Snapshot erzeugen
    vid = "v1"
    path = VERSIONS_DIR + "/" + vid
    os.makedirs(path, exist_ok=True)

    shutil.copy(LAYER_FILE, path + "/layers.json")

    return {
        "status": "GENESIS_LOCKED",
        "layer": genesis["id"],
        "version": vid
    }

def get_genesis():
    if not os.path.exists(GENESIS_FILE):
        return None
    return json.load(open(GENESIS_FILE))
