# Route-Map — document intake handling concepts

## User Input

Territory: this inquiry's artifacts (`_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md` + `innovation.md` + `critique.md`).

Goal: enumerate the onward route-field this inquiry opens for document intake. 5 load-bearing decisions committed (Pandoc-md-superset / structure-preservation / IntakeDoc tree+cross-ref / 7-policy split / Pandoc-as-lever + OCR sub-pipeline) + 38 concepts across 4 layers + 3 REFINE-direction adjustments from critique + Frontier F4 (Mac-app re-entry).

Mode: `root / project-space (breadth)`. Entry: `fresh` (no prior `_route.md`).

---

## Map Header

- **Identity count:** 21
- **Teleological:** 13 · **Epistemic:** 8
- **High-priority count:** 5
- **Convergence:** PROCEED (territory swept at identity resolution; no LAYER 1 failure-mode flags)

---

## Route Index (at-a-glance)

| # | Direction | grain | kind | engagement-type | Priority |
|---|---|---|---|---|---|
| R1 | `IntakeDoc` pydantic schema | project-space | teleological | DEVELOP | **HIGH** |
| R2 | NonMainLangPartsPolicy perception detector | project-space | teleological | DEVELOP | MED |
| R3 | SourceApparatusPolicy perception detector | project-space | teleological | DEVELOP | MED |
| R4 | VoiceMarkingPolicy perception detector | project-space | teleological | DEVELOP | MED |
| R5 | ArchaicRegisterPolicy perception detector | project-space | teleological | DEVELOP | MED |
| R6 | HonorificsPolicy perception detector | project-space | teleological | DEVELOP | MED |
| R7 | FormulaicOpeningPolicy perception detector | project-space | teleological | DEVELOP | MED |
| R8 | EmbeddedPoetryPolicy perception detector | project-space | teleological | DEVELOP | MED |
| R9 | OCR sub-pipeline design (Tesseract + OCRmyPDF + layout analysis) | project-space | teleological | DEVELOP | MED |
| R10 | Pandoc invocation per format | project-space | teleological | DEVELOP | MED |
| R11 | Multi-file project intake mechanics | project-space | teleological | DEVELOP | LOW |
| R12 | Intake-quality-metrics + gates | project-space | teleological | DEVELOP | MED |
| R13 | Paratext handling override mechanism | project-space | teleological | DEVELOP | LOW |
| R14 | End-to-end Pandoc → IntakeDoc prototype on Risale-i Nur PDF | project-space | teleological | PURSUE-SEED | **HIGH** |
| R15 | Mac-app intake UI re-entry (F4) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R16 | Standard intake pipeline-stage engineering (C3-C9) | project-space | teleological | DEVELOP | MED |
| R17 | Structure-engineering items (B3 / B11 / B12) | project-space | teleological | DEVELOP | LOW |
| R18 | Format-engineering items (A5 / A7) | project-space | teleological | DEVELOP | LOW |
| R19 | Decision 1 less-portable concern refinement | project-space | epistemic | REFINE | **HIGH** |
| R20 | Decision 2 typography-meaning concern refinement | project-space | epistemic | REFINE | **HIGH** |
| R21 | B5 PDF-marginalia format-dependent caveat | project-space | epistemic | REFINE | **HIGH** |
| R22 | Pandoc + 7-policy split empirical validation on calibration corpus | project-space | epistemic | TEST | MED |
| R23 | `IntakeDoc` schema versioning + idempotency + partial-intake (open questions) | project-space | epistemic | DIAGNOSE | LOW |
| R24 | Calibration corpus expansion beyond Risale-i Nur | project-space | epistemic | CONSOLIDATE | LOW |

(Listed 24 — index reflects 21 teleological+epistemic + 3 secondary epistemic; the count in Map Header reflects load-bearing identities. The 7 detectors are individuated per asymmetric-failure lean-to-split.)

---

## Per-route records

### R1 — `IntakeDoc` pydantic schema

Direction:        the `IntakeDoc` pydantic schema (typed tree containers + apparatus collections + validators)
Goal:             a designed, typed schema realizing Sensemaking Decision 3's tree-of-containers + cross-referenced flat collections shape
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         build the typed schema (pydantic classes for Document / Chapter / Section / Paragraph / Marker + apparatus dicts) that every parser populates and every translate step consumes
WHY:              load-bearing concept "the contract between intake and translate"; named in this inquiry's finding (C1) as the largest single design task; everything downstream of intake depends on it
Priority:         **HIGH**    Confidence: MED
Guidance Mode:    full
  · "start from the pseudocode in P3 Decision 3 of innovation.md — the tree+cross-ref shape is committed; fields are downstream"  (bc the shape decision is sunk; field design is the actual work)
  · "respect the 7-policy split — the apparatus collections (footnotes / marginalia / embedded_poetry / formulaic_openings / non_main_lang_spans / voice_transitions / honorifics / archaic_register_marks) directly mirror Decision 4"  (bc the perception/rendering split's intake side IS the schema)
  · "use pydantic v2 (the project uses pydantic per schemas.py); add validators for cross-ref integrity (every MarkerRun.ref-id resolves to an apparatus collection entry)"  (bc cross-ref-resolution is the structural integrity invariant)
  Meaning-gaps:
    - Field-level types per node (Text / InlineRun / MarkerRun internal structure) — mid — without these the schema is just sketch; impact-high but multiple-readings-no (Pandoc AST guides)
    - Round-trip serialization to Pandoc-md-superset on disk — high — load-bearing for the D5 hand-edit recovery workflow; if the round-trip is lossy, D5 doesn't hold
    - Schema versioning approach — low — deferable; documented as open question in P9
    - Cross-ref integrity validators (orphan markers / unresolved refs) — mid — needed for D2/D3 quality metrics
Depth-link:       none (not yet drilled)

---

### R2 — NonMainLangPartsPolicy perception detector

Direction:        the per-paragraph script/language detector feeding `NonMainLangPartsPolicy`
Goal:             a perception layer that finds non-main-language spans in source and represents them in IntakeDoc.apparatus.non_main_lang_spans
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design + build the detector (Unicode script property change + `langid.py` / `cld3` per-segment classifier + source markup `lang=` attribute extraction)
WHY:              one of the 7 perception detectors (B4 in this finding); the policy's value is vacuous without intake having perceived the spans
Priority:         MED    Confidence: MED
Guidance Mode:    compact
  · "Unicode script-change signals are deterministic; langid is probabilistic — combine with confidence threshold"  (bc the two signal-classes are complementary)
  Meaning-gaps:
    - Recall threshold for short spans (single-word non-main-lang) — mid — too aggressive = false positives; too conservative = miss inline quotes
    - Mixed-script handling (Arabic + transliteration in same paragraph) — mid — calibration-corpus-relevant
Depth-link:       none

---

### R3 — SourceApparatusPolicy perception detector

Direction:        the marginalia / glosses / apparatus criticus detector feeding `SourceApparatusPolicy`
Goal:             a perception layer that finds source-apparatus elements (marginalia + glosses) and represents them in IntakeDoc.apparatus.marginalia
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design + build the detector (Pandoc note nodes + docx margin-comments + EPUB asides + custom md divs; PLUS layout-analysis sub-pipeline for PDF marginalia per the critique-flagged caveat)
WHY:              the 7-policy split's perception arm; calibration corpus (Risale-i Nur) hashiye is the named target
Priority:         MED    Confidence: LOW (per-format detection complexity varies significantly)
Guidance Mode:    compact
  · "structured-source detection is straightforward; PDF marginalia detection is hard — couples with R9 OCR sub-pipeline depth"  (bc PDF marginalia is purely visual)
  · "Risale-i Nur's hashiye is the calibration anchor; verify detector against actual marginalia samples"  (bc the canonical use case)
  Meaning-gaps:
    - PDF layout-analysis: column detection + adjacent-block proximity + author-voice heuristic — high — without this, PDF marginalia is lost
    - Distinguishing marginalia from footnotes when both appear — mid — semantic distinction not always typographic
    - Author-voice vs cited-authority marginalia subtypes — low — secondary refinement
Depth-link:       none

---

### R4 — VoiceMarkingPolicy perception detector

Direction:        the voice-transition detector feeding `VoiceMarkingPolicy`
Goal:             a perception layer that finds author-vs-cited-authority-vs-student voice shifts and represents them in IntakeDoc.apparatus.voice_transitions
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design + build the detector (quotation marks both styles + blockquote elements + explicit-attribution pattern matching ["X said:", "according to Y"] + structural tense/register shift heuristics)
WHY:              7-policy split perception arm
Priority:         MED    Confidence: MED
Guidance Mode:    compact
  · "structural signals (quote marks + blockquote + attribution) are realistic; tense-shift detection is a refinement"  (bc primary signals are reliable; secondary signals are calibration-dependent)
  Meaning-gaps:
    - Per-language quotation conventions (curly vs straight vs guillemets vs Asian brackets) — mid — affects recall significantly
    - Implicit attribution detection (no explicit "X said:" cue) — low — calibration-dependent
Depth-link:       none

---

### R5 — ArchaicRegisterPolicy perception detector

Direction:        the archaic-register detector feeding `ArchaicRegisterPolicy`
Goal:             a perception layer that finds archaic register markers and represents them in IntakeDoc.apparatus.archaic_register_marks
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design + build the detector (lexical: per-source-language archaic vocabulary lists + syntactic: verb-conjugation pattern matchers + explicit `<sic>` markup respect)
WHY:              7-policy split perception arm
Priority:         MED    Confidence: LOW (genuinely hard; language-resource-dependent)
Guidance Mode:    compact
  · "needs language-specific archaic vocabulary resources; for Ottoman Turkish (Risale-i Nur calibration), documented lists exist"  (bc the task is calibration-language-specific)
  · "honestly flagged: detection is language-dependent — do NOT promise universal detection at v0.2"  (bc over-claiming would set up downstream failure)
  Meaning-gaps:
    - Where to source per-language archaic vocabulary lists — high — without these, the detector cannot fire
    - Distinguishing archaic from poetic register — mid — overlapping linguistic phenomena
    - Per-language extension cost — low — defer to per-language inquiry as needed
Depth-link:       none

---

### R6 — HonorificsPolicy perception detector

Direction:        the honorifics detector feeding `HonorificsPolicy`
Goal:             a perception layer that finds honorific markers (suffixes after names per tradition) and represents them in IntakeDoc.apparatus.honorifics
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design + build the detector (per-tradition suffix-pattern regex sets + named-entity adjacency check; per-tradition coverage for Islamic / Hindu / academic / military / royal honorifics)
WHY:              7-policy split perception arm
Priority:         MED    Confidence: MED
Guidance Mode:    compact
  · "per-tradition suffix patterns are well-defined and finite; named-entity adjacency uses standard NER"  (bc the perception is tractable per tradition)
  Meaning-gaps:
    - Per-tradition pattern lists (Islamic SAW/AS/RA; Hindu śrī; academic PhD/Esq.; etc.) — mid — need maintained authoritative lists
    - Contextual (no-suffix-marker) honorifics — low — rare in canonical corpora
Depth-link:       none

---

### R7 — FormulaicOpeningPolicy perception detector

Direction:        the formulaic-opening detector feeding `FormulaicOpeningPolicy`
Goal:             a perception layer that finds invocations / dedications / preambles and represents them in IntakeDoc.apparatus.formulaic_openings
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design + build the detector (per-tradition opening template matching + position-at-section-start constraint)
WHY:              7-policy split perception arm
Priority:         MED    Confidence: MED
Guidance Mode:    compact
  · "position-at-section-start is a reliable structural constraint; per-tradition template lists are calibration-bounded"  (bc structural signal narrows the search)
  · "Risale-i Nur calibration: Bismillah pattern is the named template anchor"  (bc the corpus has a known canonical opening)
  Meaning-gaps:
    - Per-tradition template coverage breadth — mid — recall depends on template list completeness
    - Detecting variant phrasings of standard formulae — low — secondary refinement
Depth-link:       none

---

### R8 — EmbeddedPoetryPolicy perception detector

Direction:        the embedded-poetry detector feeding `EmbeddedPoetryPolicy`
Goal:             a perception layer that finds verse-in-prose and represents them in IntakeDoc.apparatus.embedded_poetry
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design + build the detector (verse-shape signals: line-breaks + indentation differences from prose; attribution patterns; optional per-language meter signal as refinement)
WHY:              7-policy split perception arm
Priority:         MED    Confidence: MED
Guidance Mode:    compact
  · "verse-shape (typographic differences from surrounding prose) is the primary reliable signal; meter is a refinement"  (bc most poetry is typographically distinct)
  · "Risale-i Nur calibration: Mevlana couplets in Nursi's prose are the named target"  (bc the corpus has known embedded poetry)
  Meaning-gaps:
    - Detection in PDF when typography is lost during conversion — high — couples with R9 OCR sub-pipeline
    - Per-language meter signal availability — low — secondary refinement
Depth-link:       none

---

### R9 — OCR sub-pipeline design (Tesseract + OCRmyPDF + layout analysis)

Direction:        the OCR + layout-analysis sub-pipeline for scan-only and text-layer-poor PDFs
Goal:             a designed sub-pipeline that wraps Tesseract via OCRmyPDF + adds layout-analysis for marginalia/columns/headers/footers, producing a text-layer PDF ready for Pandoc
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design the config (per-document language tags; layout-analysis flags; fallback rules for low-quality OCR) + the layout-analysis depth-1 sub-component (column detection; margin-block detection for marginalia per R3)
WHY:              A3 in the finding; depth-1 sub-pipeline of the format-layer architectural commitment (Decision 5); load-bearing for PDF intake which is the user's painpoint
Priority:         MED    Confidence: MED
Guidance Mode:    compact
  · "OCRmyPDF wraps Tesseract; both mature; the engineering work is config + fallback + layout-analysis depth-1 addition"  (bc tools are stable, integration is the work)
  · "couples with R3 — PDF marginalia detection IS layout analysis"  (bc the two are entangled)
  Meaning-gaps:
    - Per-document language tag determination — mid — affects OCR accuracy significantly
    - Layout analysis tool choice (Tesseract's hOCR vs separate layout tool) — mid — affects R3 marginalia recall
    - Quality threshold below which to refuse OCR result — low — operational tuning
Depth-link:       none

---

### R10 — Pandoc invocation per format

Direction:        the per-format Pandoc invocation specs (reader flag, extension set, output mode)
Goal:             a designed invocation per accepted format that produces the canonical Pandoc-md-superset output for each
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design the per-format flag sets (`--from=docx --extensions=+footnotes+...`; similarly for rtf/epub/html/markdown/plain); document figure handling via `--extract-media`; document fallback paths
WHY:              A4 in the finding; Decision 5's architectural lever applied per-format; needed for R16 (parse stage engineering) to ship
Priority:         MED    Confidence: HIGH (well-defined per-format flag space)
Guidance Mode:    compact
  · "Pandoc's manual documents all reader flags and extensions; the work is selecting the right combination per format + verifying with the calibration corpus"  (bc the tooling is documented)
  Meaning-gaps:
    - PDF Pandoc invocation (vs OCR routing) — mid — PDF text-layer extraction varies; design the routing decision tree
    - Per-format extension set tuning — low — start with the canonical extension set; refine per-format if needed
Depth-link:       none

---

### R11 — Multi-file project intake mechanics

Direction:        the design for intaking multi-volume / multi-file corpora as a coherent project
Goal:             a designed mechanism for merging multiple source files into one `IntakeDoc` (or a designed `IntakeProject` container)
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design the merge mechanics (chapter-id namespacing; cross-reference resolution across volumes; per-volume metadata preservation) OR the container approach
WHY:              C10 in the finding; Risale-i Nur is multi-volume; needed when scaling beyond single-file intake
Priority:         LOW (defer until single-file intake works)    Confidence: LOW
Guidance Mode:    compact
  · "defer until R14 prototype validates single-file intake"  (bc the design choice is informed by single-file experience)
  Meaning-gaps:
    - Merged-IntakeDoc vs IntakeProject container — high — fundamental shape decision
    - Cross-reference resolution across volumes — mid — load-bearing if cross-refs exist
Depth-link:       none

---

### R12 — Intake-quality-metrics + gates

Direction:        the design for quality metrics + gates that determine whether intake output is good-enough for translation to proceed
Goal:             a designed metric set (D2/D3) + threshold gates (D4) operationalizing structure-preservation-% measurement
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design the metrics (structure-elements-preserved %, per-chapter integrity, apparatus-resolution %) + threshold defaults + the refuse-to-proceed gate logic
WHY:              D2 + D3 + D4 in the finding; load-bearing for the structure-preservation quality target (Decision 2)
Priority:         MED    Confidence: LOW (metric design is calibration-dependent)
Guidance Mode:    compact
  · "metrics should be measurable post-IntakeDoc; gates are operational policy"  (bc separates measurement from policy)
  · "couples with R1 — metric existence depends on IntakeDoc schema details (which fields to count)"  (bc the metric definition presupposes the schema)
  Meaning-gaps:
    - Threshold default values — mid — calibration-dependent; needs corpus testing
    - Per-policy quality metrics (marginalia-resolution-%, voice-transition-coverage-%) — low — refinement after baseline metrics ship
Depth-link:       none

---

### R13 — Paratext handling override mechanism

Direction:        the design for the paratext (page numbers / running headers / footers) override mechanism
Goal:             a designed override that flips D6's "drop default" to "preserve-as-metadata" for specific corpora needing it
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design the override interface (config flag? per-document tag? IntakeDoc metadata field?) + the preservation representation in IntakeDoc
WHY:              D6 in the finding; the default is decided (drop), the override is design-next
Priority:         LOW (the default covers most cases)    Confidence: HIGH (small contained design)
Guidance Mode:    compact
  · "small contained design; ship after R1 (schema) + R10 (pandoc invocations)"  (bc depends on schema for representation)
Depth-link:       none

---

### R14 — End-to-end Pandoc → IntakeDoc prototype on Risale-i Nur PDF

Direction:        the integration test seed: take ONE Risale-i Nur PDF and produce a populated IntakeDoc with quality metrics
Goal:             empirical validation of the 5 load-bearing decisions on the calibration corpus
grain:            project-space
kind:             teleological
engagement-type:  PURSUE-SEED
Movement:         build a runnable script wiring R9 (OCR if needed) + R10 (Pandoc) + R1 (IntakeDoc) + R2-R8 (a subset of detectors) for a single PDF; report quality metrics; iterate
WHY:              the inquiry's commitments need empirical test; calibration corpus IS the test substrate; integration reveals what unit tests cannot
Priority:         **HIGH** (load-bearing for validating the decisions before scaling)    Confidence: MED
Guidance Mode:    full
  · "pick ONE representative Risale-i Nur PDF (e.g., a Sozler section with hashiye and Mevlana couplets and Bismillah opening)"  (bc maximizing the calibration signal per single test)
  · "start with R1 + R10 + a stub IntakeDoc; add R2-R8 detectors incrementally"  (bc incremental integration surfaces issues at the right granularity)
  · "report per-stage timings and quality metrics; the prototype IS the calibration anchor for future inquiries"  (bc the calibration artifact persists)
Depth-link:       none

---

### R15 — Mac-app intake UI re-entry (F4)

Direction:        the Mac app's intake-document button + quality-report dialog + hand-edit recovery flow
Goal:             surface intake into the v0.x Mac app once intake is built
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         (when intake is built) design the intake-document UI surface in the Mac app
WHY:              F4 in the finding; explicitly DEFERRED to post-intake-build; user's "stop dealing with appification" was an inquiry-bound exclusion, not permanent
Priority:         LOW (deferred — fires only after R14 + R1 + most engineering ships)    Confidence: LOW
Guidance Mode:    compact
  · "do not fire until R14 prototype validates intake; the app design is informed by intake's empirical behavior"  (bc UI is informed by what intake actually does)
Depth-link:       none

---

### R16 — Standard intake pipeline-stage engineering (C3-C9)

Direction:        the implementation of the standard intake stages (parse / normalize / segment / validate / pre-validation / post-parse validation / metadata extraction)
Goal:             a runnable intake module realizing the 7 ENGINEER-tagged pipeline stages
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         implement the 7 stages per the finding's specs (Pandoc + unicodedata NFC + AST walk + pydantic validation + chardet + fail-fast pre-validation)
WHY:              C3-C9 in the finding; standard engineering work; ships after R1 (schema) exists
Priority:         MED    Confidence: HIGH (well-defined per-stage; just engineering)
Guidance Mode:    compact
  · "depends on R1 (IntakeDoc schema) + R10 (Pandoc invocations) + R18 (A7 AST mapping)"  (bc per-stage work consumes those upstream commitments)
  · "ship stage-by-stage with tests; C7 + C8 are validation gates that can ship later"  (bc dependency-ordered shipping)
Depth-link:       none

---

### R17 — Structure-engineering items (B3 / B11 / B12)

Direction:        the implementation of footnote handling + frontmatter/backmatter/TOC + emphasis-as-primitive
Goal:             a structure-perception layer realizing the 3 small ENGINEER-tagged structure items
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         implement footnote → IntakeDoc.apparatus.footnotes; frontmatter/backmatter/TOC as top-level containers; emphasis-as-semantic-primitive (Pandoc Emph/Strong → InlineRun{style})
WHY:              B3 + B11 + B12 in the finding; small engineering items
Priority:         LOW (small, well-defined)    Confidence: HIGH
Guidance Mode:    compact
  · "ships alongside R16 pipeline stages; segment stage emits these structure elements"  (bc the engineering is integrated with C5)
Depth-link:       none

---

### R18 — Format-engineering items (A5 / A7)

Direction:        the implementation of format detection (libmagic) + Pandoc AST → IntakeDoc mapping
Goal:             format-layer engineering primitives that R16 consumes
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         implement A5 (magic-bytes via python-magic) + A7 (Pandoc AST walker that emits IntakeDoc tree)
WHY:              A5 + A7 in the finding; foundational engineering for R16
Priority:         LOW (well-defined)    Confidence: HIGH
Guidance Mode:    compact
  · "A7 is the critical path — without the AST→IntakeDoc mapping, segment stage cannot fire"  (bc dependency)
Depth-link:       none

---

### R19 — Decision 1 less-portable concern refinement

Direction:        the explicit surfacing of "Pandoc-md-superset is less portable than vanilla CommonMark" as a legitimate-counter concern in finding.md's Decision 1
Goal:             preserve sensemaking Ambiguity 3's adjudication rigor without weakening
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         apply the REFINE-direction adjustment from critique.md: add a paragraph in Decision 1's text surfacing the portability concern + the override reasoning (canonical is INTERNAL only)
WHY:              critique D6 surfaced this as REFINE-direction; sensemaking adjudicated the trade-off but innovation's text suppressed the counter; restoration of the audit-trail
Priority:         **HIGH** (apply before finding.md construction)    Confidence: HIGH
Guidance Mode:    compact
  · "see critique.md → Summary for Finding.md Construction item 1 for the exact paragraph to insert"  (bc the adjustment is already drafted)
Depth-link:       none

---

### R20 — Decision 2 typography-meaning concern refinement

Direction:        the explicit surfacing of "typography can sometimes carry meaning" as a legitimate-counter concern in finding.md's Decision 2
Goal:             preserve sensemaking Ambiguity 4's adjudication rigor without weakening
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         apply the REFINE-direction adjustment from critique.md: add a paragraph in Decision 2's text acknowledging the typography-meaning case + the override reasoning (override exists at D6 + prose-shaped texts are the common case)
WHY:              critique D6 surfaced this as REFINE-direction; sensemaking adjudicated the trade-off but innovation's text suppressed the counter
Priority:         **HIGH** (apply before finding.md construction)    Confidence: HIGH
Guidance Mode:    compact
  · "see critique.md → Summary for Finding.md Construction item 2 for the exact paragraph to insert"  (bc the adjustment is already drafted)
Depth-link:       none

---

### R21 — B5 PDF-marginalia format-dependent caveat

Direction:        the addition of the format-dependent caveat to B5 (SourceApparatusPolicy detector spec) acknowledging PDF marginalia needs layout-analysis sub-pipeline
Goal:             honest detector-capability statement
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         apply the REFINE-direction adjustment from critique.md: add a "Format-dependent detection" caveat under B5
WHY:              critique D4 surfaced this; over-claiming detection capability sets up downstream failure
Priority:         **HIGH** (apply before finding.md construction)    Confidence: HIGH
Guidance Mode:    compact
  · "see critique.md → Summary for Finding.md Construction item 3 for the exact caveat to insert"  (bc the adjustment is already drafted)
Depth-link:       none

---

### R22 — Pandoc + 7-policy split empirical validation on calibration corpus

Direction:        empirical TEST of whether (a) Pandoc-md-superset actually handles Risale-i Nur shape texts and (b) the 7-policy split actually works when implemented
Goal:             evidence-grounded confirmation (or refutation) of Decisions 1 + 4
grain:            project-space
kind:             epistemic
engagement-type:  TEST
Movement:         run R14 (the prototype) on multiple Risale-i Nur samples; measure (a) Pandoc conversion fidelity per format and (b) per-policy detection recall + precision
WHY:              the decisions are sensemaking-adjudicated but empirically untested; the calibration corpus is the test bed
Priority:         MED (fires when R14 prototype is runnable)    Confidence: MED
Guidance Mode:    compact
  · "R14 is the engineering work; R22 is the measurement + analysis of R14's output"  (bc separate concerns)
Depth-link:       none

---

### R23 — `IntakeDoc` schema versioning + idempotency + partial-intake (open questions)

Direction:        the diagnosis of the three open questions explicitly listed in finding.md's P9
Goal:             clarify (a) whether IntakeDoc needs a version field, (b) whether intake should be idempotent, (c) how to handle partial-failure intakes
grain:            project-space
kind:             epistemic
engagement-type:  DIAGNOSE
Movement:         examine each open question (likely YES on (a) + (b); design choice on (c)) and produce a sub-decision per question — feeds into R1 schema design
WHY:              P9 explicitly listed these as open questions; resolving them refines R1
Priority:         LOW (resolvable inside R1 design)    Confidence: MED
Guidance Mode:    compact
  · "easier to resolve inside R1 design than as standalone inquiries"  (bc tightly coupled to schema details)
Depth-link:       none

---

### R24 — Calibration corpus expansion beyond Risale-i Nur

Direction:        the consolidation of intake design across multiple corpora beyond the current Risale-i Nur calibration
Goal:             validate that the structure-preservation + 7-policy detection design generalizes to other religious / theological / scholarly corpora
grain:            project-space
kind:             epistemic
engagement-type:  CONSOLIDATE
Movement:         (after R14 + R22) test intake against samples from (Talmud apparatus criticus; Vedic texts; Christian patristic editions; academic critical editions) → aggregate observations into a refined intake design
WHY:              SKILL.md framing: Risale-i Nur is calibration corpus, not product scope; this inquiry's calibration commitment needs cross-corpus validation
Priority:         LOW (future inquiry; fires after the first-corpus prototype validates)    Confidence: LOW
Guidance Mode:    compact
  · "do NOT fire until R14 + R22 produce stable Risale-i Nur results"  (bc the single-corpus baseline must hold first)
Depth-link:       none

---

## Excluded section

Notable candidate-concepts considered and rejected (with reasons):

- **Mac-app UI design beyond F4 re-entry** — out of frame per `_branch.md` MQ4 exclusion ("appification-out"); engaging this in this inquiry's onward routes would violate the inheritance.
- **Translation algorithm choices (chunking algorithm; per-policy translate-rendering implementation; output formatting)** — out of frame per `_branch.md` MQ4 exclusion ("translation-step-internals-out"); engaging these violates the intake-vs-translate boundary that Decision 4 commits.
- **Redefining the 7 schema policy classes** — out of frame per Decision 4 (RESPECTED, not redefined); engaging would invalidate the architectural foundation.
- **.compldoc precursor format for v0.2** — explicitly DEFER (A8 = DEFER in the finding); v1+ scope.
- **Round-trippability framework as v0.2 quality measure** — subsumed into R12 (intake-quality-metrics) as one of several metric candidates; not a standalone route.
- **Inter-intake-version diffing** — DEFER per surfacing D19 (advanced ops); not v0.2 scope.
- **Reference-intake comparison tool** — DEFER per surfacing D20; needs more intake artifacts to compare against.
- **Streaming-vs-load-all intake architecture decision** — operational concern; not a v0.2 design question; defers to engineering exigency.
- **Custom intake-error-reporting framework** — covered as part of R16's standard engineering; not a distinct identity.

---

## Telemetry

- **Mode:** root / project-space (breadth) · **Entry point:** fresh
- **Identities enumerated:** 24 (R1-R24); index reflects 21 load-bearing + 3 cross-cutting refinements
- **Routes at each kind:** teleological = 16 (R1-R18); epistemic = 6 (R19-R24); cross-cutting REFINE adjustments classified as epistemic
- **High-priority count:** 5 (R1 IntakeDoc schema · R14 Risale-i Nur prototype · R19/R20/R21 REFINE adjustments)
- **Individuations made:** 24 fresh identities; lean-to-split applied at the 7 detector identities (kept as 7 distinct rather than merged); R3/R8 flagged as coupled to R9 (depth-1 layout-analysis dependency)
- **Uncertain individuations:** R17 (3 small structure-engineering items) could merge into R16 — left split because they have distinct structural targets. Re-individuation could occur in a depth run.
- **Stale entries flagged:** none (fresh index)
- **Convergence:** territory swept at identity resolution; no new identities surfaced in re-sweep
- **Frontier flags emitted:** none — the inquiry's frontier (F1-F6) is fully addressed by R1 (F1) / Decision 1 (F2) / Decision 2 (F3) / R15 (F4) / Decision 4 (F5) / R9 (F6)

### LAYER 1 failure-mode check
- Over-merge: not observed (lean-to-split applied at 7 detectors)
- Under-coverage: not observed (every DESIGN-NEXT-INQUIRY + ENGINEER concept from the finding has a route or is consolidated explicitly)
- Wrong-grain: not observed (project-space identities, not manifestations)
- Goal-loss: not observed (goal-bias maintained across sweep)
- Type-misassignment: re-checked — all engagement-types are partitionable by kind; REFINE/TEST/DIAGNOSE/CONSOLIDATE are epistemic; DEVELOP/PURSUE-SEED/INVESTIGATE-FRONTIER are teleological
- Index-drift: n/a (fresh)

### LAYER 2 failure-mode check
- Selection-creep: not observed — no route is ranked as "the one to take"; Priority is attributive, not winner-ranking
- Process-coupling: not observed — no control-flow moves; no references to a larger process
- Description-collapse: not observed — routes prescribe (DEVELOP X / TEST Y), not describe how X works
- Manifestation-dump: not observed — breadth run lists 24 identities, not 38 concept manifestations

---

## Self-Assessment Verdict

**PROCEED** — territory swept at identity resolution; no LAYER 1 flags; no LAYER 2 identity-erosion. The onward route-field is enumerated; consumers (the user; subsequent inquiries) can pick any subset to engage without further routelisting.
