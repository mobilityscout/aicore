from core.immune_core import protect

@protect
def run(signal, tenant="default"):

    from core.worker import process

    return process(signal, tenant)
