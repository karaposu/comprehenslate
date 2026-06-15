# Branch: a7_scaffolding_levels

## Question

**Context.** The root architectural finding `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` established A7 — Scaffolding as the third axis in the Strategy family of Comprehenslate's 8-axis configuration framework, the third Strategy axis that closes the family. Per the root: A7's concept is "how much explanatory material accompanies the translation at the text surface — footnotes, parenthetical glosses, transliterations, brief in-line explanations." It answers "How much help does the reader need at the surface of the translation?" Pattern: plain ordinal, proposed 5 levels (`off / minimal / standard / rich / scholarly`).

A7 has TWO SPECIAL CHARACTERISTICS distinguishing it from other Strategy axes:

1. **A7 is the SCAFFOLDING BUDGET for A1/A3 implementation actions.** A1 cultural-reference-recognition's handling actions (INLINE-GLOSS, FOOTNOTE, EXPLICATE-FUNCTION, KEEP-AS-IS, DOMESTICATE) and A3 source-culture's handling actions (TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT, BRIDGE-CULTURAL-DISTANCE, KEEP-HONORIFICS-SOURCE, etc.) include actions that CONSUME scaffolding budget (INLINE-GLOSS, FOOTNOTE, TRANSLITERATE-WITH-GLOSS, FLAG-CULTURAL-CONTEXT, BRIDGE-CULTURAL-DISTANCE) and actions that don't (KEEP-AS-IS, EXPLICATE-FUNCTION, PARAPHRASE, ASSUME-SHARED-CULTURAL-KNOWLEDGE). A7's level determines how much scaffolding the AI can spend per translation, which in turn affects WHICH A1/A3 actions can fire. At A7=off, the AI cannot use INLINE-GLOSS / FOOTNOTE / TRANSLITERATE-WITH-GLOSS — only the scaffolding-free actions remain available. This is a STRUCTURAL constraint on the foreignization-preserving alternatives that the A1 chain + A4 + A5 policy depends on.

2. **A7 controls the MULTI-MEANING RENDER decision when polysemy policy activates.** Per root finding's Layer 2 POLICY section: "When the always-on POLICY of multi-meaning preservation activates (a polysemous word allows multiple senses simultaneously per the local construction), A7's level controls how the preserved meanings RENDER: at low Scaffolding, the primary meaning appears with a minimal footnote noting other senses; at high Scaffolding, the multiple meanings appear inline or in a full footnote. The user does not control WHETHER multiple meanings are preserved (that's policy); the user controls HOW they appear." This makes A7 the user-facing render-control surface for the polysemy policy.

A7 also subsumes the user's original sketch's "feature activation" bundle MINUS the harmony component (which became A6): footnote toggle + transliteration toggle + parenthetical glosses + brief in-line explanations. Per root: "This isn't a heterogeneous bundle; it's one ordinal dial. Higher levels mean more explanatory aid."

The Reader family (A1+A2+A3), Purpose family (A4), and the first two Strategy axes (A5 Source Fidelity + A6 Form Preservation) are now specified. 6/8 axes complete. **A7 closes the Strategy family.**

The A4 finding's matrix gave per-purpose A7 defaults: scholarly=rich; devotional=moderate; casual=rich (help unfamiliar); language-learning=MAX rich; performance=minimal.

State the question:

- **Subject:** A7 — Scaffolding level definitions (5 ordinal levels per root proposal).
- **Action:** Decide cardinality + level names + per-level scaffolding budget specification + interaction with A1/A3 actions + multi-meaning render rules + cross-axis cross-validation.
- **Level:** Axis-level (one axis, plain-ordinal per root architecture).
- **Observation targets** (multiple, preserved separately):
  1. The CARDINALITY decision (root proposed 5; validate substantively — the 5 levels off / minimal / standard / rich / scholarly cover the spectrum from no-scaffolding to apparatus-edition).
  2. The LEVEL NAMES (root suggested off / minimal / standard / rich / scholarly; validate against project use cases).
  3. The SCAFFOLDING BUDGET specification per level — what AMOUNT of explanatory material (footnotes per page; inline glosses per chapter; transliterations per page; in-line explanations per passage) is permitted at each level.
  4. The INTERACTION WITH A1/A3 ACTIONS — A7's level determines which A1/A3 actions can fire. At A7=off, INLINE-GLOSS / FOOTNOTE / TRANSLITERATE-WITH-GLOSS / FLAG-CULTURAL-CONTEXT cannot fire; the AI falls back to KEEP-AS-IS / EXPLICATE-FUNCTION / PARAPHRASE / ASSUME-SHARED. At A7=scholarly, all actions including extensive FOOTNOTE / BRIDGE-CULTURAL-DISTANCE / FULL-APPARATUS fire freely.
  5. The MULTI-MEANING RENDER rules per level — per root, A7 controls HOW multi-meaning preservation renders (low A7 = primary meaning + minimal footnote; high A7 = inline or full footnote).
  6. The A4 MATRIX CROSS-VALIDATION — A4's per-purpose A7 defaults must map to A7's level definitions.
  7. The A7 ↔ A5 INTERACTION — A5's lightly-domesticated level needs MORE scaffolding to bridge cultural distance; A5's foreignized-max level needs LESS scaffolding because the source-cultural specificity carries itself. But A7 and A5 are still distinct axes — A7 controls the BUDGET; A5 controls the STRATEGIC STANCE. Re-validate orthogonality.
  8. The A7 ↔ A6 INTERACTION — A6 (form preservation) and A7 (scaffolding) — are they orthogonal? A6=maximum needs A7=minimal (clean text for cadence); A6=off needs A7=high (scaffolding compensates for form-loss). Are they really orthogonal or related?
  9. The TEMPLATE STRUCTURE — A5's NEW translator-strategy 4-component template likely fits A7 (both translator-strategy ordinal axes).
  10. The PROJECT CORPUS — Said Nursi corpus mapping per A7 level.
  11. Receptive-only NOT APPLICABLE check (parallel to A4, A5, A6).
  12. Default-when-A7-silent (likely chain through A4 matrix).
  13. The STRATEGY-FAMILY-CLOSURE marker — A7 closes the Strategy family at 3/3.
  14. The SCAFFOLDING-BUDGET COUPLING with A1/A3 — when A7 is too low to accommodate the A1/A3 actions a low reader-level would demand, what happens? The AI may have to choose between "use a scaffolding-consuming action and exceed budget" vs "fall back to a scaffolding-free action that doesn't suit the reader-level". This is a runtime conflict.
  15. The MULTI-MEANING RENDER OPTIONS at each level — what specific render mechanisms (primary-only + footnote; inline-paren; inline-paired; full-footnote-paired) are permitted at each level?

- **Deliverable shape:** 5 ordinal levels with per-level scaffolding-budget spec + interaction-with-A1/A3-actions table + multi-meaning render rules + A4 cross-validation + A7↔A5 and A7↔A6 boundary statements + template adaptation + Said Nursi corpus per level + receptive-only non-applicability + chain default + Strategy-family CLOSURE marker.

**State the question:** **For A7 — Scaffolding (the third and final axis in the Strategy family; plain-ordinal explanatory-material-budget at the text surface; subsumes footnote toggle + transliteration toggle + parenthetical glosses + brief in-line explanations from user's original sketch; SCAFFOLDING BUDGET for A1/A3 implementation actions; RENDER CONTROL for multi-meaning policy when polysemy fires), what should the 5 ordinal level names be (root proposed off / minimal / standard / rich / scholarly), what per-level scaffolding-budget specification + interaction with A1/A3 actions + multi-meaning render rules apply, how this cross-validates with A4's per-purpose A7 defaults (scholarly=rich; devotional=moderate; casual=rich; language-learning=MAX rich; performance=minimal), how the A7↔A5 + A7↔A6 boundaries hold, and how the Strategy-family-closure marker frames the 7/8 axes complete state after this inquiry?**

## Goal

- **Criterion.** 5 ordinal levels for A7 — each operationalizable as a translator-AI prompt instruction (so the AI knows the scaffolding budget per page/chapter/passage and which A1/A3 actions can fire). Per-level scaffolding-budget spec + A1/A3 action-interaction table + multi-meaning render rules are the operational substance.

- **Use case.** The user will commit `scaffolding: Literal[...]`; the per-level prose becomes part of the translator-AI's prompt context; the AI uses the per-level budget to determine which A1/A3 actions can fire and how multi-meaning preservation renders.

- **Desired outcome.** Stable 5 levels with budget specification + A1/A3 interaction table + multi-meaning render rules + A4 cross-validation + A7↔A5/A6 boundaries + Said Nursi anchoring + receptive-only non-applicability + chain default + STRATEGY-FAMILY-CLOSURE marker (3/3).

- **What would fail.**
  - 5 levels that don't specify a scaffolding budget (just names with no operational substance).
  - Missing the A7↔A1/A3 action-interaction table (the special role).
  - Multi-meaning render rules not specified per level.
  - Conflating A7 with A6 (both interact but distinct — budget vs structural preservation).
  - Failure to cross-validate against A4 matrix.
  - Said Nursi corpus not anchored per level.
  - Failure to handle the scaffolding-budget runtime conflict when A7 is too low for required A1/A3 actions.

## Source Input

```text
lets dive deep into Strategy │ A7 Scaffolding
```

## Scope Check

Question covers goal: YES.

**Specific-vs-pattern check.** "Strategy │ A7 Scaffolding" pinpoints the specific axis but the inquiry addresses the broader pattern of scaffolding across all use cases. "Dive deep" suggests thorough treatment — full spec including scaffolding budget per level, A1/A3 action-interaction table, multi-meaning render rules, all cross-axis boundaries.

**Decoupling.** Root + A1+A2+A3 + A4 + A5 + A6 commitments inherited and re-tested.

## Synthesis Trigger

This inquiry consolidates / synthesizes commitments from 5+ prior inquiry outputs:

- `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — root. Commits to: A7 plain-ordinal; 5 levels proposed; subsumes feature-activation bundle minus harmony (which became A6); multi-meaning render control role; activation gate not specified (no activation gate for A7 — it's a budget, not a policy trigger).

- `devdocs/inquiries/2026-06-06_14-59__a6_form_preservation_levels/finding.md` — A6 (immediately prior). Commits to: NEW translator-strategy 4-component template adapted from A5; receptive-only NOT APPLICABLE pattern; chain default via A4 matrix; A6↔A7 cross-validation needed.

- `devdocs/inquiries/2026-06-06_14-38__a5_source_fidelity_levels/finding.md` — A5. Commits to: NEW translator-strategy 4-component template (the original A5 template; A7 adapts); A5 modulates A1/A3 actions but doesn't have own actions; receptive-only NOT APPLICABLE.

- `devdocs/inquiries/2026-06-06_14-05__a4_purpose_categories/finding.md` — A4. Commits to: per-purpose A7 defaults (scholarly=rich; devotional=moderate; casual=rich; language-learning=MAX rich; performance=minimal); defaults-driver role.

- `devdocs/inquiries/2026-06-06_11-47__a1_cultural_reference_recognition_levels/finding.md` (+ A3) — A1 cultural-reference-recognition handling actions (INLINE-GLOSS / FOOTNOTE / DOMESTICATE / KEEP-AS-IS / EXPLICATE-FUNCTION) that interact with A7 budget. A3 cultural-handling actions (TRANSLITERATE-WITH-GLOSS / FLAG-CULTURAL-CONTEXT / BRIDGE-CULTURAL-DISTANCE etc.) similarly interact.

Inherited commitments to re-test:
- A7 plain-ordinal (root).
- A7 5-level cardinality (root).
- A7 subsumes feature-activation bundle minus harmony (root).
- A7 multi-meaning render control role (root POLICY section).
- A4 per-purpose A7 defaults (A4 matrix).
- A7 interaction with A1/A3 actions (implicit in root + A1 + A3 + A5 chain).
- NEW translator-strategy 4-component template (A5; A6 adapted; A7 adapts).
- Receptive-only NOT APPLICABLE (A4 + A5 + A6 pattern).
- Chain default via A4 matrix.
- Language-agnostic at concept level (root + chain).
- A6↔A7 cross-validation needed (A6 finding flagged).
