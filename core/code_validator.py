import ast

def validate(code):

    try:
        ast.parse(code)
    except Exception as e:
        return {"valid": False, "error": str(e)}

    if "os.system" in code or "subprocess" in code:
        return {"valid": False, "error": "unsafe operation"}

    return {"valid": True}
