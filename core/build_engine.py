from core.code_validator import validate
from core.code_staging import store

def execute(steps):

    print("\n=== BUILD ENGINE (SAFE MODE) ===")

    for step in steps:

        if step["action"] == "BUILD_MODULE":

            code = step.get("code")

            if not code:
                print("NO CODE")
                continue

            result = validate(code["content"])

            if not result["valid"]:
                print("INVALID:", result["error"])
                continue

            store(code)

            print("STAGED:", code["name"])
