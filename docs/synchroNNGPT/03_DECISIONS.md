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

## ADR-0011 — Introduce AISA LABO

- Status: Frozen
- Frozen date: 2026-07-24

### Context

AISAは、構造化相談からConsultation Contextを生成し、AKEのDiagnostic Patternを用いて説明可能なDiagnosis Reportを提示する。Version 0.0.1は2026-07-23に最初のEnd-to-End Consultationを完了した。

次のArchitecture世代では、個々の相談をその場限りの結果として終わらせず、匿名化・構造化された相談事例として将来の相談へ役立てる必要がある。成功事例だけでなく、うまくいかなかった事例も学習可能な知見として扱う。

### Decision

構造化された相談事例を収集・提示する知見ライブラリとして **AISA LABO** を導入する。

- Internal product name: AISA LABO
- UI subtitle: みんなの知見ライブラリ
- Core philosophy: ひとつの相談が、次の誰かの力になる。
- English principle: Every consultation becomes knowledge for the next consultation.

AISA LABOは、匿名化された成功・失敗の相談事例を扱う、編集・構造化されたKnowledge Libraryである。掲示板、Social Feed、未整理のForum、Raw Search Resultsではない。利用体験は、関連する知見と予期しなかった有用な事例に出会える、Curated Bookstoreに近いものとする。

将来の共有Conceptは次の通りとする。

```text
Consultation
→ User consent
→ Anonymization
→ Structuring
→ Pattern and tag assignment
→ AISA LABO registration
```

### Rationale

- 類似相談、成功したApproach、失敗したApproachから学べる。
- 少数派TechnologyのRare Knowledgeを発見できる。
- TechnologyやProblemの一般性・希少性を理解できる。
- Evidence-based Recommendationを支えられる。
- Patternと利用者の増加に伴い、Knowledge Libraryの価値が高まる。
- 将来のAI Curatorが相談ごとに有用なCaseを選べる。

### Consequences

- AISAは、AI-powered consultation applicationから **AI-powered consultation and collective knowledge platform** へ拡張される。
- AKEが保持してきたDiagnostic Patternの責務は維持する。
- AISA LABOはPatternに加え、構造化されたCaseとEvidenceを収集・提示するKnowledge領域となる。
- Caseには成功・失敗Outcomeを含められる。
- Sample dataを利用する場合は、実EvidenceではなくFictional/Demo Dataと明示する。

### Boundaries

このDecisionは、以下を設計または実装しない。

- 匿名化の詳細方式
- PrivacyおよびPersonal Data Processing
- Consentの詳細仕様
- ModerationまたはGovernance Workflow
- AuthenticationおよびPublic Posting
- Production Database
- Evidence Ranking Algorithm
- External Source Ingestion

これらは、別途Frozen Decisionが存在する場合を除き、将来設計とする。

### Relationship

- **Pattern Engine:** Consultation Contextに適合するPattern候補を扱う。既存Recommendation Engine内のPattern Matching責務を概念上表現するが、今回Runtimeを分割しない。
- **AISA LABO:** PatternとTagに関連付けられた構造化Case/Evidenceを収集・提示する。
- **Evidence Engine:** 現在のConsultationに適したEvidenceを将来選択・順位付けする。
- **Recommendation Engine:** Pattern MatchとRelevant Evidenceを用いてRecommendationを生成する。
- **Diagnosis Report:** Recommendationと、その根拠となるEvidenceおよび時間的Contextを説明可能な形で提示する。

AISA LABOはRecommendation Engineを置き換えず、Knowledge Sourceとして支える。

## ADR-0012 — Temporal Knowledge Architecture

- Status: Frozen
- Frozen date: 2026-07-24

### Context

Knowledge is not timeless.

同じConsultationでも、2026年7月と2029年7月では、Product仕様、License条件、API、Cloud環境などの変化により、適切なRecommendationが異なる可能性がある。古いKnowledgeを上書きまたは黙って削除すると、判断の根拠と変化の履歴を失う。

Principles:

- 知識は完成しない。
- 知識は育ち続ける。
- AISAは知識とともに進化する。

### Decision

AISAはKnowledgeをtime-dependent、version-aware、historically traceableなものとして扱う。

Frozen conceptual architecture:

```text
Consultation
→ Pattern Engine
→ AISA LABO
→ Knowledge Lifecycle
→ Evidence Engine
→ Recommendation Engine
→ Diagnosis Report
```

古いKnowledgeは上書きや無通知削除を行わず、Historical Evidenceとして保持し、新しいKnowledgeによりSupersedeできる。

### Temporal Model

Conceptual Knowledge objectは少なくとも以下を持つ。

- `id`
- `pattern`
- `category`
- `technologies`
- `created_at`
- `observed_at`
- `last_verified_at`
- `valid_from`
- `valid_until`
- `confidence`
- `freshness_status`
- `evidence_count`
- `source_type`
- `ai_summary`

将来拡張可能なEnvironmental Metadata:

- Product and application version
- Operating system
- Cloud environment
- Tenant or organization conditions
- License conditions
- API version
- Deployment model
- Region
- Organization scale

これらのOptional Fieldsを、現在のRuntimeまたはIWPへ一律に強制しない。

### Freshness Statuses

- **CURRENT:** 現在検証済み、または適用可能とみなされる。
- **AGING:** まだ有用な可能性があるが、再検証が望ましくなる時点に近づいている。
- **STALE:** Warningまたは追加検証なしに依存すべきではない。
- **SUPERSEDED:** 新しいKnowledgeに置き換えられたが、Traceabilityのため保持する。
- **HISTORICAL:** 時系列分析と変化の理解を主目的に保持する。
- **UNKNOWN:** 現在のValidityを判定できない。

STALE、SUPERSEDED、HISTORICALは黙って削除しない。

### Historical Preservation and Supersession

- Newer Knowledge is not automatically better.
- Older Knowledge may remain strong Evidence when repeatedly verified and still applicable.
- Supersessionは削除ではなく、置換関係と履歴を保持する。
- Diagnosis Reportは、EvidenceのObserved時点、Verification履歴、現在Validityを説明できる方向へ拡張する。

説明例:

- This case was observed in 2026 and has been verified repeatedly since then.
- This approach succeeded in 2026 but is no longer recommended because the product specification changed.
- This evidence is old and its present validity is unknown.

### Knowledge Lifecycle Responsibilities

Knowledge Lifecycleは以下の時間的状態を管理する。

- Temporal state
- Freshness
- Verification history
- Validity period
- Supersession relationship
- Historical preservation

誰または何が更新・検証・承認するかは、この責務定義に含めない。

### Relationship to Evidence Engine

Evidence Engineは、現在のConsultationに適したEvidenceを選択・順位付けする。

Future conceptual ranking:

```text
Pattern Match
× Evidence Quality
× Freshness
× Environment Match
× Verification Score
```

これは概念式であり、確定した数学的実装ではない。Weight、Threshold、Scoring AlgorithmはこのDecisionで定義しない。

Recommendation EngineはPattern MatchingとRelevant Evidenceを用いてRecommendationを生成し、Diagnosis Reportへ時間的Contextを渡す。

### Boundaries

このDecisionは以下を定義しない。

- Knowledgeを更新する主体
- User、Administrator、AI Agent、External Sourceの役割分担
- External Product Changesの検出方法
- Reverification Request
- UpdateのApprove、Reject、Rollback
- Evidence Conflict Governance
- Review Schedule
- TrustまたはReputation Model
- Moderation Workflow
- Automated Web Monitoring
- Source Ingestion Policy

### Knowledge Governance & Renewal

**Status: Open / Future Design — Not Frozen**

Temporal Knowledge Architecture defines how time-aware knowledge is represented and consumed.

Knowledge Governance & Renewal will separately define who or what updates, verifies, approves, and retires that knowledge.

詳細は [Knowledge Governance & Renewal Open Issue](12_OPEN_ISSUE_KNOWLEDGE_GOVERNANCE_RENEWAL.md) を参照する。
