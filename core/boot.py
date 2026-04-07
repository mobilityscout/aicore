def boot():

    print("\\n=== BOOTSTRAP SYSTEM ===")

    # 🔴 IMMUNE CORE (immer zuerst!)
    try:
        from core.bootstrap import run as bootstrap
        bootstrap()
    except Exception as e:
        print("CRITICAL: bootstrap failed", e)
        return False

    # 🔴 HAUPTSYSTEM
    try:
        from core.endstate_loop import run
        return run()

    except Exception as e:
        print("SYSTEM LOAD FAIL:", e)
        return False
