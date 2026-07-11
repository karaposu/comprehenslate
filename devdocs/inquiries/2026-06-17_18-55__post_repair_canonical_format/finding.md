---
status: active
model: claude-opus-4-7
effort: max
refines: devdocs/inquiries/2026-06-17_17-49__canonical_intake_format_deep_dive/finding.md
---

# Finding: Post-Repair Canonical Format

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-17_17-49__canonical_intake_format_deep_dive/finding.md` (the prior canonical-format inquiry; verdict: three-format layered architecture — Pandoc-AST-as-JSON canonical + Pandoc-markdown hand-edit + EPUB 3 publishing).

**Revision trigger:** new evidence. Two facts emerged after the prior finding was written. First, empirical inspection of the calibration-corpus PDFs (Asa-yı Musa: text-layer Arabic with broken bidi/shaping/order; Muhakemat: Arabic entirely absent from text-layer, pasted as images) showed intake's reconstruction work is heavy — OCR-recovered Arabic spans, style-recovered emphasis, structure-detected markers, paratext-stripped body, per-policy class-tagged elements. Second, the user reframed the question from "pick the canonical format" to "even if we repair the sources first, what document type holds the reconstructed result?" with EPUB / markdown / HTML named as candidates and Pandoc-AST-as-JSON explicitly omitted from the named set.

**What's preserved:** the three-layer architecture itself (canonical intake/translate-internal + hand-edit + publishing). Two of three cells survive unchanged: Pandoc's markdown with the canonical extension set remains the hand-edit format; EPUB 3 remains the publishing format. The architectural lever — Pandoc as the universal converter (per Decision 5 of the original intake-concepts inquiry) — survives and is strengthened. The five canonical-layer rejections from the prior finding (RTF, MOBI, TEI, EPUB-as-canonical, custom format) survive on the same structural grounds.

**What's changed:** the canonical-layer format. The prior finding committed Pandoc-AST-as-JSON as the on-disk canonical; this finding swaps that one cell for **HTML5** (W3C HTML Living Standard, written in the polyglot HTML5/XHTML5 syntactic style). The architecture stands; one cell changes. The relationship label is `refines:` — one cell of the prior architecture is swapped with stronger evidence, not the architecture itself rejected.

**What's new:** per-element provenance and confidence metadata as a load-bearing dimension. The reconstruction-is-heavy reframe makes this dimension format-choice-differentiating: the format must carry, on every reconstructed element, where the content came from (`data-source` = text-layer / OCR / hand-edit / derived), how confident the reconstruction is (`data-confidence` numeric), and which intake repair pass produced it (`data-intake-pass`). HTML5's `data-*` attributes (W3C HTML Living Standard) carry this natively on any element; markdown has no per-element metadata mechanism. This dimension is what shifts the canonical-layer optimum.

**Migration:** near-zero engineering cost. The prior finding's verdict committed JSON-AST as on-disk canonical but no production code was built on it (only `SKILL/references/config/schemas.py` exists in the repository beyond Mac app UI scaffolding). The Mac app's `PipelineConfig.swift` (line 42) already has `case md, html, plain, json` in its output enum, so even the UI layer is aware of HTML5 as a format option. Swapping the committed canonical format before engineering begins is free; this finding records the swap so v0.2 implementation begins against the correct target.

---

## Question

(From `_branch.md`'s Item I1.)

> **Maybe we should repair the sources before doing anything. But still — even if we repair them — what document type will be selected to hold that information? Yes we can use OCR-like things for repair, but the end result should be what? EPUB? Markdown file? HTML maybe? This is the real question.**

The Question carries an architectural decision about three things at once: the format the intake stage writes to disk after reconstructing a faithful representation from degraded sources (the canonical layer); the format a human picks up when they want to edit the intaken document (the hand-edit layer); and the format readers eventually consume (the publishing layer). The user named three candidates (EPUB / markdown / HTML) and pointedly did not name the prior inquiry's answer (Pandoc-AST-as-JSON), which is itself a signal worth honoring.

**Goal.** A format decision about post-repair document storage, given the empirical-PDF evidence about source-degradation and the recognition that reconstruction is heavy work. The decision must specify which format holds the reconstructed content at each architectural layer (canonical / hand-edit / publishing), why this format over the candidates the user named, and what concrete spec the format-choice commits the project to. Out of scope: how to repair the sources (OCR / bidi-fixing / style-recovery is granted as accepted technique); the inherited intake-concepts inquiry's Decisions 2-5 (quality target / IntakeDoc shape / 7-policy split / Pandoc-as-lever — all stand); PDF text-extraction quality as its own problem; the Mac app's UI itself.

---

## Finding Summary

- **Canonical (intake/translate-internal) format = HTML5** (W3C HTML Living Standard, written in polyglot HTML5/XHTML5 style). HTML5 replaces the prior finding's Pandoc-AST-as-JSON commitment at this layer.
- **Hand-edit format = Pandoc's markdown** (with the canonical extension set). Preserved unchanged from the prior finding.
- **Publishing format = EPUB 3.** Preserved unchanged from the prior finding. The HTML5 → EPUB 3 conversion is a near-identity transform because EPUB 3 content documents are themselves XHTML5 per the W3C EPUB 3.3 specification.
- **Decision-mode = REFINE the prior canonical-format inquiry.** The three-layer architecture stands; the architectural lever (Pandoc as universal converter) stands; two of three cells survive unchanged; one cell — the canonical-layer format — swaps from Pandoc-AST-as-JSON to HTML5. This is a load-bearing refinement of one cell, not an overturn of the architecture.
- **Per-element provenance via HTML5 `data-*` attributes is the new load-bearing dimension.** Every reconstructed element may carry `data-source` (where the content came from), `data-confidence` (how confident the reconstruction is), and `data-intake-pass` (which repair pass produced it). HTML5's `data-*` attributes carry this on any element per W3C HTML Living Standard §3.2.6; markdown cannot carry per-element metadata without sidecar files or class-attribute overloading that defeats the policy-class semantics.
- **Migration cost is near-zero.** No production code commits to JSON-AST as canonical yet. The Mac app's output-format enum already includes HTML. The swap happens before v0.2 implementation begins.
- **The original intake-concepts inquiry's Decisions 2-5 are preserved in semantic intent.** The quality target (structure-preservation), the IntakeDoc shape (tree-of-containers + cross-referenced flat collections — now realized as parsed HTML5 DOM instead of a Pandoc-AST-wrapping pydantic class), the 7-policy intake-perception split, and Pandoc as architectural lever all carry forward. The 38 intake-handling concepts from the original carry forward; references that pointed at JSON-AST node types now point at HTML5 element types.
- **JSON-AST is not lost.** It is reachable on demand from HTML5 canonical via `pandoc -f html -t json canonical.html`, for any tool that needs the AST shape. The change is from JSON-AST as the persistent canonical to HTML5 as the persistent canonical with JSON-AST reachable when needed.

---

## Finding

The project is comprehenslate: a translation skill calibrated against Said Nursi's Risale-i Nur theological texts, with a Mac application as its v0.1 surface. The intake stage's job is to consume source documents (currently PDFs) and produce a faithful representation that downstream translation can operate on. The earlier intake-concepts inquiry settled who handles what (quality target, IntakeDoc shape, the seven schema policies, Pandoc and OCR as architectural levers). The earlier canonical-format inquiry decided what file the intake stage actually writes to disk and concluded with a three-format layered architecture: Pandoc-AST-as-JSON for canonical (intake's output and translation's input), Pandoc's markdown for hand-editing, EPUB 3 for publishing.

This inquiry reopens one cell of that decision. Two pieces of evidence forced the reopening. The first is empirical: I inspected two real Risale-i Nur PDFs in the calibration corpus. Asa-yı Musa (1996 edition) has Arabic in its text-layer but the bidi (bidirectional text) ordering and the shaping (the rules that produce contextual letter forms in Arabic script) are broken — `pdftotext` and Pandoc's PDF reader both produce garbled Arabic with letters and diacritics scattered across lines in wrong order. Muhakemat is worse: its Arabic isn't in the text-layer at all; the original Word source pasted Arabic as bitmap images, so every Bismillah opening, every embedded Hadith, every closing verse is invisible to text-layer extraction. The Turkish text-layer in Muhakemat is pristine; the Arabic-as-image gap is total. Both books also lose italic and bold styling under default extraction (some PDF tools recover it but it requires an extra pass), and both inline paratext like running headers and page numbers into the body content. The second piece of evidence is the user's reframe of the question itself: "even if we repair the sources first, what document type holds the reconstructed result?" — naming EPUB, markdown, HTML, and conspicuously not naming Pandoc-AST-as-JSON. The pattern in the user's framing across multiple turns has been to name documents, not data structures.

Taken together, these two pieces of evidence shift the canonical-layer optimum. The reconstruction-is-heavy frame means the format must carry per-element provenance — where each piece of content came from (text-layer, OCR-recovered, hand-corrected, derived) — and per-element confidence (Tesseract emits raw OCR confidence scores; detector rules emit calibrated confidence levels). Without this metadata the canonical loses verifiability against the source; the auditor cannot tell which parts of the document the system reconstructed and which parts came through clean. The user-pattern frame means the canonical should be a document — something a human can open in a text editor or a browser and read — rather than a serialized data structure. These two pressures push toward HTML5.

### Why HTML5 specifically

HTML5 (the W3C HTML Living Standard, written in the polyglot HTML5/XHTML5 syntactic style — the polyglot HTML5 concept, originally defined by the W3C Polyglot Markup NOTE which was discontinued in 2014, remains usable as a self-imposed writing convention) wins at the canonical layer for several reasons that compose.

It is simultaneously a document and a data shape. A reader can open `canonical.html` in any text editor or any browser and read it; an auditor can diff two versions of it; an engineer can query its tree via the DOM. JSON-AST is the second of those (data) but not the first (document). Markdown is the first but cannot carry per-element metadata cleanly.

It has the right primitives natively. HTML5 has `lang` and `dir` as global attributes on any element (per W3C HTML Living Standard §3.2.6) — so an Arabic span inside Turkish prose becomes `<span lang="ar" dir="rtl">…</span>` without any extension. HTML5 has `data-*` attributes (also W3C HTML Living Standard §3.2.6) — so per-element provenance becomes `<aside class="marginalia" id="h1" data-source="ocr-tesseract" data-confidence="0.92" data-intake-pass="2">…</aside>` directly. HTML5 has `<em>` and `<strong>` as semantic emphasis elements separated from visual styling. HTML5 has `<section>`, `<article>`, `<aside>`, `<figure>`, `<figcaption>`, `<blockquote>` as sectioning and content elements that map cleanly onto the reconstructed document's structure.

It is the substrate of EPUB 3. The W3C EPUB 3.3 specification defines EPUB Content Documents as XHTML5 with a polyglot profile. This means the conversion from HTML5 canonical to EPUB 3 publishing is a near-identity transform: package the canonical HTML5 files, add an OPF manifest, add metadata, zip with the `.epub` extension. Pandoc handles this packaging directly via `pandoc -f html -t epub3 -o published.epub canonical.html`. Compared to the prior architecture's JSON-AST → EPUB Pandoc-render path, the new path is structurally cleaner because the canonical and the publishing layers share the same underlying markup.

It is web-standard and not Pandoc-locked. Pandoc's JSON-AST is defined by Pandoc and its schema is Pandoc-version-specific; future Pandoc deprecation or migration would force re-derivation of stored canonicals. HTML5 is a W3C standard with broad ecosystem support; the canonical survives any single tool's deprecation.

It round-trips losslessly via Pandoc. Pandoc reads and writes HTML5 (per Pandoc's documented format matrix); the AST-representable subset survives `html → json → html` cleanly. The hand-edit workflow becomes: user edits markdown, Pandoc converts `markdown → html5`, intake re-loads the HTML5 canonical.

### Honest caveats

Three caveats balance the picture; preserving them keeps the commitment honest rather than triumphalist.

First, HTML5 is more verbose than markdown for the same prose. `<p>The text</p>` against `The text`; `<em>word</em>` against `*word*`. At the canonical layer this is acceptable because the reconstructed content is already tag-dense (Arabic spans + class-tagged policy elements + provenance attributes), so the verbosity savings markdown would offer don't accumulate. Storage isn't a constraint, and the canonical layer is for machine reading and processing, not for human prose-editing — that's the hand-edit layer's job, which is exactly where markdown stays.

Second, HTML5 has parser variability that JSON-AST does not. JSON-AST via Pandoc's `panflute` Python library has a single canonical parser and serialization shape; HTML5 has multiple parser implementations (`lxml.html`, `html5lib`, browser engines) with documented edge-case divergence around whitespace, comment handling, and attribute ordering. The project bounds this operationally with three commitments: pin a Pandoc version (see the Pandoc-version-pinning DEFERRED item below); write canonical HTML5 via Pandoc only (a single source of truth for canonical generation); read canonical HTML5 via a single named parser (the choice — `lxml.html` versus `html5lib` versus a thin pydantic layer wrapping either — is named in the in-memory representation Open Question). These bounds make HTML5's parser variability practically equivalent to JSON-AST's determinism at the canonical layer without losing HTML5's other advantages.

Third, JSON-AST has a genuine machine-readability advantage. Direct object-tree access via `panflute` is ergonomically nicer for some kinds of operations than DOM traversal via `lxml.html` or `html5lib` — the AST shape is a richer typed tree where every node knows its own kind, while the DOM is a more uniform element-tree where types are inferred from tag names. HTML5 has compensating advantages (it is a document; it is W3C-standard; it is the EPUB substrate; it has native `lang` / `dir` / `data-*`), and those advantages outweigh the access-shape difference at the canonical layer. The project does not lose JSON-AST as a working representation: when a tool needs the AST shape, `pandoc -f html -t json canonical.html` produces it deterministically.

### How the calibration corpus maps onto HTML5

The seven schema policies (`NonMainLangPartsPolicy`, `SourceApparatusPolicy`, `VoiceMarkingPolicy`, `ArchaicRegisterPolicy`, `HonorificsPolicy`, `FormulaicOpeningPolicy`, `EmbeddedPoetryPolicy` — all defined in `SKILL/references/config/schemas.py`) each map onto HTML5 with concrete element + class + `data-*` patterns. The patterns below are illustrative working assumptions; the per-policy class-attribute conventions are committed for design in MUST 2 of Next Actions.

**Source apparatus (hashiye — Said Nursi's marginalia).** Marginalia stored at body-end as `<aside>` with provenance attributes; body references via inline `<a>` anchors:

```html
<p>Body text with <a href="#h1" class="marginalia-ref">[h1]</a> reference.</p>
…
<aside class="marginalia" id="h1"
       data-source="ocr-tesseract"
       data-confidence="0.92"
       data-intake-pass="2">
  Marginalia body text here.
</aside>
```

**Embedded poetry (Mevlana couplets in prose).** Verse-block in `<figure>` with attribution in `<figcaption>`:

```html
<figure class="couplet" data-attribution="Mevlana">
  <blockquote>
    <p>Line one of the couplet.</p>
    <p>Line two of the couplet.</p>
  </blockquote>
  <figcaption>— Mevlana</figcaption>
</figure>
```

**Formulaic openings (Bismillah, Hamd).** Paragraph with class and tradition attribute, position-constrained to section-start:

```html
<section>
  <p class="formulaic-opening"
     data-tradition="islamic"
     data-source="ocr-tesseract"
     data-confidence="0.95">
    <span lang="ar" dir="rtl">بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيم</span>
  </p>
  <p>Section body begins here.</p>
</section>
```

**Non-main-language parts (Arabic spans within Turkish narrative).** Inline span with `lang` and `dir`:

```html
<p>
  Turkish prose continues
  <span lang="ar" dir="rtl"
        data-source="ocr-tesseract"
        data-confidence="0.87">ٱلْحَمْدُ لِلَّٰهِ</span>
  and continues again.
</p>
```

**Voice marking (Nursi's authorial voice vs cited authorities).** Inline `<span class="voice-cited">` with `cite` attribute for sources, or block-level `<blockquote class="voice-cited">` for longer citations.

**Archaic register (Ottoman Turkish archaisms).** Inline `<span class="archaic-register">` with `data-archaism-type` attribute.

**Honorifics (Islamic honorific markers — R.A., A.S., Radıyallahü Anh).** Inline `<span class="honorific">` with `data-tradition` and `data-form` attributes.

The uniform `data-*` provenance convention — `data-source` for origin (text-layer / OCR-tesseract / hand-edit / derived), `data-confidence` for numeric reconstruction confidence (Tesseract's raw 0–100 normalized to a project 0.0–1.0 scale), `data-intake-pass` for the repair pass that produced the element — applies across every policy. The exact field-name + value-vocabulary commitments are the subject of MUST 3 of Next Actions.

### How the in-memory IntakeDoc relates

The original intake-concepts inquiry's Decision 3 committed the in-memory IntakeDoc as a tree-of-containers plus cross-referenced flat collections. With HTML5 as on-disk canonical, the in-memory representation is the parsed HTML5 DOM (via `lxml.html` or `html5lib`) or, equivalently, the Pandoc AST obtained from `pandoc -f html -t json` (accessed via `panflute`). The two shapes are isomorphic. Each `<section>` is a Container; each `<p>` is a Paragraph; each `<aside class="marginalia">` is an apparatus entry in the marginalia flat collection; cross-references via `<a href="#id">` map directly to DOM lookups by `id`. The semantic intent of Decision 3 is preserved; the concrete representation shifts from a custom Pandoc-AST-wrapping pydantic class to a parsed HTML5 DOM (with a thin pydantic layer remaining available as a working option for project-specific invariant enforcement — that choice is in the in-memory representation Open Question).

### What this inquiry rejected and why

**JSON-AST as the on-disk canonical.** Rejected for two reasons. Structurally, the capability evidence shows HTML5 ties JSON-AST on every data-format axis (lossless round-trip via Pandoc; explicit-tree storage; queryable) and wins on every other relevant axis (document-shape; W3C-standard; EPUB substrate; native `lang` / `dir` / `data-*`). Operationally, JSON-AST is Pandoc-specific — its schema and serialization are defined by Pandoc; future Pandoc deprecation or migration would force re-derivation. JSON-AST is preserved as on-demand reachable from HTML5: `pandoc -f html -t json canonical.html` produces it for any tool that needs the AST shape, without persisting it as a separate canonical.

**Monolithic single-format (one format serves all three layers).** Rejected because the three layers have structurally distinct optima. Canonical needs machine-queryability plus per-element provenance; hand-edit needs reading-order-naturalness plus byte-stability under no-op editor save; publishing needs reader-ecosystem plus packaged-book delivery. Markdown alone fails at canonical (no per-element metadata). EPUB alone fails at hand-edit (zip plus manifest is heavyweight). HTML5 alone is closest to a universal — but markdown remains preferable for prose-heavy hand-editing because it is reading-order-natural and has minimal tag noise. The three-layer architecture survives because the per-layer use-case distinction survives.

**Custom format (custom JSON-AST or a `.compldoc` markdown+YAML hybrid).** Rejected because HTML5 with project-specific class-attribute conventions and a project RNG (Relax NG) schema profile covers what custom-format motivations would seek. Recreating those mechanisms in a project-specific format reinvents what HTML5 already provides.

**Dual *persistent* JSON-AST + HTML5 storage.** Rejected because maintaining two persistent canonicals creates synchronization debt — one must be authoritative; the other is derived. With HTML5 authoritative, JSON-AST is reachable on demand without needing persistent storage; the dual-representation use case is served without the dual-storage cost. (Dual representation itself — having the AST shape available when needed — is preserved via the on-demand Pandoc invocation.)

**TEI (Text Encoding Initiative) as canonical.** Rejected on architectural grounds: per Pandoc's documented format matrix, Pandoc cannot read TEI as input (it can write TEI Simple as output). Choosing TEI as canonical would force a custom TEI reader, which would break Decision 5 of the original intake-concepts finding — Pandoc as the architectural lever (the universal converter the project relies on). TEI remains available as a future archival output: `pandoc -f html -t tei` produces it from HTML5 canonical when a scholarly archival use case emerges or cross-corpus validation surfaces a TEI requirement.

**RTF (Rich Text Format) — unchanged from prior.** Editor-fragility: Microsoft Word, Apple Pages, Apple TextEdit, and LibreOffice each implement different subsets of the RTF spec and re-serialize on save through their rich-text engines. The hand-edit recovery workflow depends on byte-stability under no-op save, which RTF cannot guarantee in any editor that interprets it as rich text. RTF survives as an accepted user-provided input format that intake reads via Pandoc and converts to HTML5 canonical.

**MOBI — unchanged from prior.** Amazon deprecated `.mobi` in 2022; Kindle Direct Publishing stopped accepting `.mobi` uploads, and Kindle devices use `.azw3` / `.kfx`. Pandoc has no native MOBI writer. The Kindle distribution path is EPUB 3 → Send to Kindle → Amazon's conversion, already part of the publishing layer.

---

## Inherited Commitments Re-test

This finding refines the prior canonical-format inquiry and inherits commitments through that chain back to the original intake-concepts inquiry. Each inherited commitment is re-tested below.

### Prior 1 — the prior canonical-format inquiry

**Source:** `devdocs/inquiries/2026-06-17_17-49__canonical_intake_format_deep_dive/finding.md`. This finding declares `refines:` of this prior in its frontmatter.

- **Commitment:** the three-format layered architecture itself (canonical intake/translate-internal + hand-edit + publishing as use-case-distinct layers).
  - **Re-test status:** **RE-TESTED — commitment confirmed.**
  - **Evidence:** sensemaking re-evaluated the layered-vs-monolithic question against the new empirical evidence and the new provenance dimension; the per-layer use-case distinction holds (canonical needs machine-queryability + per-element provenance; hand-edit needs reading-order-naturalness + byte-stability; publishing needs reader-ecosystem + packaged-book). The three optima do not collapse.

- **Commitment:** canonical-layer format = Pandoc-AST-as-JSON.
  - **Re-test status:** **RE-TESTED — commitment found INVALID** when the full requirement set (including the new per-element provenance + confidence dimension surfaced by the reconstruction-is-heavy reframe) is evaluated and the emergent HTML5-as-universal candidate is included in the candidate space.
  - **Evidence:** the capability evidence assembled in sensemaking shows HTML5 ties JSON-AST on every data-format axis and wins on every other relevant axis (document-shape; W3C-standard; EPUB substrate; native `lang`/`dir`/`data-*`). The prior's choice was defensible within its candidate-space framing, but the framing was incomplete; the new framing's full evidence shifts the verdict. **This finding's canonical = HTML5.**

- **Commitment:** hand-edit format = Pandoc's markdown with the canonical extension set.
  - **Re-test status:** **RE-TESTED — commitment confirmed.**
  - **Evidence:** markdown's reading-order-naturalness and byte-stability properties (defined in the prior finding) remain the load-bearing reasons for choosing markdown at the hand-edit layer; neither property is undermined by the new evidence. The only change is the round-trip target: markdown now converts to HTML5 (via `pandoc -f markdown -t html5`) instead of to JSON-AST.

- **Commitment:** publishing format = EPUB 3.
  - **Re-test status:** **RE-TESTED — commitment confirmed and strengthened.**
  - **Evidence:** EPUB 3 content documents are XHTML5 per the W3C EPUB 3.3 specification. With HTML5 as canonical, the canonical → publishing transform becomes near-identity (package the HTML5 + add an OPF manifest + zip), which is structurally cleaner than the prior's JSON-AST → EPUB Pandoc-render path.

- **Commitment:** Pandoc as architectural lever (the universal converter).
  - **Re-test status:** **RE-TESTED — commitment confirmed.**
  - **Evidence:** all three formats in the refined architecture are Pandoc-native ↔ targets (Pandoc reads and writes HTML5; reads and writes Pandoc-markdown; writes EPUB 3). The lever remains universal.

- **Commitment:** the prior's five canonical-layer rejections (RTF, TEI, MOBI, EPUB-as-canonical, custom format).
  - **Re-test status:** **RE-TESTED — commitment confirmed.** All five rejections survive on the same structural grounds. TEI's frontier status (deferred-but-not-dismissed; available as future archival output via Pandoc) is preserved.

### Prior 2 — the original intake-concepts inquiry

**Source:** `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`. This finding does not directly `refines:` the original (the prior canonical-format inquiry is the intermediate refiner) but inherits Decisions 2-5 through the chain.

- **Commitment:** Decision 2 — quality target = structure-preservation.
  - **Re-test status:** **RE-TESTED — commitment confirmed.**
  - **Evidence:** HTML5's explicit-tree storage preserves structure even more directly than surface markdown; the target is unchanged.

- **Commitment:** Decision 3 — IntakeDoc shape = tree-of-containers + cross-referenced flat collections.
  - **Re-test status:** **RE-TESTED — commitment confirmed but frame revised.** The semantic intent (tree-of-containers + cross-referenced flat collections) holds; the frame revision is that the concrete representation shifts from a custom Pandoc-AST-wrapping pydantic class to a parsed HTML5 DOM (with a thin pydantic layer remaining as a working option).
  - **Evidence:** the tree-of-containers maps to `<section>` / `<article>` / `<p>` nesting; the cross-referenced flat collections map to `<aside>` / `<figure>` / `<blockquote>` collected and referenced via `<a href="#id">` plus matching `id` attributes. The structural intent is preserved; the substrate library shifts.

- **Commitment:** Decision 4 — 7-policy intake-perception + translate-rendering split.
  - **Re-test status:** **RE-TESTED — commitment confirmed.**
  - **Evidence:** the seven detectors (`NonMainLangPartsPolicy`, `SourceApparatusPolicy`, `VoiceMarkingPolicy`, `ArchaicRegisterPolicy`, `HonorificsPolicy`, `FormulaicOpeningPolicy`, `EmbeddedPoetryPolicy`) operate on the in-memory representation regardless of whether it is HTML5 DOM or Pandoc AST; their specs refine to reference HTML5 elements + classes + `data-*` attributes (per the per-policy patterns in the Finding section). Semantic refinement, not redesign.

- **Commitment:** Decision 5 — Pandoc + OCR architectural lever.
  - **Re-test status:** **RE-TESTED — commitment confirmed and strengthened.**
  - **Evidence:** all three formats in the refined architecture are Pandoc-native targets; HTML5 is a clean Pandoc reader/writer target. The OCR sub-pipeline (Tesseract for broken-bidi Arabic in Asa-yı Musa; Tesseract for image-only Arabic in Muhakemat) is unchanged — OCR produces text that intake assembles into HTML5 elements with `data-source="ocr-tesseract"` provenance attributes.

- **Commitment:** the 38 intake-handling concepts enumerated in the original.
  - **Re-test status:** **RE-TESTED — commitment confirmed but frame revised.** The semantic intent of each concept is preserved; references that pointed at JSON-AST node types now point at HTML5 element types where applicable.
  - **Evidence:** the new per-element provenance + confidence dimension is additive (new concept), not contradictory to any of the 38.

### Summary

No commitment from either prior is silently absorbed. The prior canonical-format inquiry's one canonical-layer cell is invalidated with cited evidence (the capability re-evaluation against the broadened candidate space and the new provenance dimension); the other five commitments are confirmed. The original intake-concepts inquiry's Decisions 2-5 are confirmed, with Decision 3 and the 38-concepts inheritance carrying a frame revision (concrete representation shifts from JSON-AST node types to HTML5 element types in semantic intent).

---

## Next Actions

### MUST

- **What:** design the HTML5 schema / validation profile for canonical conformance. Specify which HTML5 features are required (sectioning elements, semantic emphasis, attribute conventions); specify which are forbidden (script and style elements; what kinds of metadata in `<head>`); decide between writing a project Relax NG (RNG) schema and operating off `html5validator` (Python wrapper around vnu.jar) plus project-internal Python invariant checks. Ship `comprehenslate/intake/html5_profile.rng` (or the chosen equivalent) plus documentation.
  - **Who:** a downstream `/traverse` inquiry.
  - **Gate:** condition-bound — before any v0.2 intake-stage HTML5 generation code lands.
  - **Why:** without a project-specific profile, canonical-conformance cannot be checked beyond W3C-validity; the intake pipeline cannot reject malformed-but-W3C-valid output.

- **What:** design per-policy class-attribute conventions. Decide between (a) role-based class names (`class="marginalia"`, `class="couplet"`, `class="formulaic-opening"`, `class="voice-cited"`, `class="archaic-register"`, `class="honorific"`) which is this finding's working assumption; (b) policy-named via `data-policy="source-apparatus"` mapped to the `schemas.py` policy class names; (c) a hybrid combining both. Ship `comprehenslate/intake/policy_conventions.md`.
  - **Who:** a downstream `/traverse` inquiry (smaller scope than the schema profile).
  - **Gate:** condition-bound — before the seven detector designs are spec'd (since each detector's class-tagging behavior depends on this convention).
  - **Why:** the convention is the contract between detector perception and HTML5 storage; without it, each detector improvises and the canonical loses uniformity.

- **What:** design the per-element provenance encoding pattern. Pin `data-source` value vocabulary to a closed enum (text-layer / OCR-tesseract / hand-edit / derived); pin `data-confidence` numeric range and the Tesseract-to-internal scale conversion (Tesseract emits 0–100; project internal scale is 0.0–1.0); pin `data-intake-pass` semantics (pass-number or pass-name or both). Ship `comprehenslate/intake/provenance_spec.md`.
  - **Who:** a downstream `/traverse` inquiry.
  - **Gate:** condition-bound — before any intake-stage code emits `data-*` provenance attributes.
  - **Why:** per-element provenance is the load-bearing new dimension; if encoders, decoders, and auditors don't share a vocabulary, the dimension becomes noise.

### COULD

- **What:** design and ship the HTML5 → EPUB 3 packaging script. Specify Pandoc invocation flags; OPF manifest construction; cover-image handling; per-chapter file structure within the EPUB; CSS template for Arabic typography (font fallback chain; RTL block handling; per-policy CSS classes). Ship `comprehenslate/publish/epub.py` plus a CSS template.
  - **Who:** an engineering task plus a small downstream inquiry for the CSS template.
  - **Gate:** condition-bound — when intake produces its first HTML5 canonical output.
  - **Why:** HTML5 → EPUB is near-identity but the project-specific work (CSS template, OPF metadata, cover image) is non-trivial.
  - **Depends-on:** the per-policy class-attribute conventions MUST item (because CSS selectors target the conventions). This COULD is GATED — do not act until that MUST resolves.

- **What:** define the HTML5-to-markdown round-trip stability subset for the hand-edit workflow. Enumerate Pandoc-markdown features (per the canonical extension set); test each via `pandoc md → html → md` cycle; document which features survive losslessly and which drift; commit the hand-edit contract to the surviving subset.
  - **Who:** a downstream `/traverse` inquiry.
  - **Gate:** condition-bound — before the hand-edit recovery workflow is documented for users.
  - **Why:** hand-edit byte-stability under no-op save is load-bearing; this refines which markdown features hand-editors may rely on.

- **What:** build an end-to-end calibration prototype taking one Risale-i Nur volume (Muhakemat exercises image-only Arabic OCR; Asa-yı Musa exercises broken-bidi text-layer Arabic — choose whichever stress-tests more policy targets) through intake (with OCR for the Arabic) → HTML5 canonical → EPUB 3 publishing. Verify the EPUB output in at least three readers (Apple Books, Calibre, Google Play Books).
  - **Who:** an engineering task plus tester evaluation.
  - **Gate:** condition-bound — after the three MUST items above have ship-ready first drafts.
  - **Why:** the prototype is the calibration anchor; until a real volume goes through end-to-end, the architectural commitment is structural-only, not empirically validated.
  - **Depends-on:** all three MUST items (schema profile, class conventions, provenance encoding) because the prototype tests against them. This COULD is GATED — do not act until those MUSTs resolve.

### DEFERRED

- **What:** pin a project Pandoc version and document the upgrade-test protocol (run the calibration prototype's intake + EPUB conversion against the new Pandoc version; verify the round-trip-stable subset survives).
  - **Gate:** condition-bound — revive when the project first ships v0.2 intake-stage code that depends on Pandoc, or when a critical Pandoc release surfaces edge cases that affect HTML5 read/write.
  - **Why (if revived):** HTML5 conformance is W3C-stable, but Pandoc's HTML5 reader/writer behavior may shift between versions for edge cases. Pinning bounds the operational risk that compounds with HTML5's parser-implementation variability.

- **What:** commit a "minimum HTML5 features required" snapshot of the W3C HTML Living Standard at the time of canonical commitment, plus a feature-snapshot update cadence policy.
  - **Gate:** condition-bound — revive when a HTML5 Living Standard change actually affects a feature the project depends on, or when project policy review surfaces version-stability as an operational concern.
  - **Why (if revived):** the Living Standard evolves continuously; backward compatibility is its design constraint, so the practical risk is low, but explicit snapshot policy bounds the dependency surface.

- **What:** investigate TEI as a future archival output format. Document the Pandoc `pandoc -f html -t tei` path; specify the revival trigger.
  - **Gate:** condition-bound — revive when the project names a scholarly archival use case, or when cross-corpus validation surfaces a TEI requirement.
  - **Why (if revived):** TEI is the scholarly text-encoding standard; preserving translations in a format the TEI community recognizes is valuable for academic distribution.

- **What:** evaluate cross-corpus validation. Pick a second-corpus exemplar (Talmud apparatus criticus, Vedic texts, Christian patristic editions, modern academic books); exercise intake → HTML5 canonical → publishing; surface architectural strains.
  - **Gate:** condition-bound — revive when the calibration corpus (Risale-i Nur) has been stably processed and the project's ambition expands beyond it.
  - **Why (if revived):** the calibration corpus is the structural anchor; cross-corpus is the generalization check that protects against Risale-i-Nur-specific over-fit.

- **What:** evaluate whether archival / historical preservation needs its own temporal layer (a fifth layer alongside canonical / hand-edit / publishing — for example a long-term-stable HTML5 profile, or TEI, or JATS).
  - **Gate:** condition-bound — revive when project maturity surfaces decade-scale preservation needs distinct from publishing-cycle needs.
  - **Why (if revived):** the three current layers cover intake/translate, hand-edit, and publishing; archival is a different temporal axis (decades, not publishing-cycle) that may need separate optima.

- **What:** evaluate publishing-output format expansion beyond EPUB 3. Enumerate additional Pandoc-writable targets from HTML5 (PDF via weasyprint or wkhtmltopdf, reveal.js for slides, LaTeX for academic submissions); evaluate each against use cases.
  - **Gate:** condition-bound — revive when a specific use case names a publishing target beyond EPUB.
  - **Why (if revived):** HTML5 → many publishing formats is a structural advantage; expansion is gated by use case, not by capability.

- **What:** commit the in-memory representation choice. Decide between (a) parsed HTML5 DOM via `lxml.html`; (b) parsed HTML5 DOM via `html5lib`; (c) Pandoc AST via `panflute`; (d) a thin pydantic layer wrapping either DOM library. Evaluate by detector-design ergonomic fit + querying speed + serialization-to-canonical-HTML5 stability.
  - **Gate:** condition-bound — revive when the seven detector designs (per Decision 4 of the original intake-concepts finding) begin formal specification.
  - **Why (if revived):** the two shapes (DOM and AST) are isomorphic but Python tooling fit differs; the detector ergonomics depend on which library they target.

---

## Reasoning

This section explains why the finding's commitments hold against the alternatives that were generated and considered. It is organized by what survived, what was killed, and how contradictions across the upstream disciplines were reconciled.

### What survived adversarial scrutiny

**HTML5 as canonical.** The capability evidence was built as a 5-format × 18-requirement matrix (the five formats being Pandoc-AST-as-JSON, Pandoc-markdown, HTML5, EPUB 3, and a hypothetical custom format like `.compldoc`). Each cell was labelled native (✓✓), via-extension (✓+ext), via-workaround (✓wa), or not-supported (✗) with the W3C / Pandoc / EPUB external anchor cited. HTML5 ties JSON-AST on every data-format axis (lossless round-trip via Pandoc, explicit-tree storage, queryability, schema-validatability via RNG, document-level provenance via `<meta>`) and wins on every other axis. The decisive cell is per-element provenance + confidence: JSON-AST and HTML5 are tied (both can hold per-element metadata natively); markdown cannot (no per-element metadata mechanism); EPUB document-level OPF metadata does not extend to per-element. The reconstruction-is-heavy frame makes this row load-bearing.

Adversarial testing surfaced one matrix-omission that warranted a caveat: parser-implementation determinism. JSON-AST via `panflute` has a single canonical parser; HTML5 has multiple parsers (`lxml.html`, `html5lib`, browser engines) with documented edge-case divergence. The verdict adjusted from "Pareto-dominant" to "Pareto-dominant on every format axis, with operational bounds on the one axis (parser-determinism) where JSON-AST has a strict advantage." The operational bounds (parser-pinning, canonical-write-via-Pandoc-only, single named reader parser) close the gap practically without losing HTML5's other advantages.

**Markdown as hand-edit; EPUB 3 as publishing.** Both inherit from the prior canonical-format inquiry with their original rationales intact. Markdown's reading-order-naturalness and byte-stability under no-op editor save make it right for the hand-edit layer; this finding's HTML5-as-canonical does not undermine those properties. EPUB 3's reader ecosystem (Apple Books, Google Play Books, Calibre, Adobe Digital Editions, Kobo, Foliate, Thorium) and the Kindle distribution path (EPUB 3 → Send to Kindle → Amazon's converter) remain the right publishing choice; the conversion from HTML5 canonical to EPUB 3 is structurally cleaner (near-identity) than the prior's JSON-AST → EPUB path.

**The three-layer architecture itself.** Sensemaking re-litigated the monolithic-vs-layered question against the broadened candidate space and the new evidence. The three optima do not collapse: canonical needs machine-queryability + per-element provenance (rules out markdown alone); hand-edit needs reading-order-naturalness + byte-stability (rules out HTML5 alone); publishing needs reader-ecosystem + packaged-book delivery (rules out markdown or HTML5 alone). The use-case distinction is real; the architecture stands.

### What was killed and why

**JSON-AST as the persistent on-disk canonical.** Killed in this inquiry's sensemaking on capability-matrix grounds (HTML5 ties on every data-format axis and wins elsewhere) plus the structural concern that JSON-AST is Pandoc-version-locked (future Pandoc deprecation forces re-derivation). The user-pattern signal (consistently naming documents, never naming data structures across multiple turns of the conversation) is a secondary reason, not the primary; the matrix evidence is structural and load-bearing. JSON-AST has a genuine machine-readability advantage that HTML5 must work to match (direct AST-tree access via `panflute` versus DOM access via `lxml.html` or `html5lib`); HTML5's compensating advantages outweigh the access-shape difference at the canonical layer, but the trade-off is real and named. JSON-AST is not lost: it is reachable on demand from HTML5 via `pandoc -f html -t json canonical.html` for any tool that needs the AST shape.

**Monolithic single-format.** Killed structurally because the three layers have different optima (per the architecture-survives reasoning above). This rejection survived the same adversarial test in the prior canonical-format inquiry and was re-tested here against the new evidence; the conclusion holds.

**Custom format (custom JSON-AST schema or `.compldoc` markdown+YAML hybrid).** Killed because HTML5 with project-specific class-attribute conventions and a project RNG schema covers everything a custom format would seek; recreating those mechanisms in a project-specific format reinvents what HTML5 already provides.

**Dual *persistent* JSON-AST + HTML5 storage.** Killed because two persistent canonicals create synchronization debt — one must be authoritative; the other is derived. With HTML5 authoritative, JSON-AST is reachable on demand without storage cost. Dual representation (having the AST shape available when needed) is preserved; only dual persistent storage is rejected.

**TEI as canonical.** Killed on architectural grounds, not merely operational. Pandoc cannot read TEI as input (it can write TEI Simple as output); choosing TEI as canonical would force a custom TEI reader, which would break Decision 5 of the original intake-concepts finding — Pandoc as the architectural lever (the universal converter the project relies on). TEI as a future archival *output* is preserved (`pandoc -f html -t tei` produces it from HTML5 canonical) and is in DEFERRED with a revival trigger.

**RTF and MOBI.** Killed unchanged from the prior canonical-format inquiry. RTF: editor-fragility (every word processor implements a different RTF subset and re-serializes on save), which defeats hand-edit byte-stability. MOBI: Amazon-deprecated in 2022; Pandoc has no native MOBI writer; Kindle distribution path goes through EPUB 3 + Amazon's converter, already covered by the publishing layer.

### Contradictions reconciled across upstream disciplines

The articulation surfaced two open axes — decision-mode (re-affirm prior / overturn-with-named-candidate / restate-architecture) and temporal-layer-scope (canonical only / monolithic / three-layer-restated). Sensemaking adjudicated both: decision-mode = restate-architecture-as-refinement (one cell swapped); temporal-layer-scope = three-format-layered-architecture-restated with the canonical cell changed.

Surfacing enumerated 88 candidates across two dimensions (decision-mode × temporal-layer). Sensemaking compressed those to five core format-candidates (JSON-AST, Pandoc-md, HTML5, EPUB 3, custom format) plus an emergent candidate (HTML5-as-universal — testing whether one format could serve all three layers). The capability matrix evidence settled the universal question in the negative (markdown remains better at the hand-edit layer for prose-heavy editing because of reading-order-naturalness) while settling the canonical-layer question in HTML5's favour.

Critique surfaced four wording-level refinements that this finding integrates directly into its body:
- The parser-implementation-determinism axis: named in the matrix description and addressed via operational bounds (parser-pinning + canonical-write-via-Pandoc-only + single named reader).
- The polyglot wording precision: the W3C Polyglot Markup NOTE was discontinued in 2014, but the polyglot HTML5/XHTML5 concept remains usable as a self-imposed writing convention.
- The dual-rejection scope precision: dual *persistent* storage is rejected; dual representation (via on-demand `pandoc -f html -t json`) is preserved.
- The TEI rejection wording: the rejection is architectural (it breaks Decision 5's Pandoc-as-architectural-lever commitment), not merely operational.
- The JSON-AST bias-balance: JSON-AST has a genuine machine-readability advantage; HTML5's compensating advantages outweigh it at the canonical layer, but the trade-off is named explicitly.

---

## Open Questions

### Monitoring

The end-to-end calibration prototype on a Risale-i Nur volume (the COULD item) will produce the first empirical answer to several questions: whether HTML5's verbosity is acceptable at intake-output sizes for the calibration corpus; whether the three MUST items' specs are sufficient to produce a valid canonical or need additional fields; whether the EPUB output in real readers matches the canonical's structural commitments. Observable after the calibration prototype completes.

### Blocked

The seven detector designs (one per schema policy, per Decision 4 of the original intake-concepts finding) cannot be formally specified until the per-policy class-attribute conventions (MUST 2) and the per-element provenance encoding pattern (MUST 3) resolve. The detector specs depend on knowing what to tag elements with and how to attach provenance metadata.

The in-memory representation choice (DOM via `lxml.html` versus DOM via `html5lib` versus AST via `panflute` versus a thin pydantic layer wrapping either) is blocked on the detector-design inquiries beginning, since the choice affects detector ergonomics directly.

### Research Frontiers

Cross-corpus generalization of HTML5-as-canonical (does the commitment hold for Talmud apparatus, Vedic texts, Christian patristic editions, modern academic books?) requires either evidence from intaking exemplars from at least one other corpus, or theoretical analysis of which calibration-corpus features were Risale-i-Nur-specific versus universal. Currently no path to answer beyond exemplar evidence.

Whether archival / historical preservation needs its own temporal layer (decade-scale stability versus publishing-cycle stability) requires either real-world archival use-case emergence (someone asking for translation persistence at decade scale) or formal study of which long-term-stability properties the current architecture already provides.

### Refinement Triggers

The HTML5-as-canonical commitment re-opens if any of the following observable conditions fire:
- Pandoc deprecates or fundamentally changes its HTML5 reader/writer behavior such that round-trip stability breaks (observable from Pandoc release notes).
- W3C declares HTML5 Living Standard frozen or fundamentally restructured (extremely unlikely given Living Standard's design constraints, but observable from W3C announcements).
- The calibration prototype surfaces a structural requirement HTML5 cannot encode without contortion (observable from prototype evaluation).
- A cross-corpus validation surfaces a corpus whose policy targets HTML5 cannot accommodate via class + `data-*` conventions (observable from second-corpus prototype evaluation).

The three-layer architecture re-opens if any of the following observable conditions fire:
- The hand-edit recovery workflow proves byte-stability-unworkable in practice (observable from user feedback on actual editing sessions).
- A publishing target emerges that requires structural changes incompatible with EPUB 3 (observable from publishing requirements naming a target).
- A monolithic format emerges that genuinely satisfies all three layer optima at once (observable from format-landscape changes, e.g., a new W3C standard).

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
Here's what I had framed it as, and what it actually is.
 
  What I had framed: "Pick the canonical format intake serializes to — markdown vs RTF vs EPUB vs MOBI vs custom-AST." The three-format
  layered architecture was an answer at THAT layer. Pandoc's AST as JSON for canonical, markdown for hand-edit, EPUB for publishing. The
  user's pushback got resolved into "AST-as-storage strategy."

  What it actually is: The PDFs are the calibration corpus, and they are structurally degraded sources for the things intake needs to
  capture. Specifically: 

  - Asa-yı Musa: Arabic IS in the text layer but with broken bidi/shaping/order. pdftotext and Pandoc's PDF reader both produce garbled
  Arabic from this — letters and diacritics scattered across lines in wrong order. To get usable Arabic, intake must detect the brokenness
  and re-derive the spans via OCR (tesseract --lang ara).
  - Muhakemat: Arabic is not in the text layer at all — it's pasted as images in the Word source. pdftotext and Pandoc's PDF reader cannot
  see it. Every Bismillah opening, every embedded Hadith, every closing verse — invisible to default extraction. The Turkish text layer is
  pristine. 
  - Both: italic/bold styling is lost by default extraction. Some PDF tools can recover it (mutool draw -F text, pdf2htmlEX) but it's an
  extra pass, not automatic.
  - Both: page paratext (running headers, page numbers) gets inline-extracted as if it were body content. Has to be stripped.

  So the more precise issue is this:

  The hard part of intake is not what format we save the result to. The hard part is reconstructing a faithful representation from sources 
  where the things we care about have been lost or broken by the format conversion pipeline that produced the PDF in the first place. Arabic
  gets reduced to glyphs or images; italics drop out of the text layer; structural markers (letter-spaced "T e n b i h :", multi-title
  hierarchies, hashiye positioning) don't survive in any standard extraction. By the time we have a clean parse to serialize, the work is
  mostly done; serializing it to JSON-AST or markdown or anything else is the easy part.

yes . 

and maybe we should repair the sources before doing anything, But still question remains even if we repair them what document type will be seelcted to hold that information?  yes we can use OCR like things for repair even, but end result should be what? epub? md file ? html maybe? 

this is the real question
```

</details>
