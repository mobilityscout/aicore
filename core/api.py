from flask import Flask, request, jsonify
from core.worker import process

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def handle():

    try:
        data = request.json

        result = process(
            data.get("signal"),
            data.get("tenant", "default"),
            data.get("role", "admin")
        )

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50000)
