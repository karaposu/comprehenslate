## User Input

> But the critique caught this framing being too clean, and the correction matters. Calling the failed principles "verification-shaped" (checking-only by nature) overstates it. Take "allegorical": a first pass properly holding A1=conversational (the reader-level axis that literally excludes dense-academic vocabulary) in mind could have picked "parable" or "comparison" while writing — no separate check needed. Same for "work" vs "foothold": if the sense-disambiguation policy had fired during writing, the right word comes out the first time. So these principles are dual-natured — able to fire while writing or at a check. The honest statement is: in a single fluency-first pass they went un-fired at generation, and there was no checkpoint to catch them afterward. The practical conclusion (add a checkpoint) is unchanged; only the mechanism-claim is softened.
>
> and this made me thing that it would be really useful to use these 2 categories fireable_at_first_pass and fireable_at_second_pass for our principles or policies (not sure maybe both )

Context: follow-up to two prior inquiries — (1) `2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md` (7 errors = one fluency-first pass, no post-draft checkpoint; critique corrected "verification-shaped" → "dual-shaped" principles); (2) `2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md` (root cause = the SKILL's 3-Pass method never proceduralized by SKILL.md Step 5; two gates missing for one reason). Proposal targets the comprehenslate SKILL's principle/policy files (`references/core/*.md`; `references/config/schemas.py` Policy classes). Design/proposal inquiry + possible gated SKILL edit.

---

## Stage 1 — Itemize

**count = 1**

**Per-item identifier:** `item-1` (firing-time categorization of the SKILL's principles/policies).

**Keep-together reasoning:** the statement has two paragraphs, but the first is *rationale* (the accepted mechanism-correction: principles are dual-natured — able to fire at writing OR at a check, not verification-only), and the second is the *actual ask* (adopt two firing-time categories — `fireable_at_first_pass` / `fireable_at_second_pass`, maybe both — for the principles/policies). The rationale is not a separate work item; it is the premise the proposal rests on. Asymmetric-failure bias toward keep-together holds — the mechanism-correction and the proposal it motivates are one coupled ask.

---

## Stage 2 — Meta-question + MQA (item-1)

### MQ1 — verdict-axis: what is the user asking for?
**Answer: identified-ambiguities-list**
- **adjudication stance:** `[confirm-the-proposal-is-useful / evaluate-honestly-and-possibly-refine-or-reject / design-the-actual-scheme / diagnose-whether-it-earns-its-keep-given-the-3-Pass-fix-already-exists]`
- **tagging target (scope):** `[principles only / policies only / both principles AND policies]` — the user explicitly wavered ("for our principles or policies (not sure maybe both)")
- **category structure:** `[two independent binary flags (fireable_at_first_pass ∈ {y,n}, fireable_at_second_pass ∈ {y,n}) / a single 3-value enum (first-only / second-only / both) / a richer scheme with a "neither/inert" or "conditional" value]`
- **deliverable endpoint:** `[a yes/no-with-rationale on adopting / a concrete tag-scheme design / an actual per-principle classification inventory / a SKILL spec-edit that adds the metadata]`

### MQ2 — context-need axis: what context does the response need?
**Answer: identified-ambiguities-list**
- **verdict sub-axis (what prior/external content is needed):** `[the two prior findings as baseline (the dual-shaped correction; the two-gate 3-Pass fix) / the actual content of the SKILL's principle/policy files — references/core/{harmony_layer.md, translation_principals.md, advanced_principles.md, notes.md} and references/config/schemas.py Policy classes — to know what would be tagged and whether the tag is decidable per item]`
- **kinds sub-axis (what "principles" and "policies" concretely denote here):** `[the harmony Tier 1-4 entries / the translation_principals bullets / the advanced_principles (escalation-chain, self-illuminating-text) / the always-on no-smoothing rule / the schemas.py Policy classes (SourceApparatusPolicy, NonMainLangPartsPolicy, etc.) — these are heterogeneous; "principle" vs "policy" may tag differently]`
- **stance sub-axis:** `[honest evaluation — is firing-time tagging genuinely useful, or does it (a) overlap what the 3-Pass wiring already delivers, (b) add taxonomy overhead, (c) mis-fit principles that are genuinely dual or context-dependent? / ratify-and-design — take the proposal's value as given and produce the scheme]`

### MQ3 — intent-axis (WHAT): what is the user trying to accomplish?
**Answer: identified-ambiguities-list**
- `[make-firing-time-explicit-as-metadata (each principle carries a when-it-fires tag, for clarity/documentation) / drive-the-two-gate-procedure (first-pass tags tell Pass-1/Meaning-Lock which principles to hold while generating; second-pass tags tell Pass-3/the-check which to verify) / auto-generate-the-check-agenda (the second-pass set mechanically becomes the post-draft checklist) / establish-a-design-discipline (every present and future principle must declare its firing time as a standing invariant)]`

### MQ4 — boundary-axis: what is the user explicitly excluding?
**Answer: identified-ambiguities-list**
- `[excludes re-adjudicating the dual-natured mechanism-correction (it is stated as accepted premise — "the practical conclusion is unchanged; only the mechanism-claim is softened") / excludes re-diagnosing the 7 errors or re-deriving the 3-Pass fix (settled priors) / does NOT exclude the "both" category — the user explicitly invites it ("maybe both")]`

### MQA — alignment
**Reconcile — two joint axes identified:**
- **Joint axis 1 — CATEGORIZATION-PURPOSE (documentation vs operational-driver):** MQ1's "category structure / deliverable endpoint" and MQ3's "make-explicit-as-metadata vs drive-the-procedure vs auto-generate-the-agenda" span the same underlying axis — *is the tag inert metadata, or does it actively drive the two gates?* This is the load-bearing openness: a purely descriptive tag is cheap but may add nothing beyond the 3-Pass; an operational tag that generates the Pass-1 hold-set and the Pass-3 check-agenda is where the value would be.
- **Joint axis 2 — TAGGING-TARGET (which heterogeneous artifacts get tagged, and is the tag even well-defined per artifact):** MQ1's "tagging target (scope)" and MQ2's "kinds sub-axis" span the same axis — *what counts as a "principle" or "policy" here, and does firing-time cleanly apply to each?* Some entries (harmony Tiers, the no-smoothing rule) may be genuinely dual or context-dependent, so a clean first/second partition may not fit all of them — which is exactly why the user hedged "maybe both."

---

## Stage 3 — Deconstruct + MultiDepth (item-1)

### Deconstruct
**Tuple:** `(deliverable: a design-plus-evaluation artifact — should-we-adopt firing-time categories + what the scheme IS + what it changes, with an actual per-principle classification and/or a SKILL spec-edit as gated reach; kinds: analysis + design + possibly annotation/spec-edit; bounds: the SKILL's principle/policy files × the two-gate procedure from the prior finding × the first-pass/second-pass/both firing-time distinction)`.

**Late-split check:** the evaluate / design-the-scheme / classify-each / edit-the-SKILL endpoints are *reaches of one proposal* (a graded output-reach, exactly like the two prior inquiries' diagnose→fix-design→apply gradient), not distinct work items. No late split — one item with a reach axis.

### MultiDepth
**Literal-statement:** *"The critique's correction — that the failed principles are dual-natured (able to fire while writing OR at a check), not verification-only — makes me think it would be really useful to use two categories, `fireable_at_first_pass` and `fireable_at_second_pass`, for our principles or policies (not sure — maybe both)."*

**Identified-purpose-motivation-ambiguities (WHY-axis): identified-ambiguities-list**
- `[operationalize-the-two-gates: turn the abstract "two gates" from the prior finding into something concrete and actionable per-principle / prevent-recurrence-at-generation: the deeper failure was principles un-fired AT GENERATION; knowing which principles are first-pass-fireable is what lets Pass-1 actually fire them / enable-tooling: the second-pass set could auto-produce the post-draft check agenda, making the check mechanical rather than ad-hoc / taxonomic-understanding: simply understand the principle corpus better by classifying when each acts / design-hygiene: force every principle to declare its firing time so the "stated-but-never-fired" gap can't recur silently]`

---

## Stage 4 — Rephrase (item-1) — Considered Articulations

1. **Honest evaluation.** *"Assess whether tagging the SKILL's principles/policies with firing-time categories (`fireable_at_first_pass` / `fireable_at_second_pass` / both) is worth adopting — does it add operational value beyond what the 3-Pass wiring already delivers, or is it taxonomy overhead / a mis-fit for genuinely dual principles?"*
2. **Scheme design.** *"Design the firing-time categorization scheme — the tag structure (two binary flags vs a 3-value enum with a 'both'/'conditional' value), where the metadata lives (per-entry in `references/core/*.md` and `schemas.py`), and how a principle's firing-time is decided."*
3. **Operational driver.** *"Specify how firing-time tags DRIVE the two-gate procedure — first-pass tags become the set Pass-1 (Meaning Lock) holds while generating; second-pass tags mechanically generate the Pass-3 post-draft check agenda — so the tag is not inert metadata but the thing that wires the gates."*
4. **Annotation inventory.** *"Actually classify each of the SKILL's principles/policies (harmony Tiers, translation principles, advanced principles, the no-smoothing rule, the schemas.py Policy classes) by firing-time — first-only / second-only / both — producing the tagged inventory."*
5. **Design discipline.** *"Establish firing-time declaration as a standing requirement — every principle/policy in the SKILL, present and future, must declare when it can fire, as a design-hygiene invariant that prevents the 'stated-but-never-fired-at-generation' gap from recurring."*

---

## Self-Assessment

**Bundle self-check (LAYER 1, single LIGHT pass):**
- Mode 1 (premature split): not-fire — count=1, keep-together justified.
- Mode 2 (late multi-item): not-fire — the reach endpoints are one item's graded reach, not distinct items (Deconstruct confirms).
- Mode 3 (MQ extension): not-fire — four canonical axes only.
- Mode 4 (per-operation firing missed): not-fire — all fields present.
- Mode 5 (MQ2 missing prep content): not-fire — verdict / kinds / stance all present.
- Mode 6 (MQ2 missing kinds/stance): not-fire — both present.
- Mode 7 (2-shape violation): not-fire — every MQ answer is identified-ambiguities-list; none is a commitment.
- Mode 8 (AMBIGUITY-NATURE conflation): not-fire — MQ3 holds WHAT (action endpoints); MultiDepth holds WHY (motivations).
- Mode 9 (considered-articulations drift): not-fire — all five variants preserve the design/evaluation deliverable shape, span the identified ambiguity dimensions (purpose axis + reach axis), include no MQ4-excluded vocab (no re-diagnosis, no mechanism re-litigation), stay within substrate.

**Verdict: HIGH-PROCEED** — clean self-check, low friction. The one live tension (is firing-time tagging genuinely additive, or does it overlap the already-designed 3-Pass wiring?) is captured as the MQA joint-axis-1 openness and the MQ2 honest-evaluation stance, not suppressed — so the pipeline inherits it as a fork to resolve rather than a defect.
