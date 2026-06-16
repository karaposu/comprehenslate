# Decomposition — user_research_persona_validation

## User Input

```text
[abbreviated — see _branch.md + sensemaking.md SV6 for full context]
SV6 commits to a HYBRID 4-section deliverable with 5 personas + 10 prioritized decisions + 6-commitment Re-test + design recommendations.
```

---

## Step 1 — Perceive Coupling Topology

### Elements in the whole

- **A1** Methodology & Disclaimers (synthesis-disclaimer template; substrate-anchoring rule; bias-balance discipline; anti-pattern guards for the 5 risks R1-R5 from Sensemaking)
- **A2** Research Plan (interview script + recruitment criteria + sample size + analysis framework — for real-interview execution by the user)
- **A3** 5 Synthetic Persona Profiles (Nur Talebesi-tradition; Quran editor; Mevlana/Rumi; Talmud; academic translation-studies — each with demographics + workflow + pain-points + tools + quote + substrate-anchor)
- **A4** 50-cell Pressure-Test Walkthrough Matrix (5 personas × 10 prioritized design decisions; each cell: reaction + pain-point alignment + design implication)
- **A5** 6 Per-Commitment Re-test Verdicts (CONFIRMED / REFINED / QUESTIONED per Mac-app commitment, derived from matrix patterns)
- **A6** Synthesis-Based Design Recommendations (keep / refine / revisit per design decision)
- **A7** Inherited Commitments Re-test admin section (per CONCLUDE protocol — propagates A5 verdicts + flags non-validated substrate priors as INHERITED-WITHOUT-RE-TEST)
- **A8** Open Questions (substrate-calibration; secondary stakeholders; cross-corpus persona expansion; gap-to-real-interviews; etc.)

### Coupling map

| Pair | Strength | Why |
|---|---|---|
| A1 ↔ all others | STRONG | Methodology framing constrains every other piece (disclaimer pattern; substrate-anchoring rule applied universally) |
| A2 ↔ A3-A8 | WEAK | The research plan is for FUTURE real-interview execution; independent of the synthesis content. User could read A2 alone, or A3-A6 alone. |
| A3 ↔ A4 | STRONG | Matrix cells depend on persona profiles (each row is one persona) |
| A3a-A3e (personas among themselves) | MODERATE | Personas independent in content but the variant-spread rule (anti-homogeneity) couples their selection across the cluster |
| A4 ↔ A5 | STRONG | Verdicts derive from aggregating matrix patterns |
| A4 ↔ A6 | STRONG | Recommendations derive from matrix cells |
| A5 ↔ A6 | MODERATE | Verdicts inform recommendations |
| A5 ↔ A7 | STRONG | Re-test admin propagates verdicts |
| A8 ↔ all others | WEAK | Open questions are residuals; don't drive content |

### Clusters

- **Cluster A (methodology + framing):** A1 — the foundational disclaimer + rules.
- **Cluster B (research plan):** A2 — independent deliverable section for real-execution use.
- **Cluster C (synthetic personas):** A3 — the 5 personas as a single cluster with variant-spread coupling.
- **Cluster D (pressure-test outputs):** A4 + A5 + A6 — matrix + verdicts + recommendations, tightly coupled.
- **Cluster E (admin / residuals):** A7 + A8 — propagation + open questions.

### Major boundaries

- Between A1 (methodology) and content pieces: clear (A1 is framing; others are content).
- Between A2 (plan) and A3-A6 (synthesis content): clear (different timeline/purpose).
- Between A3 (personas) and A4 (matrix): clear interface (matrix rows reference persona profiles).
- Within Cluster D (matrix ↔ verdicts ↔ recommendations): tight but sequential (matrix → verdicts; matrix → recommendations).
- A7 + A8 are admin; sit beside content.

---

## Step 2 — Detect Boundaries (Top-Down)

The natural cuts produce **8 pieces** matching the finding's section structure:

- **P1 — Methodology & Disclaimers** (Cluster A)
- **P2 — Research Plan** (Cluster B)
- **P3 — 5 Synthetic Persona Profiles** (Cluster C; one piece with 5 sub-items)
- **P4 — Pressure-Test Walkthrough Matrix** (Cluster D-1; 5×10 cells)
- **P5 — Per-Commitment Re-test Verdicts** (Cluster D-2; 6 verdicts)
- **P6 — Synthesis-Based Design Recommendations** (Cluster D-3)
- **P7 — Inherited Commitments Re-test admin section** (Cluster E-1)
- **P8 — Open Questions** (Cluster E-2)

---

## Step 3 — Validate Boundaries (Bottom-Up)

### Atomic elements

- Disclaimer text; substrate-anchoring rule statement; anti-pattern names (5 risks) → P1
- Interview question categories; recruitment screening criteria; sample-size guidance → P2
- Persona name/role/demographics; workflow steps; pain points; current-tool list; representative quote → P3 (5 instances)
- Matrix-cell reaction text; per-cell design-implication; per-cell substrate citation → P4 (50 instances)
- Per-commitment verdict (CONFIRMED/REFINED/QUESTIONED) + supporting evidence → P5 (6 instances)
- Per-decision recommendation (keep/refine/revisit) + rationale → P6 (10 instances)
- Re-test admin per-commitment row → P7 (6+ instances)
- Open question item with type + revival trigger → P8

### Atom grouping check

| Atom class | Belongs in | Match? |
|---|---|---|
| Methodology framing atoms | P1 | YES |
| Research-plan atoms | P2 | YES |
| Per-persona profile atoms (5 personas × ~8 fields) | P3 | YES — each persona is one P3 sub-item |
| Per-cell matrix atoms (50 cells) | P4 | YES |
| Per-commitment verdict atoms (6 commitments) | P5 | YES |
| Per-decision recommendation atoms (10 decisions) | P6 | YES |
| Re-test admin row atoms | P7 | YES |
| Open-question atoms | P8 | YES |

No atom is split inappropriately; no atom is grouped with pieces it shouldn't be. **Boundary confidence: HIGH.**

---

## Step 4 — Express as Question Tree

### P1 — Methodology & Disclaimers

**Question:** What methodology frames the validation, and what disclaimers are required?

**Verification criteria:**
- [ ] AI-can't-interview structural bound stated explicitly.
- [ ] Synthesis disclaimer template (the verbatim text to attach to every synthetic output).
- [ ] Substrate-anchoring rule (each persona's pain-point must map to substrate-described needs from `references/core/` or Mac-app design).
- [ ] Bias-balance discipline (anti-confirmation + anti-critique-only; explicit instruction to surface both supporting and critical reactions).
- [ ] Anti-pattern guards for the 5 risks (confirmation bias; over-claim; pain-point invention; persona homogeneity; solution bias).
- [ ] Honest framing: best-effort first-pass; user should validate with real interviews before treating as definitive.

### P2 — Research Plan

**Question:** What research plan should the user execute when conducting real interviews?

**Verification criteria:**
- [ ] Interview script with ≥5 question categories from Surfacing R5 (background; current tools; pain points; design probes; feature priorities; differentiator validation; pricing; edge cases; hypothetical scenarios; magic-wand question).
- [ ] Recruitment criteria targeting the 5 personas (screening questions per persona-type).
- [ ] Sample size guidance (~5 per persona-type for saturation; ~20-30 total).
- [ ] Recruitment channels suggestion (academic networks; translator associations; theological publishers; LinkedIn; specialized forums).
- [ ] Analysis framework: affinity mapping → persona-pattern extraction → JTBD → feature-priority synthesis → design-impact mapping.
- [ ] Expected deliverables from the user's real-interview process (interviewed personas; verbatim quotes; pain-point ranking; feature-priority synthesis; design-impact memo).
- [ ] Ethics / IRB note (consent forms; honorarium guidance).

### P3 — 5 Synthetic Persona Profiles

**Question:** What are the 5 substrate-anchored persona profiles?

**Verification criteria:**
- [ ] 5 personas: Nur Talebesi-tradition Risale-i Nur scholar; Quran-translation editor; Mevlana/Rumi translator; Talmud translator; Academic translation-studies scholar.
- [ ] Each persona includes: **Name** (synthetic, illustrative); **Role / Title**; **Demographics** (career stage, geographic/cultural background); **Experience** (years translating; corpora worked on); **Workflow** (typical translation session shape); **Goals** (what they want to accomplish); **Pain Points** (3-5 specific frustrations with current tools, anchored in substrate); **Current Tools** (what they use today); **Representative Quote** (illustrative — synthetic).
- [ ] Each persona includes **Substrate Anchor** — references to specific `references/core/` or Mac-app finding passages that ground the persona's needs.
- [ ] Each persona carries the **synthesis disclaimer** from P1.
- [ ] Variant-spread check: the 5 personas don't cluster around one archetype.

### P4 — Pressure-Test Walkthrough Matrix

**Question:** What does each persona's walkthrough of the 10 prioritized design decisions yield?

**Verification criteria:**
- [ ] **5 personas × 10 decisions = 50 cells** populated.
- [ ] Each cell includes: **Persona's likely reaction** (positive / mixed / critical) + **Pain-point alignment** (does the decision address a substrate-anchored pain?) + **Design implication** (keep / refine / revisit; specifics).
- [ ] Substrate citations where applicable (point to the specific principle or feature the reaction draws on).
- [ ] Bias balance: across all 50 cells, both supportive and critical reactions appear (not uniformly positive).
- [ ] The 10 decisions are the SV6-committed set: D1 Project-as-data-model; D2 BYO API key; D3 10 principle-derived features; D4 multi-translation collation; D5 per-chunk lineage; D6 glossary; D7 3-tier triage/MVP; D8 multi-provider+local at v1; D9 pause/resume+chunks; D10 monetization preferences.

### P5 — Per-Commitment Re-test Verdicts

**Question:** What is the Re-test verdict per Mac-app commitment, derived from the matrix?

**Verification criteria:**
- [ ] 6 Mac-app commitments enumerated: (1) 5-layer architecture; (2) Project-as-data-model; (3) 3-tier triage + MVP scope; (4) 10 principle-derived features; (5) BYO API key + multi-provider with local at v1; (6) Pause/resume + chunked persistence.
- [ ] Each commitment receives a verdict: **CONFIRMED** (≥4 of 5 personas support it in the matrix) / **REFINED** (2-3 personas support with caveats; specific refinement noted) / **QUESTIONED** (≥3 personas raise concerns; revisit recommended).
- [ ] Each verdict cites structural evidence from the matrix (specific cells).
- [ ] REFINED verdicts include specific refinement language.
- [ ] QUESTIONED verdicts include revisit recommendation.

### P6 — Synthesis-Based Design Recommendations

**Question:** What design changes are recommended based on the synthesis?

**Verification criteria:**
- [ ] Per-decision recommendation (D1-D10): keep / refine / revisit + rationale.
- [ ] Aligned with P5 verdicts (CONFIRMED commitments → keep; REFINED → refine; QUESTIONED → revisit).
- [ ] Explicit acknowledgment that recommendations are **synthesis-based, not empirical** — should be validated with real interviews before acting.
- [ ] Priority ranking (high / medium / low) per recommendation, anchored in how many personas were affected.

### P7 — Inherited Commitments Re-test (admin section per CONCLUDE)

**Question:** How do the 6+ inherited commitments propagate to the finding's CONCLUDE Re-test section?

**Verification criteria:**
- [ ] 6 Mac-app commitments listed with verdicts from P5.
- [ ] Substrate priors from `SKILL/references/core/` (translation principles, harmony layer) listed with INHERITED-WITHOUT-RE-TEST status + reason (they're substrate that the validation USES, not commitments the validation re-tests; the personas USE substrate-described needs).
- [ ] Mac-app finding's commitments that were NOT re-tested by this validation (e.g., 5-layer architecture is implicit; not directly tested) flagged as INHERITED-WITHOUT-RE-TEST.

### P8 — Open Questions

**Question:** What open questions remain after this validation?

**Verification criteria:**
- [ ] **Substrate-calibration** noted: personas frozen at current substrate; refresh when substrate evolves (Refinement Trigger).
- [ ] **Secondary stakeholders** (editors who hire translators; publishers commissioning translations) flagged for future research (Research Frontier).
- [ ] **Cross-corpus persona expansion** (Hindu / Buddhist / Christian patristic) flagged (Research Frontier).
- [ ] **Gap to real-interview research** noted: synthesis is best-effort first-pass; real validation needed before high-stakes design changes (Refinement Trigger: when v1 build commitment imminent).
- [ ] Each open question typed (Monitoring / Blocked / Research Frontier / Refinement Trigger) with revival trigger.

---

## Step 5 — Map Interfaces

| Source | Target | Direction | What flows | Type |
|---|---|---|---|---|
| P1 (methodology) | All others | one-way | Disclaimer template + substrate-anchoring rule + bias-balance discipline + anti-pattern guards | Information / contract |
| P3 (personas) | P4 (matrix) | one-way | Persona stances feed walkthrough cells (each persona = one matrix row) | Data |
| P4 (matrix) | P5 (verdicts) | one-way | Matrix-cell aggregations → per-commitment verdicts | Data |
| P4 (matrix) | P6 (recommendations) | one-way | Matrix cells → per-decision recommendations | Data |
| P5 (verdicts) | P6 (recommendations) | one-way | Verdicts shape recommendations (CONFIRMED → keep; REFINED → refine; QUESTIONED → revisit) | Reference |
| P5 (verdicts) | P7 (Re-test admin) | one-way | Verdicts propagate to admin section per CONCLUDE protocol | Data |
| Substrate (references/core/ + Mac-app finding) | P3 (personas) | one-way | Anchor source for persona construction (anti-hallucination) | Information |
| Mac-app finding's 6 commitments | P5 (verdicts) + P7 (admin) | one-way | The commitments to be re-tested | Data |
| Sensemaking residuals + Surfacing frontier flags | P8 (open questions) | one-way | Source material | Information |

### Assumptions-not-data check

- **P3 assumes** P1's substrate-anchoring rule is committed and verbatim. **Made explicit:** P1 commits to the rule before P3 begins.
- **P4 assumes** P3's persona profiles are stable. **Made explicit:** P3 commits to the 5 persona profiles before P4 begins.
- **P5 + P6 assume** P4's matrix is complete (all 50 cells populated). **Made explicit:** P4 commits to full matrix before P5/P6 begin.
- **All pieces assume** P1's disclaimer pattern is applied. **Made explicit:** P1 commits to disclaimer template; downstream pieces attach it.
- **P5 assumes** Mac-app commitment list is settled (from prior finding's Inherited Re-test). **Verified.**

No hidden coupling detected.

---

## Step 6 — Order by Dependency

```
Level 0 (no dependencies in this inquiry):
  P1 — Methodology & Disclaimers

Level 1 (depend on P1; otherwise independent):
  P2 — Research Plan
  P3 — 5 Synthetic Personas
  P8 — Open Questions

Level 2 (depend on Level-1 outputs):
  P4 — Pressure-Test Matrix (depends on P3)
  P7 — Re-test admin (depends partly on Mac-app commitments; can run in parallel)

Level 3 (depend on P4):
  P5 — Per-Commitment Verdicts (depends on P4)
  P6 — Design Recommendations (depends on P4 + P5)

Level 4 (final propagation):
  P7 — Re-test admin (consumes P5; if Level 2 only partial, completes here)
```

Parallelism opportunities:
- P2 ‖ P3 ‖ P8 at L1
- P5 ‖ P6 at L3 (both depend on P4 but independent of each other)

No circular dependencies.

---

## Step 7 — Self-Evaluation

### Minimum 3 dimensions

| Dimension | Check | Pass? |
|---|---|---|
| **Independence** | Each piece's question answerable via defined interfaces only | **PASS** — P1 supplies methodology; each downstream piece uses interfaces explicitly |
| **Completeness** | Pieces cover the whole | **PASS** — every required section of the hybrid finding covered |
| **Reassembly** | Pieces + interfaces reconstruct the whole | **PASS** — P1 framing + P2 plan + P3 personas + P4 matrix + P5 verdicts + P6 recommendations + P7 admin + P8 questions = the 4-section hybrid finding (Methodology / Research Plan / Personas+Matrix+Recommendations / Verdicts+Open) |

### Full 7-dimension evaluation

| Dimension | Result | Notes |
|---|---|---|
| Independence | PASS | See minimum |
| Completeness | PASS | See minimum |
| Reassembly | PASS | See minimum |
| **Tractability** | PASS | Each piece is a single-focused-pass deliverable. P3 (5 personas) and P4 (50 cells) are heaviest but template-driven (consistent per-persona / per-cell structure). |
| **Interface clarity** | PASS | All cross-piece flows explicit; assumptions-not-data check passed |
| **Balance** | ACCEPTABLE | P3 + P4 are heaviest (~25% each); P1, P2, P6 medium (~10-15% each); P5, P7, P8 lighter (~5% each). No single piece carries 80%. |
| **Confidence** | HIGH | Top-down clusters + bottom-up atoms agree |

### Determination-mechanism piece check

P5's verdicts depend on a runtime determination — "what does the matrix say for this commitment?" The determination mechanism is: aggregate matrix cells touching the commitment; apply threshold (≥4 of 5 personas → CONFIRMED; 2-3 → REFINED; ≥3 raising concerns → QUESTIONED). P5's verification includes the threshold rule. Mechanism explicit; not left implicit.

### Failure mode check

| Mode | Detected? |
|---|---|
| 1 Premature Decomposition | NO — Sensemaking SV6 stable |
| 2 Wrong Boundaries | NO — cuts at weak-coupling regions (methodology / content / admin) |
| 3 Hidden Coupling | NO — assumptions-not-data check applied |
| 4 Missing Pieces | NO — Reassembly passes; determination-mechanism check passes |
| 5 Over-Decomposition | BORDERLINE — 8 pieces is on higher end. Each piece is a distinct finding section + distinct Innovation pass. Merging pieces would conflate distinct deliverable surfaces. ACCEPTED. |
| 6 Ignoring Dependencies | NO — Dependency DAG explicit; parallelism identified |
| 7 Imbalanced Decomposition | NO — Balance ACCEPTABLE |

### Verdict

**PROCEED.** All 7 self-evaluation dimensions pass; one borderline on Over-Decomposition (8 pieces) accepted because each piece corresponds to a distinct deliverable section with distinct content. No failure modes fired.
