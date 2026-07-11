# Innovation — canonical intake format deep dive

## User Input

Substrate: `_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md`. Production-task mode: Decomposition's 10 pieces (P1-P10) are the seed; Innovation generates per-piece substantive content.

---

## Phase 1 — Seed / Methodology-Mode Consideration

**Inherited methodology mode:** **Standard default** (4G+3F balanced; elaborate the committed direction). The seed framing — *"This is the discipline where the substantive content gets GENERATED"* — plus Sensemaking's locked verdict (SUBSTITUTE; three-format layered architecture) places this run in Standard default mode.

**Alternative mode considered:** **Contrarian-rethink (Framer-weighted)** — re-challenge sensemaking's verdict; surface alternatives like "validate-prior" or "design-new" at piece level.

**What follows under the alternative:** Innovation would treat the three-format architecture as questionable and surface alternatives (e.g., keep monolithic Pandoc-md; pick a custom format from scratch). Candidate-space widens, but sensemaking already ran Strongest-Counter tests on these alternatives in Phase 3 Ambiguity Collapse (Ambiguities 1, 2, 7) with HIGH-confidence resolutions.

**Decision:** **Standard default.** Piece-level Inversion at the meta-decision pieces (P2, P8) provides the contrarian surface at appropriate granularity.

`Methodology-mode-alternative-marked-inapplicable: Sensemaking's Phase 3 ran Strongest-Counter tests on the three-format architecture (Ambiguity 1) and on the SUBSTITUTE decision-mode (Ambiguity 2) with HIGH-confidence resolutions; Contrarian-rethink at Innovation would duplicate adjudication without new evidence. Piece-level Inversion at P2 and P8 provides the contrarian surface at appropriate granularity.`

---

## Phase 2 — Generate (per piece)

### P2 (META-DECISION; produced FIRST) — Architectural Commitment + Decision-Mode

**Principal candidate (content):**

> **The architectural commitment: three-format layered architecture.**
>
> The canonical intake format question has been mis-framed as "which single format is the canonical?" That framing was inherited from the prior intake-concepts finding (`devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`), which committed Pandoc's markdown as a single monolithic canonical. The user's pushback — *"markdown has big limitations; maybe RTF or EPUB or a new format"* — surfaced that the single-format frame is structurally wrong. The right frame is that "canonical" splits into **three temporal layers**, each with different optimal trade-offs:
>
> | Temporal layer | What it serves | Optimal property |
> |---|---|---|
> | Intake / translate | The format intake produces and translate reads | Lossless round-trip + queryable structure |
> | Hand-edit | When users fix bad parses by hand | Human-readable + byte-stable in any UTF-8 editor |
> | Publishing | When translation output ships as a book | Reader ecosystem + packaged-book structure |
>
> No single format optimizes all three; forcing one compromises all three. The architectural commitment is to **decouple the three layers** and pick the right format per layer.
>
> **The decision-mode: SUBSTITUTE.** This is not "validate the prior choice" (the frame was wrong); it is not "overturn the prior choice" (Pandoc's markdown is the right format for one of the three layers); it is **SUBSTITUTE** — substitute the prior monolithic frame with the three-layer frame; substitute the prior's canonical-intake choice (Pandoc-md) with Pandoc-AST-as-JSON; preserve Pandoc-md in a refined narrower role (hand-edit); add EPUB 3 as the publishing layer.
>
> **The relationship to the prior finding: `refines:`.** This finding's frontmatter declares `refines: devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`. The prior's other commitments (the quality target = structure-preservation, the `IntakeDoc` shape = tree + cross-ref-flat, the 7-policy intake/translate split, Pandoc as architectural lever, the OCR sub-pipeline) are **unchanged** by this refinement. Only Decision 1 (the canonical-format choice) and its implicit single-layer framing are refined.

**Mechanism log:**
- *Lens Shifting:* under "what does the user's pushback ACTUALLY indicate?" lens — they're not asking for a different surface format; they're sensing the conflation of three layers into one.
- *Combination:* prior finding's monolithic frame × three-temporal-layer split → the architectural reframe.
- *Constraint Manipulation (ADD):* added "the three layers have different optima" → the layered architecture follows necessarily.
- *Constraint Manipulation (REMOVE):* removed "one format must cover everything" → the three-format solution emerges.
- *Absence Recognition (patch):* the prior finding never named the publishing layer explicitly; the absence created the conflation.
- *Absence Recognition (redesign):* if intake-architecture were designed from scratch today, the three layers would be table-stakes.

**Piece-Level Inversion (required — P2 is meta-decision via framing-semantic + relationship-label properties):**

> *Inversion-candidate:* what if the prior finding's monolithic-Pandoc-md frame was actually right and the user's pushback was ungrounded intuition?
>
> *What follows under the inversion:* keep Pandoc-md as monolithic canonical (intake / translate / hand-edit all rolled into one). Reject the user's pushback. Engineering proceeds with a simpler single-format architecture. EPUB 3 publishing is deferred or kicked to a future inquiry.
>
> *Why rejected:* Ambiguity 1 in sensemaking surfaced structurally that no single format optimizes all three temporal layers — markdown surface-syntax storage has a round-trip-stable subset (some Pandoc-md features round-trip with the JSON canonical; some don't); the prior finding never named this constraint. The user's pushback is the correct signal — the prior conflation was real. Keeping monolithic Pandoc-md means accepting structural loss at the canonical layer (whatever's outside the round-trip-stable subset is silently lost). The architectural commitment to decouple resolves this; the inversion preserves the structural loss.
>
> *Intervention-shape Inversion check:* P2 commits an architectural reframe — this is REFRAME-AS-BUG in shape (the prior conflation is named as a structural defect). Alternative shapes: REVERT-REGRESSION (revert to a pre-Decision-1 state — n/a, no such state existed); REPAIR (keep the monolithic commitment but add caveats — insufficient because the frame itself is the defect). REFRAME-AS-BUG is the right shape.
>
> Verdict on Inversion: **rejected** — the monolithic frame's structural defect is named and addressed; reverting preserves the defect.

**5-test:** Novelty (the three-layer reframe is novel for this project — the prior never named the temporal layers); Scrutiny (survives "decoupling adds complexity" via the bounded-cost argument); Fertility (the layered architecture spawns three format-spec inquiries, the schema-design inquiry, the EPUB pipeline inquiry); Actionability (an engineer can pick up the three formats and start working); Mechanism independence (Lens Shifting + Combination + Absence Recognition all converge on the three-layer reframe via different paths). PASS.

---

### P3 — F1: Canonical Intake/Translate = Pandoc-AST-as-JSON

**Principal candidate (content):**

> **F1 — The canonical intake + translate format is Pandoc's Abstract Syntax Tree serialized as JSON.**
>
> When intake completes, it produces a single JSON file: the Pandoc AST representing the document. This file IS the canonical form. Every translate-stage operation reads this JSON and operates on its node tree. The in-memory `IntakeDoc` object (per the prior finding's Decision 3) is the deserialized AST.
>
> **Round-trip mechanics.** Pandoc natively reads and writes its AST in JSON:
>
> ```bash
> # md → JSON canonical
> pandoc -f markdown -t json input.md > canonical.json
>
> # JSON canonical → md (for hand-editing)
> pandoc -f json -t markdown canonical.json > for_editing.md
>
> # JSON canonical → EPUB 3 (for publishing)
> pandoc -f json -t epub3 -o published.epub canonical.json
> ```
>
> The Pandoc AST shape is documented in the `pandoc-types` Haskell library; the Python `panflute` library provides typed access from Python. The `pandoc-types-python` package exposes the node types (`Header`, `Para`, `Note`, `Span`, `Div`, `Emph`, `Strong`, `Code`, `LineBlock`, etc.) as classes.
>
> **Schema validation.** Two layers:
>
> 1. **Pandoc AST conformance** — the JSON must round-trip cleanly through `pandoc -f json -t json` (a no-op that validates structural soundness).
> 2. **Project pydantic layer** (optional) — comprehenslate may define a pydantic model on top of the AST shape to enforce project-specific invariants (e.g., "every chapter has a title"; "every footnote reference resolves"). This layer is the work of the `IntakeDoc` schema design (a downstream inquiry).
>
> **Why this format wins for the canonical role.**
>
> *Lossless round-trip.* The AST contains everything the Pandoc parser perceived; saving it as JSON and reading it back produces an identical AST. There is no "round-trip-stable subset" issue as there is with surface markdown — every node round-trips by definition.
>
> *Explicit-tree storage.* Surface markdown stores structure implicitly (a blank line means paragraph break; `#` means heading; etc.). The AST stores structure explicitly as typed nodes. Any later analysis (the seven policy detectors; the chunking stage; the validate stage) operates on the explicit tree.
>
> *Pure data.* JSON is the universal serialization format. Standard Python tooling (`json` stdlib, `pydantic`, `panflute`) handles it. Diffing two `IntakeDoc` files is a structured-diff problem with mature solutions.
>
> *Queryable.* Need to find every footnote? Walk `apparatus.footnotes`. Need every Arabic span? Walk paragraph runs for `Span` nodes with `lang=ar`. The tree is enumerable; surface markdown requires re-parsing for the same queries.
>
> **Mapping to the prior finding's `IntakeDoc`.** The prior `IntakeDoc` was defined as a tree-of-containers (Document → Chapter → Section → Paragraph) + cross-referenced flat collections (footnotes, marginalia, embedded poetry, etc.). The Pandoc AST is structurally equivalent at the in-memory level. The only change from the prior is the **on-disk representation**: was Pandoc-md; now JSON-serialized AST.

**Mechanism log:**
- *Domain Transfer (computing-native):* Pandoc's documented AST is the computing-native source for the schema.
- *Combination:* Pandoc-AST + JSON serialization + pydantic project layer → the layered schema strategy.
- *Constraint Manipulation (ADD):* added "must be lossless round-trip" → AST wins over surface markdown.

**5-test:** PASS — concrete Pandoc commands; cited tools (pandoc-types, panflute); explicit relationship to prior IntakeDoc.

---

### P4 — F2: Hand-Edit Format = Pandoc's Markdown (REFINED ROLE)

**Principal candidate (content):**

> **F2 — The hand-edit format is Pandoc's markdown with the canonical extension set.**
>
> Users do not edit JSON. When intake produces a parse the user wants to fix by hand, they open a markdown version. The extension set is the same the prior finding committed for Pandoc's markdown: footnotes, pipe and grid tables, definition lists, citations (`@key`), YAML metadata blocks, raw attributes (`{=html}`), and bracketed spans (`[text]{lang=ar dir=rtl}` for inline language and direction tagging).
>
> **The hand-edit workflow.**
>
> ```
> 1. Intake produces canonical.json
> 2. User wants to fix something
> 3. pandoc -f json -t markdown canonical.json > edit.md
> 4. User edits edit.md in any text editor (VS Code, BBEdit, Vim, etc.)
> 5. pandoc -f markdown -t json edit.md > canonical_updated.json
> 6. Intake re-loads canonical_updated.json
> ```
>
> Pandoc's markdown is byte-stable in any UTF-8 editor that preserves bytes (VS Code, Sublime Text, BBEdit, modern Vim, JetBrains, TextEdit-in-plain-mode) — the failure mode RTF has (different editors re-serialize on save) does not occur. The user can pick whatever editor they prefer.
>
> **The round-trip-stable subset.** Not every Pandoc markdown feature round-trips with the JSON canonical losslessly. For example: a citation `@smith2020` survives both directions, but some auto-link constructs may emerge as explicit `<http://...>` after round-trip; some heading attributes may shift form. The **round-trip-stable subset** is the set of Pandoc-md features guaranteed to survive `md → json → md`. Defining this subset precisely is a downstream design task (see Next Actions). For v0.2 the working assumption is: every feature explicitly named in the canonical extension set (footnotes / tables / definition lists / citations / yaml metadata / raw attributes / bracketed spans) is round-trip stable; anything outside that set may not be.
>
> **Why markdown remains the right choice for THIS role.**
>
> *Human-readable.* A footnote is `[^1]: text`; an emphasized word is `*word*`; a chapter heading is `# Title`. The syntax is reading-order-natural and learnable in minutes.
>
> *Byte-stable.* Plain text. Any UTF-8 editor preserves it. The failure mode RTF has — editor-specific re-serialization on no-op save — cannot occur.
>
> *Familiar.* The user already knows markdown from the prior finding; the workflow is unchanged for them.
>
> *Prior Decision 1 preserved.* The prior choice of Pandoc's markdown was right for this role. The prior conflation made it carry MORE responsibility than it should have; the refined frame puts it in its appropriate scope.

**Mechanism log:**
- *Combination:* prior Decision 1 (Pandoc's markdown) + new role definition (hand-edit) → the role-preserved-with-narrowed-scope content.
- *Lens Shifting:* under "what is markdown actually good for?" lens — human authoring + casual reading + diffing in version control. The hand-edit role fits exactly.

**5-test:** PASS — concrete workflow; preserves prior commitment in a defensible narrower role.

---

### P5 — F3: Publishing Format = EPUB 3

**Principal candidate (content):**

> **F3 — The publishing format is EPUB 3.**
>
> When a translated text is ready to ship to readers, it is generated as an EPUB 3 file from the JSON canonical:
>
> ```bash
> pandoc -f json -t epub3 \
>     --metadata title="Translated Title" \
>     --metadata author="Said Nursi" \
>     --metadata language="en" \
>     --epub-cover-image=cover.png \
>     --css=publication.css \
>     -o translation.epub canonical.json
> ```
>
> EPUB 3 is the open W3C-anchored ebook standard (specification at idpf.org and w3.org). The format is a ZIP archive containing xhtml content files, an OPF manifest, metadata, and optional CSS / media. Pandoc's `epub3` writer handles the manifest construction; the user provides metadata flags.
>
> **Reader ecosystem.** EPUB 3 reads natively in:
>
> - Apple Books (macOS / iOS / iPadOS)
> - Google Play Books (Android / web)
> - Calibre (cross-platform desktop library + viewer)
> - Adobe Digital Editions (cross-platform)
> - Kobo eReader devices and apps
> - Foliate (Linux GTK reader)
> - Thorium (W3C-backed cross-platform reader)
>
> Plus dictionary-integration tools (Apple Books has built-in Arabic dictionary support for example), annotation tools, library managers.
>
> **Kindle compatibility.** Amazon **deprecated the .mobi format** on August 1, 2022. The Kindle Direct Publishing platform now expects EPUB or .azw3 / .kfx; the conversion path is **EPUB 3 → Send to Kindle → .azw3 / .kfx** (Amazon's converter; runs locally or via Amazon's web UI). Users do NOT generate .mobi directly; Amazon's tooling handles the conversion from EPUB 3. Pandoc has no native MOBI writer because the format is not openly specified (Amazon proprietary).
>
> **Why EPUB 3 wins for the publishing role.**
>
> *Packaged-book format.* One .epub = one whole book (multi-chapter Risale-i Nur volumes are naturally one EPUB each; multi-volume sets can be one .epub each).
>
> *Native lang / dir / footnote semantics.* xhtml inside EPUB 3 supports `lang=`, `dir=`, `epub:type="footnote"`, `<aside epub:type="annoref">` for marginalia. The seven policy targets from the prior finding map cleanly.
>
> *Wide ecosystem.* The reader-side tooling already exists; comprehenslate's role is to produce well-formed EPUB 3, not to build a reader.
>
> *Pandoc-native.* `pandoc -t epub3` produces standard-conforming EPUB 3 directly from the JSON canonical; no custom packaging code is required for v0.2.

**Mechanism log:**
- *Domain Transfer (publishing-native):* EPUB 3 is the publishing-domain canonical for ebooks.
- *Combination:* JSON canonical + Pandoc EPUB writer → the publishing pipeline.
- *Absence Recognition:* the prior finding did not explicitly name a publishing format; this absence created the conflation of intake-format with everything-format.

**5-test:** PASS — concrete Pandoc command; ecosystem cited; MOBI rejection grounded.

---

### P6 — Rejected Candidates Rationale

**Principal candidate (content):**

> Five candidates the user named or that the prior surfacing surfaced are rejected as canonical, each on structural grounds.
>
> **RTF — rejected.** Pandoc reads and writes RTF, but RTF is **editor-fragile**: opening an RTF file in Microsoft Word, Apple Pages, Apple TextEdit, or LibreOffice and saving with no edits produces a byte-different file in each editor. This is because each editor implements its own subset of the RTF spec plus its own extensions and re-serializes on save through its rich-text engine. The hand-edit recovery workflow (concept D5 in the prior intake-concepts finding) depends on byte-stability under no-op save — a property RTF cannot guarantee in any editor that interprets it as rich text. Additionally, RTF preserves raw typography (font face, font size, color) which the prior finding's Decision 2 (quality target = structure-preservation) commits to dropping; storing typography only to filter it later is wasted intake work. RTF survives in a different role: as an **accepted user-provided input format** that intake reads via Pandoc to produce the JSON canonical.
>
> **TEI — rejected as canonical, retained as future archival output frontier.** TEI (Text Encoding Initiative) is the scholarly-text-encoding gold standard, with native support for marginalia (`<note place="margin">`), apparatus criticus (`<app>`, `<rdg>`, `<lem>`), voice marking (`<said who="...">`), and multi-language (`xml:lang`). But: **Pandoc does not READ TEI**. Per Pandoc's documented format-support matrix (referenced in the user's earlier message), TEI appears as `→ TEI Simple` only — output, not input. Choosing TEI as canonical intake would force the project to implement a custom TEI reader, breaking the architectural lever from the prior finding's Decision 5 (Pandoc as universal converter). Additionally, TEI is verbose (5-10× the markdown equivalent for the same content) and requires TEI vocabulary expertise to hand-edit. TEI is recorded in this finding's frontier as a potential future archival-output format for scholarly use cases.
>
> **MOBI — rejected.** Amazon **deprecated the .mobi format on August 1, 2022**. Kindle Direct Publishing stopped accepting .mobi uploads; Kindle devices now use .azw3 / .kfx. Pandoc never supported MOBI in any direction (it is Amazon-proprietary, not openly specified). Naming MOBI as a candidate today is wrong-target: if Kindle distribution is the goal, the path is EPUB 3 → Send to Kindle → .azw3 / .kfx, which is concept F3 above.
>
> **EPUB 3 as canonical INTAKE — rejected (EPUB 3 IS adopted at the publishing layer).** EPUB 3 is the right format at the publishing layer (concept F3) but the wrong format at the intake canonical layer. As a ZIP archive of xhtml files plus a manifest plus metadata, EPUB 3 is heavyweight for hand-editing (the user would have to unzip, edit, re-zip, validate the manifest) and Pandoc's round-trip through EPUB is lossy at the canonical level (round-tripping `md → epub → md` drifts metadata, TOC structure, and class attributes). Apparatus criticus, while encodable via `epub:type="annoref"`, is not first-class as it is in TEI. EPUB 3 at the publishing layer (rendered from the JSON canonical) gets the ecosystem benefits without the intake-layer costs.
>
> **Custom format (custom JSON-AST or `.compldoc`) — rejected.** Pandoc's AST is already a custom AST — designed for cross-format conversion, mature, well-tested, with documented types and Python tooling (`panflute`, `pandoc-types-python`). Creating a project-specific JSON-AST schema or extending Pandoc-md into a `.compldoc` superset would reinvent what already exists. If the project later needs project-specific invariants (e.g., "every chapter has a title"; "every footnote reference resolves to an apparatus entry"), those can be enforced via a pydantic layer on top of the Pandoc AST — not as a separate custom format.

**Mechanism log:**
- *Combination:* per-candidate structural-rejection × the architectural commitment → consistent rejection rationale.
- *Constraint Manipulation (ADD):* added "must round-trip losslessly through Pandoc" → TEI rejected; "must support Amazon-supported format chain" → MOBI rejected.
- *Absence Recognition (redesign):* in a redesigned intake architecture, the rejected candidates are at the wrong layer or break the architectural lever.

**5-test:** PASS — each rejection cites a specific structural property; each is consistent with the three-format architecture.

---

### P7 — Calibration-Corpus AST Mappings

**Principal candidate (content):**

> The seven policy targets from the prior intake-concepts finding's Decision 4 each map onto the Pandoc AST as follows. For the calibration corpus (Said Nursi's Risale-i Nur), the specific structural elements that motivate each policy are named.
>
> **`SourceApparatusPolicy` — Hashiye (Nursi's marginalia).** AST `Note` node (Pandoc's footnote / note type) with a class attribute distinguishing marginalia from footnote (e.g., `class="marginalia"`). Preserved losslessly in JSON canonical. Rendered in EPUB 3 as `<aside epub:type="annoref">`. Editable in Pandoc-md as `[^id]` footnote with content block; class attribute on the footnote definition.
>
> **`EmbeddedPoetryPolicy` — Mevlana couplets in Nursi's prose.** AST `LineBlock` (Pandoc's line-block / verse-block type) with attribution metadata in a class or attribute (e.g., `class="couplet" attribution="Mevlana"`). Preserved. Rendered in EPUB 3 as `<blockquote class="poetry">` with line breaks. Editable in Pandoc-md as line block (`|` line prefixes).
>
> **`FormulaicOpeningPolicy` — Bismillah (and Hamd preambles).** AST `Para` (or `Div`) with class `formulaic-opening` and constraint of position-at-section-start. Preserved. Rendered in EPUB 3 with a CSS class for styling. Editable in Pandoc-md as a paragraph with a fenced-div class wrapper (`::: {.formulaic-opening} ... :::`).
>
> **`NonMainLangPartsPolicy` — Arabic spans within Turkish narrative (Qur'anic quotations, Hadith, technical terms).** AST `Span` with `lang=ar` + `dir=rtl` attributes via Pandoc's `bracketed_spans` extension. Preserved. Rendered in EPUB 3 as `<span lang="ar" dir="rtl">`. Editable in Pandoc-md as `[ٱلْحَمْدُ لِلَّٰهِ]{lang=ar dir=rtl}`.
>
> **`VoiceMarkingPolicy` — voice transitions (Nursi's authorial voice vs cited authorities like Qur'an or Hadith).** AST `Span` with class indicating voice (e.g., `class="voice-cited"`, `class="voice-author"`). Preserved. Rendered in EPUB 3 with CSS class. Editable in Pandoc-md as a bracketed span with class attribute.
>
> **`ArchaicRegisterPolicy` — Ottoman Turkish lexical or syntactic archaisms.** AST `Span` with class `archaic-register` and an optional attribute indicating the archaism category. Preserved. Rendered in EPUB 3 with CSS class. Editable in Pandoc-md as a bracketed span.
>
> **`HonorificsPolicy` — Islamic honorific markers (SAW / AS / RA / PBUH family following names).** AST `Span` with class `honorific` and an attribute naming the tradition. Preserved. Rendered in EPUB 3 with CSS class. Editable in Pandoc-md as a bracketed span attached to the personal-name span.
>
> **NFC diacritic normalization.** The prior finding's pipeline-stage C4 (normalize) commits to `unicodedata.normalize('NFC', s)` at intake. NFC is preserved through the Pandoc AST (UTF-8 storage); through Pandoc-md (also UTF-8); through EPUB 3's xhtml (also UTF-8). At no point in the three-format chain does the diacritic representation drift, provided NFC is applied once at intake.

**Mechanism log:**
- *Combination:* the seven policy targets × Pandoc AST node types → per-policy mapping.
- *Domain Transfer (Pandoc-native):* the AST node types (Note, LineBlock, Span, Div, Para) are Pandoc-native sources.
- *Absence Recognition:* the prior finding committed the seven detectors but did not specify their AST representations; this piece fills that gap.

**5-test:** PASS — each policy target has a concrete AST representation, an EPUB rendering, and a Pandoc-md form.

---

### P8 (META-DECISION) — Inherited Commitments Re-test on Prior Decision 1

**Principal candidate (content):**

> **The prior finding's Decision 1 is `REFINED`, not `OVERTURNED`.** This finding's frontmatter declares `refines: devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`. The right verb is `refines:` — not `corrects:` (the prior was not structurally wrong within its frame) and not `supersedes:` (the prior continues to apply with its scope narrowed).
>
> **Decision 1's three rationale parts, re-tested individually:**
>
> 1. *"Pandoc's markdown covers needed primitives off-the-shelf."* — **CONFIRMED for the hand-edit role.** With the canonical extension set (footnotes / pipe tables / definition lists / citations / yaml metadata blocks / raw attribute / bracketed spans), Pandoc-md represents every primitive the calibration corpus needs IN A HUMAN-READABLE WAY. This is exactly what the hand-edit format needs. The rationale stands for that role.
>
> 2. *"Single parser surface."* — **CONFIRMED across all three formats.** Pandoc reads and writes all three of: JSON-AST (the canonical), markdown (the hand-edit format), and EPUB 3 (the publishing format). The architectural lever from prior Decision 5 (Pandoc as universal converter) is strengthened, not weakened, by the three-format architecture.
>
> 3. *"Hand-editable."* — **CONFIRMED and now PRIMARY.** Pandoc-md's hand-editability was the load-bearing reason in the prior finding's rationale. It remains the load-bearing reason — just for a narrower role. The user opens markdown to edit; Pandoc round-trips with the JSON canonical; intake re-loads from the JSON.
>
> **What the frame-shift names.** The prior finding implicitly assumed that the canonical-intake format is ALSO the canonical-translate format AND the canonical-hand-edit format AND (implicitly) the publishing format. The three temporal layers were conflated. The refined frame separates them. The prior choice (Pandoc-md) is right for ONE of the three layers (hand-edit). A different format (Pandoc-AST-JSON) is right for the canonical intake/translate layer. A third format (EPUB 3) is right for the publishing layer.
>
> **The prior finding's other commitments (Decisions 2-5):** unchanged by this refinement.
>
> | Prior commitment | Status after this finding |
> |---|---|
> | Decision 2 — quality target = structure-preservation | **UNCHANGED**. The AST canonical preserves structure better than the prior surface-md canonical; structure-preservation is strengthened, not weakened. |
> | Decision 3 — `IntakeDoc` shape = tree-of-containers + cross-referenced flat collections | **UNCHANGED at the in-memory level.** The in-memory `IntakeDoc` IS the AST shape; the change is only the on-disk representation (was Pandoc-md; now JSON). |
> | Decision 4 — 7-policy intake-perception + translate-rendering split | **UNCHANGED.** The seven policy-perception detectors operate on the AST exactly as they would have operated on the prior `IntakeDoc`. |
> | Decision 5 — Pandoc + OCR architectural lever | **STRENGTHENED.** All three formats in the new architecture are Pandoc-native; the lever applies to every conversion. |
>
> No commitment from the prior finding is invalidated. The refinement is **scope-narrowing on Decision 1 + framing-expansion on the architecture**.

**Mechanism log:**
- *Combination:* prior rationale's three parts × the refined frame → per-rationale-part re-test.
- *Absence Recognition (patch):* the prior finding never named the temporal-layer split explicitly; the absence created the conflation.

**Piece-Level Inversion (required — P8 is meta-decision via relationship-label property):**

> *Inversion-candidate:* what if the prior Decision 1 should be OVERTURNED entirely — what if Pandoc's markdown was wrong even for hand-editing, and the right move is to replace it across all roles?
>
> *What follows under the inversion:* (a) the hand-edit format would need to be something other than Pandoc-md (maybe AsciiDoc? maybe a custom Markdown dialect?); (b) the prior finding's other commitments (the seven detectors, the IntakeDoc shape, Decisions 2-5) might also need re-test (cascade); (c) the relationship label would be `corrects:` or `supersedes:`, not `refines:`.
>
> *Why rejected:* Pandoc-md's hand-editability is structurally well-evidenced — plain text in UTF-8; byte-stable in any editor; familiar syntax; broad tool support. The prior finding's three rationale parts each re-tested above with HIGH-confidence confirmation FOR THE HAND-EDIT ROLE. Overturning would discard what works. The right verb captures the actual change: the FRAME widened, the prior CHOICE inside that frame remains correct for its appropriate scope.
>
> *Intervention-shape Inversion check:* P8 commits to `refines:` relationship label. Alternative shapes from the Vocabulary: `corrects:` (the prior was wrong), `supersedes:` (the prior is dead), `REVERT-REGRESSION` (n/a — there's no prior version to revert to), `REPAIR` (change-the-text-to-fix — this is what `refines:` already encodes when applied to a frame, not a fact). The relationship-label space has `refines / corrects / supersedes` as the structural alternatives; `refines:` is the right one because the prior's choice survives and the change is scope-narrowing.
>
> Verdict on Inversion: **rejected** — the prior is preserved in its appropriate scope; overturning would discard correct work.

**5-test:** PASS — each rationale part re-tested with cited evidence; the frame-shift is named; the relationship label is structurally justified.

---

### P9 — Transition Plan + Next Actions

**Principal candidate (content):**

> **What changes from the prior intake-concepts finding's plan.**
>
> The prior finding committed Pandoc-md as the on-disk canonical. The refined plan commits Pandoc-AST-as-JSON as the on-disk canonical, with Pandoc-md as a hand-edit format and EPUB 3 as a publishing format. Translated into specific changes:
>
> - The prior finding's pipeline-stage C5 (segment) targeted Pandoc's AST as a parsing intermediate, then committed the result to the IntakeDoc in-memory. The refined plan persists that AST directly to disk as JSON; the in-memory IntakeDoc is the deserialized AST.
> - The prior finding's quality concept D5 (intake-edit-after-parse) committed Pandoc-md as the hand-edit-on-disk form. The refined plan keeps this exactly — markdown is the hand-edit format — but the path now includes the JSON canonical as the authoritative form (markdown round-trips with it).
> - The prior finding's concept C1 (the `IntakeDoc` pydantic schema design) becomes refined: the schema is Pandoc's AST shape, optionally with a project-pydantic-layer for additional invariants.
> - **A new design task emerges**: the EPUB 3 generation pipeline (Pandoc invocation; metadata; per-chapter file structure; cover-image handling; CSS for typography).
> - **A new design task emerges**: defining the round-trip-stable Pandoc-md subset (which features are guaranteed to survive `md → json → md`).
>
> **What stays the same.**
>
> - The seven policy-perception detectors (B4-B10 in the prior finding) operate on the AST exactly as designed.
> - The OCR sub-pipeline (concept A3 in the prior) is unchanged — OCR feeds Pandoc, which produces the canonical AST.
> - The pipeline stages (parse / normalize / segment / validate / pre-validation / post-parse validation / metadata extraction) are unchanged in role; the segment stage's output is the AST rather than a separate IntakeDoc structure.
> - The quality target (structure-preservation) and metrics framing — unchanged.
> - The hand-edit recovery workflow in user-facing terms — unchanged (the user still opens markdown to fix bad parses).
>
> **Next-actionable inquiries (priority order):**
>
> **MUST 1.** Design the JSON-AST canonical schema. Decide whether to use Pandoc's native AST shape directly OR layer a project-specific pydantic schema on top for type safety and project invariants (e.g., "every chapter has a title"; "every footnote reference resolves"). Output: a `comprehenslate/intake/schema.py` module (or its equivalent in whatever module structure the project commits to). Spawn as a `/traverse` inquiry.
>
> **MUST 2.** Define the round-trip-stable Pandoc-md subset. Document which Pandoc-md features are guaranteed to round-trip with the JSON canonical losslessly, and which are not. This is the contract for the hand-edit workflow. Output: a specification file naming the supported features. Spawn as a `/traverse` inquiry (smaller scope than MUST 1).
>
> **COULD 1.** Design the EPUB 3 generation pipeline. Pandoc invocation flags; metadata extraction from AST; per-chapter file structure; cover-image handling; CSS for typography; embedded font handling for Arabic. Output: a `comprehenslate/publish/epub.py` module + a CSS template. Spawn after MUST 1 commits the schema.
>
> **COULD 2.** Prototype the AST → EPUB conversion on a Risale-i Nur sample. Take one volume; run intake; generate EPUB 3; open in Apple Books, Calibre, and Google Play Books; verify Arabic + marginalia + couplets + Bismillah render correctly. Output: a runnable script + a quality-report. Spawn after COULD 1 has an initial EPUB pipeline.
>
> **DEFERRED.** TEI as future archival output — revisit when scholarly archival need emerges. Custom format design — only revisit if the AST + markdown + EPUB layered architecture proves insufficient. Pandoc version pinning — operational concern; resolved by the engineering team's version policy.

**Mechanism log:**
- *Combination:* prior finding's tasks × refined architecture → per-task delta.
- *Extrapolation:* current sensemaking commitments + likely engineering ordering → priority sequence.
- *Absence Recognition:* identifying the NEW design tasks (EPUB pipeline; round-trip subset) that the refined architecture introduces.

**5-test:** PASS — concrete deltas; explicit next-actionable inquiries; priority order grounded in dependency analysis.

---

### P10 — Open Questions / Frontier

**Principal candidate (content):**

> **Open questions resolvable in the immediate next-action inquiries:**
>
> - **Schema choice within the JSON-AST canonical.** Use Pandoc's native AST shape directly, OR layer a project-specific pydantic schema on top? The pydantic layer would add type safety (typed Python access to nodes) and enforce project-specific invariants (e.g., "every chapter has a title"). The cost is maintaining a parallel schema. Resolution: MUST 1 inquiry.
>
> - **Round-trip-stable Pandoc-md subset.** Exactly which Pandoc-md features survive `md → json → md` losslessly? The canonical extension set (footnotes / pipe tables / definition lists / citations / yaml metadata / raw attributes / bracketed spans) is the working assumption; precise verification per feature is the work. Resolution: MUST 2 inquiry.
>
> - **EPUB 3 generation flags and per-chapter file structure.** Pandoc's epub3 writer has many flags; the right combination for the calibration corpus needs choosing. Resolution: COULD 1 inquiry.
>
> **Frontier — items deferred but not dismissed:**
>
> - **TEI as future archival output.** TEI Simple is Pandoc's only TEI output target. For scholarly archival use cases, generating TEI Simple from the AST canonical is feasible (`pandoc -f json -t tei`). When and whether to do this is a future decision based on whether scholarly archival is a real demand.
>
> - **Archival / historical preservation as a possible fifth temporal layer.** The three-format architecture covers intake/translate, hand-edit, and publishing. Archival (preserving translations for the long term in a format that will outlive Pandoc and EPUB) is a possible fifth layer; TEI or JATS could serve it. Flagged as frontier.
>
> - **Pandoc version pinning policy.** The AST shape can change between Pandoc versions; the project will need a version pinning policy. Operational concern; flagged.
>
> - **Translation-output workflow before EPUB publishing.** The translation pipeline produces translated `IntakeDoc` instances (also JSON-AST). The path from translated-AST to EPUB 3 needs explicit design (likely the same EPUB pipeline as COULD 1, applied to translated rather than source AST). Flagged for the COULD 1 inquiry to address.
>
> - **Per-translation-output format expansion.** Beyond EPUB 3, other output formats may be desired (PDF for print preview; reveal.js for slideshows; LaTeX for academic submissions). Each is a Pandoc-writable target from the AST canonical. Not addressed in this inquiry; available downstream.

**Mechanism log:**
- *Absence Recognition:* "what's not yet asked about the three-format architecture?" → open-questions list.
- *Extrapolation:* future evolution paths from the current commitments.

**5-test:** PASS — open questions tied to specific resolution paths; frontier items named with conditions.

---

### P1 — Executive Summary (produced LAST per dependency order)

**Principal candidate (content):**

> The canonical intake format for translations is not one format — it is three, each serving a different temporal layer of the pipeline. The **canonical intake + translate format** is Pandoc's Abstract Syntax Tree serialized as JSON: the lossless, queryable, explicit-tree representation that every translate-stage operation reads. The **hand-edit format** is Pandoc's markdown with the canonical extension set: human-readable, byte-stable in any UTF-8 editor, round-trippable with the JSON canonical via Pandoc. The **publishing format** is EPUB 3: the open standard with the largest reader ecosystem and a clean Pandoc-generated path from the JSON canonical. This **refines** the prior intake-concepts finding (`devdocs/inquiries/2026-06-17_00-49__document_intake_handling_concepts/finding.md`) — its choice of Pandoc's markdown was right for the hand-edit role but was wrongly framed as monolithic across all layers. Decision-mode is **SUBSTITUTE**: substitute the monolithic frame with the three-layer frame; substitute Pandoc-md (as canonical intake) with Pandoc-AST-as-JSON; preserve Pandoc-md in the hand-edit role; add EPUB 3 at the publishing layer. RTF / TEI / MOBI / EPUB-as-intake / custom-format are rejected as canonical with structural reasons. The user's pushback was the correct signal — markdown alone wasn't enough — but the resolution is architectural (decouple the layers) rather than format-substitution (RTF or EPUB or new).

**Mechanism log:**
- *Combination:* the three formats + decision-mode + relationship-label + user-question-answer → the one-paragraph digest.
- *Lens Shifting:* under "what does the user need at-a-glance?" lens.

**5-test:** PASS — addresses the literal user question; names the three formats; names the decision-mode; names the relationship to the prior; sized for one-paragraph reading.

---

## Inherited Frame Audit (between Phase 2 and Phase 3)

**Step (i) — Seed central assumption.** The seed framing assumes the SV6 verdict from sensemaking (three-format layered architecture; SUBSTITUTE decision-mode; prior Decision 1 REFINED). Central assumption: **the three-format architecture is correct.**

**Step (ii) — Per-piece commitments.** Meta-decision pieces: P2 (architecture + decision-mode; framing-semantic + relationship-label) and P8 (Inherited Re-test; relationship-label). Both had Piece-Level Inversion applied.

**Step (iii) — Challenge scan.** Are there candidates challenging the central assumption?
- P2's Inversion-candidate explicitly tested "what if the monolithic frame was right" — rejected with structural evidence.
- P8's Inversion-candidate explicitly tested "what if OVERTURN, not REFINE" — rejected with structural evidence.
- P6 (rejections) explicitly tested the alternative formats (RTF, TEI, MOBI, EPUB-as-canonical, custom) and structurally rejected each.
- The Methodology-Mode override (Contrarian-rethink rejected) addressed the run-level challenge.

**Step (iv) — Firing condition.** Audit **does NOT fire**. Every meta-decision piece's commitment received an explicit Inversion-candidate that was tested structurally and rejected with cited evidence. Proceed to Phase 3 Test.

---

## Phase 3 — Test + Assembly

### Per-piece 5-test summary

All 10 pieces' principal candidates passed the 5-test cycle. Inversion candidates at P2 and P8 were generated, tested, and rejected with structural reasoning — compliance per the Piece-Level Inversion Rule.

### Assembly check

> **Does the architecture emerge from the 10 pieces' assembly?**
>
> **YES.** P1 gives the at-a-glance answer; P2 commits the architectural frame + relationship label; P3-P5 specify the three formats; P6 documents the rejections that justify the three choices over alternatives; P7 confirms the calibration corpus implications; P8 documents the inheritance relationship with cited evidence; P9 names the transition + next actions; P10 names the frontier. Read in dependency order, the assembled finding tells a coherent story that resolves the user's pushback structurally.

### Axis coverage check

Orthogonal axes the candidate space varies along:
- **Temporal-layer axis** (intake/translate / hand-edit / publishing) — varied: 3 format pieces, one per layer.
- **Decision-mode axis** (validate / substitute / design-new) — varied at P2; SUBSTITUTE committed with rejection-rationale for the others (P6).
- **Surface-vs-AST axis** — varied: the canonical is AST; the hand-edit is surface markdown; the publishing is packaged-xhtml.
- **Pandoc-native axis** — varied: all three formats are Pandoc-native; rejected candidates fail this axis (TEI) or other axes (RTF, MOBI, custom).

All 4 orthogonal axes have ≥1 candidate variant. No single-axis collapse. PASS.

### Per-row mechanism-trace

The three format pieces (P3 / P4 / P5) each have explicit mechanism work (Combination + Domain Transfer + Constraint Manipulation + Absence Recognition). The five rejections in P6 each have explicit structural-reason mechanism. The seven AST mappings in P7 each have a per-policy combination. The two meta-decision pieces (P2 + P8) have Inversion-candidate work explicitly logged. No row-baseline silent inheritance.

---

## Telemetry

### Mechanism Coverage

- **Generators applied:** 4 / 4 (Combination · Absence Recognition · Domain Transfer · Extrapolation)
- **Framers applied:** 3 / 3 (Lens Shifting · Constraint Manipulation · Inversion)
- **Coverage:** FULL (all 7 mechanisms applied across the 10 pieces)
- **Convergence:** YES — Combination + Absence Recognition + Constraint Manipulation + Lens Shifting all converge on the three-format-layered-architecture commitment through different paths (high confidence).
- **Survivors tested:** 10 / 10 principal candidates + 2 Inversion-candidates (P2, P8) = 12 / 12 tested.
- **Failure modes observed:** None.

### Production-task additional telemetry

| Piece | Mechanisms | Classification | Inversion compliance |
|---|---|---|---|
| P1 | Combination, Lens Shifting | content-production | n/a |
| P2 | Lens Shifting, Combination, Constraint Manipulation (ADD+REMOVE), Absence Recognition (patch+redesign), **Inversion** | **meta-decision** | **satisfied** (intervention-shape considered: REFRAME-AS-BUG; alternatives REVERT-REGRESSION / REPAIR considered and rejected) |
| P3 | Combination, Domain Transfer (computing-native: Pandoc AST), Constraint Manipulation (ADD) | content-production | n/a |
| P4 | Combination, Lens Shifting | content-production | n/a |
| P5 | Combination, Domain Transfer (publishing-native: EPUB 3), Absence Recognition | content-production | n/a |
| P6 | Combination, Constraint Manipulation (ADD), Absence Recognition (redesign) | content-production | n/a |
| P7 | Combination, Domain Transfer (Pandoc-native), Absence Recognition | content-production | n/a |
| P8 | Combination, Absence Recognition, **Inversion** | **meta-decision** | **satisfied** (intervention-shape considered: refines vs corrects vs supersedes; refines committed with structural reason) |
| P9 | Combination, Extrapolation, Absence Recognition | content-production | n/a |
| P10 | Absence Recognition, Extrapolation | content-production | n/a |

### Verdict

**PROCEED** — full mechanism coverage; convergence on the three-format architecture through 4+ mechanisms; all candidates tested; 2 meta-decision pieces (P2 + P8) Piece-Level Inversion compliance satisfied; Inherited Frame Audit did not fire; Assembly + Axis coverage + Per-row mechanism-trace all PASS. No failure modes observed.
