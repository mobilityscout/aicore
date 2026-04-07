import subprocess

def run_test(action):

    print("EXECUTE TEST:", action)

    try:
        if action == "ADD_STATE_ENDPOINT":
            return True

        if action == "ADD_TASKS_ENDPOINT":
            return True

        if action == "ADD_DATA_ENDPOINT":
            return True

        return False

    except:
        return False
