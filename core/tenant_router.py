from core.tenant_context import get_tenant
from core.expansion_engine import expand


def route(system):

    tenant = get_tenant()

    print(f"\n=== TENANT ROUTE → {tenant} ===")

    # 🔴 tenant-spezifischer Pfad
    target = f"{tenant}_{system}"

    expand([system])

    return True
