import json

RULE_DB = "/opt/aicore/rules/health_rules.jsonl"


def approve_latest():

    lines = open(RULE_DB).readlines()

    if not lines:
        return False

    updated = []

    for i, line in enumerate(lines):
        r = json.loads(line)

        if i == len(lines) - 1 and r.get("status") == "PENDING":
            r["status"] = "APPROVED"

        updated.append(json.dumps(r))

    with open(RULE_DB, "w") as f:
        f.write("\n".join(updated) + "\n")

    return True
