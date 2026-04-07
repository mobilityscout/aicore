import json


def analyze_state(content):

    try:
        data = json.loads(content)

        keys = list(data.keys())

        score = 0.5

        if "status" in keys:
            score += 0.2

        if "id" in keys:
            score += 0.2

        return {
            "valid": True,
            "keys": keys,
            "score": round(min(score, 1.0), 2)
        }

    except:
        return {
            "valid": False,
            "keys": [],
            "score": 0.2
        }


def analyze_code(content):

    lines = content.split("\n")

    functions = [l for l in lines if l.strip().startswith("def ")]

    return {
        "functions": len(functions),
        "score": min(0.5 + len(functions)*0.05, 1.0)
    }


def read_file(entry):

    path = entry["path"]
    ftype = entry["type"]

    try:
        with open(path, "r") as f:
            content = f.read()
    except:
        return None

    result = {
        "path": path,
        "type": ftype,
        "size": entry["size"]
    }

    # 🔴 STATE
    if ftype == "state":
        analysis = analyze_state(content)
        result["analysis"] = analysis
        result["score"] = analysis["score"]

    # 🔴 CODE
    elif ftype == "code":
        analysis = analyze_code(content[:2000])
        result["analysis"] = analysis
        result["score"] = analysis["score"]

    # 🔴 CONFIG
    elif ftype == "config":
        result["score"] = 0.7

    # 🔴 LOG
    elif ftype == "log":
        result["score"] = 0.2

    else:
        result["score"] = 0.3

    return result


def read_horizontal(data):

    results = []

    for entry in data:

        if entry["score"] < 0.7:
            continue

        res = read_file(entry)

        if res:
            results.append(res)

    return sorted(results, key=lambda x: x["score"], reverse=True)
