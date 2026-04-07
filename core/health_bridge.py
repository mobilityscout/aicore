import time
from core.orchestrator import run

LAST = 0

def health_ping():

    global LAST
    now = time.time()

    # Rate Limit (wichtig!)
    if now - LAST < 5:
        return

    LAST = now

    run("HEALTH_PING")
