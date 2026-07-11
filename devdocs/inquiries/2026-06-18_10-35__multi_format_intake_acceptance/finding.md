---
status: active
model: claude-opus-4-7
effort: max
refines: devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/finding.md
---

# Finding: Multi-Format Intake Acceptance

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/finding.md` (the intake-preprocessing-operations finding; committed 8-category preprocessing pipeline; format priority EPUB-first + PDF-with-OCR-fallback for v0.2; DEFERRED 1 = Word + plain-text format support).

**Revision trigger:** The user asked: *"I think during intake we accept txt, md, pdf, epub files all 3 [transcription typo for 'all 4']. But for complex text formattings such as multiple multi-alphabet texts etc., EPUB should be chosen. This makes sense?"* The user's mental model proposes intake accepts all four named formats with EPUB chosen for complex content. This finding validates the user's proposal and refines the prior's DEFERRED 1 wording to clarify the relationship between format **acceptance** (what intake reads) and format **priority** (what engineering invests in).

**Relationship label: `refines:`.** This finding refines one cell of the prior — the DEFERRED 1 wording — while preserving the rest. Distinct from:
- `extends:` (additive growth with no cell of prior changed). One cell DOES change here (DEFERRED 1 wording is split), so `extends:` does not fit.
- `supersedes:` (wholly replaces). Nothing is wholly replaced; the prior's format priority commitment stands.
- `corrects:` (the prior was structurally wrong). The prior was not wrong; the DEFERRED 1 wording was structurally compatible with both interpretations (priority-deferred vs acceptance-deferred), and the priority-deferred reading is the structurally-coherent one. The prior was incomplete-in-wording, not wrong.

**What's preserved.** The prior's format priority commitment (EPUB-first + PDF-with-OCR-fallback for v0.2) stands. The 8-category preprocessing pipeline stands. The "structural, not semantic" scope-line principle stands. The HTML5 canonical format stands. The two-layer corpus model stands. Decision 5 (Pandoc + OCR architectural lever, inherited from the original intake-concepts finding) stands — and was already strengthened by the prior intake-preprocessing-operations finding via Category 6; this finding consumes the already-strengthened lever without further strengthening it.

**What's changed.** The prior's DEFERRED 1 wording is refined. The prior wrote, verbatim:

> *"What: Word and plain-text format support (Category 6 extension to additional source formats). Gate: observable — when the project's source-mix expands to include Word or plain-text sources. Why (if revived): the current corpus is EPUB/PDF-dominant; engineering effort is bounded."*

This finding's per-format matrix (§2 below) supersedes that wording for all forward consumption. The prior finding remains historical record; no editing of the prior's text. The substantive change: **txt and markdown are accepted at lower quality-tier via the Pandoc baseline** (always were, since Pandoc reads them natively per Decision 5 of the original intake-concepts finding — the prior's "format support" wording conflated acceptance with engineering-priority). **Word remains DEFERRED at the priority level** (engineering for high-quality Word reader — Track Changes handling, embedded comments, etc. — is post-v0.2 work).

**What's new.**

1. The **acceptance-vs-priority distinction** — an explicit articulation of two orthogonal axes for format handling. See §1.
2. A **per-format 4×2 matrix** committing acceptance and priority verdicts for the four user-named formats plus Word. See §2.
3. A **routing mechanism** combining hybrid auto-detect (file extension first, magic-bytes verification fallback) + warn-and-degrade (process the file; emit a quality-tier flag) + UI recommendation in the Mac app. See §3.
4. A **complex-content detection commitment** — documentation + UI guidance only for v0.2; runtime auto-detection deferred. See §3.
5. A **quality-tier flag schema extension** to the prior finding's Category 7 informational-flag mechanism. See §4.

**Migration.** Zero — the user's question concerns v0.2 acceptance policy before v0.2 ships; no existing engineering relies on the prior's DEFERRED 1 wording. The per-format matrix in §2 becomes the operative reference for all v0.2 work.

---

## Question

(From `_branch.md`'s Item I1, verbatim:)

> *"I think during intake we accept txt, md, pdf, epub files all 3. But for complex text formattings such as multiple multi-alphabet texts etc., EPUB should be chosen. This makes sense?"*

The question carries three claims: (a) intake accepts four specific input formats (the user wrote "all 3" but listed 4 — transcription typo; "all 4" is intended); (b) EPUB should be chosen when the source has complex text formatting (multi-alphabet content as the named exemplar); (c) the user is asking for validation of these claims.

**Goal.** Adjudicate the user's proposal with structural clarification: yes/no validation plus an operational rationale for how the proposal composes with the prior intake-preprocessing-operations finding's commitments. Specifically: clarify how the prior's DEFERRED 1 (Word + plain-text format support) relates to the user's claim that txt + md + pdf + epub are all accepted; commit a routing mechanism that operationalizes "EPUB chosen for complex content"; specify how the quality difference between formats is signaled to downstream consumers.

Out of scope: the canonical format choice (HTML5, settled in the prior canonical-format finding); the 7-policy classification work (deferred per the recent scope narrowing); the 8-category preprocessing pipeline (settled in the prior intake-preprocessing-operations finding); translation-pipeline design (translate-stage is downstream).

---

## Finding Summary

- **Yes — the user's mental model is correct.** Intake accepts all four user-named input formats (txt + md + pdf + epub); EPUB is correctly identified as the right choice for complex content (multi-alphabet, embedded apparatus, structurally-deep texts).
- **The user's proposal and the prior commitment both hold** under a load-bearing distinction this finding articulates: **accepted format** (intake reads the source and produces canonical HTML5 output) versus **priority format** (engineering invests in a high-quality reader and format-specific repair operations). The prior finding's DEFERRED 1 wording was about priority-deferred (where engineering invests), not acceptance-deferred (what intake refuses).
- **Per-format commitment for v0.2** (see §2 for the full matrix):
  - **EPUB** — ACCEPTED + HIGH priority + quality-tier `high`. Category 6 EPUB path (spine reassembly; CSS-presentation extraction; heading-level inference; OPF metadata). Recommended for complex content.
  - **PDF** — ACCEPTED + MEDIUM priority + quality-tier `medium`. Category 6 PDF path (mid-word hyphen repair; column-order; bidi-fix; italic recovery; OCR fallback via OCRmyPDF + Tesseract).
  - **markdown** — ACCEPTED + LOW priority + quality-tier `low`. Pandoc baseline (markdown is Pandoc's primary input format); no dedicated reader engineering for v0.2.
  - **plain txt** — ACCEPTED + MINIMUM priority + quality-tier `minimal`. Pandoc baseline (read as paragraph-broken text; no structure recoverable); no dedicated reader engineering for v0.2.
  - **Word (.docx)** — ACCEPTED at MINIMUM priority via Pandoc baseline (Pandoc reads docx natively); quality-tier `minimal` for v0.2 Pandoc-baseline output; **DEFERRED engineering** for high-quality Word reader (Track Changes handling, embedded comments handling, run-merge, style-mapping). **UI exposure for Word is deferred** pending v0.2 engineering decision about Track Changes and comments handling.
- **The routing mechanism is hybrid auto-detect + warn-and-degrade + UI recommendation.** Auto-detect by file extension first, magic-bytes verification fallback via `python-magic` (PyPI library wrapping `libmagic`). When source format under-represents the content, intake processes the file and emits a Category 7 informational quality-tier flag rather than refusing. The Mac app surfaces a soft UI notice ("EPUB recommended for best results with complex content") when the user is about to ingest a non-EPUB source for a complex-content corpus.
- **Complex-content detection is documentation + UI guidance only for v0.2.** Runtime auto-detection at intake-time is deferred (Next Actions / COULD). The user knows their source's complexity better than intake can detect from a quick scan; the UI guidance surfaces before intake runs.
- **The quality-tier flag is a new field in the Category 7 informational-flag schema** (committed in the prior finding's MUST 4): `quality_tier ∈ {high, medium, low, minimal}` at the sidecar JSON top-level, plus a companion `format ∈ {epub, pdf, md, txt}` field. The flag is informational; downstream consumers (translate-stage; Mac app UI) decide whether to act.
- **Inherited commitments** from the prior intake-preprocessing-operations finding all stand. DEFERRED 1 wording is refined (split — Word remains DEFERRED-priority; txt + md were always-accepted via Pandoc baseline). Decision 5 (Pandoc + OCR architectural lever) is PRESERVED (already strengthened by the prior via Category 6; this finding consumes the lever but does not further strengthen it).

---

## Finding

### Context

The user is building comprehenslate — a generic translation project with Risale-i Nur as calibration corpus — and has been working through the intake-stage design via a sequence of inquiries. The prior intake-preprocessing-operations finding (`devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/finding.md`) committed an 8-category preprocessing pipeline anchored by a "structural, not semantic" scope-line principle, with EPUB-first + PDF-with-OCR-fallback as the v0.2 format priority and DEFERRED 1 = "Word and plain-text format support."

In conversation since that finding, the user asked whether intake accepts four input formats — txt, md, pdf, epub — with EPUB chosen for complex content. The question pivots on what "DEFERRED" meant in the prior wording, and what the operational policy for non-EPUB sources actually is.

This finding answers by articulating the load-bearing **acceptance-vs-priority distinction**: the prior's DEFERRED 1 was about engineering priority (where v0.2 invests in high-quality readers), not user-facing acceptance (what intake refuses). The architectural lever (Decision 5 of the original intake-concepts finding — Pandoc + OCR) already supports all four user-named formats natively; the prior's DEFERRED 1 wording conflated engineering-priority deferral with format-acceptance deferral. This finding splits the terminology, preserves the prior's format-priority commitment, and adds an operational routing mechanism plus a quality-tier flag.

### §1 — The acceptance-vs-priority distinction

The load-bearing distinction this finding commits:

- **Accepted format.** Intake reads the source and produces canonical HTML5 output (possibly with a quality-tier flag indicating fidelity). The user is not refused.
- **Priority format.** Engineering invests in a high-quality reader and format-specific repair operations. The format is targeted in the v0.2 engineering scope.

These are orthogonal axes. A format can be ACCEPTED + LOW-PRIORITY (read via the Pandoc baseline; no dedicated reader engineering) OR ACCEPTED + HIGH-PRIORITY (engineered reader path) OR NOT-YET-IMPLEMENTED + DEFERRED-PRIORITY (no reader path yet; engineering deferred). The two axes do not collapse into one another.

**Why this distinction is structurally grounded.** The prior intake-preprocessing-operations finding's DEFERRED 1 wording reads, verbatim:

> *"What: Word and plain-text format support (Category 6 extension to additional source formats). Gate: observable — when the project's source-mix expands to include Word or plain-text sources. Why (if revived): the current corpus is EPUB/PDF-dominant; engineering effort is bounded."*

Close reading: the qualifier "(Category 6 extension to additional source formats)" explicitly scopes the DEFERRED to Category 6 work — Category 6 is the prior's "format-specific repair" engineering category (EPUB spine reassembly; PDF OCR + bidi-fix; etc.). The "Why" clause names "engineering effort is bounded" as the gate — what's bounded is engineering effort, not user acceptance. Both phrasings support the priority-deferred reading.

The wording was genuinely ambiguous — a reader could plausibly extract either "engineering investment is deferred" or "intake refuses these formats" depending on the priors they bring to the term DEFERRED. This finding's refinement makes the priority-deferred reading explicit.

### §2 — The per-format 4×2 matrix

For each input format relevant to v0.2:

| Format | Acceptance | Priority | Quality-tier flag | Notes |
|---|---|---|---|---|
| **EPUB** | ACCEPTED | HIGH (v0.2 target) | `high` | Category 6 EPUB path (spine reassembly; CSS-presentation extraction — turn `class="bold"` into `<strong>`; heading-level inference for flat-h1 sources; OPF metadata extraction). Recommended for complex content (multi-alphabet, embedded apparatus, structural depth). Empirically validated via the Asa-yı Musa EPUB analysis (publisher-issued, well-formed; clean Unicode Arabic in text-layer; italic/bold preserved; footnote structure intact). |
| **PDF** | ACCEPTED | MEDIUM (v0.2 target) | `medium` | Category 6 PDF path (mid-word hyphen repair; column-order; bidi-fix; italic recovery via `mutool` or `pdf2htmlEX`; OCR fallback via OCRmyPDF + Tesseract `--lang ara+tur`). Necessary for sources that exist primarily in PDF (e.g., the Muhakemat PDF with image-only Arabic). |
| **markdown** | ACCEPTED | LOW | `low` | Pandoc baseline. Markdown is Pandoc's primary input format; Categories 1, 2, 4, 5 (limited structural detection from markdown-encoded structure), and 7 apply. Some structural features (e.g., per-element `lang` attribute) require Pandoc extensions (`bracketed_spans`) and may need workarounds. No dedicated reader engineering for v0.2. |
| **plain txt** | ACCEPTED | MINIMUM | `minimal` | Pandoc baseline (read as paragraph-broken text; no structure recoverable). Categories 1, 2, 4, 7 apply; Category 5 structural detection is mostly inapplicable (only blank-line paragraph inference). No dedicated reader engineering for v0.2. |
| **Word (.docx)** | ACCEPTED via Pandoc baseline | MINIMUM | `minimal` | Pandoc reads docx natively (per documented format matrix). v0.2 Pandoc-baseline output is acceptable for clean Word documents (paragraph + heading structure preserved via Pandoc's style-mapping). **UI exposure for Word is DEFERRED** pending v0.2 engineering decision about Track Changes handling, embedded comments handling, run-merge, and style-mapping refinements. **Engineering for high-quality Word reader DEFERRED** at the priority level. |

**Note on transcription.** The user's question said "all 3" but listed four formats (txt + md + pdf + epub). Treated as "all 4." No architectural impact.

**The matrix's two axes derive from §1's distinction.** Acceptance is binary (ACCEPTED via Pandoc baseline / NOT-YET-IMPLEMENTED for entirely new format paths). Priority is gradient (HIGH / MEDIUM / LOW / MINIMUM / DEFERRED). The two axes are independent: priority does not determine acceptance, and acceptance does not determine priority. This is what allows the user's proposal (all 4 accepted) and the prior commitment (EPUB + PDF priority) to both hold.

### §3 — The routing mechanism

The routing mechanism has three composable layers.

**Auto-detect** by file extension first, magic-bytes verification fallback:

1. Read the file extension from the input path; map to format candidate (`.epub` / `.pdf` / `.md` / `.txt` → EPUB / PDF / md / txt).
2. Verify by inspecting the first ~256 bytes via the `python-magic` library (PyPI; `libmagic` binding). Magic-byte signatures for the v0.2 formats:
   - **EPUB**: `PK\x03\x04` (ZIP container header) plus a `mimetype` entry containing `application/epub+zip`.
   - **PDF**: `%PDF-` header (per the PDF specification).
   - **markdown**: no magic byte (text/plain). Fallback to UTF-8 decode + markdown-pattern heuristic (heading symbols `#`; list markers `-` or `*`; etc.).
   - **plain txt**: text/plain; encoding detection per Category 6's plain-text path.
3. If extension and magic bytes agree, the route is confident. If they disagree, magic bytes take precedence and intake emits a `format-extension-mismatch` Category 7 informational flag.
4. **`format-extension-mismatch` flag downstream consequence.** The flag surfaces the disagreement to translate-stage and the Mac app UI. Translate-stage may use it to decide whether to trust the source-format metadata; the Mac app UI may display the mismatch to the user.

**Warn-and-degrade** when the source format under-represents the content:

1. Process the file via the matched Category 6 path (or Pandoc baseline for markdown / txt / docx).
2. Emit Category 7 informational flags including the quality-tier flag (per §4).
3. Do NOT refuse the source even when the quality-tier is low or minimal. The user knows their source; intake's job is to do its best and signal honestly.

**UI recommendation** in the Mac app:

1. When the user is about to ingest a non-EPUB source for a corpus the app knows has complex-content patterns (e.g., the user has previously identified the corpus as Risale-i Nur, or the app is configured with calibration-corpus context), the UI shows a soft notice: *"This source is in [format] (quality-tier: [tier]). For best results with complex content (multi-alphabet, embedded apparatus, deep structure), EPUB is recommended when available."* The user can dismiss or continue without changing source.
2. The UI does NOT block ingestion. The notice is informational.

**Complex-content detection: documentation + UI guidance only for v0.2.** Complex content is characterized in project documentation as: multi-alphabet content (Latin + Arabic + Greek + Hebrew + etc.); embedded apparatus (footnotes / marginalia / endnotes); structural depth (multiple heading levels); mixed-direction text (LTR + RTL); significant italic/bold styling; special typography (drop-caps; letter-spaced emphasis; verse blocks); citation-heavy content; tables and figures.

Runtime auto-detection at intake-time is deferred to a future version. Justification: the user knows their source's complexity better than intake can detect from a quick scan; the implementation cost (a model or heuristic to scan and classify) is not justified for v0.2 when the user's own knowledge serves; documentation + UI guidance achieves the same outcome (the user picks an appropriate format) without the runtime cost. Future versions may add runtime detection if empirical evidence shows users miss the UI guidance (Open Questions section, "UI guidance effectiveness measurement").

### §4 — The quality-tier flag schema extension

The prior intake-preprocessing-operations finding's Category 7 (Quality / hygiene flags) committed an informational-flag exposure mechanism (MUST 4 of the prior): a sidecar JSON file `<canonical>.intake-flags.json` next to the canonical HTML5 file, with a schema listing flag codes, severity, context, and source positions, plus an alternative mirror via HTML5 `<head>` `<meta>` blocks.

This finding extends that schema with two new top-level fields.

**Sidecar JSON schema extension:**

```json
{
  "source": "/abs/path/source.epub",
  "intake_timestamp": "2026-06-18T11:00:00Z",
  "quality_tier": "high",
  "format": "epub",
  "flags": [
    {"code": "format-extension-mismatch", "severity": "info", "context": "..."},
    {"code": "truncation", "severity": "warn", "context": "..."}
  ]
}
```

**HTML5 `<meta>` mirror:**

```html
<meta name="intake-quality-tier" content="high"/>
<meta name="intake-format" content="epub"/>
```

**Field semantics.**

- `quality_tier ∈ {high, medium, low, minimal}` — derived from the per-format matrix in §2:
  - `high` for well-formed EPUB (Category 6 EPUB path; structure preserved).
  - `medium` for PDF (Category 6 PDF path; OCR plus bidi-fix may have run; structure partially recovered).
  - `low` for markdown (Pandoc baseline; some structural features reachable via extensions).
  - `minimal` for plain text and v0.2 Pandoc-baseline Word output (no structure recoverable from txt; Word's Pandoc-baseline produces minimum-fidelity output for v0.2 since dedicated Word reader engineering is deferred).
- `format ∈ {epub, pdf, md, txt}` — the format intake detected after auto-detection. (Word is detected if accepted via Pandoc baseline; the corresponding `format` value would be `docx` when Word is exposed in the UI, which v0.2 has not committed.)

**Composition with existing Category 7 flags.** The quality-tier is structurally distinct from the other Category 7 flags (truncation; suspicious-line-break; duplicate-content). Those are content-quality flags (about the source's content quality regardless of format). The quality-tier is format-fidelity (about how much structure the format can carry). Both layers coexist in the same sidecar JSON or `<meta>` blocks.

**Downstream consumer semantics.** Translate-stage may use the quality-tier flag to adjust prompt engineering (e.g., for `minimal` tier, the prompt may include "the source had no structural markup; preserve paragraph structure but do not invent headings"). The Mac app may use it for UI display ("translated from a [tier]-fidelity source"). The flag is informational; downstream consumers decide whether to act.

**Legitimate caveat — EPUB-from-PDF.** The quality-tier flag may give a misleading signal when an EPUB was generated from a PDF and inherits PDF problems (broken-bidi Arabic; lost styling; bad paragraph splits). The flag would naively say `high` based on the file format, but the actual fidelity is closer to PDF-medium. The prior finding's R19 route — EPUB-from-PDF detection heuristics — addresses this case: when EPUB-from-PDF is detected (via heuristics like OCR artifacts in text, flat-h1, minimal CSS), downgrade the quality-tier from `high` to `medium`. The integration is named as Next Actions / MUST 5 below.

### §5 — Why the user's mental model is correct

The user proposed: intake accepts txt + md + pdf + epub; EPUB should be chosen for complex content. Three observations support the "yes" verdict:

1. **The architectural lever supports all four.** Decision 5 of the original intake-concepts finding committed Pandoc plus OCR as the universal converter. Pandoc reads EPUB, HTML, markdown, docx, odt, rst, latex natively per the documented format matrix. Pandoc does not natively read PDF — the PDF case is the special engineering scope (Category 6 PDF path with OCR + bidi-fix + italic recovery). The user's four named formats are exactly the ones Pandoc handles directly (for md, epub) or via the prior's existing engineering path (for pdf). txt is the degenerate case.

2. **EPUB is genuinely the highest-fidelity input for complex content.** EPUB content documents are XHTML5 (per the W3C EPUB 3.3 specification), which means they preserve heading hierarchy (h1–h6), semantic markup, language attributes via `lang=`, structural elements (section, article, aside, figure, blockquote), and metadata in the OPF manifest. For multi-alphabet content (Latin + Arabic + Greek + Hebrew), embedded apparatus (footnotes / marginalia), structural depth, and significant italic/bold styling, EPUB carries the structure cleanly. PDF requires reconstruction (OCR; bidi-fix; italic recovery); markdown requires extensions (`bracketed_spans` for `lang`); plain text loses everything. The Asa-yı Musa EPUB analysis empirically validated EPUB's fidelity for the calibration corpus.

3. **The user's "EPUB chosen for complex content" is a soft preference, not a hard rule.** This finding's commitment is to communicate the preference via documentation and Mac app UI guidance (a soft notice the user can dismiss), not to enforce. The user retains agency to ingest any of the four formats.

---

## Inherited Commitments Re-test

This finding refines the prior intake-preprocessing-operations finding (`devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/finding.md`) and through it inherits commitments from the original intake-concepts finding (`devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`) and the post-repair canonical format finding (`devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/finding.md`).

| Inherited commitment | Re-test status | Evidence |
|---|---|---|
| Format priority: EPUB-first + PDF-with-OCR-fallback for v0.2 | **RE-TESTED — commitment confirmed.** | This finding preserves EPUB + PDF as the priority targets for v0.2 engineering effort. The per-format matrix (§2) assigns HIGH priority to EPUB and MEDIUM to PDF — consistent with the prior. |
| DEFERRED 1: "Word + plain-text format support" with revival trigger "project source-mix expands" | **RE-TESTED — commitment confirmed substantively but wording REFINED.** | The substantive engineering-priority deferral for Word stands. The "plain-text" wording is split via the per-format matrix: txt and markdown are ACCEPTED at lower quality-tier via the Pandoc baseline (always were, via Decision 5); Word is ACCEPTED at MINIMUM priority via the Pandoc baseline with UI exposure deferred. High-quality Word reader engineering remains DEFERRED. The revival trigger "project source-mix expands" is implicitly fired by this user-driven inquiry. The prior finding remains historical record; this finding's per-format matrix supersedes the prior's DEFERRED 1 wording in practice. |
| "Structural, not semantic" scope-line principle | **RE-TESTED — commitment confirmed.** | The quality-tier flag is structural format-fidelity, not semantic role tagging. The flag does not cross the scope-line. |
| 8-category preprocessing pipeline | **RE-TESTED — commitment confirmed.** | The quality-tier flag extends Category 7 (Quality / hygiene informational flags) with two new fields; no new category. The pipeline stands. |
| Two-layer corpus model (generic Categories 1–7 + opt-in Category 8 extensions) | **RE-TESTED — commitment confirmed.** | Format acceptance is orthogonal to corpus extensions; the two-layer model is unchanged. |
| HTML5 canonical format (inherited via the post-repair canonical format finding) | **RE-TESTED — commitment confirmed.** | All accepted formats produce canonical HTML5 output. The canonical format is settled. |
| Decision 5 from original intake-concepts: Pandoc + OCR architectural lever | **RE-TESTED — commitment PRESERVED.** The lever was already strengthened by the prior intake-preprocessing-operations finding via Category 6 (format-specific repair leans explicitly on Pandoc readers and OCRmyPDF plus Tesseract). This finding **consumes** the already-strengthened lever to extend format acceptance (Pandoc reads EPUB / markdown / docx natively; PDF via OCR; txt as paragraph-broken text), but does not **further strengthen** the lever itself. | The lever's existing capability is what enables this finding's per-format matrix; the matrix uses what's already there. |

---

## Next Actions

### MUST

- **What:** Add `quality_tier` and `format` fields to the Category 7 informational-flag schema. Document the field semantics for downstream consumers (translate-stage; Mac app UI).
  - **Who:** the MUST 4 inquiry / engineering team (composes with the prior finding's MUST 4 schema commitment).
  - **Gate:** condition-bound — together with the prior MUST 4 schema commitment, before Category 7 engineering ships.
  - **Why:** downstream consumers need a format-fidelity signal to decide their handling.

- **What:** Document magic-byte signatures and detection algorithm for the four v0.2 input formats. Implement via `python-magic` (PyPI library wrapping `libmagic`) plus extension-first hybrid logic.
  - **Who:** Category 4 source-format-detection engineering.
  - **Gate:** condition-bound — before v0.2 ships.
  - **Why:** the routing mechanism (§3) depends on reliable format detection.

- **What:** Draft Mac app UI message text for the "EPUB recommended for complex content" notice. Specify display conditions (when the user is about to ingest a non-EPUB source for a complex-content corpus), dismissal behavior (user can continue without changing source; notice does not block), and display timing (before intake runs).
  - **Who:** Mac app engineering.
  - **Gate:** condition-bound — before v0.2 ships.
  - **Why:** the routing mechanism (§3) commits this as the user-facing guidance surface; the UI text is part of the surface.

- **What:** Integrate EPUB-from-PDF detection (per the prior finding's R19 route) with the quality-tier flag. When EPUB-from-PDF is detected, downgrade the quality-tier from `high` to `medium`.
  - **Who:** a downstream inquiry composing R19 of the prior finding with this finding's quality-tier flag.
  - **Gate:** condition-bound — when R19 of the prior finding resolves.
  - **Why:** the per-format matrix's EPUB=high assumes well-formed EPUB; the EPUB-from-PDF edge case violates the assumption.

### COULD

- **What:** Runtime complex-content auto-detection at intake-time. Heuristics or model for detecting multi-alphabet content (Unicode-range scan), embedded apparatus (footnote-anchor scan), structural depth (heading-count); intelligent EPUB recommendation.
  - **Who:** a downstream `/traverse` inquiry.
  - **Gate:** observable — when empirical evidence shows users miss the UI guidance and produce poor canonical HTML5.
  - **Why:** would catch user-error before warn-and-degrade kicks in.

- **What:** Plain-text structural recovery from blank-line patterns plus numbered-section markers. Lift the txt quality-tier from `minimal` to `low` for sources with detectable structure.
  - **Who:** a downstream `/traverse` inquiry.
  - **Gate:** observable — when users frequently hand intake plain-text Risale-i Nur sources and translation quality suffers from the loss of structure.
  - **Why:** would improve translate-quality for plain-text sources without adding format-specific engineering.

### DEFERRED

- **What:** Word reader engineering for high-quality intake (style-mapping refinements; run-merge; Track Changes handling; embedded comments handling; UI exposure of Word as a v0.2 accepted format).
  - **Gate:** observable — when the project's source-mix expands to include Word sources, OR when the Pandoc baseline output for Word proves inadequate for the calibration corpus.
  - **Why (if revived):** high-quality Word intake requires engineering investment beyond Pandoc's baseline reader behavior.

---

## Reasoning

This section explains why the recommended position holds.

### What survived adversarial scrutiny

**The acceptance-vs-priority distinction.** Critique tested whether the distinction is verbal sleight-of-hand or structurally grounded. Verbatim citation of the prior's actual DEFERRED 1 wording confirms the priority-deferred reading is structurally supported: the qualifier "(Category 6 extension to additional source formats)" scopes the DEFERRED to Category 6 engineering work, and the gate "engineering effort is bounded" names what's bounded as engineering effort, not user acceptance. The distinction makes the priority-deferred reading explicit; it is not post-hoc rationalization.

**The per-format 4×2 matrix.** Critique surfaced a Word-row consistency concern — the original innovation framed Word as "NOT YET IMPLEMENTED + DEFERRED" which was inconsistent with the txt and md treatment. This finding refines Word to "ACCEPTED via Pandoc baseline at MINIMUM priority; UI exposure DEFERRED; high-quality engineering DEFERRED" — consistent with how txt and md are treated and honest about what Pandoc reading docx natively means.

**The hybrid auto-detect routing mechanism.** Critique tested the markdown-detection ambiguity (no magic byte for text/markdown) and the format-extension-mismatch flag's downstream consequence. The finding now specifies that markdown detection relies on UTF-8 decode plus markdown-pattern heuristic, and that the format-extension-mismatch flag surfaces the disagreement to translate-stage and the Mac app UI (translate-stage uses it to decide whether to trust source-format metadata; the UI displays the mismatch to the user).

**The quality-tier flag schema.** Critique tested field placement (top-level vs inside `flags` array — top-level is correct because `quality_tier` is a per-source attribute, not a flag-event), granularity (4 tiers is intuitive and matches user understanding), and the EPUB-from-PDF caveat (acknowledged explicitly with the prior finding's R19 route as the resolution path).

**The relationship label `refines:`.** Critique tested against alternatives. `extends:` does not fit because one cell of the prior DOES change (DEFERRED 1 wording). `supersedes:` does not fit because nothing is wholly replaced. `corrects:` does not fit because the prior was not structurally wrong, just incomplete-in-wording. `refines:` is the precise label for "change one cell of inherited architecture while preserving the rest."

### What was killed and why

**The "NOT YET IMPLEMENTED" framing of Word.** Killed because it was inconsistent with how txt and md were treated. Pandoc reads docx natively, so Word is technically accepted at near-zero cost (Pandoc baseline). The honest framing is "ACCEPTED via Pandoc baseline at MINIMUM priority; UI exposure deferred" — consistent with txt and md.

**The claim that this finding STRENGTHENS Decision 5.** Killed because the prior intake-preprocessing-operations finding already strengthened Decision 5 via Category 6 explicit reliance on Pandoc readers and OCRmyPDF + Tesseract. This finding consumes the already-strengthened lever but does not add to it. The honest verdict is PRESERVED.

**The MUST item "update the prior finding's DEFERRED 1 wording."** Killed because findings are immutable historical record. Refining a prior produces a new finding (this one) whose content supersedes the prior in practice; the prior remains as-is. The honest framing is "this finding's per-format matrix supersedes the prior's DEFERRED 1 wording for all forward consumption; no editing of the prior."

**Runtime complex-content auto-detection for v0.2.** Killed (deferred to COULD) because the user knows their source's complexity better than intake can detect from a quick scan, and the implementation cost is not justified for v0.2 when documentation plus UI guidance achieves the same outcome. Future versions may revive if empirical evidence shows the guidance is missed.

### Contradictions reconciled across upstream disciplines

Articulation surfaced two open dimensions: decision-mode (validate / refine / overturn / clarify / design) and routing-mechanism (auto-detect / warn-and-degrade / refuse). Sensemaking adjudicated decision-mode = validate + refine + commit-quality-tier (the WHY-axis included scope-setting for v0.2 engineering plus wanting clarity on routing; the combined output shape serves all WHY-axis motivations) and routing-mechanism = hybrid auto-detect + warn-and-degrade + UI recommendation (user-agency principle plus standard file-handling practice).

Surfacing's 59 candidates across 10 sub-regions were partitioned via the acceptance-vs-priority distinction into the per-format matrix and the supporting mechanisms (routing; complex-content detection; quality-tier flag; relationship label).

Critique surfaced six wording-level refinements which this finding integrates: verbatim citation of the prior DEFERRED 1; Word-row consistency in the per-format matrix; format-extension-mismatch flag downstream consequence; Decision 5 verdict honest framing; update-prior MUST honest framing; addition of four frontier items (streaming intake; multi-file / multi-volume cross-referencing the prior's R20; URL input; Mac app drag-and-drop UX).

---

## Open Questions

### Monitoring

The v0.2 ship plus the calibration prototype against Risale-i Nur source files will produce the first empirical answer to several questions: whether users heed the "EPUB recommended" UI notice; whether the auto-detect mechanism produces reliable format identification across the input distribution; whether the quality-tier flag's downstream consumption (in translate-stage prompts and Mac app UI) actually improves outcomes.

### Blocked

The EPUB-from-PDF quality-tier downgrade (Next Actions / MUST 5) is blocked on resolution of the prior finding's R19 route (EPUB-from-PDF detection heuristics).

The Calibration-corpus-aware UI guidance is blocked on the prior finding's R8 route (Category 8 extensions API design).

### Research Frontiers

**Magic-bytes lookup table maintenance.** When a new format is added (RTF, FB2, ODT, MOBI, AZW3, KFX, etc.), the lookup table needs extending. Revival trigger: a new format added to the accepted set.

**UI guidance effectiveness measurement.** When v0.2 ships, observe whether users heed the EPUB-recommendation notice. If users frequently ignore the notice and produce poor canonical HTML5, revisit complex-content auto-detection. Revival trigger: empirical user-behavior evidence post-v0.2 ship.

**Additional format acceptance** (RTF / FB2 / ODT / MOBI / AZW3 / KFX). Pandoc reads several of these (ODT and RTF natively; FB2 / MOBI / AZW3 / KFX not directly). Revival trigger: a specific user case for any of these formats.

**Format conversion utilities** built into the Mac app (e.g., a "convert PDF to EPUB first for better results" utility). Revival trigger: empirical evidence that users want format-conversion built into the app.

**Calibration-corpus-aware UI guidance.** Currently the "EPUB recommended" notice is generic. A more sophisticated version would depend on knowing the corpus (e.g., for Risale-i Nur — known complex — the notice is more emphatic; for a clean modern novel — known simple — the notice may be suppressed). Revival trigger: Category 8 corpus extensions API resolves.

**Streaming intake for large source files** (100+ MB). Revival trigger: a source file exceeds in-memory processing limits.

**Multi-file / multi-volume input** (Risale-i Nur Külliyat as 5+ volumes). Cross-reference the prior intake-preprocessing-operations finding's R20 route (multi-volume document handling). Revival trigger: project ingests a multi-volume work.

**URL input** (user provides a URL rather than a local file). Revival trigger: project source-mix includes web-sourced content (Substack articles; GitHub README; online editions).

**Mac app drag-and-drop UX specifics.** Concrete UX design for how users provide source files to intake (drag-and-drop; file picker; URL input; multi-file selection; processing feedback; error display; quality-tier display). Revival trigger: Mac app v0.2 UI implementation begins.

### Refinement Triggers

**The per-format matrix re-opens if** empirical evidence from v0.2 production shows that a quality-tier assignment is wrong (e.g., markdown sources consistently produce minimum-fidelity output rather than low-fidelity).

**The acceptance-vs-priority distinction re-opens if** a future inquiry surfaces a case where the distinction breaks down (e.g., a format that is "partially accepted" — read but not fully — defying binary acceptance).

**The format-priority commitment re-opens if** Word usage becomes common and the Pandoc baseline output for Word proves inadequate for the calibration corpus (would promote Word from DEFERRED-engineering to MEDIUM-priority).

**The complex-content detection commitment re-opens if** empirical evidence post-v0.2 shows users miss the UI guidance (would revive Next Actions / COULD 1 — runtime auto-detection).

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
i think during intake we accpet txt, md, pdf, epub files all 3.  But for complex text formattings such as multiple multi alpahbet texts etc, epub should be chosen. this makes sense?
```

</details>
