# Routelister — Edge-Cases into Config Schema

## User Input

```text
territory: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/
  (this inquiry's artifacts — _branch.md + articulate_simple.md + surfacing.md + sensemaking.md
   + decomposition.md + innovation.md + critique.md)
goal: how should the 14 edge-case candidates from translation_config_edge_cases.md change the
  current 8-field TranslationConfig (per _branch.md)
```

---

## Map Header

- **Run mode:** root / project-space (breadth) | **Entry point:** fresh
- **Identities enumerated:** 22
- **Routes:** 11 teleological + 11 epistemic
- **High-priority count:** 6
- **Frontier flags:** 8 (DEFER revivals + Assembly-3 template suggestion)

---

## Route Index

| # | Direction | grain | kind | engagement | Priority |
|---|---|---|---|---|---|
| R1 | Phase 1 ratify-pre-routing documentation | project-space | epistemic | CONSOLIDATE | HIGH |
| R2 | SourceDescriptor field build-out (4 fields + EmbeddedLanguagePolicy helper) | project-space | teleological | DEVELOP | HIGH |
| R3 | Nursi-specific SourceDescriptor instance declaration | project-space | teleological | DEVELOP | HIGH |
| R4 | A3 non-modification commitment codification | project-space | epistemic | CONSOLIDATE | MED |
| R5 | UseContext non-commitment + bundling revival rule | project-space | epistemic | CONSOLIDATE | MED |
| R6 | P4 REFINE: trigger sub-conditions for #9/#10/#12 (downstream-consumer prerequisite) | project-space | epistemic | REFINE | HIGH |
| R7 | P4 REFINE: initiation paths for revival inquiries | project-space | epistemic | REFINE | HIGH |
| R8 | External-anchor refinement (verbatim quotes for chunking §7 + A3 prose + B5 framing) | project-space | epistemic | REFINE | HIGH |
| R9 | P6 caveat: additions × additions interactions documentation (#2×#13; #8×#2; #3×#13) | project-space | epistemic | REFINE | MED |
| R10 | source_temporal_register × no-smoothing CAUTION docs note | project-space | epistemic | REFINE | MED |
| R11 | source_temporal_register × register-alternation POSITIVE COMPOSITION docs note | project-space | epistemic | REFINE | MED |
| R12 | #4 voice_disambiguation DEFER revival when lahika case emerges | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R13 | #5 relay_translation DEFER revival when relay use-case emerges | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R14 | #9 consumption_mode DEFER revival when downstream renderer distinguishes | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R15 | #10 reading_session_pattern DEFER revival | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R16 | #11 prior_translation_relationship DEFER revival when third-iteration use-case | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R17 | #12 output_finality DEFER revival when pipeline distinguishes | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R18 | #14 script_direction_handling DEFER revival when apparatus-edition RTL | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R19 | EditionDescriptor promotion (revival of light str source_edition field) | project-space | teleological | DEVELOP | LOW |
| R20 | A3 re-examination (revival if conflation produces ambiguous assignments) | project-space | epistemic | DIAGNOSE | LOW |
| R21 | Assembly-3 forward-looking: 2D-decision template as suggestion for future bulk-edge-case inquiries | project-space | epistemic | INVESTIGATE-FRONTIER | LOW |
| R22 | SourceDescriptor schema prerequisite (chunking finding's MUST item — gates Phase 2) | project-space | teleological | DEVELOP | HIGH |

---

## Per-Route Records

### R1 — Phase 1 ratify-pre-routing documentation

- **Direction:** documenting that edge-cases #1, #6, #7 are inherited-ratified from chunking finding (no new schema work for these)
- **Goal:** aggregate inherited routings into a single doc the future implementer can reference
- **grain:** project-space | **kind:** epistemic | **engagement-type:** CONSOLIDATE
- **Movement:** record in a Phase-1 doc that #1 is carried by `ChunkingUnit.is_atomic`; #6 by `ChunkingUnit.attached_to`; #7 by `chunking_strategy: passage-typology-aware` literal
- **WHY:** without explicit ratification, future contributors may re-route these cases incorrectly. Per P2's RE-TESTED-OK status
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** short doc section — 3 paragraphs, one per inheritance

### R2 — SourceDescriptor field build-out

- **Direction:** the 4 SourceDescriptor additions (source_language_fluency / source_edition / source_temporal_register / embedded_languages) + EmbeddedLanguagePolicy helper class
- **Goal:** convert P3's code sketches into actual implementation
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** implement per P3's pydantic code; validate field types; add docstrings; integrate with chunking finding's SourceDescriptor stub
- **WHY:** Phase 2 implementation; P3 specifies the schema; turns SourceDescriptor from skeleton (just `source_chunking_units`) into a substantively shaped descriptor
- **Priority:** HIGH | **Confidence:** MED
- **Guidance:** depends on R22 (SourceDescriptor schema must exist first); implement EmbeddedLanguagePolicy first (carries #1 + #8), then top-level fields (#2 / #3 / #13), then declare default values
- **Depth-link:** none (not yet drilled)

### R3 — Nursi-specific SourceDescriptor instance

- **Direction:** declare the actual Nursi corpus's SourceDescriptor with concrete values
- **Goal:** prove Phase 2 works with a real instance + unblock 4_mesele translation
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** declare:
  - `source_chunking_units`: Mesele (level 0) / paragraph (level 1) / ayah (atomic)
  - `source_language_fluency`: {"tr": "native", "ar": "reading-only", "fa": "basic"}
  - `source_edition`: "Risale-i Nur Külliyatı, Yeni Asya 2003 printing"
  - `source_temporal_register`: "hybrid-by-register-domain"
  - `embedded_languages`: list with Arabic entry (quranic_citation_policy="arabic-plus-translation") + Persian entry
- **WHY:** demonstrates the Phase 2 work end-to-end; gives 4_mesele a concrete declaration to work against
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** bundle with R2 (the field implementations); Nursi-specific values get the framework's first concrete instance

### R4 — A3 non-modification commitment codification

- **Direction:** explicit documented commitment that A3 stays as-is (do not split)
- **Goal:** prevent silent drift in future contributors who might attempt A3 split
- **grain:** project-space | **kind:** epistemic | **engagement-type:** CONSOLIDATE
- **Movement:** record P5's N1 commitment in a project doc (likely as a comment in `translation_config.py` near A3 declaration); cite #2's add-beside-A3 resolution as the captured alternative
- **WHY:** the chunking finding established that explicit non-actions prevent drift
- **Priority:** MED | **Confidence:** HIGH
- **Guidance:** short comment block in code + revival trigger documented (revisit if A3 conflation produces ambiguous assignments)

### R5 — UseContext non-commitment + bundling revival rule

- **Direction:** explicit documented commitment that UseContext is NOT a schema; with revival trigger (≥2 of {#9, #10, #12} fire individually)
- **Goal:** prevent silent introduction of UseContext as a schema
- **grain:** project-space | **kind:** epistemic | **engagement-type:** CONSOLIDATE
- **Movement:** record P5's N2 commitment in this inquiry's finding + future code comment when downstream consumers emerge
- **WHY:** prevents 3-schemas-in-2-inquiries violation; preserves pacing
- **Priority:** MED | **Confidence:** HIGH
- **Guidance:** short doc section; revival rule is condition-bound

### R6 — P4 REFINE: trigger sub-conditions for #9/#10/#12

- **Direction:** refine the revival triggers for #9, #10, #12 to make downstream-consumer-existence prerequisite explicit
- **Goal:** address Critique's REFINE on P4 — the triggers currently presume downstream consumers exist; this presumption must be explicit
- **grain:** project-space | **kind:** epistemic | **engagement-type:** REFINE
- **Movement:** rewrite each trigger as: "(a) downstream consumer exists in pipeline AND (b) consumer distinguishes between modes in observable behavior"
- **WHY:** Critique P4 REFINE flagged this as load-bearing specification gap
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** update P4's trigger wording in the finding text; bundle with R7

### R7 — P4 REFINE: initiation paths for revival inquiries

- **Direction:** document who/what initiates a follow-up inquiry when a DEFER trigger fires
- **Goal:** address Critique's REFINE — when a trigger fires, the initiation path must be clear
- **grain:** project-space | **kind:** epistemic | **engagement-type:** REFINE
- **Movement:** specify per DEFER entry: user observation during translation work / AI flag at next translation cycle / explicit project-state review
- **WHY:** Critique P4 REFINE second target; without this, triggers fire but no action mechanism
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** bundle with R6 in finding-polish pass

### R8 — External-anchor refinement (verbatim quotes)

- **Direction:** quote canonical source text verbatim at load-bearing claim sites
- **Goal:** lift Critique's PARTIAL External-Grounding-Absence flag to VALIDATED
- **grain:** project-space | **kind:** epistemic | **engagement-type:** REFINE
- **Movement:** quote chunking finding §7 for #1/#6/#7 inheritance rows (P1 caveat); quote `config_base_source.md` A3 prose for "settled-prose" claim (P5 caveat); strengthen P2 B5 by explicitly stating what test was applied (Critique caveat on B5)
- **WHY:** Critique flagged this as load-bearing for synthesis-rigor; mechanism-independence quarantine lifts when external evidence is verbatim-cited
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** finding-polish pass; bundle all 3 verbatim quotes together

### R9 — P6 caveat: additions × additions interactions

- **Direction:** brief note acknowledging additions-cross-additions interactions
- **Goal:** address Critique's caveat on P6 — matrix is additions × existing axes only; intra-additions interactions unexplored
- **grain:** project-space | **kind:** epistemic | **engagement-type:** REFINE
- **Movement:** add to P6 text:
  - **#2 × #13:** low-fluency reader + archaic register → compounded difficulty (no conflict; signals A1-cascade attention)
  - **#8 × #2:** Quranic citation policy depends on Arabic fluency declared in source_language_fluency
  - **#3 × #13:** edition may determine which register-period applies
- **WHY:** Critique P6 caveat; brief note suffices (no full matrix needed)
- **Priority:** MED | **Confidence:** HIGH
- **Guidance:** 3-bullet paragraph in finding text

### R10 — source_temporal_register × no-smoothing CAUTION docs note

- **Direction:** documentation that `modernize-fully` option carries no-smoothing-policy risk
- **Goal:** prevent future contributors from defaulting to modernize-fully without awareness
- **grain:** project-space | **kind:** epistemic | **engagement-type:** REFINE
- **Movement:** add to source_temporal_register docstring (or finding text): "`modernize-fully` may smooth archaic forms in violation of no-smoothing policy; use with care; not the default precisely because of this risk"
- **WHY:** P6 explicitly flagged this CAUTION; need to surface to future contributors
- **Priority:** MED | **Confidence:** HIGH
- **Guidance:** code docstring update in R2 implementation

### R11 — source_temporal_register × register-alternation POSITIVE COMPOSITION docs note

- **Direction:** documentation that `hybrid-by-register-domain` (default) composes positively with register-alternation preservation policy
- **Goal:** make the positive composition explicit for future contributors
- **grain:** project-space | **kind:** epistemic | **engagement-type:** REFINE
- **Movement:** add to source_temporal_register docstring: "default `hybrid-by-register-domain` composes naturally with Layer-2 register-alternation preservation policy — preserves alternation between archaic theological vocab and modern narrative"
- **WHY:** P6 flagged this; surfacing the positive composition guides users toward the right default
- **Priority:** MED | **Confidence:** HIGH
- **Guidance:** code docstring update in R2 implementation; bundle with R10

### R12 — #4 voice_disambiguation DEFER revival

- **Direction:** activate #4 when lahika / extended-citation case emerges (translation case where voice rendering distinct from hashiye attachment is needed)
- **Goal:** preserve the option for #4 without committing now
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** when condition fires, open follow-up inquiry to decide schema home + Literal[] enum
- **WHY:** P4's revival trigger
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** defer until use-case forces; pre-routing via #6's attached_to covers Nursi+hashiye currently

### R13 — #5 relay_translation DEFER revival

- **Direction:** activate #5 when relay (source→intermediate→target) chain becomes needed
- **Goal:** preserve option
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** when second target language added without source-fluent translator, open follow-up inquiry
- **WHY:** P4's revival trigger
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** defer; not in current scope

### R14 — #9 consumption_mode DEFER revival

- **Direction:** activate #9 when downstream consumer distinguishes between modes
- **Goal:** preserve option
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** when observable, open follow-up inquiry; consider UseContext schema commitment if ≥2 of {#9, #10, #12} fire together
- **WHY:** P4 + P5 bundling rule
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** defer; chain with R15 + R17 for UseContext bundling

### R15 — #10 reading_session_pattern DEFER revival

- **Direction:** activate #10 when downstream consumer distinguishes between session patterns
- **Goal:** preserve option
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** when observable, open follow-up inquiry
- **WHY:** P4's revival trigger
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** chains with R14, R17 for UseContext bundling

### R16 — #11 prior_translation_relationship DEFER revival

- **Direction:** activate #11 when third translation iteration positions vs prior translators (Vahide / Akarsu / Tahşiye)
- **Goal:** preserve option
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** when condition fires (user feedback like "honor Vahide's iman rendering"), open follow-up inquiry
- **WHY:** P4's revival trigger
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** defer; revisit when comparison work in flight

### R17 — #12 output_finality DEFER revival

- **Direction:** activate #12 when downstream pipeline distinguishes finality levels
- **Goal:** preserve option
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** when observable, open follow-up inquiry; chain with R14/R15 for UseContext bundling
- **WHY:** P4's revival trigger
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** chains with R14, R15

### R18 — #14 script_direction_handling DEFER revival

- **Direction:** activate #14 when output rendering reaches apparatus-edition stage with bidirectional RTL Arabic display
- **Goal:** preserve option
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** when condition fires, open follow-up inquiry; likely lives on PipelineConfig (rendering concern)
- **WHY:** P4's revival trigger
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** defer until apparatus-edition stage

### R19 — EditionDescriptor promotion

- **Direction:** promote `source_edition: str` to a structured EditionDescriptor when variant-tracking matters
- **Goal:** preserve future enhancement path for #3
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP (when trigger fires)
- **Movement:** when multi-edition corpus added OR Nursi variants explicitly compared, open follow-up inquiry to design EditionDescriptor
- **WHY:** P3 explicitly deferred EditionDescriptor; revival trigger documented
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** defer; the str field is sufficient for Phase 2

### R20 — A3 re-examination

- **Direction:** revisit A3 if conflation produces ambiguous assignments
- **Goal:** preserve revisit path while honoring N1 non-modification now
- **grain:** project-space | **kind:** epistemic | **engagement-type:** DIAGNOSE
- **Movement:** when real translation cases produce ambiguous A3 assignments (e.g., reader is source-native culturally but `none` in fluency), open follow-up to diagnose the conflation
- **WHY:** P5 N1's revival trigger
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** defer; #2's add-beside-A3 handles the fluency dimension without forcing A3 split

### R21 — Assembly-3: 2D-decision template as suggestion

- **Direction:** apply the 2D-decision pattern (outcome × schema-home) + revival-trigger + cross-axis-check + Inherited-Re-test to future bulk-edge-case inquiries
- **Goal:** preserve the template for future re-use
- **grain:** project-space | **kind:** epistemic | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** when a future inquiry consumes multiple proposed candidates as input (similar synthesis trigger), apply this template
- **WHY:** Assembly-3 emergent (Critique: forward-looking suggestion, not strong claim)
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** suggestion-only; not committed; revival when similar inquiry pattern emerges

### R22 — SourceDescriptor schema prerequisite (chunking finding's MUST)

- **Direction:** build the SourceDescriptor schema per chunking finding's MUST item
- **Goal:** unblock this inquiry's Phase 2 (R2 + R3 depend on this)
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** implement SourceDescriptor BaseModel with `source_chunking_units` (from chunking finding) + the 4 fields (from this inquiry); declare in `translation_config.py` or a new `source_descriptor.py` module
- **WHY:** chunking finding committed SourceDescriptor as paper schema; this inquiry's Phase 2 cannot complete without it
- **Priority:** HIGH | **Confidence:** MED
- **Guidance:** this is the cross-inquiry dependency; bundle the chunking finding's ChunkingUnit work with this inquiry's 4 fields into a single implementation pass

---

## Excluded

Candidate-concepts considered and rejected — not engaged as routes because engaging them advances/sharpens nothing toward the inquiry's goal:

| Candidate | Why excluded |
|---|---|
| The 8 existing TranslationConfig axes | Substrate; not directions to engage as routes — they're stable inputs |
| The 14 edge-cases as "candidates to evaluate" | The inquiry SETTLED them — they're no longer candidates; their settled-form lives in P1's per-field decision table |
| The MVLwr pipeline structure | Process artifact, not a configuration direction |
| The 7 decomposition pieces (P1-P7) | Process artifacts — the inquiry executed them; their outputs are the routes |
| KILLed Innovation Inversions (7) | Rejected on structural grounds; engaging would re-open settled debates |
| The user's anti-bloat preference | Constraint informing every route, not a route itself |
| The chunking finding's commitments (already-routed cases) as separate routes | These ARE the inheritance; they're carried in R1 (Phase 1 ratify); separate routes would dump manifestations |
| Group α/β/γ from edge-cases innovation as separate routes | Re-tested in P2; result absorbed into R1 (ratify) + R2 (build); separate routes would be redundant |

---

## Telemetry

- **Mode:** root / project-space (breadth) | **Entry point:** fresh
- **Identities enumerated:** 22
- **Routes by kind:** teleological 11 + epistemic 11 = 22
- **Routes by engagement-type:**
  - DEEPEN: 0
  - DEVELOP: 4 (R2, R3, R19, R22)
  - PURSUE-SEED: 0
  - INVESTIGATE-FRONTIER: 8 (R12-R18, R21)
  - REFINE: 6 (R6, R7, R8, R9, R10, R11)
  - REFRAME: 0
  - DIAGNOSE: 1 (R20)
  - TEST: 0
  - CONSOLIDATE: 3 (R1, R4, R5)
- **High-priority count:** 6 (R1, R2, R3, R6, R7, R8, R22) — actually 7
- **Frontier flags:** 8 (R12-R18 individual DEFER revivals + R21 template suggestion)
- **Individuations made:** 22 (goal-relative; lean-to-split applied — e.g., R10/R11 kept separate as distinct docs notes; R12-R18 kept separate as distinct revival paths)
- **Uncertain individuations:** 0 flagged
- **Stale entries:** N/A (fresh entry point)
- **Convergence:** YES — additional sweep yields no new identities
- **LAYER 1 failure modes checked:** Over-merge / Under-coverage / Wrong-grain / Goal-loss / Type-misassignment / Index-drift — NONE fired
- **LAYER 2 failure modes checked:** Selection-creep / Process-coupling / Description-collapse / Manifestation-dump — NONE fired (no winner picked; no control-flow; routes are prescriptive; one route per identity)

### Self-Assessment Verdict

**PROCEED**

22 routes across the inquiry's onward field; 7 HIGH-priority routes carry the implementation + REFINE + verbatim-quote work; 8 frontier flags for DEFER revivals + template suggestion. Critical observation: **R22 (SourceDescriptor schema prerequisite) is a cross-inquiry dependency** — this inquiry's Phase 2 work (R2 + R3) cannot complete without R22, which is owned by the chunking finding's MUST item. CONCLUDE should surface this dependency prominently in Next Actions.
