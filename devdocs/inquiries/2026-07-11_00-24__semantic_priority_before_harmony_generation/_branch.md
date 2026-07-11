# Branch: Semantic Priority Before Harmony Generation

## Source Input

```text
u said

But the SKILL's workflow file (SKILL.md) collapses the actual translating into a single instruction — "produce the translation." So the three passes ran in spirit, as one integrated motion, not as three distinct steps with a gate between draft and output. In a single fluent motion, the mind (or model) is generating forward — reaching for the next natural-sounding English phrase. That is exactly the state in which:

a slightly literary word ("allegorical," "mute tongue") feels natural and gets written;
a clause that is a little awkward to carry ("basit avamın fehmine gelecek") gets smoothed away and quietly dropped;
the first, most common sense of a word ("work" for iş) gets taken;
a faithful-but-dense construction ("no one lacking… can…") gets produced because it mirrors the source's shape.
Each of these is the natural output of fluency-first generation. And the SKILL predicted this: one of its own always-on policies is a no-smoothing rule that explicitly names "natural target-language fluency" as the bias to guard against. The SKILL knew this failure was coming. It just had no step that would catch it.

but how these are possible? harmony layer is sth that should work on top of the base accurate  semantic understanding and translation options and pick harmony config suitable one,  it shouldnt meddle with semantic correct understanding part directly,

maybe instructions are missing? it should be explicit that first comprehend the text understand the meaning, and then with the nudge  of harmonic  config given you must generate a trasnlation

maybe problem was this instruction was not obvious and harmony layer without semantic priority did translation ?

how this can be fixed?
```

## Articulation Reference

- **File:** `articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** item-1 (semantic-priority-ordering diagnostic + fix)
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**item-1 (literal):** *"How are these errors possible if the harmony layer is supposed to work on top of accurate semantic understanding and only pick the harmony-suitable option — not meddle with semantics directly? Maybe the instructions are missing an explicit 'first comprehend the meaning, then generate a translation under the harmonic-config nudge' ordering. Maybe the problem was that this instruction wasn't obvious, so the harmony layer, without semantic priority, did the translation. How can this be fixed?"*

The ask carries these identified ambiguities (preserved, not adjudicated):

- **MQ1 verdict-axis** — adjudication stance: `[confirm-the-hypothesis / evaluate-and-possibly-correct-it / find-the-real-cause-whatever-it-is]`; relationship to the prior finding: `[SUPERSEDES the "no checkpoint" diagnosis / REFINES it (deeper layer) / COMPLEMENTARY second mechanism (pre-generation ordering AND post-generation check both true, different loci)]`; fix shape: `[design-the-explicit-ordering-instruction / restructure-the-SKILL's-process / diagnose-only-with-gated-edit]`.
- **MQ3 intent-axis (WHAT)** — `[understand-why-it-happened-more-deeply (deeper than the prior "no checkpoint") / produce-a-concrete-SKILL-instruction-edit (the explicit two-phase ordering) / establish-a-general-architectural-invariant (semantic comprehension has PRIORITY over harmony as a standing design principle)]`.

## Goal

- **Deliverable shape (Deconstruct):** a diagnostic-understanding artifact (does a missing/unenforced semantic-comprehension-priority ordering explain the errors?) **+** a fix-design (how to make comprehend-first-then-harmony-generate explicit and enforced), the fix gated like the prior inquiry's reach. NOT a re-translation.
- **Bounds:** the SKILL's process/instruction ordering × `harmony_layer.md`'s actual structure (esp. Pass-1 "Meaning Lock") × the 7 errors as evidence × the prior finding as baseline.
- **WHY-axis motivations (preserved, not chosen):** `[architectural-correctness: ensure the SKILL is layered right — semantics foundational, harmony a layer on top; deeper-root-cause: the prior "no checkpoint" addressed catching the error, not why generation produced it — the user wants the deeper generative why; fix-at-source: prevent recurrence at the GENERATION step (get meaning right first), not only at a post-draft CHECK; validate-mental-model: confirm or correct the user's "harmony on top of semantics" model against the actual SKILL]`.
- **Context the answer needs (MQ2):** whether `harmony_layer.md` ALREADY encodes a semantic-first phase (its Pass-1 Meaning Lock) — so the ordering is *present-but-unenforced* vs *missing*; whether `SKILL.md`'s workflow specifies any comprehend-then-generate order; whether the user's "harmony layer" = the whole `harmony_layer.md` file (which CONTAINS Meaning Lock — semantics already lives inside it) or a narrower "harmonic-config nudge only" notion. **Stance:** honest evaluation — if the hypothesis is partly wrong or overlaps the prior finding rather than being wholly new, say so; do not merely ratify.

## Considered Articulations

**Item item-1 — the semantic-priority-ordering diagnostic + fix:**
1. **Hypothesis-confirmation diagnostic** — test "harmony-without-semantic-priority" against the actual SKILL: does `harmony_layer.md` establish semantic priority (Meaning Lock as Pass 1) or not? Verdict + the explicit-ordering fix.
2. **This-vs-prior reconciliation** — diagnose whether the missing-ordering is a DEEPER/DIFFERENT cause than the prior "no checkpoint," or the same failure from the generation side; produce a unified two-locus account (pre-generation semantic-lock + post-generation check) and state how they relate.
3. **Architectural-layering diagnosis** — is the SKILL correctly layered (semantics foundational, harmony on top), and does it make the layering EXPLICIT and ENFORCED? Fix = encode the layering as an explicit ordered process with semantics having priority.
4. **Instruction-gap fix-design** — produce the concrete missing instruction ("first comprehend and lock the meaning, then generate under the harmony nudge") and specify where it lives and how it is made non-skippable.
5. **Disconfirm-and-refine** — test the hypothesis and possibly find it PARTLY right (ordering underspecified/unenforced) but the mechanism subtler than "harmony overrode semantics" — e.g., Meaning Lock exists as Pass-1 but produces no semantic artifact that generation must respect, so meaning and harmony collapse into one motion.

## Scope Check

**Question covers goal: YES**, with two preserved forks.

- **Fork 1 — THIS-vs-PRIOR relationship (from MQA joint-axis 1):** whether the semantic-priority-ordering hypothesis SUPERSEDES / REFINES / COMPLEMENTS the prior "no post-draft checkpoint" finding. The pipeline must hold this open and resolve it with evidence (Sensemaking / Critique), not assume it. **If it resolves to REFINES or SUPERSEDES, CONCLUDE must include an `## Inherited Commitments Re-test` section** testing the prior finding's load-bearing commitments (the "no checkpoint = the cause" claim; the "co-equal blame" framing; the scoped-verification-pass fix). Flagged here so it is not silently absorbed.
- **Fork 2 — ordering MISSING vs PRESENT-BUT-UNENFORCED:** whether the SKILL genuinely lacks the comprehend-first ordering, or contains it (Meaning Lock is literally Pass 1 of `harmony_layer.md`) but never enforces semantic priority over harmony. This changes the fix from "add a phase" to "re-order / enforce existing phases."

**IN-scope (per Deconstruct bounds):** the diagnosis of the generative mechanism + the fix-design for semantic-priority ordering. **OUT-of-scope (per MQ4):** re-translating the passage; re-litigating that the 7 errors are real; changing config-values or corpus-notes.

**Specific-vs-pattern:** the 7 errors are the specific evidence, but the user asks for the broader *generative* mechanism (why harmony/fluency drove generation) and a *structural* fix — address the broader pattern, grounded in the 7.

## Layer Commitment

**Trigger present:** the question targets the SKILL (a framework artifact) for potential restructuring — "maybe instructions are missing… it should be explicit that first comprehend… then generate." MQ1's verdict-axis includes `restructure-the-SKILL's-process`.

**Primary layer: PROCESS.** The essence the user is after is an *ordering with priority* — comprehend-and-lock-meaning FIRST, THEN generate under the harmony nudge, with semantics having standing priority over harmony. That is a procedure / sequence / gate question — the Process layer (what steps the SKILL runs, in what order, with what precedence).

**Other layers considered, out of scope for THIS run:**
- **Structural** (where the instruction text lives; adding a section to `SKILL.md` / `harmony_layer.md`) — this follows *from* the process decision; the structural edit is the fix's downstream expression, not its essence. Sequential: once the process ordering is settled, a structural edit realizes it.
- **Meaning** (what translation fundamentally IS) — not in scope; the SKILL's definition of translation is not being redefined, only the order/priority of its sub-steps.

## Prior-Finding Relationship (open — resolve in pipeline)

- **Prior:** `devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md` — commits to: (a) the 7 errors = one fluency-first pass with no post-draft checkpoint; (b) blame is co-equal (application-failure + tool-deficiency); (c) fix = a scoped post-draft verification pass; (d) principles are dual-natured, un-fired at generation with no backstop.
- This inquiry's hypothesis targets commitment (a)'s LOCUS: the prior emphasized the *missing post-draft check*; the user emphasizes a *missing pre-generation semantic-lock ordering*. Fork 1 (Scope Check) governs whether this refines/supersedes/complements. The pipeline must test the prior's commitments, not inherit them.
