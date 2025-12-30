import csv
import json
import os
import sys

# =========================
# BASE DIRECTORY
# =========================
BASE_DIR = r"C:\Users\DELL\ai-learning-guide"

# Supported input files
CSV_FILE = os.path.join(BASE_DIR, "data.csv")
XLSX_FILE = os.path.join(BASE_DIR, "data.xlsx")

# Output
JSON_FILE = os.path.join(BASE_DIR, "data.json")

# =========================
# HELPERS
# =========================
def cast_value(key, value):
    """Cast CSV string values to proper types"""
    if value is None:
        return None

    v = value.strip()

    # Boolean fields
    if key in {"voice_friendly", "low_bandwidth", "has_transcript"}:
        return v.lower() == "true"

    # Integer fields
    if key in {"duration_minutes"}:
        try:
            return int(v)
        except ValueError:
            return None

    # Float fields
    if key in {
        "quality_score",
        "structure_score",
        "practice_score",
        "clarity_score"
    }:
        try:
            return float(v)
        except ValueError:
            return None

    return v


# =========================
# CSV → JSON
# =========================
def convert_csv_to_json():
    if not os.path.exists(CSV_FILE):
        print("❌ data.csv not found.")
        print("👉 Make sure the file is saved as CSV, not Excel (.xlsx).")
        sys.exit(1)

    data = []

    with open(CSV_FILE, mode="r", encoding="utf-8-sig", newline="") as csvf:
        reader = csv.DictReader(csvf)

        for row in reader:
            clean_row = {}
            for key, value in row.items():
                clean_row[key] = cast_value(key, value)
            data.append(clean_row)

    with open(JSON_FILE, mode="w", encoding="utf-8") as jsonf:
        json.dump(data, jsonf, indent=4, ensure_ascii=False)

    print("✅ CSV → JSON conversion successful")
    print(f"📁 Output saved to: {JSON_FILE}")


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    convert_csv_to_json()
