# Branch: SKILL.md edit — coverage of prior inquiries + better-or-worse

## Source Input

The user's raw request, preserved verbatim:

```text
reread the new SKILL/SKILL.md i edited, and does it cover our missing points from last inquiries and is it better or worse ?
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-07-11_20-41__skillmd_edit_coverage_of_prior_inquiries/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** `i1`
- **Verdict:** MED-FLAG
- **Flagged conditions:** the comparison-baseline ambiguity — "**better or worse than WHAT?**" (pre-edit SKILL.md / the inquiry recommendations / an ideal end-state) is load-bearing and materially changes the verdict; plus the eval-only-vs-eval+fix-list reach overlap.

## Question

**Literal statement (i1):** "reread the new SKILL/SKILL.md i edited, and does it cover our missing points from last inquiries and is it better or worse?"

**What kinds of ask this carries (MQ1 verdict-axis, preserved as ambiguities):**
- **coverage-audit** — does the edited `SKILL/SKILL.md` actually incorporate the prior chain's missing-points / recommendations, per point (covered / partial / missing)?
- **comparative-verdict** — is the edited version *better or worse* — and than which baseline (see Scope Check)?
- **evaluation-only vs evaluation-plus-fix-list** — pure diagnosis, or also a punch-list of what to fix next?

**What action-endpoints are plausible (MQ3 intent-axis, preserved as ambiguities):**
- `validate-the-edit` (confirm the intended improvements landed) vs `find-remaining-gaps` (surface what's still missing) vs `decide-next-step` (keep / extend / revert) vs `pre-ship-sanity-check` (good enough to rely on?). Endpoint shape: a **report/verdict** vs a **prioritized fix-list** vs a **go/no-go**.

## Goal

**Deliverable shape (Deconstruct):** an **evaluation** — a point-by-point coverage audit + a comparative better/worse verdict, optionally a remaining-gap list. Kind: analysis / assessment (Markdown; likely a per-point coverage table). Bounds: object = the edited `SKILL/SKILL.md`; yardstick = the prior inquiry chain's recommendations; **evaluation-only (no edit) absent explicit authorization**.

**Motivations a good answer might serve (MultiDepth WHY-axis, preserved as ambiguities):**
- `quality-assurance-before-relying-on-it` vs `course-correction` (what to fix next) vs `close-the-loop` (validate the chain's work actually reached the SKILL) vs `independent-second-opinion-on-my-own-edit`.

**Context downstream consumers need (MQ2, preserved as ambiguities):**
- **verdict:** the current literal `SKILL/SKILL.md` text + what each prior missing-point actually was (findings 06-37 / 04-48 / 04-12 / 01-09 / 00-24 / 23-03).
- **kinds:** which missing points count — the char-budget number (3500 vs the edit's ~5000), snap-to-structure, the 3-Pass wiring, the whole-draft verification pass, the enforcement gradient (prose-nudge vs engine), chunking-mandatoriness.
- **stance:** better/worse relative to which baseline; on which axis (number-correctness / coverage-completeness / enforcement-strength); how rigorous (audit vs gut-check); and **isolation vs orchestrator** — evaluate SKILL.md's literal text alone, or as the orchestrator of the referenced files it points to (some missing points now live in those files).

**Negative spec (MQ4 exclusions):**
- `evaluation-only-not-apply` — the ask is "does it cover / better-or-worse", NOT "fix it"; the standing constraint (no SKILL edits without explicit authorization) holds — producing an edit is out of scope unless the user later authorizes.
- `reading-scoped-to-SKILL.md` — the object is that one file (though coverage may need checking whether it *wires in* referenced mechanisms).
- `don't-re-derive-the-priors` — the prior findings are the yardstick, not something to re-litigate.

## Considered Articulations

**Item i1 — "reread the new SKILL/SKILL.md ... cover our missing points ... better or worse?":**
1. **Audit vs recommendations:** point-by-point, does the edit incorporate each prior recommendation (char-budget & its number, snap-to-structure, 3-Pass wiring, whole-draft verification, enforcement gradient, chunking-mandatoriness) — mark each covered / partial / missing — and judge better-or-worse **relative to the inquiry recommendations**.
2. **Better vs the pre-edit SKILL.md:** did the edit improve the SKILL on net **compared to its previous state**, independent of matching the recommendations fully.
3. **Eval + fix-list:** the coverage/verdict **plus** a prioritized punch-list of remaining gaps to close next.
4. **Go/no-go sanity check:** is the edited SKILL.md good enough to rely on, or does it carry a blocking gap.
5. **Orchestrator reading:** assess whether SKILL.md correctly **wires in** the mechanisms (including those in referenced files it points to, e.g. case_catalog / harmony_layer) — SKILL.md as orchestrator — vs assessing only its literal in-file text.

## Scope Check

**Question covers goal: PARTIAL — the comparison baseline is unspecified and must be spanned, not silently chosen.** The Question asks "cover missing points" + "better or worse"; the Goal's yardstick (MQ2 stance) has three live baselines that give *different* verdicts:
- **vs the pre-edit SKILL.md** → almost certainly "better" (the edit adds chunking + the case_catalog wiring where there was none).
- **vs the inquiry recommendations** → "partial" (some points landed, some didn't, and at least one number diverges: 5000 vs 3500).
- **vs an ideal end-state** → surfaces the largest gap list.

Per the MED-FLAG, the downstream pipeline should **address the broader pattern across all three baselines** (default: broader pattern, not one specific reading), and explicitly report coverage per-point rather than collapsing to a single better/worse token. Also span the **isolation-vs-orchestrator** reading (does SKILL.md's *text* carry the mechanism, or does it correctly *point at* a referenced file that does).

**Specific-vs-pattern:** "our missing points from last inquiries" points at a specific set (the 6-finding chain) but the real ask is the **broader coverage pattern** — did the SKILL absorb the chain's cumulative recommendations. Address the pattern, grounded in the specific findings.

## Synthesis Trigger

This inquiry **consumes ≥2 prior inquiry outputs as the evaluation yardstick** (MQ2's verdict sub-axis names them as required context). Each prior carries a commitment/recommendation this inquiry inherits as the standard the edited SKILL.md is measured against; CONCLUDE will require an `## Inherited Commitments Re-test` naming each and re-testing whether the SKILL.md edit satisfies it (with cited evidence from the SKILL.md text) or flagging it inherited-without-re-test.

- `devdocs/inquiries/2026-07-11_06-37__char_word_count_vs_structural_chunk_budget/finding.md` — chunk by a **source-character budget (~3,500 conservative for Opus)** snapping to structure; confound-robustness; length-mechanism quarantined; comprehenslation integrity.
- `devdocs/inquiries/2026-07-11_04-48__mandatory_chunking_char_limit_adherence/finding.md` — chunking should be **mandatory** for adherence; chunk-by-structure-snapping-to-boundaries.
- `devdocs/inquiries/2026-07-11_04-12__staged_skill_borders_and_middleware/finding.md` — staged SKILL borders + the **enforcement gradient** (one-run prose instruction = weak nudge; separate call/engine = real enforcer).
- `devdocs/inquiries/2026-07-11_01-09__*/finding.md` — a **config-independent whole-draft verification spine** + a config-derived reader-keyed agenda (a post-draft check).
- `devdocs/inquiries/2026-07-11_00-24__*/finding.md` — the diagnosed root cause: the SKILL's **3-Pass method (Meaning-Lock → Harmony-Map → Target-Reconstruction) is un-wired** into Step 5.
- `devdocs/inquiries/2026-07-*_23-03__*/finding.md` — the original **7-error / one-pass / no-checkpoint** failure diagnosis.

The Sensemaking + Critique disciplines must actually re-test each of these against the current SKILL.md text, not merely record the inheritance.
