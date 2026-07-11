# Branch: Staged SKILL Borders and Middleware Files

## Source Input

The user's raw request, preserved verbatim (also in `articulate_simple.md`'s `## User Input`):

```text
u said 

Config-derived check-agenda. The checks are generated from whichever config axes are active — the reader-level axis emits a "too-hard word" scan, the fidelity rules emit the source-vs-draft comparison, and so on. (An earlier framing called this making the config "self-enforcing." The critique flagged that as an overclaim: the mechanical checks are genuinely reliable, but the judgment checks re-invoke the same fallible reading that failed the first time. The honest framing is a config-derived agenda with tiered reliability — mechanical checks are trustworthy; judgment checks are better-than-nothing but not guaranteed.)


this gave me this idea of using stage 1 stage 2 like borders in the skill (still one run but more explicit seperation of harmony and policies etc). this way we are able to stack things (principles policies etc) explicitly in right order , and we can even make middleware md files for each change so it is visible for us what rule policy changed how etc. 

lets dive deep into this , if this makes sense and if yes how
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-07-11_04-12__staged_skill_borders_and_middleware/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** Item 1 — the staged-SKILL-architecture proposal (ordered stage-borders + per-change middleware md files; evaluate + gated design)
- **Verdict:** MED-FLAG
- **Flagged conditions:** (1) late-split signal — the ordered-staging proposal vs the middleware-files proposal are separable sub-deliverables of different types (Decomposition to resolve); (2) TARGET ambiguity — runtime-staging (execution stages in one pass) vs authoring-structure (how the `.md` files are organized) vs both; (3) "middleware md files" meaning ambiguity — per-SKILL-edit changelog vs per-translation provenance trace vs per-principle passthrough-spec.

## Question

**Literal (the user's own words):** "this idea of using stage 1 stage 2 like borders in the skill (still one run but more explicit separation of harmony and policies etc) … stack things (principles policies etc) explicitly in right order, and we can even make middleware md files for each change so it is visible for us what rule policy changed how etc. lets dive deep into this, if this makes sense and if yes how."

**What kinds of ask this carries (MQ1 verdict-axis — preserved as open):**
- an **evaluation** — does explicit staging + middleware-files make sense (a soundness judgment, given the prior chain)?
- a **design** — "if yes, how": the concrete architecture (stage structure + ordering + the middleware-file scheme);
- most likely **evaluate-then-gated-design** (design gated on the evaluation, matching the prior inquiries' reach pattern).

**Two load-bearing sub-ambiguities in what's being asked:**
- **TARGET of "borders in the skill":** runtime-staging (ordered execution *stages* the model moves through while translating, in one pass) / authoring-structure (how the SKILL's `.md` files + `SKILL.md` steps are *organized* into ordered bordered sections) / both.
- **"middleware md files for each change":** "each change" = each SKILL EDIT (a changelog of what rule/policy was altered and how) / each TEXT-TRANSFORMATION at translation time (a per-run provenance trace) / "middleware" = each principle-as-its-own-passthrough-file.

**Plausible action-endpoints (MQ3 intent-axis — preserved as open):** make-implicit-order-explicit (correctness) · gain-visibility (inspection/debugging) · enable-stacking/composition (maintainability) · enforce-separation-within-one-run (prevent the collapse-into-one-fluent-motion failure).

## Goal

**Deliverable shape (Deconstruct):** an evaluation + a gated design — an understanding-artifact that judges whether explicit staging + middleware-files is sound and, if so, specifies the staged architecture + the middleware-file scheme. Kinds: {soundness-judgment, architecture/ordering-design, optional SKILL-edit spec}. Bounds: **within one run** (stated); about **structure/order/visibility, not principle-content**; grounded in the actual SKILL + the prior chain.

**Motivations a good answer might serve (MultiDepth WHY-axis — preserved as open):**
- **correctness-drive** — explicit borders prevent the passes/principles collapsing into one fluent motion (the chain's root failure); staging as an enforcement mechanism inside one run;
- **visibility/control-drive** — after the tiered-reliability finding (judgment checks not guaranteed), the user wants to SEE and control what each rule does and how it changed;
- **maintainability-drive** — a modular, explicitly-ordered, stackable architecture, easier to extend and reason about;
- **auditability-drive** — the middleware files as a traceable record ("visible for us"), distinct from correctness.

**Context downstream needs (MQ2):**
- **verdict:** the prior-chain findings (the un-applied 3-Pass method; the config-independent/derived split; the flat-Step-5-apply-bag diagnosis) as the baseline the staging modifies; AND the *actual current* SKILL.md + `references/core/*` structure that "stages/borders" would reorganize.
- **kinds:** does "stage 1 / stage 2" map onto the existing 3-Pass (Meaning Lock / Harmony Map / Target Reconstruction), onto the harmony-vs-policies separation, or onto a new axis?
- **stance:** a real implementable SKILL restructure, or a conceptual exploration of whether staging-within-one-run is sound?

**Explicit exclusions (MQ4 — the negative spec):**
- **still one run** — EXCLUDES multi-run / multi-agent / separate model invocations; staging lives inside a single model pass. (Load-bearing.)
- **structure-not-content** — plausibly excludes changing WHAT the principles are (organize/sequence/expose them, don't add/remove them).

## Considered Articulations

**Item 1 — the staged-SKILL-architecture proposal:**
1. **Runtime-staging reading (evaluate + design):** Evaluate whether reorganizing the SKILL's flat "apply these principles" step into explicit ordered *runtime* stages (still one model pass), with harmony rules and config policies separated and sequenced, is sound — and if so specify the stage structure + ordering.
2. **Authoring/document-structure reading:** Evaluate whether restructuring the SKILL's reference documents into explicitly-bordered, ordered layers (harmony layer / policy layer / …) plus a per-edit changelog ("middleware md") recording what each rule/policy change did — and design that document architecture.
3. **Runtime-provenance reading of "middleware files":** Evaluate whether adding a per-translation provenance trace (middleware md files recording, per stage, what transformation each rule/policy applied to the text) is sound and worth its cost — and design it.
4. **Prior-3-Pass-alignment reading:** Assess whether the user's "stage 1 / stage 2" *is* the prior inquiry's un-applied 3-Pass (Meaning Lock / Harmony Map / Target Reconstruction) made explicit — i.e., whether staging is the vehicle that finally applies that fix — and design the unification.
5. **Joint both-parts reading (gated reach):** Evaluate both sub-proposals together (ordered staging AND middleware traceability files) as one SKILL-architecture, decide whether each earns its keep, and design the ones that do — reach-gated (evaluate-only / +design / +apply).

## Scope Check

**Question covers goal:** YES — the question (evaluate + how) covers the goal (a soundness judgment + a gated design of the staged architecture and middleware scheme), within the stated bounds (one run; structure not content).

**Specific-vs-pattern check:** the proposal points at specific mechanisms ("stage 1 / stage 2", "middleware md files"). Default to the **broader pattern** those illustrate — i.e., *whether explicit staged organization + a per-change traceability layer is the right architecture for this SKILL*, not only whether the exact two-stage/middleware-file wording is adoptable. The literal mechanisms are treated as the user's first-draft expression of the pattern, refinable downstream (the prior siblings did the same: right instinct, refined form).

## Layer Commitment

**Primary layer: STRUCTURAL** — the proposal is chiefly about the SKILL's spec *shape*: making the flat apply-bag into explicitly-bordered, ordered, separated sections (harmony vs policies), and adding a per-change traceability artifact (the "middleware md files"). The user's own vocabulary is structural ("borders in the skill", "separation", "stack things explicitly", "visible for us what changed").

**Other layers considered, out of scope for THIS run (with reason):**
- **Process** — sequential dependency, largely **inherited** from prior `2026-07-11_00-24` (the ordered-execution semantics — whether borders actually enforce staged execution within one model pass — rests on that prior's 3-Pass Step-5 wiring). This inquiry makes that ordering *structurally explicit* and adds a visibility layer; it does not re-decide the process ordering. If the evaluation finds the borders cannot be structural-only and must change the run's procedure, a follow-up Process-layer inquiry is named.
- **Meaning** — out of scope: this does not redefine what the SKILL *is* as a translation operation; it reorganizes its structure.

## Synthesis Trigger

This inquiry builds on and restructures the outputs of the prior chain (MQ2's verdict sub-axis names ≥2 priors as required context). Priors consumed:
- `devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md` — commits the three-pass method (Meaning Lock → Harmony Map → Target Reconstruction) and the meaning-first Step-5 wiring (the un-applied fix that staging would make explicit). **Most load-bearing** — staging is a candidate vehicle for applying it.
- `devdocs/inquiries/2026-07-11_01-09__firing_time_categories_for_principles/finding.md` — commits the config-independent spine (mechanical core + soft rim) / config-derived agenda split, with tiered reliability (the springboard; staging would organize these into bordered sections).
- `devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md` — the base: one-fluency-first-pass / no-checkpoint diagnosis + the mechanical omission-diff spine.

CONCLUDE must include an `## Inherited Commitments Re-test` naming each prior's load-bearing commitments and re-testing them (does explicit staging *serve* the 3-Pass wiring or *duplicate/complicate* it? does bordering respect the tiered-reliability finding, i.e., does making a judgment check "explicit" wrongly imply it became reliable? does the "still one run" constraint keep the staging compatible with the priors' single-pass fix?). Sensemaking and Critique must do this re-testing, not just record it.
