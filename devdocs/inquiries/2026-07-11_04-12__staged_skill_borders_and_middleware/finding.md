---
status: active
model: claude-opus-4-8[1m]
effort: max
refines:
  - devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md
  - devdocs/inquiries/2026-07-11_01-09__firing_time_categories_for_principles/finding.md
---
# Finding: Staged SKILL Borders and Middleware Files

## Changes from Prior

**Prior paths:**
- `devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md` — the three-pass fix (relationship: **EXTENDS** — staging generalizes its wiring).
- `devdocs/inquiries/2026-07-11_01-09__firing_time_categories_for_principles/finding.md` — the config-independent-spine / tiered-reliability finding (relationship: **REFINES** — this inquiry confirms tiered reliability).

**Revision trigger:** A new user proposal — give the SKILL explicit "stage 1 / stage 2" borders (still one model run, harmony and policies separated and stacked in order) plus per-change "middleware md files" recording what rule/policy changed and how.

**What's preserved:** Both priors stand. This inquiry does not overturn either.

**What's changed:** Nothing in the priors is revised. What sharpens is the *reading of the user's idea*: it looks like one fresh architecture; it is actually two separable proposals, one of which mostly finishes work the priors already specified.

**What's new:** A clean split of the proposal into two independently-adoptable parts (an ordered staged Step 5; a lean authoring changelog), an honest account of what each is worth, and one reusable design lesson ("a file for each change" is an over-engineering trap).

**Migration:** No SKILL files were edited. The evaluation and the designs are delivered; whether to build or apply anything is left to the user (see Next Actions).

---

## Question

The project is **comprehenslate**, a general-purpose AI translation SKILL (a structured instruction set that tells the model how to translate). A chain of earlier investigations found that the SKILL's core translation step — Step 5 in `SKILL.md` — is a flat "apply this bag of principles" list, and that the fix is to run translation in explicit ordered passes (lock the meaning first, then handle stylistic harmony, then reconstruct and check).

Building on the most recent of those (which split the post-draft check into always-run *mechanical* checks that are trustworthy and reader-tuned *judgment* checks that are not guaranteed), the user proposed two things:

1. **Explicit stage borders** — give the SKILL "stage 1 / stage 2" sections so harmony rules and configuration policies are separated and stacked in an explicit order, rather than dumped in one flat list. Still **one model run** — the stages live inside a single pass.
2. **"Middleware md files"** — generate a small markdown file per change so it is "visible for us what rule/policy changed and how" (a traceability layer).

The question: **does this make sense, and if so, how?**

## Finding Summary

- **The idea is sound, but it is two ideas, not one — and they should be judged separately.** One is about how the translation *runs* (staging); the other is about how the *SKILL itself is maintained* (the traceability files). They have different beneficiaries, different value, and different cost.

- **The staging idea is already half-built into the SKILL.** The harmony reference file literally defines a three-pass method (lock meaning → map harmony → reconstruct); it is just never wired into the workflow. So "add stages" is largely *finishing* a fix the previous investigation already specified — plus generalizing it (stage *all* the layers, not only harmony).

- **Staging helps, but as a nudge, not a guarantee.** In a single model run, "Stage 1 / Stage 2" headers are an instruction, not a barrier — the model can still blend them. An explicit ordered instruction is more likely to be followed than a flat list (that is exactly why the earlier fix works), so staging *raises the probability* of correct ordering; it does not *enforce* it.

- **Staging does not fix the problem that inspired it.** The spark was "judgment checks are unreliable." Staging organizes and exposes structure, but it does not make a judgment check reliable — a border and a self-report are not verifications. Staging's honest correctness role is to give the *already-reliable mechanical checks* a clean home (a final check-stage), not to create new reliability.

- **The traceability idea is the genuinely-new, genuinely-useful part — in its lean form.** A single running changelog of SKILL edits ("what rule/policy changed, why, when") is cheap, serves the human author, and is the literal thing the user asked for.

- **But "a file for each change" is an over-engineering trap.** The user's literal wording — a middleware file *per change* — has the same flaw as a runtime trace with a file *per rule*: it multiplies artifacts and maintenance for little gain. The lean form of both is **entries in one document**, not a file per thing.

- **One drafting correction matters:** any "these borders don't actually enforce" caveat must live in the *authoring* docs (for the human), never in the *runtime* instruction — telling the model its own borders are optional would invite it to relax them.

- **Relationship to the priors:** the staging half **EXTENDS** the three-pass fix (`2026-07-11_00-24`) by generalizing it to all layers; the whole inquiry **REFINES** the tiered-reliability finding (`2026-07-11_01-09`) by confirming that a border and a self-report sit at its "not guaranteed" tier. Staging is **gated** — its correctness value is inert until the three-pass fix is actually applied.

## Finding

### Why this came up

The immediately-prior investigation ended on a distinction: the SKILL's post-draft checking splits into an always-run **config-independent** spine (mechanical checks like "did any source clause get dropped?" — trustworthy) and a **config-derived** agenda (reader-tuned checks like "is this word too hard for this reader?" — judgment calls, not guaranteed). The honest note there was that the judgment checks "re-invoke the same fallible reading that failed the first time."

That note is what sparked the user's idea: if the SKILL's moving parts are unreliable when jumbled together, why not give them explicit *stage borders* — separate the layers, stack them in order — and, while we are at it, keep *middleware files* recording what each rule/policy change did, so the whole thing is visible and inspectable?

### Reading the actual SKILL changed the picture

Looking at the real files (not the idea in the abstract) reshaped the evaluation in three ways.

**First: the staging is already half-there.** The harmony reference (`references/core/harmony_layer.md`) opens by defining "a translation mode that works in three passes" — Pass 1 locks meaning, Pass 2 maps harmony, Pass 3 reconstructs. Those are stages, written out in full. But `SKILL.md`'s Step 5 pulls that file in only as a "Tier 1-4 preservation policy" and never runs the three passes as an ordered sequence. So the staging the user wants, for the harmony core, is *finishing a wiring job that is already 90% specified* — which is precisely what the earlier three-pass fix (`2026-07-11_00-24`) proposed. The genuinely-new part of staging is **generalizing** that move: turn the *whole* flat Step-5 list (which currently mixes configuration, policies, principles, harmony, and notes together) into an ordered multi-stage sequence, not just insert the harmony passes.

**Second: the separation the user wants is partly present, then destroyed.** The SKILL's files are already split on disk into a config layer (`references/config/`) and a core layer (`references/core/`). Step 5 then re-mixes them into one undifferentiated "apply all of this" bag. So staging is, in part, *restoring at the workflow level a separation the file tree already implies*.

**Third: the "middleware" idea has a latent seed too.** The harmony file already mentions a "harmony report" where the translator documents its choices — a latent per-translation record. So the traceability idea is not building from nothing either.

### Why the split is the key move

The two halves of the proposal are genuinely different things:

- **Staging** serves *translation correctness* — it is about how the model runs a translation.
- **The middleware files** serve *SKILL-author maintainability* — they are read by the human developing the SKILL, never by the model at translation time.

Different beneficiary, different novelty, different cost, different reliability profile. They are only joined by a theme ("make the SKILL explicit and visible"). So they should be evaluated and adopted independently — and the rest of this finding does exactly that.

### Staging: sound, but a nudge, and gated

The sharp question about staging is whether "Stage 1 / Stage 2" borders *inside one model run* actually do anything, since nothing forces the model to finish Stage 1 before starting Stage 2.

The answer is that they help, but as a **probability-raiser, not an enforcer**. This is not a weakness unique to the user's idea — it is the exact mechanism the accepted earlier fix already relies on. The whole diagnosis of the original translation errors was that a *flat* "do all of this at once" instruction let the passes collapse into one fluent motion; the fix is an *explicit ordered* instruction. An ordered instruction is more likely to be followed than a flat bag. That is a real, if modest, gain — and it is the same lever, at the same reliability tier, that the prior fix claims.

Two honest consequences follow:

- **Do not let explicit borders create false confidence.** Naming a stage does not make the model obey the stage. There is a gradient here — a prose header is the weakest form of border; requiring the model to actually *emit* an intermediate artifact (a written "meaning-locked" version before it does harmony) would commit it more strongly; a genuinely separate pass would enforce it. But the stronger rungs cost more, and true enforcement would require relaxing the "one run" constraint the user explicitly imposed. Within "one run," staging stays at the nudge end of the gradient. (Whether an emitted artifact meaningfully beats a prose header *within* one pass is an open empirical question, not an established fact.)

- **Staging does not fix the reliability problem that inspired it.** The spark was unreliable judgment checks. Staging exposes and orders structure, but a border and a self-report are not verifications — it does not make a judgment check trustworthy. Its honest correctness contribution is narrower: it provides the **structural slot** (a final check-stage) where the *already-reliable mechanical checks* (from the prior finding) run. It *hosts* reliability; it does not create it. So staging is best understood as **primarily a maintainability win** (an ordered, sectioned, extensible SKILL is easier to reason about and grow), with a secondary, modest correctness nudge.

Because staging's correctness core *is* the prior three-pass fix, it is **gated**: applying staging into a still-flat Step 5 would strand it. It should be done together with, or after, that fix. And the stages should be presented as an ordered sequence that still *permits back-reference* to earlier stages' committed output (the reconstruction pass legitimately needs to consult the locked meaning) — not a one-way ratchet that forbids looking back.

### The middleware files: adopt the lean form, name the reader

The traceability idea is where the genuinely-new value is — but its value depends entirely on picking the right form.

- **The lean, useful form** is a *single running changelog* of SKILL edits: dated entries recording which rule or policy changed, what changed, and why (the same shape as an "architecture decision record"). It is cheap, it has no runtime cost, and it is the literal thing the user asked for ("visible for us what rule/policy changed how"). Its one real consumer is the human author, and its value is contingent on that author actually maintaining it — which is the argument for keeping it lean.

- **The over-engineered form** is the user's literal wording: a middleware file *per change*. This has the same flaw as the runtime-trace idea (a file *per rule*) that this analysis rejects: it multiplies artifacts and maintenance for little marginal insight. This is the reusable lesson — **"a file for each X" is the over-engineering shape**; the lean answer, whether for authoring history or runtime provenance, is **entries in one document** (a single changelog for authoring; the already-existing single harmony report for runtime, if runtime tracing is ever wanted at all).

One placement correction ties the two halves together: any caveat about staging's soft borders ("these are ordered instructions, not enforced barriers") belongs **in the authoring changelog / design docs**, for the human — **never in the runtime Step-5 text**. A runtime instruction that announces its own borders are optional would license the model to relax them, undermining the very ordering staging is meant to encourage.

### The honest bottom line

The proposal makes sense and yields two adoptable things: a **staged Step 5** (which mostly finishes and generalizes the prior fix, is a maintainability win plus a modest correctness nudge, and is gated on that fix) and a **lean single-file authoring changelog** (cheap, genuinely new, useful if maintained). What it does *not* do is solve the unreliable-judgment-checks problem that sparked it — that ceiling stays exactly where the prior finding left it, with only the mechanical checks trustworthy. The user's instinct toward structure and visibility is right; the refinements are to split the two ideas, keep both lean (no file-per-change), keep the enforcement honest (a nudge, not a barrier), and keep the caveat where the model cannot read it as permission.

## Inherited Commitments Re-test

This finding builds on two prior findings; each load-bearing commitment is re-tested rather than absorbed.

**Commitment 1 — the fix is the three-pass method wired into Step 5 (meaning-first).**
- **Source:** `2026-07-11_00-24/finding.md`.
- **Re-test status: RE-TESTED — commitment confirmed.** Staging is a generalization of exactly this: it wires the (already-written but un-wired) three-pass method into Step 5 and extends the same move to the other layers. Staging's correctness core *is* this commitment; it does not replace it.
- **Evidence:** `harmony_layer.md` defines the three passes but `SKILL.md` Step 5 imports the file only as a "Tier 1-4 preservation policy" — the wiring the prior finding proposed is still absent, and staging is the vehicle that would perform it.

**Commitment 2 — the meaning-lock must be a "real separate step, not narrated in one motion."**
- **Source:** `2026-07-11_00-24/finding.md` (the config-blind Pass-1 caveat).
- **Re-test status: RE-TESTED — commitment confirmed but frame revised.** This commitment IS the soft-borders question. Re-testing it against the "still one run" constraint shows that in-one-pass stage borders are precisely the "narrated in one motion" kind — soft. So the prior's own caveat is what caps staging: within one run, staging cannot deliver the "real separate step," only a stronger-worded instruction. The frame shift: the prior treated this as a Pass-1 detail; here it is the load-bearing ceiling on the entire staging proposal.
- **Evidence:** nothing in a single model pass freezes Stage-1 output before Stage-2; true separation needs the emitted-artifact or separate-pass rungs, which require relaxing "one run."

**Commitment 3 — the post-draft check splits into a trustworthy mechanical spine and a not-guaranteed judgment agenda (tiered reliability).**
- **Source:** `2026-07-11_01-09/finding.md`.
- **Re-test status: RE-TESTED — commitment confirmed.** It is load-bearing twice here: it is why the runtime-provenance idea is rejected (a self-report is a judgment, so it sits at the "not guaranteed" tier and cannot reliably attest), and it is what staging's check-stage hosts (the mechanical spine).
- **Evidence:** the analysis routes the mechanical checks to the final check-stage (reliable) and declines to have the model narrate its own judgment-level preservation (unreliable).

**Commitment 4 — within the checks, the mechanical core is reliable and the structural/judgment rim is rubber-stamp-prone.**
- **Source:** `2026-07-11_01-09/finding.md`.
- **Re-test status: RE-TESTED — commitment confirmed.** The deferred, narrowed runtime-provenance option is scoped to the *mechanical* checks only for exactly this reason — a self-report can attest a mechanical fact but not a judgment one.
- **Evidence:** the finding narrows any runtime trace to the mechanical checks and the existing harmony report, never the judgment rim.

## Next Actions

### MUST

- **What:** Decide, per proposal, how far to travel — evaluate-only [delivered]; +produce the design spec; or +apply. The two proposals are independent: the changelog can be adopted on its own, and staging is separately gated on the prior three-pass fix.
  - **Who:** the user.
  - **Gate:** before any build/apply work (condition-bound).
  - **Why:** the evaluation stands on its own; the designs and applies need authorization, and staging's apply is doubly gated (on the prior fix being applied first).

### COULD

- **What:** Adopt the lean single-file authoring changelog — one `CHANGELOG.md` (or decisions log) with dated entries (rule/policy · what · why), and house the soft-border caveat there. Explicitly one file, not a file-per-change.
  - **Who:** the SKILL author.
  - **Gate:** observable — adoptable immediately; not gated on the prior fix.
  - **Why:** the cheapest, highest-independent-value part; the literal "visible for us."
  - **Depends-on:** MUST item "decide the reach." OVERRIDE: adoption-ready independent of the staging reach and of the prior fix — this proposal is fully separable (the two-proposal split) and standalone-valuable; only the formal "go" is pending.

- **What:** Produce the finalized staged-Step-5 spec — the stage set (config-resolution → comprehension → meaning-lock → harmony-generate → check), the ordered-with-permitted-back-reference rule, the mechanical spine as the check-stage, and the caveat's placement (authoring docs).
  - **Who:** a design pass.
  - **Gate:** observable — once the reach selects design-or-apply for staging.
  - **Why:** turns the evaluation into a ready-to-apply artifact.
  - **Depends-on:** MUST item "decide the reach." This COULD is GATED — do not act until the MUST resolves.

- **What:** Apply the staged Step 5 to `SKILL.md` (restructure the flat bag into the ordered sequence).
  - **Who:** a SKILL edit pass.
  - **Gate:** condition-bound — after the prior three-pass fix (`2026-07-11_00-24`) is applied.
  - **Why:** realizes the staging; doubly gated (reach + the prior fix).
  - **Depends-on:** MUST item "decide the reach" AND the prior fix. GATED.

- **What:** Validate staging empirically — re-translate the original error-laden chunk with the staged Step 5 vs the flat bag and compare the error signature.
  - **Who:** a test pass.
  - **Gate:** observable — after the spec exists.
  - **Why:** the "probability-raiser" claim is reasoned, not evidenced; this would confirm or correct it.
  - **Depends-on:** MUST item "decide the reach." GATED.

- **What:** Back-link the prior three-pass finding, noting staging EXTENDS it (generalizes its wiring to all layers).
  - **Who:** a light edit pass.
  - **Gate:** condition-bound — whenever the prior chain is next touched.
  - **Why:** keeps the lineage coherent so staging is not read as a rival to the three-pass fix.

### DEFERRED

- **What:** The emitted-artifact enforcement upgrade — require the meaning-lock stage to emit a real intermediate artifact (the forcing function).
  - **Gate:** revival — if the user later wants *enforced* separation and is willing to relax the "still one run" constraint (this is the prior finding's deferred "real separate step").
  - **Why (if revived):** climbs the gradient from nudge toward enforcement.

- **What:** The gradient empirical question — does an emitted meaning-lock artifact *within one pass* actually beat a prose stage-header *within one pass*?
  - **Gate:** revival — after the staging validation baseline exists.
  - **Why (if revived):** turns the gradient's middle rung from plausible to established.

## Reasoning

**Why "two proposals, not one":** the staging and the middleware files differ on every axis that matters — beneficiary (translation-correctness vs SKILL-author-maintainability), novelty (staging ≈ the prior fix; the changelog is new), cost, and reliability profile. Treating them as one architecture would have bundled a modest, gated correctness restructure with a cheap, ungated maintainability convention and evaluated them together — hiding that the changelog is independently adoptable now.

**Why staging "survives modestly" and does not dissolve into the prior fix:** a redundancy challenge was run hard. Staging's correctness core *is* the prior three-pass fix. It survives only via (a) the generalization — staging *all* the collapsed layers, not just the harmony passes — and (b) providing a defined check-stage home for the mechanical spine. Both are real but modest; the load-bearing correctness work is the prior fix's.

**Why the runtime "middleware" trace and the file-per-change form were rejected:** a per-translation trace of "what each rule did" is expensive and, worse, a self-report — which the prior tiered-reliability finding places at the "not guaranteed" tier, so it cannot reliably attest the judgment-level work. And the file-per-change form of the *authoring* changelog has the identical over-engineering shape as a file-per-rule runtime trace. The lean form of both is entries in one document — the sharpest reusable lesson here.

**Why the caveat must move out of the runtime text:** an instruction that tells its reader (the model) that its own borders are non-binding invites the reader to relax them. The caveat is authoring knowledge (preventing the *human's* false confidence), so it belongs where the human reads it.

**Why EXTENDS + REFINES, not supersede:** supersede was considered and rejected — staging does not replace the three-pass method, it generalizes it; and the prior tiered-reliability finding is confirmed, not overturned (a border and a self-report are instances of its "not guaranteed" tier).

## Open Questions

### Research Frontiers
- Whether an emitted intermediate artifact *within a single model pass* measurably reduces the collapse-into-one-motion failure more than a prose stage-header does — no evidence yet; empirical.
- Whether "enforced" staging (a genuinely separate meaning-lock pass) is worth relaxing the "one run" constraint — the deferred forcing-function upgrade.

### Blocked
- Staging cannot be *applied* to correctness effect until the prior three-pass fix (`2026-07-11_00-24`) is built into the SKILL; staging's correctness core is that fix.

### Refinement Triggers
- If empirical validation shows the staged Step 5 does *not* reduce the error signature versus the flat bag, the "probability-raiser" verdict re-opens — re-open on that specific observation.
- If the authoring changelog is adopted and goes unmaintained, its "earns its keep" verdict re-opens (an unmaintained log misleads) — re-open on observed staleness.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
u said 

Config-derived check-agenda. The checks are generated from whichever config axes are active — the reader-level axis emits a "too-hard word" scan, the fidelity rules emit the source-vs-draft comparison, and so on. (An earlier framing called this making the config "self-enforcing." The critique flagged that as an overclaim: the mechanical checks are genuinely reliable, but the judgment checks re-invoke the same fallible reading that failed the first time. The honest framing is a config-derived agenda with tiered reliability — mechanical checks are trustworthy; judgment checks are better-than-nothing but not guaranteed.)


this gave me this idea of using stage 1 stage 2 like borders in the skill (still one run but more explicit seperation of harmony and policies etc). this way we are able to stack things (principles policies etc) explicitly in right order , and we can even make middleware md files for each change so it is visible for us what rule policy changed how etc. 

lets dive deep into this , if this makes sense and if yes how
```

</details>
