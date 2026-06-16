# Sensemaking — a4_purpose_categories

## User Input
`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-06_14-05__a4_purpose_categories/_branch.md` (with surfacing output at `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-06_14-05__a4_purpose_categories/surfacing.md`)

---

## SV1 — Baseline Understanding

Define ~5 categorical purposes for A4 (the fourth axis, sole axis in the Purpose family). A4 is structurally DIFFERENT from prior 3 inquiries: CATEGORICAL not ordinal; DEFAULTS-DRIVER for other 7 axes (2-tier default principle first tier). Decide cardinality, category names, per-purpose × per-axis default matrix, categorical template structure, multi-purpose handling, default-when-A4-silent, A4↔A2/A3/A8 boundaries, Purpose-family closure marker. Re-test 6 inherited commitments for A4 applicability.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints
- **C1** ~5 categorical (NOT ordinal) levels (root commitment + must validate substantively).
- **C2** Defaults-driver role for other 7 axes per 2-tier default principle.
- **C3** Skopos / Vermeer / Reiss anchored (root commitment).
- **C4** Operationalizable as translator-AI prompt context.
- **C5** Distinct from A1, A2, A3, A8 (boundaries explicit).
- **C6** Categorical pattern means each category is qualitatively distinct (no "more X than Y" ordering).
- **C7** Multi-purpose question must be settled (single-default or multi-config).
- **C8** Default-when-A4-silent must be settled (categorical has no natural "lower").
- **C9** Project corpus (Said Nursi) use cases (scholarly + devotional + casual + language-learning + performance) all present and need handling.

### Key Insights

- **KI1** Cardinality = 5 on substantive grounds. Reiss's 3-type framework (informative / expressive / operative) is theoretically clean but too coarse for translation-config purposes — it groups devotional, performance, and casual under "expressive" / "operative" without distinguishing their concrete translator-AI strategy implications. Newmark's 4-type extends Reiss but still misses language-learning as its own use-case (he treats it as pedagogical-special-case). 5 categories — scholarly / devotional / casual / language-learning / performance — cover the project's Said Nursi use cases AND map to Skopos-pragmatic translation strategy buckets that produce distinct per-axis default profiles. Going to 6+ adds complexity without coverage gain (sub-cases like liturgical / comparative / reference fold into the 5 cleanly).

- **KI2** Category names validated. Root's `scholarly / devotional / casual / language-learning / performance` are: (a) project-meaningful (Said Nursi corpus uses all 5); (b) Skopos-tradition-aligned (Vermeer's pragmatic categories); (c) AI-prompt-clear (each name conveys the reader-action). Alternatives like `study / worship / leisure / pedagogical / recitation` don't add semantic value and lose the AI-prompt-clarity. Alternatives like `academic / liturgical / general / instructional / oral` are less project-meaningful.

- **KI3** Categorical pattern confirmed. Three independent tests all pass: semantic test ("what is this translation FOR?" asks for a category not a degree); lexical test ("more scholarly than devotional" doesn't make sense); root's orthogonality test (a scholar can want a casual-feel translation; a casual reader can want deep analysis). Reiss (3-type) and Newmark (4-type) precedents are also categorical.

- **KI4** Per-purpose × per-axis default matrix is A4's CENTRAL DELIVERABLE. The root finding's 2-tier default principle says: when the user sets A4 Purpose, that value drives sensible defaults for the other 7 axes. This makes A4 the SPECIAL axis. The matrix must be SPECIFIC — for each of 5 purposes, for each of 7 other axes (A1 with 5 sub-fields, A2, A3, A5, A6, A7, A8), what value does this purpose default to? Per surfacing R5, the 5 default profiles are workable working hypotheses:

  | Purpose | A1 Reader Level | A2 Domain Expertise | A3 Source Culture | A5 Source Fidelity | A6 Form Preservation | A7 Scaffolding | A8 Analysis Depth |
  |---|---|---|---|---|---|---|---|
  | scholarly | advanced+ | educated+ | any (often outsider-with-study) | foreignized | high | rich | deep/scholarly |
  | devotional | conversational+ | aware-to-educated | source-native/heritage typical | foreignized (preserve liturgical form) | high (preserve rhythm/form) | moderate | standard |
  | casual | daily-to-conversational | lay-to-aware | outsider-to-acquainted | balanced | moderate | rich (help unfamiliar) | surface |
  | language-learning | mid (matched to learner) | lay | outsider | balanced-to-foreignized (source transparency) | high (preserve structure for pedagogy) | MAX rich | standard |
  | performance | conversational+ | any | any | balanced (poetic accessibility) | MAXIMUM (preserve cadence; rhythm=meaning per harmony_layer) | minimal (clean text for delivery) | surface |

- **KI5** Multi-purpose handling = single-purpose default + runtime-blending. Real multi-purpose cases exist (scholarly+devotional academic-spiritual-formation; casual+language-learning popular-textbook; performance+devotional Quran recitation). RESOLUTION: A4 is single-valued (one PRIMARY purpose per translation job); when the user needs multi-purpose blend, they pick the primary purpose AND set secondary axes manually (e.g., scholar wanting devotional access sets A4=devotional but A8=deep manually). Multi-purpose configuration (`purpose: list[Literal[...]]`) is richer but adds complexity; deferred to future inquiry if multi-purpose cases become primary.

- **KI6** Default-when-A4-silent = `casual`. Substantive grounds: (a) casual is the most-common case (broadest reader spectrum); (b) lowest assumption about reader effort / commitment (parallel to A1+A2+A3's conservative-bias-LOWER); (c) the casual-purpose defaults for other axes (balanced + rich-scaffolding + surface-depth) produce the safest fallback for unconfigured cases. Adding a "general" 6th category is unnecessary; `casual` covers it semantically. Requiring explicit A4 setting violates root's "specify only what you care about" principle.

- **KI7** Categorical template structure. The 4-component capacity-graded template (reader profile + frequency/canonicity/expertise-depth tier + register-tier + handling-test) doesn't fit categorical A4 — purposes don't have tiers. NEW categorical template with 4 components matching A4's structure:
  1. **Use-case profile** — what the reader will DO with the translation (replaces reader profile; reader-action-oriented)
  2. **Strategic implications** — how this purpose shapes translation strategy choices (replaces tier-component; purpose-driven-strategy)
  3. **Per-axis default mappings** — what this purpose defaults to for each of the other 7 axes (replaces register-tier with the matrix entry)
  4. **DOMESTICATE-policy emphasis** — per-purpose foreignization-emphasis (replaces handling-test; project-policy-emphasis per category)

- **KI8** DOMESTICATE-disfavored policy CARRIES THROUGH A4 (cross-cutting). The policy applies to ALL purposes; per-purpose foreignization EMPHASIS varies but the policy itself is invariant. Devotional has MAXIMUM foreignization (preserve liturgical specificity); scholarly has high foreignization (source-fidelity for study); language-learning has high foreignization (source-transparency for learner); casual has balanced (uses foreignization-preserving alternatives like EXPLICATE-FUNCTION + INLINE-GLOSS instead of DOMESTICATE); performance has balanced (poetic accessibility but preserve cadence). DOMESTICATE-CULTURAL-FRAME remains disfavored across all categories.

- **KI9** Inherited commitments re-test:
  - **Receptive-only** (A1-A3 chain): DOES NOT APPLY directly. A4 is USER decision (configuration), not reader-property; receptive vs productive doesn't apply. Note this explicitly.
  - **Conservative-bias-LOWER** (A1-A3 chain): REFORMULATED for categorical. "Default-when-A4-silent = casual" is the categorical equivalent (safest assumption about reader effort).
  - **Single-X default** (A2-A3 pattern): APPLIES as single-purpose default. Multi-purpose deferred.
  - **4-component template** (A1-A3 chain): REPLACED with new categorical template (KI7).
  - **Translator-AI runtime determination** (A2-A3): APPLIES. A4 is purely user-config; AI receives the purpose + applies per-axis defaults + adjusts strategy emphasis.
  - **DOMESTICATE-disfavored** (A1→A3 chain): APPLIES cross-cutting across all A4 categories; per-purpose foreignization emphasis varies.

- **KI10** A4↔A2 boundary: A4 = WHY (purpose); A2 = HOW MUCH KNOWN (expertise). Independence: specialist reading for casual purpose; lay reading for scholarly purpose. Already documented in A2 finding.

- **KI11** A4↔A3 boundary: A4 = WHY; A3 = WHO (cultural identity). Independence: source-native reading for casual; outsider reading for scholarly. Already in A3 finding.

- **KI12** A4↔A8 boundary: A4 = WHY (purpose); A8 = HOW MUCH COMMENTARY (analysis depth). Independence: scholar may want LOW depth (clean text); casual may want HIGH depth (need help). A4 sets DEFAULT for A8 (scholarly → deep; casual → surface) but user can override.

- **KI13** Purpose family closure. A4 is the sole axis in the Purpose family per root. After this inquiry: Reader family CLOSED (3/3 axes) + Purpose family CLOSED (1/1 axis) = 4/8 axes complete. Remaining: Strategy family (A5/A6/A7) + Depth family (A8).

- **KI14** Said Nursi corpus comprehensively covered by 5 purposes:
  - Scholarly: academic Islamic-studies research on Nursi
  - Devotional: Risale-i Nur as spiritual-practice text; dersane study circle
  - Casual: general curious reader; convert exploring
  - Language-learning: Turkish learners using Nursi
  - Performance: Nursi recitation (some passages are oratorical)

### Structural Points
- **SP1** 5 categorical purposes (decided).
- **SP2** Labels `scholarly | devotional | casual | language-learning | performance` (validated).
- **SP3** Categorical pattern (NOT ordinal). Each category qualitatively distinct.
- **SP4** New 4-component categorical template (use-case profile + strategic implications + per-axis default mappings + DOMESTICATE-policy emphasis).
- **SP5** Per-purpose × per-axis default matrix (5 purposes × 7 axes = 35-cell matrix).
- **SP6** Single-purpose default; multi-purpose at future inquiry.
- **SP7** Default-when-A4-silent = `casual`.
- **SP8** DOMESTICATE-disfavored policy carries through; per-purpose foreignization emphasis varies.
- **SP9** A4↔A2 / A4↔A3 / A4↔A8 boundaries documented.
- **SP10** Purpose-family closure marker (A4 sole axis; closes family alone).

### Foundational Principles
- **FP1** Categorical pattern (not ordinal).
- **FP2** A4 is configuration-only (not reader-property; receptive-only doesn't apply).
- **FP3** A4 is defaults-driver for other 7 axes (root's 2-tier default principle first tier).
- **FP4** Default-when-A4-silent = `casual` (categorical equivalent of conservative-bias-LOWER).
- **FP5** Single-purpose configuration; multi-purpose deferred.
- **FP6** Foreignization-preserving (DOMESTICATE-disfavored) carries through all A4 categories; per-purpose emphasis varies.
- **FP7** Language-agnostic at concept level; purposes meaningful across cultures.

### Meaning-Nodes
- **MN1** Purpose — the use-case driving translation strategy.
- **MN2** Use-case profile — what the reader DOES with the translation.
- **MN3** Strategic implications — how the purpose shapes translation choices.
- **MN4** Per-axis defaults — A4's special role as defaults-driver.
- **MN5** Reader-action — the cognitive/practical action the reader performs.

### Meta-Inspection after SV2 (hooks H4, H5)
- **H4 (concept names):** "categorical template" structurally distinct from 4-component capacity-graded template; "per-axis default mappings" is the operational matrix; "use-case profile" parallels reader profile.
- **H5 (motivating examples):** 5 categories × 5 Said Nursi use cases = 25 example clusters; cross-corpus illustration (Bible / Quran / philosophy / classics) prevents lock-in.

### SV2 — Anchor-Informed Understanding

After anchor extraction:
- 5 categorical purposes (`scholarly | devotional | casual | language-learning | performance`) validated on substantive grounds (Skopos + Said Nursi + project use cases).
- Categorical pattern confirmed (3 independent tests pass).
- NEW categorical template with 4 components matching A4's structure.
- Per-purpose × per-axis default matrix (5 × 7) is the central operational deliverable.
- Single-purpose default; multi-purpose deferred.
- Default-when-A4-silent = `casual`.
- DOMESTICATE-disfavored policy carries through.
- 6 inherited commitments re-tested for A4 applicability with explicit verdicts.
- A4↔A2/A3/A8 boundaries clean.
- Purpose family closes with A4 (sole axis).

---

## Phase 2 — Perspective Checking

### Technical / Logical
- **T1** 5 purposes mutually distinct.
- **T2** Categorical pattern verifiable by lexical + semantic tests.
- **T3** Per-axis default matrix is a deterministic function (purpose → 7 default values).
- **T4** Single-purpose decision unambiguous (one value per `purpose` field).

### Human / User
- **U1** User is translator; cares about AI applying right defaults per purpose.
- **U2** Project corpus Said Nursi uses all 5 purposes; user explicitly cares about devotional + scholarly + language-learning.
- **U3** User wants the "specify only what you care about" principle preserved — A4 default + per-axis defaults reduces config burden.
- **U4** Multi-purpose corner cases handled by manual per-axis override; not a primary use case.

### Strategic / Long-term
- **S1** A4 once committed completes Purpose family (1/1). After this inquiry: 4/8 axes spec'd.
- **S2** Next: Strategy family (A5, A6, A7) and Depth family (A8). A5/A6/A7 each interact with A4's per-purpose defaults — those defaults will need to be re-checked when those axes are defined.
- **S3** Per-purpose default matrix is forward-looking: when A5/A6/A7/A8 inquiries finish, the matrix should be re-validated.

### Risk / Failure
- **R1** Sneaking ordinality into categorical. CORRECTIVE: explicit categorical-pattern statement + tests.
- **R2** Per-purpose × per-axis matrix incomplete. CORRECTIVE: 35-cell matrix made explicit in finding.
- **R3** Multi-purpose cases left unhandled. CORRECTIVE: explicit single-purpose-default decision; manual per-axis override path.
- **R4** Default-when-A4-silent ambiguous. CORRECTIVE: `casual` explicit.
- **R5** Conflating A4 with A8 Analysis Depth. CORRECTIVE: A4 sets DEFAULT for A8 but doesn't subsume it.
- **R6** DOMESTICATE-policy override at scholarly purpose. CORRECTIVE: cross-cutting policy; per-purpose emphasis varies but policy carries.
- **R7** Categorical template confusion with prior 4-component template. CORRECTIVE: new template components explicit + named.

### Resource / Feasibility
- **Re1** 5 purposes operational.
- **Re2** Per-purpose × per-axis matrix is finite (35 cells); operationally manageable.
- **Re3** Categorical template structure is feasible.

### Definitional / Internal Consistency
- Interpretation consistent with root + A1+A2+A3 chain.
- A4 categorical (vs A1-A3 ordinal) — different pattern but consistent within root framework.
- DOMESTICATE-disfavored policy extends consistently.

### Definitional / Frame-exit Completeness (GATING)
- (i) Inherited terms from prior findings: YES (6 commitments).
- (ii) Used across ≥2 distinct values: YES (5 purposes × 7 axes; 3 cross-axis boundaries).
- Gating FIRES.

1. **Existence Enumeration.** What does "purpose" refer to project-wide?
   - TYPE axis: use-case categories (scholarly / devotional / casual / language-learning / performance).
   - LAYER axis: A4 is Layer 1 (user-facing); affects Layer 3 SOURCE-DESCRIPTION not (purpose is user-side not source-side).
   - PHASE axis: not relevant.
   - AGENT axis: user-side property (A4 is configuration).
   - TIME axis: not relevant.
   - STRUCTURAL ROLE axis: A4 is defaults-driver (special role).
   - IN-SCOPE: user's chosen purpose for this translation job + per-purpose default matrix.
   - OUT-OF-SCOPE: source text's intended purpose (source-side; Layer 3); multi-purpose simultaneous (deferred); time-varying purpose (snapshot).

2. **Role Assessment.** Source's intended purpose → Layer 3 SOURCE-DESCRIPTION; A4 is reader-side. Operation coherent.

3. **Verdict Rigor.** "Single-purpose default":
   - Counter: multi-purpose configuration (purpose: list[Literal[...]]).
   - Why fails: most jobs have ONE primary purpose; runtime axis-override handles edge cases; multi-purpose list adds complexity without operational benefit at this layer.
   - HOLDS at HIGH confidence.

4. **Residual / Coverage Justification.** None — sufficient coverage.

### Phase / Calibration-State
- No calibration dependency. Deterministic per-purpose default rules.

### Ethical / Systemic
- Sneaking ordinality (treating scholarly as "higher" than casual) would be classist. CORRECTIVE: categorical pattern explicit.
- Per-purpose defaults must not be culturally biased (e.g., devotional ≠ Christian-only). CORRECTIVE: cross-cultural illustration in finding.

### Meta-Inspection after SV3 (H1, H2, H3, H7)
- H1 (candidate set): 5 categories — validated.
- H2 (frame scope): Frame-exit handled.
- H3 (question framing): explicit.
- H7 (phase/calibration): no calibration dependency.

### SV3 — Multi-Perspective Understanding

Confirms:
- 5 categorical purposes with labels validated.
- New 4-component categorical template structure.
- Per-purpose × per-axis 5 × 7 default matrix as central deliverable.
- Single-purpose default; multi-purpose at future inquiry.
- Default-when-A4-silent = `casual`.
- DOMESTICATE-disfavored cross-cutting; per-purpose foreignization emphasis varies.
- 6 inherited commitments re-tested with explicit verdicts (1 doesn't apply; 5 apply with reformulations).
- A4↔A2/A3/A8 boundaries documented.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity A1: Cardinality (5 vs 3 vs 6+)
Substantive grounds for 5?

**Counter:** Reiss 3-type is the standard; 5 over-stratifies.

**Why fails:** Reiss 3-type groups devotional, performance, and casual under "expressive" / "operative" without distinguishing translator-AI strategy implications. Newmark 4-type extends but still misses language-learning. 5 maps to project's Said Nursi corpus + produces 5 distinct per-axis default profiles. 6+ adds complexity without coverage (sub-cases fold into 5).

**Confidence:** HIGH
**Resolution:** 5 categorical purposes. Labels `scholarly | devotional | casual | language-learning | performance`.

### Ambiguity A2: Categorical vs ordinal
**Counter:** Maybe purposes are ordinal (casual to scholarly on engagement-intensity).
**Why fails:** 3 tests fail for ordinal (semantic / lexical / orthogonality counter-examples per root). Categorical confirmed.
**Confidence:** HIGH
**Resolution:** Categorical (not ordinal). Each purpose qualitatively distinct.

### Ambiguity A3: Categorical template
**Counter:** Keep 4-component template (reader profile + tier + register + handling-test) for structural parity.
**Why fails:** Purposes don't have tiers. Forcing the template stretches each component beyond semantic fit.
**Confidence:** HIGH
**Resolution:** NEW 4-component categorical template: (1) Use-case profile, (2) Strategic implications, (3) Per-axis default mappings, (4) DOMESTICATE-policy emphasis. Preserves 4-component COUNT for parity but ADAPTS components to A4's categorical nature.

### Ambiguity A4: Per-purpose × per-axis matrix scope
**Counter:** Just A1, A2, A6, A7, A8 — skip A3, A5 since they're orthogonal.
**Why fails:** Per-purpose defaults include A5 (Source Fidelity) explicitly per root; A3 (Source Culture) has per-purpose defaults too (devotional → source-native typical reader). Full 7-axis matrix.
**Confidence:** HIGH
**Resolution:** Full 5 × 7 matrix (35 cells). Each cell is the DEFAULT value the purpose suggests; user can override per-axis.

### Ambiguity A5: Multi-purpose handling
**Counter:** Multi-purpose configuration (`purpose: list[Literal[...]]`) for richer expressiveness.
**Why fails:** Most jobs have ONE primary purpose; runtime axis-override handles edge cases without multi-purpose list. Multi-purpose list adds complexity without proportional benefit.
**Confidence:** HIGH
**Resolution:** Single-purpose default (`purpose: Literal[...]`). Multi-purpose cases handled by picking primary purpose + manual override of secondary axes. Multi-purpose explicit config deferred to future inquiry.

### Ambiguity A6: Default-when-A4-silent
**Counter:** Require explicit A4 setting.
**Why fails:** Violates root's "specify only what you care about" principle. Most users will want sensible defaults.
**Confidence:** HIGH
**Resolution:** `casual` is default-when-A4-silent. Substantive grounds: lowest-engagement assumption; broadest reader spectrum; matches categorical equivalent of conservative-bias-LOWER.

### Ambiguity A7: DOMESTICATE-policy per-purpose interaction
**Counter:** A4 = scholarly should permit DOMESTICATE for pedagogical clarity.
**Why fails:** Project policy is cross-cutting (carries through ALL purposes per A1 chain). Foreignization-preserving alternatives handle pedagogical-clarity needs (INLINE-GLOSS / EXPLICATE-FUNCTION). DOMESTICATE remains last-resort across all A4 categories.
**Confidence:** HIGH
**Resolution:** DOMESTICATE-disfavored carries through all A4. Per-purpose foreignization EMPHASIS varies (devotional max; casual balanced) but policy invariant.

### Ambiguity A8: Inherited receptive-only applicability
**Counter:** Receptive-only must apply to A4 for parity.
**Why fails:** A4 is USER CONFIGURATION not reader-property. Receptive vs productive is about what the READER does with content; A4 captures the USER's choice. Different ontological category. Receptive-only doesn't apply.
**Confidence:** HIGH
**Resolution:** Receptive-only DOES NOT APPLY to A4. Explicit non-inheritance documented.

### Meta-Inspection (Load-bearing concept test + Specific-vs-pattern)
- "Categorical template" — tested A3.
- "Per-axis default matrix" — tested A4.
- "Single-purpose default" — tested A5.
- "Default-when-A4-silent = casual" — tested A6.
- Specific-vs-pattern: 5 × 5 example clusters (5 purposes × 5 corpus examples) illustrate broader pattern.

### SV4 — Clarified Understanding

After ambiguity collapse:
- 5 categorical purposes `scholarly | devotional | casual | language-learning | performance` (cardinality + names settled).
- Categorical pattern (3 tests pass).
- NEW 4-component categorical template (use-case profile + strategic implications + per-axis defaults + DOMESTICATE-emphasis).
- Full 5 × 7 per-purpose × per-axis default matrix.
- Single-purpose default; multi-purpose deferred.
- Default-when-A4-silent = `casual`.
- DOMESTICATE-disfavored cross-cutting; per-purpose emphasis varies.
- Receptive-only DOES NOT APPLY to A4 (configuration not reader-property).
- 5 of 6 inherited commitments apply with reformulations; 1 (receptive-only) does not apply.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Variables fixed
- **VF1** 5 categorical purposes with labels.
- **VF2** Categorical pattern.
- **VF3** NEW 4-component categorical template.
- **VF4** Full 5 × 7 default matrix.
- **VF5** Single-purpose default.
- **VF6** Default-when-A4-silent = `casual`.
- **VF7** DOMESTICATE-disfavored cross-cutting.
- **VF8** Receptive-only DOES NOT APPLY.
- **VF9** A4↔A2/A3/A8 boundaries documented.
- **VF10** Purpose-family closure marker.

### Options eliminated
- **OE1** Ordinal pattern for A4.
- **OE2** 3-type or 6+ cardinality.
- **OE3** Capacity-graded 4-component template forced.
- **OE4** Multi-purpose configuration (list) at this layer.
- **OE5** Requiring explicit A4 setting.
- **OE6** DOMESTICATE-permitted at scholarly.
- **OE7** Receptive-only applied to A4.

### Viable paths
- **VP1** 5 per-category prose with new 4-component template.
- **VP2** Per-purpose × per-axis 5 × 7 default matrix as a table.
- **VP3** Said Nursi corpus mapping per purpose.
- **VP4** A4↔A2/A3/A8 boundary section.
- **VP5** Purpose-family closure marker.
- **VP6** Inherited commitments re-test (with explicit non-applicability for receptive-only).

### SV5 — Constrained Understanding

Solution space organized:
1. 5 per-category definitions with new 4-component template.
2. Per-purpose × per-axis 5 × 7 default matrix.
3. Said Nursi corpus mapping per purpose.
4. A4↔A2/A3/A8 boundary statements.
5. Multi-purpose decision + default-when-A4-silent decision + receptive-only non-applicability all documented.
6. Purpose-family closure marker.
7. Inherited Commitments Re-test (with explicit non-inheritance flag for receptive-only).

---

## Phase 5 — Conceptual Stabilization

**A4 — Purpose** = 5 categorical purposes (`scholarly | devotional | casual | language-learning | performance`) of what the translation is FOR. Categorical pattern (not ordinal). Defaults-driver role: A4's value drives sensible defaults for the other 7 axes (root's 2-tier default principle first tier). NEW 4-component categorical template (use-case profile + strategic implications + per-axis default mappings + DOMESTICATE-policy emphasis). Full 5 × 7 default matrix. Single-purpose default; multi-purpose at future inquiry. Default-when-A4-silent = `casual`. DOMESTICATE-disfavored policy carries through all categories; per-purpose foreignization emphasis varies. Receptive-only DOES NOT APPLY (A4 is configuration not reader-property). A4↔A2/A3/A8 boundaries explicit. Closes Purpose family (A4 sole axis).

### Meta-Inspection (Accommodation trigger check)
Did perspectives force model patching? NO — perspectives enriched. 8 ambiguities settled HIGH. Not premature stabilization.

### SV6 — Stabilized Model

A4 — Purpose stabilized:
- 5 categorical purposes: `scholarly | devotional | casual | language-learning | performance`
- Categorical pattern (not ordinal); each purpose qualitatively distinct
- Defaults-driver role per root's 2-tier default principle
- NEW 4-component categorical template (use-case profile + strategic implications + per-axis default mappings + DOMESTICATE-policy emphasis)
- Full 5 × 7 per-purpose × per-axis default matrix
- Single-purpose default; multi-purpose at future inquiry
- Default-when-A4-silent = `casual`
- DOMESTICATE-disfavored cross-cutting (per-purpose emphasis varies)
- Receptive-only DOES NOT APPLY (configuration not reader-property)
- A4↔A2/A3/A8 boundaries documented
- Said Nursi corpus mapped across all 5 purposes
- Purpose-family closure (1/1 axis)

**Difference from SV1:** Major. (1) Cardinality + categorical pattern validated substantively. (2) Categorical template structurally new. (3) Per-axis 5 × 7 default matrix is the central deliverable. (4) Single-purpose default. (5) `casual` default-when-silent. (6) Cross-cutting DOMESTICATE policy. (7) Explicit non-inheritance of receptive-only. (8) 6 inherited commitments re-tested with explicit applicability verdicts.

---

## Saturation Indicators

- **Perspective saturation:** 8 perspectives; APPROACHING.
- **Ambiguity resolution:** 8/8 at HIGH; 0 OPEN.
- **SV delta:** SV1→SV6 major.
- **Anchor diversity:** Constraints (9), Key Insights (14), Structural Points (10), Foundational Principles (7), Meaning-Nodes (5). DIVERSE.

**Saturation: HIGH. PROCEED.**

## Inherited Commitments Re-tested

| # | Commitment | Source | Re-test verdict |
|---|---|---|---|
| IC1 | A4 categorical pattern | root | RE-TESTED OK — 3 tests pass |
| IC2 | A4 defaults-driver role | root | RE-TESTED OK — central deliverable (5×7 matrix) |
| IC3 | A4 ~5 cardinality | root | RE-TESTED & CONFIRMED at 5 on substantive grounds |
| IC4 | Skopos / Reiss anchor | root | RE-TESTED — 5 categories extend Reiss 3-type with substantive justification |
| IC5 | A4↔A2 / A3 / A8 boundaries | root + A2 + A3 | RE-TESTED & DOCUMENTED |
| IC6 | Receptive-only (A1-A3 chain) | A1-A3 chain | NOT APPLICABLE TO A4 — A4 is config not reader-property |
| IC7 | Conservative-bias-LOWER (A1-A3 chain) | A1-A3 chain | RE-TESTED & REFORMULATED — categorical equivalent is `casual` default-when-silent |
| IC8 | Single-X default (A2-A3 pattern) | A2 + A3 | RE-TESTED & APPLIED — single-purpose default |
| IC9 | 4-component template adapts (A1-A3 chain) | A1-A3 chain | RE-TESTED & ADAPTED — NEW categorical template (4 components but different composition) |
| IC10 | DOMESTICATE-disfavored policy | A1 → A3 chain | RE-TESTED & CARRIES THROUGH — cross-cutting; per-purpose emphasis varies |
| IC11 | Translator-AI runtime determination | A2 + A3 | RE-TESTED OK — A4 is user-config; AI receives + applies defaults |
| IC12 | Language-agnostic at concept level | root + chain | RE-TESTED OK — purposes meaningful across cultures |
| IC13 | 5 categorical purposes with names `scholarly | devotional | casual | language-learning | performance` | NEW | NEW commitment; validated against Skopos + Said Nursi |
| IC14 | Full 5 × 7 per-purpose × per-axis default matrix | NEW | NEW commitment |
| IC15 | Default-when-A4-silent = `casual` | NEW | NEW commitment |
| IC16 | NEW 4-component categorical template | NEW | NEW commitment |
| IC17 | Single-purpose default + manual override path | NEW | NEW commitment |
| IC18 | Purpose-family closure (A4 sole axis) | NEW (closure marker) | NEW commitment |

## Frontier Flags for Decomposition / Critique

- **FF1** Multi-purpose configuration (`purpose: list[Literal[...]]`) for richer cases — future inquiry.
- **FF2** Per-axis default matrix forward-looking: when A5/A6/A7/A8 inquiries complete, re-validate the matrix entries.
- **FF3** Time-varying purpose (user changes purpose mid-translation) — snapshot assumption.
- **FF4** Source-side intended purpose (Layer 3 SOURCE-DESCRIPTION) — out of A4 scope; future inquiry.
