import os

BASE = "/opt/aicore/tenants"


def tenant_path(tenant):

    path = os.path.join(BASE, tenant)

    os.makedirs(path + "/systems", exist_ok=True)
    os.makedirs(path + "/data", exist_ok=True)
    os.makedirs(path + "/index", exist_ok=True)

    return path
