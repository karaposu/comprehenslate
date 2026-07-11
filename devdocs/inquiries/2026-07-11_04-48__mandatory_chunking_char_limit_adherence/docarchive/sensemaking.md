## User Input

Sensemaking over `_branch.md` + surfacing (DF1-DF8) + warm (non-severe content-conflict re-anchor). Resolve with evidence: (1) THE PIVOT — is instruction-adherence-degrades-with-load real & distinct from the un-wired-3-Pass, and is the variable source-char-count / total-context-load / active-rule-count?; (2) THE FLIP-ON POLICY — what "mandatory" rightly means given the dormant apparatus + conditional-by-construction budget; (3) THE WHOLE-SPAN REMAINDER — can chunking coexist with the whole-draft checks + Pass-2 whole-text Harmony Map + whole-passage havuz/ring/arc. Test rivals: redundancy (design exists), over-engineering (harms short texts), deep-rival (the real lever is active-load/staging not source-chunking). Full input preserved in `_branch.md` Source Input + the warm/surfacing artifacts.

---

# Structural Sensemaking — Output

## SV1 — Baseline Understanding

The user proposes making chunking mandatory because AI instruction-adherence seems to degrade above ~3500 source characters. Initial read: a plausible reliability heuristic — smaller inputs, better rule-following — that needs a design (chunk size, placement, cross-chunk structure). Treat as evaluate-plus-design.

---

## Phase 1 — Cognitive Anchor Extraction

**Constraints:**
- C1 — Tier 1-2 harmony preservation is a HARD constraint (harmony_layer.md): a chunker that splits a Tier-1 chain is rejected. (DF4)
- C2 — Pass 2 (Harmony Map) is inherently whole-text: "analyze the ORIGINAL TEXT's inter-sentence relationships." It cannot be built from isolated chunks. (DF4)
- C3 — the model-facing SKILL.md currently has NO chunking; the engine-layer PipelineConfig chunking apparatus is dormant (default-off) and unbuilt beyond the knobs. (DF1)
- C4 — reach-gated (evaluate/design only, no SKILL edits without authorization); the ~3500 number is illustrative, not to be pinned (DF8).

**Key Insights:**
- K1 — the existing chunking design targets a 200K CAPACITY budget; the user's ~3500 chars ≈ 875 tokens is ~0.4% of that → the user's driver is NOT capacity; it is a much-smaller-scale ADHERENCE claim. (DF3)
- K2 — at translate-time the load = a LARGE FIXED instruction stack (SKILL + 7 reference files + ~80 principles + Tier 1-4 + 8 axes) + the source + the generated output; source-char-count is one term among several. (DF6)
- K3 — chunking the source bounds the per-unit TRANSFORMATION working-set (source-unit read + output generated + local coherence tracked) but leaves the fixed instruction load and the active-rule-count untouched. (DF6)
- K4 — the existing design's asymmetric-failure rule ("over-chunk under uncertainty") and A6-cascade ("mandatory harmony-aware when A6≥light") already lean the user's direction. (DF7)

**Structural Points:**
- S1 — two levers reduce adherence load: (i) chunk the source/generation (transformation-working-set); (ii) stage/prune the instructions (fixed + rule-count load — the staging 04-12 lever). They address DIFFERENT load components.
- S2 — the pipeline has three natural layers: whole-text comprehension + harmony map (before) → generation (where chunking lives) → whole-draft assembly + structural check (after).
- S3 — the chunking apparatus is split-placed (SourceDescriptor / PipelineConfig / TranslationConfig) with a hidden hybrid harmony-aware mechanism (DF2).

**Foundational Principles:**
- P1 — LLM instruction-following degrades as total cognitive load + output length + simultaneously-active constraints grow (a real, well-grounded tendency; "lost in the middle," constraint-satisfaction decay).
- P2 — mechanical/structural interventions (chunking) are model-judgment-independent; attractive for the same reason the chain trusts mechanical checks (feedback_translation_verification_pass memory).

**Meaning-Nodes:** adherence-under-load · transformation-working-set · budget-gated-always-on · whole-text bracket · the two load levers (chunk vs stage).

### SV2 — Anchor-Informed Understanding

The proposal is not "introduce chunking" (it is designed + dormant) and not primarily "about source-char-count." It is a claim on the LOAD-MAGNITUDE axis of adherence, whose real variable is the per-unit transformation working-set, and whose remedy (chunking the generation) is one of two load levers. The question sharpens to: is that axis real & distinct, what should "mandatory" mean given the dormant conditional apparatus, and can chunked generation coexist with the whole-text obligations.

*(Meta-Inspection H4/H5: "transformation-working-set" is a real structural distinction — the VARIABLE load [source-unit + output + local tracking] vs the FIXED load [instruction stack] — not a coined neologism; it maps to the user's "how much an AI session can follow rules and do the translation." The ~3500 figure [H5] is treated as an illustrative example of a pattern, not the whole problem, per the branch's specific-vs-pattern check.)*

---

## Phase 2 — Perspective Checking

**Technical / Logical.** Chunking bounds the transformation working-set per generation call, which directly reduces omission-type errors (fewer clauses in view to drop) and constraint-tracking load. But each call still reloads the full fixed instruction stack — chunking does not reduce that. So chunking attacks a real and large component of adherence load (transformation), not the whole of it.

**Human / User.** The user's lived experience (they manually chunk at mesele level — DF2/chunk_types finding) is the evidence behind the instinct. Their "it starts skipping instructions" is a real observation of load-driven omission; their "~3500 chars" is an eyeball estimate of where they felt it. The instinct is trustworthy; the dial-reading is approximate.

**Strategic / Long-term.** If adherence-driven chunking flips the budget from capacity-scale (200K) to adherence-scale (much smaller), that is a large, durable change to how every translation runs — and it makes the (currently opt-in, dormant) apparatus a correctness-load-bearing default. Worth getting right; worth validating before flipping.

**Risk / Failure.** The dominant risk is the whole-span remainder: chunk too small and you can't preserve havuz/ring/arc/Pass-2. The existing design's failure-mode-10 ("cross-chunk reference unresolved") is only PARTIALLY mitigated. Chunking that ignores this trades adherence for harmony — swapping one error class for another.

**Resource / Feasibility.** The apparatus exists in schema; the mechanism is designed; the intake feeder is designed. So the feasibility cost is low for the ENGINE path — but the engine is unbuilt, and the model-facing SKILL.md has no chunking at all. Feasibility differs sharply by which layer you target (see Phase/Calibration-State below).

**Definitional / Internal Consistency.** Does "mandatory chunking" contradict the whole-text obligations (C2, C1)? Only if chunking is placed at the wrong layer. If chunking bounds GENERATION while whole-text comprehension/harmony-map (before) and whole-draft check (after) bracket it, there is no contradiction — the whole is preserved at the layers that need it. The apparent contradiction is a layer-confusion, not a real one.

**Phase / Calibration-State (REQUIRED — the rule is phase-dependent).** "Flip chunking on" means different things by project phase: in the CURRENT phase (SKILL.md is the only model-facing reality; the engine/PipelineConfig is unbuilt), mandatory chunking can only be a model-facing INSTRUCTION ("translate in units of ~N, snapping to structural/harmony boundaries; assemble; then run the whole-draft check"). In a LATER phase (the chunking engine + SourceDescriptor + intake are built), it is the PipelineConfig budget-gated policy the two 06-14 findings designed. The correct near-term default is the instruction-level version; the engine-level version is gated on the engine being built. Failing to state this phase-split would mis-scope the whole finding.

### SV3 — Multi-Perspective Understanding

Major shift: the contradiction between "chunk small" and "keep whole" is a LAYER-PLACEMENT question, not a real conflict — chunk the generation, bracket it with whole-text passes. And "flip chunking on" is PHASE-DEPENDENT — a model-facing instruction now, an engine policy later. The pivot (is adherence-under-load real & distinct) survives all perspectives: real (P1), distinct from the un-wired-3-Pass (load-magnitude vs method-structure), variable = transformation-working-set (K3), source-char-count an approximate proxy.

*(Meta-Inspection H2/H3/H7: H3 — the question's "should chunking be MANDATORY" pre-biases toward a yes/no on a crude "always-split"; reframed to "flip the dormant apparatus on as a budget-gated policy," which dissolves the crude binary. H7 — phase-dependence surfaced explicitly above. H2 — frame is translate-stage chunking; intake segmentation is the feeder [in scope as context], the engine layer is where the policy lives [in scope], cross-model budget [in scope]; no load-bearing referent excluded.)*

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — Is instruction-adherence-degrades-with-load REAL and DISTINCT from the un-wired-3-Pass? (THE PIVOT)

**Strongest counter-interpretation:** it is not distinct — the 7 errors were fully explained by the un-wired-3-Pass (meaning+harmony collapse in one motion), so "adherence-decay-under-load" is just that same failure re-described; adding a load story explains nothing new and chunking is a distraction from wiring the 3-Pass.

**Why the counter fails (structural grounds):** the two mechanisms operate on DIFFERENT axes and predict differently. The un-wired-3-Pass is a METHOD-STRUCTURE failure: meaning and harmony collapse because no ordered method separates them — this occurs *even in a two-sentence chunk* (order, not size, is the cause). Adherence-decay-under-load is a LOAD-MAGNITUDE failure: as the per-unit transformation working-set grows (more source clauses in view, longer output being generated, more simultaneously-tracked constraints), the probability of dropping a clause or losing a constraint rises — this scales *with size*, holding method fixed. They make different predictions: the method failure appears at all sizes; the load failure appears more at large sizes. A short chunk translated with the collapsed method still errs (method), but a long chunk errs MORE (load). Both are real; neither reduces to the other. Distinctness is structural, not stipulated.

**Confidence:** HIGH (the two mechanisms are separable on the size-dependence axis; grounded in the well-established load/instruction-decay tendency, P1).

**Resolution:** adherence-decay-under-load is REAL and DISTINCT (load-magnitude axis), COMPLEMENTARY to the un-wired-3-Pass (method-structure axis). The variable is the per-unit **transformation working-set** (source-unit + output + local tracking), for which source-char-count is an approximate proxy; the fixed instruction load and active-rule-count are NOT reduced by source-chunking. The ~3500 figure is an unvalidated, model-dependent estimate — real-in-kind, approximate-in-value.

**What is now fixed:** chunking attacks a genuine, distinct adherence axis; it does not dissolve into the 3-Pass.
**What is no longer allowed:** treating chunking as a rival to (or substitute for) wiring the 3-Pass; treating "3500 source chars" as the precise threshold or the sole variable.
**What now depends on this:** the flip-on policy (chunking is worth turning on because it addresses a real distinct axis) + the complementary relationship to 00-24.
**What changed in the model:** the inquiry's weight moves from "is chunking good" to "chunking is a real lever on the transformation-load component; how far on, and how bracketed."

### Ambiguity 2 — What does "mandatory" rightly mean? (THE FLIP-ON POLICY)

**Strongest counter-interpretation:** "mandatory" means always-split — chop every source into ~N-sized pieces unconditionally, because if adherence degrades with size, every text benefits from smaller units.

**Why the counter fails (structural grounds):** always-split harms short texts on two structural grounds: (i) a source already under the adherence budget gains nothing from splitting and pays the cross-chunk-consistency + boundary-drawing cost (parallel_mode's "terminology drift" risk); (ii) forcing boundaries into a small passage can cut a small-scale Tier-1 structure (C1) that would have been safe whole. The schema already encodes the correct alternative: `chunking_budget` set to a value means "chunk only what EXCEEDS the budget" (DF7) — conditional-by-construction. So "mandatory" as always-split is strictly dominated by "mandatory-policy, budget-gated split."

**Confidence:** HIGH (the conditional form is already in the schema and strictly dominates always-split).

**Resolution:** "mandatory" = flip the dormant apparatus ON as a **budget-gated, harmony-boundary-snapping, per-model-calibrated policy** — always-active as a policy, but only actually splitting when the unit exceeds an adherence-calibrated budget; short texts pass through whole; boundaries snap to structural/harmony units (existing `harmony-tier-aware`/`fixed-budget-with-snap` mechanisms) so a split never cuts a Tier-1 chain. The budget is empirical and per-model (the user's "lower for smaller models" → `chunking_budget:int` per-model).

**What is now fixed:** the policy shape (always-on, conditionally-splitting, boundary-snapping, per-model).
**What is no longer allowed:** always-split; a single fixed char threshold; a capacity-scale budget standing in for an adherence-scale one.
**What now depends on this:** the empirical calibration of the budget (a deferred MUST — no evidence yet, DF8); the cross-model budget map.
**What changed in the model:** "mandatory vs optional" dissolves into "always-on policy with a conditional gate" — the user's "mandatory" and "don't harm short texts" become compatible.

### Ambiguity 3 — Can chunking coexist with the whole-text obligations? (THE WHOLE-SPAN REMAINDER)

**Strongest counter-interpretation:** no — chunking fundamentally destroys the whole. Pass-2's Harmony Map needs the whole source; havuz/ring/arc span passages; the prior-01-09 whole-draft checks need the whole draft. If you chunk, the model never sees the whole, so these are impossible.

**Why the counter fails (structural grounds) — PARTIALLY:** the obligation and the chunking live at DIFFERENT layers, so bracketing dissolves MOST of the conflict. Sequence: (1) whole-text comprehension + Pass-2 Harmony Map run on the WHOLE source FIRST, producing a harmony blueprint; (2) chunked GENERATION (Pass-1 Meaning-Lock + Pass-3 Reconstruction per unit, load-bounded) consults that blueprint; (3) the whole-draft structural check (01-09) runs on the ASSEMBLED output LAST, when the whole exists again. The whole is seen where it is needed (comprehension + final check); only the generation is load-bounded. So chunking does NOT make the checks impossible.

**BUT the counter partially SURVIVES (Clean-Resolution-Trap corrective):** bracketing REDUCES the tension; it does not fully ELIMINATE it. Residual: when a single Tier-1 structure's span EXCEEDS the adherence-safe chunk size (e.g., a havuz convergence spanning 10K tokens, with an adherence budget near ~1K), the per-chunk generation must carry that structure's harmony-blueprint slice into EACH of the ~10 chunks to preserve it — which re-adds load, partly defeating the point. So very-long-span structures + a very-small adherence budget genuinely conflict at the margin. This is a real residual trade, not a clean victory: the budget must be set high enough that most Tier-1 structures fit within a chunk, which BOUNDS HOW SMALL the adherence budget can go. The adherence lever and the harmony lever therefore constrain each other — the budget is the negotiated point between them.

**Confidence:** HIGH on coexistence-by-bracketing for the common case; the residual (long-span-structure vs small-budget) is a genuine bounded trade, flagged not dissolved.

**Resolution:** chunking coexists with the whole-text obligations via LAYER SEPARATION (whole-text comprehension + harmony map BEFORE; chunked generation IN THE MIDDLE; whole-draft check AFTER) — which makes chunking architecturally ENTANGLED with the un-wired 3-Pass (Pass 2 is the whole-text bracket that makes safe chunking possible). The residual long-span-vs-small-budget trade sets a FLOOR on the adherence budget (it cannot go below the size of the Tier-1 structures it must not fragment).

**What is now fixed:** the three-layer sequencing; chunking entangled-with (not independent-of) the 3-Pass; a harmony-imposed floor on the budget.
**What is no longer allowed:** chunking as a standalone pre-step blind to the whole; an adherence budget set so low it fragments Tier-1 structures.
**What now depends on this:** the budget calibration must respect BOTH the adherence ceiling (small enough to help adherence) AND the harmony floor (large enough to not fragment Tier-1 spans).
**What changed in the model:** the "deepest tension" becomes a solved-in-the-common-case + bounded-trade-at-the-margin, with the budget as the negotiated middle.

### SV4 — Clarified Understanding

All three resolve. The pivot: real + distinct + variable-is-transformation-working-set. The flip-on: budget-gated-always-on, boundary-snapping, per-model. The remainder: coexist by bracketing (chunk generation, whole-text before + after), entangled with the 3-Pass, with a harmony floor on the budget. Chunking is a real lever on a real distinct axis — not redundant with the 3-Pass, not the crude always-split, not blind to the whole.

---

## Phase 4 — Degrees-of-Freedom Reduction — Rival Tests

**(a) REDUNDANCY rival — is this just the existing chunking design re-surfaced?**
PARTIALLY LANDS — and this is honest scoping, not a kill. The "HOW to chunk" (mechanism, granularity ladder, split-placement, hybrid harmony-aware) is comprehensively designed already (DF2); on that axis the proposal adds nothing and should REUSE, not re-derive. But the proposal SURVIVES on three axes the existing design lacks: (1) the RATIONALE — "instruction-adherence-under-load" is absent from the design's five reasons (DF3); (2) the BUDGET SCALE — adherence-calibrated (small) vs the design's capacity-calibrated (200K), a ~200× change; (3) the POLICY FLIP — the existing design defaults chunking OFF/opt-in; the adherence rationale, if real, makes it a correctness-load-bearing DEFAULT (flip on). Redundancy lands on the "how," not on the "why / at-what-scale / whether-on."

**(b) OVER-ENGINEERING rival — does mandatory chunking harm short texts / over-formalize?**
DEFUSED by the flip-on resolution. Against the crude reading (always-split) it would land (harms short texts, fragments small-passage harmony). Against the resolved reading (budget-gated-always-on, conditional-by-construction, boundary-snapping, short-texts-pass-through) it does not land — that IS the minimal correct form, and it is already what the schema supports (DF7). The over-engineering risk is real only if the design ignores the conditional gate; the resolution builds the gate in.

**(c) DEEP rival — is the real insight "reduce active load" (staging/rule-count, 04-12) not "chunk the source"?**
PARTIALLY LANDS — and sharpens the model. The user's deep insight IS "reduce the model's load to preserve adherence," which is DEEPER than "chunk." That insight has TWO levers on DIFFERENT load components: (i) chunk the source/generation → bounds the TRANSFORMATION working-set; (ii) stage/prune the instructions → bounds the FIXED instruction load + active-rule-count (the 04-12 staging lever). Source-chunking addresses (i) and does NOTHING for (ii) — the ~80 active principles fire per chunk regardless. So source-chunking PARTLY MISSES the load problem (it leaves the large fixed-rule load untouched). BUT it does NOT dissolve into staging: the transformation working-set is a genuine, distinct, large component that staging does not touch. The honest synthesis: chunking and staging are SIBLING levers under one "bounded-load translation" principle, partitioning the load — chunking the variable/transformation part, staging the fixed/instruction part. The complete adherence answer is BOTH.

**Degrees of freedom fixed:**
- Chunking survives as its own contribution (real, distinct axis) — does NOT dissolve into the 3-Pass or into staging.
- "Mandatory" = budget-gated-always-on policy (not always-split).
- Chunking is entangled-with the 3-Pass (Pass 2 brackets it) and a sibling-of staging (partitioned load).
- The "how" is redundant with the existing design (reuse); the "why/scale/flip" is new.
- Phase-dependence: instruction-level now (SKILL.md), engine-policy later (built apparatus).

### SV5 — Constrained Understanding

The solution space is now: chunking is a real, distinct, mechanical lever on the transformation-load component of adherence; it is worth flipping on as a budget-gated-always-on, boundary-snapping, per-model policy; it must be bracketed by whole-text comprehension/harmony-map (before) and whole-draft check (after), which entangles it with the un-wired 3-Pass; its budget is bounded below by a harmony floor and calibrated empirically (unvalidated); and it is a sibling to staging under a bounded-load principle — the two together, not chunking alone, are the complete adherence answer. The "how" is already designed; the new yield is the rationale + scale + policy-flip + the bracketing architecture.

---

## Phase 5 — Conceptual Stabilization

No accommodation trigger fired — the model stabilized by layer-separation + load-partition rather than by patching. One residual is carried honestly (the long-span-structure vs small-budget trade), which is a bounded trade, not a model-misfit.

### SV6 — Stabilized Model

**The user's instinct is right and valuable; the form refines, and the genuinely-new yield is modest-but-real.**

1. **THE PIVOT resolves (HIGH):** instruction-adherence-degrades-with-load is **REAL and DISTINCT** from the un-wired-3-Pass — it is the LOAD-MAGNITUDE axis (scales with size), where the 3-Pass is the METHOD-STRUCTURE axis (order, size-independent); COMPLEMENTARY, not rival. The true variable is the per-unit **transformation working-set** (source-unit + output + local tracking), NOT source-char-count alone (an approximate proxy) and NOT the fixed instruction load (which chunking doesn't touch). The ~3500 figure is real-in-kind, approximate-and-model-dependent-in-value.

2. **THE FLIP-ON resolves (HIGH):** "mandatory" rightly means flipping the **already-designed, dormant** apparatus ON as a **budget-gated-always-on, harmony-boundary-snapping, per-model-calibrated policy** — conditional-by-construction (short texts pass through), never always-split. Phase-dependent: a **model-facing SKILL.md instruction now** (the engine is unbuilt), the **PipelineConfig budget policy later**.

3. **THE WHOLE-SPAN REMAINDER resolves (HIGH, with a flagged residual):** chunking coexists with the whole-text obligations by **layer separation** — whole-text comprehension + Pass-2 Harmony Map BEFORE, chunked generation IN THE MIDDLE, whole-draft structural check (01-09) AFTER — which makes chunking **architecturally entangled with the un-wired 3-Pass** (Pass 2 is the bracket that makes safe chunking possible). Residual bounded trade: a Tier-1 structure whose span exceeds the adherence-safe chunk size sets a **harmony FLOOR** on the budget (it can't go so small it fragments Tier-1 spans) — so the adherence ceiling and the harmony floor negotiate the budget.

4. **RIVALS:** redundancy lands on the "how" (reuse the existing design) not the "why/scale/flip" (new); over-engineering is defused by the budget-gate; the deep-rival partially lands — chunking is ONE of two sibling load levers (transformation-load), staging (04-12) is the other (instruction/rule-load), and the **complete adherence answer is both**, not chunking alone.

**Relationships:** COMPLEMENTARY-AND-ENTANGLED with the un-wired-3-Pass (`00-24`; Pass 2 brackets chunking); SIBLING to staging (`04-12`) under a bounded-load principle; INTERACTS-WITH the whole-draft checks (`01-09`; they are the post-assembly bracket); EXTENDS the existing chunking design (`06-14` findings) with a new driver that re-scales the budget + flips the policy on. Supersedes nothing.

**Difference from SV1:** SV1 saw a plausible reliability heuristic needing a design. SV6 sees a real, distinct load-axis lever whose HOW is already designed (reuse), whose genuinely-new yield is a rationale + a ~200× smaller budget scale + an opt-in→mandatory flip, which must be bracketed by whole-text passes (entangling it with the un-wired 3-Pass) and paired with staging as the two-lever complete answer — with the ~3500 number an unvalidated, model-dependent, harmony-floored estimate.

---

## Telemetry

- **Perspective saturation:** reached — the last perspectives (Phase/Calibration-State, Definitional) added the phase-split and the layer-separation but no new anchor TYPES.
- **Ambiguity resolution ratio:** 3/3 core ambiguities resolved (one with a flagged residual — the long-span-vs-small-budget trade).
- **SV delta:** large (SV1 "reliability heuristic + design" → SV6 "distinct load-axis lever, how-already-designed, new-yield-is-rationale+scale+flip, bracketed+entangled, sibling-to-staging").
- **Anchor diversity:** constraints + insights + structural points + principles + meaning-nodes, from 7 perspectives.
- **Failure modes checked:** Status-Quo-Bias (credited the existing design but showed the new driver survives — not over-protected); Premature-Stabilization (the deep-rival's partial-landing + the 3-Pass entanglement were non-obvious surprises, not early clarity); Anchor-Dominance (the "load" anchor partitions into transformation-vs-instruction, not monolithic); Clean-Resolution-Trap (the whole-span remainder was NOT resolved cleanly — the long-span residual is carried honestly); Self-Reference-Blindness (n/a — evaluating a translation architecture, not a cognitive discipline).

**Stabilized. Proceed to Decomposition.**
