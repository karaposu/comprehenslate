# articulate_simple — multi-format intake acceptance

## User Input

```
i think during intake we accpet txt, md, pdf, epub files all 3.  But for complex text formattings such as multiple multi alpahbet texts etc, epub should be chosen. this makes sense?
```

---

## Stage 1 — Itemize

**count:** 1

**items:**

- **I1:** "Should intake accept txt + md + pdf + epub all four (user wrote 'all 3' but listed four formats — transcription preserved as-is) input formats, with EPUB chosen when the source has complex text formatting (multiple multi-alphabet texts etc.)? Does this make sense?"

**Keep-together rationale.** The statement has three tightly-coupled claims: (a) intake accepts 4 specific input formats; (b) EPUB should be chosen under complex-content conditions; (c) validation request ("this makes sense?"). They share one deliverable shape: an adjudicated answer about the format-acceptance policy for intake. The three claims are facets of one proposal, not three distinct work items.

The "all 3 vs 4" discrepancy is a small transcription issue (user wrote "all 3" while listing 4 formats) — preserved verbatim; MQ1 surfaces this as an ambiguity to be addressed in the response, not as a separate item.

---

## Stage 2 — Meta-questions + MQA (Item I1)

### MQ1 (verdict-axis): What is the user asking for?

**Answer (identified-ambiguities-list):**

- *Kind of validation requested:* `[validate-the-proposal-as-correct (yes/no) / refine-the-proposal (yes with adjustments to wording or scope) / overturn-prior-finding's-format-priority (the just-finished intake-preprocessing-operations finding committed EPUB-first + PDF-fallback with txt/md/Word DEFERRED; the user is now proposing all 4 accepted) / clarify-what-"chosen"-means (does user select the format? does intake auto-route? does intake error-out on non-EPUB for complex content?)]`
- *Number-of-formats discrepancy:* `[four-formats-is-intended (txt/md/pdf/epub all 4 — "3" is transcription typo) / three-of-these-four (user means a subset of the named formats) / different-three (user named 4 but meant 3 of them)]`

### MQ2 (context-need axis): What context does the response need?

**Answer (identified-ambiguities-list):**

- *verdict (need-to-know facts):*
  - the just-completed inquiry's format-priority commitment: EPUB-first + PDF-with-OCR-fallback for v0.2; Word + plain-text DEFERRED to future format additions (trigger: project source-mix expands)
  - the post-repair canonical format finding's source-format-handling commitments
  - what "complex text formattings such as multiple multi-alphabet texts" maps to operationally — is it Arabic-in-Turkish + nested apparatus + structural hierarchy + italic/bold preservation?
  - how the routing decision is made (does user name the format at intake-time? does intake auto-detect from file extension + magic bytes? does intake error-out on insufficient-fidelity formats for complex content?)
  - the prior finding's distinction between "accepted formats" and "priority formats" — the prior never said txt/md were UNACCEPTABLE; they were DEFERRED-PRIORITY
- *kinds (categories of format-policy responses to consider):*
  - all-formats-accepted-equal-treatment (intake reads any of 4 with same pipeline)
  - per-format-quality-tier (EPUB high; PDF medium; md low-structural; txt lowest-structural; with quality-flag exposure)
  - source-quality-driven routing (EPUB-from-PDF gets PDF treatment regardless of extension; well-formed EPUB stays in EPUB path)
  - user-warning-on-format-choice (intake works on all 4 but flags when complex content + non-EPUB; e.g., "this PDF has image-only Arabic — translation quality will be lower than EPUB equivalent")
  - reject-non-EPUB-for-complex-content (hard error: refuse to ingest)
  - implicit accept-all-but-priority-tier (the just-finished finding's actual position)
- *stance (curation posture):*
  - decisive yes/no on the user's proposal
  - refining (yes with adjustments to the wording — clarify "all 3 vs 4"; clarify "chosen")
  - rejecting-prior-commitment (revising the just-finished finding's DEFERRED 1)
  - accepting-prior-commitment-with-clarification (the prior finding already implies most of this; clarify the difference between "DEFERRED priority" and "accepted format")
  - design-space-exploration (lay out routing-mechanism options)

### MQ3 (intent-axis, WHAT): What is the user trying to accomplish?

**Answer (identified-ambiguities-list):**

- `[validate-mental-model (the user is checking if their understanding matches what the architecture supports) / propose-an-update-to-format-priority (revise the just-completed finding's DEFERRED 1 — Word + plain-text deferred; user is saying actually we should accept txt + md as first-class) / clarify-routing-mechanism (how does intake decide what to do per source format?) / design-the-user-facing-format-policy (what does the user see when they hand intake a file?) / formalize-an-intuition-about-EPUB-preference (the user has an instinct that EPUB is best for complex content; wants it stated as policy)]`

### MQ4 (boundary-axis): What is the user explicitly excluding?

**Answer (identified-ambiguities-list):**

- `[the-canonical-format-choice-OUT — HTML5 settled in the prior canonical-format finding; this question is about INPUT formats, not output canonical]`
- `[classification-work-OUT — per the recent scope narrowing]`
- `[publishing-stage-design-OUT — publishing is downstream]`
- `[translation-pipeline-design-OUT — translate-stage is downstream]`
- `[Word-(.docx)-format-OUT — user named txt/md/pdf/epub specifically, omitting Word; the prior finding had Word as DEFERRED 1 alongside plain-text; user's omission of Word here implies Word stays DEFERRED]`
- `[the-8-category-recommended-set-OUT — the categories are settled; this question is about which source formats feed into the pipeline]`

### MQA — Meta-question Alignment

**Verdict:** **surface** — two irreducible overlaps.

**Overlap 1 — Decision-mode joint axis.** MQ1's `validate-the-proposal-as-correct / refine-the-proposal / overturn-prior-finding's-format-priority / clarify-routing` ambiguity, MQ3's `validate-mental-model / propose-update / clarify-routing-mechanism / design-format-policy / formalize-intuition` ambiguity, and MQ2's stance axis `decisive yes/no / refining / rejecting / accepting-with-clarification / design-space` all span the same underlying axis: what kind of response does the user want? The joint axis is identifiable (decision-mode), but the partition is not crisp — `validate-the-proposal-as-correct` and `validate-mental-model` are near-duplicates; `refine-the-proposal` and `propose-update` are near-duplicates; `accepting-with-clarification` and `clarify-routing-mechanism` are near-duplicates. Surfacing preserves the open options.

**Overlap 2 — Routing-mechanism joint axis.** MQ1's `what 'chosen' means (user selects / intake auto-routes / error-out)`, MQ3's `clarify-routing-mechanism`, and MQ2's kinds-axis `user-warning-on-format-choice / reject-non-EPUB-for-complex-content / source-quality-driven routing` all span the joint axis of HOW the system decides what to do given a source format. The user's question is implicit about this (the word "chosen" assumes some mechanism). The downstream pipeline must adjudicate.

---

## Stage 3 — Deconstruct + MultiDepth (Item I1)

### Deconstruct

- **deliverable:** an adjudicated yes/no answer to the user's proposal + clarification of (a) the 3-vs-4 discrepancy, (b) what "chosen" means operationally (the routing mechanism), and (c) the relationship to the just-finished finding's format-priority + DEFERRED 1 (Word + plain-text deferred).
- **kinds:** validation answer + routing-mechanism clarification + (conditional on decision-mode) refinement of the prior finding's format-acceptance characterization.
- **bounds:** input-format-acceptance policy for intake; doesn't touch canonical format (HTML5 settled); doesn't touch classification (deferred); doesn't touch the 8-category recommended set (settled).

**Late-split check:** Deconstruct's tuple is single. Validation + routing + conditional refinement are facets of one adjudication deliverable. No late-split signal fires.

### MultiDepth

**Literal-statement (verbatim restatement):**
> *"I think during intake we accept txt, md, pdf, epub files all 3. But for complex text formattings such as multiple multi-alphabet texts etc., epub should be chosen. This makes sense?"*

**Identified-purpose-motivation-ambiguities (WHY-axis):**

- `[the-just-narrowed-format-priority-feels-too-narrow]` — the just-finished inquiry committed EPUB-first + PDF-fallback with txt + md + Word + plain-text DEFERRED; the user is now articulating that actually we should accept txt + md + pdf + epub as the first-class input set.
- `[wanting-the-Mac-app-to-accept-any-text-source]` — practical concern about what the user can drop into the app's intake.
- `[wanting-clarity-on-routing-mechanism]` — when user gives a complex source as plain text, what happens? Does intake refuse? Process and warn? Process silently?
- `[wanting-the-EPUB-preference-formalized]` — the user has an intuition that EPUB is best for complex content (multi-alphabet; embedded apparatus); wants it codified as architecture-level policy.
- `[testing-my-understanding-of-the-architecture]` — checking if the user's mental model matches what the architecture supports.
- `[scope-expansion-vs-clarification]` — is this asking to EXPAND intake's accepted set (add txt + md as new first-class formats), or to CLARIFY that all 4 are already acceptable in some form even if not equally prioritized?
- `[honoring-user-agency]` — the user (a translator working with Risale-i Nur) may have a source in any of 4 formats; the intake stage shouldn't reject them arbitrarily.

---

## Stage 4 — Rephrase (Item I1)

**Composition sources:**
- Deconstruct deliverable-shape: validation + routing-clarification + conditional refinement.
- Identified-ambiguities aggregated: decision-mode (validate/refine/overturn/clarify/design); routing-mechanism (user-selects vs auto-routes vs error-out vs warn-and-degrade); number-of-formats (transcription clarification).
- MQ4 NOT-list: canonical format / classification / publishing / translation pipeline / Word format / 8-category set.
- Substrate: warm — just-finished intake-preprocessing-operations finding (format-priority = EPUB-first + PDF-fallback for v0.2; Word + plain-text DEFERRED 1 with revival trigger "source-mix expands"); prior canonical-format finding; the calibration corpus context (Risale-i Nur with Arabic-in-Turkish, hashiye, structural markers); project_scope memory (generic translation; Risale-i Nur as calibration corpus).

### Considered Articulations

1. **Validate the user's mental model with adjustments.** "Confirm the architecture supports accepting txt + md + pdf + epub as intake input formats; clarify that EPUB-preference under complex content is the right heuristic; the just-finished finding's DEFERRED 1 (Word + plain-text DEFERRED) was about the engineering effort to BUILD high-quality readers for those formats, not about REJECTING them at intake. Update the prior finding's wording to distinguish 'accepted formats' (all 4) from 'priority formats' (EPUB + PDF for v0.2 engineering effort)."

2. **Refine the format-priority commitment.** "Promote txt + md from DEFERRED to first-class accepted formats; EPUB remains the recommended format for complex content (multi-alphabet, embedded apparatus, structural hierarchy preservation); txt + md are accepted but with explicit quality-tier semantics — best when the source is simple prose; flag-and-degrade when source has features txt/md can't structurally represent. Update the prior finding's DEFERRED 1 to apply only to Word (.docx) format."

3. **Design the routing mechanism for the 4 accepted formats.** "Specify HOW intake routes per source format: EPUB → Category 6 EPUB path (spine reassembly + CSS-presentation extraction + OPF metadata); PDF → Category 6 PDF path (with bidi-fix + OCR fallback when needed); md → Pandoc markdown reader + Categories 1-5 + 7; txt → Categories 1 + 2 + 4 + 7 only (no structural detection possible from plain text; flag the limitation). 'EPUB chosen for complex content' becomes 'EPUB is the source-format with the highest structural fidelity; intake reads any of 4 but flags structural-fidelity warnings when source format under-represents the content.'"

4. **Just answer 'yes' to the validation with structural caveats.** "Yes — your mental model is correct: intake should accept all 4 formats; EPUB is the right choice for complex content because EPUB preserves structure (headings, footnotes, italic/bold, embedded language spans). The just-completed finding's DEFERRED 1 specifically named Word + plain-text as DEFERRED; txt is the same as plain-text DEFERRED but md was not separately addressed. Clarify whether the prior's 'plain-text' DEFERRED included txt and md (it did) and explain why this finding's framing differs."

5. **Surface a quality-tier framing for format acceptance.** "Reframe the format-policy as a quality-tier: (a) EPUB = highest fidelity for complex content (recommended for multi-alphabet, apparatus-rich, structurally-deep sources); (b) PDF = lower fidelity but recoverable via OCR + bidi-fix + italic recovery; (c) md = good for clean prose but cannot represent some structural features (footnotes via Pandoc extensions, but lang= spans are workaround); (d) txt = lowest fidelity (no structural info; only Categories 1 + 2 normalization applicable). All 4 accepted; EPUB recommended for complex content; quality-tier flag emitted at intake-time."

---

## Statement-Level Bundle

- **Itemize count:** 1
- **Per-item identifiers:** `[I1]`
- **MQA verdict:** surface (two irreducible overlaps — decision-mode joint axis + routing-mechanism joint axis)
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

**Self-check result:** zero fires. Bundle is clean. Friction during execution: low (input was clear; the prior finding's substrate was directly applicable; the 3-vs-4 transcription was preserved as an explicit ambiguity rather than silently resolved).

---

## Self-Assessment Verdict

**HIGH-PROCEED**
