import json, os

RULE_DB = "/opt/aicore/rules/health_rules.jsonl"


def load_rules():

    if not os.path.exists(RULE_DB):
        return []

    rules = []

    for line in open(RULE_DB):
        try:
            r = json.loads(line)

            # 🔴 NUR VALIDIERTE REGELN
            if r.get("status") == "VALIDATED":
                rules.append(r)

        except:
            continue

    return rules


def classify(signal):

    content = signal.get("content", "").lower()
    rules = load_rules()

    best = {
        "type": "OK",
        "confidence": 0
    }

    for r in rules:

        pattern = r.get("pattern", "").lower()

        if pattern and pattern in content:

            if r.get("confidence", 0) > best["confidence"]:
                best = r

    return best.get("type", "OK")
