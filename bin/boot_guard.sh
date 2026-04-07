#!/bin/bash

CORE_URL="http://127.0.0.1:50000/health"
UI_PORT=50505

echo "=== BOOT GUARD START ==="

# --- CORE CHECK ---
while true
do
    STATUS=$(curl -s $CORE_URL | grep -c "ok")

    if [ "$STATUS" -gt 0 ]; then
        echo "CORE HEALTH OK"
        break
    fi

    echo "CORE NOT READY → REPAIR"

    pkill -f live_ui.py || true
    sleep 1
    python3 /opt/aicore/bin/live_ui.py &

    sleep 2
done

echo "=== CORE STABLE ==="

# --- UI CHECK ---
UI_RUNNING=$(ss -tulnp | grep -c $UI_PORT)

if [ "$UI_RUNNING" -gt 0 ]; then
    echo "UI already running → OK"
else
    echo "UI not running → START"

    cd /opt/aicore/ui
    python3 -m http.server $UI_PORT &
fi

echo "=== SYSTEM READY ==="
