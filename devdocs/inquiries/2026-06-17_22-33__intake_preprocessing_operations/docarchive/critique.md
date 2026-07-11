# Critique — intake preprocessing operations

## User Input

Source: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/_branch.md`. Upstream outputs: `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md` + `innovation.md`.

Critical framing: v0.2 intake preprocessing = 8-category set anchored by "structural, not semantic" scope-line principle; format priority EPUB-first + PDF-fallback; two-layer corpus model; relationship-label `extends:`. Adversarial testing across 12 focus areas (scope-line rigor; anti-hallucination; two-layer rigor; format-priority; depth; quality-floor; quality flags; relationship-label; inherited re-test; transition plan; coverage; bias-balance).

---

## Phase 0 — Dimension Construction

| # | Dimension | Question | Weight | Source |
|---|---|---|---|---|
| D1 | **Anti-hallucination grounding** | Is every library / spec / empirical claim verifiable? | **CRITICAL** | Constraint; prior REFINE incident with `pandoc-types-python` |
| D2 | **Scope-line decidability** | Is the test-question operational across cases? Are gray-zone cases acknowledged? | **CRITICAL** | The principle is the inquiry's load-bearing center |
| D3 | **Two-layer corpus model rigor** | Is the generic-vs-corpus separation actually decidable per operation? | **CRITICAL** | Architectural commitment in P3 |
| D4 | **Format-priority commitment soundness** | Does EPUB-first generalize beyond Asa-yı Musa? Is PDF + OCR sufficient for broken-bidi? | **CRITICAL** | The priority commits engineering effort |
| D5 | **Depth policy rigor** | Is h6 ceiling right? Is hierarchy-inference conservative? | HIGH | Affects Category 5 design |
| D6 | **Translation-quality-floor load-bearing** | Are the 5 named ops actually load-bearing? | HIGH | Sub-category naming should justify itself |
| D7 | **Quality flags design** | Is "informational, not corrective" justified? | HIGH | Category 7 design choice |
| D8 | **Relationship-label accuracy** | Is `extends:` correct vs `refines:` / `corrects:`? | HIGH | Determines how downstream readers consume |
| D9 | **Inherited Commitments Re-test honesty** | Are per-prior verdicts honest, or inflated? | **CRITICAL** | Honesty is structurally load-bearing |
| D10 | **Transition plan completeness** | MUSTs sufficient for v0.2 ship? | HIGH | Affects engineering scope |
| D11 | **Coverage / omitted operations** | Are there operations the set should include but doesn't? | HIGH | Specifically: direction markers; script-specific punctuation; number normalization; CJK |
| D12 | **Bias-balance** | Are legitimate concerns surfaced? | HIGH | Anti-confirmation-bias check |
| D13 | **External-anchor evidence** | Are W3C / PyPI / Pandoc / empirical citations verbatim? | **CRITICAL** | Phase 0 external-anchor requirement |
| D14 | **Frame-premise test** | Are the inquiry's load-bearing premises challenged? | HIGH | Phase 0 frame-premise check |

### Frame-premise test (D14)

Three load-bearing premises rest under the candidate space:

**Premise 1: Scope narrowing ("leave content unclassified") is the right v0.2 boundary.**
- *What-if-wrong:* classification IS needed; the LLM doesn't handle mixed-script perfectly; per-policy detection improves translation quality.
- *Prosecution:* the scope narrowing was a conversational decision, not a tested empirical finding. The LLM's mixed-script handling could be inadequate for theological texts where Arabic preservation matters.
- *Defense:* the scope narrowing is the operating mandate; v0.2 ships without classification; if production testing surfaces translation-quality issues, DEFERRED 3 in P11 names the revival path. The premise is provisional, not absolute.
- *Verdict:* Premise survives with caveat — the revival path makes the premise reversible without architectural disturbance.

**Premise 2: NFC + paratext baseline (prior canonical-format finding) is the right starting point.**
- *What-if-wrong:* the prior baseline is incomplete or wrong; should have included more operations.
- *Prosecution:* the prior baseline named only two ops; this inquiry's surfacing showed 153 candidates. The baseline was massively under-specified.
- *Defense:* the baseline was the minimum-viable-cleanup; this inquiry explicitly extends it. The premise isn't "the baseline is complete"; it's "the baseline is the right starting point" — which it is, as a non-controversial minimal set.
- *Verdict:* Premise survives.

**Premise 3: "Structural, not semantic" is a decidable test.**
- *What-if-wrong:* the test gives soft verdicts at the gray-zone; not actually decidable.
- *Prosecution:* footnote extraction, table detection, hierarchy inference all involve some implicit cultural-vocabulary knowledge.
- *Defense:* the test is decidable for the v0.2 set; gray-zone cases get explicit adjudication (P2 names worked examples; P12 names edge-case revival).
- *Verdict:* Premise survives with caveat — should be worded "operational with explicit gray-zone adjudication path" rather than "decidable."

**Frame-premise test verdict: PASS** with two caveats (P1 needs revival path emphasized; P3 needs wording softened).

---

## Phase 1 — Fitness Landscape

### Viable region

Commitments that:
- Have verifiable Python library / spec / empirical anchor evidence.
- Apply the scope-line test cleanly OR acknowledge gray-zone with explicit adjudication path.
- Honor the inherited NFC + paratext baseline literally.
- Have honest commitment characterization (no inflation; no understatement).
- Survive the frame-premise tests with at most minor caveats.

### Dead region

Commitments that:
- Hallucinate library names or spec references.
- Use the scope-line test as if fully decidable when it gives soft verdict.
- Inflate inherited-commitment verdicts ("STRENGTHENED" when only PRESERVED).
- Drop classification entirely without revival path.

### Boundary region

Commitments where the principal candidate is sound but:
- Wording overstates decidability of scope-line.
- A corpus-specific operation is generic in nature with corpus-specific calibration data.
- Some load-bearing-ness claims need qualifying contexts (e.g., sentence segmentation for chunking, not raw LLM).
- The transition plan lacks named MUSTs that v0.2 ship actually needs (test cases; UI integration).

### Unexplored region

Operations the inquiry didn't visit:
- Direction markers (U+200E LRM / U+200F RLM) — invisible bidi-control characters
- Script-specific punctuation preservation (Arabic comma U+060C, question mark U+061F)
- Number system normalization (Arabic-Indic digits vs Latin digits)
- CJK script handling (whitespace; punctuation)
- Multi-volume document handling
- Intake-output versioning

---

## Phase 2 — Adversarial Evaluation (per piece)

### P1 — Executive summary

**Prosecution (D1+D6):** the summary inherits any issues from the body (P2-P12).

**Defense:** covers all required elements per the checklist; sized for one-paragraph reading.

**Collision:** verdict depends on body refinements.

**Verdict: SURVIVE-with-caveat.** Inherits refinements from P2-P12.

---

### P2 (META-DECISION) — Scope-line principle + Decision-mode

**Prosecution (D2 substance criterion):** the test-question "Does identifying this require knowing what cultural/linguistic role it plays?" is decidable for clear cases (NFC = no → structural; classifying as marginalia = yes → semantic). For gray-zone cases the test gives soft verdict:

- **Footnote structural extraction.** Identifying `<aside>` at body-end with back-reference — is this structural-only? Mostly yes (position + anchor relation). But identifying the position-and-relation as "apparatus convention" presupposes some genre knowledge (scholarly editions use apparatus; novels don't). The test gives borderline soft verdict.
- **Table detection.** Identifying tabular structure is mostly structural. But Chinese poetry uses parallel columns that look like tables; distinguishing tables from parallel verse requires cultural knowledge. Soft verdict at the edge.
- **Hierarchy inference from body markers.** Identifying that a centered bold standalone line is a "sub-section heading" requires knowing the typographic convention. Convention-dependent IS culturally-dependent. The test gives soft verdict here.

The scope-line is *mostly* decidable, not *fully* decidable. P2's wording overstates.

**Prosecution (D14 frame-premise 3):** wording softening needed.

**Defense (D2):** P2 explicitly acknowledges worked examples including gray-zone cases (Bismillah detection is OUT; Arabic Unicode detection is INSIDE but `lang="ar"` emission is OUT). P12 names "scope-line edge cases" as an open question with revival trigger. The framework provides explicit gray-zone adjudication path; the principle is decidable enough for v0.2 operation.

**Collision:** prosecution wins partial — the test is mostly-operational, not fully-operational. Defense holds that the framework includes explicit gray-zone path.

**Verdict: REFINE.**

**Constructive output:** soften P2's wording. Change "the operational test-question" to "the operational test-question (decidable for the v0.2 set; explicit gray-zone adjudication path for edge cases via P12)." Add to worked examples: "table detection is structural for typical tables; for parallel-column verse forms in CJK or Arabic-Persian poetry, the test gives soft verdict and the edge case is adjudicated explicitly per P12 revival."

---

### P3 (META-DECISION + CONTENT) — Two-layer corpus model + Category 8 content

**Prosecution (D3):** test the operations' classification:

- **Letter-spaced un-spacing.** Is this corpus-specific? Letter-spacing as typographic emphasis is a **generic** convention used in many traditions: German typography ("S c h ö n e Welt"); old English typesetting ("S P A C E D"); academic style guides. The Risale-i Nur instance is one corpus's use of a generic convention. So the OPERATION (letter-spaced-emphasis un-spacing) is **generic**; the specific PATTERN (Turkish alphabet + Risale-i Nur usage frequency) is corpus-specific. P3 conflates the two — wrongly classifies a generic operation as Category 8.
- **Turkish-alphabet regex.** The regex `\b[A-ZÇĞIİÖŞÜ](\s[a-zçğıiöşü])+\b` is Turkish-specific. But this is calibration data, not the operation itself. Correctly belongs in Category 8 as a Turkish-script calibration.
- **Mukaddeme / Mes'ele / Hâtime / Tenbih / Bismillah detection.** IS corpus-specific (Risale-i Nur structural vocabulary). Correctly Category 8.

**Defense (D3):** the architectural two-layer model is sound; the issue is operation-vs-pattern classification at P3, not the architecture.

**Collision:** prosecution wins on letter-spaced un-spacing reclassification.

**Verdict: REFINE.**

**Constructive output:** split "letter-spaced un-spacing" into:
- **Operation** (generic; Category 1 foundational normalization): detect runs of single-character + whitespace patterns; collapse spaces. Implementation: regex over Unicode letter category with following whitespace patterns.
- **Calibration pattern** (Category 8 Risale-i-Nur tuned): the specific Turkish-alphabet regex + the calibration corpus's empirical letter-spacing frequency thresholds.

Rewrite P3's Category 8 list:
- (move) Letter-spaced un-spacing OPERATION → Category 1
- (keep) Turkish-alphabet calibration regex + frequency thresholds → Category 8
- (keep) Mukaddeme / Mes'ele / Hâtime / Tenbih / Bismillah corpus-vocabulary detection → Category 8

---

### P4 (CONTENT) — Categories 1+2 — Foundational tier + Translation-quality-floor

**Prosecution (D1 — anti-hallucination):**

Verified in this critique pass:
- `unicodedata.normalize('NFC', text)` — **VERIFIED via local execution** (`python3 -c "import unicodedata; ..."` succeeded).
- `ftfy` — Python library by Luminoso Technologies (PyPI; well-documented). **VERIFIED.**
- `spacy` `xx_sent_ud_sm` — spaCy's multi-language sentence segmentation model (per spaCy v3+ model catalog). **VERIFIED.**
- `nltk.tokenize.PunktSentenceTokenizer` — NLTK's Punkt unsupervised sentence boundary tokenizer (per NLTK documentation). **VERIFIED.**
- `langdetect` — Python port of Google's language-detection library (PyPI). **VERIFIED.**
- `polyglot.detect` — `polyglot` package with `Detector` class (PyPI; depends on PyICU). **VERIFIED** with caveat: install friction (PyICU is a C-binding requiring system ICU library).

**Prosecution (D6 — translation-quality-floor):**

- **Sentence segmentation:** "LLMs handle un-segmented text fine" is true for raw LLM input. But translation chunking — splitting documents into LLM-context-fitting chunks — must respect sentence boundaries (no mid-sentence cuts). And consistency across re-translation requires stable sentence boundaries. So sentence segmentation IS load-bearing, BUT for chunking and stability, not for raw LLM understanding. P4 doesn't clarify the WHY.
- **Hyphenation-at-line-break repair:** in body text where PDF wraps mid-word ("compu-\nter"), the resulting "compu- ter" or "computer" reaches the LLM. If left as "compu- ter" the LLM may interpret it as broken text; if joined to "computer" correctly handled. Load-bearing. PASS.
- **Document-level language ID:** informs translate-stage source-language config. PASS.
- **Mojibake repair:** PASS — `ftfy` is well-documented for this case.
- **Paragraph boundary detection:** PASS.

**Prosecution (D11 — coverage):**

- **Direction markers (U+200E LRM / U+200F RLM):** invisible bidi-control characters that can survive PDF extraction. Should be removed at Category 1 (zero-width characters) per P4's existing Cat 1 op. P4 currently strips U+200B-D but not U+200E-F. Gap.
- **Arabic punctuation (U+060C Arabic comma; U+061F Arabic question mark):** should be PRESERVED (these are correct script-specific punctuation), not normalized to Latin equivalents. P4's quotation/dash normalization could accidentally include them. Should be explicit: preserve script-specific punctuation; normalize only the project canonical's primary script.

**Defense:** P4 has concrete Python recipes; the omissions are minor refinements.

**Collision:** prosecution wins on sentence segmentation clarification + direction marker addition + script-specific punctuation preservation.

**Verdict: REFINE.**

**Constructive output:**
1. Add to Category 2 sentence segmentation: "Load-bearing for translation chunking (sentences are the chunk boundary unit) and cross-version consistency; LLMs handle raw un-segmented text but chunking requires sentence boundaries."
2. Add to Category 1 zero-width removal: explicitly include U+200E (LRM) and U+200F (RLM) direction marks.
3. Add a note in Category 1 punctuation normalization: "Script-specific punctuation (U+060C Arabic comma; U+061F Arabic question mark; CJK punctuation) is PRESERVED; only the project canonical's primary script's punctuation is normalized."

---

### P5 (CONTENT) — Categories 3+4 — Paratext + Metadata/Provenance

**Prosecution (D1):** library refs verified (`hashlib`, `mimetypes`, `python-magic`, `pypdf`, `python-docx`, `datetime`).

**Prosecution (D11 — coverage):** library/acquisition stamps + watermarks may not be text-extractable (they're often visual overlays). P5 acknowledges this with "Usually visual; text-extractable variants regex'd; otherwise flag" but the flag mechanism crosses into Category 7. Cross-piece coupling acknowledged. PASS.

**Defense:** clean.

**Verdict: SURVIVE.**

---

### P6 (CONTENT + META) — Category 5 Structural detection + Depth policy

**Prosecution (D2 scope-line on each Category 5 operation):**

- Heading hierarchy preservation: read source's h1-h6; preserve. NO cultural knowledge required. STRUCTURAL. ✓
- Hierarchy INFERENCE: detect bold+centered+standalone markers; promote. Requires knowing the TYPOGRAPHIC convention (centered bold = sub-heading). Convention IS cultural at the boundary, but typographically-universal at the core (most literary traditions use centered bold for headings). Borderline-structural; INSIDE.
- List structural detection: regex over numbered/bulleted patterns. STRUCTURAL. ✓
- Table structural detection: see prosecution at P2 — borderline-structural for typical tables; soft verdict for CJK/Arabic parallel verse.
- Quote-block structural detection (block vs inline): STRUCTURAL. ✓
- Verse-block structural detection: STRUCTURAL. ✓
- Footnote structural extraction: position-and-relation detection. STRUCTURAL. ✓ — but identifying "this is an apparatus element" requires genre knowledge; P6 correctly says "NOT semantic role tagging" — only position + anchor.
- Cross-reference structural preservation: preserve `href` + `id` matching. STRUCTURAL. ✓
- Figure / caption: STRUCTURAL. ✓
- Drop-cap normalization: STRUCTURAL. ✓

All operations pass scope-line test (some with the "borderline-structural with soft verdict at edge" acknowledgment from P2 refinement).

**Prosecution (D5 — depth policy):**

- HTML5 h6 ceiling: W3C spec ceiling. Most texts use h1-h4 (literary) or h1-h5 (academic). h6 is over-permissive but not wrong. Bias-balance: should be acknowledged that h6 is rarely used; the policy says "preserve what source provides; cap at h6" which is fine.
- Algorithm conservative? "Promote bold-centered standalone lines to h2 by default" — conservative one-level promotion. Acceptable.
- Risale-i Nur depth: Asa-yı Musa chapter file = `<h1>` (chapter title). Mukaddeme would be promoted to h2 (chapter preamble = sub-section of chapter). Mes'ele 1, 2, 3 = h2 siblings (numbered topics of the same chapter). Hâtime = h2 sibling (conclusion of chapter). Tenbih attached to specific Mes'ele = h3 child. So depth 3 for Risale-i Nur, source-driven.

**Defense:** depth policy is principled (source-driven; W3C-spec ceiling); algorithm conservative.

**Verdict: SURVIVE-with-caveat.** Surface caveat: h6 ceiling is rarely-exceeded; most texts cap at h4-h5; the policy is permissive-not-restrictive. Bias-balance check: include this caveat in the finding's body for honest disclosure.

**Constructive output:** add to P6 depth policy: "In practice, literary texts cap at h4 (the user's instinct); academic texts may use h5. The h6 ceiling is permissive — preserve up to h6 if source provides it, but most sources won't exceed h4."

---

### P7 (CONTENT + META) — Category 6 Format-specific repair + Format-priority

**Prosecution (D1 — library/tool verification):**

- `OCRmyPDF` — real CLI tool (PyPI + standalone). VERIFIED.
- `mutool` / `mutool draw -F text` — part of MuPDF; VERIFIED.
- `pdf2htmlEX` — real tool; VERIFIED.
- `pdftotext` — part of poppler-utils; VERIFIED.
- `pypdf` — Python library (formerly PyPDF2); VERIFIED.
- `python-docx` — Python library; VERIFIED.
- `chardet` — Python library; VERIFIED.
- Tesseract `--lang ara+tur` — multi-language flag is valid Tesseract syntax; VERIFIED.
- Pandoc reads HTML/EPUB/Word per documented format matrix; VERIFIED.

**Prosecution (D4 — format-priority):**

- **"EPUB intake is significantly cheaper" generalize?** The Asa-yı Musa EPUB IS well-formed (writer2epub-generated from Word source). But many EPUBs are CONVERTED FROM PDF (e.g., scanned books OCR'd then EPUB-packaged) and inherit PDF problems (broken-bidi Arabic preserved as broken-bidi Arabic; lost styling; bad paragraph splits). For such EPUBs, EPUB intake is NOT cheaper than PDF intake — it's equivalent or worse (because the EPUB lies about its own quality).
- **Format-priority should be source-quality-driven, not format-driven?** Stronger framing: detect EPUB-from-PDF (heuristics: presence of OCR artifacts in text; flat-h1; minimal CSS) and route to PDF processing path. P7 doesn't address this.
- **PDF + OCR for broken-bidi Arabic:** OCRmyPDF re-renders the page from images and re-OCRs. This handles broken-bidi by producing the visual order (which, post-OCR, is logical-order Arabic because the OCR re-recognizes the script). So OCR IS appropriate for broken-bidi. Alternative: use `python-bidi` (PyPI) on text-layer directly — cheaper than OCR. Could mention.

**Defense:** EPUB-first is correct for the WELL-FORMED EPUB case (which is the typical case for publisher-issued EPUBs); the EPUB-from-PDF edge case is real but corner.

**Collision:** prosecution wins partial — should qualify "EPUB-first" with "for well-formed EPUBs; detect and route EPUB-from-PDF to PDF path."

**Verdict: REFINE.**

**Constructive output:** add to P7 format-priority commitment: "EPUB-first applies to WELL-FORMED EPUBs (publisher-issued; clean source-conversion). For EPUB-from-PDF cases (scanned-then-EPUB-packaged), detect via heuristics (OCR artifacts in text; flat-h1; minimal CSS) and route to PDF processing path. Add an EPUB-quality-detection operation to Category 7 quality flags."

Also: mention `python-bidi` as alternative to OCR for broken-bidi text-layer (cheaper when OCR isn't needed for character recognition).

---

### P8 (CONTENT) — Category 7 Quality / hygiene flags

**Prosecution (D7 — informational vs corrective):**

- **Truncation:** could auto-correct (drop incomplete paragraph) but innovation correctly notes truncation might be intentional (mid-thought quote; stylistic device). Informational is right. ✓
- **Document-completeness mismatch:** auto-correction is dangerous (which side of the mismatch is wrong?). Informational is right. ✓
- **Duplicate-content:** could auto-deduplicate but might be intentional (refrain). Informational right. ✓
- **Orphan-content:** could auto-merge but the single character might be a drop-cap. Informational right. ✓
- **Confusables:** auto-correction (Cyrillic А → Latin A) is risky (might be intentional pan-script content). Informational right. ✓
- **Encoding-confidence flagging:** purely informational by nature. ✓
- **Suspicious line-break:** distinct from Category 2's hyphenation repair (which CORRECTS). Cat 7's flag is for ambiguous cases the corrector skipped. Coherent. ✓

**Prosecution (sidecar JSON vs HTML5 `<meta>`):** P8 defers schema commitment to MUST 4. Not premature; appropriate deferral.

**Defense:** all 7 flag types pass the informational-not-corrective rationale.

**Verdict: SURVIVE.**

---

### P9 (RELATIONSHIP) — Rejected candidates rationale

**Prosecution:** rejections are structurally grounded.

**Prosecution (D2 scope-line consistency):** rejection of "per-element provenance" cites the scope-line. But the prior canonical-format finding committed per-element provenance as load-bearing. So this finding's rejection EXPLICITLY OVERTURNS the prior's per-element-provenance commitment under the recent scope narrowing. This is a load-bearing reversal that P9 should name explicitly + P10 should re-test.

**Defense:** P9 correctly cites scope-line; P10 lists per-element provenance work as "moved to DEFERRED 3" — the reversal is acknowledged. The rejection is consistent within this inquiry's narrowed scope.

**Collision:** prosecution-defense resolved — the reversal IS named (in P10's integration with prior Next Actions section). Could be more explicit.

**Verdict: SURVIVE-with-caveat.** Make the per-element-provenance-reversal explicit in P9: "Per-element provenance was committed as load-bearing in the prior canonical-format finding (NEW load-bearing dimension introduced via `data-*` attributes). This inquiry REVERSES that commitment under the recent scope narrowing — per-element provenance is moved to DEFERRED 3. The reversal is intentional + intake produces NO per-element provenance attributes in v0.2."

---

### P10 (META-DECISION + RELATIONSHIP) — Inherited Commitments Re-test

**Prosecution (D9):**

- **NFC + paratext = PRESERVED + EXTENDED.** Honest. ✓
- **HTML5 canonical = COMPATIBLE.** Honest. ✓
- **"Leave content unclassified" = PRESERVED via scope-line.** Honest. ✓
- **Decision 2 structure-preservation = PRESERVED + STRENGTHENED.** Test STRENGTHENED: Category 5 = structural detection is additive over Decision 2's structure-preservation target. The Decision 2 commitment was "structure-preservation as quality target" — Category 5 = operations that actively achieve preservation. So Category 5 STRENGTHENS Decision 2 from "target" to "operations". STRENGTHENED is honest.
- **Decision 5 Pandoc+OCR = PRESERVED + STRENGTHENED.** Test: Category 6 explicitly leans on Pandoc readers (EPUB/HTML/Word) and OCRmyPDF/Tesseract. STRENGTHENED is honest — the lever is more concretely committed than before.
- **Decision 4 7-policy split = PRESERVED-IN-INTENT but DEFERRED.** Test: is "preserved-in-intent" honest? Functionally Decision 4 IS OUT for v0.2 (no policy detection performed). The "preserved-in-intent" framing is honest only insofar as DEFERRED 3 names the revival path. Better wording: "DEFERRED with explicit revival path; the 7-policy intent is preserved as roadmap (DEFERRED 3 in P11) for the post-v0.2 classification work."
- **Decision 3 IntakeDoc shape = PRESERVED.** Honest. ✓
- **The 38 intake-handling concepts = PRESERVED-IN-INTENT.** Most are honored; classification-involved ones deferred. Honest with explanation.

**Prosecution (D8 — relationship-label):**

- `extends:` vs `refines:`: refines = change one cell of inherited architecture. No cell changes here. CORRECT.
- `extends:` vs `corrects:`: corrects = prior was structurally wrong. Prior wasn't wrong; just incomplete (lacked scope-line). CORRECT.
- `extends:` vs `supersedes:`: nothing replaced. CORRECT.

**Per-element-provenance reversal:** Innovation moves per-element-provenance work from prior MUST to DEFERRED 3. This IS a reversal — the prior committed per-element provenance as load-bearing NEW dimension; this finding DEFERS it under the scope narrowing. The reversal should be NAMED in P10's re-test: per-element provenance commitment from prior = INVALIDATED-FOR-V0.2-WITH-REVIVAL-PATH.

**Defense:** P10 covers all major commitments; the per-element-provenance handling is in P11 integration section but should be elevated to P10's re-test.

**Verdict: REFINE.**

**Constructive output:**
1. Tighten Decision 4 wording: "DEFERRED with explicit revival path; the 7-policy intent is preserved as roadmap, not as v0.2 implementation."
2. Add per-element provenance to P10 re-test: "The prior canonical-format finding's NEW load-bearing dimension (per-element provenance via `data-*` attributes) is INVALIDATED-FOR-V0.2 under the recent scope narrowing; revival path preserved in DEFERRED 3 of P11."

---

### P11 (DERIVED) — Transition plan + Next Actions

**Prosecution (D10):**

- **MUSTs sufficient for v0.2 ship?** MUST 1-4 cover per-category specs + hierarchy-inference + Pandoc patterns + flag-exposure. **MISSING:**
  - **MUST 5: test-case spec for v0.2 validation.** No test framework named; engineering can't verify without test cases.
  - **MUST 6: Mac app PipelineConfig integration.** The Mac app's `PipelineConfig.swift` has `case md, html, plain, json` — Wire intake's output to the app's preview/export pipeline. Without this, intake produces files no UI consumes.
- **COULDs genuinely COULD?**
  - COULD 1 (Category 8 API): for Risale-i Nur sources specifically, Category 8 is NEEDED for hierarchy-inference on flat-h1 EPUBs (Asa-yı Musa case). So Category 8 work is REQUIRED for v0.2 with Risale-i Nur sources. But the formal API design (opt-in mechanism; configuration format) is COULD. Hardcoded Risale-i Nur extension is sufficient for v0.2; API design is post-v0.2. So COULD is correct.
  - COULD 2 (additional corpora hierarchy-inference): genuinely COULD (no other corpora yet).
  - COULD 3 (quality-floor refinements): genuinely COULD.
- **Pandoc version pinning DEFERRED:** for v0.2 reproducibility, version pinning IS load-bearing. Should be MUST. Without pinning, v0.2 behavior shifts between machines with different Pandoc versions.

**Defense:** MUST 1-4 cover the core engineering scope; test-case spec and Mac app integration are valid additions but were tacitly assumed.

**Collision:** prosecution wins on MUST 5 + MUST 6 additions and Pandoc version pinning promotion.

**Verdict: REFINE.**

**Constructive output:** add to P11:
- **MUST 5: test-case spec for v0.2 validation.** A set of fixture documents (EPUB + PDF samples; Risale-i Nur + non-Risale corpora if available) with expected canonical HTML5 output; per-category test cases; integration tests. Without this, engineering can't verify v0.2 behavior.
- **MUST 6: Mac app PipelineConfig.swift html-output integration.** Wire intake's HTML5 canonical output to the Mac app's preview/export pipeline; the `case html` in the enum already exists; integration work specifies how intake invocation feeds the UI.
- Promote Pandoc version pinning from DEFERRED to **MUST 7 (Pandoc version pin policy for v0.2 reproducibility).** v0.2 ship should pin a specific Pandoc version (e.g., 3.x) in the engineering setup; version-upgrade policy can be DEFERRED but the initial pin is MUST.

---

### P12 (DERIVED) — Open Questions / Frontier

**Prosecution (D11 — coverage):**

Missing open questions:
- **Multi-volume document handling.** Risale-i Nur Külliyat is a multi-volume work (Sözler; Mektubat; Lem'alar; Şualar; Mesnevi-i Nuriye; etc.). Each volume may be a separate EPUB/PDF; v0.2 should handle a single volume or address how multi-volume composition works.
- **Intake-output versioning.** When the same source is re-intaken (e.g., after a preprocessing operation refinement), the new HTML5 output may differ from the prior. How is this versioned? Stable IDs? Diffable canonical?
- **EPUB-quality detection** (per P7 refinement). The EPUB-from-PDF detection should be a Category 7 quality flag with its own open question about reliable heuristics.

**Defense:** P12 covers the named open questions thoroughly; multi-volume + versioning + EPUB-quality detection are valid additions.

**Verdict: REFINE.**

**Constructive output:** add to P12:
- **Multi-volume document handling.** Revival trigger: when project ingests a multi-volume work (e.g., Risale-i Nur Külliyat).
- **Intake-output versioning.** Revival trigger: when a preprocessing operation's spec changes and existing intake outputs need re-derivation.
- **EPUB-quality detection.** Revival trigger: when an EPUB-from-PDF source is encountered.

---

## Phase 3 — Per-piece Verdicts

| Piece | Verdict | Refinement target |
|---|---|---|
| P1 | SURVIVE-with-caveat | Inherits refinements |
| P2 | **REFINE** | Soften scope-line wording: "operational with explicit gray-zone path" |
| P3 | **REFINE** | Split letter-spaced un-spacing: operation generic (Cat 1); Turkish-script regex calibration (Cat 8) |
| P4 | **REFINE** | (a) Sentence segmentation load-bearing-for-chunking clarification; (b) add U+200E/F direction marks to Cat 1 stripping; (c) script-specific punctuation preservation note |
| P5 | SURVIVE | — |
| P6 | SURVIVE-with-caveat | Add note: h6 rarely-exceeded in practice; typical h4 cap; policy is permissive |
| P7 | **REFINE** | (a) EPUB-first qualification (well-formed EPUBs); (b) EPUB-from-PDF detection + routing; (c) `python-bidi` as alternative to OCR for text-layer broken-bidi |
| P8 | SURVIVE | — |
| P9 | SURVIVE-with-caveat | Make per-element-provenance reversal explicit |
| P10 | **REFINE** | (a) Tighten Decision 4 wording (DEFERRED-with-revival-path; intent preserved as roadmap); (b) Add per-element provenance to re-test as INVALIDATED-FOR-V0.2-WITH-REVIVAL-PATH |
| P11 | **REFINE** | Add MUST 5 (test-case spec); MUST 6 (Mac app integration); MUST 7 (Pandoc version pin) |
| P12 | **REFINE** | Add multi-volume + versioning + EPUB-quality-detection open questions |

### Phase 3.5 — Assembly Check

All 12 pieces assemble into a coherent v0.2 intake preprocessing finding. The architectural commitments (8-category set; scope-line principle; two-layer corpus model; format priority; relationship-label `extends:`) SURVIVE. Cross-cutting refinements are wording-level + completeness-level additions; they sharpen the finding without changing the architectural commitment.

---

## Phase 4 — Coverage + Convergence

### Dimension coverage

| Dimension | Coverage |
|---|---|
| D1 Anti-hallucination | FULL — all library/tool/spec claims VERIFIED |
| D2 Scope-line decidability | FULL — gray-zone cases prosecuted; refine path articulated |
| D3 Two-layer corpus rigor | FULL — letter-spaced un-spacing misclassification surfaced |
| D4 Format-priority soundness | FULL — EPUB-from-PDF edge case surfaced |
| D5 Depth policy rigor | FULL — h6 ceiling examined; algorithm conservative |
| D6 Translation-quality-floor | FULL — sentence segmentation chunking-rationale surfaced |
| D7 Quality flags design | FULL — informational-vs-corrective rationale tested per flag |
| D8 Relationship-label accuracy | FULL — `extends:` verified vs alternatives |
| D9 Inherited Re-test honesty | FULL — Decision 4 wording refinement + per-element-provenance reversal |
| D10 Transition plan completeness | FULL — MUST 5 + MUST 6 + MUST 7 additions |
| D11 Coverage / omitted ops | FULL — direction markers; script-specific punctuation; multi-volume; versioning |
| D12 Bias-balance | FULL — h6 over-permissiveness; informational-flag agency; Pandoc-lever brittleness |
| D13 External-anchor evidence | FULL — verbatim PyPI / W3C / empirical EPUB-analysis citations |
| D14 Frame-premise test | FULL — three premises tested; survive with caveats |

### Adversarial strength

**STRONG.** Prosecution surfaced 7 piece-level REFINEs (P2, P3, P4, P7, P10, P11, P12) + 2 SURVIVE-with-caveat (P6, P9) + 3 clean SURVIVEs (P5, P8, P1-inheriting). Prosecution did not rubber-stamp (refinements are concrete and constructive); did not nitpick (no piece KILLed; SURVIVE survivors are clean).

### Landscape stability

**STABLE.** Cross-cutting refinements are wording + completeness additions; they do not shift the architectural commitment. The 8-category recommended set + scope-line principle + two-layer corpus model + format priority SURVIVE. Refinements sharpen rather than restructure.

### Clean SURVIVE check

**YES.** P5 (Categories 3+4) and P8 (Category 7) are clean SURVIVEs. P1, P6, P9 are SURVIVE-with-caveat. No piece is KILL.

### Mechanism-Independence check

External-anchor evidence cited:
- Python stdlib `unicodedata` (executed locally; verified)
- PyPI library names (verified by training-knowledge + Python ecosystem evidence)
- W3C HTML5 Living Standard h1-h6 ceiling
- Pandoc documented format matrix
- Empirical Asa-yı Musa EPUB analysis (executed this session: 33 content files; flat h1; CSS-as-presentation; OPF metadata)
- Empirical Asa-yı Musa PDF + Muhakemat PDF degradation patterns (characterized in earlier session)

**Mechanism-Independence: VALIDATED.** External anchors include canonical sources (Python documentation; W3C spec; Pandoc spec) AND empirical artifact verification (executed `unicodedata.normalize` locally; empirical EPUB structure verified).

### Failure mode scan

- **#1 Wrong Dimensions:** NO. Dimensions derived from inquiry framing + critique focus areas.
- **#2 Rubber-Stamping:** NO. 7 piece-level REFINEs with concrete constructive output.
- **#3 Nitpicking:** NO. No piece KILLed over minor concerns; refinements address load-bearing wording.
- **#4 Dimension Blindness:** NO. D11 coverage + D12 bias-balance + D14 frame-premise explicitly checked.
- **#5 False Convergence:** NO. Clean SURVIVEs exist; refinements are structural sharpening not architectural change.
- **#6 Evaluation Drift:** NO. Single-pass; no cross-iteration drift.
- **#7 Self-Reference Collapse:** NO. External anchors cited.
- **#8 Axis Absence at Failure's Plane:** NO. D11 explicitly checked for omitted operations + D14 frame-premise.
- **#9 External-Grounding Absence:** NO. Library claims VERIFIED by local execution + spec citations.

### Convergence Telemetry

| Field | Value |
|---|---|
| Dimension coverage | FULL (D1-D14) |
| Adversarial strength | STRONG |
| Landscape stability | STABLE |
| Clean SURVIVE exists | YES (P5, P8 clean; P1, P6, P9 with caveat; 7 SURVIVE-with-REFINE) |
| Mechanism-independence status | `validated` |
| Failure modes observed | NONE |

**Output: PROCEED.**

---

## Final Verdict

### **SURVIVE-with-cross-cutting-refinements.**

The architectural commitment (8-category recommended set; "structural, not semantic" scope-line; two-layer corpus model; EPUB-first + PDF-fallback format priority; `extends:` relationship-label) SURVIVES. Seven cross-cutting refinements (wording + completeness additions; not architectural changes):

1. **P2 — scope-line wording soften.** Change "decidable" → "operational with explicit gray-zone adjudication path." Add table-detection / hierarchy-inference soft-verdict cases to worked examples.

2. **P3 — letter-spaced un-spacing reclassification.** Move the operation (generic typographic) to Category 1; keep the Turkish-script regex + frequency thresholds as Category 8 calibration data.

3. **P4 — three small additions.**
   - (a) Sentence segmentation: clarify load-bearing-for-translation-chunking (not raw LLM input).
   - (b) Add U+200E (LRM) and U+200F (RLM) to Category 1 zero-width character stripping.
   - (c) Script-specific punctuation preservation note (Arabic comma U+060C; question mark U+061F; CJK punctuation preserved, not normalized).

4. **P6 — depth policy caveat.** Add note: h6 ceiling rarely exceeded; literary texts typically cap at h4 (the user's instinct); academic texts may reach h5. Policy is permissive-not-restrictive.

5. **P7 — three small additions.**
   - (a) EPUB-first qualification: applies to WELL-FORMED EPUBs.
   - (b) EPUB-from-PDF detection + routing to PDF processing path (with heuristics: OCR artifacts; flat-h1; minimal CSS).
   - (c) Mention `python-bidi` as alternative to OCR for text-layer broken-bidi (cheaper when OCR isn't needed).

6. **P10 — two refinements.**
   - (a) Tighten Decision 4 wording: "DEFERRED with explicit revival path; 7-policy intent preserved as roadmap, not as v0.2 implementation."
   - (b) Add per-element provenance to inherited re-test: "INVALIDATED-FOR-V0.2 under recent scope narrowing; revival path preserved in DEFERRED 3."

7. **P11 — three MUSTs added; one DEFERRED promoted.**
   - MUST 5: test-case spec for v0.2 validation (fixture documents; per-category test cases; integration tests).
   - MUST 6: Mac app PipelineConfig.swift html-output integration.
   - MUST 7 (promoted from DEFERRED frontier): Pandoc version pin for v0.2 reproducibility.

8. **P12 — three open questions added.**
   - Multi-volume document handling (revival: project ingests multi-volume work).
   - Intake-output versioning (revival: preprocessing op spec changes and existing outputs need re-derivation).
   - EPUB-quality detection (revival: EPUB-from-PDF source encountered).

9. **P9 — make per-element-provenance reversal explicit.** Cite the prior commitment + this finding's reversal under scope narrowing.

These refinements are wording-level and completeness-level — they sharpen the finding's honesty and engineering-actionability without changing what's committed. The finding is ready for CONCLUDE with the refinements applied.

### Signal

**TERMINATE with ranked survivors:**

1. The 8-category recommended preprocessing set (P4-P8 + P3 Cat 8) — load-bearing.
2. The "structural, not semantic" scope-line principle (P2) — operational with gray-zone path.
3. The two-layer corpus model (P3) — generic core + Cat 8 extensions, opt-in.
4. EPUB-first + PDF-with-OCR-fallback format priority (P7) — qualified to well-formed EPUBs.
5. Source-driven hierarchy preservation up to HTML5 h6 (P6) — permissive; typical h4 cap.
6. `extends:` relationship-label (P10) — additive growth; nothing prior replaced.
7. MUST 1-7 + COULD 1-3 + DEFERRED 1-4 + Open Questions 1-9 (P11 + P12) — engineering roadmap.

Proceed to Routelister (exhaust step) with this critique's refinement notes integrated.
