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
