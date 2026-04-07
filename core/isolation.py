def enforce(tenant, path):

    # 🔴 darf nur im eigenen Tenant arbeiten
    if f"/tenants/{tenant}/" not in path:
        raise Exception(f"ACCESS DENIED: {path}")

    return True
