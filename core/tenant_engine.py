import os
import shutil

CORE = "/opt/aicore/core_baseline"
TENANTS = "/opt/aicore/tenants"


def ensure_tenant(name):

    base = f"{TENANTS}/{name}"
    os.makedirs(base, exist_ok=True)
    os.makedirs(f"{base}/overlay", exist_ok=True)
    os.makedirs(f"{base}/runtime", exist_ok=True)
    os.makedirs(f"{base}/backup", exist_ok=True)

    return base


def build_runtime(name):

    base = ensure_tenant(name)

    runtime = f"{base}/runtime"

    # 🔴 CORE → Runtime kopieren
    for f in os.listdir(CORE):
        shutil.copy(f"{CORE}/{f}", f"{runtime}/{f}")

    # 🔴 Overlay überschreibt Core
    overlay = f"{base}/overlay"

    for f in os.listdir(overlay):
        shutil.copy(f"{overlay}/{f}", f"{runtime}/{f}")

    print(f"[{name}] RUNTIME BUILT")
    return runtime
