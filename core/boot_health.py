import os

CRITICAL_PATHS = [
    "/opt/aicore/index",
    "/opt/aicore/db",
    "/opt/aicore/bin/live_ui.py",
    "/opt/aicore/core/orchestrator.py"
]


def check():

    issues = []

    for p in CRITICAL_PATHS:

        if not os.path.exists(p):
            issues.append(p)

    return issues


def repair():

    issues = check()

    if not issues:
        print("BOOT HEALTH: OK")
        return True

    print("BOOT HEALTH: ISSUES DETECTED")

    for i in issues:

        print("MISSING:", i)

        if i.endswith("/index"):
            os.makedirs(i, exist_ok=True)

        if i.endswith("/db"):
            os.makedirs(i, exist_ok=True)

        if i.endswith(".py"):
            print("STRUCTURE FILE MISSING → REQUIRE REBUILD")

    return False
