from core.semantic_core import interpret
from core.semantic_executor import execute
from core.sot_storage import store


def process(signal, tenant):

    semantic = interpret(signal)

    semantic["tenant"] = tenant

    # 🔴 Entscheidung zentral
    result = execute(semantic)

    store({
        "tenant": tenant,
        "signal": signal,
        "result": result
    })

    return result
