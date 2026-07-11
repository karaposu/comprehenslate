# Surfacing — canonical intake format deep dive

## User Input

Input passed to surfacing: `_branch.md` + warm substrate (the prior intake-concepts finding committing Decision 1 = Pandoc's markdown; the schema; the calibration-corpus framing; Pandoc's conversion matrix). Possibility-mode candidates organized in 10 format families (A-J) + 4 requirement-criterion categories (K-N).

Inquiry purpose (from `_branch.md`'s Goal, lifted verbatim):

> Produce an analysis + decision/recommendation about the canonical intake format for comprehenslate's translation pipeline. Shape depends on the **decision-mode** (joint axis from MQA): `[validate-prior (Pandoc's markdown survives) / re-decide-with-existing-alternative (swap to RTF / EPUB / MOBI / TEI / other) / design-new-format-from-requirements (custom)]`. Serves one or more of `[prior-doesn't-feel-right / richer-fidelity / avoid-rework / corpus-match / validate-intuition / publishing-considerations]`. Excludes PDF-text-extraction, app UI, translation-stage internals.

---

## Mode + Entry + Scope

- **Mode:** hybrid — `artifact` (warm substrate for grounding; prior finding's commitments) + `possibility` (the format-candidates + requirement-criteria require candidate-generation; each gets a relevance tag).
- **Entry point:** `signal-first` (purpose given via `_branch.md`).
- **Territory:** `explicit-bounded` (the 10 families A-J + the 4 criterion categories K-N are the enumeration scope).
- **Boundary-discovery sub-phase:** not fired (territory explicit-bounded).
- **Exclusions honored:** PDF-extraction-out, app-UI-out, translation-internals-out.

---

## Workspace work-product (in-context, session-local)

The session has read (or holds via prior turns) the warm substrate — the prior intake finding's Decision 1 commitment, the schema's 7 policy classes, the calibration corpus framing, Pandoc's conversion matrix. The 10 candidate families + 4 criterion categories from the input form the enumeration scope. Per-item relevance tags below are emitted into workspace and captured at the moment of tagging into the Trace.

---

## Traversal Trace

Per-item granularity: each candidate carries a relevance tag (`core` / `sub` / `side` / `umbrella`) + confidence (`HIGH` / `MED` / `LOW`). All items are `{source: none, value: null}` (possibility-mode, no filesystem backing).

### Region R1 — Warm substrate (orientation, not enumeration)

| # | Item | Role |
|---|---|---|
| W1 | `2026-06-17_00-49__document_intake_handling_concepts/finding.md` | Prior Decision 1 commitment + the 5 load-bearing decisions this inquiry's verdict will refine/preserve/overturn |
| W2 | `SKILL/references/config/schemas.py` lines 18-122 (the 7 policy classes) | Any candidate format must support intake-side perception of these |
| W3 | `SKILL/SKILL.md` | Calibration corpus framing (Risale-i Nur as anchor, not as scope-limit) |
| W4 | Pandoc's conversion matrix (~30 formats; ↔︎ ← → conversion directions) | Defines what "Pandoc-supported" means concretely; constrains the candidate space |

---

### Region R2 (A) — Lightweight Markup family

| # | Candidate | Tag | Conf | Note |
|---|---|---|---|---|
| A01 | **Pandoc's markdown** (the prior Decision 1) | **core** | HIGH | Incumbent; must be re-tested against stronger prosecution |
| A02 | **CommonMark** (strict spec) | **core** | HIGH | The minimal-extension baseline; what markdown rejection implicitly defaults to |
| A03 | GitHub Flavored Markdown (GFM) | sub | HIGH | CommonMark + tables + strikethrough + task lists; less rich than Pandoc's |
| A04 | CommonMark_x (CommonMark + Pandoc extensions) | sub | MED | Pandoc's extension layered on CommonMark; midway between strict and full Pandoc |
| A05 | **AsciiDoc** | **core** | HIGH | Richer than markdown — native footnotes, includes, attributes, nested blocks; a real markdown alternative |
| A06 | reStructuredText | sub | MED | Python-community's structured-text format; well-defined; less ecosystem |
| A07 | Emacs Org-mode | side | MED | Very expressive but Emacs-coupled; usable but unusual outside Emacs |
| A08 | Djot | side | LOW | Newer (2022); cleaner spec than markdown but immature ecosystem |
| A09 | MultiMarkdown | side | LOW | Pandoc-adjacent but Pandoc's markdown subsumes most of its features |
| A10 | Markua | side | LOW | Leanpub-specific; ecosystem-locked |
| A11 | Textile | side | LOW | Older; mostly displaced by markdown |

**Region R2 coverage:** 11 items. Two `core` (A01 incumbent + A02 baseline). One emerging `core` (A05 AsciiDoc — the strongest markdown-family challenger).

---

### Region R3 (B) — Word-Processor / Rich-Text family

| # | Candidate | Tag | Conf | Note |
|---|---|---|---|---|
| B01 | **RTF** (Rich Text Format) | **core** | HIGH | The user's named intuition candidate; must be steel-manned and re-tested |
| B02 | Microsoft Word .docx (Office Open XML) | sub | HIGH | Pandoc-supported; ISO-standardized; but binary-shaped zip; not human-editable |
| B03 | OpenDocument .odt (LibreOffice/OpenOffice) | side | MED | Pandoc-supported; similar trade-offs to docx; less encumbered |

**Region R3 coverage:** 3 items. One `core` (B01 RTF — user's intuition).

---

### Region R4 (C) — Ebook / Publishing family

| # | Candidate | Tag | Conf | Note |
|---|---|---|---|---|
| C01 | **EPUB 3** | **core** | HIGH | User's intuition + Pandoc ↔︎ + the publishing-format the calibration corpus would eventually ship as |
| C02 | EPUB 2 | sub | MED | Older version; lacks media-overlays; superseded by EPUB 3 |
| C03 | **MOBI** | **core** | HIGH | User's intuition; but Amazon-deprecated as of 2022 (Kindle replaced .mobi with .azw3/.kfx); included to be honestly evaluated then likely rejected |
| C04 | AZW3 / KF8 (Amazon's modern format) | side | MED | EPUB-derived but proprietary; vendor-locked |
| C05 | FictionBook2 (FB2) | side | LOW | XML-based ebook format; Pandoc ↔︎; Russian-origin; niche outside that ecosystem |

**Region R4 coverage:** 5 items. Two `core` (C01 EPUB 3 + C03 MOBI — both user-named).

---

### Region R5 (D) — Structured / Scholarly XML family

| # | Candidate | Tag | Conf | Note |
|---|---|---|---|---|
| D01 | **TEI (Text Encoding Initiative)** | **core** | HIGH | Designed exactly for scholarly text encoding — native marginalia, apparatus criticus, voice marking, lang attribute. The strongest contender from the structured-XML space for the calibration-corpus shape. |
| D02 | TEI Simple (TEI subset) | sub | MED | Less verbose TEI variant; fewer features but still TEI-shaped |
| D03 | DocBook 5 | sub | MED | XML; technical-documentation domain; Pandoc-supported; less calibrated for marginalia + apparatus than TEI |
| D04 | DocBook 4 | side | LOW | Older version; superseded by DocBook 5 |
| D05 | JATS (Journal Article Tag Suite) | sub | MED | Academic-article format; Pandoc supports; less book-shaped |
| D06 | BITS (Book Interchange Tag Suite) | **core** | HIGH | JATS extension for BOOKS; closer fit than JATS-for-articles to the calibration corpus's multi-volume book shape |

**Region R5 coverage:** 6 items. Two `core` (D01 TEI + D06 BITS — both scholarly-text-encoding standards calibrated for book-shaped corpora with apparatus).

---

### Region R6 (E) — Web Format family

| # | Candidate | Tag | Conf | Note |
|---|---|---|---|---|
| E01 | **HTML5 + lang/dir attributes** | **core** | HIGH | Native lang= and dir= attributes; semantic markup (article, section, aside, figure); broad tool support; Pandoc ↔︎; a real contender |
| E02 | XHTML (HTML5 in strict XML mode) | sub | MED | Stricter parsing; schema-validatable via DTD; similar feature set to HTML5 |
| E03 | Chunked HTML | side | LOW | Pandoc → only; a derivative output format, not a canonical-intake candidate |

**Region R6 coverage:** 3 items. One `core` (E01 HTML5+ARIA — the strongest non-markdown, non-XML candidate).

---

### Region R7 (F) — Typesetting family

| # | Candidate | Tag | Conf | Note |
|---|---|---|---|---|
| F01 | LaTeX | sub | HIGH | Pandoc ↔︎; preserves math + structure; verbose; academic-corpus-friendly but not book-publishing-friendly |
| F02 | ConTeXt | side | MED | Pandoc → only; LaTeX alternative; niche |
| F03 | Typst (new LaTeX alternative) | side | LOW | Pandoc ↔︎; newer; immature for this use case |
| F04 | roff / mdoc | side | LOW | Pandoc ↔︎ for roff; mdoc ← only; legacy Unix manual format; out of scope |

**Region R7 coverage:** 4 items. Zero `core` — typesetting formats are output-oriented, not canonical-intake-shaped.

---

### Region R8 (G) — Serialization / AST-as-Storage family

| # | Candidate | Tag | Conf | Note |
|---|---|---|---|---|
| G01 | **Pandoc-AST-as-JSON** | **core** | HIGH | Pandoc's native AST serialized as JSON; lossless round-trip via Pandoc; bypasses markdown-syntax limitations by storing the parsed tree directly |
| G02 | Pandoc-AST-as-XML | sub | MED | Same as G01 but XML serialization; more verbose, similar lossless-ness |
| G03 | **Custom JSON-AST (project-defined)** | **core** | HIGH | A project-specific schema shaping the AST to comprehenslate's exact needs; corresponds to the "design-new-format" decision-mode |
| G04 | YAML-as-document (YAML frontmatter + structured body) | sub | MED | YAML's expressiveness for metadata + structured content; readable but unusual choice for body text |
| G05 | **Custom .compldoc (Markdown + YAML hybrid)** | **core** | HIGH | The prior finding's deferred-v1+ custom format; surface for re-evaluation given the user's pushback |

**Region R8 coverage:** 5 items. Three `core` (G01 Pandoc-AST-as-JSON + G03 custom JSON-AST + G05 .compldoc) — all variants of "store the parsed tree rather than the surface syntax."

---

### Region R9 (H, I, J) — Out-of-scope families (listed for completeness)

| # | Candidate | Tag | Conf | Note |
|---|---|---|---|---|
| H01 | MediaWiki markup | umbrella | HIGH | Not designed for canonical storage; wiki-edit-oriented |
| H02 | DokuWiki | umbrella | HIGH | Same as H01 |
| H03 | Jira wiki | umbrella | HIGH | Same |
| I01 | Jupyter (.ipynb) | umbrella | HIGH | JSON-based notebook structure; interesting JSON-AST comparator (G01-G03 family) but not directly applicable as a candidate |
| J01 | PowerPoint / Beamer / reveal.js / etc. | umbrella | HIGH | Slide formats; out of scope for translation source |

**Region R9 coverage:** 5 items, all flagged `umbrella` (= out-of-scope but enumerated for honesty).

---

### Region R10 (K) — Source-fidelity criteria

| # | Concept | Tag | Conf | Note |
|---|---|---|---|---|
| K01 | Chapter / section / paragraph preservation | **core** | HIGH | The structural backbone every candidate must preserve |
| K02 | Footnote preservation | **core** | HIGH | Pandoc-md ✓; CommonMark ✗; TEI ✓; HTML5 ✓; RTF ✓; EPUB ✓ |
| K03 | Marginalia / apparatus criticus representation | **core** | HIGH | Calibration-corpus-critical; TEI has native `<note>` placement; markdown has none; HTML5 has `<aside>`; RTF has annotation; EPUB depends on subset |
| K04 | Embedded poetry / verses representation | **core** | HIGH | TEI native `<lg>` linegroup; markdown via blockquote-with-line-breaks; HTML5 via class; varies sharply by format |
| K05 | Formulaic openings detection-readiness | sub | MED | A perception target; format's role is to PRESERVE the markup, detection is downstream |
| K06 | Voice transitions detection-readiness | sub | MED | Same — format preserves; detector reads |
| K07 | **Non-main-language span tagging (lang= attribute)** | **core** | HIGH | TEI / HTML5 / EPUB native via xml:lang or lang=; markdown via Pandoc's bracketed_spans; RTF via Unicode language codes; varies sharply |
| K08 | **Direction tagging (dir= attribute for RTL)** | **core** | HIGH | HTML5 / EPUB native; markdown via Pandoc's bracketed_spans dir attribute; RTF native; TEI native |
| K09 | **Diacritic stability (NFC round-trippability)** | **core** | HIGH | UTF-8-native formats (markdown / HTML / TEI / EPUB) trivially preserve; RTF has Windows-codepage history that risks NFD/NFC instability |
| K10 | Emphasis as semantic (italic-vs-emphasis distinction) | sub | HIGH | Markdown collapses to italic; HTML5 `<em>` vs `<i>` distinguishes; TEI explicit |
| K11 | Citation handling | sub | MED | Pandoc-md ✓ via `@key`; JATS/BITS native; TEI native; markdown without Pandoc ✗ |
| K12 | Cross-references intra-document | sub | MED | HTML / EPUB / TEI native (id+href); markdown has implicit anchors |
| K13 | **Multi-volume containment** | **core** | HIGH | EPUB / BITS / FB2 are packaged-book formats (one file = whole book or set); markdown is per-file; significant architecture implication |
| K14 | Metadata (title / author / language) | sub | HIGH | YAML frontmatter for markdown; EPUB OPF metadata; TEI teiHeader; native to most formats |
| K15 | Image / figure handling (preserve vs drop) | side | MED | Format-specific; orthogonal to text |
| K16 | Table representation richness | sub | MED | Markdown limited to pipe-tables; HTML/TEI/EPUB rich tables; RTF rich |

**Region R10 coverage:** 16 items. Six `core` (K01-K04 + K07-K09 + K13) — the criteria that most distinguish formats.

---

### Region R11 (L) — Engineering / Operational criteria

| # | Concept | Tag | Conf | Note |
|---|---|---|---|---|
| L01 | **Pandoc-readable as input** | **core** | HIGH | If a format isn't Pandoc-readable, the prior architectural lever (Pandoc-as-converter) doesn't apply |
| L02 | **Pandoc-writable as output** | **core** | HIGH | Round-trip via Pandoc requires both ↔︎ |
| L03 | **Human-readable for hand-editing** | **core** | HIGH | Decision 5 (intake-edit-after-parse) depends on the canonical being editable |
| L04 | **Byte-stable on no-op save (editor-fragility)** | **core** | HIGH | The RTF rejection's load-bearing reason; tests every candidate |
| L05 | Schema-validatable (formal grammar / DTD / RNG) | sub | HIGH | XML formats (TEI / EPUB / DocBook / JATS) have formal schemas; markdown / RTF do not |
| L06 | Parser availability (Python libraries; mature vs experimental) | sub | HIGH | Pandoc covers most; pydantic for JSON-AST; lxml for XML; etc. |
| L07 | File-size efficiency (text vs zip-of-xml vs binary) | side | MED | EPUB / docx are zip-archives; XML is verbose; markdown / JSON are compact |
| L08 | Version stability (single canonical spec vs multiple dialects) | sub | HIGH | CommonMark has ONE spec; "markdown" has many; HTML5 single; RTF has many versions |

**Region R11 coverage:** 8 items. Four `core` (L01-L04) — the engineering trade-offs that decide between candidates.

---

### Region R12 (M) — Publishing / Downstream criteria

| # | Concept | Tag | Conf | Note |
|---|---|---|---|---|
| M01 | **Convertibility to reader formats (EPUB/MOBI/PDF/HTML)** | **core** | HIGH | Translation outputs eventually need to ship to readers; the canonical format should convert cleanly |
| M02 | Downstream reusability of canonical intake for publishing translation outputs | sub | MED | If canonical = EPUB or TEI, downstream publishing inherits format |
| M03 | Ecosystem tool support (ePub readers, dictionary integrations, annotation tools) | sub | MED | EPUB has rich ecosystem; markdown has rich dev-ecosystem; RTF has fading Microsoft-centric ecosystem |

**Region R12 coverage:** 3 items. One `core` (M01) — surfaces the user's likely "publishing" motivation explicitly.

---

### Region R13 (N) — Calibration-corpus-specific criteria

| # | Concept | Tag | Conf | Note |
|---|---|---|---|---|
| N01 | **Risale-i Nur's hashiye (marginalia) representation cost** | **core** | HIGH | Per-format: TEI native `<note place="margin">`; HTML5 `<aside>`; markdown via Pandoc footnote (positioned differently); RTF annotation (editor-fragile); EPUB via aside or footnote |
| N02 | **Mixed Turkish-Arabic interleaving** | **core** | HIGH | Tested at K07/K08 (lang+dir attributes) |
| N03 | Mevlana couplets as embedded poetry | sub | HIGH | Tested at K04 (verse representation) |
| N04 | Bismillah as formulaic opening | sub | HIGH | Tested by perception detector design, not by format; format's role is to preserve the markup |
| N05 | Qur'anic quotations as non-main-language spans | sub | HIGH | Tested at K07 (non-main-language span tagging) |

**Region R13 coverage:** 5 items. Two `core` (N01 + N02) — calibration-corpus-anchored tests; the others reduce to general criteria already named.

---

## State Summary

### Territory-specification echo

10 format families (A-J, with H-J flagged out-of-scope) + 4 requirement-criterion categories (K-N). All explicit-bounded by the input.

### Purpose-specification echo

Produce an analysis + decision/recommendation about the canonical intake format, with decision-mode `[validate-prior / re-decide-with-existing / design-new]` left open; serves the user's pushback motivations + the calibration-corpus richness.

### Coverage map

| Region | Coverage | Items | Aggregate relevance lean |
|---|---|---|---|
| R1 (substrate) | confirmed (orientation) | 4 | n/a |
| R2 (A. lightweight markup) | confirmed-present | 11 | 3 core (A01, A02, A05) |
| R3 (B. word-processor / rich-text) | confirmed-present | 3 | 1 core (B01 RTF) |
| R4 (C. ebook / publishing) | confirmed-present | 5 | 2 core (C01 EPUB 3, C03 MOBI) |
| R5 (D. structured / scholarly XML) | confirmed-present | 6 | 2 core (D01 TEI, D06 BITS) |
| R6 (E. web format) | confirmed-present | 3 | 1 core (E01 HTML5) |
| R7 (F. typesetting) | confirmed-present | 4 | 0 core |
| R8 (G. AST-as-storage) | confirmed-present | 5 | 3 core (G01 Pandoc-AST-JSON, G03 custom JSON-AST, G05 .compldoc) |
| R9 (H/I/J. out-of-scope) | confirmed-present | 5 | 0 core (all umbrella) |
| R10 (K. source-fidelity criteria) | confirmed-present | 16 | 7 core |
| R11 (L. engineering criteria) | confirmed-present | 8 | 4 core |
| R12 (M. publishing criteria) | confirmed-present | 3 | 1 core |
| R13 (N. corpus-specific) | confirmed-present | 5 | 2 core |

**Total items surfaced: 78 candidates (formats + criteria) + 4 substrate references.**

**Core-tagged formats: 12** — A01 Pandoc's markdown, A02 CommonMark, A05 AsciiDoc, B01 RTF, C01 EPUB 3, C03 MOBI, D01 TEI, D06 BITS, E01 HTML5+ARIA, G01 Pandoc-AST-JSON, G03 custom JSON-AST, G05 .compldoc.

**Core-tagged criteria: 14** — K01 chapter/para/section · K02 footnote · K03 marginalia · K04 embedded poetry · K07 lang attribute · K08 dir attribute · K09 NFC diacritics · K13 multi-volume · L01 Pandoc-readable · L02 Pandoc-writable · L03 human-readable · L04 byte-stable · M01 convertibility · plus calibration-corpus tests N01 + N02 (which reduce to K01/K03/K07).

### Confirmed-absent regions

None at this resolution.

### Concept-names list (load-bearing primitives — likely to recur)

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| `lossless round-trip` | vocabulary | G01/G02 | Format → AST → Format produces byte-identical (or at least information-identical) result |
| `editor-fragility` | vocabulary | L04 / B01 | A format where opening + saving with no edits produces different bytes; the RTF rejection's load-bearing reason |
| `scholarly text encoding` | structural-reference | D01 (TEI) | The discipline that designed TEI; native support for marginalia, apparatus, voice, lang |
| `schema-validatability` | vocabulary | L05 | Formal grammar / DTD / RNG / XSD allows automated validation; XML formats have it; markdown doesn't |
| `packaged-book format` | coined-term | R4 (EPUB/MOBI/FB2/BITS) | Single-file or zip representation of a whole book (multi-chapter, manifest, metadata) — versus per-file text formats |
| `AST-as-storage` | coined-term | R8 (G01-G05) | Strategy of storing the parsed-tree rather than surface syntax; bypasses surface-format limitations |
| `bracketed_spans` | structural-reference | A01 (Pandoc's markdown) | Pandoc-specific extension for inline span attributes (lang, dir, class); the lang= mechanism in the prior finding's NonMainLangPartsPolicy detector |
| `surface-format vs internal-AST` | coined-term | R8 | The distinction underlying the AST-as-storage strategy: store the parsed semantics, render to surface format on demand |
| `decision-mode` | vocabulary | MQA from articulate_simple | The joint axis [validate-prior / re-decide-with-existing / design-new] this inquiry's verdict will commit to |
| `apparatus criticus` | structural-reference | D01 (TEI) / K03 | Scholarly text-editing apparatus: textual variants, editor notes, manuscript witness markings |

### Recency distribution

All items: `{source: none, value: null}` (possibility-mode).

### Frontier flags

| Flag | Concept | Why frontier |
|---|---|---|
| F1 | Custom-format design as standalone deliverable | If decision-mode resolves to "design-new," the deliverable shape SHIFTS from comparison + recommendation to format-spec sketch. Sensemaking will need to surface this conditional. |
| F2 | The lang= + dir= attribute support across formats | Surfaced as K07+K08 but not yet feature-matrixed; downstream feature-matrix construction is implied |
| F3 | Pandoc's coverage of TEI / BITS / FB2 / EPUB-3 / HTML5 — is the conversion lossless? | The architectural lever from prior Decision 5 depends on Pandoc handling the new candidate cleanly; needs empirical verification |
| F4 | The "publishing-considerations" motivation — should the canonical intake format BE the publishing format? | If yes, EPUB 3 becomes load-bearing; if no, intake and publishing decouple |
| F5 | MOBI obsolescence — is the user aware it's deprecated? | The user named MOBI; honest response includes naming Amazon's deprecation |
| F6 | The decision-mode's third value (design-new) bypass possibility — is custom-AST genuinely needed, or do existing formats cover? | The strongest critique question for the design-new path |

### Workspace-populated status

`{populated: true, populated-at: 2026-06-17_17-55, extent: "10 format families + 4 criterion categories traversed; 78 candidates tagged + 10 concept-names extracted; 6 frontier flags emitted"}`

### Re-invocation parameters (suggested)

- **rsp1:** "feature-matrix construction across the 12 core-tagged formats against the 14 core-tagged criteria" — concrete adjudication input.
- **rsp2:** "TEI deep dive — is the scholarly-text-encoding gold standard worth the verbosity cost?" — focused on D01.
- **rsp3:** "EPUB 3 as canonical — what does that change in the prior architecture?" — focused on C01 + frontier F4.
- **rsp4:** "AST-as-storage strategy — Pandoc-AST-JSON vs custom JSON-AST" — focused on R8.

---

## Telemetry

- **Mode:** hybrid (artifact substrate + possibility candidates) · **Entry point:** signal-first
- **Cycles run:** 12 (one per region R2-R13; R1 substrate orientation only)
- **Items enumerated:** 78 candidates + 4 substrate references
- **Items tagged at each relevance level:** core = 26 (12 formats + 14 criteria) · sub = 28 · side = 19 · umbrella = 5
- **Sub-phase fired:** no (territory was explicit-bounded)
- **Workspace-overload trigger:** not fired
- **Failure modes checked:**
  - LAYER 1 mode 1 (missed-relevance): low risk — coverage spans 10 format families + 4 criterion categories; if a format isn't surfaced, it's likely a wiki-markup or slide format (correctly umbrella'd) or a truly niche option
  - LAYER 1 mode 2 (surfaced-irrelevance): some risk — 19 side-tagged items may be irrelevant noise; downstream pruning will handle
  - LAYER 1 mode 3 (over-coverage): possible — 78 candidates is broad; sensemaking will collapse via feature-matrix
  - LAYER 1 mode 4 (territory-mis-binding): no — exclusions honored (PDF-extraction-out, app-UI-out, translation-internals-out; H/I/J families flagged umbrella correctly)
  - LAYER 1 mode 5 (workspace overload): not fired (78 items manageable; the format space is genuinely large)
  - LAYER 1 mode 6 (artifact under-specification): no
  - LAYER 1 mode 7 (workspace-artifact desync): no (capture-at-moment)
  - LAYER 1 modes 8 & 9 (recency): n/a (no mtime)
- **Items with mtime / without mtime:** 0 / 78
- **Self-assessment verdict:** **PROCEED**

The inventory is broad enough to seed sensemaking's collapse-via-feature-matrix on the 12 core formats × 14 core criteria. The frontier flags name the load-bearing structural questions (decision-mode-conditional deliverable shape; lang/dir attribute support; Pandoc conversion lossless-ness; publishing-vs-intake decoupling; MOBI obsolescence honesty; custom-AST necessity).
