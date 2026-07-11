# Branch: document intake handling concepts

## Source Input

```text
okay for now lets stop dealing with the appification and focus on document intake , which is a real painpoint
lets start by identifying list of intake handling concepts we need to figure out, 

for example in pdfs formatting can be really bad, and maybe they should be converted to md file first? but md file has limitations and maybe we should use rtf as standard intake format along with md for complicated texts
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** `[I1]`
- **Verdict:** HIGH-PROCEED
- **Flagged conditions (if any):** none

## Question

**Item I1 — Identify a list of intake-handling concepts that need to be figured out for document intake (in comprehenslate's pipeline).**

Literal statement (from MultiDepth, near-verbatim):
> *"Identify a list of intake-handling concepts that need to be figured out for document intake."*

The Question carries **two open verdict-axis ambiguities (MQ1)** about what kind of list is being asked for:

1. *List-shape per entry* — `[enumeration-only / enumeration-plus-brief-definitions / enumeration-plus-prioritization / enumeration-plus-tentative-resolutions]`.
2. *Territory bound* — `[scope-to-v0.x-pipeline / scope-to-full-product-lifetime / scope-to-comprehenslate-as-translation-product / scope-to-document-intake-as-an-abstract-domain]`.

And **four open intent-axis ambiguities (MQ3)** about action-endpoint shape:

1. *enumerate-for-future-deepening* — list seeds sub-inquiries on each concept.
2. *enumerate-for-current-decision* — pick the intake-format standard now using this list.
3. *enumerate-for-checklist* — each concept becomes an engineerable subtask in v0.2+.
4. *enumerate-for-architecture-foundation* — the list shapes intake-layer design.

These ambiguities are **identified, not adjudicated**. The downstream pipeline operates over the Considered Articulations set, not over a chosen reading.

## Goal

For Item I1:

**Deliverable shape (from Deconstruct):**

- **deliverable:** a list-shaped artifact enumerating concepts.
- **kinds:** named concepts, each with brief framing (one-line motivation + decision-needed flag, depending on stance).
- **bounds:** document intake — the file-to-corpus stage of comprehenslate's pipeline, before translation begins. Excludes the Mac-app's UI surface and the translation-stage internals.

**Motivations a good answer might serve (WHY-axis, from MultiDepth — preserved as ambiguities, not collapsed):**

- `[unblock-real-painpoint]` — PDF intake quality is a current obstacle; this enumeration breaks the obstacle into perceivable pieces.
- `[avoid-architecture-debt]` — picking an intake-format standard now prevents downstream rework; the list helps choose deliberately rather than ad-hoc.
- `[scope-the-engineering-task]` — the list bounds what v0.2+ needs to build; without it, intake-work is unbounded.
- `[meta-reframe]` — away-from-app-UI back-to-product-fundamentals; the list re-grounds the project in its actual painpoint after a session of UI work.

**Context the downstream consumers need (MQ2 — preserved as ambiguities):**

- *verdict (need-to-know facts):* `[scope-of-document-types-in-play (PDFs / EPUBs / DOCX / .txt / scans / HTML); definition-of-intake (file-to-text vs file-to-structured-text vs file-to-segmented-corpus); intake-quality-target (structure-preserving vs typography-preserving vs semantic-only); calibration-corpus-fit (Risale-i Nur scripture-style verses + marginalia)]`.
- *kinds (concept-categories the list might span):* `[format-layer (PDF, RTF, md, EPUB, DOCX, plain text) / structure-layer (chapter, paragraph, footnote, marginalia, embedded poetry, formulaic openings, verses) / pipeline-layer (parse, normalize, segment, validate, hand-off-to-chunking) / quality-layer (fidelity, lossiness, round-trippability, human-review gate)]`.
- *stance (curation posture):* `[research-breadth-scan vs engineering-pragmatic-prune; authoritative-prescriptive vs exploratory-open]`.

**Negative spec — what would explicitly fail (MQ4 exclusions):**

- `[appification-out]` — answers about the Swift Mac app UI surface, picker shapes, or Xcode/SwiftUI structure are out-of-scope. *"Stop dealing with the appification"* is a hard boundary for this inquiry.
- `[translation-step-internals-out]` — answers about translate / chunk / output stages are out-of-scope; the inquiry is about INTAKE specifically.
- `[current-Xcode-session's-work-is-NOT-the-substrate]` — intake is a different problem space than the app's UI/state.

## Considered Articulations

**Item I1 — Identify a list of intake-handling concepts that need to be figured out for document intake:**

1. **Format-layer-leaning · enumerate-for-current-decision.** *"Enumerate the document-intake formats comprehenslate must accept and the format-conversion concepts (PDF → md fidelity, md limitations, RTF richness handling, plain-text fallback) needed to pick a standard intake-format right now."*

2. **Structure-layer-leaning · enumerate-for-architecture-foundation.** *"Enumerate the document-structure concepts (chapter, paragraph, footnote, marginalia, embedded poetry, formulaic openings, verses, source-apparatus) that intake must perceive and preserve before any downstream translation can honor them — the list shapes how intake-layer is architected."*

3. **Pipeline-layer-leaning · enumerate-for-checklist.** *"Enumerate the pipeline-stage concepts that intake comprises (parse, normalize, segment, validate, hand off to chunking) so each becomes an engineerable subtask in v0.2 onward, with no architectural rework needed once they ship."*

4. **Cross-layer breadth · enumerate-for-future-deepening.** *"Enumerate document-intake concepts spanning format, structure, pipeline, and quality layers — producing a concept-list that seeds future deep-dive inquiries on each, rather than committing to any one layer's reading right now."*

5. **Pragmatic-painpoint-leaning · enumerate-for-current-decision.** *"Enumerate the document-intake concepts that are CURRENT obstacles to comprehenslate's pipeline (PDF formatting fidelity, md richness vs RTF complexity, scripture-style verse handling, marginalia preservation) so the immediate next decision (pick intake-format standard) is made deliberately."*

## Scope Check

**Question covers goal.** The Question asks for a concept-list; the Goal specifies the list's shape, the motivations a good list serves, the context categories the list must span (format / structure / pipeline / quality), and the exclusions (appification, translation-step-internals). All Goal facets are inflected aspects of the same Question — no widening needed.

**Specific-vs-pattern check:** the user's substrate examples are specific (PDF, md, RTF — the format-layer). The Question itself is broader (*"list of intake handling concepts"*). The pattern is: **the inquiry addresses the BROADER pattern of intake-handling concepts**, not just the PDF/md/RTF triad. The specific examples illustrate the *kind* of concept; the answer must span the kinds-axis (format / structure / pipeline / quality) per MQ2. The variants in Considered Articulations explicitly preserve this — variant 1 is format-only, variants 2–4 expand to other layers, variant 5 is pragmatic-mixed.
