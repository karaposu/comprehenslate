## User Input

Warm-settled anchor (non-severe content-conflict — right instinct, refined form). Resolve against the MEASURED reality (4_mesele src 4,345/out 7,080 GOOD; 5th_word src 4,148 unjudged; ikinci_huccet out 28,330 FAILED, source absent, over-expanded 2.57×; user's "3500"≈good-example source; mistakes.md errors = un-wired-3-Pass class; `chunking_budget:int|None` untyped + `chunking_granularity` separate + `fixed-budget-with-snap` a mechanism; "comprehenslation integrity" newly coined). Resolve: (1) the TARGET-UNIT REFRAME (char-vs-structure a false either/or → stable-unit budget snapping to structure; char vs token vs word; source vs output side); (2) the CONFOUND / evidence-weight (what 2-3 points establish; does it re-open 04-48's complementary-not-rival); (3) DEFINE comprehenslation integrity. Test rivals: dissolution / confound-collapse / spurious-proxy. Full note + branch in the invocation + `_branch.md`.

---

# Sensemaking — SV1 → SV6

## SV1 — Baseline
The user says character/word count beats structural units as the chunk-budget unit, and ~3500 is empirically grounded from real translations. Naive reading: switch the budget unit to characters, set it to ~3500.

## Phase 1 — Cognitive Anchor Extraction

**Constraints**
- **C1** gated reach (no SKILL edits without authorization); the endpoint is deepen-understanding.
- **C2** Tier-1/2 harmony-boundary preservation is a HARD constraint (chain-wide): a cut must not break a meaning-chain.
- **C3** the schema ALREADY separates the roles: `chunking_budget: int|None` (untyped size) + `chunking_granularity` (structural ladder) + `fixed-budget-with-snap` (a mechanism). Budget and snap coexist by design.
- **C4** the evidence is n=2–3 with success PERFECTLY correlated with size (small good, big failed).

**Key Insights**
- **KI1** "char vs structure" is a **FALSE either/or**: budget = the size TARGET; granularity/snap = the cut LOCATION. Different roles. The user's real, valid point is narrower — a structural LEVEL is too size-variable (a paragraph = 2 or 30 sentences ≈ 15× range) to be a reliable size TARGET; but structure remains the SNAP.
- **KI2** the measured numbers are directionally right but loose + count an ambiguous side — "3500" ≈ the good example's SOURCE (4,345); "11000" ≠ the 28,330 OUTPUT (likely the absent source; the translation over-expanded 2.57× vs a healthy 1.5–1.6×).
- **KI3 (the crux)** `mistakes.md` shows the failure's errors are register/word-sense/fluency = **un-wired-3-Pass class** → the two examples **confound** length and method. The evidence gives existence-proof + direction, NOT a threshold, NOT the mechanism.
- **KI4 (the survival argument)** a size budget helps **regardless of which confounded mechanism dominates**: a smaller chunk is easier for the model to hold ANY method over — including the un-wired 3-Pass. The 4_mesele success (short, 3-Pass NOT wired, yet GOOD) is *itself* evidence that small size lets an un-wired method survive.
- **KI5** the 2.57× over-expansion is an output-side signal — the working-set spans source AND output; a source budget is a proxy for the whole.

**Structural Points** — SP1 budget-role vs snap-role (the user conflated "unit I budget in" with "thing I cut on"). SP2 char/token/word = three candidate measures. SP3 source-side vs output-side. SP4 comprehenslation integrity = the protected outcome variable.

**Foundational Principles** — FP1 a budget UNIT must be stable across texts to be a reliable target (variance-of-size disqualifies structural levels — the user's core valid criterion). FP2 n=2 with perfectly-correlated confounds cannot separate causes. FP3 a safeguard that helps regardless of which of two confounded causes is true is robust (decision under uncertainty).

**Meaning-Nodes** — MN1 comprehenslation integrity. MN2 the target-unit reframe. MN3 the confound / evidence-weight.

### SV2 — Anchor-informed
The naive "adopt char-count, 3500" reframes: the user is RIGHT that a stable size unit beats a variable structural level as the TARGET — but "char vs structure" is a false dichotomy (different roles, already coexisting), and "3500 is empirically grounded" needs the confound-aware reading (real anchor + direction, not a threshold or a mechanism).

*Meta-inspection (H4/H5): "comprehenslation integrity" is a coined term → test in Phase 3. The 2–3 files are the motivating examples → specific-vs-pattern test in Phase 3 (do 2–3 points tell us the wider pattern? Partially — existence + direction, not the curve).*

## Phase 2 — Perspective Checking

- **Technical/Logical:** char-count is O(1), tokenizer-free, language-robust (same regardless of model). Tokens need a model-specific tokenizer + are TR/EN-asymmetric. Words are whitespace/agglutination-fragile. → **characters win on stability + legibility + feasibility; tokens win on load-faithfulness** (the model's real load IS tokens).
- **Human/User:** the author sees characters in their editor NOW; a char budget is usable in the human-in-the-loop stage without a tool. Tokens aren't human-legible. → characters win for the authoring stage.
- **Strategic/Long-term:** the measure matters less than (a) having a stable unit at all and (b) confound-honesty. Over-fitting "3500 exactly" is the risk.
- **Risk/Failure:** the danger is cargo-culting 3500 as a proven cliff (it's the good example's source size) and treating char-budget as a SUBSTITUTE for wiring the 3-Pass. Mitigated by KI4 (it's a complement, and robust to the confound).
- **Resource/Feasibility:** char-count is trivially computable (no model call). Point FOR characters.
- **Definitional/Internal Consistency:** does "char beats structure" contradict 04-48's "chunk by structure"? **NO** — 04-48 said "chunk by structure, *snapping to boundaries*," which was already budget+snap, with the number quarantined. This inquiry REFINES 04-48 (the size target is a stable unit; the snap stays structural) and PARTIALLY LIFTS its quarantine. Consistent, not contradictory.
- **Phase/Calibration-State (required — phase-dependent rule):** the ~3500 is per-model ("lower for smaller models") and pending real calibration; the project has n=2–3 anecdotal points, no systematic sweep. → the early-stage default is a **conservative char budget (~the good example's source size, rounded down), per-model, flagged calibratable** — exactly the shape of 04-48's magnitude quarantine.

### SV3 — Multi-perspective
Every perspective converges: characters are the right *human-facing budget unit* (stable/legible/feasible), tokens the *truer internal measure* for later, words rejected; the ~3500 is a *conservative per-model anchor pending calibration*; the reframe (budget-role vs snap-role) is consistent with 04-48 and refines it.

*Meta-inspection (H1/H2/H3/H7): H3 — the question's "char vs structure" framing carried a false-dichotomy premise; the budget-vs-snap-role reframe corrects it (Question-Premise check fired). H7 — phase-dependence confirmed (per-model, calibratable). Frame-exit gating (inherited "size" used across source/output values): Existence Enumeration surfaces source-size vs output-size vs whole-working-set; the user's source-only frame EXCLUDES the output-side, which the 2.57× over-expansion implicates → Role Assessment: output-side is load-bearing → re-locate, don't exclude: the SOURCE budget is the control point, understood as a proxy for the whole working-set, with output-over-expansion as an independent warning sign.*

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — char vs structure as the budget unit
- **Counter:** structure is better because it snaps to meaning (04-48's point).
- **Why it fails (structural):** budget and snap are DIFFERENT ROLES the schema already composes (`chunking_budget` + `chunking_granularity` + `fixed-budget-with-snap`). Structure can't be the size TARGET (its size varies ~15×); a target must be stable. Structure REMAINS the snap.
- **Confidence: HIGH** (schema composition + variance argument, not precedent).
- **Resolution:** budget unit = a STABLE SIZE MEASURE (characters); structure governs the SNAP (cut lands at the nearest harmony boundary ≤ budget). **Fixed:** budget=size-target, snap=structure. **No longer allowed:** treating "chunk by paragraph/section" as reliable SIZE control; treating char and structure as rivals.

### Ambiguity 2 — character vs token vs word
- **Counter:** tokens are truest (the model's load IS tokens).
- **Why it partially holds but doesn't win the config slot:** tokens ARE truest to load, but need a model-specific tokenizer, are TR/EN-asymmetric, and aren't human-legible for the authoring stage. For a CONSERVATIVE, HUMAN-FACING safeguard, characters are better (imprecision absorbed by conservatism). Words are strictly worse (agglutination + whitespace).
- **Confidence: HIGH** (word-elimination); **MED** (char-over-token — tokens genuinely truer to load).
- **Resolution:** **CHARACTERS** as the primary human-facing budget unit; **tokens** as the truer internal measure the engine may compute later; **words rejected**. **Fixed:** char = config/human unit.

### Ambiguity 3 — what does the evidence establish? (the crux)
- **Counter (confound-collapse rival):** the examples establish NOTHING about length because the errors are method-errors (un-wired-3-Pass) — so 3500 measures the wrong thing.
- **Why the counter PARTIALLY succeeds but doesn't collapse the intervention:** it is RIGHT that the evidence doesn't establish length as THE cause (confound real; `mistakes.md` leans method) → "3500 is a validated length threshold" is FALSE, that part collapses. It is WRONG that the evidence establishes nothing: an **existence-proof + a direction** survive, AND (KI4) **a size budget helps regardless of which mechanism dominates** — a smaller chunk lets ANY method (incl. the un-wired 3-Pass) survive; the SHORT 4_mesele succeeding *despite* the un-wired 3-Pass proves exactly this.
- **Confidence: HIGH** on the split.
- **Resolution:** the evidence **PARTIALLY LIFTS** 04-48's quarantine — ~3500 is a real, provenance-backed **conservative anchor** (the good example's source, 4,345), NOT the "zero evidence" 04-48 claimed, but ALSO not a validated threshold or a proven length-mechanism. Mechanism stays **confounded**; this **RE-CONFIRMS 04-48's complementary-not-rival** (small size helps the un-wired method survive). **Fixed:** 3500 = conservative per-model anchor, calibratable. **Not allowed:** "3500 is the proven cliff"; "length is the established cause"; "chunking replaces wiring the 3-Pass."

### Ambiguity 4 (load-bearing concept test) — "comprehenslation integrity": real term or rename?
- **Counter:** it's just a rename of "Tier-1/2 preservation" or "not collapse-in-one-motion."
- **Why it fails:** it is BROADER than either — Tier-1/2 preservation is one component (whole-span harmony), collapse-in-one-motion is one failure mode. "Comprehenslation integrity" = the **unified OUTCOME**: source meaning comprehended AND faithfully rendered, the thing that EVERY principle-drop (register, word-sense, harmony, Tier-1 break) degrades. It's the "what's at stake" umbrella, not a component-rename.
- **Confidence: MED-HIGH**; **user-language alignment HIGH** (user coined it).
- **Resolution:** define comprehenslation integrity = the degree to which a translation preserves BOTH the comprehended source meaning AND its faithful target rendering — the unified outcome the whole SKILL protects, degraded by any principle-drop whether caused by load OR un-wired method. Adjacent-but-broader-than Tier-1/2 preservation (a component) and collapse-in-one-motion (a failure mode).

### SV4 — Clarified
The user's contribution refines to four survivors: (1) budget in a stable unit (characters), snapping to structure [HIGH]; (2) ~3500 = a conservative per-model anchor with real provenance but confounded mechanism [HIGH]; (3) the char-budget is confound-robust — helps whether the cause is length or method [HIGH]; (4) comprehenslation integrity = the protected-outcome umbrella [MED-HIGH].

## Phase 4 — Degrees-of-Freedom Reduction

**Fixed:** budget unit = characters (human-facing; tokens = truer internal for later); structure = the snap, not the size target; ~3500–4000 source chars = a demonstrated-safe regime → conservative per-model anchor (round DOWN; lower for smaller models), calibratable; mechanism = confounded (length + un-wired-3-Pass), char-budget robust to it; comprehenslation integrity = the protected outcome.
**Eliminated:** word-count as the unit; "char vs structure" as a real dichotomy; "3500 is a validated threshold"; "chunking replaces the 3-Pass wiring."
**Viable:** adopt a char budget (source-side primary, ~conservative anchor, per-model) as a confound-robust conservative safeguard that snaps to structure and COMPLEMENTS wiring the 3-Pass; validate the number + consider an output-side guard later.

### SV5 — Constrained
The solution space collapses to: define `chunking_budget`'s unit as **characters** (source-side, ~conservative anchor, per-model), keep structural snapping, treat it as a **confound-robust conservative safeguard complementing (not replacing) the un-wired-3-Pass fix**, protecting comprehenslation integrity. Open variables: the exact number (calibratable) + whether to also bound the output-side (the over-expansion signal).

## Phase 5 — Conceptual Stabilization

No accommodation trigger fired — perspectives converged without forcing patches; one honest residual (the exact number + output-side guard) carried as OPEN.

### SV6 — Stabilized Model

1. **THE TARGET-UNIT REFRAME (HIGH).** "Char vs structure" is a false either/or. Budget (size target) and snap (cut location) are different roles already composed in the schema (`fixed-budget-with-snap`). The user's valid, correct point: a structural LEVEL is too size-variable (~15×) to be a reliable size TARGET; a stable unit must be the target, structure stays the snap.
2. **THE MEASURE (HIGH ordering; MED char-vs-token).** Characters = the human-facing budget unit (stable, legible, feasible, language-robust); tokens = the truer-to-load internal measure for the engine later; words rejected. Source-side is the primary budget (the pre-generation control point), understood as a proxy for the whole working-set; the 2.57× over-expansion is a signal to also watch output-side.
3. **THE EVIDENCE-WEIGHT (HIGH).** The 2–3 measured points establish an existence-proof + a direction and give ~3500 real provenance (the good example's source = 4,345) — **partially lifting 04-48's "zero evidence" quarantine**. They do NOT establish a validated threshold or the mechanism (length vs un-wired-3-Pass confounded; `mistakes.md` leans method).
4. **THE CONFOUND-ROBUSTNESS (HIGH — the key survival argument).** The char-budget survives EVEN IF the mechanism is method-not-length: a smaller chunk is easier to hold ANY method over. The 4_mesele success (short, 3-Pass-not-wired, yet GOOD) is itself evidence — small size lets the un-wired method survive. This RE-CONFIRMS 04-48's complementary-not-rival and explains why the user's instinct works regardless of mechanism.
5. **COMPREHENSLATION INTEGRITY (defined, MED-HIGH).** The unified outcome — source meaning comprehended AND faithfully rendered — that the whole SKILL protects; degraded by any principle-drop (register/word-sense/harmony/Tier-1) whether from load or un-wired method. Broader than Tier-1/2 preservation (a component) and collapse-in-one-motion (a failure mode); a useful umbrella for "what's at stake."
6. **RECONCILIATION with 04-48 (HIGH).** This REFINES 04-48's "chunk by structure" → "budget in characters, snap to structure," and PARTIALLY LIFTS its magnitude quarantine (~3500 gains real provenance but stays a conservative-anchor-pending-calibration, mechanism confounded). It does not overturn 04-48; it sharpens the budget-unit and upgrades the evidence status from "zero" to "anecdotal-but-real."

**Rivals:**
- **DISSOLUTION** — PARTIALLY lands: "char vs structure" does dissolve (both coexist), leaving the contribution as "define the (untyped!) budget unit as characters + the provenance-anchor + the confound-robustness argument." Not nothing — the schema field IS untyped, so defining it is a real yield.
- **CONFOUND-COLLAPSE** — PARTIALLY lands: the evidence does NOT establish length-as-cause (that claim collapses), but the intervention survives as confound-robust (KI4), so the char-budget doesn't collapse with the mechanism claim.
- **SPURIOUS-PROXY** — addressed: char-count may be an imperfect proxy for difficulty/native-capacity, but a conservative char-budget is still a useful, cheap, stable safeguard that bounds the working-set regardless of the exact driver — not cargo-culting IF held as a conservative safeguard, not a proven cliff.

**How SV6 differs from SV1:** SV1 = "adopt char-count, set 3500." SV6 = "the dichotomy is false — budget in characters *snapping to structure*; 3500 is a **confound-robust conservative anchor** with real-but-anecdotal provenance, per-model + calibratable, **complementary to** (not a replacement for) the un-wired-3-Pass, protecting **comprehenslation integrity**; the mechanism stays confounded and the exact number + an output-side guard are OPEN."

## Telemetry
- SV delta SV1→SV6: LARGE (naive unit-swap → confound-aware, role-separated, evidence-honest, prior-reconciled model).
- Perspective saturation: reached (last perspectives confirmed, didn't add new anchor types).
- Ambiguity resolution: 4/4 resolved (3 HIGH, 1 MED-HIGH); 1 residual carried OPEN (exact number + output-side guard).
- Anchor diversity: constraints + insights + structural points + principles + meaning-nodes, from 7 perspectives incl. Phase/Calibration + Frame-exit.
- Failure modes checked: Status-quo (not protecting 04-48 — actively refined it) · Premature-stabilization (4 perspectives produced new anchors; confound tested hard) · Anchor-dominance (no single pillar — reframe + evidence + robustness + concept are independent) · Clean-resolution (the confound-collapse counter was tested structurally, not dismissed) · Self-reference (evaluating a translation-budget, not the discipline) · Perspective-blindness (checked the uncomfortable one — the confound-collapse rival that could have dissolved the whole claim).
