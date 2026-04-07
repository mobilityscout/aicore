from core.deploy_queue import load, clear
from core.deploy_iam import approve
from core.deploy_executor import deploy


def run():

    print("\n=== DEPLOY PIPELINE ===")

    staged = load()

    if not staged:
        print("NOTHING TO DEPLOY")
        return False

    approved = approve(staged)

    for entry in approved:
        deploy(entry)

    clear()

    print("DEPLOY COMPLETE")

    return True
