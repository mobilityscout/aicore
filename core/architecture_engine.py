import os

BASE = "/opt/aicore/core"


def exists(system):

    path = os.path.join(BASE, system.lower() + ".py")
    return os.path.exists(path)


def detect_missing_capabilities(state):

    missing = []

    # 🔴 WRITE SYSTEM
    if not exists("write_system"):
        missing.append("WRITE_SYSTEM")

    # 🔴 ADVANCED SCAN
    if not exists("advanced_scan_system"):
        missing.append("ADVANCED_SCAN_SYSTEM")

    # 🔴 IAM
    if not exists("iam_system"):
        missing.append("IAM_SYSTEM")

    return missing
