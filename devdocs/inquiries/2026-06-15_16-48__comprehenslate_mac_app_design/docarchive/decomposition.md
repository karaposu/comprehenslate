# Decomposition — comprehenslate_mac_app_design

## User Input

```text
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/_branch.md

Upstream outputs in same folder: articulate_simple.md + surfacing.md + sensemaking.md. The SV6 stabilized model is the substrate to decompose:

- 5-layer architecture: (1) Project shell / (2) Configuration surface / (3) Execution engine / (4) Reading & output / (5) Quality & translation-craft
- 3-tier triage per layer: essential / differentiating / deferrable
- Cross-cutting concerns: privacy / performance / accessibility / Mac-platform polish
- MVP roadmap (3-tier-as-phases)
- 7 translation-principle-derived UI features for the differentiating tier

The pieces should reflect the 5 layers + cross-cutting + roadmap + Inherited Re-test + Open Questions. Innovation will then generate per-layer content (essential + differentiating + deferrable items per layer).

Save decomposition output to: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/decomposition.md
```

---

## Step 1 — Perceive Coupling Topology

### Elements in the whole

The deliverable is one finding answering the Mac-app design question. Stabilized substrate from Sensemaking produces these elements:

**Architectural commitments:**
- **A1** — the 5-layer architecture spine (the layer-list itself + Project-as-data-model + `.compldoc` format)
- **A2** — Layer 1 (Project shell) feature triage (essential / differentiating / deferrable)
- **A3** — Layer 2 (Configuration surface) feature triage
- **A4** — Layer 3 (Execution engine) feature triage
- **A5** — Layer 4 (Reading & output) feature triage
- **A6** — Layer 5 (Quality & translation-craft) feature triage
- **A7** — Cross-cutting concerns (privacy / performance / accessibility / Mac-platform polish)

**Phasing element:**
- **A8** — MVP roadmap (v1 = essential per layer; v2 = adds differentiating; v3+ = adds deferrable)

**Principle-derived element:**
- **A9** — the 7 translation-principle-derived UI features as a coherent differentiating-tier cluster (cross-layer; primarily Quality-layer-resident)

**Synthesis-trigger elements:**
- **A10** — Inherited Commitments Re-test (already produced at Sensemaking Phase 3 Ambiguity 6; just needs propagation)
- **A11** — Open Questions (monetization out-of-architecture; mobile/iPad future; localization-of-the-app; cross-corpus extension; etc.)

**Reasoning element:**
- **A12** — Reasoning (why 5 layers; why Project-as-data-model; why 3 tiers; why selective principle-mapping; etc.)

### Coupling map

| Pair | Strength | Why |
|---|---|---|
| A1 ↔ A2-A6 | STRONG | The architecture spine defines the layer-list; each layer's feature inventory is a sub-detail of one specific layer |
| A2 ↔ A3, A4, A5, A6 (between-layer features) | WEAK | After the 5-layer commitment is fixed and Project-as-data-model is committed, each layer's feature inventory is independent of others' inventories |
| A1 ↔ A7 (architecture ↔ cross-cutting) | STRONG | Cross-cutting concerns are part of the architectural commitments, not per-layer additions |
| A7 ↔ A2-A6 (cross-cutting ↔ per-layer features) | WEAK-to-MODERATE | Cross-cutting concerns apply to every layer but aren't tightly coupled to any specific feature inventory |
| A8 ↔ A2-A6 (roadmap ↔ per-layer triage) | STRONG | Roadmap IS the essential-tier-per-layer extraction across all layers |
| A9 ↔ A6 (principle-derived ↔ Quality layer) | STRONG | 5 of 7 principle-derived features primarily live in Quality layer |
| A9 ↔ A3, A5 (principle-derived ↔ Config + Reading) | WEAK-to-MODERATE | A few principle-derived features span (lineage spans Config; analysis-depth spans Reading) |
| A10 ↔ all (Re-test ↔ design) | WEAK | Re-test is already done in Sensemaking; just propagated to finding |
| A11 ↔ all (Open Questions ↔ design) | WEAK | Open questions are residual signals; not load-bearing for the architecture |
| A12 ↔ A1 (reasoning ↔ architectural spine) | STRONG | Reasoning IS the rationale for the architectural commitments |

### Clusters

- **Cluster A (architectural commitments):** A1 + A7 + A12 — the architecture spine, cross-cutting concerns, and reasoning that motivates them.
- **Cluster B (per-layer feature triages):** A2 + A3 + A4 + A5 + A6 — five independent sibling sub-clusters, one per architectural layer.
- **Cluster C (principle-derived cluster):** A9 — cross-layer principle-derived features (mostly Quality-layer-resident but with cross-layer references).
- **Cluster D (phasing):** A8 — MVP roadmap derived from per-layer triages.
- **Cluster E (synthesis admin):** A10 + A11 — Re-test propagation + Open Questions.

### Major boundaries

- Between Cluster A and Cluster B: clear (architecture defines layer-list; per-layer content lives within it).
- Between siblings in Cluster B: clear (each layer is its own scope; feature inventories don't overlap once layer-list is fixed).
- Between Cluster B and Cluster C: blurry but justified (principle-derived features cross layers; cluster honors the "innovative-heavy surface" the user explicitly asked for).
- Between Cluster B and Cluster D: clear (roadmap is the essential-tier-extraction).
- Cluster E sits beside everything (admin sections of the finding).

---

## Step 2 — Detect Boundaries (Top-Down)

The natural cuts produce **10 pieces**:

- **P1 — Architectural commitments.** 5-layer architecture spine + Project-as-data-model + `.compldoc` file format + cross-cutting concerns. (Cluster A.)
- **P2 — Project shell layer feature triage.**
- **P3 — Configuration surface layer feature triage.**
- **P4 — Execution engine layer feature triage.**
- **P5 — Reading & output layer feature triage.**
- **P6 — Quality & translation-craft layer feature triage.**
- **P7 — 7 translation-principle-derived differentiating features.** Cross-layer cluster, primarily Quality-layer-resident. (Cluster C.)
- **P8 — MVP roadmap.** v1 / v2 / v3+ phasing derived from per-layer triages. (Cluster D.)
- **P9 — Inherited Commitments Re-test.** Propagation of Sensemaking's Ambiguity 6 outputs.
- **P10 — Open Questions.** Monetization out-of-architecture; mobile/iPad future; etc.

---

## Step 3 — Validate Boundaries (Bottom-Up Check)

Atomic elements identifiable: each surfaced feature item (from surfacing.md's 155 items); each architectural principle (FP1-FP7 from sensemaking); each inherited commitment (6 priors); each cross-cutting concern (privacy / performance / accessibility / platform polish); each principle-derived feature (the 7 named at Sensemaking Phase 3 Ambiguity 3).

### Atom grouping

| Atom class | Belongs in | Top-down/bottom-up match? |
|---|---|---|
| Architectural principles (FP1-FP7) | P1 | YES |
| Cross-cutting concerns (privacy / perf / accessibility / platform polish) | P1 | YES |
| Per-layer feature items from surfacing | P2-P6 (one layer each) | YES — each item maps to one layer naturally |
| 7 principle-derived features | P7 (primarily) + cross-referenced in primary-layer's piece (P3/P5/P6) | YES — the cross-reference is acknowledged as the cluster's nature |
| Essential-tier extraction per layer | P8 | YES — derives from P2-P6 |
| Per-prior commitment status | P9 | YES |
| Open-question item | P10 | YES |

No atom is split across pieces inappropriately; no atom is grouped that should be split. **Boundary confidence: HIGH.**

---

## Step 4 — Express as Question Tree

### P1 — Architectural commitments

**Question:** What is the Mac app's architectural skeleton — the layer-list, the data model, and the cross-cutting concerns?

**Verification criteria:**
- [ ] 5 architectural layers named with intent + 1-line scope per layer: Project shell / Configuration surface / Execution engine / Reading & output surface / Quality & translation-craft surface.
- [ ] **Project as primary data model** explicitly named; `.compldoc` directory-bundle file format committed; per-Project content list (source + config + state + outputs + glossary + TM + bookmarks).
- [ ] **Foundational principles** committed: local-first; BYO credentials; native Mac patterns where natural; Tier 1-2 harmony preservation as non-negotiable; 3-layer schema architecture as canonical config surface; 5-step SKILL workflow as UX spine; FP2 "don't declare what the LLM can infer" enforced at intake.
- [ ] **Cross-cutting concerns** enumerated: privacy (local-first, Keychain); performance (streaming, lazy lists, Swift concurrency); accessibility (VoiceOver, Dynamic Type, dark mode); Mac-platform polish (document-based-app, menu bar, notifications, Spotlight, share extension, keyboard shortcuts).
- [ ] **3-tier triage mechanism** stated: essential / differentiating / deferrable. Per-tier criterion: essential = MVP-critical or non-negotiable; differentiating = unique-to-Comprehenslate or differentiates from generic LLM-translation apps; deferrable = nice-to-have / future.

### P2 — Project shell layer feature triage

**Question:** What features comprise the Project shell layer across essential / differentiating / deferrable tiers?

**Verification criteria:**
- [ ] Essential tier: ≥4 items including project list / project create wizard / open existing / per-project bundle persistence.
- [ ] Differentiating tier: ≥2 items including project templates (Nursi preset; Bible preset; Quran preset; etc.) and onboarding tutorial.
- [ ] Deferrable tier: ≥2 items (multi-document projects; per-project encryption; iCloud sync; project archive).
- [ ] Document-based-app pattern referenced.

### P3 — Configuration surface layer feature triage

**Question:** What features comprise the Configuration surface layer?

**Verification criteria:**
- [ ] Essential tier: ≥4 items including TC editor (8 axes); Policy editor (7 Policy classes); PC editor (engine knobs); LLM provider/model settings; API key Keychain storage; two-level provider config (app-default + per-project-override); A4 purpose preset chips.
- [ ] Differentiating tier: ≥3 items including inline calibration explanation (from `config_base_source.md` / `policy_config_base_source.md`); per-policy preview (show what changing a policy value does to a sample chunk); config preset save/load; config-diff comparison view.
- [ ] Deferrable tier: ≥2 items.

### P4 — Execution engine layer feature triage

**Question:** What features comprise the Execution engine layer?

**Verification criteria:**
- [ ] Essential tier: ≥6 items including chunked orchestration (per `PC.chunking_granularity`); per-chunk persistence; pause/resume controls; cancel-with-state-preservation; background continuation; crash recovery; multi-provider abstraction; rate-limit handling; per-chunk retry.
- [ ] Differentiating tier: ≥3 items including smart cache (source+config-hashed); cost prediction; cumulative-cost display; local-LLM auto-discovery; parallel-mode controls (per `PC.parallel_mode`); model A/B compare.
- [ ] Deferrable tier: ≥2 items.

### P5 — Reading & output layer feature triage

**Question:** What features comprise the Reading & output surface layer?

**Verification criteria:**
- [ ] Essential tier: ≥4 items including live reading view (translation as it happens); side-by-side source-target alignment; export to MD; export to PDF.
- [ ] Differentiating tier: ≥3 items including bilingual side-by-side export; translator-notes export; per-chunk analysis-depth explanation overlay (per `TC.A8`); reading-aloud TTS mode.
- [ ] Deferrable tier: ≥3 items including ePub / HTML / plain / JSON exports; LaTeX / BibTeX; custom output template.

### P6 — Quality & translation-craft layer feature triage

**Question:** What features comprise the Quality & translation-craft layer?

**Verification criteria:**
- [ ] Essential tier: ≥2 items including terminology consistency checker; per-project glossary (term → preferred translation).
- [ ] Differentiating tier: ≥5 items including harmony-layer Tier 1-2 violation flagging; multi-translation collation (Vahide / Akarsu / Comprehenslate); per-chunk lineage view; idiom-alert inbox; cultural-reference inbox; passage bookmarks; embedded-language detection visualization; honorific consistency tracking.
- [ ] Deferrable tier: ≥2 items including translation memory (TM); cross-project TM; quality dashboard; review/edit workflow.

### P7 — 7 translation-principle-derived differentiating features

**Question:** What are the 7 translation-principle-derived UI features that differentiate Comprehenslate, and where does each live primarily?

**Verification criteria:**
- [ ] 7 features named: harmony-layer visualization; multi-translation collation; per-chunk lineage view; per-chunk analysis-depth explanation; passage bookmarks (fihrist); idiom alerts; cultural-reference inbox.
- [ ] Per-feature: principle of origin (which `references/core/` principle motivates it); primary-layer-home (Quality / Config / Reading); 1-line UX description.
- [ ] Cross-references to per-layer pieces (P3 / P5 / P6) where applicable.

### P8 — MVP roadmap

**Question:** What does the v1 / v2 / v3+ phasing look like, derived from per-layer triages?

**Verification criteria:**
- [ ] v1 = essential-tier-only across all 5 layers + provider abstraction (2 providers); estimated 3-6 months single-developer.
- [ ] v2 = adds differentiating-tier features per layer + local LLM + extended exports + 4-6 of the 7 principle-derived features.
- [ ] v3+ = adds deferrable-tier features + remaining principle-derived features + power-user surfaces (scripting, plugins, Continuity).
- [ ] Cross-version dependencies noted (e.g., harmony visualization in v2 depends on harmony-layer engine support in v1).

### P9 — Inherited Commitments Re-test

**Question:** What is the status of each commitment inherited from the 6 substrate priors?

**Verification criteria:**
- [ ] 6 commitment statuses propagated from Sensemaking Ambiguity 6: 3-layer schema architecture (CONFIRMED); SKILL.md 5-step workflow (CONFIRMED); harmony-layer Tier 1-2 preservation as non-negotiable (CONFIRMED); translation principles' "comprehensation" identity (CONFIRMED with frame revision); anti-bloat principle (CONFIRMED); FP2 "don't declare what the LLM can infer" (CONFIRMED and extended).
- [ ] Each status cites structural evidence from the Mac app design (which UI feature embodies the commitment).

### P10 — Open Questions

**Question:** What open questions remain after this design?

**Verification criteria:**
- [ ] Monetization model is OUT of architecture scope (one-time purchase / Mac App Store / direct download / open-source / donation-ware are distribution decisions).
- [ ] Mobile / iPad future (Catalyst port? separate native iPad app?) flagged as future.
- [ ] Localization of the app UI itself (English first; later French / Turkish / Arabic).
- [ ] R12+R13 surfacing frontier (power-user features not exhausted; cross-corpus extension to non-Islamic theological corpora — same frontier flag as the chunk_types_vs_mechanisms inquiry).
- [ ] Each open question typed (Monitoring / Blocked / Research Frontier / Refinement Trigger) with revival trigger.

---

## Step 5 — Map Interfaces

| Source | Target | Direction | What flows | Type |
|---|---|---|---|---|
| P1 | P2, P3, P4, P5, P6 | one-way | Layer definitions + cross-cutting principles + 3-tier triage mechanism | Information / contract |
| P1 | P7 | one-way | Layer definitions (for primary-layer-home anchoring) | Information |
| P1 | P8 | one-way | Architectural spine (for roadmap structure) | Information |
| P2-P6 | P8 | one-way | Per-layer essential-tier extraction | Data |
| P2-P6 | P7 | sparse one-way | Some principle-derived features cross-reference per-layer pieces | Reference |
| P7 | P5 + P6 (especially P6) | one-way | Quality-layer-resident principle features anchor inside Quality piece | Reference |
| Sensemaking (Ambiguity 6) | P9 | one-way | Already-completed Re-test content | Data |
| Sensemaking (residuals) + Surfacing (frontier flags) | P10 | one-way | Open-question source material | Information |

### Assumptions-not-data check

- **P2-P6 assume** P1's 5-layer commitment is verbatim and stable. Hidden coupling risk if P1 reorders or renames mid-Innovation. **Made explicit:** P1 commits to the 5-layer sequence + cross-cutting concerns list before P2-P6 begin.
- **P7 assumes** the 7 principle-derived features from Sensemaking Phase 3 Ambiguity 3 are preserved verbatim. **Made explicit:** P7 inherits the 7-feature list from Sensemaking; doesn't re-derive.
- **P8 assumes** each per-layer piece commits to a 3-tier triage with at least the minimum item counts in P2-P6 verification criteria. **Made explicit:** P2-P6 each commit to tier sizes; P8 reads them.
- **P9 + P10 assume** Sensemaking's content is propagable verbatim. **Made explicit:** these pieces don't generate new content; they propagate.
- **P3 assumes** the 7 Policy classes from `schemas.py` (verified earlier this session) are stable. **Made explicit:** schemas.py is settled substrate (Inherited Re-test confirms).

No hidden coupling detected.

---

## Step 6 — Order by Dependency

```
Level 0 (no dependencies in this inquiry):
  P1 — Architectural commitments

Level 1 (depend on P1; otherwise independent):
  P2 — Project shell layer
  P3 — Configuration surface layer
  P4 — Execution engine layer
  P5 — Reading & output layer
  P6 — Quality & translation-craft layer
  P7 — 7 principle-derived features (depends on P1; inherits from Sensemaking)
  P9 — Inherited Commitments Re-test (depends on Sensemaking, not on P1-P6)
  P10 — Open Questions (depends on Sensemaking + Surfacing residuals)

Level 2 (depend on Level 1 outputs):
  P8 — MVP roadmap (depends on P2-P6 for per-layer triage extraction)
```

Parallelism: P2 ‖ P3 ‖ P4 ‖ P5 ‖ P6 ‖ P7 ‖ P9 ‖ P10 at Level 1 (8-way parallel feasible).

No circular dependencies. P1 has no incoming dependencies, must run first.

---

## Step 7 — Self-Evaluation

### Minimum 3 dimensions

| Dimension | Check | Pass? |
|---|---|---|
| **Independence** | Each piece's question answerable without reading sibling pieces (except through defined interfaces) | **PASS** — P2-P6 use P1's architectural commitments as shared substrate; otherwise independent. P7-P10 also Level-1-independent. |
| **Completeness** | Pieces cover the whole | **PASS** — every required section of a finding under the Synthesis Trigger is covered: architectural skeleton (P1), per-layer feature triage (P2-P6), principle-derived cluster (P7), roadmap (P8), inherited re-test (P9), open questions (P10). |
| **Reassembly** | Pieces + interfaces reconstruct the whole | **PASS** — assembling P1 architectural commitments into P2-P6 + P7 (anchored at P1) + P8 (derived from P2-P6) + P9 (propagated from Sensemaking) + P10 (residuals) produces a finding that satisfies the CONCLUDE template + the Synthesis Trigger enforcement. |

### Full 7-dimension evaluation

| Dimension | Result | Notes |
|---|---|---|
| Independence | PASS | See minimum above |
| Completeness | PASS | See minimum above |
| Reassembly | PASS | See minimum above |
| **Tractability** | PASS | Each piece is a single-focused-pass deliverable. P2-P6 have similar shape and similar item count; P7 is medium; P1, P8 are lighter; P9, P10 are admin-style. |
| **Interface clarity** | PASS | All cross-piece flows explicit; assumptions-not-data check passed. |
| **Balance** | ACCEPTABLE | P2-P6 are similar weight (~10-15% each of finding); P7 is medium (~8%); P1 is medium (~10%); P8, P9, P10 are smaller (~5% each). No single piece carries 80% of the work. |
| **Confidence** | HIGH | Top-down (cluster identification from Sensemaking SV6) and bottom-up (atom validation across 155 surfaced items) agree on boundaries. |

### Determination-mechanism piece check

The 3-tier triage involves design-time determinations ("is this feature essential / differentiating / deferrable?"). Each per-layer piece (P2-P6) makes these determinations. The criterion mechanism is stated explicitly in P1: essential = MVP-critical or non-negotiable; differentiating = unique-to-Comprehenslate; deferrable = nice-to-have. P1 names the mechanism; P2-P6 apply it. The determination mechanism is not left implicit.

### Failure mode check

| Mode | Detected? |
|---|---|
| 1 Premature Decomposition | NO — Sensemaking produced a stable SV6; decomposition cuts at the architectural layer boundaries that emerged naturally from coupling analysis. |
| 2 Wrong Boundaries | NO — cuts are at weak-coupling regions (between-layer-features; between layer-content and roadmap). |
| 3 Hidden Coupling | NO — Assumptions-not-data check applied; no unstated assumptions detected. |
| 4 Missing Pieces | NO — Reassembly passes; determination-mechanism check passes (P1 names the triage criterion). |
| 5 Over-Decomposition | BORDERLINE — 10 pieces is on the higher end. Per-layer pieces (P2-P6) could in principle merge into one "per-layer feature triage" piece, but the per-layer content is genuinely independent and each warrants its own Innovation pass to generate concrete feature inventories. The 10-piece decomposition is justified by the finding's structure (each piece corresponds to a distinct finding section). ACCEPTED. |
| 6 Ignoring Dependencies | NO — Dependency DAG explicit; parallelism opportunities identified. |
| 7 Imbalanced Decomposition | NO — Balance check ACCEPTABLE; no single piece dominates. |

### Verdict

**PROCEED.** All 7 self-evaluation dimensions pass; one borderline on Over-Decomposition (10 pieces) accepted because each piece corresponds to a distinct finding section + a distinct Innovation pass with distinct content. No failure modes fired.
