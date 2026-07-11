# Route Map — post-repair canonical format

## User Input

territory: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/ (this inquiry's artifacts — _branch.md + articulate_simple.md + surfacing.md + sensemaking.md + decomposition.md + innovation.md + critique.md).

goal: from _branch.md's Goal — enumerate the onward route-field this inquiry opens for the post-repair canonical format question. The inquiry committed the architectural REFINEMENT: three-layer architecture PRESERVED + canonical-layer format SWAP JSON-AST → HTML5 (F1 = HTML5 canonical; F2 = Pandoc's markdown hand-edit preserved; F3 = EPUB 3 publishing preserved). REFINES prior canonical-format inquiry; PRESERVES original intake-concepts Decisions 2-5.

The route-field should enumerate: MUST 1/2/3 + COULD 1/2/3 actions from P9; 4-5 cross-cutting refinements from critique; frontier items from P10; onward concept routes the HTML5-as-canonical commitment opens (intake pipeline; 7 detector designs on HTML5 DOM; calibration prototype; EPUB CSS; Mac app integration).

Save to: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/routelister.md (route-map) + .../\_route.md (persistent index; fresh).

---

## Map Header

- **Identities enumerated:** 22
- **High-priority count:** 7 (R1, R2, R3, R6, R19, R20 + R22)
- **Mode:** root / project-space (breadth)
- **Entry point:** fresh (no prior `_route.md` for this inquiry; goal is single-purpose)

## Route Index

| # | Direction | grain | kind | engagement-type | Priority |
|---|---|---|---|---|---|
| R1 | HTML5 schema / validation profile (MUST 1) | project-space | teleological | DEVELOP | HIGH |
| R2 | Per-policy class-attribute conventions (MUST 2) | project-space | teleological | DEVELOP | HIGH |
| R3 | Per-element provenance encoding pattern (MUST 3) | project-space | teleological | DEVELOP | HIGH |
| R4 | HTML5 → EPUB 3 packaging pipeline (COULD 1) | project-space | teleological | DEVELOP | MED |
| R5 | HTML5-to-markdown round-trip-stable subset (COULD 2) | project-space | epistemic | REFINE | MED |
| R6 | Risale-i Nur sample prototype (COULD 3) | project-space | epistemic | TEST | HIGH |
| R7 | Parser-determinism axis caveat (P2 + P3 refinement) | project-space | epistemic | REFINE | MED |
| R8 | Polyglot wording precision (P4 refinement) | project-space | epistemic | REFINE | LOW |
| R9 | Dual-persistent clarification (P7 refinement) | project-space | epistemic | REFINE | LOW |
| R10 | TEI architectural-lever wording (P7 refinement) | project-space | epistemic | REFINE | LOW |
| R11 | JSON-AST bias-balance acknowledgment (P7 refinement) | project-space | epistemic | REFINE | MED |
| R12 | TEI as future archival output format | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R13 | Pandoc version pinning policy | project-space | teleological | DEVELOP | MED |
| R14 | HTML5 Living Standard version stability snapshot | project-space | teleological | DEVELOP | LOW |
| R15 | Cross-corpus format-architecture validation | project-space | epistemic | TEST | LOW |
| R16 | Archival / historical preservation as 5th temporal layer | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R17 | In-memory representation choice (HTML5 DOM vs Pandoc AST) | project-space | teleological | PURSUE-SEED | MED |
| R18 | Per-translation-output format expansion (PDF / reveal.js / LaTeX) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R19 | Intake pipeline producing HTML5 canonical | project-space | teleological | DEVELOP | HIGH |
| R20 | The 7 detector designs operating on HTML5 DOM | project-space | teleological | DEEPEN | HIGH |
| R21 | EPUB CSS template for Arabic typography | project-space | teleological | DEVELOP | MED |
| R22 | Mac app PipelineConfig.swift html-output integration | project-space | teleological | DEVELOP | MED |

---

## Per-Route Records

### R1 — HTML5 schema / validation profile (MUST 1)

```
Direction:        HTML5 schema / validation profile design
Goal:             commit a HTML5 profile + validation tooling for the canonical layer
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         specify which HTML5 features are required (sections; aside; figure;
                  span with semantic classes), which are forbidden (script/style; pure-
                  content forbiddance); pick project RNG schema OR html5validator + Python
                  checks; ship a `intake/html5_profile.rng` (or equivalent) + docs
WHY:              the finding's canonical commitment is HTML5 Living Standard as the
                  working assumption; without a project-specific profile, canonical-conformance
                  cannot be checked beyond W3C-validity
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "two-layer split — layer 1 = HTML5 conformance via html5validator (operational day 1);
     layer 2 = project RNG profile" (bc innovation P4's hedge specifies this split)
  · "RNG schema vs Python checks is the load-bearing decision" (bc RNG is declarative + reusable; Python checks are flexible + project-coupled)
  Meaning-gaps:
    - choice between RNG and html5validator+Python checks — high — gates downstream tooling shape
    - "pure-content" forbiddance scope (script? style? meta beyond head?) — mid — affects downstream readers
Depth-link:       none (not yet drilled)
```

### R2 — Per-policy class-attribute conventions (MUST 2)

```
Direction:        per-policy class-attribute conventions for the 7 schema policies
Goal:             commit a stable convention mapping {policy → HTML5 element + class}
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         decide between (a) role-based class names — class="marginalia" /
                  class="couplet" / class="formulaic-opening" / class="voice-cited" /
                  class="archaic-register" / class="honorific" — per innovation P6
                  working assumption; (b) policy-named via data-policy="source-apparatus"
                  mapped to schemas.py class names; (c) hybrid. Ship
                  intake/policy_conventions.md.
WHY:              the 7 detectors (Decision 4 of original intake-concepts) operate on
                  the conventions; the convention IS the contract between detector
                  perception and HTML5 storage
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "role-based is innovation's working assumption" (bc P6 used it for the worked examples)
  · "policy-named gives 1:1 traceability to schemas.py class names" (bc it preserves the policy-class name as the contract anchor)
  Meaning-gaps:
    - whether the hybrid (role-based class + policy-named data-attribute) is over-engineered — mid — affects spec parsimony
    - how the convention extends when a new policy is added (forward-compatibility) — mid — bears on schema profile evolution
Depth-link:       none
```

### R3 — Per-element provenance encoding pattern (MUST 3)

```
Direction:        per-element provenance + confidence encoding (data-* spec)
Goal:             commit data-* field names + value vocabularies + confidence calibration
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         pin data-source values to a closed enum
                  ("text-layer" / "ocr-tesseract" / "hand-edit" / "derived");
                  pin data-confidence numeric range + Tesseract-to-internal scale
                  conversion (Tesseract 0–100 → internal 0.0–1.0); pin data-intake-pass
                  semantics (pass-number; pass-name; both?); ship
                  intake/provenance_spec.md
WHY:              the load-bearing NEW dimension; markdown's structural absence here
                  is what kills markdown at canonical; the data-* mechanism must be
                  unambiguous for detectors + readers + auditors to depend on it
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "data-source as closed enum keeps validators simple" (bc free-form would defeat schema validation)
  · "Tesseract 0–100 → 0.0–1.0 is a conversion convention not a value-domain convention" (bc both scales are semantically equivalent; the project picks the internal one)
  Meaning-gaps:
    - whether data-intake-pass carries pass-number, pass-name, or both — mid — affects log / audit shape
    - whether non-reconstructed (text-layer-clean) elements MUST carry data-* attrs or MAY — mid — affects file size + auditability
Depth-link:       none
```

### R4 — HTML5 → EPUB 3 packaging pipeline (COULD 1)

```
Direction:        HTML5 → EPUB 3 packaging script
Goal:             ship a deterministic HTML5-to-EPUB-3 conversion + packaging path
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         specify Pandoc invocation flags (pandoc -f html -t epub3); OPF
                  manifest construction; cover-image handling; per-chapter file structure
                  within the EPUB; CSS template (links to R21); ship publish/epub.py
                  + CSS template
WHY:              HTML5 → EPUB is the near-identity transform (EPUB IS xhtml +
                  manifest + zip); making the path deterministic is engineering-only
Priority:         MED     Confidence: HIGH
Guidance Mode:    compact
  · "Pandoc handles xhtml5 → epub3 packaging mostly out-of-the-box" (bc EPUB content documents are xhtml)
  · "the project-specific work is the CSS template + OPF metadata + cover image" (bc Pandoc's defaults are not project-aware)
Depth-link:       none
```

### R5 — HTML5-to-markdown round-trip-stable subset (COULD 2)

```
Direction:        the markdown features that survive HTML5 ↔ markdown round-trips
Goal:             define the hand-edit format's actual capability boundary
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         enumerate Pandoc-markdown features (per the canonical extension set);
                  test each via pandoc md → html → md cycle; document which features
                  survive losslessly; document which features drift and how; commit the
                  hand-edit contract to the survivors
WHY:              hand-edit byte-stability under no-op save is load-bearing for the
                  recovery workflow; this REFINEs which markdown features hand-editors
                  may rely on
Priority:         MED     Confidence: HIGH
Guidance Mode:    compact
  · "Pandoc's documented format matrix lists native-to-Pandoc features" (bc those are most likely to survive)
  · "the boundary is empirical, not declarable from the spec alone" (bc Pandoc's md reader/writer behavior is the test)
Depth-link:       none
```

### R6 — Risale-i Nur sample prototype (COULD 3)

```
Direction:        end-to-end prototype on a calibration corpus sample
Goal:             validate the architectural refinement against a single volume
grain:            project-space
kind:             epistemic
engagement-type:  TEST
Movement:         pick ONE Risale-i Nur volume (Asa-yı Musa OR Muhakemat, whichever
                  exercises more policy targets); run intake (text-layer Pandoc +
                  OCR Tesseract for broken-bidi or image-only Arabic) → HTML5
                  canonical (with 7-policy elements + provenance data-* attributes);
                  verify in 3+ EPUB readers (Apple Books, Calibre, Google Play Books);
                  iterate the schema profile + class conventions + provenance encoding
                  against findings
WHY:              the prototype IS the calibration anchor; until a real volume goes
                  through end-to-end, the commitment is structural but unvalidated
                  empirically
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "Muhakemat exercises image-only Arabic (harder)" (bc OCR-tesseract sub-pipeline is fully exercised)
  · "Asa-yı Musa exercises broken-bidi text-layer Arabic" (bc bidi-repair sub-pipeline is exercised; different stress test)
  · "MUST 1-3 should be drafted before R6 begins" (bc the prototype needs the conventions to test against)
Depth-link:       none
```

### R7 — Parser-determinism axis caveat (P2 + P3 refinement)

```
Direction:        add parser-implementation-variability axis to the finding
Goal:             the finding honestly engages JSON-AST's parser-determinism advantage
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         in P3 capability matrix, add a row "Parser-implementation determinism"
                  with JSON-AST=✓✓ (single canonical parser via panflute) and HTML5=✓wa
                  (multiple parsers — lxml.html / html5lib / browser parsers — with
                  documented edge-case divergence; bounded operationally via parser-
                  pinning + canonical-write-via-Pandoc-only + single named reader parser);
                  in P2, add a caveat-sentence naming the trade-off + operational bounds;
                  adjust P3's Pareto-dominance verdict wording from "Pareto-dominant" to
                  "Pareto-dominant on every format axis; with operational bounds on the
                  one axis (parser-determinism) where JSON-AST has a strict advantage"
WHY:              critique D2 substance-criterion check surfaced parser-determinism as
                  a JSON-AST advantage axis the matrix omits; honest engagement strengthens
                  the finding's claim shape
Priority:         MED     Confidence: HIGH
Guidance Mode:    compact
  · "the refinement is wording + one matrix row; not architectural" (bc HTML5 still wins overall)
  · "operational bounds belong in P9's transition plan too" (bc Pandoc version pinning + parser pinning are operational concerns)
Depth-link:       none
```

### R8 — Polyglot wording precision (P4 refinement)

```
Direction:        precision on the W3C Polyglot Markup NOTE's status
Goal:             the finding does not overstate W3C's polyglot guidance
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         refine P4's "per W3C polyglot guidelines" to "per the polyglot HTML5
                  concept (the W3C Polyglot Markup NOTE, discontinued 2014, defined
                  the writing convention; the concept remains usable as a self-imposed
                  convention)"
WHY:              critique D1 anti-hallucination check surfaced the wording-imprecision;
                  the polyglot CONCEPT is real; the W3C "guideline" wording overstates
                  the spec's current status
Priority:         LOW     Confidence: HIGH
Guidance Mode:    compact
  · "self-imposed-convention framing preserves the substance" (bc polyglot HTML5/XHTML5 is operational regardless of W3C status)
Depth-link:       none
```

### R9 — Dual-persistent clarification (P7 refinement)

```
Direction:        precision on "dual JSON-AST + HTML5" rejection scope
Goal:             P7 makes clear it rejects dual PERSISTENT storage, not dual representation
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         change P7's "Dual JSON-AST + HTML5 — rejected" to "Dual *persistent*
                  JSON-AST + HTML5 — rejected (dual representation IS preserved via
                  on-demand `pandoc -f html -t json`)"
WHY:              critique D3 rejection-rigor check found the wording slightly ambiguous;
                  the substance (no dual persistent storage) is correct; the wording
                  benefits from explicit scope
Priority:         LOW     Confidence: HIGH
Guidance Mode:    compact
  · "the on-demand reachability of JSON-AST IS the dual-representation preservation" (bc it satisfies any consumer that needs the AST shape without storage cost)
Depth-link:       none
```

### R10 — TEI architectural-lever wording (P7 refinement)

```
Direction:        strengthen TEI rejection wording from "operational" to "architectural-lever"
Goal:             the rejection's structural basis is named correctly
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         change P7's "The rejection is operational" framing for TEI to "The
                  rejection is architectural — it would break Decision 5's Pandoc-as-
                  architectural-lever commitment from the original intake-concepts
                  finding"
WHY:              the substance is architectural-lever preservation (Decision 5), not
                  merely operational; the wording strengthening makes the basis explicit
Priority:         LOW     Confidence: HIGH
Guidance Mode:    compact
  · "this connects the TEI rejection to inherited Decision 5" (bc Pandoc-as-lever is what hard-blocks Pandoc-read-absent formats)
Depth-link:       none
```

### R11 — JSON-AST bias-balance acknowledgment (P7 refinement)

```
Direction:        add bias-balance acknowledgment to JSON-AST rejection in P7
Goal:             the rejection engages JSON-AST's machine-readability advantage explicitly
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         add to P7's JSON-AST rejection: "JSON-AST has a genuine machine-
                  readability advantage (direct object-tree access via panflute) that
                  HTML5 (DOM access via lxml.html / html5lib) must work to match. This
                  is the legitimate concern preserved; HTML5's compensating advantages
                  (document-shape; W3C-standard; EPUB substrate; native lang/dir/data-*)
                  outweigh the access-shape difference at the canonical layer."
WHY:              critique D10 bias-balance check found JSON-AST's machine-readability
                  technically engaged but not narratively acknowledged
Priority:         MED     Confidence: HIGH
Guidance Mode:    compact
  · "bias-balance is preventing confirmation bias on the swap commitment" (bc the swap looks cleaner if HTML5's costs aren't surfaced)
Depth-link:       none
```

### R12 — TEI as future archival output format

```
Direction:        TEI as a future archival-output target from HTML5 canonical
Goal:             retain TEI as a deferred-but-not-dismissed archival route
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         document TEI as a possible future archival-output format generated
                  via `pandoc -f html -t tei` from HTML5 canonical; specify the revival
                  trigger (scholarly archival use case named by the project OR cross-
                  corpus validation surfaces a TEI requirement)
WHY:              TEI is the scholarly-text-encoding standard; the rejection at canonical
                  is architectural (Decision 5 / Pandoc-read absence); TEI as archival
                  OUTPUT (Pandoc-write-supported) is structurally available
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "revival-trigger-gated — do not enter until trigger fires" (bc current scope is publishing/translation, not archival)
Depth-link:       none
```

### R13 — Pandoc version pinning policy

```
Direction:        Pandoc version pinning + migration policy
Goal:             the project pins a Pandoc version and documents migration policy
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         pin a project Pandoc version (engineering choice); document the
                  upgrade-test protocol (run R6 prototype's intake + EPUB conversion
                  against new Pandoc version; verify round-trip-stable subset survives);
                  ship a pinning + migration policy doc
WHY:              HTML5 conformance is W3C-stable; Pandoc's HTML5 reader/writer
                  behavior MAY shift between versions for edge cases; version pinning
                  bounds the risk
Priority:         MED     Confidence: HIGH
Guidance Mode:    compact
  · "the parser-determinism caveat (R7) and this pinning policy compose" (bc both bound the multi-parser variability operationally)
Depth-link:       none
```

### R14 — HTML5 Living Standard version stability snapshot

```
Direction:        commit a "minimum HTML5 features required" snapshot policy
Goal:             the canonical commitment doesn't drift with HTML5 Living Standard updates
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         pin the project's HTML5 feature dependencies as a snapshot of the
                  Living Standard at intake-time; document a "minimum features
                  required" policy + an update-cadence (annual? trigger-based?)
WHY:              HTML5 Living Standard evolves continuously; new elements + attributes
                  MAY be added; project policy should bound the dependency surface
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "low frequency — Living Standard rarely breaks existing features" (bc backward compatibility is its design constraint)
Depth-link:       none
```

### R15 — Cross-corpus format-architecture validation

```
Direction:        test HTML5-as-canonical against corpora beyond Risale-i Nur
Goal:             empirically validate the architecture generalizes
grain:            project-space
kind:             epistemic
engagement-type:  TEST
Movement:         pick a second-corpus exemplar (Talmud apparatus criticus; Vedic texts;
                  Christian patristic editions; modern academic books); exercise intake
                  → HTML5 canonical → publishing; surface architectural strains
WHY:              the calibration corpus is Risale-i Nur; the project's wider
                  ambition (per CLAUDE memory and prior inquiries) is generalizable
                  translation; cross-corpus is the generalization check
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "scaling-gated — do not enter until calibration is stable" (bc cross-corpus on an unstable architecture is premature)
Depth-link:       none
```

### R16 — Archival / historical preservation as 5th temporal layer

```
Direction:        archival / historical preservation as a separate temporal layer
Goal:             evaluate whether the architecture needs a 5th layer for archival
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         frame the question: do canonical (intake/translate) + hand-edit +
                  publishing cover all temporal needs, or is long-term archival
                  (TEI? JATS? a long-term-stable HTML5 profile?) a separate layer?
                  investigate when project maturity surfaces the need
WHY:              the three-layer architecture covers intake/translate, hand-edit,
                  publishing; archival is a different temporal axis (decades, not
                  publishing-cycle); may need separate optima
Priority:         LOW     Confidence: MED
Guidance Mode:    compact
  · "carried forward from prior canonical-format inquiry's frontier" (bc deferral chain is consistent)
Depth-link:       none
```

### R17 — In-memory representation choice (HTML5 DOM vs Pandoc AST)

```
Direction:        in-memory representation choice — HTML5 DOM vs Pandoc AST
Goal:             commit which Python representation the IntakeDoc uses
grain:            project-space
kind:             teleological
engagement-type:  PURSUE-SEED
Movement:         decide between (a) parsed HTML5 DOM via lxml.html or html5lib;
                  (b) Pandoc AST via panflute; (c) thin pydantic layer wrapping either;
                  evaluate by detector-design fit + querying ergonomics + serialization
                  to canonical HTML5; commit the choice in the detector design inquiries
WHY:              the two shapes are isomorphic but Python tooling fit differs;
                  the seven detectors operate on the in-memory shape — fit matters
                  for code clarity + ergonomic queries
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "this decision feeds into R20 (detector designs)" (bc detector ergonomics depend on which library they target)
  · "thin pydantic over DOM is the working assumption" (bc P4 notes project-specific invariants may want enforcement)
  Meaning-gaps:
    - whether either choice meaningfully constrains the detector design — high — affects R20 entry shape
    - whether dual-mode (DOM for queries; AST for transforms) becomes attractive — mid — affects code complexity
Depth-link:       none
```

### R18 — Per-translation-output format expansion (PDF / reveal.js / LaTeX)

```
Direction:        publishing-output format expansion beyond EPUB 3
Goal:             identify additional output formats reachable from HTML5 canonical
grain:            project-space
kind:             teleological
engagement-type:  INVESTIGATE-FRONTIER
Movement:         enumerate additional Pandoc-writable targets from HTML5 (PDF via
                  weasyprint / wkhtmltopdf; reveal.js for slides; LaTeX for academic
                  submissions); evaluate each against use cases; expand the publishing
                  layer's format options as use cases emerge
WHY:              HTML5 → many publishing formats is a structural advantage; the
                  three-layer architecture's publishing slot is currently EPUB-only;
                  expansion is gated by use case
Priority:         LOW     Confidence: HIGH
Guidance Mode:    compact
  · "expansion-gated — enter when use case names a target" (bc speculative format-expansion is over-engineering)
Depth-link:       none
```

### R19 — Intake pipeline producing HTML5 canonical

```
Direction:        the intake pipeline producing HTML5 canonical
Goal:             build the engineering that turns source PDFs into HTML5 canonical
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         design + implement the multi-pass intake pipeline (text-layer Pandoc-md
                  + OCR Tesseract + style recovery + structure detection + paratext
                  stripping + 7-policy classification + provenance attribution) producing
                  HTML5 canonical output; the pipeline IS the engineering version of
                  the original intake-concepts finding's 5-stage shape applied to the
                  refined canonical commitment
WHY:              the intake pipeline is the load-bearing engineering work — until it
                  exists, the architectural commitment is structural-only; the prior
                  intake-concepts finding's 38 concepts and 5 stages need to become code
Priority:         HIGH    Confidence: HIGH
Guidance Mode:    compact
  · "the pipeline orchestration was Decision 5's lever — Pandoc + OCR" (bc both are external tools the pipeline orchestrates)
  · "MUST 1-3 are inputs to this pipeline's spec" (bc the schema profile / class conventions / provenance encoding all bear on output shape)
  · "this is the engineering scope, not a single inquiry" (bc the pipeline subsumes many smaller engineering inquiries)
  Meaning-gaps:
    - whether the pipeline is composed pass-by-pass (modular) or single-call (monolithic) — mid — affects testability
    - whether HTML5 generation is via Pandoc (md → html5) or direct DOM-builder (after OCR + classification) — high — affects detector ergonomics
Depth-link:       none
```

### R20 — The 7 detector designs operating on HTML5 DOM

```
Direction:        the 7 policy-perception detectors' specs refined to HTML5 DOM operations
Goal:             each detector's spec is concrete against the HTML5 representation
grain:            project-space
kind:             teleological
engagement-type:  DEEPEN
Movement:         take each of the 7 detectors (NonMainLangPartsPolicy /
                  SourceApparatusPolicy / VoiceMarkingPolicy / ArchaicRegisterPolicy /
                  HonorificsPolicy / FormulaicOpeningPolicy / EmbeddedPoetryPolicy) and
                  specify its perception algorithm + DOM operation + class-tagging
                  pattern (per R2 conventions) + confidence emission (per R3 spec); the
                  detector designs are 7 sister inquiries
WHY:              the 7 detectors were committed in Decision 4 of the original intake-
                  concepts finding; their specs were schema-level; this inquiry's HTML5
                  commitment refines them to DOM-level concreteness
Priority:         HIGH    Confidence: MED
Guidance Mode:    compact
  · "depends on R17 (in-memory representation choice) for the operating substrate" (bc detector code differs by lxml/html5lib/panflute)
  · "each detector is a separate /traverse inquiry" (bc each has distinct calibration content + algorithm choice)
  Meaning-gaps:
    - whether detectors operate during intake (writing classes inline) or post-intake (annotating an unclassed DOM) — high — affects pipeline staging
    - the inter-detector ordering when multiple detectors apply to one element — mid — affects determinism
Depth-link:       none
```

### R21 — EPUB CSS template for Arabic typography

```
Direction:        EPUB CSS template specifically for Arabic + bilingual typography
Goal:             ship a project CSS template covering Arabic font + RTL + per-policy classes
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         specify font fallback chain (Amiri / Naskh fonts for Arabic spans;
                  Latin font for Turkish narrative; bilingual rendering at span level);
                  RTL block handling (dir=rtl on blocks + spans); per-policy CSS classes
                  (marginalia formatting; couplet formatting; honorific styling); ship
                  publish/epub.css
WHY:              EPUB 3's typography support is technically there; the quality of Arabic
                  + Turkish bilingual rendering is project-specific work; a template is
                  the engineering deliverable
Priority:         MED     Confidence: MED
Guidance Mode:    compact
  · "depends on R2 (class conventions) for the class-name targets" (bc CSS selectors target the conventions)
  · "depends on R4 (packaging pipeline) for the CSS embedding mechanism" (bc Pandoc accepts --css for EPUB)
Depth-link:       none
```

### R22 — Mac app PipelineConfig.swift html-output integration

```
Direction:        Mac app's PipelineConfig.swift html case integration with intake
Goal:             the Mac app surfaces HTML5 as an output format pointing at canonical
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         the Mac app's PipelineConfig.swift line 42 already has
                  `case md, html, plain, json` — wire the `html` case to mean
                  "render the canonical HTML5 directly" (display in preview pane;
                  export to file); decide whether `json` case keeps meaning Pandoc-AST
                  on-demand (per HTML5-as-canonical-with-JSON-AST-reachable) or is
                  dropped/renamed; expose the Mac app's translation pane to the canonical
                  HTML5 flow
WHY:              the Mac app is the v0.1 UI surface; the canonical commitment must be
                  reachable from the UI; the enum already has `html` so the integration
                  is connection work, not enum addition
Priority:         MED     Confidence: HIGH
Guidance Mode:    compact
  · "json case in the enum bears re-decision" (bc HTML5-as-canonical + JSON-AST-on-demand makes its UI meaning ambiguous)
  · "the Mac app currently has no intake hookup" (bc only Translation/Pipeline config UI exists; pipeline execution is downstream)
Depth-link:       none
```

---

## Excluded

| Candidate | Reason |
|---|---|
| "Build v0.2 of the intake pipeline" | wrong-grain — too coarse; covered by R19 + R20 + R22 as atomic identities |
| "OCR-to-HTML5 reconstruction sub-pipeline" | not a new direction this inquiry opens — preserved unchanged as concept A3 of the original intake-concepts finding's Decision 5 (Pandoc + OCR lever); engaged via R19 |
| "Re-test inherited intake-concepts Decisions 2-5" | done in innovation P8; no onward route to enumerate (Inherited Commitments Re-test was a piece, not a route) |
| "Restate the prior canonical-format inquiry's rejected formats" | done in innovation P7; no onward route to enumerate (rejection rationale was content, not direction) |
| "Re-affirm the user's named formats (EPUB / md / HTML)" | done at the architectural commitment level (HTML5 canonical + md hand-edit + EPUB 3 publishing); no separate route |
| "Decide whether to add an archival temporal layer now" | covered by R16 as INVESTIGATE-FRONTIER; not separately routable |
| "Spec the Mac app's intake-stage pipeline execution" | wrong-grain — that's the Mac app's downstream concern beyond UI integration (R22 covers UI integration); intake pipeline itself is R19 |
| "Re-evaluate whether the architecture should be monolithic vs layered" | done in sensemaking Ambiguity 1; HIGH-confidence resolved; no onward route |

---

## Telemetry

| Field | Value |
|---|---|
| Mode | root / project-space (breadth) |
| Entry point | fresh |
| Identities enumerated | 22 |
| Routes — teleological | 14 |
| Routes — epistemic | 8 |
| High-priority count | 7 |
| Individuations made | 22 (22 splits; 0 merges; one split-and-keep: R23 OCR-sub-pipeline collapsed into R19 — kept whole; one excluded — see Excluded) |
| Uncertain individuations flagged | 1 (R17 in-memory representation choice — borderline PURSUE-SEED vs DIAGNOSE; chose PURSUE-SEED because surfaced-not-taken-up) |
| Stale entries flagged | 0 (fresh entry point) |
| Convergence status | converged (sweep cycle yields no new identities; territory swept at identity resolution) |
| Frontier flags emitted | 0 (no sub-territories warranted "drill here" beyond the route identities themselves) |
| LAYER 1 modes scanned | Over-merge: no (lean-to-split applied; e.g., the 5 critique refinements kept separate). Under-coverage: no (P9 + critique cross-cutting + P10 + onward-concept-routes all covered per user goal). Wrong-grain: no (all routes at identity grain; the engineering-pipeline route R19 acknowledged as broad-scope but identity-bounded). Goal-loss: no (goal-bias preserved through all routes). Type-misassignment: no (verbs match the membership test; teleological/epistemic split honored). Index-drift: NA (fresh). |
| LAYER 2 modes scanned | Selection-creep: no (Priority/Confidence attributive only; no winner pick). Process-coupling: no (no references to /traverse / CONCLUDE control flow within route definitions; routes name target inquiries as Movement but don't define routelisting by a loop position). Description-collapse: no (routes prescribe directions, not describe how the territory works). Manifestation-dump: no (one route per identity; no per-document-page expansion). |
| Self-assessment verdict | **PROCEED** |

---

## Self-Assessment

**PROCEED.** Territory swept at identity resolution; 22 concept-identities individuated from the inquiry's 7 artifacts + user-named scope items. No LAYER 1 flags. No LAYER 2 flags. One uncertain-individuation noted (R17 engagement-type ambiguity; chose PURSUE-SEED with reasoning). Output ready for the routelog / consumer step.
