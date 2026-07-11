# Route Map — intake preprocessing operations

## User Input

territory: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/` (this inquiry's artifacts — `_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md` + `innovation.md` + `critique.md`).

goal: enumerate the onward route-field this inquiry opens for v0.2 intake preprocessing. Committed: 8-category preprocessing pipeline; "structural, not semantic" scope-line principle; two-layer corpus model; EPUB-first + PDF-fallback format priority; `extends:` relationship-label to prior canonical-format finding.

---

## Map Header

- **Identities enumerated:** 23
- **High-priority count:** 8 (R1-R7 MUSTs + R15 cross-cutting refinements)
- **Mode:** root / project-space (breadth)
- **Entry point:** fresh (no prior `_route.md` for this inquiry)

## Route Index

| # | Direction | grain | kind | engagement-type | Priority |
|---|---|---|---|---|---|
| R1 | Per-category operation specs (MUST 1) | project-space | teleological | DEVELOP | HIGH |
| R2 | Hierarchy-inference algorithm for flat-h1 sources (MUST 2) | project-space | teleological | DEVELOP | HIGH |
| R3 | Format-specific Pandoc invocation patterns (MUST 3) | project-space | teleological | DEVELOP | HIGH |
| R4 | Category 7 flag-exposure mechanism (MUST 4) | project-space | teleological | DEVELOP | HIGH |
| R5 | Test-case fixture corpus (MUST 5 — critique add) | project-space | teleological | DEVELOP | HIGH |
| R6 | Mac app PipelineConfig html-output integration (MUST 6 — critique add) | project-space | teleological | DEVELOP | HIGH |
| R7 | Pandoc version pin for v0.2 reproducibility (MUST 7 — critique add) | project-space | teleological | DEVELOP | HIGH |
| R8 | Category 8 extensions API design (COULD 1) | project-space | teleological | DEVELOP | MED |
| R9 | Hierarchy-inference for additional corpora (COULD 2) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R10 | Quality-floor sub-category boundary refinements (COULD 3) | project-space | epistemic | REFINE | MED |
| R11 | Word + plain-text format support (DEFERRED 1) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R12 | Cross-corpus validation (DEFERRED 2) | project-space | epistemic | TEST | LOW |
| R13 | Classification work — per-element provenance + 7-policy detection (DEFERRED 3) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R14 | Per-corpus configuration UI in Mac app (DEFERRED 4) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R15 | Cross-cutting critique refinements integration (8 wording/completeness edits at finding-compose time) | project-space | epistemic | REFINE | HIGH |
| R16 | Scope-line edge case adjudication (open question) | project-space | epistemic | REFINE | MED |
| R17 | Sentence segmentation Turkish quality (open question) | project-space | epistemic | TEST | MED |
| R18 | Hyphenation-repair false-positives mitigation (open question) | project-space | epistemic | DIAGNOSE | MED |
| R19 | EPUB-from-PDF detection heuristics (open question; critique-derived) | project-space | teleological | DEVELOP | MED |
| R20 | Multi-volume document handling (open question; critique-derived) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R21 | Intake-output versioning (open question; critique-derived) | project-space | epistemic | INVESTIGATE-FRONTIER | LOW |
| R22 | CI for v0.2 reproducibility (onward concept — engineering infrastructure) | project-space | teleological | DEVELOP | MED |
| R23 | Calibration of empirical thresholds (onward concept) | project-space | epistemic | TEST | MED |

---

## Per-Route Records

### R1 — Per-category operation specs (MUST 1)

```
Direction:        per-category operation specs (8 categories × per-operation algorithm + library refs + test cases)
Goal:             ship engineering specs ready for v0.2 intake code
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         take each of 8 categories; produce per-operation: input shape, algorithm sketch,
                  Python library ref, expected output shape, test cases
WHY:              the load-bearing engineering contract; without specs, v0.2 intake's behavior is under-specified;
                  innovation P4-P8 provided the operations + library refs, but per-operation algorithm
                  details and test cases are downstream MUST 1 work
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "Could be 8 sister `/traverse` inquiries (one per category) OR a single consolidated spec doc" (bc per-category is the natural grain;
     consolidated is easier to ship)
  · "Categories 5+6 are the heaviest (structural detection + format-specific repair); the other 6 are short specs" (bc reflects substantive weight)
  Meaning-gaps:
    - per-operation test case shape (golden output? property-based? snapshot?) — high — affects engineering reproducibility
    - hierarchy-inference algorithm in Cat 5 is its own MUST 2; specs for Cat 5 need to integrate with MUST 2 output — mid — coordination cost
Depth-link:       none
```

### R2 — Hierarchy-inference algorithm for flat-h1 sources (MUST 2)

```
Direction:        hierarchy-inference algorithm for flat-h1 sources (the Asa-yı Musa EPUB case)
Goal:             ship the algorithm spec that promotes body markers to h2/h3 in flat-h1 sources
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         specify marker-detection regex set (bold + centered + standalone); clustering policy
                  (frequency / position); depth-promotion rules (default h2; deeper via Category 8 extensions);
                  edge cases (false-positives; missing markers)
WHY:              the Asa-yı Musa EPUB has flat h1 but Mukaddeme/Mes'ele/Hâtime markers in body; without
                  inference, sub-section structure is lost; load-bearing for translation chunking + citation
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "Generic algorithm operates on bold-centered-standalone signal; Category 8 plugs in corpus-vocabulary keywords" (bc separation honors two-layer model)
  · "Conservative one-level promotion (h2 default) avoids over-inference" (bc empirical caution)
  Meaning-gaps:
    - false-positive rate on generic bold-centered-standalone detection — high — affects whether algorithm needs ML or pure regex
    - whether the algorithm produces nested `<section>` containers or flat h2 markup — mid — affects HTML5 canonical structure
Depth-link:       none
```

### R3 — Format-specific Pandoc invocation patterns (MUST 3)

```
Direction:        format-specific Pandoc invocation patterns for EPUB + PDF intake
Goal:             ship reproducible Pandoc command + pre/post-processing chain
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         document exact Pandoc commands for EPUB intake (pandoc -f epub -t html5 ...);
                  PDF intake pre-OCR chain (OCRmyPDF + Tesseract; then pandoc -f html ...);
                  post-processing for italic recovery, paratext stripping, hierarchy-inference
WHY:              Pandoc is the architectural lever (Decision 5 of original intake-concepts);
                  without documented invocation patterns, reproducibility breaks; Pandoc-version-pin
                  (MUST 7) bounds the variability operationally
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "Compose with MUST 7 (Pandoc version pin); the pattern is for a specific Pandoc version" (bc reproducibility)
  · "EPUB: pandoc + post-processing; PDF: OCRmyPDF first then pandoc" (bc per-format pipeline order)
Depth-link:       none
```

### R4 — Category 7 flag-exposure mechanism (MUST 4)

```
Direction:        Category 7 quality flags — exposure mechanism (schema + format)
Goal:             ship the flag-schema + the sidecar JSON vs HTML5 <meta> design choice
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         pick primary exposure mechanism (sidecar JSON recommended; HTML5 <meta> mirror);
                  define the JSON schema (flag codes; severity; context; positions);
                  specify how downstream consumers (translate-stage; reviewer UI) read the flags
WHY:              Category 7's "informational, not corrective" semantics require a clear exposure
                  channel; without schema, flag consumers cannot act
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "Sidecar JSON is recommended (innovation P8 working assumption)" (bc easier to extend; doesn't pollute canonical HTML5)
Depth-link:       none
```

### R5 — Test-case fixture corpus (MUST 5 — critique add)

```
Direction:        test-case fixture corpus for v0.2 validation
Goal:             ship a fixture set of source documents + expected canonical HTML5 outputs
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         collect representative fixtures (Asa-yı Musa EPUB; Asa-yı Musa PDF;
                  Muhakemat PDF; small non-Risale-i-Nur fixtures if available);
                  produce expected canonical HTML5 per fixture; per-category test cases;
                  integration tests
WHY:              critique surfaced this as a gap — engineering cannot verify v0.2 behavior
                  without test cases; reproducibility requires golden outputs
Priority:         HIGH    Confidence: MED
Guidance Mode:    compact
  · "Start with Asa-yı Musa EPUB (well-formed; easy)" (bc establishes the floor)
  · "Add Muhakemat PDF for OCR-fallback exercise" (bc tests Category 6 PDF path)
  Meaning-gaps:
    - what fixtures exist for non-Risale-i-Nur corpora — high — affects cross-corpus testing without DEFERRED 2 work
    - golden output format (HTML5 file? diff against reference?) — mid — affects test framework choice
Depth-link:       none
```

### R6 — Mac app PipelineConfig html-output integration (MUST 6 — critique add)

```
Direction:        Mac app PipelineConfig.swift html-output integration with intake
Goal:             wire intake's HTML5 canonical output to the Mac app preview/export pipeline
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         the Mac app's PipelineConfig.swift (line 42) already has `case md, html, plain, json`;
                  wire the `html` case to mean "render canonical HTML5"; integration with intake
                  invocation produces output the UI consumes
WHY:              critique surfaced this as a gap — without UI integration, intake produces files
                  no UI consumes; v0.2 ship needs the user-facing surface
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "The enum already has html; integration is wiring not enum addition" (bc reduces engineering scope)
  · "Re-decide `json` case meaning (HTML5 canonical's on-demand JSON-AST? drop?)" (bc ambiguity post-finding)
Depth-link:       none
```

### R7 — Pandoc version pin for v0.2 reproducibility (MUST 7 — critique add)

```
Direction:        Pandoc version pin for v0.2 reproducibility
Goal:             commit a specific Pandoc version for v0.2 engineering setup
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         pin a specific Pandoc version (e.g., 3.x specific minor); document in engineering
                  setup; specify upgrade-test protocol (run R5 fixtures + Category 6 EPUB/PDF
                  conversion against new Pandoc version; verify outputs match goldens)
WHY:              HTML5 conformance is W3C-stable; Pandoc's HTML5 reader/writer behavior may shift
                  between versions for edge cases; pinning bounds operational variability;
                  critique promoted this from DEFERRED to MUST for v0.2 reproducibility
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "Pin to Pandoc 3.x (specific minor) for v0.2 ship" (bc current stable line)
  · "Composes with R22 CI for reproducibility (CI enforces the pin)" (bc operational composition)
Depth-link:       none
```

### R8 — Category 8 extensions API design (COULD 1)

```
Direction:        Category 8 extensions API design (opt-in plugin mechanism)
Goal:             commit the corpus-extension plug-in mechanism for future corpus expansion
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         specify the opt-in attachment mechanism (--corpus flag at intake-time);
                  per-corpus configuration format; registration protocol; how extensions plug into
                  R2 hierarchy-inference algorithm
WHY:              Category 8 v0.2 can hardcode Risale-i Nur extension; formal API design is post-v0.2
                  needed only when a second corpus enters the project
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "v0.2 hardcoded Risale-i Nur Cat 8 is sufficient; API formalization is COULD" (bc lean-to-ship)
  · "Depends-on: R2 (hierarchy-inference) — the extension API plugs into R2's interface; GATED" (bc API depends on what to plug into)
  Meaning-gaps:
    - extension API surface (Python plugin? config file? both?) — high — affects engineering effort
Depth-link:       none
```

### R9 — Hierarchy-inference for additional corpora (COULD 2)

```
Direction:        hierarchy-inference extensions for new corpora beyond Risale-i Nur
Goal:             support more corpora as they enter the project
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         when project ingests a second corpus, identify its structural vocabulary;
                  design a Category 8 extension; integrate via R8 API
WHY:              honors the two-layer corpus model's extensibility; gated by corpus diversity
                  expansion
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "GATED on R8 (API) AND DEFERRED 2 (cross-corpus validation surface)" (bc need both before extension fires)
Depth-link:       none
```

### R10 — Quality-floor sub-category boundary refinements (COULD 3)

```
Direction:        translation-quality-floor sub-category boundary refinements
Goal:             promote / demote operations between Categories 1 and 2 as empirical evidence accumulates
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         empirical evidence from v0.2 testing may show that some Category 1 operations are
                  load-bearing for translation quality (promote to Category 2) or that some Category 2
                  operations are byte-consistency only (demote to Category 1); refine the boundary
WHY:              translation-quality-floor sub-category is named in innovation P4 but boundaries
                  are working assumption; empirical evidence may surface refinements
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "Trigger: empirical evidence from v0.2 production" (bc gated by data, not theory)
Depth-link:       none
```

### R11 — Word + plain-text format support (DEFERRED 1)

```
Direction:        Word + plain-text format support (Category 6 extensions)
Goal:             extend format priority to Word + plain-text when sources expand
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         when project source-mix expands to include Word or plain-text sources,
                  implement Category 6 operations for those formats (style-mapping; run-merge;
                  encoding detection; line-ending normalization)
WHY:              current corpus is EPUB/PDF-dominant; engineering effort is bounded by
                  observable source-mix expansion
Priority:         LOW     Confidence: HIGH
Guidance Mode:    compact
  · "Trigger: observable — project ingests Word or plain-text source" (bc demand-driven)
Depth-link:       none
```

### R12 — Cross-corpus validation (DEFERRED 2)

```
Direction:        cross-corpus validation — does the 8-category set + scope-line principle generalize?
Goal:             test the architecture against non-Risale-i-Nur corpora
grain:            project-space
kind:             epistemic
engagement-type:  TEST
Movement:         pick a second-corpus exemplar (academic book; Talmud apparatus; modern novel);
                  run intake → canonical HTML5; identify architectural strains;
                  refine the 8-category set or scope-line principle if generalization gaps surface
WHY:              project_scope memory commits generic translation; cross-corpus is the
                  generalization check that protects against Risale-i-Nur-specific over-fit
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "GATED on R5 stability — establish v0.2 floor on Risale-i Nur first" (bc cross-corpus on unstable architecture is premature)
Depth-link:       none
```

### R13 — Classification work (DEFERRED 3)

```
Direction:        classification work — per-element provenance + 7-policy detection
Goal:             revive the deferred classification scope when production testing requires it
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         when minimal-intake is tested in production AND translation quality empirically
                  requires classification, design per-element provenance encoding + 7-policy
                  detection per the original intake-concepts finding's Decision 4 roadmap
WHY:              the 7 schema policies (NonMainLangParts / SourceApparatus / VoiceMarking /
                  ArchaicRegister / Honorifics / FormulaicOpening / EmbeddedPoetry) are the canonical
                  classification roadmap; preserved as roadmap, not v0.2 implementation
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "Revival trigger: condition-bound — minimal-intake tested AND classification empirically needed" (bc two conditions)
  · "Composes with the prior canonical-format finding's per-policy class conventions + provenance encoding MUSTs (now also DEFERRED)" (bc cross-finding gate)
Depth-link:       none
```

### R14 — Per-corpus configuration UI in Mac app (DEFERRED 4)

```
Direction:        per-corpus configuration UI in the Mac app
Goal:             user-facing corpus selection at intake-time
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         add UI element to the Mac app for corpus selection at intake-time; integrate with R8 API
WHY:              corpus selection becomes user-facing only when multiple corpora exist;
                  GATED on R8 API + a second corpus
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "GATED on R8 AND R9 (extension AND additional corpus)" (bc both must exist)
Depth-link:       none
```

### R15 — Cross-cutting critique refinements integration (HIGH-priority pre-CONCLUDE work)

```
Direction:        integrate critique's 8 cross-cutting refinements into the finding at CONCLUDE
Goal:             the finding's text reflects critique-surfaced wording + completeness sharpening
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         apply per critique.md verdicts:
                  (a) P2 — soften scope-line wording: "operational with explicit gray-zone path"
                  (b) P3 — split letter-spaced un-spacing: operation generic (Cat 1); Turkish regex calibration (Cat 8)
                  (c) P4 — three small additions (sentence-seg chunking-rationale; LRM/RLM in zero-width stripping; script-specific punctuation preservation note)
                  (d) P6 — h6 ceiling caveat (rarely-exceeded; typical h4 cap; permissive policy)
                  (e) P7 — three small additions (EPUB-first well-formed qualification; EPUB-from-PDF routing; python-bidi alternative to OCR)
                  (f) P9 — per-element-provenance reversal explicit
                  (g) P10 — Decision 4 wording tightened + per-element provenance in re-test as INVALIDATED-FOR-V0.2
                  (h) P12 — three open questions added (multi-volume; intake-output versioning; EPUB-quality detection)
WHY:              critique surfaced 8 refinement targets; CONCLUDE composes finding.md and is the
                  moment to apply; without integration, finding text doesn't reflect critique honesty
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "Apply at CONCLUDE composition time (before finding.md is committed)" (bc workflow-anchored)
  · "All are wording/completeness; no architectural change" (bc bounds the work)
Depth-link:       none
```

### R16 — Scope-line edge case adjudication (open question)

```
Direction:        scope-line edge case adjudication (as new gray-zone operations surface)
Goal:             refine the principle's gray-zone adjudication path
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         when a new gray-zone operation surfaces during v0.2 engineering or in sister inquiries,
                  apply the scope-line test; document the adjudication; update P2's worked examples
WHY:              the principle has worked examples + an explicit gray-zone path (P12 open question);
                  refinement accumulates as evidence
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "Trigger: observable — new gray-zone operation surfaces" (bc demand-driven)
Depth-link:       none
```

### R17 — Sentence segmentation Turkish quality (open question)

```
Direction:        sentence segmentation quality for Turkish
Goal:             validate spacy xx_sent_ud_sm or nltk Punkt against Turkish corpus
grain:            project-space
kind:             epistemic
engagement-type:  TEST
Movement:         exercise sentence segmentation against Turkish text (Asa-yı Musa Turkish prose);
                  measure error rate at known boundary cases (abbreviations; ordinals; Bismillah-prefix);
                  evaluate against alternatives if needed
WHY:              Category 2 commits sentence segmentation as load-bearing for chunking;
                  empirical validation against Turkish is needed; out-of-the-box models may
                  have Turkish-specific failure cases
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "Trigger: empirical evidence of segmentation errors in v0.2 testing" (bc gated by data)
  · "Refinement may require custom Punkt training or Turkish-specific abbreviation dictionary" (bc known mitigation paths)
Depth-link:       none
```

### R18 — Hyphenation-repair false-positives mitigation (open question)

```
Direction:        hyphenation-at-line-break repair false-positives mitigation
Goal:             prevent false-positive merges (intentional line-breaks in verse, lists, emphasis)
grain:            project-space
kind:             epistemic
engagement-type:  DIAGNOSE
Movement:         characterize false-positive instances (when the regex merges intentional line-breaks);
                  design mitigation (apply only in body paragraphs; exclude verse-block / list contexts);
                  document conditions
WHY:              Category 2's hyphenation-repair regex `(\w+)-\n(\w+)` may wrongly merge intentional
                  line-breaks; identifying the failure modes is prerequisite for mitigation
Priority:         MED     Confidence: HIGH
Guidance Mode:    compact
  · "Trigger: false-positive instances observed during v0.2 testing" (bc empirical)
  · "Mitigation: apply hyphenation-repair only in body paragraphs, not in verse/list contexts" (bc straightforward bound)
Depth-link:       none
```

### R19 — EPUB-from-PDF detection heuristics (open question; critique-derived)

```
Direction:        EPUB-from-PDF detection heuristics (route low-quality EPUBs to PDF path)
Goal:             detect EPUBs that were converted from PDF and inherit PDF problems
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design detection heuristics (OCR artifacts in text; flat-h1 only; minimal CSS;
                  presence of mid-word hyphens; broken-bidi Arabic in text-layer);
                  combine with Category 7 quality flags; route detected cases to PDF processing path
WHY:              critique surfaced that EPUB-first commitment is well-formed-EPUB-first;
                  EPUB-from-PDF cases inherit PDF problems and benefit from PDF intake's bidi-fix +
                  OCR fallback; detection is needed for routing
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "Heuristic combination — no single signal is decisive" (bc empirical detection)
  · "Composes with Category 7 quality flags (epub-quality-low could be one)" (bc design integration)
Depth-link:       none
```

### R20 — Multi-volume document handling (open question; critique-derived)

```
Direction:        multi-volume document handling (e.g., Risale-i Nur Külliyat)
Goal:             handle multi-volume works coherently
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         when project ingests a multi-volume work, decide whether each volume is its own
                  intake unit or whether they compose into a single multi-volume canonical;
                  design cross-volume references / inter-volume cross-references
WHY:              Risale-i Nur Külliyat is 5+ volumes (Sözler; Mektubat; Lem'alar; Şualar; Mesnevi-i Nuriye);
                  current v0.2 handles single-volume; multi-volume composition needs design
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "Trigger: project ingests a multi-volume work" (bc demand-driven)
Depth-link:       none
```

### R21 — Intake-output versioning (open question; critique-derived)

```
Direction:        intake-output versioning (when preprocessing op specs change, existing outputs re-derive)
Goal:             enable re-intake of existing sources after operation spec refinement
grain:            project-space
kind:             epistemic
engagement-type:  INVESTIGATE-FRONTIER
Movement:         design versioning scheme for canonical HTML5 output (intake-version stamp; diff against
                  prior version; stable IDs for sections across re-intakes);
                  determine when to re-derive (auto on spec change? on-demand? never?)
WHY:              critique surfaced as gap — when a Cat 5 or Cat 6 operation's spec changes,
                  existing canonical HTML5 outputs become outdated; versioning enables tracked re-derivation
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "Trigger: a preprocessing op spec changes and existing outputs need re-derivation" (bc demand-driven)
Depth-link:       none
```

### R22 — CI for v0.2 reproducibility (onward concept)

```
Direction:        CI infrastructure for v0.2 reproducibility (engineering)
Goal:             automated verification that v0.2 intake produces stable canonical HTML5
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         set up CI pipeline that runs R5 fixture intake; compares against golden HTML5 outputs;
                  verifies the Pandoc-version pin is in place; runs per-category test cases;
                  surfaces failures as CI blockers
WHY:              v0.2 ship requires reproducible behavior; CI enforces R7 (Pandoc pin) +
                  catches regressions in R1 per-category specs; load-bearing for engineering discipline
Priority:         MED     Confidence: HIGH
Guidance Mode:    compact
  · "Composes with R5 (fixtures) + R7 (Pandoc pin) + R1 (per-category specs)" (bc CI consumes all three)
  · "GitHub Actions or local pre-commit; engineering choice" (bc infrastructure detail)
Depth-link:       none
```

### R23 — Calibration of empirical thresholds (onward concept)

```
Direction:        calibration of empirical thresholds (for various heuristic operations)
Goal:             commit specific threshold values for heuristic preprocessing operations
grain:            project-space
kind:             epistemic
engagement-type:  TEST
Movement:         enumerate operations that depend on empirical thresholds (letter-spaced un-spacing
                  frequency cutoff; bold-centered standalone-line heading-detection threshold;
                  orphan-content character-count threshold; duplicate-content similarity threshold);
                  measure against calibration corpus; commit threshold values
WHY:              several operations have implicit thresholds that v0.2 needs to commit;
                  empirical calibration against the corpus is the natural mechanism
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "Trigger: when v0.2 engineering needs threshold commitments" (bc engineering-pull)
  · "Calibration corpus = Risale-i Nur initially; revisit as cross-corpus validation surfaces" (bc anchor + revision)
Depth-link:       none
```

---

## Excluded

| Candidate | Reason |
|---|---|
| "Re-implement classification (per-element provenance / per-policy detection) in v0.2" | excluded — DEFERRED 3 per scope narrowing; revival path preserved as R13; not v0.2 work |
| "Word + plain-text format support in v0.2" | excluded — DEFERRED 1 per format-priority commitment; revival as R11; not v0.2 work |
| "Per-element lang= tagging at intake" | excluded — semantic role tagging per scope-line principle; deferred with classification (R13) |
| "Drop the prior canonical-format finding's HTML5 commitment" | excluded — settled; this inquiry doesn't re-open canonical format |
| "Re-litigate the user's depth-4 instinct vs source-driven up-to-h6" | excluded — settled in P6 + critique R-P6 caveat; not a route, a commitment |
| "Per-category sub-inquiries (8 separate routelisting calls)" | excluded — over-decomposition at routelist breadth grain; R1 is the proper merged identity |
| "Define preprocessing for translate-stage prompt prep (tokenization; chunking)" | excluded — translate-stage scope, not intake; per MQ4 exclusion |
| "Publishing-stage CSS template for Arabic typography" | excluded — publishing-stage scope, not intake; per MQ4 exclusion |

---

## Telemetry

| Field | Value |
|---|---|
| Mode | root / project-space (breadth) |
| Entry point | fresh |
| Identities enumerated | 23 |
| Routes — teleological | 14 |
| Routes — epistemic | 9 |
| High-priority count | 8 (R1-R7 + R15) |
| Individuations made | 23 splits; 0 merges; one deliberate merge (R15 cross-cutting refinements bundled at finding-compose-time grain) |
| Uncertain individuations flagged | 1 (R8 Category 8 API design — borderline DEVELOP vs INVESTIGATE-FRONTIER; chose DEVELOP because the API shape is concrete enough) |
| Stale entries flagged | 0 (fresh entry point) |
| Convergence status | converged (territory swept at identity resolution; no uncertain-relevance items filtered) |
| Frontier flags emitted | 0 (no sub-territories warranted "drill here") |
| LAYER 1 modes scanned | Over-merge: no (lean-to-split applied; R7 vs R22 kept separate; R10 vs R23 kept separate). Under-coverage: no (MUST/COULD/DEFERRED + critique-refinements + open-questions + onward-concepts all covered per user goal). Wrong-grain: no (all routes at identity grain). Goal-loss: no (goal-bias preserved). Type-misassignment: no (verbs match membership test). Index-drift: NA (fresh). |
| LAYER 2 modes scanned | Selection-creep: no (Priority/Confidence attributive). Process-coupling: no (routes are concept-directions). Description-collapse: no (routes are prescriptive). Manifestation-dump: no (one route per identity). |
| Self-assessment verdict | **PROCEED** |

---

## Self-Assessment

**PROCEED.** Territory swept at identity resolution; 23 concept-identities individuated from the inquiry's 7 artifacts + user-named scope items. No LAYER 1 or LAYER 2 flags. One uncertain-individuation noted (R8 engagement-type borderline; chose DEVELOP with reasoning). Output ready for the routelog / consumer step.
