from core.system_guard import is_stable

def run(signal):

    print("\n=== SYSTEM TRIGGER ===")

    # ------------------------
    # HARD STOP (WICHTIG)
    # ------------------------
    if is_stable(signal):
        print("SYSTEM STABLE → STOP")
        return

    # ------------------------
    # HEALTH RESOLVE
    # ------------------------
    from core.health_resolver import resolve
    action = resolve(signal)

    # ------------------------
    # MATCH → EXECUTION
    # ------------------------
    if action:
        print("→ EXECUTION TRIGGER")

        from core.execution_engine import run as exec_run
        exec_run()
        return

    # ------------------------
    # NO MATCH → RESEARCH
    # ------------------------
    print("→ RESEARCH TRIGGER")

    from core.research_engine import run as research_run
    research_run()

    print("\n→ EXECUTION AFTER RESEARCH")

    from core.execution_engine import run as exec_run
    exec_run()

    print("\n=== SYSTEM BUILD COMPLETE ===")
