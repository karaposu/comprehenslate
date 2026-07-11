# Decomposition — document intake handling concepts

## User Input

Substrate: `_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md`. The SV6 stabilized model carries 5 load-bearing decisions + 38-concept layered list (4 layers × 4 decision-status tags). Decomposition's job: identify the pieces Innovation will generate content for.

---

## Step 1 — Perceive Coupling Topology

The "whole" being decomposed is the future `finding.md` content. Elements:

| Element | Role |
|---|---|
| Methodology / pruning rationale | How 110 → 38; why the 4 layers; the 4 decision-status tags |
| 5 load-bearing decisions | Each commits a foreclosing choice |
| 7-policy split (decision #4) | Relationship-label affecting B4-B10 |
| Layer A (format) 8 concepts | Format-layer enumeration |
| Layer B (structure) 12 concepts | Structure-layer enumeration; B4-B10 = 7 policy-perception detectors |
| Layer C (pipeline) 10 concepts | Pipeline-stage enumeration |
| Layer D (quality) 8 concepts | Quality-layer enumeration |
| Inherited Commitments Re-test | Verdicts on articulate_simple / surfacing / schema / Mac-app substrate |
| Frontier flags + open questions | Forward-looking pointers |
| Executive summary / user central question callback | The "what IS the list?" answer-at-a-glance |

### Coupling gradient

**Strong coupling (must stay together):**
- The 5 decisions cluster — each is a discrete decision but together they define the inquiry's commitment surface.
- Each layer-list's entries (within a layer) share the layer's framing.
- B4-B10 (7-policy detectors) share the policy-split relationship — but they're cohesive with Layer B's structure framing, not the decisions piece.

**Moderate coupling (boundary candidates):**
- Decisions → Layer lists (decisions are prerequisites that the lists reference but don't redefine).
- Methodology / status-tag legend → Layer lists (the legend defines tags used by every layer entry).
- Decision 3 (IntakeDoc shape) → Layer B (perception) + Layer C (pipeline) (the shape is consumed by both).
- Decision 4 (7-policy split) → Layer B (B4-B10 detectors framed by it).

**Weak coupling (clean boundaries):**
- Methodology vs Decisions (methodology is meta; decisions are the substantive commits).
- Layer A vs Layer B vs Layer C vs Layer D (once decisions + methodology are committed, each layer's content is independent of the others).
- Re-test vs the rest (re-test reads EXTERNAL priors, not THIS finding's content).
- Frontier vs the rest (forward-looking; pointer artifact).
- Executive summary vs the rest (summary is a digest; depends on all others to exist before being written).

### Coupling clusters

| Cluster | Members |
|---|---|
| **M** (meta) | Methodology + status-tag legend |
| **D** (decisions) | 5 load-bearing decisions (incl. 7-policy split as #4) |
| **L** (lists) | Layer A · Layer B · Layer C · Layer D — four sub-clusters within |
| **R** (re-test) | Inherited Commitments Re-test |
| **F** (forward) | Frontier flags + Next Actions |
| **S** (summary) | Executive summary / user-central-question callback |

Six clusters. Boundaries fall between clusters and between layers within Cluster L.

---

## Step 2 — Detect Boundaries (Top-Down)

Natural cut points where coupling is lowest:

| Boundary | Couplings crossing | Strength |
|---|---|---|
| M ↔ D | Methodology defines the 4-status legend used by D's commitments (one-way) | clean |
| D ↔ L | Decisions are prerequisites that L entries reference (one-way) | clean |
| L's internal — A ↔ B ↔ C ↔ D-sub | Each layer is independent given M+D | clean |
| L ↔ R | Re-test is independent of L | clean |
| L ↔ F | F reads L's status tags to identify open items | weak one-way |
| S ↔ everything | S is a digest of all others | last-step dependency |

### Initial piece set

- **P1**: Executive summary / user central question callback
- **P2**: Methodology + pruning rationale + status-tag legend
- **P3**: The 5 load-bearing decisions
- **P4**: Layer A — Format concepts (8 items)
- **P5**: Layer B — Structure concepts (12 items incl. 7-detector sub-cluster)
- **P6**: Layer C — Pipeline concepts (10 items)
- **P7**: Layer D — Quality concepts (8 items)
- **P8**: Inherited Commitments Re-test
- **P9**: Frontier flags + Next Actions + Open Questions

**9 pieces. Within target (8-12).**

---

## Step 3 — Validate Boundaries (Bottom-Up)

Atoms (irreducible elements) in each piece, grouped by which cluster they belong to:

| Piece | Atoms | Predicted cluster | Match? |
|---|---|---|---|
| P1 | "executive summary" | S | ✓ |
| P2 | pruning rationale · 4-layer rule · 4-tag legend | M | ✓ |
| P3 | 5 decisions: canonical-format · quality-target · IntakeDoc-shape · 7-policy-split · Pandoc-lever | D | ✓ |
| P4 | A1-A8 (8 atoms) | L/A | ✓ |
| P5 | B1-B12 (12 atoms; B4-B10 = 7-detector sub-cluster) | L/B | ✓ |
| P6 | C1-C10 (10 atoms) | L/C | ✓ |
| P7 | D1-D8 (8 atoms) | L/D | ✓ |
| P8 | 4 re-test verdicts (articulate_simple / surfacing / schema / Mac-app) | R | ✓ |
| P9 | 6 frontier flags + Next-Actions list | F | ✓ |

No atoms split across boundaries. No atoms grouped together that should be separate. **High-confidence boundaries.**

---

## Step 4 — Question Tree

### P1 — Executive Summary / User Central Question Callback
**Q:** "What is the actionable list of intake-handling concepts comprehenslate needs to figure out, in one paragraph?"
**Verification criteria:**
- [ ] One-paragraph answer naming the 4-layer × 4-tag structure
- [ ] Names the 5 load-bearing decisions
- [ ] Points reader to the layer lists for the enumerated concepts
- [ ] Anchors back to user's literal question without restating it verbatim

### P2 — Methodology / Pruning Rationale / Status-Tag Legend
**Q:** "How were 110 candidates pruned to 38, and what do the 4 status tags mean?"
**Verification criteria:**
- [ ] Pruning criteria stated (schema-named OR downstream-consequence OR engineering-required)
- [ ] 4-layer structure (format/structure/pipeline/quality) named with one-line role each
- [ ] DECIDE-NOW / DESIGN-NEXT-INQUIRY / ENGINEER / DEFER each defined with when-to-apply criteria
- [ ] Anti-hallucination statement: every concept is grounded in schema-reference OR Pandoc-fact OR sensemaking-anchor
- [ ] 110 → 38 attribution: which 72 dropped and into which bucket (edge / redundant / v1+)

### P3 — The 5 Load-Bearing Decisions
**Q:** "What 5 decisions does this inquiry commit to, why, and what does each foreclose?"
**Verification criteria:**
- [ ] Decision 1 — canonical intake format = Pandoc-md-superset (rationale: covers Risale-i Nur primitives off-the-shelf, single parser surface, hand-editable; forecloses: vanilla CommonMark, RTF-as-canonical, custom-format-for-v0.2)
- [ ] Decision 2 — quality target = structure-preservation (rationale: matches user's painpoint; forecloses: typography-fidelity, semantic-only stripping)
- [ ] Decision 3 — IntakeDoc shape = tree-of-containers + cross-referenced flat collections (rationale: chunking-by-chapter + apparatus reference; forecloses: pure-tree, pure-flat)
- [ ] Decision 4 — 7-policy split = each policy has intake-perception + translate-rendering halves (table mapping each of 7 policies; rationale: policy value is vacuous without perceived target)
- [ ] Decision 5 — Pandoc-as-architectural-lever + OCR sub-pipeline for scan-only PDFs (rationale: ~80% of format-conversion is free engineering; forecloses: writing parsers from scratch)
- [ ] Each decision carries: text · rationale · what's foreclosed · revisitability flag

### P4 — Layer A: Format-Layer Concepts
**Q:** "What format-layer concepts must intake handle?"
**Verification criteria:**
- [ ] All 8 concepts present (A1 canonical format · A2 accepted user-provided formats · A3 OCR sub-pipeline · A4 Pandoc invocation per format · A5 format detection / sniffing · A6 mixed-script + RTL handling · A7 Pandoc-AST→IntakeDoc mapping · A8 format-fidelity gradient)
- [ ] Each concept: one-line definition + decision-status tag + rationale-pointer
- [ ] A1 + A2 tagged DECIDE-NOW with committed values
- [ ] A3 / A4 / A6 tagged DESIGN-NEXT-INQUIRY with frontier-flag pointer
- [ ] A5 + A7 tagged ENGINEER with implementation-note
- [ ] A8 tagged DEFER (v1+)

### P5 — Layer B: Structure-Layer Concepts (incl. 7-detector sub-cluster)
**Q:** "What structure-layer concepts must intake perceive — and what 7 perception detectors does the policy split require?"
**Verification criteria:**
- [ ] All 12 concepts present (B1 structure-vs-style axiom · B2 hierarchical containment · B3 footnotes · B4-B10 7 policy-perception detectors · B11 frontmatter/backmatter/TOC · B12 emphasis-as-primitive)
- [ ] B4-B10 grouped as a sub-section "the 7 perception detectors" with explicit reference back to Decision 4
- [ ] B1 tagged DECIDE-NOW as axiom
- [ ] B2 tagged DECIDE-NOW as tree-as-primary commitment
- [ ] B3 + B11 + B12 tagged ENGINEER
- [ ] B4-B10 each tagged DESIGN-NEXT-INQUIRY with per-detector frontier-flag (what signals identify this element in source?)
- [ ] Per-detector: name policy fed · perception-signals (heuristic + structural) · representation-in-IntakeDoc

### P6 — Layer C: Pipeline-Layer Concepts
**Q:** "What pipeline-layer stages does intake comprise?"
**Verification criteria:**
- [ ] All 10 concepts present (C1 IntakeDoc schema design · C2 intake-vs-translate boundary · C3 parse · C4 normalize · C5 segment · C6 validate · C7 pre-validation · C8 post-parse validation · C9 intake metadata + language detection · C10 multi-file project intake)
- [ ] C1 tagged DESIGN-NEXT-INQUIRY (the pydantic schema is the largest single design task)
- [ ] C2 tagged DECIDE-NOW (the architectural seam)
- [ ] C3-C9 tagged ENGINEER as standard stages w/ Pandoc-leverage note
- [ ] C10 tagged DESIGN-NEXT-INQUIRY (merge vs stack mechanics)
- [ ] Stage ordering shown: parse → normalize → segment → validate → hand-off

### P7 — Layer D: Quality-Layer Concepts
**Q:** "What quality-layer concepts frame intake's success?"
**Verification criteria:**
- [ ] All 8 concepts present (D1 quality target · D2 fidelity/lossiness · D3 metrics · D4 quality gates · D5 intake-edit-after-parse · D6 paratext default · D7 error attribution · D8 source-of-truth declaration)
- [ ] D1 tagged DECIDE-NOW = structure-preservation
- [ ] D5 tagged DECIDE-NOW = SUPPORTED (hand-editing recovery path)
- [ ] D8 tagged DECIDE-NOW = YES (IntakeDoc canonical; original read-only)
- [ ] D2 / D3 / D4 / D6 tagged DESIGN-NEXT-INQUIRY
- [ ] D7 tagged ENGINEER (stage-tagged errors)
- [ ] Per-concept: one-line definition + status tag + downstream-pointer

### P8 — Inherited Commitments Re-test
**Q:** "What prior commitments did this inquiry inherit, and what's the verdict per prior?"
**Verification criteria:**
- [ ] articulate_simple's 5 considered articulations: verdict per variant (variant 4 PRIMARY, variant 5 SECONDARY, variants 1-3 PARTIALLY-ACCEPTED)
- [ ] surfacing's 110 candidates: verdict on pruning (38 kept; 72 dropped → broken down by category: edge / redundant / v1+)
- [ ] schema's 7 policies: verdict = RESPECTED (no redefinition; intake feeds them)
- [ ] Mac-app session substrate: verdict = OUT-OF-FRAME (excluded by MQ4; re-entry flagged for post-CONCLUDE)
- [ ] Per-prior: cited evidence (file paths or section references)

### P9 — Frontier + Next Actions + Open Questions
**Q:** "What's left open, and what's the immediate next move?"
**Verification criteria:**
- [ ] All 6 surfacing-emitted frontier flags addressed: F1 (IntakeDoc schema shape) — resolved as Decision 3 + escalated as C1 DESIGN-NEXT-INQUIRY; F2 (canonical format) — resolved as Decision 1; F3 (quality trichotomy) — resolved as Decision 2; F4 (Mac-app re-entry) — flagged for post-build; F5 (policy intake/translate attribution) — resolved as Decision 4; F6 (OCR sub-pipeline depth) — escalated as A3 DESIGN-NEXT-INQUIRY
- [ ] Next-actionable inquiry(ies) named in priority order: (1) design the IntakeDoc pydantic schema (C1); (2) design the 7 perception detectors (B4-B10); (3) prototype Pandoc → IntakeDoc on a single Risale-i Nur PDF (A7+OCR validation)
- [ ] Open questions explicitly marked (not silently dropped)

---

## Step 5 — Interface Map

| # | Source | Target | What flows | Direction | Assumption coupling |
|---|---|---|---|---|---|
| I1 | P2 (status-tag legend) | P4 / P5 / P6 / P7 | The 4-tag vocabulary | one-way | P4-P7 assume tags as defined; explicit |
| I2 | P3 (Decision 1) | P4 (A1, A2, A7) | Canonical-format = Pandoc-md-superset commitment | one-way | A1+A2 cite Decision 1; explicit |
| I3 | P3 (Decision 2) | P7 (D1, D2, D3) | Quality target = structure-preservation | one-way | D1 cites Decision 2; explicit |
| I4 | P3 (Decision 3) | P5 (all), P6 (C1, C3-C9) | IntakeDoc shape commitment | one-way | B5 perception detectors target IntakeDoc fields; explicit |
| I5 | P3 (Decision 4) | P5 (B4-B10 sub-cluster) | 7-policy perception/rendering split | one-way | Each detector framed as policy-feeder; explicit |
| I6 | P3 (Decision 5) | P4 (A3, A4, A7) | Pandoc + OCR architectural lever | one-way | A3+A4+A7 cite Decision 5; explicit |
| I7 | P2 (methodology) | P9 (frontier) | Pruning rationale informs which dropped items become Frontier vs DEFER | one-way | P9 assumes the rationale exists; explicit |
| I8 | P3 (all decisions) | P9 (frontier-F-resolution) | Which Frontier flags got resolved by which decision | one-way | P9 cites which decisions resolved which F-flags; explicit |
| I9 | P4 / P5 / P6 / P7 (all layer-status tags) | P9 (Next Actions) | DESIGN-NEXT-INQUIRY items become next-actionable | one-way | P9 enumerates from layer-list status tags; explicit |
| I10 | EXTERNAL (priors) | P8 (re-test) | articulate_simple / surfacing / schema / Mac-app substrate paths | one-way | P8 reads externals; documented in priors |
| I11 | P2 + P3 + P4-P7 + P8 + P9 | P1 (exec summary) | Digest of all preceding pieces | one-way (last-step) | P1 written LAST; depends on all others |

**Assumptions-not-data check (Step 5 refinement):**

| Hidden-assumption risk | Check | Result |
|---|---|---|
| P4-P7 assume P2's 4-tag set is stable | P2's tag set defined explicitly; tag-rename would require P4-P7 update | ✓ explicit |
| P5's 7-detector framing assumes Decision 4 holds | Decision 4 is in P3; B4-B10 cite it | ✓ explicit |
| P6 (C1) assumes Decision 3 commits the *shape* not the *fields* | Decision 3 explicitly says "shape committed; field schema is C1" — boundary stated | ✓ explicit |
| P9 assumes the DESIGN-NEXT-INQUIRY tags from P4-P7 are stable | If a tag flips from DESIGN-NEXT-INQUIRY to ENGINEER, P9's Next Actions list shifts | ✓ explicit (cite tag flip) |
| P1 assumes the user's literal question matches the answer given | Verified at write-time by re-reading `_branch.md`'s Source Input | ✓ explicit |

No hidden coupling detected.

---

## Step 6 — Dependency Order

```
Order      Piece                  Depends on               Can parallelize with
─────      ─────                  ──────────               ────────────────────
1          P2                     —                        —
2          P3                     P2 (tags vocabulary)     —
3a         P4                     P2, P3                   P5 ‖ P6 ‖ P7 (all parallel)
3b         P5                     P2, P3                   P4 ‖ P6 ‖ P7
3c         P6                     P2, P3                   P4 ‖ P5 ‖ P7
3d         P7                     P2, P3                   P4 ‖ P5 ‖ P6
4          P8                     —                        independent (parallel w/ Group 3)
5          P9                     P3 + P4-P7 (status tags) —
6          P1                     ALL                      LAST (digest)
```

**Critical-path ordering for Innovation:** P2 → P3 → Group α (P4 ‖ P5 ‖ P6 ‖ P7) → P9 → P1. P8 runs in parallel with Group α (independent of inquiry-internal content). The order honors all I1–I11 interface flows.

No circular dependencies.

---

## Step 7 — Self-Evaluation

### Minimum 3-dimension evaluation

| Dimension | Check | Verdict | Note |
|---|---|---|---|
| **Independence** | Can each piece be worked on without others (beyond declared interfaces)? | **PASS** | P4-P7 independent of each other once P2+P3 exist. P1 + P9 explicitly depend on others (declared in interfaces). P8 fully independent. |
| **Completeness** | Pieces cover the finding's whole? | **PASS** | Methodology + decisions + 4 layer lists + re-test + frontier + summary = every section the finding needs. No gap. |
| **Reassembly** | Pieces + interfaces → coherent finding? | **PASS** | Concatenated in dependency order, the 9 pieces produce a readable `finding.md` with executive summary, methodology, decisions, the actionable list across 4 layers, re-test, and frontier. |

### Full 7-dimension evaluation (high-stakes recommended)

| Dimension | Check | Verdict |
|---|---|---|
| Independence | (above) | **PASS** |
| Completeness | (above) | **PASS** |
| Reassembly | (above) | **PASS** |
| **Tractability** | Each piece small enough for one focused Innovation pass? | **PASS** — P5 is heaviest (12 concepts incl. 7 sub-detectors), but each detector is one-paragraph generation; P3 is 5 decisions × ~80-100 words each; manageable. |
| **Interface clarity** | All cross-piece flows explicit? | **PASS** — I1-I11 mapped; assumptions-not-data check ran; no hidden coupling. |
| **Balance** | Roughly equal complexity? | **MILD IMBALANCE** — P5 (12 concepts incl. 7-detector cluster) ≈ 1.5x larger than P7 (8 concepts). Not extreme; acceptable. If Innovation finds P5 too heavy, the 7-detector cluster could be lifted as a sibling piece (DV2 trigger). |
| **Confidence** | Top-down (Step 2) ↔ bottom-up (Step 3) agree? | **HIGH** — atom-to-cluster mapping passed with no disagreements. |

### Determination-mechanism piece check (Step 7 refinement)

Are there load-bearing concepts whose use depends on runtime determination, and is the determination mechanism itself a piece?

| Concept | Runtime determination | Determination mechanism's piece |
|---|---|---|
| OCR sub-pipeline (A3) | "does this PDF have a text layer?" | A3 itself is tagged DESIGN-NEXT-INQUIRY → the mechanism is downstream of this finding, not missing from it |
| Format detection (A5) | "what format IS this file?" | A5 is the determination mechanism for format ambiguity; tagged ENGINEER |
| The 7 perception detectors (B4-B10) | "does the source HAVE marginalia / poetry / honorifics / etc.?" | Each detector IS the determination mechanism; tagged DESIGN-NEXT-INQUIRY → these ARE the next inquiry's work |
| Multi-file project intake (C10) | "are these 30 PDFs one book or separate works?" | C10's design IS the determination mechanism; tagged DESIGN-NEXT-INQUIRY |
| Quality gates (D4) | "did intake produce good-enough output to proceed to translate?" | D4's threshold-definition IS the determination mechanism; tagged DESIGN-NEXT-INQUIRY |

**No missing pieces** — every runtime determination has an associated piece (either ENGINEER for now, or DESIGN-NEXT-INQUIRY for downstream). The Reassembly check holds.

### Failure-mode self-scan

- **Premature decomposition:** ✗ Sensemaking ran first; SV6 stabilized the whole. Coupling perception followed.
- **Wrong boundaries:** ✗ Top-down + bottom-up agree; cuts at low-coupling valleys (between meta/decisions/layers/re-test/frontier/summary).
- **Hidden coupling:** ✗ Assumptions-not-data check ran; all interface assumptions made explicit.
- **Missing pieces:** ✗ Completeness pass + Determination-mechanism check; no gaps.
- **Over-decomposition:** ✗ 9 pieces for a 38-concept finding; ~4 concepts per piece (excluding meta/re-test/frontier/summary which are role-specialized).
- **Ignoring dependencies:** ✗ Dependency order explicit; critical path P2→P3→Group α→P9→P1.
- **Imbalanced decomposition:** ⚠ Mild — P5 ≈ 1.5x P7; documented; DV2 trigger flagged if Innovation needs.

### Self-assessment verdict

**PROCEED to Innovation.** 9 pieces with explicit interfaces, dependency ordering, and verification criteria. The 7-detector sub-cluster in P5 is flagged for monitoring during Innovation — if it becomes unmanageable, split it as a sibling piece in DV2.

---

## Final Deliverable — Summary Table

| # | Piece | Question | Status |
|---|---|---|---|
| P1 | Executive summary / user central question callback | What is the actionable list in one paragraph? | last |
| P2 | Methodology + status-tag legend | How were 110 pruned to 38; what do the 4 tags mean? | first |
| P3 | The 5 load-bearing decisions | What 5 decisions does this inquiry commit, why, what does each foreclose? | second |
| P4 | Layer A — Format concepts | What format-layer concepts must intake handle? | parallel α |
| P5 | Layer B — Structure concepts (incl. 7-detector sub-cluster) | What structure-layer concepts must intake perceive? | parallel α |
| P6 | Layer C — Pipeline concepts | What pipeline-layer stages does intake comprise? | parallel α |
| P7 | Layer D — Quality concepts | What quality-layer concepts frame intake's success? | parallel α |
| P8 | Inherited Commitments Re-test | What prior commitments inherited; verdict per prior? | independent |
| P9 | Frontier + Next Actions + Open Questions | What's left open; immediate next move? | after α |
