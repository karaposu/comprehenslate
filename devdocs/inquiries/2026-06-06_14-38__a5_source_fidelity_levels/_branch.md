# Branch: a5_source_fidelity_levels

## Question

**Context.** The root architectural finding `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` established A5 — Source Fidelity as the first axis in the Strategy family of Comprehenslate's 8-axis configuration framework. Per the root: A5's concept is "the translator's strategic stance on the foreignization ↔ domestication spectrum (Lawrence Venuti's framework)"; it answers "Should the translation sound like a translation, or read as if originally written in the target language?"; A5 controls lexical / idiomatic choices at the SURFACE of the translation. The root proposed 3 ordinal levels (heavily-foreignized / balanced / heavily-domesticated) but explicitly deferred level-value finalization to "the next inquiry." Distinct from A6 Form Preservation (which is structural — rhythm, parallelism, word order as meaning); root demonstrated four-corners orthogonality between A5 and A6.

The Reader family (A1+A2+A3) and Purpose family (A4) are now fully specified. 4/8 axes complete. A5 opens the Strategy family.

**A5 has a SPECIAL CONSTRAINT inherited from the prior chain.** The DOMESTICATE-disfavored project policy — established in `a1_cultural_reference_recognition_levels/finding.md`, extended through `a3_source_culture_levels/finding.md`, and confirmed as cross-cutting in `a4_purpose_categories/finding.md` — directly affects A5's range. A5 IS the axis on the foreignization-domestication spectrum. If the policy DISFAVORS DOMESTICATE across all purposes, then A5's user-configurable range cannot include a "default-domestication" or "freely-domesticated" level without contradicting the policy. The user-controllable range of A5 must operate WITHIN the policy constraints — likely an asymmetric range biased toward foreignization with restricted domestication options.

This is the central design tension this inquiry must resolve:
- If A5's range is symmetric (foreignized → balanced → domesticated), the user can OPT OUT of the project policy by choosing heavy domestication, contradicting the policy's intent.
- If A5's range is asymmetric (foreignized → balanced → light-restricted-domestication), the user has nuanced control within policy.
- If A5 only exposes the foreignization side (max-foreignized → moderate-foreignized → balanced), the user cannot configure even nuanced domestication choices, possibly over-restricting.

State the question:

- **Subject:** A5 — Source Fidelity level definitions.
- **Action:** Decide cardinality and level values; resolve the policy-constraint vs user-control tension; settle template + boundaries + per-purpose default cross-validation from A4.
- **Level:** Axis-level (one axis, plain-ordinal per root architecture).
- **Observation targets** (multiple, preserved separately):
  1. The CARDINALITY decision (root proposed 3; pattern across A1-A3 was 5; the policy constraint may suggest different count).
  2. The LEVEL NAMES (root proposed `heavily-foreignized / balanced / heavily-domesticated` but policy may need different labels).
  3. The CONCEPT each level captures (lexical / idiomatic surface choices — what proportion of foreignization vs domestication at the word/phrase level).
  4. The POLICY-CONSTRAINT vs USER-CONTROL tension resolution — how does the user-configurable range respect the cross-cutting DOMESTICATE-disfavored policy?
  5. The TEMPLATE STRUCTURE (capacity-graded 4-component from A1-A3? or different?).
  6. The A5↔A6 BOUNDARY — lexical/idiomatic surface (A5) vs structural form (A6); orthogonality already demonstrated in root; re-validate.
  7. The A5↔A4 DEFAULTS — A4 inquiry's matrix gave per-purpose A5 defaults (scholarly=foreignized; devotional=foreignized-max; casual=balanced; language-learning=balanced-to-foreignized; performance=balanced). Cross-validate against A5's level definitions.
  8. The A5↔A1 cultural-reference-recognition INTERACTION — A1's cultural-reference-handling actions (TRANSLITERATE-WITH-GLOSS / EXPLICATE-FUNCTION / DOMESTICATE) are FOREIGNIZATION-IMPLEMENTING actions. A5 is the strategic stance; A1 is the per-reference implementation. Boundary.
  9. The Venuti / Newmark / Nida theoretical anchors.
  10. The PROJECT CORPUS (Said Nursi) implications — Nursi's source culture is Islamic-Turkish; the project corpus consistently favors foreignization. What A5 levels does this corpus need?
  11. The HANDLING-ACTIONS structure — does A5 have its own handling actions or does it just modulate the actions from A1 + A3?

- **Deliverable shape:** N ordinal levels (cardinality decided substantively) with per-level definition + tension-resolution + template adaptation + A5↔A4/A6 boundary statements + per-purpose default cross-validation + Said Nursi corpus mapping + Strategy-family-opens marker.

**State the question:** **For A5 — Source Fidelity (the first axis in the Strategy family, plain-ordinal on the Venuti foreignization↔domestication spectrum, controlling lexical/idiomatic SURFACE choices distinct from A6's structural Form Preservation), what should the cardinality be (root proposed 3; A1-A3 pattern was 5; the cross-cutting DOMESTICATE-disfavored policy from the A1 chain + A4 may suggest an asymmetric range), what should each level capture, how does the user-configurable range respect the policy without contradicting it, what's the template adaptation, how does this cross-validate with A4's per-purpose defaults (scholarly/devotional foreignized; casual/performance balanced), and what's the A5↔A6 boundary (lexical/idiomatic surface vs structural) — anchored to Venuti / Newmark / Nida and the project's Said Nursi corpus?**

## Goal

- **Criterion.** N (3, 4, or 5) ordinal levels for A5 — each operationalizable as a translator-AI prompt instruction (so the AI knows what stance to take per encountered translation choice). The policy-constraint vs user-control tension MUST be resolved explicitly. The cardinality decision must be on substantive grounds.

- **Use case.** The user will commit `source_fidelity: Literal[...]`; the per-level prose becomes part of the translator-AI's prompt context; the per-level stance modulates handling actions at A1, A3 levels for individual choices.

- **Desired outcome.** A stable, named, defined set of A5 levels with per-level definition + policy-tension resolution + template adaptation + A5↔A6 boundary + A5↔A4 defaults cross-validation + Strategy-family-opens marker.

- **What would fail.**
  - Adopting symmetric foreignization-domestication range that lets the user opt out of the cross-cutting DOMESTICATE-disfavored policy.
  - Asymmetric range that's so restrictive it makes A5 useless as a configurable axis.
  - Conflating A5 with A6 Form Preservation (lexical/idiomatic vs structural).
  - Failing to cross-validate against A4's per-purpose defaults.
  - Failing to map to Said Nursi corpus.
  - Levels defined only by example without explicit per-level concept.
  - Failure to address the policy-tension explicitly.

## Source Input

```text
now lets do it for a5 source fidelity
```

## Scope Check

Question covers goal: YES.

The Question targets cardinality + level names + concepts + policy-tension resolution + template + A5↔A6 / A5↔A4 / A5↔A1 boundaries + Said Nursi + Venuti anchor + Strategy-family-opens marker. The Goal asks for all of those + operationalizability.

**Specific-vs-pattern check.** "Now lets do it for a5 source fidelity" — broader pattern of A5 across all corpora (not Said Nursi-only).

**Decoupling from prior chain commitments.** Root + A1+A2+A3 + A4 commitments are inherited and re-tested. The DOMESTICATE-disfavored policy interaction with A5 is the central substantive question.

**Template-adaptation in scope.** Whether A1-A3's capacity-graded template applies or A4's categorical template applies or A5 needs its own template is open.

## Synthesis Trigger

This inquiry consolidates / synthesizes commitments from 3+ prior inquiry outputs:

- `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — root architectural finding. Commits to: A5 concept (Venuti foreignization↔domestication); A5 plain-ordinal pattern (3 levels proposed, deferred); A5↔A6 four-corners orthogonality; Venuti / Nida / Newmark anchors.

- `devdocs/inquiries/2026-06-06_14-05__a4_purpose_categories/finding.md` — A4 inquiry. Per-purpose A5 defaults committed (scholarly foreignized; devotional foreignized-max; casual balanced; language-learning balanced-to-foreignized; performance balanced); DOMESTICATE-disfavored policy CARRIES THROUGH cross-cutting; default-when-A4-silent = casual (implies A5=balanced as default).

- `devdocs/inquiries/2026-06-06_11-47__a1_cultural_reference_recognition_levels/finding.md` — A1 cultural-reference-recognition. Established DOMESTICATE-disfavored project policy anchored to user's translation-register-fidelity memory + Venuti foreignization. Defined per-reference handling actions (TRANSLITERATE-WITH-GLOSS / EXPLICATE-FUNCTION / DOMESTICATE last-resort). A5 is the strategic stance these actions implement.

- `devdocs/inquiries/2026-06-06_13-33__a3_source_culture_levels/finding.md` — A3 inquiry. Extended DOMESTICATE-disfavored policy to A3 cultural handling. Defined 10 cultural handling actions in 4 categories.

Inherited commitments to re-test (non-exhaustive):
- A5 plain-ordinal pattern (root).
- A5 ~3 cardinality (root proposed).
- A5 controls lexical/idiomatic SURFACE (root).
- A5↔A6 orthogonality (root).
- Venuti foreignization↔domestication framework (root).
- DOMESTICATE-disfavored policy cross-cutting (A1 chain + A4) — CENTRAL CONSTRAINT for A5.
- A4 per-purpose A5 defaults (cross-validation).
- 4-component template adapts as needed (A1-A3 chain) — applicability to A5.
- Language-agnostic at concept level (root + chain).
- Receptive-only commitment (A1-A3 chain) — applicability to A5 (A5 is translator-strategy, not reader-property — may not apply, parallel to A4).
- Conservative-bias-LOWER default-when-silent (A1-A3) — applicability to A5 (A4 already overrides via per-purpose defaults).

Sensemaking will adjudicate; Critique will re-test.
