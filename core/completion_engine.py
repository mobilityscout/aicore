from core.ai_builder import build
from core.write_system import write
from core.integration_engine import integrate
from core.functional_validator import validate


def complete(system, state):

    print("\n=== SEMANTIC BUILD:", system, "===")

    blueprint = build(system, state)

    write(blueprint)

    # 🔴 FUNKTIONALE PRÜFUNG
    ok = validate(system)

    if not ok:
        print("SEMANTIC FAIL → REBUILD:", system)

        blueprint = build(system, state)
        write(blueprint)

    integrate(system)

    print("SYSTEM READY:", system)

    return True


def run(scores, state):

    for k, v in scores.items():

        if k == "ui":
            complete("UI_SYSTEM", state)

        elif k == "state":
            complete("STATE_SYSTEM", state)
