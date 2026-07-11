---
status: active
model: claude-opus-4-8[1m]
effort: max
refines: devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md, devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md
---
# Finding: Mandatory Chunking & the Character-Limit Adherence Hypothesis

## Changes from Prior

This finding sits in a chain of inquiries about the **comprehenslate** translation SKILL (a generic AI-translation instruction-set, calibrated on Said Nursî's *Risale-i Nur*). It relates to five prior findings in different ways; the frontmatter's `refines:` names the two it most directly builds on.

**Prior path:** `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` and `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md` (together, "the 06-14 chunking design").

- **What's preserved:** the entire *mechanism* of how to chunk — how to split a source into pieces, where the chunking logic lives in the pipeline, the granularity ladder (sentence → paragraph → passage → sub-chapter → chapter), and the harmony-aware splitting rule that refuses to break a Tier-1 meaning-chain. This finding reuses all of it unchanged.
- **What's changed:** the 06-14 design chunks for large-scale reasons (fitting a 200,000-token context window, consistency, cost). This finding adds a *new and much smaller-scale* reason — instruction-adherence — that lowers the natural chunk budget by roughly 200× and changes chunking's status from an optional efficiency knob to a candidate correctness necessity.
- **What's new:** the adherence rationale itself; the "flip the default on" policy question; and an enforcement analysis (how strongly a chunking instruction actually binds the model) that connects to the staging finding below.
- **Relationship to the other three priors** (detailed in the Inherited Commitments Re-test):
  - `devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md` — this finding **refines its framing**: it demotes that inquiry's "the un-wired 3-Pass method is *THE* root cause" to "one of *two* complementary causes on different axes." The 3-Pass commitment itself survives.
  - `devdocs/inquiries/2026-07-11_01-09__firing_time_categories_for_principles/finding.md` — **interacts with**: its whole-draft structural checks become chunking's post-assembly safety bracket.
  - `devdocs/inquiries/2026-07-11_04-12__staged_skill_borders_and_middleware/finding.md` — **sibling to**: chunking and staging are the two levers of one "bounded-load" idea.

## Question

The user proposed, tentatively: *"chunking should be mandatory maybe — I think there's a limit to how much an AI session can follow rules and translate; above a certain character count (around 3,500 for Claude Opus 4.8 max, probably lower for smaller models) it starts skipping instructions."*

This is two questions bundled into one:

1. **Is the mechanism real?** Does an AI's adherence to its instructions actually degrade as the input grows — and if so, is raw source character-count (~3,500) the right measure, or is the real driver something else (the total load in context, or the number of rules active at once)?
2. **If real, should chunking be mandatory, and how?** — where "mandatory" and "how" must be reconciled against a hard tension: chunk *small* so the model stays under its adherence limit, versus keep the text *whole* so cross-chunk structures (an escalation that builds across paragraphs, a ring composition that closes at the end, a convergence that pools many clauses into one) survive.

The reach is gated, exactly like the prior inquiries in this chain: evaluate → design → apply, and **no SKILL files are edited without explicit user authorization.**

## Finding Summary

- **The proposal survives, in a refined form.** The user's instinct is right and useful: adherence does degrade under load, smaller *is* safer, and the whole-versus-chunk tension is real. What changes is the *form* of the useful contribution.

- **"How to chunk" is already solved — this inquiry does not re-invent it.** Two prior findings from June 14 already worked out the full chunking mechanism. The genuinely new yield here is narrower and honest to state: a **new reason** to chunk (adherence), at a **much smaller scale** (~200× smaller budget), that **flips chunking's default** from off to a conditional-on. That yield is modest but real.

- **The core claim splits into two confidence levels** (this is the single most important correction the inquiry made). That adherence-under-load is a *distinct* phenomenon from the chain's already-diagnosed root cause is **high-confidence** — it rests on a structural argument, not on measurement. That it degrades *enough, at translation-relevant sizes, to matter* is **medium-confidence and quarantined** — there is currently zero empirical evidence for it. The whole design is therefore a low-regret bet conditional on an unmeasured-but-plausible effect.

- **The real variable is not "source characters."** It is the per-unit **transformation working-set** — the source span the model is translating *plus* the output it is generating *plus* the local bookkeeping it must hold while doing so. Source character-count is an approximate proxy for that. The "~3,500" is real-in-kind, approximate, and model-dependent — not a threshold to hard-code.

- **This is complementary to the prior root cause, not a rival.** The chain's earlier diagnosis — the SKILL's 3-Pass translation method (Meaning Lock → Harmony Map → Target Reconstruction) is never actually wired into the translation step — explains errors that appear *even in short texts*. Chunking cannot fix that collapse; it reduces how much gets dropped *per chunk*. The two stack.

- **"Mandatory" rightly means budget-gated-always-on, never always-split.** Short texts pass straight through; chunking engages only above a budget. So "mandatory" costs short texts nothing — it is conditional by construction.

- **Chunk by structure, which relocates the missing number rather than eliminating it.** Because there is no evidence for a specific character count, the design chunks on *structural* units (a section, a paragraph). This is a genuine improvement — a structural level is something the model can act on and there are sensible defaults — but it does not make the unknown quantity vanish: "which structural level is adherence-safe" is still a calibration question, just a discrete and defaulted one.

- **The whole-versus-chunk tension is resolved by bracketing, with one honest dependency.** Analyze the whole text first (comprehension + a harmony map), generate chunk-by-chunk in the middle, and check the whole reassembled draft at the end. The *front* bracket is the same whole-text harmony analysis the 3-Pass fix needs — so safe chunking and that fix share a component and should be designed together. The *back* bracket (the whole-draft check) works regardless.

- **A chunking instruction you can put in the SKILL today is a weak nudge; the real enforcement needs the engine.** Telling the model "translate one section at a time" inside a single run is a probability-raiser the model can quietly ignore — the same softness a prior inquiry found in staged instructions. Only *separate calls per chunk* physically stop the model from seeing too much at once. And even that enforces only the transformation-load half — each separate call still reloads the full instruction stack, so aggressive chunking actually *works against* the other load lever (staging).

## Finding

To see why the answer takes the shape it does, start from where the chain was. Earlier inquiries diagnosed a set of ~7 translation errors and traced them to a root cause: the SKILL *describes* a disciplined three-pass translation method in one of its reference files, but its main workflow file (`SKILL.md`, the step-by-step instructions the model actually follows) never tells the model to *run* that method — Step 5 is a flat "apply this bag of ~80 principles" list. So the model translates in one fluent motion and the method's safeguards never fire. The user now proposes a different and possibly competing explanation: the model skips instructions because there is simply *too much text* for it to hold all its rules and translate at once. Hence: chunk the source, and make it mandatory.

The inquiry evaluated that hypothesis and, finding it sound in a refined form, designed how it would work. The results follow.

### 1. What was already true before this inquiry (the reframe)

The single biggest surprise on investigation is that **chunking is not a new idea to introduce — it is an existing, fully-designed, but dormant capability.** Three facts establish this:

- The SKILL's configuration schema (`references/config/schemas.py`) already contains a complete set of chunking controls — a chunk budget, a chunk granularity (sentence/paragraph/passage/sub-chapter/chapter), a choice of splitting mechanism (including a "harmony-tier-aware" one that avoids breaking meaning-chains), and a parallel-processing mode. **Every one of these defaults to off and none is wired into the model-facing `SKILL.md`.** This is the exact same pattern as the un-wired 3-Pass method: a capability that exists in the engine layer but was never connected to the instructions the model reads.

- Two dedicated prior findings from June 14 (`chunking_deep_dive` and `chunk_types_vs_mechanisms`, together "the 06-14 design") already worked out the *how* in depth: how to separate the three distinct operations chunking bundles (splitting the source, managing the model's context window, and applying configuration at different granularities); where each belongs in the pipeline; the granularity ladder; and a hybrid harmony-aware splitting mechanism that starts from document structure, uses a heuristic to detect Tier-1 meaning-chains it must not break, and calls the model itself as a judge in ambiguous cases.

- The intake stage of the pipeline already produces sentence-segmented text explicitly described as the feeder for chunk boundaries.

The consequence is decisive for scoping this finding: **the "how to chunk" question is answered, and re-deriving it would add nothing.** What the user's proposal genuinely contributes is not a mechanism but three things layered on top of the existing one:

- a **new rationale** — adherence-under-load — that is absent from the 06-14 design's five stated reasons for chunking (context-window capacity, consistency, config-granularity, Tier-1 preservation, cost);
- a **much smaller scale** — the user's ~3,500 characters is roughly 875 tokens, about 0.4% of the 200,000-token window the 06-14 design chunks for; if adherence really is the driver, the right budget is ~200× smaller than the existing design assumed;
- a **policy flip** — from chunking as an opt-in efficiency knob to chunking as an always-considered correctness measure.

This is a modest-but-real yield, and naming it honestly (rather than presenting the whole apparatus as this inquiry's invention) is part of the finding.

### 2. The core claim, split into two confidence levels

The pivot question — is adherence-under-load real, and distinct from the already-diagnosed un-wired-3-Pass cause? — does not get one answer. It gets two, and separating them is the inquiry's most important analytical move.

**Distinctness: high confidence.** Adherence-under-load and the un-wired-3-Pass are different *kinds* of failure on different axes. The un-wired-3-Pass is a **method-structure** failure: the right procedure is never invoked, and this happens regardless of length — it shows up even in a two-sentence text. Adherence-under-load is a **load-magnitude** failure: the more the model must juggle at once, the more it drops. One is about *whether the method runs*; the other is about *how much the model can hold while running it*. Because the distinctness argument is structural — it follows from what the two failures *are*, not from any measurement — it holds at high confidence. This is what makes the relationship **complementary, not rival**: chunking does not replace the 3-Pass fix, it stacks on it. (The evidence pointing the same way: the ~7 observed errors look like collapse-in-one-motion, the kind that appears even in short spans — a 3-Pass symptom. Chunking would not have prevented them; it reduces the *opportunity* for omission per chunk on longer texts.)

**Magnitude-at-scale: medium confidence, quarantined.** Whether adherence degrades *enough*, at the sizes real translation passages actually reach, for chunking to be worth turning on — that is reasoned, not measured. There is no empirical evidence in the project that adherence drops with input size, no grounding for "3,500," and the 06-14 design's own validation was itself never run. The general tendency of language models to drop instructions under heavier load is well-established, so the reasoning is not baseless; but "well-reasoned" is not "measured." This claim is therefore **quarantined**: the design proceeds on it as a plausible working assumption, and the finding explicitly flags that its action-confidence rests on an unvalidated premise. Lifting the quarantine requires the experiment described in Next Actions.

**The variable.** Whatever the magnitude, the user's named variable — *source* character-count — is an approximation. The thing that actually loads the model at translation time is the per-unit **transformation working-set**: the source span being translated, plus the target text being generated, plus the local tracking the model holds while transforming (which term maps to which, the register, the pending structural obligations). Source size is a rough proxy for that working-set, not the working-set itself. Two things it notably does *not* capture: the large **fixed** instruction load (the SKILL plus its seven reference files plus ~80 principles plus eight configuration axes), which chunking the source does not reduce at all; and the number of rules active at once. So "~3,500 characters" is best read as *real-in-kind, approximate, and model-dependent* — a proxy pointing at a real thing, not a threshold to encode.

### 3. What "mandatory" should mean

"Mandatory" sounds like "always split the text," which would be wrong — it would needlessly fragment short passages and threaten the small-scale harmony of a tightly-built short section. That is not the right reading.

The right reading is **budget-gated-always-on**: chunking is always *in force* as a policy, but it only *engages* above a budget. Below the budget, the text passes through whole. This is conditional by construction — setting the budget to "none" is off; setting it to a value means "chunk only above this." So "mandatory" costs a short text nothing. (The SKILL already has one precedent for this shape: a configuration axis governing harmony-analysis depth is effectively mandatory-when-a-certain-richness-threshold-is-met.)

Two refinements complete the policy:

- **Per-model budget.** The user's instinct that the limit is "lower for smaller models" is correct and means the budget is a per-model value, not a universal constant — a weaker model gets a smaller budget.
- **Chunk by structure, not by a number** — with the honest caveat that this relocates the unknown rather than removing it. Because there is no validated character threshold, the design chunks on *structural* units: translate a section, a paragraph, a self-contained passage. This is a real improvement over a raw character count — a structural unit is something the model can perceive and act on, it snaps naturally to the harmony boundaries that must not be broken, and the granularity ladder already has sensible per-purpose defaults. But it does not make the missing number disappear. A structural unit can itself be large (a whole chapter can exceed any adherence-safe size), so the question "*which* structural level is adherence-safe?" is the same unknown quantity, now relocated to a discrete, defaulted, five-rung choice instead of a continuous character count. That is more tractable, and still ultimately a calibration question the experiment must answer.

### 4. Resolving the whole-versus-chunk tension: bracketing

The deepest design tension is that some of the SKILL's most important fidelity requirements need the *whole* text, and chunking removes the whole. An escalation chain that builds across many paragraphs, a ring composition that closes at the end by echoing the beginning, a convergence that pools a dozen clauses into a single resolving image — these span across any chunk boundary. The 06-14 design's harmony-aware splitter protects a *single* meaning-chain from being cut, but it does not, on its own, preserve these whole-*passage* structures, and it does not cover the whole-text "Harmony Map" the 3-Pass method builds. This is an acknowledged partial-coverage gap in the existing design.

The resolution is to **bracket** the chunked generation between two whole-text passes:

- **Before** — analyze the whole text: comprehend it, and build the harmony map (which whole-span structures exist and where they run). This produces a compact blueprint, not a translation.
- **Middle** — generate chunk by chunk, each chunk's generation consulting the relevant slice of the blueprint so it knows what larger structure it is participating in.
- **After** — run the whole-draft structural check (from the 01-09 finding) over the *reassembled* translation, catching any cross-boundary breaks the per-chunk generation could not see.

Two honest qualifications ride on this, both from the inquiry's adversarial critique:

- **The front bracket is not free, and its payoff is conditional.** Analyzing the whole text before chunking re-introduces *some* whole-text processing — the very thing chunking was meant to reduce. The reason it still nets positive is that *analysis load* and *generation load* are different: the before-pass reads and annotates (producing a small blueprint), whereas the failure the user observed is instruction-skipping during *generation* (producing the translation under all ~80 principles at once). Bracketing pays back a little analysis load to remove a lot of generation load — *but only if generation is genuinely the dominant failure locus*. If the model actually fails more from *reading* a long source than from *generating* under load, the bracket helps less. That is one more thing the validation experiment should probe.

- **The front bracket is the same component the 3-Pass fix needs.** The whole-text harmony analysis this design puts *before* chunking is exactly the "Harmony Map" pass (Pass 2 of the un-wired 3-Pass method). In this SKILL, that is the only whole-text harmony mechanism there is. So safe chunking's front bracket and the separate 3-Pass fix are not merely compatible — they **share a component** and should be **designed together** rather than bolted on independently. (The inquiry initially called this "entanglement"; the critique correctly downgraded that to "shares a component / best co-designed" — it is a concrete overlap in this SKILL, not a logical necessity that any whole-text pass would satisfy.) The *back* bracket, by contrast, needs nothing from the 3-Pass and is available regardless.

Where a Tier-1 whole-span structure is longer than the adherence-safe chunk size, the two constraints genuinely conflict: the structure sets a **harmony floor** on the budget (you cannot fragment it) while adherence sets a **ceiling**. A very long structure plus a very small adherence budget is an irreducible trade-off, not a bug to be designed away — and the finding records it as such.

### 5. How strongly a chunking rule actually binds — and the lever interaction

A crucial distinction determines *how much* of this can be done now versus later. Chunking can be expressed two ways, and they differ sharply in enforcement strength:

- **As an instruction inside a single run** — "translate one structural unit at a time." The model still has the whole source in its context; it is merely *asked* to proceed unit by unit. This is a **weak probability-raiser**: it nudges, but the model can quietly ignore it. It is the *same one-run softness* a prior inquiry (04-12, on staged SKILL borders) already identified — an instruction that looks done but isn't enforced.

- **As separate calls, one per chunk** — the model literally cannot see the other chunks' source, because they are not in the call. This **physically bounds** the transformation working-set. This is the real enforcement, and it requires the pipeline engine to be built (it does not exist yet).

This yields the phase-split in Next Actions: an instruction can go into `SKILL.md` now as a genuine-but-weak nudge, while the strong version waits for the engine. And it carries a lesson from the 04-12 finding about *where caveats go*: the model-facing text should be a clean, actionable instruction ("translate one structural unit at a time"), while the honest note that *this is only a nudge, not enforcement* belongs in the **authoring documentation**, not in the model-facing instruction — because telling the model in its own instructions that a rule isn't really enforced licenses it to relax the rule.

Finally, an interaction the critique surfaced that sharpens the whole picture. Chunking addresses the *transformation* load (the source-plus-output working-set). It does **not** address the *fixed instruction* load — and separate-call chunking actually *re-pays that fixed load on every call*: ten chunks means reloading the full ~80-principle stack ten times. That fixed-instruction load is precisely what the sibling "staging" lever (04-12) tries to reduce. So the two levers do not simply partition the problem cleanly — they **interact with tension**: aggressive chunking multiplies the very instruction-load that staging is trying to cut. The complete adherence answer needs *both* levers, and they must be tuned against each other, not independently.

### 6. The honest bottom line

The user was right to raise this, and right that it matters. The refined answer is: turn the existing dormant chunking on, as a budget-gated per-model policy that chunks by structure and brackets the chunked generation between whole-text analysis and a whole-draft check — *but* recognize that (a) the strong version needs the engine, the now-version is only a nudge; (b) the whole thing rests on an unmeasured assumption that adherence degrades enough to matter, which should be validated before it is trusted; and (c) chunking is one of two load levers, not a complete fix by itself.

## Inherited Commitments Re-test

This inquiry declared a Synthesis Trigger consuming prior findings and inherits commitments from five of them. Each is re-tested below.

- **Commitment:** The un-wired 3-Pass method is *THE* root cause of the ~7 translation errors.
  - **Source:** `devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md`.
  - **Re-test status:** RE-TESTED — commitment confirmed but frame revised.
  - **Evidence:** The un-wired-3-Pass remains a real and load-bearing cause — the observed errors are collapse-in-one-motion failures that appear even in short texts, which is a method-structure failure, not a load failure. But this inquiry establishes a *second, distinct* cause on a different axis (load-magnitude), so the framing "THE root cause" (singular, exhaustive) is revised to "one of two complementary causes." The 00-24 commitment's *content* holds; its *exclusivity* does not.

- **Commitment:** The whole-draft structural-fidelity checks (a config-independent mechanical spine plus a config-derived agenda) need the whole draft to operate.
  - **Source:** `devdocs/inquiries/2026-07-11_01-09__firing_time_categories_for_principles/finding.md`.
  - **Re-test status:** RE-TESTED — commitment confirmed.
  - **Evidence:** The commitment holds and is actively used: because these checks need the whole draft, they become chunking's *post-assembly* bracket, run over the reassembled translation (Finding §4). Chunking does not undermine them — it runs them at the one point where the whole exists again (after reassembly). The interaction is confirmed and turned into a design element rather than a conflict.

- **Commitment:** The base diagnosis — the ~7 errors stem from one fluency-first pass with no post-draft checkpoint.
  - **Source:** `devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md`.
  - **Re-test status:** RE-TESTED — commitment confirmed.
  - **Evidence:** "Overload above a character threshold" was tested as an alternative explanation for the same ~7 errors and found *not* to be the better account of them — they are one-motion-collapse symptoms, consistent with the no-checkpoint diagnosis, not with size-driven skipping (which would spare short texts). Adherence-under-load is a genuine additional factor for *longer* texts, but it does not re-explain the base 7. The base diagnosis stands.

- **Commitment:** The full chunking mechanism — the 3-operation disaggregation, split-placement, granularity ladder, and hybrid harmony-aware splitter.
  - **Source:** the 06-14 chunking design (`2026-06-14_00-50__chunking_deep_dive` + `2026-06-14_17-04__chunk_types_vs_mechanisms`).
  - **Re-test status:** RE-TESTED — commitment confirmed but frame revised.
  - **Evidence:** The mechanism is reused wholesale (Finding §1) — this inquiry does not challenge any of it. The frame revision is that the design's *driver set and scale* are extended: adherence is added as a sixth reason, the budget is re-scaled ~200× smaller, and the default flips toward on. One caveat inherited with it: the 06-14 design's own empirical validation was never run, so "reuse the mechanism" inherits that un-validated status — now doubly motivating the experiment in Next Actions.

- **Commitment:** Reducing the model's simultaneously-active load improves adherence (the "staging" lever).
  - **Source:** `devdocs/inquiries/2026-07-11_04-12__staged_skill_borders_and_middleware/finding.md`.
  - **Re-test status:** RE-TESTED — commitment confirmed but frame revised.
  - **Evidence:** The load-reduction idea holds and generalizes: chunking and staging are the *two levers* of one bounded-load idea — chunking bounds the transformation load, staging bounds the fixed-instruction load. The frame revision is the newly-surfaced *interaction* (Finding §5): separate-call chunking re-pays the fixed-instruction load per call, working against staging. So the two are not independent partitions; they must be tuned together. Also inherited and applied: the 04-12 lesson that "this isn't enforced" caveats belong in authoring notes, not model-facing text.

## Next Actions

The reach is gated. The **reach decision itself** (evaluate-only → design → apply the SKILL edit) and **any SKILL-file edit** belong to the user; nothing below is executed without explicit authorization. The one item that is *not* gated on a SKILL edit is the validation experiment.

### MUST

- **What:** Run an empirical validation of adherence-under-load — matched-size translation trials that hold the method constant (same SKILL, same 3-Pass wiring state across arms) and vary only the per-unit transformation working-set size, per model, measuring instruction-adherence (dropped clauses, skipped principles). Isolate the variable by varying source-size, output-size, and active-rule-count *independently*. Report the adherence-safe structural granularity level and a numeric cap, per model.
  - **Who:** a dedicated evaluation inquiry / test harness (not a SKILL edit — no authorization needed to *measure*).
  - **Gate:** condition-bound — this is the prerequisite for treating any of the design below as grounded; the always-on flip (the COULD items) should not ship *before* this returns evidence.
  - **Why:** it is the only thing that lifts the quarantine on the magnitude claim. Until it runs, the entire design rests on a reasoned-but-unmeasured premise. It is doubly motivated: it is also the 06-14 design's own never-run validation.

### COULD

- **What:** Add a model-facing chunking instruction to `SKILL.md` now — "translate one structural unit at a time, snapping to structure," expressed in structural units, budget-gated (short texts pass through). Put the "this is a nudge, not enforcement" caveat in the authoring notes, not the model-facing text.
  - **Who:** a SKILL.md edit (authorization required).
  - **Gate:** condition-bound — on the user's reach decision to reach "apply," and on authorization.
  - **Why:** a genuine, immediately-available adherence nudge for longer texts, before the engine exists.
  - **Depends-on:** MUST item "empirical validation." OVERRIDE: partially adoption-ready despite the open MUST, because the instruction is low-cost and low-risk (it cannot harm short texts, which pass through) and its structural-unit default (e.g. section-level) is conservative. Reason: the MUST calibrates the *budget*, but the nudge's value does not depend on an exact budget; a conservative default is safe to ship and refine. The user may still prefer to wait for evidence.

- **What:** When the pipeline engine is built, flip the dormant chunking budget from off to a structural default, add the per-model dimension, and drive generation as separate calls per chunk.
  - **Who:** an engine build + a `schemas.py`/pipeline change (authorization required).
  - **Gate:** condition-bound — on the engine existing, the reach decision, and authorization.
  - **Why:** this is the real enforcement (physically bounds the working-set); the instruction version is only a nudge.
  - **Depends-on:** MUST item "empirical validation." This COULD is GATED — the per-model budget value should come from the experiment before the always-on separate-call flip ships.

- **What:** Develop the whole-draft structural check (from the 01-09 finding) as chunking's post-assembly bracket — run it over the reassembled translation, targeting cross-chunk seams specifically.
  - **Who:** a design + SKILL edit (authorization required).
  - **Gate:** condition-bound — on the reach decision and authorization.
  - **Why:** catches cross-boundary structural breaks that per-chunk generation cannot see; notably, it needs *nothing* from the un-wired 3-Pass, so it is available independent of that fix.

### DEFERRED

- **What:** Co-design chunking's front bracket together with the un-wired 3-Pass (recognizing the front bracket *is* the Pass-2 harmony map they share).
  - **Gate:** condition-bound — revives when the 3-Pass is actually wired into `SKILL.md` (the 00-24 fix is applied). Until then there is no Pass-2 to share.
  - **Why (if revived):** prevents building two redundant whole-text passes and ensures safe chunking and the 3-Pass fix compose rather than collide.

- **What:** State "bounded-load translation" (chunk the transformation load + stage the instruction load, tuned against their interaction) as a standing design principle.
  - **Gate:** condition-bound — revives if a *third* load lever appears, giving the principle more than two instances to rest on.
  - **Why (if revived):** unifies chunking and staging under one frame; deferred now because two instances is thin, and over-generalizing from two points is the risk the inquiry explicitly flagged.

## Reasoning

The finding is the product of an adversarial pass (the inquiry's critique step) that produced no outright kills but seven refinements. The field of what was considered:

- **Rival explanation — "adherence-under-load replaces the un-wired-3-Pass as the root cause."** *Rejected.* The observed errors are one-motion-collapse symptoms present even in short texts; size-driven skipping would spare short texts. The two are on different axes (method-structure vs load-magnitude) and stack. This is why the finding lands on *complementary*, not *rival*.

- **Rival explanation — "the proposal is just the existing 06-14 chunking design re-surfaced, adding nothing" (the redundancy challenge).** *Partially upheld, and it shaped the finding's honesty.* The *how* is indeed entirely reused; the finding leads by crediting 06-14 for the mechanism. But the redundancy does not fully land: the adherence rationale, the ~200× re-scale, the default-flip, and the enforcement analysis are genuinely new (more than the near-zero-novelty of some prior inquiries in this chain). The relationship label "extends 06-14" is honest provided the mechanism is credited to 06-14 — which the finding does.

- **Rival explanation — "the real lever is not source-chunking but reducing active rule-count" (the deep rival).** *Partially upheld, and it sharpened the answer.* Source-chunking does not touch the fixed instruction load at all — so chunking alone is an incomplete fix. But it does not dissolve the contribution: chunking still owns the *transformation-load* component, which staging does not touch. The result is the two-lever picture plus the newly-found lever-interaction (separate-call chunking re-pays the instruction load staging cuts).

- **Over-engineering challenge — "mandatory chunking over-formalizes and harms short texts."** *Defused.* "Mandatory" is budget-gated-always-on, so short texts pass through untouched; the policy is conditional by construction.

- **The "structure solves the no-number problem" claim (survived as a refinement).** The innovation step initially claimed chunking-by-structure *sidesteps* the absence of a validated character threshold. The critique corrected this to *relocates* — the unknown reappears as "which structural level is adherence-safe." The finding states the weaker, honest version.

- **The "whole-text-before defeats the purpose" challenge (survived as a refinement).** The front bracket does re-introduce some whole-text load; it nets positive only because analysis-load and generation-load differ, and only if generation is the dominant failure locus. The finding carries that condition rather than asserting a clean win.

- **The pivot's confidence (survived as the central refinement).** The claim was initially rated uniformly high. The critique split it: distinctness is high (structural), magnitude-at-scale is medium and quarantined (unmeasured). This split is the finding's most important correction and the reason the design is framed as a low-regret conditional bet rather than a settled fix.

## Open Questions

### Research Frontiers

- **Does adherence measurably degrade with the transformation-working-set size, at translation-relevant scales, per model?** No known evidence exists; this is the quarantined premise. The MUST experiment is the path. Its by-products (the adherence-safe granularity level, a per-model numeric cap, and which sub-component of the working-set drives decay) are all currently unknown.
- **Is the dominant failure locus generation or reading?** The bracket's net-positive depends on it being generation. Untested.

### Blocked

- **The strong (enforcing) form of chunking** cannot be built until the pipeline engine exists — today only the weak in-run instruction is available.
- **The front-bracket co-design** cannot be done until the un-wired 3-Pass is actually wired (the 00-24 fix is applied), since there is no Pass-2 to share until then.

### Refinement Triggers

- **Re-open the "complementary, not rival" verdict** if the validation experiment shows adherence degrading even at very short lengths (which would make it look more like the method-structure failure than a distinct load failure).
- **Re-open the budget-and-granularity design** when the validation experiment returns a per-model adherence-safe granularity — the conservative structural default should be replaced by the measured one.
- **Re-open "bounded-load as a stated principle"** if a third load lever is discovered.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
chunking should be mandatory maybe, i think there is a limit of how much AI session can follow rules and do the translation, above certain amount of character (around 3500 charrs for claude opus 4.8 max and proabbly lower for smaller AI models) it starts skipping insturcitons  maybe.
```

</details>
