# Nonprofit AI Learning Guidance System (MVP v0.1)

This project is a **nonprofit AI learning guidance system** that helps learners find the *right* educational resources based on their level, learning style, language, and budget.

The focus of this system is **guidance, not persuasion**.

This repository contains the **frozen MVP (v0.1)**.

---

## Why This Project Exists

Learners often struggle with:
- Choosing where to start learning a topic
- Identifying genuinely beginner-friendly resources
- Finding high-quality free content
- Understanding *why* a resource is recommended

There is an abundance of content online, but very little **structured guidance**.

This project exists to address that gap.

---

## What the MVP Does

The MVP (v0.1):

- Accepts structured learner inputs (topic, level, preferences)
- Retrieves real learning resources (no content generation)
- Applies strict constraint-based filtering
- Ranks resources using transparent, rule-based logic
- Explains recommendations in plain language
- Runs deterministically without LLM dependency

---

## Architecture Overview

Learner Inputs
→ Learner Profile Normalization
→ Semantic Resource Retrieval
→ Strict Constraint Filtering
→ Rule-Based Ranking
→ Explanation Layer
→ Final Recommendations

yaml
Copy code

For full technical reasoning and design philosophy, see  
📄 **ARCHITECTURE.md**

---

## Project Status

✅ Phase 1 — Foundation: Completed  
✅ Phase 2 — Intelligence (MVP): Completed  

🔒 **MVP v0.1 is frozen and documented**

---

## What Comes Next (Post-MVP)

- Accessibility (voice / IVR, low-bandwidth access)
- Multi-language support
- Optional, safe LLM usage for explanations only
- Feedback-driven improvements

These will be built **on top of the frozen MVP**, not replace it.

---

## Nonprofit Intent

This project is built for **equitable access to learning** and will remain open, transparent, and guidance-focused.

---

## License & Use

Intended for nonprofit, educational, and research use.

Feedback and collaboration are welcome.