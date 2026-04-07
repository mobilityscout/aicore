import shutil
import os


def deploy(tenant, sandbox):

    print("\n=== DEPLOY ENGINE ===")

    src = sandbox + "/systems"
    dst = f"/opt/aicore/tenants/{tenant}/systems"

    if os.path.exists(dst):
        shutil.rmtree(dst)

    shutil.copytree(src, dst)

    print("DEPLOYED")
    return True
