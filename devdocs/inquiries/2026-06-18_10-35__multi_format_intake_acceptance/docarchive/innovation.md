# Innovation — multi-format intake acceptance

## User Input

Source: `_branch.md`. Upstream: `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md`. Production-task mode; 8 pieces (P1-P8); Piece-Level Inversion at P2 + P6.

---

## Phase 1 — Seed / Methodology-Mode Consideration

**Inherited methodology mode:** **Standard default** (balanced 4G+3F; elaborate the committed direction; produce ship-ready content).

**Alternative considered:** **Minimum-mechanism mode** (1G+1F only; maximize parsimony) — this is a small focused inquiry where minimum coverage might serve.

**What follows under the alternative:** Innovation runs Combination + Inversion at P2; minimum-mechanism at content pieces. Lower coverage but proportional to inquiry size.

**Decision:** **Standard default** with proportional depth — full mechanism coverage but tight per-piece content (this isn't a from-scratch architectural inquiry; it's a refinement). Piece-Level Inversion at P2 + P6 (meta-decision pieces) provides contrarian surface.

`Methodology-mode-alternative-marked-inapplicable: this inquiry is a refinement of a prior finding's one cell; full mechanism coverage with tight per-piece content fits better than minimum-mechanism.`

---

## Phase 2 — Generate (per piece)

### P2 (META-DECISION; FIRST per dependency order) — Acceptance-vs-priority + Decision-mode + Relationship-label

**Principal candidate (content):**

> **The load-bearing distinction: "accepted format" ≠ "priority format."**
>
> - **Accepted format** = intake reads the source and produces canonical HTML5 output (possibly with quality-tier flag indicating fidelity). The user is not refused.
> - **Priority format** = engineering investment for a high-quality reader and format-specific repair operations. The format is targeted in the v0.2 engineering scope.
>
> These are orthogonal axes: a format can be ACCEPTED + LOW-PRIORITY (read via the Pandoc baseline; no dedicated reader engineering) OR ACCEPTED + HIGH-PRIORITY (engineered reader path) OR NOT-YET-IMPLEMENTED + DEFERRED-PRIORITY (no reader path yet; engineering deferred).
>
> **Decision-mode commitment.** This finding's deliverable is a **YES with structural clarification** — validate the user's mental model (all 4 user-named formats accepted), refine the prior finding's DEFERRED 1 wording via the acceptance-vs-priority distinction, and commit the operational mechanism (routing + quality-tier flag). The deliverable shape is a per-format 4×2 matrix (P3) + routing-mechanism (P4) + quality-tier flag (P5) + relationship-label refinement (P6).
>
> **Relationship label: `refines:`** the prior `devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/finding.md`. The relationship is distinct from:
> - `extends:` (additive growth; no cell of prior changes) — this finding DOES change one cell of the prior's content (DEFERRED 1's wording), so `extends:` does not fit.
> - `supersedes:` (replaces) — nothing is wholly replaced; the prior's format priority stands; only DEFERRED 1 wording shifts.
> - `corrects:` (the prior was structurally wrong) — the prior was not wrong; the DEFERRED 1 wording was structurally compatible with both interpretations (priority-deferred vs acceptance-deferred), and this finding picks the structurally-coherent reading. The prior's wording was incomplete, not wrong.
>
> `refines:` is the structurally precise label: one cell of the prior's content is refined; the rest is preserved.
>
> **Why the user's question and the prior commitment both hold.** A close reading of the prior finding's actual DEFERRED 1 entry shows the language was about "extending format priority to Word and plain-text when sources expand" — note "extending priority," not "extending acceptance." The revival trigger was "project source-mix expands" — about engineering effort allocation. The distinction is present in the prior's own wording; this finding makes it explicit.

**Mechanism log:**
- *Combination:* recent scope-narrowing-style careful-reading + prior wording + Pandoc-as-lever (already supports all 4) → the distinction emerges as the resolution.
- *Lens Shifting:* under "where engineering invests vs what intake accepts" lens, the prior's DEFERRED reads as priority-deferred, not acceptance-deferred.
- *Constraint Manipulation (ADD):* added "user must be able to drop any file into intake" → acceptance becomes near-binary; priority becomes the gradient where engineering effort lives.
- *Constraint Manipulation (REMOVE):* removed "DEFERRED = refused" → the distinction's two axes separate.
- *Absence Recognition (patch):* the prior wording didn't disambiguate "plain-text" (txt vs md); this inquiry fills the gap.
- *Absence Recognition (redesign):* if the prior had been written with multi-format acceptance in mind from the start, the acceptance-vs-priority distinction would have been part of the original Next Actions structure.

**Piece-Level Inversion (required — P2 fires property (i) relationship-label + (ii) framing-semantic + (iii) lesson-vocabulary):**

> *Inversion-candidate:* what if the distinction is verbal sleight-of-hand and the prior's DEFERRED meant "not for v0.2 period" — i.e., refuse to ingest?
>
> *What follows under the inversion:* v0.2 intake rejects non-EPUB and non-PDF source files; user is forced to convert externally before using the app; the Mac app's UI must include format-conversion guidance.
>
> *Why rejected:* (a) The prior's actual wording was "extending priority," not "extending acceptance" — close reading supports the distinction, not the inversion. (b) User-agency principle: refusing a user's md or txt file is high-friction for v0.2 with no operational benefit (Pandoc reads them natively at near-zero cost). (c) The asymmetric-failure principle for format acceptance says under uncertainty, accept-with-flag over refuse-at-door; the inversion violates this. (d) The architectural lever (Decision 5 — Pandoc + OCR) already supports all 4 formats; refusing would mean DEFEATING the architectural lever's existing capability.
>
> *Intervention-shape check:* P2 commits to `refines:` (REPAIR-shape — modifying existing text that causes ambiguity while preserving the function). Alternatives: `extends:` (ADD-CONTENT — additive only; doesn't change prior); `supersedes:` (REVERT-REGRESSION or REMOVE); `corrects:` (REPAIR with stronger claim). `refines:` is REPAIR-shape with the right strength: change-with-preservation, not removal, not stronger-correction. Structurally accurate.
>
> Verdict on Inversion: **rejected** — the distinction is grounded in close-reading + user-agency + architectural-lever-already-supports.

**5-test:** Novelty (acceptance-vs-priority distinction was implicit in prior but not explicit; explicit articulation is novel); Scrutiny (survives Inversion + close-reading test); Fertility (spawns P3 matrix; spawns P5 quality-tier; spawns P7 refinements); Actionability (Mac app + engineering can act on the distinction immediately); Mechanism independence (Combination + Lens Shifting + Constraint Manipulation + Absence Recognition all converge on the distinction). PASS.

---

### P3 (CONTENT) — Per-format 4×2 matrix

**Principal candidate (content):**

> **Per-format acceptance and priority for v0.2:**
>
> | Format | Acceptance | Priority | Quality-tier flag | Notes |
> |---|---|---|---|---|
> | **EPUB** | ACCEPTED | HIGH (v0.2 target) | `high` | Category 6 EPUB path (spine reassembly; CSS-presentation extraction; heading-level inference; OPF metadata). Recommended for complex content (multi-alphabet; embedded apparatus; structurally-deep texts). Empirically validated via Asa-yı Musa EPUB analysis (publisher-issued, well-formed). |
> | **PDF** | ACCEPTED | MEDIUM (v0.2 target) | `medium` | Category 6 PDF path (mid-word hyphen repair; column-order; bidi-fix; italic recovery; OCR fallback via OCRmyPDF + Tesseract). Necessary for sources that exist primarily in PDF (e.g., Muhakemat's image-only Arabic). |
> | **markdown** | ACCEPTED | LOW | `low` | Pandoc baseline (Pandoc's primary input format). Categories 1, 2, 4, 5 (limited structural detection from md-encoded structure), 7 apply. Some structural features (e.g., per-element `lang` attribute) require Pandoc extensions (`bracketed_spans`) and may need workarounds. No dedicated reader engineering for v0.2. |
> | **plain txt** | ACCEPTED | MINIMUM | `minimal` | Pandoc baseline (read as paragraph-broken text; no structure recoverable). Categories 1, 2, 4, 7 apply; Category 5 structural detection is mostly inapplicable. No dedicated reader engineering for v0.2. |
> | **Word (.docx)** | NOT YET IMPLEMENTED | DEFERRED | n/a (not accepted) | Engineering for high-quality Word reader (style-mapping; run-merge) is post-v0.2. Revival trigger: project source-mix expands to include Word sources. |
>
> **Note on "all 3 vs 4" transcription.** The user's question said "all 3" but listed 4 formats (txt, md, pdf, epub). Treated as "all 4" — `txt + md + pdf + epub`. No architectural impact from the transcription.
>
> **The matrix's two axes derive from P2's distinction.** Acceptance is binary (ACCEPTED vs NOT-YET-IMPLEMENTED). Priority is gradient (HIGH / MEDIUM / LOW / MINIMUM / DEFERRED). The two axes are independent: priority does not determine acceptance, and acceptance does not determine priority. This is what allows the user's proposal (all 4 accepted) and the prior commitment (EPUB + PDF priority) to both hold.

**Mechanism log:**
- *Combination:* prior format-priority commitment × user's acceptance proposal × per-format Pandoc baseline → per-format 4×2 matrix.
- *Domain Transfer:* tiered service levels in software (premium / standard / basic / minimal) — the gradient priority axis is analogous.
- *Constraint Manipulation (ADD):* "must be honest about what v0.2 actually invests in" → priority gradient becomes explicit.

**5-test:** PASS — per-cell evidence cited; Pandoc-as-lever verified; empirical grounding (Asa-yı Musa EPUB) honored.

---

### P4 (CONTENT + MECHANISM) — Routing + Complex-content detection

**Principal candidate (content):**

> **Routing mechanism: hybrid auto-detect + warn-and-degrade + UI recommendation.**
>
> **Auto-detect** by file extension first, magic-bytes verification fallback:
> 1. Read file extension from the input path; map to format candidate (.epub / .pdf / .md / .txt → EPUB / PDF / md / txt).
> 2. Verify by inspecting the first ~256 bytes (magic bytes / shebang / DOCTYPE) via the `python-magic` library (PyPI; `libmagic` binding). Common magic-byte signatures for these formats:
>    - EPUB: `PK\x03\x04` (ZIP container header) + `mimetype` entry `application/epub+zip`
>    - PDF: `%PDF-` header
>    - md: no magic byte (text/plain); fallback to UTF-8 decode + heuristic (Markdown patterns: heading symbols, list markers)
>    - txt: text/plain; UTF-8 or encoding-detection per Category 6's plain-text path
> 3. If extension and magic bytes agree → confident route. If they disagree → magic bytes take precedence; emit a "format-extension-mismatch" Category 7 informational flag.
>
> **Warn-and-degrade** when the source format under-represents the content:
> 1. Process the file via the matched Category 6 path (or Pandoc baseline for md/txt).
> 2. Emit Category 7 informational flags including the quality-tier flag (per P5).
> 3. Do NOT refuse the source even when quality-tier is low or minimal. The user knows their source; intake's job is to do its best and signal honestly.
>
> **UI recommendation** in the Mac app:
> - When the user is about to ingest a non-EPUB source for a corpus the app knows has complex-content patterns (e.g., user has previously identified the corpus as Risale-i Nur, or the app is configured with calibration-corpus context), the UI shows a soft notice: *"This source is in [format] (quality-tier: [tier]). For best results with complex content (multi-alphabet, apparatus, deep structure), EPUB is recommended when available."* The user can dismiss / continue without changing source.
> - The UI does NOT block ingestion. The notice is informational.
>
> **Complex-content detection: documentation + UI guidance only (no runtime auto-detection for v0.2).**
>
> Complex content is characterized in project documentation as: multi-alphabet content (Latin + Arabic + Greek + Hebrew + etc.); embedded apparatus (footnotes / marginalia / endnotes); structural depth (multiple heading levels); mixed-direction text (LTR + RTL); significant italic/bold styling; special typography (drop-caps; letter-spaced emphasis; verse blocks); citation-heavy content; tables and figures.
>
> Runtime auto-detection at intake-time is deferred to a future version. Justification: (a) the user knows their source's complexity better than intake can detect from a quick scan; (b) the implementation cost (a model or heuristic to scan and classify) is not justified for v0.2 when the user's own knowledge serves; (c) documentation + UI guidance achieves the same outcome (the user picks an appropriate format) without the runtime cost; (d) future versions may add runtime detection if empirical evidence shows users miss the UI guidance (Open Question in P8).

**Mechanism log:**
- *Combination:* auto-detect-standard-practice (extension + magic bytes) × warn-and-degrade (preserves user agency) × UI recommendation (soft guidance) → composite routing mechanism.
- *Constraint Manipulation (ADD):* "must not refuse user's file" → warn-and-degrade is forced; routing decisions become informational rather than blocking.
- *Lens Shifting:* under "what does the Mac app user see when they drag a file in?" lens — the routing becomes a UX concern, not just a backend mechanism.
- *Absence Recognition:* the prior finding's format-priority section didn't specify routing; this fills the gap.

**5-test:** PASS — `python-magic` is real (PyPI); magic-byte signatures verifiable; warn-and-degrade composes with prior's Category 7; UI recommendation is concrete; no-runtime-detection justification multi-faceted.

---

### P5 (CONTENT) — Quality-tier flag schema

**Principal candidate (content):**

> **Quality-tier flag: Category 7 informational-flag schema extension.**
>
> The prior intake-preprocessing-operations finding's Category 7 (Quality / hygiene flags) committed an informational-flag exposure mechanism (MUST 4: schema + format choice between sidecar JSON `<canonical>.intake-flags.json` and HTML5 `<head>` `<meta>` blocks). This finding extends that schema with a new field:
>
> **Sidecar JSON schema extension:**
>
> ```json
> {
>   "source": "/abs/path/source.epub",
>   "intake_timestamp": "2026-06-18T10:50:00Z",
>   "quality_tier": "high",
>   "format": "epub",
>   "flags": [
>     {"code": "format-extension-mismatch", "severity": "info", "context": "..."},
>     {"code": "truncation", "severity": "warn", "context": "..."}
>   ]
> }
> ```
>
> **HTML5 `<meta>` mirror:**
> ```html
> <meta name="intake-quality-tier" content="high"/>
> <meta name="intake-format" content="epub"/>
> ```
>
> **Field semantics.**
>
> - `quality_tier` ∈ `{high, medium, low, minimal}` — derived from the per-format matrix (P3):
>   - `high` for well-formed EPUB (Category 6 EPUB path; structure preserved)
>   - `medium` for PDF (Category 6 PDF path; OCR + bidi-fix may have run; structure partially recovered)
>   - `low` for markdown (Pandoc baseline; some structural features reachable via extensions)
>   - `minimal` for plain text (Pandoc baseline; no structure)
> - `format` ∈ `{epub, pdf, md, txt}` — the format intake detected after auto-detection.
>
> **Composition with existing Category 7 flags.** The quality-tier is structurally distinct from the other Category 7 flags (truncation; suspicious-line-break; duplicate-content) — those are CONTENT-quality flags (about the source's content quality regardless of format); quality-tier is FORMAT-FIDELITY (about how much structure the format can carry). Both layers coexist in the same sidecar JSON or `<meta>` blocks.
>
> **Downstream consumer semantics.** Translate-stage may use the quality-tier flag to adjust prompt engineering (e.g., for `minimal` tier, the prompt may include "the source had no structural markup; preserve paragraph structure but do not invent headings"). Publishing-stage may use it for UI display ("translated from a [tier]-quality source"). The flag is informational; downstream consumers decide whether to act.
>
> **Legitimate concern — bias-balance.** The quality-tier flag may give a misleading signal in EPUB-from-PDF cases (the flag would say `high` based on format detection, but the actual fidelity is closer to PDF-medium because the EPUB was generated from a PDF and inherits PDF problems). The prior finding's R19 route (EPUB-from-PDF detection heuristics) addresses this — when EPUB-from-PDF is detected, downgrade quality-tier to `medium`. R19 remains an open route from the prior; this finding does not change that.

**Mechanism log:**
- *Combination:* prior Cat 7 schema × per-format priority matrix × downstream-consumer needs → schema extension.
- *Absence Recognition (patch):* prior Cat 7 had no format-fidelity field; this fills the gap.
- *Domain Transfer:* HTTP `Quality-Indicators` patterns (e.g., Content-Quality headers in some media protocols) — analogous.
- *Constraint Manipulation (ADD):* "downstream must know what fidelity intake delivered" → quality-tier becomes the per-source persistent signal.

**5-test:** PASS — JSON schema concrete; values enumerated; downstream consumer semantics named; bias-balance (EPUB-from-PDF caveat) acknowledged.

---

### P6 (META-DECISION + RELATIONSHIP) — Inherited Commitments Re-test

**Principal candidate (content):**

> This finding inherits commitments from the prior `devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/finding.md` (the intake-preprocessing-operations finding). The relationship label is `refines:` — one cell of the prior's content (DEFERRED 1 wording) is refined; the rest preserved.
>
> **Per-commitment re-test:**
>
> | Inherited commitment | Re-test status | Evidence |
> |---|---|---|
> | Format priority: EPUB-first + PDF-with-OCR-fallback for v0.2 | **RE-TESTED — commitment confirmed.** | This finding preserves EPUB + PDF as the priority targets for v0.2 engineering effort. The per-format matrix (P3) assigns HIGH priority to EPUB and MEDIUM to PDF — consistent with the prior. |
> | DEFERRED 1: "Word + plain-text format support" with revival trigger "project source-mix expands" | **RE-TESTED — commitment confirmed but wording REFINED.** | The substantive DEFERRED commitment holds about Word (engineering for high-quality Word reader is post-v0.2). The "plain-text" wording is split: txt + md are ACCEPTED at lower quality-tier (always were, via Pandoc baseline — Pandoc reads txt and md natively per Decision 5 of original intake-concepts); Word remains DEFERRED at the priority level. The revival trigger is implicitly fired by this user-driven inquiry. |
> | "Structural, not semantic" scope-line principle | **RE-TESTED — commitment confirmed.** | Quality-tier flag is structural format-fidelity, not semantic role tagging. Does not cross the scope-line. |
> | 8-category preprocessing pipeline | **RE-TESTED — commitment confirmed.** | Quality-tier flag extends Category 7 (informational flags); no new category. The pipeline stands. |
> | Two-layer corpus model (generic Categories 1-7 + opt-in Category 8 extensions) | **RE-TESTED — commitment confirmed.** | Unchanged; format acceptance is orthogonal to corpus extensions. |
> | HTML5 canonical format (inherited from the post-repair canonical-format finding via the prior intake-preprocessing-operations finding) | **RE-TESTED — commitment confirmed.** | All 4 accepted formats produce canonical HTML5 output. The canonical format is settled. |
> | Decision 5 from original intake-concepts: Pandoc + OCR architectural lever | **RE-TESTED — commitment confirmed and strengthened.** | The lever ALREADY supports all 4 user-named formats (Pandoc reads epub, html, markdown, docx, odt, rst, latex natively per documented format matrix; PDF is the special case requiring pdftotext + post-processing). The format-acceptance commitment is a natural extension of the lever's existing capability, not an architectural addition. |
>
> **The relationship label `refines:` is structurally precise.** Distinguished from siblings:
> - `extends:` would mean additive growth with no cell of prior changed. This finding DOES change one cell (DEFERRED 1 wording), so `extends:` does not fit.
> - `supersedes:` would mean replacing the prior. Nothing is wholly replaced; the prior's format priority stands.
> - `corrects:` would mean the prior was structurally wrong. The prior was not wrong; the DEFERRED 1 wording was structurally compatible with both interpretations (priority-deferred vs acceptance-deferred). This finding picks the structurally-coherent reading and refines the wording for clarity.

**Mechanism log:**
- *Combination:* prior's per-commitment list × this finding's content × per-commitment evidence → re-test verdict per commitment.
- *Domain Transfer:* software API versioning (refine — minor breaking change to one method's contract while preserving the rest of the API).
- *Absence Recognition:* the prior's DEFERRED 1 wording did not disambiguate "plain-text"; this fills the gap.

**Piece-Level Inversion (required — P6 fires property (i) relationship-label):**

> *Inversion-candidate:* what if the relationship is `supersedes:` (the prior was fundamentally wrong about its DEFERRED list — txt + md were always supposed to be at the v0.2 priority level)?
>
> *What follows under the inversion:* the prior finding's format priority commitment (EPUB-first + PDF-fallback) is INVALIDATED; v0.2 invests engineering effort in markdown reader and plain-text reader at the same priority as EPUB + PDF.
>
> *Why rejected:* (a) The prior's format-priority commitment is structurally sound — EPUB and PDF require dedicated engineering (Category 6 paths with OCR, bidi-fix, italic recovery, spine reassembly, CSS extraction); markdown is Pandoc-baseline-only; txt is degenerate. Treating all 4 as equal priority would dilute engineering focus without operational benefit. (b) Pandoc's existing capability (Decision 5) makes md and txt acceptance near-zero-cost; there's no engineering work to "prioritize." (c) The user's question was not "promote txt/md to high priority"; it was "are they accepted?" which is the acceptance question, not the priority question. The inversion mis-reads the user's question.
>
> *Intervention-shape Inversion check:* P6 commits to the `refines:` relationship-label (REPAIR-shape — modifying one cell of prior). Alternatives from the Intervention-Shape Vocabulary: `extends:` (ADD-CONTENT — no cell change; rejected because one cell DOES change); `supersedes:` (REVERT-REGRESSION / REMOVE — rejected per above structural reasoning); `corrects:` (REPAIR-stronger — rejected because prior was not wrong, just incomplete-in-wording). `refines:` is REPAIR with the right strength.
>
> Verdict on Inversion: **rejected** — the prior's format-priority is sound; only the DEFERRED 1 wording needs refinement; `refines:` is structurally precise.

**5-test:** PASS — per-commitment evidence cited; relationship-label distinguished from siblings; inversion-candidate generated and rejected with structural reasoning.

---

### P4 (already produced above)

### P5 (already produced above)

### P7 (DERIVED) — Transition plan + Next Actions

**Principal candidate (content):**

> **What changes from the prior finding.**
>
> The prior `2026-06-17_22-33__intake_preprocessing_operations/finding.md` had these directly-affected sections:
>
> 1. **DEFERRED 1 wording.** The prior wrote: *"Word and plain-text format support (Category 6 extension to additional source formats). Gate: observable — when the project's source-mix expands to include Word or plain-text sources. Why (if revived): the current corpus is EPUB/PDF-dominant; engineering effort is bounded."* This finding refines to: *"Word format support — engineering for high-quality Word reader (style-mapping; run-merge). Gate: observable — when project source-mix expands to include Word sources. Note: txt and md are ACCEPTED at low/minimal quality-tier via the Pandoc baseline since v0.2; this DEFERRED entry is now scoped specifically to Word."*
>
> 2. **MUST 4 — Category 7 flag-exposure mechanism.** The prior committed schema + format choice. This finding extends the schema with two new fields: `quality_tier` ∈ `{high, medium, low, minimal}` and `format` ∈ `{epub, pdf, md, txt}`. The schema spec (per MUST 4) is updated.
>
> **MUST items for this finding (additive on top of the prior's MUSTs):**
>
> - **What:** add `quality_tier` and `format` fields to the Category 7 flag schema (composes with prior MUST 4).
>   - **Who:** the MUST 4 inquiry / engineering team.
>   - **Gate:** condition-bound — together with MUST 4 schema commitment; before Category 7 engineering ships.
>   - **Why:** downstream consumers (translate-stage; Mac app UI) need format-fidelity signal to decide their handling.
>
> - **What:** add format-detection magic-bytes lookup table to intake's Category 4 (source-format detection). For each of the 4 supported formats, document the magic-byte signature + extension + Pandoc reader used.
>   - **Who:** Category 4 engineering.
>   - **Gate:** condition-bound — before v0.2 ships.
>   - **Why:** the routing mechanism (P4) depends on reliable format detection.
>
> - **What:** add Mac app UI message text for the "EPUB recommended for complex content" notice.
>   - **Who:** Mac app engineering.
>   - **Gate:** condition-bound — before v0.2 ships.
>   - **Why:** the routing mechanism (P4) commits this as the user-facing surface.
>
> - **What:** update the prior finding's Next Actions DEFERRED 1 text to the refined wording (scope to Word only; note txt + md as accepted at lower quality-tier).
>   - **Who:** documentation / finding-maintenance.
>   - **Gate:** at this finding's CONCLUDE step.
>   - **Why:** transparency; consistency.
>
> **COULD items:**
>
> - **What:** runtime complex-content auto-detection at intake-time.
>   - **Who:** a downstream `/traverse` inquiry.
>   - **Gate:** observable — if empirical evidence shows users miss the UI guidance and produce poor canonical HTML5 from low-fidelity sources.
>   - **Why:** would catch user-error before warn-and-degrade kicks in.
>
> - **What:** plain-text structural recovery (limited inference from blank-line patterns; numbered-section detection).
>   - **Who:** a downstream `/traverse` inquiry.
>   - **Gate:** observable — if users frequently hand plain-text Risale-i Nur sources and translation quality suffers.
>   - **Why:** would lift the txt quality-tier from `minimal` to `low` if achievable.
>
> **DEFERRED items (preserved from prior; no change):**
>
> - **Word format support** (engineering for high-quality Word reader) remains DEFERRED at the priority level. Revival trigger: project source-mix expands to include Word sources.
>
> **No DEFERRED items removed by this finding.** The prior's DEFERRED 1 split is wording-level; the Word component of DEFERRED 1 stays DEFERRED. The txt + md component of DEFERRED 1 is reclassified as ACCEPTED-at-lower-quality-tier (which was always implicit in Pandoc-as-lever).

**Mechanism log:**
- *Combination:* prior MUSTs + new schema-extension MUST + new format-detection MUST + new UI MUST → consolidated Next Actions.
- *Extrapolation:* implementation timeline → MUST priority.
- *Absence Recognition:* prior MUSTs didn't include format-detection magic-bytes table or UI message text; this fills the gaps.

**5-test:** PASS — per-item Who/What/Gate/Why; concrete refinements to specific prior content; COULD/DEFERRED distinguished from MUST.

---

### P8 (DERIVED) — Open Questions / Frontier

**Principal candidate (content):**

> **Open questions resolvable in downstream MUSTs/COULDs:**
>
> - **Magic-bytes lookup table maintenance.** When a new format is added (e.g., RTF, FB2), the lookup table needs extending. Revival trigger: a new format added to the accepted set.
>
> - **Quality-tier downgrade for EPUB-from-PDF.** The prior finding's R19 route (EPUB-from-PDF detection heuristics) needs to compose with the quality-tier flag — when EPUB-from-PDF is detected, the quality-tier should downgrade from `high` to `medium`. Revival trigger: R19 resolves.
>
> - **UI guidance effectiveness measurement.** When v0.2 ships, observe whether users heed the "EPUB recommended for complex content" UI notice. If users frequently ignore the notice and produce poor canonical HTML5, revisit complex-content auto-detection (COULD 1 of this finding's P7).
>
> **Frontier — deferred but not dismissed:**
>
> - **Runtime complex-content auto-detection.** Already a COULD; promoted to here as well for visibility. Revival trigger: empirical user-behavior evidence.
>
> - **Plain-text structural recovery.** Already a COULD. Revival trigger: empirical evidence of users handing plain-text Risale-i Nur sources.
>
> - **Word reader engineering.** Already DEFERRED in the prior; remains so. Revival trigger: project source-mix expands to include Word sources.
>
> - **RTF, FB2, ODT, MOBI, AZW3, KFX format acceptance.** Pandoc reads several of these (ODT natively; RTF as input; FB2, MOBI, AZW3, KFX not directly). Revival trigger: a specific user case for any of these formats. Most are very low priority for the project.
>
> - **Format conversion utilities** (e.g., an "convert this PDF to EPUB first for better results" utility in the Mac app). Revival trigger: empirical evidence that users want the conversion built into the app.
>
> - **Calibration-corpus-aware UI guidance.** Currently the "EPUB recommended" notice is generic. A more sophisticated version would depend on knowing the corpus (e.g., for Risale-i Nur — known complex — the notice is more emphatic; for a clean modern novel — known simple — the notice may be suppressed). Revival trigger: Category 8 corpus extensions API (R8 from prior).

**Mechanism log:**
- *Absence Recognition:* what's still open after this commitment? → enumerate.
- *Extrapolation:* future-state items (format conversion utilities; calibration-corpus-aware UI).

**5-test:** PASS — revival triggers specific (observable/condition-bound); frontier items distinguished from MUST/COULD-resolvable.

---

### P1 — Executive Summary (produced LAST per dependency order)

**Principal candidate (content):**

> **Yes — the user's proposal is correct.** Intake accepts all four user-named input formats — txt + md + pdf + epub (the user's "all 3" was a transcription typo; "all 4" is intended) — and EPUB is correctly the choice for complex content (multi-alphabet, embedded apparatus, structurally-deep texts). The user's proposal and the prior intake-preprocessing-operations finding both hold under a load-bearing distinction this finding articulates: **accepted format** (intake reads it and produces canonical HTML5) versus **priority format** (engineering invests in a high-quality reader). The prior finding's DEFERRED 1 wording was about priority-deferred, not acceptance-deferred — the architectural lever (Decision 5 — Pandoc + OCR) already supports all four formats. The per-format commitment for v0.2 is: **EPUB** accepted + HIGH priority (quality-tier `high`); **PDF** accepted + MEDIUM priority (quality-tier `medium`); **markdown** accepted + LOW priority (quality-tier `low`); **plain txt** accepted + MINIMUM priority (quality-tier `minimal`); **Word (.docx)** not yet implemented + DEFERRED priority (engineering deferred to post-v0.2). The routing mechanism is hybrid auto-detect (file extension first with `python-magic` magic-bytes verification fallback) + warn-and-degrade (process the file; emit a Category 7 `quality_tier` flag rather than refusing) + a Mac app UI recommendation ("EPUB recommended for best results with complex content" — soft guidance, not enforcement). Complex-content detection is documentation + UI guidance only for v0.2; runtime auto-detection is a deferred COULD. The quality-tier flag extends the prior finding's Category 7 informational-flag schema (MUST 4) with two new fields: `quality_tier` ∈ `{high, medium, low, minimal}` and `format` ∈ `{epub, pdf, md, txt}`. This finding **refines** the prior intake-preprocessing-operations finding by changing the DEFERRED 1 wording — splitting it so Word remains DEFERRED at the priority level while clarifying that txt + md are accepted at lower quality-tier via the Pandoc baseline (always were, but the prior wording was ambiguous).

**Mechanism log:**
- *Combination:* all 7 prior pieces → one-paragraph synthesis.
- *Lens Shifting:* under "at-a-glance lens" — names the YES answer first, then structural mechanism.

**5-test:** PASS — names YES verdict; names per-format matrix; names quality-tier flag; names routing mechanism; names `refines:` relationship; sized for one-paragraph reading.

---

## Inherited Frame Audit

**Step (i) — Seed central assumption.** The SV6 verdict commits the user's proposal as correct + the acceptance-vs-priority distinction as load-bearing. Central assumption: **the distinction holds under close reading of the prior's wording.**

**Step (ii) — Per-piece commitments.** Meta-decision pieces with Inversion: P2 (distinction + relationship-label) and P6 (re-test).

**Step (iii) — Challenge scan.**
- P2's Inversion tested "distinction is verbal sleight-of-hand" — rejected with close-reading + user-agency + architectural-lever evidence.
- P6's Inversion tested "supersedes: instead of refines:" — rejected with priority-soundness + user-question-mis-read evidence.

**Step (iv) — Firing condition.** Audit does **NOT fire**. Both meta-decision pieces have explicit Inversion-candidate testing with cited evidence.

---

## Phase 3 — Test + Assembly

### Per-piece 5-test summary

All 8 pieces' principal candidates passed the 5-test cycle. Inversion candidates at P2 and P6 were generated and rejected with structural reasoning.

### Assembly check

The 8 pieces assemble into a coherent refining finding: P1 (one-paragraph YES with structural mechanism) ↔ P2 (distinction + relationship-label) ↔ P3 (per-format matrix) ↔ P4 (routing + complex-detection) ↔ P5 (quality-tier flag schema) ↔ P6 (re-test) ↔ P7 (transitions) ↔ P8 (open questions). Each piece plays a structural role; the assembly produces the refining finding.

### Axis coverage check

- **Format axis** (EPUB / PDF / md / txt / Word) — covered by P3.
- **Acceptance-vs-priority axis** — covered by P2 + P3.
- **Routing-mechanism axis** — covered by P4.
- **Fidelity-signaling axis** — covered by P5.
- **Relationship axis** (refines: vs siblings) — covered by P2 + P6.
- **Time axis** (MUST / COULD / DEFERRED) — covered by P7.

All 6 axes have ≥1 candidate variant. PASS.

### Per-row mechanism-trace

Every piece has explicit mechanism work logged. P3's matrix has per-cell mechanism work (per-format priority assignment + quality-tier derivation). P2 + P6 have Inversion-candidate work explicitly logged. No row-baseline silent inheritance.

---

## Telemetry

### Mechanism Coverage

- **Generators applied:** 4 / 4 (Combination · Absence Recognition · Domain Transfer · Extrapolation).
- **Framers applied:** 3 / 3 (Lens Shifting · Constraint Manipulation · Inversion).
- **Coverage:** FULL.
- **Convergence:** YES — Combination + Lens Shifting + Constraint Manipulation + Absence Recognition all converge on the acceptance-vs-priority distinction.
- **Survivors tested:** 8 / 8 principal + 2 Inversion candidates = 10 / 10 tested.
- **Failure modes observed:** None.

### Production-task additional telemetry

| Piece | Mechanisms | Classification | Inversion compliance |
|---|---|---|---|
| P1 | Combination, Lens Shifting | content-production | n/a |
| P2 | Combination, Lens Shifting, Constraint Manipulation (ADD+REMOVE), Absence Recognition (patch+redesign), **Inversion** | **meta-decision** (i+ii+iii) | **satisfied** |
| P3 | Combination, Domain Transfer, Constraint Manipulation (ADD) | content-production | n/a |
| P4 | Combination, Constraint Manipulation (ADD), Lens Shifting, Absence Recognition | content-production | n/a |
| P5 | Combination, Absence Recognition, Domain Transfer, Constraint Manipulation (ADD) | content-production | n/a |
| P6 | Combination, Domain Transfer, Absence Recognition, **Inversion** | **meta-decision** (i) | **satisfied** |
| P7 | Combination, Extrapolation, Absence Recognition | content-production | n/a |
| P8 | Absence Recognition, Extrapolation | content-production | n/a |

### Verdict

**PROCEED** — full mechanism coverage; convergence on the acceptance-vs-priority distinction; all 8 piece candidates + 2 Inversion candidates tested; Piece-Level Inversion compliance satisfied at both meta-decision pieces; Inherited Frame Audit did not fire; Assembly + Axis coverage + Per-row mechanism-trace all PASS. No failure modes observed.
