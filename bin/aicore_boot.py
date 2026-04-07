import time, sys
from core.pipeline import Pipeline

print("AICORE BOOT START", flush=True)

while True:
    try:
        p = Pipeline()

        res = p.run({
            "sender":"system",
            "security":"secure_token",
            "size":1000
        })

        print("RUN:", res, flush=True)

    except Exception as e:
        print("ERROR:", e, flush=True)

    time.sleep(5)
