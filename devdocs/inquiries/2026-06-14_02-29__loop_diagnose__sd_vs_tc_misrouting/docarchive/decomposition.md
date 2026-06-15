# Decomposition — Loop Diagnose: SD vs TC Misrouting

## User Input

Input: `_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md`. SV6 stabilized: PRIMARY attribution to edge-cases sensemaking SV6 + edge-cases critique; CONTRIBUTORY to chunking principle articulation; 2 strong maintenance candidates + 1 gated contributory.

---

## Step 1 — Coupling Topology

### Elements

| # | Element | Role |
|---|---|---|
| E1 | Correction Chain Summary (prior path + corrected direction + human correction + what changed) | LOOP_DIAGNOSE required output section |
| E2 | Hypothesis 1: edge-cases sensemaking SV6 locked-in misrouting | PRIMARY failure hypothesis |
| E3 | Hypothesis 2: edge-cases critique missed principle-application correctness (with smoking-gun internal contradiction) | PRIMARY failure hypothesis |
| E4 | Hypothesis 3: chunking finding's principle anchored too specifically (CONTRIBUTORY) | CONTRIBUTORY failure hypothesis |
| E5 | Failure Attribution Summary table | LOOP_DIAGNOSE required output section |
| E6 | Maintenance Candidate 1: substance-axis sub-axis sharpening in td-critique | Strong evidence |
| E7 | Maintenance Candidate 2: comparative-pattern test as sensemaking perspective | Strong evidence |
| E8 | Maintenance Candidate 3: principle sharpening in chunking finding (gated; contributory) | Lower evidence; gated |
| E9 | Inherited Commitments Re-test (Synthesis Trigger requirement) | Re-tests chunking + edge-cases commitments |
| E10 | Diagnostic Verdict (ACTIONABLE / PARTIAL / INCONCLUSIVE) | LOOP_DIAGNOSE required output section |
| E11 | The corrected routing (3 fields → TC; 1 field → SD) — secondary constructive output per WHY-axis practical-application-now | Optional constructive content |

### Coupling clusters

**CHAIN-FRAMING cluster (E1, E9):** the Correction Chain Summary and Inherited Commitments Re-test both anchor the inquiry to specific priors. Tightly coupled (both reference same 2 inquiries).

**HYPOTHESIS cluster (E2, E3, E4):** the 3 failure hypotheses. Tightly coupled internally (each follows LOOP_DIAGNOSE's failure-hypothesis schema; attribution distributes across them).

**ATTRIBUTION cluster (E5):** the summary table that aggregates the 3 hypotheses. Strong coupling to HYPOTHESIS cluster.

**MAINTENANCE cluster (E6, E7, E8):** the 3 maintenance candidates. Tightly coupled internally (each follows the candidate schema). MC1 + MC2 are strong; MC3 is gated.

**VERDICT cluster (E10):** the diagnostic verdict aggregating overall confidence.

**CONSTRUCTIVE cluster (E11):** the corrected routing — secondary to the diagnostic but addresses the user's WHY-axis `practical-application-now`.

### Coupling valleys (boundaries)

- CHAIN-FRAMING ↔ HYPOTHESIS — moderate (chain framing provides context; hypotheses operate on it)
- HYPOTHESIS ↔ ATTRIBUTION — strong (attribution aggregates hypotheses; can be one piece, but separable for output clarity)
- HYPOTHESIS ↔ MAINTENANCE — moderate (each maintenance candidate addresses one or more hypotheses)
- MAINTENANCE ↔ VERDICT — moderate (verdict depends on whether maintenance candidates have concrete gates)
- CONSTRUCTIVE ↔ all — low (independent secondary output)

---

## Step 2 — Boundaries (Top-Down)

Pieces:

1. **P1 — Correction Chain Summary** (E1)
2. **P2 — Failure Hypothesis 1** (edge-cases sensemaking SV6 locked-in misrouting — E2)
3. **P3 — Failure Hypothesis 2** (edge-cases critique missed principle-application correctness — E3)
4. **P4 — Failure Hypothesis 3** (chunking finding principle articulation contributory — E4)
5. **P5 — Failure Attribution Summary table** (E5)
6. **P6 — Maintenance Candidate 1: substance-axis sub-axis** (E6)
7. **P7 — Maintenance Candidate 2: comparative-pattern perspective** (E7)
8. **P8 — Maintenance Candidate 3: chunking principle sharpening (gated)** (E8)
9. **P9 — Inherited Commitments Re-test** (E9)
10. **P10 — Diagnostic Verdict** (E10)
11. **P11 — Corrected routing (secondary constructive output)** (E11)

11 pieces. Note: per LOOP_DIAGNOSE's required-output structure, these map directly to the finding's sections; the decomposition mirrors the protocol's deliverable shape.

---

## Step 3 — Boundary Validation (Bottom-Up Check)

Atoms:

| Atom | Natural home |
|---|---|
| Prior path 1 (chunking) + Prior path 2 (edge-cases) + corrected direction + human correction quote | P1 |
| Hypothesis 1 schema (8 fields per LOOP_DIAGNOSE: affected-stage / shortcoming-type / evidence-prior / evidence-correction / evidence-corrected / confidence / why-not-stronger / maintenance-candidate / evaluation-gate) | P2 |
| Hypothesis 2 schema (same 8 fields) | P3 |
| Hypothesis 3 schema (same 8 fields) | P4 |
| 3-row attribution table | P5 |
| MC1 schema (what / file-affected / risk-class / expected-benefit / evaluation-gate / branch-experiment?) | P6 |
| MC2 schema (same 6 fields) | P7 |
| MC3 schema (same 6 fields; gated) | P8 |
| 14 Inherited Commitments (9 chunking + 5 edge-cases) each with RE-TESTED status | P9 |
| Verdict + best-supported-diagnosis + strongest-MC + main-uncertainty + next-step | P10 |
| 4-row corrected routing table | P11 |

All atoms assigned cleanly. No splits across pieces. HIGH confidence.

---

## Step 4 — Question Tree (compact)

| Piece | Question |
|---|---|
| P1 | What is the correction chain (priors + correction signal + what changed)? |
| P2 | Was edge-cases sensemaking SV6 the locus where the misrouting was first locked in? Evidence? |
| P3 | Did edge-cases critique miss principle-application correctness? Smoking-gun? |
| P4 | Did chunking finding's principle articulation contribute by being anchored too specifically? |
| P5 | What is the aggregate attribution across hypotheses (table)? |
| P6 | What does a substance-axis sub-axis sharpening in td-critique look like, and what's its evaluation gate? |
| P7 | What does a comparative-pattern sensemaking perspective look like, and what's its evaluation gate? |
| P8 | What does a chunking-principle sharpening look like; why is it gated? |
| P9 | Which inherited commitments from the 2 priors hold, are revised, or are invalidated? |
| P10 | What is the diagnostic verdict (ACTIONABLE/PARTIAL/INCONCLUSIVE) + best-supported diagnosis + recommended next step? |
| P11 | What is the corrected routing for the 4 misrouted fields? |

Verification criteria are LOOP_DIAGNOSE-protocol-shaped per piece (omitted here for brevity; the schemas are well-specified in `loop_diagnose.md` Step 4).

---

## Step 5 — Interfaces (compact)

| ID | From | To | Flow | Direction |
|---|---|---|---|---|
| I1 | P1 | P2-P4 | priors + correction context → hypotheses operate on it | one-way |
| I2 | P2-P4 | P5 | individual hypotheses → attribution aggregate | one-way |
| I3 | P2-P4 | P6-P8 | each hypothesis → maintenance candidate addressing it | one-way (P2→P6; P3→P6; P4→P8; etc.) |
| I4 | P5 + P6-P8 | P10 | attribution + candidates → verdict | one-way |
| I5 | P1 + P2-P4 | P9 | priors + hypotheses → re-test of inherited commitments | one-way |
| I6 | All | P11 | secondary constructive output (independent) | independent |

**Assumptions:** P9 assumes chunking + edge-cases inquiries are the only priors (yes per Synthesis Trigger). P11 assumes the corrected routing is a useful secondary output (per WHY-axis `practical-application-now`). All explicit.

---

## Step 6 — Dependency Order

```
L0:  P1 (Correction Chain Summary)
        ▼
L1:  P2 + P3 + P4 (3 hypotheses, parallel)
        ▼
L2:  P5 (Attribution Summary), P9 (Inherited Re-test) — parallel
        ▼
L3:  P6 + P7 + P8 (3 Maintenance Candidates — parallel)
        ▼
L4:  P10 (Verdict)

Independent: P11 (secondary corrected routing)
```

Parallel-eligible: 3 hypotheses at L1; attribution + re-test at L2; 3 candidates at L3.

---

## Step 7 — Self-Evaluation

| Dimension | Verdict |
|---|---|
| Independence | PASS — each piece answerable via interfaces |
| Completeness | PASS — covers LOOP_DIAGNOSE's required output sections + Synthesis Re-test + constructive secondary |
| Reassembly | PASS — pieces + interfaces reconstruct a LOOP_DIAGNOSE-protocol-compliant finding |
| Tractability | PASS — each piece is focused |
| Interface clarity | PASS — 6 interfaces enumerated |
| Balance | MEDIUM — P9 (14-commitment re-test) is the largest; acceptable for Synthesis-rigor |
| Confidence | PASS |

Failure-mode check: NONE fired.

### Verdict

**PROCEED to Innovation.**

11 pieces; 6 interfaces; 4-level dependency DAG. Critical path: P1 → P2/P3/P4 → P5 → P10.
