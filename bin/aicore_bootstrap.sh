#!/bin/bash
set -e

BASE="/opt/aicore"
CORE="$BASE/core"
DB="$BASE/db"
BIN="$BASE/bin"

mkdir -p $CORE $DB $BIN

########################################
# LAW (immutable)
########################################
cat << 'PY' > $CORE/law.py
LAW = [
    "VERTICAL",
    "HORIZONTAL",
    "EVALUATE",
    "DECIDE",
    "ACT",
    "STORE"
]
PY

########################################
# STATE (single source of truth)
########################################
cat << 'PY' > $CORE/state.py
import json, os, time

DB = "/opt/aicore/db/state.json"

def load():
    if not os.path.exists(DB):
        return {
            "layer": 0,
            "history": [],
            "last_ok": None
        }
    return json.load(open(DB))

def save(s):
    s["t"] = time.time()
    json.dump(s, open(DB, "w"), indent=2)
PY

########################################
# IAM (entscheidet + load control)
########################################
cat << 'PY' > $CORE/iam.py
import os

def mem():
    try:
        return int(os.popen("free -m | awk '/Mem:/ {print $3}'").read())
    except:
        return 0

def decide(signal):

    m = mem()

    # --- RESOURCE LAW ---
    if m < 100:
        mode = "STOP"
    elif m < 500:
        mode = "SLOW"
    else:
        mode = "FULL"

    # --- DECISION ---
    actions = []

    if signal.get("tasks") == 404:
        actions.append("BUILD_TASKS")

    if signal.get("data") == 404:
        actions.append("BUILD_DATA")

    decision = "REPAIR" if actions else "OK"

    return {
        "mode": mode,
        "decision": decision,
        "actions": actions,
        "mem": m
    }
PY

########################################
# GUARD (führt aus + validiert)
########################################
cat << 'PY' > $CORE/guard.py
import requests

def act(actions):

    result = {}

    for a in actions:

        if a == "BUILD_TASKS":
            result["tasks_build"] = True

        if a == "BUILD_DATA":
            result["data_build"] = True

    # --- VALIDATION ---
    try:
        r = requests.get("http://127.0.0.1:50000/tasks", timeout=1)
        result["tasks_status"] = r.status_code
    except:
        result["tasks_status"] = 404

    try:
        r = requests.get("http://127.0.0.1:50000/data", timeout=1)
        result["data_status"] = r.status_code
    except:
        result["data_status"] = 404

    return result
PY

########################################
# ENGINE (einzige Ausführungseinheit)
########################################
cat << 'PY' > $CORE/engine.py
import requests, time, json, os
from core.state import load, save
from core.iam import decide
from core.guard import act

LOG = "/opt/aicore/db/worklog.jsonl"

def log(entry):
    with open(LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")

def vertical():
    return {}

def horizontal():
    signal = {}

    try:
        r = requests.get("http://127.0.0.1:50000/tasks", timeout=1)
        signal["tasks"] = r.status_code
    except:
        signal["tasks"] = 404

    try:
        r = requests.get("http://127.0.0.1:50000/data", timeout=1)
        signal["data"] = r.status_code
    except:
        signal["data"] = 404

    return signal

def run():

    s = load()

    # VERTICAL
    signal = vertical()

    # HORIZONTAL
    signal.update(horizontal())

    # EVALUATE + DECIDE
    iam = decide(signal)

    # ACT
    results = {}
    if iam["mode"] != "STOP":
        results = act(iam["actions"])

    # STORE
    s["layer"] += 1
    s["history"].append({
        "signal": signal,
        "iam": iam,
        "results": results
    })

    if iam["decision"] == "OK":
        s["last_ok"] = s["layer"]

    save(s)

    entry = {
        "layer": s["layer"],
        "signal": signal,
        "iam": iam,
        "results": results
    }

    log(entry)

    return entry
PY

########################################
# LIVE UI (nur Anzeige, keine Logik)
########################################
cat << 'PY' > $BIN/live_ui.py
from flask import Flask, jsonify
from core.engine import run

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(run())

@app.route("/tasks")
def tasks():
    return jsonify({}, 404)

@app.route("/data")
def data():
    return jsonify({}, 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50000)
PY

########################################
# START
########################################
pkill -9 -f live_ui.py || true
python3 $BIN/live_ui.py & disown

echo "=== AICORE ENGINE ACTIVE ==="
