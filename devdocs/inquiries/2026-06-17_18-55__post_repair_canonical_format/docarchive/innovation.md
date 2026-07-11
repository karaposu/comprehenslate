# Innovation — post-repair canonical format

## User Input

Substrate: `_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md`. Production-task mode: Decomposition's 10 pieces (P1-P10) are the seed; Innovation generates per-piece substantive content. SV6 verdict: HTML5 as canonical (replaces JSON-AST); three-format architecture preserved; `refines:` prior canonical-format finding.

---

## Phase 1 — Seed / Methodology-Mode Consideration

**Inherited methodology mode:** **Standard default** (4G+3F balanced; elaborate the committed direction; produce ship-ready content).

**Alternative mode considered:** **Contrarian-rethink (Framer-weighted)** — re-challenge sensemaking's HTML5-as-canonical verdict; surface alternatives at piece level.

**What follows under the alternative:** Innovation would treat the HTML5-as-canonical commitment as questionable and surface alternatives like "JSON-AST is still right" or "monolithic single-format" or "custom JSON-AST." Candidate space widens, but sensemaking already ran Strongest-Counter tests via the capability matrix on 7 ambiguities with HIGH-confidence resolutions; Contrarian-rethink at Innovation would duplicate that adjudication.

**Decision:** **Standard default.** Piece-level Inversion at meta-decision pieces (P2, P8) provides the contrarian surface at appropriate granularity.

`Methodology-mode-alternative-marked-inapplicable: Sensemaking's Phase 3 ran Strongest-Counter tests on each of 7 ambiguities (including HTML5-vs-JSON-AST, monolithic-vs-layered, JSON-AST+HTML5 dual, user-non-mention-of-JSON-AST signal, provenance dimension impact) with HIGH or HIGH-MED-confidence resolutions; Contrarian-rethink at Innovation would duplicate adjudication. Piece-level Inversion at P2 and P8 provides contrarian surface at appropriate granularity.`

---

## Phase 2 — Generate (per piece)

### P2 (META-DECISION; FIRST per dependency order) — Architectural Commitment + Decision-Mode

**Principal candidate (content):**

> **The architectural commitment: three-layer architecture PRESERVED with canonical-layer format SWAPPED.**
>
> The prior canonical-format inquiry (`devdocs/inquiries/2026-06-17_17-49__canonical_intake_format_deep_dive/finding.md`) committed three formats for three temporal layers: **Pandoc-AST-as-JSON** at the canonical (intake/translate-internal) layer; **Pandoc's markdown** at the hand-edit layer; **EPUB 3** at the publishing layer. This finding **PRESERVES the three-layer architecture** and **SWAPS the canonical-layer format from Pandoc-AST-as-JSON to HTML5**. The other two layers — Pandoc-markdown hand-edit and EPUB 3 publishing — are preserved unchanged.
>
> **The decision-mode is REFINE.** This is not "re-affirm-prior-unchanged" (the canonical-layer format changes substantively); it is not "overturn" (the three-layer architecture stands; the other two cells survive). It is **REFINE** — one cell of the architecture changes; the surrounding commitments hold.
>
> **The relationship label is `refines:`.** This finding's frontmatter declares `refines: devdocs/inquiries/2026-06-17_17-49__canonical_intake_format_deep_dive/finding.md`. The prior finding's three-format architecture is the load-bearing inheritance; one cell is replaced with stronger evidence. The other inherited commitments — from the original intake-concepts inquiry (`devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`) — are PRESERVED unchanged (see Inherited Commitments Re-test).
>
> **The NEW evidence driving the swap.** Two facts emerged between the prior canonical-format finding and this one. **First**, empirical inspection of the calibration corpus's PDFs (Asa-yı Musa with broken-bidi text-layer Arabic; Muhakemat with image-only Arabic) revealed that intake's reconstruction work (OCR for Arabic; style recovery for italic/bold; structure detection; paratext stripping) produces RICH content with PER-ELEMENT provenance and confidence metadata — which the prior canonical-format inquiry's "lossless round-trip" frame didn't surface as load-bearing. **Second**, the candidate set surfaced an emergent alternative — HTML5-as-universal — that wasn't on the prior inquiry's solution-space radar. Together, these two facts shift the canonical-layer optimum.
>
> **Why HTML5 dominates the canonical layer.** The capability matrix (see P3) shows HTML5 is **Pareto-dominant** for the canonical role: it ties JSON-AST on every data-format property (lossless round-trip via Pandoc; explicit-tree storage; queryable) AND wins on every other relevant axis — it is a document (human-readable as markup) where JSON-AST is data; it has native `lang=` and `dir=` attributes via W3C HTML5 Living Standard rather than Pandoc-specific extensions; it has `data-*` attributes for per-element provenance carriage; it is the substrate of EPUB 3 (EPUB 3 content documents ARE xhtml5); it is web-standard and not Pandoc-locked. The provenance + confidence dimension is the markdown-killer: markdown alone has no per-element metadata mechanism, and the reconstruction reframe makes per-element provenance required.
>
> **What the prior architecture got right.** Three temporal layers (canonical / hand-edit / publishing) are USE-CASE distinctions with different optima. That insight stands. What changes is the recognition that the canonical layer's optimum aligns with HTML5 — a format the prior inquiry didn't promote because the emergent "HTML5-as-universal" candidate hadn't surfaced.

**Mechanism log:**
- *Lens Shifting:* under "what lens does the user's pushback signal?" → they named documents (EPUB / md / HTML); they didn't name data (JSON-AST). The lens shift surfaces the user-pattern.
- *Combination:* prior three-layer architecture × HTML5 candidate + provenance dimension → the architectural refinement.
- *Constraint Manipulation (ADD):* added "must carry per-element provenance" → markdown drops out at canonical.
- *Constraint Manipulation (REMOVE):* removed "canonical must be data-structure" → HTML5 (a document) becomes viable.
- *Absence Recognition (patch):* the prior inquiry didn't include HTML5 as a candidate at the canonical layer.
- *Absence Recognition (redesign):* if intake architecture were designed today, the format that is simultaneously document + data + web-standard + EPUB-substrate would be the obvious canonical.

**Piece-Level Inversion (required — P2 is meta-decision via framing-semantic + relationship-label properties):**

> *Inversion-candidate:* what if the prior canonical-format inquiry's Pandoc-AST-as-JSON commitment was correct as-is and the user's pushback was ungrounded — the right move is to preserve the prior unchanged?
>
> *What follows under the inversion:* keep JSON-AST as canonical; ignore the user's named EPUB/md/HTML candidates as alternative-suggestions rather than as pattern-signals; defer the provenance + confidence dimension as out-of-scope; the architecture is preserved exactly.
>
> *Why rejected:* the capability matrix in P3 shows HTML5 is Pareto-dominant at the canonical layer when the provenance + confidence dimension is included; sensemaking Ambiguity 1 tested this with the strongest counter ("JSON-AST is still right") and found it weaker than the matrix evidence. The user's pattern signal (consistently naming documents, never naming data structures) is structurally distinct from "one user's incidental omission" — it has appeared across multiple turns. The reconstruction-is-heavy reframe is genuinely new evidence; treating it as out-of-scope would dismiss what intake actually has to do.
>
> *Intervention-shape Inversion check:* P2 commits a relationship-label-and-architectural-refinement. Alternative intervention shapes: `corrects:` (the prior was wrong — too strong; the prior was DEFENSIBLE within its framing, just not optimal when the matrix is broadened); `supersedes:` (the prior is dead — too strong; two of three layers survive and the architecture itself survives); REVERT-REGRESSION (revert to pre-prior — n/a; no such state). `refines:` is the structurally accurate intervention shape: scope-narrowing on one cell while preserving the architecture and adjacent cells.
>
> Verdict on Inversion: **rejected** — the prior's choice was right for its framing but the framing was incomplete; the swap is structurally grounded.

**5-test:** Novelty (HTML5-as-canonical is novel for this project; the prior didn't have it on candidates); Scrutiny (survives strongest counter via capability matrix); Fertility (spawns the HTML5 schema profile + per-policy class conventions + provenance encoding inquiries); Actionability (engineer can implement HTML5 generation from intake today); Mechanism independence (Lens Shifting + Combination + Constraint Manipulation + Absence Recognition all converge on HTML5-as-canonical via different paths). PASS.

---

### P3 — Capability Matrix (EVIDENCE)

**Principal candidate (content):**

> The verdict's evidence is a capability matrix — five core candidate formats × the load-bearing requirements for the canonical layer. Cells use the four-level support classification: **native** (✓✓) — the format has a first-class W3C-or-Pandoc-or-IDPF-defined primitive; **via-extension** (✓+ext) — supported via a specific named Pandoc or W3C extension; **via-workaround** (✓wa) — encodable but requires user-defined conventions over generic class/attribute mechanisms; **not-supported** (✗) — the format cannot hold this without sidecars or other out-of-band mechanisms.
>
> | Requirement | JSON-AST | Pandoc-md | **HTML5** | EPUB 3 | Custom .compldoc |
> |---|---|---|---|---|---|
> | Arabic span with `lang=ar` | ✓✓ | ✓+ext (`bracketed_spans`) | **✓✓** (W3C any element) | ✓✓ | ✓+ext |
> | Arabic span with `dir=rtl` | ✓✓ | ✓+ext (`bracketed_spans`) | **✓✓** (W3C any element) | ✓✓ | ✓+ext |
> | Italic-as-semantic emphasis | ✓✓ (Emph) | ✓+ext (AST Emph) | **✓✓** (`<em>` semantic) | ✓✓ | ✓+ext |
> | Bold-as-strong emphasis | ✓✓ (Strong) | ✓+ext (AST Strong) | **✓✓** (`<strong>` semantic) | ✓✓ | ✓+ext |
> | Marginalia with ref-to-body-position | ✓wa | ✓+ext (Pandoc footnote) | **✓✓** (`<aside>` + id/href) | ✓wa (epub:type) | ✓+ext |
> | Embedded poetry + attribution + verse-shape | ✓✓ (LineBlock + attrs) | ✓+ext (LineBlock syntax) | **✓✓** (`<figure>` + `<blockquote>`) | ✓✓ | ✓+ext |
> | Formulaic openings + position constraint | ✓wa (Para + class) | ✓+ext (fenced div) | **✓✓** (`<p class>` + `<section>`) | ✓✓ | ✓+ext |
> | Chapter / section / paragraph hierarchy | ✓✓ | ✓+ext | **✓✓** (`<section>`/`<article>`/`<p>`) | ✓✓ | ✓+ext |
> | Cross-references (apparatus-ref → body) | ✓✓ | ✓+ext (Pandoc cite/footnote) | **✓✓** (`href="#id"` + matching `id`) | ✓✓ | ✓+ext |
> | Document-level provenance | ✓✓ | ✓+ext (YAML frontmatter) | **✓✓** (`<meta>` in `<head>`) | ✓wa (OPF) | ✓+ext |
> | **Per-element provenance + confidence (A19)** | ✓✓ | **✗** (no per-element metadata mechanism) | **✓✓** (`data-*` attributes; W3C §3.2.6) | **✗** (only doc-level OPF) | ✓wa (YAML sidecar) |
> | Round-trip with Pandoc | ✓✓ (lossless within version) | ✓wa (round-trip-stable subset) | **✓✓** (Pandoc ↔︎ HTML5) | ✓wa (lossy at metadata) | ✓+ext |
> | Human-readable as document | ✗ (data, not document) | ✓✓ (reading-order-natural) | **✓wa** (markup with tag-noise but readable) | ✗ raw / ✓wa unzipped | ✓✓ |
> | Schema-validatable | ✓wa (Pandoc AST types documented; not formal JSON Schema) | ✗ (no formal schema) | **✓✓** (HTML5 DTD / RNG schemas exist) | ✓✓ (EPUBCheck) | ✗ |
> | Web-standard / not Pandoc-locked | ✗ | ✗ | **✓✓** (W3C HTML Living Standard) | ✓✓ (W3C/IDPF) | ✗ |
> | EPUB 3 publishing path | via Pandoc render | via Pandoc render | **near-identity** (EPUB IS xhtml + manifest + zip) | already EPUB | via Pandoc render |
> | HTML web-output path | via Pandoc render | via Pandoc render | **identity** (already HTML) | unzip + serve | via Pandoc render |
> | PDF print-output path | via Pandoc + LaTeX/HTML | via Pandoc + LaTeX/HTML | **direct via weasyprint / wkhtmltopdf** | via reader-export | via Pandoc + LaTeX/HTML |
>
> **HTML5 is Pareto-dominant for the canonical layer.** It ties or beats every other candidate on every requirement except "human-readable as document" — where markdown wins for prose-heavy reading (markdown's edge there is real but not at the canonical layer; markdown serves the hand-edit layer instead). The cell that decides it: **per-element provenance (A19)**. JSON-AST and HTML5 are tied (both can hold per-element metadata); markdown alone CANNOT. The reconstruction-is-heavy reframe makes A19 load-bearing.
>
> The cells are grounded in: W3C HTML5 Living Standard (`html.spec.whatwg.org` — definitive for HTML5 elements and attributes; `data-*` is §3.2.6); Pandoc's documented format matrix (`pandoc.org/MANUAL.html`; the `↔︎ HTML5` and `↔︎ EPUB version 2 or 3` entries); EPUB 3 specification (`w3.org/TR/epub-33/` — definitive that EPUB content documents are XHTML5).

**Mechanism log:**
- *Combination:* the 18 requirements × the 5 candidates → the 90-cell matrix with per-cell evidence.
- *Domain Transfer (web-native):* HTML5 cells cite W3C spec — computing-native sources.
- *Constraint Manipulation (ADD):* added "must support per-element metadata" → A19 row becomes the discriminator.

**5-test:** PASS — matrix is the load-bearing evidence; per-cell evidence cited; Pareto-dominance demonstrated.

---

### P4 — F1: HTML5 as Canonical (LOAD-BEARING NEW COMMITMENT)

**Principal candidate (content):**

> **F1 — The canonical intake/translate format is HTML5** (W3C HTML Living Standard).
>
> When intake completes, it produces a single HTML5 file: the document representing the reconstructed source. This file IS the canonical form. Every translate-stage operation reads this HTML5 and operates on its DOM tree. The in-memory `IntakeDoc` (per the original intake-concepts finding's Decision 3) is the parsed HTML5 DOM — or equivalently, the Pandoc AST obtained via `pandoc -f html -t json`. Both shapes are isomorphic.
>
> **Profile and syntax.**
>
> - **HTML5 Living Standard** (per `html.spec.whatwg.org`) is the authoritative spec.
> - **Polyglot syntax** — the file is valid as both HTML5 and XHTML5 (per W3C polyglot guidelines). Lowercase tags; closed elements; quoted attribute values; explicit `<html lang="...">` root; XML-style void elements where applicable. This keeps the file parseable by both HTML and XML parsers.
> - **UTF-8 encoding** — required for the calibration corpus's mixed-script content.
>
> **Semantic elements used for structure.**
>
> Per W3C HTML5 sectioning content semantics:
>
> - `<html lang="tr" dir="ltr">` — document root with primary-language declaration.
> - `<head>` with `<meta>` for document-level metadata (title, author, source-PDF, intake-time, hash).
> - `<body>` containing the document body.
> - `<section>` for chapter and section containers.
> - `<article>` reserved for top-level standalone documents within a corpus.
> - `<header>`, `<footer>`, `<nav>` for paratextual structure when preserved.
> - `<aside>` for marginalia and side-content (see P6).
> - `<figure>` and `<figcaption>` for embedded poetry, illustrations, captions.
> - `<blockquote>` and `<q>` for quoted content.
> - `<p>` for paragraphs.
> - `<span>` for inline annotation spans.
> - `<em>` and `<strong>` for semantic emphasis (italic-as-emphasis and bold-as-strong-emphasis, per Decision 2 of the original intake-concepts finding).
>
> **Attributes used.**
>
> Per W3C HTML5 (any-element attributes unless otherwise noted):
>
> - `lang="..."` — language tag (W3C HTML5; BCP 47 language tags).
> - `dir="ltr"` / `dir="rtl"` / `dir="auto"` — text direction (W3C HTML5).
> - `class="..."` — space-separated semantic classes (W3C HTML5).
> - `id="..."` — unique identifier for cross-reference targets (W3C HTML5).
> - `data-*` — application-specific data attributes (W3C HTML Living Standard §3.2.6). Used for per-element provenance, confidence, intake-pass history, and per-policy semantic tagging.
>
> **Pandoc round-trip.**
>
> Pandoc reads and writes HTML5 (per Pandoc's documented format matrix, `↔︎ HTML5`). The canonical workflow:
>
> ```bash
> # Source format → HTML5 canonical
> pandoc -f markdown -t html5 input.md > canonical.html
>
> # HTML5 canonical → markdown (for hand-editing)
> pandoc -f html -t markdown canonical.html > for_editing.md
>
> # HTML5 canonical → EPUB 3 publishing (near-identity)
> pandoc -f html -t epub3 -o published.epub canonical.html
>
> # HTML5 canonical → JSON-AST (on-demand reachable; for tools that need AST shape)
> pandoc -f html -t json canonical.html > ast.json
> ```
>
> The Python `panflute` package (per `panflute.readthedocs.io` and PyPI as `panflute`) provides typed AST access from Python; `lxml.html` and `html5lib` provide direct HTML5 DOM access.
>
> **Schema validation strategy.**
>
> Two layers:
>
> 1. **HTML5 conformance** — the file must be valid HTML5 per W3C Living Standard. Validators: `html5validator` (Python), the W3C HTML Validator, or `vnu.jar`. A no-op round-trip (`pandoc -f html -t html` or `tidy -q -m`) catches structural soundness.
>
> 2. **Project-specific RNG profile (working assumption; downstream design)** — a project Relax-NG schema constraining HTML5 to comprehenslate's expected structure (e.g., "every `<section>` has a heading"; "every `<aside class='marginalia'>` has an `id`"; "every `<span class='honorific'>` has a `data-tradition` attribute"). The profile is documented in MUST 1 of Next Actions; this finding commits HTML5 as canonical, not the exact RNG profile.
>
> **Relationship to the in-memory `IntakeDoc`.**
>
> The prior intake-concepts finding committed `IntakeDoc` as a tree-of-containers + cross-referenced flat collections in memory. With HTML5 as on-disk canonical, the in-memory shape IS the parsed HTML5 DOM: each `<section>` is a Container; each `<p>` is a Paragraph; each `<aside class="marginalia">` is an apparatus entry in the flat marginalia collection; cross-references via `<a href="#id">` map to direct DOM lookups via `id=`. The IntakeDoc shape's semantic intent from Decision 3 is preserved; the concrete representation is now HTML5 DOM rather than a custom Python pydantic class wrapping Pandoc AST nodes. (A pydantic layer can still wrap the DOM if project-specific invariants need enforcement — this is the working-assumption split with the project-specific RNG profile; downstream design.)
>
> **Why HTML5 wins over JSON-AST for this role.**
>
> The capability matrix shows the tie on data-format properties (lossless round-trip; explicit-tree; queryable). HTML5's wins are at the surfaces JSON-AST cannot reach:
>
> - HTML5 IS a document — openable in any text editor; renders in any browser; the user looks at it and reads it.
> - HTML5 IS web-standard — survives Pandoc deprecation; cross-vendor; portable.
> - HTML5 IS the EPUB 3 substrate — the publishing-layer conversion is near-identity rather than Pandoc re-render.
> - HTML5 has native `lang=` and `dir=` attributes on any element per W3C — no extension needed (Pandoc-md's `bracketed_spans` extension is needed for the same capability).
>
> **Why HTML5 wins over Pandoc-markdown for this role.**
>
> Markdown is reading-order-natural for prose editing — that's why markdown stays as the hand-edit format (F2; preserved unchanged from the prior canonical-format finding). At the canonical layer, however, two requirements break markdown:
>
> 1. **Per-element provenance + confidence (A19)** — markdown has no per-element metadata mechanism. Encoding it requires either sidecar JSON files (loses single-file canonical), or YAML extensions (operates only at document level), or class-attribute overloading via Pandoc's `bracketed_spans` (loses class semantics for policy targets). HTML5's `data-*` attributes handle this natively on any element.
>
> 2. **The round-trip-stable subset issue** — the prior canonical-format inquiry flagged this as a real constraint on Pandoc-md as canonical: some markdown features survive `md → json → md`, some don't, and the boundary is not crisp. HTML5 has no such subset issue at canonical layer (round-trips via the AST cleanly per Pandoc's HTML5 reader/writer).
>
> **Legitimate concern preserved.** HTML5 is **more verbose** than markdown for the same content — `<p>The text</p>` vs `The text`; `<em>word</em>` vs `*word*`. At the canonical layer this is acceptable because (a) storage isn't a constraint; (b) the reconstructed content IS tag-dense regardless of format (Arabic spans + class-tagged policies + provenance attributes); (c) the canonical layer is for storage and processing, not direct prose editing — the hand-edit workflow uses markdown for prose. HTML5's verbosity-cost is bounded; markdown's verbosity-savings is irrelevant at the canonical layer where tag density is already high.

**Mechanism log:**
- *Combination:* W3C HTML5 elements × W3C HTML5 attributes × the 7 policy targets + provenance dimension → the spec.
- *Domain Transfer (computing-native):* `panflute`, `lxml.html`, `html5lib`, `html5validator` are computing-native sources.
- *Constraint Manipulation (ADD):* added "polyglot syntax" → the file is parseable by both HTML and XML tools.
- *Lens Shifting:* under "what is HTML5 for the user's purposes?" lens — a document they can open, read, validate against the source.

**5-test:** PASS — concrete Pandoc commands; cited W3C-spec features; explicit relationship to prior IntakeDoc; legitimate-concern (verbosity) surfaced and addressed.

---

### P5 — F2 + F3: Preserved Layers (markdown hand-edit + EPUB 3 publishing)

**Principal candidate (content):**

> **F2 — The hand-edit format is Pandoc's markdown with the canonical extension set.** This is **PRESERVED unchanged from the prior canonical-format finding** (Decision F2 of `devdocs/inquiries/2026-06-17_17-49__canonical_intake_format_deep_dive/finding.md`). The extension set, the byte-stability properties, the user-facing workflow, and the choice rationale all apply unchanged. The only adjustment is the round-trip target: the user edits markdown, and Pandoc converts to HTML5 (rather than to JSON-AST) — `pandoc -f markdown -t html5 edit.md > canonical.html`. The round-trip-stable subset (defined in COULD 2 of Next Actions) defines which markdown features are guaranteed to survive `md → html → md`.
>
> **F3 — The publishing format is EPUB 3.** This is **PRESERVED unchanged from the prior canonical-format finding** (Decision F3). The reader ecosystem (Apple Books, Google Play Books, Calibre, Adobe Digital Editions, Kobo, Foliate, Thorium), the rejection of MOBI (Amazon-deprecated in 2022), and the Kindle compatibility path (EPUB 3 → Send to Kindle → .azw3 / .kfx) all apply unchanged. **What does change** is the generation path: HTML5 → EPUB 3 is a **near-identity transform** since EPUB 3 content documents ARE xhtml5 (per EPUB 3 specification at `w3.org/TR/epub-33/`). The Pandoc command `pandoc -f html -t epub3 -o out.epub canonical.html` packages the HTML5 + adds an OPF manifest + metadata + cover-image. This is structurally cleaner than the prior path (JSON-AST → EPUB 3 via Pandoc render) because EPUB IS xhtml.
>
> For full specifications of F2 and F3, see the prior canonical-format finding. This finding's contribution at these layers is **acknowledgment of preservation + path-update to flow from HTML5 canonical**.

**Mechanism log:**
- *Combination:* prior F2 + F3 specs × HTML5 canonical → the workflow updates.
- *Lens Shifting:* under "what survives and what shifts" lens — F2 + F3 survive; only the source-of-conversion shifts.

**5-test:** PASS — brief; preservation explicit; path-update named.

---

### P6 — Per-policy HTML5 patterns (Calibration corpus)

**Principal candidate (content):**

> The seven policy targets from the original intake-concepts finding's Decision 4 each map onto HTML5 as follows. For Risale-i Nur specifically, the recurring elements (Bismillah openings, Mevlana couplets in prose, Said Nursi's hashiye, mixed Turkish-Arabic spans, voice transitions, archaic Ottoman vocabulary, Islamic honorifics) carry concrete element + class + `data-*` patterns.
>
> **`SourceApparatusPolicy` — hashiye (Nursi's marginalia).** Marginalia stored at body-end as `<aside>` elements; body references via inline `<a>` anchors:
>
> ```html
> <p>Body text with <a href="#h1" class="marginalia-ref">[h1]</a> reference.</p>
> ...
> <aside class="marginalia" id="h1"
>        data-source="ocr-tesseract"
>        data-confidence="0.92"
>        data-intake-pass="2">
>   Marginalia body text here.
> </aside>
> ```
>
> **`EmbeddedPoetryPolicy` — Mevlana couplets in prose.** Verse-block in `<figure>` with attribution in `<figcaption>`:
>
> ```html
> <figure class="couplet" data-attribution="Mevlana">
>   <blockquote>
>     <p>Line one of the couplet.</p>
>     <p>Line two of the couplet.</p>
>   </blockquote>
>   <figcaption>— Mevlana</figcaption>
> </figure>
> ```
>
> **`FormulaicOpeningPolicy` — Bismillah (and Hamd preambles).** Paragraph with class + tradition attribute, position-constrained to section-start:
>
> ```html
> <section>
>   <p class="formulaic-opening"
>      data-tradition="islamic"
>      data-source="ocr-tesseract"
>      data-confidence="0.95">
>     <span lang="ar" dir="rtl">بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيم</span>
>   </p>
>   <p>Section body begins here.</p>
> </section>
> ```
>
> **`NonMainLangPartsPolicy` — Arabic spans within Turkish narrative** (Qur'anic quotations, Hadith, technical terms):
>
> ```html
> <p>
>   Turkish prose continues
>   <span lang="ar" dir="rtl"
>         data-source="ocr-tesseract"
>         data-confidence="0.87">ٱلْحَمْدُ لِلَّٰهِ</span>
>   and continues again.
> </p>
> ```
>
> **`VoiceMarkingPolicy` — voice transitions** (Nursi's authorial voice vs cited authorities like Qur'an or Hadith):
>
> ```html
> <p>
>   Author voice prose.
>   <span class="voice-cited" cite="quran-17-44">
>     Cited content.
>   </span>
>   Author resumes.
> </p>
> ```
>
> Or for block-level citations:
>
> ```html
> <blockquote class="voice-cited" cite="hadith-bukhari-1">
>   <p>Cited block content.</p>
> </blockquote>
> ```
>
> **`ArchaicRegisterPolicy` — Ottoman Turkish archaisms** (lexical or syntactic):
>
> ```html
> <p>
>   Modern prose with
>   <span class="archaic-register" data-archaism-type="lexical">
>     Kemalât-ı insaniye
>   </span>
>   archaism.
> </p>
> ```
>
> **`HonorificsPolicy` — Islamic honorific markers** (SAW / AS / RA / PBUH family following names):
>
> ```html
> <p>
>   <span class="person-name">İmam-ı Ali</span>
>   <span class="honorific" data-tradition="islamic" data-form="ra">
>     Radıyallahü Anh
>   </span>
>   said:
> </p>
> ```
>
> **NFC diacritic normalization.** Applied at intake (per the original intake-concepts finding's normalize-stage commitment). HTML5 storage is UTF-8 native; NFC normalization is stable across the HTML5 ↔ markdown ↔ EPUB chain.
>
> **Per-element provenance + confidence — the uniform `data-*` pattern.** Every reconstructed element MAY carry:
>
> - `data-source` — one of `"text-layer"` (extracted from PDF text layer), `"ocr-tesseract"` (recovered via OCR), `"hand-edit"` (human-corrected), `"derived"` (computed from siblings).
> - `data-confidence` — a numeric 0.0–1.0 (Tesseract emits this directly; detector-rule confidences calibrated downstream).
> - `data-intake-pass` — the repair pass number that produced this element (1 = first pass; 2 = OCR fallback; etc.).
> - `data-original-source` — the source PDF path or hash; usually set at document root via `<meta name="..." content="...">` rather than per-element.
>
> These attributes are W3C-compliant (HTML Living Standard §3.2.6 — `data-*` attributes for application-specific data). Project-specific vocabulary (the exact values for `data-source`, the calibration of `data-confidence`, the meaning of `data-intake-pass` codes) is committed in MUST 3 of Next Actions.
>
> **Per-policy class-attribute convention.** Each policy class label uses the policy's role (e.g., `class="marginalia"`, `class="couplet"`, `class="formulaic-opening"`, `class="voice-cited"`, `class="archaic-register"`, `class="honorific"`) as the convention. An alternative convention — `data-policy="source-apparatus"` mapping to the schema's policy class name — is under MUST 2 design. This finding commits the role-based class convention as the working assumption; MUST 2 may refine.

**Mechanism log:**
- *Combination:* 7 schema policy targets × HTML5 elements + attributes × calibration corpus features → per-policy patterns.
- *Domain Transfer (W3C HTML5):* semantic elements (`<aside>`, `<figure>`, `<blockquote>`, `<section>`, `<span>`) are HTML5-native sources for the patterns.

**5-test:** PASS — each pattern is concrete; cites W3C semantic element + W3C-spec attribute mechanism; provenance encoding made explicit.

---

### P7 — Rejected Candidates Rationale

**Principal candidate (content):**

> Six candidates considered for the canonical-layer role are rejected here, each on structural grounds drawn from the capability matrix and the user's framing signal.
>
> **JSON-AST as canonical — rejected.** Pandoc-AST-as-JSON is technically capable (capability matrix shows it ties HTML5 on every data-format property). The rejection is structural in two ways. **First**, JSON-AST is data, not a document — the user's consistent framing pattern across multiple turns has been to name documents (EPUB / markdown / RTF / HTML / MOBI), never to name data structures. Honoring this pattern is structurally appropriate when the matrix shows no quality loss in doing so. **Second**, JSON-AST is Pandoc-specific — its schema and serialization are defined by Pandoc; future Pandoc deprecation or migration would force a re-derivation. HTML5 is W3C-standard and not locked to Pandoc. JSON-AST is **not lost** — `pandoc -f html -t json canonical.html` produces it on-demand for any tool that needs the AST shape.
>
> **Monolithic single-format — rejected.** Collapsing the three temporal layers (canonical / hand-edit / publishing) to one format compromises at least one layer's optimum. Markdown alone fails at canonical (per-element provenance ✗). EPUB alone fails at hand-edit (zip + manifest is heavyweight). HTML5 alone is closest to a universal — but markdown remains preferable for prose-heavy hand-editing (reading-order-natural; minimal tag noise). The three-layer architecture survives because the use-case-per-layer distinction survives.
>
> **Custom format (custom JSON-AST or `.compldoc`) — rejected.** HTML5 with project-specific class-attribute conventions covers what custom-format motivations would seek. The class + `data-*` mechanism handles project invariants; a project RNG schema handles structural validation. Recreating these in a project-specific format reinvents what HTML5 already provides.
>
> **Dual JSON-AST + HTML5 — rejected.** Maintaining two persistent canonicals creates synchronization debt — one must be authoritative; the other is derived. With HTML5 authoritative, JSON-AST is reachable on-demand (`pandoc -f html -t json`) without needing persistence. The dual structure adds storage cost and risk-of-divergence without architectural benefit.
>
> **TEI as canonical — rejected (TEI remains as future archival output frontier).** TEI is the scholarly-text-encoding standard with native support for marginalia, apparatus criticus, voice marking, and multi-language tagging. The rejection is operational: per Pandoc's documented format matrix, Pandoc **cannot read TEI as input** (only writes TEI Simple as `→ TEI Simple`). Choosing TEI as canonical would force a custom TEI reader, breaking the architectural lever (Pandoc as universal converter) from the original intake-concepts finding's Decision 5. TEI is recorded in the frontier as a possible future archival-output format generated from HTML5 canonical via `pandoc -f html -t tei`, when scholarly archival need emerges.
>
> **RTF — rejected** (unchanged from prior canonical-format finding). Editor-fragility: Microsoft Word, Apple Pages, Apple TextEdit, and LibreOffice each implement different subsets of the RTF spec and re-serialize on save through their rich-text engines. The hand-edit recovery workflow depends on byte-stability under no-op save — a property RTF cannot guarantee in any editor that interprets it as rich text. RTF survives as an accepted user-provided input format that intake reads via Pandoc and converts to HTML5 canonical.
>
> **MOBI — rejected** (unchanged from prior canonical-format finding). Amazon deprecated the .mobi format in 2022; Kindle Direct Publishing stopped accepting .mobi uploads, and Kindle devices use .azw3 / .kfx. Pandoc has no native MOBI writer. The Kindle distribution path is EPUB 3 → Send to Kindle → .azw3 / .kfx (Amazon's converter), already part of F3 publishing.

**Mechanism log:**
- *Combination:* per-candidate × per-structural-reason from the capability matrix and prior commitments.
- *Constraint Manipulation (ADD):* added "must satisfy A19 provenance" → JSON-AST and HTML5 survive; markdown and EPUB don't (at canonical layer).
- *Absence Recognition:* the user's pattern-signal (consistently naming documents, never data) is what's surfaced as the JSON-AST-rejection's secondary reason.

**5-test:** PASS — each rejection structurally grounded; JSON-AST's continued availability via on-demand Pandoc conversion noted; TEI's frontier status preserved.

---

### P8 (META-DECISION) — Inherited Commitments Re-test

**Principal candidate (content):**

> This finding inherits commitments from **two priors**. Each is re-tested separately.
>
> **Prior 1 — the canonical-format inquiry** (`devdocs/inquiries/2026-06-17_17-49__canonical_intake_format_deep_dive/finding.md`).
>
> This finding's frontmatter declares `refines:` of this prior. The prior committed three formats at three layers — JSON-AST canonical + Pandoc-markdown hand-edit + EPUB 3 publishing — with decision-mode SUBSTITUTE refining its own prior (the original intake-concepts finding). The verdict on the prior's commitments after this inquiry:
>
> | Prior commitment | Status |
> |---|---|
> | Three-format layered architecture (intake/translate-canonical + hand-edit + publishing as USE-CASE distinctions) | **RE-TESTED — commitment confirmed.** The three temporal layers stand; their use-case-per-layer optima are real. |
> | Canonical = Pandoc-AST-as-JSON | **RE-TESTED — commitment found INVALID** when the canonical's full requirement set (including the NEW provenance + confidence dimension surfaced by the reconstruction-is-heavy reframe) is evaluated and the emergent HTML5-as-universal candidate is included. The prior's choice was DEFENSIBLE within its framing but the framing was incomplete. **This finding's canonical = HTML5.** |
> | Hand-edit format = Pandoc's markdown with the canonical extension set | **RE-TESTED — commitment confirmed.** Markdown remains the right hand-edit format; only the round-trip target shifts (md ↔ HTML5 via Pandoc rather than md ↔ JSON-AST). |
> | Publishing format = EPUB 3 | **RE-TESTED — commitment confirmed and STRENGTHENED.** HTML5 → EPUB is near-identity (EPUB IS xhtml + manifest) rather than the prior's Pandoc-render path. |
> | Pandoc as architectural lever | **RE-TESTED — commitment confirmed.** All three formats remain Pandoc-native ↔︎. |
> | Reasons for prior's other rejected candidates (RTF / TEI / MOBI / EPUB-as-canonical / custom-format) | **RE-TESTED — commitment confirmed.** All five rejections survive on the same structural grounds; TEI's frontier status is preserved. |
>
> The net change: **one cell of the architecture swaps** (canonical-layer format JSON-AST → HTML5). The architecture itself stands. The relationship label `refines:` is structurally appropriate.
>
> **Prior 2 — the original intake-concepts inquiry** (`devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`).
>
> This finding does **not** directly refine the original intake-concepts inquiry (the canonical-format inquiry above is the intermediate refiner). But the original's Decisions 2-5 are inherited through the chain. Their status:
>
> | Original commitment | Status |
> |---|---|
> | Decision 2 — quality target = structure-preservation | **PRESERVED.** HTML5's explicit-tree storage preserves structure even more directly than surface markdown; the target is unchanged. |
> | Decision 3 — `IntakeDoc` shape = tree-of-containers + cross-referenced flat collections | **PRESERVED in semantic intent**; the concrete representation shifts from a custom Pandoc-AST-wrapping pydantic class to a parsed HTML5 DOM. The tree-of-containers maps to `<section>`/`<article>`/`<p>` nesting; the cross-referenced flat collections map to `<aside>` / `<figure>` / `<blockquote>` collected and referenced via `<a href="#id">`. |
> | Decision 4 — 7-policy intake-perception + translate-rendering split | **PRESERVED.** The seven policy-perception detectors operate on the in-memory DOM (or AST; equivalent); their specs refine to reference HTML5 elements + classes + `data-*` attributes (per P6). Semantic refinement, not redesign. |
> | Decision 5 — Pandoc + OCR architectural lever | **PRESERVED and STRENGTHENED.** All three formats in the architecture are Pandoc-native ↔︎; HTML5 is a clean Pandoc target. The OCR sub-pipeline (concept A3 in the original) is unchanged — OCR feeds Pandoc; Pandoc produces HTML5 canonical. |
> | The 38 intake-handling concepts enumerated in the original | **PRESERVED in semantic intent**; references shift from JSON-AST node types to HTML5 element types where applicable. |
>
> **No commitment from the original intake-concepts inquiry is invalidated.** The reconstruction-is-heavy reframe surfaces NEW concepts (per-element provenance + confidence) that the original didn't have; these are ADDITIVE, not contradictory.

**Mechanism log:**
- *Combination:* prior canonical-format inquiry's 6 commitments × this inquiry's evidence → per-commitment re-test verdict.
- *Combination:* original intake-concepts inquiry's 4 decisions × HTML5-canonical commitment → per-decision preservation status.
- *Absence Recognition:* the original didn't have the provenance + confidence dimension; named as ADDITIVE not invalidating.

**Piece-Level Inversion (required — P8 is meta-decision via relationship-label property):**

> *Inversion-candidate:* what if the prior canonical-format finding's commitments should be OVERTURNED rather than REFINED — what if the architecture itself is wrong, not just one cell of it?
>
> *What follows under the inversion:* (a) the three-layer architecture is rejected; (b) all three layer-commitments are re-opened; (c) the relationship label becomes `corrects:` or `supersedes:`; (d) the entire prior finding's content is dropped from inheritance, including its preserved hand-edit and publishing layers.
>
> *Why rejected:* the three-layer architecture survives every structural test in sensemaking — perspectives confirm; the prior inquiry's adjudication of monolithic-vs-layered (Ambiguity 1 in the prior) found the monolithic frame structurally wrong; this inquiry's sensemaking Ambiguity 1 re-tested and reached the same conclusion. The canonical-layer cell IS wrong (in the framing-incomplete sense); the architecture isn't. `refines:` captures this distinction precisely; OVERTURN would discard the use-case-per-layer insight that survives.
>
> *Intervention-shape Inversion check:* P8 commits `refines:` for prior 1 (canonical-format inquiry) and PRESERVED for prior 2 (original intake-concepts inquiry). Alternatives from the Intervention-Shape Vocabulary: `corrects:` (the prior was structurally wrong — applies to the canonical-LAYER cell but not to the architecture); `supersedes:` (the prior is dead — too strong; two of three layers and the architecture survive); REVERT-REGRESSION (n/a; no pre-prior to revert to). `refines:` is the right intervention shape for prior 1; PRESERVED for prior 2.
>
> Verdict on Inversion: **rejected** — the per-commitment re-test verdicts hold; the architecture and 4 of 5 prior-canonical-format-inquiry commitments survive; only one cell changes. The relationship label is structurally accurate.

**5-test:** PASS — each prior commitment re-tested with cited verdict; distinction between the two priors made explicit; inversion-candidate tested and rejected with structural reasoning.

---

### P9 — Transition Plan + Next Actions

**Principal candidate (content):**

> **What changes from the prior canonical-format finding.**
>
> The prior committed JSON-AST as on-disk canonical. The refined plan commits HTML5 as on-disk canonical. Specific changes:
>
> - The **on-disk canonical format** shifts: was JSON-AST file (`canonical.json`); now HTML5 file (`canonical.html`).
> - **Per-element provenance + confidence** is NEW: every reconstructed element MAY carry `data-source` + `data-confidence` + `data-intake-pass` attributes. This wasn't in the prior architecture; it's a load-bearing addition driven by the reconstruction reframe.
> - The **HTML5 → EPUB 3 packaging path** is NEW (and cleaner): near-identity transform (EPUB IS xhtml + manifest); replaces the prior's JSON-AST → EPUB Pandoc-render path.
> - The **intake stage's output** is HTML5 rather than JSON-AST: `pandoc -f markdown -t html5` (from text-layer Pandoc-md) or constructed directly via DOM-builder libraries (after OCR + reconstruction).
> - The **hand-edit workflow's round-trip target** is HTML5 rather than JSON-AST: user edits markdown → `pandoc -f markdown -t html5` → intake re-loads HTML5.
>
> **What stays the same.**
>
> - The **three-layer architecture** (canonical / hand-edit / publishing).
> - The **hand-edit format** = Pandoc's markdown with the canonical extension set.
> - The **publishing format** = EPUB 3.
> - The **in-memory `IntakeDoc` shape** (tree-of-containers + cross-referenced flat collections in semantic intent; concrete representation is HTML5 DOM).
> - The **7 policy-perception detectors** (specs refine to HTML5 element references rather than JSON-AST node references; semantic refinement only).
> - The **OCR sub-pipeline** (Tesseract + OCRmyPDF; unchanged).
> - The **quality target** = structure-preservation.
> - **Pandoc as architectural lever** (all three formats Pandoc-native ↔︎).
> - The **intake stages** (parse / normalize / segment / validate / hand-off) — unchanged in role; segment stage's output target is HTML5 rather than JSON-AST.
>
> **Engineering migration cost.** **NEAR-ZERO.** v0.2 has not been built yet. The prior canonical-format inquiry's verdict committed JSON-AST canonical but no engineering exists on it. Switching the committed format from JSON-AST to HTML5 BEFORE engineering starts costs nothing. This is the right time to swap.
>
> **Next-actionable inquiries.**
>
> **MUST 1.** Design the HTML5 schema / validation profile. Specify which HTML5 features are required for canonical conformance (`<section>`, `<aside>`, `<figure>`, `<span>` with semantic classes, etc.); specify which are forbidden (`<script>`, `<style>` may be either way — pure-content canonical might forbid both); decide whether to write a project-specific RNG schema or operate off-spec with `html5validator` + project-internal Python checks. Output: a `comprehenslate/intake/html5_profile.rng` (or equivalent) + documentation. Spawn as a `/traverse` inquiry.
>
> **MUST 2.** Design per-policy class-attribute conventions. Decide between (a) role-based class names (`class="marginalia"`, `class="couplet"`, etc.) — the working assumption per P6; (b) policy-named via `data-policy="source-apparatus"` mapped to schema policy classes; (c) hybrid. Document the conventions; commit them to the project spec. Output: a `comprehenslate/intake/policy_conventions.md` document. Spawn as a `/traverse` inquiry; smaller scope than MUST 1.
>
> **MUST 3.** Design per-element provenance encoding pattern. Specify exact `data-*` field names (`data-source` vs `data-prov-source`; etc.), value vocabularies (`data-source` enum: `"text-layer" | "ocr-tesseract" | "hand-edit" | "derived"`), and the confidence-numeric calibration (Tesseract's raw confidence is 0–100; our scale is 0.0–1.0; need a conversion convention). Output: a `comprehenslate/intake/provenance_spec.md` document. Spawn as a `/traverse` inquiry.
>
> **COULD 1.** Design the HTML5 → EPUB 3 packaging script. Since the transform is near-identity, this is minimal: specify Pandoc invocation flags; OPF manifest construction; cover-image handling; per-chapter file structure within the EPUB; CSS for Arabic typography (font fallback chain; RTL block handling; per-policy CSS classes). Output: a `comprehenslate/publish/epub.py` module + a CSS template.
>
> **COULD 2.** Define the HTML5-to-markdown round-trip stability subset for the hand-edit workflow. Document which Pandoc-markdown features survive `markdown → html → markdown` round-trips losslessly. This refines the hand-edit format's contract to its actual capability.
>
> **COULD 3.** Build the end-to-end prototype taking ONE Risale-i Nur volume (Asa-yı Musa or Muhakemat from the calibration corpus, depending on which exercises more policy targets) through intake (with OCR for broken-bidi or image-only Arabic) → HTML5 canonical → EPUB 3 publishing. Verify in 3+ EPUB readers (Apple Books, Calibre, Google Play Books). The prototype IS the calibration anchor for cross-corpus validation.

**Mechanism log:**
- *Combination:* prior architecture × HTML5 swap → per-element transition deltas.
- *Extrapolation:* current sensemaking commitments + likely engineering ordering → MUST/COULD priority.
- *Absence Recognition:* the MUST 3 provenance spec is NEW (the prior architecture didn't include it); the COULD 1 packaging script is NEW (near-identity transform makes it different from the prior's Pandoc-render path).

**5-test:** PASS — concrete deltas; explicit next-actionable inquiries; near-zero migration cost named; priority order grounded.

---

### P10 — Open Questions / Frontier

**Principal candidate (content):**

> **Open questions resolvable in the next-action inquiries.**
>
> - **HTML5 schema / validation profile.** Which HTML5 features are required for canonical conformance; which are forbidden; project RNG schema vs `html5validator` + project Python checks. Resolvable in MUST 1.
>
> - **Per-policy class-attribute conventions.** Role-based class (`class="marginalia"`) vs policy-named (`data-policy="source-apparatus"`) vs hybrid. Resolvable in MUST 2.
>
> - **Per-element provenance encoding pattern.** Exact `data-*` field names + value vocabularies + confidence-numeric calibration. Resolvable in MUST 3.
>
> - **HTML5-to-markdown round-trip stability subset.** Which Pandoc-markdown features survive `md → html → md` losslessly. Resolvable in COULD 2.
>
> - **HTML5-to-EPUB packaging specifics.** Pandoc flags; OPF manifest; CSS template (especially for Arabic typography). Resolvable in COULD 1.
>
> **Frontier — items deferred but not dismissed.**
>
> - **TEI Simple as future archival output.** Pandoc can write TEI Simple from HTML5 canonical (`pandoc -f html -t tei`). For scholarly archival use cases (preserving translations in a format the TEI community recognizes), TEI is the standard. **Revival trigger:** scholarly archival use case named by the project, OR cross-corpus validation surfaces a TEI requirement.
>
> - **JSON-AST on-demand reachability.** JSON-AST remains available via `pandoc -f html -t json canonical.html` for any tool that needs the AST shape. This is documented as a tooling fact, not a persistence commitment.
>
> - **Pandoc version pinning policy.** HTML5 conformance is stable across Pandoc versions (HTML5 is W3C-standard, not Pandoc-specific). But Pandoc's HTML5 reader/writer behavior MAY shift between versions for edge cases. **Operational concern:** the project's engineering team should pin a Pandoc version and document migration policy. Less load-bearing than the prior canonical-format inquiry's flag because HTML5 itself is W3C-stable; the Pandoc-specific risk is bounded.
>
> - **HTML5 Living Standard version stability.** The W3C HTML Living Standard evolves continuously; new elements + attributes may be added. The canonical commits to the Living Standard as of intake-time; project policy should document a "minimum HTML5 features required" snapshot.
>
> - **Cross-corpus format-architecture validation.** Does the HTML5-as-canonical commitment generalize to corpora other than Risale-i Nur (Talmud apparatus criticus; Vedic texts; Christian patristic editions; modern academic books)? **Revival trigger:** scaling beyond the calibration corpus.
>
> - **Archival / historical preservation as a fifth temporal layer** (carried from prior canonical-format inquiry's frontier). The three-layer architecture covers intake/translate, hand-edit, and publishing. A separate archival layer (TEI? JATS? a long-term-stable HTML5 profile?) may emerge with project maturity.
>
> - **In-memory representation: HTML5 DOM vs Pandoc AST.** The in-memory IntakeDoc can be either the parsed HTML5 DOM (via `lxml.html` / `html5lib`) or the Pandoc AST (via `panflute`). Both are isomorphic; the project's choice depends on which Python tooling fits the seven detector designs cleaner. Resolvable in the detector-design inquiries from the original intake-concepts finding.
>
> - **Per-translation-output format expansion** (carried from prior frontier). Beyond EPUB 3, other output formats (PDF for print; reveal.js for slides; LaTeX for academic submissions). Each is a Pandoc-writable target from HTML5 canonical.

**Mechanism log:**
- *Absence Recognition:* "what's still open after the HTML5 commit?" → open-questions list.
- *Extrapolation:* future evolution paths from current commitments.

**5-test:** PASS — open questions tied to specific resolution paths; frontier items named with revival triggers.

---

### P1 — Executive Summary (produced LAST per dependency order)

**Principal candidate (content):**

> The canonical intake format for translations is **HTML5** (W3C HTML Living Standard) — a polyglot HTML5 file with semantic markup (`<section>`, `<aside>`, `<figure>`, `<span>`, `<em>`, `<strong>`), native `lang=` and `dir=` attributes for Arabic spans, project-defined class conventions for the seven schema policy targets, and `data-*` attributes for per-element provenance and confidence. The hand-edit format (Pandoc's markdown) and the publishing format (EPUB 3) are **preserved unchanged** from the prior canonical-format finding. This **refines** the prior finding (`devdocs/inquiries/2026-06-17_17-49__canonical_intake_format_deep_dive/finding.md`) by swapping its canonical-layer format from Pandoc-AST-as-JSON to HTML5 — the three-layer architecture itself stands; one cell changes. The swap is driven by two new facts: **empirical inspection of the calibration-corpus PDFs** showed that intake's reconstruction work (OCR for broken-bidi or image-only Arabic; style recovery; structure detection; paratext stripping) produces RICH content with per-element provenance and confidence metadata; and **HTML5-as-universal** emerged as a candidate the prior inquiry didn't consider. HTML5 is Pareto-dominant for the canonical layer per the capability matrix: it ties JSON-AST on data-format properties (lossless round-trip via Pandoc; explicit-tree storage; queryable) AND wins on every other axis — it is a document (the user's framing pattern named EPUB / markdown / HTML, never JSON-AST); it has W3C-native lang/dir/data attributes; it is the EPUB 3 substrate (EPUB content documents ARE xhtml5, so HTML5 → EPUB is near-identity); it is web-standard and not Pandoc-locked. The provenance + confidence dimension — markdown's structural weakness — confirms the choice: markdown alone has no per-element metadata mechanism, and the reconstruction reframe makes per-element provenance load-bearing.

**Mechanism log:**
- *Combination:* HTML5 canonical + preserved markdown hand-edit + preserved EPUB 3 publishing + relationship label + new evidence + Pareto-dominance summary → one-paragraph digest.
- *Lens Shifting:* under "what does the reader need at-a-glance?" lens.

**5-test:** PASS — addresses the user's literal question; names HTML5 as canonical with brief rationale; names preserved layers; names the relationship to the prior; sized for one-paragraph reading.

---

## Inherited Frame Audit (between Phase 2 and Phase 3)

**Step (i) — Seed central assumption.** The seed framing assumes the SV6 verdict from sensemaking (HTML5 as canonical; three-layer architecture preserved; REFINES prior). Central assumption: **HTML5 is the right canonical given the new evidence.**

**Step (ii) — Per-piece commitments.** Meta-decision pieces: P2 (architecture + decision-mode + relationship-label) and P8 (Inherited Re-test). Both had Piece-Level Inversion applied.

**Step (iii) — Challenge scan.** Are there candidates challenging the central assumption?
- P2's Inversion-candidate tested "what if the prior was correct and the user's pushback was ungrounded" — rejected with capability-matrix + pattern-signal evidence.
- P8's Inversion-candidate tested "what if OVERTURN rather than REFINE" — rejected with three-layer-architecture-survives evidence.
- P7 (rejections) tested 6 alternative formats and structurally rejected each.

**Step (iv) — Firing condition.** Audit does **NOT fire**. Every meta-decision piece's commitment received explicit Inversion-candidate testing with cited evidence. Proceed to Phase 3 Test.

---

## Phase 3 — Test + Assembly

### Per-piece 5-test summary

All 10 pieces' principal candidates passed the 5-test cycle. Inversion candidates at P2 and P8 were generated, tested, and rejected with structural reasoning — compliance per the Piece-Level Inversion Rule.

### Assembly check

> **Does the architecture emerge from the 10 pieces' assembly?**
>
> **YES.** P1 gives the headline; P2 commits the architectural refinement + relationship label; P3 presents the matrix evidence; P4 specifies HTML5 canonical in detail; P5 acknowledges preserved layers; P6 maps the 7 policies onto HTML5 concretely; P7 rejects alternatives structurally; P8 re-tests inherited commitments and distinguishes the two priors; P9 names the (near-zero) transition + next actions; P10 names what's open. Read in dependency order, the assembled finding tells a coherent story: the prior architecture is preserved; one cell is swapped; the swap is structurally grounded.

### Axis coverage check

Orthogonal axes the candidate space varies along:
- **Temporal-layer axis** (canonical / hand-edit / publishing) — varied: P4 (canonical) + P5 (hand-edit + publishing preserved).
- **Decision-mode axis** (re-affirm / overturn / refine) — REFINE committed at P2 with rejection-rationale for alternatives.
- **Per-policy mapping axis** — 7 policies × HTML5 patterns at P6.
- **Provenance + confidence axis** (NEW) — addressed via `data-*` attribute encoding at P4 and P6.

All 4 orthogonal axes have ≥1 candidate variant. No single-axis collapse. PASS.

### Per-row mechanism-trace

The 7 policy patterns (P6) each have explicit mechanism work (Combination + Domain Transfer from W3C HTML5 semantic elements). The 6 rejections (P7) each have explicit structural-reason mechanism. The 2 meta-decision pieces (P2, P8) have Inversion-candidate work explicitly logged. No row-baseline silent inheritance.

---

## Telemetry

### Mechanism Coverage

- **Generators applied:** 4 / 4 (Combination · Absence Recognition · Domain Transfer · Extrapolation).
- **Framers applied:** 3 / 3 (Lens Shifting · Constraint Manipulation · Inversion).
- **Coverage:** FULL.
- **Convergence:** YES — Combination + Constraint Manipulation + Absence Recognition + Domain Transfer all converge on HTML5-as-canonical through different paths.
- **Survivors tested:** 10 / 10 principal candidates + 2 Inversion-candidates (P2, P8) = 12 / 12 tested.
- **Failure modes observed:** None.

### Production-task additional telemetry

| Piece | Mechanisms | Classification | Inversion compliance |
|---|---|---|---|
| P1 | Combination, Lens Shifting | content-production | n/a |
| P2 | Lens Shifting, Combination, Constraint Manipulation (ADD+REMOVE), Absence Recognition (patch+redesign), **Inversion** | **meta-decision** | **satisfied** (intervention-shape: `refines:` committed with alternatives `corrects:` / `supersedes:` / REVERT considered and rejected) |
| P3 | Combination, Domain Transfer (W3C + Pandoc), Constraint Manipulation (ADD) | content-production (evidence artifact) | n/a |
| P4 | Combination, Domain Transfer (W3C HTML5 + panflute/lxml/html5lib computing-native), Constraint Manipulation (ADD), Lens Shifting | content-production | n/a |
| P5 | Combination, Lens Shifting | content-production | n/a |
| P6 | Combination, Domain Transfer (W3C semantic elements) | content-production | n/a |
| P7 | Combination, Constraint Manipulation (ADD), Absence Recognition | content-production | n/a |
| P8 | Combination, Absence Recognition, **Inversion** | **meta-decision** | **satisfied** (intervention-shape: `refines:` for prior 1 + PRESERVED for prior 2; alternatives `corrects:` / `supersedes:` considered and rejected) |
| P9 | Combination, Extrapolation, Absence Recognition | content-production | n/a |
| P10 | Absence Recognition, Extrapolation | content-production | n/a |

### Verdict

**PROCEED** — full mechanism coverage; convergence on HTML5-as-canonical through 4+ mechanisms; all candidates tested; 2 meta-decision pieces (P2 + P8) Piece-Level Inversion compliance satisfied; Inherited Frame Audit did not fire; Assembly + Axis coverage + Per-row mechanism-trace all PASS. No failure modes observed.
