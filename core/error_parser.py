import re


def parse(error):

    text = str(error)

    # 🔴 FALL 1: Missing Function
    m = re.search(r"cannot import name '(.+?)' from '(.+?)'", text)
    if m:
        return {
            "type": "MISSING_FUNCTION",
            "function": m.group(1),
            "module": m.group(2).split(".")[-1]
        }

    # 🔴 FALL 2: Missing Module (mit oder ohne Quotes)
    m = re.search(r"No module named ['\"]?(.+?)['\"]?$", text)
    if m:
        return {
            "type": "MISSING_MODULE",
            "module": m.group(1)
        }

    # 🔴 FALL 3: Syntax Error
    if "syntax error" in text.lower():
        return {
            "type": "SYNTAX_ERROR",
            "error": text
        }

    return {
        "type": "UNKNOWN",
        "raw": text
    }
