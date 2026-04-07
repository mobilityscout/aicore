import os
from core.tenant_engine import build_runtime
from core.central_iam import run as central_iam

TENANTS = "/opt/aicore/tenants"


def list_tenants():
    if not os.path.exists(TENANTS):
        return []
    return [t for t in os.listdir(TENANTS) if os.path.isdir(f'{TENANTS}/{t}')]


def execute_for_tenant(name, context):

    print(f"\n=== TENANT: {name} ===")

    runtime = build_runtime(name)

    # 🔴 nur ausführen, nicht entscheiden
    decision = context["decision"]

    print(f"[{name}] EXECUTE:", decision)

    return True


def broadcast(signal):

    # 🔴 IAM entscheidet EINMAL
    context = central_iam(signal)

    if not context:
        return None

    tenants = list_tenants()

    results = {}

    for t in tenants:
        try:
            res = execute_for_tenant(t, context)
            results[t] = res
        except Exception as e:
            results[t] = str(e)

    return results
