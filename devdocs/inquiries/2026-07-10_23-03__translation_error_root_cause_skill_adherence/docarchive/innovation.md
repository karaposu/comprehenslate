# Innovation — Enforcement-Point Designs for the Verification-Shaped Error Class

## User Input

`_branch.md` (root-cause diagnostic). Generate ideas primarily for reach pieces **D** (prevention mechanism) and **E** (SKILL-repair) from `decomposition.md`, plus any non-obvious re-framings of the diagnosis itself. **Settled ground (not re-derived):** the 7 errors are verification-shaped principles left un-fired by a single fluency-first pass; the fix must be SCOPED (volume pressure); the SKILL contains the antidotes but has no enforcement point (`SKILL.md` Step 5 monolithic emit; `harmony_layer.md` 3-Pass un-gated). Governing clauses in `surfacing.md`; severity spectrum in `articulate_warm.md`. Produce candidate designs for HOW to add a render-time enforcement point so this error-class is caught before emit — spanning cheap/scoped to structural/SKILL-embedded. Save to `innovation.md`.

---

## Phase 1 — Seed

**Seed (Gap + Failure type):** *An enforcement point should exist between draft and emit — a place where verification-shaped principles fire — but the workflow has none. Design it, across a cost/depth range.*

The seed is well-constrained by upstream (Sensemaking SV5: solution space = "enforcement-mechanism designs … grounded in 'the knowledge exists but has no execution point'"). Innovation's job is coverage of that constrained space, not re-opening it.

### Methodology-Mode Consideration (seed-time)

- **(a) Inherited mode:** **Standard default** (balanced 4G + 3F; "produce candidate designs" = elaborate/produce ship-ready output) — carrying a *breadth-on-one-axis* rider ("spanning cheap/scoped to structural/SKILL-embedded").
- **(b) Alternative mode named:** **Generator-weighted exploration** (novelty-first, maximize raw candidate breadth).
- **(c) What follows under the alternative:** more exotic enforcement designs generated, each tested shallowly. But the space is *already narrowed* by settled ground (scoped, enforcement-point, verification-shaped). Unbounded Generator-weighting would spend budget producing candidates that violate the scoped/execution-point constraints and get killed at Test — low yield.
- **(d) Decision:** **Default — use the inherited Standard-default mode.** Reason: downstream Critique needs *developed, testable* candidates spanning a cost axis, not a wide shallow spread; the breadth requirement is one-axis (cost/depth), which Standard-default handles by attending to that axis during generation. Not a mode-switch; not an override.

---

## Phase 2 — Generate

Each mechanism → three variations (generic / focused / contrarian). Generators create the enforcement designs; Framers find the conditions that make them correct.

### G1 — Combination *(Generator)*

- **Generic:** enforcement-point **+ the config the user already sets** → a **config-keyed check-list**: each *active* axis emits its own scoped check (A1 → dense-vocab scan; A1-syntax → nested-clause scan; A2 → layman-word scan; Pass-1 → omission-diff). Emerges from connecting "a thing already in the workflow" (config) with "a post-draft scan."
- **Focused:** enforcement-point **+ the existing `harmony_layer` 3-Pass** → the checks aren't a *new* stage, they're the **missing content of the passes that already exist**. Omission-diff + word-sense belong in **Meaning Lock**; register-exclusion + naturalness belong in **Target Reconstruction**. Emergent: the 3-Pass stops being three names for one blur and becomes three gates each with a check payload.
- **Contrarian:** enforcement-point **+ fluency-as-signal** → a **fluency heatmap**: mark every spot where the English reads *perfectly smooth* as a *suspect* (fluency is the named driver of the error class), inverting the usual "flag the awkward bits." The smoothest sentence is the likeliest to have quietly dropped a clause.

### G2 — Absence Recognition *(Generator)*

- **Patch-level (missing):** there is **no persisted draft object** between generate and emit — the workflow goes draft→emit in one motion, so there is nothing for a check to *run against*. The missing artifact is a *named, provisional draft* the process is required to hold before emitting.
- **Redesign-level (missing, from scratch):** if the SKILL were built today, **each config axis would ship as a `(description, check)` pair**, not a description alone. `A1=conversational` currently *describes* an exclusion ("no dense-academic vocab") with no attached *procedure*. The structural absence: axes are declarative profiles with no executable verification predicate.
- **Redesign-level (already present in different form):** the verification pass **already exists — as a human behavior.** The user's own error-by-error critique against source + config *is* the missing pass, run by hand, post-hoc (Sensemaking, Human/User perspective). We are not inventing a pass; we are **migrating an existing human pass from post-hoc-external to process-internal.** What is absent is the migration, not the knowledge.

### G3 — Domain Transfer *(Generator)*

- **Generic (deliberately-different — aviation / surgery):** the **pre-emit checklist** (pilot pre-landing, WHO surgical checklist). Imported property: checklists work *because* they are short, scoped to the known killers, and read at a specific gate — **not exhaustive.** Maps exactly onto the "scoped" constraint: a 4-item pre-emit list (register / omission / word-sense / naturalness), not a re-read of 1752 config lines.
- **Focused (native-domain guard — compilers / linters):** the **linter pass.** Native to software. Imported property: checking is an *architecturally separate phase* from generation, mechanical, emitting *located* warnings keyed to rules (`"allegorical" — dense-academic token, A1 violation`). This is the native-domain source the guard requires, and it directly ratifies the diagnosis: generation-shaped vs verification-shaped ≈ *codegen vs type-check* — you never ask the generator to also be the checker.
- **Contrarian (native-domain, inverted — TDD):** **write the check before the translation.** Derive the config-keyed acceptance checklist at a new **Step 4.5**, *before* Step 5 emit — so constraints are salient during generation AND pre-committed as the post-draft gate (you cannot quietly skip a check already written down).

### G4 — Extrapolation *(Generator)*

- **Generic:** the SKILL's declarative mass only grows (more axes, policies, corpus notes). Without an enforcement architecture the declarative↔procedural gap **widens monotonically** — every new principle is one more verification-shaped clause with no execution point. At the limit, **a maximally-rich SKILL with no enforcement point ≈ a maximally-unreliable translator.** The enforcement point is what makes richness *usable*, not polish on top.
- **Focused:** extend "the human runs the pass by hand." As chunk-count grows (a whole book, many books), hand-audit doesn't scale; the human stops; the errors ship. The pass must go process-internal **before** production volume makes hand-audit infeasible — i.e., *now*, at calibration stage.
- **Contrarian:** extend "base models keep improving." Maybe fluency-bias self-corrects and the enforcement point becomes an obsolete scaffold. *(Tested — and partially fails — in Phase 3: better instruction-following raises the floor but still creates no execution point for a check-against-source in one forward pass. The fix is architectural, not capability-gated.)*

### F1 — Lens Shifting *(Framer)*

- **Generic:** current frame = "enforcement is QA burden / friction." Shift to **"the config is a promise the SKILL makes."** Under the promise-keeping lens, the check isn't added burden — it's **the only thing that makes the config non-fictional.** `A1=conversational` is a lie the SKILL tells if nothing ever checks output against it. Enforcement becomes mandatory-by-definition.
- **Focused:** shift from "catch errors" to **"give the verification-shaped principles an execution point."** Same design, re-evaluated as *completing the SKILL's own architecture*. Under this lens the minimal-correct fix is whatever lets each already-present principle fire — which argues for embedding checks in the existing 3-Pass rather than a new external QA stage. *The lens picks the fix-home.*
- **Contrarian:** shift to **the reader, not the translator.** Evaluate from the seat of the A1 lay reader who hits "allegorical" and stumbles. The check becomes experiential ("read as the configured audience; mark every stumble") not rule-based ("does this violate clause X"). Produces a **simulated-reader pass** that can catch errors no rule enumerates — precisely the "reads badly" class (err-4, err-5).

### F2 — Constraint Manipulation *(Framer)* — both directions mandatory

- **ADD (generic):** add *"the draft may not reach the user until a check-artifact exists beside it."* Forces the enforcement point into existence structurally — emit is impossible without the check. Expands the space by making the check a **deliverable, not an option.**
- **ADD (focused):** add *"one dimension per pass — look for exactly ONE error-class at a time."* The scoping constraint made mandatory; defeats saturation (you never hold the whole config at once). Counterintuitively *expands* what's catchable — a pass hunting **only** omissions (source↔draft diff, everything else ignored) catches err-2a that a holistic read glides over.
- **REMOVE (mandatory):** remove *"the translation is produced in one emit"* — the implicit monolithic-emit constraint of `SKILL.md` Step 5. **This is the root constraint:** removing it is what makes *any* post-draft pass possible; it lets draft and final be different artifacts separated by a gate (which Pass-3 "Target Reconstruction" already licenses). Second removal: *"checking = re-reading the whole SKILL"* → enables scoped checks that never reload the full config.

### F3 — Inversion *(Framer)* — depth-check + multi-axis

- **Level 1 (component):** "the translator should check its draft" → "the translator should NOT — a *separate* checker should." (Workaround: a second pass/persona.)
- **Level 2 (system, primary axis):** "something must check *after* generation" → **"nothing checks after — the constraints are enforced *during* generation, so no smooth draft to over-smooth ever exists."** System-level architectural alternative: **incremental unit-level translation with inline verification**, converting verification-shaped principles into generation-shaped ones by construction.
- **Level 3 (identity-axis):** "the draft **is** the translation" → **"the draft is NOT the translation; it is raw material the verification pass consumes."** Reconceives Step 5 as producing a *provisional draft* (never emittable); a new step produces the translation from it. **The emit-gate moves.**
- **Existence-axis:** "there are N post-hoc checks" → **"there are ZERO post-hoc checks"** — verification folded entirely into generation. Converges with Level-2. *Two competing system-level statements (fold-into-generation vs move-the-emit-gate) — the multi-axis case; both retained as the radical-structural end.*

---

## Inherited Frame Audit *(between Generate and Test)*

**Step (i) — seed's central assumption:** *"the enforcement point is a post-draft **check** (a verification pass)"* — inherited from Sensemaking SV4/SV6 ("scoped post-draft verification point").
**Challenge present?** **YES, explicit.** F3 existence-axis states the reversal ("ZERO post-hoc checks; fold verification into generation") and F3 Level-2 gives the system-level alternative (incremental inline generation). Reversal + existence-to-zero signals both fire. **The seed-level frame IS challenged → audit does not fire on it.**

**Step (ii) — piece-level commitments:**
- **Piece D** (prevention mechanism) commits an **intervention-shape** = ADD-TEST/ADD-CONTENT (append a check). Property (v) fires. Challenged? **YES** — C3 inverts the shape to REORGANIZE/REPAIR (gate the existing 3-Pass, adding no new stage); C4 inverts to REPAIR (change Step 5's emit-identity). Shape-axis inverted across the candidate set.
- **Piece E** (SKILL-repair) commits a **fix-home** (embed in Step 5 / gate the 3-Pass). Challenged? **YES** — candidates span new-step (C4) / in-3-Pass (C3) / in-generation (C5) / pre-generation (C8).
- **Settled-ground "scoped":** committed by the user + Sensemaking Ambiguity-2 at HIGH confidence. Tensioned by the holistic simulated-reader pass (F1-contrarian), and legitimately committed upstream. Recorded as **challenged-in-tension**, not un-challenged.

**Step (iv) — firing condition:** every seed-level and piece-level commitment has ≥1 explicit challenge in the candidate set. **Audit does NOT fire.** No orchestration procedure needed. *(The audit's value here was forcing the fold-into-generation alternative (C5) and the shape-inversions (C3/C4) to be generated rather than producing only post-draft-checklist variants.)*

---

## Consolidated Candidate Designs (mapped to the cost/depth axis)

The mechanism outputs collapse into 8 distinct designs. Positioned cheap→structural (the requested span):

| # | Design | Mechanisms | Cost/depth |
|---|---|---|---|
| **C1** | **Scoped self-audit checklist** appended to `SKILL.md` Step 5 — 4 checks, one dimension at a time (register-exclusion · source↔draft omission-diff · word-sense-in-context · naturalness reread) | G1-gen, G3-aviation, F2-ADD-one-dim | **cheapest** |
| **C6** | **Simulated-reader pass** — read the draft *as* the A1 lay reader; mark every stumble | F1-contrarian | cheap |
| **C7** | **Fluency heatmap** — flag the *smoothest* spots as source-infidelity suspects | G1-contrarian | cheap (heuristic) |
| **C2** | **Config-derived checks** — each *active* axis auto-emits its own check line (`axis = (description, check)`) | G2-redesign, G1-gen, G3-TDD | low-mid |
| **C8** | **Test-first checklist** — derive config-keyed checks at a new Step 4.5, *before* emit; pre-commit so it can't be skipped | G3-contrarian, F2-ADD | low-mid |
| **C3** | **Gate the existing 3-Pass** — make Meaning Lock / Harmony Map / Target Reconstruction discrete checkable steps; hang the checks on them (REORGANIZE, no new stage) | G1-focused, F1-focused | mid (edits existing structure) |
| **C4** | **Deferred emit / provisional draft** — Step 5 produces a *non-final draft*; new Step 6 produces the translation from it; emit blocked until check-artifact exists | F3-identity, F2-REMOVE, G2-patch | **structural** |
| **C5** | **Incremental unit-level generation with inline verification** — no big fluent draft; verify at unit boundaries, converting verification-shaped → generation-shaped | F3-Level-2/existence | **most structural** |

**Cost-axis coverage confirmed:** cheap (C1/C6/C7) → low-mid (C2/C8) → mid (C3) → structural (C4/C5). The requested span is populated end to end.

---

## Phase 3 — Test *(5 tests + dispositions)*

### The convergent core: **C1 + C2 + C3** → "config-keyed scoped checklist embedded in the 3-Pass"

- **Novelty:** artifact-relative PASS — checklists/linters aren't novel in the abstract, but *config-axis-derived scoped checks hung on `harmony_layer`'s existing 3-Pass* do not currently exist (surfacing confirmed Step 5 is monolithic). New **to this SKILL.**
- **Scrutiny survival:** strongest objection — *"the same fluency-biased model running a checklist on its own draft will rubber-stamp it."* Survives **with refinement:** the *scoping* is the answer — a single-dimension pass ("list source clauses ABSENT from the draft") is a different cognitive act than holistic re-reading, and the **omission-diff is near-mechanical** (zero judgment). The objection retains teeth for the *judgment* checks (register, naturalness) → answered by pairing with the **simulated-reader frame (C6)** and an **adversarial stance** ("assume there IS an error; find it"). Survives.
- **Fertility:** HIGH — C2 opens "every config axis ships with an executable check," a general architecture for the *whole* SKILL, not just these 7 errors; opens the translation-linter direction.
- **Actionability:** HIGH — concretely editable: add a verification sub-section to `SKILL.md` Step 5 or gate the 3-Pass in `harmony_layer.md`, 4 checks keyed to the surfaced clauses; token-cheap vs re-translation.
- **Mechanism independence:** reached by Combination, Domain Transfer (linter + checklist), Absence Recognition (redesign), Constraint Manipulation (one-dimension), Lens Shifting (execution-point) — **5 mechanisms.** *Shared-input caution (refinement):* several draw on the same upstream "verification-shaped" framing → convergence is partly shared-input. But the *designs* arrive from independent grounds (aviation = domain-external; config-derived = absence-driven; one-dimension = constraint-driven), so the convergence is robust, not tautological. **PASS**, shared-input flagged.

**Disposition: ACTIONABLE** (multi-mechanism convergent). This is the primary deliverable for pieces D + E.

### C4 — deferred emit *(structural end)*
Novelty HIGH (for the SKILL); survives as the **high-enforcement variant** (objection: "heavier than C1 for the same checks" — true; it buys a *hard gate*, can't emit without the pass); fertile (licenses aggressive Target Reconstruction rewrites via the "draft = raw material" reframe); actionable but higher-cost; Inversion + Constraint-REMOVE + Absence-patch (3 mechanisms). **Disposition: ACTIONABLE as the structural-end option** — the "how strong" knob (advisory C1 ↔ blocking C4).

### C5 — incremental unit-level generation *(most structural)*
**Critical scrutiny result:** strongest objection is **fatal to the pure form** — *the generation-shaped principles that WERE honored (harmony_layer Tier-1/2: ring composition, escalation, convergence, nazm) are inherently **supra-sentential**; translating sentence-by-sentence with inline checks would honor the verification-shaped principles at the cost of the generation-shaped ones — trading one error class for another.* Survives only **hybridized** (unit = passage/paragraph, verification at passage boundaries). Single-mechanism (Inversion only). **Disposition: DEFERRED with revival trigger** — *revive the passage-level-checkpoint hybrid if the post-draft checklist (C1/C3) proves unable to catch supra-sentential errors across the next 2–3 chunks.*

> **Design constraint surfaced by C5's testing (feeds back onto the ACTIONABLE core):** the verification checks must operate at **word/clause granularity** and must **not force sentence-chopping**, or they will damage the supra-sentential harmony work that currently succeeds. *The enforcement point must be scoped in dimension AND bounded in granularity.* This is a genuine finding — testing caught a way the fix could regress what works.

### C6 — simulated-reader pass
Survives as a **complement**, not a replacement: experiential frame catches "reads badly" errors (err-4, err-5) that a rule-checklist may not enumerate; cheap (one persona-framed read). Lens-shifting (mostly single-mechanism). **Disposition: ACTIONABLE-as-complement** — folds in as the *method* for C1's naturalness check.

### C8 — test-first checklist
Survives as a **strengthener**: pre-committing the config-keyed checks at Step 4.5 means the post-draft gate can't be silently skipped. Domain-Transfer + Constraint-ADD. **Disposition: ACTIONABLE-as-strengthener** — folds into C2.

### C7 — fluency heatmap
Objection has merit: fluency is the *driver* but a poor *locator* (doesn't say which smooth spot dropped a clause); flags too broadly. Survives weakly as an **attention-allocation heuristic** (spend more check-budget on the smoothest passages). Combination-only. **Disposition: DEFERRED / RESEARCH FRONTIER** — *revive fluency-weighting if missed errors cluster in the most fluent passages.*

### G4-contrarian — "better models make this obsolete"
**Fails testing (informatively):** better instruction-following raises the floor but does not create an execution point for check-against-source in a single forward pass. **Killed → becomes confirming evidence:** the fix is architectural, not capability-gated. (New-seed value: the enforcement point is durable, not a temporary scaffold.)

---

## Assembly Check

Combining the ACTIONABLE survivors yields one coherent design with emergent value:

> **"Config-keyed scoped verification gate — pre-committed, embedded in the 3-Pass, adversarially run, granularity-bounded."**
>
> 1. **Step 4.5 — pre-commit (C8 + C2):** derive a scoped checklist from the *active* config axes; each active axis emits its check line. Write it down.
> 2. **Step 5 — generate (unchanged):** produce the draft; preserve the supra-sentential harmony work.
> 3. **Step 5.5 — the gate (C1 + C3, hung on the 3-Pass):** run the checklist **one dimension at a time** against the draft —
>    - *Meaning-Lock checks:* source↔draft omission-diff (mechanical) · word-sense-in-context flags;
>    - *Target-Reconstruction checks:* register-exclusion scan · naturalness reread **via the simulated-reader frame (C6)**;
>    - *granularity bound (from C5's testing):* word/clause level only — never force sentence-chopping that breaks harmony.
> 4. **Enforcement knob (C1 ↔ C4):** advisory sub-section (cheap) **or** deferred-emit hard gate (structural, high-assurance).

**Emergent value no single piece has:** the assembly makes the config **self-enforcing** — the *same axes the user sets to configure generation automatically generate the checks that verify it.* This realizes the redesign-level absence (G2/C2: every axis becomes a `(description, check)` pair) and **inverts the Extrapolation-generic finding**: with the gate in place, the SKILL's declarative richness becomes an *asset to enforcement* (more axes = more checks = more coverage) instead of a *liability* (more axes = more un-fired principles). Richness→unreliability becomes richness→coverage. That inversion is the innovation; the checklist is merely its cheapest instantiation.

---

## Axis Coverage Check

The problem has four orthogonal axes; each has ≥1 variant (no single-axis bias):

| Axis | Variants present |
|---|---|
| **WHERE the check lives** | new external stage (C1) · in existing 3-Pass (C3) · folded into generation (C5) · before generation (C8) |
| **WHAT drives the check content** | fixed list (C1) · config-derived (C2) · reader-simulation (C6) · fluency-heuristic (C7) |
| **WHEN it fires** | post-draft (C1/C3) · pre-draft (C8) · during-draft (C5) · at-emit-gate (C4) |
| **HOW STRONG** | advisory checklist (C1) · blocking gate / required check-artifact (C4, F2-ADD) |

**PASS** — all four axes populated. The single-axis bias the check guards against (inheriting only "post-draft checklist" from upstream) did not occur.

---

## Telemetry

- **Generators applied:** 4 / 4 (Combination, Absence Recognition, Domain Transfer, Extrapolation)
- **Framers applied:** 3 / 3 (Lens Shifting, Constraint Manipulation, Inversion)
- **Coverage:** FULL (7/7), 3 variations each.
- **Convergence:** **YES** — 5 mechanisms converge on the config-keyed scoped checklist embedded in the 3-Pass (ACTIONABLE core). Divergence retained productively at the structural end (C4 move-the-gate vs C5 fold-into-generation — the multi-axis Inversion tension).
- **Survivors tested:** 8 designs + 1 killed extrapolation, all 5-tested. Dispositions: **ACTIONABLE** — assembled core (C1+C2+C3+C6+C8) and C4 (structural end); **DEFERRED w/ trigger** — C5 (passage-level hybrid), C7 (fluency-weighting).
- **Production-task refinements:** Piece D intervention-shape (ADD-TEST) **inverted** across the set (→ REORGANIZE C3, REPAIR C4/C5) — Intervention-Shape-Axis Inversion **satisfied**. Piece E fix-home **inverted** (4 WHERE-variants) — **satisfied**. Methodology-Mode Consideration recorded at seed (default, no switch).
- **Inherited Frame Audit:** examined seed-level + both piece-level commitments; every commitment carries an explicit challenge (F3 existence-axis challenges the core "post-draft check" frame) → **does not fire**; no override needed.
- **Shared-input detection:** convergence partly shares the upstream "verification-shaped" framing; ratified as robust because designs arrive from independent grounds (domain-external, absence-driven, constraint-driven). Flagged, not dismissed.
- **Failure modes observed:** none. (No premature evaluation — generate fully preceded test; no single-mechanism trap — 7/7; no early frame-lock — audit + Inversion forced the fold-into-generation alternative; grounded — every design 5-tested; no exhaustion; no survival bias — the uncomfortable C5 was tested with extra care and its fatal supra-sentential objection surfaced rather than being smoothed over.)
- **Overall: PROCEED** — full coverage, strong convergence on an ACTIONABLE assembled design, all survivors tested, cost-axis span populated end to end, one real design-constraint recovered by testing (granularity bound).
