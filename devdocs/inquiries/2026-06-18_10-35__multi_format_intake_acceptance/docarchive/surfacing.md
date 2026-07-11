# Surfacing — multi-format intake acceptance

## User Input

Source: `_branch.md`. Upstream articulation: `articulate_simple.md`. CONTINUES FROM: `devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/finding.md` (this inquiry REFINES that finding's format-priority + DEFERRED 1).

Critical framing: 8-category preprocessing pipeline settled; HTML5 canonical settled; format priority = EPUB-first + PDF-fallback for v0.2 with txt/md/Word/plain-text DEFERRED. User asks whether intake should ACCEPT txt + md + pdf + epub (all 4) with EPUB CHOSEN for complex content.

---

## Mode + Entry Point

- **Mode:** `possibility` — the territory is the design space of format-acceptance + routing policy.
- **Entry-point:** `signal-first` — purpose given.
- **Territory spec:** `explicit-bounded` via 10 sub-regions (A-J).
- **Boundary-discovery sub-phase:** skipped.

---

## Traversal Trace

Relevance legend per §2.3: core / sub / side / umbrella. Confidence: H/M/L. Recency: all `{source: none, value: null}` (possibility-mode).

### Sub-region A — Per-format fidelity analysis

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| A1 | EPUB structural fidelity (h1-h6 hierarchy; lang/dir spans; semantic markup; CSS; aside/figure/blockquote; OPF metadata) | core | H | The reference high-fidelity input format; matches HTML5 canonical structure 1:1 |
| A2 | PDF structural fidelity (text-layer + layout + sometimes styling; OCR-recoverable; structure usually lost) | core | H | Lower fidelity; requires Category 6 PDF path (bidi-fix; OCR; italic recovery) |
| A3 | Markdown (Pandoc md with extensions) structural fidelity (ATX/setext headings; fenced divs for class; bracketed_spans for lang=; footnotes via extension; tables; lists) | core | H | Most structural features reachable via Pandoc extensions; some workarounds required |
| A4 | Plain txt structural fidelity (no headings; no metadata; no spans; only line/paragraph breaks inferrable from blank lines) | core | H | Minimum fidelity; Categories 1 + 2 + 4 + 7 only; structural detection impossible |
| A5 | Word (.docx) structural fidelity (styles → headings; runs; tables; embedded media; metadata) | sub | M | Comparable to EPUB but DEFERRED per prior finding; not in user's named set |
| A6 | RTF structural fidelity (text + styling but structure lost) | side | L | Editor-fragile per prior canonical-format finding |
| A7 | HTML5 directly as input (same as EPUB content document) | sub | M | EPUB IS xhtml5 packaged; direct HTML5 is essentially an unwrapped EPUB |

### Sub-region B — Routing-mechanism options

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| B1 | User-names-format-at-intake-time (CLI flag --format epub; UI dropdown) | sub | H | Explicit user input; lowest implementation cost |
| B2 | Auto-detect by file extension (.epub / .pdf / .md / .txt) | core | H | Standard practice; default expectation |
| B3 | Auto-detect by magic bytes (ignore extension; inspect header) | sub | H | Robust against mis-named extensions; minor overhead |
| B4 | Hybrid: extension first, magic bytes as verification | core | H | Best-of-both; standard for file-handling toolchains |
| B5 | User-must-confirm (auto-detect proposes; user confirms) | side | M | UI friction; appropriate when stakes are high |
| B6 | Reject-non-EPUB-for-complex-content (hard error) | side | L | Violates user-agency; over-restrictive |
| B7 | Warn-and-degrade (process the file but emit quality flag) | core | H | Honors user agency while signaling fidelity limits |
| B8 | Per-format quality-tier exposed at UI ("EPUB recommended" with override) | core | H | Mac app UI surface — informational guidance, not enforcement |

### Sub-region C — Complex-content detection heuristics

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| C1 | Multi-alphabet content (Latin + Arabic + Greek + Hebrew + etc.) | sub | H | The user's named exemplar; Unicode-range detection |
| C2 | Embedded apparatus (footnotes / marginalia / endnotes) | sub | H | Risale-i Nur hashiye case |
| C3 | Structural depth (multiple heading levels; sub-sections) | sub | M | Hierarchy depth as complexity signal |
| C4 | Mixed-direction text (LTR + RTL) | sub | H | Implies bidi handling requirements |
| C5 | Italic / bold styling significant | sub | M | Plain text loses; markdown supports; EPUB preserves |
| C6 | Special typography (drop-caps; letter-spaced emphasis; verse blocks) | side | M | Edge cases requiring specific representation |
| C7 | Citation-heavy academic content | sub | M | Footnote + cross-reference structure |
| C8 | Tables / figures | side | M | Structural primitives that txt cannot represent |
| C9 | The "complex content" concept itself as a runtime detection (vs static / per-source declaration) | core | H | Could be detected at intake-time from source preview, OR declared by user, OR documented as guidance — design choice |

### Sub-region D — Prior finding's DEFERRED 1 re-examination

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| D1 | DEFERRED 1's exact wording: "Word + plain-text format support" | core | H | The prior committed this DEFERRED list |
| D2 | "plain-text" ambiguity — did this mean .txt? .md? both? | core | H | Critical clarification; the prior didn't disambiguate |
| D3 | DEFERRED 1's revival trigger: "project source-mix expands" | core | H | The user's CURRENT question IS a source-mix expansion signal |
| D4 | "Accepted" vs "DEFERRED" semantic — the prior never said txt/md UNACCEPTABLE | core | H | Distinction may resolve question without overturning |
| D5 | Pandoc reads md as primary input format (md is Pandoc-native) | core | H | The DEFERRED wording for md may have been about reader-tuning, not basic acceptance |
| D6 | Implicit assumption: DEFERRED-priority ≠ DEFERRED-acceptance | core | H | Distinction worth surfacing explicitly |

### Sub-region E — "All 3 vs 4" transcription

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| E1 | User wrote "all 3" but listed 4 formats (txt, md, pdf, epub) | sub | H | Surface as transcription clarification |
| E2 | Plausible interpretation: typo for "all 4" | sub | H | Most likely reading |
| E3 | Plausible interpretation: "3 of these 4" excluding one | side | L | Less likely; would need to know which |
| E4 | Surfacing default: treat as "all 4" with explicit acknowledgment in finding | core | H | Asymmetric-failure: lean to acknowledging |

### Sub-region F — Acceptance-vs-priority semantic distinction

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| F1 | "Accepted format" definition: intake reads it, produces canonical HTML5 | core | H | The acceptance bar |
| F2 | "Priority format" definition: engineering invests in high-quality reader/repair operations | core | H | The priority bar |
| F3 | "DEFERRED" mapped to priority-deferred, not acceptance-deferred | core | H | Key disambiguation that resolves the user's question |
| F4 | This distinction allows: "accept all 4; prioritize EPUB + PDF" — both prior commitment and user's proposal hold | core | H | Coherent resolution |

### Sub-region G — EPUB-preference formalization options

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| G1 | UI recommendation in Mac app ("EPUB recommended for complex content") | core | H | Soft guidance; user-agency-preserving |
| G2 | Hard rule (intake refuses non-EPUB for detected complex content) | side | L | Violates user agency |
| G3 | Quality-tier flag (Category 7 emits fidelity tier; downstream consumes) | core | H | Composes with existing Category 7 design |
| G4 | Source-quality-driven routing (extend EPUB-from-PDF detection to format-quality detection) | sub | M | Architectural extension of the prior |
| G5 | Documentation only (informal guidance; no enforcement) | sub | M | Minimum implementation |
| G6 | Hybrid: UI recommendation + quality-tier flag + documentation (likely the right blend) | core | H | Multiple non-conflicting layers |

### Sub-region H — Use-case scenarios

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| H1 | Source only available in PDF (Muhakemat case) | sub | H | PDF path well-justified |
| H2 | Source is a markdown file the user wrote themselves | sub | H | Hand-edited intake — common in iterative translation work |
| H3 | Source is a clean Word document | side | M | DEFERRED per prior; not promoted |
| H4 | Source is a plain-text dump (copy-paste from webpage) | sub | M | Low-fidelity but accepted with degradation |
| H5 | Source is published markdown (GitHub README; Substack export) | sub | M | Pandoc-md is natural target |
| H6 | Source is converted-from-EPUB markdown (lossy conversion) | side | M | Edge case; some structure recoverable |

### Sub-region I — Pandoc's role

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| I1 | Pandoc natively reads epub, html, markdown, docx, odt, rst, latex (per documented format matrix) | core | H | Architectural lever already supports all 4 user-named formats |
| I2 | Pandoc does NOT natively read PDF (relies on pdftotext + post-processing) | core | H | PDF is the special case requiring Category 6 PDF path |
| I3 | Plain txt is degenerate Pandoc input (read as paragraph-broken text; no structure) | core | H | txt acceptance via Pandoc is effectively pass-through |
| I4 | Decision 5 (original intake-concepts) commits Pandoc + OCR as architectural lever | core | H | Already-committed lever supports the format-policy expansion |

### Sub-region J — Quality-tier scheme for format-fidelity

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| J1 | quality-tier=high (EPUB; well-formed source-conversion) | core | H | Top tier |
| J2 | quality-tier=medium (PDF with OCR + bidi-fix; HTML; Word with styles) | core | H | Mid tier; recovery-required |
| J3 | quality-tier=low (markdown with extensions; lossy structure recovery; markdown without extensions) | core | H | Low tier; some features unrepresentable |
| J4 | quality-tier=minimal (plain text; no structure) | core | H | Minimum tier; Categories 1+2+4+7 only |
| J5 | Composition with Category 7 quality flags (the Category 7 informational-flag mechanism extends to a `quality-tier` flag) | core | H | Reuses existing mechanism; clean integration |

---

## State Summary

### Territory + Purpose echo

- **Territory:** the design space of input-format-acceptance policy + routing-mechanism + EPUB-preference formalization, partitioned into 10 sub-regions (A through J).
- **Purpose:** adjudicate the user's proposal that intake accept txt + md + pdf + epub (all 4) with EPUB chosen under complex-content; refine the prior finding's DEFERRED 1 wording.

### Coverage map

| Sub-region | Items | core | sub | side | umbrella |
|---|---|---|---|---|---|
| A — Per-format fidelity | 7 | 4 | 2 | 1 | 0 |
| B — Routing-mechanism options | 8 | 4 | 2 | 2 | 0 |
| C — Complex-content detection | 9 | 1 | 6 | 2 | 0 |
| D — DEFERRED 1 re-examination | 6 | 6 | 0 | 0 | 0 |
| E — "all 3 vs 4" transcription | 4 | 1 | 2 | 1 | 0 |
| F — Acceptance-vs-priority semantic | 4 | 4 | 0 | 0 | 0 |
| G — EPUB-preference formalization | 6 | 3 | 2 | 1 | 0 |
| H — Use-case scenarios | 6 | 0 | 4 | 2 | 0 |
| I — Pandoc's role | 4 | 4 | 0 | 0 | 0 |
| J — Quality-tier scheme | 5 | 5 | 0 | 0 | 0 |
| **Total** | **59** | **32** | **18** | **9** | **0** |

### Confirmed-absent regions

None; territory was bounded and exhaustively traversed.

### Concept-names (selected high-relevance items)

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| Acceptance-vs-priority semantic distinction | coined-term | F1-F4 | The key disambiguation: accepted ≠ priority |
| EPUB-as-highest-fidelity-input | structural-reference | A1, J1 | Top of format-quality tier |
| Pandoc-as-architectural-lever-supports-all-4 | structural-reference | I1, I4 | Decision 5 already covers the proposed expansion |
| Quality-tier flag (Category 7 extension) | coined-term | J1-J5, G3 | Reuses existing flag mechanism for fidelity tier |
| Warn-and-degrade routing | structural-reference | B7 | The conservative routing posture |
| Hybrid auto-detect (extension + magic-bytes) | structural-reference | B4 | Standard practice for file-format routing |
| DEFERRED 1 wording re-examination | structural-reference | D1-D6 | The prior wording needs splitting (Word vs txt/md) |
| Source-mix expansion as revival trigger | structural-reference | D3 | Current user question IS the trigger |

### Recency distribution

All items `source: none, value: null` (possibility-mode candidates).

### Frontier flags

- **F-1: Decision-mode joint axis** (from articulation MQA) — validate / refine / overturn / clarify / design. Sensemaking adjudicates which mode the response takes.
- **F-2: Routing-mechanism joint axis** (from articulation MQA) — does intake auto-detect? warn-and-degrade? require user confirmation? Sensemaking commits.
- **F-3: "Plain-text" disambiguation in DEFERRED 1.** Did the prior mean .txt? .md? both? Sensemaking commits the interpretation.
- **F-4: Complex-content detection — runtime vs static vs documentation-only?** Sensemaking adjudicates whether complex-content detection is a runtime decision, a per-source declaration, or pure documentation guidance.
- **F-5: Acceptance-vs-priority distinction load-bearing potential.** If this distinction is committed, the user's question may be answered without overturning the prior finding's commitment. Sensemaking tests.

### Workspace-populated status

- **populated:** true
- **populated-at:** 2026-06-18 10:36 UTC
- **extent:** 59 items across 10 sub-regions; relevance-tagged at all relevant levels; confidence-tagged.

---

## Telemetry

- **Mode:** possibility / signal-first
- **Cycles:** 10 (one per sub-region; non-iterative; bounded territory)
- **Items enumerated:** 59
- **Items tagged core:** 32 (54%)
- **Items tagged sub:** 18 (31%)
- **Items tagged side:** 9 (15%)
- **Items tagged umbrella:** 0
- **Boundary-discovery sub-phase fired:** no
- **Convergence:** met
- **Workspace-overload trigger fired:** no
- **items_with_mtime:** 0
- **items_without_mtime:** 59
- **Failure modes scanned:** all 7 LAYER 1 + 3 LAYER 2 — none fired

---

## Self-Assessment Verdict

**PROCEED**

Territory bounded; 59 candidates individuated across 10 sub-regions; 5 frontier flags for sensemaking; high core-relevance ratio (54%) reflects the focused inquiry scope; no failure modes observed.
