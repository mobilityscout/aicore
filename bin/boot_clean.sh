#!/bin/bash

echo "=== IAM CLEAN BOOT ==="

# 🔴 ALLES KILLEN (hart, vollständig)
pkill -9 -f live_ui.py 2>/dev/null || true
pkill -9 -f boot.py 2>/dev/null || true
pkill -9 -f python3 2>/dev/null || true

sleep 1

echo "ALL PROCESSES STOPPED"

# 🔴 PORT CLEAN
fuser -k 50000/tcp 2>/dev/null || true

sleep 1

echo "PORT CLEAN"

# 🔥 EINZIGER STARTPUNKT
echo "START BOOT..."

python3 /opt/aicore/bin/boot.py

