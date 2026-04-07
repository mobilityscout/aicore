from core.iam_core import decide
from core.layer_core import add
from core.guard_core import execute

def run():

    signal = {}

    iam = decide(signal)
    decision = iam.get("decision", "OBSERVE")
    actions = iam.get("actions", [])

    # --- ACT ---
    results = execute(actions)

    layer = add(decision, {
        "actions": actions,
        "results": results
    })

    return {
        "state": decision,
        "layer": layer["id"],
        "results": results
    }
