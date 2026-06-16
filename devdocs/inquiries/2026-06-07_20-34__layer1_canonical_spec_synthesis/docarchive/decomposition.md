# Decomposition — layer1_canonical_spec_synthesis

## User Input
`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-07_20-34__layer1_canonical_spec_synthesis/_branch.md` (with prior outputs: surfacing.md and sensemaking.md in the same folder)

---

## Step 1 — Coupling Topology

### Elements (SV6)
- E1: Framework Overview (4-layer + 4-family + 8-axis + scope)
- E2: 9-Pattern Compendium (composite + categorical + asymmetric + explicit-zero + dual-tier + content-type-by-level + action-permission + harmony report + multi-meaning three-layer)
- E3: 8 per-axis sections (A1-A8; each with concept + user-question + pattern + cardinality + level enum + per-level prose + cross-axis boundaries + default chain + receptive-only + handling action vocabulary)
- E4: 40-cell per-purpose × per-axis default matrix (refinement notes applied inline)
- E5: 28-pair cross-axis orthogonality verification matrix (4 relation types)
- E6: 3-channel apparatus separation table (text-surface / harmony-report / separate-sections × 8 axes)
- E7: Action-vocabulary map (own actions / modulates / produces / drives-default × 8 axes)
- E8: 5 × 8 = 40-cell policy interaction map
- E9: Receptive-only APPLIES (A1-A3) + NOT APPLICABLE (A4-A8) compendium
- E10: Default-derivation chains per axis (conservative-bias-LOWER / A4 chain / dual-tier)
- E11: Pydantic dataclass structure HINT (pydantic-like syntax; not actual code)
- E12: Said Nursi corpus per-axis mapping
- E13: Versioning v1.0 + inline Changelog
- E14: 2 MUST carry-forward items (A4 maintenance pass + .env.example DEPTH_PROFILE)
- E15: Next Actions COULD list (preset catalog + policy operational specs + source-description schema + UX surface)
- E16: 23-IC Re-test table (synthesis-level)

### Clusters
- **A — Architectural framing:** E1, E2 (set the scene — framework + patterns)
- **B — Per-axis content:** E3 (8 per-axis sections; parallel-structure pieces)
- **C — Cross-axis matrices:** E4, E5, E6, E7 (4 matrices consolidating per-axis content)
- **D — Policy interaction:** E8 (separate from cross-axis because policies are Layer 2, not Layer 1 axes)
- **E — Meta-pattern compendia:** E9, E10 (receptive-only + default chains)
- **F — Implementation hint:** E11 (pydantic structure HINT)
- **G — Concrete corpus anchor:** E12 (Said Nursi mapping)
- **H — Meta-governance:** E13 (versioning + Changelog)
- **I — Action items:** E14, E15 (carry-forward MUST + downstream-unblock COULD)
- **J — Inheritance audit:** E16 (ICs Re-test)

### Coupling perception
- Strong coupling within Per-axis content (E3 — each per-axis section's 4-component template).
- Moderate coupling: E3 ↔ E4 (per-axis A4 defaults feed 40-cell matrix); E3 ↔ E5 (per-axis cross-axis boundary statements feed 28-pair matrix); E3 ↔ E6 (per-axis apparatus channel statements feed 3-channel table); E3 ↔ E7 (per-axis action vocabularies feed action-vocabulary map); E3 ↔ E9 (per-axis receptive-only statements feed compendium); E3 ↔ E10 (per-axis default statements feed chains).
- Moderate coupling: E2 patterns reference all 8 axes (composite → A1; categorical → A4; asymmetric → A5; explicit-zero → A6/A7/A8; dual-tier → A8; content-type-by-level → A8; action-permission → A7; harmony report → A6; multi-meaning three-layer → policy + A7 + A8).
- Weak coupling: E1 framework overview is structurally independent from per-axis content (it sets context; details elaborate downstream).
- Weak coupling: E13 versioning, E11 pydantic hint, E14 + E15 action items, E12 corpus mapping are all atomic-ish pieces with limited inter-coupling.
- Read-only coupling: E16 ICs Re-test consumes all upstream pieces.

---

## Step 2-3 — Pieces

| # | Piece (Canonical Spec Section) | Cluster | Coupling |
|---|---|---|---|
| P1 | Framework Overview (4-layer architecture + 4-family + 8-axis + scope statement) | A | atomic; no internal pieces |
| P2 | Patterns Compendium (9 architectural patterns documented) | A | STRONG internal; references all 8 axes |
| P3 | Per-Axis Sections (8 sub-sections A1-A8; each full 4-component template + per-level prose + cross-axis boundaries + default chain + receptive-only) | B | STRONG internal; bidirectional with matrices |
| P4 | 40-cell per-purpose × per-axis default matrix (with refinement notes applied inline) | C | STRONG; depends P3 + P6/P7/P8/P9/P10 for per-axis values |
| P5 | 28-pair cross-axis orthogonality verification matrix (4 relation types) | C | STRONG; depends P3 + cross-axis boundary statements |
| P6 | 3-channel apparatus separation table (text-surface / harmony-report / separate-sections × 8 axes) | C | atomic; depends P3 for axis ownership |
| P7 | Action-vocabulary map (own actions / modulates / produces / drives-default × 8 axes) | C | atomic; depends P3 for axis action profiles |
| P8 | Policy Interaction Map (5 always-on policies × 8 axes = 40 cells) | D | STRONG; depends P3 + root policy enumeration |
| P9 | Receptive-only Applicability Compendium (APPLIES vs NOT APPLICABLE) | E | atomic; depends P3 |
| P10 | Default-Derivation Chains (per axis) | E | atomic; depends P3 default chain statements |
| P11 | Pydantic Dataclass Structure HINT (pydantic-like syntax; not actual code) | F | atomic |
| P12 | Said Nursi Corpus Mapping (per axis) | G | atomic; depends P3 |
| P13 | Versioning v1.0 + Inline Changelog | H | atomic |
| P14 | Carry-Forward Maintenance Bundle (Next Actions MUST: 2 items) | I | atomic; consolidates refinement notes |
| P15 | Downstream-Unblock List (Next Actions COULD) | I | atomic |
| P16 | Inherited Commitments Re-test (synthesis-level table; 23 ICs) | J | depends on all |

All atoms validate. HIGH confidence at boundaries (top-down + bottom-up agree).

---

## Step 4 — Question Tree

### P1 — Framework Overview
**Question:** What is the canonical Layer 1 framework's architecture — 4 layers, 4 families, 8 axes — and what's in-scope (Layer 1) vs out-of-scope (Layers 2/3/4 + Layer 1A presets)?

**Verification:**
- [ ] 4-layer architecture named (Layer 1 USER-FACING + Layer 2 POLICY + Layer 3 SOURCE-DESCRIPTION + Layer 4 SYSTEM-FLAGS)
- [ ] 4-family organization named (Reader + Purpose + Strategy + Depth)
- [ ] 8-axis inventory listed (A1 Reader Level + A2 Domain Expertise + A3 Source Culture + A4 Purpose + A5 Source Fidelity + A6 Form Preservation + A7 Scaffolding + A8 Analysis Depth)
- [ ] Scope statement (in-scope: Layer 1; out-of-scope: Layers 2/3/4 + Layer 1A presets + Layer 2 policy operational specs)
- [ ] FRAMEWORK CLOSURE marker (8/8 axes specified)

### P2 — Patterns Compendium
**Question:** What are the 9 architectural patterns the canonical spec documents (where they apply + why they exist)?

**Verification:**
- [ ] composite-axis pattern (A1 — headline + 5 sub-fields with same-labels-for-propagation + per-sub-field overrides)
- [ ] categorical pattern (A4 — qualitatively distinct purposes; not ordinal)
- [ ] asymmetric pattern (A5 — policy-embedded structural absence of `heavily-domesticated`)
- [ ] explicit-zero level pattern (A6 `off` + A7 `off` + A8 `none`)
- [ ] dual-tier default pattern (A8 — A4 chain when A4 set; conservative-bias fallback when A4 silent)
- [ ] content-type-by-level table pattern (A8 — 12 × 5 = 60 cells; structurally distinct from action-permission)
- [ ] action-permission table pattern (A7 — scaffolding budget gates A1/A3 budget-consuming actions)
- [ ] harmony report apparatus channel pattern (A6 Levels 3+ — meta-analytic apparatus distinct from text-surface and separate-sections)
- [ ] multi-meaning three-layer treatment pattern (Policy invariant + A7 render + A8 analysis at high levels)

### P3 — Per-Axis Sections
**Question:** For each of the 8 axes, what is the full canonical-spec content (concept + user-question + pattern + cardinality + level enum + per-level prose + cross-axis boundaries + default chain + receptive-only applicability + handling action vocabulary)?

**Verification (per axis A1-A8):**
- [ ] Concept (1-paragraph statement)
- [ ] User-question
- [ ] Pattern (composite-axis / plain-ordinal / categorical / asymmetric ordinal)
- [ ] Cardinality + level enum
- [ ] Per-level prose (full 4-component template per level)
- [ ] Cross-axis boundaries (named adjacent axes with criterion)
- [ ] Default chain statement
- [ ] Receptive-only applicability (APPLIES / NOT APPLICABLE)
- [ ] Handling action vocabulary (own actions / modulates / produces / drives defaults — refer to action-vocabulary map)
- [ ] Said Nursi corpus mapping snippet per level (linked to P12)
- [ ] DOMESTICATE-disfavored policy mention where applicable (A1/A3/A4/A5)

**Per-axis verification additionally requires:**
- [ ] A1: 5 sub-fields fully specified (vocabulary-breadth / syntactic-processing-capacity / idiom-recognition / inference-capacity / cultural-reference-recognition)
- [ ] A4: 5 categorical with NEW 4-component categorical template
- [ ] A5: 4 asymmetric (no `heavily-domesticated`); A5 → A1/A3 modulation tables
- [ ] A6: 5 levels with Tier 1-4 mapping + activation gate at Level 3 `light`
- [ ] A7: 5 levels with action-permission table + 5 multi-meaning render rules + EXPLICATE-FUNCTION fallback
- [ ] A8: 5 levels with `none` + content-type-by-level table (12 × 5) + 3-framing A7↔A8 rule + harmony-report-location

### P4 — 40-Cell Per-Purpose × Per-Axis Default Matrix
**Question:** For each of 5 A4 purposes, for each of 7 other axes (A1 headline + A2 + A3 + A5 + A6 + A7 + A8), what is the default value (with refinement notes applied inline for internal consistency)?

**Verification:**
- [ ] 5 × 7 = 35 cells filled (A1 headline counted once for the composite-axis)
- [ ] Refinement notes applied inline:
  - A5 column language-learning: `foreignized` (not `balanced-to-foreignized`)
  - A6 column: A4 "moderate"→`light`; A4 "high"→`standard`; A4 "MAXIMUM"→`maximum`
  - A7 column: A4 "moderate"→`standard`; A4 "MAX rich"→`scholarly`
  - A8 column: A4 "deep+scholarly"→`scholarly`
- [ ] Per-cell justification (key entries cite the per-axis finding rationale)
- [ ] Matrix carries override-path note (user can override any cell)

### P5 — 28-Pair Cross-Axis Orthogonality Matrix
**Question:** For each of 28 unordered axis pairs, what is the relation type (orthogonal / gated / orthogonal-with-modulation / drives-default)?

**Verification:**
- [ ] All 28 pairs listed (8 choose 2)
- [ ] Each pair labeled with one of 4 relation types
- [ ] Each pair's rationale 1-line statement
- [ ] A4↔X drives-default for X ∈ {A1, A2, A3, A5, A6, A7, A8} — 7 pairs
- [ ] A7↔A1 gated, A7↔A3 gated — 2 pairs
- [ ] A5↔A1, A5↔A3 orthogonal-with-modulation — 2 pairs
- [ ] A6↔A7, A6↔A8, A7↔A8 orthogonal (apparatus channel separation) — 3 pairs
- [ ] Remaining pairs orthogonal — 14 pairs

### P6 — 3-Channel Apparatus Separation Table
**Question:** For each of 3 apparatus channels (text-surface / harmony-report / separate-sections), what is each axis's role (produces / owns / does not contribute / drives defaults / modulates / cross-references at high level)?

**Verification:**
- [ ] 3 × 8 = 24-cell table
- [ ] A7 OWNS text-surface
- [ ] A6 OWNS harmony-report (at Levels 3+)
- [ ] A8 OWNS separate-sections
- [ ] Cross-references at A8 deep+ and A6 Levels 3+ noted
- [ ] Per-axis row consistent with action-vocabulary map (P7) and per-axis section (P3)

### P7 — Action-Vocabulary Map
**Question:** For each of 8 axes, what is the action-role (own actions with vocabulary specified / modulates other axes' actions / produces content directly / drives defaults via matrix)?

**Verification:**
- [ ] A1: own actions per sub-field (5 sub-fields with different vocabularies; cultural-reference-recognition has 5 actions)
- [ ] A2: own actions (9 actions in 2 categories + 1 bridge)
- [ ] A3: own actions (10 actions in 4 categories)
- [ ] A4: drives defaults (no own actions)
- [ ] A5: modulates A1 + A3 actions (no own actions)
- [ ] A6: 3-Pass methodology + tier preservation (no per-reference actions)
- [ ] A7: scaffolding budget gates A1/A3 + 5 multi-meaning render rules (no own per-reference actions)
- [ ] A8: produces 12 content-types directly (own content-types; the only content-producing axis)

### P8 — 5 × 8 Policy Interaction Map
**Question:** For each of 5 always-on policies × 8 axes = 40 cells, how does the policy interact with the axis (invariant / activation gate at level X / renders preserved senses per axis level / analyzes preserved senses at high level / drives policy emphasis / modulates / not applicable)?

**Verification:**
- [ ] 5 policies named (multi-meaning preservation / register-alternation preservation / polysemy-via-local-construction / nazm preservation / no-smoothing)
- [ ] 5 × 8 = 40 cells filled
- [ ] Load-bearing cells highlighted:
  - Multi-meaning × A7 (renders) and × A8 (analyzes) — three-layer treatment
  - Register-alternation × A6 (Tier 1/2 structure)
  - Nazm × A6 (activation gate at Level 3 `light`)
  - No-smoothing × all (invariant)
- [ ] Per-cell rationale 1-line statement

### P9 — Receptive-only Applicability Compendium
**Question:** Which axes have receptive-only commitment APPLIES vs NOT APPLICABLE, and what's the rationale?

**Verification:**
- [ ] APPLIES: A1 (5 sub-fields), A2, A3 (Reader family)
- [ ] NOT APPLICABLE: A4, A5, A6, A7, A8 (translator-strategy)
- [ ] Rationale: A4-A8 are user-configuration / translator-strategy; not reader-property
- [ ] Future productive case (e.g., language-learning back-translation) noted as deferred

### P10 — Default-Derivation Chains
**Question:** For each of 8 axes, what is the default-derivation mechanism (conservative-bias-LOWER / A4 chain / dual-tier / direct)?

**Verification:**
- [ ] A1 (5 sub-fields): conservative-bias-LOWER per sub-field; headline propagates
- [ ] A2: conservative-bias-LOWER; default `lay`
- [ ] A3: conservative-bias-LOWER; default `outsider`
- [ ] A4: default `casual` when silent
- [ ] A5: A4 chain → matrix; A4 silent → `balanced`
- [ ] A6: A4 chain → matrix; A4 silent → `light` (activation gate)
- [ ] A7: A4 chain → matrix; A4 silent → `rich`
- [ ] A8: DUAL-TIER (A4 chain when A4 set; conservative-bias `standard` when A4 silent — A8 unique)

### P11 — Pydantic Dataclass Structure HINT
**Question:** What is the pydantic dataclass structure for the 8 axes (pydantic-like syntax; not actual code; Literal types per axis + composite class for A1 + receptive-only mode noted)?

**Verification:**
- [ ] A1 composite class with 5 sub-fields each `Literal[5 values]`
- [ ] A2 `Literal[5 values]`
- [ ] A3 `Literal[5 values]`
- [ ] A4 `Literal[5 values]`
- [ ] A5 `Literal[4 values]` (asymmetric)
- [ ] A6 `Literal[5 values]`
- [ ] A7 `Literal[5 values]`
- [ ] A8 `Literal[5 values]` (with `none` at position 1)
- [ ] Receptive-only mode noted as currently-default for Reader-family (A1/A2/A3); not applicable for A4-A8
- [ ] Hint NOT actual code — implementation specifics (validators / base-class / serializers) deferred to downstream

### P12 — Said Nursi Corpus Mapping
**Question:** For each of 8 axes, what is the Said Nursi corpus level the AI uses (the project's primary anchor)?

**Verification:**
- [ ] A1: typical Nursi reader fluency (varies by use case; defaults to daily/conversational)
- [ ] A2: typical Islamic-theology depth (varies; defaults to aware/educated)
- [ ] A3: typical Nursi reader cultural proximity (varies; outsider for general; familiar+ for Naqshbandi-Khalidi readers)
- [ ] A4: per A4 purpose (scholarly / devotional / casual / language-learning / performance — all 5 are valid Nursi use cases)
- [ ] A5: typically `foreignized` for scholarly/devotional Nursi; `balanced` for casual
- [ ] A6: typically `standard` (Tier 1+2+3 conditional) for scholarly Nursi; `maximum` for performance
- [ ] A7: typically `rich` for casual Nursi; `scholarly` for full apparatus edition
- [ ] A8: typically `deep` for scholarly Nursi; `surface` for performance

### P13 — Versioning + Inline Changelog
**Question:** What is the canonical spec's version + Changelog format?

**Verification:**
- [ ] Version v1.0 (first canonical synthesis after framework closure)
- [ ] Status: active
- [ ] Refines list: 9 priors named with paths
- [ ] Inline Changelog section at end of spec
- [ ] v1.0 entry: "Initial canonical synthesis after A8 framework closure at 8/8 axes"
- [ ] Version-increment rule: minor (v1.1) for refinement notes propagation, additional patterns, or non-breaking matrix cell updates; major (v2.0) for axis-level revisions or new sub-fields
- [ ] Refinement triggers section

### P14 — Carry-Forward Maintenance Bundle
**Question:** What 2 Next Actions MUST carry-forward items consolidate the accumulated refinement notes from A5/A6/A7/A8?

**Verification:**
- [ ] MUST item 1: A4 finding maintenance pass with 4-5 refinements bundled:
  - A5 column language-learning: `balanced-to-foreignized` → `foreignized`
  - A6 column: A4 "moderate"→`light`; A4 "high"→`standard`; A4 "MAXIMUM"→`maximum`
  - A7 column: A4 "moderate"→`standard`; A4 "MAX rich"→`scholarly`
  - A8 column: A4 language-learning "deep+scholarly" → `scholarly`
- [ ] MUST item 2: `.env.example` DEPTH_PROFILE refinement (add `none` at position 1 of DEPTH_PROFILE values; document legacy compatibility)
- [ ] Each MUST item: Who / Gate / Why per CONCLUDE template

### P15 — Downstream-Unblock List
**Question:** What Next Actions COULD items enumerate the downstream work the canonical spec unblocks?

**Verification:**
- [ ] Schema commit (pydantic dataclass) — MUST (separate; not in COULD)
- [ ] Per-purpose × per-axis default matrix synthesis — PRODUCED here (no separate item)
- [ ] Layer 1A UX preset catalog — COULD
- [ ] Layer 2 POLICY operational specs (5 policies) — COULD (1-5 separate inquiries)
- [ ] Layer 3 SOURCE-DESCRIPTION schema — COULD
- [ ] UX-layer runtime conflict surface — COULD
- [ ] Translator-AI prompt assembly with all 8 axes + policies — MUST after schema commit
- [ ] Per-target-language refinements (Tier 4 feasibility; scaffolding feasibility; analysis-content feasibility) — DEFERRED

### P16 — Inherited Commitments Re-test
**Question:** How are the 23 inherited commitments from 9 priors re-tested at synthesis level?

**Verification:**
- [ ] 23 ICs named with source
- [ ] Each IC verdict: RE-TESTED OK / RE-TESTED & DOCUMENTED / RE-TESTED & EXTENDED / RE-TESTED & CONSOLIDATED / RE-TESTED & EMBODIED
- [ ] No silently-absorbed commitments
- [ ] Cross-reference to canonical spec section where each IC is documented

---

## Step 5 — Interface Map

| From | To | Direction | What flows |
|---|---|---|---|
| P1 | P3 | One-way | Framework context referenced in per-axis sections |
| P1 | P2 | One-way | Framework context referenced in patterns compendium |
| P2 | P3 | Bi-directional | Patterns reference axes; per-axis sections cite which patterns apply |
| P3 | P4 | One-way | Per-axis A4 default cells feed the matrix |
| P3 | P5 | One-way | Per-axis cross-axis boundary statements feed the orthogonality matrix |
| P3 | P6 | One-way | Per-axis apparatus channel statements feed the 3-channel table |
| P3 | P7 | One-way | Per-axis action profiles feed the action-vocabulary map |
| P3 | P8 | One-way | Per-axis policy interactions feed the policy interaction map |
| P3 | P9 | One-way | Per-axis receptive-only statements feed the compendium |
| P3 | P10 | One-way | Per-axis default chain statements feed the chains section |
| P3 | P12 | One-way | Per-axis Nursi mapping snippets feed the corpus section |
| P5 ↔ P6 | Bi-directional | Orthogonality includes A6↔A7/A6↔A8/A7↔A8 channel separation — must agree with 3-channel table |
| P4 | P11 | One-way | Matrix defaults consumed by pydantic structure HINT's default values |
| P3 | P14 | One-way | Refinement notes from per-axis sections feed the bundle |
| P11 | P15 | One-way | Pydantic structure HINT enables schema commit (downstream-unblock) |
| All | P16 | Read-only | All upstream pieces consumed by IC re-test |
| Source Input | All | One-way | Branch _branch.md is preserved as Section 14 |

**Assumptions-not-data check:**
- P3 assumes P1's framework context (verified).
- P3 assumes P2's pattern vocabulary (verified — per-axis sections reference patterns by name).
- P4 assumes P3's per-axis A4 cross-validation tables are settled (verified — surfacing R2-R9).
- P5 assumes P3's cross-axis boundary statements use 4 relation types (verified — sensemaking KI3, A12).
- P6 assumes P3's apparatus channel statements distinguish 3 channels (verified — sensemaking KI4).
- P8 assumes root's 5 policies + per-axis policy interaction statements (verified — sensemaking KI6).
- P14 assumes P3's refinement notes accumulated across A5/A6/A7/A8 (verified — sensemaking KI9).

No hidden coupling.

---

## Step 6 — Dependency Order

LEVEL 0 (atomic; can start independently): P1 Framework Overview, P11 Pydantic Hint, P13 Versioning, P14 Carry-Forward Bundle, P15 Downstream-Unblock List
LEVEL 1: P2 Patterns Compendium (references all 8 axes; can start before per-axis full content)
LEVEL 2: P3 Per-Axis Sections (8 sub-sections; each independent of others except for cross-axis references)
LEVEL 3: P4 40-Cell Matrix, P5 28-Pair Matrix, P6 3-Channel Table, P7 Action-Vocabulary Map (all depend on P3)
LEVEL 4: P8 Policy Interaction Map (depends P3 + root policies), P9 Receptive-only Compendium, P10 Default Chains, P12 Said Nursi Mapping (all depend on P3)
LEVEL 5: P16 ICs Re-test (depends on all upstream)

**Critical path:** P1 → P3 → P4 / P5 / P6 / P7 → P8 / P9 / P10 / P12 → P16

**Parallel-eligible:** {P1, P11, P13, P14, P15} at Level 0; per-axis sub-sections within P3; P4/P5/P6/P7 at Level 3; P8/P9/P10/P12 at Level 4.

---

## Step 7 — Self-Evaluation

### Minimum 3 dimensions

**Independence:** PASS — each piece's question is answerable given its dependencies. P3 (per-axis sections) is the largest piece; each sub-section (per axis) is independently writeable from the per-axis finding's content.

**Completeness:** PASS — all SV6 commitments mapped:
- 14-section canonical spec → P1 through P16 (Source Input section auto)
- Self-contained dense → P3 reproduces full per-level prose
- 40-cell matrix → P4
- 28-pair orthogonality → P5
- 3-channel apparatus → P6
- Action-vocabulary map → P7
- 5 × 8 policy interaction → P8
- Receptive-only compendium → P9
- Default-derivation chains → P10
- Pydantic HINT → P11
- Said Nursi mapping → P12
- Versioning + Changelog → P13
- 2 MUST carry-forward → P14
- Downstream-unblock → P15
- 23 ICs → P16
- 9-pattern compendium → P2

No gaps. **PASS.**

**Reassembly:** PASS — pieces + interfaces reconstruct the canonical spec. Given P1 (Framework Overview) + P2 (Patterns Compendium) + P3 (8 Per-Axis Sections) + P4-P7 (4 Cross-Axis Matrices) + P8 (Policy Interaction Map) + P9 (Receptive-only Compendium) + P10 (Default Chains) + P11 (Pydantic HINT) + P12 (Said Nursi Mapping) + P13 (Versioning + Changelog) + P14 (Carry-Forward MUST) + P15 (Downstream-Unblock COULD) + P16 (ICs Re-test), the canonical spec contains: framework architecture, architectural patterns, per-axis content with full prose, cross-axis consolidation matrices, policy interaction with the framework, meta-pattern compendia, implementation hint, corpus anchor, governance, action items, inheritance audit. The original question (consolidate 8 axes into single canonical spec) is answered.

**Determination-mechanism piece check:** the canonical spec's runtime determinations (which content-types fire / which actions modulate / which apparatus channel content lives in) are all DOCUMENTED by P4-P8 and the per-axis P3 sub-sections. No runtime determination is presupposed without being documented. PASS.

### Full 7 dimensions (high-stakes)

**Tractability:** P3 (per-axis sections) is the biggest — 8 sub-sections × ~50-100 lines each = ~400-800 lines just for Section 3. Each sub-section is tractable in a single focused pass. P4 (40-cell matrix) and P5 (28-pair matrix) are also substantive but tabular (compact). PASS.

**Interface clarity:** PASS — all interfaces explicit; assumptions audited; no hidden coupling.

**Balance:** P3 ≈ 50% of total finding length; P4-P8 (5 matrices/maps) ≈ 25%; P1+P2+P11+P12+P13+P14+P15+P16 ≈ 25%. P3's larger weight is operationally necessary (self-contained dense reproduction of per-axis prose). PASS with note that P3 is naturally the largest piece — sub-decomposition by axis is structural-not-implementational.

**Confidence:** HIGH — top-down + bottom-up boundaries agree.

---

## Final Deliverable

### Question Tree (16 pieces; 14 canonical spec sections + meta)
- P1 Framework Overview
- P2 Patterns Compendium (9 patterns)
- P3 Per-Axis Sections (A1-A8; 8 sub-sections with full prose)
- P4 40-Cell Per-Purpose × Per-Axis Default Matrix (refinement notes applied inline)
- P5 28-Pair Cross-Axis Orthogonality Matrix (4 relation types)
- P6 3-Channel Apparatus Separation Table
- P7 Action-Vocabulary Map
- P8 5 × 8 Policy Interaction Map
- P9 Receptive-only Applicability Compendium
- P10 Default-Derivation Chains
- P11 Pydantic Dataclass Structure HINT
- P12 Said Nursi Corpus Mapping
- P13 Versioning + Inline Changelog
- P14 Carry-Forward Maintenance Bundle (2 Next Actions MUST items)
- P15 Downstream-Unblock List (Next Actions COULD)
- P16 Inherited Commitments Re-test (23 ICs from 9 priors)

### Dependency Order
LEVEL 0 {P1, P11, P13, P14, P15} → LEVEL 1 {P2} → LEVEL 2 {P3 (8 sub-sections)} → LEVEL 3 {P4, P5, P6, P7} → LEVEL 4 {P8, P9, P10, P12} → LEVEL 5 {P16}.

### Content-generation points to Innovation
16 CG points (one per piece). The synthesis is mostly consolidation (low novelty per piece) — Innovation will be Standard-default mode with low Generator coverage; Framer mechanisms (Lens Shifting on prior commitments + Inversion of synthesis structure choices) carry most of the load. Methodology-mode pre-decided.
