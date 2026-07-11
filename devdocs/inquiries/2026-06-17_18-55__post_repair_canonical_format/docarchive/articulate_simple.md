# articulate_simple — post-repair canonical format

## User Input

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

---

## Itemize

- **count:** 1
- **items:** `[I1]`

Reasoning: paragraphs 1-5 of the input are substrate (a reframe of the prior inquiry the user is responding TO), not work-items. The user's actual ask is one cohesive question: *"given that repair is a precondition, what document type holds the repaired result?"* The two clauses ("we should repair the sources" + "what document type for the result") are tightly coupled — repair is the precondition; format is the question. The three named candidates (EPUB / markdown / HTML) are alternatives within the question, not separate items. Keep-together holds.

- **I1 — text:** *"Given that intake-side repair (OCR for broken/missing Arabic, style recovery, structure detection) is a precondition that we accept, what document format holds the repaired/reconstructed result — EPUB, markdown, HTML, or something else?"*

---

## Per-item bundle

### Item I1 — Post-repair canonical format

#### Stage 2 — Meta-questions + MQA

**MQ1 (verdict-axis) — what is the user asking for?**

Answer shape: **identified-ambiguities-list**.

- `[final-format-pick (commit to ONE: EPUB / markdown / HTML / other) / comparative-tradeoff-analysis (lay out options + their costs) / re-litigation-of-prior-Decision (the prior committed Pandoc-AST-as-JSON; the user names different candidates and doesn't mention AST-JSON) / spec-for-the-format (define the format's contract, not just name it)]`
- `[narrow-to-the-three-named-candidates (EPUB / markdown / HTML only) / open-to-broader-set (including the prior's AST-JSON, custom format, TEI, etc.)]`

**MQ2 (context-need axis) — what context does the response need?**

Answer shape: **identified-ambiguities-list** with verdict / kinds / stance sub-axes.

- **verdict (need-to-know facts):**
  - Does the user implicitly REJECT the prior's Pandoc-AST-as-JSON answer by not naming it? Or are they listing common formats and AST-JSON is still implicitly on the table?
  - What does the user mean by "document type"? — a surface human-readable format (EPUB / markdown / HTML are all surface formats) OR something more abstract (data structure / schema like JSON-AST)?
  - What does "hold that information" mean — storage-on-disk OR translate-stage-input OR publishing-output OR all of the above?
  - Given the reconstruction pipeline produces rich content (Arabic spans + italic/bold styling + structural markers + apparatus collections + paratext-stripped body), what does that content REQUIRE the format to support?
  - Did the user see the prior inquiry's verdict (three-format layered architecture)? Are they asking IT to be re-tested, or asking a fresh question?

- **kinds (categories of candidate format):**
  - `[surface-markup formats (markdown / HTML / xhtml / Pandoc-md-superset)]`
  - `[packaged-book formats (EPUB 2/3, FB2, BITS)]`
  - `[serialization formats (JSON-AST, custom AST, YAML-doc)]`
  - `[scholarly XML (TEI, DocBook, JATS)]`
  - `[layered architectures (multi-format like the prior's three-format)]`

- **stance (curation posture):**
  - decisive (pick now) vs exploratory (lay out options)
  - skeptical of prior verdict vs open to confirming
  - single-format vs multi-format-layered
  - the prior's AST-JSON as default-still-correct vs prior's AST-JSON as open-to-revision

**MQ3 (intent-axis, WHAT) — what is the user trying to accomplish?**

Answer shape: **identified-ambiguities-list**. WHAT-axis = action-endpoint.

- `[pick-the-right-format-given-new-evidence (the empirical PDF evidence about reconstruction-being-heavy reshapes the answer) / understand-what-each-candidate-format-can-hold (catalog the trade-offs) / verify-or-overturn-prior-Decision (the prior verdict on canonical format) / commit-to-a-storage-format-decision (close the question definitively)]`.
- `[end-result-as-on-disk-canonical-for-intake / end-result-as-translation-input / end-result-as-publishing-output / end-result-as-all-of-above (collapsing the layered architecture back to one)]`.

**MQ4 (boundary-axis) — what is the user explicitly excluding?**

Answer shape: **identified-ambiguities-list**.

- `[repair-pipeline-design-is-OUT (the user said "we can use OCR like things for repair even" — granting repair as a given, not asking how to do it)]`.
- `[the-prior-intake-concepts-inquiry's-other-commitments-stand (Decisions 2-5 from the prior: quality target, IntakeDoc shape, 7-policy split, Pandoc+OCR lever — this inquiry is about the format-choice scope only)]`.
- `[PDF-text-extraction-as-its-own-problem-OUT (the user previously named "pdftext extraction is another issue")]`.
- `[the-Mac-app-UI-still-OUT (inherited)]`.

**MQA — Meta-question alignment**

Examine overlaps.

The strongest joint axis is **decision-mode**: MQ1's "final-format-pick / comparative / re-litigation / spec-for-format" and MQ3's "pick-given-new-evidence / understand / verify-or-overturn-prior / commit" both span the same axis with values:
- `[re-affirm-prior-verdict (Pandoc-AST-as-JSON still wins given the new reconstruction-is-heavy reframe — the rich reconstructed content needs explicit-tree storage; surface formats lose information)]`
- `[overturn-prior-with-a-different-named-candidate (the user names EPUB / markdown / HTML as candidates — one of them substitutes)]`
- `[restate-prior-architecture-with-sharper-rationale (the three-format layered architecture stands but its WHY changes; the user's named candidates map onto the architecture's layers)]`

A second irreducible overlap: the **temporal-layer axis** — the user's question "what document type holds the result" is ambiguous about WHICH layer (canonical vs hand-edit vs publishing). The prior committed three formats for three layers; if the user is asking about ONE layer specifically, the answer is one of the three; if asking about ALL layers, the answer is the layered architecture itself; if asking about collapsing the three layers back to one monolithic format, that's an architectural-frame challenge.

MQA emission: **surface — "the question carries two irreducible overlaps. (1) Decision-mode: re-affirm prior vs overturn with named candidate vs restate architecture. (2) Temporal-layer: the user's framing 'document type for the result' does not specify whether they mean canonical/hand-edit/publishing or all-at-once. The downstream pipeline must operate over both axes and the combinations they produce."**

#### Stage 3 — Deconstruct + MultiDepth

**Deconstruct — tuple (deliverable, kinds, bounds):**

- **deliverable:** a format decision/recommendation about post-repair document storage, given the empirical-PDF evidence about source-degradation + reconstruction-being-heavy-work. Shape depends on decision-mode value — re-affirmation argument, substitution argument, or architecture-restatement.
- **kinds:** comparative analysis of candidate formats × layer assignments + adjudicated decision + (possibly) format-spec sketch.
- **bounds:** the document-format choice for the repaired/reconstructed intake result. Excludes the repair pipeline design (OUT per user), the prior intake-concepts inquiry's Decisions 2-5 (unchanged), PDF-text-extraction (OUT), and Mac app UI (OUT).

**Late-split check:** does I1 internally feel like multiple items? No — the format question is single-deliverable; the three candidates are alternatives within it.

**MultiDepth — literal-statement:**

*"Maybe we should repair the sources before doing anything. But still — even if we repair them — what document type will be selected to hold that information? Yes we can use OCR-like things for repair, but the end result should be what? EPUB? Markdown file? HTML maybe? This is the real question."* (Near-verbatim restatement; no expansion, no reframing.)

**MultiDepth — identified-purpose-motivation-ambiguities (WHY-axis):**

Answer shape: **identified-ambiguities-list**. WHY-axis = motivation-chain.

- `[the-prior-Decision-still-doesn't-feel-final (the JSON-AST answer from the prior inquiry was technically clean but did not resolve the user's intuitive concern — the user is still asking the question)]`.
- `[the-new-empirical-evidence-changes-the-question (seeing the actual PDFs and the reconstruction work makes the format-choice feel different than the abstract prior-inquiry framing)]`.
- `[wanting-a-tangibly-readable-format (the three named candidates — EPUB / markdown / HTML — are all human-readable surface formats; this contrasts with JSON-AST which is data, not a document. The user may want a document, not data)]`.
- `[the-translation-output's-format-as-the-real-question (the user phrased the prior inquiry as "format used for translations"; perhaps they care about what the TRANSLATED text ships as, not what the intake-stage-internal canonical is)]`.
- `[publishing-considerations (EPUB is publishing-format; the user lists it first; perhaps the publishing layer is the actually-important layer for them and the other layers are implementation detail)]`.
- `[scope-the-engineering-task (knowing the format scopes what the engineer builds; the user wants a commitment they can act on)]`.

#### Stage 4 — Rephrase (considered articulations)

Composition sources:
- Deconstruct deliverable-shape: a format decision/recommendation.
- Identified ambiguities (post-MQA): **decision-mode** axis with values `[re-affirm-prior / overturn-with-named / restate-architecture]`; **temporal-layer** axis with values `[canonical / hand-edit / publishing / all-layers-collapsed]`; **abstract-vs-readable-format** axis (JSON-AST data vs surface markup).
- MQ4 NOT-list: **repair-pipeline-out, prior-Decisions-2-5-stand, PDF-extraction-out, Mac-app-UI-out**.
- Substrate: warm — the prior canonical-format inquiry's three-format layered architecture (AST-JSON / markdown / EPUB 3); the empirical PDF evidence (Asa-yı Musa and Muhakemat); the reconstruction-is-heavy reframe; the user's framing that names EPUB / markdown / HTML specifically and does not mention JSON-AST.

Generated variants (5; floor+ side of 2-6 range; each spans a distinct axis-combination):

1. **Re-affirm prior verdict with sharper rationale.** *"The reconstruction-is-heavy reframe doesn't change the answer: Pandoc-AST-as-JSON is still the right canonical because the reconstructed content (Arabic-span-with-lang-attribute, italic-as-emphasis class-tagged, marginalia-with-position, formulaic-opening-tagged) needs explicit-tree storage. Surface formats — EPUB, markdown, HTML — all lose some of this at the canonical layer (markdown's round-trip-stable subset; EPUB's apparatus-not-first-class; HTML's class-attribute conventions vary). The prior three-format layered architecture stands; this inquiry's contribution is sharpening WHY AST-as-storage was the right strategy: because the reconstruction produces content too rich for surface storage."*

2. **Overturn prior with markdown as monolithic.** *"The empirical evidence shifts the answer: Pandoc-markdown (with the canonical extension set) IS sufficient for the post-repair result. The reconstruction pipeline produces structured content that fits Pandoc-md's primitives (footnotes for marginalia; bracketed-spans for Arabic-with-lang+dir; class attributes for emphasis; fenced divs for formulaic openings). Storing it as markdown gets human-readability and editability for free; the prior's AST-JSON was over-engineering. Three-format architecture collapses to one format with optional EPUB rendering."*

3. **Overturn prior with HTML5 + ARIA.** *"HTML5 (with semantic markup + native lang= and dir= attributes) is the right post-repair format. It is human-inspectable like markdown, supports apparatus via <aside> + <footer>, has lang/dir as first-class W3C primitives, converts cleanly to EPUB (which is xhtml under the hood) AND to PDF AND to plain web pages, and has the broadest standards-tooling ecosystem. The prior's AST-JSON was Pandoc-specific; HTML5 is web-standard and survives Pandoc deprecation."*

4. **Overturn prior with EPUB as monolithic.** *"EPUB 3 IS the right end-format: it's the publishing-ready container; the reconstructed content (chapters + apparatus + Arabic spans) maps natively; users get a publishable artifact directly. The three-layer architecture collapses to one format. The intake/translate/publish layers were over-decoupled; one format serves all three. If hand-editing is needed, EPUB unzips to xhtml + manifest."*

5. **Restate the prior architecture with the user's named candidates mapped onto its layers.** *"The reframe doesn't change the THREE LAYERS; it changes how the user's candidates MAP onto them. The user's EPUB / markdown / HTML are all SURFACE formats — they're candidates for the publishing or hand-edit layers, not for the canonical (which needs the explicit-tree structure that surface formats lack). The prior committed JSON-AST canonical + markdown hand-edit + EPUB publishing; the user's new examples confirm the assignment (EPUB → publishing; markdown → hand-edit; HTML is a candidate for either or for an additional web-output layer). The answer is the prior architecture, restated with the new reconstruction-is-heavy evidence as load-bearing justification, plus possibly an HTML output layer added."*

---

## Statement-level fields

- **Itemize count:** 1
- **Per-item identifiers:** `[I1]`
- **Self-assessment verdict:** **HIGH-PROCEED**

LAYER 1 self-check (single LIGHT pass):

| # | Mode | Fire? |
|---|---|---|
| 1 | Premature Itemize split | not-fire |
| 2 | Late-detected multi-item case | not-fire |
| 3 | MQ extension violates bounded-extensibility | not-fire |
| 4 | Per-operation firing missed | not-fire |
| 5 | MQ2 answer missing preparation content | not-fire (verdict / kinds / stance all present) |
| 6 | MQ2 missing kinds-axis or stance-axis | not-fire |
| 7 | 2-shape violation | not-fire (every MQ + MultiDepth emits identified-ambiguities-list) |
| 8 | AMBIGUITY-NATURE conflation | not-fire (MQ3 WHAT-axis = action-endpoint; MultiDepth WHY-axis = motivation) |
| 9 | Considered-articulations drift outside composition bounds | not-fire (all 5 variants respect deliverable + ambiguities + NOT-list + substrate) |

Zero LAYER 1 fires. Perceived friction: **moderate** — the question is structurally clean but two irreducible overlaps were surfaced at MQA (decision-mode axis × temporal-layer axis), which means the downstream pipeline operates over a two-dimensional ambiguity space, not a one-dimensional one. The five variants honor both dimensions.

Verdict: **HIGH-PROCEED**.
