def run_until_stable(context):

    history = []
    stable_counter = 0

    while True:

        result = {}

        # --- GRUNDGESETZ ---
        result["vertical"] = context["scan_structure"]()
        result["horizontal"] = context["scan_content"](result["vertical"])
        result["evaluation"] = context["evaluate"](result)
        result["decision"] = context["decide"](result)
        result["action"] = context["act"](result)

        context["store"](result)

        history.append(result)

        # --- STABILITÄT ---
        if result["decision"]["next"] == "NO_CHANGE":
            stable_counter += 1
        else:
            stable_counter = 0

        if stable_counter >= 2:
            result["state"] = "STABLE"
            return result

