def execute(work):

    print("\n=== HEALTH EXECUTION ===")

    for step in work.get("steps", []):

        print("EXEC:", step["action"])

    return True


# 🔴 KOMPATIBILITÄT (WICHTIG!)
def handle(*args, **kwargs):

    print("HEALTH HANDLE FALLBACK")

    return execute({"steps": []})
