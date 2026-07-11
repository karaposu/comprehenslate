# Sensemaking — document intake handling concepts

## User Input

Input passed to sense-making: `_branch.md` + upstream `articulate_simple.md` + `surfacing.md` (110 candidates across 4 regions A. format / B. structure / C. pipeline / D. quality; 12 concept-names; 6 frontier flags).

Sensemaking directives:
- Adjudicate the kinds-axis ambiguity (4 layers vs format-only).
- Commit to a finding-shape (flat / layered / decision-driven / hybrid).
- Prune the 110 candidates to the load-bearing set.
- Adjudicate F2 (canonical intake format).
- Adjudicate F3 (quality-target trichotomy).
- Commit to the 7 policies' intake-vs-translate attribution.
- Commit to `IntakeDoc` high-level shape.
- Answer the user's central question (what IS the actionable list?).
- Inherited Commitments Re-test for articulate_simple + surfacing + schema.

Keep at INTAKE level — no app-UI drift, no translation-internals drift, no schema-redefinition.

---

## SV1 — Baseline Understanding

The user asked for a list of intake-handling concepts. They lean format-layer (PDF / md / RTF) but the request reads broader. The list should help unblock the real painpoint (PDF intake quality is bad), avoid architecture debt (an early decision should not require rework), and scope engineering (the list should be actionable for v0.2+). The first read: produce a layered enumeration of ~30-50 concepts.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1.** The 7 policy classes in `SKILL/references/config/schemas.py` are ALREADY defined; intake design must respect them as the downstream contract, NOT redefine them.
- **C2.** `TranslationConfig` (8 fields) + `PipelineConfig` (6 fields) are downstream of intake; intake produces input to these stages, not the other way around.
- **C3.** The current v0.1 Mac app's `LLMClient` sends raw text in a single call — no chunking, no intake structure beyond raw bytes-to-string. v0.2 is the first real intake stage.
- **C4.** Calibration corpus (Risale-i Nur) carries marginalia (`hashiye`), embedded poetry (Mevlana couplets), formulaic openings (Bismillah), mixed-script (Turkish + Arabic), archaic register — intake must handle these even at v0.2 to validate the design.
- **C5.** Mac app UI surface is excluded (MQ4); the finding is about the intake stage, not the intake UX.
- **C6.** Translation-stage internals (chunking algorithm, parallel mode, output format) are excluded (MQ4); intake's responsibility ends at handoff.
- **C7.** Deliverable shape must be LIST (per user's literal wording: "list of intake handling concepts").

### Key Insights

- **KI1.** Examining `schemas.py`: ALL 7 policies operate on something intake must PERCEIVE in the source. `SourceApparatusPolicy` references marginalia (Said Nursi's hashiye); `EmbeddedPoetryPolicy` references Mevlana couplets in Nursi's prose; `HonorificsPolicy` references honorific suffixes; `NonMainLangPartsPolicy` references non-main-language spans. None of the 7 policies' values are sensible without intake having first found the things they apply to.
- **KI2.** The clean split: intake **PERCEIVES + REPRESENTS**; translate **CHOOSES + RENDERS**. The policy's value (the chosen Literal string) is a translate-time decision; the policy's activation condition (whether this source HAS marginalia at all) is an intake-time perception.
- **KI3.** "Canonical intake format" is actually TWO distinct questions: (a) what format does the USER PROVIDE? (b) what format does INTAKE PRODUCE INTERNALLY (the `IntakeDoc` representation)? The user's PDF→md substrate is about (a). The `IntakeDoc` schema is about (b). These have different answers.
- **KI4.** PDF is structurally HARDER than every other intake format because PDF often only carries visual layout, not markup. docx, EPUB, html, md, RTF all have markup that names structure. PDF intake is therefore a sub-pipeline distinct from "all other formats."
- **KI5.** User's painpoint = STRUCTURE LOSS ("PDF formatting can be really bad" = chapter / paragraph / footnote boundaries lost, columns collapsed, hyphenation artifacts). This signal commits the quality-target trichotomy to **structure-preservation**.
- **KI6.** The 4 layers (format / structure / pipeline / quality) are NOT independent — they COMPOSE: format is the substrate; structure is what intake perceives WITHIN the format; pipeline is the stages that go format → structure; quality is how well the pipeline preserved structure. They are 4 aspects of one problem, not 4 alternative problems.
- **KI7.** Therefore the kinds-axis "scope to format-only OR span all 4 layers" debate is a false choice: all 4 layers must be present because they ARE the problem at different cuts. Scoping to format-only would leave structure-decisions implicit and architectural-debt-laden.
- **KI8.** Pandoc covers most format conversions cleanly (PDF→md, docx→md, html→md, RTF→md, EPUB→md). Pandoc is the architectural lever — it absorbs most format-layer concepts as engineering, not design.

### Structural Points

- **SP1.** Intake stage = (detect format) → (parse format) → (normalize) → (perceive structure) → (emit `IntakeDoc`) → (hand off to translate).
- **SP2.** `IntakeDoc` is the CONTRACT between intake and translate; it's the load-bearing object — every parser populates it; every translate step consumes it.
- **SP3.** Two natural read-modes for the finding's list: (i) engineering checklist (concepts that need code), (ii) design-decision list (concepts that need a CHOICE before code). Both modes are needed — hybrid via per-concept tags.
- **SP4.** The 7 policies split structurally: their VALUE lives in `TranslationConfig` (translate-time choice); their ACTIVATION lives in `IntakeDoc` (intake-time perception). The fields are in `translation_config.py`; the perceived-source-elements live in the doc.

### Foundational Principles

- **FP1.** Asymmetric-failure for intake: false-negative (intake DROPPED structure translate needs) is worse than false-positive (intake PRESERVED noise translate must filter). Lean to preserve under uncertainty.
- **FP2.** Schema-as-contract: `IntakeDoc` design must precede parser implementation, because all parsers must populate it.
- **FP3.** Round-trippability is a property, not a requirement: lossy intake is acceptable IF the lossiness is intentional and named.
- **FP4.** Human-readable intake is operationally valuable: an `IntakeDoc` that serializes to a human-readable form (markdown-superset, YAML frontmatter for apparatus) enables hand-editing as a recovery path for bad parses.

### Meaning-Nodes

- **MN1.** `IntakeDoc` — the schema produced by intake; the contract with translate.
- **MN2.** Intake-vs-translate boundary — what intake DOES vs what translate DOES; the architectural seam.
- **MN3.** Source-perception — what intake must FIND in the source so translate can render it.
- **MN4.** Structural fidelity — what intake must PRESERVE; the quality property the user cares about.
- **MN5.** Format gradient — raw PDF → canonical intake format → `IntakeDoc`; loss happens along this curve.
- **MN6.** Canonical intake format — the format intake INTERNALIZES every source into.

### SV2 — Anchor-Informed Understanding

The kinds-axis is not a multiple-choice question — all 4 layers cohere as ASPECTS of the same problem (KI6/KI7). The user's lean to format-layer is a starting-point bias, not a scope-limit. The deliverable should reflect that all 4 layers are relevant, with the format-layer being weighted heaviest because PDF intake is the active painpoint. Pandoc absorbs ~80% of format-conversion engineering (KI8); the design questions concentrate in (1) what canonical intake format Pandoc emits, (2) what `IntakeDoc` schema represents, (3) which policies' perceptions intake delivers.

### Meta-Inspection — H4 (concept names) + H5 (motivating examples)

- **H4.** "IntakeDoc" — load-bearing structural placeholder, not yet a stable class name. The role is committed; the label is editable downstream.
- **H4.** "Pandoc-md-superset" — load-bearing structural distinction (it's NOT vanilla CommonMark; it has footnotes/tables/definition-lists/citations as Pandoc-native extensions). The label is precise enough.
- **H5.** Motivating examples were PDF/md/RTF — all format-layer. The finding must generalize beyond these examples (per the Specific-vs-pattern check below at Ambiguity 1).

---

## Phase 2 — Perspective Checking

### Technical / Logical

Pandoc handles most format conversions (PDF→md via pdftotext + heuristics, docx→md, RTF→md, html→md, EPUB→md). Using Pandoc as the universal converter reduces the format-layer to: (i) does the source need OCR first? (Tesseract / OCRmyPDF for scan-only PDFs); (ii) does the Pandoc conversion preserve enough structure for the quality-target? (need post-conversion validation).

`IntakeDoc` as a TREE-of-containers (chapter → section → paragraph) is natural for hierarchical containment (B24 in surfacing). FLAT-list-with-region-tags is simpler for chunking handoff. HYBRID (tree of nodes + cross-referenced flat collections for apparatus) covers both: tree for chunk-by-chapter; flat collections for marginalia/poetry which reference back to inline positions.

### Human / User

The user's painpoint is CONCRETE (PDF formatting), the other layers are abstract. A finding that leads with format and shows how the other layers compose around it serves the user's mental model.

User wrote "list" — emphasis on list. Flat or layered list is more useful than narrative.

### Strategic / Long-term

Intake design will outlive v0.2; getting the load-bearing decisions right (canonical format, `IntakeDoc` shape, policy split) prevents rework. The 7 policies are already committed; intake must be designed to FEED them, not to redefine them.

### Risk / Failure

- Premature commitment to vanilla md as canonical intake format → loses Risale-i Nur features (no footnote primitive in CommonMark → marginalia can't be represented).
- Premature commitment to RTF as fallback for "complicated texts" → RTF is editor-fragile (looks different in Word / Pages / TextEdit); defeats the post-parse hand-editing workflow.
- Over-modeling intake (too many concepts, too many sub-inquiries) → paralysis without a build path. The list must converge to ~30-40 actionable concepts, not 110.

### Resource / Feasibility

Pandoc covers ~80% of format conversion as off-the-shelf. OCR (Tesseract + OCRmyPDF) handles scan-only PDFs. The remaining 20% is edge cases (math notation, complex multi-column layout, embedded media). v0.2 can ship with Pandoc + Tesseract path covering ~80% of intake; edge cases iterate.

### Definitional / Frame-exit Completeness

**Gating predicate check:** the inquiry inherits the 7 policies + `TranslationConfig` + `PipelineConfig` from the schema; the inquiry's committed structures (the 4-layer concept-list) use these inherited terms across distinct values/levels. **Gating fires.**

1. **Existence Enumeration.** Each of the 7 policies, when examined across "where does this fire?", surfaces TWO project-wide referent values: (a) the policy's VALUE (Literal string) lives in `TranslationConfig`; (b) the policy's TARGET ELEMENT (what it operates on) must be PRESENT in the parsed source — i.e., in `IntakeDoc`.

2. **Role Assessment.** The TARGET ELEMENT referent (b) is excluded from this inquiry's translation-internals-out frame... wait. Let me recheck. (b) is INSIDE the intake frame — `IntakeDoc` IS intake's product. So actually this referent IS in-frame. The translate-time VALUE choice (a) is the out-of-frame referent. Both referents are needed: (a) belongs to translate (out-of-frame per MQ4), (b) belongs to intake (in-frame). **The two referents map cleanly to the in/out-of-frame split. No re-location needed.**

3. **Verdict Rigor.** "Translation-internals-out" verdict — strongest counter is: but the 7 policies STRADDLE the boundary, so calling translate-internals out-of-frame might exclude design questions intake needs (e.g., "what does intake need to perceive to feed `HonorificsPolicy`?"). Counter test: this is genuine — intake's perception scope is DEFINED BY what each policy needs. So intake can't be designed without referencing the policies. **Resolution:** the policies' VALUES are out-of-frame; the policies' INPUT REQUIREMENTS (what intake must perceive to feed them) are IN-frame. This is the perception/rendering split from KI2. Sound on structural grounds.

4. **Residual / Coverage Justification.** Any frame-exit concern not captured? — The Mac app's UI surface (MQ4 exclusion). Existence: present project-wide (the v0.1 app exists). Role: the app eventually needs an intake button / quality-report dialog — but that's downstream of the intake stage's existence. **Verdict:** correctly out-of-frame for this inquiry; flagged for future inquiry once intake is built.

### Phase / Calibration-State

Project state: v0.1 with the Mac app; v0.2 is the first real intake stage. Calibration corpus: Risale-i Nur. Intake design should be calibrated for the corpus (test on Risale-i Nur features) but not scoped to it (per SKILL.md's generic-product framing). The 7 policies' default values are already calibrated for Risale-i Nur-shape texts; intake just needs to PERCEIVE the elements those defaults are tuned for.

### Meta-Inspection — H1 (candidate set), H2 (frame scope, covered above), H3 (question framing), H7 (phase, covered above)

- **H1.** The candidate set (110 → ~30-40) is the right SET — all 4 layers are present, weighted by relevance. Pruning criteria honor the schema (KI1-KI3) + the painpoint (KI5) + the engineering-actionability criterion (SP3).
- **H3.** The question "identify a list of intake-handling concepts" is framed without pre-bias — the user gave examples (PDF/md/RTF) but didn't constrain the list's shape. The finding's hybrid (layered + decision-flagged) honors the wording.

### SV3 — Multi-Perspective Understanding

After perspective checking:

1. The deliverable should be **HYBRID**: layered grouping (4 layers) + per-concept decision-status flag (DECIDE-NOW / DESIGN-NEXT-INQUIRY / ENGINEER / DEFER).
2. **Pandoc** is the architectural lever for format conversion; OCR (Tesseract / OCRmyPDF) is the depth-1 sub-pipeline for scan-only PDFs.
3. **Canonical intake format = Pandoc-md-superset** (Pandoc's extended markdown with footnotes, tables, definition lists, citations, YAML frontmatter for apparatus).
4. **Quality target = structure-preservation** (the painpoint-aligned choice).
5. **`IntakeDoc` shape = tree-of-containers + cross-referenced flat collections** (tree for chunking; flat for apparatus).
6. **The 7 policies divide cleanly: intake PERCEIVES (sets `IntakeDoc` fields/tags); translate CHOOSES + RENDERS** (sets the policy's Literal value).
7. Pruning the 110 candidates → ~30-40 load-bearing concepts.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — Kinds-axis scope (Specific-vs-pattern recognition cue applies)

**Ambiguity:** Does the concept-list span all 4 layers (format / structure / pipeline / quality) or scope to format-layer only (user's substrate examples)?

**Strongest counter-interpretation (format-only):** the user's only specific examples were PDF / md / RTF — all format-layer. The substrate strongly suggests format-thinking. A small list of examples might be exactly the whole problem the user has — not a "few cases of a wider pattern."

**Why the counter fails (structural grounds):** the four layers COMPOSE into one problem (KI6/KI7). You cannot make a format decision without knowing what structure intake must perceive — picking md without knowing you need footnotes for marginalia is exactly the architecture-debt path. You cannot define perception without naming the pipeline stages (parse / normalize / segment) that produce it. You cannot validate intake without defining quality (preservation %). Format-only would leave the engineer blind to structure decisions that the format choice forecloses. The user's examples are NOT the whole problem — they are the SURFACE of the painpoint, with structural decisions implicit underneath.

**Confidence:** HIGH.

**Resolution:** ALL 4 layers in the concept-list, with format-layer weighted heaviest (matches painpoint).

**What is now fixed:** deliverable spans 4 layers.
**What is no longer allowed:** format-only scoping.
**What depends:** finding-shape (must accommodate 4-layer grouping).
**Conceptual model change:** kinds-axis is non-rivalrous; layers cohere.

### Ambiguity 2 — Finding shape

**Ambiguity:** Flat list (a) / layered (b) / decision-driven (c) / hybrid (d)?

**Strongest counter-interpretation (flat list):** user said "list," not "structured set of layered groups." Flat respects the literal ask.

**Why the counter fails:** a flat list of 30-50 concepts loses layer relationships (KI7). The user needs to USE the list (decide canonical format, design `IntakeDoc`, plan engineering); flat forces them to re-derive structure. Hybrid (b+c) gives layers AND decision-status, serving all 4 WHY-axis motivations (unblock painpoint / avoid debt / scope engineering / meta-reframe).

**Confidence:** HIGH.

**Resolution:** hybrid (d) — layered grouping (4 layers) + per-concept tag from `{DECIDE-NOW, DESIGN-NEXT-INQUIRY, ENGINEER, DEFER}`.

**What is fixed:** finding shape.
**What is no longer allowed:** pure-flat or pure-decision-driven shape.
**What depends:** the load-bearing pruned list's structure.

### Ambiguity 3 — F2: Canonical intake format

**Ambiguity:** md (CommonMark) / md + RTF / Pandoc-md-superset / custom (.compldoc precursor)?

**Strongest counter-interpretations:**
- **md (CommonMark):** clean, lossless md→md, universal tool support. Counter: no native footnotes / tables / definition-lists / marginalia primitive → cannot represent Risale-i Nur features in v0.2.
- **md + RTF:** covers md's gaps with RTF for "complicated texts." Counter: RTF is editor-fragile (looks different in Word / Pages / TextEdit); defeats hand-editing recovery path (FP4); format-fragmentation increases parser surface.
- **Pandoc-md-superset:** Pandoc's extended markdown — footnotes, tables, definition-lists, citations, YAML frontmatter, raw-attribute escape. Single format, covers md's gaps. Counter: Pandoc-specific extensions are less portable than vanilla md.
- **Custom (.compldoc precursor):** total control over schema. Counter: significant engineering burden for v0.2; reinvents Pandoc.

**Why counters fail / why Pandoc-md-superset wins:**

- **vs vanilla CommonMark:** genuinely lacks needed primitives for Risale-i Nur — footnotes for marginalia, tables for apparatus criticus, definition-lists for glossaries. Trying to represent these in pure CommonMark requires custom inline syntax → effectively reinventing Pandoc-md-superset under another name.
- **vs md + RTF:** RTF's editor-fragility means the same RTF file looks different across Word / Pages / TextEdit. The hand-editing recovery path (FP4) depends on a stable on-disk representation. RTF fails this. Also, having TWO canonical formats doubles the parser surface and the test surface.
- **vs custom:** v0.2 has no resources for designing + implementing a custom format. Pandoc-md-superset is "free" engineering. Custom is v1+ when intake patterns are established.

Pandoc-md-superset wins on: (i) covers all needed primitives off-the-shelf; (ii) single format → single parser surface; (iii) human-readable (text + YAML); (iv) hand-editable; (v) Pandoc-as-converter absorbs the format-layer; (vi) revisitable later if scaling.

**Confidence:** MEDIUM-HIGH. Pandoc-md-superset is the right choice for v0.2 given the corpus + the resource constraint; the choice is revisitable when scaling beyond Risale-i Nur.

**Resolution:** Canonical intake format = **Pandoc-md-superset** (Pandoc's extended markdown: footnotes, tables, definition-lists, citations, YAML frontmatter for apparatus + metadata). USER-PROVIDED formats accepted: PDF (text-layer + OCR pathway), docx, RTF, md, EPUB, HTML, plain-text → all converted to Pandoc-md-superset via Pandoc on intake.

**What is fixed:** canonical intake format.
**What is no longer allowed:** vanilla CommonMark as canonical; RTF as canonical (still accepted as USER input).
**What depends:** every parser uses Pandoc; `IntakeDoc` field design must capture footnote / table / definition-list / citation primitives.
**Conceptual model change:** "intake-format standard" is no longer a PER-DOCUMENT user choice; it's an INTERNAL canonical representation. The user just provides whatever they have; intake normalizes.

### Ambiguity 4 — F3: Quality-target

**Ambiguity:** structure-preservation / typography-preservation / semantic-only?

**Strongest counter-interpretations:**
- **typography-preservation:** preserves italic / bold / font choices that may carry meaning. Counter: typography is conflated with semantic emphasis. Intake should preserve EMPHASIS as a structural primitive (italic-as-emphasis, bold-as-strong-emphasis); raw typography (font face, size, color) is rendering, not structure.
- **semantic-only:** drops typography AND structure, keeps text only. Counter: loses chapter / paragraph boundaries that translation needs for context (chunking-by-chapter is a real `PipelineConfig.chunking_granularity` option).

**Why counters fail:**

- **typography-preservation** includes too much (font / size / color is rendering noise) and not enough (might miss chapter-level structure visible only via heading-typography signals — a heading IS structural even when its only signal is being-larger).
- **semantic-only** drops too much (chapter / paragraph boundaries are NEEDED for chunking + for translation context). User's painpoint is EXACTLY this loss.

**Confidence:** HIGH.

**Resolution:** Quality target = **structure-preservation** (preserve hierarchical containment, paragraph boundaries, footnotes, marginalia, embedded poetry, voice transitions, archaic register markers, formulaic openings, non-main-language spans). Emphasis (italic / bold) is preserved as a STRUCTURAL primitive (semantic emphasis); raw typography (font / size / color) is dropped.

**What is fixed:** quality target = structure-preservation.
**What is no longer allowed:** typography-fidelity as a primary goal; semantic-only stripping.
**What depends:** intake-quality-metrics (measure structure-elements-preserved %); `IntakeDoc` fields (must hold the 7 policy targets as perceived elements).
**Conceptual model change:** "structure-preservation" becomes the load-bearing quality property; "fidelity" and "lossiness" are measured against it.

### Ambiguity 5 — F5: 7 policies' intake-vs-translate attribution

**Ambiguity:** Which of the 7 policies operate at intake-time vs translate-time?

**Strongest counter-interpretation:** ALL 7 are translate-time only — the schema names them as translation policies (they live in the translation config). Counter: but the schema's docstrings reference SOURCE features (Said Nursi's hashiye, Mevlana couplets, Islamic honorifics) — these are things present in the SOURCE, not invented at translate-time.

**Why the counter fails (structural grounds):** the policy VALUE (chosen Literal string) is set at translate. But the policy's ACTIVATION CONDITION (does this source have marginalia AT ALL?) is set at intake. Without intake having perceived marginalia, `SourceApparatusPolicy.translate-as-footnote` has nothing to apply to — it would be a vacuous setting.

**Confidence:** HIGH.

**Resolution:** ALL 7 policies have BOTH an intake-time PERCEPTION component (what intake must FIND in the source and represent in `IntakeDoc`) AND a translate-time RENDERING component (the value choice in `TranslationConfig`). The split:

| Policy | Intake-time perception | Translate-time rendering |
|---|---|---|
| `NonMainLangPartsPolicy` | Detect non-main-language spans (script change, langid signal) | Choose render strategy (preserve / replace / translate / annotate) |
| `SourceApparatusPolicy` | Detect marginalia / glosses / apparatus criticus | Choose render placement (drop / inline-bracketed / footnote / channel) |
| `VoiceMarkingPolicy` | Detect voice transitions (author vs cited authority vs student) | Choose marking style |
| `ArchaicRegisterPolicy` | Detect archaic register markers (lexical / syntactic) | Choose modernize / preserve / hybrid |
| `HonorificsPolicy` | Detect honorifics (suffix patterns after names) | Choose render (preserve / transliterate / translate / abbreviate / drop) |
| `FormulaicOpeningPolicy` | Detect formulaic openings (Bismillah, dedications, preambles) | Choose render |
| `EmbeddedPoetryPolicy` | Detect embedded poetry (verse-in-prose) | Choose render |

**What is fixed:** every policy has both halves; intake's perception scope is exactly the union of these 7 perceptions.
**What is no longer allowed:** treating any of the 7 policies as translate-only (it would skip the perception step).
**What depends:** `IntakeDoc` must have a representation for each of these 7 perceived element-types.

### Ambiguity 6 — F1: `IntakeDoc` high-level shape

**Ambiguity:** tree-of-chapters / flat-list-of-paragraphs-with-region-tags / hybrid?

**Strongest counter-interpretations:**
- **pure tree:** cleaner hierarchy. Counter: marginalia and embedded poetry are NOT cleanly tree-attached — they reference back to a position in the main body. Forcing them into the tree either breaks paragraph-adjacency or produces awkward sub-node positions.
- **pure flat-list-with-region-tags:** simpler chunking. Counter: loses hierarchical context. Chunking-by-chapter (a real `PipelineConfig.chunking_granularity` option) requires reconstructing the tree from tags — fragile.

**Why counters fail:** pure tree forces apparatus into the wrong place; pure flat loses chapter-context.

**Confidence:** MEDIUM-HIGH (the SHAPE is committed; exact fields are downstream).

**Resolution:** Hybrid — **tree of containers (chapter → section → paragraph) with each leaf-node carrying region-tag metadata + inline markers that reference cross-collections** at the `IntakeDoc` root (footnotes, marginalia, embedded-poetry, voice-transitions). Pseudocode:

```
IntakeDoc:
  metadata: {title, author, source-format, intake-time, language, ...}
  body: Container (root)
    children: [Container | Paragraph]
      Container (chapter | section)
        title: Text
        children: [...]
      Paragraph
        runs: [Text | Marker]
          Marker:
            type: footnote-ref | marginalia-ref | voice-mark | ...
            ref-id: → root-level collection
  apparatus:
    footnotes: {id → FootnoteNode}
    marginalia: {id → MarginaliaNode}
    embedded-poetry: {id → PoemNode}
    formulaic-openings: {id → OpeningNode}
    non-main-language: {id → SpanNode}
```

**What is fixed:** high-level shape (tree + cross-ref-flat).
**What is no longer allowed:** pure tree (forces apparatus into wrong place); pure flat (loses chapter context).
**What depends:** every parser populates this shape; every translate step consumes it.

### Ambiguity 7 — Load-bearing concept test for "IntakeDoc"

**Ambiguity:** Is "IntakeDoc" a load-bearing structural term or a loop-coined neologism?

**Strongest counter-interpretation:** "IntakeDoc" is generic / non-distinctive; the project might prefer `Document` / `ParsedSource` / `CanonicalDoc` / `Compldoc` / something else.

**Why the counter fails (partial):** there's no prior project commitment to a name. The schema doesn't name the object. The ROLE (the doc produced by intake; the contract with translate) is structural and load-bearing. The LABEL is editable.

**Confidence:** HIGH on the role; LOW on the specific name.

**Resolution:** Use **`IntakeDoc`** as the canonical placeholder in this finding; flag that the actual class/file name is a downstream decision (likely `Document` or similar, aligned with whatever the project's Python module structure adopts).

### Ambiguity 8 — User's central question: what IS the actionable list?

**Ambiguity:** After all the above, what's the actual concept-list the user wanted?

**Strongest counter (against any specific number):** the user might have wanted a much smaller list (5-10 items, format-only) rather than a 30-40-item hybrid.

**Why the counter fails:** a 5-10-item list would either drop layers (incompleteness; KI7 violation) or merge concepts (loss of decision-granularity; SP3 violation). The hybrid 4-layer ~30-40-concept list is the smallest list honoring the kinds-axis without information-loss.

**Confidence:** HIGH.

**Resolution:** ~30-40 concepts, organized in 4 layers, each tagged DECIDE-NOW / DESIGN-NEXT-INQUIRY / ENGINEER / DEFER. The finding's Action List section (see SV6) is the realization.

### SV4 — Clarified Understanding

After ambiguity collapse, the model commits to:
- **Shape:** hybrid (4-layer grouping + per-concept decision-status tag).
- **Canonical intake format:** Pandoc-md-superset.
- **Quality target:** structure-preservation.
- **`IntakeDoc` shape:** tree-of-containers + cross-referenced flat collections.
- **7 policies:** all have intake-time perception + translate-time rendering halves.
- **Coverage:** ~30-40 load-bearing concepts.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed

- All 4 layers (format / structure / pipeline / quality) present.
- Hybrid finding shape.
- Pandoc-md-superset as canonical intake format.
- Pandoc as architectural lever for conversion; OCR (Tesseract / OCRmyPDF) as depth-1 sub-pipeline for scan-only PDFs.
- Structure-preservation as quality target.
- `IntakeDoc` shape = tree-of-containers + cross-referenced flat collections.
- 7 policies split: perception at intake; rendering at translate.

### Eliminated

- Format-only scoping (Ambiguity 1).
- Pure-flat or pure-decision-driven finding shape (Ambiguity 2).
- Vanilla CommonMark as canonical (Ambiguity 3).
- RTF as canonical (still accepted as user input; Ambiguity 3).
- Custom format (.compldoc precursor) for v0.2 (Ambiguity 3).
- Typography-fidelity as quality target (Ambiguity 4).
- Semantic-only stripping (Ambiguity 4).
- Treating any policy as translate-only or intake-only (Ambiguity 5).
- Pure-tree or pure-flat `IntakeDoc` (Ambiguity 6).

### Remaining variables (downstream inquiries)

- Exact `IntakeDoc` field schema (typed pydantic class with all the apparatus collections + the tree).
- Per-format Pandoc invocation flags (e.g., `--extract-media` for figures; `--standalone`; per-format reader).
- OCR sub-pipeline depth (Tesseract config, OCRmyPDF wrapping, layout-analysis options).
- Human-review gate UX (when intake quality is uncertain — out-of-frame for THIS inquiry; future).
- Multi-file project intake mechanics (a book is 30 PDFs; do we merge to one `IntakeDoc` or stack many?).
- The perception detectors for each of the 7 policies (these are 7 distinct engineering tasks in v0.2+).

### SV5 — Constrained Understanding

The concept-list converges to ~30-40 items across 4 layers, with per-concept decision-status. Five immediate decisions are now made (canonical format, quality target, `IntakeDoc` shape, perception/rendering split, Pandoc-as-architectural-lever). The remaining design-next-inquiry items concentrate around `IntakeDoc` schema details + the 7 perception detectors. The engineer-now items are the standard intake pipeline stages. The defer items are v1+ concerns (.compldoc precursor, schema versioning machinery, advanced quality metrics).

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Did perspectives keep destabilizing the model? **No.** The "4 layers cohere as aspects" insight (KI6/KI7) stabilized the model in Phase 1. Phase 2 confirmed without revising. Phase 3 refined the decisions (canonical format, quality target, etc.) without dropping back to re-extract anchors. The model fits the territory — no patching required.

### Self-Reference Blindness check

Is the inquiry's subject the discipline being applied? **No.** The subject is intake-handling concepts; the framework is sense-making. Different substrates. External grounding present (the schema's existing 7 policies; Pandoc's known capabilities; the user's painpoint).

### SV6 — Stabilized Model

The deliverable is a **layered + decision-flagged list of ~30-38 intake-handling concepts**, organized in 4 layers, each concept tagged with its decision-status (DECIDE-NOW / DESIGN-NEXT-INQUIRY / ENGINEER / DEFER). The five load-bearing commitments are:

1. **Canonical intake format = Pandoc-md-superset.**
2. **Quality target = structure-preservation.**
3. **`IntakeDoc` shape = tree-of-containers + cross-referenced flat collections.**
4. **7-policy split: intake perceives + represents; translate chooses + renders.**
5. **Pandoc as architectural lever for format-layer; OCR (Tesseract/OCRmyPDF) as depth-1 sub-pipeline for scan-only PDFs.**

The user's central question — "what IS the actionable list?" — is answered by the next section.

---

## The Concept List (Stabilized Output)

### Layer A — Format-layer (8 concepts)

| # | Concept | Status | One-line |
|---|---|---|---|
| A1 | Canonical intake format | **DECIDE-NOW: Pandoc-md-superset** | Pandoc's extended md (footnotes, tables, def-lists, citations, YAML frontmatter) — internal representation |
| A2 | Accepted user-provided formats | **DECIDE-NOW: PDF + docx + RTF + md + EPUB + html + .txt** | Pandoc handles 6 of 7; PDF needs the OCR sub-pipeline when text-layer absent |
| A3 | OCR sub-pipeline (Tesseract + OCRmyPDF) | DESIGN-NEXT-INQUIRY | Depth-1 sub-pipeline for scan-only PDFs; config + flags + fallback rules |
| A4 | Pandoc invocation per format | DESIGN-NEXT-INQUIRY | Reader flags, extensions enabled, `--standalone`, `--extract-media` per source format |
| A5 | Format detection / sniffing | ENGINEER | When the file extension is unreliable; magic-bytes + mime |
| A6 | Mixed-script + RTL handling | DESIGN-NEXT-INQUIRY | Arabic + Turkish + Latin interleaved (Risale-i Nur shape); diacritics preservation |
| A7 | Pandoc → `IntakeDoc` conversion | ENGINEER | The mapping from Pandoc AST to our `IntakeDoc` shape |
| A8 | Format-fidelity gradient | DEFER (v1+) | Measure-and-report format-conversion loss along the gradient |

### Layer B — Structure-layer (12 concepts)

| # | Concept | Status | One-line |
|---|---|---|---|
| B1 | The structure-vs-style distinction | **DECIDE-NOW: AXIOM** | Intake preserves structure; raw style (font/size/color) is dropped; semantic emphasis (italic-as-emphasis) is structure |
| B2 | Hierarchical containment (chapter → section → paragraph) | DECIDE-NOW: tree-as-primary | The skeleton of `IntakeDoc` |
| B3 | Footnotes / endnotes | ENGINEER | Pandoc-md-superset has native footnote syntax; cross-ref into apparatus collection |
| B4 | Marginalia / hashiye (perception for `SourceApparatusPolicy`) | DESIGN-NEXT-INQUIRY | What signals identify marginalia in source? How represented in `IntakeDoc`? |
| B5 | Embedded poetry (perception for `EmbeddedPoetryPolicy`) | DESIGN-NEXT-INQUIRY | What signals identify verse-in-prose? Detector heuristics |
| B6 | Formulaic openings (perception for `FormulaicOpeningPolicy`) | DESIGN-NEXT-INQUIRY | What signals identify invocations / preambles? Detector heuristics |
| B7 | Voice transitions (perception for `VoiceMarkingPolicy`) | DESIGN-NEXT-INQUIRY | What signals identify author-vs-cited-authority shifts? |
| B8 | Archaic register markers (perception for `ArchaicRegisterPolicy`) | DESIGN-NEXT-INQUIRY | What signals identify archaic register? |
| B9 | Honorifics (perception for `HonorificsPolicy`) | DESIGN-NEXT-INQUIRY | What suffix patterns identify honorifics? Per-tradition? |
| B10 | Non-main-language spans (perception for `NonMainLangPartsPolicy`) | DESIGN-NEXT-INQUIRY | Script change + langid signals |
| B11 | Frontmatter / backmatter / TOC | ENGINEER | Distinct boundaries; tag `body` vs `frontmatter` vs `backmatter` |
| B12 | Emphasis as structural primitive | ENGINEER | Italic → emphasis; bold → strong-emphasis; preserved in `IntakeDoc` |

### Layer C — Pipeline-layer (10 concepts)

| # | Concept | Status | One-line |
|---|---|---|---|
| C1 | `IntakeDoc` schema (the tree + apparatus shape) | DESIGN-NEXT-INQUIRY | Exact pydantic class with fields, types, validators |
| C2 | The intake-vs-translate boundary | **DECIDE-NOW: intake outputs `IntakeDoc`; translate consumes it** | Architectural seam; intake's contract is the schema |
| C3 | Parse stage | ENGINEER | Pandoc reader → Pandoc AST |
| C4 | Normalize stage | ENGINEER | Whitespace canonicalization, unicode NFC, punctuation normalization, line-ending unify |
| C5 | Segment stage | ENGINEER | Identify chapter / section / paragraph boundaries from Pandoc AST |
| C6 | Validate stage | ENGINEER | Sanity-check the parsed `IntakeDoc` against schema + per-format expectations |
| C7 | Pre-validation (file is supported) | ENGINEER | Fail-fast before parsing |
| C8 | Post-parse validation (structure makes sense) | ENGINEER | Per `IntakeDoc` schema + heuristic checks |
| C9 | Intake metadata + language detection | ENGINEER | YAML frontmatter; langid for language; encoding-detection for raw `.txt` |
| C10 | Multi-file project intake | DESIGN-NEXT-INQUIRY | A book = 30 PDFs → one `IntakeDoc` (merged chapters) or stacked? |

### Layer D — Quality-layer (8 concepts)

| # | Concept | Status | One-line |
|---|---|---|---|
| D1 | Intake-quality-target | **DECIDE-NOW: structure-preservation** | The chosen target; structure preserved, raw typography dropped, semantic emphasis preserved |
| D2 | Fidelity + lossiness framing | DESIGN-NEXT-INQUIRY | How is "% of structure preserved" measured per `IntakeDoc` field? |
| D3 | Intake-quality-metrics | DESIGN-NEXT-INQUIRY | Structure-elements-preserved %, per-chapter integrity, apparatus-resolution % |
| D4 | Intake-quality-gates | DESIGN-NEXT-INQUIRY | Threshold below which translation should refuse to proceed |
| D5 | Intake-edit-after-parse | DECIDE-NOW: SUPPORTED | The hand-editing recovery path; `IntakeDoc` round-trips to Pandoc-md-superset on disk |
| D6 | Paratext handling (page numbers, headers, footers) | DESIGN-NEXT-INQUIRY | Default: drop. Preserve as metadata only if a flag is set |
| D7 | Intake-time-vs-translate-time error attribution | ENGINEER | Errors carry stage tags so debugging is tractable |
| D8 | Source-of-truth declaration (intake output = canonical; original = read-only after intake) | DECIDE-NOW: YES | Once intake completes, the `IntakeDoc` is the canonical; the user's original file is preserved-as-read-only |

**Total: 38 concepts.** Decision-status distribution: **DECIDE-NOW = 9** · **DESIGN-NEXT-INQUIRY = 18** · **ENGINEER = 11** · **DEFER = 1**.

---

## Inherited Commitments Re-test

### From `articulate_simple.md` — the 5 considered articulations

| Variant | Status after sense-making | Rationale |
|---|---|---|
| 1 — Format-leaning, decision-now | **PARTIALLY ACCEPTED** | Format-layer decisions are made (A1, A2 = DECIDE-NOW), but layer is not standalone |
| 2 — Structure-leaning, architecture-foundation | **PARTIALLY ACCEPTED** | Structure-layer is load-bearing (B1, B2 = DECIDE-NOW), but layer is not standalone |
| 3 — Pipeline-leaning, checklist | **PARTIALLY ACCEPTED** | Pipeline-layer concepts are mostly ENGINEER, becomes the engineering checklist |
| **4 — Cross-layer breadth, enumerate-for-future-deepening** | **PRIMARY** | The hybrid finding shape spans all 4 layers; many concepts seed future inquiries (DESIGN-NEXT-INQUIRY tag) |
| **5 — Pragmatic-painpoint, enumerate-for-current-decision** | **SECONDARY** | The DECIDE-NOW tagged concepts (9 of them) answer the user's immediate decision needs |

Variant 4 is the primary commit; variant 5 is layered into it via decision-status tags. Variants 1/2/3 are absorbed as layer-internal weight.

### From `surfacing.md` — 110 candidates spanning 4 layers

Pruning honored: 38 load-bearing of 110 (~35%). The 72 dropped:
- 10-15 format-layer edge cases (LaTeX, math notation, ligature handling per-format, .compldoc precursor v1+) → deferred to scaling-beyond-Risale-i-Nur inquiries.
- 15-20 structure-layer edge cases (code blocks, captions, citations sub-types, original-vs-modernized spelling, colophons, editorial brackets) → covered by Pandoc-md-superset's primitive set without needing per-concept design.
- 5-10 pipeline-layer operational concepts (logging, audit trail, streaming-vs-load-all, schema versioning) → deferred to v1+.
- 8-12 quality-layer secondary concerns (round-trippability as measure, reference intake, inter-intake-diffing, "good-intake=downstream-success" framing) → either subsumed by quality-metrics design or deferred.

Pruning purpose-bias check: the 38 retained all have downstream consequences for one or more of `[unblock-real-painpoint / avoid-architecture-debt / scope-the-engineering-task / meta-reframe]`. The dropped 72 are either redundant, edge, or v1+.

### From `SKILL/references/config/schemas.py` — the 7 policy classes

Re-test: the finding RESPECTS the 7 policies as the downstream contract; does NOT redefine them. The finding's commitment is to PERCEIVE the elements each policy operates on (intake-time) and represent them in `IntakeDoc` (the contract). The policies' VALUES (Literal choices) remain unchanged and translate-time. No schema change required for this inquiry.

### From the warm Mac-app session substrate

Re-test: the Mac app's UI surface is OUT-OF-FRAME for this inquiry (per MQ4). When intake is built (v0.2+), the app eventually needs an intake button + a quality-report dialog — flagged as Frontier F4 for after-CONCLUDE.

---

## How SV6 differs from SV1

| Dimension | SV1 (baseline) | SV6 (stabilized) |
|---|---|---|
| Scope | "List of intake concepts, lean format" | All 4 layers, weighted by relevance + decision-status |
| Shape | "Probably a layered enumeration" | HYBRID: layered + per-concept decision-status tag |
| Format choice | "md or md+RTF, undecided" | **Pandoc-md-superset** (with vanilla CommonMark and RTF-as-canonical eliminated) |
| Quality target | "Undecided" | **Structure-preservation** (typography-fidelity and semantic-only eliminated) |
| `IntakeDoc` shape | "Some kind of document structure" | **Tree-of-containers + cross-referenced flat collections** |
| 7 policies attribution | "Probably all translate-side" | **All 7 have intake-perception + translate-rendering halves** |
| Action surface | "Vague — read the list" | **9 DECIDE-NOW + 18 DESIGN-NEXT-INQUIRY + 11 ENGINEER + 1 DEFER** |

The shift is from a vague "produce a list" to a stabilized model that names the load-bearing decisions (5), commits to them, and routes the remaining work into typed downstream tracks.

---

## Self-Assessment

- **Saturation indicators:**
  - Perspective saturation: ✓ (perspectives 4-6 mostly confirmed Phase 1 anchors).
  - Ambiguity resolution: 8/8 resolved (all HIGH or MED-HIGH confidence).
  - SV delta: substantial (SV1 said "vague list," SV6 commits to 5 decisions + 38-concept structure).
  - Anchor diversity: 7 constraints + 8 insights + 4 structural points + 4 principles + 6 meaning-nodes; perspectives 6/6.

- **Failure modes checked:**
  - Status Quo Bias: no — the finding doesn't defend the schema-as-is; it splits the policies into perception/rendering halves, which is a genuine new commitment.
  - Premature Stabilization: no — 8 ambiguities each tested with strongest counter.
  - Anchor Dominance: no — KI7 (4 layers cohere) is load-bearing but doesn't carry every decision (e.g., Pandoc-md-superset comes from KI8 + resource analysis, not KI7).
  - Perspective Blindness: no — Risk and Feasibility perspectives produced real anchors (RTF editor-fragility, Pandoc-handles-80%).
  - Clean Resolution Trap: not on F2 (counter-arguments for md+RTF and CommonMark structurally tested); not on F3 (counter for typography-preservation structurally tested).
  - Self-Reference Blindness: no (subject is intake; framework is sense-making — disjoint).

- **Meta-Inspection summary:**
  - H1 (candidate set): tested — 110 → 38 with explicit pruning rationale.
  - H2 (frame scope): tested via Frame-exit Completeness perspective; 7 policies cleanly split.
  - H3 (question framing): tested informally — user's literal "list" honored via hybrid shape.
  - H4 (concept names): tested for "IntakeDoc" (label editable, role committed) and "Pandoc-md-superset" (precise enough).
  - H5 (motivating examples): tested via Specific-vs-pattern check at Ambiguity 1 — user's PDF/md/RTF examples are surface, not whole.
  - H6 (model fit): no patching observed; Accommodation trigger not fired.
  - H7 (phase/calibration state): tested — design calibrated to Risale-i Nur, not scoped to it.
  - H8 (self-reference): tested — no shared framework.
  - H9 (user-language alignment): tested — "IntakeDoc" is placeholder; user said "list" and got list.

- **Verdict:** **PROCEED to Decomposition.** The stabilized model carries 5 load-bearing commitments, an 8-row decision-status matrix, and a 38-concept layered list ready to be decomposed into engineerable pieces.
