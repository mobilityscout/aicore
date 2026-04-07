def is_stable(signal):

    return all(v == 200 for v in signal.values())
