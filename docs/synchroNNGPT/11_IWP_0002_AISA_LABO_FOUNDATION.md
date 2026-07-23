# IWP-0002 — Introduce AISA LABO Foundation

- Status: Proposed / Not Implemented
- Architecture basis: ADR-0011, ADR-0012
- Runtime target: Existing Python standard library + JSON + Memory application

## Objective

Full Evidence EngineまたはKnowledge Governance Systemを実装せず、AISA LABOの最小で可視的なFoundationを導入する。

## Context

AISA Version 0.0.1は、Local Browser UIでConsultation Contextを生成し、Diagnostic Pattern MatchからDiagnosis ReportまたはKnowledge Unknownを表示するVertical Slice 0を実装済みである。

次のSmall Startとして、成功・失敗のFictional/Demo Consultation Casesを閲覧でき、Temporal MetadataとFreshness Statusを認識できる最小画面を追加する。

## Scope

- AISA LABO screenまたはlocal route
- Subtitle: `みんなの知見ライブラリ`
- 適切な既存画面からのNavigation
- Local fictional/demo consultation cases
- 成功例を最低1件
- 失敗例を最低1件
- Case fields:
  - ID
  - Category
  - Technologies
  - Observed date
  - Freshness status
  - Summary
  - Outcome
- Similar-case browsingまたはCase list presentation
- 明確なFreshness表示
- HistoricalまたはStale ExampleをText/Statusで視覚的に区別
- 現在のJSON + Memory Runtimeに整合するLocal Data Model
- Data loadingとprimary route/viewのTests
- Future Extension PointsのDocumentation
- すべてのSample CaseをFictional/Demo Dataと明示

## Out of Scope

- Real multi-user storage
- Authentication
- Public posting
- Full anonymization engine
- Personal data processing
- Production database
- Evidence scoring algorithm
- Automatic Knowledge updates
- External information ingestion
- Knowledge Governance & Renewal
- Moderator or administrator workflow
- Full recommendation integration
- Network services unless already required by existing architecture
- New framework、cloud service、database、dependency

## Tasks

1. Existing static UIとHTTP routingに沿ってAISA LABO routeを追加する。
2. Existing screenからAISA LABOへの最小Navigationを追加する。
3. Fictional/Demo Case用JSONを追加する。
4. Existing catalog loading conventionに沿ってCase loaderを追加する。
5. Case listへCategory、Technologies、Observed Date、Freshness Status、Summary、Outcomeを表示する。
6. Success CaseとFailure Caseを最低1件ずつ用意する。
7. STALEまたはHISTORICAL Caseを明確に表示する。
8. Sampleがreal user evidenceではないことを画面とDataで明示する。
9. Data loading testとHTTP route/view testを追加する。
10. Vertical Slice 0、Knowledge Unknown、existing testsにRegressionがないことを確認する。
11. Future Evidence EngineおよびKnowledge LifecycleへのExtension PointをDocumentする。

## Deliverables

- AISA LABO local screen/route
- Existing UIからのNavigation
- Fictional/Demo case JSON
- Case data loader
- Freshness-aware case presentation
- Success/Failure examples
- Automated tests
- Runtime/extension documentation update

## Acceptance Criteria

- Local executionだけでAISA LABOへアクセスできる。
- `AISA LABO` と `みんなの知見ライブラリ` が表示される。
- SuccessとFailureのFictional/Demo Caseが最低1件ずつ表示される。
- Category、Technologies、Observed Date、Freshness Status、Summary、Outcomeが確認できる。
- STALEまたはHISTORICAL CaseがWarning/Text/Statusで明確に区別される。
- Sample dataはreal user evidenceではないと明示される。
- New dependency、database、authentication、network serviceを追加しない。
- Existing Vertical Slice 0が引き続き動作する。
- Existing Knowledge Unknown handlingが引き続き動作する。
- Data loadingとprimary route/viewのTestsが成功する。

## Definition of Done

- Scope内のTasksとDeliverablesが完了している。
- Acceptance Criteriaがすべて検証されている。
- 全Relevant Testsが成功している。
- Architecture Frozen Decisionsを変更していない。
- Out of Scope項目を実装していない。
- Fictional/Demo Data以外を収集・公開していない。
- Completion Reportが作成されている。
- AgreeとAlignをReview可能な状態で提示している。

## Future Extension Points

- Knowledge LifecycleによるFreshness/Validity/Supersession管理
- Evidence EngineによるCase selection/ranking
- Recommendation EngineへのRelevant Evidence integration
- Diagnosis ReportへのTemporal Explanation
- AI CuratorによるCase discovery
- Knowledge Governance & Renewal（別Architecture設計）

これらはIWP-0002の実装Scopeではない。

## Completion Report Format

1. Summary
2. Files created
3. Files modified
4. Scope completed
5. Out-of-scope confirmation
6. Sample data declaration
7. Tests added or updated
8. Commands executed
9. Test results
10. Vertical Slice 0 verification
11. Knowledge Unknown verification
12. Architecture conflicts or ambiguities
13. Unresolved items
14. Agree
15. Align
16. Git status and commit
