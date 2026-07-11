# Branch: post-repair canonical format

## Source Input

```text
Here's what I had framed it as, and what it actually is.
 
  What I had framed: "Pick the canonical format intake serializes to — markdown vs RTF vs EPUB vs MOBI vs custom-AST." The three-format
  layered architecture was an answer at THAT layer. Pandoc's AST as JSON for canonical, markdown for hand-edit, EPUB for publishing. The
  user's pushback got resolved into "AST-as-storage strategy."

  What it actually is: The PDFs are the calibration corpus, and they are structurally degraded sources for the things intake needs to
  capture. Specifically: 

  - Asa-yı Musa: Arabic IS in the text layer but with broken bidi/shaping/order. pdftotext and Pandoc's PDF reader both produce garbled
  Arabic from this — letters and diacritics scattered across lines in wrong order. To get usable Arabic, intake must detect the brokenness
  and re-derive the spans via OCR (tesseract --lang ara).
  - Muhakemat: Arabic is not in the text layer at all — it's pasted as images in the Word source. pdftotext and Pandoc's PDF reader cannot
  see it. Every Bismillah opening, every embedded Hadith, every closing verse — invisible to default extraction. The Turkish text layer is
  pristine. 
  - Both: italic/bold styling is lost by default extraction. Some PDF tools can recover it (mutool draw -F text, pdf2htmlEX) but it's an
  extra pass, not automatic.
  - Both: page paratext (running headers, page numbers) gets inline-extracted as if it were body content. Has to be stripped.

  So the more precise issue is this:

  The hard part of intake is not what format we save the result to. The hard part is reconstructing a faithful representation from sources 
  where the things we care about have been lost or broken by the format conversion pipeline that produced the PDF in the first place. Arabic
  gets reduced to glyphs or images; italics drop out of the text layer; structural markers (letter-spaced "T e n b i h :", multi-title
  hierarchies, hashiye positioning) don't survive in any standard extraction. By the time we have a clean parse to serialize, the work is
  mostly done; serializing it to JSON-AST or markdown or anything else is the easy part.

yes . 

and maybe we should repair the sources before doing anything, But still question remains even if we repair them what document type will be seelcted to hold that information?  yes we can use OCR like things for repair even, but end result should be what? epub? md file ? html maybe? 

this is the real question
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-17_18-55__post_repair_canonical_format/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** `[I1]`
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**Item I1 — Given intake-side repair is a precondition, what document format holds the repaired/reconstructed result?**

Literal statement (from MultiDepth, near-verbatim):
> *"Maybe we should repair the sources before doing anything. But still — even if we repair them — what document type will be selected to hold that information? Yes we can use OCR-like things for repair, but the end result should be what? EPUB? Markdown file? HTML maybe? This is the real question."*

The Question carries **two open verdict-axis ambiguities (MQ1)** about what kind of "deep dive" is being asked for:

1. *Kind of deliberation* — `[final-format-pick (commit to ONE: EPUB / markdown / HTML / other) / comparative-tradeoff-analysis (lay out options + their costs) / re-litigation-of-prior-Decision (the prior committed Pandoc-AST-as-JSON; the user names different candidates and doesn't mention AST-JSON) / spec-for-the-format (define the format's contract, not just name it)]`.
2. *Candidate-set scope* — `[narrow-to-the-three-named-candidates (EPUB / markdown / HTML only) / open-to-broader-set (including the prior's AST-JSON, custom format, TEI, etc.)]`.

And **two open intent-axis ambiguities (MQ3)** about action-endpoint:

1. *Decision-mode* — `[pick-the-right-format-given-new-evidence (the empirical PDF evidence reshapes the answer) / understand-what-each-candidate-can-hold (catalog the trade-offs) / verify-or-overturn-prior-Decision (Pandoc-AST-as-JSON from the prior inquiry) / commit-to-a-storage-format-decision (close the question definitively)]`.
2. *Temporal-layer scope* — `[end-result-as-on-disk-canonical-for-intake / end-result-as-translation-input / end-result-as-publishing-output / end-result-as-all-of-above (collapsing the layered architecture back to one)]`.

The **MQA reconciliation** surfaces **two irreducible overlaps**:

- **Decision-mode axis** (joint across MQ1 and MQ3): `[re-affirm-prior-verdict (Pandoc-AST-as-JSON still wins) / overturn-prior-with-a-different-named-candidate (one of EPUB / markdown / HTML substitutes) / restate-prior-architecture-with-sharper-rationale (the three-format layered architecture stands but its WHY changes; the user's candidates map onto its layers)]`.
- **Temporal-layer axis** (joint across MQ1, MQ2, MQ3): the user's "document type for the result" is ambiguous about WHICH layer (canonical vs hand-edit vs publishing) OR all-collapsed.

The downstream pipeline operates over the two-dimensional product of these axes, not over a one-dimensional decision. The variants in Considered Articulations span the load-bearing combinations.

## Goal

For Item I1:

**Deliverable shape (from Deconstruct):**

- **deliverable:** a format decision/recommendation about post-repair document storage, given the empirical-PDF evidence about source-degradation + reconstruction-being-heavy-work. Shape depends on the decision-mode value — a re-affirmation argument (preserving the prior verdict with sharper rationale), a substitution argument (replacing the prior with a named candidate), or an architecture-restatement (preserving the three-layer architecture but re-mapping its layer assignments).
- **kinds:** comparative analysis of candidate formats × layer assignments + adjudicated decision + (possibly) format-spec sketch.
- **bounds:** the document-format choice for the repaired/reconstructed intake result.

**Motivations a good answer might serve (WHY-axis, from MultiDepth — preserved as ambiguities, not collapsed):**

- `[the-prior-Decision-still-doesn't-feel-final]` — the JSON-AST answer from the prior inquiry was technically clean but did not resolve the user's intuitive concern; the user is still asking the question.
- `[the-new-empirical-evidence-changes-the-question]` — seeing the actual PDFs (Asa-yı Musa with broken bidi Arabic; Muhakemat with image-only Arabic) and the reconstruction work makes the format-choice feel different than the abstract prior-inquiry framing.
- `[wanting-a-tangibly-readable-format]` — the three named candidates (EPUB / markdown / HTML) are all human-readable surface formats; this contrasts with JSON-AST which is data, not a document. The user may want a document, not data.
- `[the-translation-output's-format-as-the-real-question]` — the user phrased the earlier inquiry as "format used for translations"; perhaps they care about what the TRANSLATED text ships as, not what the intake-stage-internal canonical is.
- `[publishing-considerations]` — EPUB is publishing-format; the user lists it first; perhaps the publishing layer is the actually-important one and the other layers are implementation detail.
- `[scope-the-engineering-task]` — knowing the format scopes what the engineer builds; the user wants a commitment they can act on.

**Context the downstream consumers need (MQ2 — preserved as ambiguities):**

- *verdict (need-to-know facts):*
  - Does the user implicitly REJECT the prior's Pandoc-AST-as-JSON answer by not naming it? Or are they listing common surface formats and AST-JSON is still implicitly on the table?
  - What does the user mean by "document type" — a surface human-readable format (EPUB / markdown / HTML are all surface) OR something more abstract (data structure / schema like JSON-AST)?
  - What does "hold that information" mean — storage-on-disk OR translate-stage-input OR publishing-output OR all of the above?
  - Given the reconstruction pipeline produces rich content (Arabic spans + italic/bold styling + structural markers + apparatus collections + paratext-stripped body), what does that content REQUIRE the format to support?
- *kinds (candidate-format categories):*
  - `[surface-markup (markdown / HTML / xhtml / Pandoc-md-superset)]`
  - `[packaged-book (EPUB 2/3, FB2, BITS)]`
  - `[serialization (JSON-AST, custom AST, YAML-doc)]`
  - `[scholarly XML (TEI, DocBook, JATS)]`
  - `[layered architectures (multi-format like the prior's three-format)]`
- *stance (curation posture):*
  - decisive (pick now) vs exploratory (lay out options)
  - skeptical of prior verdict vs open to confirming
  - single-format vs multi-format-layered
  - the prior's AST-JSON as default-still-correct vs prior's AST-JSON as open-to-revision

**Negative spec — what would explicitly fail (MQ4 exclusions):**

- `[repair-pipeline-design-is-OUT]` — the user explicitly granted "OCR-like things for repair" as accepted; this inquiry is about format choice POST-repair, not about how to repair.
- `[the-prior-intake-concepts-inquiry's-other-commitments-stand]` — Decisions 2-5 from the prior intake-concepts inquiry (quality target = structure-preservation; IntakeDoc shape; 7-policy split; Pandoc+OCR architectural lever) are inherited unchanged; this inquiry is about the format-choice scope only.
- `[PDF-text-extraction-as-its-own-problem-OUT]` — the user previously named "pdftext extraction is another issue"; that exclusion stands.
- `[the-Mac-app-UI-still-OUT]` — inherited from the original intake-concepts inquiry.

## Considered Articulations

**Item I1 — Given intake-side repair is a precondition, what document format holds the repaired/reconstructed result?**

1. **Re-affirm prior verdict with sharper rationale.** *"The reconstruction-is-heavy reframe doesn't change the answer: Pandoc-AST-as-JSON is still the right canonical because the reconstructed content (Arabic-span-with-lang-attribute, italic-as-emphasis class-tagged, marginalia-with-position, formulaic-opening-tagged) needs explicit-tree storage. Surface formats — EPUB, markdown, HTML — all lose some of this at the canonical layer (markdown's round-trip-stable subset; EPUB's apparatus-not-first-class; HTML's class-attribute conventions vary). The prior three-format layered architecture stands; this inquiry's contribution is sharpening WHY AST-as-storage was the right strategy: because the reconstruction produces content too rich for surface storage."*

2. **Overturn prior with markdown as monolithic.** *"The empirical evidence shifts the answer: Pandoc-markdown (with the canonical extension set) IS sufficient for the post-repair result. The reconstruction pipeline produces structured content that fits Pandoc-md's primitives (footnotes for marginalia; bracketed-spans for Arabic-with-lang+dir; class attributes for emphasis; fenced divs for formulaic openings). Storing it as markdown gets human-readability and editability for free; the prior's AST-JSON was over-engineering. Three-format architecture collapses to one format with optional EPUB rendering."*

3. **Overturn prior with HTML5 + ARIA.** *"HTML5 (with semantic markup + native lang= and dir= attributes) is the right post-repair format. It is human-inspectable like markdown, supports apparatus via <aside> + <footer>, has lang/dir as first-class W3C primitives, converts cleanly to EPUB (which is xhtml under the hood) AND to PDF AND to plain web pages, and has the broadest standards-tooling ecosystem. The prior's AST-JSON was Pandoc-specific; HTML5 is web-standard and survives Pandoc deprecation."*

4. **Overturn prior with EPUB as monolithic.** *"EPUB 3 IS the right end-format: it's the publishing-ready container; the reconstructed content (chapters + apparatus + Arabic spans) maps natively; users get a publishable artifact directly. The three-layer architecture collapses to one format. The intake/translate/publish layers were over-decoupled; one format serves all three. If hand-editing is needed, EPUB unzips to xhtml + manifest."*

5. **Restate the prior architecture with the user's named candidates mapped onto its layers.** *"The reframe doesn't change the THREE LAYERS; it changes how the user's candidates MAP onto them. The user's EPUB / markdown / HTML are all SURFACE formats — they're candidates for the publishing or hand-edit layers, not for the canonical (which needs the explicit-tree structure that surface formats lack). The prior committed JSON-AST canonical + markdown hand-edit + EPUB publishing; the user's new examples confirm the assignment (EPUB → publishing; markdown → hand-edit; HTML is a candidate for either or for an additional web-output layer). The answer is the prior architecture, restated with the new reconstruction-is-heavy evidence as load-bearing justification, plus possibly an HTML output layer added."*

## Scope Check

**Question covers goal.** The Question asks for a format decision about post-repair storage; the Goal specifies the deliverable shape (analysis + decision/recommendation; shape depends on decision-mode), the motivations a good answer serves (prior-doesn't-feel-final / new-evidence-changes-question / wanting-readable / translation-output-focus / publishing-considerations / scope-engineering), the context categories (surface / packaged-book / serialization / scholarly XML / layered), and the exclusions (repair-out, prior-Decisions-2-5-stand, PDF-extraction-out, Mac-app-UI-out). All Goal facets are inflected aspects of the same format-choice question.

**Specific-vs-pattern check:** the user named three specific candidates (EPUB / markdown / HTML). The inquiry should address **both the specific candidates the user named AND the broader landscape** (per MQ2's kinds-axis which surfaced surface-markup + packaged-book + serialization + scholarly-XML + layered as adjacent categories). The user's explicit non-mention of JSON-AST (the prior verdict) is itself a signal that needs honest treatment — was it intentional rejection or merely omission? The downstream pipeline must surface both readings.

## Synthesis Trigger

This inquiry's primary substrate is the prior canonical-intake-format inquiry's verdict (three-format layered architecture: JSON-AST canonical + Pandoc-md hand-edit + EPUB 3 publishing), which the user is asking to be re-tested against new empirical evidence. The downstream finding's relationship to the prior should be one of:

- `refines:` — if the verdict is re-affirmed with sharper rationale (variant 1) or restated with the user's candidates mapped onto its layers (variant 5).
- `supersedes:` — if the verdict is overturned with a different monolithic format (variants 2, 3, or 4) and the three-format layered architecture is rejected.
- `corrects:` — if the prior was structurally wrong; less likely but possible.

The priors being re-tested:

- `devdocs/inquiries/2026-06-17_17-49__canonical_intake_format_deep_dive/finding.md` — the prior canonical-format inquiry's verdict (three-format layered architecture + decision-mode SUBSTITUTE + the five rejected candidates).
- `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md` — the original intake-concepts inquiry's commitments (Decisions 2-5 inherited unchanged; Decision 1 already refined by the prior canonical-format inquiry).

The CONCLUDE step will require an `## Inherited Commitments Re-test` section in the finding. Sensemaking + Critique should plan to actually re-test the prior canonical-format inquiry's verdict against the new empirical evidence (not just record the inheritance).
