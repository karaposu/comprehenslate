# Sensemaking — multi-format intake acceptance

## User Input

Source: `_branch.md`. Upstream outputs: `articulate_simple.md` + `surfacing.md`. CONTINUES FROM: prior intake-preprocessing-operations finding (which committed EPUB-first + PDF-fallback for v0.2 with Word + plain-text DEFERRED 1).

Sensemaking adjudicates 5 frontier flags from surfacing: decision-mode; routing-mechanism; "plain-text" disambiguation; complex-content detection; acceptance-vs-priority load-bearing potential.

---

## SV1 — Baseline Understanding

The user proposed: intake accepts txt + md + pdf + epub (4 formats; wrote "all 3" — transcription typo), and EPUB should be chosen for complex text formattings (multi-alphabet content etc.). The prior finding committed EPUB-first + PDF-fallback with Word + plain-text DEFERRED. Question: does the user's proposal make sense, and how does it compose with the prior commitment?

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- The prior intake-preprocessing-operations finding committed EPUB-first + PDF-with-OCR-fallback as the v0.2 format priority.
- DEFERRED 1 named "Word + plain-text format support" with revival trigger "project source-mix expands."
- HTML5 canonical commitment is settled (prior canonical-format finding); not re-opened.
- The 8-category preprocessing pipeline is settled; not re-opened.
- Classification work is deferred per the recent scope narrowing; not re-opened here.
- Pandoc reads txt, md, html, epub, docx natively (Decision 5 from original intake-concepts finding).
- The user is a translator working with Risale-i Nur sources; the practical Mac app concern is what files they can drop into intake.

### Key insights

- **The user's question and the prior finding can both hold** if there's a distinction between "accepted format" (intake reads it; produces canonical HTML5) and "priority format" (engineering invests in high-quality reader). The prior's DEFERRED was about priority, not acceptance.
- **Pandoc-as-architectural-lever already supports all 4 user-named formats** (txt as degenerate paragraph-broken text; md natively; HTML5/EPUB natively; PDF via OCR + Category 6 PDF path). The architecture doesn't need to expand to accept the 4 formats; it already does.
- **The "EPUB chosen for complex content" intuition is correct** because EPUB has the highest structural fidelity for multi-alphabet + apparatus-rich + structurally-deep content. This is a quality-tier observation, not a routing decision.
- **The prior finding's DEFERRED 1 wording ("Word + plain-text") conflated** what is genuinely deferred (engineering effort for high-quality Word reader; structure-recovery for plain text beyond Categories 1+2+4+7) with what was always implicitly accepted (Pandoc handles txt + md natively at baseline).
- **The user's question IS the revival trigger** named in DEFERRED 1's ("project source-mix expands"). The trigger fires not because the source-mix expanded externally, but because the user is articulating that the source-mix naturally includes md + txt as inputs even at v0.2.

### Structural points

- Two distinct concepts: **acceptance** (binary: accept / refuse) and **priority** (gradient: engineering investment level).
- Two distinct mechanisms: **routing** (how intake decides what to do per source format) and **fidelity flagging** (how intake communicates quality-tier downstream).
- The Mac app's UI surface is the natural place for the "EPUB recommended for complex content" guidance — soft recommendation, not enforcement.

### Foundational principles

- Honor user agency: intake should not reject sources arbitrarily; warn-and-degrade is the conservative posture.
- Composition over replacement: extend the prior finding's Category 7 quality-flag mechanism rather than introducing a parallel scheme.
- Pandoc-as-architectural-lever already supports format breadth; expansion is configuration, not architecture.
- Asymmetric-failure: under uncertainty about format acceptance, prefer accept-with-flag over reject-at-door (intake refusing a user's file is high-friction; intake processing with a quality flag is low-friction).

### Meaning-nodes

- **Acceptance-vs-priority distinction** — the structural pivot that resolves the user's question.
- **Quality-tier flag** — the operational mechanism that surfaces fidelity to downstream consumers.
- **Routing mechanism** — how the system decides what to do (auto-detect by extension + magic bytes).
- **Complex-content detection** — what counts as "complex" and how it's communicated (documentation + UI guidance, not runtime auto-detection).

---

## SV2 — Anchor-Informed Understanding

The user's question is answered by surfacing the acceptance-vs-priority distinction: the prior finding's DEFERRED 1 was about priority-deferred (where engineering invests), not acceptance-deferred (what intake refuses). All 4 user-named formats ARE accepted at intake; EPUB + PDF are the v0.2 priority targets for engineering investment; txt + md are accepted with lower quality-tier (Pandoc-native baseline; some structural features unrepresentable); Word stays DEFERRED at the priority level (no high-quality Word reader effort for v0.2). The "EPUB chosen for complex content" intuition is correct as a quality-tier observation, communicated via UI recommendation + Category 7 quality-tier flag.

---

## Phase 2 — Perspective Checking

### Technical / logical

The Pandoc architectural lever already reads all 4 user-named formats. txt is a degenerate Pandoc input (Pandoc reads it as paragraph-broken text; no structure recoverable). md is Pandoc's primary input format; structure reachable via Pandoc extensions (footnotes; tables; lists; fenced divs for class; bracketed_spans for lang=). PDF is the special case requiring Category 6 PDF path (bidi-fix; OCR; italic recovery). EPUB is the cleanest path. From a logical-implementation standpoint, accepting all 4 is essentially free (Pandoc already handles them).

**New anchor:** acceptance of all 4 is implementation-free given the existing architectural lever.

### Human / user

The user is a translator handing intake source files. They may have a clean publisher EPUB (best case); a PDF (only-format-available case); a markdown document (often the case when working with web-sourced texts); a plain text dump (rare but possible). Refusing any of these forces the user to convert externally before using the app, which is a friction the project shouldn't impose for v0.2.

**New anchor:** user-agency principle supports accept-with-flag over refuse-at-door.

### Strategic / long-term

The acceptance-vs-priority distinction extensibly handles future format additions (RTF, FB2, etc.) without architectural change. Word's continued DEFERRED status is consistent — Word reader engineering effort isn't justified yet by the project's source-mix.

**New anchor:** the distinction provides a clean evolution path for format support.

### Risk / failure

What can go wrong:
- **Accepting txt at intake but producing wrong canonical HTML5** because the structural detection has nothing to work with — risk of bad output. Mitigation: quality-tier flag is loud; user knows their source's quality tier.
- **User assumes EPUB-level quality from a plain-text source** — risk of disappointed expectations. Mitigation: UI recommendation + Category 7 flag.
- **EPUB-from-PDF (low quality EPUB) being accepted at high-fidelity assumption** — risk noted in prior critique; the prior finding's EPUB-from-PDF detection heuristics (now Open Question 19 in the prior's R19 route) handle this.

**New anchor:** quality-tier flag is the primary risk mitigation.

### Resource / feasibility

Implementation cost is low — Pandoc lever already supports the formats; quality-tier flag extends an existing Category 7 mechanism; UI recommendation is one Mac app message. No new engineering category needed.

### Frame-exit completeness

Gating predicate: this inquiry's commitments will inherit terms from the prior finding (acceptance / priority / DEFERRED). Multi-value test: yes, the inquiry uses these terms at multiple levels (per-format acceptance verdict; per-format priority tier; per-format DEFERRED status).

**Existence enumeration on "acceptance":** project-wide referents include (a) intake-stage acceptance (input format the intake reads); (b) translate-stage acceptance (what the LLM-translator accepts as input — not in scope here); (c) publishing-stage acceptance (what publishing outputs — out of scope). The inquiry frame is correctly scoped to (a).

**Existence enumeration on "DEFERRED":** the prior's DEFERRED list (1 Word + plain-text; 2 cross-corpus validation; 3 classification; 4 per-corpus UI) has 4 distinct items. This inquiry only re-tests DEFERRED 1. The other 3 DEFERREDs are out of scope.

**Verdict rigor:** the strongest counter to "DEFERRED 1 wording should be split" is "leave the prior wording alone; the user's question is just a clarification request." Structurally, the prior wording IS ambiguous (does "plain-text" mean txt only, or md too, or both?); splitting clarifies. The counter fails on structural grounds.

### Phase / calibration-state

The project is pre-v0.2 (no production code; only schemas.py + UI scaffolding). The calibration corpus is Risale-i Nur. Acceptance of txt + md at v0.2 means: when a user hands intake a plain-text or markdown Risale-i Nur source, intake processes it (with quality-tier flag) rather than refusing.

**New anchor:** at this phase, acceptance has near-zero implementation cost; refusing would be over-restrictive.

---

## SV3 — Multi-Perspective Understanding

The recommended position crystallizes:

1. **Acceptance verdict:** intake accepts all 4 user-named formats (txt + md + pdf + epub). The "all 3" typo is interpreted as "all 4."
2. **Priority verdict:** EPUB + PDF are the v0.2 priority formats (engineering investment for high-quality readers + repair operations). txt + md are accepted at lower quality-tier without dedicated reader engineering (Pandoc-native baseline; some structural features unrepresentable). Word stays DEFERRED at the priority level.
3. **Routing mechanism:** hybrid auto-detect (file extension first; magic bytes verification fallback) + warn-and-degrade (process the file; emit Category 7 quality-tier flag) + UI recommendation in the Mac app ("EPUB recommended for complex content").
4. **Complex-content detection:** documentation + UI guidance only. Runtime complex-content auto-detection at intake-time is over-engineering for v0.2; the user knows their source better than intake can detect from a quick scan.
5. **Quality-tier flag:** extends Category 7 quality-flag mechanism with a `quality-tier` field. Values: `high` (EPUB; Word-with-styles); `medium` (PDF with OCR + bidi-fix; HTML); `low` (markdown with Pandoc extensions); `minimal` (plain txt).
6. **Prior finding refinement:** DEFERRED 1 wording REFINED — split into "Word format support DEFERRED" (engineering effort for high-quality Word reader is post-v0.2) and "txt + md accepted at low-to-minimal quality-tier" (Pandoc baseline; structural workarounds where possible).

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — Decision-mode (which considered articulation?)

**Strongest counter-interpretation:** the user is just asking "this makes sense?" — a YES/NO validation. Adding refinements + commitments over-engineers the response.

**Why the counter fails:** the WHY-axis ambiguities from articulation include "scope-setting for v0.2 engineering" and "wanting clarity on routing mechanism" — pure YES doesn't serve these. Validation + refinement + structural framing serves all WHY-axis motivations simultaneously. The counter underestimates the structural value of the acceptance-vs-priority distinction.

**Confidence:** HIGH. The combination of (1) validate + (2) refine + (5) quality-tier framing is the right output shape.

**Resolution:** Commit to a combination — **validate the user's mental model + refine the prior finding's DEFERRED 1 wording + commit a quality-tier framing**. The verdict is YES with structural clarification, not bare YES.

**Fixed:** deliverable shape = validate + refine + frame.
**Excluded:** bare YES; full overturn; design-routing-from-scratch.
**Depends on:** the acceptance-vs-priority distinction holding (tested in Ambiguity 6).

### Ambiguity 2 — Acceptance-vs-priority distinction

**Strongest counter-interpretation:** the distinction is verbal sleight-of-hand; "DEFERRED" in the prior wording clearly meant "not for v0.2," which is acceptance-deferred for practical purposes.

**Why the counter fails:** the prior finding's actual content (re-read directly) describes DEFERRED 1 as "extending format priority to Word and plain-text when sources expand" — note "extending priority," not "extending acceptance." The revival trigger is "project source-mix expands" — about engineering effort allocation, not about user-facing acceptance. The distinction is structurally present in the prior's actual wording; this inquiry just makes it explicit.

**Confidence:** HIGH. The distinction is grounded in the prior finding's own wording.

**Resolution:** Commit the **acceptance-vs-priority distinction** as load-bearing. "Accepted format" = intake reads it and produces canonical HTML5 output. "Priority format" = engineering investment for high-quality reader / repair operations. The prior's DEFERRED was always priority-deferred, not acceptance-deferred.

**Fixed:** the distinction holds; both prior and current commitments can coexist.
**Excluded:** treating DEFERRED as acceptance-deferred.
**Depends on:** the rest of the recommended position.

### Ambiguity 3 — Routing mechanism

**Strongest counter-interpretation:** require user to name the format at intake-time (CLI flag or UI dropdown); avoid auto-detection complexity.

**Why the counter fails:** user friction. Standard file-handling practice is auto-detect-by-extension with magic-bytes fallback; users expect this. Forcing user-names-format adds UI friction without operational benefit.

**Confidence:** HIGH.

**Resolution:** Commit **hybrid auto-detect (extension first; magic-bytes verification fallback) + warn-and-degrade (process the file; emit quality-tier flag) + UI recommendation in Mac app**.

**Fixed:** auto-detect + warn-and-degrade.
**Excluded:** hard-error rejection of non-EPUB sources; user-must-confirm.

### Ambiguity 4 — "Plain-text" disambiguation in DEFERRED 1

**Strongest counter-interpretation:** the prior wording's "plain-text" obviously meant only `.txt`; markdown was always accepted and just not named.

**Why the counter fails:** the prior finding's actual wording was "Word + plain-text format support" without distinguishing `.txt` from markdown. The reader could plausibly interpret either way. Splitting the terminology removes the ambiguity.

**Confidence:** HIGH.

**Resolution:** Commit **terminology split**: "Word format support DEFERRED" (engineering effort) + "txt + md accepted at lower quality-tier" (Pandoc-native baseline; no dedicated reader engineering). The "plain-text" wording in the prior is RETIRED in favor of this split.

### Ambiguity 5 — Complex-content detection mechanism

**Strongest counter-interpretation:** auto-detect at intake-time (scan source preview; if multi-alphabet + apparatus-rich, flag).

**Why the counter fails:** over-engineering for v0.2. The user knows their source's complexity better than intake can quickly detect. Auto-detection adds implementation cost without obvious benefit when documentation + UI guidance achieves the same outcome (the user picks the appropriate format).

**Confidence:** HIGH-MED. Future versions may add runtime detection if empirical evidence shows users miss the guidance.

**Resolution:** Commit **documentation-only + UI guidance ("EPUB recommended for complex content")**. Runtime auto-detection deferred.

### Ambiguity 6 — Acceptance-vs-priority distinction load-bearing test

**Strongest counter-interpretation:** the distinction resolves the user's question only superficially; the underlying issue (what does v0.2 actually accept?) is unresolved.

**Why the counter fails:** the distinction is operationally complete. Acceptance is binary (intake reads / refuses). Priority is gradient (engineering investment level). For each of the 4 user-named formats, both values are committed: txt = ACCEPTED + minimal-priority; md = ACCEPTED + low-priority; pdf = ACCEPTED + medium-priority (v0.2 priority target); epub = ACCEPTED + high-priority (v0.2 priority target). Word = ACCEPTED-NOT-YET-IMPLEMENTED + DEFERRED-priority (engineering for high-quality reader is post-v0.2). The 5-format × 2-axis matrix is fully specified.

**Confidence:** HIGH.

**Resolution:** The distinction is structurally load-bearing and operationally complete. Confirmed.

### Ambiguity 7 — Quality-tier flag scheme

**Strongest counter-interpretation:** introducing a new flag adds cognitive overhead; just use the existing Category 7 informational flags without a dedicated tier name.

**Why the counter fails:** the quality-tier is structurally distinct from the other Category 7 flags (truncation; suspicious-line-break; duplicate-content). Those are content-quality flags; quality-tier is format-fidelity. Naming the distinction makes the structural difference explicit. The implementation cost is one additional enum field in the flag schema.

**Confidence:** HIGH-MED.

**Resolution:** Commit **quality-tier flag as a new Category 7 field**: `quality_tier` ∈ {high, medium, low, minimal}. Composes with existing flags; extends Category 7 rather than replacing.

### Ambiguity 8 — "All 3 vs 4" transcription

**Resolution:** Treat as "all 4" with explicit acknowledgment in the finding. The user listed 4 formats; "3" is a typo. No structural impact.

---

## SV4 — Clarified Understanding

The recommended position stabilizes:

**Acceptance verdict (per format):**
- EPUB — ACCEPTED + quality-tier=high
- PDF — ACCEPTED + quality-tier=medium (with OCR + bidi-fix Category 6 path)
- markdown (Pandoc-md with extensions) — ACCEPTED + quality-tier=low
- plain txt — ACCEPTED + quality-tier=minimal
- Word (.docx) — NOT YET IMPLEMENTED for v0.2; DEFERRED at priority level

**Priority verdict (per format, for v0.2 engineering investment):**
- EPUB — HIGH priority (v0.2 target; Category 6 EPUB path)
- PDF — MEDIUM priority (v0.2 target; Category 6 PDF path with OCR + bidi-fix)
- markdown — LOW priority (Pandoc baseline acceptance; no dedicated reader engineering)
- plain txt — MINIMUM priority (Pandoc baseline acceptance; Categories 1+2+4+7 only)
- Word — DEFERRED priority (engineering effort post-v0.2)

**Routing mechanism:** hybrid auto-detect (extension first; magic-bytes verification fallback) + warn-and-degrade + UI recommendation in Mac app.

**Complex-content detection:** documentation + UI guidance only.

**Quality-tier flag:** extends Category 7 with a `quality_tier` field.

**Relationship to prior finding:** REFINES the prior finding's DEFERRED 1 wording — split "Word format support DEFERRED" (priority-deferred) from "txt + md accepted at lower quality-tier" (always-accepted via Pandoc).

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed

- Acceptance-vs-priority distinction is load-bearing.
- All 4 user-named formats are ACCEPTED at intake.
- Priority tiers: EPUB high; PDF medium; md low; txt minimal; Word DEFERRED.
- Routing = hybrid auto-detect + warn-and-degrade + UI recommendation.
- Complex-content detection = documentation + UI guidance only.
- Quality-tier flag = Category 7 extension.
- Relationship to prior = REFINES the DEFERRED 1 wording.

### Eliminated

- Hard-rejection of non-EPUB for complex content.
- Runtime auto-detection of complex content (for v0.2).
- User-must-name-format-at-intake.
- Treating DEFERRED as acceptance-deferred.
- Overturning the prior format-priority commitment.

### Viable

- The finding's body specifying per-format verdicts in a 4-format × 2-axis matrix.
- Concrete refinement of the prior finding's Next Actions where DEFERRED 1 is named.
- Open question on EPUB-from-PDF quality detection (still open; not blocking).

---

## SV5 — Constrained Understanding

The recommended position is determinate: validate the user's mental model + refine the prior finding's DEFERRED 1 wording via the acceptance-vs-priority distinction + commit a quality-tier flag. The deliverable shape combines (a) the per-format 4×2 matrix, (b) the routing-mechanism commitment, (c) the quality-tier flag schema extension, (d) the refinement to the prior's DEFERRED 1 wording.

---

## Phase 5 — Conceptual Stabilization

### SV6 — Stabilized Model

**The user's mental model is correct.** Intake accepts all four formats (txt, md, pdf, epub) — the "all 3" was a transcription typo; "all 4" is intended. EPUB is correctly identified as the right choice for complex content (multi-alphabet, embedded apparatus, structurally-deep texts).

**The user's proposal and the prior finding both hold** because the prior finding's DEFERRED 1 was about **priority** (where engineering effort goes), not about **acceptance** (what intake refuses). This acceptance-vs-priority distinction is load-bearing for this inquiry.

**The format-policy commitment (per format, for v0.2):**

| Format | Acceptance | Priority | Notes |
|---|---|---|---|
| EPUB | ACCEPTED | HIGH (v0.2 target) | Category 6 EPUB path; quality-tier=high; recommended for complex content |
| PDF | ACCEPTED | MEDIUM (v0.2 target) | Category 6 PDF path with OCR + bidi-fix; quality-tier=medium |
| markdown | ACCEPTED | LOW | Pandoc baseline; no dedicated reader engineering; quality-tier=low |
| plain txt | ACCEPTED | MINIMUM | Pandoc baseline; Categories 1+2+4+7 only; quality-tier=minimal |
| Word (.docx) | NOT YET IMPLEMENTED | DEFERRED | Engineering for high-quality Word reader post-v0.2 |

**Routing mechanism:** hybrid auto-detect (file extension first; magic-bytes verification fallback) + warn-and-degrade (process the file; emit Category 7 `quality_tier` flag) + UI recommendation in the Mac app ("EPUB recommended for best results with complex content").

**Complex-content detection:** documentation + UI guidance only. v0.2 does not perform runtime complex-content auto-detection at intake-time; the user knows their source's complexity better than intake can detect from a quick scan. (Frontier: revisit if empirical evidence shows users miss the guidance.)

**Quality-tier flag:** Category 7 informational-flag mechanism extends with a `quality_tier` ∈ {high, medium, low, minimal} field. This composes with existing Category 7 flags rather than replacing them.

**Pandoc-as-architectural-lever** (Decision 5 of the original intake-concepts finding) already supports all 4 user-named formats. EPUB and HTML5 are read natively; markdown is Pandoc's primary input format; plain txt is read as paragraph-broken text; PDF requires the existing Category 6 PDF path (Pandoc plus OCR plus bidi-fix). No new architectural lever is needed.

### Inherited Commitments Re-test

**Prior:** `devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/finding.md` (the intake-preprocessing-operations finding).

| Inherited commitment | Re-test status | Evidence |
|---|---|---|
| Format priority = EPUB-first + PDF-with-OCR-fallback for v0.2 | **RE-TESTED — commitment confirmed.** | This inquiry preserves EPUB + PDF as the priority targets for v0.2 engineering effort. |
| DEFERRED 1 = "Word + plain-text format support" with revival trigger "project source-mix expands" | **RE-TESTED — commitment confirmed but wording REFINED.** | The DEFERRED commitment held about Word (engineering for high-quality Word reader); the "plain-text" wording is REFINED to split: txt + md are ACCEPTED at lower quality-tier (always were, via Pandoc baseline); Word remains DEFERRED at the priority level. The revival trigger "project source-mix expands" is implicitly fired by this inquiry. |
| "Structural, not semantic" scope-line principle | **RE-TESTED — commitment confirmed.** | Quality-tier flag is structural format-fidelity, not semantic role tagging. Doesn't cross the scope-line. |
| 8-category preprocessing pipeline | **RE-TESTED — commitment confirmed.** | Quality-tier flag extends Category 7; no new category needed. |
| Two-layer corpus model | **RE-TESTED — commitment confirmed.** | Unchanged; format acceptance is orthogonal to corpus extensions. |
| HTML5 canonical format | **RE-TESTED — commitment confirmed.** | All 4 accepted formats produce canonical HTML5 output. |
| Decision 5 (original intake-concepts) — Pandoc + OCR architectural lever | **RE-TESTED — commitment confirmed and strengthened.** | The lever ALREADY supports all 4 user-named formats; the format-acceptance commitment is a natural extension of the lever, not an architectural addition. |

### Differences from SV1

- SV1: "the user asked a yes/no validation question."
- SV6: "the user asked a yes/no validation question; YES is correct; the answer composes with the prior commitment via the acceptance-vs-priority distinction; the prior DEFERRED 1 wording is REFINED to split Word (priority-deferred) from txt + md (always accepted)."

### Telemetry

- SV delta from SV1 to SV6: substantial (introduced acceptance-vs-priority distinction; committed per-format 4×2 matrix; committed routing mechanism; committed quality-tier flag scheme; refined prior DEFERRED 1 wording).
- Perspective saturation: 6 perspectives applied; new anchors emerged at each.
- Ambiguity resolution ratio: 8 ambiguities identified; all 8 resolved with HIGH or HIGH-MED confidence.
- Anchor diversity: anchors span all 5 types.

### Failure mode check

- Status Quo Bias — not fired (interrogated the prior wording rather than protecting it).
- Premature Stabilization — not fired (8 ambiguities resolved with explicit counter-argumentation).
- Anchor Dominance — boundary-approached. Acceptance-vs-priority distinction does heavy lifting; remove it and the position partially collapses. BUT: the routing mechanism, quality-tier flag, and Pandoc-as-lever each contribute independently.
- Perspective Blindness — not fired.
- Clean Resolution Trap — not fired (counter-arguments tested per ambiguity).
- Self-Reference Blindness — not applicable.

### Verdict

**SUBSTANTIVE VERDICT:** the user's proposal is correct. Intake accepts all 4 user-named formats (txt + md + pdf + epub); EPUB is correctly the choice for complex content. The prior finding's DEFERRED 1 wording is REFINED to clarify the acceptance-vs-priority distinction: Word remains DEFERRED at the priority level; txt + md were always accepted at lower quality-tier via the Pandoc baseline. Routing = hybrid auto-detect + warn-and-degrade + UI recommendation. Quality-tier flag extends Category 7.

**PROCEED** — ready for Decomposition.
