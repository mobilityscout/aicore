import os, time
from core.memory import init, save_state
from core.tasks import load, step

BASE = "/opt/aicore/tenants/ms24/ai-platform/storage"
OKFILE = BASE + "/OK.signal"

init()

def scan():
    dirs, files = 0,0
    for r,d,f in os.walk(BASE):
        dirs += len(d)
        files += len(f)
    return dirs, files

def check_ok():
    if os.path.exists(OKFILE):
        os.remove(OKFILE)
        return True
    return False

progress = 0

while True:

    dirs, files = scan()

    state = {
        "dirs": dirs,
        "files": files,
        "progress": progress
    }

    if check_ok():
        progress += 1

        # echte Arbeitsschritte
        if progress == 1: step("SCAN_STRUCTURE")
        elif progress == 2: step("ORDER_DATA")
        elif progress == 3: step("BUILD_INDEX")
        elif progress == 4: step("LINK_SIGNALS")
        elif progress == 5: step("READY_FOR_CHAT")

        os.makedirs(BASE + "/growth_" + str(progress), exist_ok=True)

    save_state(state)

    time.sleep(2)
