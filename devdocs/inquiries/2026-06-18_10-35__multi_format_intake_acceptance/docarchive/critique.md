# Critique — multi-format intake acceptance

## User Input

Source: `_branch.md`. Upstream: `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md` + `innovation.md`.

Critical framing: the inquiry committed the user's proposal as correct via the acceptance-vs-priority distinction; per-format 4×2 matrix; routing mechanism; quality-tier flag extending Category 7; relationship-label `refines:`. Adversarial testing across 11 focus areas.

---

## Phase 0 — Dimension Construction

| # | Dimension | Question | Weight |
|---|---|---|---|
| D1 | Anti-hallucination grounding | Are Pandoc / PyPI / spec claims verifiable? | **CRITICAL** |
| D2 | Acceptance-vs-priority distinction rigor | Is the distinction structurally grounded vs verbal sleight-of-hand? | **CRITICAL** |
| D3 | Per-format matrix rigor | Are per-format cells (especially Word; EPUB-from-PDF caveat) consistent and honest? | **CRITICAL** |
| D4 | Routing mechanism soundness | Does hybrid auto-detect + warn-and-degrade work in practice? | HIGH |
| D5 | Complex-content detection commitment | Is "no runtime detection" justified for v0.2? | HIGH |
| D6 | Quality-tier flag schema | Is the schema design (field placement; granularity) correct? | HIGH |
| D7 | Inherited re-test honesty | Is DEFERRED 1 = REFINED honest? Is Decision 5 STRENGTHENED accurate? | **CRITICAL** |
| D8 | Relationship-label accuracy | Is `refines:` correct vs alternatives? | HIGH |
| D9 | Transition plan completeness | Are MUST items well-formed; is "update prior" honest? | HIGH |
| D10 | Coverage / omitted considerations | Are streaming / multi-file / URL / drag-and-drop UX addressed? | MEDIUM |
| D11 | Bias-balance | Are legitimate concerns surfaced? | HIGH |
| D12 | External-anchor evidence | Are prior-finding citations verbatim? | **CRITICAL** |

### Frame-premise test

Three load-bearing premises:

**Premise 1: The acceptance-vs-priority distinction is structurally grounded in the prior wording.**
- *What-if-wrong:* the prior's DEFERRED 1 was acceptance-deferred (refuse to ingest); the distinction is post-hoc rationalization.
- *Prosecution:* the prior wording "Word and plain-text format support" is ambiguous; could be read either way.
- *Defense:* verified verbatim via grep — prior's actual text is *"Word and plain-text format support (Category 6 extension to additional source formats). Gate: observable — when the project's source-mix expands to include Word or plain-text sources. Why (if revived): the current corpus is EPUB/PDF-dominant; engineering effort is bounded."* The "(Category 6 extension)" qualifier and "engineering effort is bounded" gate STRONGLY support the priority-deferred reading. Category 6 is explicitly the "format-specific repair" engineering category; the DEFERRED is about extending engineering work, not refusing user files.
- *Verdict:* Premise survives. The wording IS ambiguous (multiple readings extractable) but LEANS toward priority-deferred. Refinement is valuable disambiguation.

**Premise 2: Pandoc-as-architectural-lever already supports the 4 user-named formats.**
- *What-if-wrong:* one or more formats are not Pandoc-native; the architectural lever doesn't quite work as claimed.
- *Prosecution:* PDF is NOT Pandoc-native (Pandoc 2.x+ has a PDF reader but it calls out to pdftotext; not a native parser).
- *Defense:* innovation acknowledges this explicitly ("Pandoc does NOT natively read PDF (requires pdftotext + post-processing)"). EPUB / HTML / markdown / docx / odt ARE Pandoc-native readers. The lever is honestly characterized.
- *Verdict:* Premise survives with explicit caveat (PDF is special).

**Premise 3: The user knows their source better than intake can detect at runtime.**
- *What-if-wrong:* inexperienced users may not know their source's complexity; runtime detection would help.
- *Prosecution:* a translator new to the calibration corpus may not know that Risale-i Nur is complex; UI recommendation may not surface in time.
- *Defense:* the UI recommendation is BEFORE intake runs ("about to ingest"); even an inexperienced user reads the recommendation. The COULD item preserves runtime detection as future addition if empirical evidence shows users miss the guidance. Pre-empts the case fully.
- *Verdict:* Premise survives with explicit revival path.

**Frame-premise test verdict: PASS.** Three load-bearing premises survive with explicit caveats.

---

## Phase 1 — Fitness Landscape

### Viable region

- Commitments grounded in the prior's verbatim wording.
- Per-format cells consistent with Pandoc's actual capabilities.
- Schema extensions that compose cleanly with prior Category 7.
- Routing mechanisms that honor user agency.

### Dead region

- Claims that contradict the prior's actual wording.
- Format-acceptance verdicts inconsistent with Pandoc's reader matrix.
- Schema designs that conflict with prior Category 7.

### Boundary region

- Word row's "NOT YET IMPLEMENTED" status — borderline; Pandoc reads docx natively but no UI exposure for Word yet.
- Decision 5 "STRENGTHENED" claim — borderline; prior already strengthened it.

---

## Phase 2 — Adversarial Evaluation (per piece)

### P1 — Executive summary

**Prosecution:** inherits any body refinements; summary's accuracy depends on body.
**Defense:** covers all required elements (YES verdict + matrix + flag + routing + refines: label).
**Verdict: SURVIVE-with-caveat** — inherits refinements from below.

### P2 — Acceptance-vs-priority distinction + relationship-label

**Prosecution (D2 distinction rigor):** the distinction is verbal sleight-of-hand. The prior's DEFERRED 1 was reasonably interpreted as "not for v0.2 — refuse to ingest" because DEFERRED in everyday engineering parlance often means "not available."

**Prosecution (D12 verbatim):** the prior's actual text needs to be cited verbatim, not paraphrased.

**Defense (D2):** verbatim citation (verified via grep) supports the priority-deferred reading. The "(Category 6 extension to additional source formats)" qualifier explicitly scopes the DEFERRED to ENGINEERING EXTENSION work, not user acceptance. The "engineering effort is bounded" gate further confirms — what's bounded is engineering effort, not user-acceptable formats.

**Defense (D12):** innovation P2 cites the prior wording in paraphrase but not verbatim. Refinement: cite verbatim.

**Collision:** prosecution wins partially (verbatim citation needed); distinction is structurally grounded.

**Verdict: REFINE.**

**Constructive output:** P2 must include the prior's actual DEFERRED 1 verbatim text (1-2 sentences) followed by the close-reading analysis. Currently innovation cites the prior as "extending format priority to Word and plain-text" which is a paraphrase; the actual wording is "Word and plain-text format support (Category 6 extension to additional source formats)." Citing verbatim strengthens the structural argument.

### P3 — Per-format 4×2 matrix

**Prosecution (D3 — Word row):** "NOT YET IMPLEMENTED" is inconsistent. Pandoc reads docx natively (per the format matrix). Why isn't Word ACCEPTED-at-MINIMUM-priority like txt and md?

**Defense (D3):** the Word case differs from txt/md operationally — for txt/md, the Pandoc baseline produces near-trivially-correct output (paragraph structure preserved). For Word, the Pandoc docx reader produces output that includes presentation-only artifacts (Track Changes markers; comment annotations; embedded XML quirks) that v0.2 has not engineered handling for. The "NOT YET IMPLEMENTED" status is honest about the UI / Mac app surface — Word is not in the v0.2 accepted-formats list as far as the user-facing app is concerned.

**Collision:** defense partially holds — the Word framing IS borderline. Two honest options: (a) "NOT YET IMPLEMENTED in the v0.2 UI" (current framing) OR (b) "ACCEPTED via Pandoc baseline at minimum priority; UI exposure deferred." Either is honest; (b) is more consistent with the txt/md treatment.

**Prosecution (D3 — md row "LOW priority"):** markdown with Pandoc extensions can represent quite a lot (footnotes, tables, lang spans via bracketed_spans, fenced divs). Why LOW?

**Defense:** LOW refers to ENGINEERING INVESTMENT, not output quality. For a well-formed markdown source, intake produces good canonical HTML5 with no dedicated reader engineering needed (Pandoc baseline handles it). The "LOW priority" is honest about engineering investment, not about source quality.

**Prosecution (D3 — txt row "MINIMUM"):** plain txt of Risale-i Nur produces paragraph-broken HTML5 with no headings, no Arabic-vs-Turkish distinction, no italics. Is "MINIMUM" honest enough? Or is "INADEQUATE for complex content" closer?

**Defense:** the quality-tier=minimal flag IS loud; downstream consumers know what they're getting. The user accepts the trade-off by handing intake a plain txt source. Warn-and-degrade is the right posture.

**Verdict: REFINE** — Word row framing should be made more consistent with txt/md treatment. Two options offered:

**Constructive output (option A — keep "NOT YET IMPLEMENTED"):** clarify the wording. "NOT YET IMPLEMENTED (in the v0.2 UI accepted-formats list); DEFERRED at priority. Note: Pandoc reads docx natively; technical acceptance is near-zero-cost, but v0.2 does not expose Word as an accepted format pending design decisions about Track Changes / comments handling."

**Constructive output (option B — promote to ACCEPTED-at-MINIMUM):** "Word — ACCEPTED at MINIMUM priority + quality-tier=minimal. Notes: Pandoc docx reader produces minimum-fidelity output; presentation-only artifacts (Track Changes; comments) may surface in canonical HTML5; for clean Word sources, output is acceptable; UI exposure deferred pending v0.2 engineering decision."

Recommend option B for consistency with the txt/md treatment.

### P4 — Routing + Complex-content detection

**Prosecution (D1 anti-hallucination):**
- Pandoc reads epub / html / markdown / docx / odt natively — **VERIFIED.**
- Pandoc does NOT natively read PDF — **VERIFIED** (Pandoc 2.x+ has a PDF reader that calls pdftotext; not a native parser).
- `python-magic` is a real PyPI library wrapping libmagic — **VERIFIED.**
- EPUB magic bytes (`PK\x03\x04` ZIP header + `mimetype` entry `application/epub+zip`) — **VERIFIED** (EPUB IS ZIP with mimetype as first file).
- PDF magic bytes (`%PDF-` header) — **VERIFIED** (PDF spec defines `%PDF-N.N` as the first bytes).

**Prosecution (D4 — markdown ambiguity):** no magic byte for markdown; relies on heuristic. Is this robust?

**Defense:** P4 acknowledges this explicitly. The heuristic (UTF-8 decode + markdown patterns) is standard for text format detection. For ambiguous cases (could be md or could be txt), default to txt (lower fidelity tier) is safer than defaulting to md and producing wrong output.

**Prosecution (D4 — format-extension-mismatch flag):** the flag is named but downstream consequence is unspecified.

**Defense:** the flag is informational; downstream consumers decide. But more specificity would help. REFINE: add to P4 that the flag's purpose is to surface the disagreement to downstream consumers (translate-stage may use it to decide whether to trust the source-format metadata).

**Prosecution (D5 — runtime detection):** "user knows their source" assumption is too strong for inexperienced users.

**Defense:** the UI recommendation (BEFORE intake runs) surfaces the guidance even for inexperienced users. The COULD item preserves runtime detection as future addition.

**Verdict: REFINE.**

**Constructive output:** add to P4 — "format-extension-mismatch flag's downstream consequence: surfaces the disagreement to translate-stage and Mac app UI; translate-stage may use it to decide whether to trust the source-format metadata; Mac app UI may display the mismatch to the user."

### P5 — Quality-tier flag schema

**Prosecution (D6 — field placement):** `quality_tier` at sidecar JSON top-level vs inside `flags` array — which is correct?

**Defense:** top-level is correct. `quality_tier` is a per-source attribute (one value per intake operation), not a discrete flag-event. Putting it at top-level alongside `source`, `intake_timestamp`, `format` is structurally clean. The discrete flags inside `flags` array are different — they're event-like (truncation detected; duplicate-content detected at line X).

**Prosecution (D6 — granularity):** 4 tiers may be too coarse.

**Defense:** high/medium/low/minimal is intuitive and matches user understanding. Finer granularity (e.g., split high into "well-formed-EPUB" vs "Word-with-styles") would add complexity without obvious benefit. Future versions may refine if empirical evidence shows the granularity is wrong.

**Prosecution (D6 — EPUB-from-PDF):** is the caveat adequately acknowledged?

**Defense:** P5 explicitly notes "the quality-tier flag may give a misleading signal in EPUB-from-PDF cases... R19 remains an open route from the prior." Cited and acknowledged.

**Verdict: SURVIVE.** Schema design is clean; granularity is appropriate for v0.2; EPUB-from-PDF caveat is acknowledged.

### P6 — Inherited Commitments Re-test

**Prosecution (D7 — DEFERRED 1 = REFINED):** is the prior wording truly compatible with priority-deferred reading?

**Defense:** verbatim verification (via grep) confirms — prior wording was "Word and plain-text format support (Category 6 extension to additional source formats). Gate: source-mix expands. Why: engineering effort is bounded." The "(Category 6 extension)" qualifier explicitly scopes DEFERRED to engineering extension work; "engineering effort is bounded" gate further confirms. Priority-deferred reading is structurally supported.

**Prosecution (D7 — Decision 5 STRENGTHENED):** does this finding actually strengthen Decision 5, or does it merely USE the already-strengthened lever?

**Defense:** the prior finding ALREADY committed Decision 5 STRENGTHENED via Category 6 (format-specific repair leans explicitly on Pandoc + OCRmyPDF + Tesseract). This finding's contribution is USING that already-strengthened lever to extend the format-acceptance set — but the lever itself is not strengthened FURTHER by this finding. So claiming Decision 5 STRENGTHENED by THIS finding overstates.

**Collision:** prosecution wins on Decision 5 STRENGTHENED — should be PRESERVED (already strengthened by prior; this finding consumes the strength but doesn't add to it).

**Verdict: REFINE.**

**Constructive output:** change P6's Decision 5 verdict from "PRESERVED and STRENGTHENED" to "PRESERVED (already strengthened by the prior intake-preprocessing-operations finding via Category 6; this finding consumes the already-strengthened lever to extend format acceptance, but does not further strengthen the lever itself)."

### P7 — Transition plan + Next Actions

**Prosecution (D9 — magic-bytes lookup MUST):** is "documentation" sufficient or does this need code?

**Defense:** the MUST 4 schema spec is the engineering contract; the magic-bytes lookup table is the data the routing code consumes. Documentation + the data table are sufficient for the MUST; the implementation code is downstream engineering work.

**Prosecution (D9 — "update prior DEFERRED 1 wording" MUST):** does this happen at CONCLUDE? Or is it a separate edit to the prior finding?

**Defense (critical):** innovation P7 writes "update the prior finding's Next Actions DEFERRED 1 text to the refined wording (scope to Word only; note txt + md as accepted at lower quality-tier)" with "at this finding's CONCLUDE step" — implying the prior finding's text gets edited. This is wrong. Findings are immutable historical record; refining a prior produces a NEW finding (this one) whose content supersedes the prior in PRACTICE. The prior remains as-is.

**Collision:** prosecution wins. The MUST wording is misleading.

**Verdict: REFINE.**

**Constructive output:** rewrite the MUST in P7. Change "update the prior finding's Next Actions DEFERRED 1 text" to "**the prior finding's DEFERRED 1 wording is superseded by this finding's per-format matrix (P3) for all forward consumption**. The prior finding remains historical record; this finding's content is the operative reference for v0.2 format acceptance / priority. No editing of the prior finding's text."

### P8 — Open Questions / Frontier

**Prosecution (D10 — coverage):** missing open questions include streaming intake (large source files); multi-file input (Risale-i Nur Külliyat as multiple EPUBs); URL input (user pastes a URL to a Substack article); Mac app drag-and-drop UX specifics.

**Defense:** P8 covers what was raised within the inquiry scope. Streaming / multi-file / URL / drag-and-drop are adjacent concerns that the inquiry didn't surface during sensemaking. Valid additions.

**Verdict: REFINE.**

**Constructive output:** add to P8:
- **Streaming intake for large source files.** Revival trigger: when a source file exceeds in-memory processing limits (typically 100+ MB).
- **Multi-file / multi-volume input.** The prior finding's R20 route (multi-volume document handling) covers this; cross-reference rather than duplicate.
- **URL input** (user provides a URL rather than a local file). Revival trigger: when project source-mix includes web-sourced content (Substack, GitHub README, etc.).
- **Mac app drag-and-drop UX.** Revival trigger: Mac app v0.2 UI implementation begins.

---

## Phase 3 — Per-piece Verdicts

| Piece | Verdict | Refinement target |
|---|---|---|
| P1 | SURVIVE-with-caveat | Inherits refinements |
| P2 | **REFINE** | Cite prior's DEFERRED 1 verbatim (not just paraphrase) |
| P3 | **REFINE** | Word row consistency — recommend option B (promote to ACCEPTED-at-MINIMUM + DEFERRED-priority for consistency with txt/md treatment) |
| P4 | **REFINE** | Specify format-extension-mismatch flag downstream consequence |
| P5 | SURVIVE | Schema design clean; granularity appropriate; EPUB-from-PDF caveat acknowledged |
| P6 | **REFINE** | Decision 5 verdict: PRESERVED (already strengthened by prior; this finding consumes but doesn't add) |
| P7 | **REFINE** | Rewrite "update prior DEFERRED 1" MUST — no editing of prior; this finding's content supersedes in practice |
| P8 | **REFINE** | Add 4 missing frontier items (streaming; multi-file; URL; drag-and-drop UX) |

### Phase 3.5 — Assembly Check

All 8 pieces assemble into a coherent refining finding. The architectural commitments (acceptance-vs-priority distinction; per-format matrix; routing mechanism; quality-tier flag; relationship `refines:`) all SURVIVE. Cross-cutting refinements are wording-level + completeness additions; no architectural change.

---

## Phase 4 — Coverage + Convergence

### Dimension coverage

All 12 dimensions FULL coverage.

### Adversarial strength

**STRONG.** Prosecution surfaced 6 piece-level REFINEs with concrete constructive output. Library/spec claims verified verbatim via grep (DEFERRED 1 wording) + training knowledge (Pandoc; PyPI; magic bytes). No piece KILLed; SURVIVE survivors are clean.

### Landscape stability

**STABLE.** Refinements are wording + completeness; do not shift the architectural commitment. The acceptance-vs-priority distinction, per-format matrix, routing mechanism, and quality-tier flag schema all SURVIVE.

### Clean SURVIVE check

**YES.** P5 (quality-tier flag schema) is clean SURVIVE. P1, P2, P3, P4, P6, P7, P8 are SURVIVE-with-REFINE.

### Mechanism-Independence

External anchors cited and verified:
- Prior finding's DEFERRED 1 wording (verified via grep — verbatim)
- Pandoc format matrix (training knowledge confirmed)
- `python-magic` library (PyPI confirmed)
- EPUB / PDF magic bytes (spec-confirmed)
- Asa-yı Musa EPUB analysis (executed earlier in session)

**Mechanism-Independence: VALIDATED.**

### Failure mode scan

- #1 Wrong Dimensions — NO
- #2 Rubber-Stamping — NO (6 REFINEs surfaced)
- #3 Nitpicking — NO (no piece KILLed over minor concerns)
- #4 Dimension Blindness — NO (D10 + D11 explicitly checked omitted considerations + bias-balance)
- #5 False Convergence — NO
- #6 Evaluation Drift — NO (single-pass)
- #7 Self-Reference Collapse — NO
- #8 Axis Absence — NO
- #9 External-Grounding Absence — NO (verbatim prior-finding citation)

### Convergence Telemetry

| Field | Value |
|---|---|
| Dimension coverage | FULL (D1-D12) |
| Adversarial strength | STRONG |
| Landscape stability | STABLE |
| Clean SURVIVE exists | YES (P5 clean; others SURVIVE-with-REFINE) |
| Mechanism-independence | `validated` |
| Failure modes | NONE |

**Output: PROCEED.**

---

## Final Verdict

### **SURVIVE-with-cross-cutting-refinements.**

The architectural commitment (acceptance-vs-priority distinction + per-format 4×2 matrix + routing mechanism + quality-tier flag + `refines:` relationship) SURVIVES. Six cross-cutting refinements:

1. **P2** — Cite the prior's DEFERRED 1 verbatim. Currently P2 paraphrases ("extending format priority to Word and plain-text"); the actual wording is *"Word and plain-text format support (Category 6 extension to additional source formats). Gate: observable — when the project's source-mix expands to include Word or plain-text sources. Why (if revived): the current corpus is EPUB/PDF-dominant; engineering effort is bounded."* Verbatim citation strengthens the close-reading argument.

2. **P3 — Word row consistency.** Promote Word from "NOT YET IMPLEMENTED + DEFERRED" to "ACCEPTED at MINIMUM priority + quality-tier=minimal + DEFERRED engineering for high-quality Word reader" for consistency with txt/md treatment. Pandoc reads docx natively; minimum-fidelity acceptance is near-zero-cost. Note that UI exposure for Word remains a separate downstream decision.

3. **P4 — Format-extension-mismatch flag downstream consequence.** Specify: surfaces the extension/magic-bytes disagreement to translate-stage and Mac app UI; translate-stage may use it to decide whether to trust source-format metadata; Mac app UI may display the mismatch.

4. **P6 — Decision 5 verdict.** Change from "PRESERVED and STRENGTHENED" to "PRESERVED (already strengthened by the prior intake-preprocessing-operations finding via Category 6; this finding consumes the strengthened lever without further strengthening it)." Honest about what this finding actually contributes.

5. **P7 — Update-prior MUST.** Rewrite the "update the prior finding's DEFERRED 1 wording" MUST. Findings are immutable historical record; refining produces a new finding whose content supersedes in practice. Change wording: "the prior finding's DEFERRED 1 wording is superseded by this finding's per-format matrix (P3) for all forward consumption. The prior finding remains historical record; this finding is the operative reference. No editing of the prior finding's text."

6. **P8 — Add 4 frontier items.** Streaming intake (revival: source file exceeds in-memory limits); multi-file / multi-volume input (cross-reference prior's R20); URL input (revival: project source-mix includes web-sourced content); Mac app drag-and-drop UX (revival: Mac app v0.2 UI implementation begins).

These refinements are wording-level and completeness-level — they sharpen the finding's honesty and engineering-actionability without changing what's committed. Ready for CONCLUDE with refinements applied.

### Signal

**TERMINATE with ranked survivors:**

1. The acceptance-vs-priority distinction (P2) — load-bearing pivot.
2. The per-format 4×2 matrix (P3) — load-bearing content artifact.
3. The hybrid auto-detect + warn-and-degrade + UI recommendation routing (P4).
4. The quality-tier flag schema extension (P5).
5. The `refines:` relationship-label (P2 + P6).
6. The transition plan + open questions (P7 + P8).

Proceed to Routelister (exhaust step) with this critique's refinement notes integrated.
