# Branch: multi-format intake acceptance

## Source Input

```text
i think during intake we accpet txt, md, pdf, epub files all 3.  But for complex text formattings such as multiple multi alpahbet texts etc, epub should be chosen. this makes sense?
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-18_10-35__multi_format_intake_acceptance/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** `[I1]`
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**Item I1 — Should intake accept txt + md + pdf + epub (all four; user wrote "all 3" but listed four — transcription preserved) input formats, with EPUB chosen when the source has complex text formatting (multiple multi-alphabet texts etc.)?**

Literal statement (from MultiDepth, verbatim):
> *"I think during intake we accept txt, md, pdf, epub files all 3. But for complex text formattings such as multiple multi-alphabet texts etc., epub should be chosen. This makes sense?"*

The Question carries **two open verdict-axis ambiguities (MQ1)** about what kind of response is being asked for:

1. *Kind of validation:* `[validate-the-proposal-as-correct (yes/no) / refine-the-proposal (yes with adjustments) / overturn-prior-finding's-format-priority (the just-finished inquiry committed EPUB-first + PDF-fallback with txt/md/Word DEFERRED) / clarify-what-"chosen"-means (user selects? intake auto-routes? error-out on non-EPUB?)]`.
2. *Number-of-formats discrepancy:* `[four-formats-is-intended ("3" is transcription typo) / three-of-these-four / different-three]`.

And **five open intent-axis ambiguities (MQ3)** about action-endpoint:

1. *Validate mental model* — checking if understanding matches what the architecture supports.
2. *Propose update to format-priority* — revise the just-completed finding's DEFERRED 1.
3. *Clarify routing mechanism* — how does intake decide what to do per source format?
4. *Design the user-facing format policy* — what does the user see when they hand intake a file?
5. *Formalize the EPUB-preference intuition* — codify the heuristic as architecture-level policy.

The **MQA reconciliation** surfaces **two irreducible overlaps:**

- **Decision-mode joint axis** (joint across MQ1, MQ3, and MQ2's stance): what kind of response does the user want — validate / refine / overturn / clarify / design? The partition is not crisp; near-duplicates exist across the axes. Downstream pipeline navigates the surface.
- **Routing-mechanism joint axis** (joint across MQ1's "what 'chosen' means," MQ3's "clarify-routing-mechanism," MQ2's kinds-axis options): how does the system decide what to do per source format — user-selects? auto-detect by extension? warn-and-degrade? error-out? The user's question is implicit about this; the inquiry must commit a position.

## Goal

For Item I1:

**Deliverable shape (from Deconstruct):**

- **deliverable:** an adjudicated yes/no answer to the user's proposal + clarification of (a) the 3-vs-4 discrepancy, (b) what "chosen" means operationally (the routing mechanism), and (c) the relationship to the just-finished finding's format-priority + DEFERRED 1 (Word + plain-text deferred).
- **kinds:** validation answer + routing-mechanism clarification + (conditional on decision-mode) refinement of the prior finding's format-acceptance characterization.
- **bounds:** input-format-acceptance policy for intake; doesn't touch canonical format (HTML5 settled); doesn't touch classification (deferred); doesn't touch the 8-category recommended set (settled).

**Motivations a good answer might serve (WHY-axis, from MultiDepth — preserved as ambiguities, not collapsed):**

- `[the-just-narrowed-format-priority-feels-too-narrow]` — the just-finished inquiry deferred txt/md/Word/plain-text; user now articulating that txt + md + pdf + epub should be first-class accepted.
- `[wanting-the-Mac-app-to-accept-any-text-source]` — practical concern about what the user can drop into intake.
- `[wanting-clarity-on-routing-mechanism]` — when user gives complex source as plain text, what happens?
- `[wanting-the-EPUB-preference-formalized]` — codify the intuition that EPUB is best for complex content.
- `[testing-my-understanding-of-the-architecture]` — checking if mental model matches.
- `[scope-expansion-vs-clarification]` — is this expanding intake's accepted set, or clarifying that all 4 are already acceptable in some form?
- `[honoring-user-agency]` — the user may have a source in any format; intake shouldn't reject arbitrarily.

**Context the downstream consumers need (MQ2 — preserved as ambiguities):**

- *verdict (need-to-know facts):*
  - the just-completed inquiry's format-priority commitment (EPUB-first + PDF-with-OCR-fallback; Word + plain-text DEFERRED 1 with revival trigger "source-mix expands").
  - the prior canonical-format finding's source-format handling.
  - what "complex text formattings such as multiple multi-alphabet texts" maps to operationally.
  - how the routing decision is made (user names format? auto-detect from extension + magic bytes? error-out on insufficient-fidelity?).
  - the distinction between "accepted formats" and "priority formats" — the prior never said txt/md were UNACCEPTABLE; they were DEFERRED-PRIORITY.
- *kinds (categories of format-policy responses):*
  - all-formats-accepted-equal-treatment
  - per-format-quality-tier (EPUB high; PDF medium; md low-structural; txt lowest)
  - source-quality-driven routing (EPUB-from-PDF gets PDF treatment regardless of extension)
  - user-warning-on-format-choice (intake works on all 4 but flags fidelity warnings)
  - reject-non-EPUB-for-complex-content (hard error)
  - implicit accept-all-but-priority-tier (the just-finished finding's actual position)
- *stance:*
  - decisive yes/no on user's proposal
  - refining (yes with adjustments)
  - rejecting-prior-commitment (revising DEFERRED 1)
  - accepting-prior-commitment-with-clarification
  - design-space-exploration

**Negative spec — what would explicitly fail (MQ4 exclusions):**

- `[the-canonical-format-choice-OUT]` — HTML5 settled in prior canonical-format finding; this is INPUT formats, not output canonical.
- `[classification-work-OUT]` — per recent scope narrowing.
- `[publishing-stage-design-OUT]` — publishing is downstream.
- `[translation-pipeline-design-OUT]` — translate-stage is downstream.
- `[Word-(.docx)-format-OUT]` — user named txt/md/pdf/epub; Word omitted; implicit exclusion implies Word stays DEFERRED.
- `[the-8-category-recommended-set-OUT]` — categories settled; this is about which source formats feed the pipeline.

## Considered Articulations

**Item I1 — Should intake accept txt + md + pdf + epub all four, with EPUB chosen for complex content?**

1. **Validate the user's mental model with adjustments.** "Confirm the architecture supports accepting txt + md + pdf + epub as intake input formats; clarify that EPUB-preference under complex content is the right heuristic; the just-finished finding's DEFERRED 1 was about the engineering effort to BUILD high-quality readers for Word + plain-text, not about REJECTING txt/md at intake. Update the prior finding's wording to distinguish 'accepted formats' (all 4) from 'priority formats' (EPUB + PDF for v0.2 engineering effort)."

2. **Refine the format-priority commitment.** "Promote txt + md from DEFERRED to first-class accepted formats; EPUB remains the recommended format for complex content; txt + md are accepted with explicit quality-tier semantics — best when source is simple prose; flag-and-degrade when source has features txt/md can't structurally represent. Update DEFERRED 1 to apply only to Word (.docx)."

3. **Design the routing mechanism for the 4 accepted formats.** "Specify HOW intake routes per source format: EPUB → Category 6 EPUB path; PDF → Category 6 PDF path; md → Pandoc markdown reader + Categories 1-5 + 7; txt → Categories 1 + 2 + 4 + 7 only (no structural detection possible from plain text; flag the limitation). 'EPUB chosen for complex content' becomes 'EPUB is the source-format with the highest structural fidelity; intake reads any of 4 but flags structural-fidelity warnings when source format under-represents the content.'"

4. **Just answer 'yes' to the validation with structural caveats.** "Yes — your mental model is correct: intake should accept all 4 formats; EPUB is the right choice for complex content because EPUB preserves structure (headings, footnotes, italic/bold, embedded language spans). The just-completed finding's DEFERRED 1 specifically named Word + plain-text as DEFERRED; clarify whether 'plain-text' included txt and md and explain why this finding's framing differs."

5. **Surface a quality-tier framing for format acceptance.** "Reframe as a quality-tier: (a) EPUB = highest fidelity for complex content; (b) PDF = lower fidelity but recoverable via OCR + bidi-fix + italic recovery; (c) md = good for clean prose but cannot represent some structural features; (d) txt = lowest fidelity (no structural info; only Categories 1 + 2 normalization applicable). All 4 accepted; EPUB recommended for complex content; quality-tier flag emitted at intake-time."

## Scope Check

**Question covers goal.** The Question asks for validation of the user's format-acceptance proposal; the Goal specifies the deliverable shape (validation + routing-clarification + conditional refinement), the motivations a good answer serves (just-narrowed-feels-too-narrow / Mac-app-acceptance / routing-clarity / EPUB-preference-formalized / mental-model-test / scope-expansion / user-agency), the context categories (kinds-axis on format policies), and the exclusions (canonical format / classification / publishing / translation / Word / 8-category set). All facets are inflected aspects of the same format-acceptance question.

**Specific-vs-pattern check:** the user named four specific input formats (txt + md + pdf + epub) and one specific condition (complex text formatting). The inquiry should address **both the named formats AND the broader pattern** of input-format-acceptance policy (e.g., what about RTF? Office Open XML beyond .docx? scanned-image-only PDFs?). The user's explicit non-mention of Word — combined with the prior finding's DEFERRED 1 listing Word + plain-text — is itself a signal that Word stays deferred while txt/md are being promoted. The downstream pipeline must surface this distinction.

## Synthesis Trigger

This inquiry's substrate includes commitments from one recent prior — the intake-preprocessing-operations finding that just concluded:

- `devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/finding.md` — committed:
  - 8-category preprocessing set anchored by "structural, not semantic" scope-line.
  - Format priority: EPUB-first + PDF-with-OCR-fallback for v0.2.
  - DEFERRED 1: Word + plain-text format support, with revival trigger "project source-mix expands."
  - Two-layer corpus model.

The CONCLUDE step will require an `## Inherited Commitments Re-test` section in the finding. Sensemaking and Critique should re-test:
- Whether DEFERRED 1's "Word + plain-text" should be SPLIT (txt + md promoted to accepted; Word stays DEFERRED).
- Whether the format-priority commitment (EPUB-first + PDF-fallback) needs to extend to include explicit txt/md acceptance.
- Whether the routing-mechanism (auto-detect by extension + magic bytes; warn-and-degrade for fidelity gaps) is consistent with the prior finding's spec.

This is a **refines:** synthesis trigger — the just-finished finding's DEFERRED 1 wording is being refined (splitting txt + md from Word + plain-text), not overturned.
