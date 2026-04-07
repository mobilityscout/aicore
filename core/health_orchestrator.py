import time
from core.memory import read_short, find_solution, write_long

def run():

    data = read_short()
    if not data:
        print("NO SIGNAL")
        return

    signal = data.get("signal")

    print("\n=== HEALTH ORCHESTRATION START ===")

    error = None
    for k,v in signal.items():
        if v != 200:
            error = k
            break

    if not error:
        print("NO ERROR → HEALTH STOP")
        return

    print("ERROR:", error)

    solution = find_solution(signal)

    if solution:
        print("SOLVED PATTERN FOUND")
        print("→ ACTION:", solution)
        return

    print("NO SOLUTION AVAILABLE")

    cause = {
        "endpoint_missing": error,
        "code": signal[error]
    }

    print("CAUSE:", cause)

    decision = "RESEARCH"
    print("DECISION:", decision)

    write_long({
        "t": time.time(),
        "signal": signal,
        "analysis": cause,
        "status": "NEW"
    })

    print("STORED AS NEW CASE")
    print("\n=== HEALTH WAIT ===")
