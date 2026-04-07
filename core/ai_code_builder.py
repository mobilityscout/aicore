def build(module):

    if module == "learning_memory":

        return {
            "name": "learning_memory",
            "path": "core.learning_memory",
            "file": "/opt/aicore/core/learning_memory.py",
            "content": """import json
import os

FILE = "/opt/aicore/ai_learning.json"

def store(entry):

    data = []

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append(entry)

    with open(FILE, "w") as f:
        json.dump(data, f)
"""
        }

    return None
