import json, os, time
from collections import Counter

BASE = "/opt/aicore/library"
ERROR_FILE = BASE + "/errors.jsonl"
RULE_FILE = BASE + "/rules.json"
LAW_FILE = BASE + "/law.json"

# --- ENSURE FILES ---
def ensure():
    os.makedirs(BASE, exist_ok=True)

    if not os.path.exists(ERROR_FILE):
        open(ERROR_FILE, "w").close()

    if not os.path.exists(RULE_FILE):
        json.dump({}, open(RULE_FILE, "w"), indent=2)

# --- LOAD ---
def load_errors():
    with open(ERROR_FILE) as f:
        return [json.loads(l) for l in f if l.strip()]

def load_rules():
    return json.load(open(RULE_FILE))

def save_rules(rules):
    json.dump(rules, open(RULE_FILE, "w"), indent=2)

# --- ERROR INPUT ---
def add_error(error_type, context=None):

    entry = {
        "t": time.time(),
        "type": error_type,
        "context": context or {}
    }

    with open(ERROR_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return entry

# --- CORE: RULE GENERATION ---
def build_rules():

    ensure()

    errors = load_errors()
    rules = load_rules()

    if not errors:
        return rules

    # Fehler zählen
    counter = Counter([e["type"] for e in errors])

    for err, count in counter.items():

        # Regel nur wenn relevant
        if count >= 3:

            if err not in rules:

                # automatische Regelbildung
                rules[err] = {
                    "action": infer_action(err),
                    "count": count,
                    "created": time.time()
                }

    save_rules(rules)
    return rules

# --- INTELLIGENTE ACTION ABLEITUNG ---
def infer_action(error):

    if "NO_TASK" in error:
        return "INIT_TASK_LAYER"

    if "404" in error:
        return "BUILD_ENDPOINT"

    if "IMPORT" in error:
        return "FIX_IMPORT_PATH"

    return "OBSERVE"

# --- APPLY RULES (für Health) ---
def apply_rules(signal):

    rules = load_rules()

    actions = []

    for err, rule in rules.items():
        actions.append(rule["action"])

    return actions

