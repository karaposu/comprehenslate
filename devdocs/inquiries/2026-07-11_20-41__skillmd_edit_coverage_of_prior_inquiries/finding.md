---
status: active
model: claude-opus-4-8[1m]
effort: max
---
# Finding: Does the edited SKILL.md cover the prior inquiries' missing points — and is it better or worse?

## Question

The user recently hand-edited `SKILL/SKILL.md` — the top-level workflow file of **comprehenslate**, a configurable AI-translation skill. They asked: does the edited file **cover the "missing points" from the last inquiries**, and is it **better or worse**?

"The last inquiries" is a chain of six diagnostic findings (all under `devdocs/inquiries/`) about why the translation skill was producing errors and how to fix it:
- **`2026-07-10_23-03`** — the original diagnosis: errors came from a single forward-generating pass with no checkpoint (a "7-error / one-pass / no-checkpoint" pattern).
- **`2026-07-11_00-24`** — the root cause: the skill's own **3-Pass translation method** (Pass 1 *Meaning Lock* → Pass 2 *Harmony Map* → Pass 3 *Target Reconstruction*), which lives in the reference file `harmony_layer.md`, is **read but never actually run** by the workflow. The fix: rewire the translate step into those three ordered passes, with the Meaning-Lock pass running **first and config-blind** (without the reader-style settings in view, so style can't contaminate comprehension).
- **`2026-07-11_01-09`** — a config-independent **post-draft verification pass** (re-read the finished draft: was content dropped? invented? were sentence boundaries kept? did the large-scale structure survive?).
- **`2026-07-11_04-12`** — the **enforcement gradient**: a one-run prose instruction is a weak nudge the model can ignore; only the **engine** (separate model calls) truly enforces.
- **`2026-07-11_04-48`** — chunking long texts should be mandatory (budget-gated, snapping to structure), and a chunking instruction in the skill is a nudge — the engine is the real enforcer.
- **`2026-07-11_06-37`** — a source-character chunk budget (~3,500 conservative for the Opus model), held as an approximate band, not a hard threshold.

"Better or worse" is baseline-relative — better/worse *than what?* — so the answer is given against three baselines: the pre-edit SKILL.md, the inquiry recommendations, and an ideal end-state.

**Goal:** an honest, measured coverage audit (point-by-point) plus a better/worse verdict — evaluation only; no edit to the skill without the user's explicit authorization.

## Finding Summary

- **Better than the pre-edit version; partial against the recommendations.** The edit is a real improvement, but it lands only *half* of what the chain recommended.

- **The one clean structural truth:** a prose `.md` file can only **nudge** the model toward the fix; the failure class the chain diagnosed is **closed** only at the **engine layer** (separate model calls). The edit is the best the prose layer can do — the real close is a different artifact.

- **What landed (the chunking half):** chunking is now present (budget-gated, snaps to sentence/paragraph boundaries) where the pre-edit file had none; the case-catalog of niche translation patterns is now wired into the translate step; and the translate step is no longer a flat "apply everything at once" list — it now defers finalization through an ordered 4-layer process.

- **What did NOT land — the load-bearing shortfall (the root cause, `00-24`):** the translate step still **leads with the config** ("map the text… with most loyalty to the TranslationConfig") instead of a **config-blind Meaning-Lock first**. So the specific mechanism the root-cause finding named — style/config contaminating comprehension — is **not closed**. (The one-motion-collapse aspect *is* partially softened by the new deferral; the config-contamination aspect is not.)

- **What did NOT land — the second gap (secondary, and dependent on the first):** there is **no post-draft verification pass** (`01-09`). Per that finding's own words, verification is "inert until the meaning-lock fix is built," so this gap is downstream of the first.

- **Not defects — held as nuances:** the Opus chunk number is **~5,000** where `06-37` recommended **~3,500**; since the user set it themselves and that finding treated the number as approximate, this is a **calibration choice to confirm**, not a mistake. And the chunking-as-prose is the **honest ceiling of a `.md`** — the engine part was never the file's job. (Minor: `SKILL.md` line 34 points at a `notes.md` that no longer exists.)

- **The "better than pre-edit" leg is the least certain** — it rests on the earlier finding's *description* of the old translate step, not on a measured copy of it (the pre-edit version was not independently recovered).

## Finding

### Why this matters

The comprehenslate skill's quality problem was traced, across the six-finding chain, to one root cause: the skill *describes* a careful 3-Pass translation method but never *runs* it — meaning and style get decided together in one forward motion, and things get dropped or mistranslated. The user then edited `SKILL.md`. The question is whether that edit actually absorbed the chain's cumulative fixes. The honest answer is: it absorbed the easier half well, gestured at the harder half, and left the root-cause fix and the verification pass for later — and, importantly, some of what's "left for later" can only be done at the engine, not in this file at all.

### 1. What the edit measurably did (all verbatim-grounded)

Reading the current `SKILL.md`:

- **Chunking is now present** (Rules 7–8): per-model source-character budgets (Opus ~5,000; Sonnet ~2,500; Fable ~7,000), stretched to the nearest sentence/paragraph boundary, with the skill reporting the chunk count up front. The pre-edit file had no chunking at all.
- **The translate step (Step 5) is now a 4-layer ordered process:** (1) map the text into the target language "with most loyalty to the TranslationConfig," (2) apply policies, (3) check the case-catalog for niche patterns, (4) apply the harmony layer last — with each non-final layer saying "don't concrete the translation yet" and the final one saying "you can concrete now." This *defers finalization*, which softens the "decide everything in one motion" collapse.
- **The case-catalog is wired in** (Step 5.3) — the 139-entry catalog of niche meaning-carrying patterns.
- **The harmony layer is referenced as a step** (Step 5.4, naming "Harmony Map") — an improvement over the state `00-24` diagnosed, where the harmony file was pulled in *only* for its preservation-policy, never its method.

### 2. The load-bearing shortfall: the root-cause fix is not wired (the `00-24` crux)

The root-cause finding's fix has two parts, and it is precise about both:
1. an **anti-collapse structure** (don't decide meaning and style in one motion), and
2. a **config-blind Meaning-Lock as the first executed pass** — comprehend the meaning *before the style settings are in view*, "so style can't contaminate comprehension."

The edit lands part 1 partially (the "don't concrete until the end" deferral). It does **not** land part 2. Step 5.1 comprehends the text "with most loyalty to the TranslationConfig" — config-led from the first read, the exact opposite of config-blind. And the harmony/3-Pass is placed **last** (Step 5.4), so the Meaning-Lock is not the *first executed pass* — the ordering is effectively inverted from the 3-Pass.

Stated precisely (this is the critique's correction to an earlier, blunter phrasing): **the config-contamination mechanism is not closed; the one-motion-finalization aspect is partially softened.** The failure class `00-24` diagnosed — meaning and style decided together, producing dropped clauses and wrong word-senses — is therefore **not yet closed** on its load-bearing axis.

### 3. The second gap: no verification pass — and it is secondary

There is no post-draft verification step anywhere in `SKILL.md`. The harmony layer's Tier-1/2 preservation (Rule 5) is a *preservation policy applied during* translation, not a *re-read of the finished whole draft* checking for dropped/invented content — which is what `01-09` (and the "back bracket" of `04-48`, and the "checkpoint" of `23-03`) call for. So this recommendation is **MISSING**.

But it is **secondary and dependent on the first gap**: `01-09` itself says its verification content is "inert until the [meaning-lock] three-pass fix is actually built." So the sequence is: wire the meaning-lock first, then the verification pass has something to check against.

### 4. The clean structural truth: the SKILL layer nudges; the engine closes

This is the finding's deepest point, and it reframes what "coverage" can even mean here. Per the enforcement-gradient finding (`04-12`) and the project's design memory, a one-run prose instruction is a **weak nudge the model can quietly ignore**. That means:

- Even a *perfectly reordered* config-blind 3-Pass written into `SKILL.md` (see Next Actions R1) would still be **one model motion** — the model can still collapse it. It raises the probability of meaning-first behavior; it does not physically guarantee it.
- The failure class is **closed** only at the **engine**: separate model calls — a config-blind meaning-lock call whose output feeds a reconstruction call, plus per-chunk calls and a verification call. The scaffolding for this (`PipelineConfig` in `schemas.py`) already exists but is unwired.

So the coverage question splits by layer. **`SKILL.md` did the strongest thing a prose file can do** on several fronts; the recommendations that actually require the engine (`04-12`'s enforcement; the *guaranteed* close of `00-24`) are **not a defect of this file** — they belong to a different artifact that hasn't been built.

### 5. The coverage scorecard (with the critique's calibration corrections)

| Prior finding | Its recommendation | Verdict |
|---|---|---|
| **`04-48`** mandatory chunking | budget-gated chunking, snap to structure | **COVERED** (the mechanism is present) |
| **`04-12`** enforcement gradient | real enforcement needs the engine | **SKILL-layer share done (prose nudge) / engine share OPEN** — *not* "covered"; the load-bearing half (engine enforcement) is out of a `.md`'s scope |
| **`06-37`** chunk number | ~3,500 conservative for Opus | **PARTIAL** — snap + budget landed; the ~5,000 number is a **user calibration choice to confirm**, not a defect |
| **`01-09`** verification pass | config-independent post-draft check | **MISSING** — but **secondary and dependent** on the meaning-lock fix |
| **`00-24`** wire the 3-Pass | config-blind Meaning-Lock first | **PARTIAL** — anti-collapse deferral landed; config-blind-Meaning-Lock-first **not** wired (the load-bearing shortfall); harmony now referenced as a step (an improvement) |
| **`23-03`** end one-pass; add checkpoint | checkpoint after drafting | **PARTIAL** — one-pass softened; checkpoint still missing (= the `01-09` gap) |

(Note the `04-12` cell is deliberately *not* labeled "covered." Calling a prose nudge "covered" would over-credit the file: `04-12`'s primary recommendation — engine enforcement — is unaddressed, just not by this artifact. This is the single place the audit most risked inflating coverage.)

### 6. Better or worse (baseline-relative)

- **vs the pre-edit `SKILL.md` → BETTER** — chunking added, the flat one-motion translate list replaced by a deferred ordered process, the case-catalog and harmony referenced as steps; nothing lost. *(Confidence reduced: this baseline is inferred from `00-24`'s description of the old step, not from a recovered, measured copy — see Open Questions.)*
- **vs the inquiry recommendations → PARTIAL** — the chunking half landed; the 3-Pass-wiring and verification half did not.
- **vs an ideal end-state → the gap-list** — wire the config-blind Meaning-Lock first; add the verification pass; confirm the number; and, for the real close, wire the engine.

**The single most useful sentence for the user:** *Better than before — but the chain's most important recommendation, wiring the meaning-first / config-blind 3-Pass (the diagnosed root cause), is not yet landed, and there's no post-draft verification pass; the chunking half landed well, the ~5,000 number is yours to confirm against the ~3,500 the finding recommended, and the guaranteed close of the failure class needs the engine, not this file.*

## Inherited Commitments Re-test

This inquiry consumed six prior findings as the yardstick (a Synthesis Trigger). Each commitment is re-tested against the measured `SKILL.md`:

- **Commitment (`23-03`):** errors stem from one-pass generation with no checkpoint; end the one-pass, add a checkpoint.
  **Re-test status:** RE-TESTED — commitment confirmed but frame revised. **Evidence:** the one-pass is *partially* softened (the new "don't concrete until the end" deferral); the checkpoint is still absent. The commitment holds; the edit addresses one half.

- **Commitment (`00-24`):** wire the 3-Pass into the translate step, Meaning-Lock first and config-blind.
  **Re-test status:** RE-TESTED — commitment found PARTIALLY satisfied. **Evidence:** Step 5.1 comprehends "with most loyalty to the TranslationConfig" (config-led, not config-blind), and the 3-Pass is referenced last rather than wired as the governing first-pass structure. The anti-collapse deferral landed; the config-blind-Meaning-Lock-first mechanism did not. This is the load-bearing shortfall.

- **Commitment (`01-09`):** add a config-independent post-draft verification pass.
  **Re-test status:** RE-TESTED — commitment found INVALIDATED-in-coverage (MISSING). **Evidence:** no post-draft re-read exists; the harmony layer's preservation is a during-translation policy, not an after-draft check. Confirmed absent; secondary and dependent on the `00-24` fix per `01-09`'s own "inert until" note.

- **Commitment (`04-12`):** prose = weak nudge; engine = real enforcer.
  **Re-test status:** RE-TESTED — commitment confirmed. **Evidence:** the edit's chunking and staged translate step are prose nudges; this finding re-confirms the gradient and uses it as the load-bearing lens (the SKILL nudges; the engine closes). The recommendation's engine half is unaddressed but out of a `.md`'s scope.

- **Commitment (`04-48`):** budget-gated, snap-to-structure chunking, mandatory.
  **Re-test status:** RE-TESTED — commitment confirmed (mechanism). **Evidence:** Rules 7–8 provide budget-gated, boundary-snapping chunking. Landed as a prose nudge (the enforced version is engine-level).

- **Commitment (`06-37`):** ~3,500 conservative source-char floor for Opus, held as a band.
  **Re-test status:** RE-TESTED — commitment confirmed but frame revised. **Evidence:** snap-to-structure and a budget landed; the number is ~5,000 (above the ~3,500 floor and the demonstrated-safe 4,345). Since `06-37` quarantined the number as approximate and the user set 5,000 deliberately, this is a calibration choice to confirm, not a coverage defect.

*(Statuses are mostly "confirmed but frame revised" or "partially satisfied," not clean "confirmed" — the re-test genuinely tested each commitment against the text rather than rubber-stamping inheritance.)*

## Next Actions

All course-correction actions are **GATED**: this inquiry is evaluation-only, and no edit to the skill happens without the user's explicit authorization. (Routes R1–R7 are enumerated in `routelister.md`.)

### MUST

- **What:** Keep the audit's calibrated framing whenever it is reused — `04-12` is "SKILL-share-done / engine-share-open," not "covered"; the `00-24` crux is "config-contamination not closed / finalization softened," not a flat "not closed"; the verification gap is secondary-and-dependent.
  **Who:** whoever acts on this finding.
  **Gate:** condition-bound — on any reuse.
  **Why:** prevents over-crediting coverage (the finding's whole value is an honest audit).

- **What:** Keep every SKILL-editing action gated on explicit user authorization.
  **Who:** the implementing agent.
  **Gate:** condition-bound — until the user authorizes a specific edit.
  **Why:** the standing project constraint.

### COULD

- **What (R1):** Reorder Step 5 to a config-blind Meaning-Lock 3-Pass spine — make 5.1 comprehend *without* the config in view, then Harmony Map, then a Target-Reconstruction pass that applies config/policies/case-catalog/harmony and concretes.
  **Who:** the implementing agent. **Gate:** on authorization. **Why:** the strongest SKILL-layer nudge toward closing the root-cause crux. **Depends-on:** MUST "keep gated." This COULD is GATED — and note it is a **nudge, not a guaranteed close** (that is R4).

- **What (R2):** Add a whole-draft verification pass (a final step: re-read the finished draft — content dropped? invented? boundaries kept? structure survived?).
  **Who:** the implementing agent. **Gate:** on authorization; sequence **after R1** (verification is inert until the meaning-lock is wired). **Why:** closes the second gate at the SKILL-ceiling. **Depends-on:** MUST "keep gated"; and R1.

- **What (R3):** Confirm the chunk number — ask the user whether Opus ~5,000 is deliberate or should align to the ~3,500 the finding recommended.
  **Who:** a one-question exchange. **Gate:** observable — doable now. **Why:** resolves the one open residual (see Open Questions).

- **What (R5):** Recover the pre-edit `SKILL.md` from git history and measure it, to lift the reduced-confidence marker on "better than pre-edit."
  **Who:** a quick `git show`. **Gate:** observable. **Why:** anchors the vs-pre-edit verdict in a measured diff rather than an inferred description.

- **What (R6):** Fix the broken `notes.md` reference (line 34) — drop or repoint it (confirm with the user whether it was renamed or removed).
  **Who:** the implementing agent. **Gate:** on authorization. **Why:** removes a missing-file snag at the skill's Step 2. **Depends-on:** MUST "keep gated."

### DEFERRED

- **What (R4 — the real close):** Wire engine-level enforcement — separate calls (config-blind meaning-lock → reconstruction → per-chunk → verification), using the `PipelineConfig` fields already defined in `schemas.py`.
  **Gate:** condition-bound — revives when the project takes on engine/pipeline work.
  **Why (if revived):** this is where `04-12` actually lands and the only way to *physically close* the failure class rather than raise its probability. The standing structural frontier.

- **What (R7):** Record the "within-prose enforcement sub-gradient" (a flat list < ordered/named passes, both nudges) as an authoring lesson.
  **Gate:** condition-bound — revives on a genuine third instance.
  **Why (if revived):** extends the enforcement-gradient design rule; premature at two instances.

## Reasoning

The critique produced no kills — every part of the evaluation survived — but it applied three real calibration corrections that changed what the finding asserts, and understanding those is the substance here.

- **The `04-12` cell was de-credited from "covered" to "SKILL-share-done / engine-share-open."** Prosecution: calling a prose nudge "covered" over-credits the file, because `04-12`'s load-bearing recommendation is engine enforcement, which the file does not provide. Defense: the finding *anticipated* that the engine is a separate layer. Collision: the label was the problem — "covered" reads as "recommendation satisfied," so it was relabeled to say the SKILL did its share and the engine share is open (out of a `.md`'s scope). This is the place the audit most risked inflating coverage.

- **The root-cause verdict was made precise.** "The failure class is not closed" was too blunt — the deferral *does* soften the one-motion aspect. The corrected verdict splits it: the config-contamination mechanism is not closed; the finalization-collapse aspect is partially softened. This strengthens the finding by naming exactly what is open versus softened.

- **The verification gap was re-ranked from co-equal to secondary.** `01-09`'s own text says its content is inert until the meaning-lock is built, so the two gaps are not peers — the verification gap is downstream of the crux.

- **The "better than pre-edit" claim was quarantined.** Its baseline is inferred from `00-24`'s description of the old translate step, not a measured copy; so that one leg of the verdict carries a reduced-confidence marker until the pre-edit version is recovered (R5).

The deepest survivor was the reframe that the whole in-`SKILL.md`-prose approach is capped by the enforcement gradient — no prose edit can *guarantee* the fix; the engine is the real close. That is not nihilism about the edit: an ordered/named-pass instruction is a meaningfully stronger nudge than a flat "apply everything" list, which is exactly why the edit is better than the pre-edit version even though both are prose.

## Open Questions

### Blocked
- **Was the Opus ~5,000 number deliberate?** Cannot be resolved without the user (a different working corpus, or their own judgment, versus the ~3,500 the finding recommended). Surfaced as the one open residual.
- **Was `SKILL.md`'s pre-edit translate step really the "flat apply-everything-at-once list"** the "better than pre-edit" leg assumes? Blocked until the pre-edit version is recovered from git history (R5) and measured.

### Research Frontiers
- **Engine-level enforcement (R4)** — the separate-call pipeline that would *physically close* the failure class (not just nudge). Requires engine/pipeline work beyond a `.md` edit; the `PipelineConfig` scaffolding exists but is unwired.

### Refinement Triggers
- **Re-open the coverage verdict for `00-24` and `01-09`** if the reorder (R1) and verification pass (R2) are authorized and applied — the PARTIAL/MISSING cells move toward covered-at-the-ceiling (still nudges until R4).
- **Re-open "the SKILL layer only nudges"** if engine-level enforcement (R4) is built — at that point the failure class can actually be closed, and the coverage frame shifts from the SKILL file to the engine.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
reread the new SKILL/SKILL.md i edited, and does it cover our missing points from last inquiries and is it better or worse ?
```

</details>
