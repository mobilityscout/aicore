#!/bin/bash

echo "=== IAM BOOTSTRAP START ==="

# SNAPSHOT VORHER
python3 - << 'PY'
from core.snapshot_core import create
p = create("before_boot")
print("SNAPSHOT BEFORE:", p)
PY

# IAM VALIDATION + REPAIR
python3 - << 'PY'
from core.iam_validator import validate

result = validate()

print("IAM STATUS:", result["status"])

if result["status"] == "BROKEN":
    print("SYSTEM NOT RECOVERABLE → STOP")
    exit(1)

if result["status"] == "RECOVERED":
    print("SYSTEM REPAIRED")

PY

# SNAPSHOT NACH REPAIR
python3 - << 'PY'
from core.snapshot_core import create
p = create("after_repair")
print("SNAPSHOT AFTER:", p)
PY

# CLEAN
rm -f /opt/aicore/db/*.tmp 2>/dev/null || true

# KILL
pkill -f live_ui.py || true

# START
python3 /opt/aicore/bin/live_ui.py & disown

echo "=== SYSTEM STARTED CLEAN ==="
