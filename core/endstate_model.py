import os

BASE = "/opt/aicore"

def evaluate_path(path):

    return {
        "exists": os.path.exists(path),
        "files": len(os.listdir(path)) if os.path.exists(path) else 0
    }

def build_state_model():

    model = {}

    # 🔴 CORE SYSTEMS
    model["state"] = evaluate_path(BASE + "/state")
    model["ui"] = evaluate_path(BASE + "/ui")
    model["db"] = evaluate_path(BASE + "/db")
    model["core"] = evaluate_path(BASE + "/core")

    return model
