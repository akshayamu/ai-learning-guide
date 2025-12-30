import json
import re
import uuid

ALLOWED_LEVELS = {"beginner", "intermediate", "advanced"}
ALLOWED_FORMATS = {"video", "article", "course"}
LANGUAGE = "english"
TOPIC = "machine learning"

def clean_text(text: str) -> str:
    if not text:
        return ""

    text = text.lower()

    # remove urls
    text = re.sub(r"http\S+", "", text)

    # remove timestamps (00:12, 1:23:45)
    text = re.sub(r"\b\d{1,2}:\d{2}(:\d{2})?\b", "", text)

    # remove promotions
    promos = [
        "like and subscribe",
        "subscribe to the channel",
        "follow me on",
        "check out my course"
    ]
    for p in promos:
        text = text.replace(p, "")

    # remove emojis & non-text chars
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    # normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def normalize_level(level: str) -> str | None:
    if not level:
        return None
    level = level.lower().strip()
    return level if level in ALLOWED_LEVELS else None


def normalize_format(fmt: str) -> str | None:
    if not fmt:
        return None
    fmt = fmt.lower().strip()
    return fmt if fmt in ALLOWED_FORMATS else None


def clean_dataset(input_path: str, output_path: str):
    with open(input_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    cleaned = []

    for row in raw_data:
        content = clean_text(row.get("content") or row.get("description", ""))

        level = normalize_level(row.get("level"))
        fmt = normalize_format(row.get("format"))

        # strict filtering
        if not content or not level or not fmt:
            continue

        if row.get("cost", "").lower() != "free":
            continue

        doc = {
            "id": str(uuid.uuid4()),
            "content": content,
            "metadata": {
                "topic": TOPIC,
                "level": level,
                "language": LANGUAGE,
                "format": fmt,
                "cost": "free",
                "duration_minutes": int(row.get("duration_minutes", 0)),
                "url": row.get("url", "")
            }
        }

        cleaned.append(doc)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2, ensure_ascii=False)

    print(f"Cleaned documents: {len(cleaned)}")


if __name__ == "__main__":
    clean_dataset(
        input_path="data/raw/resources.json",
        output_path="data/cleaned/documents.json"
    )
