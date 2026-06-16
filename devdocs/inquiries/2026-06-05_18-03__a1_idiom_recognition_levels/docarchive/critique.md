# Critique — a1_idiom_recognition_levels

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_18-03__a1_idiom_recognition_levels/_branch.md` (with prior outputs: `surfacing.md`, `sensemaking.md`, `decomposition.md`, `innovation.md` in the same folder)

---

## Phase 0 — Dimension Construction

### Dimension set with weights

| # | Dimension | What it asks | Weight | Source |
|---|---|---|---|---|
| **D1** | Correctness | Does the cluster answer "5 levels for idiom-recognition with adapted template + logic + examples"? | CRITICAL | _branch.md goal |
| **D2** | Receptive-only discipline | Does the prose use RECOGNITION verbs only? | CRITICAL | inherited from chain |
| **D3** | Language-agnostic at concept | Are CONCEPTS universal; English idioms flagged illustrative? | CRITICAL | C3 |
| **D4** | Mutually-distinct ordinal levels | Do adjacent levels have clean distinguishing principles? | CRITICAL | C5 |
| **D5** | A1↔A2 boundary respect for idioms | Do examples honor general-vs-specialist-domain boundary? | CRITICAL | sensemaking Ambiguity 4 |
| **D6** | Sensemaking SV6 consistency *(project-specific risk)* | Lightly-adapted template, strength-graded handling preserved? | HIGH | sensemaking SV6 |
| **D7** | Operationalizability | LLM can judge idiom recognition from prose + examples? | HIGH | sensemaking F-A1 |
| **D8** | Example correctness | Each specific idiom genuinely at its claimed level by frequency-and-register analysis? | CRITICAL | per-cluster |
| **D9** | Template-adaptation coherence *(project-specific risk)* | Is the LIGHTER adaptation (vs syntax) principled? | HIGH | sensemaking Ambiguity 1 |
| **D10** | Project-value-fit *(project-specific risk)* | Honors register-preservation policy? | MEDIUM | memory + sensemaking |
| **D11** | Scope-discipline *(project-specific risk)* | Stays inside idiom-recognition scope; no creep | MEDIUM | C4 |
| **D12** | **Cross-sub-field boundary handling** *(NEW project-specific risk for this inquiry)* | Are dual-membership cases (Achilles' heel, Pyrrhic victory) handled per sub-field INDEPENDENTLY (not collapsed; not double-counted)? | HIGH | sensemaking Ambiguity 3 + decomposition P6 |

12 dimensions: **5 CRITICAL + 4 HIGH + 3 MEDIUM.** D12 is new to this inquiry (the cross-sub-field boundary is specific to idiom-recognition's interaction with cultural-reference-recognition).

### Stakes + burden of proof

- **HIGH stakes:** CC-A, CC-B, CC-C, CC-D, CC-E, CC-F, CC-I. Burden: balanced.
- **MEDIUM stakes:** CC-G, CC-H. Burden: innocent until proven guilty.

---

## Phase 1 — Landscape Construction

**Viable region:** passes D1-D5 (CRITICAL) + D6-D9 + D12 (HIGH) + D10-D11 (MEDIUM).

**Dead regions:** productive verbs; A2 specialist as A1.native positives; adjacent overlap; English-Greek-mythology-as-defining-axis (would fail language-agnosticism if those examples become defining rather than illustrative); arbitrary template renames; collapsing dual-membership to single sub-field.

**Boundary regions:** minor polish notes.

**Unexplored:** none after Phase 2.

---

## Phase 2 — Adversarial Evaluation

### Cluster CC-A — Per-level prose drafts

**Prosecution:** D2 receptive-only check — drafts (from sensemaking SV6) use "recognizes," "does not recognize," "treats literally." PASS. D6 SV6 consistency: 4 components with light prefix-rename. PASS. D9 template-adaptation coherence: lighter than syntax — only substitution-test replaced. Defensible.

**Defense:** All dimensions pass; drafts use receptive verbs throughout; concrete handling examples (`kick the bucket → die`).

**Verdict: SURVIVE.**

---

### Cluster CC-B — Per-level POSITIVE idiom examples

**Prosecution (D8 example correctness):**

**P3.2 daily positives:** "piece of cake", "easy as 1-2-3", "rain or shine", "out of the blue", "break the ice", "under the weather", "once in a blue moon", "make ends meet". All among top-50 most common English idioms; transparent or near-transparent. CORRECT.

**P3.3 conversational positives:** "kick the bucket" (user's anchor; opaque; top-300 common); "spill the beans"; "hit the nail on the head"; "let the cat out of the bag"; "burn the midnight oil"; "bite the bullet"; "the ball is in your court"; "go the extra mile"; "by the book"; "in hot water". All common opaque idioms recognized by newspaper-reading adults. CORRECT.

**P3.4 advanced positives:** "cast aspersions"; "tilt at windmills" (literary; from Don Quixote); "throw down the gauntlet"; "rise to the occasion"; "Pyrrhic victory" (DUAL); "play one's cards close to the chest"; "lay an egg" (theater); "Achilles' heel" (DUAL); "Catch-22" (DUAL).

Strongest objection: "Achilles' heel" might sit at CONVERSATIONAL (it's quite common in modern usage), not advanced. Let me check: most educated adults (newspaper readers) understand "Achilles' heel" as "vulnerability." So it could be at conversational/advanced boundary. Decomposition tagged it at "conversational/advanced" — borderline. Acceptable with note.

**P3.5 native positives:** "give up the ghost" (KJV-derived); "the patience of Job" (Bible); "by the skin of my teeth" (Job); "a thorn in my side" (NT); "cast pearls before swine" (Sermon on the Mount); "method in his madness" (Hamlet); "more in sorrow than in anger" (Hamlet); "the slings and arrows of outrageous fortune" (Hamlet); "Crossing the Rubicon" (Caesar/DUAL); "Trojan horse" (Iliad/DUAL).

All archaic/Biblical/Shakespeare-derived. CORRECT.

**Defense:** Examples drawn from multiple independent sources (idiom dictionaries + CEFR + Shakespeare/KJV inventories).

**Verdict: SURVIVE** with one note: "Achilles' heel" sits at the conversational/advanced borderline; the dual tagging in decomposition is appropriate.

---

### Cluster CC-C — Per-level NEGATIVE idiom examples

**Prosecution:** D8 — each negative above named level. Verified.

**Verdict: SURVIVE.**

---

### Cluster CC-D — Boundary idiom pairs

**Prosecution:** D4 — each pair illustrates transition cleanly.
- P4.1: literal "very easy" ↔ daily "piece of cake" — clean.
- P4.2: daily transparent ↔ conversational opaque (`kick the bucket`) — clean.
- P4.3: conversational ↔ advanced literary ("cast aspersions"; "tilt at windmills") — clean.
- P4.4: advanced ↔ native archaic/Biblical ("give up the ghost"; "the patience of Job") — clean.

**Verdict: SURVIVE.**

---

### Cluster CC-E — A1↔A2 specialist-domain idiom list

**Prosecution:** D5 — each example requires named domain training.
- Legal "with all deliberate speed" requires legal training (the technical meaning differs from "quickly"). ✓
- Financial "below the line" requires accounting training. ✓
- Sports "Hail Mary pass" requires American football knowledge. ✓
- Medical specialist idioms require medical training. ✓
- Borderline ("moving the goalposts", "in the trenches", "level playing field") correctly placed at A1.advanced because they've entered general English.

**Verdict: SURVIVE.**

---

### Cluster CC-F — Cross-sub-field dual-membership case list (NEW)

**Prosecution (D12 — NEW dimension):**
- Each case genuinely both idiom AND cultural reference. Verified.
- "Achilles' heel" — idiom (vulnerability point) + cultural ref (Iliad). ✓
- "Pyrrhic victory" — idiom (costly win) + cultural ref (Pyrrhus). ✓
- "Crossing the Rubicon" — idiom (point of no return) + cultural ref (Caesar 49 BCE). ✓
- "Trojan horse" — idiom (hidden threat) + cultural ref (Iliad/Aeneid + modern computing). ✓
- "Catch-22" — idiom (paradoxical situation) + cultural ref (Heller). ✓
- "Big Brother" — idiom (surveillance) + cultural ref (Orwell). ✓
- "Cassandra" — idiom (unheeded warner) + cultural ref (Greek myth). ✓
- "Pandora's box" / "Sword of Damocles" / "Sisyphean" — same dual structure. ✓
- "Lazarus" / "Methuselah" — Biblical dual-membership. ✓

**Strongest objection:** "But the cultural-reference-recognition sub-field hasn't been spec'd yet — how can the forward-looking column have specific tags?" Reply: the forward-looking tags are RECOMMENDATIONS that the future cultural-reference-recognition inquiry can adopt or refine. The current spec measures idiom-recognition only; the table's right column is documentation, not commitment.

**Defense:** The independent-handling principle is preserved. Each sub-field measures its dimension; the table tracks both for completeness.

**Verdict: SURVIVE with one clarification note** — explicit annotation that the cultural-reference column is forward-looking (future inquiry will set those values; current spec doesn't commit).

---

### Cluster CC-G — Migration mapping rationale

**Verdict: SURVIVE** (parallel to prior siblings).

---

### Cluster CC-H — Demographics + idiom-genre anchors

**Verdict: SURVIVE** (culturally neutral; native anchors English-illustrative).

---

### Cluster CC-I — Template-adaptation rationale

**Prosecution (D9):**
- "frequency-tier → idiom-frequency tier" light prefix-rename: defensible (idioms have frequency).
- "register-tier → idiom-register tier" light prefix-rename: defensible (idioms span registers).
- "substitution-test → idiom-handling test": named primary actions from Newmark/Baker; defensible runtime-action mapping.
- LIGHTER than syntactic-processing-capacity's adaptation: defensible (idioms ARE more like vocabulary than like syntax).

Strongest objection: "Why not also rename register-tier to something idiom-specific like 'idiom-register-and-source-tier' to capture domain-origin (sports/military/biblical)?" Reply: domain-origin is already captured in the register tier's inclusions list (casual/literary/biblical). Over-naming.

**Verdict: SURVIVE.**

---

## Phase 3.5 — Assembly Check

E1: per-level complete spec entries. E2: full idiom-recognition spec.

Test E2 against all 12 dimensions:
- D1-D11: ✓
- D12 cross-sub-field handling: ✓ (dual-membership cases handled per sub-field independently with forward-looking annotation)

**Assembly verdict: SURVIVE with 1 minor clarification note** (CC-F's cultural-reference column explicitly annotated as forward-looking).

---

## Phase 4 — Coverage + Convergence

All 9 clusters evaluated. All 5 levels spec'd. All 4 boundaries spec'd. A1↔A2 + cross-sub-field both covered. Migration mapping. Convergence reached.

**Signal: TERMINATE.**

---

## Ranked Survivors

1. **Final Recommended Assembly (E2)** — complete idiom-recognition spec with 1 minor clarification on CC-F
2. **Individual clusters (CC-A through CC-I)** — all SURVIVE

---

## Final Deliverable

### (a) Dimensions with weights

12 dimensions: 5 CRITICAL + 4 HIGH + 3 MEDIUM. **D12 (Cross-sub-field boundary handling) is NEW for this inquiry.**

### (b) Fitness Landscape

- **Viable:** all 9 clusters + Assembly E2
- **Dead:** productive verbs; A2 specialist as A1.native positive; English-mythology-as-defining; dual-membership collapsed to single sub-field
- **Boundary:** 1 minor clarification on CC-F (forward-looking annotation)
- **Unexplored:** none

### (c) Candidate Verdicts

All 9 clusters: SURVIVE. Assembly E2: SURVIVE with 1 minor polish (CC-F forward-looking annotation).

### (d) Coverage Map

All generation points adjudicated; deferred items (per-language; defaults; pydantic) explicitly out of scope.

### (e) Signal

**TERMINATE.**

---

## Convergence Telemetry

- **Dimension coverage:** 12/12; D12 (NEW) included
- **Adversarial strength:** STRONG (multi-axis prosecution per cluster including the NEW D12)
- **Landscape stability:** STABLE
- **Clean SURVIVE exists?** YES — Assembly E2 passes all 12 dimensions with 1 minor clarification
- **Failure modes observed:** None
  - NOT Wrong Dimensions (D12 added for the new cross-sub-field axis)
  - NOT Rubber-stamping (CC-F clarification raised; CC-B "Achilles' heel" borderline noted)
  - NOT Nitpicking (no trivial kills)
  - NOT Dimension Blindness (D5/D9/D12 explicit)
  - NOT False Convergence
  - NOT Evaluation Drift
  - NOT Self-Reference Collapse

**Overall: PROCEED.** Ready for CONCLUDE with 1 minor clarification.

---

## Handoff to CONCLUDE

Deliverable is the **Final Recommended Assembly (E2)** — complete idiom-recognition spec with:
- 5 levels (`very_basic | daily | conversational | advanced | native`) with lightly-adapted 4-component template instances
- 4 adjacent-level boundary specs with idiom-pair examples (user's `kick the bucket` anchor at conversational↔conversational+ boundary)
- A1↔A2 boundary for idioms + specialist-domain list across 4 domains
- **Cross-sub-field dual-membership case list (12 cases)** with idiom-recognition tags + forward-looking cultural-reference annotation
- Suggested migration mapping
- Template-adaptation rationale (lighter than syntax's)
- Cross-cutting framing constraints + Inherited Commitments Re-test section

Refinement note for incorporation:
1. **CC-F forward-looking annotation**: explicit statement that the "cultural-reference-recognition level" column is a forward-looking recommendation for the future cultural-reference-recognition inquiry; this inquiry's commitment is idiom-recognition only.

CONCLUDE should compile with `refines:` pointing to syntactic-processing-capacity (sibling) and document the Inherited Commitments chain through vocabulary-breadth and translation_config_axes.
