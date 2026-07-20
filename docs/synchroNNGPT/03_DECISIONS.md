# Decisions

## DEC-000 — Adopt GitHub as the Single Source of Truth

- Date: 2026-07-19
- Status: Accepted

### Decision

GitHubをAISA開発のSingle Source of Truthとする。`docs/synchroNNGPT/` をCodexとNNGPTの共通コンテキストとして採用する。

### Rationale

理念、記憶、進捗、判断を同じ場所で履歴管理し、人とAIが同じ前提から協働できるようにするため。

## DEC-001 — Review Changes through Pull Requests

- Date: 2026-07-19
- Status: Accepted

### Decision

mainへの通常の直接コミットを禁止し、Pull Requestで変更をレビューする。レビューの共通語として次を用いる。

- **Agree:** 変更内容と目的に同意できるか。
- **Align:** 創設理念、現在の方針、優先事項と整合しているか。

## DEC-002 — Collaborate by Value, Not Fixed Roles

- Date: 2026-07-19
- Status: Accepted

### Decision

人とAIの役割を固定せず、その時点で最も価値を生み出せる主体が役割を担う。人とAIを競争、比較、分断する思想を採用しない。

## DECISION-008 — Beta Diagnostic Engine

- Status: Accepted

### Decision

The Beta version shall use a rule-based diagnostic engine.

AI APIs are optional extensions,
not the primary diagnostic engine.

## DECISION-009 — One Session Principle

- Status: Accepted

### Decision

Every consultation should produce the user's best possible first action.

Subsequent consultations are considered continuous evolution,
not re-diagnosis.

## DECISION-010 — AISA Knowledge Engine (AKE)

- Status: Accepted

### Decision

Unknown consultations are analyzed,
reviewed,
and permanently registered into AKE.

AKE becomes the continuously growing knowledge asset of AISA.
