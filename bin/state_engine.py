import os, json, time

DB = "/opt/aicore/db/state.db.json"

def load():
    with open(DB) as f:
        return json.load(f)

def save(data):
    with open(DB, "w") as f:
        json.dump(data, f, indent=2)

def compute():
    data = load()

    dir_count = int(os.popen("find / -type d 2>/dev/null | wc -l").read())
    file_count = int(os.popen("find / -type f 2>/dev/null | wc -l").read())

    last_dir = data.get("last_dir", 0)

    if dir_count > last_dir:
        state = "VERTICAL_GROWING"
    else:
        state = "VERTICAL_STOP"

    data["last_dir"] = dir_count
    data["last_file"] = file_count
    data["state"] = state

    data["history"].append({
        "t": time.time(),
        "dirs": dir_count,
        "files": file_count,
        "state": state
    })

    save(data)

    return {
        "dirs": dir_count,
        "files": file_count,
        "state": state
    }
