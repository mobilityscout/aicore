import requests

CORE_API = "http://127.0.0.1:5000/process"

def send(signal):
    return requests.post(CORE_API, json={
        "tenant": "tenant_1",
        "signal": signal
    }).json()
