def approve(entries):

    print("\n=== IAM APPROVAL ===")

    approved = []

    for e in entries:
        # 🔴 einfache Regel (später erweiterbar)
        if e.get("content") and len(e["content"]) > 5:
            approved.append(e)

    print("APPROVED:", [e["name"] for e in approved])

    return approved
