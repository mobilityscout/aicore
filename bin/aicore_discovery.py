import time
from core.scanner import scan
from core.order import build_structure
from core.readiness import analyze

BASE = "/opt/aicore/tenants/ms24/ai-platform/storage"

print("DISCOVERY START")

while True:

    items = scan(BASE)
    structure = build_structure(items)
    state = analyze(structure)

    print("STATE:", state)

    time.sleep(5)
