import os, json

def load_versions(layer_path):
    files = sorted([f for f in os.listdir(layer_path) if f.startswith("V")])
    return [json.load(open(f"{layer_path}/{f}")) for f in files]

def find_last_stable(layer_path):
    versions = load_versions(layer_path)
    for v in reversed(versions):
        if v["status"] == "FINAL":
            return v
    return None

def reverse_find(run_path, layers):
    for layer in reversed(layers):
        path = f"{run_path}/{layer}"
        if not os.path.exists(path):
            continue
        stable = find_last_stable(path)
        if stable:
            return {"layer": layer, "data": stable}
    return None
