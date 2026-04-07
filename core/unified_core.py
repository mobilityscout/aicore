import json
import time
import os

from tenants.ai.ai_core import run as ai_run
from core.health_engine import handle as health
from core.evolution_engine import evolve
from core.deploy_engine import deploy

BASE = "/opt/aicore"
SOT = BASE + "/sot/main.jsonl"


def interpret(text):

    t = text.lower()

    if "baue" in t:
        return {"action": "EVOLVE", "target": "UI_SYSTEM"}

    return {"action": None}


def store(entry):

    os.makedirs("/opt/aicore/sot", exist_ok=True)

    entry["timestamp"] = time.time()

    with open(SOT, "a") as f:
        f.write(json.dumps(entry) + "\n")


def run(signal, tenant="default"):

    print("\n=== UNIFIED CORE ===")

    try:

        decision = ai_run(signal, tenant)
        semantic = interpret(signal)

        if semantic["action"] == "EVOLVE":

            def builder(path):
                file = path + "/ui_system.py"
                with open(file, "w") as f:
                    f.write("def run(): return 'UI EVOLVED'")

            ok, sandbox = evolve(tenant, "UI_SYSTEM", builder)

            if ok:
                deploy(tenant, sandbox)

        store({
            "tenant": tenant,
            "signal": signal,
            "decision": decision
        })

        return True

    except Exception as e:
        return health(str(e), tenant)
