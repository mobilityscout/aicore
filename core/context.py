import os

def get_tenant():
    return os.environ.get("AICORE_TENANT", "ms24")

def get_root():
    return f"/opt/aicore/tenants/{get_tenant()}/ai-platform"
