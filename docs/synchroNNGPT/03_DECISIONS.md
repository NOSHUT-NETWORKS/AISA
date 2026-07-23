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

## ADR-00X — Recommendation Engine is driven by AKE

### Decision

The Recommendation Engine does not contain business knowledge.

Instead, it evaluates and ranks diagnostic patterns stored in the AISA Knowledge Engine (AKE).

Unknown requests are never discarded.

When sufficient knowledge does not exist,
the request enters the Unknown Route,
is analyzed,
reviewed,
and registered as a new AKE Pattern.

### Status

Accepted

## ADR: Consultation Navigator generates Consultation Context

### Decision

Consultation Navigatorは、ユーザーとの対話を管理し、
Recommendation Engineへ渡す標準化されたConsultation Contextを生成する。

Conversation EngineやUIはRecommendation Engineへ直接、
会話履歴や自然言語全文を渡さない。

Recommendation Engineは原則としてConsultation Contextを入力として扱う。

### Reason

- UIやチャネルを交換可能にするため
- Web、Teams、LINE、音声など複数の相談窓口に対応可能にするため
- Recommendation Engineを会話表現から分離するため
- 診断ロジックの再現性を確保するため
- テスト可能性を高めるため

### Consequences

- Consultation Context Schemaが必要となる
- 自然言語回答からContextへの変換処理が必要となる
- Context確定前の確認処理が必要となる
- 未回答状態を正式な状態として扱う必要がある

## ADR: Diagnostic Patterns and Navigation Logic are separated

### Decision

Diagnostic PatternへNavigation Logicを直接埋め込まない。

AKE内では以下を論理的に分離して管理する。

- Diagnostic Patterns
- Question Catalog
- Navigation Rules
- Reference Data

### Reason

- 同一質問の重複登録を防ぐため
- 質問文と分岐条件を独立して変更可能にするため
- Pattern追加時の影響範囲を限定するため
- DBおよびデータ構造の複雑化を抑えるため
- Navigationのテストを独立して実施可能にするため

### Principle

Pattern = 答えの知識

Navigation = 答えに到達するための進み方

## ADR: Optional consultation fields remain unanswered unless required

### Decision

Consultation Contextでは、診断上の必須項目以外を強制的に取得しない。

任意項目は未回答状態を許容する。

未回答状態は、値が存在しないことや条件不一致とは区別する。

Recommended conceptual states:

- answered
- unanswered
- not_applicable

実際のSchema表現はPhase5で正式決定する。

### Reason

- 質問数を必要最低限に抑えるため
- One Session Principleを維持するため
- 不要な質問による離脱を防ぐため
- 情報不足と条件不一致を区別するため

## ADR: Consultation completion is based on minimum sufficient context

### Decision

Consultation Navigatorは、以下を満たした時点で質問を終了する。

- 診断に必要な必須項目が取得済み
- 候補Diagnostic Patternが概ね1〜3件へ絞られている
- 追加質問による診断精度向上が限定的

Beta初期では、上記を単純なルールとして実装してよい。

### Reason

すべての情報を収集することではなく、
最初の具体的な行動を提示できる最低限のContextを得ることが目的であるため。

## ADR: Answer correction restarts the consultation in the initial Beta

### Decision

Beta初期では、ユーザーが過去の回答を修正する場合、
現在の相談Contextを部分的に再計算せず、相談を最初からやり直す。

### Reason

- 依存関係管理を初期実装へ持ち込まないため
- Context不整合を避けるため
- Vertical Slice 0を単純に保つため

### Future

将来的には変更項目に依存する後続Contextのみを再評価する。

## ADR: Free-text interpretation requires user confirmation

### Decision

自由回答をConsultation Contextへ登録する場合、
AIまたは解析処理が構造化候補を生成し、
ユーザー確認後に確定値として登録する。

Flow:

Free-text answer
↓
Structured candidate
↓
User confirmation
↓
Consultation Context update

AIによる解釈結果を、確認なしで確定Contextへ登録しない。

### Reason

- 誤解釈を防ぐため
- 診断根拠を明確にするため
- ユーザー自身の納得感を維持するため

### Vertical Slice 0

自由回答対応はPendingとし、
選択式回答を中心に構築する。

## ADR: Information Unknown and Knowledge Unknown are distinct

### Decision

Unknownを以下の2種類へ分離する。

#### Information Unknown

診断に必要なConsultation Contextが不足している状態。

Action:

追加質問を行う。

#### Knowledge Unknown

必要なConsultation Contextは揃っているが、
AKE内に適合するDiagnostic Patternが存在しない状態。

Action:

Unknown Routeへ送る。

Unknown Route:

Engineering Analysis
↓
Human Review
↓
AKE Registration
↓
Future Automatic Diagnosis

### Reason

情報不足の相談が誤って人間レビューへ送られることを防ぐため。
