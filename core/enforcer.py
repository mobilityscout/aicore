from core.roles import has
from core.policy import allowed


def enforce(role, action):

    if not has(role, action):
        raise Exception(f"ROLE BLOCKED: {role} → {action}")

    if not allowed(role, action):
        raise Exception(f"POLICY BLOCKED: {role} → {action}")

    return True
