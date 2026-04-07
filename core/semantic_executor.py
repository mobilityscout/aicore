from core.tenant_router import route
from core.sot_storage import store


def execute(semantic):

    intent = semantic.get("intent")
    target = semantic.get("target")
    tenant = semantic.get("tenant")

    if not intent or not target:
        return False

    route(target)

    store({
        "tenant": tenant,
        "intent": intent,
        "target": target,
        "status": "EXECUTED"
    })

    return True
