import json

CHUNK_SIZE = 400
CHUNK_OVERLAP = 80


def simple_chunk(text, chunk_size, overlap):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap

    return chunks


def chunk_documents(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        documents = json.load(f)

    chunked_docs = []

    for doc in documents:
        chunks = simple_chunk(doc["content"], CHUNK_SIZE, CHUNK_OVERLAP)
        for chunk in chunks:
            chunked_docs.append({
                "content": chunk,
                "metadata": doc["metadata"]
            })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunked_docs, f, indent=2, ensure_ascii=False)

    print(f"Total chunks created: {len(chunked_docs)}")


if __name__ == "__main__":
    chunk_documents(
        input_path="data/cleaned/documents.json",
        output_path="data/cleaned/chunks.json"
    )
