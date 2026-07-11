# Sensemaking — Does firing-time categorization survive as its own contribution?

## User Input

`_branch.md` + surfacing (18 items, the actual corpus) + warm (non-severe content-conflict = form-refinement). Warm-settled anchor: firing-time is a genuine useful axis (instinct affirmed) but the clean-2-category-over-a-homogeneous-list FORM mis-fits; resolve Fork 1 (inert vs operational; does it earn its keep or is it redundant with the 3-Pass wiring?) and Fork 2 (the right FORM given dual-majority + missing-comprehension-phase), and test three rivals: (a) redundancy, (b) over-engineering, (c) the deep rival (does firing-time dissolve into the prior inquiries' config-derived scoped check?). Ground against the actual corpus; don't assume.

---

## SV1 — Baseline Understanding

The user, prompted by the prior critique's "dual-shaped principles" correction, proposes tagging the SKILL's principles/policies with two firing-time categories (`fireable_at_first_pass` / `fireable_at_second_pass`, maybe both). At first read this is an appealing, clean formalization of the two-gate insight. The task is to design/evaluate it.

---

## Phase 1 — Cognitive Anchor Extraction

**Constraints:**
- C1 — The corpus is heterogeneous (≥4 kinds: harmony components / ~80 detection principles / config policies / meta-principles). A single tagging scheme must survive this heterogeneity (DF1).
- C2 — Dual ("both") is the majority: most substantive principles can fire at generation AND be checked after (DF2). A possibility-tag ("can it fire at second pass?") lands "yes" for most → non-discriminating.
- C3 — Metadata is a real cost: harmony components already carry Tier-weight (+ Tier-3 context-condition); firing-time is a 3rd axis (DF4).
- C4 — The prior inquiries already exist and are load-bearing: `2026-07-10_23-03` (dual-shaped principles; the ACTIONABLE design = config-keyed scoped check-agenda with a **mechanical omission-diff spine first**) and `2026-07-11_00-24` (the 3-Pass wired meaning-first; two gates).

**Key Insights:**
- KI1 — The value of a firing-time tag is entirely in whether it produces a **small, actionable set**. A tag that classifies most of the corpus into "both" produces no useful partition (DF5).
- KI2 — "Can fire at second pass" (possibility) ≠ "must wait for second pass" (necessity). The former is true for almost everything; the latter isolates a small, meaningful set (FF2). The reframe is the crux.
- KI3 — There are TWO independent sources a post-draft check-agenda can be derived from: **config-derived** (keyed to A1-A8: e.g., A1=conversational → check too-hard words) and **config-independent** (structural checks that must happen regardless of config: did I drop a clause? did I merge sentences?). The prior inquiry's agenda is primarily config-derived; firing-time's "must-wait" set is the config-independent complement.

**Structural Points:**
- SP1 — The real pipeline has ≥3 moments (comprehend the source → generate the draft → check the draft), matching the 3-Pass's 3 passes; a 2-category tag mismatches both (DF3).
- SP2 — The prior inquiry `2026-07-10_23-03`'s design already contains a **"mechanical omission-diff spine first"** — a config-independent, must-happen-post-draft check. Firing-time's "must-wait set" overlaps this spine heavily.

**Foundational Principles:**
- FP1 — Mechanical > judgment for checks (from the priors): a check that can be run as a near-mechanical diff (config-independent) is more reliable than one requiring the model to re-judge its own fluent output.
- FP2 — The SKILL is declarative-rich/procedurally-thin; the recurring fix-shape is "turn an in-context principle into an executed step / a machine-usable artifact."

**Meaning-Nodes:**
- MN1 — "firing time" = when in the pipeline a principle can act.
- MN2 — "the check-spine" = the small set of config-independent structural checks that must run against the finished draft.
- MN3 — "selection criterion" = a rule for deciding which principles belong in the check-spine.

### SV2 — Anchor-Informed Understanding
The proposal is no longer "tag everything with 2 categories." It is now framed by the tension between KI1/KI2 (a tag is only useful if it isolates a small set, which requires the necessity reframe) and C4/SP2 (the priors already contain a config-independent mechanical spine that firing-time's must-wait set would largely reproduce). The live question sharpens: **does firing-time add anything to the priors, or does it reproduce their spine?**

*(Meta-inspection H4/H5: the concept names "must-wait" vs "can-fire" (H4) are load-bearing and tested in Phase 3; the motivating examples "allegorical"/"work-vs-foothold" (H5) are FIRST-pass-fixable cases — they show generation-time firing, not the second-pass set, so they don't by themselves motivate a second-pass tag. Flagged for Phase 3.)*

---

## Phase 2 — Perspective Checking

- **Technical/Logical:** A per-principle enum over ~80+ principles is a large annotation surface (C3). A binary that lands "both" for most (C2) has low information content. The information concentrates in the minority tail (the must-wait set). Technically, the efficient encoding is not a per-principle tag but a **membership list** of the small must-wait set.
- **Human/User:** The user's underlying want (from the WHY-axis) is *operationalize the two gates / prevent recurrence at generation*. What actually serves that: knowing, at Pass-1, what to hold (mostly the config + the comprehension analysis), and having a small reliable Pass-3 checklist. The user framed it as "tag principles"; the served need is "a small reliable check-spine + a clear first-pass hold-set."
- **Strategic/Long-term:** A standing "declare firing-phase for every new principle" discipline (design-hygiene) has long-term value ONLY if the declaration is cheap and used. If most declarations are "both," the discipline becomes ritual. The durable version is narrower: "when adding a principle, ask *must this wait for the draft?* — if yes, add it to the check-spine."
- **Risk/Failure:** The failure mode of adopting the full scheme is metadata-theater — 80 tags nobody consults, most saying "both." The failure mode of rejecting it entirely is losing the genuine insight (the config-independent must-wait checks are a real gap in a purely config-derived agenda).
- **Resource/Feasibility:** The lean version (isolate the must-wait set, ~5-15 items) is cheap and immediately usable as the Pass-3 spine. The heavy version (tag all principles across 3 phases) is expensive and mostly redundant with Tier + config.
- **Definitional/Internal-Consistency:** Does "firing-time tagging" contradict the priors? No — it's consistent with and extends them. But it PARTIALLY reduces to them (SP2). The honest internal-consistency check: firing-time is not a NEW mechanism; it's a **selection criterion** that populates the priors' already-existing mechanical spine.
- **Phase/Calibration-State (required — the scheme is phase-dependent):** firing-time tags are only operational IF the 3-Pass is actually wired (prior `2026-07-11_00-24`'s fix, currently UN-applied pending user reach-authorization). Absent that wiring, the tags have nowhere to fire. So the proposal is **downstream of / gated on** the prior fix — it is the prior fix's metadata layer, not a standalone capability.

### SV3 — Multi-Perspective Understanding
The perspectives converge hard on a reframe: the useful object is **not a per-principle firing-time tag** but a **small config-independent check-spine, selected by the criterion "must this principle wait for the finished draft to be verified?"** — which extends (does not replace) the prior inquiries' config-derived agenda + their existing omission-diff spine. The user's instinct (firing-time matters) is affirmed; the deliverable is re-shaped from "tagging scheme" to "selection criterion + the small spine it selects."

*(Meta-inspection H1 — candidate-set convergence: "firing-time tagging" and "the prior's mechanical spine" are close to the SAME thing. This is the redundancy rival; resolved in Phase 3. H2 — frame scope: the config-independent vs config-derived boundary is the load-bearing frame.)*

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — Fork 1: is the tag inert-metadata or operational-driver, and does it earn its keep?
**Strongest counter-interpretation (the REDUNDANCY rival):** firing-time tagging is just the 3-Pass wiring + the prior's mechanical omission-diff spine re-described as metadata; it adds nothing. The 3-Pass already sequences generate-then-check by position; the prior already has a config-independent mechanical spine.
**Why the counter fails (structural grounds):** it fails *partially but not wholly*. The prior's spine was instantiated as ONE item ("mechanical omission-diff first") with no stated criterion for what else belongs in it. Firing-time supplies the **general selection criterion** — "must-wait-for-second-pass = cannot be reliably verified without the finished draft" — which *generalizes* the single omission-diff into a principled SET (omission-diff + no-add + no-merge/split + whole-draft structural checks like "is the escalation/ring-composition/havuz-convergence intact?"). That criterion is not in the priors; it answers a question the priors left implicit ("what belongs in the mechanical spine?"). So the tag is **operational, not inert**, but its surviving contribution is narrow and specific: **a selection criterion that populates the prior inquiries' check-spine.**
**Confidence:** HIGH — the config-independent whole-draft structural checks (e.g., "did the reconstruction preserve the escalation pattern?") are genuinely NOT derivable from A1-A8 config values, so a purely config-derived agenda misses them; the must-wait criterion catches them. This is a structural gap, not a precedent citation.
**Resolution:** Fork 1 = **OPERATIONAL, contribution = a selection criterion for the check-spine (config-independent must-wait items), extending the priors — not a standalone full-corpus tagging scheme.**
**What is now fixed:** the tag's value = isolating the config-independent must-wait set. **No longer allowed:** treating firing-time as inert documentation, or as a corpus-wide per-principle scheme justified on its own. **Now depends on this:** Fork 2's form; the relationship-to-priors (REFINES+EXTENDS).
**Model change:** the deliverable shifts from "a tagging scheme" to "a selection criterion + the small spine it yields, plugged into the prior 3-Pass's Pass-3."

### Ambiguity 2 — Fork 2: the right FORM
**Strongest counter-interpretation (the OVER-ENGINEERING rival):** a 3-phase (comprehend/generate/check) per-principle tag over the whole corpus is the "complete" scheme, so build it. / Or the opposite over-simplification: a clean 2-way partition is fine.
**Why both fail (structural grounds):** the full 3-phase per-principle tagging over-formalizes (C3 metadata cost; most tags would be "comprehend+both" and go unconsulted) — it fails the resource/risk perspectives. The clean 2-way partition fails C2 (dual-majority → non-discriminating) and DF3 (omits comprehension). What survives both counters is the **lean, necessity-framed, scoped** form: (i) SCOPE to the substantive principles + hard constraints, excluding config policies (trivially dual, low-stakes) and meta-principles (about the process, FF4); (ii) frame as **must-wait-for-second-pass** (necessity) not can-fire (possibility); (iii) the actionable output is the **membership of the small check-spine**, not a tag on every principle; (iv) acknowledge the 3 phases *conceptually* (comprehend/generate/check) — relevant to the prior inquiry's config-blind-Pass-1 comprehension question — but do NOT build heavy per-principle 3-phase tags.
**Confidence:** HIGH — the lean form is forced by the convergence of technical (efficient encoding = membership list), resource (cheap), and risk (avoids metadata-theater) perspectives against the heavy form, and by C2 against the 2-way partition.
**Resolution:** Fork 2 = **a scoped, necessity-framed selection criterion whose actionable output is the small config-independent check-spine; 3 phases acknowledged conceptually, not tagged exhaustively.**
**What is now fixed:** the form is a criterion + a membership list, scoped + necessity-framed. **No longer allowed:** a clean 2-way partition; a full-corpus 3-phase per-principle tagging. **Now depends on this:** the annotation/edit reach (what gets written); the design-discipline (the standing "must-this-wait?" question for new principles).

### Ambiguity 3 — the DEEP rival: does firing-time DISSOLVE into the prior fix?
**Strongest counter-interpretation:** the user's real insight is just "the check-agenda should be small and derived," which IS the prior inquiry's config-keyed scoped verification pass — so firing-time adds nothing new; it's the prior fix wearing a new name.
**Why the counter fails (structural grounds):** the prior's agenda is **config-derived** (its items are keyed to the chosen A1-A8 values). Firing-time's contribution is precisely the **config-INDEPENDENT** axis — checks that must run *whatever* the config is (structural fidelity: omission, no-merge/split, escalation/ring/havuz preservation). A config-keyed agenda, by construction, does not emit a check that no config value keys to. So firing-time does NOT fully dissolve — it adds the orthogonal config-independent spine and the criterion that defines it. It **partially** overlaps (the omission-diff was already there) but contributes the generalization + the config-independent structural checks.
**Confidence:** HIGH (structural: config-keying cannot generate config-independent checks).
**Resolution:** firing-time **SURVIVES** as a distinct-but-modest contribution: the config-independent must-wait check-spine + its selection criterion, orthogonal to the prior's config-derived agenda. It does not dissolve; nor is it a grand new scheme.

### Load-bearing concept test (H4 concept names + H5 motivating examples)
- **"must-wait-for-second-pass" (H4):** tested — is it a real structural distinction or an incidental label? Real: it names "cannot be reliably verified without the finished draft," which is a genuine property (omission can only be diffed against a complete draft; you cannot check "did I drop a clause" mid-generation). HIGH.
- **"selection criterion for the spine" (H4):** tested — does firing-time reduce to just this, or is it more? It reduces to exactly this (Ambiguity 1). Naming it honestly prevents over-claiming a full tagging scheme. HIGH.
- **The motivating examples "allegorical" / "work-vs-foothold" (H5):** these are the user's cited cases — but they are **first-pass-FIXABLE** (hold A1=conversational / the sense-disambiguation policy while writing → right the first time). They motivate the **generation-time hold-set**, NOT the second-pass check-spine. So the user's own examples are examples of the *first-pass* category, which is the *config-derived / comprehension* side — reinforcing that the genuinely-novel contribution (the config-independent must-wait spine) is a DIFFERENT set than the examples that sparked the idea. This is the specific-vs-pattern catch: the examples are first-pass cases; generalizing them to "we need firing-time categories" actually points more at the first-pass hold-set (≈ the prior's config-blind Pass-1 + config-derived checks) than at a new second-pass scheme.

### SV4 — Clarified Understanding
Firing-time survives, modestly and precisely: as a **selection criterion** ("must this wait for the finished draft?") that yields a **small, config-independent check-spine**, extending the prior inquiries' config-derived Pass-3 agenda and generalizing their single omission-diff. The user's clean-2-category-over-everything form is set aside (dual-majority + metadata cost + comprehension-phase). The user's own motivating examples turn out to be first-pass cases, so the biggest practical payoff is on the first-pass/comprehension side (already largely the priors'), while firing-time's *novel* payoff is the config-independent second-pass spine.

---

## Phase 4 — Degrees-of-Freedom Reduction

**Fixed:** (i) the deliverable = a selection criterion + the small config-independent check-spine it selects (+ conceptual 3-phase clarification), NOT a corpus-wide tagging scheme; (ii) scope = substantive principles + hard constraints, excluding config policies + meta-principles; (iii) framing = necessity (must-wait) not possibility (can-fire); (iv) relationship = REFINES+EXTENDS the two priors, gated on the prior 3-Pass wiring being applied.
**Eliminated:** the clean 2-way partition; the heavy per-principle 3-phase tagging; the claim that firing-time is a standalone new capability; the claim that it's fully redundant.
**Viable paths remaining (for Innovation/Critique):** (a) exactly how to express the criterion + spine (a short list in harmony_layer.md's Pass-3? a `must_verify_post_draft` flag on the few hard constraints?); (b) whether to also lightly mark the comprehension-phase principles (the ~80 detection ones) as "comprehension-time" to serve the prior's config-blind-Pass-1 question, or leave that out as scope-creep; (c) whether the standing design-discipline ("ask must-this-wait for new principles") is worth stating.

### SV5 — Constrained Understanding
The problem is now: *specify the config-independent must-wait check-spine (the criterion + its membership) as an extension of the prior inquiries' Pass-3 agenda, scoped and necessity-framed, gated on the 3-Pass wiring.* The grand tagging scheme is off the table; the modest, real contribution is what remains.

---

## Phase 5 — Conceptual Stabilization

**Accommodation check (H6):** the model did not require repeated patching — it settled once the "possibility→necessity" reframe (KI2) and the "config-derived vs config-independent" split (KI3) were in place. Two reframes, then stable. No model-misfit.

### SV6 — Stabilized Model

**The errors-are-possible question is not this inquiry's; this inquiry's question is "is firing-time categorization useful, and in what form?" The stabilized answer:**

1. **The user's instinct is affirmed but its scope is much smaller than first framed.** "When can a principle fire" is a real property, and a *subset* of it is genuinely useful. But it is NOT a clean 2-category tag applied to "our principles/policies" as a homogeneous list — that form fails on three structural grounds: the corpus is heterogeneous (≥4 kinds), dual is the majority (a possibility-partition is non-discriminating), and a comprehension phase is unaccounted (the pipeline has 3 moments, not 2).

2. **The single reframe that rescues the idea: possibility → necessity.** Tag not "*can* this fire at second pass" (true for almost everything → useless) but "*must* this wait for the finished draft" (true for few → useful). This isolates a small set.

3. **What that small set IS: the config-independent check-spine.** The must-wait items are the structural checks that must run against the finished draft regardless of config — omission-diff, no-add, no-merge/split, and whole-draft structural-fidelity checks (was the escalation / ring-composition / havuz-convergence preserved?). These are *orthogonal* to the prior inquiries' **config-derived** agenda (too-hard-word / word-sense / naturalness, keyed to A1-A8).

4. **Firing-time's surviving contribution, precisely stated:** it is a **selection criterion** ("must this wait for the finished draft to be verified?") that (a) *generalizes* the prior inquiry `2026-07-10_23-03`'s single "mechanical omission-diff spine" into a principled config-independent set, and (b) *complements* that inquiry's config-derived checks. It does **not** dissolve into the priors (config-keying can't emit config-independent checks) and it is **not** a standalone new mechanism (it plugs into the prior `2026-07-11_00-24`'s Pass-3 gate and is gated on that wiring being applied).

5. **Scope and cost:** apply the criterion to the substantive principles + hard constraints only; exclude config policies (trivially dual, low-stakes) and meta-principles (about the process). Do NOT build a per-principle 3-phase tag over the whole corpus — that is metadata-theater (most tags would say "both"/"comprehend+both" and go unconsulted). Acknowledge the 3 phases *conceptually* (it corrects the user's 2-category framing and connects to the prior's config-blind-Pass-1 comprehension question), but the *actionable* object is the small must-wait membership list.

6. **A notable twist (specific-vs-pattern):** the user's own motivating examples ("allegorical", "work"-vs-"foothold") are *first-pass-fixable* — they argue for the generation-time hold-set (≈ the prior's config-blind Pass-1 + config-derived checks), not for a new second-pass scheme. So the idea that *sparked* "firing-time categories" actually points mostly at work the priors already do; firing-time's *own novel* yield is the config-independent second-pass spine (a smaller prize than the framing suggested, but real).

**Relationship to priors:** REFINES the dual-shaped-principles claim (confirms dual is the majority — which is *why* possibility-tagging fails and necessity-tagging works) and EXTENDS the Pass-3 check-agenda (adds the config-independent spine + its criterion). Not a supersede; both priors stand.

**Difference from SV1:** SV1 saw an appealing clean 2-category formalization of the two gates. SV6 sees that the clean form fails structurally, that most of the apparent value is already in the priors, and that firing-time's genuine surviving contribution is narrow and precise — a necessity-framed selection criterion that populates a small config-independent check-spine.

**Rivals disposition:** REDUNDANCY rival — partially lands (much overlaps the priors) but firing-time survives via the generalization + config-independent axis. OVER-ENGINEERING rival — lands against the heavy full-corpus 3-phase tagging (rejected), not against the lean spine. DEEP rival — firing-time does NOT fully dissolve (config-independent ≠ config-derived), but its independent contribution is modest.

**Open for Decomposition/Innovation/Critique:** the exact expression of the criterion + spine; whether to lightly mark comprehension-time principles; whether the standing design-discipline is worth stating; and the honest cost/benefit verdict (is even the lean spine worth adding, given the prior's omission-diff already covers the biggest must-wait item?).
