import os, json, time, hashlib
from core.context import get_root

IAM_LIMITS = {
    "node_A": 200 * 1024 * 1024 * 1024,  # 200GB
    "node_B": 50 * 1024 * 1024 * 1024
}

class SnapshotEngine:

    def __init__(self):
        self.base = get_root()
        self.snapshot_path = f"{self.base}/storage/snapshots"
        os.makedirs(self.snapshot_path, exist_ok=True)

    def validate_size(self, sender, size):
        limit = IAM_LIMITS.get(sender, 10 * 1024 * 1024 * 1024)

        if size > limit:
            raise Exception(f"IAM LIMIT EXCEEDED: {size} > {limit}")

        return True

    def create_snapshot(self, meta):
        raw = json.dumps(meta)
        h = hashlib.sha256(raw.encode()).hexdigest()

        snapshot = {
            "id": h,
            "time": time.time(),
            "sender": meta["sender"],
            "size": meta["size"],
            "status": "COMPLETE"
        }

        path = f"{self.snapshot_path}/{h}.snap"

        with open(path, "w") as f:
            f.write(json.dumps(snapshot))

        return snapshot

    def verify_complete(self, snapshot):
        if snapshot["status"] != "COMPLETE":
            raise Exception("INCOMPLETE SIGNAL")

        return True
