# Sensemaking — a7_scaffolding_levels

## User Input
`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-07_19-07__a7_scaffolding_levels/_branch.md` (with surfacing output)

---

## SV1 — Baseline Understanding

Define 5 ordinal levels for A7 — Scaffolding (third and final Strategy axis; plain-ordinal explanatory-material-budget at text surface). A7 has two special characteristics: (1) it's the scaffolding budget A1/A3 actions consume; (2) it controls multi-meaning render when polysemy policy fires. Decide per-level budget specification + A1/A3 action permission table + multi-meaning render rules + runtime conflict resolution + A4 cross-validation + cross-axis boundaries + Said Nursi per level + chain default + Strategy-family-closure marker.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints
- **C1** Plain-ordinal pattern (root).
- **C2** 5-level cardinality (root proposed; A4 matrix-implied; level-naming chain natural).
- **C3** Subsumes feature-activation bundle minus harmony (root): footnote toggle + transliteration toggle + parenthetical glosses + brief in-line explanations.
- **C4** Multi-meaning render control role when polysemy policy activates (root POLICY section).
- **C5** A4 per-purpose A7 defaults committed (A4 matrix).
- **C6** A1/A3 action vocabularies established (A1: 5 actions; A3: 10 actions in 4 categories) — A7 interacts.
- **C7** A5↔A6↔A7 orthogonality preserved (root + A6 finding).

### Key Insights

- **KI1** Cardinality = 5 confirmed. The off / minimal / standard / rich / scholarly spectrum maps cleanly to natural use cases: utility translation (off); pop-translation (minimal); standard scholarly edition (standard); Norton-Critical-style (rich); SBL/Brill apparatus-edition (scholarly). The A4 matrix uses 4 distinct A7 levels (minimal, moderate, rich, MAX rich) plus the implicit performance-permits-zero indicating 5+ levels needed. Going to 4 merges minimal+standard or rich+scholarly; loses operational distinction (Norton Critical vs SBL Greek NT are operationally different editions). Going to 6+ over-stratifies.

- **KI2** Labels `off | minimal | standard | rich | scholarly` validated. These names map directly to edition-tradition exemplars and are operationally clear to translator-AI prompt context. Alternative naming (`none / low / standard / high / max`) loses the apparatus-edition signal at "scholarly". Root proposal stands.

- **KI3** Per-level scaffolding budget specification has TWO complementary components:
  1. **Qualitative budget** — the verbal threshold ("rich" = extensive footnotes per page; "minimal" = sparse footnotes only for hardest references; etc.) — matches root's terminology.
  2. **Per-page operational guidance** — concrete unit AI can monitor (e.g., off = 0 footnotes per page; minimal = 0-1 per page; standard = 1-3 per page; rich = 3-6 per page; scholarly = 6+ per page including endnote/appendix references). These are NOT hard caps but orientation thresholds.
  
  The combination (qualitative orientation + per-page guidance) is operationally useful: gives the AI prompt-clear qualitative stance plus a sanity-check budget.

- **KI4** A1/A3 action permission table per level. The OPERATIONAL SUBSTANCE of A7 — specifying which A1/A3 actions can fire at each A7 level:

  | A7 Level | A1 budget-consuming actions | A3 budget-consuming actions |
  |---|---|---|
  | `off` | INLINE-GLOSS BLOCKED; FOOTNOTE BLOCKED | TRANSLITERATE-WITH-GLOSS BLOCKED (use TRANSLITERATE-FULLY); FLAG-CULTURAL-CONTEXT BLOCKED; BRIDGE-CULTURAL-DISTANCE BLOCKED |
  | `minimal` | INLINE-GLOSS sparingly (1-2 per page for hardest); FOOTNOTE rare | TRANSLITERATE-WITH-GLOSS first-use only; FLAG-CULTURAL-CONTEXT sparingly; BRIDGE-CULTURAL-DISTANCE BLOCKED |
  | `standard` | INLINE-GLOSS moderately (3-5 per page); FOOTNOTE for context | TRANSLITERATE-WITH-GLOSS routine; FLAG-CULTURAL-CONTEXT routine; BRIDGE-CULTURAL-DISTANCE moderate |
  | `rich` | INLINE-GLOSS routine + extensive; FOOTNOTE extensive | TRANSLITERATE-WITH-GLOSS + FLAG-CULTURAL-CONTEXT routine; BRIDGE-CULTURAL-DISTANCE extensive |
  | `scholarly` | All actions fire freely + full apparatus (introduction + glossary + endnotes) | All A3 budget-consuming actions fire freely + full apparatus |
  
  Budget-FREE actions (KEEP-AS-IS / EXPLICATE-FUNCTION / DOMESTICATE / ASSUME-SHARED / KEEP-HONORIFICS-SOURCE / PRESERVE-CULTURAL-SPECIFICITY / TARGET-LANGUAGE-EQUIVALENT / ANGLICIZE-HONORIFICS / DOMESTICATE-CULTURAL-FRAME) are available at all A7 levels (subject to A5 policy bias).

- **KI5** Multi-meaning render rules per level. Surfacing identified 6 render mechanisms; map to levels:

  | A7 Level | Multi-meaning render mechanism |
  |---|---|
  | `off` | PRIMARY-ONLY render forced — BUT this would VIOLATE multi-meaning policy. RESOLUTION: A7=off + polysemy policy fires → AI uses EXPLICATE-FUNCTION (paraphrase combining senses without bracket scaffolding); harmony report flags the constraint. The policy itself is preserved (multiple senses noted) but the render is forced into the body without scaffolding. |
  | `minimal` | PRIMARY + MINIMAL FOOTNOTE NOTING OTHER SENSES — primary in body; brief footnote like "also: judgment / religion / truth". 1 footnote per polysemous-passage. |
  | `standard` | INLINE PARENTHETICAL PAIRED — both senses inline with brackets: "din [judgment / religion]" or "judgment (also religion / truth)". Used for high-load polysemous passages. |
  | `rich` | INLINE PAIRED WITHOUT BRACKETS or FULL FOOTNOTE PAIRED — both senses fully integrated into body where syntactically possible ("the day of judgment, of religion, of truth"); FULL FOOTNOTE PAIRED for cases requiring explanation. |
  | `scholarly` | APPARATUS-EDITION RENDER — body + full footnote + scholarly apparatus citing exegetical/linguistic literature on the polysemy + glossary entry. |

  **A7=off + polysemy policy interaction is the resolution-via-EXPLICATE-FUNCTION case.** The policy says preserve multiple senses; A7=off blocks scaffolding-render. EXPLICATE-FUNCTION (a budget-free action) provides the preservation by paraphrasing rather than bracketing.

- **KI6** Runtime conflict resolution (A7 too low for required A1/A3 actions). The cleanest resolution: AI falls back to budget-FREE actions and flags the trade-off in the harmony report (or translator's note at scholarly+ levels). Alternative — UX-layer surface-at-config-time — is also valuable but is a UX inquiry concern (deferred).

  Specifically:
  - A7=off + reader who would need INLINE-GLOSS (e.g., A1=very_basic + foreignized A5): AI uses EXPLICATE-FUNCTION (budget-free) and flags in harmony report that source-cultural specificity is preserved via paraphrase rather than gloss.
  - A7=off + DOMESTICATE-disfavored project policy + lay reader: AI may need to settle for compromise — EXPLICATE-FUNCTION when possible; PARAPHRASE-IN-LAYMAN-TERMS as last resort (still respects policy at lower priority than scaffolding).

- **KI7** A4 matrix cross-validation with refinement note (parallel to A6 finding's refinement note):

  | A4 Purpose | A4 matrix A7 default | A7 5-level mapping |
  |---|---|---|
  | scholarly | rich | `rich` |
  | devotional | moderate | `standard` (A4 "moderate" → A7 `standard`) |
  | casual | rich (help unfamiliar) | `rich` |
  | language-learning | MAX rich | `scholarly` (parallel-text edition with full apparatus) |
  | performance | minimal | `minimal` |
  
  A4 finding refinement note: A4 used informal "moderate" / "MAX rich" verbiage; A7 uses precise `off | minimal | standard | rich | scholarly` labels. Propagate at next A4 maintenance pass: "moderate" → `standard`; "MAX rich" → `scholarly`.

- **KI8** A7 ↔ A5 / A6 / A8 orthogonality re-confirmed:
  - **A5↔A7:** A5 = strategic stance modulating A1/A3 action SELECTION; A7 = budget constraining the BUDGET that some of those actions consume. Distinct mechanisms. A5=foreignized + A7=off forces AI to use scaffolding-free foreignization-preserving alternatives (EXPLICATE-FUNCTION over INLINE-GLOSS).
  - **A6↔A7:** A6 = which harmony_layer tiers are preserved (and produces a harmony REPORT as separate apparatus at Levels 3+); A7 = text-surface scaffolding (footnotes etc on the reading page). Both A6 harmony report and A7 footnotes are separate apparatus channels; orthogonal.
  - **A7↔A8 (forthcoming):** A7 = text-surface scaffolding; A8 = separate-sections analysis depth. Distinct surfaces (per root explicit). Will be re-validated when A8 inquiry runs.

- **KI9** NEW A7-adapted 4-component template (parallels A5/A6 with A7-specific composition):
  1. **Scaffolding stance description** — what the AI does at this level (how much explanatory material on the reading page)
  2. **Per-level budget specification** — qualitative + per-page operational guidance
  3. **A1/A3 action permission table reference + multi-meaning render rule** — the operational substance
  4. **Cross-axis interaction note** — A4 matrix match + A5/A6 orthogonality reminders + A8 forthcoming-validation note

- **KI10** Default-when-A7-silent = chain through A4 matrix. When A4 silent → A4 = casual → A7 = `rich` (per A4 matrix; casual reader needs help unfamiliar). Final default = `rich`. (Interesting: A7's default is HIGHER than A6's default `light`. This reflects casual-reader-needs-help dynamic — even casual readers benefit from rich scaffolding.)

  Note: this is a non-obvious choice. The user might expect "casual" to default to LOW scaffolding (no apparatus). But the A4 matrix's casual A7 = "rich (help unfamiliar)" reflects the project's commitment to accessibility for outsider/uninitiated readers. The default is RICH so casual readers get the help they need.

- **KI11** Receptive-only NOT APPLICABLE (parallel to A4, A5, A6). A7 is translator-strategy / user-configuration / scaffolding-budget — not a reader-property. Explicit non-inheritance.

- **KI12** Said Nursi corpus per A7 level (with edition-tradition exemplars):
  - A7=off: oral recitation passage (performance-purpose); clean text only.
  - A7=minimal: pop-translation general-audience Risale-i Nur paperback; sparse footnotes for hardest references; first-use transliteration gloss only ("Bediuzzaman (wonder of the age)").
  - A7=standard: standard scholarly Risale-i Nur edition (devotional default per A4); moderate footnotes; inline glosses for Sufi/kalam terms first use; multi-meaning footnotes for major polysemous concepts.
  - A7=rich: Norton-Critical-style Risale-i Nur edition (scholarly/casual default per A4); extensive footnotes per page; inline glosses; appendix-light; inline parentheticals for polysemy.
  - A7=scholarly: full scholarly apparatus edition (language-learning default per A4); extensive footnotes + endnotes + introduction + glossary + appendix + critical apparatus + exegetical history of major polysemous terms.

- **KI13** A7 closes the Strategy family at 3/3. After this inquiry: 7/8 axes complete (Reader 3/3 + Purpose 1/1 + Strategy 3/3). Only A8 Analysis Depth remains (Depth family).

### Structural Points
- **SP1** 5 ordinal levels `off | minimal | standard | rich | scholarly`.
- **SP2** Per-level scaffolding budget: qualitative + per-page operational guidance.
- **SP3** A1/A3 action permission table per level (the operational substance).
- **SP4** 5 multi-meaning render rules per level (with A7=off → EXPLICATE-FUNCTION fallback).
- **SP5** NEW A7-adapted 4-component template.
- **SP6** Runtime conflict resolution: fallback to budget-FREE actions + flag in harmony report (UX-layer surface-at-config-time deferred to future UX inquiry).
- **SP7** Default `rich` via A4 chain (casual → A4 matrix's "rich help unfamiliar").
- **SP8** A4 finding refinement note (naming alignment).
- **SP9** A5↔A7 / A6↔A7 / A7↔A8 orthogonality preserved.
- **SP10** Receptive-only NOT APPLICABLE.
- **SP11** Strategy-family-closure marker (3/3).

### Foundational Principles
- **FP1** Plain-ordinal pattern.
- **FP2** Budget for scaffolding-consuming A1/A3 actions.
- **FP3** Multi-meaning render control role (polysemy policy interaction).
- **FP4** Translator-strategy (receptive-only NOT APPLICABLE).
- **FP5** Subsumes feature-activation bundle minus harmony.
- **FP6** Chain-inherits A4 matrix defaults.
- **FP7** Language-agnostic at concept level.
- **FP8** Runtime conflict resolution by fallback + harmony-report flagging.

### Meaning-Nodes
- **MN1** Scaffolding budget — explanatory material allotted at text surface.
- **MN2** Action permission — which A1/A3 budget-consuming actions can fire.
- **MN3** Render mechanism — how multi-meaning preservation appears at text surface.
- **MN4** Edition tradition — concrete exemplar per level for AI prompt context.

### Meta-Inspection after SV2 (H4, H5)
- **H4 (concept names):** "Scaffolding budget" distinguishes A7's role from A1/A3 vocabularies. "Multi-meaning render rule" maps cleanly to surfacing's 6 mechanisms. Labels `off | minimal | standard | rich | scholarly` map to edition-tradition exemplars.
- **H5 (motivating examples):** Edition exemplars per level (Penguin Classics / NIV+study / Norton Critical / Robert Alter / SBL Greek NT) + Said Nursi per level provide cross-cultural anchoring.

### SV2 — Anchor-Informed Understanding

5 levels `off | minimal | standard | rich | scholarly` with per-level scaffolding budget (qualitative + per-page operational guidance); A1/A3 action permission table per level; 5 multi-meaning render rules per level (with A7=off → EXPLICATE-FUNCTION fallback); NEW A7-adapted 4-component template; runtime conflict resolution by fallback + harmony-report flagging; default `rich` via A4 chain; A4 refinement note; cross-axis orthogonality preserved; receptive-only NOT APPLICABLE; Strategy-family-closure (3/3).

---

## Phase 2 — Perspective Checking

### Technical / Logical
5 levels ordinally distinct. A1/A3 action permission deterministic per level. Multi-meaning render rules per level deterministic. Runtime conflict resolution mechanical (fallback to budget-FREE; flag in harmony report).

### Human / User
User wants nuanced control over scaffolding. Project default `rich` reflects casual-reader-needs-help dynamic. Said Nursi project: typical use case is `rich` (casual) or `standard` (devotional) per A4 defaults.

### Strategic / Long-term
After A7: Strategy 3/3; Strategy family CLOSED. A7↔A8 boundary forward-looking — to be re-validated when A8 inquiry runs.

### Risk / Failure
- R1: A7=off conflicts with foreignization-preferring A5 and lay reader. CORRECTIVE: fallback to EXPLICATE-FUNCTION + harmony-report flag.
- R2: Multi-meaning render at A7=off violates polysemy policy. CORRECTIVE: A7=off + polysemy → EXPLICATE-FUNCTION (paraphrase combining senses).
- R3: A4 matrix naming mismatch. CORRECTIVE: A4 finding refinement note.
- R4: A6/A7 conflation. CORRECTIVE: explicit boundary (harmony report vs text-surface scaffolding; both apparatus channels separate).

### Resource / Feasibility
Action permission table operational. Per-page budget guidance feasible. Multi-meaning render rules feasible.

### Definitional / Internal Consistency
Interpretation consistent with root + A1-A6 chain.

### Definitional / Frame-exit Completeness (GATING)
- (i) Inherited terms: YES.
- (ii) Used across ≥2 values: YES.
- Gating FIRES.

1. **Existence:** "Scaffolding" project-wide → text-surface explanatory material (footnotes / glosses / transliterations). LAYER: A7 is Layer 1 user-facing + Layer 2 POLICY interaction (multi-meaning render control). AGENT: user-side configuration.
2. **Role:** Out-of-scope: A6 harmony report (separate apparatus); A8 separate-sections analysis (separate surface); source-text intended scaffolding (Layer 3). KEEP OUT.
3. **Verdict Rigor:** "Default `rich` via A4 chain" verdict:
   - Counter: default should be `standard` for safer baseline.
   - Why fails: A4 matrix's casual A7 = "rich (help unfamiliar)" is the project's commitment to accessibility for outsider readers. Default `rich` reflects the casual-reader-needs-help dynamic and follows the established chain pattern.
   - HOLDS at HIGH.
4. **Residual:** None.

### Phase / Calibration-State
No calibration dependency.

### Ethical / Systemic
Rich scaffolding for casual readers reflects ethical commitment to accessibility. Counter: over-scaffolding can be patronizing. Mitigation: rich is moderate not maximum; scholarly is the maximum.

### SV3 — Multi-Perspective Understanding

Confirms 5 levels with per-level budget + action permission + render rules + runtime conflict resolution + chain default + cross-axis boundaries. Frame-exit handled. Ethical considerations addressed.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity A1: Cardinality (5 vs 4 vs 6)
**Counter (4):** Merge minimal+standard or rich+scholarly.
**Why fails:** Norton Critical (rich) vs SBL Greek NT (scholarly) are operationally different editions. A4 matrix uses 4 distinct levels + performance-implicit-zero = 5 distinct level values.
**Confidence:** HIGH
**Resolution:** 5 levels. Labels `off | minimal | standard | rich | scholarly`.

### Ambiguity A2: Default-when-A7-silent (`rich` vs `standard`)
**Counter:** Default `standard` for safer baseline.
**Why fails:** A4 matrix's casual A7 = "rich (help unfamiliar)" is project's accessibility commitment. Chain pattern (A4 silent → casual → A7 = rich) settles.
**Confidence:** HIGH
**Resolution:** Default `rich`.

### Ambiguity A3: A7=off + multi-meaning policy render
**Counter:** A7=off forces PRIMARY-ONLY render, violating polysemy policy.
**Why fails:** Policy says preserve multiple senses; A7=off blocks scaffolding-render. Resolution: EXPLICATE-FUNCTION (budget-free action) provides preservation by paraphrasing rather than bracketing — both senses fit into the body text without scaffolding.
**Confidence:** HIGH
**Resolution:** A7=off + polysemy → EXPLICATE-FUNCTION fallback (budget-free preservation via paraphrase); harmony report flags.

### Ambiguity A4: A1/A3 action permission strictness at A7=off
**Counter:** A7=off should permit some minimal scaffolding for cases the AI deems essential.
**Why fails:** This makes A7=off operationally similar to A7=minimal; loses distinction. Strict: A7=off blocks all budget-consuming actions. AI falls back to budget-FREE actions; flags in harmony report.
**Confidence:** HIGH
**Resolution:** Strict A7=off blocks all budget-consuming actions; AI falls back; flags.

### Ambiguity A5: Per-page budget vs qualitative budget
**Counter:** Use only qualitative.
**Why fails:** Per-page guidance gives AI sanity-check; qualitative alone is too loose.
**Counter:** Use only per-page hard caps.
**Why fails:** Hard caps over-constrain; some passages legitimately need more.
**Confidence:** HIGH
**Resolution:** Qualitative orientation + per-page operational guidance (NOT hard caps; orientation thresholds).

### Ambiguity A6: A4 finding refinement note
**Counter:** Leave A4 verbiage as-is.
**Why fails:** Schema commit needs consistency (parallel to A6 finding refinement note).
**Confidence:** HIGH
**Resolution:** A4 finding refinement note for naming alignment.

### Ambiguity A7: Receptive-only applicability
**Counter:** Maintain parity with A1-A3.
**Why fails:** A7 is translator-strategy not reader-property (parallel to A4, A5, A6).
**Confidence:** HIGH
**Resolution:** NOT APPLICABLE.

### Ambiguity A8: Runtime conflict resolution mechanism
**Counter:** Budget-exceed for must-haves (AI can exceed scaffolding budget for must-have references).
**Why fails:** Defeats budget purpose; A7 becomes advisory not operational.
**Counter:** UX-layer surface conflict at config time (warn user "A7=off + foreignized A5 may produce uncomfortable text").
**Why partially fails:** UX-layer is valuable but is a UX inquiry concern. For A7 axis spec, the runtime resolution must be deterministic.
**Counter:** Strict budget; fallback to budget-FREE; flag in harmony report.
**Why succeeds:** Deterministic; preserves A7 axis semantics; UX-layer can be added later without changing A7 spec.
**Confidence:** HIGH
**Resolution:** Strict budget + fallback to budget-FREE actions + harmony-report flag at A6 levels 3+. UX-layer surface-at-config-time deferred to future UX inquiry.

### Ambiguity A9: Multi-meaning render granularity
**Counter:** Use only 2 render mechanisms (footnote vs inline).
**Why fails:** Loses operational distinction. 5 mechanisms map to 5 levels naturally.
**Confidence:** HIGH
**Resolution:** 5 render mechanisms per level (with A7=off → EXPLICATE-FUNCTION fallback, technically a 6th case).

### SV4 — Clarified Understanding

After 9 ambiguity collapses:
- 5 levels `off | minimal | standard | rich | scholarly`
- Per-level budget: qualitative + per-page operational guidance (not hard caps)
- A1/A3 action permission table per level (operational substance)
- Multi-meaning render rules per level (5 mechanisms + A7=off → EXPLICATE-FUNCTION fallback)
- Default `rich` via A4 chain
- A4 finding refinement note (naming alignment)
- NEW A7-adapted 4-component template
- Runtime conflict resolution: strict budget + fallback + harmony-report flag
- Receptive-only NOT APPLICABLE
- Cross-axis orthogonality preserved (A5/A6/A8)
- Strategy-family-closure marker (3/3)

---

## Phase 4 — Degrees-of-Freedom Reduction

### Variables fixed
- VF1-VF11 per Structural Points above.

### Options eliminated
- 4 or 6 cardinality.
- Default `standard`.
- Lax A7=off (permits some scaffolding).
- Hard-cap per-page budget.
- Receptive-only applied.
- Budget-exceed runtime resolution.
- 2-mechanism multi-meaning render.

### Viable paths
- VP1: 5 per-level definitions with NEW template.
- VP2: A1/A3 action permission table.
- VP3: Multi-meaning render rules per level.
- VP4: A4 cross-validation + refinement note.
- VP5: Cross-axis boundaries.
- VP6: Runtime conflict resolution spec.
- VP7: Said Nursi per level.
- VP8: Strategy-family-closure marker.
- VP9: IC re-test.

### SV5 — Constrained Understanding

Solution space: per-level definitions with full operational substance (budget + action permission + render rules); A4 cross-validation; cross-axis boundaries; runtime conflict spec; Said Nursi per level; Strategy-closure; IC re-test.

---

## Phase 5 — Conceptual Stabilization

**A7 — Scaffolding** = 5 ordinal levels (`off | minimal | standard | rich | scholarly`) of explanatory material accompanying translation at the text surface. Plain-ordinal. Subsumes the user's original feature-activation bundle minus harmony (which became A6): footnote toggle + transliteration toggle + parenthetical glosses + brief in-line explanations.

**Two special characteristics:**
1. **SCAFFOLDING BUDGET for A1/A3 implementation actions.** A1's INLINE-GLOSS / FOOTNOTE and A3's TRANSLITERATE-WITH-GLOSS / FLAG-CULTURAL-CONTEXT / BRIDGE-CULTURAL-DISTANCE consume budget. KEEP-AS-IS / EXPLICATE-FUNCTION / DOMESTICATE / TRANSLITERATE-FULLY / ASSUME-SHARED-CULTURAL-KNOWLEDGE / KEEP-HONORIFICS-SOURCE / PRESERVE-CULTURAL-SPECIFICITY / TARGET-LANGUAGE-EQUIVALENT / ANGLICIZE-HONORIFICS / DOMESTICATE-CULTURAL-FRAME don't consume budget. A7's level determines which budget-consuming actions can fire.

2. **MULTI-MEANING RENDER CONTROL** when polysemy policy fires. 5 render mechanisms map to 5 A7 levels (with A7=off → EXPLICATE-FUNCTION fallback as 6th case).

Per-level scaffolding budget = qualitative orientation + per-page operational guidance (not hard caps). A1/A3 action permission table operationalizes which actions fire. Multi-meaning render rules specify per-level render. NEW A7-adapted 4-component template. Runtime conflict resolution: strict budget + fallback to budget-FREE + harmony-report flag at A6 levels 3+. UX-layer surface-at-config-time deferred. Default `rich` via A4 chain (casual default reflects accessibility commitment). A4 finding refinement note (naming alignment). Receptive-only DOES NOT APPLY. A5↔A7 / A6↔A7 / A7↔A8 orthogonality preserved. CLOSES Strategy family at 3/3.

### Accommodation trigger check
NO patching. 9 ambiguities settled HIGH.

### SV6 — Stabilized Model

A7 stabilized:
- 5 ordinal levels: `off | minimal | standard | rich | scholarly`
- Per-level scaffolding budget (qualitative + per-page operational guidance)
- A1/A3 action permission table per level (operational substance)
- 5 multi-meaning render rules per level (6th case A7=off → EXPLICATE-FUNCTION fallback)
- NEW A7-adapted 4-component template (scaffolding stance + budget + action permission/render rule + cross-axis interaction)
- Runtime conflict resolution: strict + fallback + harmony-report flag
- Default `rich` via A4 chain
- A4 finding refinement note (naming alignment)
- Receptive-only NOT APPLICABLE
- A5↔A7/A6↔A7/A7↔A8 orthogonality
- Strategy-family-CLOSURE (3/3)

**Difference from SV1:** Major. Cardinality validated; labels confirmed; per-level budget specification (qualitative + per-page) decided; A1/A3 action permission table (the operational substance) specified; multi-meaning render rules (5 mechanisms + A7=off fallback) decided; runtime conflict resolution decided; default `rich` via chain decided; A4 refinement note added; cross-axis boundaries documented; Strategy-family-closure marked.

---

## Saturation
- Perspective: APPROACHING.
- Ambiguity: 9/9 HIGH; 0 OPEN.
- SV delta: major.
- Anchor diversity: 7 Constraints, 13 Key Insights, 11 Structural Points, 8 Foundational Principles, 4 Meaning-Nodes. DIVERSE.

**Saturation: HIGH. PROCEED.**

## Inherited Commitments Re-tested

| # | IC | Source | Verdict |
|---|---|---|---|
| IC1 | A7 plain-ordinal | root | RE-TESTED OK |
| IC2 | A7 5-level cardinality | root | RE-TESTED & CONFIRMED |
| IC3 | A7 subsumes feature-activation bundle minus harmony | root | RE-TESTED OK |
| IC4 | A7 multi-meaning render control role | root POLICY | RE-TESTED & SPECIFIED (5 render mechanisms per level + A7=off fallback) |
| IC5 | A4 per-purpose A7 defaults | A4 finding | RE-TESTED & CROSS-VALIDATED with naming refinement note |
| IC6 | A7 interaction with A1/A3 actions | A1+A3+chain | RE-TESTED & SPECIFIED (full action permission table per level) |
| IC7 | NEW translator-strategy 4-component template | A5+A6 | RE-TESTED & ADAPTED for A7 |
| IC8 | Receptive-only NOT APPLICABLE | A4+A5+A6 | RE-TESTED OK |
| IC9 | Chain default via A4 matrix | A5+A6 | RE-TESTED & APPLIED — default `rich` |
| IC10 | Language-agnostic at concept level | root + chain | RE-TESTED OK |
| IC11 | A6↔A7 cross-validation (flagged by A6 finding) | A6 | RE-TESTED & DOCUMENTED — orthogonality holds (harmony report vs text-surface scaffolding) |
| IC12 | 5 ordinal levels `off | minimal | standard | rich | scholarly` | NEW | NEW |
| IC13 | Per-level scaffolding budget (qualitative + per-page operational guidance) | NEW | NEW |
| IC14 | A1/A3 action permission table per level | NEW | NEW |
| IC15 | 5 multi-meaning render rules per level + A7=off → EXPLICATE-FUNCTION fallback | NEW | NEW |
| IC16 | Runtime conflict resolution: strict budget + fallback to budget-FREE + harmony-report flag | NEW | NEW |
| IC17 | A4 finding refinement note (naming alignment, parallel to A6) | NEW | NEW |
| IC18 | A7-adapted 4-component template | NEW | NEW |
| IC19 | Strategy-family-CLOSURE marker (3/3) | NEW | NEW |

## Frontier Flags for Decomposition / Critique

- FF1: UX-layer config-time surface for runtime conflicts ("A7=off + foreignized A5 may produce uncomfortable text") — future UX inquiry.
- FF2: A4 finding refinement note propagation at next A4 maintenance pass.
- FF3: A7↔A8 cross-validation when A8 inquiry runs (forward-looking).
- FF4: Per-target-language scaffolding feasibility — does scholarly apparatus differ per target language tradition? Future inquiry.
- FF5: Polysemy policy operational spec (the always-on policy itself) — separate POLICY inquiry per root commitment.
