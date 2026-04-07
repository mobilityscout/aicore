import os

def scan(base):

    found = []

    for root, dirs, files in os.walk(base):
        for d in dirs:
            found.append({"type":"dir","path":os.path.join(root,d)})
        for f in files:
            found.append({"type":"file","path":os.path.join(root,f)})

    return found
