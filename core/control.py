from core.iam import mode

class Control:

    def decide(self, analysis):

        m = mode()

        decision = {
            "mode": m,
            "allowed": True,
            "action": "CONTINUE"
        }

        # BASIC VALIDATION
        layers = analysis.get("layers", {})
        if len(layers) < 6:
            decision["allowed"] = False
            decision["reason"] = "INCOMPLETE"

        # MODE LOGIK
        if m == "AUTO":
            decision["action"] = "CONTINUE"

        elif m == "MANUAL":
            decision["action"] = "WAIT"

        elif m == "HYBRID":
            if decision["allowed"]:
                decision["action"] = "CONTINUE"
            else:
                decision["action"] = "WAIT"

        return decision
