# Branch: intake preprocessing operations

## Source Input

```text
u said 

NFC normalization picks the canonical composed form (U+015F for ş, never U+0073 + U+0327) so that the same visible text always has the
  same bytes. Standard one-pass operation; Python's unicodedata.normalize('NFC', text) does it. Should run once on intake before anything
  else.

  Paratext stripping
  
  "Paratext" is the publishing term for everything in a book that is not the body content. Includes:

  - Running headers — the book title or chapter title repeated at the top of every page
  - Running footers — same, at the bottom
  - Page numbers — folios
  - Catchwords — older printing convention: the next page's first word printed at the bottom of the current page
  - Section markers / editorial boilerplate — "[continued]" / "[end of chapter]" insertions
  - Publisher metadata — copyright lines printed at chapter starts in some editions
  
  The problem at intake: PDF extractors don't know body from paratext. pdftotext walks the page geometrically and emits everything as a
  stream. So you get garbage like: 

  …ve bu hakikat o kadar açıktır ki herkes kabul eder.
     Asa-yı Musa
     47
     Bu nokta-i nazardan bakıldığında…

  — where "Asa-yı Musa" is the running header and "47" is the page number, both wedged in the middle of a sentence that should have run
  continuously. The body text reads as …herkes kabul eder. Bu nokta-i nazardan bakıldığında… once paratext is stripped.


i agree we should have these 2 steps, but maybe also we should detect natural sementic boundaries of the text? for example new chapter or subchapter or subsubchapter subsubsubchapter (this is deep enough i think)

and what other preprocessing operations cna be think of ? be creative
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** `[I1]`
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**Item I1 — In addition to NFC normalization + paratext stripping, what other preprocessing operations should intake include — and specifically, should structural / semantic boundary detection (chapter / subchapter / sub-sub-chapter / sub-sub-sub-chapter — depth ~4) be one of them?**

Literal statement (from MultiDepth, verbatim):
> *"I agree we should have these 2 steps [NFC + paratext stripping], but maybe also we should detect natural semantic boundaries of the text? For example new chapter or subchapter or sub-sub-chapter or sub-sub-sub-chapter (this is deep enough I think). And what other preprocessing operations can we think of? Be creative."*

The Question carries **two open verdict-axis ambiguities (MQ1)** about what kind of move is being asked for:

1. *Decision-mode of the deliverable* — `[enumerate-creative-list (open-ended brainstorm prioritizing breadth over commitment) / commit-to-a-recommended-set (decide which operations intake's v0.2 should ship with) / evaluate-the-named-candidate-only (adjudicate structural boundary detection on its own; defer broader brainstorm) / classify-operations-by-cost-vs-value-axis (organize the design space without picking winners) / interrogate-the-preprocessing-vs-classification-boundary (use brainstorm to probe where intake's scope ends)]`.
2. *Depth-of-boundary-detection acceptance* — `[accept-user's-depth-4-framing-as-given / examine-whether-4-is-the-right-depth (could be 2 / 3 / 5 depending on corpus)]`.

And **four open intent-axis ambiguities (MQ3)** about action-endpoint:

1. *Populate the preprocessing design space* (see options before deciding what v0.2 ships with).
2. *Commit to a final preprocessing pipeline spec* (close the question).
3. *Extend the prior NFC+paratext baseline additively* (add on top of what's already named).
4. *Interrogate the preprocessing-vs-classification boundary* (probe where intake's scope ends; surface the gray zone).

The **MQA reconciliation** surfaces **two irreducible overlaps:**

- **Decision-mode joint axis** (joint across MQ1, MQ3, and MQ2's stance): what kind of move is the user asking for — generative breadth-first, committal, additive, classificatory, or interrogative-of-the-boundary? The partition is not crisp; downstream pipeline must navigate the surface.
- **Scope-of-preprocessing joint axis** (joint across MQ2's stance, MQ3's intent, and MQ4's NOT-list): where does preprocessing end and classification begin? The user's "be creative" instinct is in tension with the very recent "leave content unclassified; trust the LLM" scope narrowing. This tension is the irreducible content of the overlap.

The downstream pipeline operates over both axes' product space, not over a one-dimensional decision. The variants in Considered Articulations span the load-bearing combinations.

## Goal

For Item I1:

**Deliverable shape (from Deconstruct):**

- **deliverable:** an enumeration of preprocessing operations + (per the decision-mode ambiguity) possibly an adjudicated recommended subset for v0.2 intake; specifically includes a verdict on whether structural-boundary detection (depth ~4) belongs.
- **kinds:** comparative catalog of candidate operations + per-operation light cost / value assessment + (conditional on decision-mode) an adjudicated subset recommendation.
- **bounds:** intake-stage preprocessing operations only; before classification work; before translate-stage; doesn't touch the canonical-format choice (HTML5 vs markdown) which is already settled.

**Motivations a good answer might serve (WHY-axis, from MultiDepth — preserved as ambiguities, not collapsed):**

- `[the-just-narrowed-intake-scope-feels-too-narrow]` — the user is sensing intake might be doing too little after the "leave content unclassified" decision and wants to put SOMETHING more back in without crossing into classification.
- `[scope-setting-for-v0.2-engineering]` — wanting to know what to build.
- `[structural-boundary-detection-feels-like-an-obvious-gap]` — the user named it specifically because it strikes them as a missing essential.
- `[the-creative-brainstorm-instinct]` — the user explicitly says "be creative"; wanting expansive rather than minimalist thinking; wanting to surface operations they haven't considered.
- `[design-space-exploration-before-commitment]` — wanting to see the field before committing.
- `[testing-my-thinking-against-richer-options]` — collaborative ideation; check whether my "minimal intake = just NFC + paratext" was complete or impoverished.
- `[the-translation-quality-floor-might-need-more-than-minimal]` — preprocessing operations that AREN'T classification but DO improve downstream LLM translation quality (e.g., sentence segmentation; correct quotation marks) might be load-bearing for quality even in minimal-intake mode.

**Context the downstream consumers need (MQ2 — preserved as ambiguities):**

- *verdict (need-to-know facts):*
  - intake's current narrowed scope per the most recent conversation: "leave content unclassified; trust the LLM" — does this rule out operations that could be classification-adjacent (like detecting structural markers via class-tagging)?
  - the just-finished canonical-format finding's commitments (NFC + paratext are already named; what's the baseline this inquiry extends?)
  - the project's actual source-format mix (EPUB? PDF? Word? other?) — preprocessing operations differ per source format
  - the calibration corpus (Risale-i Nur)'s specific structural features versus generic-corpus features — should preprocessing operations be cross-corpus generic or corpus-specific?
  - the v0.2 engineering budget / time horizon — do we ship a minimal pipeline now or invest in a richer one?
- *kinds (categories of preprocessing operations to consider):*
  - text-level cleanup (NFC, whitespace normalization, character / encoding mapping, dash / quote / ellipsis normalization)
  - structural detection (chapter / section / heading hierarchy detection; list and table block detection; quote block detection; verse-block detection)
  - paratext-and-non-body removal (already in the baseline)
  - metadata extraction (title / author / ISBN / chapter numbers / table-of-contents structure)
  - format-specific repair (PDF: bidi-fix / italic recovery; EPUB: CSS-presentation extraction; Word: style-mapping)
  - linguistic preprocessing (sentence segmentation; paragraph boundary detection; encoding-confidence detection)
  - apparatus separation (footnote extraction; marginalia separation; cross-reference linking)
  - quality / hygiene checks (typo / spelling-error flagging; broken-unicode detection; orphan-content detection; suspicious-line-break detection)
  - normalization-beyond-Unicode (punctuation marks; quotation-mark variants; em-dash vs en-dash vs hyphen; ellipsis as three dots vs single character; non-breaking spaces; combining-character ordering)
  - source-provenance stamping (document-level: source file path; intake timestamp; checksum; version-of-intake-code)
  - language identification (which language(s) appear; main language vs embedded spans)
- *stance (curation posture):*
  - decisive (recommend a final set) vs exploratory (lay out options without picking)
  - generic-cross-corpus vs Risale-i-Nur-tuned
  - minimal-intake-aligned (small set; defer richer ops) vs ambitious (more operations including some that edge toward classification)
  - per-format flow (different operations per source format) vs format-agnostic (uniform pipeline)
  - creative-bias (prioritize novel operations the user hasn't seen) vs comprehensive-bias (cover the textbook list)

**Negative spec — what would explicitly fail (MQ4 exclusions):**

- `[classification-work-OUT]` — per the just-narrowed scope: "leave content unclassified; trust the LLM"
- `[per-element-provenance-OUT]` — deferred per the just-finished post-repair canonical format finding
- `[the-7-schema-policy-detection-OUT]` — deferred per the same scope narrowing
- `[translation-pipeline-design-OUT]` — preprocessing is intake-stage only; translate-stage is downstream
- `[PDF-text-extraction-tooling-design-OUT]` — preprocessing operates on extracted text/markup; the PDF→text problem is its own concern
- `[the-canonical-format-choice-OUT]` — already settled in the prior inquiry; this inquiry doesn't re-open the HTML5/markdown question

## Considered Articulations

**Item I1 — In addition to NFC + paratext stripping, what other preprocessing operations should intake include — and should structural boundary detection (depth ~4) be one?**

1. **Generative breadth-first brainstorm.** "Enumerate broadly — be creative, surface the full space of preprocessing operations that intake could include beyond NFC + paratext stripping. Include structural boundary detection (depth ~4) as one named candidate among many. The output is a catalog organized by category (text-level / structural / linguistic / metadata / hygiene / etc.), not a recommendation. Commitments come later."

2. **Recommended v0.2 minimal-extended pipeline.** "Decide which preprocessing operations intake's v0.2 should ship with. Anchor on the NFC + paratext baseline. Evaluate structural boundary detection on the merits. For each additional candidate operation, render verdict: include / defer. Output is a recommended pipeline spec."

3. **Probe the preprocessing-vs-classification boundary.** "Use structural boundary detection as a test case for where intake's scope ends. If chapter detection is preprocessing, why not section-class detection? Where exactly is the line between cleanup-and-structuring (intake) and per-element classification (deferred)? Surface other operations that live in the gray zone."

4. **Just adjudicate structural boundary detection.** "Address the named candidate directly — should intake detect chapter / subchapter / sub-sub / sub-sub-sub hierarchies, or not? If yes, with what algorithm and what depth? Defer the broader 'what else creative' brainstorm to a separate inquiry."

5. **Cost-value-scope 2D map of operations.** "For each candidate operation (named + brainstormed), tag with three axes: cost (low/med/high implementation effort); value (low/med/high quality impact for translation); scope-fit (inside-minimal-intake / on-boundary / inside-classification-territory). Output is a 2D space the user can navigate, not a recommendation."

## Scope Check

**Question covers goal.** The Question asks for preprocessing-operations enumeration + the structural-boundary-detection adjudication; the Goal specifies the deliverable shape (catalog + light cost/value assessment + optional recommendation; shape depends on decision-mode), the motivations a good answer serves (scope-not-too-narrow / v0.2-engineering-scope / boundary-detection-gap / creative-instinct / design-space-exploration / collaborative-ideation / translation-quality-floor), the context categories (text-level / structural / paratext / metadata / format-specific / linguistic / apparatus / quality / normalization-beyond-Unicode / provenance / language-ID), and the exclusions (classification-OUT / 7-policy-OUT / translation-design-OUT / PDF-extraction-OUT / canonical-format-OUT). All Goal facets are inflected aspects of the same preprocessing-design question.

**Specific-vs-pattern check:** the user named one specific candidate (structural boundary detection with depth ~4) AND asked an open-ended generative question ("what other preprocessing operations can we think of? be creative"). The inquiry should address **both the named candidate AND the broader pattern** of intake preprocessing operations. The downstream pipeline operates over the union.

The depth-4 framing (sub-sub-sub-chapter) the user proposed should be honestly examined — the user said "this is deep enough I think" with a hedge; the inquiry should test whether 4 is the right depth for the calibration corpus and for generic translation use cases, or whether a different depth (2, 3, 5) fits better.

## Synthesis Trigger

This inquiry's substrate includes commitments from two prior inquiries:

- `devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/finding.md` — the post-repair canonical format inquiry's verdict (three-layer architecture; HTML5 canonical; per-element provenance and per-policy classification DEFERRED under the "leave content unclassified; trust the LLM" scope narrowing). NFC + paratext stripping were the two named cleanup operations under minimal intake; this inquiry extends that set.
- `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md` — the original intake-concepts inquiry's commitments (quality target = structure-preservation; IntakeDoc shape; Pandoc + OCR architectural lever). The Decision 2 quality target (structure-preservation) is the load-bearing inheritance for this inquiry — preprocessing operations are evaluated against whether they contribute to structure preservation.

The CONCLUDE step will require an `## Inherited Commitments Re-test` section in the finding. Sensemaking and Critique should plan to re-test:
- The "leave content unclassified" scope narrowing (very recent conversational decision, not yet codified in a finding) — does every preprocessing operation surfaced in this inquiry respect that boundary, or do some cross it?
- The Decision 2 structure-preservation quality target — does the recommended preprocessing set contribute to it?
- The post-repair canonical format finding's NFC + paratext baseline — is this inquiry extending it additively, or replacing it?
