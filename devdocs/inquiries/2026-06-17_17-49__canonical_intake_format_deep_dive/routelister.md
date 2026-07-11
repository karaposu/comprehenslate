# Route-Map — canonical intake format deep dive

## User Input

Territory: this inquiry's artifacts (`_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md` + `innovation.md` + `critique.md`).

Goal: enumerate the onward route-field this inquiry opens for the canonical intake format. The inquiry committed the three-format layered architecture (Pandoc-AST-JSON canonical / Pandoc's markdown hand-edit / EPUB 3 publishing) refining the prior intake-concepts finding's Decision 1.

Mode: `root / project-space (breadth)`. Entry: `fresh` (no prior `_route.md` for this inquiry).

---

## Map Header

- **Identity count:** 12
- **Teleological:** 5 · **Epistemic:** 7
- **High-priority count:** 4
- **Convergence:** PROCEED (territory swept at identity resolution; no LAYER 1 failure-mode flags)

---

## Route Index (at-a-glance)

| # | Direction | grain | kind | engagement-type | Priority |
|---|---|---|---|---|---|
| R1 | JSON-AST canonical schema design | project-space | teleological | DEVELOP | **HIGH** |
| R2 | Round-trip-stable Pandoc-md subset definition | project-space | teleological | DEVELOP | **HIGH** |
| R3 | EPUB 3 generation pipeline design | project-space | teleological | DEVELOP | MED |
| R4 | End-to-end AST → EPUB prototype on Risale-i Nur sample | project-space | teleological | PURSUE-SEED | **HIGH** |
| R5 | Apply the 4 REFINE-direction adjustments at finding.md construction | project-space | teleological | REFINE | **HIGH** |
| R6 | Re-spec the seven policy-perception detectors for AST node types | project-space | epistemic | REFINE | MED |
| R7 | Pandoc cross-version stability validation | project-space | epistemic | TEST | MED |
| R8 | Cross-corpus format-architecture validation (beyond Risale-i Nur) | project-space | epistemic | TEST | LOW |
| R9 | TEI as future archival output | project-space | epistemic | INVESTIGATE-FRONTIER | LOW |
| R10 | Custom format revisit (only if AST + md + EPUB prove insufficient) | project-space | epistemic | INVESTIGATE-FRONTIER | LOW |
| R11 | Archival / historical preservation as a fifth temporal layer | project-space | epistemic | REFRAME | LOW |
| R12 | Pandoc version pinning operational policy | project-space | epistemic | REFINE | LOW |

---

## Per-route records

### R1 — JSON-AST canonical schema design

Direction:        the JSON-AST canonical schema (Pandoc's native AST shape + optional project pydantic layer for project-specific invariants)
Goal:             a designed schema that defines the contract every intake stage populates and every translate stage reads
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         decide between Pandoc-AST-direct vs Pandoc-AST + project pydantic overlay; specify the schema; document the validator
WHY:              the canonical intake/translate format (F1 in this finding) is load-bearing; without the schema, no intake stage can ship
Priority:         **HIGH**    Confidence: MED (the Pandoc-AST shape is documented; the choice between direct vs overlay is the work)
Guidance Mode:    full
  · "start from Pandoc's documented AST types (pandoc-types Haskell library; mirrored in panflute Python package)"  (bc the AST shape is canonical and documented)
  · "decide pydantic-overlay-or-not based on what project invariants need enforcement (e.g., 'every chapter has a title'; 'every footnote ref resolves'; 'apparatus collection ids are unique')"  (bc the overlay is conditional on invariant requirements)
  · "specify the cross-version migration story — Pandoc's JSON header carries api-version; pin a Pandoc version and document the migration path for version bumps"  (bc the critique flagged cross-version stability)
  Meaning-gaps:
    - Direct-AST vs pydantic-overlay choice — high — the foundational schema-strategy decision; affects all downstream code
    - Cross-version migration mechanism — mid — needed before shipping; not blocking for design
    - Validator for cross-reference integrity (every MarkerRun.ref-id resolves to apparatus entry) — mid — load-bearing for IntakeDoc correctness
Depth-link:       none (not yet drilled)

---

### R2 — Round-trip-stable Pandoc-md subset definition

Direction:        the specification of which Pandoc-md features round-trip losslessly with the JSON canonical
Goal:             a documented subset so the hand-edit workflow's contract is explicit
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         enumerate Pandoc-md features systematically; per feature, test md → json → md byte-stability; document the subset that's stable + the exceptions
WHY:              F2 (hand-edit format) depends on this contract; without it, users hit silent drift when their markdown round-trips
Priority:         **HIGH**    Confidence: MED (the subset is testable but the enumeration is non-trivial)
Guidance Mode:    full
  · "start with the canonical extension set from the prior finding (footnotes / pipe_tables / definition_lists / citations / yaml_metadata_block / raw_attribute / bracketed_spans) and verify each survives md → json → md round-trip"  (bc the working assumption is this set is stable)
  · "concrete test method: a Python script that emits sample md per feature, runs pandoc twice, byte-compares"  (bc this is the only way to verify; reasoning alone insufficient)
  · "iterative refinement — expect to surface edge cases during R4 prototyping"  (bc edge cases live in the corpus, not the abstract)
  Meaning-gaps:
    - Per-feature round-trip-test methodology — high — without a test method, the subset can't be defined
    - Edge cases in escape characters and inline-attribute syntax — mid — likely surface during R4
    - Documentation form for the subset (a markdown spec? a test suite?) — low — operational detail
Depth-link:       none

---

### R3 — EPUB 3 generation pipeline design

Direction:        the per-translation EPUB 3 generation pipeline (Pandoc invocation flags + metadata extraction + per-chapter file structure + CSS + cover-image handling)
Goal:             a runnable EPUB 3 generation pipeline that takes a translated JSON canonical and produces a publication-ready .epub file
grain:            project-space
kind:             teleological
engagement-type:  DEVELOP
Movement:         specify the Pandoc invocation flags per use case; design the metadata extraction; design the CSS template for typography (especially Arabic + RTL); handle embedded fonts; cover-image workflow
WHY:              F3 (publishing format) needs an implementation; without it, the publishing-layer commitment is theoretical
Priority:         MED    Confidence: HIGH (Pandoc's epub3 writer is mature; the work is configuration + CSS + metadata orchestration)
Guidance Mode:    compact
  · "Pandoc invocation: `pandoc -f json -t epub3 --metadata key=value --css=template.css --epub-cover-image=cover.png -o out.epub canonical.json`"  (bc the basic command is documented)
  · "CSS template for typography: Arabic-aware font fallback chain; RTL block handling; per-policy class styling (.marginalia, .formulaic-opening, .embedded-poetry)"  (bc the calibration corpus has specific rendering needs)
  · "downstream-couples to R4 (the prototype validates the EPUB output)"  (bc empirical validation matters)
  Meaning-gaps:
    - CSS template for Arabic typography — mid — needs an Arabic-font-aware design (Amiri / Noto Sans Arabic / Scheherazade)
    - Per-policy class styling (.marginalia / .embedded-poetry / .formulaic-opening) — mid — needed for visual differentiation
    - Embedded font handling (whether to embed Arabic font in EPUB or rely on reader fonts) — low — operational
Depth-link:       none

---

### R4 — End-to-end AST → EPUB prototype on Risale-i Nur sample

Direction:        the integration test seed: take one Risale-i Nur volume sample; run intake; populate IntakeDoc as JSON-AST canonical; generate EPUB 3 via the R3 pipeline; verify Arabic + marginalia + couplets + Bismillah render correctly in Apple Books / Calibre / Google Play Books
Goal:             empirical validation that the three-format architecture works end-to-end on the calibration corpus
grain:            project-space
kind:             teleological
engagement-type:  PURSUE-SEED
Movement:         build a runnable script wiring intake (R1 schema in draft) + EPUB pipeline (R3 in draft) + a representative Risale-i Nur PDF (with hashiye, Mevlana couplets, Bismillah); report quality + per-stage timings + visual EPUB output
WHY:              the architectural verdict needs empirical confirmation; the calibration corpus IS the test substrate; integration reveals what unit tests cannot
Priority:         **HIGH** (the prototype validates the whole architecture before scaling)    Confidence: MED
Guidance Mode:    full
  · "pick ONE representative section (e.g., one Sözler section with hashiye + a Mevlana couplet + a Bismillah opening)"  (bc maximizing the calibration signal per single test)
  · "iterate R1 + R2 + R3 in lockstep; the prototype reveals what the schemas need"  (bc empirical-first surfaces design gaps)
  · "test the EPUB output in at least 3 readers (Apple Books, Calibre, Google Play Books) — Arabic + RTL rendering verifies in different rendering engines"  (bc Arabic typography is renderer-dependent)
  · "this prototype IS the calibration anchor for future cross-corpus validation (R8)"  (bc the prototype persists as the baseline)
Depth-link:       none

---

### R5 — Apply the 4 REFINE-direction adjustments at finding.md construction

Direction:        the surgical content edits to apply when CONCLUDE produces finding.md (anti-hallucination + syntax-specificity)
Goal:             a finding.md that incorporates the critique's REFINE-direction adjustments verbatim
grain:            project-space
kind:             teleological
engagement-type:  REFINE
Movement:         apply each of the 4 adjustments from critique.md's Summary section
WHY:              critique surfaced anti-hallucination + concrete-syntax issues that need to be in the finding (not just in the inquiry's working notes)
Priority:         **HIGH** (apply during CONCLUDE; do NOT publish finding.md without these)    Confidence: HIGH
Guidance Mode:    full
  · "(1) P3: replace `pandoc-types-python` with `panflute` (the canonical Python AST library); add a cross-version stability qualifier on the round-trip claim citing Pandoc's `api-version` field"  (bc anti-hallucination)
  · "(2) P5: soften 'August 1, 2022' for MOBI deprecation to 'in 2022' (avoid precise-date hallucination)"  (bc date-precision risk)
  · "(3) P7: add concrete Pandoc-md syntax patterns for each policy mapping — e.g., for hashiye: 'fenced div ::: {.marginalia ref-id=h1} hashiye-body ::: (block-level) OR inline span [short text]{.marginalia ref-id=h1}'"  (bc syntax-specificity prevents downstream confusion)
  · "(4) P8: adjust the Decision 4 row from 'UNCHANGED' to 'UNCHANGED in structural intent; per-detector specs need adjustment to reference AST node types (e.g., Note, Span, Div with class) rather than markdown surface signals. The work is design-refinement, not redesign.'"  (bc detector specs need refinement)
Depth-link:       none

---

### R6 — Re-spec the seven policy-perception detectors for AST node types

Direction:        the design refinement on each of the seven policy-perception detectors (B4-B10 in the prior intake-concepts finding) to operate on AST node types rather than markdown surface signals
Goal:             refined detector specs that match the JSON-AST canonical
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         per detector, update the "perception signals" section to reference Pandoc AST node types + attributes (Note / Span with lang= / Div with class= / LineBlock with class= / Para with class=); preserve the structural intent of each detector
WHY:              the prior finding's detector specs referenced markdown surface signals; the new canonical is JSON-AST; the detector signals refresh
Priority:         MED    Confidence: HIGH (the structural intent of each detector is unchanged; only the source-signal reference shifts)
Guidance Mode:    compact
  · "each detector's perception-signal section becomes 'AST-node + attribute' based"  (bc the canonical changed)
  · "this is design-refinement, not redesign — the seven detectors' structural roles are preserved"  (bc Decision 4 from prior is preserved)
  · "spawn alongside R1 schema design — the detector signals depend on the schema's apparatus-collection shape"  (bc tight coupling)
Depth-link:       none

---

### R7 — Pandoc cross-version stability validation

Direction:        empirical TEST of whether the JSON-AST canonical's round-trip is stable across Pandoc versions
Goal:             evidence-grounded confirmation (or named-mitigation) of the cross-version stability claim
grain:            project-space
kind:             epistemic
engagement-type:  TEST
Movement:         take a representative IntakeDoc; round-trip it through Pandoc 3.x and Pandoc 2.x; document drift; specify the api-version pinning + migration mechanism
WHY:              the critique flagged this as a REFINE-direction; the architectural commitment depends on cross-version stability being manageable
Priority:         MED (resolvable inside R1 schema design)    Confidence: MED
Guidance Mode:    compact
  · "Pandoc's JSON header carries an api-version field; same api-version = same AST shape"  (bc the mechanism exists)
  · "the test is: same source through two different Pandoc versions → byte-compare the JSON"  (bc empirical method)
  · "resolution likely: pin Pandoc 3.x as the project's canonical version; document the migration path"  (bc operational pragmatism)
Depth-link:       none

---

### R8 — Cross-corpus format-architecture validation (beyond Risale-i Nur)

Direction:        empirical TEST of whether the three-format layered architecture generalizes to corpora other than Risale-i Nur
Goal:             evidence the architecture isn't over-fit to one calibration corpus
grain:            project-space
kind:             epistemic
engagement-type:  TEST
Movement:         (after R4 + R1 + R3 are stable) test intake on samples from other corpora (Talmud with apparatus criticus; Vedic texts with embedded poetry; Christian patristic editions; modern academic books); verify the JSON-AST canonical + EPUB output handle each
WHY:              SKILL.md framing: Risale-i Nur is calibration corpus, not product scope; this inquiry's architectural commitment needs cross-corpus validation
Priority:         LOW (fires after R4 stabilizes)    Confidence: LOW
Guidance Mode:    compact
  · "do NOT fire until R4 produces stable Risale-i Nur results"  (bc single-corpus baseline must hold first)
  · "couples to R10 if a corpus surfaces requirements AST + md + EPUB cannot serve"  (bc condition for custom-format revisit)
Depth-link:       none

---

### R9 — TEI as future archival output

Direction:        the consideration of TEI Simple as an archival output format generated from the JSON-AST canonical
Goal:             a future decision on whether to add TEI as a separate archival/scholarly output (alongside EPUB 3 publishing)
grain:            project-space
kind:             epistemic
engagement-type:  INVESTIGATE-FRONTIER
Movement:         (when scholarly archival need emerges) prototype `pandoc -f json -t tei` on a Risale-i Nur sample; evaluate TEI Simple coverage of the policy targets; design the TEI generation pipeline if warranted
WHY:              TEI is the scholarly-text-encoding standard; archival use cases may emerge; Pandoc CAN write TEI Simple (output-only)
Priority:         LOW (frontier; conditional on scholarly archival need)    Confidence: LOW
Guidance Mode:    compact
  · "do NOT fire until either (a) scholarly archival use case emerges OR (b) cross-corpus validation R8 surfaces TEI as a requirement"  (bc avoid premature investment)
  · "the path is `pandoc -f json -t tei`; this is OUTPUT-only via Pandoc"  (bc Pandoc-read TEI absence)
Depth-link:       none

---

### R10 — Custom format revisit (conditional)

Direction:        the conditional revisit of the custom-format option if the three-format AST + md + EPUB architecture proves insufficient
Goal:             a documented condition + revisit path so the rejection of custom-format isn't permanent
grain:            project-space
kind:             epistemic
engagement-type:  INVESTIGATE-FRONTIER
Movement:         (only if a SPECIFIC requirement surfaces that AST + md + EPUB cannot serve) revisit the custom-format design path with the failed requirement as the seed
WHY:              the rejection of custom-format in this finding is conditional; the revisit-trigger should be explicit
Priority:         LOW (frontier; gated by specific requirement emergence)    Confidence: LOW
Guidance Mode:    compact
  · "specific revisit triggers: (a) corpus surfaces primitives Pandoc-AST can't represent; (b) Pandoc deprecation or migration cost becomes prohibitive; (c) project needs a format Pandoc cannot generate"  (bc named triggers prevent unbounded revisit)
Depth-link:       none

---

### R11 — Archival / historical preservation as a fifth temporal layer

Direction:        the consideration of whether the three-format architecture should add a fifth temporal layer for archival / long-term preservation
Goal:             a future decision on whether to add archival as its own layer with its own format
grain:            project-space
kind:             epistemic
engagement-type:  REFRAME
Movement:         (when archival need emerges) reframe the three-format architecture as four-format (add archival layer; format is TEI or JATS or zip-of-AST-plus-source); evaluate the new layer's optima
WHY:              the three-format architecture covers intake/translate + hand-edit + publishing; archival is a possible fifth layer that may emerge with project maturity
Priority:         LOW (frontier)    Confidence: LOW
Guidance Mode:    compact
  · "fires when (a) cross-corpus R8 surfaces archival need OR (b) the project commits to long-term preservation of source + translated corpora"  (bc named conditions)
Depth-link:       none

---

### R12 — Pandoc version pinning operational policy

Direction:        the operational policy for which Pandoc version the project commits to and how version migrations are handled
Goal:             a documented version-pinning policy + migration mechanism
grain:            project-space
kind:             epistemic
engagement-type:  REFINE
Movement:         pick a Pandoc version (likely the current stable, e.g., 3.5.x); document the policy in the project's engineering README; specify the migration test (re-run R7 on each version bump)
WHY:              the JSON-AST canonical depends on Pandoc version stability; operational policy must be explicit
Priority:         LOW (resolvable inside the project's engineering setup; small task)    Confidence: HIGH
Guidance Mode:    compact
  · "resolved by picking a Pandoc version + documenting it; no design work needed"  (bc operational, not architectural)
Depth-link:       none

---

## Excluded section

Notable candidate-concepts considered and rejected (with reasons):

- **Re-litigating Decision 1 again (revisit the architectural verdict)** — out of scope; the inquiry committed SUBSTITUTE with a clean verdict; further revisit requires NEW evidence (e.g., a specific Pandoc-AST limitation surfacing in R4 prototype).
- **Re-litigating Decisions 2-5 from the prior intake-concepts finding** — out of scope per `refines:` relationship; the other decisions are inherited and unchanged by this inquiry.
- **OCR sub-pipeline design** — out of scope of this format-choice inquiry; covered by the prior intake-concepts finding's frontier (its R3 / R9-equivalent).
- **Mac app intake UI re-entry** — out of scope; covered by prior finding's F4 frontier; this inquiry didn't shift it.
- **The 7 policy-perception detector designs as standalone work** — partially in scope as R6 (spec refinement for AST) but the actual detector design work is the prior finding's onward route field.
- **PDF text extraction issues** — explicitly excluded by the user ("pdftext extraction is another issue").
- **Format detection (libmagic-style file-type sniffing)** — covered by prior finding's A5; not new from this inquiry.
- **Translation-stage algorithm choices** — explicitly excluded per inherited MQ4.

---

## Telemetry

- **Mode:** root / project-space (breadth) · **Entry point:** fresh
- **Identities enumerated:** 12 (R1-R12); index reflects 12 load-bearing identities
- **Routes at each kind:** teleological = 5 (R1-R5); epistemic = 7 (R6-R12)
- **High-priority count:** 4 (R1 JSON-AST schema · R2 round-trip-stable subset · R4 prototype · R5 REFINE adjustments)
- **Individuations made:** 12 fresh identities; lean-to-split applied at R3+R4 (kept separate — R3 is design inquiry; R4 is integration validation) and R5+R6 (kept separate — R5 is finding.md construction; R6 is detector-spec refinement)
- **Uncertain individuations:** none
- **Stale entries flagged:** none (fresh index)
- **Convergence:** territory swept at identity resolution; no new identities surfaced in re-sweep

### LAYER 1 failure-mode check
- Over-merge: not observed (lean-to-split applied at R3/R4 + R5/R6)
- Under-coverage: not observed (every MUST + COULD + DEFERRED + REFINE-direction adjustment + frontier item has a route)
- Wrong-grain: not observed (project-space identities, not manifestations)
- Goal-loss: not observed
- Type-misassignment: re-checked — REFINE/TEST/INVESTIGATE-FRONTIER/REFRAME are epistemic; DEVELOP/PURSUE-SEED are teleological
- Index-drift: n/a (fresh)

### LAYER 2 failure-mode check
- Selection-creep: not observed (Priority is attributive)
- Process-coupling: not observed
- Description-collapse: not observed
- Manifestation-dump: not observed (12 identities, not manifestations)

---

## Self-Assessment Verdict

**PROCEED** — territory swept at identity resolution; no LAYER 1 or LAYER 2 flags. The onward route-field is enumerated; the inquiry's downstream consumers can pick any subset to engage.
