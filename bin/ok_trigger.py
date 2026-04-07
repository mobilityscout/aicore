import json, os, time

BASE = "/opt/aicore/tenants/ms24/ai-platform/storage"
STATE = BASE + "/DISCOVERY_STATE.json"
OKLOG = BASE + "/OK.log"

def load():
    if not os.path.exists(STATE):
        return None
    return json.load(open(STATE))

def log(s):
    with open(OKLOG,"a") as f:
        f.write(json.dumps({"time":time.time(),"state":s})+"\n")

s = load()

if s:
    log(s)
    print("OK STORED:", s)
else:
    print("NO STATE")
