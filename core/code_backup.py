import shutil
import os

TARGET = "/opt/aicore/bin/live_ui.py"
BACKUP = "/opt/aicore/backup/live_ui.py"


def update_backup():

    if os.path.exists(TARGET):
        shutil.copy(TARGET, BACKUP)
        print("BACKUP UPDATED")
