# Decomposition — Chunking Deep-Dive

## User Input

Input file: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/_branch.md`
Upstream: `articulate_simple.md` + `surfacing.md` + `sensemaking.md` in same folder. SV6 stabilized model is the substrate to decompose.

---

## Step 1 — Coupling Topology

### Elements in the whole (the chunking deep-dive finding)

From SV6's 5 committed concepts + supporting structure:

| # | Element | Notes |
|---|---|---|
| E1 | Three-operation category definition | The conceptual frame |
| E2 | Source segmentation operation (i) | First of three ops |
| E3 | LLM-context-window management operation (ii) | Second of three ops |
| E4 | Config-application granularity operation (iii) | Third of three ops |
| E5 | SourceDescriptor placement (`source_chunking_units`) | Where (i) lives |
| E6 | TranslationConfig placement (`chunking_strategy`) | Where (iii) lives (user surface) |
| E7 | PipelineConfig placement (`chunking_budget`) | Where (ii) lives |
| E8 | Strategy enum literals (8 categories) | Content of `chunking_strategy` |
| E9 | A4-driven defaults matrix (5 purposes × strategy) | Default propagation |
| E10 | A6 activation-gate cascade | A6 ≥ light → harmony-aware required |
| E11 | Multi-meaning chunk-size lower bound | Polysemy + disambiguator co-presence |
| E12 | Tier 1-2 preservation hard constraint | The non-negotiable |
| E13 | LLM-based feasibility verdict (cost + accuracy) | Answers user's "possible?" |
| E14 | Recommended hybrid harmony-aware approach | Operational default |
| E15 | Empirical validation plan (deferred MUST) | Validation on Nursi corpus |
| E16 | Caching argument (config-independent) | Cost amortization |
| E17 | 10 failure modes from R8 | Concrete failure cases |
| E18 | Cross-axis interaction map (A1-A8 + edge-cases) | How chunking touches each axis |
| E19 | Generalization to broader pattern (Bible/Quran/Hindu) | Pattern-level claim |
| E20 | De-facto mesele-level baseline (user's implicit practice) | Default justification |

### Coupling clusters

**CONCEPTUAL cluster (E1-E4):** strong internal coupling. The category def AND the three operations are jointly the conceptual frame. Change to E1 forces change to E2/E3/E4; change to any operation may force E1 to revise scope.

**PLACEMENT cluster (E5-E7):** strong internal coupling. The three placements are jointly the split decision. E5 also tightly couples to E2 (source segmentation operation determines source_chunking_units); E7 tightly couples to E3.

**STRATEGY cluster (E6, E8, E9):** strong internal coupling. The strategy enum lives in TranslationConfig placement; the A4-driven defaults are encoded in this schema's defaults.

**CONSTRAINTS cluster (E10-E12):** strong internal coupling. The three constraints jointly bound what any chunker output can be. E10 is the runtime cascade; E11 is the runtime invariant lower bound; E12 is the absolute hard constraint.

**FEASIBILITY cluster (E13-E16):** strong internal coupling. Cost analysis → recommended approach → validation plan → caching enabler. The hybrid recommendation is justified by all four together.

**FAILURE MODES (E17):** moderate coupling to constraints (each failure is a constraint articulated as forbidden outcome) + moderate coupling to recommended approach (each failure must have a mitigation).

**CROSS-AXIS (E18):** moderate coupling across CONSTRAINTS (A6 cascade is here), STRATEGY (A4 defaults are here), and the existing 8-axis schema as an input.

**SUPPORTING / FRAMING (E19, E20):** loose coupling. Generalization (E19) is a justification argument for PLACEMENT; baseline (E20) is a justification argument for STRATEGY default. Each folds into its host cluster.

### Coupling valleys (boundaries)

- **CONCEPTUAL ↔ PLACEMENT** — moderate coupling (operations imply placement candidates; placement decision is independent of operation enumeration). Cuttable.
- **PLACEMENT ↔ STRATEGY** — moderate coupling (strategy enum lives in TranslationConfig schema; strategy content can be enumerated without schema-shape commitment). Cuttable.
- **STRATEGY ↔ CONSTRAINTS** — moderate coupling (constraints filter strategy choices; constraints can be specified independently of strategy enumeration). Cuttable.
- **CONSTRAINTS ↔ FEASIBILITY** — low coupling (correctness vs engineering). Clean cut.
- **CROSS-AXIS spans clusters** — moderate coupling. Its own piece, with interfaces to STRATEGY (A4 defaults) and CONSTRAINTS (A6 cascade).
- **FAILURE MODES spans CONSTRAINTS + FEASIBILITY** — moderate coupling. Its own piece, with interfaces to both.

---

## Step 2 — Boundaries (Top-Down)

Cut at the valleys above. Initial piece set:

1. **P1 — Three-operation category (CONCEPTUAL)** — what IS chunking in Comprehenslate?
2. **P2 — Split placement across three schemas (PLACEMENT, includes E19 generalization)** — where does chunking LIVE?
3. **P3 — Strategy enum + A4-driven defaults (STRATEGY, includes E20 baseline)** — what STRATEGIES are exposed?
4. **P4 — Cross-cutting constraints (CONSTRAINTS)** — what must chunker output respect?
5. **P5 — LLM feasibility + recommended hybrid + empirical validation (FEASIBILITY)** — is LLM-based chunking POSSIBLE, what's the default, how to validate?
6. **P6 — Cross-axis interaction matrix (CROSS-AXIS)** — how does chunking interact with A1-A8 + edge-cases?
7. **P7 — Failure modes list with mitigations (FAILURE MODES)** — what fails, what mitigates?

7 pieces.

---

## Step 3 — Boundary Validation (Bottom-Up Check)

Atoms (irreducible):

| Atom | Natural home |
|---|---|
| The three operations (segmentation / LLM-context / config-granularity) | P1 |
| The three schema names (SourceDescriptor / TranslationConfig / PipelineConfig) | P2 |
| Generalization argument to Bible/Quran/Hindu | P2 (justifies split-placement) |
| 8 strategy enum literals | P3 |
| 5 A4-purposes × strategy matrix cells | P3 |
| Mesele-level baseline | P3 (justifies default choice) |
| Tier 1-2 hard constraint | P4 |
| Multi-meaning chunk-size lower bound | P4 |
| A6 activation-gate cascade | P4 (mentioned in P6 as A6-interaction) |
| LLM cost numbers + caching argument | P5 |
| Hybrid harmony-aware mechanism description | P5 (full); P3 (literal name only) |
| Empirical validation plan | P5 |
| Each A1-A8 axis interaction cell | P6 |
| Each relevant edge-case interaction cell | P6 |
| Each of 10 failure modes | P7 |
| Per-failure-mode mitigation mapping | P7 |

Bottom-up check:
- No atom split across pieces ✓
- No atom grouped that should be independent ✓
- A6 cascade appears in both P4 (constraint) and P6 (cross-axis interaction) — this is intentional: P4 owns the cascade RULE; P6 cross-references it as the A6 interaction example.
- "Hybrid harmony-aware" appears in P3 (as literal name) and P5 (full mechanism) — also intentional: P3 owns the enum slot; P5 owns the recommendation justification.

**Confidence: HIGH.** Top-down boundaries and bottom-up atom-grouping agree.

---

## Step 4 — Question Tree

### P1 — Three-operation category

**Question:** What IS chunking in Comprehenslate as a category, and what are its component operations?

**Verification criteria:**
- [ ] Category named ("three-operation chunking category")
- [ ] Three operations enumerated:
  - [ ] (i) Source segmentation
  - [ ] (ii) LLM-context-window management
  - [ ] (iii) Config-application granularity
- [ ] Definition stated per operation
- [ ] Inter-operation relationships specified (partially independent but interact)
- [ ] Why-conflated-under-one-word addressed (user's framing, why disaggregation matters)

### P2 — Split placement across three schemas

**Question:** Where does each chunking operation LIVE architecturally — TranslationConfig, SourceDescriptor, or PipelineConfig — and why is the split structurally motivated?

**Verification criteria:**
- [ ] Each operation mapped to schema (i → SourceDescriptor; ii → PipelineConfig; iii → TranslationConfig)
- [ ] Each schema's field signature sketched (`source_chunking_units` / `chunking_budget` / `chunking_strategy`)
- [ ] Split-placement justified vs monolithic-9th-axis alternative
- [ ] Generalization argument stated (Bible/Quran/Hindu use different source-natural-units; split-placement absorbs the variance)
- [ ] Granularity-of-config insight articulated (chunking is the granularity MECHANISM, not a parallel axis)

### P3 — Strategy enum + A4-driven defaults

**Question:** What strategy literals should `TranslationConfig.chunking_strategy` expose, with what per-A4-purpose defaults?

**Verification criteria:**
- [ ] Strategy enum literals enumerated (≥7 from: `source-structural-unit` / `paragraph` / `sentence` / `harmony-tier-aware` / `passage-typology-aware` / `LLM-detected` / `fixed-budget-with-snap` / `hybrid`)
- [ ] Each strategy described with mechanism + cost/quality profile
- [ ] A4-driven defaults matrix specified (5 purposes × strategy mapping)
- [ ] De-facto mesele-level baseline aligned to one of the literals as default for Nursi case
- [ ] Pattern-level applicability stated (corpus-agnostic labels)

### P4 — Cross-cutting constraints

**Question:** What cross-cutting constraints must any chunker output respect, and how do they cascade?

**Verification criteria:**
- [ ] Tier 1-2 hard constraint articulated (chunker outputs that break Tier 1 chains are rejected/repaired)
- [ ] Multi-meaning chunk-size lower bound specified (polysemy + disambiguating local-construction co-presence)
- [ ] A6 activation-gate cascade documented (A6 ≥ `light` → harmony-tier-aware required; below → simpler permitted)
- [ ] Cascade interactions among constraints specified (Tier 1-2 is harder than multi-meaning lower bound, which is harder than A6 cascade)
- [ ] Asymmetric-failure (under-chunking > over-chunking on failure scale) stated

### P5 — LLM-based feasibility + recommended hybrid + empirical validation

**Question:** Is LLM-based chunking feasible for Comprehenslate, what's the recommended operational default, and what empirical validation is required?

**Verification criteria:**
- [ ] Cost analysis stated (~$9-45 per Risale-i-Nur-sized corpus with Opus at one-shot pre-processing)
- [ ] Caching argument stated (config-independent → cacheable across config tweaks)
- [ ] Recommended approach (hybrid harmony-aware) detailed at mechanism level
- [ ] Empirical validation plan outlined as deferred MUST
- [ ] Feasibility verdict explicit (YES at one-shot pre-processing; NO at per-translation runtime)
- [ ] Distinction between (a) technical feasibility and (b) economic + qualitative feasibility addressed

### P6 — Cross-axis interaction matrix

**Question:** How does chunking interact with each existing axis (A1-A8) and the 14 edge-case candidates?

**Verification criteria:**
- [ ] Interaction with each A1-A8 axis stated (each row in the matrix; ≥5 should be HIGH-signal)
- [ ] Interaction with relevant edge-case candidates stated:
  - [ ] passage_typology (#7) — sister-concept disambiguation
  - [ ] embedded_source_languages (#1) — atomic embedded quotation
  - [ ] source_apparatus_handling (#6) — hashiye attached to referent
  - [ ] voice_disambiguation (#4) — voice-cluster preservation
- [ ] A6 cascade cross-referenced from P4
- [ ] A4-driven defaults cross-referenced from P3

### P7 — Failure modes list with mitigations

**Question:** What are the chunking failure modes, and how does the recommended approach mitigate each?

**Verification criteria:**
- [ ] 10 failure modes from R8 enumerated
- [ ] Severity classified per mode (HARD constraint violation / cohesion / size / cross-reference)
- [ ] Per-failure-mode mitigation in the recommended approach documented
- [ ] Asymmetric-failure direction respected (under-chunking flagged worse than over-chunking)
- [ ] Unaddressed failure modes flagged as deferred research

---

## Step 5 — Interface Map

| ID | From | To | What flows | Direction |
|---|---|---|---|---|
| I1 | P1 | P2 | Operation definitions (source-segmentation / LLM-context / config-granularity) → placement candidates per operation | one-way |
| I2 | P2 | P3 | Schema decision (TranslationConfig holds chunking_strategy) → enum content lives in this schema | one-way |
| I3 | P3 | P4 | Strategy enum literals → constraints filter/cascade-determine permissible | one-way (forward) |
| I4 | P4 | P3 | Constraint cascade → which enum literals are permitted at which A6 setting (e.g., A6 ≥ `light` permits only harmony-aware variants) | one-way (back-flow) — pair with I3, makes bidirectional |
| I5 | P5 | P3 | Recommended approach IS one of the strategy enum literals (`hybrid` or `hybrid-harmony-aware`) | one-way |
| I6 | P5 | P4 | Feasibility analysis verifies recommended approach respects constraints (caching makes Tier 1-2-aware LLM chunking economical) | one-way |
| I7 | P6 | P3 | Cross-axis A4 × strategy interaction → A4-driven defaults matrix cells | one-way |
| I8 | P6 | P4 | Cross-axis A6 × chunking interaction → A6 activation-gate cascade rule | one-way (the A6 cascade IS the constraint) |
| I9 | P7 | P4 | Failure modes ↔ constraints (each failure articulates a constraint as forbidden outcome; each constraint prevents a failure) | bidirectional |
| I10 | P7 | P5 | Failure-mode mitigation logic informs recommended-approach justification | one-way |

### Assumptions-not-data check

| Piece | Assumes |
|---|---|
| P2 | The three-operation category is settled (depends on P1's commit) |
| P3 | Placement decision is settled and TranslationConfig holds the strategy enum (depends on P2's commit); strategy enum INCLUDES a "hybrid harmony-aware" literal (set by P5 round-trip) |
| P4 | Constraints can be applied to ANY strategy (not specific ones); constraints have cascade semantics — they interact, not just stack |
| P5 | Strategy enum HAS a hybrid literal slot to fill with the recommendation; constraints are explicitly enumerable (depends on P4's commit) |
| P6 | The existing 8 axes + edge-case candidates are stable inputs (frozen for this inquiry) |
| P7 | Failure modes from R8 surfacing are exhaustive at this surfacing resolution (acknowledged limitation; deferred research) |

All assumptions documented. No hidden coupling.

### Determination-mechanism piece check

The Q-tree references "LLM-detected boundaries" (strategy enum literal in P3) and "hybrid harmony-aware" (P3 literal + P5 recommendation). Whether either is applicable depends on a runtime determination — does the chunker-AI actually find valid boundaries? **P5 (feasibility + empirical validation) IS the determination-mechanism piece.** ✓ included; Reassembly check passes.

---

## Step 6 — Dependency Order

```
Level 0:  P1 (three-operation category)
              │
              ▼
Level 1:  P2 (placement)              ◀────╮
                                            │
Level 2:  P7 (failure modes — parallel-eligible with P2)
              │
              ▼
Level 3:  P4 (constraints — needs P7)  ◀───┤
                                            │
Level 4:  P6 (cross-axis — needs P2)       │
              │                             │
              ▼                             │
Level 5:  P3 (strategy enum + A4 defaults — needs P2, P4, P6, P7)
              │
              ▼
Level 6:  P5 (feasibility + recommended hybrid + validation — needs P3, P4)
```

**Parallel-eligible:**
- L1-L2: P2 and P7 can be developed in parallel (P7 sources from surfacing R8 directly; P2 sources from P1).
- L3-L4: P4 (needs P7) and P6 (needs P2) can partially parallel.

**Bidirectional I3/I4:** P3 ↔ P4 may require iteration — P3 lists candidate strategies, P4 filters which are permitted at which A6 setting, P3 absorbs the filter into its A4 × A6 matrix. Single iteration sufficient (no circularity).

**No circular dependencies.**

---

## Step 7 — Self-Evaluation

### Minimum (3 dimensions)

| Dimension | Check | Verdict |
|---|---|---|
| **Independence** | Can each piece be worked on without the others existing? | **PASS** — each piece's question is answerable in isolation through defined interfaces. P3 needs P2's placement decision but can be partially developed with placeholder assumption, then refined. |
| **Completeness** | Do the pieces cover the whole? | **PASS** — Reassembly check: P1 (what IS) + P2 (where LIVES) + P3 (what STRATEGIES) + P4 (what CONSTRAINTS) + P5 (FEASIBILITY) + P6 (CROSS-AXIS) + P7 (FAILURE MODES) fully covers SV6's stabilized model. |
| **Reassembly** | Pieces + interfaces = whole? | **PASS** — assembled, the 7 pieces + 10 interfaces reconstruct SV6's 5 committed concepts. |

### Full (additional 4 dimensions)

| Dimension | Check | Verdict |
|---|---|---|
| **Tractability** | Each piece small enough for a focused pass? | **PASS** — each piece is a focused question. P3 is the largest (8 enum literals × 5 A4 purposes ~40-cell matrix) but tractable. |
| **Interface clarity** | All cross-piece flows explicit? | **PASS** — 10 interfaces enumerated with direction; bidirectional flows marked (I3↔I4, I9); assumptions-not-data check applied. |
| **Balance** | Complexity proportional? | **MEDIUM** — P3 carries ~2-3× the weight of P1/P7 because it's the strategy matrix + A4 defaults + cross-cuts. Not 80/20 imbalanced. Acceptable: P3 is the genuine load-bearing piece for downstream Innovation. |
| **Confidence** | Top-down + bottom-up agree? | **PASS** — Step 2 boundaries match Step 3 atom-groupings. HIGH confidence. |

### Determination-mechanism piece check

P5 covers the runtime-determination for "LLM-detected" / "hybrid-harmony-aware" enum literals. Reassembly check passes.

### Failure-mode check

| Failure mode | Status |
|---|---|
| Premature decomposition | NO — sensemaking SV6 stabilized first |
| Wrong boundaries | NO — coupling-valley cuts; no high-coupling region split |
| Hidden coupling | NO — assumptions-not-data check applied; all assumptions documented |
| Missing pieces | NO — determination-mechanism check confirms P5 covers runtime-determination |
| Over-decomposition | NO — 7 pieces; consolidated framing concerns (P8/P9/P10 candidates folded into P2/P3/P5) |
| Ignoring dependencies | NO — explicit topological ordering with parallel-eligible markers |
| Imbalanced decomposition | MILD — P3 ~2-3× weight; acceptable for the load-bearing piece |

### Verdict

**PROCEED to Innovation.**

7 pieces; 10 interfaces; 6-level dependency DAG. Critical path: P1 → P2 → P6 → P3 → P5. P7 + P4 develop in parallel paths.

Downstream Innovation operates per-piece, generating candidate text for each. Critique runs adversarial testing against the candidates. Routelister enumerates onward routes.
