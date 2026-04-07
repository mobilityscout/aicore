import os

UI_PATH = "/opt/aicore/ui.html"


def exists():
    return os.path.exists(UI_PATH)


def validate():

    if not exists():
        return False, "MISSING"

    with open(UI_PATH, "r") as f:
        content = f.read()

    if "<html>" not in content or "</html>" not in content:
        return False, "CORRUPTED"

    if "fetch(" not in content:
        return False, "NO_API_LINK"

    return True, "OK"


def build():

    content = """<html>
<head><title>AI Worker</title></head>
<body>
<h2>AI Worker</h2>

<input id="input" placeholder="baue ui"/>
<button onclick="send()">Send</button>

<pre id="out"></pre>

<script>
async function send(){
    let val = document.getElementById("input").value;

    let res = await fetch("/process", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({
            token: "TEST",
            tenant: "tenant_1",
            role: "admin",
            signal: val
        })
    });

    let data = await res.json();

    document.getElementById("out").innerText =
        JSON.stringify(data, null, 2);
}
</script>

</body>
</html>
"""

    with open(UI_PATH, "w") as f:
        f.write(content)

    print("UI REBUILT")
