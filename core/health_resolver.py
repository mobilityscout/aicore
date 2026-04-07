import json, os

LIB = "/opt/aicore/db/library.jsonl"

def match(signal):

    if not os.path.exists(LIB):
        return None

    for line in open(LIB):
        try:
            e = json.loads(line)

            if e.get("task", {}).get("signal") == signal:
                if e.get("lifecycle", {}).get("status") == "LOCKED":
                    return e

        except:
            continue

    return None

def resolve(signal):

    print("\n=== HEALTH RESOLVE ===")

    match_case = match(signal)

    if not match_case:
        print("NO MATCH IN LIBRARY")
        return None

    action = match_case.get("decision", {}).get("action")

    print("MATCH FOUND")
    print("ACTION:", action)

    return action
