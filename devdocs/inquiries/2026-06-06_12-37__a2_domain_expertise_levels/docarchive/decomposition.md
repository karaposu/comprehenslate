# Decomposition — a2_domain_expertise_levels

## User Input
`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-06_12-37__a2_domain_expertise_levels/_branch.md` (with prior outputs: surfacing.md, sensemaking.md)

---

## Step 1 — Coupling Topology

### Elements identified (from sensemaking SV6)

- E1 5 levels with labels `lay | aware | educated | trained | expert`
- E2 5 stratification dimensions rising together (technical-vocabulary depth + conceptual schema + discourse conventions + specialist debates + primary-source canon familiarity)
- E3 4-component template: reader profile + expertise-depth-tier + discourse-register-tier + domain-handling-test
- E4 9 handling actions in 2 categories + 1 bridge (vocabulary-level: USE-FREELY / INLINE-DEFINE / FOOTNOTE / PARAPHRASE; discourse-level: INVOKE-DEBATES / ATTRIBUTE-TO-SCHOOL / UNATTRIBUTED-CONSENSUS / AVOID-DEBATES; bridge: KEEP-SOURCE-TERM-WITH-GLOSS)
- E5 5 per-level concept definitions
- E6 Distinguishing logic between 4 adjacent-level boundaries (explicit per user's directive)
- E7 Cross-domain examples per level (5 domains × 5 levels = 25 example clusters)
- E8 Single-domain default commitment (source's domain implicit at runtime)
- E9 Reader-relative commitment (configuration captures reader's expertise)
- E10 Receptive-only commitment
- E11 Conservative-bias LOWER default
- E12 A2↔A1 boundary (general fluency vs domain-specialist knowledge; same-word-fires-both)
- E13 A2↔A3 boundary (competence vs identity; four-corners)
- E14 A2↔A4 boundary (expertise vs purpose; independence demonstrated)
- E15 5 forward-tagged specialist canons from A1's cultural-reference-recognition (legal / math / science / medical / specialist-philosophy) received
- E16 Plain-ordinal pattern (no sub-fields, no propagation)
- E17 12 Inherited Commitments re-test (IC1-IC12: 9 inherited + 3 NEW)
- E18 Translator-AI runtime determination (AI judges term's domain-specialist-ness at runtime based on training)

### Coupling map

Major clusters (high internal coupling):

**Cluster A — Framework core:** E1, E2, E3, E4, E8, E9, E10, E11, E16, E18. STRONG internal coupling — labels + 5 dimensions + template + actions + orthogonal commitments + runtime determination form a coherent foundation.

**Cluster B — Per-level instantiation:** E5, E6, E7. STRONG internal coupling — per-level definitions + distinguishing logic + cross-domain examples co-vary.

**Cluster C — Cross-axis boundaries:** E12, E13, E14. STRONG internal coupling — three boundary statements sharing structure (criterion + independence demonstration).

**Cluster D — Forward-tagged canons integration:** E15. Atomic.

**Cluster E — Meta:** E17 (Inherited Commitments Re-test).

Inter-cluster coupling:

| Pair | Coupling | Reason |
|---|---|---|
| A ↔ B | STRONG | per-level instantiation embeds framework |
| A ↔ C | MODERATE | boundary statements reference framework concepts (domain-specialist vs general fluency) |
| A ↔ D | STRONG | forward-tagged canons mapped to framework's 5 levels via expertise-depth dimension |
| A ↔ E | WEAK | meta references framework but is largely independent |
| B ↔ C | MODERATE | boundary statements cite per-level examples |
| B ↔ D | STRONG | per-level examples include specialist canon examples |
| B ↔ E | WEAK | independent |
| C ↔ D | WEAK | independent |
| C ↔ E | WEAK | independent |
| D ↔ E | WEAK | independent |

### Coupling-valley boundaries

- Between {A, B, D} (highly coupled framework + per-level + specialist-canons) and {C} (boundaries) and {E} (IC re-test): clean valleys
- {C} (boundaries) is mostly independent of the framework-instantiation cluster; can be authored in parallel

---

## Step 2 — Detect Boundaries (Top-Down)

Initial boundary set produces these candidate pieces:

| # | Piece | Cluster source | Internal coupling | External coupling |
|---|---|---|---|---|
| P1 | Framework (4-component template + 5 expertise-depth tiers + 9 handling actions + orthogonal-axes commitments + runtime determination) | A | STRONG | MODERATE to P2, P4, P5 |
| P2 | 5 per-level definitions + distinguishing logic + cross-domain examples | B | STRONG | depends on P1 |
| P3 | Cross-axis boundaries (A2↔A1, A2↔A3, A2↔A4) | C | STRONG | WEAK to all (independent) |
| P4 | 5 forward-tagged specialist canons integration | D | atomic | depends on P1, P2 |
| P5 | Inherited Commitments Re-test (12 ICs) | E | atomic | depends on all |

---

## Step 3 — Validate Boundaries (Bottom-Up)

Identify obvious irreducible atoms and check they group naturally:

| Atom | Natural piece | Match? |
|---|---|---|
| 4-component template structure | P1 | ✓ |
| 5 expertise-depth tier labels | P1 | ✓ |
| Reader-relative single-domain commitment | P1 | ✓ |
| Receptive-only commitment | P1 | ✓ |
| Conservative-bias LOWER commitment | P1 | ✓ |
| Plain-ordinal pattern statement | P1 | ✓ |
| Translator-AI runtime determination note | P1 | ✓ |
| 4-action vocabulary-level vocabulary | P1 | ✓ |
| 4-action discourse-level vocabulary | P1 | ✓ |
| 1 bridge action (KEEP-SOURCE-TERM-WITH-GLOSS) | P1 | ✓ |
| `lay` 4-component definition | P2 | ✓ |
| `aware` 4-component definition | P2 | ✓ |
| `educated` 4-component definition | P2 | ✓ |
| `trained` 4-component definition | P2 | ✓ |
| `expert` 4-component definition | P2 | ✓ |
| 4 adjacent-level distinguishing logics (explicit per user) | P2 | ✓ |
| Cross-domain examples per level (5 × 5 = 25 clusters) | P2 | ✓ |
| Said Nursi corpus example progression | P2 | ✓ |
| A2↔A1 same-word-fires-both criterion | P3 | ✓ |
| A2↔A3 competence-vs-identity four-corners | P3 | ✓ |
| A2↔A4 expertise-vs-purpose independence | P3 | ✓ |
| Forward-tagged 5 specialist canons mapped to A2 levels | P4 | ✓ |
| 12 inherited commitments + verdicts | P5 | ✓ |

All atoms align with top-down boundaries. **Confidence: HIGH.**

---

## Step 4 — Question Tree

### P1 — Framework
**Question:** What is the framework for A2 — Domain Expertise: the 4-component template, the 5 expertise-depth tiers (1-to-1 with reader levels `lay | aware | educated | trained | expert`), the 9 handling actions (4 vocabulary-level + 4 discourse-level + 1 bridge), and the orthogonal-axes commitments (single-domain default, reader-relative, receptive-only, conservative-bias LOWER, plain-ordinal pattern, translator-AI runtime determination)?

**Verification:**
- [ ] 4-component template stated with each component's role (reader profile + expertise-depth-tier + discourse-register-tier + domain-handling-test)
- [ ] 5 expertise-depth tiers labeled 1-to-1 with reader levels
- [ ] 5 stratification dimensions enumerated (technical-vocabulary depth + conceptual schema + discourse conventions + specialist debates + primary-source canon familiarity)
- [ ] 9 handling actions named with role per action
- [ ] Single-domain default explicit (with audience-level hand-off note for multi-domain future inquiry)
- [ ] Reader-relative commitment explicit
- [ ] Receptive-only commitment explicit
- [ ] Conservative-bias LOWER default explicit
- [ ] Plain-ordinal pattern explicit (no sub-fields)
- [ ] Translator-AI runtime determination noted (AI judges term's specialist-ness at runtime; reader-level config specifies what the reader recognizes)
- [ ] Template adaptation tagged MEDIUM (parallel to A1 inference-capacity's MEDIUM; cleanly between idiom's LIGHT and syntax's HEAVY)

### P2 — 5 Per-Level Definitions
**Question:** For each of 5 levels (`lay | aware | educated | trained | expert`), what is the 4-component definition + at least 3-domain example spread + explicit distinguishing logic from adjacent levels (the user's flagged "main challenge")?

**Verification:**
- [ ] 5 level definitions with all 4 components each
- [ ] Each level has examples spread across at least 3 different domains (Islamic theology + biblical + philosophy + science + law)
- [ ] Each of 4 adjacent-level boundaries has explicit distinguishing logic in prose (per user directive)
- [ ] Said Nursi corpus example included at each appropriate level (the project's primary corpus)
- [ ] Receptive-only framing maintained per level
- [ ] Per-level handling test specifies which actions fire at which level for which term types
- [ ] Conservative-bias commitment reflected per level
- [ ] "Educated-IN-THIS-DOMAIN" framing explicit at level 3 to prevent A1 conflation

### P3 — Cross-Axis Boundaries
**Question:** What are the explicit boundaries between A2 and the adjacent axes (A1 general reading fluency, A3 cultural identity, A4 purpose), with criterion + four-corners independence demonstration per boundary?

**Verification:**
- [ ] A2↔A1 boundary: criterion (general fluency vs domain-specialist knowledge); same-word-fires-both example ("ratiocination" → A1 general vocab; "isnād" → A2 Islamic-studies vocab); independence example (non-native ESL Bible scholar)
- [ ] A2↔A3 boundary: criterion (competence-based vs identity-based); four-corners independence demonstration (specialist-outsider; lay-source-native; specialist-source-native; lay-outsider)
- [ ] A2↔A4 boundary: criterion (expertise vs purpose); independence example (specialist reading for casual purpose; lay reading for scholarly purpose)
- [ ] All three boundary criteria stated cleanly enough for the translator-AI to apply at runtime (when to fire A1 vs A2 vs A3 handling for an encountered item)

### P4 — Forward-Tagged 5 Specialist Canons Integration
**Question:** How are the 5 forward-tagged specialist canons from `a1_cultural_reference_recognition_levels/finding.md` (legal precedents / mathematical figures / scientific figures / medical eponyms / specialist philosophy) received into A2's framework via the expertise-depth dimension?

**Verification:**
- [ ] Each of 5 specialist domains mapped to A2's 5 levels (lay → expert progression)
- [ ] Per-domain example progression for each specialist canon
- [ ] Boundary criterion from A1 ("general cultural literacy → A1; domain training required → A2") cited as forward-tagging justification
- [ ] Note that within any given translation job, only ONE of these 5 specialist domains is the source's domain (single-domain commitment from P1)
- [ ] Gray-zone cases acknowledged (Einstein, Pythagorean theorem, Marx — references that migrated specialist→general; the A1 finding's gray-zone list inherited)

### P5 — Inherited Commitments Re-test
**Question:** How are the 12 inherited commitments (9 inherited from root + A1 chain + 3 NEW to this inquiry) re-tested with cited evidence?

**Verification:**
- [ ] All 12 ICs named (IC1-IC12)
- [ ] Each marked: RE-TESTED OK / RE-TESTED & REFINED / RE-TESTED & APPLIED / INHERITED-WITHOUT-RE-TEST (with reason) / NEW
- [ ] Re-test verdicts cite the corresponding sensemaking ambiguity-resolution or framework decision
- [ ] IC10 (domain-meaningful labels), IC11 (single-domain default), IC12 (9-action vocabulary) explicitly marked NEW

---

## Step 5 — Interface Map

| From | To | Flows | Direction |
|---|---|---|---|
| P1 | P2 | Framework structure (4 components + 5 expertise-depth tiers + 9 handling actions); orthogonal-axes commitments | One-way |
| P1 | P3 | Framework concepts (domain-specialist vs general fluency; reader-relative; competence vs identity) referenced in boundary statements | One-way |
| P1 | P4 | Framework's expertise-depth dimension applied to each specialist canon | One-way |
| P1 | P5 | Framework decisions tested by IC verdicts | One-way (read-only) |
| P2 | P4 | Per-level handling rules applied to specialist canons | One-way |
| P2 | P3 | Per-level examples cited as cross-axis distinguishing evidence | One-way (sparse) |
| P3 | P5 | Boundary commitments tested by IC verdicts | One-way (read-only) |
| P4 | P5 | Forward-tagged canons integration tested by IC8 verdict | One-way (read-only) |
| P1, P2, P3, P4 | P5 | All committed commitments tested by IC re-test | One-way (read-only consumption) |

### Assumptions-not-data check (refinement rule)

Hidden coupling check — what does each piece ASSUME the others provide?

- P1 assumes labels `lay | aware | educated | trained | expert` are settled (per sensemaking A1). Captured in P1's verification line.
- P1 assumes the AI determines term's domain-specialist-ness at runtime. Captured in P1's runtime-determination note.
- P2 assumes P1's framework + per-level conservative-bias instructions. Explicit interface.
- P3 assumes the framework's concepts (domain-specialist vs general fluency) are available. Explicit interface.
- P4 assumes the 5 forward-tagged canons are correctly listed per A1's cultural-reference-recognition finding. P4 cites the source.
- P5 assumes 12 ICs are exhaustively enumerable per sensemaking's IC list. Captured.

All assumptions captured. No silent hidden coupling.

---

## Step 6 — Dependency Order

### Topological order

**LEVEL 0 (independent — parallel-authorable):**
- P3 (Cross-axis boundaries) — independent of framework specifics
- P1 (Framework)

**LEVEL 1 (depends on LEVEL 0):**
- P2 (Per-level definitions) — depends on P1

**LEVEL 2 (depends on LEVEL 1):**
- P4 (Forward-tagged canons integration) — depends on P1 + P2

**LEVEL 3 (depends on all):**
- P5 (Inherited Commitments Re-test) — depends on P1 + P2 + P3 + P4

### Critical path
P1 → P2 → P4 → P5

### Parallel opportunities
- LEVEL 0: P1 and P3 can be authored simultaneously

No circular dependencies.

---

## Step 7 — Self-Evaluation

### Minimum 3 dimensions

**Independence:** Can each piece be worked on without the others existing?
- P1, P3: YES, fully independent.
- P2: depends only on P1.
- P4: depends on P1 + P2 — explicit interfaces.
- P5: depends on all — read-only consumption.
**PASS.**

**Completeness:** Do the pieces cover the whole inquiry?
Cross-check against sensemaking SV6 commitments:
- 5 labels `lay|aware|educated|trained|expert` → P1 + P2 ✓
- Plain-ordinal pattern → P1 ✓
- 5 expertise-depth tiers → P1 ✓
- 4-component template → P1 + P2 ✓
- 9 handling actions → P1 ✓
- Single-domain default → P1 ✓
- Reader-relative → P1 ✓
- Receptive-only → P1 + P2 ✓
- Conservative-bias LOWER → P1 ✓
- A2↔A1 boundary → P3 ✓
- A2↔A3 boundary → P3 ✓
- A2↔A4 boundary → P3 ✓
- Forward-tagged 5 specialist canons → P4 ✓
- Cross-domain examples → P2 ✓
- Distinguishing logic per adjacent level → P2 ✓
- Said Nursi corpus integration → P2 ✓
- Translator-AI runtime determination → P1 ✓
- IC re-test → P5 ✓
**PASS.**

**Reassembly:** Pieces + interfaces = whole?
- P1 + P2 → framework + per-level definitions
- + P3 → cross-axis boundaries
- + P4 → forward-tagged canons integration
- + P5 → IC re-test
- Together → complete inquiry answer.
**PASS.**

### Full 7 dimensions

**Tractability:** Each piece is small enough for a single focused pass?
- P1, P3, P5: small (1-3 paragraphs each).
- P2: large (5 levels × 4 components × cross-domain examples × distinguishing logic). Coheres as single section.
- P4: medium (5 specialist canons × 5-level progression).
**PASS** (P2 is large but coherent).

**Interface clarity:** All cross-piece flows explicit?
Mapped in Step 5; assumptions-not-data check applied; hidden coupling caught (runtime-determination note in P1).
**PASS.**

**Balance:** Complexity roughly proportional?
- P2 ≈ 45% (largest; natural anchor of a level-defining inquiry)
- P4 ≈ 15%
- P1 ≈ 20%
- P3 ≈ 10%
- P5 ≈ 10%
Slight P2 weight is natural for a level-defining inquiry. Acceptable.

**Confidence:** Top-down and bottom-up agree?
All atoms identified in Step 3 mapped to their top-down piece without conflict.
**HIGH CONFIDENCE.**

### Determination-mechanism piece check

The runtime determination mechanism (E18) — how the translator-AI determines a specific term's domain-specialist-ness at runtime — was identified as a load-bearing concept. The Reassembly check verifies that the question tree includes a piece addressing this. **YES — P1 includes a verification line for the translator-AI runtime determination mechanism.** No missing piece.

---

## Final Deliverable

### Coupling Map
5 clusters/pieces with internal strong coupling and well-defined inter-piece interfaces. 1 atom (translator-AI runtime determination, E18) folded into P1 framework.

### Question Tree (5 pieces)
- **P1** Framework (4-component template + 5 expertise-depth tiers + 9 handling actions + orthogonal-axes commitments + runtime determination)
- **P2** 5 per-level definitions + distinguishing logic + cross-domain examples
- **P3** Cross-axis boundaries (A2↔A1, A2↔A3, A2↔A4)
- **P4** 5 forward-tagged specialist canons integration
- **P5** Inherited Commitments Re-test (12 ICs)

### Interface Map
Documented in Step 5. Critical-path: P1 → P2 → P4 → P5. P3 parallel to P1.

### Dependency Order
LEVEL 0 {P1, P3} → LEVEL 1 {P2} → LEVEL 2 {P4} → LEVEL 3 {P5}. No circular dependencies.

### Self-Evaluation
- Independence: PASS
- Completeness: PASS (18 SV6 commitments mapped)
- Reassembly: PASS
- Tractability: PASS
- Interface clarity: PASS (assumptions-not-data check applied)
- Balance: PASS (P2 is naturally largest)
- Confidence: HIGH
- Determination-mechanism piece check: PASS (P1 absorbs E18)

**5 content-generation points handed to Innovation.**

## Content-generation points for Innovation

- **CG1 (P1):** Frame the 4-component template + 5 expertise-depth tiers (1-to-1 mapping with labels) + 9 handling actions in 2 categories + 1 bridge + orthogonal-axes commitments (single-domain / reader-relative / receptive-only / conservative-bias LOWER / plain-ordinal / runtime determination).
- **CG2 (P2):** Author 5 per-level definitions (lay / aware / educated / trained / expert) with 4 components each + at least 3-domain example spread per level + explicit distinguishing logic between adjacent levels. Said Nursi corpus example included.
- **CG3 (P3):** Author 3 cross-axis boundary sub-sections (A2↔A1, A2↔A3, A2↔A4) with criterion + independence demonstration per boundary.
- **CG4 (P4):** Author 5-specialist-canon integration showing each domain's 5-level progression; cite A1's forward-tagging justification.
- **CG5 (P5):** Author 12-IC re-test section with verdicts per commitment.
