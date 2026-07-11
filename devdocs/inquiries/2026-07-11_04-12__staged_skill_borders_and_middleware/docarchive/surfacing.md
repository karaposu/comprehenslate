## User Input

`_branch.md`. Territory (artifact case): the comprehenslate SKILL's actual structure — `SKILL.md` (esp. Step 2 flat-load + Step 5 flat "Apply:" bag), `references/core/harmony_layer.md` (the 3-Pass + Tier 1-4 + hard constraints + harmony report), `references/core/{translation_principals,advanced_principles,notes}.md`, `references/config/{schemas.py, config_base_source.md, policy_config_base_source.md}` — plus the prior chain findings. Purpose: draw into attention the SPECIFIC structures bearing on whether explicit staged borders (still one run) + per-change "middleware md files" make sense and how — resolving the three flags (runtime-staging vs authoring-structure; middleware-file meaning; the staging/middleware late-split). Mode: artifact / signal-first.

---

# Surfacing — Staged SKILL Borders + Middleware Files

## Regions traversed (7)

| Region | What it holds | Relevance |
|---|---|---|
| **R1 — SKILL.md Workflow** | Step 2 flat-loads ALL reference files "in full"; Step 5 (line 73 "Then produce the translation. Apply:") is a FLAT 5-bullet bag (config choices · policy defaults · principles · harmony Tier 1-4 · notes) | **core** (HIGH) — the exact restructure target |
| **R2 — harmony_layer.md** | line 7 "works in three passes" (Pass-1 Meaning Lock / Pass-2 Harmony Map / Pass-3 Target Reconstruction); the Tier 1-4 preserve-weight ordering; the hard-constraints block (line 15-17); the "harmony report" (lines 145, 166) | **core** (HIGH) — the staging half + the middleware half both latent here |
| **R3 — file-level layering** | `references/config/` (schemas + 2 calibration files) vs `references/core/` (4 principle/harmony files) — a de-facto separation already on disk | **core** (HIGH) — "separation of harmony and policies" is partially present already |
| **R4 — schemas.py** | `TranslationConfig` (A1-A8) + Policy classes + **`PipelineConfig`** (a "pipeline" abstraction already named) | **sub** (MED) — the config layer; PipelineConfig is a latent staging hook |
| **R5 — config calibration files** | `config_base_source.md` (the 8 axes' calibration) + `policy_config_base_source.md` (the Policy enums) | **side** (MED) — the config layer's depth; a candidate "policy stage" |
| **R6 — core principles** | `translation_principals.md` + `advanced_principles.md` + `notes.md` — the ~80 "On X" detection principles (the comprehension-time bloc) | **sub** (MED) — a candidate "comprehension stage" |
| **R7 — prior chain findings** | `2026-07-11_00-24` (wire the 3-Pass into Step 5) · `2026-07-11_01-09` (config-independent spine + config-derived agenda, tiered reliability) · `2026-07-10_23-03` (one-fluency-pass / no-checkpoint) | **core** (HIGH) — the baseline the staging overlaps/extends |

## Decisive findings (the surfacing yield)

**DF1 — the STAGING half is already LATENT in the SKILL, just un-wired.** `harmony_layer.md` line 7 literally defines "a translation mode that works in three passes" — Pass-1 Meaning Lock ("the foundation that cannot be violated"), Pass-2 Harmony Map, Pass-3 Target Reconstruction. **The stages exist as text.** But `SKILL.md` Step 5 imports the file ONLY as "the harmony-layer Tier 1-4 preservation policy" (line 78) and never invokes the 3-Pass as an ordered runtime sequence. So the user's "stage 1 / stage 2 borders" is, for the harmony core, ~*make explicit and wire what is already written as stages*. This is DECISIVE: the staging proposal is not building from nothing — it is finishing an un-wired structure. (It is also nearly identical to prior `2026-07-11_00-24`'s fix — see DF5.)

**DF2 — the "separation of harmony and policies" is PARTIALLY present, then COLLAPSED at Step 5.** On disk there is already a layer split: `references/config/` (schemas + config calibration + policy calibration) vs `references/core/` (principles + advanced + harmony + notes). But Step 5's flat "Apply:" bag (lines 73-79) re-mixes config choices + policy defaults + translation principles + harmony Tiers + notes into ONE undifferentiated list. So the separation the user wants exists at the *directory* level and is *destroyed* at the *workflow* level. Staging = restore, at the workflow, the separation the file tree already implies.

**DF3 — "stack in the right order" is under-specified because there are ALREADY ≥3 orthogonal orderings.** Inside `harmony_layer.md` alone: (a) the **3-Pass temporal order** (Meaning → Harmony → Target); (b) the **Tier 1-4 priority order** (preserve-weight); (c) the **hard-constraints block** (absolute prohibitions). Across the SKILL: (d) the config→policy→principles→harmony layering. "Stage 1 / stage 2 borders" must choose WHICH axis it means — these are not one line, and conflating them is a real risk. The most defensible reading: the *temporal* order (comprehend → generate → check) is the "stage" axis; the Tier/priority orderings are *within-stage* content.

**DF4 — the MIDDLEWARE half also has a latent seed: the "harmony report."** `harmony_layer.md` already references a **harmony report** where the translator "documents the choice" (line 166) and acknowledges untransferable features (line 145). That is a latent *runtime-provenance* artifact — a per-translation record of what each harmony decision did. So "middleware md files for each change" has two live readings, one of which is half-built: (i) **runtime-provenance** = formalize/extend the harmony report into a per-stage "what each rule did to this text" trace; (ii) **authoring-changelog** = a per-SKILL-edit record of what rule/policy changed and why. `schemas.py`'s `PipelineConfig` is a third latent hook (a named "pipeline" the stages could attach to).

**DF5 — the staging half HEAVILY OVERLAPS prior `2026-07-11_00-24` (redundancy pressure).** Making Step 5 an ordered staged sequence *is* substantially that prior's fix ("wire the 3-Pass into Step 5, meaning-first"), generalized from the harmony 3-Pass to *all* layers. So the genuinely-NEW content of this proposal is narrower than it looks: (a) **generalizing** the wiring beyond harmony (an explicit config-stage / policy-stage / comprehension-stage / harmony-stage / check-stage ordering), and (b) the **middleware/traceability files** (no prior proposed these). The bare "add stage borders" idea, for the harmony core, is the prior fix re-described.

**DF6 — "still one run" makes the borders SOFT, which is the core soundness question.** Borders inside a single model pass are textual headers the model reads; nothing *enforces* that Stage-1 output is frozen before Stage-2 begins. Prior `2026-07-11_00-24` already flagged exactly this: "config-blind Pass-1 is robust only if it is a real separate step, not narrated in one motion." So explicit "Stage 1 / Stage 2" headers **help** (they make the intended order visible and instructable) but do **not guarantee** the passes don't blend — the same collapse-into-one-fluent-motion failure the whole chain diagnosed can recur one level up. This maps directly onto the springboard finding's *tiered reliability*: a textual border is a "better-than-nothing but not guaranteed" enforcement, exactly like a judgment check. Naming a stage does not make the model obey the stage.

## Frontier flags (for Warm / Sensemaking / Decomposition)

- **FF1 — which ordering axis?** Does "stage borders" mean the temporal comprehend→generate→check order, the Tier priority order, or the config/policy/harmony layer-type separation? (DF3.) Default lean: temporal stages as the border axis; the others are within-stage.
- **FF2 — middleware = runtime-provenance (formalize the harmony report) OR authoring-changelog?** (DF4.) The two differ sharply in cost and value; resolve which (or both) before designing.
- **FF3 — do textual borders in one run enforce separation, or are they soft?** (DF6.) This is THE soundness question for the staging half — and it inherits the tiered-reliability answer (helps, not guaranteed).
- **FF4 — the late-split:** evaluate staging and middleware-files separately — they have different overlap-with-priors (staging ≈ the prior fix; middleware is genuinely new) and different cost. (Articulate flag 1.)

## State Summary

- **Territory:** the comprehenslate SKILL (`SKILL.md` + `references/core/*` + `references/config/*`) + the prior chain findings. Explicit-bounded.
- **Purpose:** locate the structures bearing on explicit staged borders + middleware files, and resolve the three articulation flags.
- **Coverage:** R1/R2/R3/R7 confirmed (read in full / decisive); R4 confirmed (schemas structure + PipelineConfig noted); R5/R6 scanned (known from prior inquiries — the config calibration + the ~80 detection principles).
- **Confirmed-absent:** no existing "middleware"/changelog/traceability artifact anywhere in the SKILL (the harmony report is the closest latent seed; no per-change record exists) — this is the genuinely-empty region the middleware half would fill.
- **Concept-names surfaced:** three-passes (latent stages) · Tier 1-4 (priority ordering) · hard-constraints block (the spine) · harmony report (latent runtime-provenance) · PipelineConfig (latent pipeline hook) · config/core file split (latent layer separation) · the flat Step-5 Apply-bag (the collapse point).
- **Workspace-populated:** true.

**Self-assessment: PROCEED** — territory swept at identity resolution; the three flags are resolvable against surfaced structure; one strong redundancy-pressure finding (DF5) and one core soundness question (DF6) handed to Sensemaking. Asymmetric-failure honored (included the latent-seed readings rather than pre-filtering). No LAYER 1/2 flags.
