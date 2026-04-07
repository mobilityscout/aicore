# 🔴 CORE LOCK SYSTEM

SIGNAL_REGISTRY = set()
EXECUTION_REGISTRY = set()

ENV_LOCK = {
    "active": False
}


def signal_lock(signal):
    h = signal.get("hash")

    if h in SIGNAL_REGISTRY:
        return False

    SIGNAL_REGISTRY.add(h)
    return True


def execution_lock(action):
    key = str(action)

    if key in EXECUTION_REGISTRY:
        return False

    EXECUTION_REGISTRY.add(key)
    return True


def environment_lock():
    if ENV_LOCK["active"]:
        return False

    ENV_LOCK["active"] = True
    return True
