#!/bin/bash

STATE_FILE="/opt/aicore/signal_state.log"
LAST_COUNT=0

echo "=== SIGNAL LOOP START ==="

while true
do
    echo ""
    echo "--- NEW IMPULSE ---"

    # VERTICAL READ (Existenz)
    DIR_COUNT=$(find / -type d 2>/dev/null | wc -l)
    FILE_COUNT=$(find / -type f 2>/dev/null | wc -l)

    echo "DIRS: $DIR_COUNT"
    echo "FILES: $FILE_COUNT"

    # Vergleich mit vorherigem Impuls
    if [ "$DIR_COUNT" -eq "$LAST_COUNT" ]; then
        echo "VERTICAL_STOP detected"
        echo "STATE: COMPLETE_VERTICAL" >> $STATE_FILE
        break
    else
        echo "STATE: GROWING_VERTICAL" >> $STATE_FILE
    fi

    LAST_COUNT=$DIR_COUNT

    # WAIT FOR OK (dein Impuls!)
    echo ""
    echo "WAITING FOR OK..."
    read OK

    if [ "$OK" != "ok" ]; then
        echo "NO OK → LOOP PAUSED"
        exit 0
    fi

done

# HORIZONTAL SIGNAL (automatisch nach STOP)
echo ""
echo "=== HORIZONTAL SIGNAL TRIGGERED ==="

echo "READING CONTENT SAMPLE..."

find /opt/aicore -type f 2>/dev/null | head -n 20 > /opt/aicore/content_sample.log

echo "STATE: HORIZONTAL_ACTIVE" >> $STATE_FILE

# IAM CHECK (minimal, nur Signal)
echo ""
echo "=== IAM CHECK ==="
echo "New signal detected → review required"

echo "=== LOOP END ==="
