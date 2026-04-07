ROLES = {
    "admin": ["ALL"],
    "tenant": ["BUILD", "READ"],
    "ai": ["ANALYZE", "SUGGEST"],
    "system": ["EXECUTE"]
}


def has(role, action):

    perms = ROLES.get(role, [])

    if "ALL" in perms:
        return True

    return action in perms
