# Consultation Navigator

## 1. Purpose

Consultation Navigatorは、
ユーザーの曖昧な相談を段階的に整理し、
Recommendation Engineが利用できるConsultation Contextへ変換する。

Consultation Navigatorは診断結果を決定しない。

診断結果はRecommendation EngineとAKE Diagnostic Patternsが決定する。

関連文書: [Recommendation Engine](06_RECOMMENDATION_ENGINE.md)、[Architecture Principles](04_ARCHITECTURE_PRINCIPLES.md)

---

## 2. Responsibilities

Consultation Navigatorの責務:

- 相談開始
- Question Catalogから質問を取得
- Navigation Rulesを評価
- ユーザー回答を取得
- 回答を検証
- Consultation Contextを更新
- 必須情報の充足状況を確認
- 候補Pattern数を確認
- 相談終了条件を判定
- Information Unknownを検出
- Recommendation EngineへConsultation Contextを渡す

責務外:

- 診断Patternの決定
- 推奨順位の算出
- Recommendation Scoreの算出
- Knowledge Unknownの技術分析
- AKE Patternの登録承認

---

## 3. Three-Step Consultation Structure

相談は原則として、以下の3段階で構成する。

### Step 1: Purpose

ユーザーが何を実現したいかを確認する。

Examples:

- 業務を効率化したい
- 自動化したい
- AIを導入したい
- 品質を上げたい
- コストを削減したい
- 比較検討したい

### Step 2: Current State

現在の環境や利用サービス、組織条件を確認する。

Examples:

- 利用中のサービス
- 業務ツール
- 組織規模
- 業種
- セキュリティ要件
- 現在の運用方法

### Step 3: Main Problem

ユーザーが最も困っていることを確認する。

Examples:

- 転記が多い
- 同じ資料を繰り返し作成している
- 承認工程が遅い
- 品質が担当者によって異なる
- 問い合わせ対応に時間がかかる

Step 3のMain Problemは、
Recommendation Engineが候補Patternを絞り込むための重要項目として扱う。

---

## 4. Architecture

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
↓
AKE Diagnostic Patterns
↓
Diagnosis Report

---

## 5. AKE Logical Areas

AKEは単一の巨大テーブルとして設計しない。

論理的に以下を分離する。

### Diagnostic Patterns

条件に対して、どの推奨を提示するかを保持する。

### Question Catalog

ユーザーへ提示する質問そのものを保持する。

### Navigation Rules

どのContext条件で、どのQuestionを提示するかを保持する。

### Reference Data

業種、サービス、目的、課題区分などの共通値を保持する。

---

## 6. Question Catalog

Question Catalogは、質問文と回答形式を共通部品として管理する。

Conceptual example:

question_id: Q-APP-001
text: 現在、主に利用しているアプリはどれですか？
answer_type: multiple_choice
options:
  - Word
  - Excel
  - Teams
  - SharePoint
  - Other
context_field: current_tools
required: false

質問文をDiagnostic PatternやNavigation Ruleへ直接重複登録しない。

---

## 7. Navigation Rules

Navigation Rulesは、
Consultation Contextの現在値に応じて次のQuestionを決定する。

Conceptual example:

rule_id: NAV-MS-001

when:
  purpose: automation
  current_tools:
    contains: Word

ask:
  question_id: Q-WORD-002

Navigation Ruleは質問本文を持たず、
Question CatalogのQuestion IDを参照する。

---

## 8. Consultation Context

Consultation Contextは、
Recommendation Engineへ渡される標準化された相談情報である。

Conceptual example:

purpose: automation
current_tools:
  - Word
main_problem: repetitive_document_creation
approval_required: unanswered
budget_level: unanswered
security_level: unanswered

Consultation Contextは会話履歴そのものではない。

自然言語表現ではなく、
標準化されたキーと値を保持する。

---

## 9. Required, Optional, and Unanswered Fields

Consultation Contextの項目は以下へ分類する。

- Required
- Optional
- Unanswered
- Not Applicable

方針:

- 診断に必要な項目のみRequiredとする
- Optional項目は無理に質問しない
- 未回答は正式な状態として扱う
- 未回答と条件不一致を混同しない
- Schema上の正式表現はPhase5で決定する

---

## 10. Completion Check

相談終了条件:

- Required Fieldsが充足している
- 候補Diagnostic Patternが1〜3件程度へ絞られている
- 追加質問による診断精度向上が限定的である

Beta初期では、
Required Fieldsの充足と候補Pattern数を中心に単純判定してよい。

---

## 11. Answer Validation

選択式回答については、
Question Catalogで定義された値以外を原則として確定Contextへ登録しない。

自由回答は以下の流れとする。

Free-text answer
↓
Structured candidate
↓
User confirmation
↓
Consultation Context update

Vertical Slice 0では自由回答対応をPendingとする。

---

## 12. Answer Correction

Beta初期では、
過去回答を修正する際は相談を最初からやり直す。

Partial Context Recalculationは実施しない。

将来的には、
変更項目に依存する後続Contextのみを再評価する仕組みを検討する。

---

## 13. Unknown Classification

Unknownは以下へ分離する。

### Information Unknown

必要なConsultation Contextが不足している。

Action:

Consultation Navigatorが追加質問を行う。

### Knowledge Unknown

必要なConsultation Contextは揃っているが、
AKEに適合Patternが存在しない。

Action:

Recommendation EngineがUnknown Routeへ送る。

---

## 14. Relationship with Recommendation Engine

Consultation Navigator:

- ユーザーと対話する
- Contextを生成する
- 情報不足を検出する

Recommendation Engine:

- Contextを受け取る
- Diagnostic Patternを検索する
- 候補を評価する
- 推奨結果を生成する
- Knowledge Unknownを検出する

---

## 15. Relationship with AKE

Consultation Navigatorは以下を参照する。

- Question Catalog
- Navigation Rules
- Reference Data

Recommendation Engineは以下を参照する。

- Diagnostic Patterns
- Reference Data

AKEは知識の中心であるが、
各データ領域の責務は分離する。

---

## 16. Vertical Slice 0 Boundary

Vertical Slice 0は、Phase 4の次の実装マイルストーンである。

Vertical Slice 0では、以下を対象とする。

- 単一相談テーマ
- Question 3〜5件
- Navigation Rule数件
- Consultation Context生成
- Diagnostic Pattern 1件以上
- 単純一致判定
- 診断結果表示
- 回答修正時の最初からやり直し

以下はPendingとする。

- 自由回答のAI解析
- Context部分再計算
- 高度なRecommendation Scoring
- 複雑な分岐
- 管理画面
- 本格DB
- 外部公開環境

---

## 17. Design Principles

- Conversation is not the diagnosis input.
- Consultation Context is the diagnosis input.
- Ask only what is necessary.
- Unanswered is a valid state.
- Navigation and Diagnostic Patterns remain separated.
- AI interpretation requires user confirmation.
- Information Unknown and Knowledge Unknown are different.
- The initial Beta prioritizes simplicity over dynamic recalculation.
