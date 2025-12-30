# System Architecture — MVP v0.1

This document explains the technical design of the Nonprofit AI Learning Guidance System MVP in plain, grounded terms.

The goal of this system is not to look intelligent, but to be **trustworthy, predictable, and fair**—especially for learners who are often underserved by complex or opaque technology.

This MVP is intentionally simple. Every design decision prioritizes **clarity over cleverness**.

---

## Core Philosophy

Before describing the system, it is important to understand the mindset behind it.

This system is built on five non-negotiable principles:

1. **Find information before generating anything**  
   Real learning resources are retrieved first. The system does not fabricate content.

2. **Prefer deterministic logic over black-box behavior**  
   Every decision can be traced back to a clear rule.

3. **Explainability matters more than optimization**  
   Learners should understand *why* something was recommended.

4. **Minimal dependencies mean long-term stability**  
   The system must run reliably on modest hardware.

5. **Accessibility comes first, even if delivered later**  
   The architecture is designed to support future voice and low-tech access.

This is not an engagement-driven product.  
It is a **guidance system**, not a persuasion engine.

---

## High-Level Flow

Learner Inputs
→ Learner Profile Normalization
→ Semantic Resource Retrieval
→ Strict Constraint Filtering
→ Rule-Based Ranking
→ Clear Explanation of Results
→ Final Recommendations


Each step performs exactly one responsibility.

---

## 1. Learner Input Layer

### Purpose
Collect learner needs in a structured and limited format.

### Inputs
- Topic
- Level (beginner / intermediate / advanced)
- Learning style (practical / conceptual / mixed)
- Language
- Budget (free / paid)

### Design Choice
- No free-form chat
- Fixed, structured inputs only

### Reason
- Avoids ambiguity and misinterpretation
- Makes behavior auditable and predictable
- Treats all learners fairly

---

## 2. Learner Profile Extractor

### Purpose
Normalize learner inputs into a clean profile.

### Output Example
```json
{
  "topic": "machine learning",
  "level": "beginner",
  "learning_style": "practical",
  "language": "english",
  "budget": "free"
}

Design Choice

Rule-based validation only

No LLM usage

Reason

Deterministic behavior

No hallucination risk

Transparent constraint handling

3. Semantic Retrieval Layer
Purpose

Find learning resources relevant to the learner’s goal.

Implementation

TF-IDF vectorization (scikit-learn)

FAISS vector index (IndexFlatL2)

Design Choice

Classical information retrieval

CPU-only, OS-stable stack

Reason

Reliable on all systems

Easy to debug and maintain

Sufficient for early-stage guidance

Accuracy is important, but trustworthiness is essential.

4. Filtering Layer (Hard Constraints)
Purpose

Strictly enforce learner constraints.

Rules

Learning level must match

Language must match

Cost must respect budget

Design Choice

Hard filtering before ranking

Reason

Prevents inappropriate recommendations

Builds learner trust

Eliminates second-guessing

5. Ranking Layer (Soft Preferences)
Purpose

Order valid resources by suitability.

Signals Used

Learning style vs resource format

Topic alignment

Duration suitability

Design Choice

Simple, additive scoring rules

No machine-learned ranking models

Reason

Fully explainable

Easy to audit and adjust

No hidden optimization

6. Explanation Layer
Purpose

Explain why each resource was recommended.

Example Explanations

Matches your beginner level

Uses practical, hands-on examples

Short and beginner-friendly

Each explanation maps directly to an applied rule.

Design Choice

Rule-based explanations only

Reason

Transparency

No persuasive or marketing language

The system informs, it does not influence

What This MVP Intentionally Avoids

Large language models in core logic

Black-box recommendation systems

Engagement or retention tricks

Automated content generation

Personal data collection

These exclusions are deliberate and principled.

Known Limitations (Accepted)

Single-language support

Small, curated dataset

No adaptive feedback loop

No mobile or voice interface yet

These are trade-offs, not oversights.

Final Summary

This MVP is designed to earn trust before it earns scale.

It prioritizes:

Explainability over intelligence

Stability over sophistication

Fair access over engagement metrics