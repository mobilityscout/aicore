import os

REQUIRED = ["L0.log","L1.log","L2.log","L3.log","L4.log","L5.log","structure"]

def is_complete(run_path):
    files = os.listdir(run_path)
    return all(r in files for r in REQUIRED)
