# Recommendation Engine

## Purpose

The Recommendation Engine generates the best recommendation using patterns stored in the AISA Knowledge Engine (AKE).

It does not own knowledge itself.

Knowledge is stored only inside AKE.

---

## Responsibilities

- Pattern Matching
- Candidate Selection
- Success Probability Scoring
- First Action Scoring
- Recommendation Ranking
- Diagnosis Report Generation
- Unknown Route Detection

---

## Relationship

User Consultation

↓

Recommendation Engine

↓

AKE Pattern Search

↓

Matched Patterns

↓

Scoring

↓

Diagnosis Report

If no sufficient pattern exists

↓

Unknown Route

↓

Engineering Analysis

↓

Human Review

↓

AKE Registration

↓

Future Diagnosis

---

## AKE Data Model

Each AKE Pattern stores:

- Pattern ID
- Business Category
- Consultation Purpose
- Applicable Conditions
- Exclusion Conditions
- Recommended Architecture
- AI Requirement Level
- Automation Rate
- Estimated Cost
- Difficulty
- Maintainability
- Risks
- First Action
- Success Probability
- Related Patterns

---

## Design Principle

AKE is not intended to be complete.

It is designed to grow continuously through real consultations.

Recommendation Engine always evaluates registered patterns before considering Unknown Route.
