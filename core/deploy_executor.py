from core.write_system import write
from core.integration_engine import integrate

BASE = "/opt/aicore/core/"

def deploy(entry):

    name = entry.get("name")
    code = entry.get("content")

    file_path = BASE + name + ".py"
    module_path = "core." + name

    write(file_path, code)
    integrate(name, module_path)

    print("DEPLOYED:", name)
