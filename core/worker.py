from core.entrypoint import run
from core.execution_context import detect


def process(input_data, tenant="default", role="tenant"):

    print("\n=== WORKER ===")

    context = detect(input_data)

    print("CONTEXT:", context)

    # 🔴 FALL: Bash Fehler erkannt
    if context == "BASH_ERROR":
        return {
            "status": "error",
            "message": "Du hast Python-Code im Bash ausgeführt"
        }

    # 🔴 FALL: Python Code
    if context == "PYTHON":
        return {
            "status": "info",
            "message": "Python Code erkannt – wird nicht direkt ausgeführt"
        }

    # 🔴 normaler Flow
    return run(input_data, tenant)
