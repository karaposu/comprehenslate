# Surfacing — intake preprocessing operations

## User Input

Source: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/_branch.md`

Upstream articulation: same folder's `articulate_simple.md`. CONTINUES FROM the prior post-repair canonical format finding (NFC + paratext as established baseline) and the original intake-concepts finding (Decision 2 structure-preservation quality target).

Critical framing: minimal intake (no classification; no per-element provenance; no 7-policy detection; no per-span lang= tagging). HTML5 canonical settled. Generic translation project; Risale-i Nur as calibration corpus. User's question is GENERATIVE ("be creative") with structural-boundary detection (depth ~4) as one explicitly-named candidate.

---

## Mode + Entry Point

- **Mode:** `possibility` — the territory is the conceptual design space of preprocessing operations; items are candidate-generated, not enumerated from a pre-existing artifact set.
- **Entry-point:** `signal-first` — the inquiry's purpose is given (enumerate preprocessing ops beyond NFC + paratext; evaluate structural boundary detection; be creative).
- **Territory spec:** `explicit-bounded` via 14 sub-regions named in `_branch.md`'s Context section.
- **Boundary-discovery sub-phase:** skipped (territory edges are pre-given).
- **Prior-artifact:** none (fresh).
- **Prior-workspace:** none.

---

## Traversal Trace

Per-item relevance verdict legend (per §2.3 relevance-attribution; purpose-conditioned, content-driven):

- **core** — operation is clearly intake preprocessing, plausibly load-bearing for v0.2 minimal-extended pipeline OR named by the user OR a structural staple.
- **sub** — preprocessing but specialized; addresses a specific edge case or source-format.
- **side** — adjacent to preprocessing; lives in the gray zone with classification, OR is publishing-stage / translate-stage rather than intake-stage.
- **umbrella** — granularity uncertain; included per asymmetric-failure (lean to inclusion).

Confidence legend: H / M / L.
Recency annotation: all items `{source: none, value: null}` (possibility-mode candidates; no filesystem backing).

### Sub-region T — Text-level cleanup

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| T1 | NFC Unicode normalization | core | H | Baseline; established in prior finding |
| T2 | NFD / NFKC / NFKD comparison | side | M | Alternative normalization forms; NFKC over-normalizes (eats compatibility chars); rarely the right choice for intake |
| T3 | Whitespace normalization (collapse runs; trim line ends; normalize newlines to LF) | core | H | Standard one-pass; prevents mid-paragraph multiple-space artifacts and CR/LF/CRLF inconsistencies |
| T4 | Zero-width space removal (U+200B, U+200C, U+200D) | core | H | Invisible chars that survive copy-paste and break search/diff |
| T5 | Non-breaking space handling (U+00A0 vs regular space U+0020) | sub | M | Often introduced by PDF extraction; decide policy (preserve as semantic NBSP or replace with U+0020) |
| T6 | Quotation mark normalization (curly / straight / French / German / Turkish forms) | core | H | Risale-i Nur uses Turkish quotation convention; mixed PDF extraction often produces dual forms |
| T7 | Dash normalization (em / en / hyphen / minus / figure-dash → project canonical) | core | H | Em-dash vs en-dash carries semantic difference; PDF often substitutes hyphens; standardize |
| T8 | Ellipsis normalization (three dots U+002E×3 vs single U+2026) | sub | M | Visually identical; bytes differ; pick canonical |
| T9 | Soft hyphen removal (U+00AD) | core | H | Invisible hyphenation hint; breaks search; safely strippable in most cases |
| T10 | Combining-character canonical ordering | sub | M | Mostly handled by NFC; standalone op when NFC isn't run |
| T11 | Confusables detection (Cyrillic А vs Latin A; Greek Ο vs Latin O) | sub | M | Important for OCR-derived corpora; less for clean EPUB |
| T12 | Ligature decomposition (ﬁ → fi; ﬂ → fl; ﬃ → ffi) | core | H | PDF text-layer commonly contains ligatures; intake must decompose for search and consistency |
| T13 | Turkish diacritic disambiguation (i with dot vs ı dotless; İ vs I) | sub | H | Turkish-specific; could cross to corpus-specific if generic policy doesn't cover Turkish |
| T14 | Smart-quote vs typewriter-quote heuristic (apostrophe ' vs prime ' vs typographic ') | sub | M | Edge case; usually unified by quotation-mark normalization (T6) |
| T15 | Bullet character normalization (• ◦ ▪ → list markup) | sub | M | Could be either preprocessing (cleanup) or structural (list detection) |

### Sub-region P — Paratext / non-body removal

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| P1 | Running headers (book/chapter title repeated per page) | core | H | Baseline; established |
| P2 | Running footers | core | H | Baseline; established |
| P3 | Page numbers / folios | core | H | Baseline; established |
| P4 | Catchwords (next page's first word at bottom) | sub | M | Older typesetting convention; rare in modern texts |
| P5 | Editorial boilerplate ("[continued]" / "[end of chapter]") | core | H | Baseline; established |
| P6 | Publisher metadata at chapter starts | core | H | Baseline; established |
| P7 | Watermarks / "scanned by" stamps (PDF artifacts) | sub | H | Common in archive.org / google books PDFs |
| P8 | Decorative page-break ornaments (asterism * * * ; dingbats) | sub | H | Could be paratext (skip) or section-break signal (preserve as <hr>) — design choice |
| P9 | Blank pages | core | H | Trivial to detect; should be skipped |
| P10 | OCR low-confidence regions (flag for re-OCR pass) | side | M | More quality-check than paratext-removal; lives at quality layer (Q) |
| P11 | Frontispiece / dedication / colophon (front/back matter that's not body) | sub | M | Decide per-policy whether body or paratext |
| P12 | Advertisement pages (common in older books) | sub | M | Archival editions often have publisher ads at end; not body |
| P13 | Library / acquisition stamps (in scanned editions) | sub | H | Visible in many PDF scans; not body content |

### Sub-region B — Structural boundary detection (USER'S NAMED CANDIDATE)

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| B1 | Chapter-level boundary detection (h1) | core | H | The user's primary named candidate |
| B2 | Subchapter / section boundary detection (h2) | core | H | The user's named candidate |
| B3 | Sub-sub-chapter detection (h3) | core | H | The user's named candidate |
| B4 | Sub-sub-sub-chapter detection (h4) | core | M | The user's depth-4 ceiling; should depth be examined? |
| B5 | Depth-of-detection policy (2 vs 3 vs 4 vs 5 vs unlimited) | core | H | The user said "this is deep enough I think" with hedge — adjudicate honestly |
| B6 | Detection signals: heading font size / weight / centering | sub | H | Format-dependent (PDF: layout; EPUB: existing h-tags; Word: styles) |
| B7 | Detection signals: numbered prefix ("1." / "Chapter 3" / "Birinci") | sub | H | Language-aware; Turkish ordinals (Birinci/İkinci/Üçüncü) |
| B8 | Detection signals: letter-spaced emphasis ("T e n b i h") | sub | M | Risale-i-Nur-specific; un-spacing needed to recognize the marker |
| B9 | Detection signals: corpus-specific keywords (Mukaddeme / Mes'ele / Hâtime / Tenbih) | side | M | Corpus-tuned; tension with "generic translation project" framing |
| B10 | Hierarchy inference when source uses flat h1 only (EPUB case we just saw) | core | H | The Asa-yı Musa EPUB has flat h1; Mukaddeme/Mes'ele markers live in body text |
| B11 | Cross-corpus generality test (academic books / drama / poetry / religious texts have different hierarchies) | sub | H | Should the depth policy be format-agnostic or per-corpus? |
| B12 | Nested-section container model (<section> + h2 inside <section> + h1) | sub | M | The implementation question — flat headings vs nested containers |
| B13 | Section identity preservation across re-intake (stable IDs for sections) | sub | M | If re-intake of the same source produces section "Mes'ele 2", it should get the same identity each time |

### Sub-region S — Other structural detection

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| S1 | Paragraph boundary detection (when paragraphs collapse) | core | H | PDFs commonly collapse paragraphs; intake re-paragraphs |
| S2 | List detection (numbered / bulleted / nested) | sub | M | Adjacent to structural detection |
| S3 | Table detection (rows × columns; cell content) | sub | H | Generic-corpus relevant (academic, technical); rare in Risale-i Nur |
| S4 | Quote-block detection (indented; cited) | side | M | Borders on voice-marking classification |
| S5 | Verse / poetry-block detection (line-broken; centered; couplet pairs) | side | M | Borders on EmbeddedPoetryPolicy classification |
| S6 | Code-block detection (monospace; indented) | sub | L | Rare in literary corpus; high for technical books |
| S7 | Footnote / endnote detection (apparatus separation) | core | H | EPUB analysis showed Risale-i Nur footnotes are first-class; intake must preserve structure |
| S8 | Marginalia detection (hashiye) | side | M | Risale-i-Nur-specific structural feature; borders on SourceApparatusPolicy |
| S9 | Cross-reference detection ("see chapter 3"; "ibid"; "op. cit.") | sub | M | Could be preprocessing (mark up the reference) or classification (resolve the link) |
| S10 | Table-of-contents detection (front-matter ToC; back-matter index) | sub | M | Useful for chapter-numbering and ToC reconstruction |
| S11 | Figure / illustration caption detection | sub | M | Captions are structurally distinct from body |
| S12 | Drop-cap detection (large initial capital letter at chapter opener) | sub | M | Should be normalized (the "T" of "The..." that's drop-cap shouldn't extract as separate from "he...") |
| S13 | Block-quote vs inline-quote distinction | side | M | Borders on voice marking |

### Sub-region L — Linguistic preprocessing

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| L1 | Sentence segmentation (sentence-boundary detection with abbreviation handling) | core | H | Load-bearing for translation chunking; LLM benefits from sentence-clean input |
| L2 | Paragraph segmentation (paragraph-boundary detection) | core | H | Companion to S1 (paragraph boundary detection) |
| L3 | Document-level language identification | core | H | Cheap, useful; informs translate-stage's source-language config |
| L4 | Per-span language identification (Arabic in Turkish; Latin in French) | side | M | Crosses into classification per the recent scope narrowing |
| L5 | Encoding detection / mojibake repair (UTF-8 misread as latin1) | core | H | Cheap; one-pass; saves downstream pain |
| L6 | Tokenization (word boundaries) | side | L | Usually translate-stage's job; not intake's |
| L7 | Right-to-left text run identification (without classifying script) | side | M | Could be done without lang= tagging — just identify Unicode bidi-strong runs |
| L8 | Hyphenation-at-line-break repair (mid-word hyphens from PDF) | core | H | Cheap; high value; common PDF artifact |

### Sub-region M — Metadata extraction

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| M1 | Title extraction (from front matter or metadata block) | core | H | Document-level; clearly preprocessing |
| M2 | Author extraction | core | H | Document-level |
| M3 | Publication date / publisher | core | H | Document-level |
| M4 | ISBN / DOI / ASIN | sub | M | Useful for cross-reference; less universal across formats |
| M5 | Chapter numbers + chapter titles → reconstructed ToC | core | H | Pairs with B (boundary detection) |
| M6 | Volume / part / edition info | sub | M | For multi-volume works |
| M7 | Source-format metadata extraction (EPUB OPF; PDF /Info; Word docProps) | core | H | Format-specific; cheap; useful |
| M8 | Cover image extraction | sub | M | For publishing layer; useful at intake-time to associate with document |
| M9 | Language tag extraction from source metadata (EPUB <dc:language>) | core | H | Cheap document-level signal; informs L3 |
| M10 | License / copyright extraction | sub | M | For corpus provenance and legal handling |

### Sub-region F — Format-specific repair

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| F1 | PDF bidi-fix for broken-bidi Arabic | core | H | The Asa-yı Musa PDF case; if PDF intake is supported, this is load-bearing |
| F2 | PDF italic / bold recovery (extra extraction pass) | sub | H | mutool / pdf2htmlEX provides this; not automatic with pdftotext |
| F3 | PDF column-order repair (multi-column extraction) | sub | M | Academic papers; less relevant for Risale-i Nur (single-column) |
| F4 | PDF mid-word hyphen repair (text wrap artifacts) | core | H | Companion to L8; usually a PDF-specific artifact |
| F5 | EPUB CSS-presentation extraction (turn `class="bold"` into `<strong>`) | core | H | The Asa-yı Musa EPUB analysis showed presentation-only spans; intake should semanticize |
| F6 | EPUB heading-level inference (when source uses h1 only) | core | H | Asa-yı Musa EPUB has flat h1; intake should infer hierarchy from body markers |
| F7 | Word style-mapping (Heading 1 / Heading 2 → semantic; "Normal" → `<p>`) | core | H | If Word intake supported; standard for .docx ingestion |
| F8 | HTML cleanup (remove inline styles; strip presentation-only spans) | core | H | Useful for any HTML/XHTML source |
| F9 | OCR artifact fixing (smart space removal; common substitutions like "rn" → "m") | sub | M | For OCR-derived sources; needs careful pattern bank |
| F10 | EPUB spine reassembly (read content documents in spine order; concatenate) | core | H | EPUB-specific; cheap; should be standard |
| F11 | Word run-merge (consecutive runs with same formatting → single run) | sub | M | Word docs split text into runs; intake should merge |
| F12 | Plain-text encoding detection (BOM; chardet; fallback) | core | H | If plain-text intake supported; foundational |

### Sub-region A — Apparatus / cross-reference

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| A1 | Footnote/endnote extraction and reattachment | core | H | EPUB analysis showed hashiye are first-class apparatus; intake must preserve structure |
| A2 | Marginalia detection and separation | side | M | Risale-i Nur hashiye; borders on SourceApparatusPolicy classification |
| A3 | Cross-reference resolution (anchor + href) | sub | M | Preprocessing if just preserving links; classification if resolving "see Chapter 3" |
| A4 | Citation parsing (extract author / year / page from inline citations) | side | M | Borders on classification; useful for academic books |
| A5 | Bibliographic entry detection (back matter bibliography) | sub | M | Structural detection at front/back matter |
| A6 | Index entry extraction (back matter index) | sub | M | Structural detection at back matter |
| A7 | Footnote-back-reference linking (body anchor + footnote anchor) | core | H | EPUB analysis showed Asa-yı Musa already has this — just preserve |

### Sub-region Q — Quality / hygiene

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| Q1 | Broken-Unicode detection (lone surrogates; invalid UTF-8) | core | H | Cheap; fundamental |
| Q2 | Orphan-content detection (single char / one-word paragraphs) | sub | M | Surfaces extraction artifacts |
| Q3 | Suspicious line-break detection (mid-word; mid-sentence) | sub | M | Common PDF artifact |
| Q4 | Typo / spelling-error flagging (against dictionary) | side | L | Could cross to translate-stage; intake doesn't usually correct typos |
| Q5 | OCR-confidence aggregation per region | sub | M | If OCR is in the pipeline; document-level quality signal |
| Q6 | Document-completeness check (ToC matches headings; footnote refs match footnotes) | sub | M | Structural sanity check |
| Q7 | Duplicate-content detection (boilerplate; OCR run twice) | sub | M | Quality signal |
| Q8 | Truncation detection (file ends mid-sentence) | sub | H | Common when intake input is partial; should flag loudly |
| Q9 | Encoding-confidence flagging (if encoding detection is uncertain) | sub | M | Companion to L5 |
| Q10 | Round-trip stability test (NFC(NFC(x)) == NFC(x)) | sub | L | Self-check; verification not preprocessing |

### Sub-region V — Source-provenance stamping (document-level)

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| V1 | Source-file path / URL | core | H | Cheap; foundational |
| V2 | Source-file checksum (SHA-256) | core | H | Cheap; enables idempotency check and corpus deduplication |
| V3 | Intake-timestamp | core | H | Cheap; foundational |
| V4 | Intake-tool version | sub | H | Useful for reproducibility |
| V5 | Intake-pipeline configuration hash | sub | M | If preprocessing config can vary between runs |
| V6 | Source-format detection result | core | H | Records what intake decided the source was |
| V7 | Source-language declaration | core | H | From metadata or L3 auto-detection |
| V8 | Source-mime-type recording | sub | M | Useful for format-aware downstream tools |
| V9 | Source-encoding recording (UTF-8 / latin1 / etc.) | sub | M | Companion to L5 |
| V10 | Intake-stages-log (which preprocessing operations ran; outcomes) | sub | M | Document-level audit log |

### Sub-region E — Edit-friendliness / output-shape ops

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| E1 | Markdown round-trip-stable subset filtering (only emit features that survive md→html→md) | side | M | Only relevant if hand-edit layer in markdown is actually used; the prior finding committed this layer |
| E2 | Line-wrap normalization (hard vs soft wraps) | sub | M | For markdown hand-edit output |
| E3 | Indentation normalization (tabs vs spaces; consistent indent width) | sub | L | Edge case |

### Sub-region C — Creative / novel operations

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| C1 | Reading-order semantic reconstruction (for PDFs with weird multi-flow layouts) | sub | M | PDF-specific; useful for academic / multi-column |
| C2 | Drop-cap detection (large chapter-opening capital) | sub | M | Visual feature; needs normalization |
| C3 | Stamp / handwritten-note detection in scanned books | sub | L | Niche; archive.org scans have these |
| C4 | Page-break-as-structural-signal detection | sub | M | Some books use page breaks to mark new sections |
| C5 | Hyperlink resolution and stub generation | sub | L | For source documents with internal links |
| C6 | Image alt-text extraction | sub | M | If images are in source; useful for accessibility and search |
| C7 | Author-voice vs editor-voice separation (foreword written by someone else) | side | L | Borders on classification |
| C8 | Decorative-character cleanup (asterism; section-break ornaments) | sub | H | Visual ornaments that should be normalized or stripped |
| C9 | Letter-spaced-emphasis detection ("T e n b i h") | sub | M | Risale-i-Nur-specific; intake should un-space and recognize |
| C10 | Drop-numbered-list-shape detection (when "1." / "2." should be a list) | sub | M | Numbered paragraph vs list distinction |
| C11 | Inline-citation detection ("Smith 2020") | side | L | Academic-corpus relevant; borders on classification |
| C12 | Headword detection for glossary/dictionary entries | sub | L | Reference-text-specific |
| C13 | Speaker-tag detection in dialogue ("Alice:" / "Bob:") | sub | L | Drama / interview / dialogue formats |
| C14 | Two-column layout extraction (handle bilingual side-by-side editions) | sub | M | For parallel-text editions |
| C15 | Inline-equation / math notation preservation | sub | L | Academic / technical books |
| C16 | Initialism / acronym expansion ("USA" → "United States of America") | side | L | Borders on translate-stage prep; not intake |
| C17 | Date / number normalization (dates / currency to canonical form) | side | L | Could be translate-stage prep |
| C18 | Section-heading capitalization normalization | sub | L | "CHAPTER ONE" vs "Chapter One" vs "chapter one" |
| C19 | Frequency-based glossary candidate detection (terms appearing often) | side | L | Borders on translate-stage context-prep |
| C20 | Hyperlink target validation (broken internal links) | sub | L | Quality signal |

### Sub-region D — Depth-of-boundary-detection candidates (sub-territory of B)

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| D1 | Depth 1 only (chapters; flat structure) | sub | M | Minimum viable; matches Asa-yı Musa EPUB |
| D2 | Depth 2 (chapter + section) | core | H | Common literary book depth |
| D3 | Depth 3 (chapter + section + subsection) | core | H | Academic book depth |
| D4 | Depth 4 (chapter + section + subsection + sub-subsection) — user's proposal | core | H | User-named ceiling; "this is deep enough I think" |
| D5 | Depth 5 (book / part / chapter / section / subsection) | sub | M | Multi-volume textbooks |
| D6 | Depth 6+ (deeply nested academic / encyclopedic) | side | L | Rare in target corpora |
| D7 | Unlimited / adaptive (let the corpus decide) | sub | M | Implementation strategy; might over-fit |
| D8 | Per-format depth caps (different ceilings per source format) | sub | M | EPUB might cap at 2-3; PDF might support deeper |
| D9 | Risale-i Nur specific depth: Book → Risale → Mukaddeme/Mes'ele/Hâtime → sub-paragraph | side | M | Corpus-specific instance |

### Sub-region G — Scope-line gray-zone analysis

| # | Item | Tag | Conf | Brief gloss |
|---|---|---|---|---|
| G1 | Operations CLEARLY preprocessing (NFC; whitespace; paratext; ligature; encoding) | core | H | The unambiguous yes-set |
| G2 | Operations CLEARLY classification AND OUT per scope narrowing (7-policy; per-element provenance; per-span lang=; voice marking) | core | H | The unambiguous no-set |
| G3 | Gray zone: structural boundary detection — is heading detection classification? | core | H | The decision-mode trigger: user named this; inquiry must adjudicate where it lives |
| G4 | Gray zone: sentence segmentation — structural detection, preprocessing? | sub | H | Most pipelines treat as preprocessing |
| G5 | Gray zone: footnote extraction — apparatus IS a class but extraction can be structural | core | H | EPUB analysis showed footnote markup is structural, not classificational, when source has explicit structure |
| G6 | Gray zone: table detection — identifying structural class | sub | M | Most pipelines treat as preprocessing |
| G7 | Gray zone: quote-block detection — borders on voice marking | side | M | Where does indentation-quotes end and voice-class begin? |
| G8 | Gray zone: per-span language identification — lang= tag IS the result; clearly classification | core | H | The scope narrowing explicitly rules this out |
| G9 | Gray zone: metadata extraction (title / author) — document-level vs per-element | sub | H | Document-level extraction is preprocessing; per-element is classification |
| G10 | Principle: structural-not-semantic distinction — preserve structure WITHOUT semantic role tagging | core | H | The proposed scope-line: structural detection (where things are) is preprocessing; semantic classification (what role they play) is classification |

---

## State Summary

### Territory + Purpose echo

- **Territory:** the conceptual design space of intake preprocessing operations, partitioned into 12 sub-regions (T text-cleanup; P paratext; B boundary-detection; S other-structural; L linguistic; M metadata; F format-specific; A apparatus; Q quality; V provenance; E edit-friendliness; C creative) + 2 sub-territories (D depth-of-boundary; G scope-line analysis).
- **Purpose:** enumerate preprocessing operations for intake beyond the NFC + paratext baseline; evaluate structural boundary detection (depth ~4) as one named candidate; surface creative / non-obvious operations; respect the minimal-intake scope narrowing.

### Coverage map

| Sub-region | Coverage status | Item count | core | sub | side | umbrella |
|---|---|---|---|---|---|---|
| T — Text-level cleanup | confirmed | 15 | 6 | 8 | 1 | 0 |
| P — Paratext / non-body removal | confirmed | 13 | 6 | 6 | 1 | 0 |
| B — Structural boundary detection | confirmed | 13 | 5 | 7 | 1 | 0 |
| S — Other structural detection | confirmed | 13 | 2 | 6 | 5 | 0 |
| L — Linguistic preprocessing | confirmed | 8 | 5 | 0 | 3 | 0 |
| M — Metadata extraction | confirmed | 10 | 6 | 4 | 0 | 0 |
| F — Format-specific repair | confirmed | 12 | 8 | 4 | 0 | 0 |
| A — Apparatus / cross-reference | confirmed | 7 | 2 | 3 | 2 | 0 |
| Q — Quality / hygiene | confirmed | 10 | 1 | 7 | 2 | 0 |
| V — Source-provenance stamping | confirmed | 10 | 5 | 5 | 0 | 0 |
| E — Edit-friendliness | confirmed | 3 | 0 | 2 | 1 | 0 |
| C — Creative / novel operations | confirmed | 20 | 0 | 12 | 8 | 0 |
| D — Depth-of-boundary sub-territory | confirmed | 9 | 3 | 4 | 2 | 0 |
| G — Scope-line gray-zone analysis | confirmed | 10 | 5 | 3 | 2 | 0 |
| **Total** | — | **153** | **54** | **71** | **28** | **0** |

### Confirmed-absent regions

None. The territory was bounded and exhaustively traversed at the candidate-resolution. No sub-region was found empty of candidates.

### Concept-names (selected high-relevance items + key sub-territory anchors)

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| NFC normalization | structural-reference | T1 | Baseline; established in prior finding |
| Whitespace normalization | structural-reference | T3 | Standard one-pass; prevents extraction artifacts |
| Ligature decomposition | structural-reference | T12 | PDF text-layer commonly contains ligatures |
| Paratext stripping | structural-reference | P1–P6 | Baseline; established in prior finding |
| Structural boundary detection | structural-reference | B1–B13 | User's named candidate; depth-policy adjudication needed |
| Hierarchy inference from flat-h1 source | structural-reference | B10, F6 | EPUB case where source uses h1 only |
| Sentence segmentation | structural-reference | L1 | Load-bearing for translation chunking |
| Document-level language identification | structural-reference | L3 | Cheap; informs translate-stage config |
| Hyphenation-at-line-break repair | structural-reference | L8, F4 | High-value low-cost PDF artifact fix |
| Mojibake repair | structural-reference | L5 | Encoding detection / repair |
| Title / author / metadata extraction | structural-reference | M1–M3 | Document-level; clearly preprocessing |
| Footnote / apparatus extraction | structural-reference | A1, A7, S7 | Structural in EPUB; classification-adjacent otherwise |
| Source-provenance stamping | structural-reference | V1–V7 | Document-level audit / reproducibility |
| Broken-Unicode detection | structural-reference | Q1 | Cheap; fundamental quality check |
| Truncation detection | structural-reference | Q8 | High-impact when source is partial |
| Scope-line: structural-not-semantic | coined-term | G10 | Proposed scope-line — preserve structure WITHOUT semantic role tagging |
| Depth-of-detection policy | coined-term | B5, D1–D9 | The user's depth-4 ceiling — should be examined |
| Letter-spaced emphasis | structural-reference | C9, B8 | Risale-i-Nur-specific marker (Tenbih) needing un-spacing |
| Drop-cap detection | structural-reference | C2, S12 | Visual feature needing normalization |
| Decorative-character cleanup | structural-reference | C8 | Asterism / dingbats / section-break ornaments |
| Two-column / bilingual layout | structural-reference | C14 | Parallel-text edition handling |

### Recency distribution

All items are possibility-mode candidates with `{source: none, value: null}` — no filesystem backing. Per-region: `{newest: null, oldest: null, no-mtime-count: <region item count>, total-items: <region item count>}` for every region. The recency-distribution field is structurally empty as expected for `possibility` mode.

### Frontier flags

- **F-1: Decision-mode joint axis** (irreducible overlap from articulation MQA) — the inquiry must navigate `[generative-breadth-first / commit-to-recommended-set / probe-the-boundary / evaluate-named-candidate-only / classify-by-cost-value]`. Sensemaking adjudicates.
- **F-2: Scope-line joint axis** (irreducible overlap from articulation MQA) — where does preprocessing end and classification begin? Sub-region G surfaced 10 gray-zone items; sensemaking must commit a principle (G10 candidate: structural-not-semantic).
- **F-3: Depth-of-boundary-detection adjudication** — the user proposed depth 4 with a hedge ("this is deep enough I think"). Sub-region D enumerated 9 depth options. Sensemaking decides whether depth 4 fits, or whether the right framing is per-format / per-corpus / adaptive.
- **F-4: Source-format mix unknowable from articulation** — the inquiry doesn't yet know whether the project supports PDF / EPUB / Word / plain-text inputs equally or focuses on one. Many operations (F sub-region especially) are format-conditional. Sensemaking may need to commit a format-priority or surface this as Open Question.
- **F-5: Cross-corpus generality vs corpus-tuning tension** — operations like B9 (Mukaddeme/Mes'ele/Hâtime keyword detection) and C9 (Tenbih letter-spaced emphasis) are Risale-i-Nur-specific. The project_scope memory says generic; but calibration corpus is Risale-i Nur. Sensemaking must decide per operation.
- **F-6: Translation-quality-floor question** — some preprocessing operations (sentence segmentation; quotation-mark normalization; hyphenation repair) clearly improve translation quality even without classification. Should the preprocessing set be chosen by "quality contribution to translation" rather than by abstract "is this preprocessing or classification"?

### Workspace-populated status

- **populated:** true
- **populated-at:** 2026-06-17 22:34 UTC
- **extent:** 153 items across 14 sub-regions; relevance-tagged at all four levels; confidence-tagged.

### Re-invocation parameters (suggested)

If sensemaking surfaces gaps:
- Refined-sub-purpose: focus on Sub-region B + D (depth-of-boundary) if user explicitly wants boundary-detection deep-dive.
- Refined-sub-purpose: focus on Sub-region G (scope-line) if downstream wants the principle articulated before the catalog.

---

## Telemetry

- **Mode:** possibility / signal-first
- **Cycles:** 14 (one per sub-region; non-iterative; territory bounded)
- **Items enumerated:** 153
- **Items tagged core:** 54 (35%)
- **Items tagged sub:** 71 (46%)
- **Items tagged side:** 28 (18%)
- **Items tagged umbrella:** 0 — all items had confidence in tag emission; asymmetric-failure principle still respected (no item filtered at uncertain level)
- **Boundary-discovery sub-phase fired:** no (territory was explicit-bounded)
- **Convergence:** met — bounded territory traversed at candidate-resolution; no uncertain-relevance filtering applied
- **Workspace-overload trigger fired:** no (153 items at item-identifier-and-gloss granularity stayed within context budget)
- **items_with_mtime:** 0
- **items_without_mtime:** 153 (possibility-mode; expected)
- **Failure modes scanned:** 1 Missed-relevance (not fired); 2 Surfaced-irrelevance (not fired); 3 Over-coverage (boundary-approached at C sub-region's 20 items but justified by "be creative" purpose); 4 Territory-mis-binding (not fired); 5 Workspace overload (not fired); 6 Artifact under-specification (not fired — every entry has identifier + tag + confidence + gloss); 7 Workspace-artifact desync (not fired — capture-at-moment respected); 8 Recency-Equates-Idleness (not applicable; possibility mode); 9 Recency-Bias-Filter (not applicable; possibility mode); L2: Interpretive-overstep (not fired — no cross-item relational claims); Purpose-loss (not fired — every region tagged against purpose); Self-coupling-to-downstream (not applicable; single-pass)

---

## Self-Assessment Verdict

**PROCEED**

Territory was bounded and exhaustively traversed at candidate-resolution. Relevance-attribution applied per item with confidence assignment. Six frontier flags surfaced for downstream sensemaking. No LAYER 1 or LAYER 2 failure modes fired. Sub-region C ("Creative / novel operations") boundary-approached over-coverage at 20 items, but this was justified by the user's explicit "be creative" purpose — including more candidates is asymmetric-failure-preferred over filtering.
