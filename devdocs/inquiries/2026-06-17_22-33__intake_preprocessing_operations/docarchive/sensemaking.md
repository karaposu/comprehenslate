# Sensemaking — intake preprocessing operations

## User Input

Source: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-17_22-33__intake_preprocessing_operations/_branch.md`

Upstream outputs: `articulate_simple.md` + `surfacing.md`.

CONTINUES FROM: (1) post-repair canonical format finding (NFC + paratext baseline; HTML5 canonical; "leave content unclassified" scope narrowing); (2) original intake-concepts finding (Decision 2 structure-preservation quality target; Decision 5 Pandoc + OCR architectural lever).

Sensemaking job: adjudicate 6 frontier flags from surfacing; commit a stabilized model.

---

## SV1 — Baseline Understanding

The inquiry asks for preprocessing operations beyond NFC + paratext stripping, with structural boundary detection (depth ~4) as one named candidate and "be creative" for the rest. Surfacing produced 153 candidates across 14 sub-regions. My job: stabilize a model that adjudicates (a) where preprocessing ends and classification begins; (b) what the depth-of-boundary policy should be; (c) which operations v0.2 should commit to. The user's "be creative" instinct is in tension with the very recent scope narrowing ("leave content unclassified; trust the LLM").

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **Minimal-intake scope (recent decision):** no per-element classification; no per-span lang= tagging; no 7-policy detection.
- **HTML5 canonical format settled** (prior finding); this inquiry does not re-open it.
- **Generic translation project** (per `project_scope` memory); Risale-i Nur is calibration corpus, not purview.
- **v0.2 hasn't been built**; preprocessing operations must be specified before engineering starts.
- **Structure-preservation = quality target** (Decision 2 inherited).
- **Pandoc + OCR architectural lever** (Decision 5 inherited).
- **MQ4 exclusions:** translation-pipeline design OUT; PDF-extraction tooling OUT; canonical-format choice OUT.

### Key insights

- The scope-line between preprocessing and classification is **not crisp**. Surfacing's sub-region G surfaced 10 gray-zone items; the inquiry must commit a principle that decides these case-by-case.
- Some preprocessing operations clearly **improve translation quality without crossing into classification** (sentence segmentation; quotation-mark normalization; mojibake repair; hyphenation repair). These should be load-bearing even in minimal-intake mode.
- The user's "be creative" framing is about **avoiding under-coverage**, not about producing creative output for its own sake. The WHY-axis from articulation includes "scope-setting for v0.2 engineering" — they want a commitment they can act on, not just a brainstorm.
- **Source-format mix matters**: many operations are format-conditional (PDF bidi-fix; EPUB CSS-extraction; Word style-mapping). The format-mix question is unsettled and must be navigated.
- The user's **depth-4 instinct** ("this is deep enough I think") is a hedge inviting examination, not a fixed commitment.

### Structural points

- **Three preprocessing-relevance levels** emerging from the candidates:
  - **Foundational** (always run; format-agnostic; cheap; high value): NFC, whitespace, ligatures, etc.
  - **Quality-floor** (always run; mostly format-agnostic; load-bearing for translation): sentence segmentation, mojibake repair, hyphenation.
  - **Format-specific** (conditional on source format): PDF bidi-fix, EPUB CSS-extraction, Word style-mapping.
- **Scope-line candidate principle** (from surfacing G10): "structural, not semantic" — preprocessing identifies WHERE things are and HOW they nest; classification identifies WHAT semantic role they play.

### Foundational principles

- **Asymmetric-failure for scope-line:** missing a load-bearing op is worse than including a borderline op (the latter is recoverable downstream; the former isn't).
- **Prefer cheap-and-foundational over speculative-and-elaborate** in v0.2 baseline.
- **Generic-corpus operations over corpus-tuned** (per `project_scope`), BUT corpus-tuned extensions are preservable in a separate layer.
- **Source-driven structure preservation** (per Decision 2 quality target).

### Meaning-nodes

- **Scope-line** (preprocessing vs classification).
- **Quality-floor** (preprocessing that helps translation regardless of classification commitments).
- **Structural-not-semantic** (the proposed scope principle).
- **Depth-of-boundary** (the user's named question).
- **Format-priority** (which source formats v0.2 supports at what level of investment).
- **Two-layer corpus model** (generic core + corpus-tuned extensions).

---

## SV2 — Anchor-Informed Understanding

The inquiry isn't primarily "enumerate creative operations" — it's about navigating two tensions: (1) the scope-line between preprocessing and classification, and (2) the cross-corpus generality vs corpus-specific calibration. The "be creative" framing prevents under-coverage but the deliverable is a categorized recommended set, not a raw brainstorm. The 153 surfaced candidates need to be partitioned via a scope-line principle into clearly-in / clearly-out / requires-design-choice buckets.

---

## Phase 2 — Perspective Checking

### Technical / Logical

Which operations are **mechanically tractable** vs **heuristic-based** vs **model-required**?

- Mechanically tractable (cheap, deterministic): NFC, whitespace normalization, ligature decomposition, quotation/dash normalization, mojibake repair, soft-hyphen removal, source-format metadata extraction, paratext stripping (when source has clean structure).
- Heuristic-based (cheap, mostly-correct): sentence segmentation (regex + abbreviation dictionary), hyphenation-at-line-break repair, paragraph boundary detection, structural heading detection (in formats that mark headings).
- Heuristic-based (more design): paratext stripping (in PDF where paratext is layout-positional), structural boundary detection when source is flat (EPUB case), drop-cap detection.
- Model-required (LLM or specialized model): per-span language identification, per-element classification — but these are OUT per scope narrowing.

**New anchor:** the recommended set should heavily favor mechanically-tractable + cheap-heuristic operations. Model-required operations cross into classification and are out.

### Human / User

What does the user actually want? The articulation surfaced multiple motivations:
- "Scope-setting for v0.2 engineering" — wants a commitment to build against.
- "The just-narrowed intake scope feels too narrow" — wants more put back in.
- "Structural boundary detection feels like an obvious gap" — wants validation.
- "Be creative" — wants breadth in options before commitment.
- "Testing my thinking against richer options" — collaborative.

A categorized recommended set with named-and-rejected items serves all of these: provides the commitment (engineering scope), surfaces breadth (via surfacing's 153 candidates), validates structural boundary detection (yes, included), and is collaborative (categories + rationale invite pushback).

### Strategic / Long-term

What does this commitment lock in?

- It scopes intake-stage engineering work for v0.2.
- It defines the interface translate-stage reads.
- It does NOT affect publishing-stage (HTML5 → EPUB is already committed).
- It does NOT lock out future classification work — classification can be added in a later version without changing the preprocessing layer.

**New anchor:** the recommended set should be additively-extensible — future classification work should compose ON TOP of preprocessing, not replace it.

### Risk / Failure

What can go wrong?

- **Under-including operations:** translation quality degrades (missing sentence segmentation produces worse LLM output; missing mojibake repair propagates garbled bytes).
- **Over-including operations:** v0.2 ships later; engineering effort is wasted on operations that cross into classification.
- **Mis-classifying gray-zone operations:** if structural-boundary-detection is mis-classified as classification, it's deferred unnecessarily; if mis-classified as preprocessing, it bloats the v0.2 scope.

**New anchor:** the scope-line principle is risk-mitigation infrastructure — it makes mis-classification recoverable by providing an explicit test.

### Resource / Feasibility

What's the implementation effort?

- Most foundational ops (NFC, whitespace, ligatures, quotes/dashes) are 1-day implementations.
- Translation-quality-floor (sentence seg; mojibake) are well-supported by existing libraries (`spacy` / `nltk` for sentences; `ftfy` for mojibake).
- Format-specific repair (PDF bidi-fix; EPUB CSS-extraction) is heavier — each is multi-day.
- Structural boundary detection in formats that mark headings is cheap; in flat-h1 EPUB sources, requires heuristic design.

**New anchor:** v0.2 should commit ALL the cheap ops and SOME format-specific ops, with the rest as deferred. Format-priority (EPUB first) bounds the format-specific scope.

### Frame-exit Completeness

**Gating predicate fires:** the inquiry's commitments include terms inherited from prior findings ("preprocessing," "intake," "classification," "structure preservation") used at multiple distinct levels.

**Existence Enumeration on "preprocessing":**
- Inquiry-frame referent: **intake-stage preprocessing** (operations between source-read and translate-stage hand-off). This is what the inquiry adjudicates.
- Project-wide referent (TYPE-axis): **translate-stage preprocessing** (prompt construction, chunking, context-packing). Out of scope per MQ4.
- Project-wide referent (TYPE-axis): **publishing-stage preprocessing** (HTML5 → EPUB conversion, CSS templating). Out of scope per MQ4.

**Role Assessment:** the inquiry frame is correctly scoped to intake-stage preprocessing. The other two project-wide referents are intentionally excluded; their operation doesn't depend on this inquiry's adjudication. ✓

**Verdict Rigor on "intake-stage preprocessing" as the inquiry's scope:** the strongest counter is "the user said 'preprocessing' without specifying intake-stage, so the inquiry might be under-scoped." Structurally, the user's input context grounds the preprocessing-stage as intake-stage (NFC + paratext were named as intake operations; the inquiry continues that framing). Confidence HIGH.

**Residual:** no further frame-exit concern emerges.

### Phase / Calibration-State

**Required:** the inquiry involves rules that may behave differently in different project phases.

- **Current phase:** pre-v0.2 (engineering hasn't begun); calibration corpus available (Risale-i Nur PDFs + EPUBs); no other corpora yet.
- **Phase-dependent rules:** cross-corpus validation (F-5) can't fire until other corpora are in the project. **Early-stage default:** include Risale-i-Nur-tuned operations in a SEPARATE layer (corpus-specific extensions), not in the generic core; this preserves the ability to validate against future corpora without locking in corpus-specific assumptions.
- **Phase-dependent rules:** format-priority (F-4) can't be fully validated until v0.2 ships and is tested. **Early-stage default:** EPUB-first per quality-of-available-source evidence; PDF-fallback per empirical-evidence-of-need (broken-bidi Arabic; image-only Arabic).

---

## SV3 — Multi-Perspective Understanding

The recommended preprocessing pipeline crystallizes around three insights:

1. The **scope-line principle** ("structural, not semantic") is the load-bearing decision — it provides a test that decides gray-zone operations case-by-case.
2. The deliverable is a **categorized recommended set** (8 categories) with explicit verdicts per operation, organized by always-run vs format-conditional vs corpus-conditional. This serves all of the articulation's WHY-axis motivations.
3. The **two-layer corpus model** (generic core + corpus-tuned extensions) resolves the cross-corpus tension cleanly: generic operations are part of v0.2; corpus extensions are available but separate.

The depth-of-boundary question dissolves into a simpler answer: **preserve source-encoded hierarchy up to HTML5's h1-h6 ceiling**. The user's depth-4 is close to the empirical mean for literary texts but isn't an absolute cap. Source-driven up-to-h6 is the right framing.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — Where does preprocessing end and classification begin?

**Strongest counter-interpretation:** there is no crisp line. Everything that touches semantic structure (footnote extraction; quote-block detection; metadata extraction) is on a continuum. Any line we draw is arbitrary; better to just enumerate operations without a scope principle.

**Why the counter fails (structural grounds):** the structural-vs-semantic distinction provides a decidable test for any candidate operation: "Does identifying this require knowing what cultural/linguistic role it plays?" If yes → semantic (classification). If no → structural (preprocessing). The line isn't perfectly crisp at every case, but the test is workable: identifying that an `<aside>` element exists at body-end with a back-reference link is structural (positional + relational); identifying that the `<aside>` contains "Said Nursi's marginalia" is semantic. The test fires per-operation; gray-zone cases get adjudicated explicitly via the test.

**Confidence:** HIGH. The scope-narrowing decision made a principle load-bearing; the structural-vs-semantic distinction is the cleanest principle that respects the scope narrowing without trivializing it.

**Resolution:** Commit **"structural, not semantic"** as the load-bearing scope-line principle. Preprocessing identifies WHERE things are and HOW they nest in the source; classification identifies WHAT semantic role they play.

**What is now fixed?** The scope-line principle. Every candidate operation gets the test applied; the verdict is "in" if it identifies structure, "out" if it identifies semantic role.

**What is no longer allowed?** Operations that perform semantic role tagging (per-element provenance; per-policy classification; per-span lang= tagging; voice marking; cited-source identification). These are deferred per the recent scope narrowing.

**What now depends on this?** Per-operation verdicts on every gray-zone item from surfacing's G sub-region; per-category membership in the recommended set.

**What changed in the conceptual model?** The scope-line is no longer fuzzy. Every operation has a test it can be evaluated against. Gray-zone ambiguity collapses to per-operation decisions.

### Ambiguity 2 — Decision-mode (which of the 5 considered articulations?)

**Strongest counter-interpretation:** "be creative" was the user's primary cue; the right output is a generative breadth-first brainstorm (variant 1), not a commit to a recommended set (variant 2).

**Why the counter fails (structural grounds):** the WHY-axis motivations from articulation include both "design space exploration" (served by variant 1) AND "scope-setting for v0.2 engineering" (served by variant 2). The articulation's MQA flagged this as an irreducible overlap. Surfacing's 153-candidate enumeration already satisfied the breadth-first generative ask (variant 1 deliverable). What remains unserved is the commit-to-v0.2 ask. A recommended set with surfacing's breadth preserved as the "rejected items + rationale" backing serves both motivations.

**Confidence:** HIGH-MED. The user might want more brainstorm; if so they will say. Variant 2 is the higher-utility default given the WHY-axis ambiguity.

**Resolution:** Commit to **a categorized recommended preprocessing set for v0.2**, organized by 8 categories, with per-operation verdicts based on the scope-line principle. Surfacing's 153 candidates serve as the design-space backing; the rejected items are explicitly named with reasons.

**What is now fixed?** The deliverable shape: categorized recommended set + per-operation verdicts + rationale for rejections.

**What is no longer allowed?** Just-adjudicate-boundary-detection (variant 4 — we evaluate it within the broader set); cost-value-scope 2D map (variant 5 — collapsed into the categorized set's per-operation tags); pure-brainstorm-without-commit (variant 1 — preserved as backing).

**What now depends on this?** Innovation generates per-category operation specs + per-rejection rationale.

**What changed?** The output shape is determinate.

### Ambiguity 3 — Depth-of-boundary-detection (is depth 4 the right ceiling?)

**Strongest counter-interpretation:** the user said "this is deep enough I think" with hedge; an adaptive depth (let the source decide) might be cleaner.

**Why the counter fails (structural grounds):** "adaptive" and "source-driven up to a sensible ceiling" converge in practice — and the HTML5 ceiling (h1-h6) provides the right structural cap because (a) HTML5 is the committed canonical format; (b) Pandoc reads source headings into h1-h6 natively across all input formats; (c) literary texts rarely exceed depth 4-5 anyway; (d) academic texts may use depth 5-6 but never deeper. The h1-h6 ceiling is therefore source-driven (preserve what's in the source) AND principled (matches the canonical format's ceiling).

**Confidence:** HIGH. The h1-h6 ceiling is W3C HTML5 spec; the source-driven framing is operationally clean; the depth-4 instinct is close to the empirical mean.

**Resolution:** Adopt **source-driven hierarchy preservation up to HTML5 h1-h6 ceiling**. In practice most literary texts won't exceed h4; academic texts may go to h5-h6. No absolute depth cap below 6. When the source is flat (e.g., the Asa-yı Musa EPUB with h1-only), intake performs hierarchy INFERENCE up to h6 using detectable structural markers in body text.

**What is now fixed?** Depth policy = source-driven, up to h6.

**What is no longer allowed?** Arbitrary depth caps below 6 (e.g., "stop at h4 even if source provides h5"); over-promotion of body markers beyond what the source actually structures.

**What now depends on this?** The hierarchy inference algorithm (when source is flat); the per-format default depth (EPUB sources may use h1-only; PDF extraction may have its own conventions).

**What changed?** The depth-4 instinct is honored (it's the empirical mean) but generalized to a source-driven up-to-h6 policy.

### Ambiguity 4 — Source-format mix (does v0.2 support PDF / EPUB / Word / plain-text equally?)

**Strongest counter-interpretation:** defer the format-priority question; commit to one format in v0.2 and add others later.

**Why the counter fails (structural grounds):** the calibration corpus has BOTH PDF AND EPUB available for Asa-yı Musa (we analyzed the EPUB; the PDF was characterized in earlier session). The original intake-concepts finding's Decision 5 (Pandoc + OCR architectural lever) natively supports multiple formats. Deferring would over-narrow v0.2's scope, and EPUB intake is significantly cheaper than PDF intake (no OCR; no bidi-fix; structure already encoded). Committing to format priority resolves the question without forcing one-format scope.

**Confidence:** HIGH-MED. The priority assignment isn't fully constrained by inquiry inputs, but the available-evidence direction is clear.

**Resolution:** Commit **EPUB-first + PDF-with-OCR-fallback** as the v0.2 format priority. EPUB is the primary intake path; PDF is the fallback for sources that exist only in PDF (per the empirical evidence — broken-bidi Arabic in Asa-yı Musa PDF; image-only Arabic in Muhakemat). Word and plain-text are future format additions.

**What is now fixed?** EPUB is primary; PDF is fallback; other formats are future.

**What is no longer allowed?** PDF-only or EPUB-only v0.2; equal-weight investment across all four formats simultaneously.

**What now depends on this?** Format-specific repair operations (F sub-region) get prioritized: EPUB ops at higher priority than PDF ops than Word ops.

**What changed?** Format-mix is no longer unresolved.

### Ambiguity 5 — Cross-corpus generality vs corpus-tuning tension

**Strongest counter-interpretation:** the project is generic per `project_scope` memory; drop all corpus-specific operations entirely.

**Why the counter fails (structural grounds):** the project being generic doesn't preclude corpus-tuned EXTENSIONS — it means generic operations are CORE and corpus-tuned operations are optional extensions. Drop-everything-corpus-specific would also discard the empirical-evidence-driven knowledge that made the inquiry useful (we know hashiye has clean structure because of Risale-i Nur; we know letter-spaced Tenbih markers exist because of Risale-i Nur). The two-layer model (generic core + corpus extensions) preserves this knowledge without violating the generic-project commitment.

**Confidence:** HIGH. Preserving extensibility is structurally sound and respects the `project_scope` memory.

**Resolution:** Commit **two-layer corpus model**: (1) generic preprocessing operations form the v0.2 core; (2) Risale-i-Nur-tuned operations (Mukaddeme/Mes'ele keyword detection; letter-spaced Tenbih un-spacing) are available as **calibration-corpus extensions** — preserved but explicitly tagged as corpus-specific, not part of the v0.2 generic pipeline.

**What is now fixed?** The two-layer structure exists; the generic core is v0.2; corpus extensions are a separate layer.

**What is no longer allowed?** Generic-pipeline-includes-Mukaddeme-detection; drop-everything-corpus-specific.

**What now depends on this?** Per-operation tagging: each surfaced operation gets either "generic" or "corpus-tuned" label.

**What changed?** The tension is resolved structurally.

### Ambiguity 6 — Does the "translation-quality-floor" sub-category warrant naming?

**Strongest counter-interpretation:** all preprocessing serves translation eventually; introducing a "quality-floor" sub-category adds cognitive overhead without operational payoff.

**Why the counter fails (structural grounds):** the sub-category is load-bearing for deciding what NOT to defer. Some operations (sentence segmentation; mojibake repair) are "always run; cheap; high impact on translation quality"; others (NFC; whitespace) are "always run; cheap; foundational byte-consistency." The first group has DIFFERENT motivation than the second: foundational normalization is for downstream byte-consistency; quality-floor is for downstream LLM-translation quality. Naming the distinction makes the recommended set's "must-include" subset transparent.

**Confidence:** HIGH-MED. The distinction is real but the cost-of-naming is small enough that the counter (cognitive overhead) is weak.

**Resolution:** Adopt **translation-quality-floor** as a named sub-category within the recommended set. Members: sentence segmentation, document-level language identification, hyphenation-at-line-break repair, mojibake repair. These are always-run for translation-quality reasons distinct from byte-consistency.

**What is now fixed?** The quality-floor sub-category exists; its members are named.

**What is no longer allowed?** Deferring sentence segmentation or mojibake repair as "advanced" or "future."

**What now depends on this?** The recommended set's organization separates foundational (byte-consistency) from quality-floor (translation-load-bearing).

**What changed?** The "what is load-bearing for translation even in minimal-intake mode?" question is answered.

### Load-bearing concept test (Refinement note)

Two concepts in this Sensemaking output are load-bearing:

**Concept 1: "Structural, not semantic" (scope-line principle).**
- *Counter:* "Is this the project's actual principle, or an external default the loop adopted without testing?"
- *Response:* The scope narrowing decision is documented in conversation but not in a finding yet. This Sensemaking is the first articulation of the principle as a load-bearing rule. Structurally the principle is sound (it provides a decidable test); it's not external default because no external precedent named it for this project. The principle's name aligns with the user's framing (they distinguished "structure" from "classification" implicitly via the scope narrowing).
- *Confidence:* HIGH (structurally sound + user-framing-aligned).

**Concept 2: "Translation-quality-floor" (sub-category name).**
- *Counter:* "Does this term match the project's actual vocabulary, or is it a loop-coined neologism?"
- *Response:* The term is loop-coined for this inquiry. Project vocabulary doesn't have a prior term for this concept; the user's framing didn't include one. The name is descriptive ("quality-floor" = "operations load-bearing for translation quality even at the floor of intake's scope"); validation = user pushback if any.
- *Confidence:* MED (loop-coined; flag for user-language alignment in CONCLUDE).

### Specific-vs-pattern recognition cue (Refinement note)

The user's named candidate ("structural boundary detection at depth ~4") is one specific case of the broader pattern ("structural detection more generally"). The inquiry should address both — the named candidate (boundary detection) gets explicit verdict; the broader pattern (S sub-region from surfacing: paragraph / list / table / quote / verse / footnote / marginalia / cross-reference / ToC / figure-caption detection) gets the same scope-line principle applied. The recommended set spans the broader pattern, not just the named candidate. ✓

---

## SV4 — Clarified Understanding

The recommended preprocessing set for v0.2 stabilizes as:

**Scope-line principle:** "Structural, not semantic." Preprocessing identifies WHERE things are and HOW they nest; it does NOT identify WHAT semantic role they play.

**Eight categories:**

1. **Foundational normalization** (always; format-agnostic; byte-consistency)
2. **Translation-quality-floor** (always; mostly format-agnostic; translation-load-bearing)
3. **Paratext stripping** (always; established baseline)
4. **Source-format metadata + provenance** (always; cheap; document-level)
5. **Structural detection** (always; "structural, not semantic" core; up to HTML5 h1-h6)
6. **Format-specific repair** (conditional on source format; EPUB-first; PDF-fallback)
7. **Quality / hygiene** (always; informational flags; not corrective)
8. **Corpus-specific extensions** (calibration-corpus-tuned; separate layer; NOT v0.2 generic)

**Depth policy:** source-driven, up to HTML5 h1-h6 ceiling. When source is flat, infer hierarchy from body markers.

**Format priority:** EPUB-first + PDF-with-OCR-fallback for v0.2; Word and plain-text as future.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed

- Scope-line principle = "structural, not semantic"
- Decision-mode = categorized recommended v0.2 preprocessing set (8 categories)
- Depth policy = source-driven up to HTML5 h1-h6
- Format priority = EPUB-first + PDF-fallback
- Two-layer corpus model = generic core + calibration-corpus extensions
- Translation-quality-floor sub-category named (members specified)

### Eliminated

- Generative-only output without commit (variant 1 from articulation)
- Just-adjudicate-boundary-detection in isolation (variant 4)
- Depth-4 as absolute cap (replaced by source-driven up-to-h6)
- PDF-only or EPUB-only v0.2 scope
- Drop-everything-corpus-specific (corpus extensions preserved separately)
- Per-element classification operations (out per scope narrowing — semantic-not-structural)
- Per-span lang= tagging (out per scope narrowing — semantic)
- 7-policy detection (out — semantic)
- Model-required operations beyond LLM-translate-stage (out — would cross into classification)

### Viable

- Per-category operation specs + per-rejection rationale (Innovation generates)
- Per-operation cost / value / scope-fit / format-applicability tags
- Risale-i-Nur-tuned operations as a tagged extension layer (not in v0.2 generic core)
- Source-flat-h1 hierarchy inference algorithm (Innovation specifies)
- Quality-floor sub-category as named-and-prioritized members in the foundational tier

---

## SV5 — Constrained Understanding

The deliverable shape is determinate: a categorized recommended set with 8 categories, per-operation verdicts driven by the structural-not-semantic principle, and a two-layer corpus model (generic + extensions). Innovation's job is to populate each category with specific operation names, brief specs, and rationale. Critique's job is to test the principle and verdicts adversarially. Decomposition's job is to organize the recommended set into engineering-actionable pieces.

---

## Phase 5 — Conceptual Stabilization

### SV6 — Stabilized Model

The intake preprocessing pipeline for v0.2 is a categorized set of operations anchored by the load-bearing principle **"structural, not semantic"**.

**The principle:** preprocessing identifies WHERE things are in the source and HOW they nest; classification identifies WHAT semantic role they play. Preprocessing is in scope; classification is deferred per the recent scope narrowing.

**The 8 categories of v0.2 preprocessing:**

1. **Foundational normalization** (always; format-agnostic; byte-consistency)
   - NFC Unicode normalization
   - Whitespace normalization (collapse runs; trim line ends; normalize newlines)
   - Zero-width character removal (U+200B-D)
   - Soft hyphen removal (U+00AD)
   - Quotation mark normalization (curly/straight/national variants → project canonical)
   - Dash normalization (em/en/hyphen/minus → project canonical)
   - Ellipsis normalization (three dots vs single)
   - Ligature decomposition (ﬁ → fi; etc.)
   - Broken-Unicode detection

2. **Translation-quality-floor** (always; format-agnostic; load-bearing for translation quality even in minimal-intake)
   - Sentence segmentation (with abbreviation handling)
   - Paragraph boundary detection
   - Document-level language identification
   - Hyphenation-at-line-break repair (PDF artifact)
   - Mojibake repair (encoding detection + repair via `ftfy` or equivalent)

3. **Paratext stripping** (always; established baseline)
   - Running headers / footers
   - Page numbers / folios
   - Catchwords (when present)
   - Editorial boilerplate
   - Publisher metadata at chapter starts
   - Blank pages / decorative ornaments
   - Watermarks ("scanned by" inserts)
   - Library/acquisition stamps

4. **Source-format metadata + provenance** (always; cheap; document-level)
   - Source-format detection (EPUB / PDF / Word / plain-text)
   - Source-file path / URL
   - Source-file SHA-256 checksum
   - Intake-timestamp + intake-tool-version
   - Title / author / publication date / publisher (from source metadata)
   - Source-language declaration (from source metadata or auto-detected)
   - Source-format metadata pass-through (EPUB OPF; PDF /Info; Word docProps)

5. **Structural detection** (always; "structural, not semantic" core)
   - Heading hierarchy preservation (h1-h6 source-driven)
   - Heading hierarchy INFERENCE when source is flat (e.g., flat-h1 EPUB) using detectable body markers
   - List structural detection (numbered / bulleted)
   - Table structural detection (rows × cells; structure only, not content classification)
   - Quote-block structural detection (block-vs-inline; structure only)
   - Verse-block structural detection (line-broken; structure only — does not classify as poetry-policy)
   - Footnote / endnote STRUCTURAL extraction (apparatus separation by position + anchor; NOT semantic-role tagging)
   - Cross-reference structural preservation (`href` + matching `id`; structure only — does not resolve citations)
   - Figure / illustration caption structural separation
   - Drop-cap normalization (visual feature → semantic separation)

6. **Format-specific repair** (conditional on source format; EPUB-first; PDF-fallback)
   - **EPUB:** spine reassembly; CSS-presentation extraction (turn `class="bold"` into `<strong>`); heading-level inference from flat-h1; OPF metadata extraction
   - **PDF:** mid-word hyphen repair (line-wrap artifacts); column-order repair; bidi-fix for broken-bidi Arabic (Asa-yı Musa case); italic / bold recovery via secondary extraction tool (mutool / pdf2htmlEX); OCR fallback for image-only spans (Muhakemat case)
   - **Word:** style-mapping (Heading 1-9 → semantic); run-merge (consecutive same-format runs)
   - **Plain text:** encoding detection (BOM + chardet + fallback); line-ending normalization

7. **Quality / hygiene** (always; informational flags; not corrective)
   - Suspicious-line-break detection (mid-word; mid-sentence)
   - Truncation detection (file ends mid-sentence)
   - Document-completeness check (ToC matches headings; footnote refs match footnotes)
   - Duplicate-content detection (boilerplate; OCR re-runs)
   - Orphan-content detection (single char / one-word paragraphs)
   - Confusables detection (Cyrillic А vs Latin A; OCR-derived sources)
   - Encoding-confidence flagging (when L5 detection is uncertain)

8. **Corpus-specific extensions** (calibration-corpus-tuned; separate layer; NOT v0.2 generic)
   - Letter-spaced-emphasis un-spacing ("T e n b i h" → "Tenbih")
   - Risale-i-Nur structural-marker keyword recognition (Mukaddeme / Mes'ele / Hâtime / Tenbih / Bismillah)
   - Other Risale-i-Nur-specific patterns
   - **Note:** these are AVAILABLE as a separate layer for corpora that match Risale-i Nur; they are NOT part of the v0.2 generic intake pipeline.

**Depth-of-boundary policy:** source-driven hierarchy preservation, up to HTML5 h1-h6 ceiling. When source is flat, hierarchy inference using structural markers in body text. No absolute depth cap below 6.

**Format priority for v0.2:** EPUB-first (per quality of available EPUB intake sources in calibration corpus); PDF-with-OCR-fallback (per empirical evidence of broken-bidi / image-only Arabic problems). Word and plain-text as future format additions.

### Inherited Commitments Re-test

- **NFC + paratext baseline (post-repair canonical format finding):** PRESERVED and EXTENDED. NFC is category 1; paratext is category 3 (own category). The baseline expands into a structured 8-category set.
- **"Leave content unclassified" scope narrowing (recent conversation):** PRESERVED via scope-line principle. All 8 categories are structural-not-semantic; no per-element classification commitment.
- **Decision 2 structure-preservation quality target (original intake-concepts finding):** PRESERVED and STRENGTHENED. The structural-detection category (5) is explicitly aligned to structure-preservation; the scope-line principle makes preservation primary.
- **Decision 5 Pandoc + OCR architectural lever (original intake-concepts finding):** PRESERVED and STRENGTHENED. Format-specific repair (category 6) explicitly leans on Pandoc readers (EPUB / PDF / Word readers) and OCR (for PDF Arabic).
- **HTML5 canonical format (prior finding):** COMPATIBLE. The recommended set produces structure that fits HTML5 (h1-h6 hierarchy; semantic elements like `<aside>` for footnotes; `<figure>` for verse-blocks) without crossing into classification (no `class="marginalia"` or `class="couplet"` tagging — those are semantic and OUT).

### Differences from SV1

1. **Scope-line principle surfaced as load-bearing.** SV1 didn't have a principled scope-line; SV6 commits "structural, not semantic" as the test for every operation.
2. **Depth-4 reframed as source-driven up to h6.** SV1 took depth-4 as given; SV6 honors the empirical instinct while generalizing to source-driven HTML5 ceiling.
3. **Translation-quality-floor sub-category named.** SV1 didn't distinguish translation-load-bearing operations from byte-consistency operations; SV6 makes the distinction structural.
4. **Cross-corpus tension resolved via two-layer model.** SV1 had the tension unresolved; SV6 separates generic core from corpus extensions.
5. **Format priority committed.** SV1 left format-mix unresolved; SV6 commits EPUB-first + PDF-fallback.
6. **Decision-mode determined.** SV1 had 5 considered articulations open; SV6 commits to the categorized recommended set (with surfacing's breadth as backing).

### Telemetry

- **SV delta from SV1 to SV6:** large (6 named structural shifts). Healthy.
- **Perspective saturation:** 7 perspectives applied; the last 2 (Frame-exit Completeness; Phase / Calibration-State) added new anchors. Approaching saturation but not exhausted.
- **Ambiguity resolution ratio:** 6 ambiguities identified; all 6 resolved with structural-grounds counter-argumentation (5 HIGH confidence; 1 HIGH-MED). No ambiguities remain OPEN.
- **Anchor diversity:** anchors span all 5 types (constraints; insights; structural points; principles; meaning-nodes) and multiple perspectives. Diverse.

### Failure mode check

- **Status Quo Bias** — not fired. NFC + paratext baseline is preserved AND extended; the inquiry interrogates the baseline rather than defending it.
- **Premature Stabilization** — not fired. 6 ambiguities resolved with explicit counter-argumentation; 7 perspectives produced new anchors; SV4-SV6 took deliberate revision passes.
- **Anchor Dominance** — boundary-approached. The "structural, not semantic" principle does heavy lifting; remove it and the model would partially collapse. BUT: the two-layer corpus model, the format-priority, and the quality-floor sub-category each contribute distinct structure independent of the scope-line principle. So multi-anchored, not one-pillar.
- **Perspective Blindness** — not fired. Frame-exit Completeness perspective produced new anchors (existence enumeration on "preprocessing"); Phase / Calibration-State perspective produced new anchors (early-stage defaults).
- **Clean Resolution Trap** — not fired. Each ambiguity's resolution survives a stated counter-argument tested on structural grounds.
- **Self-Reference Blindness** — not applicable. The inquiry's subject (preprocessing operations) is not the discipline (sensemaking).

### Verdict

**SUBSTANTIVE VERDICT:** the v0.2 intake preprocessing pipeline is an 8-category set anchored by the "structural, not semantic" scope-line principle; depth policy is source-driven up to HTML5 h1-h6; format priority is EPUB-first + PDF-fallback; corpus-specific operations live in a separate extensions layer.

**PROCEED** — ready for Decomposition.
