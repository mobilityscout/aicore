import json
import os

INDEX = "/opt/aicore/index/main.jsonl"


def extract_tenant(path):

    parts = path.split("/")

    if "tenants" in parts:
        i = parts.index("tenants")
        if i + 1 < len(parts):
            return parts[i + 1]

    return "core"


def build_entry(item):

    entry = {
        "path": item.get("path"),
        "type": item.get("type"),
        "score": item.get("score"),
        "tenant": extract_tenant(item.get("path"))
    }

    analysis = item.get("analysis", {})

    if "keys" in analysis:
        entry["keys"] = analysis["keys"]

    if "functions" in analysis:
        entry["functions"] = analysis["functions"]

    return entry


def store_index(data):

    with open(INDEX, "a") as f:
        for item in data:
            entry = build_entry(item)
            f.write(json.dumps(entry) + "\n")


def load_index():

    if not os.path.exists(INDEX):
        return []

    result = []

    for line in open(INDEX):
        try:
            result.append(json.loads(line))
        except:
            continue

    return result


def query_index(qtype=None, tenant=None):

    data = load_index()

    results = []

    for d in data:

        if qtype and d.get("type") != qtype:
            continue

        if tenant and d.get("tenant") != tenant:
            continue

        results.append(d)

    return sorted(results, key=lambda x: x.get("score", 0), reverse=True)
