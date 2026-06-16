---
status: active
model: claude-opus-4-7[1m]
effort: max
---
# Finding: Target-Side Accidental Polysemy — Diagnosis + Layered Fix

## Question

**From `_branch.md`.** During translation of `mytrasnlations/asayi_musa/4_mesele.md` under the casual-reader config (A4=casual / A5=lightly-domesticated / A6=standard / A7=standard / A8=none), the Turkish phrase `Herkesin İman mukabilinde... Davası başına açılmış` was rendered as English `For every person, set against his Faith, a Case has been opened`. The Turkish `mukabil` means *facing / in exchange for / put up against [as the second side of a barter or stake]* — Nursi's sustained legal-courtroom metaphor: Faith is the *stake* the person puts up, with the eternal estate as the prize. But the English `set against his Faith` naturally reads as *in opposition to / hostile to his Faith* — the OPPOSITE of the source's direction.

The user asked two questions: (1) what mechanism in the existing framework (harmony_layer.md / notes.md / advanced_principles.md / canonical Layer 1 spec at config_base_source.md) was at fault for not catching this? (2) how do we prevent further similar cases? Specifically: is the issue with harmony_layer.md or notes.md? Which part?

**Goal.** Precise diagnosis (named failure mode + located gap + clear gap analysis) + concrete prevention proposal (proposed principle text + which artifact + translator check procedure + invariant policy). Should answer the user's specific harmony_layer-vs-notes question structurally — not deflect, not shrug, not pick one. The user will apply the fix to the framework.

## Finding Summary

- **The failure mode has a canonical name: `target-side accidental polysemy` (general) with high-severity subcase `direction-flip leakage`.** The general name captures: target rendering admits a sense the source does not admit. The subcase captures the worst case: target admits an OPPOSITE-direction reading (in-favor-of vs against / with vs without / in-exchange-for vs in-opposition-to). Direction-flip is structurally worse than mere ambiguity because it produces ACTIVELY WRONG comprehension, not just under-completeness.

- **Structural diagnosis: existing framework principles all operate SOURCE→TARGET (preserve); the missing principle operates TARGET→SOURCE (verify).** Every existing principle (multi-meaning preservation, polysemy-via-local-construction, register-alternation preservation, nazm preservation, no-smoothing, the 3-Pass methodology, the Tier 1–4 system, all of advanced_principles.md) checks "did target preserve the source's meaning?" The missing principle is its inverse: "did target admit a meaning the source does not have?" That direction was never specified anywhere in the framework. The notes.md entry "On polysemy and the local-construction trump" is the *structural inverse* of what was missing: it handles SOURCE-side polysemy disambiguation (which sense the source means); its inverse-counterpart handles TARGET-side accidental polysemy elimination (which sense the target accidentally adds).

- **Why the existing principles missed this specific case, in three parts:**
  1. The 3-Pass methodology's Pass 3 check is UNIDIRECTIONAL — "did target preserve source meaning?" The chosen `set against` technically preserves the in-exchange-for sense (it's one valid reading), so the unidirectional check fires "preserved." It never asks "does target ALSO admit a reading source doesn't?"
  2. The hard constraint *"Adding information not present in the original is forbidden"* could in principle have caught it — opening a negation/opposition reading IS adding information — but its operative scope is "don't INSERT content into the translation," not "don't let chosen wording CARRY content as a SIDE EFFECT." The translator (me) read the constraint at its operative scope; the side effect slipped through.
  3. `notes.md` has rich source-side polysemy principles but ZERO target-side accidental-polysemy principles. The symmetric inverse slot was empty.

- **Direct answer to your question — `harmony_layer.md` or `notes.md`? Which part?** **BOTH**, layered by what each artifact owns:
  - **`notes.md` owns the PRINCIPLE (the WHY/WHAT).** A new entry — *"On target-side accidental polysemy and direction-flip risk"* — placed immediately after *"On polysemy and the local-construction trump"* so the symmetric-inverse pairing is visible to any future reader.
  - **`harmony_layer.md` owns the OPERATIONAL CHECK (the HOW).** Two additions: (a) the hard-constraint list gets refined so *"Adding information not present in the original is forbidden"* explicitly covers target-rendering side-effects; (b) a new **Pass 3.5 — Reverse-Read Verification** sub-section is added under Pass 3, specifying the 6-step verification procedure.
  - **`advanced_principles.md` owns the WORKED EXAMPLE** — the `mukabil`/`set against` case walked through all 6 Pass 3.5 steps, plus an English-side parallel illustration (à la the "teacher" istilzam example).
  - **`config_base_source.md` (canonical Layer 1 spec) owns the INVARIANT POLICY** — v1.0 → v1.1 increment adding a 6th Layer 2 always-on policy *"Target-side accidental polysemy prevention,"* cross-referenced to no-smoothing as bidirectional dual.

- **Pass 3.5 Reverse-Read — the 6-step procedure.** For each phrase rendered at Pass 3:
  1. Set aside the source.
  2. Read the target rendering as a fresh target-language reader would; enumerate the readings it naturally admits.
  3. Compare to the readings the source admits.
  4. For each target reading not in source set: would a target reader land on this reading? If yes, the rendering is open to that reading.
  5. **Direction-flip emphasis** (dedicated sub-step): does any unintended target reading reverse the source's direction? Direction-flip is the highest-severity subcase.
  6. If unintended readings exist (especially direction-flip), re-render with a target phrase that eliminates the false readings while preserving source meaning.

- **The new policy is anchored in the same project value as no-smoothing, cross-referenced as bidirectional dual.** No-smoothing prevents UNDER-translation via source-smoothing (don't smooth source's awkwardness away). Target-side accidental polysemy prevention prevents OVER-translation via target-smoothing (don't let idiomatic target choice carry meaning source doesn't have). Both protect against surface-form-preferences distorting meaning; both are project-values invariants; both belong at Layer 2.

- **The A5=lightly-domesticated config did NOT fail.** A5 operated as specified — it permits narrow target-naturalization where source-fidelity isn't load-bearing. The translator (me) judged "set against" as a narrow naturalization; that judgment was wrong because the directional semantics ARE load-bearing. But A5 wasn't the failure; the missing GATING CHECK on A5's narrow-naturalization decisions is the failure. The new policy is exactly that missing gate.

- **The user's stored memory should get an inverse counterpart.** A new memory file `feedback_translation_polysemy_target_side` (separate from the existing `feedback_translation_polysemy`) preserves the source-side ↔ target-side symmetric pairing visually and ensures the principle persists across sessions.

- **The companion `deathbed-room` case (the `sekerat` mistranslation) is OUT OF SCOPE.** It is a *different* failure mode — failure to APPLY an existing principle (KEEP-SOURCE-TERM-WITH-GLOSS for a load-bearing source-specific technical term) versus this inquiry's failure to HAVE applicable principle. Flagged for a separate inquiry.

## Finding

### 1. The failure mode named + structural diagnosis

#### 1.1 The two-part name

**Target-side accidental polysemy** — the general failure mode. *Target rendering admits a sense the source does not admit.* Distinguished from:
- Source-side polysemy (notes.md "On polysemy and the local-construction trump") — multiple valid senses IN the source, where local construction picks the intended.
- Source-side multi-meaning preservation (canonical Layer 1 spec Layer 2 policy 1) — multiple simultaneously-valid source senses, preserved across translation.
- Target-side intentional polysemy — when the target's polysemy MIRRORS the source's polysemy (legitimate; not a failure).

**Direction-flip leakage** — the high-severity subcase. *Target rendering admits a reading that REVERSES the source's direction* (in-favor-of vs against / with vs without / in-exchange-for vs in-opposition-to / cause vs effect / for-the-sake-of vs at-the-expense-of). Worse than non-direction-flip accidental polysemy because the reader can land on the INVERSE meaning instead of just an under-specified meaning. Worth a dedicated check beyond the general check.

The two-part name mirrors the operational structure of the prevention check: a general "does target admit unintended readings?" step plus a dedicated "is any unintended reading in opposite direction?" sub-step.

#### 1.2 The structural inverse argument

Every load-bearing principle in the existing framework runs SOURCE→TARGET (preserve source content / structure / meaning in the target):
- `harmony_layer.md` 3-Pass methodology: Meaning Lock → Harmony Map → Target Reconstruction. All three preserve source.
- `harmony_layer.md` Tier 1–4 system: each tier ranks what source-side features must be preserved.
- `harmony_layer.md` hard constraints: "Adding information not present in the original is forbidden / Removing information present in the original is forbidden / Changing semantic content is forbidden." All three address source-preservation.
- `notes.md` "On polysemy and the local-construction trump": source-side polysemy → local construction picks the source's intended sense.
- `notes.md` "On a single word carrying multiple valid readings simultaneously" (`din`): preserve source's multi-meaning in target.
- `advanced_principles.md` istilzam chains: ensure source's unpacked entailments survive into target.
- `config_base_source.md` Layer 2 policies (5 of them): all preserve source-side features.

There is no principle anywhere in the framework that runs TARGET→SOURCE (verify target doesn't have additions absent in source). The structural inverse slot is empty. That's the gap.

The new principle fills it. It is the symmetric inverse of the existing source-side polysemy principle:

| Source-side polysemy preservation (existing) | Target-side accidental polysemy prevention (new) |
|---|---|
| When source word has multiple senses, local construction picks intended sense; if construction permits multiple, preserve all. | When target rendering admits multiple senses (especially in opposite direction to source), source's intended direction picks the sense; target idiom momentum doesn't override; unintended target-admitted readings must be eliminated. |
| Operates source-side: disambiguate IN. | Operates target-side: disambiguate OUT. |

#### 1.3 Why the existing principles missed this specific case

Three precise reasons:

1. **The 3-Pass Pass 3 check is unidirectional.** Pass 3 asks "did target preserve source meaning?" `Set against` technically preserves the in-exchange-for sense (it's one available reading); the check fires "preserved." Pass 3 never asks "does target ALSO admit a reading source doesn't?" The reverse-direction check was missing.

2. **The hard constraint's operative scope was too narrow.** *"Adding information not present in the original is forbidden"* could have caught this — opening an opposition reading IS adding information (a negation that wasn't there). But the operative scope is "don't INSERT new content," not "don't let the chosen wording CARRY content as a side effect." The translator read the constraint at its operative scope.

3. **`notes.md` had no inverse counterpart.** The source-side polysemy principle is documented (and recorded in user memory `feedback_translation_polysemy`); the target-side inverse-counterpart slot was empty. With nothing to apply, the failure went undetected.

### 2. Pass 3.5 — Reverse-Read Verification (the 6-step operational check)

The prevention mechanism is a verification sub-step that fits between Pass 3 (target reconstruction) and the harmony report. It is named Pass 3.5 — Reverse-Read because it preserves the 3-Pass methodology's identity (it's a sub-step of Pass 3, not a new pass) while making the verification visible.

For each phrase the translator renders at Pass 3:

1. **Set aside the source.** Cover the source side. The check is target-only.
2. **Enumerate target readings.** Read the target rendering as a fresh target-language reader would (one with no source access). List the readings the rendering naturally admits in the target language.
3. **Source-set comparison.** Now look at the source. Enumerate the readings the source admits.
4. **Unintended-reading test.** For each target reading not in source set, ask: would a target reader actually land on this reading? (Plausibility test in the target language.) If yes, the rendering is open to that reading.
5. **Direction-flip emphasis.** Dedicated sub-step: of the unintended target readings, does any reverse the source's direction? (In-favor-of vs against / with vs without / in-exchange-for vs in-opposition-to / cause vs effect / for-the-sake-of vs at-the-expense-of.) Direction-flip is the high-severity subcase.
6. **Re-render if needed.** If unintended readings exist (especially direction-flip), re-render with a target phrase that eliminates the false readings while preserving source meaning.

**Worked example: `İman mukabilinde` → `set against his Faith` → re-render.**

| Step | Result |
|---|---|
| 1. Set aside source | (covered) |
| 2. Enumerate target readings of *"set against his Faith"* | (a) "in opposition to his Faith" — primary natural English reading; (b) "with his Faith as the counter-stake" — secondary archaic/idiomatic reading |
| 3. Source's admitted readings | "with Faith as counter-stake / in exchange for Faith" — singular |
| 4. Unintended-reading test | reading (a) "in opposition to his Faith" — yes, target reader lands on this reading; NOT in source set. UNINTENDED. |
| 5. Direction-flip check | reading (a) reverses the source's direction (in-exchange-for → in-opposition-to). **Direction-flip. High severity.** |
| 6. Re-render | "with his Faith put up as the stake" / "with his Faith as what he stakes against the prize" / "Faith being the price-tag of" — any of these eliminates the opposition reading while preserving in-exchange-for sense. |

**Scope:** the check applies at any level — word / phrase / clause / sentence. The example is phrase-level, but word-level direction-flip is also possible (rare but real).

### 3. Layered fix — what to change in each artifact

The fix is layered across four artifacts plus a user-memory file. Each artifact owns its layer; together they compose into a complete prevention mechanism.

#### 3.1 `notes.md` — the PRINCIPLE entry (WHY/WHAT)

Add a new entry immediately after the existing *"On polysemy and the local-construction trump"* so the symmetric-inverse pairing is visible. Proposed text:

> **On target-side accidental polysemy and direction-flip risk:**
> The structural inverse of the local-construction trump. When the target rendering of a source phrase opens a reading that the source does not — especially when the target reading is the OPPOSITE of the source meaning — the target rendering has introduced a false ambiguity that the translator must eliminate. *Test:* read the target as a fresh target-language reader; enumerate the readings it admits; compare to source's admitted readings; if any target reading is unintended (and especially if it reverses the source's direction), re-render. The direction-flip subcase (target admits in-favor-of when source says against, or in-exchange-for when source says in-opposition-to, or with when source says without, etc.) is the high-severity failure mode — it produces actively WRONG comprehension rather than just under-completeness. Apply at Pass 3.5 — Reverse-Read Verification (see `harmony_layer.md`). Cross-referenced to no-smoothing as bidirectional dual: no-smoothing prevents under-translation by retaining source-side awkwardness; this prevents over-translation by retaining target-side rigor against accidental sense-addition.

#### 3.2 `harmony_layer.md` — the OPERATIONAL CHECK (HOW)

Two additions.

**3.2.a Hard-constraint refinement.** The existing hard constraint *"Adding information not present in the original is forbidden"* gets explicitly extended in scope:

> "Adding information not present in the original is forbidden — *including* information added as a SIDE EFFECT of the target rendering opening a reading the source does not admit (especially OPPOSITE-direction readings). The target rendering must not admit a sense the source does not. Admitting an unintended sense at the target side is functionally identical to adding information."

**3.2.b New sub-section: Pass 3.5 — Reverse-Read Verification.** Insert immediately after the Pass 3 description. Contents: the 6-step procedure from Section 2 above. Cross-reference: notes.md principle entry for the WHY; canonical Layer 1 spec v1.1 Layer 2 policy 6 for the invariant.

#### 3.3 `advanced_principles.md` — the WORKED EXAMPLE

Add a new extended-example entry illustrating the principle in operation. Proposed content:

- The `İman mukabilinde` → `set against his Faith` case walked through all 6 Pass 3.5 steps (per Section 2's worked example table).
- An English-side parallel illustration (à la the istilzam "teacher" example) showing target-side direction-flip in a non-Nursi case — e.g., translating Russian "за" (which can mean both "for" and "behind") into English requires the Pass 3.5 check because English "behind" has no for-the-sake-of sense.
- Composes-with statement: how the new principle interacts with source-side polysemy preservation (they are duals; both must fire), with no-smoothing (bidirectional companion), and with the 3-Pass methodology (extends Pass 3).

#### 3.4 `config_base_source.md` (canonical Layer 1 spec) — the INVARIANT POLICY

Version bump v1.0 → v1.1. Changelog entry:

> **v1.1 (2026-06-08):** Added 6th Layer 2 always-on policy "Target-side accidental polysemy prevention" triggered by the `set against his Faith` translation failure in `mytrasnlations/asayi_musa/4_mesele_en.md`. Layered fix: `notes.md` principle entry, `harmony_layer.md` Pass 3.5 Reverse-Read check + hard-constraint refinement, `advanced_principles.md` worked example. Cross-referenced to no-smoothing as bidirectional dual. Policy interaction map expanded 5 × 8 = 40 cells → 6 × 8 = 48 cells. Diagnosis inquiry: `devdocs/inquiries/2026-06-08_01-36__diagnose_target_side_direction_flip/finding.md`.

The 6th policy entry in the Patterns Compendium 2.9 ("Multi-meaning three-layer treatment") policy list:

> **(6) Target-side accidental polysemy prevention** — target rendering must not admit a reading the source does not admit, especially OPPOSITE-direction readings. The Pass 3.5 Reverse-Read check enforces. Cross-referenced to no-smoothing as bidirectional dual. INVARIANT across all 8 axes.

The 6 × 8 policy interaction map gets 8 new cells (the 6th policy row × the 8 axes columns). Following the no-smoothing pattern, the cells are likely:

| | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 |
|---|---|---|---|---|---|---|---|---|
| Target-side accidental polysemy prevention | INVARIANT | INVARIANT | INVARIANT | INVARIANT | INVARIANT (gates A5's narrow-naturalization decisions) | INVARIANT | INVARIANT | INVARIANT |

INVARIANT across all axes, with the A5 cell explicitly noting that the policy gates A5=lightly-domesticated's narrow-naturalization decisions.

#### 3.5 User stored memory — cross-session persistence

New memory file: `/Users/ns/.claude/projects/-Users-ns-Desktop-projects-comprehenslate/memory/feedback_translation_polysemy_target_side.md`

Frontmatter:
```
---
name: feedback-translation-polysemy-target-side
description: When a target rendering admits a sense the source doesn't admit (especially an OPPOSITE-direction sense), eliminate the false sense via target-side disambiguation. Inverse counterpart of feedback_translation_polysemy.
metadata:
  type: feedback
---
```

Body (concise):
> When the target rendering opens a reading the source does not admit — especially when that reading is in the OPPOSITE direction (in-favor-of vs against / with vs without / in-exchange-for vs in-opposition-to) — re-render to eliminate the false target reading while preserving source meaning. **Why:** the 2026-06-08 `set against his Faith` mistranslation in 4_mesele_en.md (Turkish `İman mukabilinde` = "with Faith put up as the stake" rendered as English admitting "in opposition to his Faith" — opposite direction). **How to apply:** at Pass 3 (target reconstruction), run the Pass 3.5 Reverse-Read check before committing: read target as a fresh reader, enumerate readings, compare to source set, eliminate unintended (especially direction-flip). Structural inverse of [[feedback-translation-polysemy]] (which addresses source-side polysemy disambiguation).

MEMORY.md index entry added.

### 4. A5=lightly-domesticated didn't fail

The user's translation was configured with A5=lightly-domesticated. The MVLw inquiry surfaced and sensemaking confirmed: **A5 operated exactly as specified**. The A5=lightly-domesticated stance permits *narrow target-naturalization where source-fidelity isn't load-bearing*. The translator (me) judged that "set against" was a narrow naturalization, deciding the in-exchange-for sense survived. The judgment was wrong because the directional semantics ARE load-bearing — Nursi's sustained courtroom metaphor depends on the in-exchange-for direction. But A5's permission was not the failure. The failure was that there was no GATING CHECK on A5's narrow-naturalization decisions. The new policy + Pass 3.5 Reverse-Read IS that gate. With the gate in place, A5=lightly-domesticated continues to operate as specified, but its narrow-naturalization decisions get verified before committing.

### 5. Companion `deathbed-room` case is out of scope (different failure mode)

The conversation that prompted this MVLw inquiry also discussed a second translation failure in 4_mesele_en.md: the rendering of Turkish `sekerat` (death-agonies — a STATE/MOMENT in Islamic theological terminology) as English `deathbed-room` (a physical location compound that doesn't exist in English). This is a *structurally different* failure mode:

- **`set against his Faith` failure (this inquiry):** failure to HAVE applicable principle. The framework had no target-side accidental polysemy principle; the principle slot was empty.
- **`deathbed-room` failure (separate inquiry):** failure to APPLY existing principle. The framework HAS the KEEP-SOURCE-TERM-WITH-GLOSS principle for load-bearing source-specific technical terms; `sekerat` is exactly that kind of term; the principle didn't fire at translation time.

Mixing the two failure modes in one diagnosis dilutes both. The user's MVLw scope was explicitly the set-against case. The `deathbed-room` failure is flagged for a separate diagnostic inquiry — see Next Actions COULD.

## Next Actions

### MUST

- **What:** Add the new principle entry to `notes.md` per Section 3.1.
  **Who:** User (manual edit).
  **Gate:** observable — immediate, since the inquiry's prevention mechanism depends on it.
  **Why:** notes.md is the conceptual home; without the principle entry, the fix has no WHY/WHAT documentation.

- **What:** Add the hard-constraint refinement + new Pass 3.5 Reverse-Read sub-section to `harmony_layer.md` per Section 3.2.
  **Who:** User (manual edit).
  **Gate:** observable — immediate.
  **Why:** harmony_layer.md is the operational home; without the Pass 3.5 sub-section, future translations have no procedure to run.

- **What:** Add the worked example to `advanced_principles.md` per Section 3.3.
  **Who:** User (manual edit).
  **Gate:** observable — immediate.
  **Why:** the worked example bridges the conceptual (notes.md) and the operational (harmony_layer.md); without it, future translators (AI or human) lack a concrete illustration.

- **What:** Increment canonical Layer 1 spec `config_base_source.md` from v1.0 to v1.1 with the 6th Layer 2 policy + Changelog entry + 8 new policy-interaction-map cells per Section 3.4.
  **Who:** User (manual edit).
  **Gate:** observable — immediate.
  **Why:** without the v1.1 increment, the principle isn't an INVARIANT policy; could be skipped under certain user-axis configurations. As corruption-prevention, the principle belongs at Layer 2.

- **What:** Create the new user stored memory file `feedback_translation_polysemy_target_side.md` per Section 3.5; update MEMORY.md index.
  **Who:** User (or AI on user's behalf).
  **Gate:** observable — immediate.
  **Why:** persists the principle across sessions; matches the existing `feedback_translation_polysemy` source-side counterpart.

- **What:** Re-render the `set against his Faith` passage in `mytrasnlations/asayi_musa/4_mesele_en.md` using the new Pass 3.5 Reverse-Read check.
  **Who:** User (or AI on user's request).
  **Gate:** observable — when the user wants the translation cleaned up.
  **Why:** the specific failure that prompted this inquiry should be fixed in the actual artifact.

### COULD

- **What:** Run a separate diagnostic inquiry on the `deathbed-room` failure (Turkish `sekerat` rendered as `deathbed-room`).
  **Who:** future `/MVLw` inquiry.
  **Gate:** condition-bound — when the user wants the deathbed-room case diagnosed too.
  **Why:** different failure mode (failure-to-APPLY vs failure-to-HAVE applicable principle); needs its own targeted treatment around when KEEP-SOURCE-TERM-WITH-GLOSS should fire for load-bearing source-specific technical terms.

- **What:** Apply the same bidirectional-by-design pattern to other source-side principles in the framework. Specifically, examine whether register-alternation preservation / nazm preservation / multi-meaning preservation each need target-side counterparts (target shouldn't add register-alternation source doesn't have / target shouldn't add nazm structures source doesn't have / target shouldn't add multi-meaning source doesn't have).
  **Who:** future inquiries.
  **Gate:** condition-bound — when a real translation failure surfaces for any of these.
  **Why:** the structural diagnosis (existing principles all source→target; missing target→source counterparts) is general; this inquiry's polysemy fix is the FIRST instance of a broader pattern.
  **Depends-on:** MUST items above must resolve first (establishes the pattern).

- **What:** AI-runtime adaptive Pass 3.5 — the AI learns high-risk target phrases (those with directional dual senses) from past corrections; maintains a learned blacklist for fast-path checking.
  **Who:** long-horizon research.
  **Gate:** condition-bound — when corpus of corrections is large enough.
  **Why:** speeds the Pass 3.5 check on familiar high-risk phrases.

### DEFERRED

- **What:** Bidirectional-by-design framework redesign — pair every source-side principle with its target-side counterpart as a v1.2/v1.3 incremental project.
  **Gate:** revival when N≥3 failure cases like `set against his Faith` are observed (i.e., when the broader pattern is empirically confirmed).
  **Why (if revived):** completes the symmetric-inverse architecture the polysemy fix opens.

- **What:** Per-target-language high-risk-phrase compendium (English phrases with directional dual senses; Russian phrases with directional dual senses; etc.).
  **Gate:** revival when Comprehenslate adds a second target language.
  **Why (if revived):** per-target-language operational anchors for the Pass 3.5 check.

## Reasoning

### Why "BOTH, layered" not "pick one"

The user's framing was binary — harmony_layer.md OR notes.md, which part? The structural answer is that neither owns the whole fix; each owns a layer. notes.md is the conceptual home (style: principle + reasoning + Comprehenslate application). harmony_layer.md is the operational home (style: mechanism spec + tier system + hard constraints). A complete fix lives in BOTH because the principle (WHY/WHAT) lives in notes.md style and the operational check (HOW) lives in harmony_layer.md style. Picking one would either give the principle without enforcement (notes.md alone) or give enforcement without conceptual grounding (harmony_layer.md alone). The original failure happened DESPITE the related notes.md polysemy principle being known — proving that operational check is needed beyond conceptual home.

### Why a STANDALONE policy rather than extending no-smoothing

Sensemaking considered: could the new principle be folded into no-smoothing as a bidirectional extension ("no-smoothing applies both ways: don't smooth source's awkwardness; don't let target's idiomatic smoothness add false readings")? The answer is NO because the failure mechanisms are different:
- No-smoothing's mechanism is "translator's instinct to make output cleaner removes source content" — prevents under-translation.
- Target-side accidental polysemy's mechanism is "translator's instinct to choose idiomatic target phrases inadvertently adds target content" — prevents over-translation.

Different mechanisms → different policies. Same underlying value (don't let surface preferences distort meaning) → cross-referenced as bidirectional dual but kept structurally separate.

### Why v1.1 increment (not skip canonical spec)

Sensemaking considered: skip the canonical-spec increment; principle + operational check in notes.md + harmony_layer.md suffices. Rejected because without the spec increment, the principle isn't an INVARIANT policy — it could be skipped under certain user-axis configurations. As corruption-prevention (same character as no-smoothing — actively WRONG comprehension at stake when direction-flips), the principle belongs at Layer 2 invariant. v1.0 just landed yesterday, and the Changelog system EXPLICITLY anticipates "if real translations reveal..." refinement triggers. This case is exactly such a trigger; the increment is healthy framework evolution.

### Why two-part name not single name

Sensemaking considered: "target-side false-friend" alone (single name) or "direction-flip" alone (single name). Single-name "target-side false-friend" is too narrow because "false friend" in linguistics usually means cross-language word-similarity-different-meaning; here the failure is target-INTERNAL ambiguity. Single-name "direction-flip" is too narrow because it misses non-direction-flip unintended target readings (e.g., target admits a benign extra reading that should also be eliminated). Two-part name preserves both: "target-side accidental polysemy" is the general failure mode; "direction-flip leakage" is the high-severity subcase. The two-part structure mirrors the operational structure of the prevention check (general check + dedicated direction-flip emphasis).

### Why not include the deathbed-room case

Sensemaking considered: include both failure cases in one diagnosis. Rejected because they are structurally different. The `set against` failure is failure-to-HAVE applicable principle (the inverse principle slot was empty). The `deathbed-room` failure is failure-to-APPLY existing principle (KEEP-SOURCE-TERM-WITH-GLOSS exists in the framework but didn't fire at the load-bearing technical term `sekerat`). Mixing them dilutes both diagnoses and both fixes. The user's MVLw scope was explicitly the set-against case; respecting that scope preserves diagnostic precision. Companion case flagged for separate inquiry.

### Bidirectional-by-design as the broader pattern

This inquiry's fix is the FIRST instance of a broader pattern: every source-side principle in the framework may need a target-side counterpart. The polysemy fix demonstrates the pattern for one principle (multi-meaning preservation / polysemy-via-local-construction). Future instances might include: register-alternation source-side preservation paired with target-side counterpart (don't smooth source register variation; don't add register variation source doesn't have); nazm source-side preservation paired with target-side counterpart (don't lose source's structural rhythm; don't impose target structural rhythm source doesn't have). The bidirectional-by-design redesign is the LONG-HORIZON v1.2/v1.3 project that this v1.1 increment opens. Deferred to revival when N≥3 cases confirm the pattern empirically.

## Open Questions

### Monitoring

- After the layered fix is implemented and a few new translations run, does Pass 3.5 catch additional target-side accidental polysemy cases? Calibration of the operational check's hit rate.
- Does the direction-flip subcase emphasis catch most high-severity failures, or do non-direction-flip unintended readings also surface as real failures?

### Blocked

- Bidirectional-by-design framework redesign (v1.2/v1.3) blocked by N≥3 empirical confirmation of the pattern.

### Research Frontiers

- AI-runtime adaptive Pass 3.5 (learned high-risk phrase blacklist).
- Per-target-language high-risk-phrase compendium.
- Whether other source-side principles (register-alternation, nazm, multi-meaning) have analogous failure cases.

### Refinement Triggers

- If the operational check turns out to be too heavy at runtime (every phrase reverse-read is expensive), consider selective application to load-bearing phrases only.
- If non-direction-flip unintended readings turn out to be the more common failure (not direction-flip), revisit the subcase emphasis.
- If multiple analogous failure cases surface for register-alternation / nazm / multi-meaning, promote the bidirectional-by-design redesign from DEFERRED to MUST.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
we discussed 

For every person, set against his Faith,                                                                                                  

  what this means ?                                                                                                                         

  (dont make any edits just tell me)                                                                                                        

⏺ The Turkish source is Herkesin İman mukabilinde... bir tarla ve mülkü kazanmak veya kaybetmek Davası başına açılmış.

  The phrase doing the work is İman mukabilinde. Mukabil means facing, in exchange for, in return for, put up against — like the second side
  of a barter or a stake in a bet. It does not mean "opposed to / hostile to."

  So Nursi's intended sense is:

  ▎ With his Faith put up as the stake — Faith being what each person is offering against the prize — a Case has been opened in which he 
  ▎ either wins or loses an eternal estate the size of the Earth.

  The legal-courtroom metaphor is sustained: there's a Case, there's a prize (the eternal estate), and there's the currency you put up as
  your side of the trade — that currency is your Faith. If you have valid Faith (the "Faith-Certificate firmly in hand," as the next
  sentence says), you win the estate. If you don't have it, you lose.

  My English set against his Faith is ambiguous and that's a real problem — in English set against more naturally reads as opposed to / 
  hostile to, which is the opposite of what the Turkish means. A cleaner rendering of the same meaning would be something like with his 
  Faith put up as the stake or with his Faith as what he stakes against the prize or Faith being the price-tag of — anything that keeps the
  in-exchange-for sense rather than letting the reader hear in-opposition-to.

i want to identify what mechanism is fault of not catching that...  and how can we prevent further similar cases..
is the issue with harmony_layer.md or notes.md ? what part?
```

</details>
