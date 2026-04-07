from core.guard_core import risk_level
from core.health_learning import find as learn_find, store as learn_store
import time
from core.signal_core import normalize_signal, validate_signal, is_duplicate
from core.fragment_matcher import match_fragments
from core.health_rules import classify
from core.health_rule_trigger import should_create_rule


def system_state():
    return {
        "timestamp": time.time(),
        "status": "GREEN"
    }


def run(raw_signal):

    print("\n=== HEALTH START ===")

    signal = normalize_signal(raw_signal)

    if not validate_signal(signal):
        print("HEALTH DROP → INVALID")
        return None

    signal["duplicate"] = is_duplicate(signal)

    status = classify(signal)
    signal["health_status"] = status

    # 🔴 RULE TRIGGER
    if should_create_rule(signal):
        signal["rule_needed"] = True
    else:
        signal["rule_needed"] = False

    if status == "THREAT":
        print("🚨 THREAT → BLOCKED")
        return None

    signal["fragments"] = match_fragments(signal)

    state = system_state()

    ensure_index_structure()
    risk = risk_level(raw_signal)
    print("HEALTH RISK:", risk)
    print("HEALTH OK → FORWARD")
    print("STATUS:", status)

    return signal, state

import os

def ensure_index_structure():

    path = "/opt/aicore/index"

    if not os.path.exists(path):
        print("HEALTH: INDEX STRUCTURE MISSING → BUILD")
        os.makedirs(path, exist_ok=True)

        file = path + "/main.jsonl"
        open(file, "a").close()

        return True

    return False

def detect_error(raw):

    raw = str(raw)

    if "IndentationError" in raw:
        return "indentation_error"

    if "SyntaxError" in raw:
        return "syntax_error"

    return "unknown_error"

def learn_and_fix(raw):

    err_type = detect_error(raw)

    fix = learn_find(err_type)

    if fix:
        print("HEALTH: APPLY LEARNED FIX:", fix)

        if fix == "restore_boot":
            import shutil
            shutil.copy("/opt/aicore/baseline/boot.py", "/opt/aicore/core/boot.py")
            return True

    print("HEALTH: NEW ERROR → LEARN")

    if err_type == "indentation_error":
        learn_store(err_type, "restore_boot")

    return False
