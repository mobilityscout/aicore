REGISTRY = {}

def register(name, path):

    REGISTRY[name] = path

    print("REGISTERED:", name)


def get(name):
    return REGISTRY.get(name)
