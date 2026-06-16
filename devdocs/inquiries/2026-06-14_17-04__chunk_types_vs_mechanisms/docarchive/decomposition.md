# Decomposition — Chunk Types vs Mechanisms

## User Input

Input: `_branch.md` + upstream `articulate_simple.md` + `surfacing.md` + `sensemaking.md`. SV6 stabilized model: 7-component architecture.

---

## Step 1 — Coupling Topology

### Elements

| # | Element | Role |
|---|---|---|
| E1 | TC field spec: `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"] = "paragraph"` | central schema commitment |
| E2 | SD ChunkingUnit addition: `canonical_level: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]` | corpus-type-to-ladder mapping |
| E3 | PipelineConfig optional override: `chunking_mechanism_override: Literal[...] \| None = None` | advanced/eval use |
| E4 | Default mechanism (hidden): hybrid harmony-aware per chunking finding | AI implementation |
| E5 | A4-driven defaults revision (types-only) | preserved A4 pattern |
| E6 | Cross-cutting Tier 1-2 hard constraint | preserved |
| E7 | Inherited Commitments Re-test | Synthesis Trigger requirement |
| E8 | MC1 + MC2 strengthened evidence | LOOP_DIAGNOSE branch-test outcome |
| E9 | LOOP_DIAGNOSE finding note ("survived intact" too strong; routings-correct stands) | meta-output |
| E10 | Migration plan (chunking finding text + config_base_source.md updates) | propagation |

### Coupling clusters

- **SCHEMA cluster (E1, E2, E3, E4):** tight coupling — the 4 schema components together define the revised architecture.
- **DEFAULTS cluster (E5):** moderate coupling to SCHEMA (defaults reference E1's enum values).
- **CONSTRAINTS cluster (E6):** low coupling — constraint applies regardless of schema shape.
- **SYNTHESIS cluster (E7):** moderate coupling to all schema pieces (re-tests their inherited commitments).
- **META cluster (E8, E9):** loose coupling — outputs about the LOOP_DIAGNOSE process itself.
- **MIGRATION cluster (E10):** depends on SCHEMA + DEFAULTS being settled.

---

## Step 2 — Boundaries

Pieces:

1. **P1 — TC chunking_granularity field spec** (E1)
2. **P2 — SD ChunkingUnit canonical_level addition** (E2)
3. **P3 — PipelineConfig mechanism override** (E3)
4. **P4 — Default mechanism (hidden) documentation** (E4)
5. **P5 — A4 defaults revision** (E5)
6. **P6 — Cross-cutting constraints preservation note** (E6)
7. **P7 — Inherited Commitments Re-test** (E7)
8. **P8 — MC1 + MC2 evidence note (LOOP_DIAGNOSE branch-test outcome)** (E8)
9. **P9 — LOOP_DIAGNOSE finding revision note** (E9)
10. **P10 — Migration plan** (E10)

10 pieces.

---

## Step 3 — Boundary Validation (Bottom-Up)

Atoms cleanly assigned. The 5 enum literals → P1; the 5 corpus mappings (Nursi mesele≈subchapter etc.) → P2; the override enum → P3; the hybrid harmony-aware mechanism spec → P4; the 5 A4 defaults → P5; the 3 hard constraints (Tier 1-2 / multi-meaning lower bound / A6 cascade) → P6; chunking + LOOP_DIAGNOSE commitments → P7; MC1 + MC2 strengthened-evidence → P8; "survived intact" too strong + routings-correct stands → P9; chunking finding text + config_base_source updates → P10. HIGH confidence.

---

## Step 4 — Question Tree (compact)

| Piece | Question |
|---|---|
| P1 | What is the TC chunking_granularity field signature, enum, default, and rationale? |
| P2 | What field is added to SD's ChunkingUnit to map corpus-types to the canonical ladder, and what are the Nursi/Bible/Quran/Hindu mappings? |
| P3 | What does the PipelineConfig optional mechanism override look like, and when does it fire? |
| P4 | What is the default mechanism (hidden) and how does the AI apply it? |
| P5 | What are the revised A4-driven defaults for chunking_granularity? |
| P6 | What cross-cutting constraints survive the redesign? |
| P7 | Which chunking finding commitments + LOOP_DIAGNOSE commitments hold / are revised / are invalidated? |
| P8 | How does this inquiry's outcome strengthen MC1 + MC2's evidence for promotion? |
| P9 | What note needs to be added to the LOOP_DIAGNOSE finding about its "survived intact" framing? |
| P10 | What is the migration plan (chunking finding text + config_base_source.md updates)? |

---

## Step 5 — Interfaces

| ID | From | To | Flow | Direction |
|---|---|---|---|---|
| I1 | P1 | P2 | TC's canonical ladder defines SD's canonical_level enum domain | one-way |
| I2 | P1 | P5 | TC enum is the value domain for A4 defaults | one-way |
| I3 | P4 | P3 | Default mechanism content informs override's enum values | one-way |
| I4 | P1, P2, P3, P4 | P6 | Cross-cutting constraints apply across schema pieces | one-way |
| I5 | All schema (P1-P5) | P7 | Inherited commitments re-tested per piece | one-way |
| I6 | P1-P9 | P10 | Migration plan integrates all preceding | one-way |
| I7 | P1, P2, P3 | P8 | MC2 catches the conflation across schema pieces; MC1 catches internal contradiction in chunking_strategy literals | one-way |

---

## Step 6 — Dependency Order

```
L0:  P1 (TC chunking_granularity)
        ▼
L1:  P2 (SD canonical_level), P3 (PipelineConfig override), P4 (default mechanism) — parallel
        ▼
L2:  P5 (A4 defaults), P6 (constraints) — parallel
        ▼
L3:  P7 (Inherited Re-test), P8 (MC evidence), P9 (LOOP_DIAGNOSE note) — parallel
        ▼
L4:  P10 (Migration plan)
```

Critical path: P1 → P2/P3/P4 → P5/P6 → P7 → P10.

---

## Step 7 — Self-Evaluation

| Dimension | Verdict |
|---|---|
| Independence | PASS |
| Completeness | PASS — covers SV6 stabilized model + Synthesis Re-test + meta-outputs + migration |
| Reassembly | PASS |
| Tractability | PASS |
| Interface clarity | PASS — 7 interfaces enumerated |
| Balance | MEDIUM — P1 + P10 are larger; acceptable |
| Confidence | PASS |

Failure-mode check: NONE fired.

### Verdict

**PROCEED to Innovation.**

10 pieces; 7 interfaces; 4-level DAG.
