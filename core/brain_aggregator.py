from core.central_brain import store


def aggregate(findings):

    print("\n=== BRAIN AGGREGATION ===")

    summary = {}

    for f in findings:

        key = f["finding"]

        summary[key] = summary.get(key, 0) + 1

    for k, v in summary.items():

        entry = {
            "type": "GLOBAL_PATTERN",
            "pattern": k,
            "count": v,
            "status": "SUCCESS",
            "confidence": min(1.0, 0.5 + v * 0.1)
        }

        store(entry)
