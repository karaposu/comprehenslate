# Critique — Loop Diagnose: SD vs TC Misrouting

## User Input

Input: `_branch.md` + upstream `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md` + `innovation.md`. Candidates: 11 piece principals + 3 Assembly emergents = 14 candidates.

---

## Phase 0 — Dimension Construction

### Dimensions (8)

| # | Dimension | Weight | Source |
|---|---|---|---|
| 1 | **Correctness** | HIGH | LOOP_DIAGNOSE protocol's required-output schema; SV6 stabilized model |
| 2 | **Evidence-strength** | CRITICAL | LOOP_DIAGNOSE Step 4 confidence requirements (HIGH = multiple artifacts converge) |
| 3 | **LOOP_DIAGNOSE-protocol-conformance** | HIGH | Protocol's required output sections + per-hypothesis schema + per-MC schema |
| 4 | **Attribution-rigor** | HIGH | LOOP_DIAGNOSE guardrails ("allow mixed or unknown attribution"; "do not collapse all failures into discipline failures") |
| 5 | **Maintenance-candidate-actionability** | HIGH | LOOP_DIAGNOSE Step 5 ("only propose source edit when evidence is strong enough"; require evaluation gates) |
| 6 | **Self-reference-mitigation** | HIGH | The subject IS the loop framework; this critique is itself a discipline of the loop being diagnosed. Critical risk per Self-Reference Collapse failure mode |
| 7 | **External-anchor compliance** | MED | Anchors available: chunking finding text (verbatim quoted in surfacing item 1); edge-cases finding text (smoking-gun docstring quoted in surfacing item 7); existing 8 axes (config_base_source.md) |
| 8 | **Anti-overreach** (per LOOP_DIAGNOSE Step 5 guardrails) | HIGH | "Do not propose broad fundamentals rewrites from one weak correction chain" |

### Frame-premise test

SV6's central assumption: "PRIMARY attribution to edge-cases sensemaking SV6 + edge-cases critique; CONTRIBUTORY to chunking principle articulation." Load-bearing premises:

1. **The misrouting was NOT introduced at chunking finding stage.** Independent test: the chunking finding's own routings (#1/#6/#7) are correct (verified by surfacing item 3). Premise SURVIVES.

2. **The smoking-gun docstring contradiction (docstring "Refines A3" while routing to SD) was visible to substance-axis prosecution.** Independent test: substance-axis prosecution is defined in td-critique spec as "apply the candidate's own mechanism to the candidate's worked examples and primary unit *literally*, not via intuitive reading." The docstring is a worked example; applying it literally would have surfaced the contradiction. Premise SURVIVES.

3. **The conversation correction's argument was reachable from substrate available to the original inquiries.** Independent test: A1/A2/A3 are in `config_base_source.md` (verified by surfacing items 10-12); the existing 8-axis pattern was knowable. Premise SURVIVES.

### Substance-vs-Label success criteria

Critical dimensions need substance-level criteria:
- **Correctness substance:** does each piece's text actually contain the LOOP_DIAGNOSE-required fields, or just label them?
- **Evidence-strength substance:** do citations point at specific verifiable file locations?
- **Attribution-rigor substance:** is mixed attribution genuinely traced through evidence, or is "mixed" a hedge?

### External-anchor dimension

Anchors:
- Chunking finding line 113 quoted verbatim in surfacing R1 item 1 ✓
- Edge-cases finding's P3 docstring quoted in surfacing R2 item 7 ✓
- Existing 8-axis schema (TC fields) referenced ✓
- Conversation correction preserved verbatim in `_branch.md` Source Input ✓

---

## Phase 1 — Fitness Landscape

- **Viable:** HIGH all 8 dimensions.
- **Dead:** fails Evidence-strength (vague citations) OR Self-reference-mitigation (uncritical self-validation) OR Anti-overreach (broad rewrites).
- **Boundary:** Evidence MED OR Self-reference partial.
- **Unexplored:** has the LOOP_DIAGNOSE protocol's evaluation gates actually been TESTED on a real branch experiment? (No — first use; gates remain theoretical until tested.)

---

## Phase 2 — Adversarial Evaluation

### P1 — Correction Chain Summary

**Prosecution.** Substance check: priors named with paths; correction signal preserved verbatim; what-changed stated. External-anchor: chunking finding line 113 cited (verbatim from surfacing); edge-cases finding's P3 docstring quoted. PASS substance.

**Specific failure case:** does P1 acknowledge the comparative-evidence-not-ground-truth status? YES ("Corrected direction (comparative evidence per LOOP_DIAGNOSE; NOT ground truth)").

**Verdict: SURVIVE.** Clean.

### P2 — Hypothesis 1 (edge-cases sensemaking SV6)

**Prosecution.**
- **Substance:** affected-stage named (Sensemaking SV6 Ambiguity 4 resolution); shortcoming-type specific (Frame-exit Completeness applied on wrong axis); evidence cited (Ambiguity 4 reasoning contradicted itself).
- **Specification-gap:** "Frame-exit Completeness applied on wrong axis" — does the artifact show this concretely? Yes — sensemaking.md cites "Frame-exit Completeness GATING fired (chunk has 6 project-wide referents)" — confirming it fired on chunking axis, not on Group α membership axis. Evidence concrete.
- **Evidence-strength sub-axis:** HIGH per LOOP_DIAGNOSE definition ("multiple artifacts converge"): the SV6 commitment is the locus; the docstring contradiction is internal; the comparative pattern is external. Three artifacts.

**Verdict: SURVIVE.** Clean.

### P3 — Hypothesis 2 (edge-cases critique)

**Prosecution.**
- **Substance (smoking gun is load-bearing):** P3 explicitly quotes the docstring contradiction — "Refines A3 source_culture" while routing to SD. Direct artifact citation.
- **Evidence-strength sub-axis:** HIGH ("smoking gun" is exactly the "multiple artifacts converge" condition — internal contradiction + missing dimension enumeration + corrected-direction-uses-pattern-comparison).
- **Specific failure case prosecution:** P3 says the critique's Correctness dimension "performed correctly given its frame; the frame inherited the SV6 error." Is this nitpicking on a valid critique pass, or honest attribution? It's honest — the critique can't catch a frame-level error its dimensions don't probe. This is a structural attribution to the critique stage, not to the dimensions' execution.

**Verdict: SURVIVE.** Clean.

### P4 — Hypothesis 3 (chunking principle CONTRIBUTORY)

**Prosecution.**
- **Attribution-rigor sub-axis:** the hypothesis EXPLICITLY says CONTRIBUTORY not primary. Confidence MED stated. Why-not-stronger field cites the substrate-reachability argument. Mixed-attribution is genuine.
- **Anti-overreach:** "principle as STATED is correct; sharpening it requires evidence beyond one correction chain (per LOOP_DIAGNOSE guardrail)." Direct citation of protocol guardrail.
- **Evidence-strength:** MED — principle articulation responsibility is a judgment call.

**Verdict: SURVIVE.** Clean — appropriately MED-confidence; honest contributory attribution.

### P5 — Failure Attribution Summary

**Prosecution.**
- **Attribution-rigor:** 3-row table mirrors the 3 hypotheses; PRIMARY x 2 + CONTRIBUTORY x 1. Per LOOP_DIAGNOSE: "Do not force every failure into a discipline" — table includes specific stage names (sensemaking SV6, critique P3, principle articulation), NOT "loop framing in general." Specific.

**Verdict: SURVIVE.** Clean.

### P6 — MC1 substance-axis sub-axis sharpening

**Prosecution.**
- **Maintenance-candidate-actionability:** specific file path (`td-critique.md` Phase 2); name given ("Candidate-Self-Consistency sub-axis"); risk-class LOW; expected-benefit concrete (would have caught the docstring contradiction); evaluation gate observable (branch test on next bulk-edge-case inquiry's critique).
- **Anti-overreach:** ~5-10-line refinement note — narrow, not broad rewrite.
- **External-anchor:** the smoking-gun docstring case is the worked example proving the sub-axis would catch the right thing.

**Verdict: SURVIVE.** Strongest MC.

### P7 — MC2 Comparative-Pattern Test perspective

**Prosecution.**
- **Maintenance-candidate-actionability:** specific file path (`sense-making.md` Phase 2 Perspective Checking); name given ("Comparative-Pattern Test perspective"); evaluation gate observable.
- **Anti-overreach:** new perspective entry in established list of perspectives — additive, narrow.
- **Specific failure case:** could the new perspective be folded into existing Definitional/Internal Consistency perspective? Innovation's P7 Inversion-candidate already addressed this — Specific-vs-pattern recognition cue at Phase 3 is about whether a key insight generalizes; the new perspective is about whether a structural decision matches an existing routing pattern. Different operations. KEEP separate.

**Verdict: SURVIVE.** Co-strongest MC.

### P8 — MC3 principle sharpening (GATED)

**Prosecution.**
- **Anti-overreach:** EXPLICITLY GATED — revival trigger is "second correction chain involves similar facts-vs-strategies conflation." Direct adherence to LOOP_DIAGNOSE guardrail ("Do not propose broad fundamentals rewrites from one weak correction chain").
- **Evidence-strength:** acknowledged as MED (contributory); gating is appropriate.

**Verdict: SURVIVE.** Clean GATED-MC.

### P9 — Inherited Commitments Re-test

**Prosecution.**
- **Synthesis-rigor sub-axis:** 14 commitments enumerated (4 from chunking + 10 from edge-cases); per-commitment status assigned (RE-TESTED-confirmed / RE-TESTED-frame-revised / RE-TESTED-INVALID / INHERITED-WITHOUT-RE-TEST with reason). Three commitments INVALIDATED (B2 TC delta = 0; B4 3 of 4 SD additions; B8 EmbeddedLanguagePolicy carrying quranic_citation_policy) — substantive re-test producing invalidations, not rubber-stamping.
- **Substance-axis:** each invalidation cites specific evidence; not just a label.

**Verdict: SURVIVE.** Strong synthesis-rigor performance.

### P10 — Diagnostic Verdict

**Prosecution.**
- **Verdict assignment correctness:** ACTIONABLE because at least one MC has concrete shape + evaluation gate (MC1 + MC2 both do). Per LOOP_DIAGNOSE definition of ACTIONABLE: matches.
- **Main uncertainty stated:** "relative weight between Hypothesis 1 and Hypothesis 2." Honest.
- **Next step concrete:** branch-test MC1 + MC2 on next bulk-edge-case inquiry.

**Verdict: SURVIVE.** Clean.

### P11 — Corrected routing (secondary)

**Prosecution.**
- **Secondary-status marking:** P11 explicitly labels itself "secondary constructive output." Per LOOP_DIAGNOSE guardrail (diagnose-not-fix), this is the right framing.
- **Substance:** 4 fields with original vs corrected routing + reasoning per field. Direct quote of P3 docstring at row 2 ("the edge-cases P3 docstring 'Refines A3' already names the correct home"). Concrete.
- **Specific failure case:** could P11 be more deeply correct? Yes — row 13 `source_temporal_register` notes "the FACT that the source has archaic register → could be a SD declaration (e.g., `source_archaism_present: bool` or implicit in `source_edition`)". This raises the question: should the FACT live on SD (e.g., `source_archaism_present`) alongside the strategy on TC (`source_temporal_register`)? P11 mentions but doesn't decide. Acceptable for secondary output.

**Verdict: SURVIVE with caveat** — for completeness, the optional "facts" companion fields on SD (e.g., `source_archaism_present`) could be noted as a future-frontier candidate.

### Assembly Emergent 1 — substrate-reachability anchor

**Prosecution.** Claim: failure is "missing test against available information," not "missing information." Backed by: A1/A2/A3 in config_base_source.md (available); P3 docstring (available internally). Substrate-grounded.

**Verdict: SURVIVE.** Clean.

### Assembly Emergent 2 — MC1+MC2 complementary

**Prosecution.** Substance: MC1 catches internal contradictions; MC2 catches external-pattern mismatches. Different mechanisms. Edge-cases misrouting failed both — true. Future misroutings might fail only one — plausible.

**Verdict: SURVIVE.** Clean.

### Assembly Emergent 3 — Self-Reference Blindness partial mitigation

**Prosecution.** Critical examination — this is the most important Assembly emergent for THIS inquiry. The AI is running disciplines on itself (the AI wrote chunking + edge-cases findings; the AI is now diagnosing them).
- **Mitigation 1:** LOOP_DIAGNOSE's protocol explicitly addresses self-reference (comparative-evidence framing).
- **Mitigation 2:** user pushback was the trigger — not AI self-discovery.
- **Mitigation 3:** independent re-test via Frame-exit Completeness perspective applied to Group α membership-types (not the same axis used in the original inquiry).
- **Residual blind spot:** the AI's diagnostic role is to SYSTEMATIZE the user's intuition; the AI's own reasoning may protect aspects the user didn't pushback on.

**Specific failure case prosecution:** could the diagnosis be self-validating? The MC1 sub-axis is named "Candidate-Self-Consistency" — applying THIS test to THIS diagnostic itself, does the diagnostic apply its own internal claims against its own conclusions? Let me check: the diagnostic claims MC1 + MC2 are testable; the evaluation gates name specific observables; the diagnostic does NOT claim MC1/MC2 have already proved their worth. Self-consistency holds.

**Verdict: SURVIVE.** Clean — mitigation acknowledged, residual blind spot named.

---

## Phase 3 — Verdict Summary

| Candidate | Verdict |
|---|---|
| P1 Correction Chain Summary | SURVIVE |
| P2 Hypothesis 1 (sensemaking SV6) | SURVIVE |
| P3 Hypothesis 2 (critique) | SURVIVE |
| P4 Hypothesis 3 (chunking principle CONTRIBUTORY) | SURVIVE |
| P5 Attribution table | SURVIVE |
| P6 MC1 substance-axis sub-axis | SURVIVE |
| P7 MC2 comparative-pattern perspective | SURVIVE |
| P8 MC3 principle sharpening (GATED) | SURVIVE |
| P9 Inherited Re-test | SURVIVE |
| P10 Diagnostic Verdict | SURVIVE |
| P11 Corrected routing (secondary) | SURVIVE with caveat (note optional SD-fact companion fields as future-frontier) |
| Assembly 1 substrate-reachability | SURVIVE |
| Assembly 2 MC1+MC2 complementary | SURVIVE |
| Assembly 3 Self-Reference partial mitigation | SURVIVE |

**Distribution:** 13 clean SURVIVE + 1 SURVIVE-with-mild-caveat + 0 REFINE + 0 KILL.

This distribution looks unusually clean. Let me apply the Rubber-Stamping check: did prosecution genuinely try? The smoking-gun, substrate-reachability, and self-reference-residual-blindspot tests were genuine attacks. The fact that they didn't produce REFINE or KILL is because the upstream sensemaking and innovation absorbed the structural shifts already (Frame-exit Completeness fired; per-piece Inversion-candidates tested; LOOP_DIAGNOSE protocol's guardrails were directly cited). The diagnostic is genuinely clean. **Not rubber-stamping.**

---

## Phase 3.5 — Assembly Check

The 11 principals + 3 emergents jointly form a LOOP_DIAGNOSE-protocol-compliant finding. No new emergent assembly beyond what Innovation surfaced.

---

## Phase 4 — Coverage + Convergence

### Coverage
- 8 dimensions applied to all 14 candidates.
- LOOP_DIAGNOSE's required-output schema fully covered (P1 Chain + P2-P4 Hypotheses + P5 Attribution + P6-P8 MCs + P10 Verdict).
- Synthesis Trigger covered (P9 14-commitment re-test).
- Secondary user-WHY-axis motivation covered (P11).

### Convergence
- **Landscape stability:** STABLE.
- **Clean SURVIVE exists:** YES (13 of 14).
- **Mechanism-Independence status:** VALIDATED. External anchors cited verbatim (chunking line 113; edge-cases P3 docstring; existing 8 axes). Multiple discipline outputs cited (chunking finding § 3; edge-cases sensemaking; edge-cases critique; conversation correction). Multiple-anchor convergence.

### Failure-mode check

| # | Mode | Status |
|---|---|---|
| 1 | Wrong Dimensions | NO — 8 dimensions tuned to LOOP_DIAGNOSE protocol + project-specific risks |
| 2 | Rubber-Stamping | NO — see explicit check above; prosecution was genuine; clean verdicts result from upstream rigor not absent challenge |
| 3 | Nitpicking | NO — 0 KILL; caveats are operational |
| 4 | Dimension Blindness | NO — Frame-premise test applied; Self-reference dimension included |
| 5 | False Convergence | NO — verdict ACTIONABLE has concrete MCs with evaluation gates |
| 6 | Evaluation Drift | N/A — single iteration |
| 7 | Self-Reference Collapse | **PARTIAL MITIGATION (acknowledged in Assembly 3)** — subject is the loop framework itself; mitigated by LOOP_DIAGNOSE protocol + user-pushback trigger + Frame-exit-on-different-axis; residual blind spot named |
| 8 | Axis Absence | NO |
| 9 | External-Grounding Absence | NO — verbatim quotes present at load-bearing claim sites (chunking line 113; edge-cases docstring) |

---

## Final Deliverable

### (a) Dimensions

8 dimensions: Correctness HIGH, Evidence-strength CRITICAL, LOOP_DIAGNOSE-protocol-conformance HIGH, Attribution-rigor HIGH, Maintenance-candidate-actionability HIGH, Self-reference-mitigation HIGH, External-anchor MED, Anti-overreach HIGH.

### (b) Fitness Landscape

- Viable (14 candidates): all 11 principals + 3 emergents.
- Boundary: empty.
- Dead: empty.

### (c) Verdicts

13 clean SURVIVE + 1 SURVIVE-with-mild-caveat (P11). 0 REFINE. 0 KILL.

### (d) Coverage Map

| Region | Candidates | Coverage |
|---|---|---|
| LOOP_DIAGNOSE-required-output | P1, P2-P4, P5, P6-P8, P10 | Confirmed |
| Synthesis Trigger compliance | P9 | Confirmed |
| Secondary constructive (user WHY-axis) | P11 | Confirmed |
| Substrate-reachability framing | Assembly 1 | Confirmed |
| MC complementarity | Assembly 2 | Confirmed |
| Self-Reference mitigation | Assembly 3 | Confirmed (partial-mitigation acknowledged) |

### (e) Signal

**TERMINATE with ranked survivors.**

Top 5:
1. **P6 MC1 Candidate-Self-Consistency sub-axis** — strongest MC; concrete spec change with smoking-gun evidence.
2. **P7 MC2 Comparative-Pattern Test perspective** — co-strongest MC; would have caught misrouting via different mechanism than MC1.
3. **P3 Hypothesis 2** — strongest hypothesis (smoking-gun docstring contradiction).
4. **P2 Hypothesis 1** — joint-primary hypothesis (Frame-exit Completeness on wrong axis).
5. **P10 Diagnostic Verdict ACTIONABLE** — backed by MC1 + MC2 concrete shapes + evaluation gates.

P11 caveat to address at CONCLUDE: note optional SD-fact companion fields (e.g., `source_archaism_present`) as future-frontier suggestion.

---

## Convergence Telemetry

- Dimension coverage: 8/8 applied to 14 candidates.
- Adversarial strength: STRONG — substance-axis + smoking-gun + substrate-reachability + self-reference probes applied.
- Landscape stability: STABLE.
- Clean SURVIVE exists: YES (13/14).
- Mechanism-Independence: VALIDATED.
- Failure modes observed: 1 PARTIAL-MITIGATION (Self-Reference Collapse — acknowledged in Assembly 3; not silent).
- **Overall: PROCEED.** No FLAG needed; Self-Reference is structurally inherent to the inquiry and is handled per LOOP_DIAGNOSE protocol.
