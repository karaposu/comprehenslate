# Branch: Firing-Time Categories for Principles

## Source Input

```text
But the critique caught this framing being too clean, and the correction matters. Calling the failed principles "verification-shaped" (checking-only by nature) overstates it. Take "allegorical": a first pass properly holding A1=conversational (the reader-level axis that literally excludes dense-academic vocabulary) in mind could have picked "parable" or "comparison" while writing — no separate check needed. Same for "work" vs "foothold": if the sense-disambiguation policy had fired during writing, the right word comes out the first time. So these principles are dual-natured — able to fire while writing or at a check. The honest statement is: in a single fluency-first pass they went un-fired at generation, and there was no checkpoint to catch them afterward. The practical conclusion (add a checkpoint) is unchanged; only the mechanism-claim is softened.

and this made me thing that it would be really useful to use these 2 categories fireable_at_first_pass and fireable_at_second_pass for our principles or policies (not sure maybe both )
```

## Articulation Reference

- **File:** `articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** item-1 (firing-time categorization of the SKILL's principles/policies)
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**item-1 (literal):** *"The critique's correction — that the failed principles are dual-natured (able to fire while writing OR at a check), not verification-only — makes me think it would be really useful to use two categories, `fireable_at_first_pass` and `fireable_at_second_pass`, for our principles or policies (not sure — maybe both)."*

The ask carries these identified ambiguities (preserved, not adjudicated):

- **MQ1 verdict-axis** — adjudication stance: `[confirm-the-proposal-is-useful / evaluate-honestly-and-possibly-refine-or-reject / design-the-actual-scheme / diagnose-whether-it-earns-its-keep-given-the-3-Pass-fix-already-exists]`; tagging target (scope): `[principles only / policies only / both]`; category structure: `[two independent binary flags / a single 3-value enum (first-only / second-only / both) / a richer scheme with a 'neither-inert' or 'conditional' value]`; deliverable endpoint: `[yes/no-with-rationale on adopting / a concrete tag-scheme design / a per-principle classification inventory / a SKILL spec-edit adding the metadata]`.
- **MQ3 intent-axis (WHAT)** — `[make-firing-time-explicit-as-metadata (documentation/clarity) / drive-the-two-gate-procedure (first-pass tags → Pass-1 Meaning-Lock hold-set; second-pass tags → Pass-3 check) / auto-generate-the-check-agenda (the second-pass set becomes the post-draft checklist mechanically) / establish-a-design-discipline (every principle must declare its firing time as a standing invariant)]`.

## Goal

- **Deliverable shape (Deconstruct):** a design-plus-evaluation artifact — *should we adopt firing-time categories* + *what the scheme IS* + *what it changes* — with an actual per-principle classification and/or a SKILL spec-edit as gated reach (the same diagnose → design → apply reach gradient as the two prior inquiries). NOT a re-translation, NOT a re-diagnosis.
- **Bounds:** the SKILL's principle/policy files (`references/core/{harmony_layer.md, translation_principals.md, advanced_principles.md, notes.md}`; `references/config/schemas.py` Policy classes) × the two-gate procedure from the prior finding × the first-pass / second-pass / both firing-time distinction.
- **WHY-axis motivations (preserved, not chosen):** `[operationalize-the-two-gates: make the abstract "two gates" concrete and actionable per-principle / prevent-recurrence-at-generation: the deeper failure was principles un-fired AT GENERATION — knowing which are first-pass-fireable is what lets Pass-1 fire them / enable-tooling: the second-pass set could auto-produce the post-draft check agenda / taxonomic-understanding: classify the principle corpus to understand it better / design-hygiene: force every principle to declare its firing time so the "stated-but-never-fired" gap can't recur silently]`.
- **Context the answer needs (MQ2):** the two prior findings as baseline (the dual-shaped correction; the two-gate 3-Pass fix); the actual content of the SKILL's principle/policy files (to know what would be tagged and whether firing-time is decidable per entry); what "principle" vs "policy" concretely denote here (harmony Tiers / translation-principle bullets / advanced principles / the no-smoothing rule / the schemas.py Policy classes — heterogeneous, may tag differently). **Stance:** honest evaluation — if firing-time tagging overlaps what the 3-Pass wiring already delivers, or adds taxonomy overhead, or mis-fits genuinely dual/context-dependent principles, say so; do not merely ratify.

## Considered Articulations

**Item item-1 — firing-time categorization of the SKILL's principles/policies:**
1. **Honest evaluation** — assess whether firing-time tagging (`fireable_at_first_pass` / `fireable_at_second_pass` / both) is worth adopting, or is overhead / a mis-fit for dual principles / redundant with the 3-Pass wiring.
2. **Scheme design** — design the tag structure (two binary flags vs a 3-value enum with a 'both'/'conditional' value), where the metadata lives, and how a principle's firing-time is decided.
3. **Operational driver** — specify how the tags DRIVE the two gates (first-pass → Pass-1 hold-set; second-pass → Pass-3 check-agenda), so the tag is not inert metadata.
4. **Annotation inventory** — actually classify each principle/policy by firing-time (first / second / both), producing the tagged inventory.
5. **Design discipline** — establish firing-time declaration as a standing requirement for every present and future principle/policy, as a design-hygiene invariant.

## Scope Check

**Question covers goal: YES**, with two preserved forks (from the MQA reconciliation).

- **Fork 1 — CATEGORIZATION-PURPOSE (inert metadata vs operational driver):** is the firing-time tag descriptive documentation, or does it actively drive the two-gate procedure (generating the Pass-1 hold-set and the Pass-3 check-agenda)? This is the load-bearing openness — a descriptive tag is cheap but may add nothing beyond the already-designed 3-Pass; an operational tag is where value would be, but it rides on the prior inquiry's 3-Pass wiring. The pipeline resolves this with evidence, esp. whether the tag earns its keep.
- **Fork 2 — TAGGING-TARGET well-definedness (does firing-time cleanly apply to each heterogeneous artifact?):** what counts as a "principle" vs "policy" here (harmony Tiers, translation-principle bullets, advanced principles, the no-smoothing rule, the schemas.py Policy classes), and whether some entries are genuinely dual or context-dependent so a clean first/second partition mis-fits them — which is exactly why the user hedged "maybe both."

**IN-scope (per Deconstruct bounds):** the evaluation of the proposal + the scheme design + (gated) the per-principle classification and/or the spec-edit. **OUT-of-scope (per MQ4):** re-adjudicating the dual-natured mechanism-correction (accepted as premise); re-diagnosing the 7 errors or re-deriving the 3-Pass fix (settled priors); re-translating the passage.

**Specific-vs-pattern:** the "allegorical" and "work"-vs-"foothold" examples are the specific evidence that principles are dual-fireable; the user asks for the broader *categorization scheme* over the whole principle/policy corpus — address the broader pattern, grounded in those examples.

## Layer Commitment

**Trigger present:** the question targets a framework artifact (the SKILL's principle/policy corpus) for a meta-restructure — adding a firing-time classification dimension. MQ1's verdict-axis includes `design-the-actual-scheme` and a spec-edit deliverable.

**Primary layer: STRUCTURAL.** The essence of the ask is *adding a classification attribute* (firing-time) to the principle/policy artifacts — what the principle corpus's spec/schema LOOKS LIKE gains a new dimension. The deliverable the user names ("use these 2 categories for our principles/policies") is a metadata/organization scheme over existing artifacts, not a redefinition of what translation or a principle IS, and not (primarily) a new procedure.

**Other layers considered, out of scope (or sequential) for THIS run:**
- **Process** (how the tags are CONSUMED — first-pass tags driving Pass-1's hold-set, second-pass tags generating Pass-3's check-agenda). This is coupled and is where the tag's operational value lives, BUT it rides on the prior inquiry's already-designed 3-Pass wiring (`2026-07-11_00-24`). **Sequential plan:** Structural first (design the scheme + classify the corpus); the Process consumption-wiring is a follow-on that largely overlaps the prior inquiry's 3-Pass fix, and would be its own gated edit. Fork 1 (Scope Check) tests whether the structural tag is worth anything WITHOUT the process consumption — i.e., whether this must be Process-coupled to earn its keep.
- **Meaning** (what a "principle" or "policy" fundamentally IS) — not in scope; existing principles are being classified, not redefined.

## Synthesis Trigger

This inquiry consumes TWO prior inquiry outputs as load-bearing inputs and inherits commitments from each (MQ2's verdict sub-axis named both as needed context). The proposal is a direct formalization of their shared insight, so their commitments must be re-tested, not silently absorbed.

- `devdocs/inquiries/2026-07-10_23-03__translation_error_root_cause_skill_adherence/finding.md` — commits to: the 7 errors = one fluency-first pass with no post-draft checkpoint; principles are **dual-shaped** (able to fire at generation OR at a check) — critique-corrected from "verification-shaped"; blame co-equal. **The "dual-shaped" commitment is the premise this entire proposal rests on** (the firing-time categories ARE the dual-shaped insight formalized).
- `devdocs/inquiries/2026-07-11_00-24__semantic_priority_before_harmony_generation/finding.md` — commits to: the root cause is the SKILL's 3-Pass method never being proceduralized by `SKILL.md` Step 5; two gates (generation-time meaning-lock + post-draft check) missing for one reason; the fix = wire the 3-Pass meaning-first; principles present-as-principle but absent-as-procedure. **The two-gate structure is what the firing-time tags would populate** (first-pass = gate 1's hold-set; second-pass = gate 2's check-agenda).

CONCLUDE must include an `## Inherited Commitments Re-test` section testing: (i) the dual-shaped-principle claim (does every principle actually partition into first/second/both, or are some inert / context-dependent, which would strain the taxonomy?); (ii) the two-gate procedure (does the firing-time tagging actually operationalize both gates, or only re-describe them?); (iii) whether this proposal is additive to the 3-Pass fix or redundant with it. Sensemaking and Critique must do the re-testing, not just record it.
