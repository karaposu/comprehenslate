# Decomposition — Edge-Cases into Config Schema

## User Input

Input: `_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md` in same folder. SV6 stabilized model: 14 edge-cases resolve to 3 ALREADY-ROUTED + 4 ADD-now-to-SourceDescriptor + 7 DEFER; TranslationConfig gains 0 new fields.

---

## Step 1 — Coupling Topology

### Elements

| # | Element | Role |
|---|---|---|
| E1 | Per-field decision table (14 rows × outcome × schema-home × phase) | central spine |
| E2 | Chunking finding's pre-routing (#1 → is_atomic, #6 → attached_to, #7 → orthogonal) — re-test | inherited commitment |
| E3 | Group α/β/γ Assembly proposal from edge-cases innovation — re-test | inherited commitment |
| E4 | SourceDescriptor additions: #2 `source_language_fluency`, #3 `source_edition`, #8 `quranic_citation_policy` (within EmbeddedLanguagePolicy), #13 `source_temporal_register` | Phase 2 schema work |
| E5 | DEFER specifications with revival triggers: #4, #5, #9, #10, #11, #12, #14 | Phase 3 deferrals |
| E6 | Non-modification commitments: A3 stays as-is; Group γ UseContext deferred as schema | explicit non-actions |
| E7 | Cross-axis conflict check: verify no breaks with A1-A8 + Layer-2 policies + chunking commitments | gate for additions |
| E8 | Migration phase sequencing: Phase 1 / Phase 2 / Phase 3 with gates | wrapper |
| E9 | Code sketches for the 4 SourceDescriptor additions | implementation-readiness output |

### Coupling clusters

**SPINE cluster (E1):** the per-field table is the central organizing artifact. Every other cluster references it.

**INHERITED-COMMITMENT cluster (E2, E3):** the chunking-finding pre-routing + Group α/β/γ Assembly proposal are inherited and need re-test treatment per CONCLUDE's Inherited Commitments Re-test requirement.

**SCHEMA-ADDITION cluster (E4, E9):** the 4 SourceDescriptor additions + their code sketches.

**DEFER-SPECIFICATION cluster (E5):** the 7 DEFER entries with revival triggers.

**NON-MODIFICATION cluster (E6):** the explicit "don't do this" commitments (A3, UseContext).

**CONFLICT-CHECK cluster (E7):** the gate that validates additions don't break existing.

**MIGRATION cluster (E8):** the phased wrapper tying everything together.

### Coupling valleys

- SPINE ↔ all other clusters — moderate (each cluster elaborates one column/row of the spine)
- INHERITED-COMMITMENT ↔ SCHEMA-ADDITION — low (inherited cases ARE NOT being added; they're being ratified)
- SCHEMA-ADDITION ↔ DEFER — low (different outcomes)
- NON-MODIFICATION ↔ all — low (explicit non-actions; clean boundary)
- CONFLICT-CHECK ↔ SCHEMA-ADDITION — moderate (check operates on additions)
- MIGRATION ↔ all — moderate (every decision has a phase)

---

## Step 2 — Boundaries (Top-Down)

Cut at the valleys. Initial piece set (7 pieces):

1. **P1 — Per-field decision table** (SPINE)
2. **P2 — Inherited-commitment re-test** (chunking finding + Group α/β/γ; the Inherited-Commitments-Re-test work)
3. **P3 — SourceDescriptor addition sketches** (4 fields with code shape)
4. **P4 — DEFER revival-trigger specifications** (7 deferred fields)
5. **P5 — Non-modification commitments** (A3 + UseContext)
6. **P6 — Cross-axis conflict check** (gate against A1-A8 + Layer-2 policies + chunking commitments)
7. **P7 — Migration phase sequencing** (Phase 1 / 2 / 3 with gates)

---

## Step 3 — Boundary Validation (Bottom-Up Check)

Atoms:

| Atom | Natural home |
|---|---|
| 14 per-field rows (one per edge-case) | P1 |
| Each row's outcome + schema-home + phase + notes | P1 |
| chunking finding pre-routing for #1 → ChunkingUnit.is_atomic | P2 |
| chunking finding pre-routing for #6 → ChunkingUnit.attached_to | P2 |
| chunking finding pre-disposition for #7 → orthogonal sister-concept | P2 |
| Group α/β/γ Assembly proposal | P2 |
| #2 source_language_fluency field sketch | P3 |
| #3 source_edition field sketch | P3 |
| #8 quranic_citation_policy as EmbeddedLanguagePolicy property | P3 |
| #13 source_temporal_register field sketch | P3 |
| 7 DEFER entries with revival triggers (one per deferred field) | P4 |
| "A3 stays as-is" non-modification | P5 |
| "Group γ UseContext deferred as schema" non-modification | P5 |
| Per-axis cross-axis interaction notes (A1-A8) | P6 |
| Per-Layer-2-policy compatibility notes (5 policies) | P6 |
| Per-chunking-commitment compatibility notes | P6 |
| Phase 1 definition + gate (ratify pre-routing; what unblocks) | P7 |
| Phase 2 definition + gate (depends on SourceDescriptor schema existing) | P7 |
| Phase 3 definition + gate (revival triggers from P4) | P7 |

All atoms assigned cleanly. No split across pieces. No atom grouped that should be independent. **HIGH confidence.**

---

## Step 4 — Question Tree

### P1 — Per-field decision table

**Question:** What is the per-field decision (outcome × schema-home × phase) for each of the 14 edge-cases?

**Verification:**
- [ ] Table with 14 rows
- [ ] Outcome column ∈ {ALREADY-ROUTED / ADD-now / REFINE-existing-axis / DEFER / REJECT} per row
- [ ] Schema-home column populated when outcome = ADD-now
- [ ] Phase column ∈ {Phase 1 / Phase 2 / Phase 3} per row
- [ ] Notes column with brief reasoning per row

### P2 — Inherited-commitment re-test

**Question:** Which inherited commitments from the synthesis priors (chunking finding + edge-cases innovation Assembly) are RE-TESTED-OK / RE-TESTED-REVISED / INHERITED-WITHOUT-RE-TEST?

**Verification:**
- [ ] Each inherited commitment listed with source path
- [ ] Re-test status assigned per commitment
- [ ] Evidence cited for each RE-TESTED status
- [ ] Reason cited for each INHERITED-WITHOUT-RE-TEST
- [ ] Specifically covers: chunking finding's #1 / #6 / #7 dispositions; chunking finding's split-placement decision; edge-cases innovation's Group α / β / γ; user's anti-bloat preference

### P3 — SourceDescriptor addition sketches

**Question:** What does each SourceDescriptor addition look like as a pydantic field signature?

**Verification:**
- [ ] 4 fields with signatures: #2 `source_language_fluency`, #3 `source_edition`, #8 `quranic_citation_policy` (as EmbeddedLanguagePolicy property, not top-level), #13 `source_temporal_register`
- [ ] Each with appropriate type and default
- [ ] Each with corpus-applicability note (Nursi-specific vs pattern-level)
- [ ] Compose with chunking finding's SourceDescriptor + ChunkingUnit fields

### P4 — DEFER revival-trigger specifications

**Question:** For each of the 7 DEFER decisions, what is the explicit revival trigger?

**Verification:**
- [ ] 7 deferred fields (#4 / #5 / #9 / #10 / #11 / #12 / #14) each with revival trigger
- [ ] Each trigger is time-bound / condition-bound / observable per protocol style rule
- [ ] Reason for deferral cited per entry

### P5 — Non-modification commitments

**Question:** What modifications are explicitly NOT being made, and why?

**Verification:**
- [ ] A3 stays as-is (do not split into source_culture + source_language)
- [ ] Group γ UseContext deferred as schema commitment
- [ ] Reasoning per non-modification (composability with existing axes; incremental-addition pattern; 3-schemas-in-one-push violation)

### P6 — Cross-axis conflict check

**Question:** Does the per-field routing conflict with any existing commitment (A1-A8 + 5 Layer-2 policies + chunking commitments)?

**Verification:**
- [ ] Each addition (#2 / #3 / #8 / #13) checked against A1-A8
- [ ] Each addition checked against 5 always-on Layer-2 policies (multi-meaning preservation; register-alternation; polysemy disambiguation via local construction; nazm preservation; no-smoothing)
- [ ] Each addition checked against chunking commitments
- [ ] Cross-axis interactions documented per addition

### P7 — Migration phase sequencing

**Question:** What is the migration phase for each decision, with explicit gates?

**Verification:**
- [ ] Phase 1 items listed (3 ratify-pre-routing items: #1 / #6 / #7)
- [ ] Phase 2 items listed (4 SourceDescriptor additions: #2 / #3 / #8 / #13) with gate ("SourceDescriptor schema must exist")
- [ ] Phase 3 items listed (7 DEFER) with revival triggers (referencing P4)
- [ ] Non-modifications documented as "no migration needed" per P5

---

## Step 5 — Interface Map

| ID | From | To | What flows | Direction |
|---|---|---|---|---|
| I1 | P1 ↔ P2 | per-field table cites inherited commitments for ALREADY-ROUTED rows; re-test confirms which commitments hold | bidirectional |
| I2 | P1 | P3 | which fields land in SourceDescriptor (4 rows from P1 expand to code sketches) | one-way |
| I3 | P1 | P4 | which fields DEFER (7 rows from P1 expand to revival triggers) | one-way |
| I4 | P1 | P5 | non-modification entries reference the explicit "do not" decisions | one-way |
| I5 | P3 | P6 | SourceDescriptor additions are the input to cross-axis conflict check | one-way |
| I6 | P4 | P7 | DEFER revival triggers become Phase 3 entries with explicit gates | one-way |
| I7 | P2 | P7 | ALREADY-ROUTED commitments are Phase 1 items in migration plan | one-way |
| I8 | P3 | P7 | SourceDescriptor additions are Phase 2 items in migration plan | one-way |
| I9 | P6 | P1 | back-flow: cross-axis conflicts may force changes to per-field decisions | back-flow (makes I5↔I9 bidirectional under conflict) |
| I10 | P5 | P7 | non-modifications are documented as "no migration needed" entries | one-way |

### Assumptions-not-data check

| Piece | Assumes |
|---|---|
| P1 | The 7 routing-outcome categories from SV6 are settled |
| P2 | Chunking finding's pre-routing is the source of truth for #1, #6, #7 |
| P3 | SourceDescriptor schema either exists or will be built per chunking finding's MUST item |
| P4 | Revival triggers can be expressed as time-bound / condition-bound / observable |
| P5 | A3's current state is stable (no in-flight modification inquiry) |
| P6 | The 8 axes + 5 Layer-2 policies + chunking commitments are stable inputs |
| P7 | Phase 1/2/3 categorization is exhaustive for the 14 decisions |

All assumptions documented. No hidden coupling.

### Determination-mechanism piece check

The Q-tree includes "DEFER until revival trigger fires" — runtime determination of when a deferred field becomes active. **P4 IS the determination-mechanism piece** (specifies HOW the revival trigger is checked: per-entry time-bound / condition-bound / observable signal). ✓ Reassembly check passes.

---

## Step 6 — Dependency Order

```
Level 0:  P1 (per-field table — spine; no internal deps)
              │
              ▼
Level 1:  P2 (inherited re-test — needs P1's ALREADY-ROUTED rows identified)
              │
              ▼
Level 2:  P3 (SourceDescriptor sketches — needs P1's ADD-now rows)
              │   parallel
              ├── P4 (DEFER revival triggers — needs P1's DEFER rows)
              │   parallel
              └── P5 (non-modifications — needs P1's explicit-NO entries)
              │
              ▼
Level 3:  P6 (cross-axis conflict check — needs P3 additions to check)
              │
              ▼
Level 4:  P7 (migration plan — needs P2 + P3 + P4 + P5 + P6 all complete)
```

**Critical path:** P1 → P3 → P6 → P7.
**Parallel-eligible:** P3, P4, P5 at Level 2 (consume P1 independently).
**Bidirectional I1, I9:** P1 ↔ P2 may iterate once; P6 may force P1 revision under conflict. Single iteration sufficient.
**No circular dependencies.**

---

## Step 7 — Self-Evaluation

### Minimum (3 dimensions)

| Dimension | Check | Verdict |
|---|---|---|
| **Independence** | Each piece answerable in isolation through defined interfaces? | **PASS** — P1 is spine but P2-P7 each cite specific rows; no cross-reading required |
| **Completeness** | Pieces cover the whole SV6 model? | **PASS** — table (P1) + inherited (P2) + adds (P3) + defers (P4) + non-mods (P5) + check (P6) + phasing (P7) covers all of SV6's stabilized commitments |
| **Reassembly** | Pieces + interfaces reconstruct SV6? | **PASS** — final assembly produces the per-field routing + migration plan + inherited-commitment-re-test + cross-axis-conflict-verified output that SV6 specifies |

### Full (additional 4 dimensions)

| Dimension | Check | Verdict |
|---|---|---|
| **Tractability** | Each piece focused for single pass? | **PASS** — P3 is the widest (4 sketches) but tractable |
| **Interface clarity** | All cross-piece flows explicit? | **PASS** — 10 interfaces enumerated; 2 bidirectional flagged; assumptions documented |
| **Balance** | Complexity proportional? | **MEDIUM** — P1 and P7 are larger than P5; P5 is small (2 explicit non-mods); not 80/20 imbalanced |
| **Confidence** | Top-down + bottom-up agree? | **PASS** — Step 2 boundaries match Step 3 atom-groupings. HIGH confidence |

### Determination-mechanism piece check

P4 covers DEFER revival triggers as the determination mechanism. ✓ Reassembly passes.

### Failure-mode check

| Mode | Status |
|---|---|
| Premature decomposition | NO — sensemaking SV6 stabilized first |
| Wrong boundaries | NO — coupling-valley cuts |
| Hidden coupling | NO — assumptions-not-data check applied |
| Missing pieces | NO — determination-mechanism check confirms P4 covers DEFER runtime |
| Over-decomposition | NO — 7 pieces; P5 is small but warrants separation (explicit non-actions are structurally distinct from actions) |
| Ignoring dependencies | NO — explicit topological ordering |
| Imbalanced decomposition | MILD — P1+P7 larger than P5; acceptable |

### Verdict

**PROCEED to Innovation.**

7 pieces; 10 interfaces (2 bidirectional); 4-level dependency DAG. Critical path: P1 → P3 → P6 → P7. Parallel-eligible: P3, P4, P5 at L2.
