def detect(input_data):

    if isinstance(input_data, str):

        # 🔴 Python erkennen
        if "def " in input_data or "import " in input_data:
            return "PYTHON"

        # 🔴 typische Bash Fehler
        if "syntax error near unexpected token" in input_data:
            return "BASH_ERROR"

        # 🔴 normaler Text
        return "TEXT"

    return "UNKNOWN"
