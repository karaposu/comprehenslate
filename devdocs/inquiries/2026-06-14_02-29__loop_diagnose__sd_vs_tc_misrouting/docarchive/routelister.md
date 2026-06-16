# Routelister — Loop Diagnose: SD vs TC Misrouting

## User Input

```text
territory: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_02-29__loop_diagnose__sd_vs_tc_misrouting/
  (this inquiry's artifacts — _branch.md + 6 discipline outputs)
goal: Use LOOP_DIAGNOSE to diagnose what went wrong in the loop chain that produced the
  SourceDescriptor-vs-TranslationConfig misrouting visible in the conversation correction snippet.
```

---

## Map Header

- **Run mode:** root / project-space (breadth) | **Entry point:** fresh
- **Identities enumerated:** 15
- **Routes:** 8 teleological + 7 epistemic
- **High-priority count:** 6
- **Frontier flags:** 3

---

## Route Index

| # | Direction | grain | kind | engagement | Priority |
|---|---|---|---|---|---|
| R1 | Apply the corrected routing to `translation_config.py` and create `source_descriptor.py` | project-space | teleological | DEVELOP | HIGH |
| R2 | Branch-test MC1 (Candidate-Self-Consistency sub-axis) on next bulk-edge-case inquiry's critique | project-space | epistemic | TEST | HIGH |
| R3 | Branch-test MC2 (Comparative-Pattern Test perspective) on next bulk-edge-case inquiry's sensemaking | project-space | epistemic | TEST | HIGH |
| R4 | Promote MC1 to canonical td-critique spec after successful branch-test | project-space | teleological | DEVELOP | MED |
| R5 | Promote MC2 to canonical sense-making spec after successful branch-test | project-space | teleological | DEVELOP | MED |
| R6 | Update `edge_cases_into_config_schema` finding text with INVALID commitments (B2, B4-3of4, B8) | project-space | epistemic | REFINE | HIGH |
| R7 | Update `chunking_deep_dive` finding text with frame-revised commitment (A1 principle sharpening note) | project-space | epistemic | REFINE | HIGH |
| R8 | Watch for second correction chain involving facts-vs-strategies conflation (triggers MC3 promotion) | project-space | epistemic | INVESTIGATE-FRONTIER | LOW |
| R9 | Codify LOOP_DIAGNOSE as a permanent skill (gated: after 5-10 successful runs per protocol Step 5) | project-space | epistemic | INVESTIGATE-FRONTIER | LOW |
| R10 | Investigate optional SD-fact companion fields (e.g., `source_archaism_present`) per P11 caveat | project-space | epistemic | INVESTIGATE-FRONTIER | LOW |
| R11 | Re-examine 7 DEFER fields from edge-cases finding under the corrected facts-vs-strategies distinction (do their revival triggers still hold?) | project-space | epistemic | DIAGNOSE | MED |
| R12 | Audit other recent inquiries for facts-vs-strategies conflation pattern | project-space | epistemic | DIAGNOSE | MED |
| R13 | Document the Frame-exit-Completeness-on-wrong-axis failure pattern as a sense-making meta-failure example | project-space | epistemic | CONSOLIDATE | MED |
| R14 | Document the substance-axis-prosecution-missed-internal-contradiction pattern as a td-critique meta-failure example | project-space | epistemic | CONSOLIDATE | MED |
| R15 | Update the in-flight 4_mesele translation work to use the corrected routing (R1) | project-space | teleological | DEVELOP | HIGH |

---

## Per-Route Records

### R1 — Apply corrected routing to schema files

- **Direction:** modify `translation_config.py` to add 3 new TC fields (`source_language_fluency`, `source_temporal_register`, `quranic_citation_policy` — or as A8-style apparatus axis); create `source_descriptor.py` with `SourceDescriptor` class containing `source_chunking_units`, `source_edition`, and `embedded_languages: list[str]` (facts only).
- **Goal:** land the corrected routing in actual code; resolves the user's WHY-axis `practical-application-now`.
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** implement per P11 corrected-routing table.
- **WHY:** the misrouting needs to be undone before further work depends on it.
- **Priority:** HIGH | **Confidence:** MED (depends on SourceDescriptor schema implementation per chunking finding's MUST)
- **Guidance:** add 3 fields to TC first (cheap; non-blocking); declare SD stub with the 3 source-only fields; bundle with R6 + R7 finding-text updates

### R2 — Branch-test MC1

- **Direction:** apply the new "Candidate-Self-Consistency sub-axis" on the next inquiry whose critique handles bulk-edge-case routing decisions
- **Goal:** validate MC1 catches at least one internal-contradiction-shaped issue
- **grain:** project-space | **kind:** epistemic | **engagement-type:** TEST
- **Movement:** when next bulk-edge-case inquiry runs, apply the sub-axis as a branch experiment; observe whether it fires; observe whether it catches anything
- **WHY:** per LOOP_DIAGNOSE guardrail "Do not promote LOOP_DIAGNOSE into a standalone skill or discipline until 5 to 10 diagnostic MVLw findings show a stable internal method" — same principle applies to MCs: branch-test before promoting
- **Priority:** HIGH | **Confidence:** MED
- **Guidance:** evaluation gates per P6; if fires + catches: PROMOTE per R4; if fires + no catches: monitor; if doesn't fire: defect

### R3 — Branch-test MC2

- **Direction:** apply the new "Comparative-Pattern Test perspective" on the next inquiry whose sensemaking handles structural-routing decisions
- **Goal:** validate MC2 catches at least one pattern-mismatch issue
- **grain:** project-space | **kind:** epistemic | **engagement-type:** TEST
- **Movement:** as R2 but for sensemaking perspective
- **WHY:** complementary to MC1 (different mechanism); both should be branch-tested before canonical promotion
- **Priority:** HIGH | **Confidence:** MED
- **Guidance:** evaluation gates per P7

### R4 — Promote MC1 to canonical spec

- **Direction:** add Candidate-Self-Consistency sub-axis to `td-critique.md` Phase 2 Multi-axis prosecution depth check
- **Goal:** make MC1 part of the canonical critique discipline
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** ~5-10-line refinement note in td-critique spec
- **WHY:** consolidates branch-test evidence
- **Priority:** MED | **Confidence:** MED
- **Guidance:** gated on R2 success

### R5 — Promote MC2 to canonical spec

- **Direction:** add Comparative-Pattern Test perspective to `sense-making.md` Phase 2 perspective list
- **Goal:** make MC2 part of the canonical sense-making discipline
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** ~10-15-line perspective entry in sense-making spec
- **WHY:** consolidates branch-test evidence
- **Priority:** MED | **Confidence:** MED
- **Guidance:** gated on R3 success

### R6 — Update edge-cases finding text

- **Direction:** add a Changes-from-Prior note to `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md` reflecting B2 / B4 (3 of 4) / B8 INVALID commitments per P9 inherited-re-test
- **Goal:** prevent future readers from inheriting the misrouting
- **grain:** project-space | **kind:** epistemic | **engagement-type:** REFINE
- **Movement:** inline correction note at top of finding citing this diagnostic inquiry; revise the per-field decision table; revise the TC-delta-0 headline
- **WHY:** the edge-cases finding is the closest thing to canonical truth on the schema; leaving the misrouting in place is high-risk
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** add at finding's top as a Correction Notice; do not delete original content (preserves diagnostic-trail)

### R7 — Update chunking finding text

- **Direction:** add inline note to `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` section 3 reflecting A1 commitment frame-revision (principle anchored to source-natural-units; sharpening gated per MC3)
- **Goal:** make the chunking principle's scope explicit
- **grain:** project-space | **kind:** epistemic | **engagement-type:** REFINE
- **Movement:** ~3-5-line inline addition near line 113
- **WHY:** prevents future over-generalization
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** small inline note; gated principle sharpening per MC3 remains gated

### R8 — Watch for second facts-vs-strategies correction chain

- **Direction:** monitor future inquiries for a second instance of facts-vs-strategies conflation
- **Goal:** trigger MC3 promotion when revival condition fires
- **grain:** project-space | **kind:** epistemic | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** when second instance occurs, open follow-up to promote principle sharpening
- **WHY:** LOOP_DIAGNOSE guardrail — wait for second instance before canonical principle change
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** revival trigger documented; no action until trigger fires

### R9 — Codify LOOP_DIAGNOSE as permanent skill

- **Direction:** once 5-10 LOOP_DIAGNOSE runs have shown stable internal method, codify as standalone skill
- **Goal:** preserve LOOP_DIAGNOSE pattern beyond protocol wrapper
- **grain:** project-space | **kind:** epistemic | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** when count threshold reached, propose skill spec
- **WHY:** per `loop_diagnose.md` Step 5 guardrail: "Do not promote LOOP_DIAGNOSE into a standalone skill or discipline until 5 to 10 diagnostic MVLw findings show a stable internal method"
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** count-based revival; this is run #1 of LOOP_DIAGNOSE

### R10 — Investigate SD-fact companion fields

- **Direction:** examine whether SD should carry FACT-side companions to TC strategy fields (e.g., `source_archaism_present: bool` companion to `source_temporal_register`)
- **Goal:** sharpen the facts-vs-strategies model
- **grain:** project-space | **kind:** epistemic | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** future inquiry when SD is being implemented
- **WHY:** P11 caveat from critique
- **Priority:** LOW | **Confidence:** LOW
- **Guidance:** defer; not blocking

### R11 — Re-examine 7 DEFER fields under corrected distinction

- **Direction:** check whether any of the 7 deferred fields from edge-cases finding (#4, #5, #9, #10, #11, #12, #14) would route differently under the corrected facts-vs-strategies distinction
- **Goal:** ensure the DEFER revival triggers still target the right schema home
- **grain:** project-space | **kind:** epistemic | **engagement-type:** DIAGNOSE
- **Movement:** brief audit of the 7 fields against the corrected distinction
- **WHY:** the misrouting may have propagated to revival-trigger framing
- **Priority:** MED | **Confidence:** MED
- **Guidance:** quick audit; likely most fields stay deferred but routing-when-revived may need re-examination

### R12 — Audit other recent inquiries for facts-vs-strategies conflation pattern

- **Direction:** scan recent inquiries (other than chunking + edge-cases) for similar conflation
- **Goal:** confirm the pattern is isolated, or surface other instances
- **grain:** project-space | **kind:** epistemic | **engagement-type:** DIAGNOSE
- **Movement:** light scan; not a full LOOP_DIAGNOSE per inquiry
- **WHY:** if pattern is widespread, MC3 promotion case strengthens
- **Priority:** MED | **Confidence:** LOW
- **Guidance:** quick scan first; deep diagnostic only if pattern observed

### R13 — Document Frame-exit-Completeness-on-wrong-axis failure as sense-making meta-failure example

- **Direction:** add the "applied perspective but on wrong axis" pattern as a documented failure example in `sense-making.md` failure modes
- **Goal:** generalize the lesson beyond this specific case
- **grain:** project-space | **kind:** epistemic | **engagement-type:** CONSOLIDATE
- **Movement:** brief addition to sense-making spec's failure-mode catalog
- **WHY:** the pattern is structurally distinct from Perspective Blindness (which is "perspective not applied"); this is "perspective applied wrong"
- **Priority:** MED | **Confidence:** MED
- **Guidance:** bundle with R5 promotion

### R14 — Document substance-axis-prosecution-missed-internal-contradiction pattern

- **Direction:** add the "substance-axis didn't apply candidate's own claims" pattern as a documented failure example in `td-critique.md`
- **Goal:** generalize the lesson
- **grain:** project-space | **kind:** epistemic | **engagement-type:** CONSOLIDATE
- **Movement:** brief addition to td-critique spec's failure-mode catalog
- **WHY:** the pattern is the inverse-companion of MC1 (the MC catches it going forward; the failure-mode entry helps recognize it retrospectively)
- **Priority:** MED | **Confidence:** MED
- **Guidance:** bundle with R4 promotion

### R15 — Update 4_mesele translation work to use corrected routing

- **Direction:** the in-flight 4_mesele translation needs to use the corrected schema (not the misrouted one)
- **Goal:** propagate correction to actual translation work
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** when 4_mesele translation work resumes, use corrected schema per R1
- **WHY:** the original misrouting would have applied to 4_mesele; correction must propagate
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** depends on R1; gated on R1 completion

---

## Excluded

| Candidate | Why excluded |
|---|---|
| The 14 edge-cases as candidates | Settled in P9 inherited re-test (4 INVALID + 10 confirmed/revised); not directions to engage again |
| KILLed Innovation Inversions | Rejected on structural grounds |
| The LOOP_DIAGNOSE protocol's own pipeline (A→Su→S→D→I→C→R) | Process artifact; not a route |
| User's anti-bloat preference | Constraint informing every route, not a route itself |
| The decomposition pieces P1-P11 | Process artifacts; their outputs ARE the routes |
| Future bulk-edge-case inquiries themselves | The inquiries are vessels; the routes are MC branch-tests within those inquiries |

---

## Telemetry

- **Mode:** root/project-space (breadth) | **Entry point:** fresh
- **Identities enumerated:** 15
- **Routes by kind:** 8 teleological + 7 epistemic
- **Routes by engagement-type:**
  - DEVELOP: 4 (R1, R4, R5, R15)
  - TEST: 2 (R2, R3)
  - REFINE: 2 (R6, R7)
  - INVESTIGATE-FRONTIER: 3 (R8, R9, R10)
  - DIAGNOSE: 2 (R11, R12)
  - CONSOLIDATE: 2 (R13, R14)
  - DEEPEN/PURSUE-SEED/REFRAME: 0
- **High-priority count:** 6 (R1, R2, R3, R6, R7, R15)
- **Frontier flags:** 3 (R8, R9, R10)
- **LAYER 1 + LAYER 2 failure modes:** NONE fired

### Self-Assessment Verdict

**PROCEED**

15 routes; 6 HIGH-priority covering immediate corrective work (R1, R6, R7, R15) + branch-test work (R2, R3); 3 frontier flags for gated future work. Critical observation: **R1 + R6 + R7 + R15 form a tight bundle — the corrective propagation must happen end-to-end (code + finding-text + downstream-translation-work) or the misrouting remains live**.
