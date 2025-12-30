import faiss
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


# Load FAISS index
index = faiss.read_index("vectorstore/faiss_index/index.faiss")

# Load metadata
with open("vectorstore/faiss_index/metadata.pkl", "rb") as f:
    metadatas = pickle.load(f)

# Load vectorizer
with open("vectorstore/faiss_index/vectorizer.pkl", "rb") as f:
    vectorizer: TfidfVectorizer = pickle.load(f)


query = "i want to learn machine learning from scratch"

# Vectorize query
q_vec = vectorizer.transform([query]).astype(np.float32).toarray()

# Search
D, I = index.search(q_vec, k=5)

from intelligence.profile_extractor import build_learner_profile
from intelligence.ranking import filter_and_rank
from intelligence.explainer import explain_resource

# Build learner profile
profile = build_learner_profile(
    topic="machine learning",
    level="beginner",
    learning_style="practical",
    language="english",
    budget="free"
)

# Existing FAISS retrieval code stays the same
# Assume `metadatas` and FAISS search already done

raw_results = [metadatas[idx] for idx in I[0]]

final_results = filter_and_rank(raw_results, profile)

print("\nFinal Personalized Recommendations:\n")

for r in final_results:
    print(f"Score: {r['score']}")
    print(f"Format: {r['format']} | Duration: {r['duration_minutes']} mins")
    print(f"URL: {r['url']}")
    print("Why this fits you:")
    for reason in explain_resource(r, profile):
        print(f" - {reason}")
    print("-" * 60)
