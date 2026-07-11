# Innovation — document intake handling concepts

## User Input

Substrate: `_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md`. Production-task mode: Decomposition's 9 pieces (P1-P9) are the seed; Innovation generates per-piece substantive content for the eventual finding.

---

## Phase 1 — Seed / Methodology-Mode Consideration

**Inherited methodology mode:** **Standard default** (4G + 3F balanced; elaborate the committed direction; produce ship-ready output). Signal: the seed framing says *"This is the discipline where the substantive content gets GENERATED"* + Decomposition pre-committed the 9-piece structure.

**Alternative mode considered:** **Contrarian-rethink (Framer-weighted)**. Under that mode, Innovation would treat the 5 sensemaking decisions and the 9-piece decomposition as questionable rather than committed; surface contrarian alternatives to each.

**What follows under the alternative:** the run would re-debate the 5 load-bearing decisions (canonical format = Pandoc-md-superset; quality target = structure-preservation; etc.) instead of elaborating them. Candidate-space would widen (alternative canonical formats; alternative quality targets) at the cost of not producing the finding content the user asked for.

**Decision:** **Standard default.** Sensemaking already adjudicated the 5 decisions through Phase 3 Ambiguity Collapse with full Strongest-Counter-Interpretation tests — re-running contrarian-rethink would duplicate that work without new evidence. Inversion candidates will fire at meta-decision pieces (P2, P3, P8) per the per-piece rule; that handles the contrarian surface at piece level without globalizing it.

`Methodology-mode-alternative-marked-inapplicable: Sensemaking's Phase 3 already ran Strongest-Counter tests on each of the 5 decisions with HIGH-confidence resolutions; Contrarian-rethink at Innovation would duplicate the adjudication without new evidence. Piece-level Inversion at meta-decision pieces (P2/P3/P8) provides the contrarian surface at appropriate granularity.`

---

## Phase 2 — Generate (per piece)

### P2 (META-DECISION; produced FIRST per dependency order) — Methodology / pruning rationale / status-tag legend

**Principal candidate (content):**

> **Methodology disclaimer.** This finding's concept list is anchored to four grounding sources, in order of priority: (i) **schema reference** — the 7 policy classes + `TranslationConfig` + `PipelineConfig` in `SKILL/references/config/schemas.py`; (ii) **Pandoc-fact** — Pandoc's documented format support and extension set (`pandoc --list-extensions`, the official manual at pandoc.org); (iii) **sensemaking-anchor** — commitments stabilized at SV6 (the 5 load-bearing decisions); (iv) **explicit-extrapolation-flag** — any claim that extends beyond (i)-(iii) is marked `[extrapolation: <reason>]` inline.
>
> **Pruning.** Surfacing produced 110 candidate concepts across 4 layers; sensemaking pruned to 38 load-bearing concepts. The pruning criterion per candidate: keep if AT LEAST ONE of [(a) schema-named or schema-implied; (b) downstream-consequential for translation quality; (c) requires v0.2+ engineering decision]. Drop if any of [redundant under Pandoc; format-edge irrelevant to Risale-i Nur shape; v1+ scope]. The 72 dropped concepts cluster as: ~15 format-edge (LaTeX, math notation, ligatures per-format), ~18 structure-edge (code blocks, captions, citation sub-types, original-vs-modernized spelling), ~12 pipeline-operational (logging detail, streaming-vs-load-all, schema versioning machinery), ~12 quality-secondary (round-trippability framing, reference intake, inter-intake-diffing), ~15 already-subsumed-by-Pandoc-md-superset (e.g., footnote-syntax-design — already Pandoc).
>
> **Status-tag legend.**
>
> | Tag | When to apply | Operational meaning |
> |---|---|---|
> | **DECIDE-NOW** | The concept's resolution is committed in this finding | The reader takes this as a foreclosing choice |
> | **DESIGN-NEXT-INQUIRY** | The concept needs a downstream inquiry before engineering | Spawn a sub-inquiry; do not engineer blind |
> | **ENGINEER** | The concept is well-defined; ready for code | Standard implementation work; no further design needed |
> | **DEFER** | The concept is real but v1+ scope | Out-of-scope for v0.2; record in Frontier; revisit |
>
> *Anti-padding statement:* Every concept entry in Layers A-D carries (i) a one-line definition, (ii) a status tag, (iii) a downstream-pointer or grounding-anchor. Entries that cannot meet all three are dropped.

**Mechanism log:**
- *Constraint Manipulation (ADD):* added "must cite grounding source" → forced four-source taxonomy.
- *Constraint Manipulation (REMOVE):* removed "preserve all 110 surfaced candidates" → pruning rationale emerged.
- *Absence Recognition (patch-level):* what's missing from typical methodology disclaimers → the anti-padding statement.
- *Absence Recognition (redesign-level):* if intake-handling were designed from scratch, the four-source grounding would be table-stakes, not novel.

**Piece-Level Inversion (required — P2 is meta-decision via framing-semantic + lesson-vocabulary properties):**

> *Inversion-candidate:* what if the methodology should NOT name four grounding sources — what if the user wanted a raw list without epistemic guards?
>
> *What follows:* the finding becomes a flat list of 38 concepts without provenance per entry; reader trusts the list but cannot audit. Downstream consumer cannot tell which concepts are anchored vs extrapolated. Verdict on inversion: **rejected** — the user's "real painpoint" framing implies they will act on this list; un-auditable lists invite later rework when extrapolations turn out wrong. The principal direction stands.

**5-test:** Novelty (the four-source grounding is novel for this project — Pandoc, schema, sensemaking, explicit-extrapolation as named sources); Scrutiny (audit-trail survives "where did this come from?"); Fertility (the four-source taxonomy can be reused in future findings); Actionability (a reader can audit any concept's anchor); Mechanism independence (Combination of methodology-anchoring patterns from prior findings + Absence Recognition produced the same four-source taxonomy). PASS.

---

### P3 (META-DECISION; produced SECOND) — The 5 load-bearing decisions

**Principal candidate (content):**

> **Decision 1 — Canonical intake format = Pandoc-md-superset.**
>
> *Commit:* Comprehenslate's intake stage internalizes every source document into Pandoc's extended markdown (Pandoc-md-superset): the CommonMark base plus the Pandoc-native extensions `footnotes`, `pipe_tables` / `multiline_tables`, `definition_lists`, `citations`, `yaml_metadata_block`, and `raw_attribute` for inline tag-escapes. YAML frontmatter carries metadata + apparatus references; the body markdown carries the tree structure.
>
> *Rationale:* (a) CommonMark alone lacks footnotes (needed for marginalia and source-apparatus per `SourceApparatusPolicy`), tables (needed for apparatus criticus), and definition-lists (needed for glossary terms). [grounding: schema reference + Pandoc-fact via `pandoc -t markdown --list-extensions`] (b) Pandoc is the universal converter for the 6 other accepted formats (docx / RTF / EPUB / html / PDF-with-text-layer / plain-text), so picking Pandoc's superset as the canonical means a single internal parser surface. (c) Pandoc-md-superset is human-readable + hand-editable — supports the recovery workflow when auto-parse degrades (decision D5).
>
> *What's foreclosed:* vanilla CommonMark as canonical (lacks needed primitives); RTF as canonical (editor-fragility defeats hand-editing); .compldoc-precursor for v0.2 (significant engineering cost; v1+ scope).
>
> *Revisitability:* MEDIUM. If scaling beyond Risale-i Nur reveals primitives Pandoc-md-superset cannot express (e.g., complex mathematical notation, music notation), revisit by either (a) adopting Pandoc's `raw_html`/`raw_tex` escape hatches or (b) graduating to a custom `.compldoc` format.
>
> **Decision 2 — Quality target = structure-preservation.**
>
> *Commit:* Intake's success is measured by **structural-element-preservation percentage** against the source: chapter/section boundaries preserved; paragraph boundaries preserved; footnotes / marginalia / embedded poetry / formulaic openings / voice transitions / archaic register markers / non-main-language spans (the 7 policy targets) detected and represented; emphasis (italic-as-emphasis, bold-as-strong-emphasis) preserved as a semantic primitive.
>
> *Rationale:* (a) The user's painpoint is structural loss ("PDF formatting can be really bad" = chapter / paragraph / footnote boundaries collapse). [grounding: user input verbatim + sensemaking SV6 KI5] (b) The 7 policy classes operate on structural elements; without intake having perceived them, the policies have nothing to apply to. [grounding: schema reference] (c) Raw typography (font face / size / color choice) is rendering decoration, not structural meaning — preserving it would commit `IntakeDoc` to typesetting state that translation cannot use.
>
> *What's foreclosed:* typography-fidelity as a primary goal (includes too much rendering noise; misses structural signal in heading-typography); semantic-only stripping (drops chapter/paragraph context that chunking needs).
>
> *Revisitability:* LOW. The choice is load-bearing for `IntakeDoc` field design (decision 3) and the 7 detectors (B4-B10).
>
> **Decision 3 — `IntakeDoc` shape = tree-of-containers + cross-referenced flat collections.**
>
> *Commit:* `IntakeDoc` is structured as a **tree** of typed containers (Document → Chapter → Section → Paragraph) where each leaf node carries inline content with embedded markers; the markers reference **flat collections at the `IntakeDoc` root** for apparatus (footnotes, marginalia, embedded-poetry, formulaic-openings, non-main-language spans, voice-transition annotations).
>
> *Pseudocode sketch [extrapolation: schema sketch — actual field design is C1 DESIGN-NEXT-INQUIRY]:*
>
> ```
> # NOT actual Python — illustrative shape only
> IntakeDoc:
>     metadata: {title, author, source-format, source-language, intake-time, intake-version}
>     body: Document
>         children: [Chapter | FrontMatter | BackMatter]
>             Chapter:
>                 title: InlineText
>                 children: [Section | Paragraph]
>                     Section: { title, children: [Section | Paragraph] }
>                     Paragraph: { runs: [TextRun | MarkerRun] }
>                         MarkerRun: { type, ref-id → root collection }
>     apparatus:
>         footnotes:        Dict[id, FootnoteNode]
>         marginalia:       Dict[id, MarginaliaNode]   # SourceApparatusPolicy target
>         embedded_poetry:  Dict[id, PoemNode]         # EmbeddedPoetryPolicy target
>         formulaic_openings: Dict[id, OpeningNode]    # FormulaicOpeningPolicy target
>         non_main_lang_spans: Dict[id, SpanNode]      # NonMainLangPartsPolicy target
>         voice_transitions: Dict[id, VoiceMarkNode]   # VoiceMarkingPolicy target
>         honorifics: Dict[id, HonorificMarkNode]      # HonorificsPolicy target
>         archaic_register_marks: Dict[id, RegisterNode] # ArchaicRegisterPolicy target
> ```
>
> *Rationale:* (a) Pure-tree would force apparatus into either sub-tree positions (breaking paragraph-adjacency for marginalia, which references back to a body position) or parallel streams (loses cross-reference). (b) Pure-flat-with-region-tags loses chapter-context that `PipelineConfig.chunking_granularity = "chapter"` requires. (c) Tree + cross-ref-flat is the smallest shape that supports both chunking-by-container AND apparatus-by-reference. [grounding: schema reference for chunking_granularity literals]
>
> *What's foreclosed:* pure tree without cross-ref (apparatus mis-positioned); pure flat-list-without-hierarchy (chunking-by-chapter fragile).
>
> *Revisitability:* The SHAPE is committed; the FIELD-level schema (exact pydantic class) is C1 DESIGN-NEXT-INQUIRY — that inquiry can adjust field types without revisiting the tree+cross-ref decision.
>
> **Decision 4 — 7-policy split: intake PERCEIVES + REPRESENTS; translate CHOOSES + RENDERS.**
>
> *Commit:* Each of the 7 policy classes (`NonMainLangPartsPolicy`, `SourceApparatusPolicy`, `VoiceMarkingPolicy`, `ArchaicRegisterPolicy`, `HonorificsPolicy`, `FormulaicOpeningPolicy`, `EmbeddedPoetryPolicy`) has TWO halves:
>
> 1. **Intake-time perception** (the detector) — finds the target element in the source, represents it in `IntakeDoc`'s apparatus collections.
> 2. **Translate-time rendering** (the policy value) — chooses which `Literal` option to apply when producing translation output.
>
> The policy's `Literal` value lives in `TranslationConfig`; the policy's TARGET ELEMENT lives in `IntakeDoc`. Each detector (B4-B10) is downstream of this split.
>
> *Rationale:* (a) [grounding: schema reference] Each policy's docstring references SOURCE features (Said Nursi's hashiye for `SourceApparatusPolicy`; Mevlana couplets for `EmbeddedPoetryPolicy`) — these are intake-perceived, not translate-invented. (b) Without intake having perceived marginalia, `SourceApparatusPolicy.translate-as-footnote` has nothing to apply to — vacuous setting. (c) The split keeps the 7-policy contract stable while clarifying who does what.
>
> *What's foreclosed:* treating policies as translate-only (perception step skipped, downstream breaks).
>
> *Revisitability:* LOW. The split is structural.
>
> **Decision 5 — Pandoc as architectural lever; OCR (Tesseract + OCRmyPDF) as depth-1 sub-pipeline.**
>
> *Commit:* Format-layer engineering leverages Pandoc — accepted user formats (PDF / docx / RTF / md / EPUB / html / .txt) all convert through Pandoc to Pandoc-md-superset. PDFs without a text layer (scan-only) route through an OCR sub-pipeline: OCRmyPDF wraps Tesseract; output is a text-layer-PDF that then flows through the Pandoc path.
>
> *Rationale:* (a) [grounding: Pandoc-fact] Pandoc handles all 6 non-PDF formats natively; PDF text-layer extraction works for born-digital. (b) [grounding: Pandoc-fact] OCRmyPDF and Tesseract are mature, scriptable, well-documented tools. (c) Building parsers from scratch is unnecessary engineering cost; Pandoc + OCR covers ~80% of intake at v0.2.
>
> *What's foreclosed:* writing per-format parsers from scratch.
>
> *Revisitability:* MEDIUM. If specific formats (e.g., complex multi-column scholarly PDFs) routinely fail Pandoc, supplement with format-specific tools (pdf2htmlEX, mammoth for docx).

**Mechanism log:**
- *Combination:* Pandoc-as-converter + schema-perception split + tree-with-cross-ref → all 5 decisions cohere as one architectural commitment.
- *Constraint Manipulation (ADD):* added "must respect 7 schema policies" → forced the perception/rendering split.
- *Constraint Manipulation (REMOVE):* removed "must write per-format parsers" → Pandoc-as-lever emerged.
- *Absence Recognition (patch-level):* nothing names the perception/rendering split anywhere in current docs → load-bearing absence → decision 4.
- *Absence Recognition (redesign-level):* if intake were designed from scratch today, Pandoc would be canonical lever (already-present in narrative — sensemaking SV6 KI8 named it).
- *Lens Shifting:* under the "what does the engineer need on day 1?" lens — they need to know format, target, doc shape, policy contract, conversion tools. The 5 decisions ARE that day-1 brief.

**Piece-Level Inversion (required — P3 IS the meta-decisions piece):**

> *Inversion-candidate at piece-level:* what if the right move is to NOT commit any of the 5 decisions and instead present them as open options for v0.2's engineering inquiry to adjudicate?
>
> *What follows:* the finding becomes a survey of options without commitment. Engineering work in v0.2 starts with re-debating canonical format / quality target / `IntakeDoc` shape rather than building. The user's "scope the engineering task" motivation (WHY-axis) fails — without decisions, the task remains unbounded.
>
> *Per-decision Inversion (the decisions themselves are individually meta-decisions):*
> - **D1 inverse:** custom format from day one. Rejected — engineering cost; sensemaking Ambiguity 3 already adjudicated. The custom format is the v1+ path.
> - **D2 inverse:** typography-preservation as target. Rejected — sensemaking Ambiguity 4 already adjudicated; includes rendering noise.
> - **D3 inverse:** pure tree (no cross-ref). Rejected — sensemaking Ambiguity 6 already adjudicated; apparatus mis-positioned.
> - **D4 inverse:** policies are translate-only; intake doesn't perceive them. Rejected — sensemaking Ambiguity 5 already adjudicated; vacuous policy values.
> - **D5 inverse:** write parsers from scratch. Rejected — engineering cost; Pandoc-fact + sensemaking KI8 ground the lever.
>
> Verdict on piece-level inversion: **rejected** — each per-decision inverse was already adjudicated structurally in sensemaking Phase 3; un-deciding here would discard that work.

**Intervention-shape axis check:** P3 doesn't fire property (v) (no intervention-shape commitment in the Vocabulary sense — the piece commits architectural decisions, not maintenance-shape commitments). `Intervention-shape-Inversion-marked-inapplicable: P3 commits architectural design decisions, not maintenance/intervention shapes from the Vocabulary; the intervention-shape axis is not the piece's axis.`

**5-test:** Novelty (the per-policy intake/translate split is novel for this project); Scrutiny survival (each decision withstands its strongest counter — see sensemaking Phase 3); Fertility (each decision spawns downstream inquiry tracks); Actionability (an engineer reading these 5 decisions can start work on day 1); Mechanism independence (Combination + Constraint Manipulation + Absence Recognition + Lens Shifting all converge on the same 5 decisions). PASS.

---

### P4 — Layer A: Format-Layer Concepts (8)

**Principal candidate (content):**

> **A1. Canonical intake format = Pandoc-md-superset.** *[DECIDE-NOW]* The internal representation every source converts into; Pandoc-extended markdown with footnotes / pipe_tables / definition_lists / citations / yaml_metadata_block / raw_attribute. [grounding: Decision 1 + Pandoc-fact]
>
> **A2. Accepted user-provided formats = PDF (born-digital or scanned), docx, RTF, md, EPUB, html, plain text.** *[DECIDE-NOW]* Pandoc handles 6 of 7 natively; PDF-without-text-layer routes via OCR sub-pipeline (A3) before Pandoc. [grounding: Decision 5 + Pandoc-fact]
>
> **A3. OCR sub-pipeline (Tesseract + OCRmyPDF).** *[DESIGN-NEXT-INQUIRY]* Sub-pipeline configuration: OCRmyPDF wrapping Tesseract; per-document language tags; layout-analysis flags; quality threshold for fallback. The detection mechanism (text-layer present? → route to Pandoc; absent? → route to OCR) is itself a design decision. [grounding: Decision 5 + Pandoc-fact (`pdftotext`-readable signals)] Frontier-pointer: F6.
>
> **A4. Pandoc invocation per format.** *[DESIGN-NEXT-INQUIRY]* Per-format reader flags: `--from=docx`, `--from=rtf`, `--from=epub`, `--from=html`, `--from=markdown`; extension set `+footnotes+pipe_tables+definition_lists+citations+yaml_metadata_block+raw_attribute`; `--standalone --wrap=none --extract-media=<dir>` for figure handling. [grounding: Pandoc-fact: `man pandoc`] Note: exact flag set per format is downstream; the principle is "Pandoc with the canonical extension set."
>
> **A5. Format detection / sniffing.** *[ENGINEER]* When file extension is unreliable: magic-bytes inspection (`%PDF-` / `PK\x03\x04` for docx-as-zip / `{\rtf` / etc.), MIME-type detection via `python-magic` or `libmagic`. Falls back to extension if magic-bytes are inconclusive. [grounding: standard libmagic behavior — extrapolation flagged but well-known]
>
> **A6. Mixed-script + RTL handling.** *[DESIGN-NEXT-INQUIRY]* Risale-i Nur shape: Turkish + Arabic interleaved; diacritics meaning-bearing; ligatures (Arabic) and combining characters need NFC normalization. Detector design: per-paragraph script-fraction + langid signals → tag as non-main-language span (feeds `NonMainLangPartsPolicy`). [grounding: schema reference (NonMainLangPartsPolicy) + sensemaking KI2 substrate]
>
> **A7. Pandoc-AST → IntakeDoc mapping.** *[ENGINEER]* Walk Pandoc's AST (Pandoc emits a Haskell-typed tree; the python `pandoc` library exposes it as nested dicts): `Header` → Chapter/Section; `Para` → Paragraph; `Note` → footnote (apparatus); `Span` with `lang` attribute → non-main-language span; `Div` with custom class → marginalia / formulaic-opening (per attribute conventions). [grounding: Pandoc-fact: AST documented at pandoc.org/lua-filters.html]
>
> **A8. Format-fidelity gradient.** *[DEFER (v1+)]* The measurement of conversion loss along PDF → Pandoc-md-superset → IntakeDoc. Per-stage metrics (chars-preserved-%, structure-elements-preserved-%, apparatus-resolution-%). Out-of-scope for v0.2; record in Frontier.

**Mechanism log:**
- *Combination:* schema-grounding + Pandoc-fact-grounding → per-concept anchors.
- *Domain Transfer:* libmagic from Linux filesystem → A5 format-detection.
- *Domain Transfer (NATIVE source-domain guard):* Pandoc's documented AST = computing-native source for A7's mapping spec.
- *Absence Recognition (patch-level):* Pandoc CLI flag set is documented but uncodified for this project → A4 names them.

**5-test:** PASS — each concept actionable; A4 + A7 cite Pandoc-fact; A6 cites schema; downstream-pointers explicit.

---

### P5 — Layer B: Structure-Layer Concepts (12; includes 7-detector sub-cluster)

**Principal candidate (content):**

> **B1. The structure-vs-style distinction (AXIOM).** *[DECIDE-NOW]* Intake preserves STRUCTURE (hierarchical containment + apparatus + semantic emphasis). Intake drops STYLE (font face / size / color / decorative typography). Italic and bold are preserved as SEMANTIC primitives (italic-as-emphasis / bold-as-strong-emphasis), not as typography. [grounding: Decision 2]
>
> **B2. Hierarchical containment (tree-as-primary).** *[DECIDE-NOW]* Document → Chapter → Section → Paragraph. Each leaf is a paragraph; each paragraph carries inline runs (text + markers). Containers carry an optional title. [grounding: Decision 3]
>
> **B3. Footnotes.** *[ENGINEER]* Pandoc-md-superset's `[^id]` footnote syntax → IntakeDoc.apparatus.footnotes[id] = FootnoteNode. Paragraph runs reference footnotes via MarkerRun{type: footnote-ref, ref-id: id}. [grounding: Pandoc-fact]
>
> **B4 — B10. The 7 perception detectors.** *Each tagged [DESIGN-NEXT-INQUIRY]*. The shared shape per detector:
>
> | # | Policy fed (schema) | Perception signals (heuristic + structural) | IntakeDoc representation |
> |---|---|---|---|
> | **B4** | `NonMainLangPartsPolicy` | Script change (Unicode script property: Arabic ↔ Latin); langid per-segment (e.g., `langid.py`, `cld3`); explicit `lang=` attributes from source markup | `apparatus.non_main_lang_spans[id]` with `{lang, script, body}` + MarkerRun reference inline |
> | **B5** | `SourceApparatusPolicy` | Pandoc note nodes (`[^id]`); marginalia signals — docx margin-comments / EPUB aside-elements / md custom-div `:::marginalia`; heuristic: short author-voice spans adjacent to body paragraphs | `apparatus.marginalia[id]` + MarkerRun{type: marginalia-ref} |
> | **B6** | `VoiceMarkingPolicy` | Quotation marks (curly + straight); blockquote elements; explicit-attribution patterns ("X said:"); structural shift in tense/register | `apparatus.voice_transitions[id]` with `{voice: author \| cited \| student, body-range}` |
> | **B7** | `ArchaicRegisterPolicy` | Lexical signals (archaic vocabulary lists per source-language); syntactic signals (verb-conjugation patterns); explicit markup (e.g., `<sic>` in TEI) | `apparatus.archaic_register_marks[id]` with `{span-range, signals}` |
> | **B8** | `HonorificsPolicy` | Suffix patterns after personal names per tradition (Islamic: ﷺ / [ر] / [ع] / SAW / AS / RA; Hindu: śrī; academic: PhD / Esq.; military rank); presence detected via regex + named-entity adjacency | `apparatus.honorifics[id]` with `{name-span, honorific-token, tradition}` |
> | **B9** | `FormulaicOpeningPolicy` | Section-opening templates per tradition (Islamic: Bismillah / al-Hamdu; legal: "Whereas..."; academic dedication patterns); always at start of major section | `apparatus.formulaic_openings[id]` with `{template-match, body, position: section-start}` |
> | **B10** | `EmbeddedPoetryPolicy` | Verse-shaped formatting (line-breaks + indentation different from prose); meter signals (per-language); attribution patterns ("Mevlana says:") | `apparatus.embedded_poetry[id]` with `{body, attribution, verse-shape}` |
>
> [grounding for all 7: schema reference (`schemas.py:18-122`) + sensemaking Decision 4]
>
> **B11. Frontmatter / Backmatter / TOC.** *[ENGINEER]* Three structural boundaries. Frontmatter = pre-body content (cover, copyright, dedication, foreword, TOC). Backmatter = post-body content (appendix, glossary, index, colophon). TOC = generated from heading levels (h1/h2/h3) OR present in source frontmatter as enumerated list. Each is a top-level container in IntakeDoc.body alongside Chapter. [grounding: standard book structure — extrapolation flagged but well-known]
>
> **B12. Emphasis as structural primitive.** *[ENGINEER]* Pandoc emits `Emph` (italic) and `Strong` (bold) AST nodes. Map: `Emph` → InlineRun{style: emphasis}; `Strong` → InlineRun{style: strong}. Both preserved as semantic; downstream translation respects emphasis when rendering. [grounding: Pandoc-fact + Decision 2]

**Mechanism log:**
- *Combination:* schema's 7 policies × Pandoc's AST node types → per-detector mapping table.
- *Constraint Manipulation (ADD):* added "every detector must name policy fed + signals + IntakeDoc rep" → forced uniform structure across 7 detectors.
- *Domain Transfer:* `langid.py` / `cld3` from NLP-langid domain → B4 perception signals.
- *Absence Recognition:* footnote syntax already covered by Pandoc → no design inquiry needed (B3 = ENGINEER not DESIGN-NEXT).

**5-test:** PASS — each of the 12 concepts grounded; 7 detectors uniformly framed; each names a policy + signals + representation.

---

### P6 — Layer C: Pipeline-Layer Concepts (10)

**Principal candidate (content):**

> **Stage ordering (parse → normalize → segment → validate → hand-off):**
>
> ```
> [source file]
>    │
>    ▼
> C7 Pre-validation (format supported? size sane? readable?)
>    │
>    ▼
> C3 Parse (Pandoc → AST; or OCR → text-layer-PDF → Pandoc → AST)
>    │
>    ▼
> C4 Normalize (Unicode NFC; whitespace canonical; line-endings; punctuation)
>    │
>    ▼
> C5 Segment (AST → IntakeDoc tree containers; per-paragraph runs)
>    │
>    ▼
> C9 Metadata + language + encoding detection (populate IntakeDoc.metadata)
>    │
>    ▼
> C8 Post-parse validation (IntakeDoc against schema; structural sanity heuristics)
>    │
>    ▼
> [IntakeDoc handed to translate stage]
> ```
>
> **C1. `IntakeDoc` schema design.** *[DESIGN-NEXT-INQUIRY]* The pydantic class hierarchy realizing Decision 3's shape. Field types for each container + apparatus collection; validators; versioning. **The single largest design task downstream of this finding.** [grounding: Decision 3]
>
> **C2. Intake-vs-translate boundary.** *[DECIDE-NOW]* Intake's output is `IntakeDoc`; translate's input is `IntakeDoc`. The boundary is the schema's contract. Intake does NOT make policy-value choices (translate's job); translate does NOT re-parse the source (intake's job). [grounding: Decision 4]
>
> **C3. Parse stage.** *[ENGINEER]* Per-format Pandoc invocation (per A4) producing Pandoc AST; PDF text-layer extraction; OCR routing for scan-only PDFs (per A3).
>
> **C4. Normalize stage.** *[ENGINEER]* Unicode NFC normalization (per Python `unicodedata.normalize('NFC', s)`); whitespace canonicalization (collapse runs of `\s` to single space within paragraphs; preserve paragraph breaks); line-ending unification (CRLF → LF); punctuation normalization (curly → straight quotes? or preserve? — per source-language convention — DEFER detail to C1 schema).
>
> **C5. Segment stage.** *[ENGINEER]* Walk Pandoc AST (per A7); construct IntakeDoc tree containers; populate paragraph runs; resolve apparatus references; populate apparatus collections via B4-B10 detector outputs.
>
> **C6. Validate stage.** *[ENGINEER]* Run IntakeDoc through schema validation (pydantic auto); run heuristic checks (e.g., "every Chapter has ≥1 Paragraph"; "every apparatus reference resolves to a collection entry"); collect violations as `IntakeWarning` items in IntakeDoc.metadata. [grounding: pydantic-fact]
>
> **C7. Pre-validation.** *[ENGINEER]* Before parsing: file readable + non-empty + size below memory threshold + format in accepted list (A2). Fail fast with named error categories (FormatUnsupported, FileEmpty, FileTooLarge).
>
> **C8. Post-parse validation.** *[ENGINEER]* See C6 (the same validation stage; C8 is a re-naming for the post-parse check vs C7 pre-parse check).
>
> **C9. Intake metadata + language detection.** *[ENGINEER]* Populate IntakeDoc.metadata: title (from YAML / docx core props / EPUB metadata / PDF title-tag / filename); author (similar); source-format (the detected format from A5); source-language (per-document langid on first-N-paragraphs); encoding (UTF-8 detected via `chardet` or `cchardet` for raw .txt). [grounding: standard practice; extrapolation flagged]
>
> **C10. Multi-file project intake.** *[DESIGN-NEXT-INQUIRY]* Risale-i Nur is a multi-volume work; one `IntakeDoc` per volume vs one IntakeDoc for the whole project? Merge-mechanics: chapter-id namespacing, cross-reference resolution across volumes, per-volume metadata. The design decision: one merged IntakeDoc (chapters are stacked; cross-refs resolve globally) vs many IntakeDocs in an IntakeProject container. [grounding: sensemaking SV5 remaining variables]

**Mechanism log:**
- *Combination:* parse + normalize + segment + validate + hand-off — borrowed from standard ETL patterns.
- *Domain Transfer (computing-native):* pydantic validation + chardet encoding detection are computing-native sources.
- *Absence Recognition:* multi-file intake not addressed elsewhere → C10 surfaces it.

**5-test:** PASS — stages ordered; per-stage anchors grounded; C1 + C10 explicitly DESIGN-NEXT-INQUIRY for known-unknowns.

---

### P7 — Layer D: Quality-Layer Concepts (8)

**Principal candidate (content):**

> **D1. Quality target = structure-preservation.** *[DECIDE-NOW]* See Decision 2. Measurement is structural-element-preservation-%, not character-preservation-% or typography-preservation-%. [grounding: Decision 2]
>
> **D2. Fidelity + lossiness framing.** *[DESIGN-NEXT-INQUIRY]* Operationalize "% of structure preserved": per-container existence (chapter/section/paragraph counts vs source signals), apparatus-resolution rate (footnotes matched to bodies, marginalia matched to positions), and emphasis preservation. The metric set design is downstream — this concept names the framing.
>
> **D3. Intake-quality-metrics.** *[DESIGN-NEXT-INQUIRY]* The concrete metric set: (a) chars-preserved-% (lossy-vs-lossless format-conversion check); (b) structure-elements-preserved-% (containers + apparatus); (c) per-chapter integrity score (does each chapter have plausible structure?); (d) apparatus-resolution-% (orphan footnotes? unresolved marker refs?). [grounding: extrapolation: standard quality-metric patterns; specific thresholds = downstream]
>
> **D4. Intake-quality-gates.** *[DESIGN-NEXT-INQUIRY]* Threshold(s) below which translation refuses to proceed. Examples: "if structure-preservation-% < 70%, require human review before translation"; "if apparatus-resolution-% < 95%, flag specific orphan items and require user resolution." Threshold values themselves are calibration-dependent — downstream inquiry.
>
> **D5. Intake-edit-after-parse.** *[DECIDE-NOW: SUPPORTED]* The IntakeDoc serializes to Pandoc-md-superset on disk (the canonical form). Users can hand-edit the markdown to fix bad parses. Re-loading the edited markdown produces an updated IntakeDoc. This is the recovery workflow for messy PDFs where Pandoc + heuristics underperform. [grounding: Decision 1 + sensemaking FP4]
>
> **D6. Paratext handling (page numbers / headers / footers).** *[DESIGN-NEXT-INQUIRY]* Default: drop (typically noise — running headers, page numbers, footer-annotations are typographic chrome, not body content). Override flag: preserve-as-metadata for specific use cases (citations referencing source pagination; critical editions where paratext is signal). Default is decision-now (drop); the override mechanism is design-next.
>
> **D7. Intake-time vs translate-time error attribution.** *[ENGINEER]* Every error carries a stage-tag in `IntakeWarning` / `IntakeError`: which stage (parse / normalize / segment / validate / OCR / metadata), which input subset, which failure category. Tracts intake errors apart from translation errors during debugging.
>
> **D8. Source-of-truth declaration.** *[DECIDE-NOW: IntakeDoc is canonical; original is read-only-after-intake]* Once intake completes, `IntakeDoc` (serialized as Pandoc-md-superset) is the canonical representation. The user's original file is preserved untouched as `_original.<ext>` and not re-read during translation. This locks the format-conversion at intake-time; downstream is monoformat. [grounding: sensemaking SP2 + FP4]

**Mechanism log:**
- *Combination:* structure-preservation + per-stage error tagging → unified quality framing.
- *Constraint Manipulation (ADD):* added "must be measurable" → forced D3 metric set surfacing.
- *Lens Shifting:* under "what makes intake debuggable in production?" → D7 attribution emerges as central.

**5-test:** PASS — quality framing operational; D5 + D8 lock the workflow; D3 + D4 explicitly downstream.

---

### P8 (META-DECISION) — Inherited Commitments Re-test

**Principal candidate (content):**

> **From articulate_simple.md — 5 considered articulations.**
>
> | Variant | Verdict | Rationale |
> |---|---|---|
> | 1 — Format-leaning, decision-now | PARTIALLY ACCEPTED | Format-layer decisions made (A1, A2 = DECIDE-NOW); layer is not standalone; this finding spans all 4 layers per sensemaking Ambiguity 1 resolution |
> | 2 — Structure-leaning, architecture-foundation | PARTIALLY ACCEPTED | Structure-layer load-bearing (B1, B2 = DECIDE-NOW); layer not standalone |
> | 3 — Pipeline-leaning, checklist | PARTIALLY ACCEPTED | Pipeline-layer = mostly ENGINEER concepts (C3-C9); becomes the engineering checklist |
> | **4 — Cross-layer breadth, enumerate-for-future-deepening** | **PRIMARY ACCEPTED** | The hybrid finding shape spans all 4 layers; 18 DESIGN-NEXT-INQUIRY items seed future inquiries |
> | **5 — Pragmatic-painpoint, enumerate-for-current-decision** | **SECONDARY ACCEPTED** | The 9 DECIDE-NOW items answer immediate decisions (5 load-bearing + 4 layer-specific) |
>
> *Re-test evidence cite:* sensemaking.md → Phase 3 Ambiguity 1 + 2 + the SV6 commitment to hybrid (layered + decision-flagged) finding shape.
>
> **From surfacing.md — 110 candidates spanning 4 layers.**
>
> *Verdict:* PRUNING HONORED.
>
> | Layer | Surfaced | Retained | Dropped |
> |---|---|---|---|
> | A. Format | 27 | 8 | 19 (LaTeX, math-notation, ligature-handling-per-format, .compldoc precursor, Pandoc-specific-tool variants subsumed-by-Decision-5, format-fidelity-gradient → DEFER, etc.) |
> | B. Structure | 36 | 12 | 24 (code blocks, captions, citation sub-types, original-vs-modernized spelling, colophons, editorial brackets, lists/tables subsumed-by-Pandoc, etc.) |
> | C. Pipeline | 27 | 10 | 17 (logging detail, streaming-vs-load-all, schema-versioning-machinery, audit-trail detail, intake-reproducibility tests, etc.) |
> | D. Quality | 20 | 8 | 12 (round-trippability framing subsumed-by-D5, reference-intake DEFER, inter-intake-diffing DEFER, "good-intake = downstream-success" framing subsumed-by-D1, etc.) |
> | **Total** | **110** | **38** | **72** |
>
> *Pruning purpose-bias check:* 38 retained all have downstream consequences for ≥1 of `[unblock-real-painpoint / avoid-architecture-debt / scope-the-engineering-task / meta-reframe]`. Dropped 72 are either: edge cases beyond Risale-i Nur calibration; redundant under Pandoc-md-superset commitment; v1+ scope; framing duplicates of retained concepts.
>
> *Re-test evidence cite:* sensemaking.md → Inherited Commitments Re-test section + this finding's P2 methodology disclaimer.
>
> **From SKILL/references/config/schemas.py — 7 policy classes.**
>
> *Verdict:* RESPECTED + EXTENDED (perception/rendering split).
>
> Each of the 7 policies (`NonMainLangPartsPolicy`, `SourceApparatusPolicy`, `VoiceMarkingPolicy`, `ArchaicRegisterPolicy`, `HonorificsPolicy`, `FormulaicOpeningPolicy`, `EmbeddedPoetryPolicy`) is unchanged at the schema level — no Literal values added or removed. The finding's contribution is naming the perception-side of each policy (B4-B10 detectors) and committing the IntakeDoc representation for each policy's target element. No redefinition.
>
> *Re-test evidence cite:* `schemas.py:18-122` (the 7 policy classes) + this finding's Decision 4 + B4-B10 detector specs.
>
> **From the Mac-app session substrate (v0.1 finding + ContentView/LLMClient code).**
>
> *Verdict:* OUT-OF-FRAME (MQ4 exclusion).
>
> The v0.1 Mac app's UI surface (toolbar gear, Config sheet, pickers), the LLMClient's single-call no-chunking translation, and the AppSettings persistence model are all out-of-frame for this intake-handling concepts inquiry. Frontier flag F4 carries the eventual re-entry: when intake is built (v0.2+), the app needs an "intake document" button + a quality-report dialog. That work is downstream of this finding, not within it.
>
> *Re-test evidence cite:* `_branch.md` MQ4 exclusions + Frontier F4.

**Mechanism log:**
- *Combination:* prior-finding pointers × per-inheritance-source verdict table → unified re-test record.
- *Absence Recognition (patch-level):* prior inquiries do not have inheritance-re-test sections; this finding adds the pattern.

**Piece-Level Inversion (required — P8 is meta-decision via relationship-label property):**

> *Inversion-candidate:* what if the inherited commitments should be REJECTED in this finding rather than respected?
>
> *What follows:* (a) Reject articulate_simple's 5 variants → re-articulate from scratch; the user would lose the framing baseline. (b) Reject surfacing's 110 → re-survey from scratch; the user would lose the pruning rationale. (c) Reject schemas.py's 7 policies → redefine them; THIS violates the inquiry's MQ4 exclusion (translation-internals-out). (d) Reject MQ4 exclusion of Mac-app → app-UI questions re-enter; violates the user's "stop dealing with appification" framing.
>
> Verdict on inversion: **rejected for each inheritance**. The schema rejection is structurally forbidden by MQ4; the other rejections destroy the inquiry's traceability. The principal direction (respect inheritances; document re-test verdicts) stands.

**5-test:** PASS — each inheritance has a verdict with cited evidence; inversion candidates surfaced and rejected on structural grounds.

---

### P9 — Frontier flags F1-F6 resolution + Next Actions + Open Questions

**Principal candidate (content):**

> **Frontier flag resolutions:**
>
> | # | Surfacing flag | Resolution in this finding |
> |---|---|---|
> | F1 | IntakeDoc schema shape | **RESOLVED at shape level** by Decision 3 (tree-of-containers + cross-ref-flat). **ESCALATED at field level** as C1 DESIGN-NEXT-INQUIRY. |
> | F2 | Canonical intake format choice (md / md+RTF / Pandoc-md-superset / custom) | **RESOLVED** by Decision 1 (Pandoc-md-superset). |
> | F3 | Quality-target trichotomy (structure / typography / semantic-only) | **RESOLVED** by Decision 2 (structure-preservation). |
> | F4 | Where Mac-app re-enters | **DEFERRED to post-build.** When intake stage exists, the app needs (i) intake-document button, (ii) quality-report dialog showing D3 metrics, (iii) hand-edit recovery flow per D5. Out-of-frame for this finding. |
> | F5 | 7 policies' intake-vs-translate attribution | **RESOLVED** by Decision 4 (perception/rendering split) + B4-B10 detector specs. |
> | F6 | OCR sub-pipeline depth | **ESCALATED** as A3 DESIGN-NEXT-INQUIRY. |
>
> **Next-actionable inquiries (priority order):**
>
> 1. **Design the IntakeDoc pydantic schema** (C1 — the largest single design task; ~1-2 weeks). Output: a `comprehenslate/intake/schema.py` module with the typed tree containers + apparatus collections; validators; round-trip Pandoc-md-superset serialization. Spawn as `/traverse`.
>
> 2. **Design the 7 perception detectors** (B4-B10 — 7 sub-inquiries, can run in parallel; ~1 week each). Per detector: perception-signals algorithm (heuristics + ML if needed); IntakeDoc representation (apparatus collection field-level); detection-quality metric. Spawn as 7 `/traverse` inquiries (or 7 `/aMVLwr` for tighter scope per detector).
>
> 3. **Prototype Pandoc → IntakeDoc on a single Risale-i Nur PDF** (A7 + A3 + B4 + B6 + B8 + B9 — validation work; ~1 week). Output: a runnable script that takes one PDF and emits a populated `IntakeDoc`, with quality metrics reported. This is the integration test for decisions 1-5.
>
> 4. **Design the OCR sub-pipeline** (A3 — when scan-only PDFs need to be processed; ~3-5 days). Output: a config + script wrapping Tesseract via OCRmyPDF; per-document language tags; layout-analysis flags; fallback rules.
>
> 5. **Design multi-file project intake** (C10 — when the corpus is multi-volume; can defer until project-level intake is needed; ~3-5 days).
>
> 6. **Design intake-quality-metrics** (D3 + D4 — once detectors exist; ~3-5 days). Output: concrete metric formulas + threshold defaults for D4 gates.
>
> **Open questions (explicit; not silently dropped):**
>
> - Should `IntakeDoc` carry a `version` field so future schema migrations are tractable? (Likely yes; design at C1.)
> - Should intake be re-runnable on the same source idempotently (same source → identical `IntakeDoc` modulo timestamp)? (Likely yes; engineering property — guidance at C1.)
> - When intake encounters a partial failure (parse succeeds for chapters 1-5 but fails on chapter 6), should it (a) refuse and require user fix, (b) emit a partial IntakeDoc with warnings, or (c) prompt the user mid-run? (Out-of-frame; surfacing C11 candidate dropped; revisit at C1 design.)
> - The default for paratext (page numbers / running headers): drop. But when does the user need to override? (D6 DESIGN-NEXT-INQUIRY.)

**Mechanism log:**
- *Combination:* surfacing's F-flag set × this finding's decision/concept content → resolution table.
- *Extrapolation:* current sensemaking commitments + likely engineering durations → next-action priority order.
- *Absence Recognition:* "what's not yet asked about intake?" → open questions list.

**5-test:** PASS — all 6 F-flags addressed (not silently dropped); next-actions specific + ordered + sized; open questions explicit.

---

### P4-P7 cross-check (Layer B 7-detector sub-cluster — DV2 trigger note)

The 7 detectors (B4-B10) form a sub-cluster within P5 that, per Decomposition's self-eval, was flagged for DV2 if Innovation found them too heavy. Verdict: **NOT triggered.** Each detector fits in a single table row with a uniform shape (policy + signals + representation); the sub-cluster compresses cleanly. No DV2 split needed.

---

### P1 — Executive summary (produced LAST per dependency order)

**Principal candidate (content):**

> **What this finding answers, in one paragraph.** Document intake — the stage that converts a user-provided source file into the canonical representation translation operates on — comprises **38 concepts spanning 4 layers**: 8 about format (PDF / docx / RTF / md / EPUB / html / .txt → canonical), 12 about structure (chapters / paragraphs / footnotes / marginalia / verses / etc.), 10 about pipeline (parse / normalize / segment / validate / hand-off), and 8 about quality (fidelity / metrics / gates / hand-edit recovery). Of the 38, **9 are decided now**, **18 need their own downstream design inquiry**, **11 are engineering work**, and **1 is deferred to v1+**. Five load-bearing decisions undergird the list: **(1)** canonical intake format = Pandoc-md-superset; **(2)** quality target = structure-preservation; **(3)** `IntakeDoc` shape = tree-of-containers + cross-referenced flat collections; **(4)** the 7 schema policies split into intake-perception + translate-rendering halves; **(5)** Pandoc as architectural lever, OCR (Tesseract + OCRmyPDF) as depth-1 sub-pipeline for scan-only PDFs. The list answers the user's question — *"what intake handling concepts do we need to figure out?"* — and routes the unanswered design work into typed downstream tracks rather than leaving it implicit.

**Mechanism log:**
- *Combination:* the 5 decisions + the layer/status grid → one-paragraph digest.
- *Lens Shifting:* under "what does the reader want at-a-glance?" → numbers + names + decisions, not narrative.

**5-test:** PASS — answers the user's literal question; sized for one-paragraph reading; points to the substantive sections.

---

## Inherited Frame Audit (between Phase 2 and Phase 3)

**Step (i) — Seed central assumption.** The seed framing assumes: *"Decomposition's 9 pieces are the seed structure"* + *"5 load-bearing decisions"* are committed. Central assumption: **the 5 decisions are correct and the 9 pieces are sufficient.**

**Step (ii) — Per-piece commitments.** P2 (framing-semantic + lesson-vocabulary), P3 (5 architectural decisions), P8 (relationship-label) are the meta-decision pieces.

**Step (iii) — Challenge scan.** Are there candidates challenging the seed's central assumption?
- P3 Piece-Level Inversion ran per-decision inversions and rejected each on structural grounds with sensemaking-cited evidence.
- P2 Piece-Level Inversion ran the "raw-list-without-grounding" inversion and rejected on user-painpoint-grounded evidence.
- P8 Piece-Level Inversion ran the "reject-inheritances" inversion and rejected on MQ4 + traceability grounds.
- The seed's central assumption (5 decisions correct; 9 pieces sufficient) HAS been challenged via the per-piece inversions + the methodology-mode alternative consideration (Phase 1 Seed).

**Step (iv) — Firing condition.** Audit does **NOT fire**. Every meta-decision piece's commitment received an explicit inversion-candidate; the seed-level methodology-mode also surfaced an alternative; all were tested + rejected with structural reasons. Proceed to Phase 3 Test.

---

## Phase 3 — Test + Assembly

### Per-piece 5-test summary

All 9 pieces' principal candidates passed the 5-test cycle (logged per-piece above). Inversion candidates at P2 / P3 / P8 were generated and rejected with structural reasoning — compliance per the Piece-Level Inversion Rule.

### Assembly check

> **Does the architecture emerge from the 9 pieces' assembly?**
>
> **YES.** The 5 decisions (P3) define the architectural commitments; the 4 layer-lists (P4-P7) populate the consequences across format/structure/pipeline/quality; the methodology (P2) explains the pruning; the re-test (P8) carries inheritance traceability; the frontier (P9) routes onward work; the summary (P1) gives readers the digest. The whole is greater than the parts — the inquiry produces both an actionable list AND a foundation for v0.2 engineering AND a queue of downstream design inquiries.

### Axis coverage check

Orthogonal axes the candidate space varies along:
- **Layer-axis** (format / structure / pipeline / quality) — varied: 8 / 12 / 10 / 8 candidates.
- **Status-axis** (DECIDE-NOW / DESIGN-NEXT-INQUIRY / ENGINEER / DEFER) — varied: 9 / 18 / 11 / 1.
- **Source-axis** (schema / Pandoc-fact / sensemaking-anchor / extrapolation) — varied: each grounding source has multiple anchored concepts.
- **Time-axis** (immediate decisions vs near-term design vs deferred) — varied via status tags.

All 4 orthogonal axes have ≥1 candidate variant. No single-axis collapse. PASS.

### Per-row mechanism-trace

The 7 detectors (B4-B10) each have explicit mechanism work (Combination of schema policy × Pandoc AST signals); the 5 decisions each have explicit mechanism work (per the Mechanism log entries under P3). No row-baseline silent inheritance.

---

## Telemetry

### Mechanism Coverage

- **Generators applied:** 4 / 4 (Combination · Absence Recognition · Domain Transfer · Extrapolation)
- **Framers applied:** 3 / 3 (Lens Shifting · Constraint Manipulation · Inversion)
- **Coverage:** FULL (all 7 mechanisms applied across the 9 pieces)
- **Convergence:** YES — Combination + Absence Recognition + Domain Transfer + Constraint Manipulation all converge on the 5 load-bearing decisions through different paths (high confidence).
- **Survivors tested:** 9 / 9 principal candidates + 3 Inversion-candidates (P2, P3, P8) = 12 / 12 candidates tested.
- **Failure modes observed:** None.

### Production-task additional telemetry

| Piece | Mechanisms | Classification | Inversion compliance |
|---|---|---|---|
| P1 | Combination, Lens Shifting | content-production | n/a |
| P2 | Constraint Manipulation (ADD + REMOVE), Absence Recognition (patch + redesign), **Inversion** | **meta-decision** | **satisfied** |
| P3 | Combination, Constraint Manipulation (ADD + REMOVE), Absence Recognition (patch + redesign), Lens Shifting, **Inversion (per-decision)** | **meta-decision** | **satisfied** (intervention-shape inapplicable — recorded above) |
| P4 | Combination, Domain Transfer (computing-native guard fired: libmagic + Pandoc AST), Absence Recognition | content-production | n/a |
| P5 | Combination, Constraint Manipulation (ADD), Domain Transfer, Absence Recognition | content-production | n/a |
| P6 | Combination, Domain Transfer (computing-native: pydantic + chardet), Absence Recognition | content-production | n/a |
| P7 | Combination, Constraint Manipulation (ADD), Lens Shifting | content-production | n/a |
| P8 | Combination, Absence Recognition, **Inversion** | **meta-decision** | **satisfied** |
| P9 | Combination, Extrapolation, Absence Recognition | content-production | n/a |

### Verdict

**PROCEED** — full mechanism coverage; convergence on the 5 load-bearing decisions through 4+ mechanisms; all candidates tested; all 3 meta-decision pieces compliant with Piece-Level Inversion; Inherited Frame Audit did not fire; Assembly + Axis coverage + Per-row mechanism-trace all PASS. No failure modes observed.
