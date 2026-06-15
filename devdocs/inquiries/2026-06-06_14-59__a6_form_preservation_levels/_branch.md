# Branch: a6_form_preservation_levels

## Question

**Context.** The root architectural finding `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` established A6 — Form Preservation as the second axis in the Strategy family (after A5 Source Fidelity). Per the root: A6's concept is "the strength of structural preservation — rhythm, parallelism, ring composition, word order as meaning carrier (the project corpus's central insight: nazm / arrangement IS meaning, not decoration)"; it answers "Should structural elements like rhythm and parallelism survive the crossing into the target language?" Pattern: plain ordinal, proposed 5 levels. The root explicitly ties A6 levels to the **Tier 1-4 system in `harmony_layer.md`**: at the lowest level the translation ignores harmony entirely; at the highest level it preserves all four tiers including the Tier 3 entries with PRESERVE-WHEN clauses.

The root also documented A6's special role: **A6 IS THE ACTIVATION GATE FOR THE NAZM POLICY.** Per the root's POLICY layer section: "When A6 is at 'light' or higher, the always-on policy of nazm / form-as-meaning preservation activates. The axis level is the activation gate; the policy itself is the operational rule." This means A6's level definitions directly determine whether the nazm-form-as-meaning policy fires for a given translation job.

The project's `harmony_layer.md` provides the substantive Tier 1-4 system A6 ties to:
- **Tier 1** (13 entries — Non-Negotiable): meaning IS carried by this harmony — implied question-answer flow; cause-effect chaining; conditional chain logic; hidden syllogism; reciprocal proof; semantic escalation/de-escalation; tense consistency + deliberate shifts; person/voice threading + iltifat; emotional arc continuity; convergence structure (havuz); antonym pairing; ellipsis patterns; general-to-specific / specific-to-general flow.
- **Tier 2** (12 entries — High Priority): grammatical parallelism; sentence-type alternation; pronoun chain continuity; clause-length patterning; evidence-claim rhythm; concession-rebuttal rhythm; lexical field continuity; ring composition; chiastic structure; thematic bracketing; anticipation-fulfillment; addressee consistency.
- **Tier 3** (13 entries — Context-Dependent): register consistency; synonym chaining; isotopy; callback / forward-reference; direct/indirect speech alternation; performative continuity; strophic patterning; parallel panel structure; density matching; merismus; particle threading; sentence-length rhythm. Each has PRESERVE-WHEN / SACRIFICE-WHEN clauses.
- **Tier 4** (11 entries — Low Priority): phonetic echo; internal rhyme/assonance; consonant threading; rhythmic cadence; root echo; phonetic weight; maqta' harmony; opening/closing word patterns; genre convention; formulaic echoes.

The Reader family (A1+A2+A3), Purpose family (A4), and the first Strategy axis A5 are now fully specified. 5/8 axes complete. A6 is the second Strategy axis.

**A6 differs from A5 in two structurally important ways:**

1. **A6 is directly tied to a substantive content artifact** (harmony_layer.md's Tier 1-4 system) rather than a translation-theory abstraction. The level definitions should map operationally to tier preservation.

2. **A6 has a SPECIAL ROLE as ACTIVATION GATE** for the nazm-as-meaning POLICY. Per the root, when A6 ≥ "light" the policy activates. This makes A6 the second axis (after A4) that has special-role status beyond just being a configuration value.

The A4 finding's matrix gave per-purpose A6 defaults: scholarly=high; devotional=high (preserve rhythm/form); casual=moderate; language-learning=high (preserve structure for pedagogy); performance=MAXIMUM (cadence preservation; rhythm=meaning per harmony_layer commitment).

State the question:

- **Subject:** A6 — Form Preservation level definitions (5 ordinal levels per root proposal).
- **Action:** Decide cardinality + level names + activation-gate threshold + per-level tier-coverage mapping + cross-axis validation.
- **Level:** Axis-level (one axis, plain-ordinal per root).
- **Observation targets** (multiple, preserved separately):
  1. The CARDINALITY decision (root proposed 5; validate substantively against the Tier 1-4 system + a "preserve nothing" level + a "preserve everything including Tier 4" level).
  2. The LEVEL NAMES (root suggested off / light / moderate / high / maximum implicitly; validate against project use cases).
  3. The TIER-COVERAGE MAPPING per level (which tiers does each level preserve? — the operational substance).
  4. The ACTIVATION-GATE threshold (root said "when A6 is at 'light' or higher, nazm policy activates"). Confirm which level is the activation threshold.
  5. The TEMPLATE STRUCTURE — A1-A3 capacity-graded doesn't fit (A6 is translator-strategy not reader-property); A4 categorical doesn't fit (A6 is ordinal); A5's translator-strategy template likely fits (A6 is also translator-strategy ordinal).
  6. The A6↔A5 BOUNDARY — lexical surface (A5) vs structural form (A6); root's four-corners orthogonality; re-validate.
  7. The A6↔A4 per-purpose defaults cross-validation against A4 matrix.
  8. The PROJECT POLICY interaction — A6 ACTIVATES nazm policy at threshold; A6 doesn't override the policy. Distinct from A5 where policy was EMBEDDED structurally.
  9. The PROJECT CORPUS — Said Nursi's nazm is foundational to the project (the harmony_layer.md was written for it). Said Nursi anchor per level needed.
  10. Receptive-only NOT APPLICABLE check (parallel to A4, A5).
  11. Default-when-A6-silent decision (likely chain through A4 matrix like A5).
  12. The TIER 3 PRESERVE-WHEN/SACRIFICE-WHEN clauses — these are RUNTIME determinations (does this source use the feature structurally?), not configurable. How do A6 levels interact with the Tier 3 conditional logic?

- **Deliverable shape:** 5 ordinal levels with per-level concept + tier-coverage mapping + activation-gate threshold marked + template adaptation + A6↔A5/A6↔A4 boundary statements + Said Nursi corpus mapping + receptive-only non-applicability + chain default + Strategy-family progress marker (2/3).

**State the question:** **For A6 — Form Preservation (the second axis in the Strategy family; plain-ordinal structural preservation tied directly to the project's harmony_layer.md Tier 1-4 system; activation gate for the nazm-as-meaning POLICY at the "light" threshold per root commitment), what should the 5 ordinal level names be, what per-level tier-coverage mapping (which of Tier 1, 2, 3, 4 each level preserves), where the activation-gate threshold sits, how this cross-validates with A4's per-purpose A6 defaults, how Tier 3's PRESERVE-WHEN/SACRIFICE-WHEN runtime conditionality interacts with A6 levels, and how the A5/A6 orthogonality holds — with Said Nursi corpus anchored at each level and the NEW translator-strategy 4-component template from A5 adapted?**

## Goal

- **Criterion.** 5 ordinal levels for A6 — each operationalizable as a translator-AI prompt instruction (so the AI knows which harmony_layer tiers to preserve at this level). Per-level tier-coverage mapping must be explicit. Activation-gate threshold must be marked. Tier 3 conditional logic must be specified.

- **Use case.** The user will commit `form_preservation: Literal[...]`; the per-level prose becomes part of the translator-AI's prompt context; the AI uses the per-level tier-coverage to determine which harmony features to preserve when translating.

- **Desired outcome.** Stable 5 levels with tier-coverage + activation-gate + Tier 3 conditional handling + A6↔A5/A6↔A4 boundaries + Said Nursi anchoring + receptive-only non-applicability + chain default + Strategy-family-progress marker (2/3).

- **What would fail.**
  - 5 levels that don't map cleanly to the harmony_layer.md Tier 1-4 structure.
  - Activation-gate threshold ambiguous (root committed to "light or higher").
  - Tier 3 PRESERVE-WHEN/SACRIFICE-WHEN logic ignored (Tier 3 is conditional, not flat).
  - Conflating A6 with A5 Source Fidelity (structural vs lexical).
  - Failure to cross-validate against A4 matrix.
  - Said Nursi corpus not anchored per level (the harmony_layer was written for Nursi; the project's central use case).

## Source Input

```text
now lets do it for a6 form preservation
```

## Scope Check

Question covers goal: YES.

**Specific-vs-pattern check.** Broader pattern of A6 across all corpora (not Nursi-only). But the harmony_layer.md Tier 1-4 system IS the substantive content A6 ties to; the inquiry takes that as foundational.

**Decoupling.** Root + A1+A2+A3 + A4 + A5 commitments inherited and re-tested.

## Synthesis Trigger

This inquiry consolidates / synthesizes commitments from 4+ prior inquiry outputs:

- `devdocs/inquiries/2026-06-05_14-14__translation_config_axes/finding.md` — root. Commits to: A6 plain-ordinal; 5 levels proposed; ties to harmony_layer.md Tier 1-4; activation-gate role for nazm policy; A5↔A6 orthogonality (lexical vs structural).

- `devdocs/inquiries/2026-06-06_14-38__a5_source_fidelity_levels/finding.md` — A5 (immediately prior). Commits to: NEW translator-strategy 4-component template; receptive-only NOT APPLICABLE pattern; chain default via A4 matrix; A5↔A6 orthogonality re-validated; Strategy-family-opens marker.

- `devdocs/inquiries/2026-06-06_14-05__a4_purpose_categories/finding.md` — A4. Commits to: per-purpose A6 defaults (scholarly=high; devotional=high; casual=moderate; language-learning=high; performance=MAXIMUM); categorical pattern; defaults-driver role.

- `devdocs/inquiries/2026-06-06_11-47__a1_cultural_reference_recognition_levels/finding.md` (and A3) — DOMESTICATE-disfavored policy lineage (informs A6 indirectly; A6 doesn't override policies).

- **`harmony_layer.md`** — the substantive content artifact A6 ties to. Tier 1-4 system with 49 entries total. Tier 3 entries have PRESERVE-WHEN/SACRIFICE-WHEN clauses.

Inherited commitments to re-test:
- A6 plain-ordinal (root).
- A6 5-level cardinality (root proposed; validate against tier system + edge levels).
- A6 ties to harmony_layer.md Tier 1-4 (root).
- A6 activation-gate for nazm policy at "light" threshold (root).
- A6↔A5 orthogonality (root + A5).
- A4 per-purpose A6 defaults (A4 matrix).
- NEW translator-strategy 4-component template (A5).
- Receptive-only NOT APPLICABLE (A4 + A5 pattern).
- Chain default via A4 matrix (A5 pattern).
- Language-agnostic at concept level (root + chain).
