def block(path):

    forbidden = [
        "/opt/aicore/core",
        "/opt/aicore/sot"
    ]

    for f in forbidden:
        if path.startswith(f):
            raise Exception("CORE ACCESS BLOCKED")

    return True
