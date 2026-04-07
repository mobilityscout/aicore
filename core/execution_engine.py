import json, os, time, subprocess

DB = "/opt/aicore/db"
LONG = DB + "/long.jsonl"
UI   = "/opt/aicore/bin/live_ui.py"

def load_solutions():

    if not os.path.exists(LONG):
        return []

    solved = []
    for line in open(LONG):
        try:
            e = json.loads(line)
            if e.get("status") == "SOLVED":
                solved.append(e)
        except:
            continue

    return solved

def apply(action):

    code = open(UI).read()

    if action == "ADD_STATE_ENDPOINT" and "@app.route(\"/state\")" not in code:
        code = code.replace("if __name__ == \"__main__\":",
'''
@app.route("/state")
def state():
    return {"state": "ok"}, 200

if __name__ == "__main__":
''')

    if action == "ADD_TASKS_ENDPOINT" and "@app.route(\"/tasks\")" not in code:
        code = code.replace("if __name__ == \"__main__\":",
'''
@app.route("/tasks")
def tasks():
    return {"tasks": "ok"}, 200

if __name__ == "__main__":
''')

    if action == "ADD_DATA_ENDPOINT" and "@app.route(\"/data\")" not in code:
        code = code.replace("if __name__ == \"__main__\":",
'''
@app.route("/data")
def data():
    return {"data": "ok"}, 200

if __name__ == "__main__":
''')

    open(UI, "w").write(code)

def verify():

    import requests

    def check(url):
        try:
            return requests.get(url, timeout=1).status_code
        except:
            return 404

    return {
        "state": check("http://127.0.0.1:50000/state"),
        "tasks": check("http://127.0.0.1:50000/tasks"),
        "data":  check("http://127.0.0.1:50000/data")
    }

def restart():

    os.system("pkill -9 -f live_ui.py || true")
    os.system("python3 /opt/aicore/bin/live_ui.py &")
    time.sleep(1)

def run():

    print("\n=== EXECUTION ENGINE START ===")

    solutions = load_solutions()

    if not solutions:
        print("NO SOLUTIONS FOUND")
        return

    for s in solutions:

        action = s.get("solution")

        print("\nAPPLY:", action)

        apply(action)
        restart()

        result = verify()

        print("VERIFY:", result)

        if all(v == 200 for v in result.values()):

            s["executed"] = True
            s["t_exec"] = time.time()

            print("SUCCESS → SYSTEM UPDATED")

        else:
            print("FAILED → ROLLBACK NEEDED")

    # rewrite LONG clean
    new = []
    for line in open(LONG):
        try:
            e = json.loads(line)
            for s in solutions:
                if e.get("signal") == s.get("signal"):
                    e = s
            new.append(e)
        except:
            continue

    open(LONG, "w").write("\n".join([json.dumps(x) for x in new]) + "\n")

    print("\n=== EXECUTION COMPLETE ===")
