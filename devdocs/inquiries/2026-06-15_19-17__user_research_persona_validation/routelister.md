# Routelister — user_research_persona_validation

## User Input

```text
territory: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_19-17__user_research_persona_validation/ (this inquiry's artifacts — _branch.md + articulate_simple.md + surfacing.md + sensemaking.md + decomposition.md + innovation.md + critique.md).
goal: act on R8 "user research / persona validation (interview translators)" from prior Mac-app inquiry; produce hybrid research-plan + synthetic-persona-validation deliverable that the user can act on (per _branch.md Goal + SV6 model).
Save the route-map to /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_19-17__user_research_persona_validation/routelister.md; the persistent index lives at /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_19-17__user_research_persona_validation/_route.md (load it if present — index-extending; create it if not — fresh).
```

---

## Map Header

- **Run mode:** root / project-space (breadth)
- **Entry point:** fresh
- **Identities enumerated:** 16
- **High-priority count:** 3 (R1, R2, R3)
- **Frontier flags:** 4 (I11 secondary stakeholders; I12 cross-corpus; I13 + I14 methodology meta)

---

## Route Index

| # | Direction | grain | kind | engagement | Priority |
|---|---|---|---|---|---|
| R1 | Execute the research plan with real translator interviews | project-space | teleological | DEVELOP | HIGH |
| R2 | Apply Critique REFINEs to the synthesis | project-space | epistemic | REFINE | HIGH |
| R3 | Decide what to do about AE1 + AE2 in Mac-app design | project-space | teleological | CONSOLIDATE | HIGH |
| R4 | Insert Correction Notice on Mac-app finding noting synthesis-flagged challenges | project-space | teleological | DEVELOP | MED |
| R5 | Empirically validate synthesis findings before v1 build commitment | project-space | epistemic | TEST | MED |
| R6 | Re-design BYO API key model with managed-paid option | project-space | teleological | DEVELOP | MED |
| R7 | Re-tier v1 essential / v2 differentiating split | project-space | teleological | REFINE | MED |
| R8 | Add team-license + academic-discount monetization options | project-space | teleological | DEVELOP | MED |
| R9 | Document LLM-level mechanisms for harmony viz + lineage + principle-features | project-space | epistemic | DIAGNOSE | MED |
| R10 | Refresh personas when substrate evolves | project-space | teleological | REFINE | LOW |
| R11 | Investigate secondary stakeholders (editors; publishers) as research subjects | project-space | epistemic | INVESTIGATE-FRONTIER | LOW |
| R12 | Cross-corpus persona expansion (Hindu / Buddhist / Christian patristic) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R13 | Document the synthetic-persona-validation methodology as a reusable spec | project-space | epistemic | CONSOLIDATE | LOW |
| R14 | Develop real-interview methodology playbook companion | project-space | teleological | DEVELOP | LOW |
| R15 | Cross-platform expansion (Windows / Linux / iPad) | project-space | teleological | INVESTIGATE-FRONTIER | LOW |
| R16 | Compare synthesis findings to real-interview findings to calibrate LLM-bias | project-space | epistemic | TEST | LOW |

---

## Per-Route Records

### R1 — Execute the research plan with real translators

- **Direction:** execute the research plan from §2 of the finding with 20-30 real translator interviews
- **Goal:** validate the synthetic findings empirically; produce real persona profiles + design-impact memo
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** recruit per persona screening criteria (5 personas × ~5 participants); conduct semi-structured interviews per the 10-block script; analyze per the framework (affinity mapping → JTBD → pain-point ranking → feature-priority synthesis → design-impact mapping); produce real persona profiles + memo updating Mac-app finding's verdicts
- **WHY:** the inquiry's primary onward action; everything downstream depends on real validation; gates Mac-app inquiry's R1 v1 build
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance Mode:** full
  - Sample size: ~5 per persona × 5 = ~25 participants total
  - Compensation: $50-100 academic honorarium; $100-300 professional rate; gift cards as alternative
  - Recruitment channels: ATA, AAR, FIT; theological publisher contacts (Risale-i Nur Tahsiye Vakfı; Fons Vitae; Brill); LinkedIn; specialized forums
  - IRB / ethics: institutional consent forms if academic; basic consent template otherwise
  - Expected timeline: 3-6 months for full execution (recruitment 4-8 weeks; interviews 4-6 weeks; analysis 4-6 weeks)
- **Depth-link:** none

### R2 — Apply Critique REFINEs to the synthesis

- **Direction:** fix the 5 Critique-identified epistemic + hallucination issues in the synthesis before finalizing the finding
- **Goal:** honest, substrate-anchored, properly-disclaimed synthesis output
- **grain:** project-space | **kind:** epistemic | **engagement-type:** REFINE
- **Movement:**
  - PC3: tag P2 #4 (BYO managed-preference), P4 #5 (Mac-only constraint), P5 #5 (LLM-mechanism critique) as "extrapolated beyond substrate; lower confidence"
  - PC4: remove "60%" hallucinated figure in Elena's D2 cell; flag Aliyah's D8 "travel work" as soft-extrapolation; deepen Elena's D4 cell with critic-stance applied to multi-translation collation
  - PC5: weaken verdict language from "found INVALID" to "synthesis-flagged as POTENTIALLY INVALID; requires real-interview validation"; rename "Evidence" column to "Matrix evidence (synthesis)"; add per-row synthesis-provenance
  - PC7: add per-row provenance note to Re-test admin section
  - PC8: add "Synthesis bias unknown" as Refinement Trigger
- **WHY:** the synthesis output's honesty is load-bearing; without these REFINEs, the deliverable risks treating syntheses as empirical findings
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance Mode:** full
  - apply at finding-write-time (CONCLUDE step)
  - source-of-truth: critique.md §3 Verdict Summary
- **Depth-link:** none

### R3 — Decide what to do about AE1 + AE2 in Mac-app design

- **Direction:** synthesis surfaced two strong-signal design concerns about the Mac-app design; user must decide whether to revisit immediately or gate on real-interview validation
- **Goal:** action-decision on whether AE1 BYO API key model + AE2 3-tier triage split need redesign work now or after empirical validation
- **grain:** project-space | **kind:** teleological | **engagement-type:** CONSOLIDATE
- **Movement:** review AE1 (BYO API key flagged by 4/5 personas) + AE2 (3-tier triage v1 essential tier flagged by ≥3 personas); decide: (a) act now based on synthesis (faster but risks synthesis-bias error); (b) gate on R1 + R5 empirical validation (slower but more defensible); (c) hybrid (act on one; gate the other)
- **WHY:** the synthesis-flagged concerns are the inquiry's most actionable design feedback; deferring entirely loses immediate value; acting blindly risks synthesis-bias errors
- **Priority:** HIGH | **Confidence:** MED
- **Guidance Mode:** full
  - recommended hybrid: gate AE1 (BYO key) on real-interview validation; act on AE2 (re-tier v1 essential) early because the specific re-tier moves (lineage view earlier; TM consideration) have low downside and high upside
- **Depth-link:** none

### R4 — Insert Correction Notice on Mac-app finding

- **Direction:** add a Correction Notice at the top of the prior `comprehenslate_mac_app_design` finding noting that synthesis-flagged challenges to its commitments exist, and pointing to this inquiry
- **Goal:** prevent future inquiries from inheriting Mac-app commitments without seeing the synthesis-flagged concerns
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** insert notice; reference R5 + R6 + R7 as gated follow-ups
- **WHY:** matches the inquiry's challenge of the prior; standard Correction Notice protocol per prior session findings
- **Priority:** MED | **Confidence:** HIGH
- **Guidance Mode:** compact
  - notice text: *"**Synthesis-Flagged Concerns (2026-06-15):** Persona validation in `devdocs/inquiries/2026-06-15_19-17__user_research_persona_validation/` synthesis-flagged 2 commitments as POTENTIALLY needing revision: (a) BYO API key model may be a barrier for non-technical users; (b) 3-tier triage's v1 essential vs differentiating split may need re-tiering. Validate with real-interview research before committing design changes."*
- **Depth-link:** none

### R5 — Empirically validate synthesis findings before v1 build commitment

- **Direction:** before committing to v1 build (Mac-app inquiry R1), conduct the real-interview research per R1 of this inquiry to validate or refute the synthesis-flagged concerns
- **Goal:** empirical grounding for high-stakes design changes
- **grain:** project-space | **kind:** epistemic | **engagement-type:** TEST
- **Movement:** sequence R1 (execute research plan) before Mac-app v1 build commitment; treat real-interview findings as authoritative; update Mac-app design per real findings
- **WHY:** v1 build is high-stakes; synthesis-flagged concerns must be validated before driving design changes
- **Priority:** MED | **Confidence:** HIGH
- **Guidance Mode:** compact
- **Depth-link:** none

### R6 — Re-design BYO API key model with managed-paid option

- **Direction:** if real-interview validation confirms AE1, redesign the LLM-provider model to include a managed-paid option alongside BYO API key
- **Goal:** unblock adoption for non-technical theological translators
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** specify managed-paid model (Comprehenslate-managed API keys; subscription pricing; opt-in for users who prefer convenience); preserve BYO option for privacy-preferring + tech-savvy users
- **WHY:** AE1 emergent; gated on R5 empirical validation
- **Priority:** MED | **Confidence:** MED
- **Guidance Mode:** compact
  - revival trigger: R5 confirms 4/5 synthesis ratio in real interviews
- **Depth-link:** none

### R7 — Re-tier v1 essential / v2 differentiating split

- **Direction:** if real-interview validation confirms AE2, move some currently-differentiating features (lineage view; some Quality-layer Policies; possibly TM) to v1 essential
- **Goal:** v1 MVP that real translators actually adopt
- **grain:** project-space | **kind:** teleological | **engagement-type:** REFINE
- **Movement:** re-evaluate Mac-app finding's §5 MVP roadmap; specifically consider moving per-chunk lineage view + VoiceMarkingPolicy + SourceApparatusPolicy + possibly TM into v1
- **WHY:** AE2 emergent; specific re-tier moves (lineage in v1) have low downside even before validation
- **Priority:** MED | **Confidence:** MED
- **Guidance Mode:** compact
  - some moves (lineage view to v1) could happen pre-validation per R3 hybrid recommendation
- **Depth-link:** none

### R8 — Add team-license + academic-discount monetization options

- **Direction:** monetization model should support team-license (per P2 Salma) + academic-discount (per P5 Elena)
- **Goal:** broader market fit; lower friction for editor-shops and academic users
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** specify pricing tiers: individual one-time / team-license (5-seat / 10-seat) / academic-discount (verified .edu email)
- **WHY:** D10 synthesis signal across multiple personas
- **Priority:** MED | **Confidence:** MED
- **Guidance Mode:** compact
  - gated on Mac-app finding's R10 monetization decision
- **Depth-link:** none

### R9 — Document LLM-level mechanisms for harmony viz + lineage + principle-features

- **Direction:** address P5 Elena's critique by documenting which LLM-level mechanisms back the harmony preservation, lineage, and principle-derived features — not just the UI visualization
- **Goal:** defensible research-grade tool; not "empty calories" UI claims
- **grain:** project-space | **kind:** epistemic | **engagement-type:** DIAGNOSE
- **Movement:** produce LLM-mechanism specification documents for each principle-derived feature; specify which LLM prompt patterns, which fine-tuning if any, which validation tests; make available to academic-translator users on request
- **WHY:** academic critic feedback (P5); could become a research-grade differentiator
- **Priority:** MED | **Confidence:** MED
- **Guidance Mode:** compact
- **Depth-link:** none

### R10 — Refresh personas when substrate evolves

- **Direction:** when `references/core/` or Mac-app design substrate changes, refresh the 5 synthetic personas to reflect new substrate
- **Goal:** personas stay current with substrate
- **grain:** project-space | **kind:** teleological | **engagement-type:** REFINE
- **Movement:** detect substrate change (file mtime; commit signal); re-run persona generation with updated substrate; mark old personas stale
- **WHY:** substrate-calibration trigger from Sensemaking
- **Priority:** LOW | **Confidence:** MED
- **Guidance Mode:** compact
- **Depth-link:** none

### R11 — Investigate secondary stakeholders

- **Direction:** editors who hire translators; publishers commissioning translations — they influence tool adoption but aren't direct users
- **Goal:** broader research coverage; identify adoption drivers beyond direct users
- **grain:** project-space | **kind:** epistemic | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** sub-inquiry to define secondary-stakeholder personas + research approach
- **WHY:** Open Question from Sensemaking; out of current inquiry scope
- **Priority:** LOW | **Confidence:** MED
- **Guidance Mode:** compact
- **Depth-link:** none

### R12 — Cross-corpus persona expansion

- **Direction:** add personas for Hindu / Sanskrit, Buddhist / Pali, Christian patristic / Greek-Latin translators
- **Goal:** test Mac-app design portability across non-Islamic, non-Jewish theological-translation corpora
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** sub-inquiry to generate cross-corpus personas; pressure-test design portability
- **WHY:** Research Frontier from Sensemaking; same frontier as prior `chunk_types_vs_mechanisms` inquiry
- **Priority:** LOW | **Confidence:** MED
- **Guidance Mode:** compact
  - revival trigger: when Comprehenslate scope expands beyond Risale-i Nur
- **Depth-link:** none

### R13 — Document the synthetic-persona-validation methodology as reusable spec

- **Direction:** generalize the methodology used here (synthesis disclaimer + substrate-anchoring + bias-balance + 5×N matrix + verdict thresholds) for use on other Comprehenslate components
- **Goal:** reusable validation pattern for future tool-design inquiries
- **grain:** project-space | **kind:** epistemic | **engagement-type:** CONSOLIDATE
- **Movement:** abstract the methodology from this inquiry's specifics; produce a spec document; reference it from future similar inquiries
- **WHY:** methodology has reuse value beyond this single inquiry
- **Priority:** LOW | **Confidence:** MED
- **Guidance Mode:** compact
- **Depth-link:** none

### R14 — Develop real-interview methodology playbook companion

- **Direction:** complement R13 with a "how to actually run the interviews" playbook
- **Goal:** end-to-end methodology coverage (synthesis + real-interview)
- **grain:** project-space | **kind:** teleological | **engagement-type:** DEVELOP
- **Movement:** flesh out R1's research plan into a step-by-step playbook (recruitment scripts; interviewer training notes; analysis templates; consent forms)
- **WHY:** companion to R13; supports R1 execution and future similar research
- **Priority:** LOW | **Confidence:** MED
- **Guidance Mode:** compact
- **Depth-link:** none

### R15 — Cross-platform expansion

- **Direction:** investigate Windows / Linux / iPad expansion based on P4 Avraham + P5 Elena's Mac-only concerns
- **Goal:** broaden potential user base
- **grain:** project-space | **kind:** teleological | **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** sub-inquiry on cross-platform expansion strategy (Catalyst port; native ports; cloud companion)
- **WHY:** persona-flagged constraint; from Mac-app finding's Open Questions
- **Priority:** LOW | **Confidence:** LOW
- **Guidance Mode:** compact
  - revival trigger: when Mac v1 ships
- **Depth-link:** none

### R16 — Compare synthesis findings to real-interview findings to calibrate LLM-bias

- **Direction:** after R1 completes, compare the synthesis output to the real-interview output; identify systematic biases in the LLM-synthesis
- **Goal:** calibrate future synthesis methodology; quantify LLM-bias for future inquiries
- **grain:** project-space | **kind:** epistemic | **engagement-type:** TEST
- **Movement:** side-by-side comparison; identify divergences; classify as confirmation-bias / LLM-articulation-style / substrate-availability / etc.
- **WHY:** Open Question from Critique; enables better future syntheses
- **Priority:** LOW | **Confidence:** MED
- **Guidance Mode:** compact
  - gated on R1 completion
- **Depth-link:** none

---

## Excluded

| Candidate | Why excluded |
|---|---|
| Compile finding.md (CONCLUDE step) | Control-flow / process move per §1.3 NOT-list |
| Archive discipline files to docarchive/ (CONCLUDE step) | Control-flow / process move |
| Re-do this inquiry with different methodology | Control-flow; this inquiry has converged |
| Treat the synthesis as definitive findings | Contradicts inquiry's core honesty commitment (FP1) |
| Skip the research plan and rely only on synthesis | Contradicts hybrid deliverable shape committed at Sensemaking SV6 |

---

## Telemetry

- **Mode:** root / project-space (breadth)
- **Entry point:** fresh
- **Identities enumerated:** 16
- **Routes by kind:** teleological = 9 (R1, R3, R4, R6, R7, R8, R10, R12, R14, R15); epistemic = 7 (R2, R5, R9, R11, R13, R16)
- **Routes by engagement-type:** DEVELOP = 6 (R1, R4, R6, R8, R14, R15); REFINE = 3 (R2, R7, R10); CONSOLIDATE = 2 (R3, R13); TEST = 2 (R5, R16); INVESTIGATE-FRONTIER = 3 (R11, R12, R15); DIAGNOSE = 1 (R9)
- **High-priority routes:** 3 (R1, R2, R3)
- **Individuations made:** 16 (fresh)
- **Uncertain individuations flagged:** 0
- **Stale entries:** N/A
- **Frontier flags:** 4 (R11 secondary stakeholders; R12 cross-corpus; R13 + R14 methodology meta)
- **LAYER 1 failure modes checked:** all 6 not fired
  - Over-merge: NOT FIRED (R2 R3 R4 R6 R7 each distinct identity)
  - Under-coverage: NOT FIRED (every Critique REFINE + emergent + Open Question mapped to a route)
  - Wrong-grain: NOT FIRED (breadth-run; identities not manifestations)
  - Goal-loss: NOT FIRED (every route's WHY explicit)
  - Type-misassignment: NOT FIRED (engagement-types match)
  - Index-drift: N/A
- **LAYER 2 failure modes checked:** all 4 not fired
  - Selection-creep: NOT FIRED (attributive priority; no winner chosen)
  - Process-coupling: NOT FIRED (CONCLUDE excluded)
  - Description-collapse: NOT FIRED (prescriptive verbs)
  - Manifestation-dump: NOT FIRED (R1 has sub-tasks as guidance, not separate identities)

### Self-assessment verdict

**PROCEED.**

Territory swept at identity resolution; 16 identities individuated; no LAYER 1 or LAYER 2 flags; output ready for downstream consumption (CONCLUDE will read this for the finding's Next Actions).
