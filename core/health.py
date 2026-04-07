from core.memory import find_long, write_long
import time

def decide(signal, error):

    known = find_long(signal)

    if not error:
        if not known:
            write_long({
                "t": time.time(),
                "signal": signal,
                "type": "STATE",
                "status": "STABLE"
            })
        return "STABLE"

    if known:
        return "KNOWN_ERROR"

    write_long({
        "t": time.time(),
        "signal": signal,
        "type": "ERROR",
        "status": "NEW"
    })

    return "UNKNOWN_ERROR"
