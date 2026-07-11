# Innovation — intake preprocessing operations

## User Input

Source: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/_branch.md`. Upstream outputs: `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md`.

Production-task mode: Decomposition's 12 pieces (P1-P12) are the seed. Innovation generates per-piece substantive content. Meta-decision pieces (Piece-Level Inversion required): P2, P3, P6, P7, P10.

---

## Phase 1 — Seed / Methodology-Mode Consideration

**Inherited methodology mode:** **Standard default** (4G+3F balanced; elaborate the committed direction; produce ship-ready content).

**Alternative mode considered:** **Generator-weighted exploration** (maximize candidate breadth).

**What follows under the alternative:** Innovation would surface additional preprocessing operations beyond surfacing's 153 candidates — but sensemaking already adjudicated breadth via 7 perspectives; further breadth without commitment would not serve the decision-mode commitment (categorized recommended set) the inquiry settled on.

**Decision:** **Standard default.** Piece-Level Inversion at the 5 meta-decision pieces (P2, P3, P6, P7, P10) provides contrarian surface at appropriate granularity.

`Methodology-mode-alternative-marked-inapplicable: Sensemaking's Phase 2 ran 7 perspectives including Frame-exit Completeness + Phase/Calibration-State; further generator-weighted breadth would duplicate that adjudication. Piece-level Inversion at 5 meta-decision pieces provides the contrarian surface.`

---

## Phase 2 — Generate (per piece)

### P2 (META-DECISION; FIRST per dependency order) — Scope-line principle + Decision-mode

**Principal candidate (content):**

> **The load-bearing scope-line principle for v0.2 intake preprocessing: "structural, not semantic."**
>
> **The operational test-question:** for any candidate operation, ask — *"Does identifying this require knowing what cultural, linguistic, or domain-specific role it plays?"* If YES → the operation is **semantic** (classification; OUT per the recent scope narrowing "leave content unclassified; trust the LLM"). If NO → the operation is **structural** (preprocessing; IN).
>
> **Worked applications of the test:**
> - Detecting that an `<aside>` element exists at body-end with a back-reference `<a href="#fn1">` to a body anchor → NO knowledge of cultural role required → STRUCTURAL → IN.
> - Tagging that the `<aside>` contains "Said Nursi's marginalia (hashiye)" → YES, requires knowing Risale-i Nur's apparatus tradition → SEMANTIC → OUT.
> - Detecting that a span is in Arabic script (Unicode range U+0600–U+06FF) → arguably structural (script identification); but **emitting `lang="ar"` per the prior conversation** crosses into semantic role-tagging → OUT.
> - Detecting that an opening paragraph contains the Bismillah verse and tagging it `class="formulaic-opening"` → YES, requires knowing the verse's tradition role → SEMANTIC → OUT.
> - Detecting that a verse-block is line-broken with two parallel lines → NO cultural knowledge required (just shape detection) → STRUCTURAL → IN; emit as `<figure>` containing `<blockquote>` with `<p>` per line; DO NOT classify as "Mevlana couplet" or "embedded poetry" — those are semantic.
>
> **Decision-mode commitment:** this finding's deliverable is a **categorized recommended v0.2 preprocessing set** organized by 8 categories, with per-operation verdicts driven by the scope-line principle and per-rejection rationale citing the scope-line. Surfacing's 153 candidates serve as the design-space backing; rejected items appear in P9 with structural reasons.
>
> **Relationship label:** `extends:` `devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/finding.md`. Distinct from `refines:` (no prior cell changes) and `supersedes:` (nothing prior is replaced); this inquiry **adds** an articulated scope-line principle plus 6 additional categories around the prior's NFC + paratext baseline.

**Mechanism log:**
- *Combination:* recent scope narrowing × surfacing's G10 candidate × project_scope memory's generic framing → "structural, not semantic" as a load-bearing test.
- *Lens Shifting:* lens = "what's the operational test that decides verdicts?" Surfaces the test-question.
- *Constraint Manipulation (ADD):* "classification deferred" → preprocessing scope narrows; principle becomes load-bearing.
- *Constraint Manipulation (REMOVE):* removed "intake must classify everything" → preprocessing-only is sufficient.
- *Absence Recognition (patch):* prior intake spec did not have an articulated scope-line.
- *Absence Recognition (redesign):* if intake were designed today from scratch, the scope-line would be in the spec from day 1.
- *Domain Transfer:* DOM-vs-CSS distinction (structure vs presentation) in web standards is analogous to structural-vs-semantic distinction here.

**Piece-Level Inversion (required — P2 fires property (i) relationship-label + (ii) framing-semantic + (iii) lesson-vocabulary):**

> *Inversion-candidate:* what if the scope-line is wrong — classification IS preprocessing, and the recent scope narrowing was premature?
>
> *What follows under the inversion:* intake performs the 7 schema policies' detection; per-element provenance and per-span lang= tagging happen at intake. Categories 1-7 expand to include classification operations.
>
> *Why rejected:* (a) the scope narrowing was a structurally-grounded decision (LLM handles per-span language correctly; per-policy classification is expensive heuristic work whose value is unclear without v0.2 testing first). (b) Including classification in v0.2 would massively expand engineering scope and delay ship. (c) The recent conversation explicitly walked back per-span lang= tagging because the LLM-based translator handles mixed-script text correctly. (d) Classification can be added in a later version without disturbing v0.2's preprocessing layer (additive extensibility).
>
> *Intervention-shape Inversion check:* P2 commits to the `extends:` relationship-label and the framing-semantic "structural, not semantic." Alternatives from the Intervention-Shape Vocabulary: `refines:` (no — no prior cell changes); `supersedes:` (no — nothing replaced); `corrects:` (no — prior wasn't wrong, just incomplete); REVERT-REGRESSION (n/a). `extends:` is structurally accurate.
>
> Verdict on Inversion: **rejected** — scope narrowing is principled; classification belongs at a later version; `extends:` label is structurally accurate.

**5-test:** Novelty (operational test-question for scope-line is new for this project); Scrutiny (survives Inversion + critique-style adversarial test); Fertility (spawns per-operation verdicts in P4-P9; spawns hierarchy-inference adjudication in P6; spawns rejection rationales in P9); Actionability (engineer can apply the test-question per operation); Mechanism independence (Combination + Constraint Manipulation + Absence Recognition + Domain Transfer all converge on "structural, not semantic"). PASS.

---

### P3 (META-DECISION + CONTENT) — Two-layer corpus model + Category 8 content

**Principal candidate (content):**

> **The two-layer corpus model.** v0.2 intake preprocessing has two architectural layers:
>
> 1. **Generic core (Categories 1-7):** operations that work on any source corpus regardless of its specific structural vocabulary. NFC normalization, paratext stripping, sentence segmentation, source-format metadata extraction, generic structural detection — none require knowing what corpus the document came from.
> 2. **Calibration-corpus extensions (Category 8):** operations that depend on knowing the source corpus's specific structural vocabulary. These are **opt-in** extensions that activate only when corpus context is named at intake-time (e.g., `--corpus risale-i-nur`). They are NOT part of the generic flow.
>
> **The test for which layer an operation belongs to:** ask *"Does this operation depend on knowing the corpus-specific structural vocabulary (named markers, numbering conventions, paratext patterns) of a particular text tradition?"* If YES → Category 8. If NO → Categories 1-7.
>
> **Category 8 operations (calibration-corpus = Risale-i Nur tuned):**
>
> 1. **Letter-spaced-emphasis un-spacing.** Detects markers like "T e n b i h" (where the source used letter-spacing as typographic emphasis) and joins them. Regex shape (Turkish alphabet): `\b[A-ZÇĞIİÖŞÜ](\s[a-zçğıiöşü])+\b` matching standalone letter-spaced words; collapse spaces. Caveat: false-positives possible (initialisms); tune against the calibration corpus's actual letter-spacing patterns.
> 2. **Risale-i Nur structural-marker keyword recognition.** Detects the words `Mukaddeme` (preamble) / `Mes'ele` (numbered topic, with Turkish ordinals `Birinci` / `İkinci` / `Üçüncü` / etc.) / `Hâtime` (conclusion) / `Tenbih` (note) / `Bismillah` when they appear at section-opener positions (bold + centered + standalone line) and promotes them to sub-headings (`<h2>` / `<h3>`) in the hierarchy-inference for flat-h1 sources (see P6).
>    - Detection pattern: bold + center-aligned + standalone short-line content matching the keyword regex.
>    - This is structural-detection-with-corpus-vocabulary — not semantic role tagging (which would require knowing what "Mukaddeme" means in Risale-i Nur's theology). It's keyword-position detection.
> 3. **Other Risale-i Nur-specific patterns** (deferred to Category 8 extension API design): hashiye footnote conventions; Mevlana attribution patterns in verse-blocks; Bismillah position at section start.
>
> **Attachment to v0.2:** Category 8 is an **opt-in extension layer**. At intake-time, the user (or intake config) names the corpus; intake loads the corresponding extension's operations. When no corpus is named, Categories 1-7 run alone. This honors the `project_scope` commitment (generic project; Risale-i Nur as calibration corpus, not purview) while preserving the empirical knowledge that motivated the design.

**Mechanism log:**
- *Combination:* project_scope memory's generic framing × Risale-i Nur's specific structural markers → two-layer model.
- *Absence Recognition (patch):* no prior intake spec had a corpus-extension layer.
- *Absence Recognition (redesign):* if intake were designed for multi-corpus from start, two-layer would be the obvious architecture.
- *Domain Transfer:* plugin architectures from software ecosystems (core + opt-in plugins) — directly imported.
- *Constraint Manipulation (ADD):* "corpus-tuned ops cannot pollute generic core" → two-layer architecture becomes mandatory.
- *Constraint Manipulation (REMOVE):* "all ops are generic" removed → Category 8 layer becomes available without violating generic-project commitment.

**Piece-Level Inversion (required — P3 fires property (ii) framing-semantic):**

> *Inversion-candidate:* what if there's no two-layer model — all operations live in one tier?
>
> *What follows under the inversion:* (a) generic core is "polluted" with Risale-i-Nur-specific ops, violating the generic-project commitment; OR (b) all corpus-specific ops are dropped entirely, losing the empirical knowledge that motivated their inclusion. Either choice has structural cost.
>
> *Why rejected:* the two-layer model preserves both invariants: generic-project commitment AND corpus-specific knowledge. Single-tier monolithic forces a false dichotomy. The plugin architecture analogy is well-established in software (e.g., Pandoc itself uses readers + filters + writers in distinct layers). Two-layer is structurally sound.
>
> *Intervention-shape Inversion check:* P3 commits to architectural separation (ADD-CONTENT shape — adding the corpus-extension layer). Alternative shapes: REORGANIZE-WITHOUT-ADDING (no — adding a layer is content); ADD-DIMENSION (close, but the layer is content, not an evaluation dimension); REPAIR (n/a — nothing to repair). ADD-CONTENT is structurally accurate.
>
> Verdict: **rejected** — the two-layer model preserves project_scope while honoring calibration-corpus knowledge.

**5-test:** PASS — concrete Category 8 ops with detection patterns; opt-in semantics specified; alignment with project_scope verified.

---

### P4 (CONTENT) — Categories 1+2 — Foundational tier + Translation-quality-floor

**Principal candidate (content):**

> **Category 1 — Foundational normalization** (always; format-agnostic; byte-consistency):
>
> | Operation | Python implementation | Notes |
> |---|---|---|
> | NFC Unicode normalization | `unicodedata.normalize('NFC', text)` (stdlib) | Run once, before anything else |
> | Whitespace normalization | `re.sub(r'[ \t]+', ' ', text)` per-line + LF newlines | Preserve paragraph breaks (double-newline) |
> | Zero-width character removal | `re.sub(r'[​-‍﻿]', '', text)` | U+200B-D + BOM |
> | Soft hyphen removal | `text.replace('­', '')` | Breaks search; safely strippable |
> | Quotation mark normalization | Map to project canonical (curly Unicode: `"` `"` `'` `'`) | Pandoc's `--smart` is the lever |
> | Dash normalization | Preserve em (—) / en (–) / hyphen (-) semantic distinction; convert minus / figure-dash to hyphen | |
> | Ellipsis normalization | Three dots → U+2026 single char | Pick one canonical |
> | Ligature decomposition | Targeted map: ﬁ → fi; ﬂ → fl; ﬃ → ffi; ﬄ → ffl; ﬅ → ft; ﬆ → st | NFKC over-normalizes (eats compatibility chars); use targeted map |
> | Broken-Unicode detection | Try-decode with `errors='strict'`; flag failures | Doesn't auto-correct; emits flag to Cat 7 |
>
> **Category 2 — Translation-quality-floor** (always; format-agnostic; load-bearing for translation):
>
> | Operation | Python library | Notes |
> |---|---|---|
> | Sentence segmentation | `spacy` (with `xx_sent_ud_sm` multi-lang model) OR `nltk.tokenize.PunktSentenceTokenizer` | Calibrate against Turkish abbreviations; spacy's xx_sent_ud_sm handles multi-language docs |
> | Paragraph boundary detection | Double-newline + indent heuristic | Re-paragraphs collapsed text from PDF |
> | Document-level language identification | `langdetect.detect_langs(text)` OR `polyglot.detect.Detector` | Returns BCP 47 codes; informs translate-stage source-language config |
> | Hyphenation-at-line-break repair | `re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)` | Caveat: don't merge intentional line-breaks (verse, lists) — apply only in body paragraphs |
> | Mojibake repair | `ftfy.fix_text(text)` | Handles UTF-8 misread as latin1; smart-quote glyph confusion; mojibake patterns from common PDF extraction errors |
>
> **The translation-quality-floor sub-category** names operations that are load-bearing for LLM translation quality even when intake performs no classification. These are NOT optional for v0.2 — they are the "minimum floor" of preprocessing that makes intake's output translation-ready.
>
> **Semantic distinction between Categories 1 and 2:**
> - Category 1 = byte-consistency (downstream tools see consistent bytes regardless of source-format quirks).
> - Category 2 = translation-quality-load-bearing (LLM translation quality improves with these operations even without classification).

**Mechanism log:**
- *Combination:* operations × Python library references + standardized regex patterns.
- *Absence Recognition (patch):* some markdown converters skip soft-hyphen stripping or don't normalize quote forms.
- *Domain Transfer:* `ftfy` (mojibake repair) and `spacy/nltk` (sentence segmentation) are mature NLP libraries imported directly.
- *Constraint Manipulation (ADD):* "must be format-agnostic" → confirms Cat 1+2 placement (vs Cat 6 format-specific repair).

**5-test:** PASS — every operation has a concrete Python recipe; library references are real (stdlib `unicodedata`; PyPI `ftfy`, `spacy`, `nltk`, `langdetect`); semantic distinction articulated.

---

### P5 (CONTENT) — Categories 3+4 — Paratext stripping + Source-format metadata + Provenance

**Principal candidate (content):**

> **Category 3 — Paratext stripping** (always; established baseline + extensions):
>
> | Operation | Detection approach | Notes |
> |---|---|---|
> | Running headers / footers | Detect by repetition across pages (PDF) or `<header>` / `<footer>` tags (EPUB) | PDF-specific; EPUB cleanup is usually trivial |
> | Page numbers / folios | Regex `^\s*\d+\s*$` standalone digit lines between paragraphs (PDF); ignore in EPUB | |
> | Catchwords | Older typesetting; rare; regex over end-of-page line that duplicates next-page start | Often absent in modern editions |
> | Editorial boilerplate | Regex `\[continued\]` / `\[end of chapter\]` and variations | |
> | Publisher metadata at chapter starts | Heuristic — known publisher signatures; usually a known footer pattern | |
> | Blank pages | Detect empty page content; skip | |
> | Decorative ornaments | Regex `\*\s*\*\s*\*` (asterism); known dingbat Unicode (U+2766, U+273D etc.) | Could be preserved as `<hr/>` if section-break-signal; design choice |
> | Watermarks / "scanned by" inserts | Source-specific known strings (`scanned by archive.org`); regex | |
> | Library / acquisition stamps | Usually visual; text-extractable variants regex'd; otherwise flag | |
>
> **Category 4 — Source-format metadata + provenance** (always; cheap; document-level):
>
> | Operation | Implementation | Notes |
> |---|---|---|
> | Source-format detection | File extension + magic bytes (`mimetypes.guess_type` + `python-magic`) | First step of intake |
> | Source-file path | `os.path.abspath(input_path)` | Verbatim |
> | Source-file SHA-256 checksum | `hashlib.sha256(file_bytes).hexdigest()` | Enables idempotency + dedup |
> | Intake-timestamp | `datetime.utcnow().isoformat()` | UTC; ISO 8601 |
> | Intake-tool-version | Hardcoded version string from project metadata | |
> | Title / author / publication date / publisher | Extract from source metadata block | EPUB: parse OPF `<metadata>`; PDF: `pdfinfo` / `pypdf.PdfReader().metadata`; Word: `python-docx` `core_properties` |
> | Source-language declaration | EPUB: `<dc:language>`; PDF: `/Lang` in document catalog; auto-detect fallback (Category 2 L3) | |
> | Source-format metadata pass-through | Preserve raw OPF / `/Info` / `docProps` blocks as JSON sidecar | Verbatim preservation for audit |
>
> **The Category 4 output** writes into the canonical HTML5's `<head>` as `<meta>` tags AND into the sidecar JSON metadata file (per the Category 7 flag-exposure decision in P8).

**Mechanism log:**
- *Combination:* paratext patterns × source-format conventions + provenance items × Python implementation libraries.
- *Absence Recognition:* page-number stripping is universally present; running-header detection less universally implemented; we make both explicit.

**5-test:** PASS — every operation has concrete detection / extraction approach; library refs are real (`mimetypes`, `python-magic`, `hashlib`, `datetime`, `pypdf`, `python-docx`).

---

### P6 (CONTENT + META) — Category 5 Structural detection + Depth-of-boundary policy

**Principal candidate (content):**

> **The depth-of-boundary policy:** **source-driven hierarchy preservation up to HTML5's h1-h6 ceiling.** When the source format encodes heading hierarchy (XHTML / HTML / Word with style-mapping), preserve up to depth 6 (W3C HTML Living Standard's ceiling). When the source uses flat h1 only (the Asa-yı Musa EPUB case empirically verified), perform **hierarchy inference** using body markers to promote sub-section indicators to h2/h3. No absolute depth cap below 6.
>
> **Hierarchy-inference algorithm sketch (for flat-h1 sources):**
> 1. Detect bold / centered / standalone-line markers in body text.
> 2. Cluster markers by frequency and position.
> 3. If a marker matches a Category 8 corpus-extension keyword (e.g., Mukaddeme, Mes'ele), promote per the extension's depth-mapping.
> 4. If no corpus-extension is active, promote bold-centered standalone lines to h2 by default (conservative one-level promotion); leave deeper inference to corpus extensions.
> 5. Wrap promoted sections in `<section>` containers.
>
> **Category 5 — Structural detection operations** (always; "structural, not semantic" core):
>
> | Operation | Approach | Scope-line verification |
> |---|---|---|
> | Heading hierarchy preservation (h1-h6) | Read source headings; map to HTML5 h1-h6 | Structural (where the heading lives) |
> | Hierarchy INFERENCE for flat-h1 sources | Per algorithm sketch above | Structural (position + frequency detection); semantic role tagging deferred |
> | List structural detection (numbered / bulleted) | Regex over markdown / `<ul><ol>` in XHTML / `<w:numPr>` in Word | Structural |
> | Table structural detection | Source-format dependent (HTML `<table>`; Word table; PDF column extraction) | Structural — preserve rows × cells; do not classify cell content semantically |
> | Quote-block structural detection (block vs inline) | Indented blocks → `<blockquote>`; `>` markers in markdown; Word indent style | Structural — does not tag voice or citation role |
> | Verse-block structural detection (line-broken; centered) | Multiple `<br>` tags or line-broken paragraphs → `<figure>` + `<blockquote>` | Structural — does not classify as poetry policy |
> | Footnote / endnote STRUCTURAL extraction | `<aside>` at body-end with `id` + back-reference `<a href="#fn1">` | **Structural — positional + relational; does NOT tag as marginalia / hashiye (semantic, OUT)** |
> | Cross-reference structural preservation | Preserve `href` + matching `id`; do not resolve citation | Structural |
> | Figure / illustration caption | `<figure>` + `<figcaption>` | Structural |
> | Drop-cap normalization | Detect large initial capital (CSS class or HTML pattern); merge with following text into normal paragraph flow | Structural |
>
> **The user's depth-4 instinct is honored** as the empirical mean for literary texts (Asa-yı Musa, the calibration corpus's primary EPUB, doesn't exceed h4 in any practical hierarchy-inference) — and **generalized** to source-driven-up-to-h6 because the HTML5 spec ceiling (h6) is the principled cap; depth-4 is descriptive, h6 is prescriptive.

**Mechanism log:**
- *Combination:* HTML5 h1-h6 spec × source-format hierarchy conventions × hierarchy-inference heuristics → algorithm sketch.
- *Absence Recognition:* no prior intake spec defined hierarchy-inference for flat-h1 sources; the Asa-yı Musa EPUB empirically motivates it.
- *Domain Transfer:* tree-grammar parsing from compiler design — structural parsing without semantic interpretation.
- *Constraint Manipulation (ADD):* "depth ceiling = HTML5 h6" → bounds the policy; respects HTML5 spec.
- *Constraint Manipulation (REMOVE):* "absolute depth cap below 6" removed → policy adapts to source.

**Piece-Level Inversion (required — P6 fires property (iv) evaluation-criterion):**

> *Inversion-candidate:* what if hierarchy doesn't matter — flat structure is sufficient for translation?
>
> *What follows under the inversion:* intake doesn't infer hierarchy; flat-h1 sources stay flat; structural detection's hierarchy-inference is dropped.
>
> *Why rejected:* (a) Empirical evidence — Asa-yı Musa EPUB has flat h1 but body markers (Mukaddeme, Mes'ele) clearly indicate sub-structure; preserving this structure helps translation chunking and citation. (b) The "structural, not semantic" principle includes structural-position detection; flat sources lose addressable sub-units. (c) Hierarchy inference is cheap (regex + clustering); the cost-benefit favors inference.
>
> *Intervention-shape check:* P6 commits ADD-CONTENT (the depth policy + hierarchy-inference algorithm are added). Alternatives: ADD-TEST (no — depth policy is content, not a test); REORGANIZE-WITHOUT-ADDING (no — policy is new). ADD-CONTENT is structurally accurate.
>
> Verdict: **rejected** — hierarchy inference is cost-effective and aligned with the structure-preservation quality target (Decision 2, original intake-concepts finding).

**5-test:** PASS — concrete algorithm; empirical evidence cited; scope-line verified per-operation; depth policy honors user instinct while being principled.

---

### P7 (CONTENT + META) — Category 6 Format-specific repair + Format-priority commitment

**Principal candidate (content):**

> **The format-priority commitment:** **EPUB-first + PDF-with-OCR-fallback for v0.2.** Word and plain-text are DEFERRED to future format additions (per the dependency-gating in P11).
>
> **Why EPUB-first:** EPUB intake is significantly cheaper than PDF intake. The Asa-yı Musa EPUB (`writer2epub` 1.1.17, 2012) has: clean Unicode Arabic in text-layer (no broken-bidi); italic/bold preserved as `<em>`/`<strong>`; footnote structure intact; OPF metadata extractable; flat h1 hierarchy (handled by P6 hierarchy-inference). No OCR needed. No bidi-fix needed. Categories 1-5 + 6's EPUB ops produce ready-for-translation canonical HTML5.
>
> **Why PDF-with-OCR-fallback:** the Asa-yı Musa PDF has broken-bidi Arabic (letters in display order); the Muhakemat PDF has image-only Arabic (the Arabic was pasted as bitmap images in the Word source). PDF intake without OCR fallback misses these entirely; with OCR fallback, intake recovers Arabic spans inline.
>
> **Category 6 — Format-specific repair operations:**
>
> **EPUB (v0.2 primary):**
>
> | Operation | Approach |
> |---|---|
> | Spine reassembly | Parse `content.opf`; read `<itemref>` order in `<spine>`; concatenate XHTML content documents in spine order |
> | CSS-presentation extraction | Parse CSS; map `class="bold"` / `font-weight:bold` styling → `<strong>`; map `class="italic"` → `<em>`; remove other presentation-only classes |
> | Heading-level inference | When source has only `<h1>` tags, invoke P6 hierarchy-inference algorithm |
> | OPF metadata extraction | Parse `<metadata>` block; extract `<dc:title>`, `<dc:creator>`, `<dc:language>`, `<dc:date>`, `<dc:identifier>`, `<dc:description>` |
>
> **PDF (v0.2 fallback):**
>
> | Operation | Approach |
> |---|---|
> | Mid-word hyphen repair | Regex `(\w+)-\n(\w+)` in body paragraphs; do NOT merge in verse / lists |
> | Column-order repair | Use `pdftotext -layout` or `pdf2htmlEX` to preserve geometry; reassemble in reading order |
> | Bidi-fix for broken-bidi Arabic | Detect Arabic Unicode runs (U+0600–U+06FF); check bidi correctness (RTL ordering); if broken, route to OCR fallback for the broken region |
> | Italic / bold recovery | Use `mutool draw -F text` or `pdf2htmlEX` (preserves style annotations); apply to text-layer extraction |
> | OCR fallback | `OCRmyPDF` with Tesseract `--lang ara+tur`; for image-only Arabic regions (the Muhakemat case), replace with OCR text |
>
> **Word (DEFERRED to future v0.x):**
>
> | Operation | Approach |
> |---|---|
> | Style-mapping | Read `styles.xml`; map Heading 1-9 → `<h1>`-`<h6>`; "Normal" → `<p>`; preserve formatting runs as `<strong>` / `<em>` |
> | Run-merge | Consecutive runs with identical `<rPr>` → merge text |
>
> **Plain-text (DEFERRED to future v0.x):**
>
> | Operation | Approach |
> |---|---|
> | Encoding detection | Try UTF-8 → latin1 → cp1252 → `chardet` fallback; BOM-aware |
> | Line-ending normalization | CRLF → LF; preserve paragraph breaks |
>
> **Pandoc as architectural lever** (per Decision 5 of original intake-concepts finding): all format readers compose with Pandoc — EPUB reader, PDF reader (limited), HTML reader. Category 6 operations either run before Pandoc (e.g., PDF OCR fallback) or are realized via Pandoc reader features (EPUB heading mapping). The lever is preserved and strengthened.

**Mechanism log:**
- *Combination:* Pandoc format matrix × format-specific quirks × empirical evidence (Asa-yı Musa + Muhakemat) → per-format operation set.
- *Absence Recognition:* current Pandoc EPUB reader doesn't infer heading hierarchy from flat-h1 sources; we add this as an explicit Category 6 op.
- *Constraint Manipulation (ADD):* "EPUB-first" → bounds v0.2 scope; prioritizes lowest-cost format.
- *Constraint Manipulation (REMOVE):* "must support all 4 formats equally" removed → allows priority; deferral honors v0.2 ship discipline.

**Piece-Level Inversion (required — P7 fires property (iv) evaluation-criterion):**

> *Inversion-candidate:* what if PDF should be first instead, with EPUB as fallback?
>
> *What follows under the inversion:* v0.2 invests engineering effort in PDF bidi-fix + OCR fallback + italic recovery + column-order repair as the primary path; EPUB intake becomes secondary.
>
> *Why rejected:* (a) EPUB intake is significantly cheaper (no OCR, no bidi-fix, structure already encoded). (b) The calibration corpus has both PDF and EPUB available for at least one volume (Asa-yı Musa); EPUB is the cheaper path. (c) PDF intake is genuinely necessary for sources that exist only in PDF (e.g., Muhakemat's image-only Arabic) — making it FALLBACK preserves that necessity without prioritizing it over the cheaper EPUB path. (d) The format priority orders by per-format cost, not by source availability.
>
> *Intervention-shape check:* P7 commits to a priority ranking (ADD-CONTENT — the ranking is new content). Alternatives: REPAIR (no — nothing to repair); REORGANIZE (no — new content). ADD-CONTENT is structurally accurate.
>
> Verdict: **rejected** — EPUB-first + PDF-fallback honors per-format cost while preserving PDF necessity for image-only content.

**5-test:** PASS — per-format operations concrete; library references real (`OCRmyPDF`, `mutool`, `pdf2htmlEX`, `pdftotext`, `pypdf`, `python-docx`, `chardet`); format priority structurally grounded with empirical evidence.

---

### P8 (CONTENT) — Category 7 Quality / hygiene informational flags

**Principal candidate (content):**

> **Category 7 — Quality / hygiene informational flags** (always; informational, not corrective):
>
> | Operation | Detection approach | Flag emitted |
> |---|---|---|
> | Suspicious line-break | Regex over body `(\w+)-\n(\w+)` (mid-word) — but distinguish from Cat 2 hyphenation-repair which CORRECTS; this flags cases where correction is ambiguous | `suspicious-line-break` |
> | Truncation | Last paragraph ends without sentence-terminator (`.`, `!`, `?`, `…`) | `truncation` |
> | Document-completeness | Headings count × ToC entries count; footnote refs × footnote bodies; mismatch | `document-completeness-mismatch` |
> | Duplicate-content | SHA-256 over paragraph windows; flag duplicates above threshold | `duplicate-content` |
> | Orphan-content | Paragraphs with `len(text) < N` (e.g., N=10 chars) | `orphan-content` |
> | Confusables | Unicode confusables data (Cyrillic А vs Latin A); flag mixed-script suspect chars | `confusables-detected` |
> | Encoding-confidence | When `ftfy` reported changes OR `langdetect` confidence below threshold | `encoding-confidence-low` |
>
> **Flag exposure mechanism** (working assumption; MUST 4 in P11):
>
> - **Primary:** sidecar JSON file `<canonical>.intake-flags.json` next to the canonical HTML5 file. Schema:
>   ```json
>   {
>     "source": "/abs/path/source.epub",
>     "intake_timestamp": "2026-06-17T22:55:00Z",
>     "flags": [
>       {"code": "truncation", "severity": "warn", "context": "last paragraph ends mid-sentence at line 5234"},
>       {"code": "duplicate-content", "severity": "info", "context": "paragraph at line 245 matches paragraph at line 1342"}
>     ]
>   }
>   ```
> - **Alternative (mirror):** HTML5 `<head>` `<meta name="intake-flag" content="..."/>` blocks for in-document inspection.
>
> **Why informational, not corrective:**
>
> - **Truncation** could be auto-corrected (drop incomplete paragraph) but the truncation may be intentional (a quote that ends mid-thought, or a deliberate stylistic device). Auto-correcting destroys user agency over content.
> - **Duplicate-content** could be auto-deduplicated but may be intentional (a refrain in poetry, a deliberate echo). Auto-dedup destroys author intent.
> - **Orphan-content** could be auto-removed but a single-character paragraph might be a chapter-opening drop-cap that wasn't normalized properly, or a meaningful one-word emphasis.
>
> The informational-flag approach preserves user agency: intake reports what it detected; the user (or downstream tools, or the human reviewer) decides whether to act. This composes correctly with the "leave content unclassified; trust the LLM" scope narrowing — intake observes, the human (or LLM) interprets.

**Mechanism log:**
- *Combination:* quality patterns × informational-flag exposure schema.
- *Absence Recognition:* most intake pipelines either auto-correct (destroys agency) or silently drop (loses information); we surface a third path.
- *Constraint Manipulation (ADD):* "informational not corrective" → semantic distinction; preserves user agency.
- *Lens Shifting:* under "user agency" lens, flags become information not actions.

**5-test:** PASS — detection patterns concrete; schema specified; design choice (informational vs corrective) explicitly grounded.

---

### P9 (RELATIONSHIP) — Rejected candidates rationale

**Principal candidate (content):**

> Surfacing enumerated 153 candidates across 14 sub-regions. The following candidates are explicitly REJECTED for v0.2, each with structural reason:
>
> **Semantic-role-tagging candidates — REJECTED via scope-line principle ("structural, not semantic"):**
> - **Per-element provenance attribution** (`data-source` / `data-confidence` / `data-intake-pass` per element). Structural reason: per-element provenance requires deciding WHICH element class to attribute to (was this an OCR-recovered Arabic span? an editor's correction? a derived paragraph?). The classification IS the semantic role. Deferred per scope narrowing.
> - **Per-span language identification with `lang=` tagging.** Structural reason: emitting `<span lang="ar">` requires classifying which spans are non-main-language — that classification IS semantic. LLM-based translator handles mixed-script text correctly without per-span tags (per recent conversation).
> - **7-policy detection** (NonMainLangPartsPolicy / SourceApparatusPolicy / VoiceMarkingPolicy / ArchaicRegisterPolicy / HonorificsPolicy / FormulaicOpeningPolicy / EmbeddedPoetryPolicy from `SKILL/references/config/schemas.py`). Structural reason: each policy detects cultural / linguistic role; per scope-line principle, semantic; deferred.
> - **Voice marking** (author vs cited authority distinction). Structural reason: voice IS semantic role.
>
> **Depth-policy candidate — REJECTED via empirical principle:**
> - **Depth-4 as absolute cap** (the user's named instinct). Structural reason: replaced by source-driven up-to-HTML5-h6 policy in P6; depth-4 is honored as empirical mean for literary texts but not as absolute. The user's instinct ("this is deep enough I think") was hedged; P6 generalizes it principled.
>
> **Format-priority candidates — REJECTED via priority commitment:**
> - **PDF-only v0.2** (intake supports only PDF). Structural reason: EPUB intake is cheaper AND available for the calibration corpus's primary volumes (Asa-yı Musa EPUB analyzed); ignoring EPUB wastes the cheaper path.
> - **EPUB-only v0.2** (intake supports only EPUB). Structural reason: Muhakemat exists primarily as PDF with image-only Arabic; ignoring PDF + OCR fallback loses corpus access.
> - **Equal-priority all formats.** Structural reason: equal-priority forces equal investment in EPUB / PDF / Word / plain-text engineering for v0.2 ship; delays release without empirical justification.
>
> **Corpus-tuning candidate — REJECTED via two-layer model:**
> - **Drop-everything-corpus-specific** (eliminate Risale-i Nur-tuned operations entirely). Structural reason: would discard the empirical knowledge (hashiye structure; letter-spaced markers; named ordinals) that justified the inquiry's design. P3's two-layer model preserves this knowledge as Category 8 extensions without violating the generic-project commitment.
>
> **Decision-mode candidate — REJECTED via WHY-axis fit:**
> - **Generative-only output** (variant 1 from articulation; no recommendation commit). Structural reason: surfacing's 153-candidate enumeration already satisfied the generative-only need; the user's WHY-axis included "scope-setting for v0.2 engineering" which generative-only does not serve.
>
> **Stage-line candidates — REJECTED via stage scope:**
> - **Tokenization** (L6 from surfacing). Structural reason: translate-stage's job, not intake. Intake produces sentence-segmented text; tokenization for LLM input is downstream.
> - **Per-translation-output format expansion** (C16, C17 from surfacing — initialism expansion, date/number normalization). Structural reason: publishing-stage or translate-stage prep, not intake preprocessing.

**Mechanism log:**
- *Combination:* surfacing's rejected candidates × structural reason per rejection.
- *Constraint Manipulation (ADD):* "scope-line principle decides" → mechanically rejects classification ops.
- *Constraint Manipulation (REMOVE):* "must include everything user named" removed → allows principled rejection of depth-4-absolute and drop-corpus-specific.

**5-test:** PASS — every rejection structurally grounded; scope-line / empirical / priority / stage reasons articulated per candidate.

---

### P10 (META-DECISION + RELATIONSHIP) — Inherited Commitments Re-test

**Principal candidate (content):**

> This finding inherits commitments from two priors. The relationship-label is `extends:` (additive growth; nothing prior is changed or replaced).
>
> **Prior 1: `devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/finding.md`** (the post-repair canonical format finding).
>
> | Inherited commitment | Re-test status | Evidence |
> |---|---|---|
> | NFC + paratext stripping as minimal-intake cleanup ops | **PRESERVED + EXTENDED.** NFC becomes Category 1; paratext becomes Category 3. The baseline expands into an 8-category structured set. | Categories 1 + 3 contain the prior commitments unchanged; the set grows additively. |
> | HTML5 canonical format | **COMPATIBLE.** This finding's recommended preprocessing produces structure that fits HTML5 (h1-h6 hierarchy; semantic elements like `<aside>` / `<figure>`) without crossing into semantic role tagging. | Categories 5 + 6 explicitly produce HTML5-compatible structure. |
> | "Leave content unclassified; trust the LLM" scope narrowing (very recent conversation; not yet in a finding) | **PRESERVED.** The scope narrowing is the underlying mandate that motivated this inquiry's scope-line principle ("structural, not semantic"). Every category respects the narrowing. | P2's scope-line is the operational principle that enforces the narrowing per-operation. |
>
> **Prior 2: `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`** (the original intake-concepts finding).
>
> | Inherited commitment | Re-test status | Evidence |
> |---|---|---|
> | Decision 2 — structure-preservation quality target | **PRESERVED + STRENGTHENED.** Category 5 structural detection is explicitly aligned to structure-preservation; the scope-line principle makes preservation primary by excluding semantic interpretation that could distort structure. | P6 Category 5 = structural detection operations; P2 scope-line excludes semantic distortion. |
> | Decision 5 — Pandoc + OCR architectural lever | **PRESERVED + STRENGTHENED.** Category 6 format-specific repair explicitly leans on Pandoc readers (EPUB / HTML / Word) and OCRmyPDF/Tesseract (for image-only Arabic). | P7 Category 6 operations name Pandoc readers and OCR fallback. |
> | Decision 3 — IntakeDoc shape (tree-of-containers + cross-referenced flat collections, preserved-in-semantic-intent with HTML5 DOM substrate per the prior canonical-format finding) | **PRESERVED.** This inquiry's recommended preprocessing produces HTML5 that maps to the IntakeDoc shape unchanged. | Categories 5 + 6 produce structure (sections, asides, figures, blockquotes) that fit the tree-of-containers + flat-collections model. |
> | Decision 4 — 7-policy intake-perception + translate-rendering split | **PRESERVED-IN-INTENT but DEFERRED for v0.2.** The 7-policy split is the project's classification roadmap; this inquiry's scope-line principle DEFERS classification per the recent scope narrowing. When classification is revived (P12 / P11 DEFERRED), the 7 policies are the canonical set. | P9 rejections cite the 7 policies as semantic-role-tagging; P11 DEFERRED preserves their revival path. |
> | The 38 intake-handling concepts enumerated in the original | **PRESERVED-IN-INTENT.** Most of the 38 concepts are honored across the 8 categories; the few that involve classification (apparatus role tagging; voice classification) are deferred per scope-line. | Categories 1-7 implement most of the 38; P11 DEFERRED preserves the rest. |
>
> **Relationship-label `extends:` distinguished:**
>
> - `extends:` — additive growth; new content layers onto prior commitments without changing any prior cell. THIS LABEL APPLIES because: (a) no prior commitment's content is modified; (b) prior baseline ops (NFC + paratext) become Categories 1 + 3 in a set that grows around them; (c) the scope-line principle is NEW articulation, not a revision of an existing principle.
> - `refines:` (NOT this label) — would mean changing one cell of inherited architecture. No cell changes here; only additions.
> - `supersedes:` (NOT this label) — would mean replacing prior content. Nothing is replaced.
> - `corrects:` (NOT this label) — would mean the prior was structurally wrong. The prior was not wrong; it was incomplete (lacked an articulated scope-line because classification was still under consideration).

**Mechanism log:**
- *Combination:* prior commitments × this inquiry's commitments → per-commitment re-test verdict.
- *Domain Transfer:* software API versioning (extend without breaking) — directly analogous.
- *Absence Recognition:* prior findings did not have an articulated scope-line; this inquiry adds it without disturbing prior commitments.

**Piece-Level Inversion (required — P10 fires property (i) relationship-label):**

> *Inversion-candidate:* what if the priors are wrong — `supersedes:` instead of `extends:`?
>
> *What follows under the inversion:* this finding declares the priors invalid; the 8-category set REPLACES the prior NFC + paratext baseline; HTML5 canonical commitment is REPLACED; Decisions 2 + 5 from the original are dropped.
>
> *Why rejected:* (a) NFC + paratext baseline is preserved literally as Categories 1 + 3 — no replacement needed. (b) HTML5 canonical is structurally compatible with this inquiry's outputs; no replacement needed. (c) Decisions 2 + 5 are STRENGTHENED, not replaced — Category 5 aligns with Decision 2, Category 6 leans on Decision 5. (d) The scope-line principle is NEW articulation that fills a gap, not a correction of prior content. `extends:` is structurally precise.
>
> *Intervention-shape check:* P10 commits to the `extends:` relationship-label. Alternatives from the Intervention-Shape Vocabulary: `refines:` (rejected — no cell changes); `supersedes:` (rejected — nothing replaced); `corrects:` (rejected — prior was incomplete, not wrong); REVERT-REGRESSION (n/a). `extends:` is the correct intervention shape.
>
> Verdict: **rejected** — `extends:` is structurally accurate; priors are preserved.

**5-test:** PASS — every prior commitment re-tested with cited evidence; relationship-label distinguished from siblings; inversion-candidate tested and rejected.

---

### P11 (DERIVED) — Transition plan + Next Actions

**Principal candidate (content):**

> **MUST items** (required for v0.2 intake preprocessing to ship):
>
> - **MUST 1: Per-category operation specs ready for engineering.**
>   - *What:* For each of the 8 categories, ship a brief per-operation spec (input → algorithm → output; library refs; test cases).
>   - *Who:* engineering team via 8 sister `/traverse` inquiries (one per category) OR a single consolidated spec document.
>   - *Gate:* condition-bound — before v0.2 intake code lands.
>   - *Why:* per-operation specs are the engineering contract; without them, intake's behavior is under-specified.
>
> - **MUST 2: Hierarchy-inference algorithm spec for flat-h1 sources (Category 5).**
>   - *What:* Specify the marker-detection regex set; the bold/centered/standalone-line clustering; the depth-promotion rule (h2 default; deeper inference via Category 8 extensions).
>   - *Who:* a focused `/traverse` inquiry.
>   - *Gate:* condition-bound — before v0.2 Category 5 engineering begins.
>   - *Why:* the Asa-yı Musa EPUB has flat h1; without the inference algorithm, sub-section structure is lost.
>
> - **MUST 3: Format-specific Pandoc invocation patterns (Category 6).**
>   - *What:* Document the exact Pandoc commands + pre/post-processing chain for EPUB and PDF intake paths.
>   - *Who:* engineering documentation + the existing `comprehenslate/intake/` module.
>   - *Gate:* condition-bound — before v0.2 Category 6 engineering begins.
>   - *Why:* Pandoc is the architectural lever (Decision 5); concrete invocation patterns ensure reproducibility.
>
> - **MUST 4: Category 7 flag-exposure mechanism (decide schema + format).**
>   - *What:* Commit the sidecar JSON schema and the HTML5 `<meta>` block schema; pick one as primary; ship the schema file.
>   - *Who:* a focused `/traverse` inquiry.
>   - *Gate:* condition-bound — before v0.2 Category 7 engineering begins.
>   - *Why:* without a schema, flag consumers can't act on intake's quality signals.
>
> **COULD items** (worth considering; not blocking):
>
> - **COULD 1: Category 8 extensions API design** (how corpus extensions plug in; opt-in semantics; per-corpus configuration).
>   - *Depends-on:* MUST 2 (the hierarchy-inference algorithm Category 8 extensions plug into). GATED — do not act until MUST 2 resolves.
> - **COULD 2: Hierarchy-inference for new corpora beyond Risale-i Nur.**
>   - *Depends-on:* MUST 2 AND COULD 1. GATED — do not act until both resolve.
> - **COULD 3: Quality-floor sub-category boundary refinements.**
>   - *Depends-on:* MUST 1 (per-category specs ship and empirical evidence accumulates). GATED.
>
> **DEFERRED items** (postponed; revival triggers below):
>
> - **DEFERRED 1: Word + plain-text format support** (Category 6 extension).
>   - *Gate:* observable — when project source-mix expands to include Word or plain-text sources.
>   - *Why (if revived):* current corpus is EPUB/PDF-dominant; engineering effort is bounded.
>
> - **DEFERRED 2: Cross-corpus validation.**
>   - *Gate:* condition-bound — when 2+ corpora are in the project (beyond Risale-i Nur).
>   - *Why (if revived):* validates that the scope-line principle and the 8-category set generalize beyond the calibration corpus.
>
> - **DEFERRED 3: Classification work** (per-element provenance; per-policy detection; per-span language identification; the 7 schema policies).
>   - *Gate:* condition-bound — when minimal-intake is tested in production AND translation quality empirically requires classification.
>   - *Why (if revived):* classification was DEFERRED per scope narrowing (LLM handles per-span language; per-policy classification's value is unclear without v0.2 testing first). Revival path preserves Decision 4's 7-policy intent.
>
> - **DEFERRED 4: Per-corpus configuration UI in the Mac app.**
>   - *Gate:* observable — when Category 8 API ships AND a second corpus enters the project.
>   - *Why (if revived):* corpus selection becomes user-facing only when multiple corpora exist.
>
> **Integration with prior post-repair-canonical-format finding's Next Actions:** Some of the prior's MUSTs (HTML5 schema profile; per-policy class conventions; provenance encoding) are now reclassified:
> - HTML5 schema profile → still MUST, but bounded to canonical structure (no per-policy classes).
> - Per-policy class conventions → moved to DEFERRED 3 (classification work).
> - Per-element provenance encoding → moved to DEFERRED 3 (classification work).
> - HTML5-to-EPUB packaging (COULD) → unchanged; still COULD.
> - HTML5-to-md round-trip subset (COULD) → unchanged.
> - Risale-i Nur prototype (COULD) → composes with this inquiry's MUSTs 1-4.

**Mechanism log:**
- *Combination:* 8 categories × MUST/COULD/DEFERRED priority + time/condition triggers.
- *Extrapolation:* current commitments → engineering timeline + future revival paths.
- *Constraint Manipulation (ADD):* "v0.2 ships within reasonable time" → bounds MUST list.

**5-test:** PASS — per-item Who/What/Gate/Why; COULD-MUST dependency gating applied; integration with prior Next Actions explicit; revival triggers specific (time/condition/observable).

---

### P12 (DERIVED) — Open Questions / Frontier

**Principal candidate (content):**

> **Open questions resolvable in MUST/COULD inquiries:**
>
> - **Scope-line edge cases.** As new candidate operations surface in v0.2 testing, some will be ambiguous against the test-question. Each adjudication updates the per-operation verdicts.
>   - *Revival trigger:* observable — when a new gray-zone operation surfaces during v0.2 engineering or in a sister inquiry.
>
> - **Hierarchy-inference algorithm specification (for flat-h1 sources).** The exact marker-detection regex set and clustering policy need formal specification.
>   - *Revival trigger:* condition-bound — resolves in MUST 2.
>
> - **Quality-floor sub-category boundary refinements.** Empirical evidence from v0.2 may show that some Category 1 operations belong in Category 2 (or vice versa). The sub-category boundary refines over time.
>   - *Revival trigger:* observable — when empirical evidence supports promotion / demotion of a specific operation.
>
> - **Category 8 extensions API design.** The opt-in attachment mechanism; the per-corpus configuration format; the registration protocol.
>   - *Revival trigger:* condition-bound — resolves in COULD 1; triggered by a second corpus entering the project.
>
> **Frontier items — deferred but not dismissed:**
>
> - **Format expansion** (Word + plain-text + RTF + others). HTML5 canonical accepts most input formats via Pandoc; v0.2 ships with EPUB + PDF only.
>   - *Revival trigger:* observable — project source-mix expands.
>
> - **Cross-corpus validation.** Does the 8-category set + the scope-line principle generalize to Talmud / Vedic / patristic / modern-academic-book corpora?
>   - *Revival trigger:* condition-bound — 2+ corpora in the project.
>
> - **Classification revival** (per-element provenance; per-policy detection; per-span language identification). The 7 schema policies are the canonical classification roadmap.
>   - *Revival trigger:* condition-bound — minimal-intake tested in production AND translation quality empirically requires classification. The revival composes with COULD 3 boundary refinements.
>
> - **Sentence segmentation quality for Turkish.** The `spacy xx_sent_ud_sm` or `nltk Punkt` models may produce errors on Turkish-specific abbreviations and ordinals.
>   - *Revival trigger:* observable — empirical evidence of segmentation errors in v0.2 testing.
>
> - **Hyphenation-repair false-positives.** The regex `(\w+)-\n(\w+)` may wrongly merge intentional line-breaks (verse, lists, emphasis line-breaks).
>   - *Revival trigger:* observable — false-positive instances observed; tune body-paragraph-only application.
>
> - **EPUB CSS-presentation extraction edge cases.** Many EPUBs (including Asa-yı Musa) use `class="strong"` or `class="emphasis"` instead of HTML `<strong>` / `<em>`. The mapping is straightforward in known cases but corpus-dependent for novel CSS conventions.
>   - *Revival trigger:* observable — encountering a novel CSS-class convention.
>
> - **Pandoc version pinning.** As HTML5 canonical evolves and Pandoc's reader behavior shifts, the project should pin a Pandoc version per intake configuration.
>   - *Revival trigger:* observable — when a Pandoc version change affects v0.2's reader behavior.

**Mechanism log:**
- *Absence Recognition:* "what's still open after the recommended set is committed?" → open-questions list.
- *Extrapolation:* future evolution paths from current commitments.

**5-test:** PASS — every open question has a specific revival trigger (condition / observable); frontier items distinguished from MUST/COULD-resolvable.

---

### P1 — Executive summary (produced LAST per dependency order)

**Principal candidate (content):**

> The intake preprocessing pipeline for v0.2 is a categorized 8-category recommended set anchored by the load-bearing scope-line principle **"structural, not semantic"**: preprocessing identifies WHERE things are and HOW they nest in the source, but does NOT identify WHAT cultural / linguistic role they play. The 8 categories are foundational normalization (NFC, whitespace, ligatures, quotes/dashes — byte-consistency), translation-quality-floor (sentence segmentation, language ID, mojibake repair, hyphenation — load-bearing for LLM translation quality), paratext stripping (running headers, page numbers, editorial boilerplate — established baseline extended), source-format metadata + provenance (title/author/date/checksum/intake-time — document-level), structural detection (heading hierarchy preservation + inference for flat-h1 sources; list/table/quote/verse/footnote/cross-ref/caption/drop-cap — structural only), format-specific repair (EPUB-first: spine reassembly, CSS-presentation extraction, OPF metadata; PDF-with-OCR-fallback: bidi-fix, italic recovery, OCR for image-only Arabic; Word + plain-text DEFERRED to future), quality / hygiene (informational flags — truncation, document-completeness, confusables, etc.; flag-only, not corrective), and corpus-specific extensions (Risale-i-Nur-tuned operations like letter-spaced un-spacing and Mukaddeme/Mes'ele keyword recognition — opt-in extension layer, NOT part of v0.2 generic core). The depth-of-boundary policy is source-driven hierarchy preservation up to HTML5's h1-h6 ceiling. The format priority commits EPUB-first because EPUB intake is significantly cheaper than PDF intake for the calibration corpus (per the Asa-yı Musa EPUB analysis: clean Unicode Arabic in text-layer; italic/bold preserved; footnote structure intact); PDF-with-OCR-fallback handles sources that exist only in PDF (per the Muhakemat PDF: image-only Arabic). The two-layer corpus model honors the project_scope commitment (generic translation; Risale-i Nur as calibration corpus, not purview) by separating generic operations from calibration-corpus-tuned extensions. This finding **extends** the prior post-repair canonical format finding's NFC + paratext stripping baseline (Categories 1 + 3 of this set) without modifying any prior cell — nothing prior is replaced; new content layers around the baseline. The original intake-concepts finding's Decision 2 (structure-preservation quality target) is STRENGTHENED via Category 5; Decision 5 (Pandoc + OCR architectural lever) is STRENGTHENED via Category 6. The classification work deferred per the recent scope narrowing ("leave content unclassified; trust the LLM") is preserved with explicit revival path (DEFERRED 3 in Next Actions) so the 7 schema policies remain the canonical classification roadmap when classification is revived.

**Mechanism log:**
- *Combination:* all 11 prior pieces → one-paragraph synthesis.
- *Lens Shifting:* under "what does the reader need at-a-glance?" lens.

**5-test:** PASS — names scope-line; names 8 categories with brief role; names depth policy; names format priority; names two-layer model; names `extends:` relationship; sized for one-paragraph reading.

---

## Inherited Frame Audit (between Phase 2 and Phase 3)

**Step (i) — Seed central assumption.** The seed framing assumes the SV6 verdict from sensemaking (8-category recommended set anchored by "structural, not semantic" scope-line; depth source-driven up to h6; format EPUB-first + PDF-fallback; two-layer corpus model; quality-floor sub-category). Central assumption: **"structural, not semantic" is the right scope-line for v0.2 preprocessing.**

**Step (ii) — Per-piece commitments.** Meta-decision pieces with load-bearing commitments: P2 (scope-line); P3 (two-layer corpus model); P6 (depth policy); P7 (format priority); P10 (`extends:` relationship-label).

**Step (iii) — Challenge scan.** Are there candidates challenging the central assumption?
- P2's Inversion-candidate tested "what if scope-line is wrong — classification IS preprocessing?" — rejected with structural reasoning.
- P3's Inversion-candidate tested "what if there's no two-layer model?" — rejected with project_scope-vs-empirical-knowledge reasoning.
- P6's Inversion-candidate tested "what if hierarchy doesn't matter?" — rejected with empirical (Asa-yı Musa EPUB) evidence.
- P7's Inversion-candidate tested "what if PDF should be first?" — rejected with cost-comparison reasoning.
- P10's Inversion-candidate tested "what if `supersedes:` instead of `extends:`?" — rejected with literal-preservation evidence.
- P9 (rejections) tested 11 specific alternative candidates and structurally rejected each.

**Step (iv) — Firing condition.** Audit does **NOT fire**. Every meta-decision piece's load-bearing commitment received explicit Inversion-candidate testing with cited evidence. Proceed to Phase 3 Test.

---

## Phase 3 — Test + Assembly

### Per-piece 5-test summary

All 12 pieces' principal candidates passed the 5-test cycle. Inversion candidates at P2, P3, P6, P7, P10 were generated, tested, and rejected with structural reasoning — compliance per the Piece-Level Inversion Rule.

### Assembly check

> **Does the architecture emerge from the 12 pieces' assembly?**
>
> **YES.** P1 gives the headline; P2 commits the scope-line principle + decision-mode + relationship-label; P3 commits the two-layer corpus model + Category 8 content; P4-P8 specify the 8 categories with concrete operations and library references; P9 explains rejections via the scope-line; P10 re-tests inherited commitments; P11 plans the transition; P12 names what's still open. Read in dependency order (P2 → P3-P9 parallel → P10 → P11 → P12 → P1), the assembled finding tells a coherent story: a generic v0.2 intake preprocessing pipeline organized by a load-bearing scope-line principle, extending the prior NFC + paratext baseline into an 8-category structured set, with calibration-corpus-specific operations preserved in a separate extension layer.

### Axis coverage check

Orthogonal axes the candidate space varies along:
- **Scope axis** (preprocessing vs classification) — covered by P2 + P9.
- **Depth axis** (boundary detection depth) — covered by P6 + D sub-territory from surfacing.
- **Format axis** (EPUB / PDF / Word / plain-text) — covered by P7.
- **Corpus axis** (generic / corpus-tuned) — covered by P3.
- **Time axis** (MUST / COULD / DEFERRED) — covered by P11.
- **Stage axis** (preprocessing / classification / translate / publishing) — covered by P9 rejections.

All 6 orthogonal axes have ≥1 candidate variant. No single-axis collapse. PASS.

### Per-row mechanism-trace

Every piece has explicit mechanism work logged. Every operation in P4 / P5 / P6 / P7 / P8 has a concrete Python implementation or detection approach. The 5 meta-decision pieces have Inversion candidates explicitly tested. No row-baseline silent inheritance.

---

## Telemetry

### Mechanism Coverage

- **Generators applied:** 4 / 4 (Combination · Absence Recognition · Domain Transfer · Extrapolation).
- **Framers applied:** 3 / 3 (Lens Shifting · Constraint Manipulation · Inversion).
- **Coverage:** FULL.
- **Convergence:** YES — Combination + Constraint Manipulation + Absence Recognition + Domain Transfer all converge on the categorized 8-tier set + scope-line principle via different paths.
- **Survivors tested:** 12 / 12 principal candidates + 5 Piece-Level Inversion candidates = 17 / 17 tested.
- **Failure modes observed:** None.

### Production-task additional telemetry

| Piece | Mechanisms | Classification | Inversion compliance |
|---|---|---|---|
| P1 | Combination, Lens Shifting | content-production | n/a |
| P2 | Combination, Lens Shifting, Constraint Manipulation (ADD+REMOVE), Absence Recognition (patch+redesign), Domain Transfer, **Inversion** | **meta-decision** (i+ii+iii) | **satisfied** |
| P3 | Combination, Absence Recognition (patch+redesign), Domain Transfer, Constraint Manipulation (ADD+REMOVE), **Inversion** | **meta-decision** (ii) | **satisfied** |
| P4 | Combination, Absence Recognition, Domain Transfer, Constraint Manipulation (ADD) | content-production | n/a |
| P5 | Combination, Absence Recognition | content-production | n/a |
| P6 | Combination, Absence Recognition, Domain Transfer, Constraint Manipulation (ADD+REMOVE), **Inversion** | **meta-decision** (iv) | **satisfied** |
| P7 | Combination, Absence Recognition, Constraint Manipulation (ADD+REMOVE), **Inversion** | **meta-decision** (iv) | **satisfied** |
| P8 | Combination, Absence Recognition, Constraint Manipulation (ADD), Lens Shifting | content-production | n/a |
| P9 | Combination, Constraint Manipulation (ADD+REMOVE) | content-production | n/a |
| P10 | Combination, Domain Transfer, Absence Recognition, **Inversion** | **meta-decision** (i) | **satisfied** |
| P11 | Combination, Extrapolation, Constraint Manipulation (ADD) | content-production | n/a |
| P12 | Absence Recognition, Extrapolation | content-production | n/a |

### Verdict

**PROCEED** — full mechanism coverage; convergence on the categorized 8-tier set via 4+ mechanisms; all 12 piece candidates + 5 Inversion candidates tested; Piece-Level Inversion compliance satisfied at all 5 meta-decision pieces; Inherited Frame Audit did not fire; Assembly + Axis coverage + Per-row mechanism-trace all PASS. No failure modes observed.
