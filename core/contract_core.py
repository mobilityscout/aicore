def resolve(context):

    scan = context["scan"]
    fix  = context["fix"]
    guard = context["guard"]

    result = {}

    # --- SCAN ---
    result["scan"] = scan()

    # --- FIX PROPOSAL ---
    result["fix"] = fix(result["scan"])

    # --- GUARD CHECK ---
    result["guard"] = guard(result)

    # --- IAM DECISION ---
    if result["guard"]["status"] == "BLOCK":
        decision = "REJECT"
    elif result["fix"]["status"] == "READY":
        decision = "APPROVE"
    else:
        decision = "REVIEW"

    result["decision"] = decision

    return result
