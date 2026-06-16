# Branch: a8_analysis_depth_levels

## Question

**Context.** The root architectural finding `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` established A8 — Analysis Depth as the SOLE axis in the Depth family of Comprehenslate's 8-axis configuration framework — and the FINAL axis in the framework. Per the root: A8's concept is "how much interpretive material the system surfaces ALONGSIDE the translation — not at the surface of the translation itself, but in separate analysis sections." It answers "How much interpretive commentary should accompany the translation?" Pattern: plain ordinal, proposed 4 levels (`surface | standard | deep | scholarly`). A8 inherits directly from the existing `DEPTH_PROFILE` knob in `.env.example` (the only Layer 1 axis with a pre-existing operational anchor in the project's prior configuration sketch).

A8 has THREE SPECIAL CHARACTERISTICS distinguishing it from the other axes:

1. **A8 is the FRAMEWORK-CLOSING axis.** After Reader 3/3 (A1+A2+A3), Purpose 1/1 (A4), Strategy 3/3 (A5+A6+A7), and Depth 1/1 (A8), the entire 8-axis user-facing framework closes. This is the only inquiry in the chain whose completion brings the framework to 8/8 axes complete. The Depth family is the smallest family (1/1) but closing it has cascading implications — the framework as a whole becomes ready for schema commit, pydantic dataclass work, and translator-AI prompt assembly.

2. **A8 PROPOSES 4 LEVELS, not 5.** Every other ordinal axis in the framework proposed (and settled) 5 levels (A1 sub-fields, A6, A7) or 4 levels (A5, which used an asymmetric 4-level range with policy embedded structurally). A8 proposes 4 levels (`surface | standard | deep | scholarly`) inherited from DEPTH_PROFILE. This cardinality choice must be substantively validated — does the 4-level granularity from DEPTH_PROFILE hold under A8's full framework context, or does the inheritance need refinement (5 levels? different labels?)?

3. **A8 lives in SEPARATE-SECTIONS apparatus channel, NOT text-surface.** The A7↔A8 boundary is the most consequential cross-axis boundary in the framework: A7 (Scaffolding) controls text-surface scaffolding (footnotes, glosses on the reading page); A8 (Analysis Depth) controls separate-sections analysis (etymology notes, rhetorical analysis, cross-references, study-aids sidebars, exegetical apparatus). A user can have rich Scaffolding with surface Analysis Depth OR minimal Scaffolding with scholarly Analysis Depth. The two are orthogonal in real reading experiences. A8's spec must make the separate-sections-vs-text-surface distinction operationally clear so the translator-AI doesn't bleed A8 content into A7's channel.

The Reader family (A1+A2+A3), Purpose family (A4), and Strategy family (A5+A6+A7) are all specified. 7/8 axes complete. **A8 closes the Depth family AND closes the entire framework at 8/8.**

The A4 finding's matrix gave per-purpose A8 defaults: scholarly=deep; devotional=standard; casual=surface; language-learning=deep+scholarly; performance=surface. The A7 finding's frontier flag for A7↔A8 cross-validation must be resolved here.

State the question:

- **Subject:** A8 — Analysis Depth level definitions.
- **Action:** Decide cardinality (validate root's 4-level proposal substantively) + level names + per-level depth specification + interaction with A4 matrix + A7↔A8 boundary resolution + DEPTH_PROFILE inheritance refinement + cross-axis cross-validation + Depth-family + framework-closure marker.
- **Level:** Axis-level (one axis, plain-ordinal per root architecture).
- **Observation targets** (multiple, preserved separately):
  1. The CARDINALITY decision (root proposed 4; validate substantively — is 4 right? does the 4-level granularity from DEPTH_PROFILE cover the spectrum or does adding a 5th level — e.g., `none` for pure-translation-no-analysis case — improve coverage?).
  2. The LEVEL NAMES (root suggested `surface | standard | deep | scholarly`; validate against project use cases and edition-tradition exemplars).
  3. The PER-LEVEL DEPTH SPECIFICATION — what KINDS of interpretive material (etymology notes / rhetorical analysis / cross-references / exegetical history / lexical-history / philological apparatus / target-language-equivalent analysis) are produced at each level, and what density/extent?
  4. The A7↔A8 BOUNDARY — resolving A7 finding's frontier flag. The boundary: A7 = text-surface scaffolding on the reading page (footnotes, glosses); A8 = separate-sections analysis (sections appended after the translation). What happens when A8 is high (extensive separate-sections analysis) — does the harmony report (A6) or in-page scaffolding (A7) move to the analysis section? When A7=scholarly + A8=surface, where does the apparatus live? When A7=off + A8=scholarly, do we have a clean translation followed by a heavy analysis section?
  5. The A4 MATRIX CROSS-VALIDATION — A4's per-purpose A8 defaults (scholarly=deep; devotional=standard; casual=surface; language-learning=deep+scholarly; performance=surface) must map to A8's level definitions.
  6. The A8 ↔ A5/A6 INTERACTIONS — A5 foreignized might want extensive A8 etymology to track source-language semantics; A6 maximum (harmony preservation) produces a harmony report that interacts with A8 high-depth analysis (do they merge? do they coexist?). Re-validate orthogonality at multiple level combinations.
  7. The TEMPLATE STRUCTURE — A5/A6/A7's translator-strategy 4-component template likely fits A8 (also translator-strategy ordinal axis), but A8's content-type emphasis (KINDS of analysis produced) may need a different 4th component.
  8. The PROJECT CORPUS — Said Nursi corpus mapping per A8 level (what kind of analysis is produced for Risale-i Nur at each level — etymology of Sufi/kalam terms? rhetorical analysis of nazm structure? cross-references to other Nursi passages? exegetical history of polysemous concepts?).
  9. The EDITION-TRADITION EXEMPLARS per level (cleanly mapping `surface` → no separate analysis; `standard` → light study notes / brief introductions; `deep` → Norton-Critical-style analysis chapters; `scholarly` → full critical apparatus + exegetical history + lexical-philological commentary).
  10. The DEPTH_PROFILE INHERITANCE refinement — the existing `.env.example` knob uses `surface | standard | deep | scholarly` strings. Are these the right labels at the Layer 1 axis level, or does A8 need to depart from the prior knob's naming?
  11. Receptive-only NOT APPLICABLE check (parallel to A4, A5, A6, A7).
  12. Default-when-A8-silent (likely chain through A4 matrix → casual default = `surface`; but is `standard` a safer baseline?).
  13. The DEPTH-FAMILY-CLOSURE marker — A8 closes the Depth family at 1/1.
  14. The FRAMEWORK-CLOSURE marker — A8 closes the entire 8-axis Layer 1 framework. 8/8 axes complete after this inquiry.
  15. The HARMONY-REPORT-LOCATION decision — A6's harmony report (which lives in apparatus at A6 Levels 3+) interacts with A8. When A8 is high, does the harmony report migrate to the A8 analysis section? When A8=surface, does the harmony report still exist as standalone apparatus?
  16. The MULTI-MEANING ANALYSIS at A8 high levels — when polysemy policy fires AND A8 is high, does A8 produce exegetical-history analysis of the polysemous concept (parallel to but distinct from A7's render mechanisms which control how senses appear in the translation)?

- **Deliverable shape:** 4 (or 5, if cardinality revises) ordinal levels with per-level depth specification + content-type-by-level table + A7↔A8 boundary spec + harmony-report-location decision + multi-meaning analysis spec + A4 cross-validation + A8↔A5/A6/A7 boundaries + template adaptation + Said Nursi corpus per level + edition-tradition exemplars + receptive-only non-applicability + chain default + DEPTH-FAMILY CLOSURE + FRAMEWORK CLOSURE markers.

**State the question:** **For A8 — Analysis Depth (the sole axis in the Depth family AND the final axis closing the entire 8-axis framework; plain-ordinal interpretive-material-depth in separate-sections apparatus; inherits from existing DEPTH_PROFILE knob in `.env.example`; orthogonal to A7's text-surface scaffolding; harmony-report-location decision needed), what should the ordinal level names be (root proposed `surface | standard | deep | scholarly` at 4 levels — validate or revise), what per-level depth specification + content-type-by-level table + A7↔A8 boundary + harmony-report-location + multi-meaning analysis spec apply, how this cross-validates with A4's per-purpose A8 defaults (scholarly=deep; devotional=standard; casual=surface; language-learning=deep+scholarly; performance=surface), how A8↔A5/A6/A7 orthogonality holds, and how the DEPTH-FAMILY-closure AND FRAMEWORK-closure markers frame the 8/8 axes complete state?**

## Goal

- **Criterion.** 4 (or revised cardinality) ordinal levels for A8 — each operationalizable as a translator-AI prompt instruction (so the AI knows what KINDS of separate-sections analysis to produce and at what density). Per-level depth specification + content-type table + A7↔A8 boundary + harmony-report-location decision are the operational substance.

- **Use case.** The user will commit `analysis_depth: Literal[...]`; the per-level prose becomes part of the translator-AI's prompt context; the AI uses the per-level spec to determine which content-types (etymology / rhetorical analysis / cross-references / exegetical history / lexical-philological apparatus) are produced and where (text-surface scaffolding vs separate-sections analysis).

- **Desired outcome.** Stable 4 (or 5) levels with depth specification + content-type table + A7↔A8 boundary + harmony-report-location + multi-meaning analysis + A4 cross-validation + A8↔A5/A6/A7 boundaries + Said Nursi anchoring + edition-tradition exemplars + receptive-only non-applicability + chain default + DEPTH-FAMILY-CLOSURE marker + FRAMEWORK-CLOSURE marker.

- **What would fail.**
  - 4 levels that don't specify content-type (just names like `surface | standard | deep | scholarly` with no per-level "what KINDS of analysis" substance).
  - Missing the A7↔A8 boundary resolution (the most consequential cross-axis boundary; A7 finding flagged this).
  - Failure to specify where harmony report (A6) lives across A8 levels.
  - Conflating A8 with A7 (both produce apparatus but in different channels — text-surface vs separate-sections).
  - Failure to cross-validate against A4 matrix.
  - Said Nursi corpus not anchored per level.
  - Edition-tradition exemplars missing per level.
  - Failure to mark DEPTH-FAMILY CLOSURE and FRAMEWORK CLOSURE.
  - DEPTH_PROFILE inheritance left unaudited (just rubber-stamping the prior knob's labels without substantive validation).

## Source Input

```text
lets dive deep into A8 — Analysis Depth in devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md

(reread it first)
```

## Scope Check

Question covers goal: YES.

**Specific-vs-pattern check.** "A8 — Analysis Depth" pinpoints the specific axis and the user's "dive deep" framing requests thorough treatment (parallel to A7). The inquiry addresses the full spec — cardinality validation + level names + per-level depth + content-type-by-level + A7↔A8 boundary + harmony-report-location + multi-meaning analysis + A4 cross-validation + all cross-axis boundaries + DEPTH-FAMILY-CLOSURE + FRAMEWORK-CLOSURE.

**Reread directive.** The user explicitly requested rereading the root finding before scoping; root finding was reread and the A8 section (lines 172-184), A4 default principle, A7↔A8 boundary, and DEPTH_PROFILE inheritance are all carried into this scoping.

**Decoupling.** Root + A1+A2+A3 + A4 + A5 + A6 + A7 commitments inherited and re-tested.

## Synthesis Trigger

This inquiry consolidates / synthesizes commitments from 6+ prior inquiry outputs:

- `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — root. Commits to: A8 plain-ordinal; 4 levels proposed (`surface | standard | deep | scholarly`); inherits from DEPTH_PROFILE knob; distinct from A7 (text-surface vs separate-sections); distinct from A4 (why-reading vs how-much-commentary); DEPTH family 1/1; closes framework at 8/8.

- `devdocs/inquiries/2026-06-07_19-07__a7_scaffolding_levels/finding.md` — A7 (immediately prior). Commits to: A7 controls text-surface scaffolding; A6↔A7 orthogonality (harmony report vs text-surface scaffolding); A7↔A8 cross-validation flagged as DEFERRED for A8 inquiry; harmony report (A6) location across A8 levels is open question; multi-meaning render rules (A7's role) distinct from multi-meaning analysis (potential A8 role).

- `devdocs/inquiries/2026-06-06_14-59__a6_form_preservation_levels/finding.md` — A6. Commits to: harmony report at A6 Levels 3+ as separate apparatus channel; Tier 1-4 system from harmony_layer.md; A6↔A7 / A6↔A8 boundaries.

- `devdocs/inquiries/2026-06-06_14-38__a5_source_fidelity_levels/finding.md` — A5. Commits to: NEW translator-strategy 4-component template; A5 modulates A1/A3 actions; receptive-only NOT APPLICABLE.

- `devdocs/inquiries/2026-06-06_14-05__a4_purpose_categories/finding.md` — A4. Commits to: per-purpose A8 defaults (scholarly=deep; devotional=standard; casual=surface; language-learning=deep+scholarly; performance=surface); defaults-driver role.

- A2 + A3 + A1 — Reader family commitments inherited (A8 doesn't directly interact with Reader axes the way A7 does via the action-permission table, but reader's competence still informs A8 default).

Inherited commitments to re-test:
- A8 plain-ordinal (root).
- A8 4-level cardinality proposed (root) — substantively validate.
- A8 inherits from DEPTH_PROFILE knob (root).
- A8 distinct from A7 (text-surface vs separate-sections) (root).
- A8 distinct from A4 (why-reading vs how-much-commentary) (root).
- A4 per-purpose A8 defaults (A4 matrix).
- A7↔A8 cross-validation needed (A7 finding flagged as DEFERRED).
- Harmony report location across A8 levels (A7 finding tentative answer: A6 harmony report can live either in A8's analysis section or as standalone apparatus; A7 in-page scaffolding stays in-page regardless of A8 — to be confirmed in A8 inquiry).
- NEW translator-strategy 4-component template (A5+A6+A7; A8 adapts).
- Receptive-only NOT APPLICABLE (A4+A5+A6+A7 pattern).
- Chain default via A4 matrix.
- Language-agnostic at concept level (root + chain).
- DEPTH family 1/1 closing.
- Framework closing at 8/8.
