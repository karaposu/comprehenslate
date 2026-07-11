---
status: active
model: claude-opus-4-8[1m]
effort: max
refines:
  - devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md
  - devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md
---
# Finding: Firing-Time Categories for Principles

## Changes from Prior

**Prior paths:**
- `devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md` — the first diagnosis of a batch of translation errors (relationship: **REFINES**).
- `devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md` — the refinement that located the root cause in an un-run method (relationship: **EXTENDS**).

**Revision trigger:** A new user proposal — tag the translation SKILL's principles with *when they can fire* (`fireable_at_first_pass` / `fireable_at_second_pass` / both).

**What's preserved:** Both priors stand. This finding does not overturn either; it adds a metadata layer on top of the second one's fix and generalizes a piece of the first one's fix.

**What's changed:** The first prior called the failed principles "dual-shaped" (able to fire while writing *or* at a later check). This finding confirms that and *sharpens* it: dual-fireable is not a special property of a few principles — it is the **majority** of the corpus, and that fact is exactly why the user's clean two-category tagging scheme cannot work as proposed.

**What's new:** A single, small, defensible contribution — a **config-independent check-spine**: the short set of post-draft checks that must run on every translation regardless of its settings. It is described below.

**Migration:** No SKILL files were edited. The evaluation and the design are delivered; the decision to build or apply anything is left to the user (see Next Actions).

---

## Question

The project is **comprehenslate**, a general-purpose AI translation SKILL (a structured instruction set that tells the model how to translate), calibrated on a difficult Ottoman-Turkish source text. Two earlier investigations diagnosed why a batch of translation errors slipped through, and proposed a fix built around three passes — lock the meaning, map the stylistic harmony, then reconstruct in the target language.

Building on that, the user proposed a new idea: **tag the SKILL's principles and policies with *when they can fire*** — `fireable_at_first_pass` (can be applied while writing the translation), `fireable_at_second_pass` (needs a finished draft to check against), or possibly both. The question: **is this categorization useful, and if so, what is the right scheme?** The goal was an honest evaluation plus, if the idea survived, a concrete design — with the depth of the deliverable (evaluate-only vs. design vs. apply) gated for the user to choose.

## Finding Summary

- **The instinct is right; the clean form is wrong.** Tagging by firing-time is pointing at something real, but the specific proposal — sort every principle into `first_pass` / `second_pass` / `both` — fails, for three structural reasons found by looking at the actual corpus.

- **Reason 1 — the corpus is not one kind of thing.** The SKILL's "principles/policies" are at least four different kinds (stylistic-harmony rules, ~80 source-analysis detection principles, reader-configuration policies, and methodology meta-rules). A single firing-time tag means different things for each.

- **Reason 2 — "both" is the majority, so the tag barely discriminates.** Most principles *can* be applied while writing *and* checked afterward. A category that catches almost everything sorts almost nothing.

- **Reason 3 — a whole phase is missing.** The largest block of principles fires while *reading the source* (comprehension), which is neither "writing" nor "checking." The real pipeline has three moments, not two.

- **The one move that rescues the idea:** stop tagging what *can* fire late (nearly everything) and instead isolate what **must wait for the finished draft** (few). That small "must-wait" set is the useful output.

- **What that must-wait set actually is:** the **config-independent checks** — the handful of fidelity checks that must run on *every* translation no matter what its reader-settings are (did any source content get dropped? was anything invented? were sentence boundaries preserved? does the source's large-scale structure survive?). These are distinct from the **config-derived** checks (is this word too hard *for this reader*? is the register right? is it natural?) that the first prior already handled.

- **The honest size of the contribution is small.** Most of the must-wait set already exists in the two priors or in the SKILL's existing rules. What is genuinely new is the **organizing idea** — noticing that these scattered checks form one principled family (the "always-run" checks) and giving it a membership rule — not a pile of new machinery.

- **The reframe underneath it:** the truly useful axis is not "firing-time" but **config-dependence** (does this check's pass/fail depend on the reader settings, or not?). Firing-time still does one necessary job — it tells you a check belongs *after* the draft rather than *during* writing — but config-dependence is what carries the value.

- **Relationship to the priors:** this **REFINES** the first prior's "dual-shaped principles" claim (dual is the majority) and **EXTENDS** the second prior's post-draft check step (it supplies that step's always-run content). It does not replace either, and it is **inert until** the second prior's three-pass fix is actually built.

## Finding

### Why this question came up

The second prior investigation ended with a fix: the SKILL should stop collapsing "understand the meaning" and "make it read well" into one fluent motion, and instead run three explicit passes — **Pass 1** locks the meaning, **Pass 2** maps the stylistic harmony to preserve, **Pass 3** reconstructs the text in the target language and checks it. (This lives in the SKILL's `references/core/harmony_layer.md` file; "Pass 3" is where a finished draft gets verified.) The first prior had earlier established that the errors happened because the translation was written in one fluency-first pass with no post-draft check to catch what slipped.

Along the way, the first prior corrected its own language: it had called the failed principles "verification-shaped" (as if they could *only* work as after-the-fact checks), then softened that to "dual-shaped" — a principle like "pick a word the reader can handle" or "pick the right sense of an ambiguous word" could equally well fire *while writing* (get it right the first time) or *at a check* (catch it afterward). That softening is what sparked the user's new idea: if principles are dual-natured about *when* they fire, why not tag them with that timing explicitly and use the tags to drive the two gates (the write-time gate and the check-time gate)?

### What the actual corpus shows

The proposal assumes "our principles or policies" is one homogeneous list you can cleanly sort. Reading the real files shows it is not. It is at least four different kinds of thing:

1. **Stylistic-harmony components** — the rules in `harmony_layer.md` about preserving rhythm, word-order emphasis, and structural echoes, organized by how strongly each must be preserved.
2. **Source-analysis detection principles** — roughly eighty "On X" entries (in `translation_principals.md` and `notes.md`) that tell the model what to *notice* while reading the source (an escalating argument, a structural echo, a word that triggers an entailment chain).
3. **Reader-configuration policies** — the settings-driven rules (in `schemas.py`) keyed to the eight reader axes the SKILL calls A1–A8 (reader level, register, and so on).
4. **Methodology meta-rules** — rules *about the process* itself ("comprehend first, then validate"; the always-on "no-smoothing" rule that forbids quietly ironing out the source's difficulty).

A single firing-time tag lands differently on each kind, which is the first sign the clean scheme is mis-shaped. Two more signs follow.

**"Both" is the majority.** Walk through the corpus and ask "can this fire while writing, and also be checked afterward?" For most harmony components and most detection principles the answer is yes. A sorting scheme whose largest bin is "both" is a weak discriminator — it does not actually separate the corpus into useful groups.

**A phase is missing.** The single largest block — the ~80 detection principles — does not fire while *writing* or while *checking*. It fires while **reading the source**, before any target text exists. That is a third moment: **comprehend → generate → check**. The proposal's two tags cannot name it, and (tellingly) the second prior's own fix has *three* passes, not two. So the two-category scheme mismatches both the real cognitive pipeline and the fix it was meant to serve.

### The move that rescues the idea

The failure above has a precise cause: the tag was framed as a **possibility** ("*can* this fire at second pass?"), and possibility is cheap — almost everything *can* be checked late. Flip it to a **necessity**: "*must* this wait for the finished draft to be verified reliably?" Necessity is rare. Most principles do *not* have to wait — they are better handled while writing. Only a few genuinely cannot be confirmed until the whole draft exists.

That small "must-wait" set is the entire useful yield of the firing-time idea. And when you list its members, they turn out to share a second, more important property.

### What the must-wait set actually is: the config-independent spine

The must-wait checks are precisely the ones whose correctness **does not depend on the reader settings (A1–A8)**:

- **Omission check** — did any source clause get dropped? (You can only tell against the finished draft.)
- **No-addition check** — was anything invented that the source did not say?
- **No-merge / no-split check** — were the source's sentence boundaries preserved? (`harmony_layer.md` explicitly forbids splitting one sentence into two — sentence boundaries carry structural meaning.)
- **Whole-draft structural-fidelity checks** — does the source's large-scale shape survive? An escalating argument that builds from small to large; a structural echo that opens and closes a passage; multiple threads that converge to one point; a cause-and-effect order.

None of these changes with the reader. You never drop a source clause "because the reader is casual"; fidelity is owed regardless of settings. Contrast the checks the first prior already identified — "is this word too hard *for this reader*?", "is the register right?", "is it natural?" — every one of those is **keyed to the settings**. So there are two clean groups:

- a **config-independent spine** — always run, identical for every translation; and
- a **config-derived agenda** — run the subset the current settings select.

The practical shape of the design is a **two-part Pass-3 check-list**: the always-run spine on one side, the settings-selected agenda (the first prior's contribution) on the other. The spine plugs into the *same* Pass-3 gate the second prior designed.

### The critique's three corrections (what makes this honest rather than tidy)

An adversarial pass caught three places where the clean picture overstated itself. All three are folded into the design above.

**1. The spine has a reliable core and a soft rim.** The members are not equally trustworthy. The omission / no-addition / no-boundary-change checks are **mechanically checkable** — you can enumerate source clauses and verify presence, almost like a diff. The whole-draft structural checks (does the escalation survive? did the echo close?) are **judgment calls**, and a judgment call run by the same model that just wrote a fluency-first draft is vulnerable to rubber-stamping ("looks preserved to me"). So the genuinely dependable core is the intersection of *three* properties — must-wait **and** config-independent **and** mechanically-checkable — and the structural checks sit as a softer, rubber-stamp-prone rim that should be labeled as such and ordered after the core.

**2. The novel content is nearly zero.** The omission check already exists as the first prior's "mechanical omission-diff." The no-addition and no-boundary-change checks already exist as hard constraints in `harmony_layer.md`. The structural properties already exist in the detection principles. So the spine invents almost no new checks. What it adds is the **organizing idea** — that these scattered items form one always-run family, with a membership rule that keeps the family small and stable as the corpus grows. That is a real contribution, but a modest one: an organizing generalization, not new machinery.

**3. One member was mis-filed, which proves the axis is real.** The design initially put "did I pick the right *sense* of an ambiguous word?" in the config-derived (settings-dependent) column. But by the project's own principle, the correct sense of a polysemous word is fixed by the *local source construction* (the grammar around it), not by the reader level — so sense-correctness is actually **config-independent**. The fact that applying the criterion carefully re-sorts a member is not a bug; it shows the config-dependence axis is doing genuine work rather than rubber-stamping an intuition.

### The reframe worth stating plainly

The user's entry point was "firing-time." The investigation found that the *value* does not sit on the firing-time axis — it sits on the **config-dependence** axis (does this check depend on the reader settings or not?). Firing-time and config-dependence are two different, independent questions, and the spine is the cell where both answers line up: must-wait **and** config-independent.

This raises the fair challenge: if config-dependence carries all the value, is "firing-time" just scaffolding we should discard? No — but its role is smaller than the original proposal implied. Firing-time still does one job nothing else does: it tells you a check belongs **after** the draft (in Pass 3) rather than as a hold you keep **while** writing (in Pass 1). A config-independent principle is not automatically a check — "preserve the escalation" could be something you hold in mind *while* writing. It is the *combination* — config-independent and must-wait — that lands a member in the spine. Firing-time supplies the "must-wait" coordinate; it places the check in time. Config-dependence supplies the discrimination and the novelty. Both are needed; only one is the source of the value.

### The honest bottom line

Firing-time categorization **survives — as a small organizing generalization**, not as the corpus-wide tagging scheme proposed. Tagging every principle with a firing-time label is rejected (it would be metadata for its own sake — heavy to maintain, and mostly landing in the useless "both" bin). What survives is the necessity reframe and the config-independent spine it isolates. And a caveat the user should hear clearly: the user's own motivating examples ("allegorical" should have been "parable"; "work" should have been "foothold") are **first-pass-fixable** — a properly comprehending write would have gotten them right — so they argue for the second prior's write-time meaning-lock more than for any new check. The spine's clean wins are the mechanical fidelity checks, which is a smaller prize than the original framing suggested, but a real one.

## Inherited Commitments Re-test

This finding synthesizes two prior findings, so each load-bearing commitment they carry is re-tested here rather than silently absorbed.

**Commitment 1 — principles are "dual-shaped" (can fire at generation OR at a check).**
- **Source:** `devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md` (the critique-corrected framing).
- **Re-test status: RE-TESTED — commitment confirmed but frame revised.** Dual-shaped is correct, but the frame shifts: dual is not a property of a few principles, it is the **majority** of the corpus. That is load-bearing here in a way the prior did not need — it is the specific reason the user's clean two-category tag fails (a partition whose largest bin is "both" does not discriminate).
- **Evidence:** the corpus walk in this inquiry's surfacing pass — most harmony components and most detection principles are appl-while-writing *and* checkable-after.

**Commitment 2 — the post-draft check should be config-keyed and small, with a mechanical omission-diff as its spine.**
- **Source:** `2026-07-10_23-03/finding.md` (the scoped-verification-pass design).
- **Re-test status: RE-TESTED — commitment confirmed.** It holds unchanged, and this finding builds on it: the mechanical omission-diff is exactly the flagship member of the config-independent spine. Firing-time's contribution is to *generalize* that single check into the principled always-run family.
- **Evidence:** the spine's core (omission / no-add / no-boundary-change) is the omission-diff plus its natural siblings, all config-independent and mechanically checkable.

**Commitment 3 — the fix is two gates hosted by one three-pass method (write-time meaning-lock + post-draft check).**
- **Source:** `devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md` (the three-pass "Meaning-Lock" design).
- **Re-test status: RE-TESTED — commitment confirmed.** The two gates map onto write-time (Pass 1) and check-time (Pass 3). This finding populates the check-time gate: the config-independent spine is the content of Pass 3's always-run column. The whole design is **gated on this three-pass fix being built** — without it, the spine has nowhere to fire.
- **Evidence:** the spine is defined as a Pass-3 check-list; its actionability is explicitly contingent on the second prior's fix being applied first (a double gate — see Next Actions).

**Commitment 4 — the post-draft check stays word/clause-granular, while the locked-meaning foundation is sentence-granular.**
- **Source:** `2026-07-11_00-24/finding.md` (the critique-corrected granularity caveat).
- **Re-test status: RE-TESTED — commitment confirmed but frame revised.** The word/clause-granular claim was about the omission-diff specifically, and it holds for that check. But the spine adds a *third* granularity: the whole-draft structural checks (escalation, echo, convergence) operate across the entire text, not at word/clause level. This is a compatible extension, not a contradiction — different check-types legitimately work at different granularities (word/clause for omission, whole-draft for structure).
- **Evidence:** the structural-fidelity members of the spine are relational across the full draft; they cannot be evaluated at clause granularity, and the prior never claimed they should be.

## Next Actions

### MUST

- **What:** Decide how far this deliverable should travel — (a) evaluate-only [already delivered]; (b) also produce the finalized, critique-corrected spine specification; or (c) also apply the SKILL edit that wires the spine into Pass 3.
  - **Who:** the user.
  - **Gate:** before any build/apply work begins (condition-bound).
  - **Why:** the evaluation (is firing-time useful, and in what form) is complete and stands on its own. The design and apply reaches need authorization — and the apply reach is **doubly gated**: it is inert until the second prior's three-pass fix is itself applied, because the spine is a metadata layer on a gate that does not yet exist in the SKILL.

### COULD

- **What:** Produce the finalized corrected spine spec — the three-property core (must-wait ∧ config-independent ∧ mechanically-checkable: omission / no-add / no-boundary-change), the soft structural rim (escalation / echo / convergence / cause-effect, labeled rubber-stamp-prone and ordered after the core), the two-part membership criterion plus the type-gate that excludes meta-rules, and the re-sorted membership (sense-correctness moved to the config-independent side).
  - **Who:** a design pass (a `/innovate`-style or direct authoring step).
  - **Gate:** observable — once the reach decision selects (b) or (c).
  - **Why:** turns the evaluation into a ready-to-apply artifact.
  - **Depends-on:** MUST item "decide the reach." This COULD is GATED — do not act until the MUST resolves.

- **What:** Validate the spine against real data — re-check the original error-laden translation chunk to see whether the mechanical core catches the omission/addition errors and whether the soft rim actually catches (or misses) the structural ones.
  - **Who:** a test pass.
  - **Gate:** observable — after the spec exists.
  - **Why:** the mechanical-vs-judgment reliability gradient is a critique claim, not yet evidenced; this would confirm or correct it.
  - **Depends-on:** MUST item "decide the reach." GATED.

- **What:** Add forward/back cross-references — note in the second prior that its Pass-3 gate now has a proposed always-run spine (relationship EXTENDS), and note in the first prior that its single omission-diff is now generalized into a config-independent family (relationship REFINES).
  - **Who:** a light edit pass on the two prior findings.
  - **Gate:** condition-bound — whenever the prior-chain is next touched.
  - **Why:** keeps the diagnosis→fix lineage coherent so the spine is not orphaned from the gate it populates.

### DEFERRED

- **What:** Develop "mechanically-checkable" into a general check-reliability taxonomy (mechanical vs. judgment checks, and what makes a check rubber-stamp-resistant).
  - **Gate:** revival — after the spine spec exists and has one validated instance (i.e., after the validate-against-real-data COULD runs).
  - **Why (if revived):** a reusable check-design principle beyond translation.

- **What:** Investigate hardening the soft structural rim — extract the source's structural skeleton *before* drafting, then diff the draft's skeleton against it, converting a judgment check into a more-mechanical one.
  - **Gate:** revival — only if validation shows the rim is in fact unreliable.
  - **Why (if revived):** lifts the weakest part of the spine toward the core's reliability.

## Reasoning

**Why "survives modestly" and not "adopt the tagging scheme":** three independent structural findings (heterogeneous corpus; "both" is the majority; a missing comprehension phase) each independently sink the clean two-category tag. They were not manufactured to agree — they come from three different observations about the same corpus.

**Why "survives modestly" and not "dissolves entirely into the priors":** a redundancy challenge was run hard — is firing-time tagging just the two-gate fix re-described? It partly lands: the omission-diff, the hard constraints, and the structural properties all pre-exist. But it does not fully land, because the **config-independent axis** and the **generalization** (one lone check → a named, closed family with a membership rule) are in neither prior. That residue is the surviving contribution.

**Why REFINES+EXTENDS and not SUPERSEDE:** supersede was considered and rejected. The priors' contributions are intact and larger — the second prior's three-pass architecture and the first prior's config-derived agenda are untouched; the spine only furnishes content into a gate they already built. Overturning nothing, it refines one claim and extends one step.

**What was rejected outright (the dead region):** corpus-wide per-principle firing-time tagging — attaching a `first_pass`/`second_pass`/`both` label to all ~80 principles. Killed as metadata for its own sake: heavy to maintain, and since "both" is the majority, it produces a check-list nearly as large as the whole corpus, defeating the entire point of isolating a small must-wait agenda.

**Where the design was corrected rather than accepted as first drawn:** the clean "two orthogonal columns, spine = the intersection cell" picture was too tidy. The critique added a third property (mechanical-checkability) that splits the spine into a reliable core and a rubber-stamp-prone rim; caught a mis-filed member (sense-correctness); and pushed the "small prize" estimate down to "near-zero new content, the value is the organizing idea." All three corrections are in the finding above — the design is stronger for surviving them.

## Open Questions

### Research Frontiers
- Whether the judgment-laden structural checks (the soft rim) can be made reliably rubber-stamp-resistant by extracting the source's structure before drafting and diffing after — no known method yet; requires investigation.
- Whether "mechanically-checkable" generalizes into a reusable cross-domain taxonomy of check reliability.

### Blocked
- The whole design cannot be *applied* until the second prior's three-pass fix (`2026-07-11_00-24`) is built into the SKILL. The spine is a metadata layer on a gate that does not yet exist.

### Refinement Triggers
- If validation against the real error-laden translation shows the mechanical core *misses* omission/addition errors (i.e., the same model rubber-stamps even the mechanical checks), the "mechanically-checkable = reliable" claim re-opens — re-open on that specific observation, not on generic change.
- If the corpus later gains a new whole-draft structural principle, the spine's membership re-opens for re-curation under the two-part criterion.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
But the critique caught this framing being too clean, and the correction matters. Calling the failed principles "verification-shaped" (checking-only by nature) overstates it. Take "allegorical": a first pass properly holding A1=conversational (the reader-level axis that literally excludes dense-academic vocabulary) in mind could have picked "parable" or "comparison" while writing — no separate check needed. Same for "work" vs "foothold": if the sense-disambiguation policy had fired during writing, the right word comes out the first time. So these principles are dual-natured — able to fire while writing or at a check. The honest statement is: in a single fluency-first pass they went un-fired at generation, and there was no checkpoint to catch them afterward. The practical conclusion (add a checkpoint) is unchanged; only the mechanism-claim is softened.

and this made me thing that it would be really useful to use these 2 categories fireable_at_first_pass and fireable_at_second_pass for our principles or policies (not sure maybe both )
```

</details>
