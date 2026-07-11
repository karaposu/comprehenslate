# Sensemaking — canonical intake format deep dive

## User Input

Inputs: `_branch.md` + `articulate_simple.md` + `surfacing.md` (78 candidates across 10 format families + 4 criterion categories; 12 core formats + 14 core criteria; 10 concept-names; 6 frontier flags). Sensemaking directives include feature-matrix construction; steel-mans of RTF / EPUB 3 / TEI / MOBI / AST-as-storage; verdict on decision-mode `[validate-prior / re-decide-with-existing / design-new]`; explicit Inherited Commitments Re-test on prior Decision 1; the user's "core representative format" framing; publishing-vs-intake decoupling.

---

## SV1 — Baseline Understanding

The user pushed back on prior Decision 1 (canonical intake format = Pandoc's markdown) and named RTF, EPUB, MOBI, or a new format as alternatives. The inquiry must re-evaluate at depth. The first read: re-run the format choice with a wider candidate set and richer criteria, expecting either PRESERVE-with-caveats or SUBSTITUTE.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1.** The 7 policy classes (`NonMainLangPartsPolicy`, `SourceApparatusPolicy`, `VoiceMarkingPolicy`, `ArchaicRegisterPolicy`, `HonorificsPolicy`, `FormulaicOpeningPolicy`, `EmbeddedPoetryPolicy`) must be supportable — the canonical must let intake represent each policy's target element.
- **C2.** Calibration corpus (Risale-i Nur) carries marginalia (hashiye), embedded poetry (Mevlana couplets), formulaic openings (Bismillah), mixed Turkish-Arabic interleaving, Qur'anic quotations as non-main-language spans.
- **C3.** Pandoc is the architectural lever (prior Decision 5); the canonical-format choice depends on what Pandoc handles natively. **Critical:** per the user's pasted Pandoc format list, Pandoc reads/writes ↔︎ markdown / CommonMark / GFM / AsciiDoc / RTF / docx / EPUB 2/3 / FB2 / DocBook / JATS / HTML5 / OPML / ODT / Typst / JSON-AST / XML-AST. **Pandoc does NOT read TEI** (only writes `→ TEI Simple`). **Pandoc does NOT support MOBI** at all.
- **C4.** The user's intuition (RTF / EPUB / MOBI / new) is a real signal — must be honored substantively, not dismissed.
- **C5.** Prior Decision 1's rationale: (a) Pandoc-md covers needed primitives off-the-shelf; (b) single parser surface; (c) human-readable / hand-editable.
- **C6.** PDF extraction is OUT of this inquiry's scope (explicitly).
- **C7.** App UI + translation algorithm internals are OUT (inherited MQ4).
- **C8.** The format question is FOUNDATIONAL — affects every downstream decision in v0.2+.

### Key Insights

- **KI1.** The user's framing "core representative format which will be used for translations" is **ambiguous across temporal layers**: (a) intake-time canonical (what intake produces after parsing); (b) translate-time canonical (what translate operates on); (c) storage / publishing canonical (what the project archives / ships). The prior Decision 1 conflated all three into one. The user's pushback may resolve as wanting them DECOUPLED — or wanting ONE format that covers all three but better than markdown.

- **KI2.** Three temporal layers + three plausible architectural answers:
  - Intake-time + translate-time: lossless round-trip matters most → **AST-as-storage wins**.
  - Hand-editing: human-readability matters most → **markdown wins** (Pandoc's markdown specifically).
  - Publishing: reader-format ecosystem matters most → **EPUB 3 wins** (the packaged-book format with the biggest ecosystem).
  No single format optimizes all three.

- **KI3.** The 12 core formats split into **five strategy families** at the architectural level:
  - **Surface markdown family** (Pandoc-md, CommonMark, AsciiDoc) — text-syntax-as-canonical.
  - **Rich-text family** (RTF) — proprietary-or-quasi-binary-as-canonical.
  - **Packaged-book family** (EPUB 3, MOBI, BITS) — zip-of-xhtml-as-canonical.
  - **Scholarly-XML family** (TEI) — verbose-XML-as-canonical.
  - **AST-as-storage family** (Pandoc-AST-as-JSON, custom JSON-AST, .compldoc) — parsed-tree-as-canonical.
  HTML5+ARIA sits between Surface-markdown and Packaged-book.

- **KI4.** **The user's pushback may not be about which surface format is better — it may be about whether SURFACE FORMAT vs AST-AS-STORAGE is the right strategy.** RTF "preserves more than markdown" because it stores typography. EPUB "preserves more" because it stores book structure. The pushback's common thread: markdown's SURFACE SYNTAX loses structural information that the AST would capture. The architectural fix is AST-as-storage, not a different surface format.

- **KI5.** **Pandoc's AST as canonical is essentially what the prior `IntakeDoc` was already doing.** The prior finding committed `IntakeDoc` as the in-memory representation, with Pandoc-md as the on-disk canonical. The architectural shift here is: make the JSON-serialized AST the **on-disk canonical too**, demoting Pandoc-md to a "hand-edit format" rather than the primary on-disk form.

- **KI6.** TEI's reputation as "scholarly text encoding gold standard" is real, but Pandoc's inability to READ TEI breaks the architectural lever from prior Decision 5. The cost of a custom TEI reader + the verbosity of TEI source + the requirement that hand-editors know TEI vocabulary together rule TEI OUT as canonical intake — but leave it open as a possible OUTPUT/ARCHIVAL format for scholarly publishing.

- **KI7.** MOBI is **deprecated by Amazon** (August 2022); Kindle moved to .azw3 / .kfx. Pandoc does not support MOBI. Including MOBI as a canonical candidate would be dishonest. Honest verdict: **MOBI OUT** with named rationale.

- **KI8.** The publishing-vs-intake decoupling resolves cleanly: intake-time canonical = AST-as-JSON; publishing format = EPUB 3 (rendered from AST via Pandoc). These are different layers with different optimal formats; trying to unify them forces compromises.

- **KI9.** Hand-editability is preserved EVEN with AST-as-canonical: users edit Pandoc-md (which round-trips losslessly to JSON via Pandoc); intake reads the regenerated JSON. The prior Decision 1's "hand-editable" property survives — just in a narrower role (hand-edit format, not canonical).

### Structural Points

- **SP1.** The format choice has **two orthogonal axes**:
  - **SURFACE vs AST** (text-syntax-on-disk vs parsed-tree-on-disk).
  - **SINGLE-LAYER vs MULTI-LAYER** (one format covers all three temporal layers vs decoupled per layer).
- **SP2.** The 12 core formats place on these axes:
  - Pandoc-md / CommonMark / AsciiDoc / TEI / HTML5 / RTF / EPUB 3 = **SURFACE**.
  - Pandoc-AST-as-JSON / custom JSON-AST / .compldoc = **AST** (or hybrid).
  - Pandoc-md / CommonMark / AsciiDoc / HTML5 = **SINGLE-LAYER candidates** (intake only).
  - EPUB 3 / TEI / BITS = **MULTI-LAYER candidates** (intake → publishing).
- **SP3.** The emergent winning architecture: **AST-as-internal-canonical + Pandoc-md-as-hand-edit + EPUB-as-publishing-output**. Three formats, three layers, all Pandoc-native, fully decoupled. The prior monolithic-single-format thinking is the wrong frame.
- **SP4.** Decision-mode adjudicates to **SUBSTITUTE** — Pandoc-md is REFINED (its role narrows from monolithic canonical to hand-edit format); Pandoc-AST-as-JSON is SUBSTITUTED for the canonical role; EPUB 3 is ADDED at the publishing layer.

### Foundational Principles

- **FP1.** The format choice should follow the use case per layer, not force one format across all layers. Architecture-first, not format-first.
- **FP2.** Asymmetric-failure for canonical storage: **under-preserve is worse than over-preserve**. Information dropped at intake cannot be recovered downstream; verbosity / parser-cost can. Lean to over-preserve → AST-as-storage.
- **FP3.** The simplest sufficient choice is the right choice; complexity beyond sufficiency is debt. Custom format = unnecessary if Pandoc-AST does the job.
- **FP4.** Specialized tools for specialized jobs (EPUB for ebooks; TEI for scholarly editing; markdown for human authoring); forcing one format to do all is wrong.

### Meaning-Nodes

- **MN1.** **Canonical-intake-format = Pandoc-AST-as-JSON.** On-disk + in-memory; lossless round-trip via Pandoc.
- **MN2.** **Hand-edit-format = Pandoc's markdown.** User-facing editing target; round-trips with the JSON canonical.
- **MN3.** **Publishing-format = EPUB 3.** Rendered from AST via Pandoc; for translation outputs shipped as books.
- **MN4.** **The three-layer architecture.** The clean decoupling that resolves the user's pushback.
- **MN5.** **Decision-mode = SUBSTITUTE.** Refines prior Decision 1's role rather than overturning it; introduces a new canonical at the intake/translate layer.

### SV2 — Anchor-Informed Understanding

After anchor extraction, the question reframes: the user's pushback isn't asking "which surface format is better than markdown" — it's surfacing the prior finding's implicit conflation of intake / translate / publishing into one format choice. The right architectural move is to DECOUPLE the three temporal layers and let each have its appropriate format. Pandoc-AST-as-JSON is the canonical that bypasses surface-syntax limitations; Pandoc-md remains the hand-edit format; EPUB 3 emerges as the publishing layer. All three are Pandoc-native; the architectural lever survives.

---

## Phase 2 — Perspective Checking

### Technical / Logical

**Pandoc's actual format support matrix (per the user's pasted reference):**

| Format | Pandoc support |
|---|---|
| Pandoc's markdown | ↔︎ |
| CommonMark / GFM / commonmark_x | ↔︎ |
| AsciiDoc | ↔︎ |
| reStructuredText | ↔︎ |
| Org-mode / Muse / Textile | ↔︎ |
| Djot | ↔︎ |
| docx | ↔︎ |
| RTF | ↔︎ |
| ODT | ↔︎ |
| EPUB 2 / EPUB 3 | ↔︎ |
| FictionBook2 (FB2) | ↔︎ |
| MOBI | **NOT SUPPORTED** |
| TEI | **→ TEI Simple only** (output, not input) |
| DocBook 4/5 | ↔︎ |
| JATS | ↔︎ |
| BITS | **← only** (input, not output) |
| HTML5 | ↔︎ |
| LaTeX | ↔︎ |
| Typst | ↔︎ |
| Pandoc AST (JSON / XML) | ↔︎ (native) |

**Critical implications:**
- TEI loses Pandoc-as-architectural-lever (no read support).
- MOBI is entirely absent from Pandoc.
- BITS is asymmetric (can ingest BITS sources, can't output BITS).
- Pandoc-AST as JSON or XML is NATIVE both directions — the architectural lever is strongest here.

### Human / User

- The user's intuition (RTF / EPUB / MOBI / "new") clusters around "more structure than markdown surfaces" — not around a specific format.
- The user wants the canonical to be a **stable structural object** — not a fragile surface that varies by editor or by markdown-flavor.
- Honoring the user's intuition: AST-as-JSON IS what the user is reaching for. It's the parsed STRUCTURE itself, persisted. The user named surface alternatives because the AST-as-storage option wasn't on their radar.

### Strategic / Long-term

- The translation project will eventually ship translations as books. EPUB 3 ecosystem (Apple Books, Google Play Books, Calibre, Adobe Digital Editions, Kindle via .azw3 conversion) is the right publishing target.
- Decoupling intake from publishing means each can evolve independently. If Pandoc's AST changes, only the canonical changes; publishing pipeline stays.
- The choice cements at v0.2; reversing later is expensive.

### Risk / Failure

- **If TEI as canonical:** Pandoc-read broken → custom reader engineering → loses architectural lever. CONFIRMED PROBLEM.
- **If EPUB 3 as canonical INTAKE:** zip-archive heaviness → hand-editing degraded; lossy round-trip via Pandoc (md → EPUB → md drifts metadata). REAL ISSUE.
- **If RTF as canonical:** editor-fragility (multiple editor dialects produce different bytes on save) → hand-edit workflow defeated. CONFIRMED (prior).
- **If MOBI as canonical:** Pandoc doesn't support → custom everything; Amazon deprecated → no future. EXCLUDED.
- **If AST-as-JSON as canonical:** hand-editing JSON directly is hard; mitigated by using Pandoc-md as the hand-edit format (round-trips losslessly).
- **If custom format from scratch:** engineering cost without proportional benefit; Pandoc-AST already exists.

### Resource / Feasibility

- Pandoc-AST-as-JSON works TODAY: `pandoc -f markdown -t json input.md > output.json` and `pandoc -f json -t markdown output.json` round-trips losslessly.
- Pandoc-md hand-editing works TODAY.
- EPUB 3 generation works TODAY: `pandoc -f json -t epub3 -o output.epub canonical.json`.
- TEI custom reader: significant engineering cost; not justified given AST-as-JSON serves the same role.
- Custom format spec + parser: very significant cost; not justified.

### Definitional / Internal Consistency

- Prior Decision 1 (Pandoc-md as canonical on-disk) doesn't contradict "AST-as-internal-storage." The prior finding's `IntakeDoc` IS effectively the AST. Linking them: the on-disk canonical (JSON-AST) IS the serialized form of `IntakeDoc`; Pandoc-md is one renderable surface of it.
- The Inherited Commitment Re-test on prior Decision 1 will surface this: Pandoc-md was the right format for the ROLE the prior finding gave it (hand-edit-able on-disk canonical), but the role itself was wrong (conflated three layers). The refined role keeps Pandoc-md alive in a narrower scope.

### Definitional / Frame-exit Completeness

**Gating predicate check:** the inquiry's committed structures (the 12-format candidate set evaluated across 14 criteria) inherit terms from the prior finding (`IntakeDoc`, "canonical format", "intake-vs-translate boundary"). Used across distinct values: YES (these terms span multiple cells of the feature matrix). **Gating fires.**

1. **Existence Enumeration.** "Canonical format" project-wide referents: (a) on-disk canonical (the file format intake outputs and translate reads); (b) in-memory canonical (the `IntakeDoc` shape the runtime operates on); (c) hand-edit canonical (what users edit when fixing parses); (d) publishing canonical (what reader-shippings derive from). The prior finding collapsed (a) + (b) + (c) into Pandoc-md and either implicit-deferred or omitted (d).

2. **Role Assessment.** Each referent has a distinct role: (a) on-disk = lossless persistence; (b) in-memory = type-safe operation; (c) hand-edit = human-readable + bidirectionally-stable with on-disk; (d) publishing = reader-friendly + ecosystem. **Three of four referents need different formats** — prior conflation was a structural mistake.

3. **Verdict Rigor.** Strongest counter to "decouple": "decoupling adds complexity and conversion steps." Tested: the conversion step IS a Pandoc operation (already in the architecture per Decision 5); decoupling adds zero NEW dependency and one cheap conversion. The complexity cost is bounded.

4. **Residual / Coverage Justification.** Other frame-exit concerns: is there a layer I missed? Translation-time in-memory representation IS the in-memory canonical (b); already covered. Archival/historical preservation MAY be a fifth layer; flagged for frontier.

### Phase / Calibration-State

Project state: v0.1 Mac app; no intake stage exists yet; canonical-format choice is being made BEFORE engineering commits. This is the right time to revisit; the reversal cost is low.

Calibration corpus: Risale-i Nur (multi-volume; marginalia; mixed-script; formulaic openings; embedded poetry). The choice must serve this corpus first; generalization comes later.

### Meta-Inspection — H1 (candidate set)

- The 12 core formats span surface formats + AST. **One missing axis I'd add:** the "wrapping" strategy (markdown body + side-files for apparatus). This is what `.compldoc` was; effectively covered by G05. ✓
- H4 (concept names): "AST-as-storage" is structurally distinctive — different round-trip semantics from surface storage. Not a proxy. ✓
- H5 (motivating examples): the user named RTF, EPUB, MOBI, "new." The Specific-vs-pattern check fires: their examples reveal a PATTERN — "markdown surfaces lose structure" — that the analysis must address at the pattern level (which it does: AST-as-storage), not just by responding to each named format.

### SV3 — Multi-Perspective Understanding

After perspective checking:

1. **The user's pushback resolves not as a different surface format but as a different STRATEGY**: AST-as-storage rather than surface-syntax-as-storage.
2. **Publishing-vs-intake decoupling is the architectural insight.** Intake/translate canonical = AST-as-JSON; publishing = EPUB 3.
3. **TEI's status downgrades** because Pandoc can't read it (no architectural lever).
4. **RTF's editor-fragility verdict from prior holds** AND is amplified — AST-as-storage offers the structural richness RTF aimed at without the editor-fragility cost.
5. **EPUB 3 is the right answer at the PUBLISHING layer**, not at the canonical-intake layer (zip-archive heaviness + lossy intake round-trip).
6. **The design-new path is unnecessary** — Pandoc-AST-as-JSON does what a custom AST would do, with the architectural lever (Pandoc) preserved.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — The user's framing: what does "core representative format" mean?

**Ambiguity:** Does "core representative format which will be used for translations" mean (a) intake-time canonical only, (b) translate-time canonical, (c) storage canonical across the whole pipeline, or (d) some combination?

**Strongest counter-interpretation:** It means ONE format for everything — intake + translate + storage + publishing. That's why markdown's limitations matter: a single format must serve all roles, and markdown can't.

**Why the counter fails (structural grounds):** No single format optimizes all four temporal layers. Each layer has different optimal trade-offs (intake = lossless; translate = queryable; hand-edit = human-readable; publishing = ecosystem). Forcing one format = compromising all four. The prior finding's monolithic-Pandoc-md choice was already a compromise; doubling down by picking a different single format just shifts the compromise. The architecturally correct move is to **decouple the layers**.

**Confidence:** HIGH.

**Resolution:** "Core representative format" is interpreted as **the intake/translate-canonical layer** specifically — the format that intake produces and translate reads. Other layers (hand-edit, publishing) get their own formats. Decoupling is the architectural commitment.

**What is now fixed:** the layered-format architecture.
**What is no longer allowed:** monolithic-single-format thinking.
**What depends:** which format serves which layer.

### Ambiguity 2 — Decision-mode adjudication

**Ambiguity:** Is the decision-mode `validate-prior`, `re-decide-with-existing`, or `design-new`?

**Strongest counter for `validate-prior`:** Prior Decision 1 covers what we need; user's intuition is not grounded counter-evidence; markdown works fine.

**Why counter fails:** The user's intuition IS grounded — the prior conflated three layers into one (Ambiguity 1), and the right move is to decouple, which means substituting at the canonical-intake layer. Pure validate would preserve the conflation.

**Strongest counter for `design-new`:** No existing format perfectly fits the project's requirements; we should design from requirements.

**Why counter fails:** Pandoc's AST already IS a custom AST designed for cross-format conversion. Designing a NEW custom AST when Pandoc's exists + works + has Python tooling (panflute, pandoc-types) = reinventing what's already there. The architectural lever (Pandoc) gives us the AST design for free.

**Resolution:** Decision-mode = **SUBSTITUTE — substitute Pandoc-md (as the prior Decision 1's canonical-intake format) with Pandoc-AST-as-JSON, AND introduce EPUB 3 at the publishing layer, AND preserve Pandoc-md in a narrower hand-edit-format role.** The prior Decision 1 is REFINED (its role narrows) rather than wholesale OVERTURNED.

**Confidence:** HIGH.

**What is fixed:** decision-mode.
**What is not allowed:** validate-prior (the layered architecture changes substantively); design-new (Pandoc-AST suffices).

### Ambiguity 3 — Steel-man RTF

**Strongest case FOR RTF:**
- Pandoc ↔︎ RTF (officially supported).
- RTF preserves rich-text semantics (italic, bold, font, size, color).
- RTF is openable in Microsoft Word, Apple Pages, LibreOffice, TextEdit.
- If users want to hand-edit in a familiar word-processor, RTF lets them.

**Strongest case AGAINST RTF:**
- **Editor-fragility:** opening in Word vs Pages vs TextEdit vs LibreOffice produces different files on save with no edits (verified per the prior finding). The hand-edit recovery workflow REQUIRES byte-stability under no-op save.
- **Multiple RTF versions** (1.0–1.9.1) + **editor-specific dialects** create round-trip ambiguity.
- **Encoding fragility:** mixes Windows code-pages + Unicode escapes + UTF-8 within the same document; editors disagree on read/write.
- **Raw typography is the wrong kind of richness** for translation: the prior Decision 2 commits to structure-preservation, dropping raw typography (font face / size / color). Storing it via RTF means storing info we then have to filter — anti-architectural.
- **Span-level lang= attribute is awkward in RTF** (RTF has language codes but not portably at the span level).

**Resolution:** RTF survives as an **accepted user-provided format** (intake's Pandoc reader accepts RTF) but is **rejected as canonical intake**. The user's intuition that "RTF preserves more than markdown" is correct in one sense (typography) but wrong-target (typography is decoration; we want structural richness, which AST-as-JSON provides).

**Confidence:** HIGH.

### Ambiguity 4 — Steel-man EPUB 3

**Strongest case FOR EPUB 3:**
- Packaged-book format: one .epub = whole book (multi-volume Risale-i Nur is naturally an EPUB).
- Native `lang=` and `dir=` attributes via xhtml (W3C-spec).
- Native footnote semantics (`epub:type="footnote"`; `<a epub:type="noteref">`).
- Native marginalia via `<aside epub:type="annoref">`.
- Native multi-language + metadata via OPF + DC metadata.
- Pandoc ↔︎ EPUB 3 (officially supported).
- **Massive ecosystem**: hundreds of EPUB readers (Apple Books, Google Play Books, Calibre, Adobe Digital Editions, Foliate, Kobo) + dictionary integrations + annotation tools.

**Strongest case AGAINST EPUB 3 as INTAKE canonical:**
- **Heavyweight:** zip archive with manifest + multiple xhtml files + metadata; not single-file editable.
- **Hand-editing is degraded:** opening an .epub in a text editor requires unzipping; round-trip in EPUB-aware editors (Sigil) is editor-specific.
- **Apparatus criticus / scholarly marginalia is not first-class** — EPUB 3 doesn't have native `<app>` `<rdg>` `<lem>` like TEI; the apparatus is encodable but awkward.
- **Lossy round-trip via Pandoc:** md → EPUB → md doesn't preserve all metadata (TOC structure can drift; class attributes may not survive).
- **The IntakeDoc tree-plus-cross-ref structure** maps onto EPUB but adds the file-structure layer (each chapter is its own xhtml file in the zip).

**Resolution:** EPUB 3 is the **WRONG ANSWER for canonical INTAKE** but the **RIGHT ANSWER for canonical PUBLISHING**. Decoupling per Ambiguity 1 resolves both: intake canonical = AST-as-JSON; publishing canonical = EPUB 3 (generated from AST via Pandoc).

**Confidence:** HIGH.

### Ambiguity 5 — TEI

**Strongest case FOR TEI:**
- Designed exactly for scholarly text encoding (textencodinginitiative.org).
- Native marginalia: `<note place="margin">`.
- Native apparatus criticus: `<app>`, `<rdg>`, `<lem>`, `<witList>`.
- Native voice marking: `<said who="...">`.
- Native multi-lingual: `xml:lang` attribute everywhere.
- Native critical-edition support including manuscript witnesses.
- Used by Princeton, Oxford, Brown, the TEI Consortium.

**Strongest case AGAINST TEI:**
- **Pandoc DOES NOT READ TEI as input** (per the user's pasted format list: `→ TEI Simple` is OUTPUT only). This breaks the architectural lever (Pandoc-as-converter from user formats to canonical). A TEI canonical would require a CUSTOM TEI reader — significant engineering.
- **Verbose:** a simple paragraph in TEI is 5-10x the markdown equivalent. Hand-editing requires TEI vocabulary expertise (`<p>`, `<lb/>`, `<seg type="..."/>`).
- **TEI has many subset profiles** (TEI All, TEI Simple, TEI Lite, TEI-P5); no single "TEI" but a family of subset choices. Picking one is a design decision in itself.
- **Schema validation requires TEI's RNG schema** — non-trivial Python integration.

**Resolution:** TEI is **REJECTED as canonical INTAKE** (Pandoc-read absence + verbosity). TEI may be a valuable **OUTPUT/ARCHIVAL format** for scholarly publishing use cases — documented in the frontier for revisit.

**Confidence:** HIGH.

### Ambiguity 6 — MOBI (honest adjudication)

**Honest statement:** Amazon **deprecated MOBI on August 1, 2022**. The Kindle Direct Publishing platform stopped accepting .mobi uploads; the supported formats are now EPUB, .azw3, and .kfx. Pandoc does not support MOBI in any direction. Naming MOBI as a canonical candidate without addressing this is dishonest.

**Resolution:** MOBI is **REJECTED**. If Kindle distribution is needed, the path is: canonical → EPUB 3 → Send to Kindle (Amazon's converter to .azw3 / .kfx) OR `kindlegen` / `kindlepreviewer`. The user's intuition "MOBI is good" was reasonable a few years ago; today EPUB 3 is the correct Kindle-compatible answer.

**Confidence:** HIGH.

### Ambiguity 7 — AST-as-storage strategy

**Strongest case FOR Pandoc-AST-as-JSON (G01):**
- **Pandoc native ↔︎:** `pandoc -t json input.md > output.json` writes the AST; `pandoc -f json -t markdown output.json` reads it back. Lossless round-trip by Pandoc's design.
- **Schema-validatable:** the AST shape is documented in pandoc-types (Haskell library; mirrored in Python via panflute / pandoc-types-python).
- **Bypasses surface-syntax limitations:** whatever Pandoc's parser perceived (including bracketed_spans, footnotes, citations, raw_attribute escapes) is in the AST.
- **Pure data:** can be ingested into pydantic models, queried via JSONPath, transformed via panflute filters.
- **The IntakeDoc maps cleanly onto it:** the prior finding's tree-of-containers + apparatus-flat-collections shape is expressible in Pandoc's AST (Header / Para / Note / Span / Div nodes).

**Strongest case AGAINST Pandoc-AST-as-JSON:**
- **Not human-readable as canonical:** JSON is text but the AST is nested objects; hand-editing requires AST understanding.
- **Pandoc-specific:** ties the project to Pandoc as a hard dependency.
- **AST schema can change between Pandoc versions:** versioning concern.

**Counter to the counter:** hand-editability is served by using Pandoc-md as the hand-edit format. Pandoc-specificity is already a commitment (prior Decision 5 = Pandoc as architectural lever). AST versioning is mitigated by pinning Pandoc version (already standard practice).

For **custom JSON-AST (G03):** rejected as unnecessary engineering. Pandoc's AST design is mature; recreating it adds cost without proportional benefit.

For **.compldoc (G05):** the layered architecture (AST + md + EPUB) renders .compldoc unnecessary. The wrapping strategy (markdown body + YAML metadata) is what Pandoc-md WITH bracketed_spans + yaml_metadata_block already does.

**Resolution:** **AST-as-storage = ADOPT**, with **Pandoc-AST-as-JSON (G01) as the canonical**. Custom JSON-AST and .compldoc rejected.

**Confidence:** HIGH-MED.

### Ambiguity 8 — Publishing-vs-intake decoupling

**Strongest counter:** decoupling adds complexity (more formats; more conversions; more code paths).

**Why counter fails:** the conversion AST → EPUB 3 is a single Pandoc command (`pandoc -f json -t epub3`). Already a Pandoc operation per prior Decision 5. Decoupling adds zero new dependency and a cheap one-shot conversion. The complexity is bounded and architectural-cleanliness is high.

**Resolution:** **DECOUPLE.** Intake/translate canonical = Pandoc-AST-as-JSON. Publishing format = EPUB 3 (generated from AST via Pandoc).

**Confidence:** HIGH.

### Ambiguity 9 — Load-bearing concept test: "AST-as-storage"

**Strongest counter to AST-as-storage as a load-bearing concept:** it's just markdown's parse-tree; calling it a "strategy" is over-naming.

**Why counter fails (structural grounds):** AST-as-storage IS structurally distinct from surface-syntax storage. Surface-syntax storage has round-trip-stable subsets (Pandoc-md's round-trip-stable subset is smaller than full Pandoc-md); the AST has no such subset issue (every node round-trips by definition). The distinction is real and load-bearing.

**Resolution:** "AST-as-storage" is committed as the **strategic concept name** for the canonical layer.

**Confidence:** HIGH.

### SV4 — Clarified Understanding

After ambiguity collapse, the model commits to:
- **Three-format layered architecture**: AST-as-JSON (canonical intake/translate) + Pandoc-md (hand-edit) + EPUB 3 (publishing).
- **Decision-mode = SUBSTITUTE.** Prior Decision 1 is REFINED.
- **TEI / MOBI / RTF / custom = OUT** as canonical.
- **EPUB 3 = ADOPTED** at the publishing layer (not intake).
- **Inherited prior Decision 1's hand-editability rationale is preserved**, just at a narrower scope.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed

- Three-format layered architecture (intake/translate canonical / hand-edit / publishing).
- **Intake/translate canonical = Pandoc-AST-as-JSON.**
- **Hand-edit format = Pandoc's markdown** (prior Decision 1 in a refined role).
- **Publishing format = EPUB 3.**
- Pandoc as architectural lever (preserved from prior Decision 5; reinforced by all three formats being Pandoc-native).
- TEI / MOBI / RTF / Custom-format rejected as canonical.
- RTF retained as accepted user-provided input format (intake reads it via Pandoc).

### Eliminated

- Monolithic single-format-for-everything thinking.
- Pandoc's markdown as canonical on-disk format for intake/translate (REFINED role: hand-edit format).
- TEI as canonical (Pandoc-read absent).
- MOBI in any form (deprecated).
- RTF as canonical (editor-fragility + wrong-kind-of-richness).
- Custom-format design (unnecessary given Pandoc-AST).
- EPUB 3 as canonical INTAKE (heavyweight; lossy round-trip).
- AsciiDoc / CommonMark / HTML5 as canonical (no advantage over Pandoc-AST).

### Remaining variables (downstream inquiries)

- Schema for the canonical Pandoc-AST-as-JSON: use Pandoc's native shape directly, or layer a project-specific pydantic schema on top for type safety?
- The round-trip-stable subset of Pandoc-md for the hand-edit format: define which Pandoc-md features are guaranteed to round-trip with the JSON canonical.
- EPUB 3 generation flags: Pandoc invocation; metadata; per-chapter file structure; embedded CSS for typography.
- TEI as a future ARCHIVAL output: when (if ever) to add?
- Pandoc version pinning policy.
- The transition path from prior Decision 1's monolithic commitment to this layered architecture.

### SV5 — Constrained Understanding

The canonical-intake-format question resolves cleanly into a layered architecture: three formats, three roles, all Pandoc-native, fully decoupled. The prior Decision 1 is REFINED — Pandoc-md's role narrows from "monolithic canonical" to "hand-edit format." A new canonical (Pandoc-AST-as-JSON) replaces the prior at the intake/translate layer. A publishing layer (EPUB 3) is added. All three formats round-trip via Pandoc; the architectural lever is preserved and amplified.

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Did perspectives keep destabilizing the model? **No.** Once KI1 (the three-temporal-layer ambiguity) emerged in Phase 1, the model stabilized. Phase 2 perspectives confirmed (the Pandoc-format-support data sharpened the rejections of TEI/MOBI; the user-intuition perspective confirmed that AST-as-storage IS what the user was reaching for). Phase 3 ambiguity collapses refined the details without forcing model patches. The "AST-as-storage" reframe was the key load-bearing insight; everything else followed.

### Self-Reference Blindness check

Is the inquiry's subject the framework being applied? **No.** Subject = format choice for translation pipeline. Framework = sensemaking. Different substrates. External anchors: Pandoc's documented format support matrix (the user's pasted reference); the prior intake-concepts finding; the schema. Strong external grounding.

### SV6 — Stabilized Model

The canonical-intake-format question resolves to a **three-format layered architecture** that decouples intake/translate from publishing while preserving hand-edit affordances. The prior Decision 1's monolithic frame is refined — Pandoc's markdown's role narrows, and two additional formats fill the layers the prior conflated.

**The three formats and their roles:**

1. **Canonical intake + translate format = Pandoc's AST serialized as JSON** (Pandoc's `-t json` / `-f json` round-trip).
   - On-disk representation of intake output.
   - In-memory `IntakeDoc` is the deserialized AST.
   - Lossless round-trip via Pandoc.
   - Schema-documented via pandoc-types library; validatable via JSON Schema.
   - Maps cleanly to the prior finding's `IntakeDoc` tree-of-containers + apparatus-flat-collections.

2. **Hand-edit format = Pandoc's markdown** (with the canonical extension set from the prior finding: footnotes / pipe_tables / definition_lists / citations / yaml_metadata_block / raw_attribute / bracketed_spans for lang+dir).
   - When users hand-edit bad parses, they open the markdown.
   - Pandoc converts JSON ↔ markdown losslessly within the round-trip-stable subset.
   - The prior Decision 1's choice of Pandoc-md is RIGHT for this role.

3. **Publishing format = EPUB 3.**
   - For shipping translated books.
   - Generated from the AST canonical via Pandoc (`pandoc -f json -t epub3 -o out.epub`).
   - Rich reader ecosystem (Apple Books, Google Play Books, Calibre, Adobe Digital Editions, Kobo).
   - MOBI is REJECTED — Amazon-deprecated; .azw3 conversion from EPUB 3 via Send to Kindle covers Kindle distribution.

**Decision-mode = SUBSTITUTE.** The prior Decision 1 is REFINED — Pandoc-md's role shifts; AST-as-JSON substitutes at the canonical-intake layer; EPUB 3 is added at the publishing layer.

**The user's pushback was justified.** Markdown DOES have limitations as a canonical — not because Pandoc-md is missing features (it has bracketed_spans, footnotes, yaml metadata, etc.) but because **surface-syntax storage is structurally fragile** (round-trip subset varies; the parse-tree is implicit). AST-as-storage is the right strategy. RTF / EPUB / MOBI / custom-format were intuition-correct (markdown alone wasn't enough) but wrong-target (RTF / MOBI are wrong; EPUB belongs at a different layer; custom is unnecessary given Pandoc-AST).

**Inherited Commitments Re-test — prior Decision 1:**

The prior rationale (Pandoc-md covers Risale-i Nur primitives off-the-shelf; single parser surface; hand-editable) is **REFINED, NOT OVERTURNED**:
- "covers needed primitives off-the-shelf" — TRUE for the hand-edit role.
- "single parser surface" — TRUE; Pandoc handles all formats including the new JSON canonical.
- "hand-editable" — TRUE; this is now Pandoc-md's PRIMARY role.
- The rationale does NOT extend to "monolithic on-disk canonical for intake/translate." That role needs lossless round-trip and explicit-tree storage, which AST-as-JSON provides better. The prior Decision 1 made the right CHOICE within a wrong FRAME (single-format monolithic thinking); the refined frame keeps the choice valid for its appropriate scope.

**Verdict on Decision 1:** **PRESERVE the format choice (Pandoc-md), REFINE the role (hand-edit format, not monolithic canonical), ADD the AST canonical above it, ADD the EPUB publishing layer below it.** Net effect: the inquiry STRENGTHENS the architecture without invalidating the prior.

### Calibration-corpus implications (Risale-i Nur)

For each policy target:
- **Hashiye (marginalia):** AST `Note` node with class attribute; preserved losslessly in JSON; rendered in EPUB as `<aside epub:type="footnote">`; editable in Pandoc-md as `[^id]` footnote with content block.
- **Mevlana couplets (embedded poetry):** AST `LineBlock` with attribution class; preserved.
- **Bismillah (formulaic opening):** AST `Para` with class `formulaic-opening`; preserved.
- **Arabic non-main-language spans:** AST `Span` with `lang=ar` + `dir=rtl` attributes (via Pandoc's `bracketed_spans` extension); preserved.
- **NFC diacritic normalization** (per prior Decision C4) applied at intake; stable across all three formats.

All seven policy targets remain expressible in the AST; the prior intake-side perception detectors (B4-B10 in the prior finding) operate on the AST exactly as designed.

---

## How SV6 differs from SV1

| Dimension | SV1 (baseline) | SV6 (stabilized) |
|---|---|---|
| Frame | "Pick a better single canonical format" | "Decouple three temporal layers; pick the right format per layer" |
| Strategy axis | Surface-format-only | Surface + AST-as-storage |
| Canonical (intake/translate) | Pandoc-md (prior; questioned) | **Pandoc-AST-as-JSON** |
| Hand-edit | Same as canonical (prior) | **Pandoc-md** (refined role) |
| Publishing | Implicit / deferred | **EPUB 3** (explicit layer) |
| Decision-mode | Open (validate / re-decide / design-new) | **SUBSTITUTE — refine prior; add new canonical; add publishing** |
| User's intuition (RTF / EPUB / MOBI / new) | Asked at face value | Resolved structurally — the intuition pointed at AST-as-storage and at the publishing layer; the named candidates were the wrong-target proxies |
| Inherited Decision 1 status | Unclear | **REFINED, not OVERTURNED** |

The shift is from monolithic-single-format thinking to layered-architecture thinking. The user's pushback was the right signal; the technical resolution was AST-as-storage + explicit publishing layer.

---

## Self-Assessment

### Saturation indicators

- **Perspective saturation:** ✓ (perspectives 4-6 mostly confirmed Phase 1 anchors).
- **Ambiguity resolution:** 9/9 resolved (all HIGH or HIGH-MED).
- **SV delta:** substantial (SV1 was open candidate-comparison; SV6 commits three formats in three roles with refined Decision 1).
- **Anchor diversity:** 8 constraints + 9 insights + 4 structural points + 4 principles + 5 meaning-nodes; perspectives 6/6.

### Failure modes checked

- **Status Quo Bias:** no — the inquiry doesn't defend prior Decision 1 unchanged; it refines + substitutes + adds. The change is structurally substantial.
- **Premature Stabilization:** no — 9 ambiguities each tested with strongest counter.
- **Anchor Dominance:** no — KI1 (three-layer split) is load-bearing but doesn't carry every decision; KI4 (user-intuition-as-AST-storage-signal) + KI7 (MOBI deprecation) come from different evidence streams.
- **Perspective Blindness:** no — the Technical/Logical perspective produced the critical Pandoc-format-support data that flipped TEI from candidate to rejected.
- **Clean Resolution Trap:** tested on the three-format architecture. Strongest counter ("decoupling adds complexity") tested on structural grounds and found bounded.
- **Self-Reference Blindness:** no (subject is format choice; framework is sensemaking — disjoint).

### Meta-Inspection summary

- **H1 (candidate set):** tested — 12 core formats spanned five strategy families; one wrapping-strategy candidate (.compldoc) considered and resolved as unnecessary.
- **H2 (frame scope):** tested via Frame-exit Completeness perspective; the four temporal layers enumerated; intake/translate + hand-edit + publishing covered; archival flagged for frontier.
- **H3 (question framing):** the user's literal "core representative format" interpreted with explicit decomposition into temporal layers; the inquiry honors the literal ask while resolving its inherent ambiguity.
- **H4 (concept names):** tested — "AST-as-storage" is load-bearing structural distinction; "lossless round-trip" is operationally tractable; "editor-fragility" is the prior's load-bearing rejection reason still holds.
- **H5 (motivating examples):** the user's named candidates (RTF / EPUB / MOBI / new) tested as a PATTERN — they all point at "markdown surface loses structure" — rather than as four separate questions.
- **H6 (model fit):** no patching observed; Accommodation trigger not fired.
- **H7 (phase / calibration state):** v0.2 = pre-engineering; reversal cost is low NOW; the choice cements at v0.2 commit.

### Verdict

**PROCEED to Decomposition.** The stabilized model carries 1 architectural commitment (three-format layered architecture), 3 specific format choices (AST-as-JSON / Pandoc-md / EPUB 3), 1 decision-mode commitment (SUBSTITUTE), and an explicit Inherited Commitments Re-test verdict on prior Decision 1 (REFINED, not OVERTURNED).
