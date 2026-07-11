# Decomposition — canonical intake format deep dive

## User Input

Substrate: `_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md`. SV6 stabilized model = three-format layered architecture (Pandoc-AST-JSON canonical / Pandoc-md hand-edit / EPUB 3 publishing) + decision-mode SUBSTITUTE + prior Decision 1 REFINED. Decomposition's job: identify the pieces Innovation will fill.

---

## Step 1 — Perceive Coupling Topology

Elements of the finding-to-be:

| Element | Role |
|---|---|
| Executive summary | One-paragraph user-question answer |
| Architectural commitment | Three-format layered architecture (the framing-semantic meta-decision) |
| Decision-mode commitment | SUBSTITUTE — refines prior Decision 1 (relationship-label meta-decision) |
| F1 spec | Pandoc-AST-as-JSON as canonical intake/translate format |
| F2 spec | Pandoc's markdown as hand-edit format (refined role) |
| F3 spec | EPUB 3 as publishing format |
| Rejected candidates | RTF / TEI / MOBI / EPUB-as-canonical-intake / Custom-format — each with structural reason |
| Calibration-corpus implications | Per-policy-target AST mappings |
| Inherited Commitments Re-test | Prior Decision 1's three rationale parts re-tested |
| Transition plan | From prior monolithic to new layered |
| Next actions | Immediate downstream tasks |
| Open questions | Frontier items |

### Coupling gradient

**Strong coupling (must stay together):**
- The three format roles (F1, F2, F3) are layer-decoupled but share the architectural-commitment frame; each piece references the others' roles.
- The five rejections (RTF / TEI / MOBI / EPUB-canonical / Custom) share the "candidate + structural-reason" shape.
- The seven policy-target AST mappings share the "policy → AST node" shape.

**Moderate coupling (boundary candidates):**
- Architectural commitment → F1/F2/F3 (one-way; the commitment shapes each format's role).
- Architectural commitment → Inherited Re-test (the SUBSTITUTE decision-mode IS the verdict on the prior).
- F1 spec → Calibration-corpus implications (the AST shape determines how policy targets map).
- Inherited Re-test → Transition plan (what's refined determines what changes in the build path).

**Weak coupling (clean boundaries):**
- Rejected candidates rationale vs the three F1/F2/F3 specs (parallel; each justifies the choice but doesn't depend on the others' format detail).
- Exec summary vs the rest (last-step digest).
- Open questions vs the rest (forward-looking).

### Coupling clusters

| Cluster | Members |
|---|---|
| **A (framing/meta)** | Architectural commitment + decision-mode |
| **B (format roles)** | F1 spec / F2 spec / F3 spec — three sub-clusters (one per format) |
| **C (rejections)** | Five rejected candidates with structural rationale |
| **D (re-test)** | Inherited Commitments Re-test |
| **E (corpus)** | Calibration-corpus AST mapping |
| **F (forward)** | Transition plan + Next actions |
| **G (summary)** | Executive summary |
| **H (open)** | Open Questions / Frontier |

Eight clusters. Boundaries fall between clusters and between layer-roles within Cluster B.

---

## Step 2 — Detect Boundaries (Top-Down)

Natural cut points where coupling is lowest:

| Boundary | Couplings crossing | Strength |
|---|---|---|
| A ↔ B | Architecture defines what F1/F2/F3 are (one-way commitment-flow) | clean |
| B's internal — F1 ↔ F2 ↔ F3 | Each format independent given architectural commitment | clean |
| B ↔ C | Rejections are independent of the chosen formats' specs once architecture is committed | clean |
| A ↔ D | Decision-mode IS the re-test verdict's frame (re-test resolves prior in light of decision-mode) | one-way clean |
| B (F1) ↔ E | AST shape determines mappings | one-way clean |
| A + D ↔ F | Transition path depends on architecture + re-test | one-way clean |
| All ↔ G | Summary digests; written last | last-step dependency |
| Most ↔ H | Open questions surface what's still unfixed | last-step dependency |

### Initial piece set

- **P1**: Executive summary / one-paragraph headline answer
- **P2**: Architectural commitment (three-format layered) + decision-mode (SUBSTITUTE; refines prior)
- **P3**: F1 — canonical intake/translate = Pandoc-AST-as-JSON
- **P4**: F2 — hand-edit = Pandoc's markdown (refined role)
- **P5**: F3 — publishing = EPUB 3
- **P6**: Rejected candidates rationale (RTF / TEI / MOBI / EPUB-as-canonical / Custom)
- **P7**: Calibration-corpus AST mappings
- **P8**: Inherited Commitments Re-test on prior Decision 1
- **P9**: Transition plan + Next actions (consolidated — both are forward-looking from the same root)
- **P10**: Open Questions / Frontier

**10 pieces.** At the upper bound of target (7-10).

---

## Step 3 — Validate Boundaries (Bottom-Up)

Atoms (irreducible elements) grouped by which piece they belong to:

| Piece | Atoms | Predicted cluster | Match? |
|---|---|---|---|
| P1 | "headline answer" | G | ✓ |
| P2 | architectural-commitment · decision-mode-commitment | A | ✓ |
| P3 | F1 format + role + Pandoc commands + schema-validation strategy | B/F1 | ✓ |
| P4 | F2 format + role + Pandoc commands + round-trip-stable subset note | B/F2 | ✓ |
| P5 | F3 format + role + Pandoc commands + MOBI-rejection-note | B/F3 | ✓ |
| P6 | 5 rejections (RTF / TEI / MOBI / EPUB-canonical / Custom) | C | ✓ |
| P7 | 7 policy-target AST mappings | E | ✓ |
| P8 | Re-test verdict + 3 rationale-parts re-tested + frame-shift named | D | ✓ |
| P9 | Transition steps + next-actionable inquiries | F | ✓ |
| P10 | Open Questions + Frontier items | H | ✓ |

No atoms split across boundaries. No atoms grouped together that should be separate. **High-confidence boundaries.**

---

## Step 4 — Question Tree

### P1 — Executive Summary / Headline Answer
**Q:** "What is the canonical intake format for translations, in one paragraph?"
**Verification criteria:**
- [ ] One-paragraph headline answer
- [ ] Names the three-format layered architecture explicitly
- [ ] Captures the SUBSTITUTE decision-mode + "refines prior Decision 1" relationship label
- [ ] Anchors back to the user's literal question ("core representative format which will be used for translations") without restating verbatim

### P2 — Architectural Commitment + Decision-Mode (META-DECISION)
**Q:** "What architectural commitment underwrites the three-format choice, and how does it relate to the prior intake-concepts finding?"
**Verification criteria:**
- [ ] Three-format layered architecture explained (intake/translate + hand-edit + publishing as three temporal layers with different optima)
- [ ] Why monolithic-single-format was wrong (the prior finding's conflation; the user's pushback identified this)
- [ ] Why three-format-layered is right (each layer has different optimal trade-offs; forcing one format compromises all)
- [ ] Decision-mode = SUBSTITUTE made explicit
- [ ] `refines: devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md` relationship label committed in frontmatter

### P3 — F1: Canonical Intake/Translate = Pandoc-AST-as-JSON
**Q:** "What is the canonical intake + translate format, and how does it work?"
**Verification criteria:**
- [ ] Pandoc-AST-as-JSON identified as the canonical
- [ ] On-disk + in-memory relationship: `IntakeDoc` is the deserialized AST
- [ ] Round-trip mechanics with concrete Pandoc commands (`pandoc -f markdown -t json input.md > canonical.json`; reverse direction)
- [ ] Schema-validation strategy (Pandoc's documented AST types via pandoc-types library; optional project-layer pydantic for type safety)
- [ ] Why this format wins for the canonical role: lossless round-trip; explicit tree (no surface-syntax round-trip-subset issue); queryable; pure data
- [ ] How this maps to the prior finding's `IntakeDoc` (the in-memory class IS the AST shape)

### P4 — F2: Hand-Edit Format = Pandoc's Markdown (REFINED ROLE)
**Q:** "What is the hand-edit format, and how does it relate to the canonical?"
**Verification criteria:**
- [ ] Pandoc's markdown with canonical extensions named (footnotes + pipe_tables + definition_lists + citations + yaml_metadata_block + raw_attribute + bracketed_spans — same set as prior Decision 1)
- [ ] Round-trip-stable subset commitment (the subset of Pandoc-md features that round-trip losslessly with the JSON canonical)
- [ ] Hand-edit workflow described: user opens md → edits → saves → Pandoc converts to JSON → intake re-loads from JSON
- [ ] Prior Decision 1's choice EXPLICITLY PRESERVED in this narrower role (not invalidated; reaffirmed for hand-edit)
- [ ] Why markdown remains the right choice for THIS role (human-readable; byte-stable in any UTF-8 editor; familiar to users)

### P5 — F3: Publishing Format = EPUB 3
**Q:** "What is the publishing format, and how does it work?"
**Verification criteria:**
- [ ] EPUB 3 identified as the publishing format
- [ ] Generation mechanics with concrete Pandoc command (`pandoc -f json -t epub3 -o out.epub canonical.json` plus metadata + per-chapter file structure flags)
- [ ] Reader ecosystem rationale (Apple Books / Google Play Books / Calibre / Adobe Digital Editions / Kobo)
- [ ] Kindle compatibility path: EPUB 3 → Send to Kindle → .azw3 / .kfx (Amazon's converter); NOT direct MOBI
- [ ] MOBI rejection note explicit: Amazon-deprecated August 2022; Pandoc doesn't support it; .azw3 via EPUB 3 is the modern path

### P6 — Rejected Candidates Rationale
**Q:** "What candidates were rejected as canonical, and why?"
**Verification criteria:**
- [ ] **RTF rejected** with structural reasons: editor-fragility (Word / Pages / TextEdit / LibreOffice produce different files on save with no edits — defeats hand-edit recovery workflow); wrong-kind-of-richness (typography, not structure, and prior Decision 2 drops typography); encoding fragility (Windows code pages + Unicode escapes interplay). RTF survives as **accepted user-provided input format** (Pandoc reads it).
- [ ] **TEI rejected** with structural reasons: Pandoc CANNOT READ TEI (only writes TEI Simple per the format-support matrix); a custom TEI reader would break the architectural lever from prior Decision 5; TEI's verbosity (5-10× markdown) defeats hand-editability without TEI expertise. TEI flagged for future archival-output frontier.
- [ ] **MOBI rejected** with structural reasons: Amazon-deprecated; Pandoc doesn't support; Kindle compatibility via EPUB 3 → Send to Kindle is the modern path.
- [ ] **EPUB 3 as canonical INTAKE rejected** with structural reasons: zip archive of xhtml + manifest is heavyweight to hand-edit; round-trip via Pandoc is lossy at the canonical layer (md → epub → md drifts metadata + TOC); apparatus criticus is not first-class in EPUB. (EPUB 3 IS adopted at the publishing layer — see P5.)
- [ ] **Custom format rejected** with structural reasons: Pandoc's AST already exists, is well-designed, and has Python tooling (panflute / pandoc-types). Recreating it as a custom JSON-AST or as `.compldoc` is unnecessary engineering.
- [ ] Each rejection grounded in structural evidence, not preference

### P7 — Calibration-Corpus AST Mappings
**Q:** "How do the calibration corpus's structural elements (Risale-i Nur features) map onto the AST canonical?"
**Verification criteria:**
- [ ] **Hashiye (marginalia for `SourceApparatusPolicy`)** → AST `Note` node with class attribute; preserved losslessly in JSON; rendered in EPUB as `<aside epub:type="footnote">`; editable in Pandoc-md as `[^id]` footnote with content block.
- [ ] **Mevlana couplets (embedded poetry for `EmbeddedPoetryPolicy`)** → AST `LineBlock` with attribution class; preserved.
- [ ] **Bismillah (formulaic opening for `FormulaicOpeningPolicy`)** → AST `Para` with class attribute (e.g., `formulaic-opening`); preserved.
- [ ] **Arabic non-main-language spans (for `NonMainLangPartsPolicy`)** → AST `Span` with `lang=ar` + `dir=rtl` attributes via Pandoc's `bracketed_spans` extension; preserved.
- [ ] **Voice transitions, archaic register, honorifics** → AST `Span` nodes with class + attribute distinctions; preserved per the seven detectors' designs from the prior finding.
- [ ] **NFC diacritic normalization** (per prior C4) applied at intake; stable across all three formats.
- [ ] Confirmation that all seven policy-target perceptions from the prior finding remain expressible in this canonical.

### P8 — Inherited Commitments Re-test on Prior Decision 1 (META-DECISION)
**Q:** "What is the verdict on prior Decision 1 (canonical intake format = Pandoc's markdown), with re-tested evidence?"
**Verification criteria:**
- [ ] Verdict = **REFINED, not OVERTURNED**
- [ ] Prior rationale's three parts each re-tested:
  - "covers needed primitives off-the-shelf" — TRUE for the hand-edit role
  - "single parser surface" — TRUE; Pandoc handles all formats including the new JSON canonical
  - "hand-editable" — TRUE; this is now Pandoc-md's primary role
- [ ] Frame-shift named explicitly: prior conflated three temporal layers (intake/translate + hand-edit + publishing) into one format choice; refined frame decouples
- [ ] Pandoc-md's role PRESERVED in the narrower scope (hand-edit format), not invalidated
- [ ] Other prior commitments (Decisions 2-5) explicitly addressed:
  - Decision 2 (quality target = structure-preservation) — UNCHANGED
  - Decision 3 (IntakeDoc shape = tree + cross-ref-flat) — UNCHANGED at the in-memory level; the on-disk representation is now JSON
  - Decision 4 (7-policy intake/translate split) — UNCHANGED
  - Decision 5 (Pandoc + OCR architectural lever) — STRENGTHENED (all three formats are Pandoc-native)
- [ ] The relationship label `refines:` is the right verb (not `corrects:`, not `supersedes:` — the prior was correct within its frame; the frame is being refined)

### P9 — Transition Plan + Next Actions
**Q:** "What's the transition plan from the prior monolithic architecture to the new layered architecture, and what immediate actions follow?"
**Verification criteria:**
- [ ] What CHANGES in the prior finding's plan:
  - `IntakeDoc` on-disk representation: was Pandoc-md; now JSON-serialized AST
  - The IntakeDoc Schema Design (concept C1 in prior) refined: schema is Pandoc's AST shape + optional project pydantic layer
  - A new design task: EPUB 3 generation pipeline (Pandoc invocation; metadata; per-chapter file structure)
  - A new design task: round-trip-stable Pandoc-md subset definition (which features hand-edit format guarantees to preserve through JSON round-trip)
- [ ] What STAYS THE SAME:
  - The seven policy-perception detectors (B4-B10 in prior) — they perceive in the AST exactly as designed
  - The OCR sub-pipeline (concept A3 in prior) — unchanged
  - The pipeline stages (C3-C9 in prior) — minor adjustment (segment stage targets AST not markdown surface)
  - The quality target (structure-preservation) and metrics framing — unchanged
  - The hand-edit recovery workflow — unchanged in user-facing form (markdown editing)
- [ ] Next-actionable inquiries listed:
  - **MUST** — design the JSON-AST schema (Pandoc-native vs project-pydantic-layered)
  - **MUST** — design the round-trip-stable Pandoc-md subset
  - **COULD** — design the EPUB 3 generation pipeline
  - **COULD** — prototype the AST → EPUB conversion on a Risale-i Nur sample

### P10 — Open Questions / Frontier
**Q:** "What's open after this inquiry?"
**Verification criteria:**
- [ ] Schema-choice question (Pandoc-native AST vs project-pydantic-layer) — committed to be resolved in the JSON-AST schema design inquiry
- [ ] Round-trip-stable Pandoc-md subset definition — committed to be resolved in its own design inquiry
- [ ] EPUB 3 generation flags + per-chapter file structure — committed to be resolved in the EPUB pipeline design inquiry
- [ ] TEI as future archival output — FRONTIER (revisit if scholarly archival need emerges)
- [ ] Pandoc version pinning policy — operational concern; flagged
- [ ] Archival/historical preservation as a potential fifth temporal layer — FRONTIER

---

## Step 5 — Interface Map

| # | Source | Target | What flows | Direction | Assumption coupling |
|---|---|---|---|---|---|
| I1 | P2 (architecture + decision-mode) | P3 / P4 / P5 (format role specs) | Architectural commitment defines the three layers; each format slots into one role | one-way | explicit; P3-P5 cite P2 |
| I2 | P2 (decision-mode) | P8 (re-test) | Decision-mode = SUBSTITUTE shapes the re-test verdict | one-way | explicit; P8 cites P2's decision-mode |
| I3 | P3 (AST shape) | P7 (calibration mappings) | The AST node types determine how policy targets are represented | one-way | explicit; P7 cites P3's AST shape |
| I4 | P3 + P4 + P5 (format commitments) | P9 (transition + next actions) | Format commitments determine what changes in the build path | one-way | explicit |
| I5 | P2 + P8 | P9 (transition plan) | What's refined (verdict on prior) drives the transition path | one-way | explicit |
| I6 | P3 + P4 + P5 + P7 + P8 | P10 (open questions) | What's still unfixed depends on what's fixed | one-way | explicit |
| I7 | P6 (rejections) | INDEPENDENT | No flow into other pieces; standalone rationale | n/a | independent |
| I8 | P2 + P3 + P4 + P5 + P8 | P1 (exec summary) | Digest of architecture + format commits + re-test verdict | one-way (last-step) | explicit |
| I9 | EXTERNAL (prior finding) | P8 (re-test) | Prior Decision 1's three rationale parts ARE the substrate of the re-test | one-way | external |
| I10 | EXTERNAL (prior finding, Decisions 2-5) | P8 (re-test) | Other prior decisions named as UNCHANGED or STRENGTHENED | one-way | external |

**Assumptions-not-data check:**

| Hidden-assumption risk | Check | Result |
|---|---|---|
| P3 / P4 / P5 assume P2's architecture | P2 commits architecture explicitly; P3-P5 cite it | ✓ explicit |
| P7 assumes P3's AST shape is stable | P3 references Pandoc's documented AST; P7 cites Pandoc's node types | ✓ explicit |
| P9 assumes P8's re-test verdict | P9 explicitly cites P8's REFINED verdict | ✓ explicit |
| P6 assumes the rejections don't contradict P3/P4/P5 commitments | P6's rejections are structurally distinct: it rejects formats that aren't P3/P4/P5; consistency maintained | ✓ explicit |
| P1 assumes everyone else exists | P1 is written LAST per dependency order | ✓ explicit |

No hidden coupling detected.

---

## Step 6 — Dependency Order

```
Order      Piece                       Depends on               Can parallelize with
─────      ─────                       ──────────               ────────────────────
1          P2 (architecture)           —                        —
2a         P3 (F1 canonical)           P2                       P4 ‖ P5 ‖ P6 ‖ P8
2b         P4 (F2 hand-edit)           P2                       P3 ‖ P5 ‖ P6 ‖ P8
2c         P5 (F3 publishing)          P2                       P3 ‖ P4 ‖ P6 ‖ P8
2d         P6 (rejections)             —                        P3 ‖ P4 ‖ P5 ‖ P8 (independent)
2e         P8 (re-test)                P2                       P3 ‖ P4 ‖ P5 ‖ P6
3          P7 (calibration AST)        P3                       —
4          P9 (transition + next)      P2 + P8                  —
5          P10 (open questions)        P3 + P4 + P5 + P7 + P8 + P9 | —
6          P1 (exec summary)           ALL                      LAST
```

**Critical-path ordering:** P2 → Group α (P3 ‖ P4 ‖ P5 ‖ P6 ‖ P8) → P7 → P9 → P10 → P1. P6 fully parallel with the rest.

No circular dependencies.

---

## Step 7 — Self-Evaluation

### Minimum 3-dimension evaluation

| Dimension | Check | Verdict | Note |
|---|---|---|---|
| **Independence** | Can each piece be worked on without others (beyond declared interfaces)? | **PASS** | P3-P5 independent of each other given P2; P6 fully independent; P7 depends on P3 only; P8 depends on P2 only; P9 depends on P2+P8; P10 + P1 depend on rest (explicit). |
| **Completeness** | Pieces cover the finding's whole? | **PASS** | Architecture + 3 format roles + rejections + corpus mappings + re-test + transition + open questions + summary = every section the finding needs. No gap. |
| **Reassembly** | Pieces + interfaces → coherent finding? | **PASS** | Concatenated in dependency order, the 10 pieces produce a readable `finding.md` with executive summary, architectural commitment, three format specs, rejections, calibration-corpus implications, re-test, transition plan + next actions, open questions. |

### Full 7-dimension evaluation

| Dimension | Check | Verdict |
|---|---|---|
| Independence | (above) | **PASS** |
| Completeness | (above) | **PASS** |
| Reassembly | (above) | **PASS** |
| **Tractability** | Each piece small enough for one focused Innovation pass? | **PASS** — P3 is heaviest (canonical format spec + Pandoc commands + schema discussion) but bounded; P6 has 5 sub-rejections × ~80 words each; P7 has 7 per-policy mappings × ~40 words each. All tractable. |
| **Interface clarity** | All cross-piece flows explicit? | **PASS** — I1-I10 mapped; assumptions-not-data check ran clean. |
| **Balance** | Roughly equal complexity? | **MILD IMBALANCE** — P3 (canonical) ≈ 1.5x P5 (publishing); P6 (5 rejections) is moderately heavy. Acceptable. If Innovation finds P6 unwieldy, the 5 rejections could each become a paragraph rather than a section. |
| **Confidence** | Top-down ↔ bottom-up agree? | **HIGH** — atoms group as predicted; no boundary disagreements. |

### Determination-mechanism piece check

Concepts requiring runtime determination:
- "Is this file an AST-JSON or md or EPUB?" — runtime check via file extension / magic bytes; downstream of this finding (concept A5 in prior — format detection).
- "Is this Pandoc-md feature in the round-trip-stable subset?" — runtime check during hand-edit save; defined by the round-trip-stable subset design (open question P10).

These mechanisms are NAMED in the finding (P9, P10) but DEFINED downstream. No missing piece in this finding.

### Failure-mode self-scan

- **Premature decomposition:** ✗ Sensemaking ran first; SV6 stabilized the whole.
- **Wrong boundaries:** ✗ Top-down + bottom-up agree; cuts at low-coupling valleys (between architecture / format roles / rejections / re-test / transition / corpus / open / summary).
- **Hidden coupling:** ✗ Assumptions-not-data check ran; all flows mapped.
- **Missing pieces:** ✗ Completeness pass + Determination-mechanism check.
- **Over-decomposition:** ✗ 10 pieces; each has substantive content.
- **Ignoring dependencies:** ✗ Critical path P2 → α → P7 → P9 → P10 → P1 explicit.
- **Imbalanced decomposition:** ⚠ Mild — P3 and P6 heavier than P5; not extreme; documented.

### Self-assessment verdict

**PROCEED to Innovation.** 10 pieces with explicit interfaces, dependency ordering, and verification criteria. P6 (rejections) flagged for monitoring during Innovation — if the 5 sub-rejections become unwieldy as a single piece, they can each become their own paragraph.

---

## Final Deliverable — Summary Table

| # | Piece | Question | Order |
|---|---|---|---|
| P1 | Executive summary | What is the canonical format, in one paragraph? | last |
| P2 | Architectural commitment + decision-mode (META) | What architecture underwrites the three-format choice, and how does it relate to the prior? | first |
| P3 | F1 canonical = Pandoc-AST-as-JSON | What is the canonical intake/translate format, and how does it work? | parallel α |
| P4 | F2 hand-edit = Pandoc's markdown | What is the hand-edit format, and how does it relate to the canonical? | parallel α |
| P5 | F3 publishing = EPUB 3 | What is the publishing format, and how does it work? | parallel α |
| P6 | Rejected candidates rationale | What candidates were rejected as canonical, and why? | parallel α |
| P7 | Calibration-corpus AST mappings | How do Risale-i Nur structural elements map onto the AST canonical? | after P3 |
| P8 | Inherited Commitments Re-test (META) | What is the verdict on prior Decision 1, with evidence? | parallel α |
| P9 | Transition plan + Next actions | What changes from the prior monolithic plan, and what comes next? | after P2 + P8 |
| P10 | Open questions / Frontier | What's open after this inquiry? | after rest |
