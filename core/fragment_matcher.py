from core.library_core import load_library


def match_fragments(signal):

    library = load_library()

    matches = []

    content = signal.get("content", "").lower()

    for case in library:

        try:
            pattern = case.get("type", "").lower()

            if not pattern:
                continue

            score = 0

            # einfacher Matching Score
            if pattern in content:
                score += 0.6

            if case.get("hash") == signal.get("hash"):
                score += 0.4

            if score > 0:
                matches.append({
                    "pattern": pattern,
                    "decision": case.get("decision"),
                    "confidence": round(score, 2)
                })

        except:
            continue

    # nach confidence sortieren
    matches = sorted(matches, key=lambda x: x["confidence"], reverse=True)

    return matches[:5]  # Top 5
