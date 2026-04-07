import shutil
import os

BASE_DIR = "/opt/aicore/baseline"
COUNT_DIR = "/opt/aicore/baseline/.counts"


def ensure_dirs():
    os.makedirs(BASE_DIR, exist_ok=True)
    os.makedirs(COUNT_DIR, exist_ok=True)


def get_name(path):
    return path.split("/")[-1]


def get_counter_file(name):
    return f"{COUNT_DIR}/{name}.cnt"


def get_count(name):
    f = get_counter_file(name)
    if not os.path.exists(f):
        return 0
    return int(open(f).read().strip())


def set_count(name, n):
    with open(get_counter_file(name), "w") as f:
        f.write(str(n))


def increment(name):
    c = get_count(name) + 1
    set_count(name, c)
    return c


def reset(name):
    set_count(name, 0)


def evolve(path):

    ensure_dirs()

    name = get_name(path)
    baseline_path = f"{BASE_DIR}/{name}"

    if not os.path.exists(path):
        return False

    count = increment(name)

    print(f"[{name}] STABILITY:", count)

    if count >= 3:
        shutil.copy(path, baseline_path)
        print(f"[{name}] BASELINE UPDATED")
        reset(name)
        return True

    return False
