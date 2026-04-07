def score_unit(unit):

    score = 0

    if unit["exists"]:
        score += 0.4

    if unit["files"] > 0:
        score += 0.6

    return score


def evaluate(model):

    result = {}
    total = 0

    for k, v in model.items():

        s = score_unit(v)
        result[k] = s
        total += s

    overall = total / len(model) if model else 1

    return result, overall
