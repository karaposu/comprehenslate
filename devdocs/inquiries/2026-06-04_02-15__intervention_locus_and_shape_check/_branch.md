# Branch: intervention_locus_and_shape_check

## Question

- **Subject** — the intervention LOCUS and SHAPE recommended by the two prior inquiries (translation_failure_root_cause_diagnosis at `devdocs/inquiries/2026-06-03_23-30__translation_failure_root_cause_diagnosis/finding.md` and doc_internal_contradiction_cause_and_prevention at `devdocs/inquiries/2026-06-04_01-36__doc_internal_contradiction_cause_and_prevention/finding.md`). Both findings recommended adding/editing content in `harmony_layer.md` (and related framework docs `notes.md`, `advanced_principles.md`). The user is asking whether this intervention shape (in-doc additions) is correct OR whether a different shape (different file, different mechanism, different layer entirely) would be warranted.
- **Action** — evaluate (decide). Confirm or refute the proposed intervention locus + shape; surface alternatives that were considered or that should be considered; identify when a different locus/shape would be the right choice.
- **Level** — cross-cutting. The question is about WHERE the fix lives (which file or system layer) and WHAT SHAPE it takes (edit, addition, restructure, new artifact, tooling, etc.).
- **Observation targets** — preserving both clauses of the user's binary question as separate items:
  1. **Is in-doc addition to `harmony_layer.md` the right intervention?** Why does this locus/shape fit the cause structure? What evidence supports it as the correct choice? Is there any evidence that it's wrong or incomplete?
  2. **What alternative loci/shapes exist?** Enumerate the intervention options across the possibility space (in-doc / sibling-doc / new-file-in-framework / tooling / AI-prompt-layer / process-discipline / no-intervention) and assess each: was it considered in the prior inquiries? What is its disposition? When would it be the right choice instead of the recommended one?
- **Deliverable shape** — a clear yes/no on "addition to `harmony_layer.md` is right" with structural reasoning + a complete enumeration of alternative intervention loci with each one's disposition + the criteria that determine when each alternative would be the better choice.

Then: is in-doc addition to `harmony_layer.md` the right intervention locus and shape for fixing the cause diagnosed by the prior inquiries — and what alternative loci/shapes were considered (or should be considered) so the user can be confident the proposed answer is the right one, not just the only one the AI surfaced?

## Goal

- **Criterion** — clarity (a definitive answer with structural reasoning, not vague affirmation); coverage (alternative intervention loci enumerated systematically); honesty (don't just confirm the prior recommendation — actually re-test it against alternatives).
- **Use case** — the user decides whether to proceed with the prior inquiries' recommendations as-is or pivot to a different intervention shape. The user wants to commit time to implementation only after confirming the locus is right.
- **Desired outcome** — the user has confidence that "in-doc addition to `harmony_layer.md`" is either (a) the correct intervention and they should proceed, OR (b) the wrong intervention and they should pursue an alternative the prior inquiries missed.
- **What would fail** — vague affirmation ("yes, do that") without re-testing against alternatives; missing alternative intervention loci that the prior inquiries didn't surface; over-elaborating the analysis when the answer is straightforward.

## Source Input

```text
u said Layer 2 — Structural (the amplifier in the documents). Two structural defects in the framework allowed the proximate trigger to produce undetected failures. The first defect is an active misclassification: harmony_layer.md classifies "register consistency" as Tier 3 ("important for reader comfort but doesn't change meaning"). The doc's own ranking principle states that the closer a harmony component is to carrying meaning, the higher its priority. When source text uses register-alternation as a structural device — when plain folk diction grounds elevated theology, as the Fifth Word does — register IS meaning-carrying. By the doc's own principle, register-as-alternation should be Tier 1. The doc fails to distinguish register-as-style (which is Tier 3 correctly) from register-as-alternation (which should be Tier 1). The misclassification is an in-doc proof of internal inconsistency, not just an absence of guidance. The second defect: the harmony report at the bottom of the translation file (the framework's self-audit instrument) has zero register-related entries. Its content is generated from the tier system, so when the tier system silently demotes a feature, the audit silently omits it. The audit is structurally blind to the failure mode that occurred — the framework cannot see what its own classification told it not to look for.

so the solution is to make an addition to harmonly_layer.md ? or different?
```

## Scope Check

Question covers goal. The question asks the binary "is the solution X, or different?" and the goal asks "clarity + alternative coverage." Dual match.

Specific-vs-pattern check: the user's question is specifically about the prior inquiries' recommendations for `harmony_layer.md`. But "or different?" implicitly invites the full space of alternative intervention loci, not just `harmony_layer.md`-specific alternatives. Resolution: address both — confirm/refute the specific recommendation for `harmony_layer.md` AND enumerate the full intervention-locus possibility space (in-doc / sibling-doc / new-file / tooling / AI-prompt / process / no-intervention).

## Territory boundary (for Surfacing)

This inquiry's bounded territory:

- The two prior findings: `devdocs/inquiries/2026-06-03_23-30__translation_failure_root_cause_diagnosis/finding.md` (MVF-4 surgical tier fix + Emergent Assembly + S6/S7/S8 + DEFERRED items) and `devdocs/inquiries/2026-06-04_01-36__doc_internal_contradiction_cause_and_prevention/finding.md` (MVD + Full Emergent Assembly + S6/S7 + EA-7 cross-doc).
- The two prior inquiries' archived innovation and critique outputs (where alternative intervention loci were surfaced or ruled out).
- The framework docs themselves: `harmony_layer.md` (the proposed target), `notes.md`, `advanced_principles.md` (alternative loci within the framework).
- The intervention-locus possibility space: in-doc / sibling-doc / new-file-in-framework / tooling / AI-prompt-layer / process-discipline / no-intervention.
- In-domain knowledge about intervention-shape selection in technical-doc design.

Out of scope: rewriting the framework from scratch; the architectural Layer-2 fix (already RESEARCH FRONTIER in the prior inquiries); altering the AI's training (architecturally inaccessible to the user).
