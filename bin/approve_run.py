import sys, json

run = sys.argv[1]
path = f"/opt/aicore/tenants/ms24/ai-platform/storage/signals/{run}/STATE.json"

data = json.load(open(path))
data["action"] = "CONTINUE"

json.dump(data, open(path,"w"))

print("APPROVED:", run)
