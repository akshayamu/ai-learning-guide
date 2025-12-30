import json
import pickle
import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def build_faiss_index(chunk_path, index_path):
    with open(chunk_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    texts = [c["content"] for c in chunks]
    metadatas = [c["metadata"] for c in chunks]

    # TF-IDF vectorization (CPU-safe)
    vectorizer = TfidfVectorizer(
        max_features=5000,
        stop_words="english"
    )
    X = vectorizer.fit_transform(texts)
    X = X.astype(np.float32).toarray()

    # Build FAISS index
    dim = X.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(X)

    # Save index + metadata
    faiss.write_index(index, f"{index_path}/index.faiss")

    with open(f"{index_path}/metadata.pkl", "wb") as f:
        pickle.dump(metadatas, f)

    with open(f"{index_path}/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    print("FAISS index built successfully (TF-IDF)")


if __name__ == "__main__":
    build_faiss_index(
        chunk_path="data/cleaned/chunks.json",
        index_path="vectorstore/faiss_index"
    )
