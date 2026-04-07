import os
from core.context import get_root

class OrderEngine:

    def __init__(self):
        self.base = get_root()
        self.signal_root = f"{self.base}/storage/signals"

        os.makedirs(self.signal_root, exist_ok=True)

    def discover_runs(self):
        return sorted(os.listdir(self.signal_root)) if os.path.exists(self.signal_root) else []

    def resolve_run_path(self, run_id):
        return f"{self.signal_root}/run_{run_id}"

    def ensure_structure(self, run_path):
        os.makedirs(run_path, exist_ok=True)

        required = ["L0.log","L1.log","L2.log","L3.log","L4.log","L5.log"]

        for r in required:
            p = f"{run_path}/{r}"
            if not os.path.exists(p):
                open(p,"a").close()

        struct = f"{run_path}/structure"
        os.makedirs(struct, exist_ok=True)

        for col in ["time","layer","signal","status","payload"]:
            open(f"{struct}/{col}.col","a").close()

    def locate_latest_valid(self):
        runs = self.discover_runs()

        for r in reversed(runs):
            path = f"{self.signal_root}/{r}"
            if os.path.exists(f"{path}/L0.log"):
                return path

        return None
