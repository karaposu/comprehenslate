# Decomposition — multi-format intake acceptance

## User Input

Source: `_branch.md`. Upstream: `articulate_simple.md` + `surfacing.md` + `sensemaking.md`. Substrate: SV6 stabilized model = the user's proposal validated; per-format 4×2 matrix committed; routing/complex-content/quality-tier mechanisms committed; prior finding's DEFERRED 1 wording refined.

---

## Step 1 — Perceive Coupling Topology

### Elements

- **A** — Executive summary (1 paragraph)
- **B** — Acceptance-vs-priority distinction (meta: framing-semantic + lesson-vocabulary)
- **C** — Per-format 4×2 matrix (the load-bearing content artifact)
- **D** — Routing mechanism (hybrid auto-detect + warn-and-degrade + UI recommendation)
- **E** — Complex-content detection mechanism (documentation + UI guidance only)
- **F** — Quality-tier flag schema (Category 7 extension)
- **G** — Relationship-label `refines:` + Inherited Commitments Re-test (meta)
- **H** — Transition plan / refinements to prior finding's Next Actions
- **I** — Open Questions

### Coupling analysis

**Strong:**
- B (acceptance-vs-priority) ↔ C (matrix) — the matrix uses both axes of the distinction
- B ↔ G (relationship-label) — the distinction is what makes `refines:` structurally accurate
- C (matrix) ↔ F (quality-tier flag) — flag values are derived from the matrix's priority column
- C ↔ D (routing) — routing per-format depends on the matrix entries

**Moderate:**
- D ↔ E — both are about how intake responds to source format choices; conceptually adjacent
- G ↔ H — re-test references prior Next Actions; transition refines them
- A depends on everything

**Weak/loose:**
- E ↔ F — both are about quality signaling but at different layers (UI vs flag)
- I — depends loosely on all

### Major clusters

1. **META** cluster (B, G) — distinctions + relationship labels
2. **CONTENT** cluster (C, D, E, F) — per-format matrix + mechanisms
3. **DERIVED** cluster (H, I, A) — transitions + summary

---

## Step 2 — Detect Boundaries (Top-Down)

Optimal piece set:

| # | Piece | Content |
|---|---|---|
| **P1** | Executive summary | A (1 paragraph) |
| **P2 (META)** | Acceptance-vs-priority distinction + Decision-mode + relationship-label | B + decision-mode + `refines:` declaration |
| **P3 (CONTENT)** | Per-format 4×2 matrix | C |
| **P4 (CONTENT + MECHANISM)** | Routing mechanism + Complex-content detection | D + E (bundled — both about how intake responds to format choices) |
| **P5 (CONTENT)** | Quality-tier flag schema | F |
| **P6 (META + RELATIONSHIP)** | Inherited Commitments Re-test | G (without the relationship-label which lives in P2) |
| **P7 (DERIVED)** | Transition plan / Next Actions refinements | H |
| **P8 (DERIVED)** | Open Questions / Frontier | I |

**Total: 8 pieces.** Within 6-9 range.

---

## Step 3 — Validate Boundaries (Bottom-Up Check)

### Atoms

- Specific format-acceptance verdicts (per-format ACCEPTED / NOT-YET-IMPLEMENTED).
- Specific priority verdicts (HIGH / MEDIUM / LOW / MINIMUM / DEFERRED).
- Quality-tier values (high / medium / low / minimal).
- Routing-mechanism atoms (extension auto-detect; magic-bytes fallback; warn-and-degrade; UI message text).
- Prior-commitment re-test verdicts (PRESERVED / REFINED / STRENGTHENED).
- Refinement targets (specific Next Actions in prior finding to update).
- Open question revival triggers.

### Atom-to-piece mapping

| Atom type | Piece |
|---|---|
| Format acceptance verdicts | P3 ✓ |
| Priority verdicts | P3 ✓ |
| Quality-tier values | P5 ✓ |
| Routing mechanism atoms | P4 ✓ |
| Acceptance-vs-priority definition | P2 ✓ |
| Re-test verdicts | P6 ✓ |
| Refinement targets | P7 ✓ |
| Open question triggers | P8 ✓ |
| Summary | P1 ✓ |

**Boundaries validated.** No atom misplaced. Confidence: HIGH.

---

## Step 4 — Express as Question Tree

### P1 — Executive Summary

**Q:** *What does this finding commit to in one paragraph?*

**Verification:**
- [ ] Names "all 4 formats accepted" verdict
- [ ] Names acceptance-vs-priority distinction
- [ ] Names per-format matrix (EPUB high; PDF medium; md low; txt minimum; Word deferred)
- [ ] Names quality-tier flag extension
- [ ] States `refines:` relationship to prior

### P2 (META) — Acceptance-vs-priority distinction + Decision-mode + Relationship-label

**Q:** *What is the load-bearing distinction this finding commits, and what relationship does this finding declare to the prior intake-preprocessing-operations finding?*

**Verification:**
- [ ] Defines "Accepted format" (intake reads + produces canonical HTML5)
- [ ] Defines "Priority format" (engineering investment for high-quality reader)
- [ ] States the distinction is load-bearing and resolves the user's question coherently with prior commitment
- [ ] Commits decision-mode (YES with structural clarification, not bare YES; not overturn)
- [ ] Declares `refines:` relationship to prior + cites which cell of prior is refined (DEFERRED 1 wording)
- [ ] Distinguishes `refines:` from `extends:` / `corrects:` / `supersedes:`

### P3 (CONTENT) — Per-format 4×2 matrix

**Q:** *For each of the user-named input formats (and Word), what are the acceptance verdict and priority verdict for v0.2?*

**Verification:**
- [ ] EPUB row: ACCEPTED + HIGH-priority + quality-tier=high + notes (Category 6 EPUB path; recommended for complex content)
- [ ] PDF row: ACCEPTED + MEDIUM-priority + quality-tier=medium + notes (Category 6 PDF path with OCR + bidi-fix)
- [ ] markdown row: ACCEPTED + LOW-priority + quality-tier=low + notes (Pandoc baseline; no dedicated reader engineering)
- [ ] plain txt row: ACCEPTED + MINIMUM-priority + quality-tier=minimal + notes (Pandoc baseline; Categories 1+2+4+7 only)
- [ ] Word (.docx) row: NOT-YET-IMPLEMENTED + DEFERRED-priority + notes (engineering for high-quality Word reader is post-v0.2)
- [ ] Acknowledges "all 3 vs 4" transcription explicitly

### P4 (CONTENT + MECHANISM) — Routing + Complex-content detection

**Q:** *How does intake decide what to do given a source file, and how is "complex content" identified for the EPUB-recommendation guidance?*

**Verification:**
- [ ] Commits **routing**: hybrid auto-detect (file extension first; magic-bytes verification fallback)
- [ ] Commits warn-and-degrade (intake processes the file; emits Category 7 quality-tier flag rather than refusing)
- [ ] Commits UI recommendation in Mac app ("EPUB recommended for best results with complex content")
- [ ] Commits **complex-content detection** = documentation + UI guidance only (no runtime auto-detection for v0.2)
- [ ] Justifies the no-runtime-detection choice (over-engineering; user knows source complexity better)

### P5 (CONTENT) — Quality-tier flag schema

**Q:** *How does intake communicate format-fidelity quality-tier to downstream consumers?*

**Verification:**
- [ ] Commits `quality_tier` ∈ {high, medium, low, minimal} as a new field in the Category 7 informational-flag schema
- [ ] Composes with existing Category 7 flags (does not replace)
- [ ] Sidecar JSON: extends `intake-flags.json` schema with the new field (per MUST 4 from prior finding)
- [ ] Distinguishes quality-tier (format-fidelity) from content-quality flags (truncation; duplicate-content; etc.)

### P6 (META + RELATIONSHIP) — Inherited Commitments Re-test

**Q:** *For each commitment inherited from the prior intake-preprocessing-operations finding, what is the per-commitment re-test verdict?*

**Verification:**
- [ ] Format priority commitment (EPUB-first + PDF-fallback): PRESERVED
- [ ] DEFERRED 1 wording: REFINED (split Word stays DEFERRED-at-priority; txt + md always-accepted)
- [ ] Scope-line principle "structural, not semantic": PRESERVED
- [ ] 8-category preprocessing pipeline: PRESERVED (quality-tier extends Cat 7)
- [ ] HTML5 canonical: PRESERVED
- [ ] Decision 5 (Pandoc + OCR architectural lever from original intake-concepts): PRESERVED and STRENGTHENED
- [ ] Two-layer corpus model: PRESERVED
- [ ] Per-commitment evidence cited

### P7 (DERIVED) — Transition plan / Next Actions refinements

**Q:** *What needs to happen to operationalize this refinement?*

**Verification:**
- [ ] Identifies which prior Next Actions need wording updates (DEFERRED 1 split; quality-tier flag schema spec — extends MUST 4)
- [ ] MUST items unique to this finding (e.g., Mac app UI message text; format-detection magic-bytes lookup table; quality-tier flag field added to MUST 4 schema)
- [ ] COULD items (runtime complex-content auto-detection deferred to future; advanced routing edge cases)
- [ ] DEFERRED items (Word reader engineering remains DEFERRED at priority)
- [ ] Per-item Who/What/Gate/Why

### P8 (DERIVED) — Open Questions / Frontier

**Q:** *What is still open after this commitment?*

**Verification:**
- [ ] Runtime complex-content auto-detection (revival: if empirical evidence shows users miss UI guidance)
- [ ] EPUB-quality detection composition with quality-tier (does EPUB-from-PDF detected become quality-tier=medium? — open)
- [ ] Plain-text structural recovery (if users hand intake plain-text Risale-i Nur source — should intake attempt limited structural inference from blank-line patterns? — open)
- [ ] Magic-bytes lookup table maintenance (revival: when a new format is added)
- [ ] Per-revival trigger specified

---

## Step 5 — Map Interfaces

| Source | Target | What flows | Direction |
|---|---|---|---|
| P2 (acceptance-vs-priority) | P3 (matrix) | the distinction defines the matrix's two axes | one-way provide |
| P2 (acceptance-vs-priority) | P6 (re-test) | the distinction is what makes the prior's DEFERRED 1 split honest | one-way provide |
| P3 (matrix) | P4 (routing) | per-format verdicts inform per-format routing | one-way provide |
| P3 (matrix) | P5 (quality-tier flag) | the priority column maps to quality-tier values | one-way provide |
| P3 (matrix) | P7 (transition) | per-format verdicts inform Next Actions refinements | one-way provide |
| P5 (quality-tier flag) | P4 (warn-and-degrade) | the flag is what's emitted during warn-and-degrade | one-way provide |
| P5 (quality-tier flag) | P7 (transition) | flag schema extension is a Next Actions item | one-way provide |
| P6 (re-test) | P1 (exec summary) | refines: relationship label | one-way provide |
| P6 (re-test) | P7 (transition) | refinements identify prior MUSTs to update | one-way provide |
| P7 (transition) | P8 (open questions) | DEFERRED items become open question revival triggers | one-way provide |
| All pieces | P1 (exec summary) | summary references everything | one-way provide |

### Assumptions check

- P3 (matrix) ASSUMES P2 (distinction) is committed. Interface: P2 must be read first. ✓
- P4 (routing) ASSUMES P3 (matrix) per-format verdicts. ✓
- P5 (quality-tier flag) ASSUMES P3 (matrix) priority column. ✓
- P6 (re-test) ASSUMES P2 (distinction) — the re-test's REFINED verdict on DEFERRED 1 depends on the distinction. ✓
- P7 (transition) ASSUMES P3 + P5 + P6 contents. ✓
- P8 ASSUMES P7 DEFERRED items. ✓

No hidden coupling found.

---

## Step 6 — Order by Dependency

```
Phase 1: P2 (META — distinction)               ← FIRST
              │
              ▼
Phase 2: P3 (CONTENT — matrix)                  ← depends on P2
              │
              ▼
Phase 3: P4 (routing) ‖ P5 (quality-tier flag) ‖ P6 (re-test)   ← all depend on P3 + P2; parallel
              │
              ▼
Phase 4: P7 (transition + Next Actions)         ← depends on P3 + P5 + P6
              │
              ▼
Phase 5: P8 (open questions)                    ← depends on P7
              │
              ▼
Phase 6: P1 (executive summary)                 ← LAST; depends on everything
```

**Critical path:** P2 → P3 → (P4 ‖ P5 ‖ P6) → P7 → P8 → P1.

**Parallelizable:** P4, P5, P6 all in Phase 3.

---

## Step 7 — Self-Evaluate

### Minimum 3 dimensions

| Dimension | Check | Pass? | Reason |
|---|---|---|---|
| Independence | Can each piece be worked on alone? | **PASS** | Each piece's question is answerable given interfaces |
| Completeness | Pieces cover the whole? | **PASS** | All elements (B-I) covered; nothing missing |
| Reassembly | Pieces + interfaces = whole? | **PASS** | Reassembly produces the refining finding |

### Full 7 dimensions

| Dimension | Check | Pass? |
|---|---|---|
| Independence | works alone? | PASS |
| Completeness | covers whole? | PASS |
| Reassembly | pieces + interfaces = whole? | PASS |
| Tractability | each piece small enough for single-pass? | PASS |
| Interface clarity | cross-piece flows explicit? | PASS (11 interfaces mapped; assumptions checked) |
| Balance | complexity proportional? | PASS (P3 matrix is the heaviest content; P5/P4/P6 medium; P1/P7/P8 light — proportional to substantive weight) |
| Confidence | top-down + bottom-up agree? | PASS |

### Determination-mechanism piece check

The "acceptance-vs-priority distinction" is a load-bearing concept whose application IS the runtime determination (per format: ACCEPTED yes/no? priority level?). P2 defines the distinction and the operational mapping; P3 enumerates the per-format application. Determination mechanism is specified. ✓

---

## Final Deliverable

### Coupling map (summary)

- META cluster (B, G) — provides the contract.
- CONTENT cluster (C, D, E, F) — per-format matrix + mechanisms.
- DERIVED cluster (H, I, A) — transitions + summary.

### Question tree (8 pieces)

P1 Executive Summary · P2 Acceptance-vs-priority + decision-mode + refines: · P3 Per-format 4×2 matrix · P4 Routing + complex-content detection · P5 Quality-tier flag schema · P6 Inherited Commitments Re-test · P7 Transition + Next Actions · P8 Open Questions

### Dependency order

P2 → P3 → (P4 ‖ P5 ‖ P6) → P7 → P8 → P1

### Interface map

11 interfaces documented (Step 5). Assumptions-not-data check applied; no hidden coupling.

### Self-evaluation

- 3/3 PASS minimum (Independence; Completeness; Reassembly)
- 7/7 PASS full

**Verdict: PROCEED to Innovation.**
