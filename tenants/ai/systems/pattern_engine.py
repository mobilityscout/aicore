def weight(entry):
    confidence = entry.get("confidence", 0)

    if confidence >= 0.9:
        return "HIGH"
    if confidence >= 0.7:
        return "MEDIUM"

    return "LOW"
