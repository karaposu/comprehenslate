# Sensemaking — post-repair canonical format

## User Input

Inputs: `_branch.md` + `articulate_simple.md` + `surfacing.md` (88 candidates; 5 core format-candidates + 1 emergent HTML5-as-universal; NEW provenance + confidence dimension; 6 frontier flags). Directives include capability matrix construction, decision-mode adjudication, HTML5-as-universal feasibility test, JSON-AST + HTML5 dual evaluation, user non-mention of JSON-AST honesty test, provenance dimension impact, verdict commitment, and Inherited Commitments Re-test of the prior canonical-format inquiry's three-format verdict.

---

## SV1 — Baseline Understanding

The prior canonical-format inquiry committed a three-format layered architecture: JSON-AST canonical + Pandoc-md hand-edit + EPUB 3 publishing. The user has pushed back asking "EPUB? md? html?" — naming only surface formats. The reconstruction-is-heavy reframe makes per-element provenance + confidence load-bearing. The question: re-test the prior verdict against this new evidence. The first read: likely the prior verdict's canonical-layer choice (JSON-AST) needs swap.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1.** Decisions 2-5 from the original intake-concepts inquiry are inherited unchanged (quality target = structure-preservation; IntakeDoc tree+cross-ref shape; 7-policy split; Pandoc + OCR lever).
- **C2.** Repair pipeline design is explicitly OUT-of-scope (user-stated in source input).
- **C3.** All 7 policy classes from `SKILL/references/config/schemas.py` must be supportable at intake-time perception representation.
- **C4.** Reconstruction produces RICH content: OCR-recovered Arabic spans + style-recovered emphasis + structure-detected markers + paratext-stripped body + apparatus-detected marginalia + policy-class-tagged elements + per-element provenance + confidence.
- **C5.** User explicitly named **EPUB / markdown / HTML** as candidates; the user did NOT name JSON-AST (the prior verdict).
- **C6.** User's framing pattern (naming "documents" — EPUB / md / RTF / EPUB / HTML — never naming JSON-AST / custom-data-structures) is consistent and is itself evidence.
- **C7.** Calibration corpus character (Risale-i Nur theological prose with marginalia + embedded poetry + mixed Turkish-Arabic + formulaic openings) unchanged.

### Key Insights

- **KI1.** **The user's non-mention of JSON-AST is a load-bearing signal**, not a casual omission. Their consistent pattern across multiple conversations is to name surface formats — they treat the canonical-format question as a DOCUMENT question, not a DATA-STRUCTURE question. Honest sensemaking honors this signal.

- **KI2.** **HTML5 is uniquely positioned among candidates.** It is the rare format that is simultaneously:
  - A document (human-readable as source markup; renders in any browser; can be opened in any text editor)
  - An explicit-tree (XML-like; semantic elements; the structural-tree property that JSON-AST has)
  - Web-standard (W3C-anchored; survives Pandoc deprecation)
  - The substrate of EPUB 3 (EPUB IS xhtml + manifest + metadata; HTML5 → EPUB is a near-identity transform)
  - Pandoc-native ↔︎ (per Pandoc's documented format list)
  - Has native `lang=` and `dir=` attributes (no extension needed; W3C-spec)
  - Has native `data-*` attribute mechanism for per-element provenance (W3C-spec)
  - Has semantic elements (`<section>`, `<article>`, `<aside>`, `<footer>`, `<blockquote>`, `<figure>`, `<span>`, `<em>`, `<strong>`) for the policy targets

- **KI3.** **The provenance + confidence dimension shifts the answer.** The prior canonical-format inquiry didn't consider per-element metadata (OCR confidence; source; hand-edit status; intake-pass history) because the prior's reframe was lossless-round-trip-of-content. The reconstruction reframe makes per-element provenance load-bearing — and the formats divide sharply:
  - **JSON-AST**: trivial (attributes on every node)
  - **HTML5**: trivial (data-* attributes on any element)
  - **Markdown**: awkward (no per-element metadata mechanism; requires sidecar files OR YAML extensions OR class-attribute overloading)
  - **EPUB OPF**: document-level metadata only; not per-element
  - **TEI**: native (`xml:*` attributes; `<respStmt>` for responsibility tags) but Pandoc-read absent

- **KI4.** **The three temporal layers are USE-CASES, not formats.** The prior inquiry conflated layer-with-format. Once decoupled, ONE format CAN serve multiple layers if it satisfies multiple use-cases. HTML5 does.

- **KI5.** **HTML5 → EPUB 3 is cleaner than JSON-AST → EPUB 3.** EPUB is xhtml at its core; using HTML5 as canonical means publishing is a minimal transform (package the HTML5 + add manifest + zip), not a Pandoc re-render that drifts.

- **KI6.** **Markdown remains the right hand-edit format.** HTML5 source is human-readable but has tag-noise that interrupts prose editing. Markdown is reading-order-natural. Two formats at different layers is fine when each layer's optimum is different — that's the prior architecture's load-bearing insight.

- **KI7.** **JSON-AST + HTML5 dual is unnecessary.** If HTML5 is canonical, JSON-AST is reachable on-demand (`pandoc -f html5 -t json`) but doesn't need persistence. A second on-disk canonical creates synchronization debt.

- **KI8.** **The prior architecture's load-bearing insight (three temporal layers with different optima) STANDS.** What changes: the canonical layer's specific format. JSON-AST was the prior pick; HTML5 is the refined pick. The architecture is preserved; one cell of it changes.

- **KI9.** **The user's intuition was right in a specific way.** Markdown alone isn't enough (true); EPUB is right for publishing (true); HTML is right somewhere (TRUE — at canonical). What was wrong in the user's framing: which layer each format fits. HTML5 fits CANONICAL more strongly than markdown or EPUB do.

- **KI10.** **The capability matrix is the right way to make this honestly.** Per-candidate × per-requirement support level, with cited evidence. The matrix produces the verdict; the verdict doesn't precede the matrix.

### Structural Points

- **SP1.** The three temporal layers (canonical / hand-edit / publishing) are USE-CASE distinctions independent of format choices. Format choices populate them.
- **SP2.** HTML5 satisfies more of the canonical-layer requirements than any other surface format AND ties with JSON-AST on the data-format requirements (lossless round-trip via Pandoc; explicit tree; queryable).
- **SP3.** Markdown remains the right hand-edit format for prose-heavy editing.
- **SP4.** EPUB 3 remains the right publishing format; HTML5 → EPUB is even cleaner than JSON-AST → EPUB.
- **SP5.** The new provenance + confidence dimension differentiates HTML5 and JSON-AST sharply from markdown and EPUB (at element level).
- **SP6.** The Pandoc-as-architectural-lever from the prior inquiry survives and is even strengthened — HTML5 is Pandoc-native ↔︎ and produces clean conversions to all the publishing targets.

### Foundational Principles

- **FP1.** Use-case-driven format choice, not format-driven use-case choice. Layers describe use-cases; formats fill them.
- **FP2.** Asymmetric-failure for canonical: over-preserve > under-preserve. HTML5's verbosity-over-markdown is acceptable because HTML5 over-preserves information; markdown's loss of per-element provenance is under-preservation.
- **FP3.** User-intuition-as-evidence. The user's preference for documents over data is a signal that informs the verdict's framing.
- **FP4.** Specialized vs universal: when a single format dominates multiple layers, the architecture should reflect that. HTML5 dominates canonical AND is the substrate of publishing; it should hold both roles.

### Meaning-Nodes

- **MN1.** **HTML5 as canonical** — the load-bearing architectural commitment.
- **MN2.** **Three-layer architecture preserved** — the prior inquiry's load-bearing insight survives.
- **MN3.** **Provenance + confidence dimension** — NEW from reconstruction reframe; differentiates formats sharply.
- **MN4.** **The user's document-vs-data preference** — load-bearing framing signal.
- **MN5.** **HTML5 → EPUB as near-identity transform** — strengthens the publishing path.

### SV2 — Anchor-Informed Understanding

The prior architecture's three-layer structure remains right; what changes is the canonical-layer format. HTML5 emerges as the strongest single candidate because it satisfies the canonical requirements (explicit-tree + lossless via Pandoc + per-element provenance via data-*) AND honors the user's document-vs-data intuition. The verdict is a SWAP within the preserved architecture — not a wholesale overturn, not a wholesale re-affirmation.

---

## Phase 2 — Perspective Checking

### Technical / Logical

**Pandoc format support for HTML5** (per the user's pasted Pandoc reference):
- `↔︎ HTML5` — read and write.
- `↔︎ XHTML` — strict XML mode.
- HTML5 → EPUB 3: trivial (EPUB is xhtml + manifest).
- HTML5 → PDF: via weasyprint, wkhtmltopdf, prince, pagedjs-cli (per Pandoc's PDF generation options).
- HTML5 → markdown: clean (Pandoc round-trips).
- HTML5 → JSON-AST: clean (any Pandoc input → JSON-AST output).

**W3C HTML5 spec capabilities** (verifiable at html.spec.whatwg.org):
- `lang` attribute: any element; W3C-spec-native.
- `dir` attribute: any element; values `ltr` / `rtl` / `auto`; W3C-spec-native.
- `class` attribute: any element; any value; W3C-spec-native.
- `id` attribute: any element; unique within document.
- `data-*` attributes: any element; arbitrary application-specific data; W3C-spec-native (HTML5 Living Standard §3.2.6).
- Semantic elements: `<section>`, `<article>`, `<aside>`, `<header>`, `<footer>`, `<nav>`, `<figure>`, `<figcaption>`, `<main>`, `<details>`, `<summary>`, `<blockquote>`, `<q>`, `<cite>`, `<em>` (emphasis), `<strong>` (strong importance), `<mark>`, `<small>`, `<time>`, `<address>`.
- All needed; all native.

**EPUB 3 ↔ HTML5 relationship**: EPUB 3 content documents ARE XHTML5 with EPUB-specific attributes (`epub:type=` for semantic indication). Converting HTML5 → EPUB 3 is essentially: package the HTML5 + add OPF manifest + zip.

### Human / User

The user's pattern: name documents (EPUB / md / RTF / HTML / MOBI / "new format"), not data (JSON / AST / schema). This is the second time they've done this. The verdict's framing should engage with their preference without being patronizing — confirm the verdict in their vocabulary (documents, not data).

The user's question phrasing is singular ("what should the end result be?"). They want clarity. The capability matrix gives clear comparative evidence; the verdict commits to ONE canonical (HTML5) within a preserved three-layer architecture.

### Strategic / Long-term

- HTML5 is W3C-standard. Survives Pandoc deprecation. Cross-vendor.
- JSON-AST is Pandoc-specific. Surviving Pandoc deprecation requires migration.
- Markdown-Pandoc is Pandoc-specific. Same.
- EPUB 3 is W3C/IDPF-standard. Cross-vendor.

HTML5-as-canonical reduces project lock-in to Pandoc. Pandoc is still the architectural lever for conversion (read other formats; generate EPUB / PDF / markdown), but the canonical itself is web-standard.

### Risk / Failure

- HTML5 verbosity at canonical layer: more bytes than JSON-AST per equivalent content. Acceptable; storage isn't a constraint.
- HTML5 as hand-edit: noisier than markdown; rejected for that role — markdown stays as hand-edit format.
- HTML5 parser variance: HTML5 parsing is well-specified; modern parsers (lxml.html, html5lib, jsdom) converge. Risk: low.
- HTML5 + class-attribute conventions: project must define and document its class-attribute conventions for the 7 policy targets. Risk: medium; mitigated by class-attribute convention spec (downstream design).

### Resource / Feasibility

- HTML5 generation via Pandoc: works today.
- HTML5 → EPUB via Pandoc: works today.
- HTML5 → PDF via weasyprint: works today.
- HTML5 → markdown via Pandoc (for hand-edit round-trip): works today.
- Schema validation: HTML5 DTD or RNG schemas exist; pydantic-style enforcement requires writing project-specific validators.

### Definitional / Frame-exit Completeness

**Gating predicate check:** the inquiry inherits commitments from the prior canonical-format inquiry (three-format layered architecture) and from the original intake-concepts inquiry (Decisions 2-5). Used across distinct values: YES (the three-layer architecture appears across multiple cells). **Gating fires.**

1. **Existence Enumeration.** "Canonical format" project-wide referents (from prior frame-exit analysis): (a) on-disk canonical; (b) in-memory canonical; (c) hand-edit canonical; (d) publishing canonical. Plus a new fifth one surfaced by this inquiry: (e) provenance + confidence metadata carrier. Five referents.

2. **Role Assessment.** The four prior referents are addressed by the preserved three-layer architecture. The new fifth referent (provenance + confidence) is addressed by the canonical layer's data-* attribute capability. HTML5 serves it natively; markdown doesn't. The new referent confirms the architectural choice rather than challenging it.

3. **Verdict Rigor.** Strongest counter to HTML5-as-canonical: "JSON-AST is leaner and equally lossless." Tested: HTML5 ties on losslessness (via Pandoc) AND wins on human-readability AND wins on web-standards portability AND wins on EPUB-substrate identity. The lean-vs-rich axis isn't load-bearing when storage isn't constrained.

4. **Residual / Coverage Justification.** Other frame-exit concerns: archival as a fifth temporal layer (from prior inquiry's frontier). Not directly addressed by HTML5 swap; archival's optimum (long-term-stable preservation) may still want TEI Simple as output. Flagged for frontier.

### Phase / Calibration-State

v0.2 hasn't been built. The prior canonical-format inquiry's verdict committed JSON-AST as canonical but no engineering exists on it yet. Reversal cost = near-zero NOW. The right time to swap.

### Meta-Inspection — H1 candidate set + H4 concept names

- **H1.** Candidate set: 5 core + 1 emergent. The emergent (HTML5-as-universal-canonical) should be PROMOTED to the verdict-bearing position. The set is complete.
- **H4.** "HTML5-as-canonical" — is this load-bearing structural distinction? Yes: it's a different category from JSON-AST (document vs data) AND from markdown (explicit-tree vs surface-syntax) AND from EPUB (per-element-attribute carriage vs packaged-document). Load-bearing.

### SV3 — Multi-Perspective Understanding

After perspectives, the model sharpens:

1. **HTML5 is uniquely positioned for the canonical role** — it satisfies more requirements than any single competitor (matched by JSON-AST on data-format properties but winning on document-readability + web-standards + EPUB-substrate).
2. **The three-layer architecture from the prior inquiry stands** — canonical / hand-edit / publishing remain distinct use-cases with different optima.
3. **The canonical-layer format swaps**: JSON-AST → HTML5.
4. **Hand-edit (markdown) and publishing (EPUB 3) preserved unchanged.**
5. **The provenance + confidence dimension confirms HTML5 over markdown** at canonical layer.
6. **JSON-AST + HTML5 dual is rejected** (synchronization debt).
7. **The user's non-mention of JSON-AST is a load-bearing signal** that the verdict honors by committing to HTML5 (document, not data).

---

## Phase 3 — Capability Matrix (the load-bearing artifact)

For the 5 core candidates × the load-bearing requirements (post-repair content + provenance dimension), with native (✓✓) / via-extension (✓+ext) / via-workaround (✓wa) / not-supported (✗) cells.

| Requirement | JSON-AST (B01) | Pandoc-md (B02) | HTML5 (B03/B17) | EPUB 3 (B06) | Custom .compldoc (B14) |
|---|---|---|---|---|---|
| A01 Arabic spans with `lang=ar` | ✓✓ (Span node attribute) | ✓+ext (`bracketed_spans` extension) | ✓✓ (W3C-native any element) | ✓✓ (xhtml is HTML5) | ✓+ext (inherits Pandoc-md) |
| A02 Arabic spans with `dir=rtl` | ✓✓ (Span attribute) | ✓+ext (`bracketed_spans`) | ✓✓ (W3C-native any element) | ✓✓ (xhtml is HTML5) | ✓+ext |
| A03 Italic-as-semantic-emphasis | ✓✓ (Emph node type) | ✓+ext (asterisks; AST Emph) | ✓✓ (`<em>` semantic element) | ✓✓ (xhtml is HTML5) | ✓+ext |
| A04 Bold-as-strong-emphasis | ✓✓ (Strong node) | ✓+ext (double-asterisks; AST Strong) | ✓✓ (`<strong>` semantic element) | ✓✓ | ✓+ext |
| A05 Marginalia (hashiye) with ref-to-body-position | ✓wa (Note node + class; ref via id) | ✓+ext (Pandoc footnote `[^id]`) | ✓✓ (`<aside>` + id/href) | ✓wa (`epub:type="footnote"`) | ✓+ext (Pandoc footnote + YAML) |
| A06 Embedded poetry (couplets) with attribution + verse-shape | ✓✓ (LineBlock + class + attrs) | ✓+ext (LineBlock syntax + fenced div) | ✓✓ (`<blockquote class>` + `<figure>` + `<figcaption>`) | ✓✓ | ✓+ext |
| A07 Formulaic openings with position-at-section-start | ✓wa (Para + class) | ✓+ext (fenced div) | ✓✓ (`<p class>` or `<section class>`) | ✓✓ | ✓+ext |
| A12 Chapter / section / paragraph hierarchical containment | ✓✓ (Header + Para nesting) | ✓+ext (headings + paragraphs; tree implicit) | ✓✓ (`<section>` + `<article>` + `<p>`) | ✓✓ | ✓+ext |
| A13 Cross-references (apparatus-ref → body-position) | ✓✓ (id + ref in Marker node) | ✓+ext (Pandoc citation/footnote ref) | ✓✓ (`href="#id"` + matching `id=`) | ✓✓ (xhtml is HTML5) | ✓+ext |
| **A18 Document-level provenance (source PDF, intake-time, hash)** | ✓✓ (top-level metadata; AST root attrs) | ✓+ext (YAML frontmatter) | ✓✓ (`<meta>` elements + `<head>`) | ✓wa (OPF metadata) | ✓+ext (YAML) |
| **A19 Per-element provenance (OCR confidence, source, hand-edit status)** | **✓✓** (attributes on every node) | **✗** (no per-element metadata mechanism without sidecar) | **✓✓** (`data-*` attributes on any element) | **✗** (no per-element OPF; only doc-level) | ✓wa (YAML sidecar referencing inline ids) |
| A07-policies tagged via class | ✓✓ (attrs) | ✓+ext (bracketed_spans class) | ✓✓ (class attribute native) | ✓✓ | ✓+ext |
| Round-trip with Pandoc | ✓✓ (lossless within version) | ✓wa (round-trip-stable subset) | ✓✓ (Pandoc ↔︎ HTML5; clean via AST) | ✓wa (lossy at metadata layer) | ✓+ext (markdown round-trip subset) |
| Human-readable as document | ✗ (data, not document) | ✓✓ (reading-order-natural) | ✓wa (markup; tag-noise but readable) | ✗ raw (zip) / ✓wa unzipped | ✓✓ (markdown body) |
| Schema-validatable | ✓wa (Pandoc AST documented; not formal JSON Schema published) | ✗ (no formal schema) | ✓✓ (HTML5 DTD / RNG / HTML5-Living-Standard) | ✓✓ (EPUB validation tools) | ✗ |
| Web-standard / non-Pandoc-lockin | ✗ (Pandoc-specific) | ✗ (Pandoc-md is Pandoc-specific) | ✓✓ (W3C standard) | ✓✓ (W3C/IDPF) | ✗ |
| EPUB 3 publishing path | via Pandoc render | via Pandoc render | **near-identity** (EPUB IS xhtml + manifest) | already EPUB | via Pandoc render |
| HTML web-output | via Pandoc render | via Pandoc render | **identity** (already HTML) | unzip + serve | via Pandoc render |
| PDF print-output | via Pandoc + LaTeX/HTML | via Pandoc + LaTeX/HTML | via weasyprint / wkhtmltopdf (direct) | via reader-export | via Pandoc + LaTeX/HTML |

### Per-candidate aggregate

**JSON-AST**: Strong on data-format properties (round-trip + provenance + queryable). Weak on document-readability. Pandoc-lockin.

**Pandoc-md**: Strong on hand-edit (human-readable; reading-order-natural). **Critically weak on per-element provenance** (A19 = ✗). Round-trip-stable subset issue.

**HTML5**: **Strong across the board.** Document AND data-shape. Native lang/dir/data-*. EPUB substrate. W3C standard. Schema-validatable. Per-element provenance ✓✓. Pandoc-native ↔︎.

**EPUB 3**: Strong at publishing layer (its purpose). Weak at canonical layer (heavyweight zip; per-element provenance ✗ at OPF level; lossy round-trip).

**Custom .compldoc**: Sub-derivative of markdown + YAML; inherits markdown's weaknesses on per-element provenance.

### The Pareto-dominant candidate (C04)

HTML5 dominates or ties every other candidate on every requirement except **hand-edit reading-order-naturalness** (where markdown wins) and **already-being-a-packaged-book** (where EPUB wins; but only because EPUB IS already packaged HTML5).

This is the structurally strongest finding: HTML5 is Pareto-dominant for the canonical layer.

---

## Phase 3.5 — Ambiguity Collapse

### Ambiguity 1 — Decision-mode

**Strongest counter for re-affirm-prior:** JSON-AST is still right; HTML5 is just a different surface for the same data; the verdict shouldn't shift on framing.

**Why it fails:** the matrix shows HTML5 ties JSON-AST on every data-property requirement AND wins on document-readability AND wins on web-standards-portability AND wins on EPUB-substrate-identity AND ties on per-element provenance. When a candidate Pareto-dominates the incumbent on the canonical layer, the verdict should reflect that. The prior didn't consider HTML5-as-canonical because the prior's framing was format vs Pandoc-AST as a binary; once HTML5 is on the candidate-list as canonical, the matrix evidence is one-directional.

**Strongest counter for monolithic (collapse three layers to one HTML5):** if HTML5 serves all three layers, why preserve the three-layer architecture at all?

**Why it weakens but doesn't fail:** the three temporal layers describe USE-CASES with different optima. Markdown's reading-order-naturalness IS a real advantage at hand-edit. EPUB's packaged-book IS a real advantage at publishing. Collapsing to HTML5-only means hand-editing tag-noisy markup and shipping unpackaged HTML for publishing. The layered architecture survives because the use-case distinctions survive.

**Resolution:** **Decision-mode = REFINE the prior architecture by swapping the canonical layer's format.** The architecture is preserved; the canonical-layer choice changes from JSON-AST to HTML5.

**Confidence:** HIGH.

### Ambiguity 2 — Temporal-layer scope

**Strongest counter:** the user's question "what should the end result be?" (singular) targets ONE format for everything.

**Why it weakens:** the user named THREE candidates (EPUB / md / HTML), which itself suggests they may be open to multiple-format thinking. Their question is at the "canonical / primary / load-bearing" layer; the verdict commits to that layer (HTML5) while preserving the other layers from the prior architecture.

**Resolution:** the user's question targets the canonical layer specifically. The verdict commits HTML5 there; the other two layers (markdown hand-edit; EPUB publishing) are preserved from the prior architecture.

**Confidence:** MED-HIGH (the user could push back wanting more collapse; the verdict is defensible either way but the layered architecture is the cleaner answer).

### Ambiguity 3 — HTML5-as-universal feasibility per layer

| Layer | HTML5 fitness | Verdict |
|---|---|---|
| Canonical | All requirements met natively or via class+attribute; Pareto-dominant per matrix | **HTML5 ADOPTED** |
| Hand-edit | Human-readable as markup but tag-noisy; markdown is preferable for prose-heavy editing | **Markdown preserved** (from prior) |
| Publishing | HTML5 → EPUB 3 is near-identity; HTML5 → PDF via weasyprint; HTML5 → web direct | **EPUB 3 preserved** (from prior; generated from HTML5 canonical) |

**Confidence:** HIGH on canonical adoption; HIGH on layer preservation.

### Ambiguity 4 — JSON-AST + HTML5 dual

**Strongest counter:** dual gives JSON-AST's queryability + HTML5's document-readability.

**Why it fails:** synchronization debt. One canonical must be authoritative; the other is derived. If JSON-AST is authoritative, HTML5 is a render — not a canonical. If HTML5 is authoritative (per this inquiry's adoption), JSON-AST is reachable on-demand via Pandoc (`pandoc -f html5 -t json`) without persisting a second canonical.

**Resolution:** **REJECT the dual.** HTML5 is the single canonical. JSON-AST is reachable on-demand if a translation-pipeline stage needs the AST shape, but doesn't persist as a second on-disk form.

**Confidence:** HIGH.

### Ambiguity 5 — User's non-mention of JSON-AST

**Strongest counter:** the user simply didn't think of JSON-AST; the omission is incidental.

**Why it weakens:** the user has a CONSISTENT pattern across multiple conversations — naming documents (EPUB / md / RTF / HTML / MOBI), never naming data structures. This is the second time they've reframed the format question, and both times they've named only surface formats. Pattern is signal.

**Resolution:** the user's framing is a load-bearing signal. The verdict honors it by committing HTML5 (a document, per the user's preference) as canonical. JSON-AST's role shifts to "on-demand reachable representation" — still useful in the pipeline, but not the canonical the user looks at.

**Confidence:** MED-HIGH (the verdict could be different in another framing; but honoring the user's signal is structurally appropriate here).

### Ambiguity 6 — Provenance + confidence dimension impact

**Strongest counter:** provenance is operational concern; shouldn't drive format choice.

**Why it fails:** the reconstruction reframe makes provenance LOAD-BEARING — the user explicitly cares about verifiability against source (the reconstruction is heavy; the user wants to inspect what came from text-layer vs OCR vs hand-edit). The canonical format MUST hold this. Markdown can't (A19 = ✗). HTML5 can (data-* attributes; A19 = ✓✓). The dimension is a real format-choice differentiator.

**Resolution:** the provenance + confidence dimension is **the strongest argument against markdown as canonical**. Confirms HTML5 over markdown at the canonical layer.

**Confidence:** HIGH.

### Ambiguity 7 — Load-bearing concept test for "HTML5 as canonical"

**Strongest counter:** "HTML5" is too generic; many HTML5 dialects exist (HTML5 living standard vs HTML5 strict vs XHTML5).

**Why it partially holds:** the verdict needs to be specific about which HTML5 profile. Resolution: HTML5 (living standard), polyglot syntax (works both as HTML5 and XHTML5), validated against a project-specific RNG schema. The exact validation profile is downstream; the architectural commitment is HTML5-as-canonical.

**Confidence:** HIGH on the architectural commitment; MED on the validation-profile specifics (downstream).

### SV4 — Clarified Understanding

After ambiguity collapse:
- **Canonical = HTML5** (replaces JSON-AST from prior; matrix-Pareto-dominant).
- **Hand-edit = Pandoc's markdown** (preserved from prior; prose-natural).
- **Publishing = EPUB 3** (preserved from prior; HTML5 → EPUB is near-identity).
- **Decision-mode = REFINE prior architecture** (preserve three-layer; swap canonical-layer format).
- **Provenance + confidence carried via HTML5 data-* attributes** (NEW capability).
- **JSON-AST = on-demand-reachable via Pandoc** (no persistent canonical).
- **User's document-vs-data preference honored.**

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed

- Three temporal layers preserved (canonical / hand-edit / publishing).
- **Canonical layer's format = HTML5** (W3C HTML5 living standard).
- Hand-edit format = Pandoc's markdown with canonical extension set.
- Publishing format = EPUB 3 (generated from HTML5 canonical via near-identity transform).
- Per-element provenance + confidence via HTML5 `data-*` attributes.
- Pandoc as architectural lever (preserved; Pandoc ↔︎ HTML5 + markdown + EPUB).
- The 7 policy targets represented in HTML5 via class + attribute conventions.

### Eliminated

- JSON-AST as on-disk canonical (replaced by HTML5; JSON-AST remains on-demand reachable).
- Monolithic single-format (architecture stands as three-layer).
- Custom format (.compldoc and similar — unnecessary given HTML5).
- Dual JSON-AST + HTML5 (synchronization debt).
- TEI / DocBook / JATS as canonical (HTML5 covers; TEI remains as future archival frontier).
- RTF as canonical (unchanged).
- MOBI (unchanged; Amazon-deprecated).

### Remaining variables (downstream)

- HTML5 schema / validation profile (which subset; project RNG; pydantic model on top?).
- Per-policy class-attribute conventions (`class="marginalia"` vs `data-policy="source-apparatus"` vs both).
- Per-element provenance encoding pattern (`data-source` / `data-confidence` / `data-hand-edit-status` / `data-intake-pass`).
- HTML5-to-EPUB 3 packaging script (minimal; specify metadata + manifest + cover-image).
- HTML5-to-markdown round-trip (for hand-edit workflow; specify which features are guaranteed).
- The relationship between in-memory IntakeDoc (the prior finding's tree) and HTML5 on-disk (parser + serializer).

### SV5 — Constrained Understanding

The verdict commits cleanly. HTML5 is the canonical; markdown and EPUB 3 are preserved at their layers. The new provenance + confidence dimension is served natively by HTML5's data-* mechanism. The architecture preserves three layers; one layer's format swaps. Engineering work concentrates downstream in: HTML5 schema/validation profile; per-policy class-attribute conventions; provenance encoding pattern; HTML5-to-EPUB packaging; HTML5-to-markdown round-trip subset.

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Did perspectives keep destabilizing the model? **No.** The HTML5-as-canonical insight stabilized once the matrix surfaced its Pareto-dominance. Phase 2 perspectives confirmed (W3C-spec; EPUB substrate; Pandoc ↔︎). Phase 3 ambiguity collapses refined details without forcing model patches.

### Self-Reference Blindness check

Subject = format choice. Framework = sensemaking. Disjoint. External anchors: W3C HTML5 spec; Pandoc reference manual; prior canonical-format finding; empirical PDF evidence. Strong external grounding.

### SV6 — Stabilized Model

**The post-repair canonical format question resolves to HTML5 within a preserved three-layer architecture.**

| Layer | Format | Rationale |
|---|---|---|
| Canonical (intake/translate-internal; on-disk; provenance-carrier) | **HTML5** (W3C Living Standard; semantic markup + lang/dir/class/data-* attributes; schema-validatable; Pandoc ↔︎) | Pareto-dominant per the capability matrix; document AND data-shape; native per-element provenance via data-*; web-standard not Pandoc-locked; near-identity transform to EPUB |
| Hand-edit | **Pandoc's markdown** (canonical extension set; preserved from prior) | Reading-order-natural for prose-heavy editing; familiar; Pandoc ↔︎ HTML5 for round-trip |
| Publishing | **EPUB 3** (preserved from prior; generated from HTML5 canonical) | Rich reader ecosystem; HTML5 → EPUB is near-identity (EPUB IS xhtml + manifest) |

**Decision-mode = REFINE prior architecture** (three-layer preserved; canonical-layer format swaps JSON-AST → HTML5).

**The user's pushback was honored.** They named EPUB / markdown / HTML as candidates — all surface formats; all documents-not-data. The verdict picks HTML5 (a surface format, a document) for the canonical role. Their non-mention of JSON-AST was a load-bearing signal that the verdict respects.

**The new provenance + confidence dimension confirms the choice.** Markdown can't hold per-element provenance cleanly (A19 = ✗ in the matrix). HTML5 can (data-* attributes; A19 = ✓✓). The reconstruction reframe — heavy work that produces verifiable provenance — needs the format to hold per-element metadata. HTML5 does; markdown alone doesn't.

### Inherited Commitments Re-test — prior canonical-format inquiry's verdict

The prior verdict committed three formats: JSON-AST canonical + Pandoc-md hand-edit + EPUB 3 publishing.

| Prior commitment | Status after this finding |
|---|---|
| Three-format layered architecture | **PRESERVED**. The three-temporal-layer use-case distinction is structurally sound. |
| Pandoc-md as hand-edit format | **PRESERVED**. The prior's specific extension set is unchanged. |
| EPUB 3 as publishing format | **PRESERVED and STRENGTHENED**. HTML5 → EPUB is even cleaner than JSON-AST → EPUB (near-identity vs Pandoc-render). |
| Pandoc + OCR as architectural lever | **PRESERVED and STRENGTHENED**. All three formats are Pandoc-native; HTML5 is a clean Pandoc target. |
| **Canonical = Pandoc-AST-as-JSON** | **REFINED → swap to HTML5.** The architecture preserved; one cell changes. The change is driven by NEW evidence (the reconstruction-is-heavy reframe surfacing per-element provenance as load-bearing) + the EMERGENT candidate (HTML5-as-universal). The prior choice was defensible within its framing; the new framing makes HTML5 the stronger choice. |
| Relationship label | **`refines:`** — the prior is preserved with one cell swapped; not overturned. |

### Inherited Commitments Re-test — original intake-concepts inquiry's Decisions 2-5

| Prior commitment | Status |
|---|---|
| Decision 2 — quality target = structure-preservation | **PRESERVED**. HTML5 explicit-tree storage preserves structure even more directly than surface markdown. |
| Decision 3 — IntakeDoc shape = tree-of-containers + cross-referenced flat collections | **PRESERVED in-memory**. The in-memory IntakeDoc remains the AST shape (semantically; whether implemented as Pandoc AST or as parsed HTML5 DOM); the on-disk form is now HTML5. |
| Decision 4 — 7-policy intake/translate split | **PRESERVED**. The seven policy-perception detectors operate on the in-memory shape; their AST-node references update to HTML5-element references (semantic refinement, not structural change). |
| Decision 5 — Pandoc + OCR architectural lever | **PRESERVED and STRENGTHENED**. |

### Calibration-corpus implications

For Risale-i Nur specifically, each policy target maps to HTML5 as follows:

- **Hashiye (marginalia)**: `<aside class="marginalia" id="h1" data-source="ocr" data-confidence="0.92">...</aside>` referenced from body via `<a href="#h1" class="marginalia-ref">`.
- **Mevlana couplets (embedded poetry)**: `<figure class="couplet" data-attribution="Mevlana"><blockquote>...</blockquote></figure>`.
- **Bismillah (formulaic opening)**: `<p class="formulaic-opening" data-tradition="islamic">بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيم</p>`.
- **Arabic spans within Turkish narrative**: `<span lang="ar" dir="rtl" data-source="ocr" data-confidence="0.87">ٱلْحَمْدُ لِلَّٰهِ</span>`.
- **Voice transitions**: `<span class="voice-cited">...</span>` or `<blockquote class="voice-cited" cite="...">...</blockquote>`.
- **Archaic register markers**: `<span class="archaic-register" data-archaism-type="lexical">...</span>`.
- **Honorifics**: `<span class="honorific" data-tradition="islamic">R.A.</span>` attached to preceding name span.
- **NFC diacritic normalization**: applied at intake; HTML5 storage is UTF-8 native; stable across format chain.
- **Per-element provenance**: every reconstructed element carries `data-source` (`"text-layer"` / `"ocr-tesseract"` / `"hand-edit"`) + `data-confidence` (0.0-1.0 numeric) + `data-intake-pass` (which repair pass produced this).

All seven policy targets are expressible as HTML5 patterns; the seven detector specs from the original intake-concepts inquiry refine to AST-or-HTML5-element references without redesign.

---

## How SV6 differs from SV1

| Dimension | SV1 (baseline) | SV6 (stabilized) |
|---|---|---|
| Frame | "Pick a format from EPUB / md / HTML / other" | "Refine the prior three-layer architecture by swapping canonical-layer format to HTML5" |
| Canonical format | Open (JSON-AST was prior) | **HTML5** |
| Hand-edit | Implicit (markdown probable) | **Pandoc's markdown** (preserved) |
| Publishing | Implicit (EPUB likely) | **EPUB 3** (preserved; HTML5 → EPUB near-identity) |
| Decision-mode | Open | **REFINE prior architecture** |
| User's named candidates | Treated as alternative-choices | Treated as PATTERN-signal (documents not data) |
| Provenance + confidence | Not surfaced | **Load-bearing differentiator** (matrix A19: HTML5 ✓✓ vs markdown ✗) |
| Inherited Decision 1 status | Unclear | **REFINED**: architecture preserved; canonical-layer swap |
| User's pushback honored | Implicit | **Explicit** (HTML5 = document + explicit-tree + provenance; matches user's "documents not data" pattern) |

The shift is from "open-format-choice" to a refined-architecture commitment with HTML5 as canonical. The user's intuition is honored; the prior architecture's load-bearing structure is preserved; the reconstruction reframe's new provenance dimension is served.

---

## Self-Assessment

### Saturation indicators

- **Perspective saturation:** ✓ (perspectives 4-6 confirmed Phase 1 anchors).
- **Ambiguity resolution:** 7/7 resolved (5 HIGH + 2 MED-HIGH confidence).
- **SV delta:** substantial (SV1 was open choice; SV6 commits HTML5 + preserved architecture).
- **Anchor diversity:** 7 constraints + 10 insights + 6 structural points + 4 principles + 5 meaning-nodes; perspectives 6/6.

### Failure modes checked

- **Status Quo Bias:** no — the inquiry doesn't defend the prior canonical-format inquiry's verdict unchanged; it refines with cited evidence.
- **Premature Stabilization:** no — 7 ambiguities each tested with strongest counter.
- **Anchor Dominance:** no — KI2 (HTML5 uniquely positioned) is load-bearing but doesn't carry every decision; KI3 (provenance dimension) + KI6 (markdown preserved at hand-edit) come from different evidence streams.
- **Perspective Blindness:** no — Risk and Frame-exit perspectives produced real anchors (HTML5 verbosity-cost; per-element provenance differentiation).
- **Clean Resolution Trap:** tested on HTML5-as-canonical commitment. Strongest counter ("JSON-AST is still right") tested structurally and found weaker than the matrix evidence supports.
- **Self-Reference Blindness:** no (subject = format; framework = sensemaking — disjoint).

### Meta-Inspection summary

- **H1 (candidate set):** tested — 5 core + 1 emergent; emergent promoted to verdict.
- **H4 (concept names):** "HTML5-as-canonical" tested as load-bearing structural distinction (document + data-shape + web-standard + EPUB-substrate).
- **H5 (motivating examples):** user's named candidates (EPUB / md / HTML) treated as PATTERN-signal not as exclusive set.
- **H6 (model fit):** Accommodation trigger not fired; model stabilized on HTML5-as-canonical without patching.
- **H7 (phase / calibration state):** v0.2 not built; reversal cost near-zero NOW; right time to swap.

### Verdict

**PROCEED to Decomposition.** The stabilized model carries 1 architectural refinement (canonical = HTML5; architecture preserved), per-policy AST→HTML5 mappings, an explicit Inherited Commitments Re-test (prior REFINED, not overturned), and downstream design tasks (HTML5 schema profile; per-policy class conventions; provenance encoding; HTML5-to-EPUB packaging; HTML5-to-markdown round-trip).
