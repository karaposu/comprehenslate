## User Input

Design-realization + reframe pass for the OPEN RESIDUAL (piece E) + the unit-verdict realization (piece A) + non-obvious reframes. The evaluative core (A unit-verdict, B evidence-verdict, C concept, D reconciliation) is SETTLED by sensemaking — do NOT re-derive. Must address: E1 (the number + per-model calibration; the user's ~3500 vs the demonstrated-safe 4,345 source; the cheap experiment); E2 (output-side guard; the 2.57× over-expansion — cause-to-bound or symptom-to-monitor); A-realize (define the untyped `chunking_budget:int|None` field; phase-split instruction-now/engine-later; reuse fixed-budget-with-snap); the REFRAME (is the char-budget a temporary crutch that fades once the 3-Pass is wired, or permanent?); the STANDING PRINCIPLE (confound-robust conservative safeguard / "type your config fields with their unit"). Full settled-ground + branch in the invocation + `_branch.md`.

---

# Structural Innovation — Output

## Seed + Methodology-Mode Consideration

**Seed (design-realization + reframe):** realize the settled unit-verdict + close the open residual (the number, the output-side guard) + surface the crutch-vs-permanent reframe.

- **Inherited mode:** Standard default (elaborate the committed direction — the evaluative core is settled; produce ship-ready realization). Text signals: "generate ideas primarily for… realization… reframes."
- **Alternative named:** Contrarian-rethink (Framer-weighted) — challenge the whole char-budget.
- **What follows under the alternative:** it would re-litigate the settled evaluative core (is char the right unit at all, does the evidence hold) — which sensemaking already adjudicated across 7 perspectives + 3 rivals. Run-wide contrarian would reproduce settled work.
- **Decision:** **Standard default**, with the contrarian LENS honored LOCALLY at the reframe (the crutch-vs-permanent probe IS a contrarian challenge to the "standing safeguard" frame). `Methodology-mode-alternative-marked-inapplicable (run-wide): the evaluative core is settled by sensemaking SV1-SV6 + 3 rival tests; re-litigating it run-wide is the wrong mode. Contrarian honored locally at S4.`

## Mechanism Generation

### E1 — the number + per-model calibration → **S1**
- **Domain Transfer (engineering safety factors):** you set a working load BELOW the demonstrated-safe load by a safety factor. Demonstrated-safe SOURCE = **4,345 chars** (4_mesele, GOOD). Safety factor ~0.8 → **~3,500**. → **the user's ~3500 is a sound ~0.8-safety-factored pick BELOW the one demonstrated success**, not an arbitrary guess and not over-conservative.
- **Constraint Manipulation (ADD):** "we have demonstrated-SAFE points but NO demonstrated-fail-NEAR-threshold" → the number can only be a *conservative-below-known-safe*, not a *located cliff*. **(REMOVE)** "must be a single number" → express as a **band**: safe floor ~3,500, demonstrated-safe ~4,345, unknown-region above until data.
- **Absence Recognition (patch):** the schema's `chunking_budget` has no per-model dimension. **(redesign):** express per-model as a **fraction of that model's demonstrated-safe point**, not an absolute — "lower for smaller models" = a smaller fraction, calibrated up as data arrives.
- **The cheap experiment (Combination — reuse the 04-48 never-run calibration, now provenance-anchored):** before any synthetic trial: (a) get the user's judgment on **5th_word** (~4,148 source — a candidate 2nd success point); (b) locate/measure the **ikinci_huccet SOURCE** (the missing number — is the failed source ~11,000 as the user recalls?); (c) **bisect the gap** — translate ONE medium source (~7,000–10,000 chars) to find where failure STARTS between the 4,345-safe and the 28,330-fail. Bisection is far cheaper than a full sweep and directly locates the cliff.
- **Disposition: ACTIONABLE.** Anchor = demonstrated-safe − safety-factor ≈ **3,500–4,000 source chars for Opus 4.8** (the user's 3500 is the conservative floor); per-model = fraction-of-demonstrated-safe; cheapest calibration = judge 5th_word + find the failed source-size + bisect once.

### E2 — the output-side guard → **S2**
- **Inversion:** "bound the output" → **you can't** — output is GENERATED, not an input you control; only the SOURCE size is controllable. Bounding output is a category error. *(depth-check, system-level):* the output/source **expansion ratio** is a cheap **post-hoc integrity signal** — like a checksum on the translation.
- **Absence Recognition:** there is no expansion-ratio check anywhere. Healthy = **1.49–1.63×** (measured); the failure = **2.57×**. A cheap guard: after a chunk translates, if `output_chars / source_chars > ~2.0`, **flag for review** — the model is probably padding/over-elaborating (a symptom it is already failing).
- **Lens Shifting:** under the "budget = prevention" frame, output-bounding looks necessary; under the "integrity = detection" frame (the 01-09 whole-draft-check lens), the ratio is a **detector**, not a controller.
- **Disposition: ACTIONABLE.** The over-expansion is a **SYMPTOM to monitor, not a cause to bound**: keep the SOURCE budget as the control; ADD a cheap expansion-ratio watch (flag `>~2×`) as a post-hoc integrity signal, complementary to (and sharing the back-end bracket with) the 01-09 whole-draft check.

### A-realize — define the untyped field → **S3** (meta-decision piece, property v)
- **Absence Recognition (patch):** `chunking_budget: int | None = None` carries NO unit — the exact gap that let "char vs token vs structure" become a confusion. Cheapest close: rename/document → `chunking_budget_source_chars: int | None` (or keep the name + a `# source characters` doc + a per-model note).
- **Combination (with the 04-48 phase-split):** instruction-now (SKILL.md: *"translate in source-chunks of ~3,500–4,000 characters, snapping to the nearest harmony/section boundary"*) + engine-later (type the field + per-model dim). Reuse `fixed-budget-with-snap`; do NOT re-invent.
- **Intervention-shape:** ADD-CONTENT (the SKILL.md instruction) + REPAIR (typing the untyped field).
- **Piece-level Inversion (intervention-shape axis — required):** commit-shape = ADD-CONTENT+REPAIR. Alternative shape = **DO-NOTHING** (leave the field untyped, deepen-only). *What follows under DO-NOTHING:* the untyped `int` persists and **re-invites the very char-vs-token-vs-structure confusion this whole inquiry had to resolve** — a reproduced-ambiguity cost. Also considered **REORGANIZE** (inapplicable — there's nothing to restructure, the field is a single line). → ADD-CONTENT+REPAIR justified over DO-NOTHING, BUT **gated on reach + authorization** (deepen-only is the honest null baseline the reach-gate offers). Both tested.
- **Disposition: ACTIONABLE (gated).** Type/document `chunking_budget` as source-characters (REPAIR) + the instruction-now SKILL.md text (ADD-CONTENT), phase-split like 04-48; gated on the user's reach decision + authorization.

### THE REFRAME — temporary crutch vs permanent safeguard → **S4** (the deepest yield; contrarian-honored)
- **Inversion (of "the char-budget is a standing safeguard"):** what if it's a **TEMPORARY CRUTCH** that fades once the un-wired 3-Pass is wired?
- **The reasoning (from the confound-robustness):** the survival argument says *small size lets the UN-WIRED method survive*. So:
  - **If the failure is PURELY method** (un-wired-3-Pass) and length merely correlates → wiring the 3-Pass would let LARGE chunks succeed too → the char-budget becomes **less necessary** (a crutch for the un-wired state).
  - **If the failure is PARTLY load** (adherence degrades with size even with a wired method — 04-48's actual thesis) → the char-budget stays necessary (a **permanent** safeguard).
- **Since the mechanism is confounded, we cannot know which today.** The honest landing: the char-budget is **AT LEAST a now-crutch** (it definitely helps in the current un-wired state) and **POSSIBLY a permanent safeguard** (if load-degradation is real). And its status is **empirically decidable**: wire the 3-Pass, then re-test large chunks — if they recover, it was a crutch (relax the budget); if they still fail, it's permanent (keep it).
- **Disposition: RE-TEST TRIGGER.** This recasts how the char-budget is HELD (adopt now — it helps regardless; revisit its long-run necessity AFTER the 3-Pass is wired) and it RE-TESTS 04-48's two-lever independence claim: the char-budget's *permanence* is a proxy-measurement for whether adherence-under-load is truly a distinct lever or partly a stand-in for the un-wired method. The 04-48 experiment + the wiring together decide it.

### THE STANDING PRINCIPLE → **S5** (deferred) + **S6** (small authoring lesson)
- **S5 — "confound-robust conservative safeguard" (Domain Transfer — robust decision under model uncertainty / defense-in-depth):** when two candidate mechanisms are confounded and a cheap intervention helps under BOTH, you can adopt it **without resolving the confound** — the confound stops being a blocker. This is the decision-theoretic "pick the action that's good across all plausible models." It unblocks action under exactly the uncertainty (the confound) that would otherwise stall. **Disposition: DEFERRED** — modest (2 instances: this char-budget + 04-48's low-regret-bet); state as a decision-heuristic; revival on a 3rd instance. Links [[project_skill_design_discipline]].
- **S6 — "type your config fields with their unit" (Absence Recognition, concrete):** the untyped `chunking_budget: int` is precisely what invited the char-vs-token-vs-structure confusion this inquiry spent a full traverse resolving. A config field carrying a magnitude should name its unit in its type/name. **Disposition: ACTIONABLE-small** (an authoring note; folds into S3's REPAIR).

## Inherited Frame Audit

- **Seed central assumption:** "the char-budget is worth adopting (the user's instinct is right)." **Challenged?** YES — S4 challenges its PERMANENCE (crutch-vs-permanent); S3's DO-NOTHING inversion challenges adopting-it-now; sensemaking's confound-collapse rival already challenged its basis. → **audit does NOT fire.**
- **Piece-level (S3, property v):** intervention-shape commitment challenged by the DO-NOTHING inversion above. Satisfied.

## Assembly Check + Convergence

**Convergence (4+ mechanisms):** Domain-Transfer (safety factor) + Constraint (below-known-safe) + Absence (per-model fraction) + Combination (cheap bisection experiment) all converge on: **the number is "demonstrated-safe minus a safety margin" (~3,500–4,000 source chars for Opus 4.8, the user's 3500 = the conservative floor), per-model as a fraction, calibrated by bisecting the 4,345→28,330 gap.** High confidence.

**Emergent architecture (assembly):** the pieces compose into a coherent **confound-robust conservative safeguard**: a **source-character budget** (~3,500–4,000, per-model, snapping to structure via the existing `fixed-budget-with-snap`) + a cheap **output-side expansion-ratio watch** (flag `>~2×`) + a **typed field** (closing the untyped-int ambiguity) — adopted NOW because it helps regardless of the confounded mechanism, with its LONG-RUN necessity (crutch vs permanent) left as an empirical question the 3-Pass-wiring + the bisection experiment jointly decide.

## Telemetry
- Generators applied: 4/4 (Combination, Absence, Domain-Transfer, Extrapolation[light, in the bisection/future-data reasoning]).
- Framers applied: 3/3 (Inversion, Constraint-Manipulation [ADD+REMOVE], Lens-Shifting).
- Convergence: **YES** — 4 mechanisms converge on the safety-factor/demonstrated-safe-minus-margin number + source-primary-output-watched shape.
- Survivors tested: 6/6 (S1-S6 via the 5-test cycle: novel / survives-scrutiny / fertile / actionable / mechanism-independent).
- Per-piece meta-decision log: S3 = meta-decision (property v, intervention-shape) → Piece-level Inversion **satisfied** (axis = intervention-shape: ADD-CONTENT+REPAIR vs DO-NOTHING). S4 = meta-decision (framing-semantic) → Inversion **satisfied** (crutch-vs-permanent both poles generated). S1/S2/S5/S6 = content-production.
- Failure modes observed: none (generation preceded testing; ≥1G+1F; not early-frame-locked — S4 reframe surfaced after S1-S3; uncomfortable output [DO-NOTHING, crutch-hypothesis] generated + tested).
- **Overall: PROCEED** — full coverage, convergence, all survivors tested, no failure modes; the S4 crutch-vs-permanent RE-TEST TRIGGER is the deepest yield and reaches CONCLUDE as a refinement of how the char-budget is held.
