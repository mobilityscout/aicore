import json, os, time
from collections import defaultdict

LAYER_DB = "/opt/aicore/db/layers.jsonl"
DERIVED_DB = "/opt/aicore/db/derived.jsonl"

def load_layers():
    if not os.path.exists(LAYER_DB):
        return []

    data = []
    for line in open(LAYER_DB):
        try:
            data.append(json.loads(line))
        except:
            continue
    return data


def merge_layers():

    layers = load_layers()
    groups = defaultdict(list)

    # gruppieren nach signal_hash + decision
    for l in layers:
        key = (l.get("signal_hash"), l.get("decision"))
        groups[key].append(l)

    derived_signals = []

    for (signal_hash, decision), items in groups.items():

        if len(items) < 2:
            continue

        success_count = sum(1 for i in items if i.get("state") == "GREEN")
        total = len(items)

        confidence = success_count / total if total > 0 else 0

        derived = {
            "id": str(int(time.time()*1000)),
            "type": "DERIVED",
            "signal_hash": signal_hash,
            "decision": decision,
            "count": total,
            "success": success_count,
            "confidence": round(confidence, 3),
            "timestamp": time.time()
        }

        derived_signals.append(derived)

    # speichern
    if derived_signals:
        with open(DERIVED_DB, "a") as f:
            for d in derived_signals:
                f.write(json.dumps(d) + "\n")

    print("MERGE COMPLETE:", len(derived_signals), "DERIVED SIGNALS")
    return derived_signals


if __name__ == "__main__":
    merge_layers()
