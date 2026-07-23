# Architecture Open Issue — Knowledge Governance & Renewal

- Status: Open / Future Design
- Frozen: No
- Created: 2026-07-24

## Provisional Title

Knowledge Governance & Renewal

## Purpose

Temporal Knowledge Architecture defines how time-aware knowledge is represented and consumed.

Knowledge Governance & Renewal will separately define who or what updates, verifies, approves, and retires that knowledge.

## Why This Is Intentionally Deferred

Knowledgeの時間的表現と利用方法はFrozenできるが、更新主体、Approval Authority、Trust、Moderation、External SourcesにはPrivacy、Safety、Operations、Product Policy上の追加判断が必要である。

これらを現在のIWPで推測すると、未合意のGovernance RuleをArchitectureへ固定してしまう。そのため、本IssueではQuestionを記録するだけとし、Answer、Workflow、Role、Schedule、Algorithmを決定しない。

## Unresolved Questions

- Who is responsible for updating Knowledge?
- Are updates performed by users, administrators, AI agents, external sources, or a combination?
- How are external product changes detected?
- How is reverification requested?
- Who approves, rejects, or rolls back updates?
- How are conflicts between Evidence governed?
- Are review schedules required, and if so, how are they determined?
- Are trust or reputation models required?
- What moderation workflows are appropriate?
- Should automated web monitoring exist?
- What source ingestion policies are required?
- How is consent represented and withdrawn?
- What anonymization and privacy review is required before registration?
- What audit trail is required for update, verification, supersession, and retirement?

## Explicit Non-Decisions

This Open Issue does not define or implement:

- Update ownership
- Approval authority
- Automated agents
- External monitoring
- Review schedules
- Trust scoring
- Moderation workflow
- Source policy
- Conflict resolution
- Rollback behavior

## Relationship

- [ADR-0012](03_DECISIONS.md) defines the Temporal Knowledge representation and consumption boundary.
- [Architecture Overview](08_ARCHITECTURE_OVERVIEW.md) identifies Knowledge Lifecycle responsibilities without assigning governance roles.
- [Version 2 Roadmap](10_VERSION_2_ROADMAP.md) lists this item without a version or implementation date.
- [IWP-0002](11_IWP_0002_AISA_LABO_FOUNDATION.md) explicitly excludes it.
