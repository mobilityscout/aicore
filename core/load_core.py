import os

def get_load():

    try:
        mem = int(os.popen("free -m | awk '/Mem:/ {print $3}'").read())
    except:
        mem = 0

    return mem


def decide_mode(mem):

    if mem < 100:
        return "STOP"

    elif mem < 500:
        return "SLOW"

    else:
        return "FULL"
