import os, json

def analyze_run(run_path):

    result = {
        "layers": {},
        "complete": True,
        "errors": []
    }

    layers = ["L0","L1","L2","L3","L4","L5"]

    for l in layers:
        f = f"{run_path}/{l}.log"

        if not os.path.exists(f):
            result["complete"] = False
            result["errors"].append(f"{l} missing")
            continue

        lines = [json.loads(x) for x in open(f)]

        result["layers"][l] = {
            "count": len(lines),
            "last": lines[-1] if lines else None
        }

    return result
