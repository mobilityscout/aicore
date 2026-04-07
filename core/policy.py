POLICIES = {

    "BUILD": ["admin", "system"],
    "DEPLOY": ["admin"],
    "EVOLVE": ["admin"],
    "READ": ["admin", "tenant"],
    "ANALYZE": ["ai"],
    "SUGGEST": ["ai"]
}


def allowed(role, action):

    allowed_roles = POLICIES.get(action, [])

    return role in allowed_roles
