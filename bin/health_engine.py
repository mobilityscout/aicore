import os, json, time

DB = "/opt/aicore/db/health.log"

def run():

    dirs = int(os.popen("find / -type d 2>/dev/null | wc -l").read())
    files = int(os.popen("find / -type f 2>/dev/null | wc -l").read())

    state = "OK"

    entry = {
        "t": time.time(),
        "dirs": dirs,
        "files": files,
        "state": state
    }

    with open(DB, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return entry
