import os

TENANTS_DIR = "/opt/aicore/tenants"


def list_tenants():

    if not os.path.exists(TENANTS_DIR):
        return []

    return [
        d for d in os.listdir(TENANTS_DIR)
        if os.path.isdir(os.path.join(TENANTS_DIR, d))
    ]
