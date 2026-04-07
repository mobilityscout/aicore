import ast
import os

BASE = "/opt/aicore"


def check_file(path):

    try:
        with open(path, "r") as f:
            content = f.read()

        # 🔴 leer?
        if not content.strip():
            return False, "EMPTY"

        # 🔴 Syntax prüfen
        ast.parse(content)

        return True, "OK"

    except SyntaxError as e:
        return False, f"SYNTAX_ERROR: {e}"

    except Exception as e:
        return False, f"ERROR: {e}"


def scan():

    print("\n=== INTEGRITY GUARD ===")

    issues = []

    for root, _, files in os.walk(BASE):

        for f in files:

            if not f.endswith(".py"):
                continue

            path = os.path.join(root, f)

            ok, reason = check_file(path)

            if not ok:
                print("BROKEN:", path, reason)

                issues.append({
                    "file": path,
                    "reason": reason
                })

    if not issues:
        print("INTEGRITY OK")

    return issues
