---
status: active
model: claude-opus-4-7
effort: max
refines: devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md
---
# Finding: Canonical Intake Format — Three-Format Layered Architecture

## Changes from Prior

**Prior path:** devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md

**Revision trigger:** User pushback in conversation following the prior finding's publication. The user wrote, in part: *"we should focus on core representative format which will be used for translations. i was thinking rtf is good for that. md has big limitations. we need sth different maybe? maybe we need to comeup with new format even? or epub or mobi formats are good? lets dive deep on this."* The user's intuition — that markdown alone has structural limitations as a canonical — turned out to be correct, but the architectural fix is not RTF or EPUB or MOBI as a substitute format; it is to **decouple three temporal layers** (intake/translate · hand-edit · publishing) that the prior finding implicitly conflated into a single format choice.

**What's preserved:**
- All four of the prior finding's other load-bearing decisions (quality target = structure-preservation; IntakeDoc shape = tree-of-containers + cross-referenced flat collections; the 7-policy intake-perception + translate-rendering split; Pandoc + OCR as architectural lever) — unchanged or strengthened.
- The choice of Pandoc's markdown as a load-bearing format in the architecture — preserved, but in a narrower role (hand-edit format, not monolithic canonical).
- The 38 intake-handling concepts enumerated in the prior, the seven policy-perception detectors, the OCR sub-pipeline design, and the pipeline stages — all carry forward.

**What's changed:**
- The prior Decision 1 (canonical intake format = Pandoc's markdown) is **refined**, not overturned. The prior's monolithic-single-format frame is replaced by a three-format layered architecture. Pandoc's markdown remains the right choice for the hand-edit role; a new format (Pandoc's AST serialized as JSON) takes the canonical intake/translate role; a new layer (EPUB 3) is added for publishing.
- The intake stage's on-disk output format: was Pandoc's markdown; **now JSON-serialized Pandoc AST**.
- The seven policy-perception detector specs from the prior finding now reference Pandoc AST node types rather than markdown surface signals. Structural intent unchanged; spec wording refined.

**What's new:**
- A publishing-layer commitment (EPUB 3) that the prior implicitly deferred.
- A formal three-temporal-layer architecture (intake/translate · hand-edit · publishing) that the prior implicitly conflated.
- Explicit rejections, on structural grounds, of RTF, TEI, MOBI, EPUB-as-intake-canonical, and custom-format-design.

**Migration:** v0.2 has not been built yet. No engineering migration is required — the architectural commit changes BEFORE engineering begins.

---

## Question

The user, mid-conversation about document intake, surfaced a concrete pushback on the prior finding's Decision 1: markdown felt limiting; was RTF or EPUB or MOBI or a new format the right canonical instead? The literal ask was *"lets dive deep on this."* The user's substrate examples named four specific candidates (RTF, EPUB, MOBI, "new format") and an intuition that markdown's limitations matter for translations.

The goal as articulated in `_branch.md` is to produce an analysis + decision/recommendation about the canonical intake format, with three plausible decision-modes left open: **validate-prior** (the prior choice survives stronger prosecution), **re-decide-with-existing-alternative** (swap markdown for RTF, EPUB, MOBI, or another existing format), or **design-new-format** (no existing format fits; build one). The motivations a good answer might serve include the user's pushback being honored as a real signal, richer source-fidelity than markdown surface-syntax delivers, avoiding architecture debt before engineering starts, matching the calibration corpus's richness (Risale-i Nur's marginalia, embedded poetry, mixed Turkish-Arabic content, formulaic openings), and considering publishing downstream of intake. Explicitly out of scope: PDF text extraction (the user named it as a separate issue), the Mac app UI, and the translation-stage internals (inherited from the prior inquiry).

---

## Finding Summary

- **The canonical intake format question has three answers**, not one. The prior finding's monolithic-single-format frame was structurally wrong; the right frame is that "canonical" splits into three temporal layers, each with different optimal trade-offs.

- **F1 — canonical intake + translate format = Pandoc's AST serialized as JSON.** Lossless round-trip via Pandoc (`pandoc -t json` / `pandoc -f json`); the in-memory `IntakeDoc` is the deserialized AST; pure data; queryable; explicit-tree storage that does not have markdown's round-trip-stable-subset issue.

- **F2 — hand-edit format = Pandoc's markdown** (with the canonical extension set from the prior finding: footnotes, pipe tables, definition lists, citations, YAML metadata blocks, raw attribute, bracketed spans). The prior Decision 1's choice is **preserved** in this narrower role; users hand-edit markdown and Pandoc round-trips with the JSON canonical.

- **F3 — publishing format = EPUB 3** (Pandoc-generated from the AST canonical via `pandoc -f json -t epub3`). Rich reader ecosystem — Apple Books, Google Play Books, Calibre, Adobe Digital Editions, Kobo, Foliate, Thorium. Kindle compatibility via EPUB 3 → Send to Kindle (Amazon's converter to .azw3 / .kfx). MOBI is rejected — Amazon deprecated it in 2022 and Pandoc has no MOBI writer.

- **Decision-mode = SUBSTITUTE.** Not "validate" (the frame was wrong); not "overturn" (Pandoc's markdown is right for one layer); not "design-new" (Pandoc's AST already does what a custom AST would). SUBSTITUTE — replace the monolithic frame with three layers; substitute Pandoc-md as canonical with Pandoc-AST-as-JSON; preserve Pandoc-md in the hand-edit role; add EPUB 3 at the publishing layer.

- **Five candidates rejected as canonical, each on structural grounds:** RTF (editor-fragility defeats hand-edit byte-stability; raw typography is the wrong kind of richness), TEI (Pandoc cannot read TEI as input — breaks the architectural lever; verbose), MOBI (Amazon-deprecated; not Pandoc-supported), EPUB-as-intake (heavyweight ZIP of xhtml; lossy round-trip; apparatus criticus not first-class — EPUB 3 IS adopted at the publishing layer instead), Custom format (Pandoc's AST already exists, is mature, has documented tooling).

- **The user's pushback was honored, not dismissed.** Markdown DOES have limitations as a canonical — but the structural fix is to move to AST-as-storage, not to switch to a different surface format. The user's intuition pointed at the right problem (surface-syntax storage loses structural information); the resolution is the layered architecture.

- **Prior intake-concepts finding is `refines:`, not overturned.** Pandoc's markdown choice is preserved in a narrower role; the prior's other four decisions are unchanged or strengthened; engineering work routes into specific downstream inquiries.

---

## Finding

### Why the question has three answers

The user's pushback — *"markdown has big limitations; maybe RTF or EPUB or MOBI or a new format"* — surfaced a structural defect in how the prior finding framed the canonical-intake-format question. The prior framed it as a single decision: which one file format does intake produce, persist, and hand to translate? But "canonical format" actually splits across **three temporal layers** of the translation pipeline, each with different optimal properties:

| Temporal layer | What the format serves | Optimal property |
|---|---|---|
| Intake / translate | The format intake produces and translate reads | Lossless round-trip + queryable structure |
| Hand-edit | When a user opens a file to fix a bad parse | Human-readable + byte-stable in any UTF-8 editor |
| Publishing | When a translation ships to readers as a book | Reader ecosystem + packaged-book structure |

These three optima are **structurally different and partially incompatible**. A format that's optimal for lossless round-trip (like Pandoc's AST as JSON — an explicit nested-object structure) is not human-readable for hand-editing. A format that's optimal for hand-editing (like markdown — plain text with reading-order-natural syntax) has surface-syntax storage limits that are exactly what the user's intuition was reaching for. A format that's optimal for the publishing ecosystem (like EPUB 3 — a ZIP of xhtml with manifest and metadata) is heavyweight for intake-time round-trip.

No single format optimizes all three layers. The prior finding's choice of Pandoc's markdown for the canonical role was a compromise: markdown wins for hand-editability, but it loses for the canonical lossless-round-trip requirement (some Pandoc-markdown features round-trip with the parsed tree losslessly; some do not, and the boundary is not crisp). The user's pushback identified the loss. The architectural fix is to **decouple the three layers** and pick the right format per layer.

### The three formats and their roles

#### F1 — Canonical intake + translate format = Pandoc's AST serialized as JSON

When the intake pipeline completes, it produces a single JSON file: the Pandoc Abstract Syntax Tree representing the document. This file IS the canonical form. Every translate-stage operation reads this JSON and operates on its node tree. The in-memory `IntakeDoc` object (from the prior finding's Decision 3 — tree-of-containers + cross-referenced flat collections) is the deserialized AST.

**Round-trip mechanics.** Pandoc natively reads and writes its AST in JSON:

```bash
# Markdown source → JSON canonical
pandoc -f markdown -t json input.md > canonical.json

# JSON canonical → markdown (for hand-editing)
pandoc -f json -t markdown canonical.json > for_editing.md

# JSON canonical → EPUB 3 (for publishing)
pandoc -f json -t epub3 -o published.epub canonical.json
```

The Pandoc AST shape is documented at pandoc.org as part of the Pandoc reference manual and is the native data structure of the Pandoc-types Haskell library. From Python, the **`panflute`** package (available on PyPI as `panflute`) provides typed access to AST nodes (`Header`, `Para`, `Note`, `Span`, `Div`, `Emph`, `Strong`, `Code`, `LineBlock`, and others).

**Schema validation.** Two layers:

1. **Pandoc AST conformance.** The JSON must be a valid Pandoc AST. A no-op round-trip (`pandoc -f json -t json`) validates structural soundness against the running Pandoc's expected schema.

2. **Project pydantic layer (optional).** comprehenslate may define a pydantic model on top of the AST shape to enforce project-specific invariants (for example: "every chapter has a title"; "every footnote reference resolves to an apparatus entry"; "apparatus collection ids are unique"). Whether to use this layer or operate directly on Pandoc's native AST is a downstream design decision.

**Cross-version stability.** Pandoc's JSON output carries an `api-version` field in its header that names the AST shape version. The architectural commitment is to **pin a specific Pandoc version** as the project's canonical (likely Pandoc 3.x stable at the time of build); cross-version migration is handled by running the older JSON through the newer Pandoc once (`pandoc -f json -t json`), which Pandoc handles automatically for compatible versions and signals when not. Round-trip losslessness is guaranteed within a pinned version; the operational policy for version pinning + migration is part of the project's engineering setup.

**Why this format wins for the canonical role.**

*Lossless round-trip.* The AST contains everything Pandoc's parser perceived, including bracketed-span attributes for `lang=` and `dir=`, footnote references and definitions, citation keys, and raw-attribute escapes. Saving it as JSON and reading it back produces an identical AST (within a pinned Pandoc version). There is no "round-trip-stable subset" issue as there is with surface markdown — every node round-trips by the AST's design.

*Explicit-tree storage.* Surface markdown stores structure implicitly: a blank line means paragraph break; a leading `#` means heading; indentation can mean code-block or continuation depending on context. The AST stores structure explicitly as typed nodes. Any later analysis (the seven policy-perception detectors from the prior finding; the chunking stage; the validate stage) operates on the explicit tree without re-parsing.

*Pure data.* JSON is the universal serialization format. Standard Python tooling (`json` stdlib, `pydantic`, `panflute`) handles it. Diffing two `IntakeDoc` files is a structured-diff problem with mature solutions.

*Queryable.* Need every footnote? Walk the AST's `Note` nodes. Need every Arabic span? Walk paragraph runs for `Span` nodes with `lang=ar`. The tree is enumerable; surface markdown requires re-parsing for the same queries.

**Mapping to the prior finding's `IntakeDoc`.** The prior `IntakeDoc` was defined as a tree-of-containers (Document → Chapter → Section → Paragraph) plus cross-referenced flat collections (footnotes, marginalia, embedded poetry, formulaic openings, non-main-language spans, voice transitions, honorifics, archaic register marks). The Pandoc AST is structurally equivalent at the in-memory level. The only change from the prior is the **on-disk representation**: was Pandoc's markdown; now JSON-serialized AST.

#### F2 — Hand-edit format = Pandoc's markdown (the prior Decision 1's choice, refined to a narrower role)

When a user wants to fix a bad parse by hand, they open a markdown file. The extension set is the same the prior finding committed for Pandoc's markdown: footnotes, pipe tables and grid tables, definition lists, citations (via `@key`), YAML metadata blocks, raw attributes (`{=html}`), and bracketed spans for inline language and direction tagging.

**The hand-edit workflow.**

```
1. Intake produces canonical.json
2. User wants to fix something
3. pandoc -f json -t markdown canonical.json > edit.md
4. User edits edit.md in any text editor — VS Code, BBEdit, Sublime, Vim, JetBrains, TextEdit-in-plain-mode
5. pandoc -f markdown -t json edit.md > canonical_updated.json
6. Intake re-loads canonical_updated.json
```

Pandoc's markdown is byte-stable in any UTF-8 editor that preserves bytes — the failure mode RTF has (different editors re-serialize on save through their rich-text engines) does not occur. The user can pick whatever editor they prefer.

**The round-trip-stable subset.** Not every Pandoc-markdown feature round-trips with the JSON canonical losslessly. For example: a citation `@smith2020` survives both directions, but some auto-link constructs may emerge as explicit `<http://...>` after round-trip; some heading attributes may shift form. The **round-trip-stable subset** is the set of Pandoc-md features guaranteed to survive `markdown → JSON → markdown`. Defining this subset precisely is a downstream design task (see Next Actions, MUST 2). For v0.2 the working assumption is: every feature explicitly named in the canonical extension set (footnotes, tables, definition lists, citations, YAML metadata, raw attributes, bracketed spans) is round-trip stable; anything outside that set may not be, and the subset will refine iteratively as the prototype (Next Actions, COULD 2) surfaces edge cases.

**Why markdown remains the right choice for the hand-edit role.**

*Human-readable.* A footnote is `[^1]: text`; an emphasized word is `*word*`; a chapter heading is `# Title`. The syntax is reading-order-natural and learnable in minutes.

*Byte-stable.* Plain text. Any UTF-8-respecting editor preserves it. The failure mode RTF has — editor-specific re-serialization on no-op save — cannot occur.

*Familiar.* The user already knows markdown; the workflow is unchanged for them in user-facing terms.

*Prior Decision 1 preserved.* The prior choice of Pandoc's markdown was right for this role. The prior conflation gave it more responsibility than it should have had; the refined frame puts it in its appropriate scope.

#### F3 — Publishing format = EPUB 3

When a translated text is ready to ship to readers, it is generated as an EPUB 3 file from the JSON canonical:

```bash
pandoc -f json -t epub3 \
    --metadata title="Translated Title" \
    --metadata author="Said Nursi" \
    --metadata language="en" \
    --epub-cover-image=cover.png \
    --css=publication.css \
    -o translation.epub canonical.json
```

EPUB 3 is the open W3C-anchored ebook standard (specification at idpf.org and w3.org). The format is a ZIP archive containing xhtml content files, an OPF manifest, metadata, and optional CSS and media. Pandoc's `epub3` writer handles the manifest construction; the user provides metadata flags and a CSS template.

**Reader ecosystem.** EPUB 3 reads natively in Apple Books (macOS / iOS / iPadOS), Google Play Books (Android and web), Calibre (cross-platform desktop library and viewer), Adobe Digital Editions (cross-platform), Kobo eReader devices and apps, Foliate (Linux GTK reader), and Thorium (W3C-backed cross-platform reader). Plus dictionary-integration tools (for example, Apple Books has built-in Arabic dictionary support), annotation tools, and library managers.

**Kindle compatibility.** Amazon deprecated the .mobi format in 2022 — Kindle Direct Publishing stopped accepting .mobi uploads, and Kindle devices now use .azw3 and .kfx. The conversion path is **EPUB 3 → Send to Kindle → .azw3 / .kfx** (Amazon's converter, which runs locally or through Amazon's web UI). Users do NOT generate .mobi directly; Amazon's tooling handles the conversion from EPUB 3. Pandoc has no native MOBI writer because the format is Amazon-proprietary and not openly specified.

**Why EPUB 3 wins for the publishing role.**

*Packaged-book format.* One .epub equals one whole book. A multi-volume work (the calibration corpus, for example) is naturally one EPUB per volume or one EPUB per multi-volume set.

*Native lang, dir, and footnote semantics.* The xhtml inside EPUB 3 supports `lang=` and `dir=` attributes (W3C standard) and `epub:type="footnote"` plus `<a epub:type="noteref">` for footnote references and `<aside epub:type="annoref">` for marginalia. The seven policy targets from the prior finding map cleanly.

*Wide ecosystem.* The reader-side tooling already exists; comprehenslate's role is to produce well-formed EPUB 3, not to build a reader.

*Pandoc-native.* `pandoc -t epub3` produces standard-conforming EPUB 3 directly from the JSON canonical; no custom packaging code is required for v0.2.

### Rejected candidates

Five candidates the user named or that the surfacing surfaced are rejected as canonical, each on structural grounds.

**RTF — rejected as canonical, retained as accepted user-provided input.** Pandoc reads and writes RTF, but RTF is **editor-fragile**: opening an RTF file in Microsoft Word, Apple Pages, Apple TextEdit, or LibreOffice and saving with no edits produces a byte-different file in each editor. This is because each editor implements its own subset of the RTF spec plus its own extensions, then re-serializes on save through its rich-text engine. The hand-edit recovery workflow depends on byte-stability under no-op save — a property RTF cannot guarantee in any editor that interprets it as rich text. Additionally, RTF preserves raw typography (font face, font size, color), which the prior finding's Decision 2 (quality target = structure-preservation) commits to dropping; storing typography only to filter it later is wasted intake work. RTF survives in a different role: as an **accepted user-provided input format** that intake reads via Pandoc to produce the JSON canonical.

**TEI — rejected as canonical, retained as future archival-output frontier.** TEI (Text Encoding Initiative) is the scholarly-text-encoding gold standard, with native support for marginalia (`<note place="margin">`), apparatus criticus (`<app>`, `<rdg>`, `<lem>`), voice marking (`<said who="...">`), and multi-language tagging (`xml:lang`). But Pandoc does NOT read TEI as input — its format support matrix lists TEI Simple as an output target only. Choosing TEI as canonical intake would force the project to implement a custom TEI reader, breaking the architectural lever from the prior finding's Decision 5 (Pandoc as universal converter). Additionally, TEI is verbose (typically five to ten times the markdown equivalent for the same content) and requires TEI vocabulary expertise to hand-edit. TEI is recorded in this finding's frontier as a potential future archival-output format for scholarly use cases.

**MOBI — rejected.** Amazon deprecated the .mobi format in 2022; Kindle Direct Publishing stopped accepting .mobi uploads, and Kindle devices now use .azw3 and .kfx. Pandoc never supported MOBI in any direction. Naming MOBI as a candidate today is wrong-target: if Kindle distribution is the goal, the path is EPUB 3 → Send to Kindle → .azw3 / .kfx, which is the F3 publishing layer above.

**EPUB 3 as canonical INTAKE — rejected; EPUB 3 IS adopted at the publishing layer.** EPUB 3 is the right format at the publishing layer (F3) but the wrong format at the intake canonical layer. As a ZIP archive of xhtml files plus a manifest plus metadata, EPUB 3 is heavyweight for hand-editing (the user would have to unzip, edit, re-zip, validate the manifest), and Pandoc's round-trip through EPUB is lossy at the canonical level (round-tripping `markdown → epub → markdown` drifts metadata, TOC structure, and class attributes). Apparatus criticus, while encodable via `epub:type="annoref"`, is not first-class as it is in TEI. EPUB 3 at the publishing layer — generated from the JSON canonical — gets the ecosystem benefits without the intake-layer costs.

**Custom format (custom JSON-AST or `.compldoc`) — rejected.** Pandoc's AST is already a custom AST: designed for cross-format conversion, mature, well-tested, with documented types and Python tooling via `panflute`. Creating a project-specific JSON-AST schema or extending Pandoc-markdown into a `.compldoc` superset would reinvent what already exists. If the project later needs project-specific invariants (for example, "every chapter has a title"; "every footnote reference resolves"), those can be enforced via a pydantic layer on top of the Pandoc AST — not as a separate custom format. The custom-format path is documented in the frontier as conditionally revivable if specific requirements emerge that the AST + markdown + EPUB architecture cannot serve.

### Calibration-corpus implications (Risale-i Nur)

The seven policy targets from the prior intake-concepts finding's Decision 4 each map onto the Pandoc AST as follows. For each policy, the AST representation, the EPUB rendering, and the Pandoc-markdown hand-edit syntax are named together.

- **`SourceApparatusPolicy` — Hashiye (Said Nursi's marginalia).** AST `Note` node (Pandoc's note type) optionally wrapped in a `Div` with class `marginalia` to distinguish hashiye from ordinary footnotes; preserved losslessly in the JSON canonical. Rendered in EPUB 3 as `<aside epub:type="footnote">` with CSS class. Editable in Pandoc's markdown as either a fenced div for block-level marginalia (`::: {.marginalia ref-id=h1} hashiye body :::`) or as an inline span for short marginal notes (`[short marginalia text]{.marginalia ref-id=h1}`); the exact pattern per instance is a perception-detector design choice.

- **`EmbeddedPoetryPolicy` — Mevlana couplets in Nursi's prose.** AST `LineBlock` (Pandoc's verse / line-block type) wrapped in a `Div` with class `couplet` and an attribute naming the attribution; preserved. Rendered in EPUB 3 as `<blockquote class="poetry">` with line breaks preserved. Editable in Pandoc's markdown as a line block (`| line1` `| line2`) inside a fenced div (`::: {.couplet attribution="Mevlana"} ... :::`).

- **`FormulaicOpeningPolicy` — Bismillah and Hamd preambles.** AST `Para` (or a fenced `Div`) with class `formulaic-opening`, constrained to position-at-section-start. Preserved. Rendered in EPUB 3 with a CSS class for styling. Editable in Pandoc's markdown as a paragraph with a fenced-div class wrapper (`::: {.formulaic-opening} ... :::`).

- **`NonMainLangPartsPolicy` — Arabic spans within Turkish narrative (Qur'anic quotations, Hadith, technical terms).** AST `Span` with `lang=ar` and `dir=rtl` attributes via Pandoc's `bracketed_spans` extension; preserved. Rendered in EPUB 3 as `<span lang="ar" dir="rtl">`. Editable in Pandoc's markdown as `[ٱلْحَمْدُ لِلَّٰهِ]{lang=ar dir=rtl}`.

- **`VoiceMarkingPolicy` — voice transitions (Nursi's authorial voice vs cited authorities like Qur'an or Hadith).** AST `Span` with a class indicating the voice (for example `class="voice-cited"` or `class="voice-author"`); preserved. Rendered in EPUB 3 with a CSS class. Editable in Pandoc's markdown as `[cited content]{.voice-cited}`.

- **`ArchaicRegisterPolicy` — Ottoman Turkish lexical or syntactic archaisms.** AST `Span` with class `archaic-register` and optional attribute for the archaism category; preserved. Rendered in EPUB 3 with a CSS class. Editable in Pandoc's markdown as a bracketed span with class attribute.

- **`HonorificsPolicy` — Islamic honorific markers (the SAW / AS / RA / PBUH family following names).** AST `Span` with class `honorific` and an attribute naming the tradition; preserved. Rendered in EPUB 3 with a CSS class. Editable in Pandoc's markdown as a bracketed span attached to the personal-name span.

- **NFC diacritic normalization.** The prior finding's pipeline-stage normalize commits to `unicodedata.normalize('NFC', s)` at intake. NFC is preserved through the Pandoc AST (UTF-8 storage); through Pandoc-markdown (also UTF-8); through EPUB 3's xhtml (also UTF-8). At no point in the three-format chain does the diacritic representation drift, provided NFC is applied once at intake.

The per-policy detector designs from the prior finding (the seven downstream design inquiries flagged as DESIGN-NEXT-INQUIRY in the prior intake-concepts finding) need a small spec refinement: their "perception signals" sections currently reference markdown surface signals (Pandoc note nodes, .docx margin-comments, custom-md divs); they should be re-specified to reference Pandoc AST node types and attributes (Note, Span, Div with class). The structural intent is unchanged; the spec wording shifts.

### Methodology

This finding's claims are anchored to three grounding sources, named explicitly so the reader can audit:

1. **Pandoc reference manual.** Claims about Pandoc commands, extensions (`bracketed_spans`, `footnotes`, `pipe_tables`, etc.), and AST node types (`Header`, `Note`, `Span`, `LineBlock`, etc.) are verifiable at pandoc.org. The Python ecosystem reference is `panflute`, available at panflute.readthedocs.io and on PyPI as the `panflute` package.

2. **Prior intake-concepts finding (`refines:` source).** Structural commitments from the prior — the seven policy classes from `schemas.py`, the IntakeDoc tree-of-containers + cross-referenced flat collections shape, the Pandoc-as-architectural-lever, the calibration corpus framing — carry forward.

3. **Sensemaking-anchor.** The architectural commitments made in this finding (decoupling three temporal layers; AST-as-storage strategy; the SUBSTITUTE decision-mode) rest on the sensemaking phase's adjudication, captured in `docarchive/sensemaking.md`.

Any claim that extends beyond these three sources is marked as extrapolation inline. The MOBI deprecation date is named approximately (`in 2022`) rather than precisely; the developer-time sizing estimates in Next Actions are extrapolations of typical engineering pace.

---

## Inherited Commitments Re-test

This finding `refines:` the prior intake-concepts finding. Five commitments are inherited.

- **Commitment:** Canonical intake format = Pandoc's markdown (Decision 1 of the prior).
  - **Source:** `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`, the Decision 1 section.
  - **Re-test status:** **RE-TESTED — commitment confirmed but frame revised.** The format choice (Pandoc's markdown) is the right choice for the **hand-edit role** within a three-temporal-layer architecture; the prior's monolithic-single-format frame was structurally wrong. The prior rationale's three parts each re-tested: (1) "covers needed primitives off-the-shelf" — TRUE for the hand-edit role; (2) "single parser surface" — TRUE and STRENGTHENED across all three formats since they are all Pandoc-native; (3) "hand-editable" — TRUE and now this is Pandoc-markdown's primary role.
  - **Evidence:** the Finding's section on F2 (hand-edit format) preserves Pandoc-markdown with the same canonical extension set the prior committed; the section on F1 substitutes a new canonical (Pandoc-AST-as-JSON) for the on-disk intake-time representation.

- **Commitment:** Quality target = structure-preservation (Decision 2 of the prior).
  - **Source:** `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`, the Decision 2 section.
  - **Re-test status:** **RE-TESTED — commitment confirmed.** The AST canonical preserves structure better than surface markdown (explicit-tree storage vs implicit surface-syntax). Structure-preservation is strengthened, not weakened, by the format-architecture refinement.
  - **Evidence:** the F1 section names explicit-tree storage as the canonical's load-bearing property; surface markdown's round-trip-stable-subset issue is the structural loss that the AST canonical addresses.

- **Commitment:** `IntakeDoc` shape = tree-of-containers + cross-referenced flat collections (Decision 3 of the prior).
  - **Source:** `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`, the Decision 3 section.
  - **Re-test status:** **RE-TESTED — commitment confirmed.** The in-memory `IntakeDoc` is now the deserialized Pandoc AST; the tree-of-containers + cross-referenced flat collections shape is structurally equivalent to Pandoc's AST organization (Document → Block-level nodes including Header / Para / Div / Note; Span-level nodes inline). The only change is the on-disk representation: was Pandoc-markdown; now JSON-serialized AST.
  - **Evidence:** the Calibration-corpus implications section maps each policy target onto specific Pandoc AST node types.

- **Commitment:** The 7-policy intake-perception + translate-rendering split (Decision 4 of the prior).
  - **Source:** `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`, the Decision 4 section.
  - **Re-test status:** **RE-TESTED — commitment confirmed.** **UNCHANGED in structural intent;** per-detector specs need adjustment to reference AST node types (Note, Span, Div with class) rather than markdown surface signals. The work is design-refinement, not redesign — the seven detectors' structural roles and policy-feed obligations are preserved.
  - **Evidence:** the Calibration-corpus implications section enumerates the AST representations for each of the seven policy targets, confirming each remains expressible.

- **Commitment:** Pandoc + OCR (Tesseract via OCRmyPDF) as architectural lever (Decision 5 of the prior).
  - **Source:** `devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`, the Decision 5 section.
  - **Re-test status:** **RE-TESTED — commitment confirmed and strengthened.** All three formats in the new architecture (JSON canonical, markdown hand-edit, EPUB 3 publishing) are Pandoc-native; Pandoc's role as universal converter is reinforced by being applied at all three layers. The OCR sub-pipeline is unchanged — OCR feeds Pandoc, which produces the canonical AST.
  - **Evidence:** the F1, F2, and F3 sections all reference Pandoc commands as the operational mechanism; the prior's OCR design (frontier flag for depth-1 layout analysis) is carried forward intact.

---

## Next Actions

### MUST

- **What:** Design the JSON-AST canonical schema. Decide between using Pandoc's native AST shape directly OR adding a project-specific pydantic layer for type safety and project invariants (for example, "every chapter has a title"; "every footnote reference resolves to an apparatus entry"; "apparatus collection ids are unique"). Specify the cross-version migration story (pin a Pandoc version; document the `api-version` field's role in migration).
  - **Who:** the next schema-design inquiry (likely a `/traverse` run).
  - **Gate:** condition-bound — start before any other intake engineering. The schema is the contract every stage populates.
  - **Why:** the JSON canonical is the load-bearing format commitment; without the schema, no intake stage can ship.

- **What:** Define the round-trip-stable Pandoc-markdown subset. Document which Pandoc-markdown features are guaranteed to round-trip with the JSON canonical losslessly. The working assumption is the canonical extension set (footnotes / pipe tables / definition lists / citations / yaml metadata / raw attributes / bracketed spans) is stable; per-feature verification is the work. Test method: a Python script that emits sample markdown per feature, runs `pandoc -t json` then `pandoc -f json -t markdown`, and byte-compares. Expect iterative refinement as edge cases surface during the prototype below.
  - **Who:** a smaller-scoped design inquiry, possibly inline in the schema work.
  - **Gate:** condition-bound — start alongside MUST 1 once the JSON canonical's structure is committed.
  - **Why:** the hand-edit workflow's contract depends on this subset being explicit; without it, users hit silent drift when their markdown round-trips through JSON.

### COULD

- **What:** Design the EPUB 3 generation pipeline. Specify the Pandoc invocation flags; design metadata extraction from the AST; define per-chapter file structure; design the CSS template for typography, including Arabic-aware font fallback chain (Amiri, Noto Sans Arabic, Scheherazade) and RTL block handling; per-policy CSS classes for visual differentiation; cover-image workflow; embedded-font policy.
  - **Who:** an EPUB-pipeline design inquiry.
  - **Gate:** condition-bound — start after MUST 1 commits the schema; can run in parallel with the prototype below.
  - **Why:** the publishing-layer commitment needs an implementation; without it, F3 is theoretical.
  - **Depends-on:** MUST item *the JSON-AST canonical schema*. This COULD is GATED — do not act until the MUST resolves.

- **What:** Build an end-to-end prototype taking ONE Risale-i Nur volume sample (with hashiye, a Mevlana couplet, and a Bismillah opening) through the full pipeline: intake → JSON canonical → EPUB 3. Verify Arabic + marginalia + couplets + Bismillah render correctly in at least three EPUB readers (Apple Books, Calibre, Google Play Books). Report quality metrics + per-stage timings + visual EPUB output.
  - **Who:** an engineering iteration once MUST 1 + COULD 1 have draft designs.
  - **Gate:** condition-bound — start after MUST 1 produces a draft schema and COULD 1 has an initial EPUB pipeline.
  - **Why:** the architectural verdict needs empirical confirmation on the calibration corpus. Integration testing surfaces issues that per-stage unit tests cannot. The prototype IS the calibration anchor for all subsequent format-architecture work.
  - **Depends-on:** MUST item *the JSON-AST canonical schema* + COULD item *EPUB 3 generation pipeline*. This COULD is GATED — do not act until the schema + pipeline are at least drafted.

- **What:** Re-spec the seven policy-perception detectors from the prior intake-concepts finding to reference Pandoc AST node types (Note, Span with `lang=`, Div with `class=`, LineBlock with `class=`, Para with `class=`) rather than markdown surface signals. The structural intent of each detector is unchanged; the perception-signal section refreshes.
  - **Who:** a small refinement inquiry, possibly inline in the seven downstream detector-design inquiries from the prior finding.
  - **Gate:** condition-bound — start alongside MUST 1.
  - **Why:** the new canonical is JSON-AST; the detectors must perceive in the AST.
  - **Depends-on:** MUST item *the JSON-AST canonical schema*. This COULD is GATED — do not act until the schema's apparatus-collection shape is committed.

### DEFERRED

- **What:** TEI Simple as future archival output format. Pandoc can write TEI Simple (output-only); if a scholarly archival use case emerges, the project can add TEI as a separate output layer alongside EPUB 3 publishing.
  - **Gate:** revival trigger — when either (a) a scholarly archival use case is named by the project, or (b) cross-corpus validation surfaces a TEI requirement.
  - **Why (if revived):** TEI is the scholarly-text-encoding gold standard; native support for marginalia, apparatus criticus, voice marking; useful for long-term scholarly archival.

- **What:** Revisit custom-format design. The rejection of custom format in this finding is conditional on the AST + markdown + EPUB architecture proving sufficient.
  - **Gate:** revival trigger — when specifically named: (a) a corpus surfaces primitives Pandoc's AST cannot represent; (b) Pandoc deprecation or migration cost becomes prohibitive; (c) the project needs a format Pandoc cannot generate.
  - **Why (if revived):** at least one structural defect would need to surface; without it, custom format is unnecessary engineering.

- **What:** Reframe the three-format architecture as four-format by adding an archival / historical preservation layer.
  - **Gate:** revival trigger — when (a) cross-corpus validation surfaces archival need, or (b) the project commits to long-term preservation of source and translated corpora.
  - **Why (if revived):** archival has different optimal properties from intake, hand-edit, and publishing (long-term format stability; openness; minimal external dependencies); a separate layer may be warranted.

- **What:** Pandoc version pinning policy documentation in the project engineering README.
  - **Gate:** condition-bound — resolved by the engineering team when the project's version policy is set.
  - **Why (if revived):** the JSON-AST canonical's round-trip stability is per-Pandoc-version; the policy needs explicit documentation.

---

## Reasoning

### Why three formats over one

The prior intake-concepts finding's Decision 1 was a single-format commitment: Pandoc's markdown as the canonical that intake produces, translate consumes, and users hand-edit. The user's pushback — that markdown felt limiting — surfaced the structural defect in this frame: a single format must compromise on at least one of three temporal layers (intake/translate · hand-edit · publishing), each with different optimal trade-offs.

Three single-format alternatives were considered structurally:

- **Pandoc's markdown as monolithic canonical** (the prior commitment, defended) — wins for hand-editability, loses for canonical lossless-round-trip (the round-trip-stable-subset issue is real and bounded).

- **RTF as monolithic canonical** (the user's intuition) — fails on hand-edit byte-stability across editors (Word / Pages / TextEdit re-serialize on save); the rich-text typography RTF preserves is exactly what Decision 2 commits to dropping; the encoding-fragility of RTF (Windows code-pages + Unicode escapes interplay) is a real diacritic-stability risk for the calibration corpus's Arabic content.

- **EPUB 3 as monolithic canonical** (the user's intuition) — wins for publishing ecosystem and packaged-book structure, fails for hand-editability (ZIP archive of xhtml + manifest is not single-file editable) and for canonical lossless-round-trip (Pandoc's `markdown → epub → markdown` drifts metadata).

None of the three single-format alternatives win across all three layers. The architectural correct move is to decouple the layers. The three-format architecture honors what each layer needs: JSON-AST for canonical (lossless + explicit-tree); Pandoc-markdown for hand-edit (human-readable + byte-stable); EPUB 3 for publishing (ecosystem + packaged-book).

### Why Pandoc's AST as JSON wins for the canonical role

Three alternatives were considered for the canonical role specifically:

- **Surface markdown (Pandoc's markdown).** Reasoning: human-readable; familiar; works today. Counter: the round-trip-stable subset is real and bounded; some Pandoc-markdown features round-trip with the AST losslessly and some do not; the boundary is not crisp without a documented subset. Surface storage of a parsed tree is structurally fragile.

- **Custom JSON-AST (project-specific schema).** Reasoning: total control over the schema; explicit project-specific invariants. Counter: Pandoc's AST already exists, is mature, is documented, has Python tooling via `panflute`. Recreating it would reinvent what's already there. If project-specific invariants are needed, a pydantic layer on TOP of the Pandoc AST serves them — no separate schema needed.

- **Pandoc's AST as JSON** (the chosen). Reasoning: lossless round-trip by Pandoc's design; documented; queryable; pure data; the architectural lever (Pandoc) applies natively at all three layers; the in-memory `IntakeDoc` IS the deserialized AST. Counter: not human-readable for hand-editing — addressed by the F2 layer (Pandoc-markdown as hand-edit format with `pandoc -f json -t markdown` round-trip).

### Why EPUB 3 wins for the publishing role over MOBI

Amazon deprecated MOBI in 2022. Kindle Direct Publishing stopped accepting .mobi uploads; Kindle devices now use .azw3 and .kfx. The current Kindle workflow is: EPUB 3 → Send to Kindle → .azw3 / .kfx. Pandoc has no MOBI writer because Amazon's format is proprietary and not openly specified. EPUB 3 is the open W3C-anchored standard with the largest reader ecosystem and a clean Pandoc-generated path from the JSON canonical. The user's intuition that "MOBI is good" was reasonable a few years ago; today EPUB 3 is the correct Kindle-compatible answer.

### Why `refines:` and not `corrects:`

The prior intake-concepts finding's Decision 1 — Pandoc's markdown as canonical — was the right choice for the role it occupied; what was wrong was the implicit frame that conflated three temporal layers into one. The prior's choice survives, in a narrower role (hand-edit format). The relationship label `refines:` captures this: the prior is preserved; its scope is narrowed; the architecture extends to layers the prior did not name.

`corrects:` would imply the prior's CHOICE was wrong, which it wasn't. `supersedes:` would imply the prior is dead, which it isn't (the other four prior decisions stand). `refines:` is the structurally accurate relationship.

---

## Open Questions

### Monitoring

- **Pandoc cross-version stability.** The JSON canonical's round-trip stability is per-Pandoc-version. Empirical confirmation arrives when the prototype runs across a Pandoc version bump (likely v3.x to v3.y).

- **The round-trip-stable Pandoc-markdown subset.** The working assumption is that the canonical extension set (footnotes, pipe tables, definition lists, citations, YAML metadata, raw attributes, bracketed spans) is round-trip stable. Per-feature verification will surface edge cases during the prototype.

- **The seven policy-perception detector recall on the AST-canonical pipeline.** The prior finding's detector designs are spec-refined for AST node types in this finding's Next Actions. Recall measurement on the calibration corpus will surface which detectors need more resource investment.

### Blocked

- **The EPUB pipeline design** is blocked until the JSON canonical's schema commits (MUST 1). Pandoc's `epub3` writer needs to know what the canonical shape is.

- **Cross-corpus format-architecture validation** is blocked until the calibration-corpus prototype validates. The architectural commitment must hold for Risale-i Nur first before generalization.

### Research Frontiers

- **Custom format from requirements.** The rejection of custom format is conditional. If a specific requirement surfaces that Pandoc's AST + markdown + EPUB cannot serve, the custom-format design path is conditionally revivable.

- **Archival / historical preservation as a fifth temporal layer.** The three-format architecture covers intake/translate, hand-edit, and publishing. A separate archival layer (TEI? JATS? zip-of-AST-plus-source?) may emerge with project maturity.

- **TEI as future archival output.** Pandoc writes TEI Simple (output-only). For scholarly archival use cases, generating TEI Simple from the JSON canonical is feasible. Whether and when to do this is a future decision.

### Refinement Triggers

- **The three-format architecture re-opens** if cross-corpus validation surfaces a corpus the layered architecture cannot serve.

- **The Pandoc-as-architectural-lever re-opens** if Pandoc undergoes a breaking change that the project's pinning policy cannot absorb.

- **The EPUB 3 publishing-format choice re-opens** if EPUB 3's ecosystem fragments (for example, if Apple Books, Google Play Books, and Kindle diverge on EPUB 3 support in ways that defeat the ecosystem benefit).

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
The real wrinkles aren't about Arabic per se — they're about three things markdown doesn't carry natively:
  
  - Direction metadata. Plain markdown has no concept of right-to-left. The Unicode bidirectional algorithm (UAX #9) handles RTL display at
  render time based on character properties, so a paragraph that is "mostly Arabic" displays correctly in any compliant renderer. But for
  explicit span-level direction tagging (e.g., a Turkish sentence quoting an Arabic verse, both rendered in the right direction), Pandoc's
  markdown lets you write [هِ─لَّٰ   لِ دُمْحَلْٱ]{lang=ar dir=rtl} — that's Pandoc's bracketed_spans extension with a language + direction
  attribute. The lang attribute is what feeds the NonMainLangPartsPolicy detector in the finding.
  - Diacritic normalization. Arabic uses combining marks (fatha, damma, kasra, sukun, shadda — the harakat). Same visual word can be stored
  as either composed (NFC) or decomposed (NFD) forms — different byte sequences, same display. The finding's C4 normalize stage already
  commits to unicodedata.normalize('NFC', s), which makes diacritic representation deterministic. Without this, two intakes of the same
  Arabic text could produce byte-different IntakeDoc files.
  - Presentation forms vs abstract letters. Some sources (especially badly-OCR'd PDFs) store Arabic as Presentation Forms (the U+FE70 range)
  — pre-shaped glyphs corresponding to a letter's position in a word (initial / medial / final / isolated). The Unicode-correct way is the
  abstract letter (U+0628 BEH) plus shaping at render time. If a source has presentation forms, Pandoc preserves them as-is; renderers
  display them but a search for "ءاهب" won't match if the stored bytes are presentation forms. This is a real risk in the PDF intake path
  and is what concept A3 (OCR sub-pipeline) will need to address (Tesseract has flags for this).

  3. The hand-editing workflow with Arabic is editor-quality dependent. VS Code, Sublime Text 4, BBEdit, modern Vim, and JetBrains editors
  handle UTF-8 + bidi + RTL cursor navigation correctly — the user can edit mixed Turkish/Arabic paragraphs without weirdness. Older editors
  and barebones plain-text editors can make cursor movement and selection across script boundaries confusing. But the bytes are preserved
  correctly by any editor that saves as UTF-8 without re-encoding — which is the failure mode RTF has and markdown doesn't.

  4. The biggest practical Arabic risk in our pipeline is not markdown — it's PDF text extraction. Many religious-text PDFs (including some
  Risale-i Nur editions) store Arabic as glyph IDs that don't map back to Unicode codepoints — pdftotext and Pandoc's PDF reader pull
  garbage out. This is the source-quality problem, not Pandoc's. It's why the OCR sub-pipeline (A3) is its own design-next-inquiry:
  scan-only or text-layer-broken PDFs need Tesseract + Arabic language data (tesseract --lang ara) to re-derive the Unicode, which is more
  reliable than trying to repair the original PDF's text layer.


pdftext extraction is another issue.

we should focus on core representative format which will be used for translations.  i was thinking rtf is good for that. 

md has big limitations. we need sth different maybe? maybe we need to comeup with new format even? or epub or mobi formats are good?

lets dive deep on this
```

</details>
