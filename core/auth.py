import uuid

TOKENS = {}


def create(tenant):

    token = str(uuid.uuid4())

    TOKENS[token] = tenant

    return token


def verify(token):

    if token not in TOKENS:
        raise Exception("INVALID TOKEN")

    return TOKENS[token]
