from core.iam_brain import decide

def run(signal):

    print("\n=== SYSTEM ORCHESTRATOR ===")

    context = {
        "type": "runtime_signal",
        "signal": signal
    }

    decision = decide(context)

    print("DECISION:", decision)

    d = decision["decision"]

    # ------------------------
    # IGNORE
    # ------------------------
    if d == "IGNORE":
        print("SYSTEM STABLE → STOP")
        return

    # ------------------------
    # RESEARCH FLOW
    # ------------------------
    if d == "RESEARCH":
        print("→ RESEARCH")

        from core.research_engine import run as r
        r()

        print("→ EXECUTION")

        from core.execution_engine import run as e
        e()

        return

    # ------------------------
    # FIX USAGE
    # ------------------------
    if d == "FIX_USAGE":
        print("→ FIX USAGE CONTEXT")
        return

    # ------------------------
    # INSTALL
    # ------------------------
    if d == "INSTALL":
        print("→ INSTALL MODULE:", decision.get("module"))
        return
