# Architecture Principles

## One Session Principle

Each consultation should provide a complete and actionable first recommendation.

---

## Cost First Architecture

AI should only be used where AI uniquely creates value.

Avoid unnecessary API usage.

---

## AKE Knowledge Loop

AISA continuously improves through accumulated knowledge.

Unknown consultations are not failures.

Instead they become new knowledge assets.

### Flow

Consultation

↓

AKE Search

↓

Known
→ Diagnosis

Unknown

↓

Engineering Analysis

↓

Human Review

↓

AKE Registration

↓

Future Automatic Diagnosis

### Principles

- Unknown is an opportunity to learn.
- Every analyzed consultation becomes a reusable asset.
- Recommendation Engine always prioritizes AKE before any other processing.
- AKE grows continuously through real-world consultations.

---

## Structured Consultation Principle

AISAは自然言語の会話をそのまま診断入力として扱わない。

相談内容をConsultation Contextへ構造化し、
Recommendation EngineはそのContextを基に診断する。

This enables:

- UI independence
- Channel independence
- Repeatable diagnosis
- Testable recommendation logic
- Explainable results

---

## Minimum Sufficient Context Principle

AISAは、取得可能なすべての情報を収集することを目的としない。

診断とFirst Actionの提示に必要な、
最小限かつ十分なConsultation Contextを取得する。

Optional information remains unanswered unless it materially improves the diagnosis.

See also: [Consultation Navigator](07_CONSULTATION_NAVIGATOR.md) and [Recommendation Engine](06_RECOMMENDATION_ENGINE.md).
