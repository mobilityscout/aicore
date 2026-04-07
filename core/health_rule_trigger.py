def should_create_rule(signal):

    status = signal.get("health_status")

    if status in ["UNKNOWN", "ANOMALY"]:
        return True

    return False
