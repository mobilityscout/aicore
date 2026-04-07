import os
import shutil
import time

BASE = "/opt/aicore"


def create():

    ts = int(time.time())
    path = f"/opt/aicore/sandbox/{ts}"

    os.makedirs(path, exist_ok=True)

    return path


def copy_system(tenant, sandbox):

    src = f"/opt/aicore/tenants/{tenant}/systems"
    dst = sandbox + "/systems"

    if os.path.exists(src):
        shutil.copytree(src, dst)

    return dst
