import json

RULE_DB = "/opt/aicore/rules/health_rules.jsonl"


def validate_rule(index):

    lines = open(RULE_DB).readlines()

    if index >= len(lines):
        return False

    updated = []

    for i, line in enumerate(lines):
        r = json.loads(line)

        if i == index:
            r["status"] = "VALIDATED"

        updated.append(json.dumps(r))

    with open(RULE_DB, "w") as f:
        f.write("\n".join(updated) + "\n")

    return True


def get_pending():

    pending = []

    for i, line in enumerate(open(RULE_DB)):
        try:
            r = json.loads(line)

            if r.get("status") == "PENDING":
                r["_id"] = i
                pending.append(r)
        except:
            continue

    return pending
