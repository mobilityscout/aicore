import socket
import subprocess

PORT = 50000

def check():

    status = {
        "process": False,
        "port": False,
        "local": False
    }

    # 🔴 Prozess prüfen
    try:
        out = subprocess.check_output("ps aux | grep api.py", shell=True).decode()
        if "api.py" in out and "grep" not in out:
            status["process"] = True
    except:
        pass

    # 🔴 Port prüfen
    s = socket.socket()
    try:
        s.connect(("127.0.0.1", PORT))
        status["port"] = True
    except:
        pass
    s.close()

    # 🔴 HTTP prüfen
    try:
        import urllib.request
        res = urllib.request.urlopen(f"http://127.0.0.1:{PORT}/health", timeout=2)
        if res.status == 200:
            status["local"] = True
    except:
        pass

    return status
