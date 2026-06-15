# Sensemaking — diagnose_target_side_direction_flip

## User Input
`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-08_01-36__diagnose_target_side_direction_flip/_branch.md` (with surfacing output at the same folder)

---

## SV1 — Baseline Understanding

Diagnose the framework mechanism that failed to catch the `set against his Faith` mistranslation (Turkish `İman mukabilinde` = "in exchange for / put up as stake" got rendered as English admitting "in opposition to / hostile to" reading — opposite direction). Locate the gap in harmony_layer.md / notes.md / advanced_principles.md / canonical Layer 1 spec. Propose prevention mechanism.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints
- **C1** All existing framework principles operate SOURCE→TARGET (preserve source meaning in target).
- **C2** The needed principle operates TARGET→SOURCE (verify target doesn't admit unintended readings).
- **C3** The failure is at Pass 3 (target reconstruction), not Pass 1 (meaning lock).
- **C4** `mukabil` was correctly understood by translator; failure was target-language idiom choice opening false reading.
- **C5** The opposite-direction property makes this case worse than mere ambiguity (it produces ACTIVELY WRONG comprehension, not just under-completeness).
- **C6** The framework artifacts (notes.md / harmony_layer.md / advanced_principles.md / canonical Layer 1 spec at config_base_source.md) are interconnected; a fix could live in one or be layered across multiple.
- **C7** The user explicitly asked: harmony_layer.md OR notes.md? which part?
- **C8** Companion deathbed-room case is OUT OF SCOPE (different failure mode).

### Key Insights

- **KI1 — STRUCTURAL DIAGNOSIS settles.** The failure mode is **structurally inverse** to the existing source-side polysemy preservation principle. The existing principle in `notes.md` ("On polysemy and the local-construction trump") says: when SOURCE has multiple senses, local construction picks the intended one (or preserves all if construction allows). The missing principle says: when TARGET rendering accidentally admits multiple senses (especially in the OPPOSITE direction), target-side disambiguation REMOVES the false sense. The two principles are SYMMETRIC INVERSES — source-side disambiguates IN, target-side disambiguates OUT. This symmetry is the load-bearing structural fact.

- **KI2 — Why existing principles missed it (the precise structural reason).** The 3-Pass methodology's Pass 3 check is UNIDIRECTIONAL: "does target preserve source meaning?" — yes/no. The chosen "set against" technically preserves the "in-exchange-for" sense (it's one valid reading of the phrase), so the unidirectional check fires "preserved." But the check fails to ask: "does target ALSO admit a reading source doesn't?" The missing direction is REVERSE-READ. The hard constraint "Adding information not present in the original is forbidden" COULD have caught it IF interpreted maximally (opening a negation reading IS adding information), but its operative scope is "don't INSERT content into the translation" not "don't let the chosen wording CARRY content as a SIDE EFFECT." The translator (me) interpreted the constraint at its operative scope and the side-effect slipped through.

- **KI3 — Canonical name for the failure mode: "target-side accidental polysemy" with the high-severity subcase "direction-flip leakage."** The two-part name is load-bearing:
  - **target-side accidental polysemy** — the GENERAL failure mode (any case where target rendering admits a sense source doesn't admit). Symmetric vocabulary to "source-side polysemy preservation."
  - **direction-flip leakage** — the HIGH-SEVERITY subcase where the target admits an OPPOSITE-direction reading. This is structurally worse than mere ambiguity because the reader can land on the inverse meaning rather than just an under-specified meaning.

  The naming serves the structural diagnosis (KI1): the general failure mode is the inverse of the existing source-side principle; the high-severity subcase has its own name because it deserves distinct emphasis in the prevention mechanism (the check should specifically ask "is any admitted target reading in the OPPOSITE direction?").

- **KI4 — The fix is LAYERED, not single-artifact.** The user's framing "harmony_layer.md or notes.md?" is binary but the structural answer is BOTH (with `advanced_principles.md` adjacent + `canonical Layer 1 spec` optional). Layered architecture:
  - **`notes.md`** owns the PRINCIPLE entry — the WHY/WHAT. New entry: "On target-side accidental polysemy and direction-flip risk" as an explicit INVERSE COUNTERPART to "On polysemy and the local-construction trump." This is where the conceptual home lives because notes.md's style is principle-statement + reasoning + Comprehenslate-application.
  - **`harmony_layer.md`** owns the OPERATIONAL CHECK — the HOW. Two additions: (a) hard-constraint refinement extending "Adding information not present in the original is forbidden" to explicitly cover target-rendering side-effects ("the target rendering must not admit a sense the source does not admit — admitting an unintended sense is functionally identical to adding information"); (b) extending the 3-Pass methodology with a Pass 3.5 Reverse-Read step (read the target as if you don't know the source; enumerate readings; check none are unintended; check especially for OPPOSITE-direction readings). This is where the operational home lives because harmony_layer.md's style is mechanism-spec + tier-system + hard constraints.
  - **`advanced_principles.md`** (optional) owns the WORKED EXAMPLE — operational illustration with the `mukabil`/`set against` case + the istilzam/Rahman-style worked example showing how the principle composes with existing principles. This is where examples live in advanced_principles.md's style.
  - **`config_base_source.md` (canonical Layer 1 spec)** owns the INVARIANT POLICY — v1.1 increment adding a 6th Layer 2 always-on policy: "target-side accidental polysemy prevention." This is the most invasive option; whether to include it depends on whether we want this principle enforced INVARIANTLY at the policy layer (yes — it's a corruption prevention principle, the same character as no-smoothing).

  Layered architecture composes: principle in notes.md / operational check in harmony_layer.md / worked example in advanced_principles.md / invariant policy in canonical spec.

- **KI5 — The Pass 3.5 Reverse-Read check (concrete operational form).** For each phrase the translator renders at Pass 3, an additional check:
  1. **Reverse-Read.** Set aside the source. Read the target rendering as a fresh target-language reader would.
  2. **Enumerate readings.** List the readings the target rendering naturally admits in the target language. (For "set against his Faith": [a] "in opposition to his Faith" — primary natural reading; [b] "with his Faith as the counter-stake" — secondary archaic/idiomatic reading.)
  3. **Source-set comparison.** Compare the enumerated target readings to the source's admitted readings. (Source admits: "with Faith as counter-stake / in exchange for Faith" — singular reading. Source does NOT admit: "in opposition to Faith.")
  4. **Unintended-reading test.** For each target reading not in source set, ask: would a target reader land on this reading? If YES, the target rendering is open to that reading.
  5. **Direction-flip emphasis.** Specifically check: does any unintended target reading reverse the source's direction (in-favor-of vs against / with vs without / in-exchange-for vs in-opposition-to / cause vs effect)? Direction-flip is the HIGH-SEVERITY subcase.
  6. **Re-render.** If unintended readings exist (especially direction-flip), re-render with a target phrase that ELIMINATES the false readings while preserving the source meaning. (For "set against his Faith": re-render to "with his Faith put up as the stake" or "with Faith as what he stakes against the prize" — both eliminate the opposition reading.)

  This check fits between Pass 3 (initial target reconstruction) and the harmony report. Naming it Pass 3.5 keeps the 3-Pass methodology's identity while extending it.

- **KI6 — Why this principle is INVARIANT (policy layer) not just a tier-3 conditional.** Like the no-smoothing policy ("translating away awkward/uncomfortable nuance to make output 'cleaner' is itself a form of corruption — the smoothing introduces a worse error than the awkwardness it removes"), target-side accidental polysemy is INVARIANT across all axes: regardless of A1 reader-level or A4 purpose or A7 scaffolding or A8 analysis-depth, admitting an OPPOSITE-direction reading at target is corruption. It's not a feature-flag-dependent rule. It's a project-values invariant. This argues for v1.1 increment to canonical Layer 1 spec adding a 6th Layer 2 policy.

- **KI7 — The no-smoothing policy is RELATED but DIFFERENT.** No-smoothing says "don't make awkward source clean in target" — about FILTERING OUT source content. Target-side accidental polysemy says "don't let target wording carry content source didn't have" — about TARGET ADDING content. The two are duals on the smoothing axis: no-smoothing prevents under-translation; target-side accidental polysemy prevents over-translation. Both are invariant corruption-prevention policies.

- **KI8 — Self-reference check: was the choice "set against" a smoothing?** YES — partly. The plain literal would have been "in exchange for his Faith" or "with Faith as the stake." I chose "set against" because it sounded more idiomatic English. That IS a smoothing — making the awkward Turkish phrase smoother in English. So the no-smoothing policy COULD have caught this case if applied to TARGET-SIDE smoothing too. Currently no-smoothing as stated in canonical spec applies to SOURCE-SIDE smoothing (don't smooth away source awkwardness). The proposed new policy is the dual — don't smooth target in a way that adds false readings. Could be framed as: "no-smoothing applies bidirectionally: don't smooth away source meaning, AND don't smooth in a way that adds target meaning."

  Actually this raises an important sensemaking question: is the new principle (a) a STANDALONE new policy or (b) an EXTENSION of the no-smoothing policy?

  Counter-argument for (a): the failure mechanism is different. No-smoothing's mechanism is "translator's instinct to make output cleaner removes source content." Target-side accidental polysemy's mechanism is "translator's instinct to choose idiomatic target phrases inadvertently adds target content." Different mechanisms → different policies.

  Counter-argument for (b): the underlying VALUE is the same — "the form of expression has consequences for meaning; don't let surface preferences distort meaning in either direction." Different mechanisms → same value → one policy with bidirectional scope.

  Resolution: Frame as STANDALONE but ANCHORED IN the same value as no-smoothing. The new policy is "Target-side accidental polysemy prevention" — its own named policy with its own mechanism (Reverse-Read check) — but explicitly cross-referenced to no-smoothing as the dual ("no-smoothing prevents under-translation via source-smoothing; this prevents over-translation via target-smoothing"). Two named policies sharing a value.

- **KI9 — The user's stored memory `feedback_translation_polysemy` should get an inverse counterpart.** The current memory says: "when a source word is polysemous, the local construction picks the sense, not the surrounding metaphor's momentum." Inverse counterpart: "when a target rendering admits multiple senses, the source's intended direction picks the sense; target idiom momentum doesn't override; in particular, target-admitted OPPOSITE-direction senses must be eliminated." This is the meta-memory anchor; the framework principle in notes.md is the operational artifact.

- **KI10 — Companion deathbed-room failure is DIFFERENT mode (not in scope).** The deathbed-room failure (rendering `sekerat` = death-agonies as `deathbed-room`) is a failure to APPLY existing KEEP-SOURCE-TERM-WITH-GLOSS principle for a load-bearing technical term. The set-against failure is a failure to HAVE an applicable principle. These are structurally different. Out of scope for this inquiry; flag for separate inquiry. Sensemaking confirms surfacing's R11 classification.

- **KI11 — A5=lightly-domesticated didn't "fail" — it operated as specified.** The A5=lightly-domesticated stance permits narrow target-naturalization where source-fidelity isn't load-bearing. The translator (me) chose "set against" as a narrow naturalization, judging that the in-exchange-for sense survived. The judgment was wrong because target-side direction-flip wasn't checked. So A5 didn't fail; the check that would have prevented A5's narrow-naturalization from crossing the load-bearing line wasn't there. The new principle is the missing check that should fire BEFORE A5's narrow-naturalization is committed.

- **KI12 — The fix's scope: word-level, phrase-level, or both?** Surfacing R12.5 noted "scope: word-level polysemy; phrase-level multi-meaning is a separate concern" from notes.md. The `set against his Faith` case is PHRASE-LEVEL. So the new principle is explicitly PHRASE-LEVEL accidental polysemy. Word-level (where target word has multiple senses, e.g., translating "din" as "religion" loses the judgment-sense) is a different concern. The new principle should be scoped at phrase-level + clause-level.

  Actually wait, this needs more thought. The mukabil case IS word-level (mukabil → set against). The phrase-level emergence is in the English: the dual-sense isn't in the English word but in the English PHRASAL idiom "set against." So:
  - Source-side polysemy IS often word-level (din has multiple senses; mukabil has multiple senses).
  - Target-side accidental polysemy can be word-level or phrase-level, but it's USUALLY phrase-level (rare for a single English word to have an opposite sense; common for an English phrasal idiom to have an opposite sense).
  - The new principle covers BOTH word-level and phrase-level target-side accidental polysemy.

  This corrects the scope: the new principle is NOT bounded to phrase-level; it's general target-side accidental polysemy at any level.

### Structural Points
- **SP1** Canonical name: "target-side accidental polysemy" (general) / "direction-flip leakage" (high-severity subcase).
- **SP2** Layered fix: notes.md (principle) + harmony_layer.md (operational check + hard-constraint refinement) + advanced_principles.md (worked example) + canonical Layer 1 spec (v1.1 Layer 2 policy increment).
- **SP3** Pass 3.5 Reverse-Read check (6-step procedure) — operational form.
- **SP4** New principle as standalone policy anchored in same value as no-smoothing; cross-referenced as dual.
- **SP5** User's stored memory `feedback_translation_polysemy` gets inverse counterpart (separate memory or extension of existing).
- **SP6** Scope: any-level target-side accidental polysemy (word / phrase / clause).
- **SP7** Direction-flip emphasis: opposite-direction readings get explicit dedicated check beyond general accidental-polysemy check.
- **SP8** A5=lightly-domesticated didn't fail; the missing check that gates A5's narrow-naturalization is what's needed.
- **SP9** Companion deathbed-room case OUT OF SCOPE (different failure mode).
- **SP10** The hard-constraint "Adding information not present in the original is forbidden" gets refined scope: explicitly covers target-rendering side-effects.

### Foundational Principles
- **FP1** Translation principles operate in BOTH DIRECTIONS — source→target preservation AND target→source verification.
- **FP2** Target-side accidental polysemy is the structural inverse of source-side polysemy preservation; both are needed.
- **FP3** Surface-form preferences (target idiom choice) have semantic consequences; the translator's instinct to choose idiomatic target wording must be GATED by reverse-read check.
- **FP4** Direction-flip ambiguity is structurally worse than under-completeness ambiguity (produces ACTIVELY WRONG comprehension vs. under-specified comprehension).
- **FP5** Project-values invariants (no-smoothing, multi-meaning preservation, target-side accidental polysemy prevention) live at Layer 2 policy level — invariant across user-axis configurations.

### Meaning-Nodes
- **MN1** target-side accidental polysemy — the failure mode name.
- **MN2** direction-flip leakage — the high-severity subcase name.
- **MN3** Pass 3.5 Reverse-Read check — the operational prevention mechanism.
- **MN4** layered fix — principle + operational check + worked example + invariant policy.
- **MN5** structural inverse — the symmetry between source-side polysemy preservation and target-side accidental polysemy prevention.
- **MN6** no-smoothing dual — target-side smoothing prevention as the bidirectional counterpart to source-side no-smoothing.

### Meta-Inspection after SV2 (H4, H5)
- **H4 (concept names):** "Target-side accidental polysemy" reads cleanly. Has parallel structure to "source-side polysemy preservation." Symmetric inverse vocabulary. "Direction-flip leakage" is vivid and operationally specific (names the worst-case property). "Reverse-Read check" is concrete and procedure-like. PASS.
- **H5 (motivating examples):** `set against his Faith` (the anchor case) is well-defined. The principle generalizes — example shows target-phrase admitting opposite direction. Could surface additional examples (e.g., "stand for" vs "stand against") to strengthen the operational test. Sensemaking notes this for decomposition.

### SV2 — Anchor-Informed Understanding

The failure mode is "target-side accidental polysemy" with high-severity subcase "direction-flip leakage." It's the structural inverse of existing source-side polysemy preservation. Existing principles all operate SOURCE→TARGET (preserve); the missing principle operates TARGET→SOURCE (verify target doesn't admit unintended readings). Fix is LAYERED across notes.md (principle entry), harmony_layer.md (Pass 3.5 Reverse-Read check + hard-constraint refinement), advanced_principles.md (worked example), and canonical Layer 1 spec at config_base_source.md (v1.1 increment adding 6th Layer 2 policy). The new policy is anchored in same project-values invariant as no-smoothing (cross-referenced as dual). Companion deathbed-room failure OUT OF SCOPE.

---

## Phase 2 — Perspective Checking

### Technical / Logical
The structural inverse argument is clean: source-side polysemy preservation is a 1-place predicate (does target preserve source's intended sense?); target-side accidental polysemy prevention is a 1-place predicate (does target admit a sense source doesn't?). Symmetric. Both 1-place predicates can be evaluated independently. The Pass 3.5 Reverse-Read check is a deterministic 6-step procedure. Direction-flip is a well-defined subset of "unintended target readings" (those that reverse the source's direction). Logically coherent.

### Human / User
The user explicitly asked "harmony_layer.md OR notes.md? which part?" The answer is BOTH — which initially could feel like dodging the question. But the structural argument is that they own DIFFERENT layers (principle vs operational check) and a complete fix needs both. The user is sophisticated enough (they built the framework) to accept the layered answer. The answer should be EXPLICIT about why both: principle home (WHY/WHAT) is notes.md style; operational check home (HOW) is harmony_layer.md style.

### Strategic / Long-term
The canonical Layer 1 spec just went to v1.0 yesterday. Adding a Layer 2 policy = v1.1 increment. The Changelog system anticipates exactly this; it's the FIRST canonical-spec-driven refinement after the framework's closure. Establishes the pattern: real translation failures → diagnose → fix → version increment. Healthy.

### Risk / Failure
- **R1:** Over-fitting to ONE case. The "set against his Faith" case is one example; the principle generalizes but might over-fit. CORRECTIVE: principle is general (target-side accidental polysemy), not phrase-specific.
- **R2:** Pass 3.5 Reverse-Read check might be operationally heavy. For each phrase, the AI translator must reverse-read + enumerate + compare. CORRECTIVE: at A7 lower settings the check could be applied selectively (load-bearing phrases); at A7 higher it applies to all. But the policy is INVARIANT — the check must fire; A7 just modulates how many candidate phrases get checked.
- **R3:** Direction-flip emphasis might be too narrow — non-direction-flip unintended target readings (e.g., target admits a benign-but-extra reading) might also matter. CORRECTIVE: direction-flip is the HIGH-SEVERITY subcase; the general principle covers all unintended target readings; direction-flip gets dedicated check beyond general check.
- **R4:** The layered fix is structurally heavy (4 artifacts touched). Risk of partial implementation. CORRECTIVE: priority order — notes.md principle first (the conceptual anchor); harmony_layer.md operational check second (the mechanism); advanced_principles.md worked example third (optional but desirable); canonical Layer 1 spec v1.1 fourth (invariant policy — most invasive). User can implement incrementally.

### Resource / Feasibility
The Reverse-Read check is feasible for AI translator. The check is deterministic. The artifacts to update are small (4 files, modest additions). Versioning the canonical spec v1.0 → v1.1 is anticipated by the Changelog system.

### Definitional / Internal Consistency
The new principle composes with existing principles:
- Polysemy-via-local-construction (source-side) → preserved unchanged; this is its target-side dual.
- Multi-meaning preservation (source-side) → preserved unchanged; this is its target-side dual.
- No-smoothing → cross-referenced; new principle is the over-translation prevention dual.
- 3-Pass methodology → extended with Pass 3.5.
- Hard constraints → refined to explicitly cover side-effects.
- Tier 1-4 system → unaffected (tiers are source-side preservation priorities; new principle is target-side prevention).

No internal contradictions.

### Definitional / Frame-exit Completeness (GATING)
- (i) Inherited terms: YES (polysemy / local-construction / Pass 3 / hard constraint / Layer 2 policy / 3-Pass methodology all inherited).
- (ii) Used across ≥2 values: YES (polysemy used both source-side (existing) and target-side (new)).
- Gating FIRES.

1. **Existence:** "Polysemy" project-wide → source-side (existing notes.md principle + canonical spec multi-meaning-preservation policy + polysemy-via-local-construction policy) + target-side (NEW, missing). LAYER: source-side is BOTH operational principle (notes.md) AND Layer 2 invariant policy (canonical spec); target-side should match — operational principle (notes.md) + Layer 2 invariant policy (canonical spec). "Polysemy" project-wide is BIDIRECTIONAL: source-internal (multiple senses in source word/phrase) + target-internal (multiple senses in target word/phrase, especially when only one matches source). The framework currently covers source-internal exclusively.

2. **Role:** Out-of-scope: cross-language false friends (source word resembling target word with different meaning — different concept; not the inverse here). KEEP OUT. In-scope: target-internal accidental polysemy + the high-severity direction-flip subcase.

3. **Verdict Rigor:** "Layered fix (4 artifacts)" verdict:
   - Counter: minimal fix — just add to notes.md as the conceptual home; rely on translator (AI) to apply the principle without separate operational check or canonical spec increment.
   - Why fails: the original failure happened DESPITE the existing notes.md polysemy principle being known to the translator. Just adding the inverse principle to notes.md without operational check (Pass 3.5 Reverse-Read in harmony_layer.md) wouldn't have caught the case. Operational check is needed; it lives in harmony_layer.md's style. AND canonical spec increment makes it INVARIANT (not optional / not feature-flag-dependent). Layered fix is structurally justified.
   - HOLDS at HIGH.

4. **Residual:** None.

### Phase / Calibration-State
The canonical spec v1.0 is at FRAMEWORK CLOSURE state — first canonical synthesis. v1.1 increments are expected at this calibration stage as real translation failures surface. The Versioning + Inline Changelog system in canonical spec specifically anticipates "If real translations reveal..." refinement triggers. This case is exactly such a trigger. The framework is calibration-receptive at this stage.

### Ethical / Systemic
The policy is corruption-prevention. Translating away the "in-exchange-for" sense in favor of the "in-opposition-to" sense COULD invert the author's intended meaning — that's translation corruption. The project's ethical commitment (foreignization-preserving, no-smoothing, multi-meaning preservation) all share the same value: don't let target preference distort source meaning. This principle is consistent with project ethics.

### SV3 — Multi-Perspective Understanding

Confirms layered 4-artifact fix; canonical name "target-side accidental polysemy" with subcase "direction-flip leakage"; Pass 3.5 Reverse-Read check as operational form; cross-reference to no-smoothing as bidirectional dual; canonical Layer 1 spec v1.1 increment adding 6th Layer 2 policy. Frame-exit fires; gap is BIDIRECTIONAL polysemy (currently only source-side covered). Ethical alignment with project values. v1.0 → v1.1 is healthy first canonical refinement.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity A1: Canonical name for the failure mode
**Counter:** "Target-side false-friend" alone (single-word name, borrows linguistics term).
**Why partially fails:** False-friends in linguistics is usually source-vs-target (source word resembling target word with different meaning). Here the failure is target-INTERNAL (target phrase has multiple senses one of which is wrong). Confusable.
**Counter:** "Direction-flip" alone (vivid, emphasizes worst case).
**Why partially fails:** Doesn't cover non-direction-flip unintended target readings (e.g., target admits a benign extra reading that should also be prevented). Too narrow.
**Counter:** "Target-side accidental polysemy" alone.
**Why partially fails:** Misses emphasis on direction-flip subcase.
**Confidence:** HIGH
**Resolution:** Two-part name: "target-side accidental polysemy" (general failure mode) + "direction-flip leakage" (high-severity subcase). The two-part structure mirrors the operational structure (general check + dedicated direction-flip emphasis check).

### Ambiguity A2: Single-artifact vs layered fix
**Counter:** Single artifact (notes.md alone — principle entry; rely on translator to apply).
**Why fails:** Original failure happened despite related notes.md polysemy principle being known. Operational check is needed (Pass 3.5 Reverse-Read). And invariant enforcement is needed (canonical spec Layer 2 policy).
**Counter:** Single artifact (harmony_layer.md alone — operational check; skip principle entry).
**Why fails:** harmony_layer.md style is mechanism-spec; principle reasoning belongs in notes.md style; users + translators consult notes.md for the WHY.
**Counter:** Layered 4-artifact (notes.md + harmony_layer.md + advanced_principles.md + canonical spec).
**Why succeeds:** Each artifact's style owns its layer of the fix (principle / operational check / worked example / invariant policy). Composes cleanly. User explicitly asked "harmony_layer.md OR notes.md? which part?" — answer is BOTH each owning its layer.
**Confidence:** HIGH
**Resolution:** Layered 4-artifact fix.

### Ambiguity A3: Canonical Layer 1 spec v1.1 increment necessary?
**Counter:** Skip canonical spec increment; principle + operational check in notes.md + harmony_layer.md suffices.
**Why partially fails:** Without canonical spec increment, the principle isn't an INVARIANT policy; it could be skipped under certain user-axis configurations. As corruption-prevention, the principle should be invariant (like no-smoothing). Skipping the increment makes the fix optional at runtime.
**Counter:** v1.1 increment adding 6th Layer 2 policy "target-side accidental polysemy prevention."
**Why succeeds:** Makes the principle invariant; matches no-smoothing's character (project-values-invariant corruption-prevention); fits the v1.0 Changelog system's anticipated "real translations reveal" trigger.
**Confidence:** HIGH
**Resolution:** v1.1 increment adding 6th Layer 2 policy.

### Ambiguity A4: Pass 3.5 vs new Pass 4
**Counter:** Add as Pass 4 (post-Pass 3 distinct stage).
**Why partially fails:** Pass 4 implies the check is a new stage equivalent to Meaning Lock / Harmony Map / Target Reconstruction. But the check is a VERIFICATION of Pass 3, not a new methodological stage. Operationally a check sub-step.
**Counter:** Pass 3.5 (verification sub-step within Pass 3).
**Why succeeds:** Names it as Pass-3-verification while preserving the 3-Pass methodology's identity. Naming convention is clear.
**Confidence:** HIGH
**Resolution:** Pass 3.5 Reverse-Read.

### Ambiguity A5: Standalone new policy vs extension of no-smoothing
**Counter:** Extend no-smoothing to bidirectional (don't smooth source-side; don't smooth target-side).
**Why partially fails:** The failure mechanisms are different (no-smoothing prevents UNDER-translation; target-side accidental polysemy prevents OVER-translation). Conflating them under one policy loses the operational distinction. Both anchor in same value but operate via different mechanisms.
**Counter:** Standalone policy "Target-side accidental polysemy prevention" cross-referenced to no-smoothing as bidirectional dual.
**Why succeeds:** Preserves mechanism-specific naming; explicit value-anchoring via cross-reference.
**Confidence:** HIGH
**Resolution:** Standalone policy with explicit cross-reference to no-smoothing as dual.

### Ambiguity A6: Scope (phrase-level only vs any-level)
**Counter:** Phrase-level only (the `set against his Faith` case is phrasal idiom).
**Why partially fails:** Target-side accidental polysemy can also occur at word-level (rare but real — e.g., translating Hebrew "rega" as "moment" loses the eye-blink-specific sense). General principle should cover any level.
**Counter:** Any-level (word / phrase / clause / sentence).
**Why succeeds:** Generalizes the principle to all scope levels.
**Confidence:** HIGH
**Resolution:** Any-level scope (word / phrase / clause / sentence).

### Ambiguity A7: Direction-flip subcase — separate check or fold into general?
**Counter:** Fold into general unintended-target-readings check; no dedicated subcase.
**Why partially fails:** Direction-flip is structurally worse than non-direction-flip unintended readings (actively wrong vs under-specified). Dedicated check makes the high-severity property explicit and ensures translator catches it as the worst case.
**Counter:** Separate dedicated direction-flip check on top of general check.
**Why succeeds:** Operational form preserves the severity distinction; translator's attention surfaces direction-flip as worst case.
**Confidence:** HIGH
**Resolution:** Both — general unintended-readings check + dedicated direction-flip emphasis check (the latter as a sub-step within the former).

### Ambiguity A8: Update user's stored memory `feedback_translation_polysemy`?
**Counter:** Don't update stored memory; new principle lives in framework artifacts only.
**Why partially fails:** The stored memory currently has the source-side polysemy principle as feedback to apply. Without an inverse-counterpart memory, the AI in a future session might not apply the new principle. Stored memories ARE applied automatically; framework artifacts need to be loaded.
**Counter:** Update stored memory to add inverse counterpart (target-side accidental polysemy prevention).
**Why succeeds:** Maintains parity between source-side and target-side at the memory layer; ensures application across sessions; matches the framework parity.
**Confidence:** HIGH
**Resolution:** Update stored memory with inverse counterpart (separate memory file `feedback_translation_polysemy_target_side` OR extend existing `feedback_translation_polysemy` with bidirectional content). Sensemaking leans toward SEPARATE memory file to preserve the symmetric structure.

### Ambiguity A9: Companion deathbed-room case — include or exclude?
**Counter:** Include — both cases discussed; both are translation failures; cover both.
**Why fails:** The deathbed-room failure is a failure to APPLY existing KEEP-SOURCE-TERM-WITH-GLOSS principle; the set-against failure is a failure to HAVE applicable principle. Structurally different. Mixing them dilutes both diagnoses. The user scoped the MVLw inquiry to set-against only.
**Counter:** Exclude — different failure mode; separate inquiry needed.
**Why succeeds:** Preserves diagnostic precision; respects user's scope; allows deathbed-room to get its own targeted treatment.
**Confidence:** HIGH
**Resolution:** Exclude from this inquiry; frontier flag for separate inquiry on "Pass 3 load-bearing technical term identification + when to use KEEP-SOURCE-TERM-WITH-GLOSS."

### Ambiguity A10: A5=lightly-domesticated configuration's role in the failure
**Counter:** A5=lightly-domesticated CAUSED the failure (the stance permitted target-naturalization).
**Why partially fails:** A5=lightly-domesticated permits NARROW target-naturalization where source-fidelity isn't load-bearing. The translator's judgment that "set against" was a NARROW naturalization was wrong (it crossed the load-bearing line because the directional semantics ARE load-bearing). But A5 itself operated as specified; the GATING CHECK (Pass 3.5 Reverse-Read) wasn't there to prevent A5's narrow-naturalization from crossing the line.
**Counter:** A5=lightly-domesticated didn't fail; the gating check on A5's narrow-naturalization didn't exist.
**Why succeeds:** Distinguishes A5's permission (a configurable axis stance) from the missing gating check (an invariant policy). A5 permits; policy gates.
**Confidence:** HIGH
**Resolution:** A5 didn't fail; the new policy is the missing gate on A5's narrow-naturalization decisions.

### SV4 — Clarified Understanding

After 10 ambiguity collapses:
- Canonical name: "target-side accidental polysemy" (general) + "direction-flip leakage" (high-severity subcase).
- Fix: layered 4-artifact — notes.md principle entry + harmony_layer.md Pass 3.5 Reverse-Read check + hard-constraint refinement + advanced_principles.md worked example + canonical Layer 1 spec v1.1 increment (6th Layer 2 policy).
- Pass 3.5 Reverse-Read: 6-step verification sub-step within Pass 3 (Reverse-Read → Enumerate target readings → Source-set comparison → Unintended-reading test → Direction-flip emphasis check → Re-render).
- Standalone policy cross-referenced to no-smoothing as bidirectional dual.
- Any-level scope (word / phrase / clause / sentence).
- Dedicated direction-flip emphasis on top of general unintended-readings check.
- Update user's stored memory with inverse counterpart (`feedback_translation_polysemy_target_side`).
- Companion deathbed-room case OUT OF SCOPE; frontier flag.
- A5 didn't fail; new policy gates A5's narrow-naturalization decisions.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Variables fixed
- VF1: Canonical name = "target-side accidental polysemy" + "direction-flip leakage."
- VF2: Layered 4-artifact fix architecture.
- VF3: Pass 3.5 Reverse-Read (6-step check).
- VF4: Standalone policy cross-referenced to no-smoothing as dual.
- VF5: Any-level scope.
- VF6: Dedicated direction-flip emphasis within general check.
- VF7: Update user's stored memory with inverse counterpart.
- VF8: Deathbed-room case OUT OF SCOPE.
- VF9: A5 didn't fail; new policy gates A5.
- VF10: Canonical spec v1.0 → v1.1 increment.
- VF11: Cross-reference to existing source-side polysemy principle (`feedback_translation_polysemy` + notes.md "local-construction trump") as structural inverse.

### Options eliminated
- "Target-side false-friend" alone (single name) — too narrow.
- "Direction-flip" alone (single name) — misses general non-direction-flip cases.
- Single-artifact fix — insufficient.
- Pass 4 vs Pass 3.5 — Pass 3.5 wins.
- Extend no-smoothing bidirectional — conflates mechanisms.
- Phrase-level only scope — too narrow.
- No direction-flip subcase emphasis — loses severity distinction.
- Skip stored memory update — leaves parity gap.
- Include deathbed-room — different failure mode.
- A5 caused failure — confuses configurable stance with missing invariant check.
- Skip canonical spec v1.1 increment — leaves principle non-invariant.

### Viable paths
- VP1: notes.md principle entry (the WHY/WHAT) — "On target-side accidental polysemy and direction-flip risk" as inverse counterpart to "On polysemy and the local-construction trump."
- VP2: harmony_layer.md hard-constraint refinement (extend "Adding information not present in the original is forbidden" to cover target side-effects).
- VP3: harmony_layer.md Pass 3.5 Reverse-Read check (6-step procedure) — extension of 3-Pass methodology.
- VP4: advanced_principles.md worked example (operational illustration with `mukabil` / `set against` + composes-with-existing-principles).
- VP5: canonical Layer 1 spec config_base_source.md v1.1 increment — add 6th Layer 2 always-on policy "Target-side accidental polysemy prevention" + Changelog entry.
- VP6: User memory update — new memory `feedback_translation_polysemy_target_side` with inverse counterpart.
- VP7: Companion deathbed-room frontier flag (separate inquiry).

### SV5 — Constrained Understanding

Solution space: 7 viable paths covering layered 4-artifact fix + stored memory update + frontier flag for companion case. All paths required for complete prevention; no path optional. Implementation priority: notes.md → harmony_layer.md → canonical spec → memory (the principle conceptually first; operational check enables enforcement; invariant policy ensures bidirectional translation principles; memory persists across sessions).

---

## Phase 5 — Conceptual Stabilization

**The failure mode** = **target-side accidental polysemy** (general) with high-severity subcase **direction-flip leakage**. The 3-Pass methodology's Pass 3 check operates SOURCE→TARGET (preserve source meaning) but doesn't check TARGET→SOURCE (does target admit unintended readings). The framework's polysemy principles all address source-side (multiple senses in source) but not target-side (multiple senses in target). The structural inverse is missing.

**The fix is layered:**
- `notes.md` — new principle entry "On target-side accidental polysemy and direction-flip risk" as inverse counterpart to "On polysemy and the local-construction trump."
- `harmony_layer.md` — (a) hard-constraint refinement extending "Adding information not present in the original is forbidden" to explicitly cover target rendering's side-effects; (b) Pass 3.5 Reverse-Read check as 6-step verification sub-step within Pass 3.
- `advanced_principles.md` — worked example with the `mukabil` / `set against` case + composes-with-existing-principles illustration.
- `config_base_source.md` (canonical Layer 1 spec) — v1.0 → v1.1 increment adding 6th Layer 2 always-on policy "Target-side accidental polysemy prevention" with cross-reference to no-smoothing as bidirectional dual.
- User stored memory `feedback_translation_polysemy_target_side` — inverse counterpart to existing memory.

**The Pass 3.5 Reverse-Read check (6 steps):**
1. Set aside the source.
2. Enumerate readings the target rendering naturally admits in the target language.
3. Compare to source's admitted readings.
4. For each target reading not in source set, ask: would a target reader land here?
5. Direction-flip emphasis: does any unintended target reading reverse the source's direction?
6. If unintended readings exist (especially direction-flip), re-render.

**Direct answer to the user's question (harmony_layer.md or notes.md? which part?):** **BOTH, layered.** notes.md owns the conceptual principle (the WHY/WHAT). harmony_layer.md owns the operational check (the HOW) — both the Pass 3.5 Reverse-Read methodology extension and the hard-constraint refinement to "Adding information not present in the original is forbidden." Plus advanced_principles.md gets a worked example, and canonical Layer 1 spec gets v1.1 increment for invariant enforcement.

### Accommodation trigger check
NO patching. 10 ambiguities settled HIGH. No anchors destabilize the model. Structural integrity holds.

### SV6 — Stabilized Model

Diagnosis:
- Failure mode: **target-side accidental polysemy** (general) / **direction-flip leakage** (high-severity subcase).
- Root cause: 3-Pass methodology's Pass 3 check is unidirectional (source→target preservation only); missing reverse direction check (target→source verification).
- Structural diagnosis: existing framework principles all operate source-side (preserve source meaning); the missing principle is the inverse — target-side accidental sense-addition prevention.
- Why existing principles missed it: Pass 3 check unidirectional + hard constraints scoped to insertion not side-effect + source-side polysemy principle has no inverse counterpart.

Fix (layered 4-artifact + memory + frontier flag):
- notes.md principle entry.
- harmony_layer.md Pass 3.5 Reverse-Read check + hard-constraint refinement.
- advanced_principles.md worked example.
- canonical Layer 1 spec v1.1 increment (6th Layer 2 policy).
- User memory inverse counterpart.
- Companion deathbed-room frontier flag (separate inquiry).

User's question answered: BOTH (harmony_layer.md AND notes.md), layered by ownership of WHAT/HOW.

**Difference from SV1:** Major. The diagnosis named the failure mode (target-side accidental polysemy + direction-flip leakage), located the structural inverse gap (existing principles all source-side; missing inverse target-side), proposed the layered 4-artifact fix architecture, specified the Pass 3.5 Reverse-Read check as 6-step procedure, established the cross-reference to no-smoothing as bidirectional dual, settled v1.1 increment, updated user memory pattern, and scoped out the companion deathbed-room case. The user's harmony_layer-vs-notes question got structurally answered (both, by ownership of WHAT/HOW).

---

## Saturation
- Perspective: APPROACHING.
- Ambiguity: 10/10 HIGH; 0 OPEN.
- SV delta: major.
- Anchor diversity: 8 Constraints, 12 Key Insights, 10 Structural Points, 5 Foundational Principles, 6 Meaning-Nodes. DIVERSE.

**Saturation: HIGH. PROCEED.**

## Frontier Flags for Decomposition / Critique

- **FF1** Decomposition: 6 pieces (P1 failure-mode naming / P2 notes.md principle entry / P3 harmony_layer.md hard-constraint refinement + Pass 3.5 check / P4 advanced_principles.md worked example / P5 canonical spec v1.1 increment / P6 user memory update).
- **FF2** Decomposition: the deathbed-room companion case as a Next Actions MUST/COULD item (frontier flag for separate inquiry).
- **FF3** Innovation: the Pass 3.5 Reverse-Read check's 6-step procedure has scope to refine — should it apply to ALL phrases or selectively to high-risk phrases (those with directional semantics)?
- **FF4** Innovation: stored memory architecture — single bidirectional memory vs two symmetric memories — minor decision.
- **FF5** Critique: must validate that the new principle truly is the structural inverse, not just an adjacent principle.
- **FF6** Critique: must validate that the Pass 3.5 check is operationally feasible (not just theoretically sound).
- **FF7** Critique: must validate that v1.1 canonical-spec increment doesn't trigger cascading refinements (the policy interaction map's existing 40 cells stay valid? — 5 → 6 policies × 8 axes = 48 cells).
- **FF8** Critique: must validate the user's direct question (harmony_layer.md OR notes.md? which part?) is answered explicitly.
