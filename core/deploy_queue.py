import json
import os

STAGING = "/opt/aicore/code_staging.json"

def load():
    if not os.path.exists(STAGING):
        return []
    with open(STAGING, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def clear():
    if os.path.exists(STAGING):
        os.remove(STAGING)
