import shutil
import os
import time

BASE = "/opt/aicore"


def create(target):

    ts = int(time.time())
    backup = f"/opt/aicore/snapshots/{ts}"

    os.makedirs(backup, exist_ok=True)

    if os.path.exists(target):
        shutil.copytree(target, backup + "/data")

    print("SNAPSHOT:", backup)

    return backup


def restore(snapshot, target):

    path = snapshot + "/data"

    if os.path.exists(target):
        shutil.rmtree(target)

    shutil.copytree(path, target)

    print("ROLLBACK DONE")
