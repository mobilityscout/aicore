from flask import Flask, jsonify
import traceback

from core.engine import run

app = Flask(__name__)

@app.route("/health")
def health():

    try:
        result = run()

    except Exception as e:

        # 🔥 LAW ENFORCEMENT
        result = {
            "state": "ERROR",
            "signal": {
                "exception": str(e)
            },
            "trace": traceback.format_exc()
        }

    return jsonify(result)

@app.route("/tasks")
def tasks():
    return jsonify({}, 404)

@app.route("/data")
def data():
    return jsonify({}, 404)


@app.route("/state")
def state():
    return {"state": "ok"}, 200

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=50000)

@app.route('/state')
    from core.iam_state import get as iam_get
    data = iam_get()
    return data
    from core.iam_state import get as iam_get
    data = iam_get()
    return data
def state(): return {'state':'ok'}

@app.route('/state')
    from core.iam_state import get as iam_get
    data = iam_get()
    return data
    from core.iam_state import get as iam_get
    data = iam_get()
    return data
def state(): return {'state':'ok'}

@app.route('/state')
    from core.iam_state import get as iam_get
    data = iam_get()
    return data
    from core.iam_state import get as iam_get
    data = iam_get()
    return data
def state(): return {'state':'ok'}

from core.rule_validation import get_pending, validate_rule


@app.route('/rules')
def rules():
    return {"pending": get_pending()}


@app.route('/rules/validate/<int:rid>')
def validate(rid):
    ok = validate_rule(rid)
    return {"validated": ok}

@app.route('/state')
def state(): return {'state':'ok'}

@app.route('/state')
def state(): return {'state':'ok'}
