---
status: active
model: claude-opus-4-7
effort: max
---
# Finding: Document Intake Handling Concepts

## Question

The user, mid-session, asked to step away from Mac-app UI work ("appification") and turn attention to what they named the real painpoint: **document intake** — the stage that takes a user-provided source file (PDF, .docx, .md, RTF, EPUB, HTML, plain text) and converts it into a representation the rest of comprehenslate's translation pipeline can operate on. The literal ask was *"identify a list of intake-handling concepts we need to figure out."* The user's substrate examples leaned format-layer (PDF formatting can be bad → convert to markdown first → markdown has limitations → maybe RTF as a standard intake format alongside markdown for complicated texts).

The goal as articulated in `_branch.md` is to produce a list-shaped artifact that serves one or more of four motivations: **unblock the painpoint** (PDF intake quality is currently an obstacle); **avoid architecture debt** (choose deliberately now rather than rework later); **scope the engineering task** (without a list, intake work is unbounded); **meta-reframe** (re-ground the project in its actual painpoint after a session of UI work). Explicitly out of scope: the Mac app's UI surface, and the translation-stage internals downstream of intake.

---

## Finding Summary

- **The list spans four layers, not just format.** The user's examples were format-leaning, but the request — *intake handling concepts* — is broader. Format is one layer; the others are structure (what intake must perceive within the parsed source), pipeline (the stages that produce the parsed source), and quality (how well the parsing preserved what mattered). Treating these as alternatives loses the relationships; treating them as aspects of one problem keeps them.

- **38 concepts total** — 8 format-layer, 12 structure-layer, 10 pipeline-layer, 8 quality-layer — pruned from 110 candidates by keeping concepts that are either named in the existing schema (`SKILL/references/config/schemas.py`), have downstream consequences for translation quality, or require a v0.2+ engineering decision; dropping concepts that are edge cases beyond the calibration corpus, redundant under the canonical-format choice below, or v1+ scope.

- **Each concept carries a decision-status tag.** 8 are **DECIDE-NOW** (committed in this finding plus 1 architectural principle), 18 are **DESIGN-NEXT-INQUIRY** (need their own design before engineering), 11 are **ENGINEER** (well-defined, ready for code), 1 is **DEFER** (v1+ scope).

- **Five load-bearing decisions** underwrite the list and are the reason a 38-concept list is sufficient rather than the 110-candidate surface area the inquiry started from:
   - **Decision 1** — **Canonical intake format = Pandoc-md-superset.** The internal representation that every source converts into is Pandoc's extended markdown (with footnotes, tables, definition lists, citations, YAML frontmatter, and raw-attribute escapes). Vanilla CommonMark lacks needed primitives for the calibration corpus (footnotes for marginalia); RTF is editor-fragile; a custom format is v1+ scope.
   - **Decision 2** — **Quality target = structure-preservation.** Intake's success metric is whether structural elements (chapters, sections, paragraphs, footnotes, marginalia, embedded poetry, formulaic openings, voice transitions, archaic register markers, non-main-language spans) survived. Raw typography (font face / size / color) is rendering decoration that translation cannot use; semantic emphasis (italic-as-emphasis, bold-as-strong-emphasis) is preserved.
   - **Decision 3** — **`IntakeDoc` shape = tree-of-containers + cross-referenced flat collections.** The schema produced by intake is a tree (Document → Chapter → Section → Paragraph) where leaf nodes carry inline content with markers; markers reference flat collections at the root holding the apparatus (footnotes, marginalia, embedded poetry, formulaic openings, non-main-language spans, voice transitions, honorifics, archaic register marks). The tree gives chapter-context for chunking; the cross-referenced flat collections give apparatus by reference rather than mis-nested in the tree.
   - **Decision 4** — **The 7 schema policies split.** Each of the 7 policy classes in `SKILL/references/config/schemas.py` (`NonMainLangPartsPolicy`, `SourceApparatusPolicy`, `VoiceMarkingPolicy`, `ArchaicRegisterPolicy`, `HonorificsPolicy`, `FormulaicOpeningPolicy`, `EmbeddedPoetryPolicy`) has two halves: **intake-time perception** (the detector finds the policy's target element in the source and represents it in `IntakeDoc`'s apparatus collections) and **translate-time rendering** (the Literal choice in `TranslationConfig` is applied to translation output). The policy's value is vacuous without intake having perceived its target.
   - **Decision 5** — **Pandoc as architectural lever; Tesseract + OCRmyPDF as depth-1 OCR sub-pipeline.** Pandoc handles conversion from 6 of 7 accepted user-provided formats (.docx, RTF, .md, EPUB, HTML, plain text). PDFs with text layers route through Pandoc directly; scan-only PDFs (no text layer) route through an OCR sub-pipeline using OCRmyPDF as a wrapper around Tesseract before flowing into Pandoc. Writing per-format parsers from scratch is unnecessary engineering cost.

- **The list serves both immediate decisions and downstream work.** The 8 DECIDE-NOW items answer immediate questions (what canonical format? what quality target? what is `IntakeDoc`? what's the source-of-truth?); the 18 DESIGN-NEXT-INQUIRY items name sub-inquiries that should run before their engineering (the seven policy-perception detectors; OCR sub-pipeline configuration; multi-file project intake; quality metrics); the 11 ENGINEER items are ready for code once `IntakeDoc` exists; the 1 DEFER item (format-fidelity gradient measurement) is v1+ scope.

---

## Finding

### Why this list, and what the layers mean

Comprehenslate is a translation skill for any document, calibrated against theological and layered religious-philosophical prose (the calibration anchor is currently Said Nursi's Risale-i Nur), not scoped to it. The translation stage already has a defined contract: an existing schema (`SKILL/references/config/schemas.py`) lists 8 fields of user-facing translation strategy, 6 fields of runtime engine knobs, and 7 typed policy classes — `NonMainLangPartsPolicy` for non-main-language quotes and references, `SourceApparatusPolicy` for the source's pre-existing marginalia and glosses, `VoiceMarkingPolicy` for transitions between author voice and cited authority, `ArchaicRegisterPolicy` for archaic language register, `HonorificsPolicy` for deferential and relational honorifics, `FormulaicOpeningPolicy` for invocations and dedicatory formulae, and `EmbeddedPoetryPolicy` for verses embedded in prose. What does NOT yet have a defined contract is the stage upstream of translation: **intake** — the conversion from "a user's PDF / .docx / .md / RTF / EPUB / HTML / .txt file" into the representation translation operates on.

The current Mac app (v0.1) sends raw source text in a single LLM call. That works for small pastes; it cannot work for a real book where chapter/paragraph/footnote structure carries meaning the translation must respect. v0.2 needs a real intake stage. This finding is the design substrate for that work.

The list spans **four layers** because they are aspects of one problem at four cuts, not four alternative problems:

- **Format-layer concepts** — what file types intake accepts; how each is converted into the canonical internal representation; what conversion tools the intake stage relies on.
- **Structure-layer concepts** — what elements within the parsed source intake must perceive (chapters, paragraphs, footnotes, marginalia, etc.) so translation can honor them; what semantic distinctions matter (structure vs style; emphasis vs typography).
- **Pipeline-layer concepts** — what stages intake comprises (parse → normalize → segment → validate → hand-off-to-translate); what the intake/translate boundary is; how intake metadata is extracted.
- **Quality-layer concepts** — what intake quality means; how to measure it; how to gate translation on intake quality; how to recover when intake degrades.

You cannot pick a canonical format without knowing what structure intake must preserve. You cannot define what intake must preserve without knowing what perception stages produce it. You cannot validate intake without defining what quality means. Treating these as separable would leave decisions implicit and architecture debt under each of them.

### The five load-bearing decisions in detail

#### Decision 1 — Canonical intake format = Pandoc-md-superset

The internal representation every source document converts into is **Pandoc's extended markdown** — the CommonMark base plus the Pandoc-native extensions `footnotes`, `pipe_tables` (also `multiline_tables`), `definition_lists`, `citations`, `yaml_metadata_block` (for metadata + apparatus references), and `raw_attribute` (for inline tag-escapes when needed). YAML frontmatter carries document metadata; the body markdown carries the tree structure.

Why this choice:

1. **Vanilla CommonMark alone is insufficient.** It does not natively support footnotes (which intake needs for marginalia per `SourceApparatusPolicy`), tables (which intake needs for apparatus criticus in critical-edition sources), or definition lists (which intake needs for glossary terms). Trying to represent these in pure CommonMark requires custom inline syntax — which is effectively reinventing Pandoc-md-superset under a different name.

2. **Pandoc is the universal converter for the 6 non-PDF accepted formats.** Picking Pandoc's extended markdown as the canonical means a single internal parser surface — the Pandoc reader emits an Abstract Syntax Tree that intake walks to produce `IntakeDoc`. No per-format custom parser is needed for .docx, RTF, EPUB, HTML, plain text, or markdown.

3. **It is human-readable and hand-editable.** This supports the recovery workflow (Decision 5 in the quality layer): when auto-parse underperforms on a messy PDF, the user can hand-edit the markdown to fix the parse, and intake re-loads the edited markdown into an updated `IntakeDoc`. RTF would defeat this workflow because RTF is editor-fragile — the same RTF file looks different across Microsoft Word, Apple Pages, and TextEdit.

What's foreclosed:

- Vanilla CommonMark as canonical (lacks needed primitives).
- RTF as canonical (editor-fragility defeats hand-editing; format-fragmentation across editors).
- A custom format (e.g., `.compldoc` precursor) for v0.2 (significant engineering cost; reinvents Pandoc; v1+ scope).

**Legitimate concern preserved:** Pandoc-md-superset is **less portable** than vanilla CommonMark — readers and tools that only support CommonMark cannot render its extensions. The decision accepts this because the chosen canonical is **internal** (intake-time only); user-provided documents can still be vanilla markdown, and the conversion to Pandoc-md-superset happens at intake time. Users do not need Pandoc to read or share what they originally provided.

Revisitability: medium. If scaling beyond the calibration corpus reveals primitives Pandoc-md-superset cannot express (e.g., complex mathematical notation requiring MathML, music notation), revisit by either adopting Pandoc's `raw_html`/`raw_tex` escape hatches or graduating to a custom `.compldoc` format.

#### Decision 2 — Quality target = structure-preservation

Intake's success is measured by **structural-element-preservation percentage** against the source: chapter and section boundaries preserved; paragraph boundaries preserved; the seven policy-target elements (footnotes, marginalia, embedded poetry, formulaic openings, voice transitions, archaic register markers, non-main-language spans) detected and represented in the apparatus collections; semantic emphasis (italic-as-emphasis, bold-as-strong-emphasis) preserved as a structural primitive.

Why this target rather than the alternatives:

1. **The user's painpoint is structural loss.** "PDF formatting can be really bad" describes exactly this — column boundaries collapse, paragraph breaks vanish, footnotes detach from their bodies, hyphenation creates spurious word splits. The painpoint demands structure-first.

2. **The seven schema policies operate on structural elements.** Without intake having perceived marginalia, `SourceApparatusPolicy.translate-as-footnote` has nothing to apply to. Without intake having perceived embedded poetry, `EmbeddedPoetryPolicy.preserve-original-with-prose-gloss` is a vacuous setting. The quality target's purpose is to ensure the policies have what they need.

3. **Raw typography is rendering decoration, not structural meaning.** Font face, font size, color choice are typesetting decisions translation cannot use. Preserving them would commit `IntakeDoc` to carrying rendering state translation cannot use.

What's foreclosed:

- Typography-fidelity as a primary goal (includes too much rendering noise; misses chapter-level structure that is visible only through heading-typography signals).
- Semantic-only stripping (drops chapter/paragraph boundaries that chunking requires; `PipelineConfig.chunking_granularity = "chapter"` is a real schema option that depends on intake having preserved chapter boundaries).

**Legitimate concern preserved:** Typography can sometimes carry meaning. A chapter's font can signal a genre shift; calligraphic display in Arabic religious texts can be meaning-bearing; a critical edition's italic styling can mark editorial insertion. Structure-preservation drops these signals. The decision accepts this because (a) these cases are rare in prose-shaped texts that comprise the dominant intake workload, (b) an override exists at the paratext-handling design-next-inquiry where a user can flag a specific text as typography-sensitive, and (c) preserving raw typography for the common case would force every `IntakeDoc` to carry rendering state translation cannot use.

Revisitability: low. The target is load-bearing for `IntakeDoc` field design and the seven perception detectors.

#### Decision 3 — `IntakeDoc` shape = tree-of-containers + cross-referenced flat collections

`IntakeDoc` is structured as a **tree** of typed containers (Document → Chapter → Section → Paragraph) where each leaf node carries inline content with embedded markers; the markers reference **flat collections at the `IntakeDoc` root** for the apparatus (footnotes, marginalia, embedded poetry, formulaic openings, non-main-language spans, voice transitions, honorifics, archaic register marks).

A schema sketch (illustrative shape, not the final field schema — the field design is the largest single design task downstream of this finding):

```
IntakeDoc:
    metadata: { title, author, source-format, source-language, intake-time, intake-version }
    body: Document
        children: [ Chapter | FrontMatter | BackMatter ]
            Chapter:
                title: InlineText
                children: [ Section | Paragraph ]
                    Section: { title, children: [ Section | Paragraph ] }
                    Paragraph:
                        runs: [ TextRun | MarkerRun ]
                            MarkerRun: { type, ref-id → root collection }
    apparatus:
        footnotes:              Dict[id, FootnoteNode]
        marginalia:             Dict[id, MarginaliaNode]    # SourceApparatusPolicy target
        embedded_poetry:        Dict[id, PoemNode]          # EmbeddedPoetryPolicy target
        formulaic_openings:     Dict[id, OpeningNode]       # FormulaicOpeningPolicy target
        non_main_lang_spans:    Dict[id, SpanNode]          # NonMainLangPartsPolicy target
        voice_transitions:      Dict[id, VoiceMarkNode]     # VoiceMarkingPolicy target
        honorifics:             Dict[id, HonorificMarkNode] # HonorificsPolicy target
        archaic_register_marks: Dict[id, RegisterNode]      # ArchaicRegisterPolicy target
```

Why this shape:

1. **Pure tree fails the apparatus case.** Marginalia and embedded poetry are not cleanly tree-attached — they reference back to a position in the main body. Forcing them into tree positions either breaks paragraph-adjacency (the marginalia becomes a sibling of the paragraph it annotates rather than something the paragraph runs reference) or produces awkward sub-node positions.

2. **Pure flat-list-with-region-tags fails the chunking case.** Chunking by chapter (`PipelineConfig.chunking_granularity = "chapter"`) requires reconstructing the hierarchy from tags — fragile and lossy.

3. **The hybrid gives both.** The tree gives chapter-context; the cross-referenced flat collections give apparatus by reference. Every paragraph reads as a sequence of (text runs interspersed with markers); each marker resolves to an apparatus collection entry by id.

What's foreclosed: pure-tree (apparatus mis-positioned); pure-flat (chapter-context lost).

Revisitability: the **shape** is committed; the **field-level schema** (the exact pydantic class with field types, validators, and serialization) is downstream — it is the largest single design task this finding routes to a next inquiry.

#### Decision 4 — The 7 schema policies split into intake-perception and translate-rendering halves

Each of the seven policy classes in `SKILL/references/config/schemas.py` has TWO halves:

1. **Intake-time perception** — the detector finds the policy's target element in the source and represents it in `IntakeDoc`'s apparatus collections.
2. **Translate-time rendering** — the policy's `Literal` value (chosen by the user in `TranslationConfig`) is applied to translation output.

The policy's value lives in `TranslationConfig`; the policy's target element lives in `IntakeDoc`. The split table:

| Policy class (in `schemas.py`) | Intake-time perception | Translate-time rendering |
|---|---|---|
| `NonMainLangPartsPolicy` | Detect non-main-language spans (script change via Unicode property; langid per-segment; explicit `lang=` attributes) | Choose render strategy: preserve / replace / translate / annotate |
| `SourceApparatusPolicy` | Detect marginalia / glosses / apparatus criticus | Choose render placement: drop / inline-bracketed / footnote / channel |
| `VoiceMarkingPolicy` | Detect voice transitions (author vs cited authority vs student) | Choose marking style |
| `ArchaicRegisterPolicy` | Detect archaic register markers | Choose modernize / preserve / hybrid |
| `HonorificsPolicy` | Detect honorifics (per-tradition suffix patterns; named-entity adjacency) | Choose render: preserve / transliterate / translate / abbreviate / drop |
| `FormulaicOpeningPolicy` | Detect formulaic openings (per-tradition templates; position-at-section-start) | Choose render |
| `EmbeddedPoetryPolicy` | Detect embedded poetry (verse-shape signals; attribution patterns; optional per-language meter) | Choose render |

Why the split is structural rather than incidental:

1. **The schema's docstrings reference source features.** `SourceApparatusPolicy`'s docstring names Said Nursi's hashiye (a source-side artifact); `EmbeddedPoetryPolicy`'s docstring names Mevlana couplets in Nursi's prose (also a source-side artifact). These are things intake must perceive, not things translate invents.

2. **The policy value is vacuous without perceived target.** Setting `SourceApparatusPolicy.translate-as-footnote` does nothing if intake never found the marginalia — there is nothing for translate to footnote.

3. **The split clarifies responsibility without modifying the schema.** The seven policy classes are unchanged. The split is an architectural reading that names the intake-side responsibility.

This decision does NOT redefine the schema. It declares the intake-side perception responsibility for each policy and names where that perception lives in `IntakeDoc`.

Revisitability: low. The split is structural.

#### Decision 5 — Pandoc as architectural lever; Tesseract + OCRmyPDF as depth-1 OCR sub-pipeline

Format-layer engineering leverages Pandoc. Accepted user-provided formats — PDF (born-digital with text layer, or scan-only requiring OCR), Microsoft Word .docx, RTF, markdown, EPUB, HTML, and plain text — all flow through Pandoc to produce Pandoc-md-superset. PDFs without a text layer (scan-only sources) route through an OCR sub-pipeline first: **OCRmyPDF** wraps **Tesseract** to add a text layer to the scanned PDF; the resulting text-layer PDF then flows through the Pandoc path.

Why this choice:

1. **Pandoc handles 6 of 7 formats natively.** This is documented at pandoc.org. Writing per-format parsers from scratch is unnecessary engineering cost.

2. **OCRmyPDF and Tesseract are mature, scriptable, well-documented tools.** OCRmyPDF is purpose-built for adding an OCR text layer to scanned PDFs (per the ocrmypdf.readthedocs.io documentation); Tesseract is the de facto open-source OCR engine. Both have stable command-line interfaces.

3. **The depth-1 sub-pipeline scopes the OCR investment.** v0.2 wraps existing tools rather than building an OCR engine. Layout-analysis depth (column detection, marginalia detection in PDFs where marginalia is positioned purely visually) is a sub-component of the OCR sub-pipeline design and is named as a design-next-inquiry rather than tackled in v0.2 directly.

What's foreclosed: writing per-format parsers from scratch.

Revisitability: medium. If specific formats (e.g., complex multi-column scholarly PDFs) routinely fail Pandoc, supplement with format-specific tools (pdf2htmlEX for PDF-to-HTML preservation; `mammoth` for .docx-with-style preservation).

### The 38 concepts, by layer

Each entry: concept name · one-line definition · decision-status · downstream pointer.

#### Format layer (8 concepts)

1. **Canonical intake format** — the internal representation every source document converts into. — **DECIDE-NOW: Pandoc-md-superset** with the extension set named in Decision 1.
2. **Accepted user-provided formats** — what file types intake accepts. — **DECIDE-NOW**: PDF (born-digital and scan-only), .docx, RTF, .md, EPUB, HTML, plain text.
3. **OCR sub-pipeline** — the depth-1 sub-pipeline (Tesseract via OCRmyPDF + layout-analysis) for scan-only PDFs. — **DESIGN-NEXT-INQUIRY**. Configuration includes per-document language tags; layout-analysis flags for column-detection and marginalia-detection; fallback rules for low-quality OCR output.
4. **Pandoc invocation per format** — per-format reader flags and extension sets. — **DESIGN-NEXT-INQUIRY**. Per-format flags (`--from=docx`, `--from=rtf`, `--from=epub`, `--from=html`, `--from=markdown`) plus the canonical extension set (`+footnotes+pipe_tables+definition_lists+citations+yaml_metadata_block+raw_attribute`) plus output controls (`--standalone --wrap=none --extract-media=<dir>` for figure handling).
5. **Format detection** — magic-bytes detection when file extension is unreliable. — **ENGINEER**. Uses `python-magic` or equivalent libmagic binding; magic-bytes inspection of file headers (`%PDF-`, `PK\x03\x04` for .docx-as-zip, `{\rtf`, etc.); falls back to extension when magic-bytes are inconclusive.
6. **Mixed-script and right-to-left text handling** — intake handling for documents that interleave scripts (e.g., the calibration corpus interleaves Turkish, Arabic, and Latin transliteration). — **DESIGN-NEXT-INQUIRY**. Per-paragraph script-fraction analysis plus langid signals; outputs feed the `NonMainLangPartsPolicy` perception detector. Diacritic preservation; ligature handling; combining-character normalization (Unicode NFC).
7. **Pandoc AST to `IntakeDoc` mapping** — walking Pandoc's Abstract Syntax Tree to produce the `IntakeDoc` tree. — **ENGINEER**. Pandoc emits a typed tree (Header, Para, Note, Span, Div, Emph, Strong, and others); the walker maps these to `IntakeDoc` containers and apparatus entries.
8. **Format-fidelity gradient** — the per-stage measurement of conversion loss along PDF → Pandoc-md-superset → `IntakeDoc`. — **DEFER (v1+ scope)**. Per-stage metrics (chars preserved, structure elements preserved, apparatus resolution rate) are valuable but not required for v0.2; recorded in the frontier for revival.

#### Structure layer (12 concepts)

1. **The structure-vs-style distinction** — intake preserves structure (hierarchical containment, apparatus, semantic emphasis); intake drops raw style (font face / size / color). Italic and bold are preserved as semantic primitives (italic-as-emphasis, bold-as-strong-emphasis), not as typography. — **DECIDE-NOW: this is an axiom**.
2. **Hierarchical containment** — Document → Chapter → Section → Paragraph as the tree skeleton of `IntakeDoc`. — **DECIDE-NOW: tree-as-primary**.
3. **Footnotes** — Pandoc-md-superset's `[^id]` footnote syntax maps to `IntakeDoc.apparatus.footnotes[id]`; paragraph runs reference footnotes via `MarkerRun{type: footnote-ref, ref-id}`. — **ENGINEER**.

The next seven (numbered 4-10) are the **seven policy-perception detectors** named in Decision 4. Each is a **DESIGN-NEXT-INQUIRY**: the perception-signals algorithm needs design before code, and each has per-language or per-tradition resource needs.

4. **`NonMainLangPartsPolicy` detector** — detects non-main-language spans. Signals: Unicode script-property change; per-segment langid (e.g., `langid.py`, `cld3`); source markup `lang=` attributes. Representation: `IntakeDoc.apparatus.non_main_lang_spans[id]` with `{lang, script, body}` plus inline `MarkerRun` references.
5. **`SourceApparatusPolicy` detector** — detects marginalia, glosses, and apparatus criticus. Signals: Pandoc note nodes; .docx margin-comments; EPUB aside elements; custom markdown divs (e.g., `:::marginalia`). **Format-dependent caveat:** for structured sources (.docx margin-comments, EPUB asides, custom markdown divs), detection is straightforward via the listed signals. For PDF sources where marginalia is positioned purely visually with no markup, detection requires a layout-analysis depth-1 sub-pipeline (column-detection + adjacent-block proximity + author-voice heuristic). This is part of the OCR sub-pipeline design (concept 3 above). Representation: `IntakeDoc.apparatus.marginalia[id]` with `MarkerRun{type: marginalia-ref}` references.
6. **`VoiceMarkingPolicy` detector** — detects voice transitions (author vs cited authority vs student). Signals: quotation marks (both curly and straight); blockquote elements; explicit-attribution patterns ("X said:", "according to Y"); structural shifts in tense or register as a secondary signal. Representation: `IntakeDoc.apparatus.voice_transitions[id]` with `{voice, body-range}`.
7. **`ArchaicRegisterPolicy` detector** — detects archaic register markers. Signals: per-source-language archaic vocabulary lists (lexical); per-language verb-conjugation patterns (syntactic); explicit `<sic>` or TEI-style markup. Per-language resource needs: detection requires authoritative archaic-vocabulary lists per source language; for the calibration corpus (Ottoman Turkish), such lists exist; for other languages they would need sourcing. Representation: `IntakeDoc.apparatus.archaic_register_marks[id]`.
8. **`HonorificsPolicy` detector** — detects honorifics (suffix patterns after names per tradition). Signals: per-tradition suffix-pattern regex sets (Islamic SAW / AS / RA / PBUH family; Hindu śrī; academic PhD / Esq.; military rank; royal styles); named-entity adjacency. Representation: `IntakeDoc.apparatus.honorifics[id]` with `{name-span, honorific-token, tradition}`.
9. **`FormulaicOpeningPolicy` detector** — detects formulaic openings (invocations, dedicatory formulae, ritual openings, preambles). Signals: per-tradition opening templates (Islamic Bismillah; Jewish Shema; Christian invocations; Vedic mantras; legal "Whereas..."; academic-paper dedications); structural constraint of position-at-section-start. Representation: `IntakeDoc.apparatus.formulaic_openings[id]`.
10. **`EmbeddedPoetryPolicy` detector** — detects embedded poetry (verse-in-prose). Signals: verse-shaped formatting (line breaks and indentation different from surrounding prose); attribution patterns ("Mevlana says:"); optional per-language meter signal as a refinement. Representation: `IntakeDoc.apparatus.embedded_poetry[id]`.

The last two structure-layer concepts:

11. **Frontmatter / backmatter / table-of-contents** — three structural boundaries. Frontmatter is pre-body content (cover, copyright, dedication, foreword, table-of-contents); backmatter is post-body content (appendix, glossary, index, colophon); table-of-contents is generated from heading levels or present in source frontmatter as an enumerated list. Each is a top-level container in `IntakeDoc.body` alongside Chapter. — **ENGINEER**.
12. **Emphasis as a structural primitive** — Pandoc emits `Emph` (italic) and `Strong` (bold) AST nodes. The walker maps `Emph` to `InlineRun{style: emphasis}` and `Strong` to `InlineRun{style: strong}`. Both are preserved as semantic, not as typography. — **ENGINEER**.

#### Pipeline layer (10 concepts)

The stages, ordered:

```
[source file]
     │
     ▼
   pre-validation (concept 7)        — format supported? size sane? readable?
     │
     ▼
   parse (concept 3)                 — Pandoc reader → AST (or OCR → text-layer-PDF → Pandoc → AST)
     │
     ▼
   normalize (concept 4)             — Unicode NFC; whitespace canonical; line endings; punctuation
     │
     ▼
   segment (concept 5)               — AST → IntakeDoc tree containers + apparatus collections
     │
     ▼
   metadata extraction (concept 9)   — populate IntakeDoc.metadata (title, author, language, encoding)
     │
     ▼
   post-parse validation (concept 8) — IntakeDoc against schema + structural sanity heuristics
     │
     ▼
[IntakeDoc handed to translate stage]
```

1. **`IntakeDoc` pydantic schema design** — the typed class hierarchy realizing Decision 3's shape. Field types per container and apparatus collection; validators (especially cross-reference integrity: every `MarkerRun.ref-id` resolves to an apparatus entry); versioning approach; round-trip serialization to Pandoc-md-superset on disk. — **DESIGN-NEXT-INQUIRY**: the single largest design task downstream of this finding.
2. **Intake-vs-translate boundary** — intake's output is `IntakeDoc`; translate's input is `IntakeDoc`. The boundary is the schema's contract. Intake does NOT make policy-value choices (translate's job); translate does NOT re-parse the source (intake's job). — **DECIDE-NOW**.
3. **Parse stage** — per-format Pandoc invocation per concept 4 in the format layer; the OCR routing decision for PDFs without text layers. — **ENGINEER**.
4. **Normalize stage** — Unicode NFC normalization (per `unicodedata.normalize('NFC', s)`); whitespace canonicalization (collapse runs of whitespace within paragraphs; preserve paragraph breaks); line-ending unification (CRLF → LF); per-source-language punctuation normalization decisions. — **ENGINEER**.
5. **Segment stage** — walk Pandoc AST (per concept 7 in the format layer); construct `IntakeDoc` tree containers; populate paragraph runs; resolve apparatus references; populate apparatus collections via the seven policy-perception detectors. — **ENGINEER**.
6. **Validate stage** — run `IntakeDoc` through schema validation (pydantic auto-validation); run heuristic checks (every Chapter has ≥1 Paragraph; every apparatus reference resolves to a collection entry); collect violations as `IntakeWarning` items in `IntakeDoc.metadata`. — **ENGINEER**.
7. **Pre-validation** — file readable + non-empty + size below memory threshold + format in accepted list. Fail fast with named error categories (FormatUnsupported, FileEmpty, FileTooLarge). — **ENGINEER**.
8. **Post-parse validation** — the validation stage applied after parse-segment-metadata, distinct from pre-validation. Concept 6's stage applied here. — **ENGINEER**.
9. **Intake metadata + language detection** — populate `IntakeDoc.metadata`: title (from YAML frontmatter, .docx core properties, EPUB metadata, PDF title tag, or filename); author (similar fallback chain); source-format (from concept 5 of the format layer); source-language (per-document langid on first-N-paragraphs); encoding (UTF-8 detected via `chardet` or `cchardet` for raw plain-text files). — **ENGINEER**.
10. **Multi-file project intake** — design for intaking multi-volume or multi-file corpora (the calibration corpus is a multi-volume work). One merged `IntakeDoc` (chapters stacked; cross-references resolve globally) versus an `IntakeProject` container holding many `IntakeDoc` instances. — **DESIGN-NEXT-INQUIRY**.

#### Quality layer (8 concepts)

1. **Quality target = structure-preservation** — per Decision 2. Measurement is structural-element-preservation-percent, not character-preservation-percent or typography-preservation-percent. — **DECIDE-NOW**.
2. **Fidelity and lossiness framing** — operationalize "percent of structure preserved": per-container existence checks (chapter / section / paragraph counts against source signals); apparatus-resolution rate (footnotes matched to bodies; marginalia matched to positions); emphasis preservation. — **DESIGN-NEXT-INQUIRY**.
3. **Intake-quality metrics** — the concrete metric set: chars-preserved-percent (lossy-vs-lossless check); structure-elements-preserved-percent (containers and apparatus); per-chapter integrity score (does each chapter have plausible structure); apparatus-resolution-percent (orphan footnotes; unresolved marker references). — **DESIGN-NEXT-INQUIRY**.
4. **Intake-quality gates** — threshold(s) below which translation refuses to proceed. Example: "if structure-preservation-percent < 70%, require human review before translation"; "if apparatus-resolution-percent < 95%, flag specific orphan items and require user resolution." Threshold values are calibration-dependent. — **DESIGN-NEXT-INQUIRY**.
5. **Intake-edit-after-parse** — the recovery workflow. The `IntakeDoc` serializes to Pandoc-md-superset on disk as the canonical form; users can hand-edit the markdown to fix bad parses; re-loading the edited markdown produces an updated `IntakeDoc`. — **DECIDE-NOW: supported**.
6. **Paratext handling** — page numbers, running headers, footers. Default: drop (typically noise — running headers, page numbers, footer annotations are typographic chrome, not body content). Override mechanism: preserve-as-metadata for specific use cases (citations referencing source pagination; critical editions where paratext is signal). — **DECIDE-NOW for default (drop); override mechanism is DESIGN-NEXT-INQUIRY.**
7. **Intake-time vs translate-time error attribution** — every error carries a stage tag in `IntakeWarning` and `IntakeError`: which stage (parse / normalize / segment / validate / OCR / metadata); which input subset; which failure category. This keeps intake errors and translation errors apart during debugging. — **ENGINEER**.
8. **Source-of-truth declaration** — once intake completes, `IntakeDoc` (serialized as Pandoc-md-superset) is the canonical representation. The user's original file is preserved untouched as `_original.<ext>` and not re-read during translation. This locks the format-conversion at intake-time; downstream is monoformat. — **DECIDE-NOW**.

### Methodology

This finding's content is anchored to four grounding sources, named explicitly so the reader can audit:

1. **Schema reference** — claims about the seven policy classes, `TranslationConfig`, and `PipelineConfig` cite `SKILL/references/config/schemas.py` directly.
2. **Pandoc fact** — claims about Pandoc extensions, AST node types, and command-line flags can be verified against Pandoc's official documentation at pandoc.org. The named extensions (`footnotes`, `pipe_tables`, `definition_lists`, `citations`, `yaml_metadata_block`, `raw_attribute`) and AST node types (`Header`, `Para`, `Note`, `Span`, `Div`, `Emph`, `Strong`) are Pandoc-native.
3. **Sensemaking anchor** — architectural decisions and the perception/rendering policy split rest on adjudication from the prior thinking work captured in the inquiry's `sensemaking.md` (archived in `docarchive/`).
4. **Explicit extrapolation flag** — any claim that extends beyond the three sources above is marked as extrapolation inline. Time estimates for downstream inquiries, for example, are developer-time extrapolations calibrated to the engineer's familiarity with the tools.

The 110-candidate surface area surfaced at the start of the inquiry was pruned to 38 by keeping concepts that are either (a) named or implied by the schema, (b) downstream-consequential for translation quality, or (c) require an engineering decision in v0.2 onward. The 72 dropped candidates split into roughly 15 format-edge cases (LaTeX, math notation, per-format ligature handling), 18 structure-edge cases (code blocks, captions, citation sub-types, original-vs-modernized spelling, colophons, editorial brackets), 12 pipeline-operational items (logging detail, streaming-vs-load-all, schema-versioning machinery, audit-trail detail, intake-reproducibility tests), 12 quality-secondary items (round-trippability framing as a primary measure, reference-intake tooling, inter-intake-diffing, generic "good intake equals downstream success" framing duplicates), and roughly 15 items already subsumed by the Pandoc-md-superset choice (footnote-syntax-design becomes Pandoc's design, not the project's).

---

## Inherited Commitments Re-test

This inquiry inherits commitments from four sources. Each is re-tested below.

- **Commitment:** The five articulations considered at the start of the inquiry (per `articulate_simple.md`, archived in `docarchive/`) presented different scopings — format-leaning, structure-leaning, pipeline-leaning, cross-layer breadth, and pragmatic-painpoint-leaning.
  - **Source:** `articulate_simple.md` Considered Articulations section.
  - **Re-test status:** **RE-TESTED — commitment confirmed.** The cross-layer breadth articulation (variant 4) is **primary**; the pragmatic-painpoint-leaning articulation (variant 5) is **secondary** (carried via the 8 DECIDE-NOW items that answer immediate decisions). The three single-layer articulations (variants 1-3) are **partially accepted** through the layered structure — each layer carries its weight inside the unified list rather than as a standalone scoping.
  - **Evidence:** the four-layer structure of the 38-concept list. Layer A (format) addresses variant 1; Layer B (structure) addresses variant 2; Layer C (pipeline) addresses variant 3; the layered structure plus the 5 load-bearing decisions addresses variant 4; the 8 DECIDE-NOW tags address variant 5.

- **Commitment:** The 110 surfaced candidate concepts (per `surfacing.md`, archived in `docarchive/`) span format / structure / pipeline / quality layers and should be pruned to a load-bearing set.
  - **Source:** `surfacing.md` Concept-names list and Region tables.
  - **Re-test status:** **RE-TESTED — commitment confirmed.** Pruning honored: 38 retained, 72 dropped. The retained 38 all have downstream consequences for at least one of (unblock-painpoint, avoid-architecture-debt, scope-engineering, meta-reframe).
  - **Evidence:** the per-layer breakdown above; the methodology paragraph explicitly accounts for the 72 dropped concepts by category.

- **Commitment:** The 7 policy classes in `SKILL/references/config/schemas.py` are the canonical contract for translation-stage policy adjudication.
  - **Source:** `SKILL/references/config/schemas.py` lines 18 through 122 (the seven policy classes).
  - **Re-test status:** **RE-TESTED — commitment confirmed but frame revised.** The seven policy classes are unchanged at the schema level — no Literal values added or removed; no class fields modified. The frame revision is the perception/rendering split (Decision 4): the inquiry's contribution is naming the perception-side of each policy and committing where the perceived target lives in `IntakeDoc`. This is an architectural extension, not a schema modification.
  - **Evidence:** the policy-split table in Decision 4 above; the seven policy-perception detectors (concepts 4-10 of the structure layer).

- **Commitment:** The Mac app's UI surface (toolbar, Config sheet, pickers, action bar; per the prior session's v0.1 work and ContentView/LLMClient code) is the v0.1 product surface for translation interaction.
  - **Source:** v0.1 work in this session's prior turns; `_branch.md` MQ4 exclusion of "appification."
  - **Re-test status:** **INHERITED-WITHOUT-RE-TEST**.
  - **Reason:** Out of scope for this intake-handling inquiry. The user explicitly excluded "appification" from this inquiry's frame; revisiting the app surface inside this finding would violate the inquiry's bounded territory. When intake is built (v0.2 onward), the app will need an "intake document" button, a quality-report dialog showing the intake-quality metrics named in concept 3 of the quality layer, and a hand-edit recovery flow surfacing concept 5 of the quality layer. That work is downstream of this finding.

---

## Next Actions

### MUST

- **What:** Run a new inquiry to design the `IntakeDoc` pydantic schema realizing Decision 3's tree-of-containers + cross-referenced flat collections shape. Produce a `comprehenslate/intake/schema.py` module with typed containers (Document, Chapter, Section, Paragraph, MarkerRun, TextRun, InlineRun), the eight apparatus collections, validators (especially cross-reference integrity), and round-trip Pandoc-md-superset serialization.
  - **Who:** the next design inquiry (likely a `/traverse` run).
  - **Gate:** time-bound — start before any other intake engineering. The schema is the contract that all stages and detectors populate.
  - **Why:** the schema is the load-bearing concept for everything downstream. Without it, the seven detectors have nothing to populate; the pipeline stages have nothing to produce; the quality metrics have nothing to measure.

- **What:** Run a new inquiry to design the OCR sub-pipeline. Wrap Tesseract via OCRmyPDF; specify per-document language tags; configure layout-analysis flags for column detection and adjacent-block proximity (which feeds the PDF-marginalia detection path of the `SourceApparatusPolicy` detector); specify fallback rules for low-quality OCR output.
  - **Who:** the next OCR-sub-pipeline inquiry.
  - **Gate:** condition-bound — start once the `IntakeDoc` schema inquiry has produced at least a draft schema (so the OCR sub-pipeline knows what shape to populate). Can run partially in parallel with the schema inquiry once the apparatus-collection shape is sketched.
  - **Why:** the calibration corpus includes scan-only PDF volumes; intake cannot ship without an OCR path.

- **What:** Build an end-to-end prototype taking ONE Risale-i Nur PDF (representative — containing marginalia, embedded poetry, and a formulaic opening) all the way through Pandoc + intake stages + a subset of policy-perception detectors, producing a populated `IntakeDoc` with quality metrics reported.
  - **Who:** an engineering iteration once the schema and OCR sub-pipeline have draft designs.
  - **Gate:** condition-bound — start after the schema inquiry produces a draft; iterate alongside the detector inquiries.
  - **Why:** the inquiry's commitments need empirical validation against the calibration corpus. Integration testing surfaces issues that per-stage unit tests cannot. The prototype IS the calibration anchor for all subsequent intake work.

### COULD

- **What:** Run sub-inquiries for the seven policy-perception detectors (concepts 4 through 10 of the structure layer). Each detector has distinct per-policy signals and per-language or per-tradition resource needs; running them as seven sub-inquiries allows parallel work and per-detector calibration.
  - **Who:** parallel design inquiries (potentially seven small `/traverse` or scoped runs).
  - **Gate:** condition-bound — start once the `IntakeDoc` schema inquiry has committed the apparatus-collection shape.
  - **Why:** the seven detectors are independently designable and can ship incrementally once the schema exists.
  - **Depends-on:** MUST item *the `IntakeDoc` pydantic schema design*. This COULD is GATED — do not act until the MUST resolves.

- **What:** Run an inquiry to design the intake-quality metrics and gates (concepts 2, 3, and 4 of the quality layer). Specify per-metric formulas; specify default threshold values; specify the refuse-to-proceed gate logic.
  - **Who:** the next quality-metrics inquiry.
  - **Gate:** condition-bound — start after the `IntakeDoc` schema exists and a few detectors are working (the metric definitions depend on what `IntakeDoc` actually contains).
  - **Why:** the quality target (Decision 2) needs operationalization before intake can refuse to proceed on bad output.
  - **Depends-on:** MUST item *the `IntakeDoc` pydantic schema design*. This COULD is GATED — do not act until the MUST resolves.

- **What:** Run an inquiry to design multi-file project intake mechanics (concept 10 of the pipeline layer). Choose between a merged `IntakeDoc` shape (chapters stacked; cross-references global) and an `IntakeProject` container shape (many `IntakeDoc` instances with project-level metadata).
  - **Who:** the next multi-file inquiry.
  - **Gate:** condition-bound — start after single-file intake works end-to-end (the design choice is informed by single-file experience).
  - **Why:** the calibration corpus is multi-volume; without project intake mechanics, intake can handle one volume at a time only.
  - **Depends-on:** MUST item *end-to-end Pandoc → IntakeDoc prototype on a Risale-i Nur PDF*. This COULD is GATED — do not act until the prototype shows single-file intake works.

- **What:** Implement the eleven ENGINEER-tagged concepts (format detection; Pandoc AST mapping; footnote handling; frontmatter/backmatter/TOC; emphasis-as-primitive; parse / normalize / segment / validate / pre-validation / post-parse validation / metadata-extraction stages; stage-tagged error attribution).
  - **Who:** engineering iterations alongside the schema and detector inquiries.
  - **Gate:** condition-bound — ship per-concept as upstream dependencies resolve.
  - **Why:** these are well-defined engineering items that need to exist for intake to run; they are not blockers on design inquiry but they cannot be started until the schema is at least drafted.
  - **Depends-on:** MUST item *the `IntakeDoc` pydantic schema design*. This COULD is GATED — do not act until the MUST resolves.

### DEFERRED

- **What:** Design the format-fidelity gradient measurement (concept 8 of the format layer).
  - **Gate:** revival trigger — when v0.x intake ships and per-stage conversion loss becomes a measurable engineering concern (likely v1+).
  - **Why (if revived):** measuring conversion-loss per stage (PDF → Pandoc → `IntakeDoc`) would enable per-format quality tuning and per-stage debugging.

- **What:** Design intake schema versioning (raised as an open question in the inquiry).
  - **Gate:** revival trigger — when the `IntakeDoc` schema requires its first migration (i.e., when a v0.x intake artifact needs to be re-loaded under a v0.y schema).
  - **Why (if revived):** without versioning, schema evolution forces re-intake from source.

- **What:** Reconsider Pandoc-md-superset versus a custom `.compldoc` format.
  - **Gate:** condition-bound — when scaling beyond the calibration corpus reveals primitives Pandoc-md-superset cannot express that cannot be represented via Pandoc's raw-attribute escape (e.g., complex mathematical notation requiring MathML; music notation).
  - **Why (if revived):** the Pandoc-md-superset choice has medium revisitability; a future corpus may force the question.

- **What:** Design the Mac app's intake UI surface (intake-document button, quality-report dialog, hand-edit recovery flow).
  - **Gate:** condition-bound — when intake is built and an end-to-end prototype shows what UI is actually needed.
  - **Why (if revived):** the user explicitly excluded app concerns from this inquiry; that exclusion was inquiry-bound, not permanent. The app will eventually need an intake surface.

---

## Reasoning

### Why this list over the alternatives

Three single-layer scopings were considered and partially accepted rather than chosen as primary:

- **Format-only scoping** would have produced a shorter list (eight concepts, all in the format layer) and a simpler engineering path. It was partially accepted because the format-layer concepts ARE included. It was not chosen as the primary scope because picking a canonical format without knowing what structure intake must perceive is exactly the architecture-debt path the user wanted to avoid. The choice of Pandoc-md-superset over vanilla CommonMark, for example, is only defensible against the structure-layer requirements (the seven policy targets need primitives vanilla CommonMark cannot express).

- **Structure-only scoping** would have focused on the twelve structure-layer concepts and the seven detectors. It was partially accepted because those concepts ARE included. It was not chosen as the primary scope because the structure-layer concepts cannot be perceived without naming the pipeline stages that produce them, nor validated without naming the quality target.

- **Pipeline-only scoping** would have produced a checklist of standard engineering stages. It was partially accepted because the pipeline-layer concepts ARE included as the eleven ENGINEER-tagged items. It was not chosen as the primary scope because shipping pipeline stages without `IntakeDoc` (which is the contract every stage populates) would produce stages with nothing to produce.

The chosen scope — cross-layer breadth with per-concept decision-status flagging — preserves all three single-layer concerns while making the relationships visible.

### Why Pandoc-md-superset over the format alternatives

Four canonical-format options were tested:

- **Vanilla CommonMark.** Counter-argument: it lacks footnotes (needed for marginalia per the `SourceApparatusPolicy` target), tables (needed for apparatus criticus in critical-edition sources), and definition lists (needed for glossary terms). Trying to encode these in custom inline syntax effectively reinvents Pandoc-md-superset under a different name. Rejected on the grounds that the user's calibration corpus has marginalia that vanilla CommonMark cannot represent.

- **Markdown plus RTF for complicated texts** (the user's substrate proposal). Counter-argument: RTF is editor-fragile. The same RTF file looks different across Microsoft Word, Apple Pages, and TextEdit. This defeats the hand-editing recovery workflow (concept 5 of the quality layer), where the user fixes bad parses by editing the canonical on-disk form. RTF also doubles the parser surface and the test surface. Rejected on workflow and engineering-cost grounds.

- **A custom `.compldoc` precursor.** Counter-argument: significant engineering cost; v0.2 has no resources for designing and implementing a custom format on top of designing the seven detectors and the schema. Pandoc-md-superset is "free" engineering — the parser already exists. Rejected as v1+ scope; recorded in DEFERRED Next Actions with a specific revival trigger.

- **Pandoc-md-superset.** Survives: covers the calibration corpus's primitives off-the-shelf (footnotes, tables, definition lists); single parser surface (Pandoc's reader); human-readable; hand-editable; revisitable.

### Why structure-preservation over the quality-target alternatives

Three quality targets were considered:

- **Typography-preservation.** Counter-argument: includes too much rendering noise (font face, size, color — which translation cannot use) and not enough structural signal (a heading IS structural even when its only signal is being-larger; under pure-typography preservation the heading-vs-paragraph distinction depends on font analysis rather than on structural representation). Rejected.

- **Semantic-only stripping.** Counter-argument: drops chapter and paragraph boundaries that translation needs for context. `PipelineConfig.chunking_granularity = "chapter"` is a real schema option that requires intake to have preserved chapter boundaries. Rejected.

- **Structure-preservation.** Survives: matches the user's painpoint exactly (the user described structural loss, not typographic loss); supports the seven policy detectors; supports chunking-by-chapter; drops only rendering decoration translation cannot use.

The decision text explicitly preserves the legitimate concern that typography can carry meaning in specific corpora (chapter-font as genre signal; calligraphic display in religious texts). The acceptance reasoning is that these cases are rare in prose-shaped texts, an override mechanism exists at the paratext-handling design-next-inquiry, and preserving raw typography for the common case would burden every `IntakeDoc` with rendering state.

### Why the perception/rendering policy split is structural and not incidental

The split rests on an observation about the seven policy classes' docstrings. Each docstring references a SOURCE-side artifact: `SourceApparatusPolicy` names Said Nursi's hashiye (source marginalia); `EmbeddedPoetryPolicy` names Mevlana couplets embedded in Nursi's prose (source-embedded verse). These are things intake must perceive, not things translate invents. The policy's value (the `Literal` choice in `TranslationConfig`) is vacuous without intake having perceived the policy's target — setting `SourceApparatusPolicy.translate-as-footnote` does nothing if intake never found the marginalia to footnote.

The split is therefore not a scope-expansion of the policies; it is a naming of the intake-side responsibility that was always implicit. The seven policy classes are unchanged at the schema level. The contribution is naming where each policy's target lives in `IntakeDoc`.

---

## Open Questions

### Monitoring

- **Pandoc-md-superset's actual coverage on the calibration corpus.** The decision rests on Pandoc-fact (the extension set documented at pandoc.org) plus a structural argument (those extensions cover the calibration corpus's primitives). Empirical confirmation arrives only when the end-to-end prototype runs on real Risale-i Nur PDFs and the resulting `IntakeDoc` is inspected against the source.

- **The seven policy-perception detectors' recall on the calibration corpus.** The detector signals (script-property change for non-main-language; verse-shape for embedded poetry; per-tradition templates for formulaic openings; per-tradition suffix patterns for honorifics; per-language vocabulary lists for archaic register; explicit attribution patterns for voice marking; layout-analysis plus structured-source signals for marginalia) are honest about per-language and per-tradition resource needs. Recall measurement on the calibration corpus will surface which detectors need more resource investment.

### Blocked

- **Multi-file project intake design** is blocked until single-file intake works end-to-end on at least one calibration sample. The design choice between merged `IntakeDoc` and `IntakeProject` container is informed by what single-file intake actually produces.

- **Intake-quality metric thresholds** are blocked until the metrics themselves are operational. Threshold defaults are calibration-dependent; cannot be set without measurement data.

### Research Frontiers

- **Cross-corpus generalization.** The calibration anchor is currently theological prose with marginalia + embedded poetry + formulaic openings (the Risale-i Nur shape). Whether the structure-preservation framing and the seven detector designs generalize cleanly to other corpora (Talmud apparatus criticus; Vedic texts; Christian patristic editions; academic critical editions) is a research frontier — testable after the calibration-corpus prototype validates.

- **Hand-edit recovery workflow ergonomics.** The decision commits to supporting hand-editing the canonical Pandoc-md-superset on disk. What this workflow LOOKS LIKE to the user (when does the prompt to hand-edit appear; how is the round-trip presented; what feedback signals quality improvement) is downstream of intake's existence and the eventual Mac-app re-entry.

### Refinement Triggers

- **Decision 1 (canonical format) re-opens** when scaling beyond the calibration corpus reveals primitives Pandoc-md-superset cannot express via its extension set or raw-attribute escapes (e.g., complex mathematical notation requiring MathML; music notation; non-Latin script intake requirements not handled by Unicode normalization).

- **Decision 2 (quality target) re-opens** if structure-preservation routinely fails on corpora where typography carries genre signal (e.g., critical editions where italic styling marks editorial insertion). The override mechanism in concept 6 of the quality layer is the first response; the decision itself re-opens only if the override mechanism becomes the rule rather than the exception.

- **Decision 5 (Pandoc-as-lever) re-opens** if specific formats routinely fail Pandoc on the calibration corpus or other corpora that come into scope. Supplement with format-specific tools (pdf2htmlEX for PDF-to-HTML preservation; `mammoth` for .docx-with-style preservation) before re-opening the whole decision.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
okay for now lets stop dealing with the appification and focus on document intake , which is a real painpoint
lets start by identifying list of intake handling concepts we need to figure out, 

for example in pdfs formatting can be really bad, and maybe they should be converted to md file first? but md file has limitations and maybe we should use rtf as standard intake format along with md for complicated texts
```

</details>
