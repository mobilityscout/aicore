import os

def write(path, content):

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        f.write(content)

    print("WRITTEN:", path)

    return True
