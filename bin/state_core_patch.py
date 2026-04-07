import os

LAST_FILE = "/opt/aicore/last_state.tmp"

def get_dynamic_state():
    dir_count = int(os.popen("find / -type d 2>/dev/null | wc -l").read())
    file_count = int(os.popen("find / -type f 2>/dev/null | wc -l").read())

    if os.path.exists(LAST_FILE):
        with open(LAST_FILE) as f:
            last_dir = int(f.read().strip())
    else:
        last_dir = 0

    if dir_count > last_dir:
        state = "VERTICAL_GROWING"
    else:
        state = "VERTICAL_STOP"

    with open(LAST_FILE, "w") as f:
        f.write(str(dir_count))

    return {
        "dirs": dir_count,
        "files": file_count,
        "state": state
    }
