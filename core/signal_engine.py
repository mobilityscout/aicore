import time
from core.health_core import run

def loop():

    last_state = None
    stable_count = 0

    while True:

        result = run()
        state = result.get("system_state")

        print("STATE:", state)

        # --- STABILITÄT ERKENNEN ---
        if state == last_state:
            stable_count += 1
        else:
            stable_count = 0

        last_state = state

        # --- STOP BEDINGUNG ---
        if stable_count >= 3:
            print("=== SIGNAL STABLE → STOP ===")
            break

        # --- BRÜCKE = weiterlaufen ---
        time.sleep(2)
