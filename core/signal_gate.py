import os, time, hashlib, json
from core.context import get_root

class SignalGate:

    def __init__(self):
        self.base = get_root()
        self.anchor_path = f"{self.base}/storage/anchors"
        os.makedirs(self.anchor_path, exist_ok=True)

    # ------------------------
    # HEADER VALIDATION
    # ------------------------
    def validate_header(self, meta):
        required = ["sender", "size", "security"]

        for r in required:
            if r not in meta:
                raise Exception(f"HEADER INVALID: missing {r}")

        return True

    # ------------------------
    # SIZE CHECK
    # ------------------------
    def check_size(self, size):
        # nur Logging, kein Limit
        return {
            "size_bytes": size,
            "size_mb": round(size / 1024 / 1024, 2)
        }

    # ------------------------
    # SECURITY CHECK
    # ------------------------
    def verify_security(self, meta):
        # placeholder für echte crypto prüfung
        if len(meta["security"]) < 10:
            raise Exception("SECURITY WEAK")

        return True

    # ------------------------
    # ANCHOR (Pre-Commit)
    # ------------------------
    def create_anchor(self, meta):
        raw = json.dumps(meta) + str(time.time())
        h = hashlib.sha256(raw.encode()).hexdigest()

        entry = {
            "time": time.time(),
            "sender": meta["sender"],
            "size": meta["size"],
            "hash": h
        }

        path = f"{self.anchor_path}/{h}.anchor"

        with open(path, "w") as f:
            f.write(json.dumps(entry))

        return entry

    # ------------------------
    # FULL GATE
    # ------------------------
    def process(self, meta):
        self.validate_header(meta)

        size_info = self.check_size(meta["size"])
        self.verify_security(meta)

        anchor = self.create_anchor(meta)

        return {
            "status": "ACCEPTED",
            "anchor": anchor,
            "size": size_info
        }
