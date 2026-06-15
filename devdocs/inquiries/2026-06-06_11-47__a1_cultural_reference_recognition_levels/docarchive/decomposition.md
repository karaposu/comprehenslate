# Decomposition — a1_cultural_reference_recognition_levels

## User Input
`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-06_11-47__a1_cultural_reference_recognition_levels/_branch.md` (with prior outputs: surfacing.md, sensemaking.md)

---

## Step 1 — Coupling Topology

### Elements identified (from sensemaking SV6)

- E1 Reader profile (template component 1)
- E2 Canonicity-tier (template component 2)
- E3 Register/canon-tier (template component 3)
- E4 Cultural-reference-handling test with 5 actions (template component 4)
- E5 5 level concept definitions (very_basic / daily / conversational / advanced / native)
- E6 Distinguishing logic between adjacent levels (4 boundaries)
- E7 Cross-cultural examples at each level
- E8 Reader-relative-canon commitment
- E9 Canon-choice-out-of-scope commitment
- E10 Markedness as text-property
- E11 Transparency as reference-property
- E12 DOMESTICATE-disfavored policy
- E13 EXPLICATE-FUNCTION as foreignization-preserving alternative
- E14 A1↔A2 boundary criterion
- E15 A1↔A2 specialist-domain list (legal/math/science/medical/specialist-philosophy)
- E16 20-entry forward-flagged dual-membership list
- E17 Per-entry cultural-ref canonicity tier
- E18 Per-entry per-level handling action
- E19 A1 composite-axis chain closure marker
- E20 Inherited Commitments Re-test (11 commitments)
- E21 Orthogonality with vocab
- E22 Orthogonality with syntax
- E23 Orthogonality with idiom (12-entry overlap)
- E24 Orthogonality with inference (8-entry overlap)
- E25 Triple-overlap cases (Rubicon, etc.)
- E26 Translator-AI runtime determination mechanism (transparency / markedness / canonicity-tier of a specific reference)

### Coupling map

Major clusters (high internal coupling):

**Cluster A — Framework core:** E1, E2, E3, E4 (4-component template structure), E8, E9, E10, E11 (orthogonal-axes commitments). STRONG internal coupling — changing a component or a commitment ripples to others.

**Cluster B — Per-level instantiation:** E5, E6, E7. STRONG internal coupling — distinguishing logic is derived from per-level definitions; examples instantiate definitions.

**Cluster C — Action policy:** E12, E13. STRONG internal coupling.

**Cluster D — A1↔A2 scope boundary:** E14, E15. STRONG internal coupling.

**Cluster E — Dual-membership re-tagging:** E16, E17, E18. STRONG internal coupling (entries × tier × handling form a single table).

**Cluster F — Cross-sub-field orthogonality:** E21, E22, E23, E24, E25. MODERATE coupling (related but each can be authored independently).

**Cluster G — Chain meta:** E19 (closure), E20 (inherited commitments re-test). MODERATE coupling.

**Atom — Runtime determination mechanism:** E26. SIDE concern.

Inter-cluster coupling:

| Pair | Coupling | Reason |
|---|---|---|
| A ↔ B | STRONG | per-level instantiation embeds framework |
| A ↔ C | STRONG | action policy constrains framework's component 4 |
| A ↔ D | WEAK | A1↔A2 boundary uses "general cultural literacy" concept marginally; mostly independent |
| A ↔ E | STRONG | dual-membership re-tagging uses framework's canonicity tier ladder |
| A ↔ F | MODERATE | orthogonality vs siblings references framework's reader-relative-canon commitment |
| A ↔ G | WEAK | chain meta references framework but is meta-structural |
| B ↔ C | STRONG | per-level prose embeds action policy |
| B ↔ E | STRONG | dual-membership entries use per-level handling action rules |
| B ↔ F | MODERATE | orthogonality cites per-level distinctions (e.g., idiom's 12 entries vs cultural-ref's tier) |
| C ↔ E | MODERATE | per-entry handling action references policy |
| C ↔ G | WEAK | independent |
| D ↔ E | WEAK | independent |
| D ↔ F | WEAK | A1↔A2 is scope; sibling-orthogonality is parallel sub-fields |
| E ↔ F | MODERATE | sibling-orthogonality cites dual-membership as evidence |
| E ↔ G | WEAK | independent |
| F ↔ G | WEAK | independent |

### Coupling-valley boundaries (candidate cut points)
- Between {A, B, C} (highly coupled framework + per-level + policy) and {D, F, G} (orthogonal meta sections): clean valley
- Between {E} (dual-membership table) and {D, F, G}: clean valley
- {E} sits adjacent to {A, B, C} (consumes them) but is itself a distinct artifact

---

## Step 2 — Detect Boundaries (Top-Down)

Initial boundary set produces these candidate pieces:

| # | Piece | Cluster source | Internal coupling | External coupling |
|---|---|---|---|---|
| P1 | Framework (4-component template + canonicity tiers + orthogonal-axes commitments) | A | STRONG | MODERATE to P2, P4, P6 |
| P2 | 5 per-level definitions + distinguishing logic + cross-cultural examples | B | STRONG | depends on P1, P6 |
| P3 | A1↔A2 boundary (criterion + specialist domains) | D | STRONG | WEAK to all |
| P4 | 20-entry dual-membership re-tagging table | E | STRONG | depends on P1, P2, P6 |
| P5 | Orthogonality with siblings (vs vocab/syntax/idiom/inference) | F | MODERATE | WEAK to P1, P2, P4 |
| P6 | Action-selection policy (DOMESTICATE-disfavored; EXPLICATE-FUNCTION alternative) | C | STRONG | feeds P1's C4 and P2's prose |
| P7 | A1 composite-axis chain closure | G (subset) | atomic | WEAK to all |
| P8 | Inherited Commitments Re-test (11 commitments) | G (subset) | atomic | depends on all |

---

## Step 3 — Validate Boundaries (Bottom-Up)

Identify the obvious irreducible atoms and check they group naturally:

| Atom | Natural piece | Match? |
|---|---|---|
| 4-component template structure | P1 | ✓ |
| 5 canonicity tier labels | P1 | ✓ |
| Reader-relative canon commitment | P1 | ✓ |
| Canon-choice OOS commitment | P1 | ✓ |
| Markedness text-side commitment | P1 | ✓ |
| Transparency reference-side commitment | P1 | ✓ |
| Translator-AI runtime determination mechanism | P1 (as side-note) | ✓ |
| 5-action vocabulary | P1 (as C4) | ✓ |
| `very_basic` 4-component definition | P2 | ✓ |
| `daily` 4-component definition | P2 | ✓ |
| `conversational` 4-component definition | P2 | ✓ |
| `advanced` 4-component definition | P2 | ✓ |
| `native` 4-component definition | P2 | ✓ |
| 4 adjacent-level distinguishing logics | P2 | ✓ |
| Cross-cultural examples per level | P2 | ✓ |
| A1↔A2 criterion | P3 | ✓ |
| 4-5 specialist-domain list | P3 | ✓ |
| Gray-zone cases (Einstein, etc.) | P3 | ✓ |
| 20-entry dual-membership entries | P4 | ✓ |
| Per-entry canonicity tier | P4 | ✓ |
| Per-entry per-level handling | P4 | ✓ |
| Triple-overlap cases (Rubicon) | P5 | ✓ |
| vs vocab (knowing-name vs allusive-function) | P5 | ✓ |
| vs syntax (near-orthogonal) | P5 | ✓ |
| vs idiom (12-entry overlap; allusion ≠ idiom) | P5 | ✓ |
| vs inference (8-entry overlap; recognition ≠ unpacking) | P5 | ✓ |
| DOMESTICATE-disfavored policy | P6 | ✓ |
| EXPLICATE-FUNCTION alternative | P6 | ✓ |
| Project policy grounding (Tier 1/2 + Venuti) | P6 | ✓ |
| Chain closure marker | P7 | ✓ |
| Sub-fields spec'd list (5) | P7 | ✓ |
| What's next list (A1↔A2 split inquiry; A2 sub-fields; audience config) | P7 | ✓ |
| 11 inherited commitments | P8 | ✓ |
| Re-test verdicts | P8 | ✓ |

All atoms align with top-down boundaries. **Confidence: HIGH.**

---

## Step 4 — Question Tree

### P1 — Framework
**Question:** What is the framework for cultural-reference-recognition levels — the 4-component template structure, the 5-tier canonicity ladder (with 1-to-1 mapping to reader levels), the 5 primary actions, and the orthogonal-axes commitments (reader-relative canon; canon-choice OOS; markedness/transparency as text/reference properties; translator-AI runtime determination mechanism)?

**Verification:**
- [ ] 4-component template structure stated with each component's role
- [ ] 5 canonicity tiers labeled and defined (`ubiquitous-canon | educated-mainstream-canon | literary-educated-canon | specialist-canonical | scholar-canonical`)
- [ ] 1-to-1 mapping from canonicity tiers to reader levels stated
- [ ] 5 primary handling actions named (INLINE-GLOSS / FOOTNOTE / DOMESTICATE / KEEP-AS-IS / EXPLICATE-FUNCTION)
- [ ] Reader-relative-canon commitment stated
- [ ] Canon-choice-out-of-scope commitment stated (with hand-off to audience-level)
- [ ] Markedness as text-property stated
- [ ] Transparency as reference-property stated
- [ ] Translator-AI runtime determination mechanism noted (AI determines tier/transparency/markedness from its training; reader-level config specifies reader's expected recognition)
- [ ] Template adaptation tagged MEDIUM-to-LIGHT
- [ ] Cross-cultural canon-set anchored (Greek / Biblical / Literary / Historical / Confucian / Quranic / Hindu / Persian / Said Nursi corpus enumerated as illustrative)

### P2 — 5 Level Definitions
**Question:** For each of 5 levels (`very_basic | daily | conversational | advanced | native`), what is the 4-component definition (reader profile / canonicity tier / register-canon tier / handling test) + 3-5 cross-cultural examples + per-level distinguishing logic from adjacent levels?

**Verification:**
- [ ] 5 level definitions with all 4 components each
- [ ] Each level has 3-5 examples spread across at least 3 different cultural canons (Greek, Biblical, Literary, Historical, Confucian, Quranic, Hindu, Persian, Said Nursi)
- [ ] Each of 4 adjacent-level boundaries has explicit distinguishing logic (very_basic↔daily; daily↔conversational; conversational↔advanced; advanced↔native)
- [ ] Same labels used consistently
- [ ] Receptive-only framing maintained at every level
- [ ] Per-level handling test specifies which actions fire for which canonicity tiers
- [ ] Said Nursi corpus example included at appropriate level(s) (likely advanced or native for Islamic-Sufi canon-reader; very_basic for Western-secular reader)
- [ ] DOMESTICATE-disfavored stance reflected per-level

### P3 — A1↔A2 Boundary
**Question:** What is the A1↔A2 boundary for cultural-reference-recognition? Criterion + 4-5 specialist-domain canons + gray-zone case acknowledgments.

**Verification:**
- [ ] Criterion stated (general cultural literacy → A1; domain-specialist canon training required → A2)
- [ ] 4-5 specialist domains enumerated (legal precedents; mathematical figures; scientific figures; medical eponyms; specialist philosophy)
- [ ] Gray-zone cases acknowledged (Einstein moved specialist→general; Wittgenstein remains specialist; Pythagorean theorem specialist→general; Marx political-canon variable)
- [ ] Boundary marker parallels prior siblings' A1↔A2 boundary phrasing

### P4 — Dual-Membership Re-Tagging Table
**Question:** How are the 20 forward-flagged dual-membership entries (12 from idiom-recognition; 8 from inference-capacity) INDEPENDENTLY re-tagged from cultural-reference-recognition's frame — assigned cultural-ref canonicity tier + per-level handling action?

**Verification:**
- [ ] Each of 20 entries assigned a cultural-ref canonicity tier
- [ ] Each entry has per-level handling action (across 5 levels)
- [ ] Dual-membership origin noted per entry (idiom-only / inference-only / both)
- [ ] Table format clear
- [ ] All idiom entries present (Achilles' heel; Pyrrhic victory; Crossing the Rubicon; Trojan horse; Catch-22; Big Brother; Cassandra; Pandora's box; Sword of Damocles; Sisyphean; Lazarus; Methuselah)
- [ ] All inference entries present (He met his Waterloo; Joan of Arc; Crossing the Rubicon; Trojan horse; Cassandra; Sisyphean; Pyrrhic victory; Lazarus)
- [ ] Deduplication noted (Rubicon, Trojan horse, Cassandra, Sisyphean, Pyrrhic victory, Lazarus appear in both — listed once with dual-origin tag)

### P5 — Cross-Sub-Field Orthogonality
**Question:** What is the orthogonality of cultural-reference-recognition with the other 4 A1 sub-fields, including the criterion that distinguishes each?

**Verification:**
- [ ] vs vocabulary-breadth: knowing-name vs recognizing-allusion distinction stated with example ("Cassandra" the name vs "a Cassandra" the metaphor)
- [ ] vs syntactic-processing-capacity: near-orthogonal note
- [ ] vs idiom-recognition: 12-entry overlap noted; criterion (allusion points at specific cultural source; idiom may be culturally-neutral)
- [ ] vs inference-capacity: 8-entry overlap noted; criterion (recognition = identifying the reference; inference = compressing/unpacking meaning)
- [ ] Triple-overlap cases acknowledged (Crossing the Rubicon = idiom + cultural-ref + inference)
- [ ] Per-sub-field independent handling commitment re-stated

### P6 — Action-Selection Policy
**Question:** What is the cross-cutting action-selection policy (DOMESTICATE-disfavored per project Tier 1/2 register-fidelity + Venuti; EXPLICATE-FUNCTION as foreignization-preserving alternative)?

**Verification:**
- [ ] DOMESTICATE structurally listed but project-policy disfavored
- [ ] EXPLICATE-FUNCTION presented as foreignization-preserving alternative
- [ ] Policy anchored to Tier 1/2 register-fidelity (per user's memory) + Venuti foreignization stance
- [ ] Per-level DOMESTICATE-restriction stated (at very_basic only as last resort; disabled at higher levels)
- [ ] Standard preference order stated (KEEP-AS-IS → INLINE-GLOSS → EXPLICATE-FUNCTION → FOOTNOTE → DOMESTICATE as last resort)
- [ ] Note that DELETION is escape valve (controversial)

### P7 — A1 Composite-Axis Chain Closure
**Question:** How does the finding mark the closure of the A1 composite-axis 5-sub-field chain?

**Verification:**
- [ ] Explicit `## A1 Composite-Axis Chain Closure` section
- [ ] All 5 sub-fields named with brief one-line summary each (vocabulary-breadth / syntactic-processing-capacity / idiom-recognition / inference-capacity / cultural-reference-recognition)
- [ ] What's now spec'd (A1 composite-axis fully defined across 5 sub-fields)
- [ ] What's next (A1↔A2 split inquiry; A2 sub-fields not yet defined; audience-fidelity stance; other axes from 8-axis architecture)
- [ ] What's still open per cultural-reference-recognition specifically (audience-level canon-set config; multi-canon handling; genre-canon mapping; time-shift canon membership)

### P8 — Inherited Commitments Re-test
**Question:** How are the 11 inherited commitments from prior siblings (plus this inquiry's 3 new commitments) re-tested with cited evidence?

**Verification:**
- [ ] All 11 commitments named (IC1 through IC11)
- [ ] Each marked: RE-TESTED OK / RE-TESTED & REFINED / RE-TESTED & APPLIED / INHERITED-WITHOUT-RE-TEST (with reason) / NEW
- [ ] Re-test references corresponding sensemaking ambiguity-resolution or framework decision
- [ ] IC9 (chain closure), IC10 (DOMESTICATE-disfavored), IC11 (markedness/transparency text-side) explicitly marked NEW

---

## Step 5 — Interface Map

| From | To | Flows | Direction |
|---|---|---|---|
| P1 | P2 | Framework structure (4 components + canonicity tier ladder + orthogonal-axes commitments); reader-relative-canon framing; receptive-only commitment | One-way |
| P1 | P4 | Canonicity tier ladder + 5 primary actions | One-way |
| P1 | P5 | Reader-relative-canon framing (informs orthogonality argument) | One-way |
| P1 | P6 | 5-action vocabulary | One-way |
| P2 | P4 | Per-level handling action rules | One-way |
| P6 | P1 | Policy constraint on action vocabulary (DOMESTICATE-disfavored shapes how P1's component 4 reads) | One-way (logical-ordering: P6 settles policy before P1 writes C4 prose) |
| P6 | P2 | Per-level prose embeds DOMESTICATE-disfavored policy + EXPLICATE-FUNCTION-preferred | One-way |
| P3 | P7 | A1↔A2 boundary mention referenced in closure section's "what's next" | One-way |
| P4 | P5 | Dual-membership table entries cited as evidence for sibling-orthogonality | One-way |
| P5 | P7 | Sibling-orthogonality referenced in closure as completion criterion | One-way |
| All of P1-P7 | P8 | Each piece's commitments tested by P8's re-test | One-way (read-only consumption) |

### Assumptions-not-data check (refinement rule)

Hidden coupling check — what does each piece ASSUME the others provide?

- P1 assumes the inherited labels (`very_basic`...`native`) are settled — YES, inherited from siblings.
- P1 assumes "presumed-target canon" framing — captured explicitly in P1 itself; no hidden coupling.
- P1 assumes translator-AI determines reference properties at runtime — must be stated in P1 explicitly (verification line included).
- P2 assumes P1's framework — explicit interface; no hidden coupling.
- P2 assumes P6's action policy — explicit interface; no hidden coupling.
- P2's per-level handling assumes the reader has access to footnotes or inline-gloss display surface — implicit assumption; should be noted in P1's framework as production-format-agnostic (the action vocabulary refers to abstract operations; surface rendering is downstream).
- P3 assumes "general cultural literacy" is a definable category — already addressed by P1's reader-relative-canon framing.
- P4 assumes the 20 entries' identities exactly as listed in surfacing's R19 — YES, verbatim from prior siblings' forward-flag lists.
- P4 assumes per-entry per-level handling can be derived from P1+P2's framework + P6's policy — YES.
- P5 assumes the 4 prior siblings' findings are accessible references — YES, all are in inquiry-folder paths.
- P5 assumes triple-overlap cases (Rubicon etc.) can be cited from prior siblings — YES.
- P6 assumes the project's Tier 1/2 register-fidelity is settled — anchored to user's persistent memory; should be explicitly cited in P6 to make the dependency visible.
- P6 assumes Venuti's foreignization stance is the right ethical anchor — explicitly cited.
- P7 assumes a "next conceptual step" plan exists (A1↔A2 split) — confirmed by the root inquiry's 4-layer architecture; should reference root.
- P8 assumes 11 commitments are exhaustively enumerable — confirmed by sensemaking's Inherited Commitments Re-tested section (11 items: IC1-IC11).

All assumptions captured. No silent hidden coupling.

---

## Step 6 — Dependency Order

### Topological order

**LEVEL 0 (independent — parallel-authorable):**
- P3 (A1↔A2 boundary)
- P6 (Action-selection policy)
- P7 (Chain closure section)

**LEVEL 1 (depends on LEVEL 0):**
- P1 (Framework) — depends on P6 (policy shapes C4 vocabulary)

**LEVEL 2 (depends on LEVEL 1):**
- P2 (Per-level definitions) — depends on P1 (framework structure) + P6 (policy)
- P5 (Sibling orthogonality) — depends on P1 (reader-relative-canon framing)

**LEVEL 3 (depends on LEVEL 2):**
- P4 (Dual-membership table) — depends on P1 (tiers + actions) + P2 (per-level handling rules) + P6 (policy)

**LEVEL 4 (depends on all):**
- P8 (Inherited Commitments Re-test)

### Critical path
P6 → P1 → P2 → P4 → P8

### Parallel opportunities
- LEVEL 0: P3, P6, P7 can be authored simultaneously
- LEVEL 2: P2 and P5 can be authored in parallel after P1

No circular dependencies.

---

## Step 7 — Self-Evaluation

### Minimum 3 dimensions

**Independence:** Can each piece be worked on without the others existing?
- P3, P6, P7: YES, fully independent.
- P1: depends only on P6 (policy informs framework's C4 vocabulary handling). PASS.
- P2: depends on P1 + P6 — explicit interface. PASS.
- P5: depends on P1 — explicit interface. PASS.
- P4: depends on P1 + P2 + P6 — explicit interfaces. PASS.
- P8: depends on all — read-only consumption. PASS.
**PASS.**

**Completeness:** Do the pieces cover the whole inquiry?
Cross-check against sensemaking SV6 commitments:
- 5 levels same labels → P2 ✓
- 5 canonicity tiers anchored in cultural-literacy research → P1 ✓
- 1-to-1 tier-to-level mapping → P1 + P2 ✓
- Reader-relative canon → P1 ✓
- Canon-choice OOS → P1 ✓
- Markedness/transparency text/reference properties → P1 ✓
- 5 primary actions → P1 (vocabulary) + P6 (policy) ✓
- DOMESTICATE disfavored + EXPLICATE-FUNCTION alternative → P6 ✓
- 4-component template MEDIUM-to-LIGHT adapted → P1 ✓
- A1↔A2 boundary → P3 ✓
- 20-entry dual-membership re-tagging → P4 ✓
- A1 composite-axis closure → P7 ✓
- Inherited commitments re-test → P8 ✓
- Orthogonality with siblings → P5 ✓
- Cross-cultural examples → P2 (per level) ✓
- Distinguishing logic between levels → P2 ✓
- Project policy grounding → P6 ✓
- Said Nursi corpus integration → P2 (example at appropriate level) ✓
- Translator-AI runtime determination mechanism → P1 (as framework note) ✓
**PASS.**

**Reassembly:** Pieces + interfaces = whole?
- P1 + P6 + P2 → framework + per-level definitions
- + P3 + P4 + P5 → boundary + dual-membership + orthogonality
- + P7 + P8 → closure + commitment re-test
- Together → complete answer to the inquiry's question.
**PASS.**

### Full 7 dimensions

**Tractability:** Each piece is small enough for a single focused pass?
- P1, P3, P5, P6, P7: small (1-3 paragraphs each).
- P2: large (5 levels × 4 components × multiple examples). Could be sub-decomposed if needed but coheres as a single section.
- P4: large (20 entries × tier + per-level handling). Coheres as a single table.
- P8: small (11 commitments).
**PASS** (P2 and P4 are large but coherent; not over-decomposed).

**Interface clarity:** All cross-piece flows explicit?
Mapped in Step 5; assumptions-not-data check applied; hidden coupling caught (production-format-agnostic note added to P1; user-memory anchor explicit in P6).
**PASS.**

**Balance:** Complexity roughly proportional?
- P2 ≈ 40% of work (5 levels × 4 components × examples).
- P4 ≈ 20% (20-entry table).
- P1 ≈ 15% (framework definition).
- P5 ≈ 8%.
- P3 ≈ 6%.
- P6 ≈ 5%.
- P8 ≈ 5%.
- P7 ≈ 3%.
Slightly imbalanced toward P2 (largest piece) and P4 — but these are the natural anchors of a level-defining inquiry. No piece is anomalously trivial or oversized.
**PASS** with note: P2 is the largest. Acceptable.

**Confidence:** Top-down and bottom-up agree?
All atoms identified in Step 3 mapped to their top-down piece without conflict.
**HIGH CONFIDENCE.**

### Determination-mechanism piece check

The runtime determination mechanism (E26) — how the translator-AI determines a specific reference's transparency / markedness / canonicity tier at runtime — was identified as a load-bearing concept whose use depends on a runtime determination. The Reassembly check verifies that the Q-tree includes a piece addressing this. **YES — P1 includes a verification line for the translator-AI runtime determination mechanism** ("AI determines tier/transparency/markedness from its training; reader-level config specifies reader's expected recognition"). No missing piece.

---

## Final Deliverable

### Coupling Map
8 clusters/pieces with internal strong coupling and well-defined inter-piece interfaces. 1 atom (translator-AI runtime determination mechanism) folded into P1 framework.

### Question Tree (8 pieces)
- **P1** Framework (template structure + canonicity tiers + orthogonal commitments + runtime determination mechanism + cross-cultural canon-set anchor)
- **P2** 5 per-level definitions + distinguishing logic + cross-cultural examples
- **P3** A1↔A2 boundary
- **P4** 20-entry dual-membership re-tagging table
- **P5** Cross-sub-field orthogonality
- **P6** Action-selection policy (DOMESTICATE-disfavored; EXPLICATE-FUNCTION alternative)
- **P7** A1 composite-axis chain closure
- **P8** Inherited Commitments Re-test (11 commitments)

### Interface Map
Documented in Step 5. Critical-path: P6 → P1 → P2 → P4 → P8. P3, P7 parallel to P1. P5 parallel to P2.

### Dependency Order
LEVEL 0 (P3, P6, P7) → LEVEL 1 (P1) → LEVEL 2 (P2, P5) → LEVEL 3 (P4) → LEVEL 4 (P8). No circular dependencies. P2 and P5 parallelizable in LEVEL 2.

### Self-Evaluation
- Independence: PASS
- Completeness: PASS (19 SV6 commitments mapped)
- Reassembly: PASS
- Tractability: PASS
- Interface clarity: PASS (assumptions-not-data check applied)
- Balance: PASS (slight P2/P4 weight is natural)
- Confidence: HIGH (top-down and bottom-up agreement on all atoms)
- Determination-mechanism piece check: PASS (P1 absorbs E26)

**8 content-generation points handed to Innovation.**

## Content-generation points for Innovation

The following per-piece content-generation tasks are handed to Innovation:

- **CG1 (P1):** Frame the 4-component template with each component's role, the 5-tier canonicity ladder (with 1-to-1 mapping), and the orthogonal-axes commitments — in language usable as translator-AI prompt context.
- **CG2 (P2):** Author 5 per-level definitions (very_basic / daily / conversational / advanced / native) with 4 components each + 3-5 cross-cultural examples spread across multiple canons + per-level distinguishing logic. Said Nursi corpus included at appropriate level.
- **CG3 (P3):** Author A1↔A2 boundary criterion + 4-5 specialist-domain list + gray-zone acknowledgments.
- **CG4 (P4):** Author the 20-entry dual-membership re-tagging table with per-entry canonicity tier + per-level handling action + dual-membership origin tag + deduplication.
- **CG5 (P5):** Author 4 orthogonality sub-sections (vs vocab / syntax / idiom / inference) with criterion + triple-overlap acknowledgment.
- **CG6 (P6):** Author action-selection policy statement (DOMESTICATE-disfavored; EXPLICATE-FUNCTION alternative; preference order; per-level usage rules) with project-policy grounding (Tier 1/2 register-fidelity + Venuti).
- **CG7 (P7):** Author A1 composite-axis chain closure section (5 sub-fields summary + what's next + what's still open).
- **CG8 (P8):** Author Inherited Commitments Re-test section (IC1-IC11 with verdicts).
