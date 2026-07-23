# AISA Architecture Overview

- Status: Living Overview
- Updated: 2026-07-24
- Related decisions: [ADR-0011 and ADR-0012](03_DECISIONS.md)

## Purpose

AISA is an AI-powered consultation and collective knowledge platform.

相談をConsultation Contextへ構造化し、PatternとEvidenceを用いて説明可能なRecommendationを生成する。各相談から得られる構造化Knowledgeは、User Consentなど将来定義されるBoundaryを経て、次の相談へ役立つKnowledgeになり得る。

## Frozen Conceptual Architecture

```text
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
Pattern Engine
↓
AISA LABO
↓
Knowledge Lifecycle
↓
Evidence Engine
↓
Recommendation Engine
↓
Diagnosis Report
```

Knowledge Unknown remains:

```text
No sufficient Pattern or Evidence
↓
Knowledge Unknown
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
```

## Components

### Consultation Navigator

Userとの対話、Question選択、Answer Validation、Consultation Context生成、Information Unknown検出を担う。診断結果は決定しない。

### Consultation Context

会話履歴そのものではなく、Recommendation Engineが扱える標準化された相談情報である。

### Pattern Engine

Consultation Contextに適合するDiagnostic Pattern候補を扱う概念的責務である。既存Version 0.0.1では、この責務はRecommendation EngineのPattern Matchingとして実装されている。今回、Runtime Componentの分割は行わない。

### AKE

既存Frozen ArchitectureにおけるKnowledgeの中心であり、Diagnostic Patterns、Question Catalog、Navigation Rules、Reference Dataを論理的に保持する。AISA LABOはAKEを無効化せず、Case/Evidenceの収集・提示を担うCollective Knowledge領域として拡張する。

### AISA LABO

UI name: **AISA LABO**

Subtitle: **みんなの知見ライブラリ**

匿名化・構造化された成功および失敗のConsultation Casesを、PatternやTagと関連付けて収集・提示するCurated Knowledge Libraryである。Bulletin Board、Social Feed、Forumではない。

### Knowledge Lifecycle

KnowledgeのFreshness、Verification History、Validity、Supersession、Historical Preservationを管理する。Knowledgeを誰または何が更新・承認するかは [Knowledge Governance & Renewal](12_OPEN_ISSUE_KNOWLEDGE_GOVERNANCE_RENEWAL.md) の将来設計であり、未決定である。

### Evidence Engine

現在のConsultationに適したEvidenceを選択・順位付けする将来Componentである。

Conceptual ranking factors:

```text
Pattern Match
× Evidence Quality
× Freshness
× Environment Match
× Verification Score
```

WeightやAlgorithmは未定義である。Newer Knowledgeを自動的に優先しない。

### Recommendation Engine

Pattern MatchとRelevant EvidenceからRecommendationを生成する。将来はEvidenceのObserved時点、Freshness、Environment適合、Verification Historyを考慮し、時間的ContextをDiagnosis Reportへ渡す。

既存のAKE-first、rule-based、AI-independentなBeta EngineとUnknown handlingは維持する。

### Diagnosis Report

Recommendation、First Action、根拠、Unknown状態を表示する。将来はEvidenceがいつ・どのEnvironmentで観測され、現在どのFreshness Statusにあるかを説明できる。

## Compatibility with Existing Frozen Architecture

既存の以下のDecisionは変更しない。

- Structured Consultation
- Minimum Sufficient Context
- AKE-first Recommendation
- Diagnostic Patterns and Navigation Logic separation
- Information Unknown and Knowledge Unknown separation
- Unknown Route
- Rule-based Beta Diagnostic Engine

新Architectureは、Pattern Matching後のKnowledge/Evidenceを時間軸付きで扱う責務を追加する。既存文書の「Knowledge is stored only inside AKE」は、AKEがBusiness Knowledgeの中心であるという意味を維持する。AISA LABOは別の無関係なKnowledge Storeではなく、AKEのCollective Case/Evidence領域を収集・提示するProduct Experienceとして位置付ける。

## Runtime Boundary

Version 0.0.1の実装は、Python standard library、JSON files、in-memory sessionsによるVertical Slice 0である。AISA LABO、Knowledge Lifecycle、Evidence Engineは、このOverviewだけではRuntime実装済みを意味しない。

最小実装計画は [IWP-0002](11_IWP_0002_AISA_LABO_FOUNDATION.md) を参照する。
