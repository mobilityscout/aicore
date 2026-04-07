import json

LAW_PATH = "/opt/aicore/library/law.json"

def load_law():
    return json.load(open(LAW_PATH))

def boot_signal():

    law = load_law()

    if not law:
        raise Exception("SYSTEM CANNOT START WITHOUT LAW")

    return {
        "law": law,
        "phase": "ISOLATION",
        "state": "BOOTING"
    }
