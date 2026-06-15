# Branch: a4_purpose_categories

## Question

**Context.** The root architectural finding `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` established A4 — Purpose as the fourth axis (and the only axis in the Purpose family) in Comprehenslate's 8-axis configuration framework. Per the root: A4's concept is "what the translation is FOR — the use-case"; it answers "Why is this translation being made? What will the reader do with it?"; this is the axis Skopos theory (Vermeer / Reiss) treats as the primary determinant of translation strategy. The root proposed ~5 categorical levels (scholarly study / devotional reading / casual reading / language learning / performance) but explicitly deferred level-value finalization to "the next inquiry."

The Reader family is now fully specified: A1 Reader Level (5 sub-fields × 5 levels each, completed in the A1 chain), A2 Domain Expertise (5 levels `lay | aware | educated | trained | expert`, completed in `a2_domain_expertise_levels/finding.md`), and A3 Source Culture (5 levels `outsider | acquainted | familiar | heritage | source-native`, completed in `a3_source_culture_levels/finding.md`).

A4 differs STRUCTURALLY from A1, A2, A3 in two foundational ways:

1. **A4 is CATEGORICAL, not ordinal.** Purpose categories like `devotional`, `performance`, `language-learning` are qualitatively distinct use-cases — they do not lie on a single intensity scale. A casual-to-scholarly ordering looks plausible but breaks on real cases (a scholarly reader may want a casual-feel translation for relaxation; a casual reader may want deep analysis for a passage they're stuck on). This is the root finding's own argument for categorical pattern.

2. **A4 drives DEFAULTS for other axes.** Per the root's 2-tier default principle: when the user sets A4 Purpose, that value drives sensible defaults for the other axes (a scholarly Purpose pulls Analysis Depth toward "deep"; a casual Purpose pulls Scaffolding toward "rich" for unfamiliar readers; etc.). This makes A4 the SPECIAL axis — it's not just one of 8 dials; it's the one that, once set, configures the others.

The 4-component template (reader profile + tier-component + register-component + handling-test) used for A1, A2, A3 may not apply directly. A4's purposes aren't capacity-graded; they don't have "tiers." Each purpose is its own distinct use-case with its own strategic implications.

State the question:

- **Subject:** A4 — Purpose level definitions (categorical, not ordinal).
- **Action:** Decide the categorical levels (proposed ~5: scholarly / devotional / casual / language-learning / performance — to be validated and possibly refined); define each category's concept + use-case profile + strategic implications + per-purpose defaults for other axes (the 2-tier default principle's first tier).
- **Level:** Axis-level (one axis, categorical pattern per the root architecture).
- **Observation targets** (multiple, preserved separately):
  1. The CARDINALITY decision (~5 per root proposal; substantive validation needed).
  2. The CATEGORY NAMES (proposed: scholarly / devotional / casual / language-learning / performance — should each be validated against Skopos text-typology + project use cases).
  3. The CONCEPT each category captures (what use-case profile each purpose embodies; what the reader will DO with the translation).
  4. The STRATEGIC IMPLICATIONS of each purpose (how this purpose shapes translation strategy choices — e.g., scholarly preserves more form; devotional preserves register and rhythm for liturgical use; performance preserves cadence for recitation).
  5. The PER-PURPOSE DEFAULTS for other axes (the 2-tier default principle's first tier — which value of A1 each purpose pulls toward; which A2; which A3; which A5 Source Fidelity; which A6 Form Preservation; which A7 Scaffolding; which A8 Analysis Depth).
  6. The CATEGORICAL TEMPLATE — does the 4-component template adapt or does A4 need a new template structure? Purposes don't have tiers; they have use-cases + strategic implications + defaults-driven.
  7. The Skopos theory anchor — Vermeer / Reiss text-typology (informative / expressive / operative). How does the 5-purpose proposal map to or diverge from Skopos's 3-type framework? Why 5 categories not 3?
  8. The PROJECT CORPUS anchor — Said Nursi corpus has clear devotional, scholarly, and language-learning use cases. How does the 5-purpose framework handle Said Nursi specifically?
  9. The MULTI-PURPOSE question — can a translation job have MULTIPLE purposes simultaneously (e.g., scholarly + devotional)? Or must it pick one? Parallel to A2/A3's single-X-default question.
  10. The CONSERVATIVE-BIAS question — A4 doesn't naturally have a "lower default" since the purposes are qualitatively different. What's the right default-when-user-hasn't-specified principle for A4? The root's conservative-bias-fallback for OTHER axes works when A4 is silent; but what should the CATEGORY default be when the user doesn't set A4?
  11. The TRANSLATOR-AI RUNTIME determination — A4 is user-configurable (not AI-runtime-inferred); the AI receives the purpose and adjusts. Confirm this delineation.
  12. The A4↔A2 boundary — A4 (purpose) vs A2 (expertise). Already noted in the root + A2 finding (specialist reader for casual purpose; lay reader for scholarly purpose). Re-document.
  13. The A4↔A3 boundary — A4 (purpose) vs A3 (cultural identity). Already noted in A3 finding (devotional source-native vs casual outsider). Re-document.
  14. The A4↔A8 BOUNDARY — A4 Purpose and A8 Analysis Depth interact heavily but are distinct per root (Purpose answers "why are you reading?"; Analysis Depth answers "how much interpretive material accompanies the translation?"). A scholar may want LOW Analysis Depth for a particular use; a casual reader may want HIGH Analysis Depth. Re-document.

- **Deliverable shape:** ~5 named categorical levels (validated cardinality) with per-category definition + use-case profile + strategic implications + per-purpose defaults for the other 7 axes; A4 definition template (adapted from A1+A2+A3 if applicable, or new categorical template); explicit A4↔A2, A4↔A3, A4↔A8 boundary statements; Skopos-theory anchor + project-corpus anchor; multi-purpose decision; default-when-A4-is-silent decision; Reader-family-already-closed acknowledgment + Purpose-family-now-closes-with-this-finding marker.

**State the question:** **For A4 — Purpose (the fourth axis in the configuration framework, the only axis in the Purpose family, structurally categorical and structurally special as the defaults-driver for other axes per root architectural finding), what should the categorical levels be (~5 per root proposal: scholarly / devotional / casual / language-learning / performance, validated on substantive grounds), what concept does each category capture (what the reader will DO with the translation), what strategic implications follow from each (how does this purpose shape translation choices), and what per-purpose defaults does each set for the OTHER 7 axes (the 2-tier default principle's first tier) — anchored to Skopos text-typology (Vermeer / Reiss) and the project's Said Nursi corpus, with explicit A4↔A2 / A4↔A3 / A4↔A8 boundaries, multi-purpose decision, default-when-A4-is-silent decision, and Purpose-family-closure marker?**

## Goal

- **Criterion.** N (~5) mutually distinct, qualitatively-different, spectrum-covering categorical purposes — each operationalizable as a translator-AI prompt instruction (so the AI knows the use-case and adjusts strategy + defaults accordingly). Each category needs explicit definition + strategic implications + per-purpose default mappings to other axes. The CATEGORICAL pattern (not ordinal) must be preserved per root commitment.

- **Use case.** The user will commit these as the `purpose: Literal[...]` enum values; the per-category prose becomes part of the translator-AI's prompt context; the per-purpose defaults populate the other axes when the user sets only A4.

- **Desired outcome.** A stable, named, defined set of ~5 A4 Purpose categories with definition + strategic implications + per-purpose × per-other-axis default matrix; A4↔A2 + A4↔A3 + A4↔A8 boundary statements; multi-purpose decision; default-when-A4-silent decision; Skopos + Said Nursi anchors; Purpose-family closure (A4 is the sole axis in the Purpose family).

- **What would fail.**
  - Treating A4 as ordinal (forcing a casual-to-scholarly scale that doesn't work — explicitly rejected by root).
  - Categories defined only by example without explicit use-case profile and strategic implications.
  - Categories that overlap in use-case profile.
  - Categories that aren't qualitatively distinct (just different intensities of the same use-case).
  - Missing the per-purpose × per-other-axis default matrix (the 2-tier default principle's first tier requires this).
  - Failure to map to/diverge from Skopos text-typology with explicit justification.
  - Failure to validate against the project's Said Nursi corpus.
  - Failure to address the multi-purpose question.
  - Failure to address the default-when-A4-silent question.
  - Failure to address the A4↔A2 / A4↔A3 / A4↔A8 boundaries.
  - Conflating A4 with A8 Analysis Depth (a scholar may want LOW depth; a casual reader may want HIGH).
  - Categories that lock to one religious tradition or one source culture.
  - Mixing the categorical pattern with sneaked-in ordinal stratification.

## Source Input

```text
now lets do it for a4 purpose
```

## Scope Check

Question covers goal: YES.

The Question targets the categorical-cardinality decision + category names + per-category concepts + strategic implications + per-purpose × per-other-axis default matrix + Skopos anchor + Said Nursi anchor + multi-purpose decision + default-when-A4-silent + A4↔A2/A3/A8 boundaries + Purpose-family closure marker. The Goal asks for all of those plus operationalizability and structural-pattern discipline (categorical not ordinal).

**Specific-vs-pattern check.** User said "now lets do it for a4 purpose" — apply the broader pattern of "define the levels for this axis" to A4. Scope is the broader pattern of A4 Purpose across multiple use-case profiles (not just one project corpus's use case).

**Cardinality + categorical pattern.** The user did not specify cardinality; the root proposed ~5 with categorical pattern. This inquiry validates both substantively and refines if needed.

**Decoupling from prior chain commitments.** The root finding's A4 commitments (categorical pattern; defaults-driver role; proposed ~5 categories) are inherited and re-tested. The A1+A2+A3 chain commitments (4-component template adapts as needed; receptive-only; conservative-bias-LOWER; DOMESTICATE-disfavored policy) are inherited but their APPLICABILITY to A4 needs explicit assessment — A4 is categorical not ordinal, so several inherited principles may need rethinking.

**Template-adaptation in scope.** Whether the 4-component template applies to A4 is a substantial open question. A4's categorical pattern likely needs a DIFFERENT template structure (e.g., use-case profile + strategic implications + default-mappings) rather than the capacity-graded template the ordinal axes used.

## Synthesis Trigger

This inquiry consolidates / synthesizes commitments from at least 2 prior inquiry outputs (triggers Synthesis Trigger):

- `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — root architectural finding. Commits to: A4's concept (purpose / use-case); A4's CATEGORICAL pattern (NOT ordinal); A4's special role as DEFAULTS-DRIVER for other axes (2-tier default principle first tier); ~5 categorical levels proposed; Skopos / Vermeer / Reiss anchor; A4 boundary vs A2 / A3 / A8.

- `devdocs/inquiries/2026-06-06_13-33__a3_source_culture_levels/finding.md` — the most recent sibling inquiry closing the Reader family. Commits to: receptive-only (re-test applicability to A4 — A4 is a USER decision not a reader property; receptive-only may not apply the same way); conservative-bias-LOWER (re-test applicability — A4 is categorical so "lower" doesn't apply directly); single-X default (parallel to single-purpose question); DOMESTICATE-disfavored policy (interacts with A4 since A4 = scholarly may permit different domestication choices than A4 = casual); 4-component template adapts MEDIUM (re-test applicability — A4's categorical pattern may need different template).

- `devdocs/inquiries/2026-06-06_12-37__a2_domain_expertise_levels/finding.md` — A2 inquiry that established the runtime-determination mechanism + single-domain default + 4-category handling action structure. Relevant for A4 because A4↔A2 interaction is explicit per root.

Inherited commitments to re-test (non-exhaustive):
- A4 categorical pattern (root).
- A4 defaults-driver role (root).
- A4 ~5 cardinality (root, proposed).
- Skopos / Vermeer / Reiss text-typology anchor (root).
- A4 boundary vs A2, A3, A8 (root + sibling findings).
- Receptive-only (A1+A2+A3 chain) — applicability to A4 needs assessment (A4 is user-config not reader-property).
- Conservative-bias-LOWER (A1+A2+A3 chain) — applicability to categorical A4 needs different formulation.
- Single-X default (A2+A3 pattern) — parallel single-purpose question for A4.
- DOMESTICATE-disfavored policy (A1 cultural-reference-recognition extended through A3) — interaction with A4 categories needs explicit handling.
- 4-component template adapts as needed (A1+A2+A3 chain) — applicability to categorical A4 needs assessment (likely needs different template).
- Translator-AI runtime determination (A2+A3 chain) — A4 is user-config; AI receives and adjusts.

Sensemaking will adjudicate these commitments; Critique will re-test the adjudication.
