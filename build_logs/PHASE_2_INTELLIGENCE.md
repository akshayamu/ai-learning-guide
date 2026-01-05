# Phase 2 — Intelligence (Without Illusions)

## Goal

The goal of Phase 2 was to add **decision-making** without adding:
- Hallucination
- Black-box behavior
- Hidden optimization

I wanted the system to explain *why* it recommends something, not just what.

---

## What I Tried First

My initial instinct was to:
- Use embeddings everywhere
- Add more “intelligence”
- Make the system feel smart

I quickly realized this would undermine trust.

---

## What Failed

### 1. Library instability
LangChain imports broke repeatedly due to:
- Version fragmentation
- Torch dependencies
- Windows compatibility issues

Even when things worked, they felt fragile.

### 2. Over-complication
Early ranking logic tried to do too much:
- Too many signals
- Implicit weighting
- Hard-to-explain scores

It became unclear *why* something ranked higher.

---

## How Many Attempts

- Retrieval design: 2 iterations  
- Ranking logic rewrite: 2 times  
- Explanation logic: rewritten fully once  

Each rewrite made the system simpler.

---

## What I Changed

- Switched to TF-IDF for retrieval
- Used FAISS only for similarity, not intelligence
- Added hard filters before ranking
- Made ranking rules additive and visible
- Forced every output to have a reason

This made the system boring — in a good way.

---

## What I Learned

### Technical
- Explainability is a design constraint, not a feature
- Classical IR still works surprisingly well
- You don’t need ML everywhere to be useful

### Personal
- “Smart-looking” systems are often harder to trust
- Saying no to LLMs early clarified the entire architecture
- Transparency reduced my own cognitive load

---

## Thoughts

Phase 2 changed how I think about AI.

I stopped asking:
> “How smart can this be?”

And started asking:
> “Can I defend this decision to a learner?”

That question simplified everything.
