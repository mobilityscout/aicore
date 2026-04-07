import os

BASE = "/opt/aicore"


def ensure_file(path, content):

    if not os.path.exists(path):

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w") as f:
            f.write(content)

        print("REBUILT:", path)


def rebuild_minimal():

    print("\n=== IMMUNE CORE ===")

    # 🔴 CORE FILES
    ensure_file(
        BASE + "/core/unified_core.py",
        "def run(signal, tenant='default'):\n    print('MINIMAL CORE ACTIVE')\n    return True\n"
    )

    ensure_file(
        BASE + "/core/health_engine.py",
        "def handle(error, tenant='default'):\n    print('HEALTH FALLBACK:', error)\n    return False\n"
    )

    # 🔴 AI CORE (minimal fallback)
    ensure_file(
        BASE + "/tenants/ai/ai_core.py",
        "def run(signal, tenant='default'):\n    return {'action': 'BUILD'}\n"
    )

    # 🔴 REQUIRED DIRS
    os.makedirs(BASE + "/tenants", exist_ok=True)
    os.makedirs(BASE + "/tenants/ai/systems", exist_ok=True)
    os.makedirs(BASE + "/sot", exist_ok=True)

    print("IMMUNE READY")


def boot(signal, tenant="default"):

    # 🔴 1. SELF REBUILD
    rebuild_minimal()

    # 🔴 2. LOAD REAL CORE
    try:
        from core.unified_core import run
        return run(signal, tenant)

    except Exception as e:
        print("CORE FAIL → FALLBACK:", e)
        return False
