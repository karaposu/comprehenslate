# Sensemaking — Loop Diagnose: SD vs TC Misrouting

## User Input

`_branch.md` + `articulate_simple.md` + `surfacing.md`. Per LOOP_DIAGNOSE: synthesis priors are chunking finding + edge-cases finding; re-test inherited commitments rigorously; allow mixed attribution; conversation correction = comparative evidence not ground truth.

---

## SV1 — Baseline

The chunking finding established the "schema ownership matches data ownership" principle. The downstream edge-cases inquiry applied that principle and misrouted 3 of 4 SourceDescriptor additions (`source_language_fluency`, `source_temporal_register`, `quranic_citation_policy`). The edge-cases critique gave the misrouting a clean SURVIVE. A conversation correction revealed the error using comparison to the existing 8-axis TC pattern (A1/A2/A3 reader-properties on TC). The diagnostic must identify where in the chain (chunking principle, edge-cases application, edge-cases critique) the misrouting was locked in.

---

## Phase 1 — Cognitive Anchor Extraction

**Constraints:**
- **C1** — LOOP_DIAGNOSE guardrails: conversation correction = comparative evidence (not ground truth); attribution may be mixed; broad rewrites discouraged from one correction chain.
- **C2** — The chunking finding's principle is the inherited commitment most under test; per Synthesis Trigger, must re-test rigorously.
- **C3** — Anti-bloat: maintenance candidates must be specific (no broad spec rewrites).

**Key Insights:**
- **K1** — The chunking finding's principle was articulated **specifically for source-natural-units**, not abstracted to "any fact about the source vs any strategy for handling source." The abstraction was implicit; downstream had to make it.
- **K2** — The conversation correction was **reachable from the existing substrate** (the 8 axes were in `config_base_source.md`; the A1/A2/A3 reader-property comparison was available). No new evidence emerged from outside the inquiries' reach. This means the failure is NOT "missing information" — it's "missing test against available information."
- **K3** — The smoking gun is internal: edge-cases P3 docstring says `source_language_fluency` "Refines A3 source_culture" while routing it to SD. A3 lives on TC. If a field refines A3, structural consistency demands it lives WHERE A3 LIVES (or modifies A3 directly). The docstring-vs-routing internal contradiction was visible to any test that applied the candidate's own claims against itself.
- **K4** — The misrouting was first LOCKED IN at edge-cases sensemaking SV6, ENCODED into decomposition's P3 piece-question ("What does each SourceDescriptor addition look like?"), instantiated by innovation P3, and APPROVED by critique P3 (SURVIVE clean). The chain has multiple stages that should have caught it.

**Structural Points:**
- **S1** — Three candidate failure loci (mutually compatible, not exclusive): (a) chunking finding's principle articulation under-sharpened (R6); (b) edge-cases sensemaking/innovation/decomposition encoded the misrouting (R5); (c) edge-cases critique failed to test principle-application (R4).
- **S2** — The failure modes "Substance-axis prosecution miss" and "Comparative-pattern test missing" are both load-bearing **per the conversation correction's own logic**: the correction worked by (i) reading the candidate's own docstring ("refines A3") and (ii) comparing to existing pattern (A1/A2/A3 on TC). Both moves were available to the loop and not taken.

**Foundational Principles:**
- **P1** — Per LOOP_DIAGNOSE: prefer evidence-backed hypotheses over exact root-cause; allow mixed attribution.
- **P2** — Per the sense-making spec's Load-bearing concept test refinement: inherited concepts must be re-tested when the same finding applies them.
- **P3** — Per the td-critique spec's Substance-vs-Label success criteria refinement: dimensions whose stated scope tests load-bearing claims must include substance-level criteria that operationally probe the substance, not just labels.

**Meaning-Nodes:**
- **M1 — facts-vs-strategies conflation** — the deep pattern: confusing "source HAS X" with "user wants to handle X this way."
- **M2 — internal-contradiction-not-flagged** — the docstring-vs-routing inconsistency that should have triggered substance-axis prosecution.
- **M3 — comparative-pattern test** — comparing each routing decision to the pattern of existing fields in the target schema (A1/A2/A3 demonstrate reader-property pattern on TC).
- **M4 — principle-application correctness** — a missing critique dimension or sensemaking perspective.
- **M5 — abstraction-not-made** — the chunking finding stated the principle for a specific case; downstream had to abstract it; abstraction conflated.

### SV2

The chain failed at multiple loci. The chunking finding established the principle specifically (source-natural-units → SD; strategy enum → TC); the edge-cases inquiry's sensemaking made an abstraction the chunking finding did not authorize (any "source-related" field → SD); the abstraction conflated facts-about-the-source (true source properties) with strategies-for-handling-the-source (user choices, parallel to existing TC axes). The critique used 8 dimensions but none tested "does this routing actually apply the inherited principle correctly?" The smoking-gun internal contradiction (docstring says "refines A3" while routing to SD) shows the failure is NOT a missing-information failure — it is a missing-test failure.

---

## Phase 2 — Perspective Checking

**Technical / Logical.** The 8 axes in `config_base_source.md` follow a clean pattern: reader-properties (A1, A2, A3) and user-strategies (A4-A8) all on TC. There is no facts-about-source schema yet (SourceDescriptor is paper-only). The chunking finding correctly distinguished source-NATURAL-UNITS (corpus-specific data declarations) from STRATEGY enums. The edge-cases inquiry abstracted "source-natural-units" into "anything source-related" — an unauthorized abstraction.

→ **A1 (new anchor):** The chunking finding's principle is correct AS STATED but does not authorize the abstraction the edge-cases inquiry made.

**Human / User.** The user noticed the misrouting immediately upon reading the explanation. The cue was conceptual: "fluency feels like a TranslationConfig field" — they intuitively recognized the reader-property pattern. The user did NOT cite the chunking finding's principle in their pushback; they used their own model of where reader-properties live. This suggests **the user's mental model included the right comparative pattern (A1/A2/A3 are TC fields) and the loop's processes did not**.

→ **A2:** User intuition out-performed the loop. The loop's structured tests were less effective than human pattern-matching against the existing schema.

**Strategic / Long-term.** If this conflation pattern is general (facts-vs-strategies), other inquiries may make the same mistake. The maintenance value of catching the pattern (not just the specific instance) is high.

→ **A3:** The maintenance candidates should target the GENERAL pattern (a critique dimension; a sensemaking perspective), not the specific case.

**Risk / Failure.** Per LOOP_DIAGNOSE guardrails: don't promote LOOP_DIAGNOSE into a discipline from one correction chain; don't propose broad rewrites. Maintenance candidates must be narrow with evaluation gates.

→ **A4:** Bias toward small, testable maintenance candidates with concrete evaluation gates.

**Resource / Feasibility.** Two candidate maintenance targets emerge with concrete shapes: (a) a new td-critique dimension or sub-axis "principle-application correctness" that explicitly tests routing decisions against the inherited principle; (b) a new sensemaking perspective "comparative-pattern test" that compares each candidate's routing to existing fields in the target schema.

→ **A5:** Both candidates are implementable as ~5-line refinement notes in their respective discipline specs. Low risk; testable on the next bulk-edge-case inquiry.

**Definitional / Internal Consistency.** Does the chunking finding's principle CONTRADICT the conversation correction? Let me test. The principle: "source-natural-units are properties of the source." Source-natural-units are CORPUS DECLARATIONS — what units the corpus has. That's a fact about the corpus. The principle is correct.

Does the principle extend to ANY source-related field? The principle as stated says "source-natural-units." It does NOT say "anything that references the source." The extension was an over-generalization by the edge-cases inquiry. Per the conversation correction: `source_language_fluency` "describes the reader, not the source text. The source text doesn't have fluency; the reader does." The correction REFINES the principle: facts about the source go to SD; reader-properties (even when referencing source languages) go to TC; strategies for handling source properties go to TC.

→ **A6:** The chunking finding's principle survives but needs SHARPENING: explicitly distinguish facts-about-the-source from reader-properties (even reader-properties that reference source) from strategies-for-handling-source.

**Definitional / Frame-exit Completeness.** Gating predicate test: this inquiry's commitments include inherited terms (chunking finding's principle; SourceDescriptor; TranslationConfig) used across multiple distinct values. Gating FIRES.

1. **Existence Enumeration.** What does "source-related field" refer to project-wide?
   - facts about the source text (edition, languages present, structural units) → SD
   - properties of the READER vis-à-vis the source (fluency, cultural-recognition, domain-expertise) → TC (existing pattern: A1/A2/A3)
   - user strategies for handling source properties (foreignize-vs-domesticate, preserve-vs-modernize archaism, citation rendering) → TC (existing pattern: A5/A6)
   - the source's runtime constraints (chunking budget, context size) → PipelineConfig

   The edge-cases inquiry's "Group α SourceDescriptor" lumped category (a) and a chunk of (b) and a chunk of (c) into one bucket. The conflation was load-bearing for the misrouting.

2. **Role Assessment.** Each excluded category has a clear role. Categories (b) and (c) are NOT out-of-scope for this inquiry; they're MIS-PLACED in the inquiry's frame.

3. **Verdict Rigor.** "Group α = SourceDescriptor" verdict survived edge-cases critique without test. Counter-argument: "Group α membership is a mix of source-facts and reader-properties and strategies, not a coherent schema-home grouping." Counter-failure: the verdict survived only because no test asked "is each Group α member actually a source-fact?" Confidence: HIGH that the Group α verdict was LOW CONFIDENCE in retrospect.

4. **Residual.** Any frame-exit concern not captured? The inquiry's frame did not include the EXISTING 8-AXIS PATTERN as a comparative-evidence input to test against each routing decision. That existence-enumeration omission is itself a finding.

→ **A7:** Frame-exit Completeness perspective (had it fired) would have caught the misrouting. The edge-cases inquiry's sensemaking did fire Frame-exit Completeness but applied it to "chunk has 6 project-wide referents" (about chunking), not to "Group α members have distinct referent types." The perspective was used, but on the wrong axis.

**Phase / Calibration-State.** The project is at FRAMEWORK-CLOSURE-stage-PLUS. The schemas in question (SourceDescriptor, PipelineConfig) are paper commitments. Implementing them with misrouted fields would propagate the error. Calibration urgency: HIGH.

→ **A8:** Calibration urgency is high because the misrouting hasn't propagated to code yet; correction is cheap now and expensive later.

### SV3

After 8 perspectives:
1. The chunking finding's principle is correct but stated specifically; the edge-cases inquiry over-generalized it.
2. The user's intuition out-performed the loop because the user's mental model included the existing 8-axis pattern as comparative evidence.
3. The smoking gun is internal-contradiction-not-flagged (docstring-vs-routing) plus comparative-pattern-test-missing (no test compared against A1/A2/A3 routing pattern).
4. The Frame-exit Completeness perspective COULD have caught the misrouting — it was applied at sensemaking but on the wrong axis (about chunking, not about Group α membership types).
5. Maintenance candidates: principle sharpening + critique dimension + sensemaking perspective extension.

**Meta-Inspection at SV3:** H1 candidate set — are the 6 surfacing hypotheses really distinct? Check: #32 principle-under-sharpening and #28 (chunking abstraction not made) are the same identity. #33 critique-dimension-gap and #37 comparative-pattern-test-missing partially overlap. Lean-to-split preserves: keep separate but note overlap.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: Where in the chain was the misrouting locked in?

**Counter-interpretation:** The misrouting was locked in at the chunking finding (principle was ambiguous). All downstream stages just inherited the ambiguity.

**Why counter fails (structural):** The chunking finding's principle is CORRECT as stated — it does not authorize the abstraction the edge-cases inquiry made. The chunking finding routed `source_chunking_units` to SD correctly (those ARE source facts); it did NOT route `source_temporal_register` or `source_language_fluency` at all (those aren't in the chunking inquiry's scope). The chunking finding cannot be blamed for routing decisions it did not make.

**Confidence:** HIGH for "the misrouting was locked in DOWNSTREAM of chunking, not at chunking."

**Resolution:** The misrouting was locked in at the **edge-cases inquiry's sensemaking SV6** (Ambiguity 4 resolution committed `source_language_fluency` → SD). It was encoded into the decomposition's P3 question, instantiated by innovation, and not caught by critique. Attribution is MIXED across edge-cases inquiry stages, but PRIMARY locus is sensemaking SV6 (where it was first committed) and critique (where it should have been caught).

### Ambiguity 2: Was the chunking finding's principle responsible for the conflation pattern?

**Counter-interpretation:** Yes — by not explicitly distinguishing facts-about-source from reader-properties-referencing-source from strategies-for-handling-source, the chunking principle was incomplete and the downstream conflation was a foreseeable result.

**Why counter is partly right:** The chunking finding's principle is anchored to "source-natural-units" specifically. It does NOT include the broader distinction. Sharpening the principle WOULD have made the misrouting harder to commit.

**But also:** The conversation correction was reachable from substrate that ALREADY EXISTED in the edge-cases inquiry (the 8 axes; A1/A2/A3 reader-properties on TC). The principle's specificity didn't prevent the correction from being available; it just wasn't applied.

**Confidence:** MED — partial responsibility; not the sole cause.

**Resolution:** The chunking finding's principle is PART-RESPONSIBLE (insufficient anchoring) but the downstream inquiry HAD ENOUGH SUBSTRATE to catch the misrouting and didn't. Attribution: principle-under-sharpening (CONTRIBUTING) + edge-cases critique-blind-spot (PRIMARY).

### Ambiguity 3: Which maintenance candidate has the strongest evidence?

**Counter-interpretations and resolution:**

- **Sharpen the principle in `harmony_layer.md`-style canonical doc?** Yes valuable, but ANY principle-sharpening would need testing on multiple cases before promoting. Defer pending more correction chains.
- **Add "principle-application correctness" as a td-critique dimension?** Specific; testable. Smoking-gun (internal contradiction) demonstrates substance-axis sub-axis would have caught it. STRONG.
- **Add "comparative-pattern test" as a sensemaking perspective?** Specific; testable. Conversation correction USED this exact move to reach the right answer. STRONG.
- **Audit decomposition for piece-questions that presuppose routing decisions?** Specific but more invasive. Defer.

**Resolution:** Two candidates have strongest evidence:
- **MC1: Substance-axis sub-axis sharpening in td-critique** — apply the candidate's own internal claims against its own decision (the docstring-vs-routing contradiction would have fired this).
- **MC2: Comparative-pattern test as a sensemaking perspective** — for any new schema-home routing decision, explicitly compare each candidate against the existing pattern of routed fields in the target schema.

### Ambiguity 4: Should the maintenance candidates include a sharpened principle?

**Counter:** Yes — articulate "facts-about-source go to SD; reader-properties go to TC; strategies-for-handling-source go to TC" as an explicit refinement.

**Why partial:** This IS a sharpening but the sharpening's evidence base is one correction chain. LOOP_DIAGNOSE guardrail: "Do not promote broad rewrites from one correction chain."

**Resolution:** Propose principle sharpening as a CANDIDATE for the chunking finding maintenance (low-risk inline sharpening); flag it; gate on second occurrence before treating as canonical.

### Ambiguity 5: Is the failure attributable to the LOOP framework (meta) or to specific stages?

**Counter:** The framework's discipline-set is structurally capable; this is a specific-stage failure.

**Why this holds:** Frame-exit Completeness perspective + substance-axis prosecution + Load-bearing concept test ALL existed and could have caught the misrouting. They were either not applied or applied on the wrong axis. The framework's capability was present; the application was deficient.

**Confidence:** HIGH.

**Resolution:** Attribute to specific stages (edge-cases sensemaking + edge-cases critique) plus contributory principle-under-sharpening (chunking). NOT a meta-loop framework failure.

### SV4

The chain's failure attribution:
- **PRIMARY (HIGH confidence):** edge-cases inquiry's critique stage failed to test principle-application correctness. The 8 dimensions did not include a check for whether each routing decision applied the inherited principle correctly. The substance-axis prosecution missed the internal contradiction (docstring vs routing).
- **PRIMARY (HIGH confidence):** edge-cases inquiry's sensemaking SV6 locked in the misrouting without testing against the existing 8-axis pattern. Frame-exit Completeness perspective fired but on the wrong axis.
- **CONTRIBUTORY (MED confidence):** chunking finding's principle was specifically anchored, allowing downstream over-generalization. Sharpening would have helped but is not the sole cause.

---

## Phase 4 — Degrees-of-Freedom Reduction

**Variables fixed:**
- Failure attribution: mixed (per LOOP_DIAGNOSE allowance), primary at edge-cases sensemaking SV6 + edge-cases critique; contributory at chunking principle articulation.
- Maintenance candidate count: 2 strong (MC1 substance-axis sub-axis; MC2 comparative-pattern perspective) + 1 contributory (principle sharpening, gated).
- Conversation correction status: comparative evidence (NOT ground truth). Independently verified via Frame-exit Completeness perspective applied to Group α membership-types.

**Eliminated:**
- "Single-stage failure" attribution.
- "Meta-loop framework structurally incapable" attribution.
- Broad rewrites of any spec.

**Viable paths (from 6 considered articulations):**
- Variant 2 (chain diagnosis): SURVIVES as the chosen scope.
- Variant 3 (critique-stage-focused): SURVIVES as PRIMARY hypothesis.
- Variant 4 (principle-articulation): SURVIVES as CONTRIBUTORY hypothesis.
- Variant 6 (impure with constructive output): NOT primary deliverable but the corrected routing should land in finding's Open Questions or Next Actions per WHY-axis `practical-application-now`.

### SV5

Solution space organized as 3 failure hypotheses + 2 strong maintenance candidates + 1 gated contributory candidate + diagnostic verdict ACTIONABLE.

---

## Phase 5 — Conceptual Stabilization

**Accommodation trigger check:** Did perspectives produce destabilizing patches? Frame-exit Completeness produced major insight (Group α membership conflated 3 referent types); other perspectives reinforced and refined. No destabilization. Accommodation NOT fired.

### SV6 — Stabilized model

**The loop chain failed at edge-cases sensemaking SV6 (PRIMARY) and edge-cases critique (PRIMARY), with chunking finding's principle articulation as a CONTRIBUTORY weakness. The smoking gun is an internal contradiction in the edge-cases finding's P3 docstring ("Refines A3") vs its routing (to SD) — visible to any substance-axis prosecution that applied the candidate's own claims against itself. The conversation correction used a comparative-pattern test (against A1/A2/A3) that was available to the loop and not applied. Two maintenance candidates with concrete evaluation gates: (MC1) substance-axis sub-axis sharpening in td-critique to apply candidate's own internal claims against its own decision; (MC2) a sensemaking perspective that explicitly compares routing decisions against the existing pattern of routed fields in the target schema. Both are testable on the next bulk-edge-case inquiry.**

### SV6 vs SV1 delta

SV1 framed the failure as ambiguous-chain (where did the misrouting come from?). SV6 reframes: the misrouting was locked in at edge-cases sensemaking SV6 (concrete locus), not caught by critique (concrete dimension gap), with chunking-principle-under-sharpening contributory; two specific maintenance candidates with evidence-based evaluation gates emerge.

---

## Telemetry

- Perspective saturation: 8 perspectives; Frame-exit Completeness produced major insight (Group α conflation); convergence by SV3.
- Ambiguity resolution: 5 identified, 5 resolved (4 HIGH + 1 MED).
- SV delta: substantial.
- Anchor diversity: 8 A-anchors + 4 constraints + 4 key insights + 2 structural points + 3 foundational principles + 5 meaning-nodes.

### Failure-mode check
- Status Quo Bias: NO — chunking principle was independently re-tested, not protected because it's prior.
- Premature Stabilization: NO — SV2→SV3 added Frame-exit Completeness insight.
- Anchor Dominance: NO — multiple anchors load-bearing.
- Perspective Blindness: NO — uncomfortable Frame-exit Completeness perspective applied.
- Clean Resolution Trap: NO — each ambiguity has counter + structural why-counter-fails.
- Self-Reference Blindness: PARTIAL — the subject IS the loop framework itself. Mitigated by treating chunking finding's principle as inherited commitment under formal re-test (not as truth), and by treating conversation correction as comparative evidence not ground truth. LOOP_DIAGNOSE's protocol exists to handle this exact case.

### Verdict

**PROCEED to Decomposition.**

Per LOOP_DIAGNOSE: diagnostic substrate is sufficient for ACTIONABLE verdict; two maintenance candidates have concrete shapes and evaluation gates; attribution is documented as mixed (PRIMARY edge-cases sensemaking + critique; CONTRIBUTORY chunking principle); conversation correction handled as comparative evidence per guardrails.
