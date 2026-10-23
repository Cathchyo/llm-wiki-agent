# LLM Wiki Agent — Schema & Workflow Instructions

This wiki is maintained entirely by your coding agent. No API key or Python scripts needed — just open this repo in Codex, OpenCode, or any agent that reads this file, and talk to it.

## How to Use

Describe what you want in plain English:
- *"Ingest this file: raw/papers/my-paper.md"*
- *"What does the wiki say about transformer models?"*
- *"Check the wiki for orphan pages and contradictions"*
- *"Build the knowledge graph"*

Or use shorthand triggers:
- `ingest <file>` → runs the Ingest Workflow
- `query: <question>` → runs the Query Workflow
- `health` → runs the Health Workflow (fast, every session)
- `lint` → runs the Lint Workflow (expensive, periodic)
- `build graph` → runs the Graph Workflow

---

## 输出风格

- **结论优先**：开头直接说明结果或核心判断，不先复述问题和过程。
- **精简准确**：使用短句和具体措辞，删除客套话、重复内容及无关背景。
- **重点突出**：按重要性排列信息；核心观点尽量控制在 3 条以内。
- **便于扫描**：复杂内容使用简短列表；必要时用加粗标出关键词，避免过度排版。
- **按需展开**：默认只提供理解和决策所需的信息，用户要求时再补充细节。
- **明确状态**：执行任务后简要说明完成了什么、验证结果以及仍存在的风险或阻塞。
- **不牺牲完整性**：精简不能遗漏关键限制、风险、错误或需要用户决定的事项。

## 原文忠实与证据要求

- **忠于原文**：解读论文或其他资料时，以实际读取的原文为依据，不得编造作者观点、研究动机、方法步骤、参数、结果或引文。
- **明确未知**：原文未提到的内容应说明“原文未提到”；尚未核实或无法确定的内容应说明“不知道”或“尚未核实”，不得用猜测补成事实。
- **区分事实与解释**：明确区分原文陈述、个人推断和教学比喻。虚构的示例数据必须标明为教学示例，不得当作论文实验结果；通俗解释不得改变原意或省略影响理解的关键条件。
- **提供可核查依据**：关键判断、方法差异和数值应指向原文的章节、公式、表图或文件位置；使用外部资料时明确标注来源，不得冒充当前论文的内容。

---

## WeChat Topic Judgment Workflow

This repository is also used to train topic-selection judgment for a WeChat
Official Account. Keep this workflow small: make a forecast, receive comparable
feedback, and update one judgment at a time.

### Triggers

- `记录选题：<话题>` or `topic: <topic>` -> run the Topic Decision Workflow
- `记录结果：<topic_id>` or `result: <topic_id>` -> run the Topic Result Workflow
- `复盘选题` or `review topics` -> run the Topic Review Workflow

### Three Feedback Questions

1. Did people choose to open it? Use delivered-read rate when available.
2. Did people find it worth sharing or saving? Use shares and favorites per reader.
3. Did it attract the right audience? Use new follows per 1,000 readers.

Total reads and recommendation exposure are context, not proof that the original
topic judgment was correct.

### Topic Decision Workflow

1. Create a stable `topic_id` in the form `YYYYMMDD-NN`.
2. Before publication, create `raw/topic-decisions/<topic_id>-<slug>.md` from
   `templates/topic-decision.md`.
3. Capture the reason and low/medium/high forecasts for opening, sharing/saving,
   and following. Do not demand extra fields.
4. Treat the saved decision as immutable. Later changes belong in a result or
   review record, never in the original forecast.
5. Ingest it as a source page tagged `topic-decision`, preserving `topic_id`.

### Topic Result Workflow

1. Create `raw/topic-results/<topic_id>-result.md` from
   `templates/topic-result.md`. Never add outcomes to the decision file.
2. Accept a pasted export, screenshot transcription, counts, or calculated rates.
   Missing metrics remain explicitly `unknown`.
3. Calculate only when denominators exist:
   - delivered-read rate = readers / delivered users
   - share-save rate = (sharers + favorites) / readers
   - follows per 1,000 readers = new follows / readers * 1000
4. Compare with the forecast. Mark each judgment `supported`, `not supported`, or
   `inconclusive`.
5. Write one short update for the next selection. Never infer a stable rule from
   one article.
6. Ingest it as a source page tagged `topic-result`, preserving `topic_id` and
   linking it to the paired decision page.

### Topic Review Workflow

Run after at least five results unless the user requests an earlier review.

1. Read all decision/result pairs and group comparable topics.
2. Identify judgments repeatedly supported, contradicted, or still uncertain.
3. Update concept pages for recurring hypotheses with evidence, counterexamples,
   confidence, and boundary conditions.
4. Save a synthesis only with user approval. End with one hypothesis to test next.

## Directory Layout

```
raw/          # Immutable source documents — never modify these
review/       # Human-review staging area — nothing here is part of the wiki yet
wiki/         # Agent owns this layer entirely
  index.md    # Catalog of all pages — update on every ingest
  log.md      # Append-only chronological record
  overview.md # Living synthesis across all sources
  sources/    # One summary page per source document
  entities/   # People, companies, projects, products
  concepts/   # Ideas, frameworks, methods, theories
  syntheses/  # Saved query answers
graph/        # Auto-generated graph data
tools/        # Standalone Python scripts
  health.py   # Structural checks (deterministic, no LLM calls)
  lint.py     # Content quality checks (uses LLM for semantic analysis)
  build_graph.py  # Knowledge graph generation
```

---

## Page Format

Every wiki page uses this frontmatter:

```yaml
---
title: "Page Title"
type: source | entity | concept | synthesis
tags: []
sources: []       # list of source slugs that inform this page
last_updated: YYYY-MM-DD
---
```

Use `[[PageName]]` wikilinks to link to other wiki pages.

### Obsidian Compatibility

- Keep every wiki page filename stem unique across `wiki/`.
- Internal knowledge links must use the exact filename stem: `[[PageName]]`.
- Do not use path-qualified links such as `[[concepts/PageName]]`.
- Do not use aliases or heading/block links such as `[[PageName|label]]`,
  `[[PageName#Heading]]`, or `[[PageName^block]]`; the current lint and graph
  tools treat those as different page names.
- Standard Markdown links may be used for index navigation, attachments, and
  external URLs, but only `[[PageName]]` links become knowledge-graph edges.
- Obsidian is a viewing and exploration layer. Preserve the rule that `raw/`
  source records are immutable after creation.

---

## Wiki 入库人工审核门禁

任何内容从原始文档进入 `wiki/` 前，都必须经过用户逐步审核。未经明确批准，不得创建或修改 `wiki/` 页面，也不得更新 `wiki/index.md`、`wiki/overview.md` 或 `wiki/log.md`。

按以下顺序执行，每一步完成后必须停止并等待用户审核：

1. **原始资料准备**：读取或转换文件并放入 `raw/`，报告文件和转换状态；等待用户确认原始资料完整、可读。
2. **预读摘要**：在 `review/` 中创建待审摘要，优先说明背景和任务，简述行动与结果；等待用户审核事实和表述。
3. **入库方案**：摘要获批后，在 `review/` 中列出拟创建或修改的来源页、实体页、概念页、链接、标签、概览和矛盾记录；等待用户逐项批准。
4. **正式入库**：只有用户明确表示“审核通过”“批准进入 Wiki”或同等意思后，才能把已批准内容写入 `wiki/` 并更新索引、概览和日志。
5. **入库后校验**：完成结构检查并向用户提交变更摘要；不得在校验阶段擅自加入未经审核的新判断。

用户提出修改意见只表示需要修订，不等同于批准。修订稿仍须保留在 `review/`，再次获得明确批准后才能进入下一步。若一次处理多篇文档，可以合并成一个审核文件，但每篇文档的结论必须能被单独审核。

---

## Ingest Workflow

Triggered by: *"ingest <file>"*

**Supported formats:** Markdown (`.md`) is ingested directly. Non-markdown files (`.pdf`, `.docx`, `.pptx`, `.xlsx`, `.html`, `.txt`, `.csv`, `.json`, `.xml`, `.rst`, `.rtf`, `.epub`, `.ipynb`, `.yaml`, `.yml`, `.tsv`, `.wav`, `.mp3`) are auto-converted to markdown via [markitdown](https://github.com/microsoft/markitdown) before ingestion. Use `--no-convert` to skip auto-conversion.

The steps below are the formal promotion phase. Run them only after completing the mandatory human-review gates above and receiving explicit approval.

Steps (in order):
1. Read the source document fully (auto-convert if non-markdown)
2. Read `wiki/index.md` and `wiki/overview.md` for current wiki context
3. Write `wiki/sources/<slug>.md` — use the source page format below
4. Update `wiki/index.md` — add entry under Sources section
5. Update `wiki/overview.md` — revise synthesis if warranted
6. Update/create entity pages for key people, companies, projects mentioned
7. Update/create concept pages for key ideas and frameworks discussed
8. Flag any contradictions with existing wiki content
9. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <Title>`
10. **Post-ingest validation** — check for broken `[[wikilinks]]`, verify all new pages are in `index.md`, print a change summary

### Source Page Format

```markdown
---
title: "Source Title"
type: source
tags: []
date: YYYY-MM-DD
source_file: raw/...
---

## Summary
2–4 sentence summary.

## Key Claims
- Claim 1
- Claim 2

## Key Quotes
> "Quote here" — context

## Connections
- [[EntityName]] — how they relate
- [[ConceptName]] — how it connects

## Contradictions
- Contradicts [[OtherPage]] on: ...
```

### Domain-Specific Templates

If the source falls into a specific domain (e.g., personal diary, meeting notes), the agent should use a specialized template instead of the default generic one above:

#### Diary / Journal Template
```markdown
---
title: "YYYY-MM-DD Diary"
type: source
tags: [diary]
date: YYYY-MM-DD
---
## Event Summary
...
## Key Decisions
...
## Energy & Mood
...
## Connections
...
## Shifts & Contradictions
...
```

#### Meeting Notes Template
```markdown
---
title: "Meeting Title"
type: source
tags: [meeting]
date: YYYY-MM-DD
---
## Goal
...
## Key Discussions
...
## Decisions Made
...
## Action Items
...
```

---

## Query Workflow

Triggered by: *"query: <question>"*

Steps:
1. Read `wiki/index.md` to identify relevant pages
2. Read those pages
3. Synthesize an answer with inline citations as `[[PageName]]` wikilinks
4. Ask the user if they want the answer filed as `wiki/syntheses/<slug>.md`

---

## Lint Workflow

Triggered by: *"lint"*

Check for:
- **Orphan pages** — wiki pages with no inbound `[[links]]` from other pages
- **Broken links** — `[[WikiLinks]]` pointing to pages that don't exist
- **Contradictions** — claims that conflict across pages
- **Stale summaries** — pages not updated after newer sources
- **Missing entity pages** — entities mentioned in 3+ pages but lacking their own page
- **Sparse pages** — pages with fewer than 2 outbound `[[wikilinks]]` (link density budget)
- **Data gaps** — questions the wiki can't answer; suggest new sources

Graph-aware checks (require `graph.json` from `build graph`):
- **Hub stubs** — god nodes (degree > μ+2σ) with thin content (< 500 chars)
- **Fragile bridges** — community pairs connected by only 1 edge
- **Isolated communities** — clusters with zero external connections

Output a lint report and ask if the user wants it saved to `wiki/lint-report.md`.

---

## Health Workflow

Triggered by: *"health"*

Run: `python tools/health.py` (or `python tools/health.py --json` for machine-readable output)

Fast structural integrity checks — **zero LLM calls**, safe to run every session:
- **Empty / stub files** — pages with no content beyond frontmatter (rate-limit damage)
- **Index sync** — `wiki/index.md` entries vs actual files on disk
- **Log coverage** — source pages missing a corresponding `ingest` entry in `wiki/log.md`

Output a health report. Use `--save` to write to `wiki/health-report.md`.

### Health vs Lint Boundary

| Dimension | `health` | `lint` |
|---|---|---|
| **Scope** | Structural integrity | Content quality |
| **LLM calls** | Zero | Yes (semantic analysis) |
| **Cost** | Free | Tokens |
| **Frequency** | Every session, before other work | Every 10-15 ingests |
| **Checks** | Empty files, index sync, log sync | Orphans, broken links, contradictions, gaps |
| **Tool** | `tools/health.py` | `tools/lint.py` |
| **Run order** | First (pre-flight) | After health passes |

> Run `health` first — linting an empty file wastes tokens.

---

## Graph Workflow

Triggered by: *"build graph"*

First try: `python tools/build_graph.py --open`

If Python/deps unavailable, build manually:
1. Search for all `[[wikilinks]]` across wiki pages
2. Build nodes (one per page) and edges (one per link)
3. Infer implicit relationships not captured by wikilinks — tag `INFERRED` with confidence score; low confidence → `AMBIGUOUS`
4. Write `graph/graph.json` with `{nodes, edges, built: date}`
5. Write `graph/graph.html` as a self-contained vis.js visualization

---

## Naming Conventions

- Source slugs: `kebab-case` matching source filename
- Entity pages: `TitleCase.md` (e.g. `OpenAI.md`, `SamAltman.md`)
- Concept pages: `TitleCase.md` (e.g. `ReinforcementLearning.md`, `RAG.md`)

## Index Format

```markdown
# Wiki Index

## Overview
- [Overview](overview.md) — living synthesis

## Sources
- [Source Title](sources/slug.md) — one-line summary

## Entities
- [Entity Name](entities/EntityName.md) — one-line description

## Concepts
- [Concept Name](concepts/ConceptName.md) — one-line description

## Syntheses
- [Analysis Title](syntheses/slug.md) — what question it answers
```

## Log Format

`## [YYYY-MM-DD] <operation> | <title>`

Operations: `ingest`, `query`, `health`, `lint`, `graph`, `report`

---

## Graph Health Report

Triggered by: *"graph report"* or `python tools/build_graph.py --report`

The `--report` flag generates a structured graph health report covering:
- **Health summary** — edges/node ratio, orphan %, community count, link density
- **Orphan nodes** — pages with zero graph connections
- **God nodes** — hub pages with degree > μ+2σ (disproportionate connectivity)
- **Fragile bridges** — community pairs connected by only 1 edge
- **Phantom hubs** — `[[wikilinks]]` referenced by 2+ existing pages but pointing to non-existent pages (page creation signals)

Use `--save` to write the report to `graph/graph-report.md`.

---

## Phase 3 Design Constraints (Auto-Linking — Open)

Phase 3 proposes automatic `[[wikilink]]` insertion based on graph analysis. The following hard rules apply:

### Promotion Gate: `draft → stable`
- Auto-linked edges start as `DRAFT` (visible in graph, not written to page body)
- A dedicated `promote` pass validates source grounding + consistency
- Only edges that pass get materialized as `[[wikilinks]]` in the page
- **Link density budget**: a page must have ≥2 outbound wikilinks before promotion

### Hard Rules
| ID | Rule | Rationale |
|---|---|---|
| HG-WA-01 | Graph layer MUST NOT auto-create pages from broken links — report only | LLM ingest produces hallucinated wikilinks; auto-creating amplifies noise |
| HG-WA-02 | New slash commands MUST NOT duplicate existing command coverage | Prevents user confusion; merge into existing commands instead |
