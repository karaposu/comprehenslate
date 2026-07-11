# Critique — document intake handling concepts

## User Input

Candidates evaluated: Innovation's 9 principal candidates (P1-P9) + 3 Inversion-candidates (at P2, P3, P8). Adversarial focus areas: anti-hallucination grounding · decision rigor · detector fidelity · engineering-actionability · methodology discipline · pseudocode coherence · re-test rigor · concept-name audit · meta-decision testing · assembly verification.

---

## Phase 0 — Dimension Construction

### Extracted dimensions

Sensemaking output anchors the dimension set. Constraints (C1-C7), Key Insights (KI1-KI8), Foundational Principles (FP1-FP4), Meaning-Nodes (MN1-MN6) plus the 5 load-bearing decisions yield:

| # | Dimension | Weight | Question | Source |
|---|---|---|---|---|
| **D1** | Anti-hallucination grounding | **CRITICAL** | Does every load-bearing claim cite (a) schema-ref OR (b) Pandoc-fact OR (c) sensemaking-anchor OR (d) explicit-extrapolation-flag? | Sensemaking SV6 methodology disclaimer + P2 four-source taxonomy |
| **D2** | Schema fidelity (external-anchor) | **CRITICAL** | Do the 7 policy class names match `SKILL/references/config/schemas.py` verbatim? Is the schema's role respected (not redefined)? | Sensemaking C1 + Decision 4 |
| **D3** | Pandoc-fact accuracy (external-anchor) | **CRITICAL** | Are claimed Pandoc extensions actually Pandoc-native? Is the AST node naming (Header/Span/Div/etc.) accurate? | Sensemaking KI8 + Decision 1/5 |
| **D4** | Detector fidelity (substance) | HIGH | Are the 7 perception detector signals realistic, sufficient, and not over-claiming? | Sensemaking Decision 4 + adversarial-focus directive |
| **D5** | Engineering-actionability | HIGH | Are ENGINEER-tagged concepts truly ready for code, or do they hide design dependencies on DESIGN-NEXT-INQUIRY items? | Sensemaking SP3 status-grid + adversarial-focus directive |
| **D6** | Decision-rigor preservation | HIGH | Do the 5 decisions preserve sensemaking adjudication without weakening it? Are legitimate-counter concerns (less-portable, typography-meaning-loss) explicitly surfaced? | Sensemaking Ambiguity 3 + 4 |
| **D7** | Inversion legitimacy (anti-strawman) | MEDIUM | Are Piece-Level Inversions real alternatives or strawman rejections? | Innovation Piece-Level Inversion Rule |
| **D8** | Assembly coherence | HIGH | Do the 9 pieces compose into a unified finding without contradiction or gap? | Decomposition self-eval + Critique Phase 3.5 |
| **D9** | User-question fidelity (external-anchor) | **CRITICAL** | Does the finding answer the user's literal question "what intake handling concepts do we need to figure out?" — and serve the painpoint? | `_branch.md` Source Input |

**4 CRITICAL · 4 HIGH · 1 MEDIUM.**

### Frame-premise test (per refinement note)

Inherited-frame load-bearing premises (if wrong, candidate-space invalidates):

1. **Premise P-α:** Pandoc-md-superset COVERS the primitives needed (footnotes, tables, definition-lists, citations, frontmatter) → if wrong, Decision 1 falls.
2. **Premise P-β:** The 7 schema policies operate on elements intake CAN perceive (heuristically) → if wrong, Decision 4 falls.
3. **Premise P-γ:** Tree-of-containers + cross-ref-flat IS coherent as `IntakeDoc` shape → if wrong, Decision 3 falls.

What-if-wrong prosecutions:

- **P-α wrong:** if Pandoc lacks footnotes natively → revert to vanilla CommonMark + custom syntax extension → reverts to Sensemaking Ambiguity 3's foreclosed paths. Testing: D3 verifies Pandoc-extension claims.
- **P-β wrong:** if marginalia / poetry / honorifics aren't heuristically detectable → the 7 detectors fail → policy values become vacuous. Testing: D4 verifies detector realism.
- **P-γ wrong:** if MarkerRun + cross-ref doesn't actually map inline content → IntakeDoc shape needs revision. Testing: pseudocode review under D8.

Each load-bearing premise has a corresponding dimension in the list.

### Substance-vs-Label criteria

D1 (anti-hallucination), D2 (schema fidelity), D3 (Pandoc-fact accuracy), D4 (detector fidelity) each require **substance-level** criteria (not just label):

- D1: probe per-concept citation existence + grounding-source category.
- D2: probe verbatim class-name match against `schemas.py`.
- D3: probe extension names against Pandoc's actual extension set.
- D4: probe per-detector signal realism via construction (could the signal be implemented?).

### External-anchor dimension requirement

D2 (schema), D3 (Pandoc), D9 (user input) each carry external-anchor evidence demands.

---

## Phase 1 — Landscape Construction

| Region | Criteria | Population |
|---|---|---|
| **Viable** | Passes all 4 CRITICAL dimensions + passes ≥3 of 4 HIGH dimensions | Target zone |
| **Boundary** | Passes all CRITICAL + has structural issues on HIGH (detector over-claim; engineering hidden-dependency; decision-rigor weakening) | REFINE-direction zone |
| **Dead** | Fails any CRITICAL (unflagged hallucination; schema misname; Pandoc-fact error; user question unanswered) | Target zone for KILL |
| **Unexplored** | n/a — Decomposition's Completeness check covered the inquiry's whole | Empty |

---

## Phase 2 — Adversarial Evaluation

### P1 — Executive Summary

**Prosecution:**
- Claim count: "9 DECIDE-NOW" — is the count accurate? Verify: P3 has 5 load-bearing decisions; P4-P7 has DECIDE-NOW tags on A1, A2, B1, B2, C2, D1, D5, D8 = 8 layer items + the 7-policy-split principle (named separately under Decision 4) = 9 total. ✓
- Claim "9 / 18 / 11 / 1" — sums to 39, but the finding claims 38 concepts. **Inspect:** 8 + 12 + 10 + 8 = 38 layer concepts; the "9 DECIDE-NOW" includes the 7-policy-split principle which is NOT a layer concept. So 8 DECIDE-NOW layer concepts + 18 DESIGN + 11 ENGINEER + 1 DEFER = 38. The "9th" DECIDE-NOW is the principle (Decision 4), counted separately. **Minor presentation ambiguity** — could read as "9 of 38" when it's "8 of 38 + 1 principle." Note for assembly.

**Defense:** P1 is one paragraph; reader-facing summary; numbers cohere with substance.

**Collision verdict:** **SURVIVE** (boundary-adjacent; minor counting precision note for assembly).

**Constructive note:** when assembling finding.md, write P1 as "8 concepts decided now + 1 architectural principle (the 7-policy-split)" to disambiguate.

---

### P2 — Methodology / Pruning Rationale / Status-Tag Legend

**Prosecution:**
- Four-source taxonomy (schema / Pandoc-fact / sensemaking-anchor / extrapolation-flag): is it COMPLETE? Counter: misses one common source — user input verbatim (the _branch.md Source Input). The finding cites user input under "sensemaking-anchor" implicitly, but doesn't name it as a fifth source. **MINOR — not load-bearing for D1 since the four named sources cover sensemaking-anchor which itself respects user input.**
- Pruning attribution math: ~15 + ~18 + ~12 + ~12 + ~15 = 72. ✓
- Status-tag legend operational. ✓
- Inversion-candidate (raw-list-without-grounding): rejected with painpoint-grounded reasoning — legitimate alternative tested.

**Defense:** The methodology IS the audit-trail backbone of the finding; without it, anti-hallucination claims have nowhere to point. Lesson-vocabulary (the 4-tag legend) is reused across P4-P7.

**Collision verdict:** **SURVIVE**.

---

### P3 — The 5 Load-Bearing Decisions (META-DECISION)

**Prosecution (per decision):**

- **Decision 1 (Pandoc-md-superset):**
  - Pandoc extension claims (footnotes / pipe_tables / definition_lists / citations / yaml_metadata_block / raw_attribute) — verified per Pandoc's extension list (`pandoc.org/MANUAL.html#extensions`). All 6 named extensions are Pandoc-native. ✓ **D3 PASS.**
  - **Legitimate concern check (D6):** sensemaking Ambiguity 3 named "less portable than vanilla md" as the COUNTER against Pandoc-md-superset. Does Decision 1's text in Innovation surface this? Reading the text: foreclosed-list mentions "vanilla CommonMark as canonical (lacks needed primitives)" but does NOT surface the inverse concern that Pandoc-md-superset is less portable than vanilla. **WEAKENS the sensemaking adjudication** by suppressing the legitimate concern. **REFINE-direction signal.**
  - Revisitability flag MEDIUM — consistent with sensemaking.

- **Decision 2 (structure-preservation):**
  - **Legitimate concern check (D6):** sensemaking Ambiguity 4 named "preserves italic/bold/font choices that may carry meaning" as the COUNTER against the chosen target. Decision 2 in Innovation says "raw typography (font face / size / color choice) is rendering decoration, not structural meaning" but does NOT acknowledge that font choice CAN sometimes carry meaning (e.g., a chapter's font signals a genre shift; calligraphic display in Arabic religious texts is meaning-bearing). **WEAKENS the sensemaking adjudication** by suppressing the legitimate concern. **REFINE-direction signal.**
  - Emphasis-as-semantic-primitive is the correct compromise — Innovation preserves italic/bold semantics. ✓

- **Decision 3 (IntakeDoc shape):**
  - Pseudocode review: `Paragraph: { runs: [TextRun | MarkerRun] }` with `MarkerRun: { type, ref-id → root collection }`. **Coherence check:** Markers are inline within runs (alongside TextRun); each marker references a root-level apparatus collection by id. This DOES map inline content correctly — a paragraph reads as a sequence of (text-runs interspersed with markers), where markers point to apparatus. ✓ **D8 PASS.**
  - `apparatus` dict-by-id structure is sound; `honorifics: Dict[id, HonorificMarkNode]` plus `archaic_register_marks: Dict[id, RegisterNode]` are listed. ✓

- **Decision 4 (7-policy split):**
  - 7 policy class names verification against `schemas.py`: NonMainLangPartsPolicy / SourceApparatusPolicy / VoiceMarkingPolicy / ArchaicRegisterPolicy / HonorificsPolicy / FormulaicOpeningPolicy / EmbeddedPoetryPolicy. All match the schema verbatim. ✓ **D2 PASS.**
  - Perception/rendering split: structurally defensible — the policy VALUE lives in TranslationConfig (translate-time), the TARGET ELEMENT lives in IntakeDoc (intake-time). Innovation's articulation does not conflate; the table explicitly separates perception column from rendering column. ✓
  - Schema not redefined — verified. Innovation adds an architectural EXTENSION (the split) without changing the schema's class structure or Literal values. ✓

- **Decision 5 (Pandoc-as-lever + OCR sub-pipeline):**
  - Tesseract + OCRmyPDF claim: "OCRmyPDF wraps Tesseract producing text-layer-PDF." Verified per OCRmyPDF documentation (ocrmypdf.readthedocs.io): "OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched. Uses Tesseract as the OCR engine." ✓ **D3 PASS.**
  - Pandoc covers 6 of 7 accepted formats. ✓

**Piece-Level Inversion (Innovation's per-decision inversions):**
- Each per-decision inverse was rejected with sensemaking-cited evidence. **Anti-circular check:** is "sensemaking already adjudicated" circular reasoning? **No** — sensemaking's Phase 3 ran independent structural Strongest-Counter tests with HIGH-confidence resolutions; Innovation's inversion-rejection CITES the prior work rather than re-doing it. Acceptable inheritance, not circular. **D7 PASS.**

**Defense:** The 5 decisions cohere as one architectural commitment; each foreclosure named; each revisitability flagged. The decisions are the load-bearing scaffold of the finding.

**Collision verdict:** **REFINE** — survive with mandatory adjustment on D6 for Decision 1 and Decision 2 (surface legitimate-counter concerns explicitly in the decision text).

**Constructive output (REFINE-direction):**

For Decision 1 (Pandoc-md-superset), add to decision text:
> *Legitimate concern preserved:* Pandoc-md-superset is less portable than vanilla CommonMark — readers/tools that only support CommonMark cannot render its extensions. Accepted because the chosen canonical is INTERNAL (intake-time only); user-provided documents can still be vanilla md, and the conversion to Pandoc-md-superset happens at intake time.

For Decision 2 (structure-preservation), add to decision text:
> *Legitimate concern preserved:* Typography can sometimes carry meaning (e.g., a chapter's font signals a genre shift; calligraphic display in Arabic religious texts can be meaning-bearing). Structure-preservation drops these signals. Accepted because (a) these cases are rare in prose-shaped texts, (b) the user can flag specific texts as typography-sensitive via an override DESIGN-NEXT-INQUIRY at D6 (paratext handling), and (c) preserving raw typography for the common case forces every IntakeDoc to carry rendering state translation cannot use.

---

### P4 — Layer A: Format-Layer Concepts (8)

**Prosecution:**
- A1: cites Decision 1 + Pandoc-fact. ✓
- A2: cites Decision 5 + Pandoc-fact. ✓
- A3: OCR sub-pipeline — DESIGN-NEXT-INQUIRY with frontier-pointer F6. ✓
- A4: Pandoc flag set named (`--from=docx`, `--standalone`, `--wrap=none`, `--extract-media=<dir>`). Verified per `man pandoc` — all flags are real. ✓ **D3 PASS.**
- A5: format detection (libmagic). Flagged as standard practice + extrapolation. ✓
- A6: mixed-script + RTL handling — cites NonMainLangPartsPolicy + sensemaking KI2 substrate. ✓
- A7: Pandoc AST mapping. AST node names cited (`Header`, `Para`, `Note`, `Span`, `Div`). Verified per Pandoc's Haskell-types documentation: these are real Pandoc AST node constructors. ✓ **D3 PASS.**
- A8: format-fidelity gradient — DEFER. ✓

**Defense:** Each of the 8 concepts is grounded with a citable anchor; status tags consistent; downstream-pointers explicit.

**Collision verdict:** **SURVIVE**.

---

### P5 — Layer B: Structure-Layer Concepts (12 incl. 7-detector sub-cluster)

**Prosecution (per detector for D4 detector-fidelity):**

- **B4 NonMainLangPartsPolicy detector** — signals (script change via Unicode property + `langid.py` / `cld3` per-segment langid + source markup `lang=` attributes). Realistic; well-supported in NLP toolchains. ✓ **D4 PASS.**

- **B5 SourceApparatusPolicy detector (marginalia)** — signals (Pandoc notes + docx margin-comments + EPUB asides + custom div). **Caveat:** for STRUCTURED sources (docx / EPUB / md with custom divs), detection is straightforward; for PDF where marginalia is purely visual (positioned in page margins), detection requires layout analysis NOT yet specified in the detector. **REFINE-direction signal** — Innovation should acknowledge that PDF marginalia detection requires layout-analysis stage in OCR sub-pipeline OR depth-1 visual analysis.

- **B6 VoiceMarkingPolicy detector** — signals (quotation marks + blockquote + explicit-attribution patterns + "structural shift in tense/register"). Detection via quotation/blockquote is realistic; "shift in tense/register" is genuinely hard for languages without rich inflection AND in mixed-register prose. **Minor over-claim but acceptable for v0.2** — the heuristic signals (marks + attribution) are realistic; the tense/register shift is a refinement, not the primary signal.

- **B7 ArchaicRegisterPolicy detector** — signals (lexical: archaic vocabulary lists per source-language; syntactic: verb-conjugation patterns; explicit `<sic>` markup). Adversarial-focus directive flagged this as "genuinely hard." **Counter-test:** the detector is HONEST that it needs language-specific resources (vocabulary lists, conjugation patterns); it doesn't claim universal applicability. For Risale-i Nur calibration (Ottoman Turkish), documented archaic vocabulary exists. **Acceptable — not over-claiming.** D4 PASS with explicit per-language-resource caveat.

- **B8 HonorificsPolicy detector** — signals (suffix patterns after personal names per tradition + named-entity adjacency). Per-tradition tagging is honest. Realistic for traditions with explicit markers (Islamic SAW/AS/RA; academic PhD/Esq.; military rank). For traditions WITHOUT explicit markers (purely contextual honorifics), recall is limited. **Acceptable for v0.2 with calibration-corpus framing.**

- **B9 FormulaicOpeningPolicy detector** — signals (section-opening templates per tradition + position: section-start). Adversarial-focus flagged "templates vary widely." **Counter-test:** the detector's "per tradition" qualifier acknowledges variance; position-at-section-start is reliable structural signal. For Risale-i Nur (Bismillah pattern at risalah/section opening), detection is well-defined. **Acceptable for v0.2 calibration scope.**

- **B10 EmbeddedPoetryPolicy detector** — signals (verse-shaped formatting + meter signals per-language + attribution). Adversarial-focus flagged "meter detection per-language is hard." **Counter-test:** verse-shape (line breaks + indentation differences) is the PRIMARY signal; meter is a refinement. The detector doesn't claim meter detection as the primary mechanism. **Acceptable — verse-shape catches the typical case.**

**Schema citation check (D2):**
- B4-B10 each cite `schemas.py:18-122` for grounding. Verified: 7 policy classes are defined between lines 18 (NonMainLangPartsPolicy starts at line 18) and ~122 (EmbeddedPoetryPolicy ends ~line 122). Line-range citation is structurally accurate. ✓

**Other concepts in Layer B:**
- B1 (structure-vs-style axiom) — DECIDE-NOW. ✓
- B2 (hierarchical containment) — DECIDE-NOW. ✓
- B3 (footnotes) — ENGINEER. ✓
- B11 (frontmatter/backmatter/TOC) — ENGINEER + extrapolation-flag. ✓
- B12 (emphasis as primitive) — ENGINEER. ✓

**Defense:** Each detector has uniform shape (policy + signals + IntakeDoc representation); per-detector honesty about per-language-resource needs.

**Collision verdict:** **REFINE** — survive with mandatory adjustment on B5 (PDF marginalia detection requires layout-analysis acknowledgment).

**Constructive output (REFINE-direction):**
For B5, add caveat:
> *Format-dependent detection:* For structured sources (docx margin-comments, EPUB asides, md custom-divs), marginalia detection is straightforward via the listed signals. For PDF sources where marginalia is positioned purely visually (no markup), detection requires layout-analysis as a depth-1 sub-pipeline (column-detection + adjacent-block proximity + author-voice heuristic). This is part of the A3 OCR-and-layout-analysis design inquiry.

---

### P6 — Layer C: Pipeline-Layer Concepts (10)

**Prosecution:**
- Stage ordering parse → normalize → segment → validate → hand-off — coherent. ✓
- **C3 prosecution:** C3 is tagged ENGINEER but says "per-format Pandoc invocation per A4" — A4 is DESIGN-NEXT-INQUIRY. **Counter-test:** Can C3 proceed when A4 is downstream? **Yes** — C3 IS implementable with default Pandoc settings (just `pandoc --from=auto --to=markdown --standalone` works for most cases). The A4 design inquiry refines the per-format optimization; the engineering stage can ship with defaults and iterate. **Acceptable — A4 dependency is a refinement, not a blocker.** D5 PASS.
- C1 (IntakeDoc schema design) — DESIGN-NEXT-INQUIRY. ✓
- C5 (segment) — cites A7 (ENGINEER). ✓
- C9 (metadata + langid + encoding) — cites `chardet` / `cchardet`. ✓ (both are real Python packages for encoding detection)
- C10 (multi-file project intake) — DESIGN-NEXT-INQUIRY. ✓

**Defense:** Pipeline stages are ordered, anchored, and the engineering-actionability concern (C3 depending on A4) resolves with defaults-first iteration.

**Collision verdict:** **SURVIVE**.

---

### P7 — Layer D: Quality-Layer Concepts (8)

**Prosecution:**
- D1 quality target — cites Decision 2. ✓
- D2 fidelity/lossiness — DESIGN-NEXT-INQUIRY. ✓
- D3 metrics — DESIGN-NEXT-INQUIRY. Extrapolation flagged. ✓
- D4 quality gates — DESIGN-NEXT-INQUIRY. ✓
- D5 intake-edit-after-parse — DECIDE-NOW + cites Decision 1 + sensemaking FP4. ✓
- D6 paratext default = drop; override = DESIGN-NEXT-INQUIRY. ✓
- D7 error attribution — ENGINEER. ✓
- D8 source-of-truth — DECIDE-NOW + cites SP2 + FP4. ✓

**Defense:** Quality framing is operational; D5 + D8 lock the workflow; D2-D4 explicitly downstream.

**Collision verdict:** **SURVIVE**.

---

### P8 — Inherited Commitments Re-test (META-DECISION)

**Prosecution:**
- articulate_simple's 5 variants — verdicts per variant cite sensemaking Ambiguity 1 + 2 + SV6. Per-variant verdict is grounded in specific sensemaking phases. ✓ Not summary-without-evidence.
- surfacing's 110→38 — pruning attribution math: 15 + 18 + 12 + 12 + 15 = 72. ✓
- schema's 7 policies — verdict "RESPECTED + EXTENDED" — does "EXTENDED" actually preserve "RESPECTED"? **Counter-test:** the perception/rendering split EXTENDS the architectural reading of the policies; the schema class definitions remain unchanged (no fields added/removed/renamed; no Literal values added/removed). The split is architectural-extension, not schema-modification. ✓ "RESPECTED + EXTENDED" is structurally accurate.
- Mac-app substrate — "OUT-OF-FRAME" + Frontier F4 carry-forward. ✓

**Piece-Level Inversion (Innovation's "reject-all-inheritances"):**
- Reject-schema inverse: structurally forbidden by MQ4. ✓ Real constraint.
- Reject-articulate_simple inverse: destroys framing baseline. ✓ Legitimate structural cost.
- Reject-MQ4 (Mac-app re-entry) inverse: violates user's "stop dealing with appification" — structurally legitimate counter.
- **D7 PASS:** real alternatives surfaced and rejected on structural grounds (MQ4 hard constraint; baseline-destruction cost).

**Defense:** Re-test is grounded, not summary; each inheritance has a cited evidence pointer; inversion testing legitimate.

**Collision verdict:** **SURVIVE**.

---

### P9 — Frontier + Next Actions + Open Questions

**Prosecution:**
- All 6 F-flags (F1-F6) addressed with status (RESOLVED / ESCALATED / DEFERRED). ✓
- Next actions: priority order + sizing estimates ("~1-2 weeks", "~1 week each"). **Sizing-estimate prosecution:** the time estimates are EXTRAPOLATION — they are NOT flagged with `[extrapolation: ...]`. **MINOR — unflagged extrapolation.** REFINE-direction.
- Open questions: explicit; tied to downstream design inquiries.

**Defense:** F-flag resolution table covers the surfacing-emitted flags exhaustively; next-action priority is reasoned (IntakeDoc schema before detectors before integration test).

**Collision verdict:** **SURVIVE with minor refine** — flag the time estimates as `[extrapolation: developer-time estimate; calibration-dependent]`.

**Constructive output (REFINE-direction):**
For each time estimate, append `[extrapolation: <reason>]` to honor the four-source taxonomy.

---

### Methodology-Mode Override (Phase 1 Seed)

The Contrarian-rethink alternative was overridden with: *"Sensemaking's Phase 3 already ran Strongest-Counter tests on each of the 5 decisions with HIGH-confidence resolutions; Contrarian-rethink at Innovation would duplicate the adjudication without new evidence."*

**Compliance criterion check (override must be structural + contextual):**
- Structural reason: "Sensemaking's Phase 3 ran Strongest-Counter tests" — names the specific structural property (the test type). ✓
- Contextual reason: "Phase 3 ... HIGH-confidence resolutions" — references specific upstream work (sensemaking Phase 3 + HIGH confidence). ✓
- Per-piece Inversion alternative path explicitly named ("provides contrarian surface at appropriate granularity"). ✓

**Verdict:** Override compliance SATISFIED. Methodology-mode decision (Standard default) is legitimate.

---

## Phase 3 — Verdict Summary

| Candidate | Verdict | Required adjustment |
|---|---|---|
| P1 | SURVIVE | Minor counting precision note for assembly (8 layer DECIDE-NOW + 1 principle) |
| P2 | SURVIVE | — |
| **P3** | **REFINE** | Surface legitimate concerns: "Pandoc-md-superset is less portable than vanilla" in Decision 1; "typography can sometimes carry meaning" in Decision 2 |
| P4 | SURVIVE | — |
| **P5** | **REFINE** | B5 detector: add format-dependent caveat (PDF marginalia needs layout-analysis depth-1 sub-pipeline) |
| P6 | SURVIVE | — |
| P7 | SURVIVE | — |
| P8 | SURVIVE | — |
| **P9** | **SURVIVE-minor-refine** | Flag time-estimates with `[extrapolation: developer-time estimate]` |
| Inversion-candidates (P2, P3, P8) | All REJECTED legitimately | — (not selected; not strawman) |

**3 REFINE / 5 SURVIVE / 1 SURVIVE-minor-refine.** No KILLs.

---

## Phase 3.5 — Assembly Check

**Question:** Do the 9 pieces compose into a coherent finding?

**Yes.** Reading order P1 → P2 → P3 → P4 → P5 → P6 → P7 → P8 → P9 produces a unified document:

1. **P1 (Exec summary)** answers the user's at-a-glance question.
2. **P2 (Methodology)** explains the four-source grounding + the status-tag legend.
3. **P3 (5 decisions)** commits the architecture.
4. **P4-P7 (4 layers)** enumerate the 38 concepts populated against the 4 decisions.
5. **P8 (Re-test)** documents inheritance traceability.
6. **P9 (Frontier)** routes onward work.

**Emergent assembly value:** the combination produces simultaneously (a) actionable list (P3 + P4-P7), (b) auditable provenance (P2 + P8), (c) forward routing (P9), (d) digest (P1). The whole exceeds the sum.

**Contradictions / gaps check:** None detected. Decision 4 in P3 establishes the 7-policy split; B4-B10 in P5 instantiate it; P8 re-tests it against the schema. Internal consistency maintained.

**Verdict on assembly:** **VIABLE — proceed to finding.md construction.**

---

## Phase 4 — Coverage + Convergence Assessment

### Coverage

- **Per-candidate coverage:** 12 candidates evaluated (9 principal + 3 inversion); all 9 critical-or-high dimensions applied per candidate. **Full coverage achieved.**
- **Per-solution-space coverage:** the 9 pieces span the inquiry per Decomposition's Completeness check. No unexplored regions.

### Convergence

- At least one clean SURVIVE: yes — 5 SURVIVE + 1 SURVIVE-minor-refine.
- 3 REFINE-direction signals attached to specific pieces (P3 Decision 1, P3 Decision 2, P5 B5, P9 time estimates).
- Landscape stability: STABLE — no new candidates emerged from this critique pass.
- New-information rate: low (the critique surfaced REFINE-direction adjustments, not new candidates).

### External-anchor evidence check (Mechanism-Independence Quarantine)

The surviving candidates' evidence:
- D2 schema fidelity: verified verbatim against `SKILL/references/config/schemas.py` (7 policy classes; lines 18-122). ✓ External anchor.
- D3 Pandoc-fact accuracy: verified against Pandoc's documented extension list + AST node types. ✓ External anchor.
- D9 user-question fidelity: verified against `_branch.md` Source Input verbatim. ✓ External anchor.

**Mechanism-Independence:** **VALIDATED**. Convergence does NOT rest on structural-argument agreement alone; external anchors (schema source text, Pandoc reference, user input) ground the survivors.

### Failure-mode self-scan

| # | Mode | Observed? |
|---|---|---|
| 1 | Wrong Dimensions | No — dimensions extracted from sensemaking + adversarial-focus directive |
| 2 | Rubber-Stamping | No — 3 REFINE verdicts surfaced legitimate weaknesses |
| 3 | Nitpicking | No — REFINE adjustments are load-bearing (Decision 1/2 concerns; B5 detector caveat); no minor-issue KILLs |
| 4 | Dimension Blindness | No — 9 dimensions span content + project-specific risk + external-anchor axes |
| 5 | False Convergence | No — clean SURVIVE with mechanism-independence VALIDATED |
| 6 | Evaluation Drift | No (single-iteration critique; no cross-iteration drift surface) |
| 7 | Self-Reference Collapse | No — critique evaluates Innovation output; not self-evaluating |
| 8 | Axis Absence at Failure Plane | No — frame-premise test fired; substance criteria probed at D2/D3/D4 |
| 9 | External-Grounding Absence | No — D2/D3/D9 demanded + verified external anchors |

### Convergence Telemetry

- **Dimension coverage:** 9 / 9 (4 CRITICAL + 4 HIGH + 1 MEDIUM)
- **Adversarial strength:** **STRONG** — prosecution constructed at multiple depths (per-piece + frame-premise + detector fidelity + engineering actionability + decision-rigor + Pandoc-fact verification)
- **Landscape stability:** **STABLE** — no new candidates emerged
- **Clean SURVIVE exists:** YES (multiple)
- **Failure modes observed:** NONE
- **Mechanism-Independence:** VALIDATED (external anchors cited for D2/D3/D9)

### Signal

**TERMINATE** with ranked survivors + 3 REFINE-direction adjustments to apply at finding.md assembly time.

**Ranked survivors:**

1. P3 (5 decisions) — load-bearing scaffold; REFINE per D6 (surface legitimate concerns explicitly)
2. P4 + P5 + P6 + P7 (4 layer lists) — substantive concept enumeration; P5 REFINE per D4 (B5 caveat)
3. P2 (methodology) — audit-trail backbone
4. P8 (re-test) — inheritance traceability
5. P9 (frontier) — onward routing; minor REFINE (time-estimate extrapolation flag)
6. P1 (exec summary) — digest; minor presentation note

**Final verdict:** **PROCEED to Routelister.** The Innovation output is viable for finding.md construction with the 3 REFINE-direction adjustments applied. No KILLs; no new candidates needed.

---

## Summary for Finding.md Construction

When assembling the finding (post-CONCLUDE), apply these adjustments:

1. **In P3 Decision 1's text:** add a paragraph surfacing "Pandoc-md-superset is less portable than vanilla CommonMark" as a legitimate concern that the choice nevertheless overrides (because canonical is INTERNAL).

2. **In P3 Decision 2's text:** add a paragraph surfacing "typography can sometimes carry meaning" as a legitimate concern that the choice nevertheless overrides (because override exists at D6 paratext + the painpoint demands structure-first).

3. **In P5 B5 detector:** add a format-dependent caveat — PDF marginalia detection requires layout-analysis as a depth-1 sub-pipeline (part of A3).

4. **In P9 time estimates:** flag each estimate with `[extrapolation: developer-time estimate; calibration-dependent]`.

5. **In P1 exec summary:** disambiguate "9 DECIDE-NOW" as "8 layer concepts decided now + 1 architectural principle (the 7-policy split)."

All adjustments are surgical content additions to the Innovation principal candidates; no structural rework needed.
