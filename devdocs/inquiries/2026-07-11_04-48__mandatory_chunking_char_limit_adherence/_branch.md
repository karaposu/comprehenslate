# Branch: Mandatory Chunking & the Character-Limit Adherence Hypothesis

## Source Input

```text
chunking should be mandatory maybe, i think there is a limit of how much AI session can follow rules and do the translation, above certain amount of character (around 3500 charrs for claude opus 4.8 max and proabbly lower for smaller AI models) it starts skipping insturcitons  maybe.
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-07-11_04-48__mandatory_chunking_char_limit_adherence/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** [i1]
- **Verdict:** MED-FLAG
- **Flagged conditions:** (1) evaluate-vs-design late-split (mechanism-evaluation bundled with intervention-design; carried as one item, decomposition partitions); (2) variable-identity fork (source char-count vs total context load vs active-rule-count — the real driver may be mis-described); (3) rival-vs-complementary stance (does input-size-decay compete with or stack on the un-wired-3-Pass root cause); (4) don't over-index on the exact "3500". No structural LAYER 1 fires (Mode-2 boundary-approached only).

## Question

**Literal (MultiDepth, non-contaminating):** *"Chunking should maybe be mandatory; I think there's a limit to how much an AI session can follow rules and translate — above a certain character count (around 3500 for Claude Opus 4.8 max, probably lower for smaller models) it maybe starts skipping instructions."*

**What kinds of ask this carries (MQ1 verdict-axis — preserved as ambiguities):**
- `validate-the-mechanism` — is the claim true: does instruction-adherence degrade as input grows, and is ~3500 chars the right *kind* of threshold at all?
- `decide-the-policy` — should chunking be **mandatory** in the SKILL (vs optional / advisory / situational)?
- `design-the-intervention` — *how* to chunk (chunk size; pipeline placement; cross-chunk structure handling)?
- `correct-the-variable` — is *raw source character-count* the right measure, or a proxy for total context load (SKILL + config + source together) / instruction complexity / count of simultaneously-active rules?
- `reach` (inherited gate) — evaluate-only vs +design vs +apply-the-SKILL-edit.

**Plausible action-endpoints (MQ3 intent-axis, WHAT — preserved as ambiguities):**
- `reduce-the-error-rate` — chunking as another lever on the chain's driving goal.
- `raise-instruction-adherence-specifically` — keep the model under its rule-following capacity (a narrower endpoint than error-rate).
- `add-a-mandatory-pipeline-stage` — operationalize chunking as a required Step-5 step.
- `establish-an-input-budget-principle` — a standing "keep active load under a per-model ceiling" design rule.

## Goal

**Deliverable shape (Deconstruct tuple):**
- **deliverable:** an evaluation-plus-conditional-design — a verdict on the hypothesis (is input-size adherence-decay real & distinct?) + IF-yes a design (mandatory chunking: whether, and how, reconciling *chunk-small-for-adherence* against *keep-whole-for-cross-chunk-fidelity*).
- **kinds:** diagnostic/evaluative judgment + design artifact (chunk policy, pipeline placement) + prior-reconciliation (rival-or-complementary to the un-wired-3-Pass) + commitment re-test of the priors.
- **bounds:** the comprehenslate SKILL and its translation pipeline; gated reach (no edits without authorization); Opus-4.8 **plus weaker models** (portability in-frame per "lower for smaller models").

**Motivations a good answer might serve (MultiDepth WHY-axis — preserved as ambiguities):**
- `reduce-translation-errors` — the user suspects input-size is a (or the) cause of the observed errors.
- `cross-model-robustness` — "lower for smaller models" signals a portability motive: keep load under whatever ceiling a given model has, so the SKILL survives on weaker models.
- `find-a-mechanical-lever` — chunking is structural and model-judgment-independent; attractive for the same reason the chain trusts mechanical checks over fallible in-context rule-following.
- `explain-vs-fix` — is the user seeking the **diagnosis** ("overload is why") or the **remedy** ("so chunk")?

**Context downstream consumers need (MQ2 context-need axis — preserved as ambiguities):**
- **verdict:** does the SKILL currently chunk / does Step 5 process whole texts? · is ~3500 empirically grounded or a guess? · were the 7 diagnosed errors *adherence-decay* symptoms or *3-Pass-not-wired* symptoms?
- **kinds:** LLM context-length-effect knowledge; the SKILL's current long-source handling; the corpus's long-span structural features (escalation-chain, ring-composition, havuz-convergence, cause-effect arcs) that can straddle chunk boundaries.
- **stance:** is input-size-decay a **RIVAL** root cause (competes with un-wired-3-Pass) or a **COMPLEMENTARY** independent factor (stacks on it)? — determines whether chunking *replaces* or *supplements* the prior fix.

**Explicit exclusions (MQ4 boundary-axis):**
- `reach-bounded` (extrinsic, from the chain's standing gate) — evaluate + design only; applying the SKILL edit is gated on explicit authorization.
- `not-exact-threshold-pinning` — 3500 is illustrative; the in-scope question is whether the *kind* of effect holds, not the exact number.

## Considered Articulations

**Item i1 — the mandatory-chunking proposal + its character-limit rationale:**
1. **(mechanism-validation lean)** Evaluate whether adherence genuinely degrades as input/context size grows — and whether raw source char-count (~3500) is the right variable or a proxy for total context load — *before* deciding any intervention; treat "mandatory chunking" as the tentative remedy conditional on that verdict.
2. **(policy-decision lean)** Decide whether the SKILL should make source-chunking a **mandatory** pipeline step given the adherence-decay hypothesis, and reconcile that against the whole-draft structural-fidelity checks (escalation-chain, ring-composition, havuz-convergence) that need the whole text.
3. **(design lean)** Design how mandatory chunking would work — chunk size, placement relative to the (un-wired) 3-Pass, cross-chunk structure preservation — assuming the hypothesis holds.
4. **(reframe-the-variable / contrarian)** Test whether the real driver is not *source* char-count but **total active load** (SKILL + config + source together) or instruction-complexity/active-rule-count — in which case chunking the source is a partial fix and the better lever may be reducing simultaneously-active instructions.
5. **(rival-vs-complementary lean)** Determine whether input-size-decay is a **rival** root cause to the un-wired-3-Pass (competing explanation for the 7 errors) or a **complementary** independent factor that stacks on it — and what that implies for replace-vs-supplement.
6. **(cross-model-robustness lean)** Evaluate mandatory chunking as a cross-model-robustness measure — a mechanical, judgment-independent safeguard that keeps active rule-load under whatever adherence-ceiling a given model has, so the SKILL degrades gracefully on smaller models.

## Scope Check

**IN-scope (from Deconstruct bounds):** evaluating the adherence-decay mechanism + its true variable; the rival-vs-complementary reconciliation against the priors; designing (conditionally) mandatory chunking incl. the cross-chunk-fidelity tension; cross-model portability; gated reach up to design.

**OUT-of-scope (from MQ4 exclusions):** applying the SKILL edit without explicit authorization; precisely validating "3500" as an exact numeric threshold.

**Question covers goal:** YES — the question's five MQ1 asks (validate / decide / design / correct-variable / reach) span the goal's evaluation-plus-conditional-design deliverable. The one widening the articulation forces into view (and the Question retains) is the **variable-identity** axis: the user said "character count," but the goal must not silently assume *source*-char-count is the driver — the evaluation has to test total-load and active-rule-count as rivals to the named variable.

**Specific-vs-pattern check:** the user names a specific number (~3500 for Opus 4.8) and specific models. Per default, address the **broader pattern** (does input/load size degrade instruction-adherence, and what is the right variable + intervention) rather than only the specific 3500-on-Opus point — the doubled "maybe" and "probably lower for smaller models" explicitly generalize beyond the single number. The specific figure is treated as an illustrative anchor, not the scope.

## Layer Commitment

The proposal targets the SKILL (a framework artifact) — specifically it would add a **mandatory chunking step** to the translation pipeline. Layer required.

**Primary layer: PROCESS.** The core of the proposal is a procedure — "chunk the source before/within the translation pipeline, mandatorily" — i.e., a new required *step* with a placement in the run sequence and an interaction with the (un-wired) 3-Pass and the post-draft checks. The mechanism-evaluation half ("does adherence degrade under load") is a *diagnostic precondition* about process-behavior-under-load, not itself an artifact-layer edit, and it feeds the process question.

**Other layers considered, out of scope for this run:**
- **Structural** (where a chunk-policy / chunk-size spec would live in the SKILL files, e.g., a field in schemas.py or a section in SKILL.md) — secondary/inherited; it only matters *after* the process question (mandatory? how placed?) resolves. Sequential plan: if the process verdict favors mandatory chunking, a follow-on structural inquiry would site the chunk policy.
- **Meaning** (what "chunking" fundamentally *is* as a translation operation) — not in question; the concept is clear.

## Synthesis Trigger

This inquiry consumes prior inquiry outputs as inputs and inherits commitments it must re-test (it advances a possibly-*rival* causal hypothesis to the chain's established root cause). CONCLUDE will require an `## Inherited Commitments Re-test`.

- `devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md` — commits to the **un-wired-3-Pass as THE root cause** of the 7 errors (two proximate gates downstream of one cause). This inquiry must test whether input-size-decay is a **rival** that demotes this root-cause claim, or a **complementary** independent factor — the central re-test.
- `devdocs/inquiries/2026-07-11_01-09__firing_time_categories_for_principles/finding.md` — commits to the **config-independent mechanical spine + config-derived agenda, tiered reliability**, and that the whole-draft structural-fidelity checks need the whole draft. Chunking directly stresses this: if the source is chunked, the whole-draft checks (escalation-chain, ring-composition, havuz-convergence) lose their whole. Re-test the interaction.
- `devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md` — commits to the **base 7-error / one-fluency-first-pass / no-checkpoint** diagnosis. Re-test whether "overload above a char threshold" better (or additionally) explains the same 7 errors.
