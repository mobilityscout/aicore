from core.library import write, find

def decide(signal):

    # 🔥 reuse first
    known = find(signal)

    if known:
        return known

    # 🔥 minimal logic
    actions = []

    for k, v in signal.items():
        if v == 404:
            actions.append(f"BUILD_{k.upper()}")

    # speichern (Knowledge!)
    write({
        "signal": signal,
        "action": actions
    })

    return actions
