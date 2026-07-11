# Decomposition — intake preprocessing operations

## User Input

Source: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/_branch.md`

Upstream outputs: `articulate_simple.md` + `surfacing.md` + `sensemaking.md`.

Substrate: SV6 stabilized model = 8-category preprocessing pipeline anchored by the "structural, not semantic" scope-line principle, with 5 load-bearing meta-decisions (scope-line; depth; format-priority; two-layer corpus model; translation-quality-floor sub-category).

---

## Step 1 — Perceive Coupling Topology

### Elements in the whole (Innovation will produce)

- **A** — Executive summary (one paragraph)
- **B** — Scope-line principle ("structural, not semantic") + Decision-mode commitment
- **C** — Depth-of-boundary policy (source-driven up to HTML5 h1-h6)
- **D** — Format-priority commitment (EPUB-first + PDF-fallback)
- **E** — Two-layer corpus model (generic v0.2 core + Category 8 extensions)
- **F** — Translation-quality-floor sub-category naming (members + semantics)
- **G** — Category 1 — Foundational normalization (operations + semantics)
- **H** — Category 2 — Translation-quality-floor (operations)
- **I** — Category 3 — Paratext stripping (operations + extension beyond baseline)
- **J** — Category 4 — Source-format metadata + provenance (operations)
- **K** — Category 5 — Structural detection (operations, "structural not semantic" boundary applied)
- **L** — Category 6 — Format-specific repair (operations per source format)
- **M** — Category 7 — Quality / hygiene (informational flags)
- **N** — Category 8 — Corpus-specific extensions (operations + how attached)
- **O** — Rejected candidates rationale (from surfacing's 153)
- **P** — Inherited Commitments Re-test (4 priors)
- **Q** — Transition plan + Next Actions (MUST / COULD / DEFERRED)
- **R** — Open Questions / Frontier

### Coupling analysis (gradient)

**Strong coupling:**
- B (scope-line) ↔ every category piece (G-N) — the principle decides per-operation verdicts.
- C (depth policy) ↔ K (Category 5 structural detection) — depth IS a property of structural detection.
- D (format priority) ↔ L (Category 6 format-specific repair) — priority determines which sub-bucket is v0.2 vs future.
- E (two-layer corpus model) ↔ N (Category 8 content) — the two-layer model IS the architectural separation that makes Category 8 separate.
- F (quality-floor sub-category) ↔ H (Category 2 content) — the sub-category name IS what differentiates Category 2's role.
- P (inherited re-test) ↔ B (scope-line) — re-test verifies the recent "leave content unclassified" narrowing.

**Moderate coupling:**
- O (rejected candidates) ↔ B (scope-line) — rejections are explained via the scope-line.
- Q (transition plan) ↔ each category piece — actions derive from category content.
- A (executive summary) ↔ everything — summary references all commitments.

**Weak coupling between categories themselves (G-N):**
- Each category answers a distinct "what operations live here?" question.
- The scope-line principle keeps boundaries clean — no operation crosses categories.
- Category-to-category coupling routed through meta-decisions (B), not direct.

### Major clusters

1. **META-DECISIONS cluster** (B, C, D, E, F, P) — principles + relationship labels. Tightly coupled internally; provides the contract for the categories cluster.
2. **CATEGORY CONTENT cluster** (G, H, I, J, K, L, M, N) — the 8 categories' actual operations. Internally cohesive per category; inter-category coupling LOW because meta-decisions absorb the cross-cutting logic.
3. **DERIVED cluster** (Q, R, A) — transition + open questions + summary. Depends on meta-decisions + content.
4. **RELATIONSHIP cluster** (O, P) — rejected items + inherited re-test. Depends on meta-decisions.

### Major boundaries

- **Boundary 1:** between META-DECISIONS and CATEGORY CONTENT. Interface: the scope-line principle (B) is the contract; categories consume it.
- **Boundary 2:** between distinct categories within CATEGORY CONTENT. Interface: each category is independent given the principle.
- **Boundary 3:** between CATEGORY CONTENT and DERIVED. Interface: categories' operation lists are inputs to transition plan.
- **Boundary 4:** between RELATIONSHIP cluster and the rest. Interface: rejections cite the scope-line; re-test cites the priors' commitments.

---

## Step 2 — Detect Boundaries (Top-Down)

Optimal piece set bundles tightly-coupled meta-decisions with their dependent content where coupling is dense:

- C (depth) bundles with K (Category 5) — coupling is dense; depth IS Category 5's policy.
- D (format priority) bundles with L (Category 6) — same reason.
- E (two-layer corpus) bundles with N (Category 8) — same reason.
- F (quality-floor sub-category) bundles with H (Category 2) — same reason.
- B (scope-line) remains its own piece — it touches every category; should be primary.
- Smaller related categories bundle: G+H (Categories 1+2 — foundational tier); I+J (Categories 3+4 — document-level always-run); M alone (Category 7 — distinct semantics: informational not corrective).

### Initial piece set (boundary-detection result)

| # | Piece | What's inside |
|---|---|---|
| **P1** | Executive summary | One-paragraph summary |
| **P2 (META)** | Scope-line principle + Decision-mode | B + the decision-mode framing |
| **P3 (META + CONTENT)** | Two-layer corpus model + Category 8 content | E + N (architectural separation + extension operations) |
| **P4 (CONTENT)** | Categories 1+2 (foundational tier + quality-floor sub-category) | G + H + F (sub-category name within this tier) |
| **P5 (CONTENT)** | Categories 3+4 (paratext + metadata/provenance) | I + J |
| **P6 (CONTENT + META)** | Category 5 (structural detection) + depth-of-boundary policy | K + C |
| **P7 (CONTENT + META)** | Category 6 (format-specific repair) + format-priority commitment | L + D |
| **P8 (CONTENT)** | Category 7 (quality / hygiene informational flags) | M |
| **P9 (RELATIONSHIP)** | Rejected candidates rationale | O |
| **P10 (META + RELATIONSHIP)** | Inherited Commitments Re-test | P |
| **P11 (DERIVED)** | Transition plan + Next Actions | Q |
| **P12 (DERIVED)** | Open Questions / Frontier | R |

**Total: 12 pieces.** Within the user-guided 8-12 range.

---

## Step 3 — Validate Boundaries (Bottom-Up Check)

### Atoms

- Specific operation names (e.g., NFC normalization; sentence segmentation; running header detection; spine reassembly).
- Specific principle commitments (e.g., "structural, not semantic"; source-driven up to h6; EPUB-first + PDF-fallback).
- Specific re-test verdicts (e.g., "PRESERVED and STRENGTHENED" per prior commitment).
- Specific rejection rationales (e.g., "per-element provenance is OUT because semantic-not-structural").
- Specific MUST / COULD / DEFERRED action items.

### Atom-to-piece mapping check

| Atom type | Pieces |
|---|---|
| Foundational operations (NFC; whitespace; ligatures…) | P4 ✓ |
| Quality-floor operations (sentence seg; mojibake…) | P4 ✓ |
| Paratext operations (running headers; page numbers…) | P5 ✓ |
| Metadata/provenance operations | P5 ✓ |
| Structural detection operations (hierarchy; lists; tables…) | P6 ✓ |
| Depth policy commitment | P6 ✓ (bundled) |
| Format-specific operations (EPUB / PDF / Word / plain-text) | P7 ✓ |
| Format priority commitment | P7 ✓ (bundled) |
| Quality / hygiene flags | P8 ✓ |
| Corpus-specific extension operations | P3 ✓ (bundled with two-layer model) |
| Scope-line principle | P2 ✓ |
| Decision-mode framing | P2 ✓ |
| Two-layer corpus model | P3 ✓ |
| Translation-quality-floor sub-category naming | P4 ✓ (bundled) |
| Rejection rationales | P9 ✓ |
| Inherited commitments re-test | P10 ✓ |
| MUST / COULD / DEFERRED items | P11 ✓ |
| Open questions / frontier items | P12 ✓ |
| One-paragraph summary | P1 ✓ |

**No atom misplaced.** No atom split across pieces (atoms cohere within their piece). **Boundaries validated.**

**Confidence:** HIGH — top-down boundaries and bottom-up atoms agree.

---

## Step 4 — Express as Question Tree

### P1 — Executive Summary

**Q:** *What is the v0.2 intake preprocessing pipeline in one paragraph?*

**Verification criteria:**
- [ ] Names the scope-line principle ("structural, not semantic")
- [ ] Names the 8 categories (with brief role per category)
- [ ] Names the depth policy (source-driven up to HTML5 h1-h6)
- [ ] Names the format priority (EPUB-first + PDF-fallback)
- [ ] Names the two-layer corpus model (generic core + Category 8 extensions)
- [ ] States the relationship to the prior canonical-format finding (extends NFC + paratext baseline)
- [ ] Sized for one-paragraph at-a-glance reading

### P2 (META-DECISION) — Scope-line principle + Decision-mode commitment

**Q:** *What is the load-bearing scope-line principle that decides per-operation preprocessing-vs-classification verdicts, and what shape does this finding's deliverable take?*

**Verification criteria:**
- [ ] Commits "structural, not semantic" as the load-bearing principle
- [ ] States the operational test-question: "Does identifying this require knowing what cultural/linguistic role it plays?"
- [ ] Names the test's two outcomes: yes → semantic (classification; OUT); no → structural (preprocessing; IN)
- [ ] Commits the decision-mode: categorized recommended v0.2 set with rejected items + rationale
- [ ] States the relationship-label: `extends:` the prior canonical-format finding's NFC + paratext baseline
- [ ] Cites the gray-zone case logic — how the principle decides ambiguous operations (e.g., footnote extraction is positional/structural, not semantic role tagging)

### P3 (META-DECISION + CONTENT) — Two-layer corpus model + Category 8 content

**Q:** *What is the two-layer corpus model that separates generic v0.2 preprocessing from calibration-corpus-tuned extensions, and what operations live in the Category 8 extension layer?*

**Verification criteria:**
- [ ] Commits the two-layer architectural separation
- [ ] Names what differentiates "generic" from "corpus-tuned" (the test: does this operation depend on knowing the corpus-specific structural vocabulary?)
- [ ] Enumerates Category 8 operations (letter-spaced un-spacing; Risale-i-Nur structural-marker keyword recognition for Mukaddeme / Mes'ele / Hâtime / Tenbih / Bismillah; other Risale-i-Nur-specific patterns)
- [ ] Specifies how Category 8 attaches to v0.2 (opt-in extension layer; NOT part of generic flow; activates when corpus context is named)
- [ ] Honors the `project_scope` memory commitment (generic project; Risale-i Nur as calibration corpus, not purview)

### P4 (CONTENT) — Categories 1+2 — Foundational tier + Translation-quality-floor

**Q:** *What operations live in the foundational tier (Category 1 byte-consistency + Category 2 translation-quality-floor), and what differentiates the two sub-tiers within "always-run, format-agnostic" preprocessing?*

**Verification criteria:**
- [ ] Enumerates Category 1 operations: NFC normalization; whitespace normalization (collapse runs, trim line ends, normalize newlines to LF); zero-width character removal (U+200B-D); soft hyphen removal (U+00AD); quotation mark normalization; dash normalization; ellipsis normalization; ligature decomposition; broken-Unicode detection
- [ ] Enumerates Category 2 operations: sentence segmentation (with abbreviation handling); paragraph boundary detection; document-level language identification; hyphenation-at-line-break repair; mojibake repair
- [ ] Names the translation-quality-floor sub-category and its members (Category 2 operations)
- [ ] States the semantic distinction: Category 1 = byte-consistency (downstream tools see consistent bytes); Category 2 = translation-quality-load-bearing (LLM translation quality improves with these ops in place)
- [ ] States "always run; format-agnostic" semantics for both sub-tiers
- [ ] Specifies library / tool references where applicable (`unicodedata.normalize('NFC', ...)`, `ftfy` for mojibake, `spacy` / `nltk` for sentence segmentation)

### P5 (CONTENT) — Categories 3+4 — Paratext + Metadata/Provenance

**Q:** *What operations live in the always-run document-level tier (Category 3 paratext stripping + Category 4 source-format metadata + provenance)?*

**Verification criteria:**
- [ ] Enumerates Category 3 operations: running headers / footers; page numbers / folios; catchwords; editorial boilerplate; publisher metadata at chapter starts; blank pages; decorative ornaments (asterism / dingbats); watermarks ("scanned by" inserts); library / acquisition stamps
- [ ] Enumerates Category 4 operations: source-format detection; source-file path; SHA-256 checksum; intake-timestamp; intake-tool-version; title / author / publication date / publisher extraction; source-language declaration (from source metadata or auto-detected); source-format metadata pass-through (EPUB OPF / PDF /Info / Word docProps)
- [ ] Specifies how paratext detection composes with source-format reading (paratext detection is format-aware — EPUB rarely has paratext; PDF often does)
- [ ] References the post-repair canonical format finding's Category 3 baseline as the inherited starting point

### P6 (CONTENT + META) — Category 5 — Structural detection + Depth-of-boundary policy

**Q:** *What structural detection operations are in Category 5, and what depth-of-boundary policy governs them?*

**Verification criteria:**
- [ ] Enumerates Category 5 operations: heading hierarchy preservation (source-driven, h1-h6); heading hierarchy INFERENCE (when source is flat — e.g., flat-h1 EPUB); list structural detection (numbered / bulleted / nested); table structural detection (rows × cells; structure only); quote-block structural detection (block vs inline); verse-block structural detection (line-broken; centered); footnote / endnote STRUCTURAL extraction (apparatus separation by position + anchor; NOT semantic-role tagging); cross-reference structural preservation (`href` + matching `id`); figure / illustration caption structural separation; drop-cap normalization
- [ ] Commits the depth-of-boundary policy: source-driven hierarchy preservation, up to HTML5 h1-h6 ceiling
- [ ] Specifies the hierarchy-inference approach for flat-h1 sources (e.g., detect Mukaddeme / Mes'ele markers in body and promote to h2/h3) — note this may invoke Category 8 corpus-extension for Risale-i-Nur sources
- [ ] Cites the empirical evidence (Asa-yı Musa EPUB has flat h1; needs inference)
- [ ] States the "structural, not semantic" boundary on Category 5: footnote extraction is positional/relational structural (where it lives; what it references) — NOT semantic role tagging (this is hashiye; this is editorial annotation; that's classification, deferred)
- [ ] Names the user's depth-4 instinct AS HONORED (empirical mean for literary texts) — and the policy as a generalization (source-driven up to h6)

### P7 (CONTENT + META) — Category 6 — Format-specific repair + Format-priority commitment

**Q:** *What format-specific repair operations are in Category 6, and what format priority governs which are v0.2 vs future?*

**Verification criteria:**
- [ ] Enumerates EPUB operations: spine reassembly (read content documents in spine order); CSS-presentation extraction (`class="bold"` → `<strong>`); heading-level inference (for flat-h1 EPUBs like Asa-yı Musa); OPF metadata extraction
- [ ] Enumerates PDF operations: mid-word hyphen repair (line-wrap artifacts); column-order repair (multi-column); bidi-fix (for broken-bidi Arabic — the Asa-yı Musa PDF case); italic / bold recovery (via mutool / pdf2htmlEX secondary pass); OCR fallback (for image-only Arabic — the Muhakemat case)
- [ ] Enumerates Word operations: style-mapping (Heading 1-9 → semantic); run-merge (consecutive runs with same formatting)
- [ ] Enumerates plain-text operations: encoding detection (BOM + chardet + fallback); line-ending normalization
- [ ] Commits the format priority: EPUB-first + PDF-with-OCR-fallback for v0.2; Word + plain-text as future format additions
- [ ] Cites the empirical evidence for priority (EPUB intake is significantly cheaper — no OCR; no bidi-fix; structure already encoded); PDF needs OCR for image-only Arabic + bidi-fix for broken-bidi Arabic
- [ ] References Decision 5 (Pandoc + OCR architectural lever) as the underlying mechanism

### P8 (CONTENT) — Category 7 — Quality / hygiene (informational flags)

**Q:** *What informational quality flags does intake emit (not corrective; just flags for downstream consumers)?*

**Verification criteria:**
- [ ] Enumerates Category 7 flags: suspicious-line-break detection (mid-word; mid-sentence); truncation detection (file ends mid-sentence); document-completeness check (ToC matches headings; footnote refs match footnotes); duplicate-content detection (boilerplate; OCR re-runs); orphan-content detection (single char / one-word paragraphs); confusables detection (Cyrillic А vs Latin A); encoding-confidence flagging (when Category 2 mojibake detection is uncertain)
- [ ] States the "informational, not corrective" semantics — flags are emitted as metadata / sidecar / log entries; intake does NOT auto-correct
- [ ] Specifies how flags are exposed (proposal: a structured sidecar JSON or a `<meta>` block in the canonical HTML5)
- [ ] Distinguishes Category 7 from Categories 1+2 (Category 1+2 are corrective; Category 7 is observational)

### P9 (RELATIONSHIP) — Rejected candidates rationale

**Q:** *Of surfacing's 153 candidates, which are explicitly rejected for v0.2, and what is the structural reason per rejection?*

**Verification criteria:**
- [ ] Per-element provenance / per-span lang= tagging / 7-policy detection / voice marking / per-element classification — REJECTED with structural reason "crosses scope-line into semantic role tagging; deferred per recent scope narrowing"
- [ ] Depth-4 as absolute cap — REJECTED with structural reason "replaced by source-driven up-to-h6 policy; depth-4 was instinct close to empirical mean but not absolute"
- [ ] PDF-only or EPUB-only v0.2 — REJECTED with structural reason "format priority commits both with rank order"
- [ ] Drop-everything-corpus-specific — REJECTED with structural reason "two-layer corpus model preserves Risale-i-Nur-tuned operations as Category 8 extensions; project remains generic at the v0.2 generic core"
- [ ] Generative-only output (no recommendation commit) — REJECTED with structural reason "WHY-axis ambiguity included v0.2-engineering-scope-setting; surfacing's breadth-first 153-candidate output satisfied the generative-only need; the categorized recommended set satisfies the commit-need"
- [ ] Tokenization (L6) — REJECTED with structural reason "translate-stage's job, not intake"
- [ ] Per-translation-output format expansion (C16-C17) — REJECTED with structural reason "publishing-stage or translate-stage prep, not intake preprocessing"

### P10 (META-DECISION + RELATIONSHIP) — Inherited Commitments Re-test

**Q:** *For each prior this finding inherits from (post-repair canonical format finding; original intake-concepts finding), what is the per-commitment re-test verdict?*

**Verification criteria:**
- [ ] Re-tests NFC + paratext baseline (from `devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/finding.md`): PRESERVED and EXTENDED (NFC is Category 1; paratext is Category 3; baseline expands into structured 8-category set)
- [ ] Re-tests "leave content unclassified" scope narrowing (from recent conversation; not yet in a finding): PRESERVED via the scope-line principle ("structural, not semantic"); cite the chain of preservation
- [ ] Re-tests Decision 2 structure-preservation quality target (from `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`): PRESERVED and STRENGTHENED (Category 5 structural detection is explicitly aligned)
- [ ] Re-tests Decision 5 Pandoc + OCR architectural lever (from same prior): PRESERVED and STRENGTHENED (Category 6 format-specific repair explicitly leans on Pandoc readers and OCR)
- [ ] Re-tests HTML5 canonical commitment (from `devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/finding.md`): COMPATIBLE (the preprocessing set produces structure that fits HTML5 — h1-h6 hierarchy; semantic elements `<aside>` / `<figure>` etc. — without crossing into semantic classification)
- [ ] Commits the relationship-label: `extends:` the prior canonical-format finding (additive: NFC + paratext become Categories 1+3 in a broader 8-category set)
- [ ] Distinguishes "extends" from "refines" or "supersedes" — nothing prior is replaced; the set grows

### P11 (DERIVED) — Transition plan + Next Actions

**Q:** *What needs to happen to operationalize this preprocessing pipeline for v0.2 (MUST / COULD / DEFERRED)?*

**Verification criteria:**
- [ ] Lists MUST items: per-category operation specs ready for engineering (8 categories × per-operation spec); the hierarchy-inference algorithm spec (for flat-h1 sources, Category 5); the format-specific Pandoc invocation patterns (Category 6 — EPUB and PDF first); the Category 7 flag-exposure mechanism (sidecar JSON or HTML5 `<meta>`); the integration with the prior canonical-format finding's existing Next Actions (some MUSTs may merge)
- [ ] Lists COULD items: Category 8 extensions API design (how corpus extensions plug in); the hierarchy-inference for more corpora; the quality-floor sub-category boundary refinements
- [ ] Lists DEFERRED items: Word + plain-text format support; cross-corpus validation (test against non-Risale-i-Nur corpora); classification work (per-element provenance / per-policy detection — the deferred classification scope from the recent narrowing)
- [ ] Each item has Per-item format: What / Who / Gate / Why
- [ ] Notes COULD-vs-MUST dependency gating where applicable (per CONCLUDE protocol)

### P12 (DERIVED) — Open Questions / Frontier

**Q:** *What is still open after this commitment, with what revival triggers?*

**Verification criteria:**
- [ ] Names scope-line principle's edge-case adjudication (the gray-zone operations not yet visited; revival: when a new gray-zone operation surfaces)
- [ ] Names hierarchy-inference algorithm specification (for flat-h1 sources; revival: when MUST item lands)
- [ ] Names quality-floor sub-category boundary refinements (revival: when empirical evidence shows a Category-1 operation should be promoted to quality-floor)
- [ ] Names Category 8 extension API (revival: when a second corpus enters the project)
- [ ] Names format expansion (Word + plain-text; revival: when project source-mix expands)
- [ ] Names cross-corpus validation (revival: scaling beyond calibration corpus)
- [ ] Names classification (the deferred semantic-role tagging work; revival: when minimal-intake mode has been tested in production and translation quality requires it)
- [ ] Each open question has Refinement Trigger (time-bound / condition-bound / observable) per the style rule

---

## Step 5 — Map Interfaces

| Source | Target | What flows | Direction |
|---|---|---|---|
| P2 (scope-line principle) | P3 — P9 (all content/relationship pieces) | the "structural, not semantic" test-question; the gray-zone adjudication logic | one-way provide |
| P3 (two-layer model) | P9 (rejections) | the rationale for "drop-corpus-specific" being REJECTED (because Category 8 preserves them separately) | one-way provide |
| P3 (Category 8) | P11 (transition) | Category 8 extensions API as a COULD/DEFERRED item | one-way provide |
| P4 (Categories 1+2) | P11 (transition) | per-operation MUST items for foundational + quality-floor | one-way provide |
| P5 (Categories 3+4) | P11 (transition) | per-operation MUST items for paratext + metadata/provenance | one-way provide |
| P6 (Category 5 + depth) | P11 (transition) | per-operation MUST items for structural detection + hierarchy-inference algorithm MUST | one-way provide |
| P6 (Category 5) | P3 (Category 8) | Cat 5's hierarchy-inference INVOKES Cat 8 extensions when corpus context is named | one-way reference |
| P7 (Category 6 + format priority) | P11 (transition) | per-format MUST items + format-priority decision affecting v0.2 vs future | one-way provide |
| P7 (Category 6) | P5 (Category 4) | format-specific reading produces metadata that feeds Category 4 extraction | one-way provide |
| P8 (Category 7) | P11 (transition) | flag-exposure mechanism MUST | one-way provide |
| P9 (rejections) | P10 (inherited re-test) | rejected items include semantically-tagging ops; re-test verifies scope-narrowing preserved | one-way provide |
| P10 (inherited re-test) | P11 (transition) | re-tests prior MUSTs against this inquiry's MUSTs; identifies merge candidates | one-way provide |
| P10 (inherited re-test) | P1 (executive summary) | provides the `extends:` relationship-label | one-way provide |
| P10 (inherited re-test) | P2 (scope-line) | re-tests scope-narrowing commitment (verifies "structural, not semantic" preserves narrowing) | bidirectional |
| P11 (transition) | P12 (open questions) | transition's DEFERRED items become open-question revival triggers | one-way provide |
| All pieces | P1 (executive summary) | summary references everything | one-way provide (everything → A) |

### Assumptions-not-data check (Refinement note)

Each piece's assumptions about what the others provide:

- **P3 — P9 ASSUME P2 has committed the scope-line principle** (otherwise their verdicts have no rationale). Interface: P2 must be read first. ✓
- **P11 (transition) ASSUMES** all category pieces (P4-P8) and meta-decision pieces (P2, P3, P10) have committed contents. Interface: Phase 2 + Phase 3 of dependency order both feed P11. ✓
- **P12 ASSUMES** the deferred / open items from P11 are available. Interface: P11 must feed P12. ✓
- **P3 ASSUMES** the generic v0.2 core (Categories 1-7) is well-defined elsewhere; Category 8 sits OUTSIDE it. Interface: P3's content references the generic core's existence; P4-P8 provide the generic core. ✓
- **P6 (Category 5 hierarchy-inference) ASSUMES** P3 (Category 8) is reachable as an extension when corpus context is named. Interface: P6 → P3 reference; documented. ✓
- **P10 ASSUMES** prior findings' content is correctly characterized. Interface: cite the priors' file paths verbatim. ✓

**No hidden coupling found.** All assumptions are documented in the Interface Map.

---

## Step 6 — Order by Dependency

### Dependency graph

```
                       ┌──── P2 (META — scope-line) ────┐
                       │                                  │
                       │                                  ▼
                       │                ┌─── P3 (META + CONTENT — two-layer + Cat 8) ───┐
                       │                │                                                  │
                       │                │                                                  │
                       │                │   ┌── P4 (CONTENT — Cat 1+2) ──┐                │
                       │                │   ├── P5 (CONTENT — Cat 3+4) ──┤                │
                       │                │   ├── P6 (CONTENT+META — Cat 5 + depth) ─┤      │
                       │                │   ├── P7 (CONTENT+META — Cat 6 + format) ┤      │
                       │                │   ├── P8 (CONTENT — Cat 7) ──┘                  │
                       │                │   └── P9 (RELATIONSHIP — rejections) ─┘         │
                       │                ▼                                                  │
                       │                P10 (META + RELATIONSHIP — inherited re-test) ────┘
                       │                │
                       │                ▼
                       └──────────────► P11 (DERIVED — transition + Next Actions)
                                        │
                                        ▼
                                        P12 (DERIVED — open questions + frontier)
                                        │
                                        ▼
                                        P1 (executive summary — LAST)
```

### Critical path

P2 → (P3 ‖ P4 ‖ P5 ‖ P6 ‖ P7 ‖ P8 ‖ P9) → P10 → P11 → P12 → P1

### Parallelizable groups

- **Group A (after P2):** P3, P4, P5, P6, P7, P8, P9 — all independent of each other once P2 is committed.
- **Group B (after Group A):** P10 depends on P2, P9; P11 depends on Group A; P12 depends on P11.
- **P1 LAST:** depends on everything.

### Phase summary

- **Phase 1:** P2 (scope-line principle) — ONE piece, MUST be first.
- **Phase 2:** P3, P4, P5, P6, P7, P8, P9 — seven pieces in parallel.
- **Phase 3:** P10 (inherited re-test) — depends on Phase 2 + P2.
- **Phase 4:** P11 (transition) — depends on Phase 2 + Phase 3.
- **Phase 5:** P12 (open questions) — depends on P11.
- **Phase 6:** P1 (exec summary) — depends on everything.

---

## Step 7 — Self-Evaluate

### Minimum 3 dimensions (always)

| Dimension | Check | Pass? | Reason |
|---|---|---|---|
| **Independence** | Can each piece be worked on without the others existing? | **PASS** | Each piece's question is answerable given the documented interfaces (P2 first; then category pieces in parallel; then derived pieces). No piece requires reading another's content beyond what the interfaces specify. |
| **Completeness** | Do the pieces cover the whole? | **PASS** | All 8 categories covered (G-N → P3-P8); all 5 meta-decisions covered (B,C,D,E,F → P2/P3/P6/P7/P4); rejected items covered (O → P9); inherited re-test covered (P → P10); transition covered (Q → P11); open questions covered (R → P12); summary covered (A → P1). No element from Step 1's whole is unassigned. |
| **Reassembly** | Given all pieces answered + all interfaces satisfied, is the original problem solved? | **PASS** | The original problem (specify v0.2 intake preprocessing pipeline including structural boundary detection and creative additional operations) is solved when: (a) the scope-line principle is committed [P2]; (b) the 8 categories' contents are specified [P3-P8]; (c) rejections are explained [P9]; (d) prior commitments are re-tested [P10]; (e) transition is planned [P11]; (f) open questions are named [P12]; (g) summary integrates [P1]. The reassembly produces the finding. |

### Full 7 dimensions (high-stakes; this inquiry warrants)

| Dimension | Check | Pass? | Notes |
|---|---|---|---|
| Independence | Each piece works alone? | PASS | (as above) |
| Completeness | Pieces cover whole? | PASS | (as above) |
| Reassembly | Pieces + interfaces = whole? | PASS | (as above) |
| **Tractability** | Each piece small enough for single focused pass? | **PASS** | Each piece is one category, one meta-decision, or one relationship — sized for single-pass innovation generation. |
| **Interface clarity** | Cross-piece flows explicit? No hidden dependencies? | **PASS** | 15 interfaces mapped (Step 5); assumptions-not-data check applied; no hidden coupling found. |
| **Balance** | Complexity proportional? | **BOUNDARY-APPROACHED but ACCEPTABLE** | P6 (Cat 5 structural detection + depth) and P7 (Cat 6 format-specific repair + format-priority) are larger than P8 (Cat 7 informational flags) — but this reflects substantive importance: structural detection and format-specific repair are load-bearing for the pipeline, while informational flags are observational. The imbalance is intentional and proportional to substantive weight. P8 doesn't warrant inflation. |
| **Confidence** | Top-down + bottom-up agree on boundaries? | **PASS** | All atoms map to single pieces (Step 3); no atom split across boundaries; no atom misplaced. Top-down clustering and bottom-up atom grouping converge. |

### Determination-mechanism piece check (Refinement note)

The Q-tree includes the load-bearing concept "structural, not semantic" whose application depends on a runtime determination per-operation. Is there a piece addressing HOW the determination is performed?

**Yes — P2 specifies the test-question:** *"Does identifying this require knowing what cultural/linguistic role it plays?"* with the two outcomes (yes → semantic, OUT; no → structural, IN). The determination mechanism is documented in the piece that commits the principle. ✓

Reassembly check PASSES.

---

## Final Deliverable

### Coupling Map (summary)

- META cluster (B,C,D,E,F,P) — tightly coupled; provides the contract.
- CATEGORY CONTENT cluster (G-N) — internally cohesive per category; inter-category loose via meta-decisions.
- DERIVED cluster (Q,R,A) — depends on META + CONTENT.
- RELATIONSHIP cluster (O,P) — depends on META.

### Question Tree (12 pieces)

P1 Executive Summary · P2 Scope-line + Decision-mode · P3 Two-layer + Cat 8 · P4 Cat 1+2 · P5 Cat 3+4 · P6 Cat 5 + depth · P7 Cat 6 + format priority · P8 Cat 7 · P9 Rejected candidates · P10 Inherited re-test · P11 Transition + Next Actions · P12 Open Questions

### Interface Map

15 interfaces documented (Step 5). Assumptions-not-data check applied; no hidden coupling.

### Dependency Order

P2 → (P3 ‖ P4 ‖ P5 ‖ P6 ‖ P7 ‖ P8 ‖ P9) → P10 → P11 → P12 → P1

### Self-Evaluation

- Minimum 3/3 PASS (Independence; Completeness; Reassembly)
- Full 7/7 PASS (with Balance flagged BOUNDARY-APPROACHED but justified as intentional reflecting substantive weight)
- Determination-mechanism check PASS

**Verdict: PROCEED to Innovation.**
