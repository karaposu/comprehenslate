---
status: active
model: claude-opus-4-7
effort: max
extends: devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/finding.md
---

# Finding: Intake Preprocessing Operations

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/finding.md` (the post-repair canonical format finding; verdict: three-layer architecture with HTML5 canonical, Pandoc-markdown hand-edit, EPUB 3 publishing; NFC normalization and paratext stripping named as minimal-intake cleanup operations).

**Revision trigger:** The user asked, after the prior canonical-format inquiry settled the format, what other preprocessing operations the intake stage should include beyond NFC + paratext — including structural / semantic boundary detection (chapter / subchapter / sub-sub-chapter / sub-sub-sub-chapter) as one explicit candidate, with creativity. The prior finding named two cleanup operations as the minimum-viable set; this finding extends that set into an 8-category recommended preprocessing pipeline organized by a load-bearing scope-line principle.

**Relationship label:** **`extends:`** — additive growth. This relationship is distinct from the prior canonical-format finding's `refines:` label (which means changing one cell of inherited architecture). Here, nothing prior is changed or replaced; the prior's NFC + paratext baseline becomes Categories 1 + 3 of a broader set, and a new scope-line principle is articulated to govern future additions. The label `extends:` is distinct from both `refines:` (no cell changes) and `supersedes:` (nothing replaced) and `corrects:` (the prior was not wrong, just incomplete on this dimension).

**What's preserved:** the prior canonical-format finding's three-layer architecture (HTML5 canonical / Pandoc-markdown hand-edit / EPUB 3 publishing); the prior's NFC + paratext stripping baseline; the prior's HTML5 canonical commitment. The original intake-concepts finding's Decision 2 (structure-preservation quality target), Decision 3 (IntakeDoc shape), Decision 4 (7-policy intake-perception roadmap, deferred), and Decision 5 (Pandoc + OCR architectural lever) all stand.

**What's changed:** the very-recent conversational scope narrowing — "leave content unclassified at intake; trust the LLM to handle per-span language and per-policy classification at translate-stage" — is codified here as the load-bearing scope-line principle "structural, not semantic." This is a load-bearing reversal of one prior commitment: the prior canonical-format finding committed per-element provenance (via HTML5 `data-source` / `data-confidence` / `data-intake-pass` attributes) as a NEW load-bearing dimension. This finding INVALIDATES that per-element-provenance commitment for v0.2 under the scope narrowing; the revival path is preserved in DEFERRED 3 of Next Actions.

**What's new:**

1. The scope-line principle "structural, not semantic" — an operational test-question that decides per-operation verdicts for any preprocessing candidate. (See Finding section §1.)
2. An 8-category recommended preprocessing set: Foundational normalization; Translation-quality-floor; Paratext stripping; Source-format metadata + provenance; Structural detection; Format-specific repair; Quality / hygiene flags; Corpus-specific extensions. (See Finding section §2.)
3. A two-layer corpus model — generic v0.2 core plus calibration-corpus-tuned extensions as an opt-in separate layer. (See Finding section §3.)
4. A depth-of-boundary policy — source-driven hierarchy preservation up to HTML5's h1–h6 ceiling, with hierarchy inference for sources that use a flat single-level heading structure. (See Finding section §4.)
5. A format-priority commitment — EPUB-first for well-formed EPUBs; PDF with OCR fallback for sources that exist primarily in PDF; Word and plain-text deferred. (See Finding section §5.)

**Migration:** zero — the prior finding's NFC + paratext operations carry forward as Categories 1 + 3 in this finding's set; no existing engineering depends on the per-element-provenance commitment that this finding invalidates, since v0.2 has not been built yet (only `SKILL/references/config/schemas.py` exists in the repository as the schema policy definitions; the Mac app's UI scaffolding does not implement intake yet).

---

## Question

(From `_branch.md`'s Item I1, verbatim:)

> *"I agree we should have these 2 steps [NFC + paratext stripping from the prior finding], but maybe also we should detect natural semantic boundaries of the text? For example new chapter or subchapter or sub-sub-chapter or sub-sub-sub-chapter (this is deep enough I think). And what other preprocessing operations can we think of? Be creative."*

The question carries two open dimensions: (1) whether structural / semantic boundary detection at depth around four belongs in the v0.2 intake preprocessing set, and (2) what other preprocessing operations — surfaced creatively — should accompany it. Out of scope: the canonical format choice (settled in the prior canonical-format finding as HTML5); the 7-policy classification work (deferred per the recent scope narrowing); the translation pipeline design (translate-stage is downstream); PDF text-extraction tooling design (the PDF-to-text problem is its own concern).

**Goal.** A categorized recommended preprocessing set for v0.2 intake, including a verdict on structural boundary detection. The deliverable shape combines (a) per-category operation specifications, (b) per-operation cost-vs-value assessment, (c) an adjudicated recommendation about which operations ship in v0.2 versus what is deferred. The motivations the answer should serve include scope-setting for v0.2 engineering, exploring the design space before committing, and ensuring the just-narrowed intake scope doesn't underspecify the floor of preprocessing needed for downstream translation quality.

---

## Finding Summary

- **The scope-line principle for v0.2 intake preprocessing is "structural, not semantic."** Preprocessing identifies WHERE things are and HOW they nest in the source; it does NOT identify WHAT cultural or linguistic role they play. The operational test-question per candidate operation is: *"Does identifying this require knowing what cultural, linguistic, or domain-specific role it plays?"* — yes → semantic (deferred); no → structural (in v0.2). The test is operational across the v0.2 set with an explicit gray-zone adjudication path for edge cases (e.g., parallel-column verse in CJK / Arabic-Persian poetry, where "table" vs "verse" gives a soft verdict).

- **The recommended set has 8 categories.** Foundational normalization (NFC, whitespace, ligatures, quotes, dashes, ellipsis, soft hyphen, zero-width characters including LRM / RLM bidi control marks). Translation-quality-floor (sentence segmentation, paragraph boundary detection, document-level language identification, hyphenation-at-line-break repair, mojibake repair). Paratext stripping (running headers, running footers, page numbers, catchwords, editorial boilerplate, publisher metadata, blank pages, decorative ornaments, watermarks, library stamps). Source-format metadata + provenance (source-format detection, file path, SHA-256 checksum, intake timestamp, intake-tool version, title / author / publication date, source-language declaration, source-metadata pass-through). Structural detection (heading hierarchy preservation, hierarchy inference for flat sources, list / table / quote-block / verse-block / footnote / cross-reference / figure-caption / drop-cap structural operations — all structure-only, no semantic role tagging). Format-specific repair (EPUB: spine reassembly, CSS-presentation extraction, heading-level inference, OPF metadata; PDF: mid-word hyphen repair, column-order, bidi-fix, italic recovery, OCR fallback; Word and plain-text deferred). Quality / hygiene informational flags (suspicious line-break, truncation, document-completeness mismatch, duplicate-content, orphan-content, confusables, encoding-confidence — flags only, not corrective). Corpus-specific extensions (Risale-i Nur-tuned operations: structural-marker keyword recognition for Mukaddeme / Mes'ele / Hâtime / Tenbih / Bismillah; opt-in extension layer, not part of the v0.2 generic core).

- **The depth-of-boundary policy is source-driven hierarchy preservation up to HTML5's h1–h6 ceiling.** In practice most literary texts cap at h4 (honoring the user's "deep enough" instinct); academic texts may reach h5. The h6 ceiling is permissive — preserve what the source provides up to h6; the policy is permissive-not-restrictive. When the source uses a flat single-level heading structure (e.g., the Asa-yı Musa EPUB we analyzed has 33 content files each containing only `<h1>` with sub-structure markers like Mes'ele in body text), intake performs hierarchy inference using body markers to promote sub-section indicators to h2 or h3.

- **The format priority for v0.2 is EPUB-first plus PDF-with-OCR-fallback.** EPUB-first applies to well-formed EPUBs (publisher-issued; clean source-conversion). For EPUB-from-PDF cases (where the EPUB was generated from a scanned PDF and inherits PDF problems like broken-bidi text or lost styling), intake detects the EPUB quality and routes to the PDF processing path. Word and plain-text are deferred to future versions, triggered when the project's source-mix expands.

- **The two-layer corpus model separates generic preprocessing from calibration-corpus-tuned extensions.** Categories 1 through 7 are the generic v0.2 core (no corpus-specific knowledge required). Category 8 is opt-in extensions that activate when corpus context is named at intake-time (e.g., `--corpus risale-i-nur`). The model honors the project's generic-translation scope (per the project-scope memory: comprehenslate is a generic translation project; Risale-i Nur is calibration corpus, not purview) while preserving empirical knowledge about Risale-i Nur's structural vocabulary.

- **Per-element provenance commitment from the prior canonical-format finding is INVALIDATED for v0.2.** That finding committed per-element provenance via HTML5 `data-source` / `data-confidence` / `data-intake-pass` attributes as a NEW load-bearing dimension. The recent scope narrowing — "leave content unclassified; trust the LLM" — invalidates that commitment for v0.2 because attributing provenance requires per-element classification (was this OCR-recovered? a hand-correction? text-layer extraction? a derived element?), which crosses the scope-line into semantic territory. The revival path is preserved (Next Actions / DEFERRED 3); when minimal-intake is tested in production and translation quality empirically requires classification, per-element provenance returns.

- **Inherited commitments from the original intake-concepts finding stand.** Decision 2 structure-preservation quality target is strengthened (Category 5 structural detection is operations actively achieving preservation). Decision 5 Pandoc + OCR architectural lever is strengthened (Category 6 format-specific repair leans explicitly on Pandoc readers and OCRmyPDF + Tesseract). Decision 3 IntakeDoc shape is preserved. Decision 4 7-policy split is deferred with explicit revival path (the 7 policies remain the canonical classification roadmap).

---

## Finding

### Context

Comprehenslate is a generic translation project — a translation skill and a Mac application that consumes source documents in various formats and produces translations. The calibration corpus used to develop and test the skill is Said Nursi's Risale-i Nur (theological texts in Turkish with embedded Arabic), but the project itself is generic; the calibration corpus is the test bed, not the purview.

The intake stage is the first step of the pipeline: it consumes a source document and produces a canonical representation that the translation stage can read. The canonical format was settled in the prior canonical-format finding as HTML5 (with Pandoc-markdown for hand-editing and EPUB 3 for publishing). NFC Unicode normalization and paratext stripping were named as the minimum-viable cleanup operations.

In the conversation since the prior finding, the project's intake scope was narrowed further: "leave content unclassified at intake; trust the LLM to handle per-span language and per-policy classification at translate-stage." Under this narrowing, several operations the prior finding committed as load-bearing — per-element provenance attribution; per-span language identification via `lang=` attributes; the 7-policy classification work — become deferred. The user's question that prompted this inquiry is what then remains in intake's scope: what other preprocessing operations beyond NFC + paratext does the intake stage need, including the user's specific candidate of structural boundary detection at depth around four?

This finding answers by articulating an 8-category recommended preprocessing set anchored by a load-bearing scope-line principle that decides, per candidate operation, whether the operation belongs in v0.2 preprocessing or deferred to later classification work.

### §1 — The scope-line principle: "structural, not semantic"

The load-bearing principle for v0.2 intake preprocessing is the distinction between identifying **structure** (where things are and how they nest) and identifying **semantic role** (what cultural, linguistic, or domain-specific role they play). Preprocessing belongs to the first; classification belongs to the second.

The operational test-question is: *"Does identifying this require knowing what cultural, linguistic, or domain-specific role it plays?"*

- If the answer is **no**, the operation is **structural** — preprocessing — and is in scope for v0.2.
- If the answer is **yes**, the operation is **semantic** — classification — and is deferred per the scope narrowing.

The test is operational for the v0.2 set with explicit gray-zone adjudication paths for edge cases. Some worked applications:

- Detecting that an `<aside>` element exists at body-end with a back-reference link to an in-body anchor → no cultural knowledge required (position + relation) → **structural** → in.
- Tagging that the `<aside>` contains "Said Nursi's marginalia (hashiye)" → yes, requires knowing Risale-i Nur's apparatus tradition → **semantic** → out, deferred.
- Detecting that a span contains Arabic Unicode characters (range U+0600–U+06FF) — purely script-range detection — is borderline structural and could be in. But **emitting a `lang="ar"` attribute on that span** crosses into semantic role-tagging (deciding "this is the non-main-language span") → out, deferred per the recent conversation.
- Detecting that an opening paragraph contains the Bismillah verse and tagging it as a formulaic opening → yes, requires knowing the verse's tradition role → **semantic** → out, deferred.
- Detecting that a block has multiple parallel line-broken stanzas → no cultural knowledge required (line-shape detection) → **structural** → in, emit as `<figure>` containing `<blockquote>` with one `<p>` per line. Do not classify the block as poetry or as a Mevlana couplet — those are semantic.

Some edge cases give soft verdicts:

- Detecting that something is a "table" is mostly structural (rows × columns is universal). But Chinese poetry uses parallel columns that look like tables; distinguishing table from parallel verse requires cultural knowledge. The principle gives a soft verdict at this edge.
- Identifying that a centered bold standalone line is a "sub-section heading" requires knowing the typographic convention. Typographic convention is partially universal (centered bold is widely used for headings) but partially cultural at the edge. The principle gives a soft verdict here too.

These edge cases are adjudicated explicitly via the Open Questions section — they are not silently resolved. The principle is operational across the v0.2 set; gray-zone cases get explicit case-by-case adjudication paths.

### §2 — The 8-category recommended set

The recommended preprocessing pipeline organizes operations into eight categories. The categories are themselves an operational structure — they let the engineering team scope per-category specs (Next Actions / MUST 1) and let the test framework partition fixtures (Next Actions / MUST 5).

#### Category 1 — Foundational normalization

Operations that ensure byte-consistency across formats and sources. Always run, format-agnostic.

| Operation | Python implementation | Notes |
|---|---|---|
| NFC Unicode normalization | `unicodedata.normalize('NFC', text)` (stdlib) | Run first |
| Whitespace normalization | Regex collapse intra-line whitespace runs; preserve double-newline paragraph breaks; LF newlines | |
| Zero-width character removal | Strip U+200B (zero-width space), U+200C (zero-width non-joiner), U+200D (zero-width joiner), U+FEFF (BOM), **U+200E (LRM left-to-right mark), U+200F (RLM right-to-left mark)** | The LRM and RLM bidi control characters can survive PDF extraction and break downstream tools |
| Soft hyphen removal | `text.replace('­', '')` | Invisible hyphenation hint; breaks search |
| Quotation mark normalization | Map to project canonical (curly Unicode: `"` `"` `'` `'` for the project's primary script, which is Latin/Turkish). **Script-specific punctuation in non-primary scripts is preserved** — U+060C (Arabic comma) and U+061F (Arabic question mark) inside Arabic spans are correct Arabic punctuation and must not be normalized to Latin equivalents. The normalization applies only to the project's primary script. |
| Dash normalization | Preserve em (—) / en (–) / hyphen (-) semantic distinctions; convert minus sign and figure dash to hyphen if appearing in body prose |
| Ellipsis normalization | Three dots (U+002E × 3) → U+2026 single character | Pick one canonical |
| Ligature decomposition | Targeted map: ﬁ → fi; ﬂ → fl; ﬃ → ffi; ﬄ → ffl; ﬅ → ft; ﬆ → st | NFKC over-normalizes (eats compatibility characters); use a targeted map instead |
| Broken-Unicode detection | Try-decode with `errors='strict'`; flag failures (the flag goes to Category 7; this operation does not auto-correct) | |

#### Category 2 — Translation-quality-floor

Operations that are load-bearing for translation quality even in the minimal-intake mode. These improve downstream LLM translation without crossing into classification.

| Operation | Python library | Notes |
|---|---|---|
| Sentence segmentation | `spacy` (with the `xx_sent_ud_sm` multi-language sentence-segmentation model) OR `nltk.tokenize.PunktSentenceTokenizer` | **Load-bearing for translation chunking and cross-version consistency, not for raw LLM input.** LLMs handle raw un-segmented text fine; but chunking algorithms must respect sentence boundaries (no mid-sentence cuts), and consistency across re-translation requires stable sentence boundaries. |
| Paragraph boundary detection | Double-newline + indent heuristic | Re-paragraphs collapsed text from PDF extraction |
| Document-level language identification | `langdetect.detect_langs(text)` (PyPI) | Returns BCP 47 codes; informs translate-stage source-language configuration |
| Hyphenation-at-line-break repair | Regex `(\w+)-\n(\w+)` → `\1\2`, applied **only in body paragraphs** (excluding verse-block and list contexts to avoid false-positive merges of intentional line-breaks) | |
| Mojibake repair | `ftfy.fix_text(text)` (PyPI) | Handles UTF-8 misread as latin1; smart-quote glyph confusion |

#### Category 3 — Paratext stripping

The paratext-removal baseline from the prior canonical-format finding, extended. Always run.

Running headers (book or chapter title repeated per page; detected by repetition across pages); running footers; page numbers (regex `^\s*\d+\s*$` standalone digit lines); catchwords (older typesetting convention; regex over end-of-page line duplicating next-page start); editorial boilerplate (`[continued]` / `[end of chapter]`); publisher metadata at chapter starts; blank pages (empty page content); decorative ornaments (asterism, dingbats, section-break ornaments — strippable or convertible to `<hr/>` based on use); watermarks (`scanned by archive.org` and similar known signatures); library or acquisition stamps.

#### Category 4 — Source-format metadata + provenance

Always run. Document-level metadata and provenance stamping.

Source-format detection (file extension + magic bytes via `mimetypes` + `python-magic`); source-file path; source-file SHA-256 checksum (`hashlib.sha256(file_bytes).hexdigest()`); intake-timestamp (`datetime.utcnow().isoformat()`); intake-tool-version; title / author / publication date / publisher (extracted from source metadata blocks — EPUB OPF `<metadata>`; PDF `/Info` dictionary via `pypdf.PdfReader().metadata`; Word `docProps` via `python-docx`); source-language declaration (EPUB `<dc:language>`; PDF `/Lang`; or auto-detected fallback from Category 2 language ID); source-format metadata pass-through (preserve raw OPF / `/Info` / `docProps` as JSON sidecar for audit).

#### Category 5 — Structural detection

Operations that detect WHERE structure lives in the source, without identifying semantic role. The "structural, not semantic" core of the recommended set.

Heading hierarchy preservation (read source headings 1–6; preserve in canonical HTML5). Heading hierarchy **inference** for flat-h1 sources (when source uses only `<h1>` tags, detect body markers — bold + centered + standalone lines — and promote to h2 or h3; conservative one-level promotion by default; deeper inference via Category 8 extensions when corpus context is named). List structural detection (numbered, bulleted, nested). Table structural detection (rows × cells; structure only, not cell-content classification). Quote-block structural detection (block vs inline; converted to `<blockquote>`). Verse-block structural detection (line-broken; centered; converted to `<figure>` containing `<blockquote>` with one `<p>` per line — does NOT classify as poetry or as a specific traditional verse form). Footnote / endnote **structural extraction** (`<aside>` element at body-end with `id` and back-reference `<a href="#fn1">` from in-body anchor — positional and relational; does NOT tag the aside as marginalia, hashiye, or any other semantic role). Cross-reference structural preservation (preserve `href` + matching `id`; do NOT resolve citations or semantically link). Figure / illustration caption (`<figure>` + `<figcaption>`). Drop-cap normalization (detect the large initial capital used at chapter openers; merge with following text to restore normal paragraph flow).

#### Category 6 — Format-specific repair

Per-source-format operations that handle quirks of specific formats. Conditional on source format.

**EPUB (v0.2 primary path):** Spine reassembly (parse `content.opf`; read `<itemref>` ordering in `<spine>`; concatenate XHTML content documents in spine order). CSS-presentation extraction (parse CSS; map presentation-only classes like `class="bold"` to semantic `<strong>`; map `class="italic"` to `<em>`; strip other presentation-only classes). Heading-level inference (when source uses flat `<h1>` only, invoke the Category 5 hierarchy-inference algorithm). OPF metadata extraction (parse `<metadata>` for `<dc:title>`, `<dc:creator>`, `<dc:language>`, `<dc:date>`, `<dc:identifier>`).

**PDF (v0.2 fallback path):** Mid-word hyphen repair (regex `(\w+)-\n(\w+)` in body paragraphs only). Column-order repair (`pdftotext -layout` or `pdf2htmlEX` to preserve geometry; reassemble in reading order). Bidi-fix for broken-bidi Arabic (detect Arabic Unicode runs U+0600–U+06FF; check bidi correctness; for text-layer broken-bidi cases, `python-bidi` library is an alternative to OCR when character recognition is fine but visual-order needs to be converted to logical-order; for image-only Arabic, OCR fallback is necessary). Italic / bold recovery (secondary extraction pass via `mutool draw -F text` or `pdf2htmlEX`, which preserve style annotations the default `pdftotext` strips). OCR fallback (`OCRmyPDF` with Tesseract `--lang ara+tur` for the Asa-yı Musa PDF case with broken-bidi text-layer and the Muhakemat case with image-only Arabic).

**Word (deferred to future):** Style-mapping (read `styles.xml`; map Heading 1–9 → `<h1>`–`<h6>`; Normal → `<p>`; preserve formatting runs as `<strong>` / `<em>`). Run-merge (consecutive runs with identical formatting properties → merge text content).

**Plain-text (deferred to future):** Encoding detection (try UTF-8 → latin1 → cp1252 → `chardet` fallback; BOM-aware). Line-ending normalization (CRLF → LF; preserve paragraph breaks).

**Format-priority justification.** EPUB-first applies to **well-formed EPUBs** (publisher-issued; clean source-conversion). EPUB intake is significantly cheaper than PDF intake in such cases because the Arabic Unicode is in the text-layer cleanly, italic and bold are preserved as `<em>` and `<strong>`, footnote structure is intact, and OPF metadata is extractable — none of the OCR, bidi-fix, or italic-recovery work that PDF intake requires is needed. This was empirically verified during this session via the Asa-yı Musa EPUB analysis (`writer2epub` 1.1.17, 2012; 33 content files plus a separate footnotes file and cover; clean Unicode Arabic; CSS-as-presentation extractable).

However, some EPUBs are converted FROM PDF and inherit PDF problems (broken-bidi Arabic; lost styling; bad paragraph splits). For such **EPUB-from-PDF cases**, intake detects the EPUB quality via heuristics (OCR artifacts in text; flat-h1 structure; minimal CSS; presence of mid-word hyphens; broken-bidi Arabic in text-layer) and routes to the PDF processing path. EPUB-from-PDF detection composes with Category 7 quality flags.

PDF-with-OCR-fallback handles sources that exist primarily in PDF. Empirical evidence justifying this: the Asa-yı Musa PDF has broken-bidi Arabic in its text-layer (letters in display order rather than logical order); the Muhakemat PDF has Arabic only as bitmap images (the Arabic was pasted as images in the original Word source). For broken-bidi text-layer cases, `python-bidi` is the cheaper alternative when character recognition is fine; for image-only Arabic, full OCR is necessary.

#### Category 7 — Quality / hygiene flags

Operations that detect quality issues but DO NOT auto-correct. Always run, informational, not corrective.

Suspicious line-break (mid-word or mid-sentence breaks the Category 2 hyphenation-repair didn't resolve). Truncation (last paragraph ends without sentence terminator). Document-completeness mismatch (heading count vs ToC entries; footnote refs vs footnote bodies; mismatch flagged). Duplicate-content (SHA-256 over paragraph windows; near-duplicates flagged). Orphan-content (paragraphs with very short text — potentially extraction artifacts). Confusables (Unicode confusables detection — Cyrillic А vs Latin A, etc.). Encoding-confidence (when `ftfy` reported changes or `langdetect` confidence is below threshold).

**Why informational, not corrective.** Truncation could be auto-corrected by dropping the incomplete paragraph, but the truncation may be intentional (a quote that ends mid-thought; a deliberate stylistic device). Auto-correcting destroys user agency over content. Duplicate-content could be auto-deduplicated but may be intentional (a refrain in poetry; a deliberate echo). Orphan-content could be auto-removed but a single-character paragraph might be a chapter-opening drop-cap that wasn't normalized properly. The informational-flag approach preserves user agency: intake reports what it detected; the user (or downstream tools, or the human reviewer) decides whether to act.

**Flag exposure mechanism** is committed at Next Actions / MUST 4. Working assumption: a sidecar JSON file `<canonical>.intake-flags.json` next to the canonical HTML5 file, with a schema listing flag codes, severity, context, and source positions. An alternative mirror via HTML5 `<head>` `<meta name="intake-flag" content="..."/>` blocks is being considered for in-document inspection.

#### Category 8 — Corpus-specific extensions (opt-in)

Operations that depend on knowing a specific corpus's structural vocabulary. NOT part of the v0.2 generic core; activated only when corpus context is named at intake-time (e.g., `--corpus risale-i-nur`).

The current Category 8 contents are Risale-i Nur-tuned:

- **Risale-i Nur structural-marker keyword recognition.** Detects the words `Mukaddeme` (preamble), `Mes'ele` (numbered topic — with Turkish ordinals like `Birinci` / `İkinci` / `Üçüncü`), `Hâtime` (conclusion), `Tenbih` (note), and `Bismillah` when they appear at section-opener positions (bold + centered + standalone-line content matching the keyword regex). Promotes the detected markers to sub-headings (`<h2>` or `<h3>`) within the Category 5 hierarchy-inference algorithm for flat-h1 sources (such as the Asa-yı Musa EPUB). The detection is keyword-position structural detection — not semantic role tagging (which would require knowing what Mukaddeme MEANS in Risale-i Nur's theology). The Turkish-alphabet calibration regex for the structural-marker detection is part of this Category 8 extension.

- **Other Risale-i Nur-specific patterns** (deferred to Category 8 extension API design in Next Actions / COULD 1): hashiye footnote conventions; Mevlana attribution patterns in verse blocks; Bismillah position at section start.

**Letter-spaced-emphasis un-spacing** is generic typographic cleanup (used in many traditions: German typesetting like "S c h ö n e Welt"; old English typesetting like "S P A C E D"; academic style guides). Therefore the **operation** (detect runs of single-character + whitespace patterns; collapse spaces) lives in **Category 1 — Foundational normalization**, not Category 8. The Turkish-script-specific calibration regex and frequency thresholds (which Latin alphabet's standalone uppercase + lowercase patterns to recognize as letter-spaced; what frequency cutoff distinguishes letter-spaced emphasis from initialisms like "U S A") are Category 8 calibration data for the Risale-i Nur extension.

### §3 — The two-layer corpus model

The recommended set has two architectural layers:

1. **Generic v0.2 core (Categories 1–7).** Operations that work on any source corpus regardless of its specific structural vocabulary. NFC normalization, paratext stripping, sentence segmentation, source-format metadata extraction, generic structural detection — none of these require knowing what corpus the document came from.

2. **Calibration-corpus extensions (Category 8).** Operations that depend on knowing the source corpus's specific structural vocabulary (named markers, numbering conventions, paratext patterns). These are opt-in extensions activated only when corpus context is named at intake-time.

**The test for which layer an operation belongs to.** Ask: "Does this operation depend on knowing the corpus-specific structural vocabulary (named markers, numbering conventions, paratext patterns) of a particular text tradition?" — yes → Category 8. No → Categories 1–7.

**Why this matters.** Comprehenslate is a generic translation project; Risale-i Nur is the calibration corpus, not the project's purview. A single-tier preprocessing pipeline would force a false dichotomy: either "pollute" the generic core with Risale-i Nur-specific operations (violating the generic-project commitment) or "drop" everything corpus-specific (losing the empirical knowledge that motivated the design). The two-layer model preserves both invariants — generic-project commitment plus calibration-corpus knowledge — by architectural separation. The plugin architecture analogy is well-established in software (Pandoc itself uses readers + filters + writers in distinct layers).

For v0.2, the Category 8 Risale-i Nur extension can be hardcoded; the formal extensions API (per the project's COULD 1) is post-v0.2 work, triggered when a second corpus enters the project.

### §4 — The depth-of-boundary policy

The depth policy is **source-driven hierarchy preservation up to HTML5's h1–h6 ceiling.**

- When the source format encodes heading hierarchy (XHTML / HTML / Word with style-mapping), preserve the source's hierarchy up to depth 6 (the W3C HTML Living Standard's heading-element ceiling).
- When the source uses a flat single-level heading structure (the Asa-yı Musa EPUB has 33 content files each with only `<h1>`), perform **hierarchy inference** using body markers (bold + centered + standalone-line patterns) to promote sub-section indicators to h2 or h3.
- No absolute depth cap below h6.

**Honoring the user's "deep enough" instinct.** The user proposed depth around 4 (chapter / subchapter / sub-sub-chapter / sub-sub-sub-chapter) as "deep enough I think." This finding honors the empirical observation: literary texts (including Risale-i Nur) typically cap at h4; academic books may reach h5; the h6 ceiling is permissive — preserve what the source provides up to h6, but most sources will not exceed h4. The policy is permissive-not-restrictive: it does not require depth 6; it accepts depth up to 6.

**Hierarchy-inference algorithm sketch (for flat-h1 sources).** Detect bold + centered + standalone-line markers in body text. Cluster markers by frequency and position. If a marker matches a Category 8 corpus-extension keyword (e.g., Mukaddeme, Mes'ele, Hâtime), promote per the extension's depth-mapping. If no corpus-extension is active, promote bold-centered standalone lines to h2 by default (conservative one-level promotion); leave deeper inference to corpus extensions. Wrap promoted sections in `<section>` containers.

The exact regex patterns, clustering thresholds, and edge-case handling are deferred to Next Actions / MUST 2 (the hierarchy-inference algorithm specification).

### §5 — The format priority commitment

The v0.2 format priority is **EPUB-first plus PDF-with-OCR-fallback**, with Word and plain-text deferred to future format additions.

**EPUB-first** applies to well-formed EPUBs (publisher-issued; clean source-conversion). EPUB intake is significantly cheaper than PDF intake in such cases. For EPUB-from-PDF cases (where the EPUB was generated from a scanned PDF and inherits PDF problems), intake detects the EPUB quality via heuristics and routes to the PDF processing path. EPUB-from-PDF detection is itself an open question (see Open Questions section) — the heuristics need empirical calibration.

**PDF-with-OCR-fallback** handles sources that exist primarily in PDF. The empirical evidence justifying PDF intake's necessity comes from the Asa-yı Musa PDF (broken-bidi Arabic in text-layer; visually correct, structurally broken when extracted) and the Muhakemat PDF (Arabic absent from text-layer entirely; pasted as bitmap images). For broken-bidi text-layer cases, `python-bidi` is a cheaper alternative to OCR when character recognition is fine and only visual-order-to-logical-order conversion is needed. For image-only Arabic, OCR fallback is necessary (OCRmyPDF with Tesseract `--lang ara+tur`).

**Word and plain-text are deferred** to future format additions. The revival trigger is observable: when the project's source-mix expands to include Word or plain-text sources, the deferred Category 6 operations activate.

The format priority composes with the original intake-concepts finding's Decision 5 (Pandoc + OCR architectural lever): Pandoc reads EPUB, HTML, and Word per its documented format matrix; OCRmyPDF + Tesseract handle the PDF Arabic-recovery cases; the lever stays the load-bearing universal-conversion mechanism.

### §6 — Rejected candidates

Of the 153 candidates the inquiry surfaced across 14 categories, the following are explicitly rejected for v0.2 with structural reasons:

**Per-element provenance attribution (`data-source` / `data-confidence` / `data-intake-pass` per HTML5 element).** Rejected via the scope-line principle. Attributing provenance requires deciding which element class to attribute to (was this an OCR-recovered Arabic span? a hand-correction? a derived element?), which is semantic role tagging. The prior canonical-format finding committed per-element provenance as a NEW load-bearing dimension; this finding **explicitly reverses that commitment for v0.2 under the recent scope narrowing**. The revival path is preserved in DEFERRED 3 of Next Actions; when minimal-intake is tested in production and translation quality empirically requires classification, per-element provenance returns.

**Per-span language identification with `lang=` tagging.** Rejected via the scope-line principle. Emitting `<span lang="ar">` requires classifying which spans are non-main-language; the classification is the semantic act. The LLM-based translator handles mixed-script text correctly without per-span tags (per the recent conversation that established this scope narrowing).

**The 7 schema policies** (NonMainLangPartsPolicy, SourceApparatusPolicy, VoiceMarkingPolicy, ArchaicRegisterPolicy, HonorificsPolicy, FormulaicOpeningPolicy, EmbeddedPoetryPolicy, as defined in `SKILL/references/config/schemas.py`). Each detects cultural or linguistic role; semantic; deferred. The 7 policies remain the canonical classification roadmap when classification is revived.

**Voice marking** (author vs cited authority distinction). Voice is semantic role; deferred.

**Depth-4 as absolute cap.** The user's depth-4 instinct is honored as empirical mean but not committed as absolute cap; replaced by the source-driven up-to-h6 policy.

**PDF-only v0.2** (intake supports only PDF). Rejected — EPUB intake is cheaper and available for the calibration corpus.

**EPUB-only v0.2.** Rejected — Muhakemat exists primarily as PDF with image-only Arabic; ignoring PDF + OCR loses corpus access.

**Drop-everything-corpus-specific.** Rejected — would discard the empirical knowledge (hashiye structure; named ordinals; letter-spaced markers) that motivated the inquiry's design. The two-layer corpus model preserves this knowledge as Category 8 extensions without violating the generic-project commitment.

**Generative-only output** (no recommendation commit). Rejected — surfacing's 153-candidate enumeration already satisfied the generative-only need; the WHY-axis from the question included "scope-setting for v0.2 engineering," which generative-only does not serve.

**Tokenization at intake.** Rejected — translate-stage's job. Intake produces sentence-segmented text; tokenization for LLM input is downstream.

**Per-translation-output format expansion** (initialism expansion; date / number normalization). Rejected — publishing-stage or translate-stage preparation, not intake preprocessing.

---

## Inherited Commitments Re-test

This finding inherits commitments from two priors and the recent scope-narrowing conversation. Each commitment is re-tested below.

### Prior 1 — `devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/finding.md` (the post-repair canonical format finding)

This finding's frontmatter declares `extends:` of this prior.

- **Commitment:** NFC normalization and paratext stripping as minimal-intake cleanup operations.
  - **Re-test status:** **RE-TESTED — commitment confirmed and extended.**
  - **Evidence:** NFC becomes Category 1 in the recommended set; paratext stripping becomes Category 3. The baseline expands into the structured 8-category set; both prior operations carry forward unchanged in their semantics, and Categories 2 + 4 + 5 + 6 + 7 + 8 layer around them.

- **Commitment:** HTML5 canonical format for intake.
  - **Re-test status:** **RE-TESTED — commitment compatible.**
  - **Evidence:** The recommended preprocessing produces structure (h1–h6 hierarchy; semantic elements like `<aside>` for footnotes, `<figure>` for verse-blocks) that fits HTML5 cleanly without crossing into semantic role tagging.

- **Commitment:** Per-element provenance via HTML5 `data-source` / `data-confidence` / `data-intake-pass` attributes as a NEW load-bearing dimension.
  - **Re-test status:** **RE-TESTED — commitment found INVALID for v0.2** under the recent scope narrowing ("leave content unclassified; trust the LLM").
  - **Evidence:** attributing per-element provenance requires deciding which class to attribute to (was this OCR-recovered, hand-corrected, derived, or text-layer extracted?), which is per-element classification — semantic per the scope-line principle. v0.2 intake produces NO per-element provenance attributes. The revival path is preserved: when minimal-intake is tested in production and translation quality empirically requires classification, per-element provenance returns. See Next Actions / DEFERRED 3.

- **Commitment:** Three-layer architecture (canonical HTML5 + Pandoc-markdown hand-edit + EPUB 3 publishing).
  - **Re-test status:** **RE-TESTED — commitment confirmed.**
  - **Evidence:** unchanged; this inquiry operates at the intake layer of the architecture only and does not touch the hand-edit or publishing layers.

### Prior 2 — `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md` (the original intake-concepts finding)

This finding inherits Decisions 2 through 5 through the chain.

- **Commitment:** Decision 2 — structure-preservation quality target.
  - **Re-test status:** **RE-TESTED — commitment confirmed and strengthened.**
  - **Evidence:** Category 5 structural detection is operations that actively achieve preservation; the scope-line principle makes preservation primary by excluding semantic interpretation that could distort structure.

- **Commitment:** Decision 3 — IntakeDoc shape (tree-of-containers + cross-referenced flat collections; preserved-in-semantic-intent with HTML5 DOM substrate per the prior canonical-format finding).
  - **Re-test status:** **RE-TESTED — commitment confirmed.**
  - **Evidence:** the recommended preprocessing produces HTML5 that maps to the IntakeDoc shape unchanged. Categories 5 + 6 produce structure (sections, asides, figures, blockquotes) that fits the tree-of-containers + flat-collections model.

- **Commitment:** Decision 4 — 7-policy intake-perception + translate-rendering split.
  - **Re-test status:** **RE-TESTED — commitment DEFERRED with explicit revival path.** The 7-policy intent is preserved as roadmap, not as v0.2 implementation. v0.2 intake performs no per-policy classification.
  - **Evidence:** the 7 schema policies (defined in `SKILL/references/config/schemas.py`) involve cultural / linguistic role identification — semantic per the scope-line principle. DEFERRED 3 in Next Actions names the revival trigger (minimal-intake tested in production and translation quality empirically requires classification) and preserves the 7 policies as the canonical classification roadmap.

- **Commitment:** Decision 5 — Pandoc + OCR architectural lever.
  - **Re-test status:** **RE-TESTED — commitment confirmed and strengthened.**
  - **Evidence:** Category 6 format-specific repair explicitly leans on Pandoc readers (EPUB / HTML / Word) and on OCRmyPDF + Tesseract for image-only Arabic; the lever is more concretely committed than before.

- **Commitment:** The 38 intake-handling concepts enumerated in the original finding.
  - **Re-test status:** **RE-TESTED — preserved in intent.**
  - **Evidence:** most of the 38 concepts are honored across the 8 categories; the few involving classification (apparatus role tagging; voice classification) are deferred per the scope-line principle.

### Recent scope-narrowing conversation (not yet committed to a finding before this one)

- **Commitment:** "Leave content unclassified at intake; trust the LLM to handle per-span language and per-policy classification at translate-stage."
  - **Re-test status:** **RE-TESTED — commitment confirmed.**
  - **Evidence:** the scope-line principle ("structural, not semantic") is the operational rule that enforces this narrowing per-operation. Every Category respects the narrowing. The principle gives an explicit gray-zone adjudication path for edge cases (see Finding §1).

### Summary

The prior canonical-format finding's per-element provenance commitment is invalidated for v0.2 with explicit revival path. The original intake-concepts finding's Decision 4 (7-policy split) is deferred with explicit revival path. All other inherited commitments stand or are strengthened. The relationship to the prior canonical-format finding is `extends:` — additive growth around the prior's NFC + paratext baseline; nothing prior is replaced, except the per-element provenance commitment is explicitly invalidated-for-v0.2 with revival path preserved.

---

## Next Actions

### MUST

- **What:** Per-category operation specs ready for engineering (8 categories × per-operation algorithm + library refs + test cases).
  - **Who:** engineering team; either eight sister `/traverse` inquiries (one per category) or a single consolidated spec document.
  - **Gate:** condition-bound — before v0.2 intake code lands.
  - **Why:** the load-bearing engineering contract; without specs, v0.2 intake's behavior is under-specified.

- **What:** Hierarchy-inference algorithm specification for flat-h1 sources.
  - **Who:** a focused `/traverse` inquiry.
  - **Gate:** condition-bound — before v0.2 Category 5 engineering begins.
  - **Why:** the Asa-yı Musa EPUB has flat-h1 with body markers; without inference, sub-section structure is lost. Load-bearing for translation chunking and citation.

- **What:** Format-specific Pandoc invocation patterns documented for EPUB and PDF intake paths.
  - **Who:** engineering documentation plus the project's `comprehenslate/intake/` module.
  - **Gate:** condition-bound — before v0.2 Category 6 engineering begins.
  - **Why:** Pandoc is the architectural lever (Decision 5); concrete invocation patterns ensure reproducibility.

- **What:** Category 7 flag-exposure mechanism (commit schema + format choice between sidecar JSON and HTML5 `<meta>` blocks).
  - **Who:** a focused `/traverse` inquiry.
  - **Gate:** condition-bound — before v0.2 Category 7 engineering begins.
  - **Why:** without a schema, flag consumers cannot act on intake's quality signals.

- **What:** Test-case fixture corpus for v0.2 validation. A set of fixture documents (Asa-yı Musa EPUB; Asa-yı Musa PDF; Muhakemat PDF; small non-Risale-i-Nur fixtures if available) with expected canonical HTML5 outputs and per-category test cases.
  - **Who:** engineering team.
  - **Gate:** condition-bound — before v0.2 ships.
  - **Why:** engineering cannot verify v0.2 behavior without test cases; reproducibility requires golden outputs.

- **What:** Mac app PipelineConfig.swift html-output integration with intake. The app's `PipelineConfig.swift` (line 42) already has `case md, html, plain, json` in its output enum; wire the `html` case to render canonical HTML5 from the intake stage.
  - **Who:** Mac app engineering.
  - **Gate:** condition-bound — before v0.2 ships.
  - **Why:** without UI integration, intake produces files no user interface consumes; v0.2 ship needs the user-facing surface.

- **What:** Pandoc version pin for v0.2 reproducibility. Pin a specific Pandoc version (e.g., Pandoc 3.x at a specific minor version) in the engineering setup; document the upgrade-test protocol.
  - **Who:** engineering team.
  - **Gate:** condition-bound — before v0.2 ships.
  - **Why:** HTML5 conformance is W3C-stable; Pandoc's HTML5 reader/writer behavior may shift between versions for edge cases; pinning bounds operational variability for reproducibility.

### COULD

- **What:** Category 8 extensions API design (opt-in plugin mechanism for corpus extensions).
  - **Who:** a downstream `/traverse` inquiry.
  - **Gate:** observable — when a second corpus enters the project.
  - **Why:** v0.2 can hardcode the Risale-i Nur Category 8 extension; the formal API design (configuration format; registration protocol) is post-v0.2 work needed only when multiple corpora exist.
  - **Depends-on:** MUST "Hierarchy-inference algorithm specification" (the extension API plugs into the hierarchy-inference interface). This COULD is GATED — do not act until the hierarchy-inference MUST resolves.

- **What:** Hierarchy-inference extensions for new corpora beyond Risale-i Nur.
  - **Who:** focused `/traverse` inquiries per added corpus.
  - **Gate:** observable — when the project ingests a second corpus.
  - **Why:** honors the two-layer corpus model's extensibility; gated by corpus diversity expansion.
  - **Depends-on:** COULD "Category 8 extensions API design" AND the project ingesting another corpus. This COULD is GATED — do not act until both resolve.

- **What:** Translation-quality-floor sub-category boundary refinements (promote / demote operations between Categories 1 and 2 as empirical evidence accumulates).
  - **Who:** a downstream `/traverse` inquiry.
  - **Gate:** observable — when empirical evidence supports promotion or demotion of a specific operation.
  - **Why:** the sub-category boundaries are working assumption; v0.2 production data may surface refinements.

### DEFERRED

- **What:** Word and plain-text format support (Category 6 extension to additional source formats).
  - **Gate:** observable — when the project's source-mix expands to include Word or plain-text sources.
  - **Why (if revived):** the current corpus is EPUB/PDF-dominant; engineering effort is bounded.

- **What:** Cross-corpus validation. Test the 8-category set and the scope-line principle against a non-Risale-i-Nur corpus (academic book; modern novel; Talmud apparatus; etc.).
  - **Gate:** condition-bound — when 2+ corpora are in the project (beyond Risale-i Nur).
  - **Why (if revived):** validates that the architecture generalizes beyond the calibration corpus; protects against Risale-i-Nur-specific over-fit.

- **What:** Classification work — per-element provenance (the prior canonical-format finding's INVALIDATED-FOR-V0.2 commitment), per-span language identification, the 7 schema policies.
  - **Gate:** condition-bound — minimal-intake tested in production AND translation quality empirically requires classification.
  - **Why (if revived):** the 7 schema policies are the canonical classification roadmap (per the original intake-concepts finding's Decision 4); per-element provenance is the load-bearing dimension the prior canonical-format finding identified; both are deferred under the scope narrowing but preserved as the revival roadmap.

- **What:** Per-corpus configuration UI in the Mac app.
  - **Gate:** observable — when the Category 8 extensions API ships AND a second corpus enters the project.
  - **Why (if revived):** corpus selection becomes user-facing only when multiple corpora exist.

---

## Reasoning

This section explains why the recommended set holds against the alternatives that were generated and considered.

### What survived adversarial scrutiny

**The "structural, not semantic" scope-line principle.** The principle provides an operational test-question that decides per-operation verdicts. Adversarial testing surfaced that the test is operational across the v0.2 set with explicit gray-zone adjudication paths for edge cases (parallel-column verse vs table in non-Latin scripts; convention-dependent typographic markers). The principle is decidable enough for v0.2 operation; the gray-zone path lives in the Open Questions section.

**The 8-category recommended set.** Each category corresponds to a distinct preprocessing concern (byte-consistency; translation-quality-floor; paratext; provenance; structure; format-specific quirks; quality flags; corpus extensions). The categories are internally cohesive and inter-category coupling is loose because the scope-line principle keeps boundaries clean.

**The two-layer corpus model.** Separating generic preprocessing (Categories 1–7) from calibration-corpus-tuned extensions (Category 8) preserves both the generic-project commitment and the empirical knowledge about Risale-i Nur's structural vocabulary. The plugin architecture analogy (Pandoc's reader + filter + writer layers) is well-established.

**Source-driven hierarchy preservation up to HTML5 h1–h6.** Honors the user's depth-4 instinct as empirical mean while generalizing to the W3C-spec ceiling. The policy is permissive-not-restrictive: most sources will not exceed h4, but the architecture accepts up to h6.

**EPUB-first plus PDF-with-OCR-fallback format priority.** EPUB intake is significantly cheaper for well-formed EPUBs (empirically verified via the Asa-yı Musa EPUB analysis); PDF-with-OCR handles sources that exist primarily in PDF (justified by the broken-bidi Arabic in the Asa-yı Musa PDF and the image-only Arabic in the Muhakemat PDF). For EPUB-from-PDF cases (low-quality EPUBs that inherit PDF problems), intake detects the EPUB quality and routes to the PDF processing path.

**The translation-quality-floor sub-category.** Naming the sub-category clarifies which operations are load-bearing for translation quality even in the minimal-intake mode. Sentence segmentation specifically is load-bearing for translation chunking (sentences are the chunk boundary unit) and for cross-version consistency, not for raw LLM input — LLMs handle un-segmented text fine, but chunking and consistency require sentence boundaries.

**Quality flags as informational, not corrective.** Preserves user agency over content (truncation may be intentional; duplicate-content may be a refrain; orphan-content may be a drop-cap). Auto-correction destroys decisions the user (or the human reviewer) should make.

**The `extends:` relationship label.** Distinct from `refines:` (no cell of the prior architecture changes — Categories 1 + 3 of this set ARE the prior NFC + paratext operations unchanged), from `supersedes:` (nothing is replaced), and from `corrects:` (the prior was not wrong, just incomplete on this dimension).

### What was killed and why

**Per-element provenance attribution** (the prior canonical-format finding's new load-bearing dimension). Killed for v0.2 because attributing provenance requires per-element classification (which class — OCR-recovered? hand-corrected? text-layer? derived? — does this element belong to?), which crosses the scope-line into semantic territory. The revival path is preserved: when minimal-intake is tested in production and translation quality empirically requires classification, per-element provenance returns. This is the load-bearing reversal of the prior finding.

**Per-span language identification with `lang=` tagging.** Killed via the scope-line. The LLM-based translator handles mixed-script text correctly without per-span tags (per the recent conversation that established the scope narrowing).

**The 7 schema policies** (the original intake-concepts finding's Decision 4). Killed for v0.2 via the scope-line (each policy detects cultural or linguistic role; semantic). Revival path preserved in DEFERRED 3.

**Voice marking, formulaic opening detection, embedded poetry classification** (other 7-policy operations). Same reason; same revival path.

**Depth-4 as absolute cap.** Killed in favor of source-driven up-to-h6. The user's instinct is honored as empirical mean for literary texts; the cap is principled (W3C HTML5 ceiling) not arbitrary.

**PDF-only or EPUB-only v0.2.** Killed in favor of format-priority commits to both with rank order.

**Drop-everything-corpus-specific.** Killed in favor of the two-layer corpus model.

**Generative-only output** (the surfacing-style breadth-first brainstorm without commitment). Killed in favor of the categorized recommended set; surfacing already provided the breadth (153 candidates in 14 categories).

**Tokenization at intake.** Killed — translate-stage's job. Sentence segmentation is at intake; further tokenization for LLM context-packing is downstream.

**Per-translation-output format expansion** (initialism expansion; date / number normalization). Killed — publishing-stage or translate-stage preparation, not intake preprocessing.

### Contradictions reconciled across upstream disciplines

The articulation surfaced two open dimensions: (1) decision-mode (generative brainstorm vs commit-to-recommended-set vs probe-the-boundary vs evaluate-only-boundary-detection vs cost-value-2D-map), and (2) scope-of-preprocessing (minimal vs ambitious). Sensemaking adjudicated both: decision-mode = commit-to-categorized-recommended-set (the WHY-axis included "scope-setting for v0.2 engineering" which generative-only does not serve); scope-of-preprocessing = minimal-intake-aligned (respects the recent scope narrowing) but with translation-quality-floor named as a sub-category to clarify what's load-bearing within minimal scope.

Surfacing's 153 candidates were partitioned via the scope-line principle into the 8 in-scope categories and the rejected-for-v0.2 set. The depth-4 instinct from the user was generalized to source-driven up-to-h6. The format-mix unknowable was committed via EPUB-first + PDF-fallback. The cross-corpus tension was resolved via the two-layer model.

Critique surfaced refinements (wording soften on scope-line decidability; letter-spaced un-spacing reclassification; sentence-segmentation chunking-rationale clarification; LRM/RLM addition to zero-width stripping; script-specific punctuation preservation; h6 ceiling permissive caveat; EPUB-first well-formed-only qualification; EPUB-from-PDF routing; per-element-provenance reversal explicit; Decision 4 wording tightened; transition-plan additions MUST 5 + MUST 6 + MUST 7; three new open questions). All refinements are integrated into this finding's body.

---

## Open Questions

### Monitoring

The v0.2 calibration prototype against the Asa-yı Musa fixture corpus (per the test-case MUST) will produce the first empirical answer to several questions: whether the hierarchy-inference algorithm correctly detects Mukaddeme / Mes'ele markers; whether the sentence-segmentation library handles Turkish abbreviations correctly; whether the EPUB-from-PDF detection heuristics fire correctly. Observable after the calibration prototype completes.

### Blocked

The Category 8 extensions API design (per COULD 1) cannot be finalized until a second corpus enters the project. v0.2 operates with a hardcoded Risale-i Nur extension.

The cross-corpus validation (per DEFERRED 2) cannot proceed until 2+ corpora are in the project.

### Research Frontiers

**Multi-volume document handling.** Risale-i Nur Külliyat is a multi-volume work (Sözler; Mektubat; Lem'alar; Şualar; Mesnevi-i Nuriye; etc.). Each volume may be a separate EPUB or PDF; v0.2 handles single-volume; multi-volume composition (cross-volume references; inter-volume hierarchy; single canonical for the whole collection vs per-volume canonicals) needs design. Revival trigger: observable — project ingests a multi-volume work.

**Intake-output versioning.** When the same source is re-intaken after a preprocessing operation's spec changes, the new canonical HTML5 output may differ from the prior. How is this versioned? Stable IDs across re-intakes for sections, paragraphs, footnotes? Diffable canonical between versions? Revival trigger: observable — when a preprocessing op's spec changes and existing intake outputs need re-derivation.

**EPUB-quality detection heuristics.** The EPUB-from-PDF detection cited in the format-priority section needs empirical calibration. Which combination of signals (OCR artifacts in text; flat-h1; minimal CSS; mid-word hyphens; broken-bidi text-layer) is reliable? Revival trigger: observable — when an EPUB-from-PDF source is encountered.

**Cross-corpus generalization of the scope-line principle.** Does "structural, not semantic" hold for Talmud apparatus criticus, Vedic texts, Christian patristic editions, or modern academic books? The principle's gray-zone path may need extending. Revival trigger: cross-corpus validation work (DEFERRED 2) commences.

### Refinement Triggers

**The scope-line principle re-opens if** any of the following observable conditions fire: (a) a new gray-zone operation surfaces during v0.2 engineering and the test gives a genuinely ambiguous verdict that cannot be adjudicated case-by-case; (b) translation quality empirically suffers from operations the principle deferred (specifically per-element provenance or per-span lang= tagging); (c) the LLM-based translator's mixed-script handling proves inadequate for theological texts.

**The depth policy re-opens if** the hierarchy-inference algorithm over-promotes (false positives on bold-centered standalone lines that are not actual sub-headings) or under-promotes (missed Mukaddeme/Mes'ele markers due to formatting variance). Empirical evidence from v0.2 calibration testing.

**The format priority re-opens if** EPUB-from-PDF cases become common in the project's source-mix and the EPUB-from-PDF detection heuristics prove unreliable. Empirical observable.

**The translation-quality-floor sub-category boundary re-opens if** v0.2 production evidence shows that a Category 1 operation is genuinely load-bearing for translation quality (promote to Category 2) or that a Category 2 operation is only byte-consistency (demote to Category 1).

**The two-layer corpus model re-opens if** the formal Category 8 extensions API design (COULD 1) surfaces a structural reason the two-layer model is inadequate — for example, if corpus extensions need to compose with each other in ways the opt-in single-extension model does not support.

**The `extends:` relationship label re-opens if** future findings need to identify per-element provenance as a re-committed load-bearing dimension — the revival of per-element provenance would shift the relationship semantics.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
u said 

NFC normalization picks the canonical composed form (U+015F for ş, never U+0073 + U+0327) so that the same visible text always has the
  same bytes. Standard one-pass operation; Python's unicodedata.normalize('NFC', text) does it. Should run once on intake before anything
  else.

  Paratext stripping
  
  "Paratext" is the publishing term for everything in a book that is not the body content. Includes:

  - Running headers — the book title or chapter title repeated at the top of every page
  - Running footers — same, at the bottom
  - Page numbers — folios
  - Catchwords — older printing convention: the next page's first word printed at the bottom of the current page
  - Section markers / editorial boilerplate — "[continued]" / "[end of chapter]" insertions
  - Publisher metadata — copyright lines printed at chapter starts in some editions
  
  The problem at intake: PDF extractors don't know body from paratext. pdftotext walks the page geometrically and emits everything as a
  stream. So you get garbage like: 

  …ve bu hakikat o kadar açıktır ki herkes kabul eder.
     Asa-yı Musa
     47
     Bu nokta-i nazardan bakıldığında…

  — where "Asa-yı Musa" is the running header and "47" is the page number, both wedged in the middle of a sentence that should have run
  continuously. The body text reads as …herkes kabul eder. Bu nokta-i nazardan bakıldığında… once paratext is stripped.


i agree we should have these 2 steps, but maybe also we should detect natural sementic boundaries of the text? for example new chapter or subchapter or subsubchapter subsubsubchapter (this is deep enough i think)

and what other preprocessing operations cna be think of ? be creative
```

</details>
