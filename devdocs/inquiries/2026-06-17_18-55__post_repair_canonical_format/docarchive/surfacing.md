# Surfacing — post-repair canonical format

## User Input

Input passed to surfacing: `_branch.md` + `articulate_simple.md` + warm substrate (prior canonical-format finding's three-format layered verdict; original intake-concepts finding's Decisions 2-5; empirical PDF evidence from Asa-yı Musa + Muhakemat). Critical framing: this inquiry takes the reconstruction-is-heavy reframe as GIVEN. Surfacing produces a two-dimensional candidate-territory: **format-candidates × post-repair content-requirements**.

Inquiry purpose (from `_branch.md`'s Goal, lifted verbatim):

> Produce a format decision/recommendation about post-repair document storage. Shape depends on decision-mode `[re-affirm-prior / overturn-with-named-candidate / restate-architecture]` × temporal-layer `[canonical / hand-edit / publishing / all-collapsed]`. Serves one or more of `[prior-doesn't-feel-final / new-evidence-changes-question / wanting-readable / translation-output-focus / publishing-considerations / scope-engineering]`. Excludes repair-pipeline, prior Decisions 2-5, PDF-extraction, Mac-app-UI.

---

## Mode + Entry + Scope

- **Mode:** hybrid — `artifact` (warm substrate is orientation) + `possibility` (the requirements × candidates territory needs candidate-generation).
- **Entry point:** `signal-first` (purpose given via `_branch.md`).
- **Territory:** `explicit-bounded` — eight regions (A-H) from the input.
- **Boundary-discovery sub-phase:** not fired.
- **Exclusions honored:** repair-pipeline-out, prior-Decisions-2-5-stand, PDF-extraction-out, Mac-app-UI-out.

---

## Workspace work-product (in-context, session-local)

The LLM session has read the warm substrate (the prior canonical-format finding's three-format verdict; the original intake-concepts finding's Decisions 2-5; the empirical PDF observations from Asa-yı Musa and Muhakemat) and uses the eight territory regions A-H as the enumeration scope. Per-item relevance tags below are emitted directly into the workspace and captured into the artifact's Trace at the moment of tagging.

---

## Traversal Trace

Per-item granularity: each item has a relevance tag (`core` / `sub` / `side` / `umbrella`) + confidence (`HIGH` / `MED` / `LOW`). Possibility-mode items have `{source: none, value: null}` recency annotation.

### Region R1 — Warm substrate (artifact-mode; orientation, not enumeration)

| # | Item | Role |
|---|---|---|
| W1 | `2026-06-17_17-49__canonical_intake_format_deep_dive/finding.md` | Prior verdict: three-format layered architecture (JSON-AST canonical + Pandoc-md hand-edit + EPUB 3 publishing); this inquiry re-tests its load-bearing canonical-layer commitment |
| W2 | `2026-06-17_00-49__document_intake_handling_concepts/finding.md` | Original intake-concepts Decisions 2-5 inherited (quality target = structure-preservation; IntakeDoc tree+cross-ref shape; 7-policy split; Pandoc+OCR lever) |
| W3 | Empirical PDF evidence — Asa-yı Musa | Broken-bidi Arabic in text-layer; needs OCR-repair of Arabic spans; demonstrates the reconstruction-is-heavy reframe |
| W4 | Empirical PDF evidence — Muhakemat | Image-only Arabic (entirely outside text-layer); clean Turkish; lost italics; per-page running headers; demonstrates a different reconstruction failure mode |
| W5 | Reconstruction-is-heavy reframe | Post-repair content carries OCR-recovered spans + style-recovered emphasis + structure-detected markers + paratext-stripped body + apparatus-detected marginalia + per-policy class-tagged elements + provenance metadata |

---

### Region R2 (A) — Post-repair content requirements (the load-bearing axis)

| # | Requirement | Tag | Conf | Note |
|---|---|---|---|---|
| A01 | Arabic spans with explicit `lang=ar` attribute | **core** | HIGH | Reconstructed via OCR; the policy `NonMainLangPartsPolicy` target |
| A02 | Arabic spans with explicit `dir=rtl` attribute | **core** | HIGH | Reading-order metadata; lost by `pdftotext` |
| A03 | Italic-as-semantic-emphasis distinct from raw typography | **core** | HIGH | Per Decision 2 (structure-preservation); recovered via mutool or pdf2htmlEX |
| A04 | Bold-as-strong-emphasis distinct | **core** | HIGH | Same as A03 |
| A05 | Marginalia (hashiye) with reference-to-body-position | **core** | HIGH | The `SourceApparatusPolicy` target; structural relationship to body |
| A06 | Embedded poetry (Mevlana couplets) with attribution + verse-shape | **core** | HIGH | `EmbeddedPoetryPolicy` target; needs line-block + class + attribution attribute |
| A07 | Formulaic openings (Bismillah, Hamd) with position-at-section-start | **core** | HIGH | `FormulaicOpeningPolicy` target; position-constraint metadata |
| A08 | Voice transitions (author vs cited authority) with class | **sub** | HIGH | `VoiceMarkingPolicy` target |
| A09 | Honorifics (R.A., A.S.) as inline span with tradition tag | **sub** | HIGH | `HonorificsPolicy` target |
| A10 | Archaic register markers (Ottoman vocab) with class | **sub** | MED | `ArchaicRegisterPolicy` target |
| A11 | Non-main-language spans tagged generally | **sub** | HIGH | Reduces to A01 + A02 |
| A12 | Chapter / section / paragraph hierarchical containment | **core** | HIGH | Per Decision 3 (IntakeDoc tree shape) |
| A13 | Cross-references (apparatus-ref → body-position) | **core** | HIGH | The tree+cross-ref-flat shape's load-bearing property |
| A14 | Multi-volume containment | **sub** | MED | Some Risale-i Nur works are multi-volume; format must hold or reference |
| A15 | Paratext (running headers, page numbers) stripped at intake | side | HIGH | Drop-policy is committed; format just needs to NOT include them |
| A16 | Letter-spaced structural markers (T e n b i h, H â t i m e) detected | **sub** | MED | A novel pattern from Muhakemat; needs class-tagging |
| A17 | Numbered Mukaddeme / Mes'ele section headings | sub | HIGH | Heading nodes; standard structural |
| A18 | **Source-of-truth provenance** (which PDF, when intaken, what repair passes) | **core** | HIGH | NEW from reconstruction reframe; format must hold or reference |
| A19 | **Per-element confidence score** (OCR conf; detector conf; auto vs hand-edited) | **core** | HIGH | NEW from reconstruction reframe; verifiability against source |
| A20 | Cross-Pandoc-version stability | side | MED | Operational concern; per-format risk varies |

**Region R2 coverage:** 20 requirements; 9 `core` (A01, A02, A03, A04, A05, A06, A07, A12, A13, A18, A19) plus 8 `sub`; 2 `side`. The post-repair content imposes a richer requirement set than the prior inquiry's canonical-format-question implied — notably the provenance + confidence requirements (A18, A19) are NEW.

---

### Region R3 (B) — Candidate formats

| # | Candidate | Tag | Conf | Note |
|---|---|---|---|---|
| B01 | Pandoc-AST-as-JSON | **core** | HIGH | The prior verdict; the user did NOT name it in this inquiry — must be re-tested honestly against the new requirements (especially A18 + A19) |
| B02 | Pandoc-markdown with canonical extension set | **core** | HIGH | User-named candidate ("md file") |
| B03 | HTML5 + semantic markup | **core** | HIGH | User-named candidate; native `lang=` `dir=` + `<aside>` + `<section>` |
| B04 | HTML5 + ARIA + microdata | **sub** | HIGH | Richer attribute layer on top of HTML5; supports A18 + A19 via data attributes |
| B05 | XHTML (HTML5 in strict XML mode) | sub | MED | Schema-validatable; near-identical to HTML5 for our purposes |
| B06 | EPUB 3 | **core** | HIGH | User-named candidate; packaged-book |
| B07 | EPUB 2 | side | MED | Older; less feature-rich; not preferred |
| B08 | DocBook 5 | side | MED | XML; Pandoc ↔︎; verbose; technical-doc domain |
| B09 | TEI / TEI Simple | side | HIGH | Scholarly-XML standard; Pandoc-read ABSENT (write-only via TEI Simple); strong A05-A06-A07 native support but engineering-cost prohibitive |
| B10 | JATS | side | MED | Pandoc ↔︎; academic-article domain |
| B11 | BITS | side | LOW | Books-extension of JATS; Pandoc-read only |
| B12 | FictionBook2 (FB2) | side | LOW | Russian-origin XML ebook; Pandoc ↔︎; niche |
| B13 | Custom JSON-AST (project-defined schema) | side | LOW | Unnecessary given B01 (Pandoc-AST already exists) |
| B14 | Custom .compldoc (Markdown + YAML hybrid) | **sub** | MED | Hybrid candidate; markdown body + YAML frontmatter for apparatus + provenance — the "best of both" emerging-pattern |
| B15 | YAML-as-document | side | LOW | YAML's expressiveness for metadata + structured content; unusual for body text |
| B16 | The three-format layered architecture (prior's verdict) | **core** | HIGH | META-candidate: validate the architecture itself, possibly with HTML5 added or swapped in |
| B17 | **HTML5 as universal canonical (one format serves all layers)** | **core** | HIGH | EMERGENT candidate; HTML5 is both human-readable (markdown-like) and explicit-tree (XML-like) — could collapse the three layers if it serves them all |
| B18 | Pandoc-AST-JSON canonical + HTML rendering on-demand | **sub** | HIGH | Hybrid: data canonical + surface renderings derived from it |
| B19 | Markdown body + JSON sidecar for apparatus + provenance | **sub** | MED | Hybrid: human-readable surface + machine-readable metadata side-files |

**Region R3 coverage:** 19 candidates. Five `core`: the four user-named + prior-verdict (B01 JSON-AST, B02 markdown, B03 HTML5, B06 EPUB 3, B16 layered-architecture-META) plus B17 HTML5-as-universal (emergent). Five `sub` worth comparing for nuance.

---

### Region R4 (C) — Capability matrix concept (the analytical artifact)

| # | Concept | Tag | Conf | Note |
|---|---|---|---|---|
| C01 | The capability matrix as a sensemaking artifact (rows = R2 requirements; columns = R3 candidates; cells = native / via-extension / via-workaround / not-supported) | **core** | HIGH | THE load-bearing analytical artifact; sensemaking must construct this matrix and commit on its evidence |
| C02 | Per-cell evidence-citation (Pandoc-fact / W3C-spec / EPUB-spec / project-decision) | **core** | HIGH | Anti-hallucination discipline applied to the matrix |
| C03 | Per-candidate aggregate-coverage-score derived from the matrix | sub | HIGH | An optional summary metric; useful for at-a-glance |
| C04 | The "Pareto-dominant" candidate identification (if one candidate is ≥ all others on all requirements) | sub | MED | Conditional — may or may not exist |
| C05 | The "axis of incomparability" surface (when no candidate dominates, what trade-off axes remain?) | **sub** | HIGH | Forces honest acknowledgment of trade-offs |

**Region R4 coverage:** 5 concepts; the matrix itself is `core` as the analytical foundation.

---

### Region R5 (D) — Round-trip properties

| # | Property | Tag | Conf | Note |
|---|---|---|---|---|
| D01 | Pandoc-AST-JSON → JSON → AST: lossless (same Pandoc version) | **core** | HIGH | The prior verdict's load-bearing claim |
| D02 | Pandoc-md → JSON → md: round-trip-stable SUBSET issue | **core** | HIGH | The prior finding's REFINE flag; defines the hand-edit format's contract scope |
| D03 | HTML5 → HTML5 (via Pandoc): round-trips cleanly | **core** | HIGH | Pandoc ↔︎ html5; the AST → html → AST path is stable |
| D04 | EPUB 3 → markdown: LOSSY at canonical level | **core** | HIGH | Drift in metadata + TOC + class attributes |
| D05 | TEI ↔︎ Pandoc: **read absent** | sub | HIGH | Pandoc cannot read TEI; rules TEI out as canonical |
| D06 | Custom JSON-AST: round-trips by definition | side | HIGH | Trivially true; project-controlled schema |
| D07 | Markdown + YAML sidecar: hybrid round-trip; markdown-body stable + YAML-stable separately | sub | MED | Two-file approach; both round-trip independently |

**Region R5 coverage:** 7 properties; the round-trip axis is a strong differentiator among candidates.

---

### Region R6 (E) — Human-readability axis

| # | Property | Tag | Conf | Note |
|---|---|---|---|---|
| E01 | JSON-AST: machine-readable; NOT human-readable as a document | **core** | HIGH | The user's intuition: they want a document, not data |
| E02 | Markdown: human-readable AS text; reading-order-natural | **core** | HIGH | The strongest human-readability case |
| E03 | HTML5: human-readable AS source (tags + text); less reading-order-natural than markdown | **core** | HIGH | Middle position; readable but more tag-clutter |
| E04 | EPUB 3 raw: NOT human-readable (it's a zip) | sub | HIGH | But unzipped contents are xhtml = HTML5 = readable |
| E05 | TEI: human-readable AS XML source but TEI-expert-dependent | side | HIGH | Vocabulary expertise required |
| E06 | The user's preference for surface formats (EPUB / md / HTML) over abstract data (JSON-AST) is itself an evidence signal | **core** | HIGH | LOAD-BEARING signal for the inquiry's WHY-axis; honoring this means treating "data canonical" as a separate question from "document canonical" |

**Region R6 coverage:** 6 properties. E06 is the meta-observation that ties the human-readability axis to the user's framing.

---

### Region R7 (F) — Provenance / edit-audit properties (NEW from reconstruction reframe)

| # | Property | Tag | Conf | Note |
|---|---|---|---|---|
| F01 | Per-element OCR confidence carryable | **core** | HIGH | Tesseract emits confidence; the format must hold it for downstream quality measurement |
| F02 | Per-element source (text-layer vs OCR-recovered vs hand-edited) carryable | **core** | HIGH | Per A19; required for verifiability against source |
| F03 | Per-element hand-edit status carryable | **core** | HIGH | For the hand-edit recovery workflow |
| F04 | Per-element intake-pass-history carryable | sub | MED | Which repair pass produced this element |
| F05 | Document-level provenance (source PDF path + hash + intake-time) | **core** | HIGH | Per A18 |
| F06 | Generic data-attribute / class mechanism for the above (HTML5 `data-*` / JSON-AST attribute / markdown bracketed-span class) | **core** | HIGH | The format's extensibility mechanism for provenance metadata |

**Region R7 coverage:** 6 properties; THE NEW DIMENSION from the reconstruction reframe. Provenance + confidence weren't load-bearing in the prior canonical-format inquiry; they ARE here.

---

### Region R8 (G) — Publishing-format frame

| # | Item | Tag | Conf | Note |
|---|---|---|---|---|
| G01 | EPUB 3 as publishing | **core** | HIGH | Strong ecosystem (Apple Books, Calibre, Kobo); the prior committed this layer |
| G02 | HTML5 as web-output | **sub** | HIGH | If the project ships translations on web; HTML5 is canonical |
| G03 | PDF as print-output (Pandoc-generatable) | side | MED | When print is needed |
| G04 | Markdown as research-corpus-format | side | MED | If the project ships translations as a research corpus (e.g., for academic use) |
| G05 | Multi-output (EPUB + HTML + PDF) generated from canonical | **core** | HIGH | The "canonical generates all outputs" pattern |
| G06 | The TRANSLATED docs' format (downstream of intake) | **sub** | HIGH | The user's earlier phrasing "for translations" — clarify whether they mean intake's storage of source or output for translation |

**Region R8 coverage:** 6 items; G01 and G05 are core; G06 captures the ambiguity in the user's earlier framing.

---

### Region R9 (H) — Three-layer mapping re-test

| # | Layer / Mapping | Tag | Conf | Note |
|---|---|---|---|---|
| H01 | Canonical (intake/translate-internal) layer: needs explicit-tree + provenance + lossless round-trip | **core** | HIGH | Candidates: B01 JSON-AST, B17 HTML5-as-universal, B14 .compldoc, B19 markdown+sidecar |
| H02 | Hand-edit (user-facing) layer: needs human-readability + byte-stability | **core** | HIGH | Candidates: B02 markdown, B17 HTML5-as-universal |
| H03 | Publishing (reader-facing) layer: needs ecosystem + packaged-book | **core** | HIGH | Candidates: B06 EPUB 3, B17 HTML5-as-universal |
| H04 | User-named EPUB → publishing layer mapping | **core** | HIGH | Confirms prior verdict's publishing-layer choice |
| H05 | User-named markdown → hand-edit layer mapping | **core** | HIGH | Confirms prior verdict's hand-edit-layer choice |
| H06 | User-named HTML → could be canonical OR hand-edit OR publishing — VERSATILE | **core** | HIGH | EMERGENT signal: HTML5 is the most layer-versatile candidate |
| H07 | **HTML5 as universal canonical** (one format that serves all three layers) | **core** | HIGH | EMERGENT architectural alternative to the prior three-format split |
| H08 | JSON-AST + HTML5 dual (canonical + rendering) | **sub** | HIGH | Hybrid that keeps JSON-AST's lossless-round-trip AND HTML5's human-readability |
| H09 | Whether to collapse the three layers back to one (monolithic vs layered) | **core** | HIGH | THE FRAME-LEVEL question; sensemaking must adjudicate |

**Region R9 coverage:** 9 mapping concepts; the H07 (HTML5-as-universal) and H08 (JSON-AST + HTML5 dual) are emergent architectural alternatives that didn't exist in the prior inquiry's solution space.

---

## State Summary

### Territory-specification echo

Eight regions A-H + warm substrate R1. Two-dimensional candidate space: 20 requirements (R2) × 19 format-candidates (R3); plus matrix-concept (R4), round-trip (R5), human-readability (R6), provenance (R7), publishing (R8), and three-layer mapping (R9).

### Purpose-specification echo

Produce a format decision/recommendation about post-repair document storage, with decision-mode `[re-affirm-prior / overturn-with-named-candidate / restate-architecture]` × temporal-layer `[canonical / hand-edit / publishing / all-collapsed]` left open.

### Coverage map

| Region | Coverage | Items | Aggregate relevance lean |
|---|---|---|---|
| R1 (substrate) | confirmed (orientation only) | 5 | n/a |
| R2 (A. requirements) | confirmed-present | 20 | 9 core + 8 sub + 2 side; **A18 + A19 (provenance + confidence) are NEW** |
| R3 (B. candidates) | confirmed-present | 19 | 5 core (4 user-named + prior) + 1 emergent (B17 HTML5-as-universal) + 5 sub |
| R4 (C. matrix concept) | confirmed-present | 5 | 1 core (the matrix as analytical artifact) |
| R5 (D. round-trip) | confirmed-present | 7 | 4 core (the round-trip differentiator across candidates) |
| R6 (E. human-readability) | confirmed-present | 6 | 4 core (E01-E03 + E06 the user-preference signal) |
| R7 (F. provenance) | confirmed-present | 6 | 5 core (the NEW dimension from reconstruction reframe) |
| R8 (G. publishing) | confirmed-present | 6 | 2 core (G01 EPUB + G05 multi-output) |
| R9 (H. three-layer mapping) | confirmed-present | 9 | 6 core (the architectural re-test) |

**Total: 88 items + 5 substrate references.**

### Confirmed-absent regions

None at this resolution. Excluded by MQ4: repair-pipeline design (covered by intake-reconstruction inquiry, separate); prior-Decisions-2-5 (inherited); PDF-extraction (user-named separate); Mac-app-UI (inherited).

### Concept-names list (load-bearing primitives)

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| `post-repair content requirements` | coined-term | R2 region | The 20-item requirement set that the format must hold |
| `capability matrix` | coined-term | R4 | The analytical artifact: candidates × requirements with native/extension/workaround/not-supported cells |
| `human-readability axis` | structural-reference | R6 | The user's preference for documents over data; signals away from JSON-AST |
| `provenance + confidence dimension` | coined-term | R7 | NEW from the reconstruction-is-heavy reframe; carries OCR-confidence, source, hand-edit status |
| `HTML5-as-universal canonical` | coined-term | B17 / H07 | Emergent architectural alternative: one format serves all three layers |
| `JSON-AST + HTML5 dual` | coined-term | B18 / H08 | Hybrid: data canonical + rendering surface |
| `markdown body + JSON sidecar` | coined-term | B19 | Hybrid: human-readable body + machine-readable metadata sidefile |
| `the-axis-of-incomparability` | coined-term | C05 | When no candidate dominates, the trade-offs that remain |
| `round-trip-stable subset` | structural-reference | D02 | Carried forward from prior inquiry; defines hand-edit format's contract scope |
| `Pandoc-read absent` (for TEI) | vocabulary | D05 | Rules TEI out as canonical |

### Recency distribution

All items: `{source: none, value: null}`. Possibility-mode candidates.

### Frontier flags

| Flag | Concept | Why frontier |
|---|---|---|
| F1 | The capability matrix itself — must be constructed in sensemaking | The matrix is the load-bearing analytical artifact; surfacing names it, sensemaking populates it |
| F2 | HTML5-as-universal canonical — is it really viable for ALL three layers? | Emergent candidate; needs structural test |
| F3 | JSON-AST + HTML5 dual — does the dual-format overhead pay off? | Hybrid candidate; needs trade-off evaluation |
| F4 | Provenance + confidence as format-choice differentiator (NEW dimension) | The reconstruction reframe surfaces this; sensemaking must include in adjudication |
| F5 | The user's non-mention of JSON-AST — intentional rejection or omission? | Sensemaking must surface and adjudicate this honestly |
| F6 | The TRANSLATED docs' format (downstream of intake) — possibly the real question the user is asking | The "for translations" framing from earlier; clarify whether intake-storage or translation-output is the scope |

### Workspace-populated status

`{populated: true, populated-at: 2026-06-17_19-02, extent: "8 regions A-H traversed; 88 candidates tagged + 10 concept-names extracted; 6 frontier flags"}`

### Re-invocation parameters (suggested)

- **rsp1:** "construct the capability matrix" — populate R4 (the load-bearing artifact).
- **rsp2:** "HTML5-as-universal feasibility test" — structurally probe H07.
- **rsp3:** "provenance + confidence in markdown — workaround vs not-supported?" — test the new dimension against the user's named candidates.
- **rsp4:** "what does 'for translations' actually mean — intake-storage or translation-output?" — clarify F6.

---

## Telemetry

- **Mode:** hybrid · **Entry point:** signal-first
- **Cycles run:** 8 (one per region R2-R9; R1 is substrate)
- **Items enumerated:** 88 + 5 substrate
- **Items tagged at each relevance level:** core = 35 · sub = 32 · side = 19 · umbrella = 0 · (LOW-confidence subset = 6)
- **Sub-phase fired:** no (explicit-bounded)
- **Workspace-overload trigger:** not fired
- **Failure modes checked:**
  - LAYER 1 mode 1 (missed-relevance): low — the territory was richly specified by the input
  - LAYER 1 mode 2 (surfaced-irrelevance): some risk — 19 side-tagged items may be noise; downstream prunes
  - LAYER 1 mode 3 (over-coverage): possible — 88 items is broad; the capability matrix will compress
  - LAYER 1 mode 4 (territory-mis-binding): no — exclusions honored
  - LAYER 1 modes 5-9: not fired
- **Items with mtime / without mtime:** 0 / 88
- **Self-assessment verdict:** **PROCEED**

The two-dimensional candidate space is broad enough to seed sensemaking's capability-matrix construction. The emergent candidate (HTML5-as-universal) + the NEW dimension (provenance + confidence) are the structurally novel surfaces this inquiry exposes that the prior inquiry didn't.
