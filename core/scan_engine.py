import os


def classify_file(name):

    name_l = name.lower()

    if name_l.endswith(".py"):
        return "code"

    if name_l.endswith(".json"):
        if "state" in name_l:
            return "state"
        return "config"

    if name_l.endswith(".log"):
        return "log"

    if "api" in name_l:
        return "api"

    return "unknown"


def score_file(ftype, size, depth):

    # 🔴 Basis
    score = 0.3

    # 🔴 wichtigste Strukturen
    if ftype == "state":
        score = 1.0

    elif ftype == "config":
        score = 0.9

    elif ftype == "api":
        score = 0.85

    elif ftype == "code":
        score = 0.8

    elif ftype == "log":
        score = 0.2

    # 🔴 Tiefe leicht berücksichtigen
    if depth < 4:
        score += 0.05

    return round(min(score, 1.0), 2)


def scan_vertical(base):

    results = []

    for root, dirs, files in os.walk(base):

        depth = root.count("/")

        for f in files:

            path = os.path.join(root, f)

            try:
                size = os.path.getsize(path)
            except:
                size = 0

            ftype = classify_file(f)

            entry = {
                "path": path,
                "name": f,
                "type": ftype,
                "size": size,
                "depth": depth,
                "score": score_file(ftype, size, depth)
            }

            results.append(entry)

    return sorted(results, key=lambda x: x["score"], reverse=True)
