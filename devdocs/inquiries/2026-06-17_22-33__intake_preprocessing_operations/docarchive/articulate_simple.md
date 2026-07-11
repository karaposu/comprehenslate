# articulate_simple — intake preprocessing operations

## User Input

```
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

---

## Stage 1 — Itemize

**count:** 1

**items:**

- **I1:** "In addition to NFC normalization + paratext stripping, intake should also detect natural semantic boundaries (chapters / subchapters / sub-sub-chapters / sub-sub-sub-chapters — depth ~4 is enough); also: what other preprocessing operations can we creatively think of?"

**Keep-together rationale.** The two clauses (the structural-boundary-detection proposal + the open-ended "what else, be creative" enumeration request) share one deliverable shape: an enumeration of preprocessing operations beyond the NFC + paratext baseline, with structural boundary detection as one explicitly-named candidate. The conjunction "and" extends the generative scope rather than introducing a different deliverable. The user's instinct ("be creative") frames both as one generative pass.

Asymmetric-failure bias toward keep-together preserves the user's framing; if late evidence reveals two items, Deconstruct will flag a late-split signal.

---

## Stage 2 — Meta-questions + MQA (Item I1)

### MQ1 (verdict-axis): What is the user asking for?

**Answer (identified-ambiguities-list):**

- *Decision-mode of the deliverable:* `[enumerate-creative-list (open-ended brainstorm prioritizing breadth over commitment) / commit-to-a-recommended-set (decide which operations intake should ship with in v0.2) / evaluate-the-named-candidate-only (adjudicate structural boundary detection on its own; defer the broader brainstorm) / classify-operations-by-cost-vs-value-axis (organize the design space without picking winners) / interrogate-the-preprocessing-vs-classification-boundary (use the brainstorm as a probe of where intake's scope ends)]`
- *Depth-of-boundary-detection acceptance:* `[accept-user's-depth-4-framing-as-given / examine-whether-4-is-the-right-depth (could be 2 / 3 / 5 depending on corpus)]`

### MQ2 (context-need axis): What context does the response need?

**Answer (identified-ambiguities-list):**

- *verdict (need-to-know facts):*
  - intake's current narrowed scope per the most recent conversation: "leave content unclassified; trust the LLM" — does this rule out operations that could be classification-adjacent (like detecting structural markers via class-tagging)?
  - the just-finished canonical-format finding's commitments (NFC + paratext are already named; what's the baseline this inquiry extends?)
  - the project's actual source-format mix (EPUB? PDF? Word? other?) — preprocessing operations differ per source format
  - the calibration corpus (Risale-i Nur)'s specific structural features versus generic-corpus features — should preprocessing operations be cross-corpus generic or corpus-specific?
  - the v0.2 engineering budget / time horizon — do we ship a minimal pipeline now or invest in a richer one?
- *kinds (categories of preprocessing operations to consider):*
  - text-level cleanup (NFC, whitespace normalization, character/encoding mapping, dash/quote/ellipsis normalization)
  - structural detection (chapter / section / heading hierarchy detection; list and table block detection; quote block detection; verse-block detection)
  - paratext-and-non-body removal (running headers / footers / page numbers / catchwords / publisher boilerplate — already named in the user's prior NFC+paratext baseline)
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

### MQ3 (intent-axis, WHAT): What is the user trying to accomplish?

**Answer (identified-ambiguities-list):**

- `[populate-the-preprocessing-design-space (see options before deciding what v0.2 ships with) / commit-to-a-final-preprocessing-pipeline-spec (close the question) / extend-the-prior-NFC+paratext-baseline-additively (add on top of what's already named) / interrogate-the-preprocessing-vs-classification-boundary (probe where intake's scope ends; surface the gray zone)]`

### MQ4 (boundary-axis): What is the user explicitly excluding?

**Answer (identified-ambiguities-list):**

- `[classification-work-OUT — per the just-narrowed scope: "leave content unclassified; trust the LLM"]`
- `[per-element-provenance-OUT — deferred per the just-finished post-repair canonical format finding]`
- `[the-7-schema-policy-detection-OUT — deferred per the same scope narrowing]`
- `[translation-pipeline-design-OUT — preprocessing is intake-stage only; translate-stage is downstream]`
- `[PDF-text-extraction-tooling-design-OUT — preprocessing operates on extracted text/markup; the PDF→text problem is its own concern]`
- `[the-canonical-format-choice-OUT — already settled in the prior inquiry; this inquiry doesn't re-open the HTML5/markdown question]`

### MQA — Meta-question Alignment

**Verdict:** **surface** — two irreducible overlaps.

**Overlap 1 — Decision-mode joint axis.** MQ1's `enumerate / commit / evaluate-named-only / classify / interrogate` ambiguity, MQ3's `populate-design-space / commit-to-pipeline / extend-baseline / interrogate-boundary` ambiguity, and MQ2's stance axis `decisive vs exploratory` all span the same underlying axis: what kind of move is the user asking for? The joint axis is identifiable (decision-mode), but the partition is not crisp — `commit-to-a-recommended-set` and `commit-to-a-final-preprocessing-pipeline-spec` are nearly the same; `enumerate-creative-list` and `populate-the-design-space` are nearly the same; `interrogate-boundary` could pair with either. Reconciling would collapse the variants; surfacing preserves them.

**Overlap 2 — Scope-of-preprocessing joint axis.** MQ2's stance `minimal-intake-aligned vs ambitious`, MQ3's `interrogate-preprocessing-vs-classification-boundary`, and MQ4's NOT-list (`classification OUT`, `7-policy detection OUT`) all span the question of WHERE preprocessing ends. The user's "be creative" instinct in tension with the just-narrowed "minimal intake" scope is the irreducible content of this overlap. The downstream pipeline must navigate this tension explicitly.

---

## Stage 3 — Deconstruct + MultiDepth (Item I1)

### Deconstruct

- **deliverable:** an enumeration of preprocessing operations + (per the decision-mode ambiguity) possibly an adjudicated recommended subset for v0.2 intake; specifically includes a verdict on whether structural-boundary detection (depth ~4) belongs.
- **kinds:** comparative catalog of candidate operations + per-operation light cost/value assessment + (conditional on decision-mode) an adjudicated subset recommendation.
- **bounds:** intake-stage preprocessing operations only; before classification work; before translate-stage; doesn't touch the canonical-format choice (HTML5 vs markdown) which is already settled.

**Late-split check:** the Deconstruct tuple is single. The "enumerate" + "evaluate structural-boundary-detection" pair is two faces of one deliverable (a comparative catalog where boundary-detection is one named entry). No late-split signal fires.

### MultiDepth

**Literal-statement (verbatim restatement):**
> "I agree we should have these 2 steps [NFC + paratext stripping], but maybe also we should detect natural semantic boundaries of the text? For example new chapter or subchapter or sub-sub-chapter or sub-sub-sub-chapter (this is deep enough I think). And what other preprocessing operations can we think of? Be creative."

**Identified-purpose-motivation-ambiguities (WHY-axis):**

- `[the-just-narrowed-intake-scope-feels-too-narrow — the user is sensing intake might be doing too little after the "leave content unclassified" decision and wants to put SOMETHING more back in without crossing into classification]`
- `[scope-setting-for-v0.2-engineering — wanting to know what to build]`
- `[structural-boundary-detection-feels-like-an-obvious-gap — the user named it specifically because it strikes them as a missing essential]`
- `[the-creative-brainstorm-instinct — the user explicitly says "be creative"; wanting expansive rather than minimalist thinking; wanting to surface operations they haven't considered]`
- `[design-space-exploration-before-commitment — wanting to see the field before committing]`
- `[testing-my-thinking-against-richer-options — collaborative ideation; check whether my "minimal intake = just NFC + paratext" was complete or impoverished]`
- `[the-translation-quality-floor-might-need-more-than-minimal — preprocessing operations that AREN'T classification but DO improve downstream LLM translation quality (e.g., sentence segmentation; correct quotation marks) might be load-bearing for quality even in minimal-intake mode]`

---

## Stage 4 — Rephrase (Item I1)

**Composition sources:**
- Deconstruct deliverable-shape: comparative enumeration + per-op assessment + optional adjudication.
- Identified-ambiguities aggregated: decision-mode (generate/commit/extend/interrogate); depth-of-boundary-detection acceptance; scope-of-preprocessing (minimal vs ambitious); per-format vs format-agnostic; creative-bias vs comprehensive-bias.
- MQ4 NOT-list: classification work / per-element provenance / 7-policy detection / translation design / PDF-extraction tooling / canonical-format choice.
- Substrate: warm — just-finished post-repair canonical format finding (HTML5 canonical, NFC + paratext as named cleanup ops); the very recent "leave content unclassified; trust the LLM" scope narrowing; project is GENERIC translation with Risale-i Nur as calibration corpus (per `project_scope.md` memory).

### Considered Articulations

1. **Generative breadth-first brainstorm.** "Enumerate broadly — be creative, surface the full space of preprocessing operations that intake could include beyond NFC + paratext stripping. Include structural boundary detection (depth ~4) as one named candidate among many. The output is a catalog organized by category (text-level / structural / linguistic / metadata / hygiene / etc.), not a recommendation. Commitments come later."

2. **Recommended v0.2 minimal-extended pipeline.** "Decide which preprocessing operations intake's v0.2 should ship with. Anchor on the NFC + paratext baseline. Evaluate structural boundary detection on the merits. For each additional candidate operation, render verdict: include / defer. Output is a recommended pipeline spec."

3. **Probe the preprocessing-vs-classification boundary.** "Use structural boundary detection as a test case for where intake's scope ends. If chapter detection is preprocessing, why not section-class detection? Where exactly is the line between cleanup-and-structuring (intake) and per-element classification (deferred)? Surface other operations that live in the gray zone."

4. **Just adjudicate structural boundary detection.** "Address the named candidate directly — should intake detect chapter / subchapter / sub-sub / sub-sub-sub hierarchies, or not? If yes, with what algorithm and what depth? Defer the broader 'what else creative' brainstorm to a separate inquiry."

5. **Cost-value-scope 2D map of operations.** "For each candidate operation (named + brainstormed), tag with three axes: cost (low/med/high implementation effort); value (low/med/high quality impact for translation); scope-fit (inside-minimal-intake / on-boundary / inside-classification-territory). Output is a 2D space the user can navigate, not a recommendation."

---

## Statement-Level Bundle

- **Itemize count:** 1
- **Per-item identifiers:** `[I1]`
- **MQA verdict:** surface (two irreducible overlaps — decision-mode joint axis + scope-of-preprocessing joint axis)
- **Considered articulations count for I1:** 5

---

## LAYER 1 Self-Check

| Mode | Description | Fire? |
|---|---|---|
| 1 | Premature Itemize split | not fired |
| 2 | Late-detected multi-item case | not fired |
| 3 | MQ extension violates bounded-extensibility | not fired |
| 4 | Per-operation firing missed | not fired |
| 5 | MQ2 answer missing preparation content (verdict/kinds/stance) | not fired |
| 6 | MQ2 identified-ambiguities missing kinds or stance axis | not fired |
| 7 | 2-shape violation (commitment at MQ or MultiDepth position) | not fired |
| 8 | AMBIGUITY-NATURE conflation (WHY at MQ3 or WHAT at MultiDepth) | not fired |
| 9 | Considered-articulations drift outside composition bounds | not fired |

**Self-check result:** zero fires. Bundle is clean. Friction during execution: low (input was clear; ambiguities were perceivable across all axes; substrate from the prior canonical-format finding + the very-recent scope-narrowing message was directly applicable).

---

## Self-Assessment Verdict

**HIGH-PROCEED**
