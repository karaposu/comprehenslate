# Routelister — schemas_rationale_and_policy_list

## User Input

```text
territory: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/ (this inquiry's artifacts — _branch.md + articulate_simple.md + surfacing.md + sensemaking.md + decomposition.md + innovation.md + critique.md).
goal: explain why schemas.py makes a lot more sense + list other NonMainLangPartsPolicy-shaped scenarios (per _branch.md Goal section).
Save the route-map to /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/routelister.md; the persistent index lives at /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/_route.md (load it if present — index-extending; create it if not — fresh).
```

---

## Map Header

- **Run mode:** root / project-space (breadth)
- **Entry point:** fresh (no prior `_route.md` existed)
- **Identities enumerated:** 9
- **High-priority count:** 2 (I1 + I5)
- **Frontier flags:** 2 (I3 / I6 — project-wide-doc frontier and cross-corpus frontier)

---

## Route Index

| # | Direction | grain | kind | engagement | Priority |
|---|---|---|---|---|---|
| R1 | Adopt the 6 strong Policy candidates into `schemas.py` | project-space | teleological | DEVELOP | HIGH |
| R2 | Document the FP2 test predicate at `schemas.py` module level | project-space | teleological | PURSUE-SEED | MED |
| R3 | Promote FP2 to a project-wide schema-style convention | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R4 | Pressure-test FP2 against a rare/dead-language corpus | project-space | epistemic | TEST | LOW |
| R5 | Insert Correction Notices into the 3 impacted prior findings | project-space | teleological | DEVELOP | HIGH |
| R6 | Extend the Policy catalog to non-Islamic theological-translation corpora | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R7 | Specify Policy-class co-application precedence rules | project-space | epistemic | REFINE | MED |
| R8 | Revive `source_language_fluency` field placement | project-space | teleological | PURSUE-SEED | LOW |
| R9 | Branch-test MC1 + MC2 on a non-chunking inquiry | project-space | epistemic | TEST | LOW |

---

## Per-Route Records

### R1 — Policy-class adoption into `schemas.py`

- **Direction:** adopt the 6 strong Policy candidates from Item 2 into `schemas.py`
- **Goal:** schemas.py rationale + Policy-shaped scenarios
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** extend schemas.py with `SourceApparatusPolicy`, `VoiceMarkingPolicy`, `ArchaicRegisterPolicy`, `HonorificsPolicy`, `FormulaicOpeningPolicy`, `EmbeddedPoetryPolicy` — deliberate which to include, implement adopted
- **WHY:** the 6 strong candidates pass all 4 filters with HIGH confidence and are load-bearing for Nursi-corpus translation work; `schemas.py` currently has only `NonMainLangPartsPolicy`
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance Mode:** full
  - per-candidate pydantic sketches are in `finding.md` Item 2 section (each Policy class is a single-field `BaseModel` with a `Literal[N]` enum)
  - `ArchaicRegisterPolicy` carries the homeless `source_temporal_register` field re-homed from the edge_cases finding
  - deliberation question per candidate: is this corpus-need active now (adopt), or speculative (defer)?
- **Depth-link:** none

### R2 — FP2 in-code documentation

- **Direction:** document the LLM-inferable test predicate at `schemas.py` module level
- **Goal:** schemas.py rationale + Policy-shaped scenarios
- **grain:** project-space | **kind:** teleological | **engagement-type:** PURSUE-SEED
- **Movement:** add a module-level docstring or developer-facing comment naming FP2 ("Don't declare what the LLM can infer") and the integration-time predicate ("at integration time, ask: can the LLM derive this value from the source text + the rest of the config?")
- **WHY:** PC5 COULD action; in-code documentation makes the principle visible to future contributors and prevents schema additions that violate FP2
- **Priority:** MED | **Confidence:** HIGH
- **Guidance Mode:** compact
  - text can mirror PC1's principle statement + operational form
- **Depth-link:** none

### R3 — FP2 as project-wide convention

- **Direction:** promote FP2 from finding-specific principle to a project-wide schema-style convention
- **Goal:** schemas.py rationale + Policy-shaped scenarios
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** write a project-wide schema-style guide naming FP2 with concrete examples beyond schemas.py (hypothetical logging-config schema; database-config schema; any future schema in Comprehenslate)
- **WHY:** AE1 (deferred assembly emergent from Innovation); FP2 generalizes beyond schemas.py to any AI-assisted system's schema design
- **Priority:** LOW | **Confidence:** MED
- **Guidance Mode:** expand-on-drill
  - revival trigger from AE1 — *"when project-wide schema-style guide is written or 3+ inquiries reference FP2 as load-bearing"*
- **Depth-link:** none

### R4 — LLM-inferability calibration test

- **Direction:** pressure-test FP2 against a rare-language corpus to find calibration limits
- **Goal:** schemas.py rationale + Policy-shaped scenarios
- **grain:** project-space | **kind:** epistemic | **engagement-type:** TEST
- **Movement:** pick a corpus with a rare/dead language (Aramaic, Coptic, Sumerian, Akkadian, Ge'ez); apply FP2 to its schema design; observe where the LLM-inferable test breaks
- **WHY:** Phase/Calibration-State perspective identified that FP2 assumes current-LLM-capability for source-language detection; rare/dead languages may require declarative fields the current architecture omits
- **Priority:** LOW | **Confidence:** MED
- **Guidance Mode:** compact
  - open question from PC6 Research Frontiers; specific corpora to test against not yet identified
- **Depth-link:** none

### R5 — Correction-propagation to 3 priors

- **Direction:** insert Correction Notices into the 3 impacted prior findings
- **Goal:** schemas.py rationale + Policy-shaped scenarios
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** add a Correction Notice section at the top of each impacted prior finding; preserve original content as historical record
- **WHY:** PC5 MUST actions; without notices, future inquiries land on the priors and inherit invalid commitments
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance Mode:** full
  - Three concrete impacted findings with notice text in `finding.md` Next Actions section:
    - `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md` — INVALID on TC.chunking_granularity + SD.canonical_level + corpus mappings
    - `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` — INVALID on SourceDescriptor paper schema; split-placement principle CONFIRMED-with-frame-revision
    - `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md` — INVALID on 4 SD additions (per-field sub-statuses apply)
- **Depth-link:** none

### R6 — Cross-corpus Policy catalog completeness

- **Direction:** extend the Item 2 Policy catalog to non-Islamic theological-translation corpora
- **Goal:** schemas.py rationale + Policy-shaped scenarios
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** survey each non-Islamic corpus (Tanakh; Bible; Sanskrit-Hindu; Pali Buddhist; Christian patristic) for recurring authorial edge-cases; apply the 4 filters; produce additional Policy candidates
- **WHY:** PC6 Research Frontier; Item 2 catalog was filtered through Nursi-load-bearing-ness; cross-corpus completeness is a known gap
- **Priority:** LOW | **Confidence:** MED
- **Guidance Mode:** expand-on-drill
  - revival gated on Comprehenslate scope expanding to non-Islamic corpora
  - separate inquiry seed; benefit from corpus-specific consultants per tradition
- **Depth-link:** none

### R7 — Policy-class co-application precedence rules

- **Direction:** specify or empirically test precedence rules for Policy classes that co-apply to the same text span
- **Goal:** schemas.py rationale + Policy-shaped scenarios
- **grain:** project-space | **kind:** epistemic | **engagement-type:** REFINE
- **Movement:** take known co-application cases (Bismillah governed by both `FormulaicOpeningPolicy` + `NonMainLangPartsPolicy`); evaluate whether the policies' value choices are independent on close inspection; document precedence if ambiguity surfaces in real translation work
- **WHY:** Critique's REFINE on PC6 added this as the 4th open question; co-application is functional not conflicting in current cases but may surface ambiguity in practice
- **Priority:** MED | **Confidence:** MED
- **Guidance Mode:** compact
  - refinement trigger: ambiguous render outputs from co-applying policies in actual translation work
- **Depth-link:** none

### R8 — source_language_fluency revival

- **Direction:** revive `source_language_fluency` field placement (deferred from edge-cases finding; homeless after SD-drop)
- **Goal:** schemas.py rationale + Policy-shaped scenarios
- **grain:** project-space | **kind:** teleological | **engagement-type:** PURSUE-SEED
- **Movement:** if A3 `source_culture` produces ambiguous assignments due to language-fluency conflation in actual translation work, decide between adding a `ReaderFluencyPolicy` class, revisiting TC modification, or leaving deferred
- **WHY:** open residual from edge_cases finding's 4 SD additions; deferred-with-revival-trigger in PC6
- **Priority:** LOW | **Confidence:** LOW
- **Guidance Mode:** compact
  - revival trigger: ambiguous A3 assignments observed in real translation work
- **Depth-link:** none

### R9 — MC1 + MC2 branch-test on non-chunking inquiry

- **Direction:** apply MC1 (Candidate-Self-Consistency sub-axis) at critique stage and MC2 (Comparative-Pattern Test perspective) at sensemaking stage on the next non-chunking-related inquiry
- **Goal:** schemas.py rationale + Policy-shaped scenarios
- **grain:** project-space | **kind:** epistemic | **engagement-type:** TEST
- **Movement:** on next non-chunking-related inquiry, fire MC1 + MC2 as evaluation gates; observe whether either catches a structural issue; accumulate evidence for canonical promotion
- **WHY:** gate inherited from chunk_types_vs_mechanisms finding's promotion strategy; that inquiry validated MC1 + MC2 on chunking-adjacent cases — promotion to canonical needs evidence beyond chunking-adjacent
- **Priority:** LOW | **Confidence:** MED
- **Guidance Mode:** compact
  - inherited from chunk_types_vs_mechanisms finding's Next Actions DEFERRED items
- **Depth-link:** none

---

## Excluded

| Candidate | Why excluded |
|---|---|
| Run an inquiry on Comprehenslate's overall architecture | Out of territory; this inquiry's scope is schemas.py + Policy catalog; broader architecture is a different territory |
| Restore SourceDescriptor as a schema | Contradicts user-explicit constraint (C2 — SD dropped); territory does not open this direction |
| CONCLUDE protocol steps (compile finding; archive disciplines) | Control-flow / process-control moves per §1.3 NOT-list — not concept-directions |
| Revise schemas.py to remove NonMainLangPartsPolicy | No territory signal supports this; user has just adopted NonMainLangPartsPolicy and validated it across the session |
| Rewrite TC to absorb Policy classes | Contradicts user-explicit constraint (C1 — TC frozen); territory does not open this direction |

---

## Telemetry

- **Mode:** root / project-space (breadth)
- **Entry point:** fresh
- **Identities enumerated:** 9
- **Routes by kind:** teleological = 6 (R1, R2, R3, R5, R6, R8); epistemic = 3 (R4, R7, R9)
- **Routes by engagement-type:** DEVELOP = 2 (R1, R5); PURSUE-SEED = 2 (R2, R8); INVESTIGATE-FRONTIER = 2 (R3, R6); TEST = 2 (R4, R9); REFINE = 1 (R7)
- **High-priority routes:** 2 (R1, R5)
- **Individuations made:** 9 (all new — fresh entry)
- **Uncertain-individuations flagged:** 0
- **Stale entries flagged:** N/A (fresh entry)
- **Frontier flags:** 2 (R3 — project-wide-convention frontier; R6 — cross-corpus frontier)
- **LAYER 1 failure modes checked:** all 6 not fired
  - Over-merge: NOT FIRED (each identity is structurally distinct)
  - Under-coverage: NOT FIRED (every Sensemaking / Critique residual mapped to a route)
  - Wrong-grain: NOT FIRED (breadth-run lists identities, not manifestations; correction-propagation is one identity with 3 priors as manifestations)
  - Goal-loss: NOT FIRED (every route has explicit WHY linking to the goal)
  - Type-misassignment: NOT FIRED (each engagement-type passes the membership test under its kind)
  - Index-drift: N/A (fresh entry)
- **LAYER 2 failure modes checked:** all 4 not fired
  - Selection-creep: NOT FIRED (attributive Priority/Confidence emitted; no winner chosen)
  - Process-coupling: NOT FIRED (no control-flow moves in the route-map; CONCLUDE protocol steps explicitly excluded)
  - Description-collapse: NOT FIRED (every route is prescriptive — what to DO, not what the territory IS)
  - Manifestation-dump: NOT FIRED (R5 carries 3 priors as a single concept-identity, not 3 separate routes)

### Self-assessment verdict

**PROCEED.**

Territory swept at identity resolution; 9 identities individuated; no LAYER 1 or LAYER 2 flags; output ready for downstream consumption (CONCLUDE will read this for the finding's Next Actions context).
