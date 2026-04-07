import os
import shutil
import time

BASE = "/opt/aicore/versions"


def snapshot(tenant):

    ts = int(time.time())
    path = f"{BASE}/{tenant}/{ts}"

    src = f"/opt/aicore/tenants/{tenant}"

    os.makedirs(path, exist_ok=True)

    shutil.copytree(src, path + "/data")

    print("VERSION SAVED:", path)

    return path
