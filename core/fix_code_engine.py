import ast
import shutil
import os

TARGET = "/opt/aicore/bin/live_ui.py"
BACKUP = "/opt/aicore/backup/live_ui.py"
BASELINE = "/opt/aicore/baseline/live_ui.py"


def is_valid(code):
    try:
        ast.parse(code)
        return True
    except Exception as e:
        return str(e)


def load(path):
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return f.read()


def save(path, content):
    with open(path, "w") as f:
        f.write(content)


def run(action):

    print("FIX_CODE → SELF HEAL")

    code = load(TARGET)

    if code is None:
        print("TARGET MISSING → RESTORE BASELINE")
        shutil.copy(BASELINE, TARGET)
        return True

    if is_valid(code) is True:
        print("CODE OK")
        return True

    print("BROKEN CODE → TRY BACKUP")

    backup_code = load(BACKUP)

    if backup_code and is_valid(backup_code) is True:
        save(TARGET, backup_code)
        print("BACKUP RESTORED")
        return True

    print("BACKUP FAILED → RESTORE BASELINE")

    if os.path.exists(BASELINE):
        shutil.copy(BASELINE, TARGET)
        print("BASELINE RESTORED")
        return True

    print("NO BASELINE → FAIL")
    return False
