# Sensemaking — Why the errors are possible: the un-invoked 3-Pass method

## User Input

`_branch.md`. Warm-settled anchor: the comprehend-first / semantic-priority ordering is PRESENT-AS-PRINCIPLE, ABSENT-AS-PROCEDURE. Inputs: articulate_simple.md, surfacing.md (the decisive SKILL locations), articulate_warm.md (the non-severe content-conflict = locus-refinement). Resolve two forks (this-vs-prior; the locus) + two rivals (is it just fluency-bias re-told? could the fix fail on supra-sentential granularity?). Save to `sensemaking.md`.

---

## SV1 — Baseline Understanding

Taken at face value: the harmony layer did the translation without semantic priority, and the SKILL is missing an explicit "comprehend the meaning first, then generate under the harmony nudge" instruction. (The user's framing, accepted as stated.)

---

## Phase 1 — Cognitive Anchor Extraction

**Constraints**
- **C1** — `harmony_layer.md` Pass-1: *"Meaning Lock: Translate every sentence with strict semantic fidelity. No meaning added, removed, or altered… This is the foundation that cannot be violated."* Semantic priority is a STATED hard constraint.
- **C2** — `harmony_layer.md` Pass-3: *"you may change HOW a meaning is expressed, but never WHAT meaning is expressed."* Harmony is constrained to be semantics-preserving.
- **C3** — `translation_principals.md` line 16: *"comprehensation is essentially a two-step process: generate interpretation from deep comprehension first, then validate against formal linguistic rules."* The comprehend-first ordering, stated as principle.
- **C4** — `SKILL.md` Step 5 (the only executable workflow): *"produce the translation. Apply: [config · policies · principles · harmony Tier 1-4 · notes]."* One motion, flat bag, no ordered passes.
- **C5** — `SKILL.md` Step 5 line 78 imports `harmony_layer.md` ONLY as *"the harmony-layer Tier 1-4 preservation policy."* It never invokes the 3-Pass method.
- **C6** — `schemas.py` `PipelineConfig` has no stage/pass ordering (chunking + parallelism + output only).

**Key Insights**
- **K1** — The user's architectural model (harmony on top of locked semantics) is EXACTLY what `harmony_layer.md` describes. The user is not proposing something new — they are re-describing the SKILL's own stated design. The "should" in their question is already the SKILL's "should."
- **K2** — The ordering exists as PRINCIPLE (≥3 places) but not as PROCEDURE (no workflow step runs it). Same declarative/procedural shape as the prior finding, but at a *different locus* — the ordering/priority, not the verification checks.
- **K3** — The precise mechanism: `harmony_layer.md` **double-serves** as (a) a 3-Pass METHOD (Meaning Lock → Harmony Map → Target Reconstruction — a procedure) and (b) a Tier 1-4 PRESERVATION POLICY (what to preserve/sacrifice — a priority-list). `SKILL.md` Step 5 wires ONLY (b) and ignores (a). The procedure that encodes the ordering is orphaned because the workflow imports the file for its *policy*, not its *method*.
- **K4** — "harmony without semantic priority did the translation" is imprecise: harmony did not OVERRIDE semantics (it is designed subordinate — C2, and Tier-1 = "meaning IS carried by this harmony"). Rather, because the 3-Pass never ran as steps, meaning-fixing and harmony-shaping happened in ONE fluent motion — there was never a locked-meaning artifact for harmony to operate "on top of." The layers collapsed not because harmony won, but because the procedure that separates them was never invoked.
- **K5** — This DEEPENS the prior finding. Prior: "the 3-Pass ran in spirit as one motion" (the symptom). This: WHY did it run as one motion? — because `SKILL.md` Step 5 never invokes the 3-Pass; it only pulls the Tier list. The prior named the symptom; this names the structural cause.

**Structural Points**
- **S1** — TWO gaps, ONE cause. Because Step 5 doesn't run the 3-Pass as discrete steps: (a) no meaning-lock-FIRST gate (this inquiry's locus — pre/during generation); (b) no target-reconstruction CHECK gate (the prior inquiry's locus — post-draft). One un-invoked procedure → both gates missing.
- **S2** — `harmony_layer.md`'s internal layout: the 3-Pass method is at the TOP (a short framing); the Tier 1-4 list is the BULK. `SKILL.md` line 33 describes the file as "cause-effect chains, istilzam chains, Tier 1-4 preservation policies" — the workflow's own mental model of the file is the Tier list; the method at the top is invisible to it.
- **S3** — Fix locus options: (a) wire the 3-Pass into `SKILL.md` Step 5 as ordered gates; (b) hoist a meaning-first step into the workflow; (c) restructure `harmony_layer.md` so the method isn't buried under the policy. All target the PROCEDURE/WIRING, not the principle.

**Foundational Principles (to test)**
- **F1** — (assumed) "A described procedure in a read reference file will be followed." Suspect FALSE: reading `harmony_layer.md` loads the 3-Pass into context, but the WORKFLOW frames the task as "produce the translation, applying the Tier list." The reader executes the *workflow's* framing, not a method buried in a file imported for a different purpose. The workflow's "produce" instruction overrides the reference's "three passes" description.
- **F2** — (assumed) "Semantic-priority is just the prior fluency-bias story re-told." Suspect PARTIALLY FALSE — tested at Ambiguity 1 / rival (a).

**Meaning-Nodes:** **M1** principle-procedure gap · **M2** method-vs-policy double-service (workflow wires only the policy) · **M3** layer-collapse (no locked-meaning artifact → meaning + harmony decided in one motion) · **M4** one-cause-two-gates.

### SV2 — Anchor-Informed Understanding
The errors are possible not because harmony was given priority over semantics (it is designed subordinate) and not because the comprehend-first principle is missing (it is stated in ≥3 places), but because the PROCEDURE that would enforce meaning-first — `harmony_layer.md`'s 3-Pass — is never invoked by the workflow. `SKILL.md` Step 5 imports the file only for its Tier-list policy and says "produce the translation" in one motion, so meaning-fixing and harmony-shaping collapse into a single fluent pass with no locked-meaning foundation between them.

*Meta-inspection (H4 concept-names, H5 examples):* "principle-procedure gap," "method-vs-policy double-service," "layer-collapse" are grounded in literal text (the 3-Pass IS at the top of harmony_layer.md; Step 5 DOES import only the Tier list — line 78; the two-step principle IS line 16) — structural, not proxies. The 7 errors are motivating examples; the mechanism (procedure never invoked) is general, not error-specific (tested Phase 3).

---

## Phase 2 — Perspective Checking

- **Technical/Logical.** An LLM following `SKILL.md` Step 5 as written produces the translation in one motion, applying the Tier list as constraints. It never runs Meaning Lock as a separate pass because nothing tells it to — the 3-Pass sits in a file imported "for its Tier 1-4 preservation policy." Mechanically, the ordering cannot fire: no instruction says "first do Pass 1, produce the accurate-but-choppy version, THEN harmonize."
- **Human/User.** The user (SKILL owner) has correctly intuited that the meaning-first ordering failed. Their instinct is right; their locus-description is slightly off because they reasoned from the prior finding's summary, not from the `harmony_layer.md` text — they are, in effect, rediscovering their OWN design (the 3-Pass) and noticing it never ran. New anchor: the fix is to make the SKILL *execute a design it already contains.*
- **Strategic/Long-term.** If the SKILL's richest procedural asset (the 3-Pass, with Meaning Lock as "the foundation that cannot be violated") is orphaned — described but never invoked — then the SKILL's entire "harmony on top of locked meaning" architecture is decorative; every translation collapses the layers. Strategic fix: wire the method into the workflow so the architecture is actually executed.
- **Risk/Failure.** Risk of misdiagnosis: if the real cause were something else (LLM can't hold a locked-meaning artifact; the 3-Pass is impractical), wiring it in wouldn't help. → tested at Ambiguity 3 (rival b).
- **Resource/Feasibility.** Wiring the 3-Pass into Step 5 is a cheap edit. BUT running Meaning Lock as a LITERAL sentence-by-sentence separate artifact may be token-costly and may fight the supra-sentential harmony work. New anchor: the fix is "invoke the 3-Pass as ordered phases," but Pass-1 must be understood as producing a meaning-secured (possibly choppy) FOUNDATION, not a sentence-atomized final that harmony then can't touch.
- **Definitional/Internal-Consistency.** By the SKILL's OWN files there is a contradiction: `harmony_layer.md` + `translation_principals.md` say translation is a meaning-first 3-pass process; `SKILL.md` Step 5 says "produce the translation" in one motion and imports `harmony_layer.md` only for its Tier list. **The SKILL's stated method is not the SKILL's executed workflow** — the definition's stated purpose (layered, meaning-first) outruns its mechanism (flat produce). This is a SKILL deficiency, specifically a WIRING deficiency (guards against Status-Quo Bias — do not protect the workflow because it is the documented workflow).
- **Self-Reference (H8).** Evaluating my own SKILL + my own translation. External grounding throughout: the literal quoted text (Pass-1; Pass-3; translation_principals line 16; SKILL.md Step 5 lines 73-81; line 78 "the harmony-layer Tier 1-4 preservation policy"; line 33). The diagnosis rests on what the files literally say.
- **Phase/Calibration-State.** comprehenslate is early-stage: the declarative method (3-Pass) is mature; the workflow WIRING that would invoke it is not built. "Step 5 doesn't invoke the 3-Pass" is a calibration-appropriate finding about an un-operationalized method, not a permanent flaw.

*Meta-inspection (H1 candidate-set, H3 question-framing):* candidate causes = {procedure-never-invoked, method-vs-policy-mis-wiring, workflow-overrides-reference-framing, fluency-bias-retold, LLM-can't-hold-locked-meaning}. The first three are ONE thing: Step 5 frames the task as "produce + apply Tier list," which neither invokes the 3-Pass nor leaves room for it. Question reframed from the user's "harmony did the translation without semantic priority" to "the procedure that separates meaning from harmony was never invoked" — evidence-driven (harmony is designed subordinate), not premise-accepting.

### SV3 — Multi-Perspective Understanding
The errors are the mechanical consequence of `SKILL.md` Step 5 framing translation as a single "produce + apply-the-Tier-list" motion, which neither invokes `harmony_layer.md`'s 3-Pass method (where Meaning Lock / the ordering lives) nor leaves an execution point for meaning-first. The SKILL's stated method and its executed workflow contradict each other. The user's instinct is right; the locus is the method-vs-workflow wiring gap.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — FORK 1: does this SUPERSEDE / REFINE / COMPLEMENT the prior finding?
**Strongest counter-interpretation (SUPERSEDE):** this is a different, deeper cause (the procedure never runs) that makes the prior's "no post-draft checkpoint" a mere symptom — so it supersedes.
**Why it fails (structural):** the prior's core mechanism (fluency-first single pass; principles un-fired) is NOT wrong — it is the same phenomenon from the generation side. Both reduce to ONE structural cause: `SKILL.md` Step 5 doesn't run the 3-Pass as discrete gates. From that one cause follow BOTH (a) no meaning-lock-first gate (this inquiry) AND (b) no target-reconstruction/verification gate (prior). Supersede fails because the prior's fix — a post-draft check — *survives as Pass-3's gate*; it is not discarded, it is subsumed as one of the two gates the single fix restores.
**Confidence:** HIGH.
**Resolution:** this **REFINES + COMPLEMENTS** the prior. One shared cause (un-invoked 3-Pass) → two missing gates (meaning-lock-first + reconstruction-check). The prior found gate (b); this finds the deeper cause and gate (a).
**Fixed:** not a rival to the prior — the deeper layer + the complementary gate. **No longer allowed:** treating "no checkpoint" and "no meaning-first ordering" as competing diagnoses. **Depends:** the fix (invoke the whole 3-Pass) delivers both gates at once. *(This also resolves rival (a): semantic-priority is NOT just fluency-bias re-told — it adds the pre-generation gate + the deeper cause.)*

### Ambiguity 2 — FORK 2: is the locus "harmony without priority / missing instructions," or "un-invoked procedure"?
**Strongest counter-interpretation:** maybe harmony DID override semantics — Step 5 imports the harmony Tier list but no "lock meaning first" step, so harmony-preservation was the operative instruction and meaning-first wasn't; functionally "harmony given priority."
**Why it fails (structural):** even the imported Tier list is explicitly meaning-subordinate — Tier-1 = "meaning IS carried by this harmony"; the hard constraint = "Anything that changes semantic content is forbidden." What Step 5 imported still declares meaning-primacy. The translator was not told "prefer harmony over meaning"; they were told "produce the translation, preserving these meaning-carrying harmony features." The failure is not prioritization; it is that no STEP first produced a locked-meaning artifact, so meaning-fixing and harmony-shaping happened simultaneously — and in that simultaneity, fluency captured the word-choices. The counter's grain of truth (Step 5 imports the policy but not a "lock meaning first" step) IS the un-invoked-procedure point, not "harmony given priority."
**Confidence:** HIGH.
**Resolution:** the locus is **UN-INVOKED PROCEDURE** (the 3-Pass, esp. Meaning Lock as a produced-foundation step) — not missing-principle, not harmony-over-semantics. The user's instinct (meaning-first wasn't operative) is correct; the mechanism is "no step produced the locked-meaning foundation, so the layers never separated."
**Fixed:** locus = method-vs-workflow wiring gap. **No longer allowed:** "the principle is missing" (≥3 files) or "harmony is designed to override" (designed subordinate).

### Ambiguity 3 — RIVAL (b): could the fix fail because Meaning Lock is sentence-level while harmony is supra-sentential?
**Strongest counter-interpretation:** Pass-1 says "Translate every sentence… the accurate but choppy version" — a sentence-by-sentence literal pass. Run rigidly, it yields a sentence-atomized draft, and then Pass-3's supra-sentential harmony (ring composition, escalation) must reassemble across sentences. The prior inquiry found fine-granularity operations DAMAGE the supra-sentential harmony that succeeds. So literally wiring "translate every sentence separately first" might fight the harmony work.
**Why it (largely) fails — the 3-Pass already anticipates this (structural):** Meaning Lock's PURPOSE is to secure meaning (comprehension + no add/remove/alter) as an *"accurate but choppy" FOUNDATION* — explicitly a transient raw-material stage. Pass-3 is licensed to "reorder clauses, adjust sentence length, use the target's cohesion devices" as long as meaning is preserved. So the sequence is BY DESIGN: Pass-1 secures meaning (possibly choppy, transient); Pass-3 harmonizes supra-sententially ON TOP without changing meaning. The granularity risk is real only if the workflow forced Pass-1's choppy output to be FINAL — which Pass-3 exists precisely to prevent. The prior inquiry's granularity constraint still applies to the *check* operations (stay word/clause-granular; don't force permanent sentence-chopping), but the *foundational* Pass-1 being sentence-level is fine because its choppiness is transient.
**Confidence:** HIGH that the fix is viable; MED on the exact operationalization.
**Resolution:** the fix (invoke the 3-Pass as ordered phases) is viable and does NOT inherently conflict with supra-sentential harmony — because Pass-1 is a transient meaning-secured foundation and Pass-3 is the supra-sentential harmonizer. **Caveat:** the operationalization must produce a genuine meaning-first commitment (an intermediate the harmony pass respects) and keep checks word/clause-granular. **Open sub-question:** real intermediate-artifact vs simulated-sequence within one context window (→ Innovation).

### Ambiguity 4 — does the semantic-priority framing add anything beyond the prior? (rival a, sharpened)
Resolved via Ambiguity 1: **YES.** It adds (i) the deeper structural cause (un-invoked 3-Pass, of which "no post-draft check" is one consequence); (ii) the pre/during-generation gate (meaning-lock-first) the prior didn't emphasize; (iii) a DIFFERENT, cheaper fix shape — the prior proposed *adding a new verification pass*; this proposes *invoking an existing method* (the 3-Pass), which delivers both gates by wiring what is already written. Additive, not redundant. **Confidence:** HIGH.

### SV4 — Clarified Understanding
The errors are possible because `SKILL.md` Step 5 frames translation as a single "produce + apply-the-Tier-list" motion that never invokes `harmony_layer.md`'s 3-Pass method; the comprehend-first / meaning-lock ordering exists as principle (≥3 files) but has no execution point, so meaning-fixing and harmony-shaping collapse into one fluent pass with no locked-meaning foundation between them, and in that collapse fluency captures the word-choices. This REFINES + COMPLEMENTS the prior finding (one shared cause → both the missing meaning-lock-first gate and the missing post-draft check). The user's instinct is right; the locus is the method-vs-workflow wiring gap. The fix (invoke the 3-Pass) is viable and cheaper than authoring new checks, with a granularity/intermediate-artifact caveat.

---

## Phase 4 — Degrees-of-Freedom Reduction

**Now fixed:** the ordering is present-as-principle/absent-as-procedure; the mechanism is the un-invoked 3-Pass (Step 5 imports the Tier-list policy, not the method); harmony is designed subordinate (not the culprit-by-priority); this refines+complements the prior (one cause, two gates); the fix invokes an existing method; a granularity/intermediate caveat applies.
**Eliminated:** "the principle is missing" (≥3 files); "harmony was given priority over semantics" (designed subordinate); "this supersedes the prior" (the prior's gate survives as Pass-3's); "semantic-priority is just fluency-bias re-told" (adds a locus, a cause-depth, a cheaper fix); "the config/schema values are wrong" (confirmed-absent).
**Viable remaining paths (for Innovation/Critique):** fix-designs that invoke the 3-Pass as ordered phases in `SKILL.md` Step 5 and/or restructure `harmony_layer.md` so the method isn't buried under the policy; the real-intermediate-artifact vs simulated-sequence question; OUTPUT-REACH stays open.

### SV5 — Constrained Understanding
Solution space is constrained to **wiring-the-existing-3-Pass-into-the-workflow** designs (invoke the method Step 5 currently ignores; optionally un-bury it in harmony_layer.md), grounded in "the method exists but the workflow imports only the policy."

---

## Phase 5 — Conceptual Stabilization

*Accommodation check (H6):* the model did not require repeated patching — every perspective reinforced the "un-invoked procedure / method-vs-policy wiring gap" structure. Stable, not force-fit.

### SV6 — Stabilized Model

**The errors are possible because the SKILL's executed workflow contradicts its stated method.** `harmony_layer.md` describes a 3-Pass method with Meaning Lock ("the foundation that cannot be violated") as Pass 1, and `translation_principals.md` states "comprehend first, then validate" — so the comprehend-first / semantic-priority ordering the user describes is **PRESENT AS PRINCIPLE** in ≥3 places. But `SKILL.md` Step 5 — the only executable workflow — frames translation as a single *"produce the translation. Apply: [flat bag]"* motion, and it imports `harmony_layer.md` **ONLY for its Tier 1-4 preservation policy, never invoking the 3-Pass method.** The method that encodes the ordering is orphaned: `harmony_layer.md` double-serves as both a METHOD (the 3-Pass) and a POLICY (the Tier list), and the workflow wires only the policy. So there is no execution point at which a locked-meaning foundation is produced before harmony-shaping; meaning-fixing and harmony-shaping **collapse into one fluent motion**, and in that simultaneity fluency (the prior finding's named driver) captures the word-choices — producing the 7 errors.

**Was the user right?** The **instinct — YES**: semantic priority was not operative at render time, and this is a deeper generative cause than "no post-draft checkpoint." The **locus-description — REFINED**: not "the instructions are missing" (the comprehend-first principle is stated in ≥3 files) and not "harmony was given priority over semantics" (harmony is designed strictly subordinate — Pass-3 changes HOW not WHAT; Tier-1 = "meaning IS carried by this harmony"). The real locus is the **method-vs-workflow WIRING gap**: the procedure that would enforce meaning-first is described but never invoked.

**Relationship to the prior finding: REFINES + COMPLEMENTS (not supersedes).** One shared structural cause — `SKILL.md` Step 5 doesn't run the 3-Pass as discrete gates — produces BOTH the missing meaning-lock-FIRST gate (this inquiry, pre/during generation) AND the missing target-reconstruction CHECK gate (the prior inquiry, post-draft). The prior found one face; this finds the deeper cause and the complementary face.

**The fix:** invoke the existing 3-Pass as ordered phases in the workflow (Meaning Lock produces a meaning-secured foundation → Harmony Map → Target Reconstruction harmonizes on top), rather than authoring new machinery. Cheaper than the prior's "add a new verification pass" (it wires a method already written) and delivers both gates at once. **Caveat** (rival b + prior granularity constraint): Pass-1's meaning-secured draft is a TRANSIENT "accurate but choppy" foundation; Pass-3 harmonizes it supra-sententially without changing meaning; the operationalization must produce a genuine meaning-first commitment the harmony pass respects, and checks stay word/clause-granular.

**Difference from SV1:** SV1 accepted the user's framing (harmony did the translation without semantic priority; instructions missing). SV6: the principle is NOT missing (≥3 files); harmony is NOT the culprit-by-priority (designed subordinate); the cause is an un-invoked PROCEDURE (the workflow imports harmony_layer.md's policy but not its method); this REFINES + COMPLEMENTS the prior (one cause, two gates); and the fix invokes an existing method rather than authoring a new one.

**Open ambiguities (flagged, not dropped):**
- OUTPUT-REACH — deliver the diagnosis only, or also build the wiring (→ Critique / user).
- Real intermediate-artifact vs simulated-sequence — how to make the LLM actually produce a meaning-first foundation the harmony pass respects, within one context window (→ Innovation).
- harmony_layer.md restructure — should the 3-Pass method be separated from the Tier-list policy so the workflow can't import one without the other? (→ Innovation)

**Saturation telemetry:** perspectives produced new anchor TYPES — Definitional (the method-vs-workflow internal contradiction) and Feasibility (the granularity/transient-foundation caveat). SV1→SV6 delta large. Anchors span all 5 types × 8 perspectives. Ambiguity-resolution ratio 4/4 resolved + 3 flagged OPEN (OUTPUT-REACH, intermediate-artifact, restructure). No Anchor-Dominance (the model rests on two independent pillars — the literal Step-5-imports-only-the-Tier-list fact AND the principle-stated-in-≥3-files fact; removing either still leaves a wiring gap). Self-reference externally grounded throughout.
