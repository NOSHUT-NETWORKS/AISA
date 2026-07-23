# Current Sprint

## Sprint 0 — Development Foundation (Completed)

### Goal

NNGPT Development Teamの創設理念と、Codex・NNGPT間の同期基盤をGitHubに確立する。

### Scope

- mainブランチの初期化
- `foundation/synchronngpt-v0.1` ブランチの作成
- プロジェクトREADMEの追加
- `docs/synchroNNGPT/` 共通コンテキストの追加
- Pull RequestによるAgree／Alignレビュー

### Definition of Done

- [x] mainが初期化されている
- [x] 指定された文書構成が作成されている
- [x] 創設理念とFounding Declarationが記録されている
- [x] AISAの基本的な提案モデルが記録されている
- [x] Pull Requestがレビューされ、AgreeとAlignが確認されている
- [x] mainへmergeされている

### Next

Sprint1でAISA Core Diagnostic Frameworkを開始する。

# Phase 2 — User Entry & Intent Design (Completed)

Status:
Freeze ✅

## User Entry

The consultation starts with a single prompt.

「今日はどんな相談ですか？」

The user should not be required to answer long questionnaires.

AISA gathers only the minimum information required to produce the first recommendation.

---

## Intent Design

The entry point is not limited to problems.

Supported intents include:

- Want to start
- Want to improve
- Want to compare
- Want to learn
- Want to solve a problem

---

## One Session Principle

AISA provides the most valuable first action within a single consultation.

Further conversations represent continuous improvement,
not re-diagnosis.

---

## Beta Philosophy

The Beta diagnostic engine must remain AI-independent.

Diagnosis is implemented through
rule-based decision trees
and the

AISA Knowledge Engine (AKE).

---

## AISA Knowledge Engine (AKE)

AKE is the core knowledge asset of AISA.

Workflow:

User Consultation

↓

Search AKE

↓

Known
→ Generate Diagnosis Report

Unknown
→ Escalate to NNGPT Engineering
→ Analyze
→ Human Review
→ Register into AKE
→ Available automatically for future users

AKE continuously expands through real consultations.

---

## Cost First Architecture

AI is only used where AI uniquely creates value.

The Beta diagnostic engine itself must remain AI-independent.

## Phase 3 - Freeze①

Status: ✅ Frozen

Completed:

- Recommendation Engine architecture
- AISA Knowledge Engine (AKE) responsibilities
- Unknown Route
- AKE Knowledge Loop

## Phase4: Consultation Navigator

Status:

Frozen

Purpose:

ユーザーとの対話を通じて、曖昧な相談内容をRecommendation Engineが処理可能な
Consultation Contextへ変換する。

Architecture:

User
↓
Consultation Navigator
├─ Question Catalog
├─ Navigation Rules
├─ Answer Validation
├─ Context Update
└─ Completion Check
↓
Consultation Context
↓
Recommendation Engine

Completion Criteria:

- Consultation Contextの標準構造が定義されている
- 必須項目、任意項目、未回答状態が定義されている
- Question CatalogとNavigation Rulesが分離されている
- Diagnostic PatternとNavigation Logicが分離されている
- Consultation Completion Checkが定義されている
- Information UnknownとKnowledge Unknownが区別されている
- 自由回答のContext登録前確認方針が定義されている
- 回答修正のBeta初期方針が定義されている

Next Step:

Vertical Slice 0 Specification

Phase4完了後、Phase5へ進む前に、
AISAを端から端まで最低限動作させるVertical Slice 0を設計・実装する。
