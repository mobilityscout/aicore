import ast
import shutil
import os

BASELINE = "/opt/aicore/baseline"


def check_syntax(file_path):

    try:
        with open(file_path, "r") as f:
            source = f.read()

        ast.parse(source)
        return True

    except Exception as e:
        print("CODE GUARD: SYNTAX ERROR →", e)
        return False


def restore(file_path):

    name = os.path.basename(file_path)
    backup = BASELINE + "/" + name

    if os.path.exists(backup):
        shutil.copy(backup, file_path)
        print("CODE GUARD: RESTORED FROM BASELINE →", name)
        return True

    print("CODE GUARD: NO BASELINE FOUND")
    return False


def protect(file_path):

    if not check_syntax(file_path):
        return restore(file_path)

    return True
