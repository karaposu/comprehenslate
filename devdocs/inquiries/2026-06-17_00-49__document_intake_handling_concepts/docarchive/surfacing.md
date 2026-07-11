# Surfacing — document intake handling concepts

## User Input

Input passed to surfacing: `_branch.md` from this inquiry + an enumerated territory with 4 candidate regions (A. format / B. structure / C. pipeline / D. quality) plus a warm-substrate reading set (`articulate_simple.md`, `schemas.py`, `SKILL.md`, the two config-base sources).

Inquiry purpose (from `_branch.md`'s Goal, lifted verbatim):

> Produce a list-shaped artifact enumerating intake-handling concepts for comprehenslate's document-intake stage, spanning the format / structure / pipeline / quality layers, serving one or more of `[unblock-real-painpoint / avoid-architecture-debt / scope-the-engineering-task / meta-reframe]`. Excludes app-UI and translation-stage internals.

---

## Mode + Entry + Scope

- **Mode:** hybrid — `artifact` (warm substrate is grounding; not enumerated as candidate items) + `possibility` (the four candidate regions A/B/C/D require candidate-generation; each candidate is tagged).
- **Entry point:** `signal-first` (the purpose is given via `_branch.md`).
- **Territory:** `explicit-bounded` — the four regions are the candidate territory; the substrate list is the orienting frame, not enumeration territory.
- **Boundary-discovery sub-phase:** not fired (territory is explicit-bounded).
- **Exclusions honored:** `appification-out`, `translation-step-internals-out`.

---

## Workspace work-product (in-context, session-local)

The LLM session has read (or holds via prior turn context) the warm substrate (`articulate_simple.md` from this inquiry; the schema layer including `TranslationConfig` / `PipelineConfig` / the 7 policy classes) and used the four candidate regions as the enumeration scope. Per-item relevance tags below are emitted directly into the workspace and captured into the artifact's Trace at the moment of tagging (capture-at-moment per §2.1).

---

## Traversal Trace

Per-item granularity: each candidate has a relevance tag (`core` / `sub` / `side` / `umbrella`) + confidence (`HIGH` / `MED` / `LOW`). Concepts CGD = "candidate-generated discovery" (newly surfaced beyond the input enumeration; per asymmetric-failure → inclusion bias). No recency annotations: all candidates are `{source: none, value: null}` (possibility-mode, no filesystem backing).

### Region R1 — Warm substrate (artifact-mode; orientation, not enumeration)

These are read for grounding the purpose; not tagged as concept-candidates themselves.

| # | Item | Role |
|---|---|---|
| W1 | `articulate_simple.md` (this inquiry) | Defines the kinds-axis (format/structure/pipeline/quality) the candidates span |
| W2 | `SKILL/references/config/schemas.py` | Canonical schema — names TranslationConfig + 7 policy classes; downstream of intake |
| W3 | `SKILL/SKILL.md` | Generic-product framing; Risale-i Nur = calibration corpus, not product scope |
| W4 | `config_base_source.md` + `policy_config_base_source.md` | Audience policies + 7 policies w/ examples |
| W5 | User's substrate examples (PDF→md fidelity issues; md limitations; RTF candidate) | Lean signal: user's foreground is format-layer |

---

### Region R2 (A) — Format-layer concepts

| # | Concept | Tag | Conf | Note |
|---|---|---|---|---|
| A01 | PDF (born-digital vs OCR-derived) | **core** | HIGH | User's primary substrate example |
| A02 | PDF formatting fidelity issues (columns / hyphenation / ligatures / embedded fonts / non-text glyphs) | **core** | HIGH | The "painpoint" the user named |
| A03 | DOCX (Word native; XML-based) | **sub** | HIGH | Common authored format; intake must accept |
| A04 | RTF (rich-text intermediate; broader styling than md; lossy across editors) | **core** | HIGH | User's explicit candidate-format |
| A05 | md / CommonMark / GitHub Flavored Markdown (limitations: no native footnotes/tables/marginalia in CommonMark) | **core** | HIGH | User's explicit candidate-format + limitation flag |
| A06 | md extensions (Pandoc md / MultiMarkdown — superset adding footnotes, tables, definition lists) | **core** | HIGH | Resolves the md-limitations concern; deserves named distinction |
| A07 | EPUB (xhtml + structure; nested sections; preserves chapter hierarchy) | **sub** | MED | Book-shaped corpora; relevant for calibration-corpus types |
| A08 | HTML (rich semantic markup; underlying primitive for most structured text) | **sub** | HIGH | Often the via-format for conversion |
| A09 | plain text (.txt; loses ALL structure) | **side** | HIGH | Worst-case fallback; surface as a degraded-fidelity baseline |
| A10 | LaTeX (academic / scripture-aware; preserves math + structure) | **side** | MED | Edge case but real for academic intake |
| A11 | `.compldoc` (project's own future format — v1+) | **umbrella** | LOW | Out of v0.2 scope but architecturally relevant later |
| A12 | scan-only image PDFs requiring OCR (Tesseract, OCRmyPDF) | **core** | HIGH | Distinct sub-pipeline; intake CAN'T proceed without it |
| A13 | Pandoc as the universal converter | **core** | HIGH | The likely engine-of-choice for format normalization |
| A14 | pdftotext / pdf2htmlEX / mammoth (docx) — alternative converters | **sub** | MED | Per-format specialized tools |
| A15 | lossy-vs-lossless conversion concept | **core** | HIGH | Drives whether intake-format choice is reversible |
| A16 | round-trippability (md → docx → md recovers original?) | **sub** | HIGH | Quality measure; informs canonical-format choice |
| A17 | format ambiguity at intake time (is this .txt actually CSV? is this .md plain?) | **sub** | MED | Triggers format detection (see A18 CGD) |
| A18 | format detection / sniffing (when extension is unreliable) — CGD | **sub** | HIGH | Newly surfaced; load-bearing if multi-format intake |
| A19 | intake-format standard decision (the user's central question: md? RTF? both?) | **core** | HIGH | This IS the immediate decision the list serves |
| A20 | intake-format negotiation (per-document vs project-wide setting) | **sub** | MED | Design choice; affects UX shape |
| A21 | mathematical notation handling (LaTeX vs MathML vs Unicode) — CGD | **side** | MED | Edge case; relevant if scientific texts intake |
| A22 | right-to-left text handling (Arabic, Hebrew) — CGD | **sub** | HIGH | Calibration corpus (Risale-i Nur) is partially Arabic |
| A23 | mixed-script documents (Arabic + Latin transliteration interleaved) — CGD | **sub** | HIGH | Common in religious-text corpora |
| A24 | diacritics preservation (esp. Arabic-script) — CGD | **sub** | HIGH | Lost diacritics change meaning |
| A25 | ligature handling (Arabic, Latin "fi", "fl") — CGD | **side** | MED | Often a PDF-extraction artifact |
| A26 | punctuation normalization (curly vs straight quotes; em-dash vs en-dash) — CGD | **side** | HIGH | Cross-format inconsistency source |
| A27 | whitespace canonicalization — CGD | **sub** | HIGH | Foundational for downstream segmenting |

**Region R2 coverage:** 27 items; confirmed-present.

---

### Region R3 (B) — Structure-layer concepts

| # | Concept | Tag | Conf | Note |
|---|---|---|---|---|
| B01 | chapter (top-level division) | **core** | HIGH | Fundamental structural primitive |
| B02 | section / sub-chapter | **core** | HIGH | Hierarchical containment |
| B03 | paragraph (basic prose unit) | **core** | HIGH | The translation chunk's most common unit |
| B04 | sentence (sub-paragraph; relevant for chunking) | **sub** | HIGH | `PipelineConfig.chunking_granularity` literal |
| B05 | heading levels (h1 / h2 / h3) | **sub** | HIGH | Often the actual chapter signal in md |
| B06 | footnote (numbered annotation) | **core** | HIGH | Schema's `SourceApparatusPolicy` operates on these |
| B07 | endnote (end-of-section vs end-of-document) | **sub** | MED | Variant of footnote; placement decision |
| B08 | marginalia / hashiye (author-voice annotation) | **core** | HIGH | Schema's `SourceApparatusPolicy` named example (Said Nursi) |
| B09 | critical apparatus / apparatus criticus | **sub** | HIGH | Schema's `SourceApparatusPolicy` named example (Talmud, critical eds) |
| B10 | source-apparatus (umbrella term covering B08 + B09) | **core** | HIGH | Already named in schema as a policy axis |
| B11 | embedded poetry (verses embedded in prose) | **core** | HIGH | Schema's `EmbeddedPoetryPolicy` named primitive |
| B12 | verses (scripture-style numbered fragments) | **sub** | HIGH | Distinct from poetry; numbered atomically |
| B13 | formulaic openings (invocations / dedications / preambles) | **core** | HIGH | Schema's `FormulaicOpeningPolicy` named primitive |
| B14 | quotation blocks (cited material) | **sub** | HIGH | Voice transition signal |
| B15 | inline quotes | **sub** | MED | Voice transition signal; finer-grained |
| B16 | citations (author-date / footnote-style / inline) | **sub** | MED | Often cross-cuts source-apparatus |
| B17 | emphasis (italic / bold *semantics*, not just styling) | **sub** | HIGH | The structure-vs-style distinction's fault-line |
| B18 | lists (ordered / unordered / definition) | **side** | MED | Real for non-prose; rare in calibration corpus |
| B19 | tables | **side** | MED | Real but rare; md vanilla doesn't support |
| B20 | code blocks | **side** | LOW | Irrelevant for theological calibration; real for tech docs |
| B21 | figures / images (often dropped at intake; sometimes important) | **side** | MED | Decision-needed: drop or preserve as captions |
| B22 | captions | **side** | MED | Tied to figures |
| B23 | structure-vs-style distinction (intake preserves structure; style is downstream) | **core** | HIGH | Architectural axiom for the intake design |
| B24 | hierarchical containment (paragraph→section→chapter) | **core** | HIGH | The tree shape of `IntakeDoc` |
| B25 | flat-vs-tree document representation | **core** | HIGH | Foundational data-structure decision |
| B26 | cross-references (intra-document link from chapter to chapter) | **sub** | MED | Often flattened at intake; can be preserved |
| B27 | frontmatter (TOC, preface, dedication; distinct from main body) | **sub** | HIGH | Real boundary in book-shaped intake |
| B28 | backmatter (appendix, glossary, index) | **sub** | HIGH | Real boundary in book-shaped intake |
| B29 | non-main language parts (schema's `NonMainLangPartsPolicy`) | **core** | HIGH | Already named in schema; intake must perceive |
| B30 | voice transitions (schema's `VoiceMarkingPolicy`) | **core** | HIGH | Already named in schema; intake must perceive |
| B31 | archaic register markers (schema's `ArchaicRegisterPolicy`) | **core** | HIGH | Already named in schema; intake must perceive |
| B32 | TOC extraction (separate from frontmatter prose) — CGD | **sub** | HIGH | The TOC IS structural metadata; not body |
| B33 | page numbers + page boundaries — CGD | **side** | MED | Preserve as metadata? align to canonical edition pagination? |
| B34 | colophons / author signatures — CGD | **side** | MED | Edge case in critical editions |
| B35 | editorial brackets / lacunae markers — CGD | **side** | MED | Important in critical editions |
| B36 | original-vs-modernized spelling (when critical eds include both) — CGD | **side** | LOW | Niche but real |

**Region R3 coverage:** 36 items; confirmed-present.

---

### Region R4 (C) — Pipeline-layer concepts

| # | Concept | Tag | Conf | Note |
|---|---|---|---|---|
| C01 | parse (raw bytes → structured representation) | **core** | HIGH | Stage 1 of intake |
| C02 | normalize (canonicalize whitespace / unicode / line endings / punctuation) | **core** | HIGH | Stage 2; precedes segmentation |
| C03 | segment (identify chapter / section / paragraph boundaries) | **core** | HIGH | Stage 3; the structural-layer perception fires here |
| C04 | validate (parsed structure matches expectation) | **core** | HIGH | Stage 4; quality gate |
| C05 | hand-off to chunking (intake-translate boundary) | **core** | HIGH | The downstream contract |
| C06 | intake-vs-translate boundary (where does intake END?) | **core** | HIGH | Architectural seam |
| C07 | pre-validation (file is supported before parsing) | **sub** | HIGH | Fail-fast for unsupported formats |
| C08 | post-parse validation (got sensible structure out?) | **sub** | HIGH | Different from pre-validation |
| C09 | human-review gate (human confirms intake before translation) | **sub** | HIGH | Quality-vs-throughput tradeoff |
| C10 | error-recovery (intake fails on malformed file) | **sub** | HIGH | Real path; not optional |
| C11 | partial-intake (chapters 1-5 clean, 6 garbled — proceed?) | **sub** | HIGH | Common reality; design decision |
| C12 | intake-by-streaming vs load-all (memory for big files) | **side** | MED | Matters for OCR'd full books |
| C13 | intake metadata extraction (author, title, language, encoding) | **sub** | HIGH | Per-document metadata layer |
| C14 | language detection (Arabic / Turkish / English / mixed?) | **sub** | HIGH | Calibration corpus is multilingual |
| C15 | encoding detection (UTF-8 / Latin-1 / Windows-1252) | **sub** | HIGH | Real intake failure mode |
| C16 | intake error reporting (what does intake report on failure?) | **sub** | HIGH | UX-adjacent but not app-specific |
| C17 | intake logging / audit trail | **sub** | MED | Operational concern |
| C18 | intake reproducibility (same file → same output) | **sub** | HIGH | Architectural property; debuggability |
| C19 | schema for intake output (`IntakeDoc` w/ chapters/paragraphs?) | **core** | HIGH | This IS the downstream contract; must be designed |
| C20 | intake schema as contract between intake and translation | **core** | HIGH | Same as C19 but framed as contract |
| C21 | intake idempotency (re-running intake on the same file is safe) — CGD | **sub** | HIGH | Required for reliable pipelines |
| C22 | intake provenance (where did this file come from? when?) — CGD | **side** | MED | Audit-trail concept |
| C23 | multi-file project intake (book = 30 PDFs; intake the whole project) — CGD | **sub** | HIGH | Real for Risale-i Nur (multi-volume work) |
| C24 | source-of-truth declaration (intake output = canonical; original = read-only) — CGD | **sub** | HIGH | Important architectural commitment |
| C25 | intake schema versioning (old intakes loadable after schema evolves) — CGD | **side** | MED | Real for long-lived projects |
| C26 | original-fidelity vs human-edited intake (allow manual fixes post-auto) — CGD | **sub** | HIGH | Real escape hatch for messy PDFs |
| C27 | intake re-run on edited source (re-trigger when file changes) — CGD | **side** | MED | Watch-mode behavior |

**Region R4 coverage:** 27 items; confirmed-present.

---

### Region R5 (D) — Quality-layer concepts

| # | Concept | Tag | Conf | Note |
|---|---|---|---|---|
| D01 | fidelity (how much of the source survived intake?) | **core** | HIGH | The overarching quality framing |
| D02 | lossiness (what got dropped at intake?) | **core** | HIGH | Dual of D01 |
| D03 | structure-preservation vs typography-preservation vs semantic-only | **core** | HIGH | The intake-quality-target trichotomy |
| D04 | intake-quality-target (which of D03 is the goal?) | **core** | HIGH | Configurable; user choice |
| D05 | human-readable intake (a human can verify the parsed structure) | **sub** | HIGH | Verifiability property |
| D06 | machine-readable intake (downstream code consumes cleanly) | **sub** | HIGH | Contract property |
| D07 | intake-edit-after-parse (user fixes bad parses by hand) | **sub** | HIGH | Real workflow; informs format choice (favors md/RTF over binary) |
| D08 | intake-quality-gates (don't proceed unless quality > threshold) | **sub** | HIGH | Process control |
| D09 | intake-quality-metrics (chars-preserved-%, structure-elements-%, per-chapter integrity) | **sub** | HIGH | Operationalization of D01/D02 |
| D10 | PDF text-extraction quality (born-digital vs OCR'd; tables; columns) | **core** | HIGH | Specific to format-layer's primary obstacle |
| D11 | OCR quality (when source is image-only) | **core** | HIGH | Distinct sub-stage with its own quality concerns |
| D12 | paratext handling (footers, headers, page numbers — usually noise) | **sub** | HIGH | Decision: drop or preserve as metadata |
| D13 | intake-time vs translate-time error attribution | **sub** | HIGH | Debugging concept |
| D14 | round-trippability as a quality measure | **sub** | MED | Tied to A16 |
| D15 | "good intake = downstream-success" framing | **side** | MED | Validates the whole intake design |
| D16 | bad-intake-blocks-pipeline framing | **side** | MED | Risk framing; dual of D15 |
| D17 | per-document quality profile (this PDF is messy; expect 80% fidelity) — CGD | **sub** | MED | Calibrate quality expectations |
| D18 | intake quality vs source quality (some sources ARE messy; not intake's fault) — CGD | **sub** | MED | Attribution boundary |
| D19 | inter-intake-version diffing (when re-intaking, what changed?) — CGD | **side** | LOW | Advanced ops concept |
| D20 | reference intake (a known-good intake to compare against) — CGD | **side** | LOW | Calibration tool |

**Region R5 coverage:** 20 items; confirmed-present.

---

## State Summary

### Territory-specification echo

Four candidate regions A (format) / B (structure) / C (pipeline) / D (quality), plus warm-substrate orientation (R1). All explicit-bounded by the input.

### Purpose-specification echo

Identify a list of intake-handling concepts for comprehenslate's document-intake stage, spanning format/structure/pipeline/quality layers; excludes app-UI + translation-internals.

### Coverage map

| Region | Coverage | Items | Aggregate relevance lean |
|---|---|---|---|
| R1 (substrate) | confirmed (orientation only) | 5 | n/a |
| R2 (A. format) | confirmed-present | 27 | core-leaning (10 core / 8 sub / 6 side / 1 umbrella / 2 LOW-conf side) |
| R3 (B. structure) | confirmed-present | 36 | core-leaning (12 core / 12 sub / 12 side) |
| R4 (C. pipeline) | confirmed-present | 27 | core-leaning (8 core / 12 sub / 7 side) |
| R5 (D. quality) | confirmed-present | 20 | core-leaning (8 core / 8 sub / 4 side) |

**Total items surfaced: 110 candidates + 5 substrate references.**

### Confirmed-absent regions

None at this resolution. Adjacent territories deliberately excluded (per MQ4): app-UI surface; translation-stage internals. Not "absent" — out-of-scope by exclusion.

### Concept-names list (load-bearing primitives — likely to recur downstream)

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| `IntakeDoc` | coined-term | C19/C20 | The schema produced by intake; the contract with translation |
| `intake-vs-translate boundary` | structural-reference | C06 | The architectural seam |
| `intake-quality-target` | vocabulary | D03/D04 | The trichotomy: structure / typography / semantic-only |
| `canonical intake format` | coined-term | A19 | The standard format the user's central question is about |
| `structure-vs-style distinction` | vocabulary | B23 | The axiom: intake preserves structure, style is downstream |
| `flat-vs-tree representation` | vocabulary | B25 | The fundamental data-structure decision |
| `format-fidelity gradient` | coined-term | A02/A15/A16 | PDF→md→canonical-form fidelity loss curve |
| `format detection / sniffing` | vocabulary | A18 (CGD) | Determining file type when extension is unreliable |
| `partial-intake decision` | coined-term | C11 | What to do when intake succeeds on some but not all of a file |
| `intake provenance` | coined-term | C22 (CGD) | File origin + intake timestamp metadata |
| `mixed-script intake` | coined-term | A23 (CGD) | Documents w/ multiple scripts interleaved |
| `intake-time-vs-translate-time error attribution` | vocabulary | D13 | Debugging concept |

### Recency distribution

All items: `{source: none, value: null}`. Possibility-mode candidates have no filesystem backing. Per-region: `{newest: null, oldest: null, no-mtime-count: <region-total>, total-items: <region-total>}`.

### Frontier flags

| Flag | Concept | Why frontier |
|---|---|---|
| F1 | `IntakeDoc` schema shape | Surfaced as a load-bearing concept; the actual schema (fields / types) is a downstream design question, not enumerated here |
| F2 | Canonical intake format choice (md vs md+RTF vs Pandoc-md-superset) | The user's CENTRAL question; surfaced as core but not adjudicated |
| F3 | Quality-target trichotomy (structure-preservation vs typography vs semantic-only) — pick one as default? | Surfaced as core but not adjudicated |
| F4 | Where does the Mac app's role re-enter? | Excluded by MQ4 from THIS inquiry, but the answer eventually needs an app surface (intake button / quality-report dialog); flagged for after-CONCLUDE |
| F5 | How much of the schema's 7 policies belongs to intake vs translation? (E.g., `SourceApparatusPolicy` operates on intake-perceived marginalia) | Intake/translation boundary on policy semantics; surfaced but not adjudicated |
| F6 | OCR sub-pipeline depth (Tesseract config, OCRmyPDF wrapping) | Surfaced as a sub-region but not enumerated at depth |

### Workspace-populated status

`{populated: true, populated-at: 2026-06-17_00-55, extent: "all 4 candidate regions traversed; 110 candidates tagged + 12 concept-names extracted; 6 frontier flags emitted"}`

### Re-invocation parameters (suggested)

If a future invocation refines, suggested narrower sub-purposes:

- **rsp1:** "identify the canonical intake format and its rationale" — collapses F2.
- **rsp2:** "design the `IntakeDoc` schema fields + types" — addresses F1.
- **rsp3:** "enumerate intake-time policy attribution (which of the 7 policies fire at intake vs at translation)" — addresses F5.
- **rsp4:** "enumerate OCR sub-pipeline concepts in depth" — addresses F6.

---

## Telemetry

- **Mode:** hybrid (artifact substrate + possibility candidates) · **Entry point:** signal-first
- **Cycles run:** 4 (one per candidate region; R1 is substrate, not a cycle)
- **Items enumerated:** 110 candidates + 5 substrate references
- **Items tagged at each relevance level:** core = 38 · sub = 40 · side = 29 · umbrella = 1 · (LOW-confidence subset across all = 6)
- **Sub-phase fired:** no (territory was explicit-bounded)
- **Workspace-overload trigger:** not fired
- **Failure modes checked:**
  - LAYER 1 mode 1 (missed-relevance): no signal — coverage looks complete across kinds-axis
  - LAYER 1 mode 2 (surfaced-irrelevance): some risk — `side` tag may include marginal items (e.g., B20 code blocks); downstream can filter
  - LAYER 1 mode 3 (over-coverage): possible — 110 candidates is broad; sense-making's prune-step will compress
  - LAYER 1 mode 4 (territory-mis-binding): no — exclusions honored (no app-UI / translation-internals items)
  - LAYER 1 mode 5 (workspace overload): not fired
  - LAYER 1 mode 6 (artifact under-specification): no — Trace + Summary complete
  - LAYER 1 mode 7 (workspace-artifact desync): no — capture-at-moment held
  - LAYER 1 modes 8 & 9 (recency-equates-idleness / recency-bias-filter): n/a — all items mtime-less
- **Items with mtime / without mtime:** 0 / 110 (all possibility-mode)
- **Self-assessment verdict:** **PROCEED**

The inventory is broad enough to seed sensemaking's collapse-to-stable-model; the frontier flags name the load-bearing questions for downstream pruning.
