import os, json
from core.context import get_root
from core.brain import analyze_run

def build_snapshot():

    base = f"{get_root()}/storage/signals"
    runs = sorted(os.listdir(base), reverse=True)

    if not runs:
        return {}

    run = runs[0]
    run_path = f"{base}/{run}"

    analysis = analyze_run(run_path)

    # 🔹 Layer-State laden
    state_file = f"{run_path}/LAYER_STATE.json"
    state = {}

    if os.path.exists(state_file):
        state = json.load(open(state_file))

    return {
        "run": run,
        "analysis": analysis,
        "layer_control": state
    }
