import time, os
from core.context import get_root
from core.version_engine import write_version, load_state
from core.forward_builder import rebuild_chain

LAYERS = ["L0","L1","L2","L3","L4","L5"]

class Pipeline:

    def __init__(self):
        self.base = get_root()
        self.run_id = "run_main"
        self.run_path = f"{self.base}/storage/signals/{self.run_id}"
        os.makedirs(self.run_path, exist_ok=True)

    def run(self, meta):

        for i, l in enumerate(LAYERS):

            # vorheriger Layer muss FINAL sein
            if i > 0:
                prev = LAYERS[i-1]
                ps = load_state(self.run_path, prev)
                if ps["status"] != "FINAL":
                    return self._error(f"{prev} not FINAL")

            data = {"layer": l, "input": meta}

            write_version(self.run_path, l, data, "BUILT")

            # Fehler trigger (Test)
            if meta.get("force_error") == l:
                write_version(self.run_path, l, {"error":"forced"}, "FIX")
                return self._error(f"ERROR in {l}")

            write_version(self.run_path, l, data, "FINAL")

        return {"run": self.run_id, "status": "COMPLETE"}

    def _error(self, msg):
        fix = rebuild_chain(self.run_path)
        return {"status":"ERROR","msg":msg,"fix":fix}
