def approve(blueprint):

    print("\n=== IAM ===")

    approved = []

    for step in blueprint:

        # 🔴 einfache Regel (erweiterbar)
        if step["action"]:
            approved.append(step)

    print("APPROVED:", approved)

    return approved
