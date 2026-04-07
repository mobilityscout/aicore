from core.tenant_context import get_tenant


def enrich(semantic):

    tenant = get_tenant()

    semantic["tenant"] = tenant

    # 🔴 später: State, History, SoT etc.
    semantic["context"] = {
        "tenant": tenant
    }

    return semantic
