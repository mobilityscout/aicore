import os, time, shutil

BASE = "/opt/aicore"
SNAP = BASE + "/snapshots"

def ensure():
    os.makedirs(SNAP, exist_ok=True)

def create(label="auto"):

    ensure()

    ts = str(int(time.time()))
    path = SNAP + "/" + ts + "_" + label

    os.makedirs(path, exist_ok=True)

    # relevante Bereiche sichern
    paths = [
        "/opt/aicore/library",
        "/opt/aicore/db"
    ]

    for p in paths:
        if os.path.exists(p):
            name = os.path.basename(p)
            shutil.copytree(p, path + "/" + name, dirs_exist_ok=True)

    return path


def restore(snapshot_path):

    for name in ["library", "db"]:
        src = snapshot_path + "/" + name
        dst = "/opt/aicore/" + name

        if os.path.exists(src):
            shutil.rmtree(dst, ignore_errors=True)
            shutil.copytree(src, dst)

    return "RESTORED"
