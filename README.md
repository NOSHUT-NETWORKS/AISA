# AISA

AISAは、企業そのものではなく、一つの仕事・タスクを診断し、実行可能な改善案を提示するプロジェクトです。費用、時間、AI活用の観点から選択肢を整理し、無料、低価格、本格導入の順で現実的な提案を行います。

開発は **NNGPT Development Team** が担い、中心理念として「役割ではなく、価値で協働する」を掲げます。人とAIの役割を固定せず、その時点で最も価値を生み出せる主体が役割を担います。

## Principles

- Collaboration First
- Cost First
- Small Start
- Evolution over Perfection
- GitHubをSingle Source of Truthとする
- mainへの通常の直接コミットを禁止し、Pull Requestでレビューする
- レビューの共通語としてAgreeとAlignを用いる

## Shared context

[`docs/synchroNNGPT`](docs/synchroNNGPT/) は、CodexとNNGPTがAISA開発で共有する共通コンテキストです。組織理念、プロジェクト記憶、現在のSprint、意思決定、協働規約、Codex向けプロンプトをGitHub上で同期します。

---

## Current Status

✅ Sprint 0 Completed

Next:
Sprint 1 – AISA Core Diagnostic Framework

---

## AISA First Boot — Vertical Slice 0

IWP-0001は、AISAの最初のローカル実行版です。4つの選択式質問からConsultation Contextを生成し、AKEのDiagnostic Patternを検索してDiagnosis ReportまたはKnowledge Unknownを表示します。

### Requirements

- Windows
- Python 3.10以上
- Webブラウザ

外部Pythonパッケージ、AI API、データベースは不要です。

### Run

```powershell
python run.py
```

ブラウザで次を開きます。

```text
http://127.0.0.1:8000
```

ポートを変更する場合:

```powershell
python run.py --port 8080
```

### Test

```powershell
python -m unittest discover -s tests -v
```

### Vertical Slice 0 scope

- Local Web UI
- In-memory Session Manager
- Question Catalog
- Navigation Rules
- Consultation Context
- AKE-first Recommendation Engine
- Diagnostic Pattern Matching
- Diagnosis Report
- Knowledge Unknown Route
- Restart

次は対象外です。

- AI／LLM
- 自由回答の理解
- データベース
- 認証
- Cloud／Docker必須環境
- 管理画面／Pattern Editor
