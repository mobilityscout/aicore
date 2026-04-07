CURRENT_TENANT = "default"

def set_tenant(t):
    global CURRENT_TENANT
    CURRENT_TENANT = t

def get_tenant():
    return CURRENT_TENANT
