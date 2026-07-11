# Branch: Character/Word Count vs Structural Units as the Chunking-Budget Unit

## Source Input

```text
u said 

Chunk by structure, not by a number — with the honest caveat that this relocates the unknown rather than removing it. Because there is no validated character threshold, the design chunks on structural units: translate a section, a paragraph, a self-contained passage. This is a real improvement over a raw character count — a structural unit is something the model can perceive and act on, it snaps naturally to the harmony boundaries that must not be broken, and the granularity ladder already has sensible per-purpose defaults. But it does not make the missing number disappear. A structural unit can itself be large (a whole chapter can exceed any adherence-safe size), so the question "which structural level is adherence-safe?" is the same unknown quantity, now relocated to a discrete, defaulted, five-rung choice instead of a continuous character count. That is more tractable, and still ultimately a calibration question the experiment must answer.

i feel like section paragrapgh etc are too changing in their sizes, a paragrah can be 20 sentence or 2 or 30 even. similar to section. 
this is why we need better approaximations such as character and word count, 3500 character is similar in most situations or the word count

and 3500 comes from past good translation example of mytrasnlations/asayi_musa/4_mesele.md and mytrasnlations/asayi_musa/4_mesele_en.md which was succesfull in my judgment unlike our last example , our last source file translation was approximately 11000 char long (mytrasnlations/asayi_musa/ikinci_huccet_en.md) and i thought that was too much since it failed and i come up with this safe number of 3500 for opus 4.8 model. For smaller models it should be lower to protect the comprehenslation integrity (a new term)

lets dive deep into this understanding
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-07-11_06-37__char_word_count_vs_structural_chunk_budget/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** [i1]
- **Verdict:** MED-FLAG
- **Flagged conditions:** (1) **evidential crux / confound** — ~3500 rests on TWO data points (one success, one failure); whether *length* is the true cause vs a confound (difficulty / structure / register / whether the 3-Pass fired) cannot be settled by two points alone; (2) **measure sub-fork** — character vs word vs the SKILL's existing token field (three candidate measures, differing in cross-text and cross-language stability); (3) **reach** — "dive deep into this understanding" leans understand-first but corrects a design recommendation (evaluate-vs-design-vs-apply gate open); (4) don't over-index on exact 3500 (approximate + model-dependent). No structural LAYER 1 fire (Mode-2 boundary-approached only).

## Question

**Literal (MultiDepth, non-contaminating):** *"Structural units (section, paragraph) vary too much in size to be a reliable chunk-budget unit — a paragraph can be 2 or 30 sentences. Character count (or word count) is a better, more stable approximation; ~3500 characters is 'similar in most situations.' The ~3500 figure is empirical: it comes from a translation I judged successful (4_mesele) versus one I judged failed because it was too long (~11000 chars, ikinci_huccet), so ~3500 is my safe number for Opus 4.8, and it should be lower for smaller models, to protect 'comprehenslation integrity' (a new term). Let's dive deep into this understanding."*

**What kinds of ask this carries (MQ1 verdict-axis — preserved as ambiguities):**
- `validate-the-unit-choice` — is character-count (or word-count) genuinely a better chunking-budget unit than structural units? (adjudicate the char-vs-structure dispute raised against the prior finding's "chunk by structure")
- `interpret-the-evidence` — what do the two real data points (4_mesele judged-successful at ~3500-scale; ikinci_huccet judged-failed at ~11000) actually establish? Does one-success-plus-one-failure ground a ~3500 threshold, or something weaker/different?
- `define-the-concept` — articulate/define the coined term "comprehenslation integrity" (what it is, what threatens it).
- `refine-the-prior` — reconcile with the prior finding's chunk-by-structure recommendation + its quarantined magnitude; does this evidence lift or partly-lift the quarantine?
- `pick-the-measure` — character-count vs word-count vs the SKILL's existing token field: which measure specifically?
- `reach` (inherited gate) — deepen-understanding-only vs +design vs +apply-the-SKILL-edit.

**Plausible action-endpoints (MQ3 intent-axis, WHAT — preserved as ambiguities):**
- `replace-the-budget-unit` — swap the recommended budget unit from structure to character/word count.
- `ground-the-number` — convert ~3500 from a "reasoned-not-measured" guess into an evidence-backed figure (answer the prior finding's quarantine).
- `deepen-the-understanding` — understand the phenomenon (why a character-count is a more stable proxy; what comprehenslation integrity is) rather than immediately build.
- `establish-a-per-model-scaling-rule` — "lower for smaller models" as a standing design rule.

## Goal

**Deliverable shape (Deconstruct tuple):**
- **deliverable:** an evaluation-plus-deepened-understanding — (a) a verdict on character/word-count vs structural units as the chunking-budget unit; (b) an interpretation of what the two real data points establish (and their confound limit); (c) a definition of "comprehenslation integrity"; (d) a reconciliation with the prior finding (does the evidence lift the quarantine?).
- **kinds:** diagnostic/evaluative judgment + evidence-interpretation + concept-definition + prior-reconciliation / commitment re-test.
- **bounds:** the comprehenslate SKILL's chunking-budget design; the two real translation examples in `mytrasnlations/asayi_musa/`; gated reach (no edits without authorization); Opus-4.8 **plus smaller models** (portability in-frame).

**Motivations a good answer might serve (MultiDepth WHY-axis — preserved as ambiguities):**
- `correctness-of-the-lever` — wants the *right* budget unit so chunking actually protects fidelity: a stable measure (characters) beats a variable one (structural units).
- `vindicate-the-original-instinct` — the ~3500 was not a guess; the user had a real basis (the two examples) and wants it recognized and folded into the design (answering the prior finding's "zero evidence").
- `protect-comprehenslation-integrity` — the deeper motive named by the coined term: comprehension-plus-translation fidelity degrades past a load threshold, and the budget exists to hold it.
- `cross-model-robustness` — "lower for smaller models" signals a portability motive: keep load under whatever ceiling a given model has.

**Context downstream consumers need (MQ2 context-need axis — preserved as ambiguities):**
- **verdict:** the ACTUAL character/word/token counts of `4_mesele.md` + `4_mesele_en.md` + `ikinci_huccet_en.md` (do they match the user's ~3500 vs ~11000 framing?) · what the prior 04-48 finding actually recommended + quarantined · does the SKILL's `chunking_budget` field currently take TOKENS (schemas.py), not characters?
- **kinds:** how character-count vs word-count vs tokens each correspond to LLM processing load; the two examples' content + what "success"/"failure" meant; whether the failure was attributable to LENGTH specifically.
- **stance:** is ~3500 a hard THRESHOLD or a soft budget-SCALE? · **confound check** — is the 4_mesele-vs-ikinci_huccet difference attributable to length specifically, or could the two texts differ on other variables (difficulty, structure, register, whether the 3-Pass fired) that co-vary with length?

**Explicit exclusions (MQ4 boundary-axis):**
- `not-structural-units` — the user explicitly argues AGAINST section/paragraph as the budget unit ("too changing in their sizes"); the answer should not re-recommend bare structural units as the primary measure.
- `not-exact-threshold-pinning` (inherited) — ~3500 is a working figure, approximate + model-dependent; not a demand to validate exactly 3500.
- `reach-bounded` (inherited, extrinsic) — evaluate/deepen (and at most design); applying the SKILL edit is gated on explicit authorization.

## Considered Articulations

**Item i1 — the character/word-count-as-better-budget-unit argument + its empirical provenance + comprehenslation integrity:**
1. **(validate-the-unit lean)** Evaluate whether character-count (or word-count) is a better chunking-budget unit than structural units, given that structural units vary too much in size (a paragraph = 2 or 30 sentences) to be a reliable adherence-safe measure.
2. **(interpret-the-evidence lean)** Determine what the two real data points — 4_mesele judged-successful (~3500-scale) vs ikinci_huccet judged-failed (~11000 chars) — actually establish about an adherence-safe character budget, and whether length is the true differentiator or a confound that co-varies with length.
3. **(define-the-concept lean)** Articulate "comprehenslation integrity" as a defined term: what it is (comprehension + translation fidelity held together under load), what threatens it (working-set overload), and how a character-budget protects it.
4. **(refine-the-prior lean)** Reconcile a character-count budget unit with the prior finding's chunk-by-structure recommendation and its quarantined ~3500 — does the two-example evidence lift or partly-lift the quarantine, and does character-count *replace* structural snapping or *complement* it (a size budget that still snaps to harmony boundaries)?
5. **(pick-the-measure lean)** Decide between character-count, word-count, and the SKILL's existing token-based `chunking_budget` field as the specific budget measure, weighing cross-text stability, correspondence to model load, and language/script effects (Turkish source vs English output character ratios).
6. **(per-model-scaling lean)** Establish "lower budget for smaller models" as a design principle and reason about how a per-model character budget would be set and calibrated.

## Scope Check

**IN-scope (from Deconstruct bounds):** evaluating character/word-count vs structural units as the budget unit; interpreting what the two real translation examples establish (incl. the confound limit); defining "comprehenslation integrity"; reconciling with the prior 04-48 finding + the 06-14 granularity ladder (does the evidence lift the quarantine); the char-vs-word-vs-token measure sub-fork; per-model scaling; gated reach up to design.

**OUT-of-scope (from MQ4 exclusions):** re-recommending bare structural units as the primary budget measure (the user excludes this); applying the SKILL edit without explicit authorization; validating "3500" as an exact numeric threshold.

**Question covers goal:** YES — the question's MQ1 asks (validate-unit / interpret-evidence / define-concept / refine-prior / pick-measure / reach) span the goal's evaluation-plus-understanding deliverable. One axis the articulation forces into view and the Question retains: the **confound** — the two data points differ in length AND possibly in other variables, so "length is the cause" is a hypothesis the two points alone cannot confirm; the dive must hold ~3500 as a strong real anchor without over-claiming it as validated.

**Specific-vs-pattern check:** the user names a specific number (~3500 for Opus 4.8) and two specific files. Per default, address the **broader pattern** — is a *size-based* budget (in some stable unit) the right lever, what do the examples establish about it, and what is the phenomenon (comprehenslation integrity) — while treating ~3500 and the two files as the concrete evidential anchor, not the whole scope. The "similar in most situations" and "lower for smaller models" framing explicitly generalizes beyond the single number.

## Synthesis Trigger

This inquiry consumes prior inquiry outputs as inputs and inherits commitments it must re-test (it directly disputes a recommendation of the immediately-prior finding and supplies evidence against that finding's quarantine). CONCLUDE will require an `## Inherited Commitments Re-test`.

- `devdocs/inquiries/2026-07-11_04-48__mandatory_chunking_char_limit_adherence/finding.md` — commits to **"chunk by structure, not by a number"** (structural granularity as the budget unit) and to **quarantining ~3500 as reasoned-not-measured (zero empirical evidence)**. This inquiry directly re-tests both: it disputes the structural unit (too size-variable) and supplies two real data points against the "zero evidence" quarantine. The central re-test.
- `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` — commits to the **granularity ladder (sentence → paragraph → passage → sub-chapter → chapter)** and A4-driven per-purpose defaults as the chunking granularity mechanism. This inquiry tests whether a *character/word* budget should govern instead of (or alongside) that structural ladder.
- `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md` — commits to the **harmony-aware splitting mechanism** (structural baseline that snaps to meaning-boundaries). This inquiry tests how a size budget interacts with that boundary-snapping (replace vs complement).
