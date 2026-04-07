import subprocess

def run(action):

    print("FIX EXECUTE:", action["type"])

    if action["type"] == "ADD_ENDPOINT":
        return add_endpoint(action)

    if action["type"] == "INSTALL_PACKAGE":
        return install_package(action)

    return False


def add_endpoint(action):
    try:
        # Beispiel: Flask Endpoint einfügen
        file = action.get("file", "/opt/aicore/bin/live_ui.py")

        code = "\n@app.route('/state')\ndef state(): return {'state':'ok'}\n"

        with open(file, "a") as f:
            f.write(code)

        return True

    except:
        return False


def install_package(action):
    try:
        pkg = action.get("name")
        subprocess.run(["pip3", "install", pkg])
        return True
    except:
        return False
