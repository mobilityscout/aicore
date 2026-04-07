import os, json, time
from core.context import get_root

class Storage:

    def __init__(self):
        self.base = get_root()
        self.run_id = str(int(time.time()))
        self.run_path = f"{self.base}/storage/signals/run_{self.run_id}"

        os.makedirs(self.run_path, exist_ok=True)

    def _layer_file(self, layer):
        return f"{self.run_path}/{layer}.log"

    def write(self, layer, signal, payload=None):
        entry = {
            "time": time.time(),
            "layer": layer,
            "signal": signal,
            "payload": payload or {},
            "status": "OK"
        }

        path = self._layer_file(layer)

        with open(path, "a") as f:
            f.write(json.dumps(entry) + "\n")

        return entry

    def snapshot(self):
        data = []

        if not os.path.exists(self.run_path):
            return []

        for file in sorted(os.listdir(self.run_path)):
            if not file.endswith(".log"):
                continue

            layer = file.replace(".log", "")
            full = os.path.join(self.run_path, file)

            for line in open(full):
                try:
                    e = json.loads(line)
                    data.append(e)
                except:
                    pass

        return data
