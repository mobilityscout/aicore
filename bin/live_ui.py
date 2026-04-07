from flask import Flask, jsonify
from core.index_engine import load_index
from core.tenant_orchestrator import list_tenants
from core.iam_state import get as iam_get

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "system": "AICORE",
        "status": "RUNNING"
    }


@app.route("/index")
def index():
    data = load_index()
    return jsonify(data[:50])


@app.route("/tenants")
def tenants():
    return jsonify(list_tenants())


@app.route("/iam")
def iam():
    return jsonify(iam_get())


@app.route("/health")
def health():
    return {
        "status": "OK"
    }


@app.route("/state")
def state():
    data = load_index()
    states = [d for d in data if d.get("type") == "state"]
    return jsonify(states[:50])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50000)

@app.route('/state')
def state(): return {'state':'ok'}
