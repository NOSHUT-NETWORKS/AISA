# AISA Project Brief

## Project

AISA — AI Solution Architect

## Description

AISA is an **AI-powered consultation and collective knowledge platform**.

AISAの目的はGeneric Chatではない。Structured Consultationを通じてConsultation Contextを構築し、Diagnostic PatternsとRelevant Evidenceを用いて、説明可能なRecommendationを生成する。

AISA LABOは、匿名化・構造化されたConsultation Casesを将来の相談へ活用する、Curated Knowledge Libraryである。

## Core Principles

- Cost First
- Explainable
- Local First
- Structured Consultation
- Architecture before AI
- Every consultation becomes knowledge for the next consultation.
- Knowledge evolves.
- AISA evolves with knowledge.

Japanese principles:

- ひとつの相談が、次の誰かの力になる。
- 知識は完成しない。
- 知識は育ち続ける。
- AISAは知識とともに進化する。

## Current State

- Implemented application version: 0.0.1
- Completed milestone: Vertical Slice 0 / IWP-0001
- First end-to-end consultation completed: 2026-07-23
- Current runtime: Local browser UI, Python standard library, JSON, in-memory sessions

「AISA Version 2 / Collective Intelligence」はConceptual Architecture GenerationとRoadmapを表す。現在実装済みのApplication Versionが2.0であることを意味しない。

## Current Consultation Flow

```text
Welcome
↓
Questions
↓
Consultation Context
↓
Pattern Match
↓
Diagnosis Report or Knowledge Unknown
```

## Collective Knowledge Direction

```text
Consultation
→ Pattern Engine
→ AISA LABO
→ Knowledge Lifecycle
→ Evidence Engine
→ Recommendation Engine
→ Diagnosis Report
```

## Development Principles

- NNGPT owns Architecture.
- Codex owns Implementation.
- Frozen Architecture must not be redesigned during implementation.
- If implementation requires an Architecture change, stop and report.
- Keep implementation simple.
- Avoid unnecessary abstractions and dependencies.
- Preserve Unknown handling.
- Do not represent fictional/sample cases as real Evidence.

## Current Next Work Package

[IWP-0002 — Introduce AISA LABO Foundation](11_IWP_0002_AISA_LABO_FOUNDATION.md)
