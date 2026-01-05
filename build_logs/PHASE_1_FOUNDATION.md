# Phase 1 — Foundation

## Goal

The goal of Phase 1 was to build a **minimal, trustworthy foundation** for a learning guidance system.

Not a smart system.
Not a scalable system.
Just something that:
- Works end-to-end
- Uses real data
- Can be reasoned about

---

## What I Tried First

I started by collecting learning resources in CSV format and converting them into JSON so the system could work programmatically.

At this stage, my focus was:
- Structure over volume
- Metadata over content
- Simplicity over cleverness

---

## What Failed

### 1. JSON parsing failures
My first JSON files failed to load because I had:
- Comments inside JSON
- Inconsistent formatting
- Fields that were assumed but not enforced

This broke ingestion immediately.

### 2. Over-trusting libraries
I initially tried to use newer abstraction-heavy libraries without fully understanding:
- Their dependency chains
- OS-specific requirements (Windows issues)
- Hidden assumptions (Torch, CUDA, DLLs)

This caused repeated runtime errors.

---

## How Many Attempts

- Data schema redesign: ~3 iterations  
- Cleaning pipeline rewrites: 2 times  
- Dependency stack reset: 1 full reset  

I had to step back more than once and simplify.

---

## What I Changed

- Removed comments from JSON entirely
- Made schema explicit and strict
- Reduced dependencies aggressively
- Chose CPU-only, OS-stable tooling
- Stopped optimizing early

Once I did this, things stopped breaking.

---

## What I Learned

### Technical
- “Simple” data formats are only simple if you respect their rules
- Dependency convenience hides real complexity
- Stable systems start boring, not smart

### Personal
- Rushing abstraction creates invisible debt
- Slowing down actually saved time
- Debugging is easier when you trust every layer

---

## Thoughts

Phase 1 was frustrating, but necessary.

Most failures weren’t because the idea was hard —  
they were because I tried to move too fast before earning stability.

Once I accepted that the foundation didn’t need to be impressive, everything became clearer.
