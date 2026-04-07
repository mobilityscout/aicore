import json, os, time, shutil

BASE = "/opt/aicore/db"
LAYER_FILE = BASE + "/layers.json"
VERSIONS_DIR = BASE + "/versions"

def create_version():

    if not os.path.exists(LAYER_FILE):
        return {"status": "NO_LAYER"}

    versions = sorted(os.listdir(VERSIONS_DIR)) if os.path.exists(VERSIONS_DIR) else []
    vid = "v" + str(len(versions) + 1)

    path = VERSIONS_DIR + "/" + vid
    os.makedirs(path, exist_ok=True)

    shutil.copy(LAYER_FILE, path + "/layers.json")

    return {
        "status": "VERSION_CREATED",
        "version": vid
    }
