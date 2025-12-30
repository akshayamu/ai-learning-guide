def format_matches_style(resource_format: str, learning_style: str) -> bool:
    """
    Checks whether a resource format matches the learner's preferred style.
    """
    if learning_style == "practical":
        return resource_format in {"course", "video"}
    elif learning_style == "conceptual":
        return resource_format in {"article", "video"}
    else:  # mixed
        return True


def filter_and_rank(results, profile, top_k=5):
    """
    Filters and ranks retrieved resources based on learner profile.

    results: list of resource metadata dicts
    profile: learner profile dict
    top_k: number of results to return
    """

    filtered = []

    for r in results:
        # ---------- HARD FILTERS ----------
        if r.get("level") != profile["level"]:
            continue

        if r.get("language") != profile["language"]:
            continue

        if profile["budget"] == "free" and r.get("cost") != "free":
            continue

        # ---------- SCORING ----------
        score = 0

        # Exact topic match
        if r.get("topic") == profile["topic"]:
            score += 1

        # Learning style match
        if format_matches_style(r.get("format"), profile["learning_style"]):
            score += 2

        # Shorter duration (beginner-friendly)
        if r.get("duration_minutes", 999) <= 120:
            score += 1

        ranked_resource = r.copy()
        ranked_resource["score"] = score
        filtered.append(ranked_resource)

    # Sort by score (highest first)
    ranked = sorted(filtered, key=lambda x: x["score"], reverse=True)

    return ranked[:top_k]
