TRACE = []

def log_read(step, detail):
    TRACE.append({
        "type": "READ",
        "step": step,
        "detail": detail
    })

def log_write(step, detail):
    TRACE.append({
        "type": "WRITE",
        "step": step,
        "detail": detail
    })

def get_trace():
    return TRACE
