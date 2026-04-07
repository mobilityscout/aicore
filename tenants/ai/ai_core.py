from tenants.ai.systems.analyzer import run as analyze
from tenants.ai.systems.planner import run as plan
from tenants.ai.systems.confidence import evaluate
from tenants.ai.systems.improver import run as improve
from tenants.ai.systems.validator import validate

from tenants.ai.systems.knowledge_core import (
    store_staging,
    store_restricted
)

from tenants.ai.systems.abstraction import abstract
from tenants.ai.systems.security import is_sensitive
from tenants.ai.systems.pattern_engine import weight


def run(signal, tenant="default"):

    print("\n=== AI TENANT ===")

    analysis = analyze(signal)
    print("ANALYSIS:", analysis)

    decision = plan(analysis)
    print("DECISION:", decision)

    confidence = evaluate(signal, decision)
    print("CONFIDENCE:", confidence)

    decision = improve(signal, decision, confidence)
    print("FINAL:", decision)

    valid = False
    if decision.get("action") == "BUILD":
        valid = validate("UI_SYSTEM", tenant)

    entry = {
        "tenant": tenant,
        "signal": signal,
        "decision": decision,
        "confidence": confidence
    }

    # 🔴 SECURITY
    if is_sensitive(entry):
        print("RESTRICTED")
        store_restricted(entry)
        return decision

    # 🔴 ABSTRACTION
    pattern = abstract(entry)

    if pattern:
        level = weight(entry)

        staging_entry = {
            "pattern": pattern,
            "level": level,
            "source": "AI",
            "approved": False
        }

        store_staging(staging_entry)

        print("STAGED:", staging_entry)

    return decision
