def build_learner_profile(
    topic: str,
    level: str,
    learning_style: str,
    language: str,
    budget: str
) -> dict:
    """
    Deterministic learner profile extractor.
    No LLM, no heuristics, no hallucination.
    """

    # Normalize inputs
    topic = topic.lower().strip()
    level = level.lower().strip()
    learning_style = learning_style.lower().strip()
    language = language.lower().strip()
    budget = budget.lower().strip()

    # Allowed values (strict)
    allowed_levels = {"beginner", "intermediate", "advanced"}
    allowed_styles = {"practical", "conceptual", "mixed"}
    allowed_budgets = {"free", "paid"}
    allowed_languages = {"english"}

    if level not in allowed_levels:
        raise ValueError(f"Invalid level: {level}")

    if learning_style not in allowed_styles:
        raise ValueError(f"Invalid learning style: {learning_style}")

    if budget not in allowed_budgets:
        raise ValueError(f"Invalid budget: {budget}")

    if language not in allowed_languages:
        raise ValueError(f"Unsupported language: {language}")

    profile = {
        "topic": topic,
        "level": level,
        "learning_style": learning_style,
        "language": language,
        "budget": budget
    }

    return profile


if __name__ == "__main__":
    # Example usage (CLI test)
    profile = build_learner_profile(
        topic="Machine Learning",
        level="Beginner",
        learning_style="Practical",
        language="English",
        budget="Free"
    )

    print("Learner Profile:")
    print(profile)
