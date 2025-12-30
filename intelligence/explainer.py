def explain_resource(resource, profile):
    """
    Generates a transparent explanation for why a resource was recommended.
    """

    reasons = []

    if resource.get("level") == profile["level"]:
        reasons.append(f"Matches your {profile['level']} level")

    if resource.get("language") == profile["language"]:
        reasons.append(f"Available in {profile['language'].capitalize()}")

    if resource.get("topic") == profile["topic"]:
        reasons.append("Focused on your chosen topic")

    if profile["learning_style"] == "practical" and resource.get("format") in {"course", "video"}:
        reasons.append("Uses practical examples and demonstrations")

    if profile["learning_style"] == "conceptual" and resource.get("format") == "article":
        reasons.append("Emphasizes conceptual understanding")

    if resource.get("duration_minutes", 999) <= 120:
        reasons.append("Short and beginner-friendly duration")

    return reasons
