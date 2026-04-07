import subprocess


def check_ui():

    try:
        result = subprocess.run(
            ["python3", "/opt/aicore/bin/live_ui.py"],
            capture_output=True,
            text=True,
            timeout=3
        )

        if result.returncode != 0:

            err = result.stderr.lower()

            if "indentationerror" in err or "syntaxerror" in err:
                return "error: syntax in live_ui.py"

            if "importerror" in err:
                return "error: import in live_ui.py"

            return f"error: ui failed {err}"

        return None

    except Exception as e:
        return f"error: ui exception {str(e)}"


def run():

    err = check_ui()

    if err:
        return err

    return None
