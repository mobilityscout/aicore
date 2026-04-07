MODE = "auto"  # auto | manual | hybrid


def set_mode(m):
    global MODE
    MODE = m


def get_mode():
    return MODE
