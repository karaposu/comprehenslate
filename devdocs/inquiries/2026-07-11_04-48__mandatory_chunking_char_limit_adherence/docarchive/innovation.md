## User Input

Innovation for piece C (fix-design) of inquiry `2026-07-11_04-48`: the TWO coupled sub-designs (C1 flip-on-policy + C2 whole-span-bracketing-architecture), REUSING the 06-14 chunking mechanism (do NOT re-derive), plus the non-obvious reframe (is instruction-now chunking self-defeating like 04-12's soft borders?) and the standing-principle question (is "bounded-load translation" worth stating?). Settled ground: pivot resolved (adherence-under-load real & distinct, variable = transformation working-set); how-already-designed; rivals settled; relationships (complementary-entangled 00-24 / sibling 04-12 / interacts 01-09 / extends 06-14). Full input in `_branch.md` + sensemaking.md + decomposition.md + surfacing.md.

---

# Structural Innovation — Output

## Seed + Methodology-Mode Consideration

**Seed (design-realization):** realize C1 (express "mandatory" as budget-gated-always-on + boundary-snapping + per-model + phase-split) and C2 (sequence chunking with the whole-text obligations), reusing the designed mechanism.

**Inherited methodology mode:** Standard default (elaborate the committed direction — produce ship-ready design candidates for C1+C2), carrying a strong REUSE constraint (the mechanism is designed; don't re-invent).

**Alternative mode named:** Contrarian-rethink (Framer-weighted) — the seed explicitly asks one contrarian reframe (is instruction-now self-defeating like 04-12?).

**What follows under the alternative:** a fully Framer-weighted run would challenge whether chunking-as-instruction is enforceable at all, potentially dissolving C1's instruction-now layer — valuable for the ONE reframe, but it would under-produce the design candidates the seed primarily wants.

**Decision:** `Methodology-mode-alternative-marked-inapplicable: the seed primarily asks for design candidates for C1+C2 (elaborate committed direction under a reuse constraint); the contrarian element is scoped to ONE explicit reframe (the instruction-now enforcement question), which is handled as a piece-level Inversion + a RE-TEST TRIGGER, not a run-wide Framer-weighting.` Run Standard default; honor the contrarian directive locally at the reframe.

---

## Phase 2 — Generate

### C1 — The flip-on policy

**Absence Recognition (patch-level + redesign-level).** Patch: to make chunking a "mandatory-adherence policy," three things are MISSING from the dormant apparatus — (i) a non-None default for `chunking_budget` (it is None = off); (ii) a per-model dimension (the schema is a single int, no per-model home for "lower for smaller models"); (iii) any chunking presence in the model-facing SKILL.md at all (Step 5 reads + translates whole). Redesign-level: if the model-facing workflow were designed from scratch for adherence today, Step 5 would *open* with "translate in bounded units," not treat whole-text translation as the default with chunking bolted on as an engine knob.

**Constraint Manipulation (REMOVE — the load-bearing move).** REMOVE the assumed constraint "the budget must be a NUMBER (~3500 chars / N tokens)." Once removed: the default policy chunks by **structural unit** (the existing granularity ladder — mesele/section/paragraph, A4-driven, already designed in the 06-14 findings), which is (a) model-actionable (the model chunks by reading structure, not by counting tokens), (b) harmony-boundary-snapping by construction (structural units don't cut mid-sentence), and (c) requires NO validated number. The numeric budget becomes a later-calibrated CAP (split a structural unit further only if it is itself too large). This dissolves the "where does the budget come from with no evidence" problem: **the default budget comes from STRUCTURE, not from ~3500.** (ADD-direction: ADD the constraint "a chunk must never fragment a Tier-1 harmony chain" — which the existing `harmony-tier-aware` mechanism already enforces; the ADD reuses the designed mechanism.)

**Combination (phase-split × the two layers).** Combine the phase-dependence (SV3) with the two realization layers:
- **Phase-now (instruction-level, engine unbuilt):** SKILL.md gains a chunking instruction — expressed in **structural units, not a token count**: *"If the source is longer than a single section/mesele (roughly one screen), translate it one structural unit at a time — snapping to paragraph/section/mesele boundaries, never mid-sentence, never splitting a Tier-1 harmony chain — then assemble the units into the whole before the final check."* Budget = structural granularity (model-legible).
- **Phase-later (engine-level, apparatus built):** flip `PipelineConfig.chunking_budget` from `None` to a conservative structural-default; add a per-model dimension (a per-model budget map — the "lower for smaller models" instinct gets a home); the engine performs budget-gated splitting via the designed hybrid harmony-aware mechanism. Numeric budget = tokens (engine-legible), calibrated empirically (deferred).

**Domain Transfer (native — config/feature-flag engineering).** The flip is a **feature-flag default change** (opt-in `None` → on-by-default) guarded by a **conditional gate** (budget) — a standard safe-rollout shape: the policy is "always on," the gate makes it "only act above threshold," so turning it on cannot regress short inputs. This is exactly the "budget-gated-always-on ≠ always-split" resolution, in standard config-engineering vocabulary.

### C2 — The whole-span bracketing architecture

**Combination (3-Pass + chunking + 01-09 checks into one pipeline).**
1. **BEFORE (whole-text):** whole-source comprehension (Pass-1 Meaning) + **Pass-2 Harmony Map over the WHOLE source** → produces the locked meaning + the **harmony blueprint** (the map of Tier-1-2 structures and their spans). Inherently whole-text (Pass 2 needs the whole).
2. **MIDDLE (chunked):** **Pass-3 Target Reconstruction per chunk**, each chunk's generation consulting the relevant **slice** of the whole-text harmony blueprint. The chunk is the GENERATION unit; the blueprint is whole.
3. **AFTER (whole-draft):** assemble the chunks → run the prior-01-09 whole-draft structural check (omission-diff + escalation/ring/havuz preserved) on the assembled whole.

**Domain Transfer (native — map-reduce with shared read-only context / the compiler pattern).** This architecture is a known-sound pattern: **whole-program analysis → per-unit codegen → whole-program link+verify.** The harmony blueprint = the shared read-only "symbol table" computed in a whole-text analysis pass; the chunks = the map/codegen tasks (each generates its unit against the shared table); assembly + whole-draft check = link + verify. That chunked generation with a shared whole-text analysis is a standard, sound shape is itself the reassurance that C2 is not exotic — it is the compiler/map-reduce pattern applied to translation.

**Absence Recognition + Constraint (the harmony floor, structure-derived).** The floor is COMPUTED from the blueprint: for each Tier-1 structure, its **span** (in units). The minimum safe chunk = the max span of any Tier-1 structure it would otherwise fragment. So — like C1's budget — the floor is **structure-derived, not a fixed number.** Where a Tier-1 span exceeds the adherence-safe size, the existing adaptive `harmony-tier-aware` mechanism already handles it (snap the boundary to avoid fragmenting; where impossible, either carry that structure's blueprint-slice into each sub-chunk — bounded extra load, not the whole text — or keep that structure whole and accept a larger chunk there). The residual is the 06-14 design's own failure-mode-10 (PARTIAL) — carried honestly.

### The non-obvious reframe (contrarian directive) — instruction-now vs the 04-12 gradient

**Inversion (system-level) + Lens Shifting.** Assumption: "the instruction-now version of mandatory chunking gives the adherence benefit." Invert: *within one model run, an instruction to "translate in units of N" is SOFT — the model still has the whole source in its context and can spread attention over it / translate in one motion anyway* — the SAME one-run softness the prior `04-12` staged-borders had (probability-raiser, not enforcer). So the instruction-now version is a **weak probability-raiser**, not real enforcement.

**BUT the lens shift sharpens it (chunking > staging on enforceability):** staging (04-12) was TRAPPED at the weak end of the gradient by the user's "still one run" constraint. Chunking is NOT so trapped — its natural realization is **separate generation calls** (the engine phase), which is the STRONG end: in a separate call the model **physically cannot see the other chunks' source**, so the transformation working-set is *actually* bounded, not just instructed-to-be. So chunking maps onto the same 04-12 gradient (prose-instruction < emitted-artifact < separate-call) but its natural home is the **strong end**:

| Rung | Chunking realization | Enforcement |
|---|---|---|
| prose-instruction (weak) | instruction-now in SKILL.md ("translate in units of N") | soft — model still sees the whole source in one context (same softness as 04-12 staged borders) |
| emitted-artifact (mid) | emit each unit's translation before starting the next, in one run | stronger — commits each unit, but the whole source is still in context |
| **separate-call (strong)** | engine-later: one bounded API call per chunk | **real** — the model physically cannot see the other chunks' source; the transformation working-set is actually bounded |

**The honest consequence:** the instruction-now version is worth doing (a genuine probability-raiser, like staging) but is NOT where chunking's adherence prize lands — the prize lands at **engine-later (separate calls)**, because only separate calls physically bound what the model sees per generation. This makes the phase-split load-bearing: instruction-now = weak-but-real nudge; engine-later = the actual enforcement. → **RE-TEST TRIGGER** on C1's "instruction-now" value.

### The standing-principle question — "bounded-load translation"

**Extrapolation + Combination.** The deep-rival established chunking + staging as two levers on "reduce active load to preserve adherence," attacking DIFFERENT load components. Is "bounded-load translation" a real principle? **FOR:** it genuinely unifies `04-12` and this inquiry as instances of one thing (keep active load under the adherence ceiling), it explains why they are siblings-not-rivals, and it partitions the design space (transformation-load [chunk] + instruction/rule-load [stage] — predicting a possible third lever, e.g., output-load or config-axis-count reduction). **AGAINST (specific-vs-pattern):** two instances is thin, and "reduce load" is nearly tautological — as a grand principle it risks becoming a slogan licensing any "do less" move without the specific analysis each lever needs. **Resolution:** state it as a MODEST load-partition OBSERVATION (the adherence load has ≥2 reducible components; chunking cuts the transformation part, staging cuts the instruction/rule part), NOT a universal law — DEFERRED, revival to a fuller principle if a third lever appears. It connects to the existing `[[project_skill_design_discipline]]` memory (staging = probability-raiser).

---

## Piece-Level / Intervention-Shape Inversions

**C1 (property (v) — intervention-shape commitment).** Committed shape: **ADD-CONTENT** (a chunking instruction to SKILL.md) + a **config default-flip** (chunking_budget None→structural-default). Intervention-Shape-Axis Inversion — name an alternative shape: **DO-NOTHING** (leave the apparatus dormant/opt-in) and **REORGANIZE-WITHOUT-ADDING** (get chunking by restructuring Step 2's "read the source" without new content). What follows: DO-NOTHING keeps the adherence problem unaddressed (rejected only if the pivot's "real & distinct" verdict holds — which it does, so DO-NOTHING is the null baseline the flip must beat); REORGANIZE fails because there is genuinely no chunking content to restructure — Step 2 reads whole, so chunking must be ADDED. Verdict: ADD-CONTENT (instruction) + CONFIG-FLIP is correct; DO-NOTHING is the honest null baseline (the reach gate lets the user pick it); REORGANIZE inapplicable (nothing to reorganize). Inversion tested, principal shape survives.

**C2 (property (ii) — framing-semantic).** Committed frame: the 3-layer bracketing (whole-before / chunk-middle / whole-after). Piece-Level Inversion — reverse the sequencing assumption: (a) "no BEFORE" (chunk blind, no whole-text harmony map) → reproduces failure-mode-10 (broken cross-chunk structures) — the very failure the bracket prevents; (b) "no MIDDLE" (no chunked generation, whole-text throughout) → the status quo → the adherence problem returns. Both inversions reproduce known failures → the bracket+chunk architecture is confirmed by its inversions failing. Inversion tested, frame survives.

---

## Inherited Frame Audit

**Seed central assumption:** "chunking survives as a real, distinct lever worth flipping on; the HOW is already designed (reuse)." **Challenge scan:** the candidate set DOES challenge it — (a) the reframe (instruction-now is a *weak* probability-raiser, not the prize) challenges the near-term value; (b) the DO-NOTHING intervention-shape inversion challenges the flip itself; (c) the deep-rival (sensemaking) challenged "chunking vs staging." So the frame has explicit challenges in the set. **Audit does NOT fire.**

---

## Phase 3 — Test (5-test on survivors)

**S1 — C1 structural-budget flip-on (chunk by granularity ladder now; numeric cap later; phase-split).**
Novelty: MED (reuses the mechanism; new = the structure-not-number budget default + the phase-split). Scrutiny: survives — sidesteps the no-evidence problem by chunking on structure. Fertility: opens the per-model calibration + the numeric-cap refinement. Actionability: HIGH (instruction-now is a concrete SKILL.md edit; engine-later is a concrete config flip). Mechanism-independence: reached via Absence + Constraint-REMOVE + Domain-transfer (convergent). **Survives → ACTIONABLE (offered, reach-gated).**

**S2 — C2 map-reduce bracketing (whole-text harmony map → chunked Pass-3 → whole-draft check).**
Novelty: MED (composes the 3-Pass + chunking + 01-09; the compiler/map-reduce framing is the clarifying new). Scrutiny: survives — the pattern is known-sound; inversions reproduce known failures. Fertility: HIGH (defines how chunking, the 3-Pass, and the checks compose). Actionability: HIGH (a concrete pipeline sequence). Mechanism-independence: Combination + Domain-transfer + Inversion converge. **Survives → ACTIONABLE (offered, reach-gated + gated on the 3-Pass being wired, per I7).**

**S3 — the reframe (instruction-now = weak rung; engine-later = the enforcement prize; chunking > staging on enforceability).**
Novelty: HIGH (non-obvious; connects the phase-split to the 04-12 gradient and differentiates chunking from staging). Scrutiny: survives — grounded in the physical fact that separate calls bound the context. Fertility: HIGH (recasts the whole reach discussion). Actionability: it is an evaluative caveat, not a build step. Mechanism-independence: Inversion + Lens-shift + the 04-12 precedent converge. **Survives → RE-TEST TRIGGER (recasts C1's instruction-now value + the flip-on's near-term power; the finding must be honest that the real prize is engine-later).**

**S4 — the harmony floor is structure-derived (from Pass-2's blueprint), not a number.**
Novelty: MED. Scrutiny: survives (the floor = max Tier-1 span, computed from the blueprint C2 already produces). Fertility: MED (ties the budget to structure, converging with S1). Actionability: HIGH (the existing adaptive mechanism computes it). **Survives → ACTIONABLE (folds into S2).**

**S5 — "bounded-load translation" load-partition observation.**
Novelty: MED. Scrutiny: survives only as a MODEST observation (grand-principle reading fails specific-vs-pattern). Fertility: MED (predicts a third lever). Actionability: LOW (it is an organizing note). Mechanism-independence: single-source (Extrapolation). **Survives thin → DEFERRED (revival: a third load lever appears; then promote to a stated principle).**

---

## Assembly Check

The survivors assemble into ONE architecture: **bounded-load translation, chunking lever** = a whole-text analysis pass (comprehension + harmony map) → **structure-budgeted chunked generation** (S1's structural budget = S2's chunk unit = S4's structure-derived floor, all the SAME structural granularity) → whole-draft check (01-09). The emergent value none of the pieces has alone: **the budget, the chunk unit, and the harmony floor are the SAME structural quantity** (the granularity ladder), so C1's "where does the budget come from" and C2's "what sets the floor" have ONE answer — structure — which is already designed (06-14). The phase-split (S3) tells the honest story: this architecture is a weak nudge as an instruction, the real thing as an engine. The load-partition (S5) places it beside staging.

**Axis coverage:** the candidate set varies along (i) the realization axis (instruction / config-flip / separate-call — S1, S3), (ii) the architecture axis (bracketing sequence — S2), (iii) the budget-origin axis (structure vs number — S1, S4), (iv) the principle axis (S5). Multiple orthogonal axes covered. Per-piece: C1 and C2 each received active mechanism work + inversion.

---

## Dispositions

- **ACTIONABLE (offered, reach-gated):** S1 (structural-budget flip-on, phase-split) · S2 (map-reduce bracketing) · S4 (structure-derived harmony floor, folded into S2).
- **RE-TEST TRIGGER:** S3 — the instruction-now-is-weak / engine-later-is-the-prize reframe recasts C1's near-term value and the flip-on's power; the finding's headline must carry it (instruction-now = probability-raiser like 04-12; the adherence prize is engine-later separate-calls; chunking > staging on enforceability).
- **DEFERRED (revival — a third load lever appears):** S5 — the "bounded-load translation" load-partition observation, stated modestly.
- **RESEARCH FRONTIER:** the empirical budget calibration (the adherence-safe structural granularity + numeric cap, per-model) — no evidence exists (DF8); it is the 06-14 design's own never-run validation, now additionally motivated by adherence.

---

## Telemetry

- Generators applied: 4/4 (Combination, Absence Recognition, Domain Transfer, Extrapolation)
- Framers applied: 3/3 (Lens Shifting, Constraint Manipulation, Inversion)
- Convergence: YES — S1+S2+S4 converge on "the budget = the chunk unit = the harmony floor = the structural granularity (already designed)"; independently grounded (Absence / Constraint / Combination / Domain-transfer), not spurious-shared-input.
- Survivors tested: 5/5.
- Per-piece mechanism log: `C1: [Absence, Constraint-REMOVE+ADD, Combination, Domain-transfer, Inversion:intervention-shape]` · `C2: [Combination, Domain-transfer, Absence, Inversion:framing-semantic]` · `reframe: [Inversion:system, Lens-shift]` · `principle: [Extrapolation, Combination]`.
- Meta-decision-piece classification: C1 = meta-decision (property v) — Piece-level Inversion **satisfied** (intervention-shape axis); C2 = meta-decision (property ii) — Piece-level Inversion **satisfied** (framing-semantic axis).
- Inherited Frame Audit: did NOT fire (frame challenged by the reframe + DO-NOTHING inversion + deep-rival).
- Failure modes observed: none (generation preceded testing; 7 mechanisms; no early frame-lock — the reframe surfaced the weak-rung challenge; no survival bias — the uncomfortable "instruction-now is weak / DO-NOTHING is the null baseline" survived).
- **Overall: PROCEED** (full coverage + convergence + all survivors tested + both meta-decision pieces' inversions satisfied).

Next: Critique (adjudicate S1/S2/S4 designs + the S3 reframe + the S5 principle; stress-test — the structure-not-number budget claim; the map-reduce coexistence; the instruction-now-is-weak / engine-later-is-the-prize honesty; EXTENDS-06-14 + complementary-entangled-00-24; and whether the whole thing over-reaches vs "just reuse the 06-14 design + set a smaller budget").
