---
status: active
model: claude-opus-4-7
effort: max
corrects: devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md
corrects: devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md
refines: devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md
---

# Finding: schemas_rationale_and_policy_list

## Changes from Prior

**Prior paths:**
- `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md` — the most recent finding that placed `chunking_granularity` on `TranslationConfig` and committed `SourceDescriptor.canonical_level` plus corpus mappings to schema. Three central schema-shape commitments here are now corrected.
- `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md` — routed 4 fields to `SourceDescriptor` (`source_language_fluency`, `source_edition`, `source_temporal_register`, `embedded_languages: list[EmbeddedLanguagePolicy]`). All 4 SD routings are now INVALID at schema location.
- `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` — established the *"schema ownership matches data ownership"* principle (FP1) and committed `SourceDescriptor` as a paper schema. The principle is preserved with frame revision; the SD commitment is INVALID.

**Revision trigger:** Direct user simplification — across four conversational turns (drop SD; replace per-language EmbeddedLanguage with language-agnostic `NonMainLangPartsPolicy`; freeze TC unchanged; keep `PipelineConfig` mostly unchanged) culminating in a hand-written `schemas.py`. The user then asked this inquiry: *"explain why schemas.py makes a lot more sense + list other policies like NonMainLangPartsPolicy."*

**What's preserved.**
- The 8 axes of `TranslationConfig` (frozen, unchanged from `translation_config.py`).
- The split-placement principle ("schema ownership matches data ownership") as FP1, with frame revision (see below).
- The 5-literal granularity value set (`sentence` / `paragraph` / `passage` / `subchapter` / `chapter`) — moved to `PipelineConfig` instead of `TranslationConfig`.
- The 6-literal `chunking_mechanism_override` value set on `PipelineConfig`.
- The hybrid harmony-aware default chunking mechanism (still the implicit AI default behind `chunking_mechanism_override: None`).
- `NonMainLangPartsPolicy` as the first instance of the Policy layer.
- A4-driven defaults pattern (A4 `purpose` still drives some downstream defaults).

**What's changed.**
- **New foundational principle (FP2): *"Don't declare what the LLM can infer."*** FP1 said the schema must own the data it represents; FP2 narrows what counts as data the schema must own — anything the LLM derives from the source text is no longer schema-owned data. FP2 is the load-bearing principle that generates the simplification.
- **Architecture: 3-LAYER, not 3-schema.** Was: `SourceDescriptor` (source facts) + `PipelineConfig` (runtime) + `TranslationConfig` (user strategy). Now: `TranslationConfig` (user strategy axes) + Policy classes (per-edge-case enums) + `PipelineConfig` (engine knobs). Policy is a structurally distinct third schema-kind, not a naming convention.
- **`SourceDescriptor` dropped.** Its fields were either LLM-inferable (drop), structurally inappropriate (canonical_level imposing universal hierarchy), or properly belong as Policy classes (`source_temporal_register` → `ArchaicRegisterPolicy`).
- **`chunking_granularity` moved from TC to PC.** It is operational (runtime), not strategic (user-facing).
- **Per-language `EmbeddedLanguage` replaced by language-agnostic `NonMainLangPartsPolicy`.** Per-language declarations are LLM-inferable; only the user's handling preference is human-decidable.
- **Edge-cases finding's routings re-routed.** Edge-case #1 (embedded_source_languages) → `NonMainLangPartsPolicy`; #6 (source_apparatus_handling) → `SourceApparatusPolicy` candidate; #7 (passage_typology) → deferred (not policy-shaped).

**What's new.**
- The four filters for catalog membership (structural shape; language-agnosticism; authorial-edge-case category; LLM-can't-infer).
- A 15-entry Policy catalog (6 strong + 4 moderate + 5 deferred) with pydantic class sketches.
- An explicit `Inherited Commitments Re-test` table with verdicts per inherited commitment from 3 priors.
- The LLM-inferable test predicate as an operational rule: *"at integration time, ask: can the LLM derive this value from the source text plus the rest of the config?"*

**Migration.** `schemas.py` already reflects the simplified architecture. Future Policy-class adoption from this finding's Item 2 catalog is gated on user review per the Next Actions MUST item. The 3 prior findings receive Correction Notices at top (also per Next Actions MUST).

---

## Question

From `_branch.md`, the inquiry has two items:

**Item 1:** *"Explain why `/Users/ns/Desktop/projects/comprehenslate/schemas.py` makes a lot more sense."* Implicit comparison target: the four-schema design that this conversation iterated past (`TranslationConfig` + `SourceDescriptor` + `EmbeddedLanguageProfile` + `PipelineConfig`) and, more broadly, the trajectory of design commitments from the chunking deep-dive and chunk_types_vs_mechanisms findings.

**Item 2:** *"What other scenarios, policies like `NonMainLangPartsPolicy` exist? Give me a list of them."* The shape being templated: a single-field `BaseModel` carrying a small `Literal[N]` enum that governs a recurring authorial edge-case requiring user value judgment.

**Goal.** A prose rationale that captures the design principle (Item 1) and a filtered, ranked list of Policy-class candidates with concrete pydantic sketches (Item 2). Both items derive from the same principle; section 1 names the principle, section 2 applies it.

---

## Finding Summary

- **The principle: *"Don't declare what the LLM can infer."*** A schema field belongs in `schemas.py` only when the LLM cannot derive its value from the source text plus the rest of the configuration. This refines the chunking finding's earlier *"schema ownership matches data ownership"* by narrowing what counts as data the schema must own.

- **The architecture is three-LAYER.** `TranslationConfig` (user strategy, 8 axes, frozen) + Policy classes (per-edge-case `Literal[]` enums governing authorial value judgments) + `PipelineConfig` (engine knobs the operator tunes). Policy is a structurally distinct third schema-kind, not a naming convention.

- **Four filters gate Policy-class membership.** (1) structural shape — single-field `BaseModel` with `Literal[N]` enum; (2) language-agnosticism — no language/tradition names in enum literals; (3) authorial edge-case — the phenomenon is something the author did, not translator/publication/reader-side; (4) LLM-can't-infer — the handling decision is a human value judgment, not an inference.

- **Item 1 (rationale) applied to dropped/changed classes.** `SourceDescriptor` dropped because its fields are either LLM-inferable (source language, embedded-language detection) or impose structure not present in all corpora (canonical_level). Per-language `EmbeddedLanguage` replaced by language-agnostic `NonMainLangPartsPolicy` for the same reason at a finer grain. `chunking_granularity` moved off `TranslationConfig` because granularity is operational, not strategic.

- **Item 2 (policy list) — 6 strong candidates** with pydantic sketches: `SourceApparatusPolicy` (authorial marginalia like Nursi's hashiye); `VoiceMarkingPolicy` (author vs cited voice); `ArchaicRegisterPolicy` (re-homes the homeless `source_temporal_register`); `HonorificsPolicy` (theological honorifics SAW/AS/RA, ZT"L/OBM); `FormulaicOpeningPolicy` (Bismillah / Shema / invocations); `EmbeddedPoetryPolicy` (Mevlana couplets vs prose embedded language).

- **Item 2 — 4 moderate candidates** with filter caveats: `TransliterationStandardPolicy`; `PriorTranslationStancePolicy`; `AnachronismHandlingPolicy`; `CitationReferenceFormatPolicy`.

- **Item 2 — 5 deferred candidates** with revival triggers: `ScriptDirectionPolicy` (rendering-side, not authorial); `PassageTypologyPolicy` (typology label, not strategy); consumption/reading policies (reader-side); `OutputFinalityPolicy` (pipeline-side); `RelayTranslationPolicy` (carries non-policy structure).

- **Three prior findings are corrected.** The `chunk_types_vs_mechanisms` finding's central schema-shape commitments (TC.chunking_granularity; SD.canonical_level; corpus mappings as schema content) are INVALID. The `chunking_deep_dive` finding's split-placement principle is preserved with frame revision; its `SourceDescriptor` paper-schema commitment is INVALID. The `edge_cases_into_config_schema` finding's 4 SD additions are INVALID at schema location with per-field sub-statuses.

- **Calibration-state caveat.** The LLM-inferable principle assumes current-LLM capability for source-language inference (major languages handled well by Opus 4.7-class models). Rare/dead languages (Aramaic, Coptic, Sumerian) may require declarative fields the current architecture omits. This is a Research Frontier in Open Questions.

---

## Finding

### Why we are even discussing this (small surrounding context)

Comprehenslate is an AI-assisted translation system for Said Nursi's *Risale-i Nur* corpus — 1920s-30s Turkish theological prose with embedded Arabic ayahs, Persian Mevlana couplets, transliterated Sufi formulae, and authorial marginalia called *hashiye*. The project's translation behavior is parameterized by a configuration schema. Earlier inquiries iterated this schema:

- **Original (`translation_config.py`):** an 8-axis `TranslationConfig` (`reader_level` / `domain_expertise` / `source_culture` / `purpose` / `source_fidelity` / `form_preservation` / `scaffolding` / `analysis_depth`).
- **Chunking deep-dive:** added split-placement — three paper schemas (`SourceDescriptor` for source facts; `PipelineConfig` for runtime; `TranslationConfig` for user strategy).
- **Edge-cases:** added 4 fields to `SourceDescriptor`.
- **Chunk types vs mechanisms:** added `chunking_granularity` to `TranslationConfig` and `canonical_level` mapping to `SourceDescriptor.ChunkingUnit`.

Then, in this conversation, the user re-read the proposals and simplified — drop `SourceDescriptor`; replace per-language `EmbeddedLanguage` with language-agnostic `NonMainLangPartsPolicy`; freeze `TranslationConfig` at its 8 axes; keep `PipelineConfig` for chunking knobs. The simplification reduced 4 schemas to 3 (TC + one Policy class + PC) and produced a new file: `/Users/ns/Desktop/projects/comprehenslate/schemas.py`.

The user then asked for two things: an explanation of why this simplification makes more sense (the rationale), and a list of other Policy-class candidates that would fit the same shape (the catalog). This finding answers both.

### 1. The principle: *"Don't declare what the LLM can infer."*

The simplification rests on a new foundational principle. State it verbatim:

> **Don't declare what the LLM can infer.**

This is FP2 — the second foundational principle of the configuration architecture. FP1 is the chunking finding's *"schema ownership matches data ownership"* (the schema must own the data it represents). FP2 doesn't replace FP1; it tightens its application by narrowing what counts as *data the schema must own*: anything the LLM derives from the source text plus the rest of the configuration is no longer schema-owned data.

The principle's operational form is a single integration-time predicate:

> **At integration time, ask of each candidate field: *"Can the LLM derive this value from the source text plus the rest of the config?"* If YES → no schema field needed (the LLM infers it). If NO → schema field carries the user's value judgment.**

This is the LLM-inferable test. It is the gate that decides whether a candidate belongs in the schema.

The user's correction made FP2 explicit: *"translation happens regardless of the source language via LLMs, LLM just needs to know to what lang tranastion happens, and with what config. so we dont need SourceDescriptor."* Modern LLMs detect source language at high reliability for major languages; they don't need it declared. The same logic applies to other corpus facts — embedded-language detection, structural boundaries, paragraph breaks.

### 2. The architecture: three layers, not three schemas

FP2 generates a three-layer architecture. The layers are distinguished by **who decides what**:

| Layer | Holds | Decision axis | Defaults driver | Typical consumer |
|---|---|---|---|---|
| **`TranslationConfig` (TC)** | Continuous strategy axes (the 8 enums) | User-facing translation choices | A4 `purpose` drives some axis defaults | User, once per job |
| **Policy classes** | Per-edge-case `Literal[N]` enum | Authorial edge-case handling decision | Sensible per-edge-case default | User, per relevant edge-case |
| **`PipelineConfig` (PC)** | Runtime engine knobs | Pipeline tuning | None / engine-derived | Operator / dev (rarely user) |

The three columns differ on every row. The layers are not three-schemas-with-different-names; they are three structurally distinct kinds of fact:

- **TC** carries the user's broad strategic preferences (how foreignizing? what reader level? what scaffolding?). The 8 axes are continuous gradients (one per axis).
- **Policy classes** carry the user's per-edge-case value judgments (when an author embeds Arabic in Turkish prose, do you preserve / replace / annotate?). Each Policy class governs ONE recurring authorial edge-case the LLM cannot autonomously decide.
- **PC** carries the operator's engine knobs (token budgets; chunking granularity; mechanism overrides). Not user-facing strategic; not authorial-edge-case-decidable.

`NonMainLangPartsPolicy` is the canonical Policy example. The Policy layer is structurally real, not a naming pattern — a Policy class cannot be collapsed into TC without violating TC-frozen, and cannot be collapsed into PC without losing its "user value judgment" character.

### 3. Item 1 — Why schemas.py makes more sense (the rationale)

Apply FP2 to each dropped or changed class from the prior 4-schema design:

#### `SourceDescriptor` dropped

`SourceDescriptor` carried corpus facts — `source_language`, embedded-language declarations, structural unit declarations, source edition metadata. Under FP2, these are LLM-inferable from the source text itself; declaring them duplicates inference. The user's correction makes this explicit: *"translation happens regardless of the source language via LLMs."* SD becomes redundant once you accept that the LLM handles source-language detection at runtime.

This is the load-bearing application of FP2. It generates the simplification's biggest move (one fewer schema; one fewer class for the user to fill in).

#### Per-language `EmbeddedLanguage` replaced by `NonMainLangPartsPolicy`

The four-schema design carried `embedded_languages: list[EmbeddedLanguagePolicy]` on SD, with per-language declarations (`language_code="ar"`, `language_code="fa"`, etc.) and per-language handling policies. Under FP2:

- **Per-language declaration** is LLM-inferable. The LLM detects Arabic in Turkish prose without being told it's Arabic.
- **Per-language handling policy** is human-decidable (preserve / replace / annotate / use famous translation). Only this part needs to stay in schema.

The result: drop the per-language plumbing; keep only the handling policy. The handling policy is language-agnostic — same enum literals work for Arabic, Persian, Latin, Hebrew, Sanskrit. The output is a single `NonMainLangPartsPolicy` class with a 5-literal `policy` field.

This is FP2 applied at finer grain — the LLM-inferable test runs per sub-aspect of a candidate, not just per whole-class.

#### `chunking_granularity` moved off TC to PC

The `chunk_types_vs_mechanisms` finding placed `chunking_granularity: Literal[5]` on `TranslationConfig`, reasoning that granularity is a strategic choice the user makes. The current simplification moves it to `PipelineConfig`. The shift is generated by two principles:

- **C1 (TC frozen).** The user's explicit constraint — *"translation_config is good as it is"* — makes TC unmodifiable. Adding `chunking_granularity` to TC violates this. (This is a constraint, not FP2 directly.)
- **Architectural reclassification.** Re-read at the layer-level: chunking granularity is operational (the AI pipeline tunes it per job to fit context budgets and corpus structure), not strategic (the user doesn't typically pick sentence vs paragraph chunking as a translation-strategy choice). It belongs to PC's "runtime engine knobs" category.

These two principles compose. The 5-literal value set (`sentence` / `paragraph` / `passage` / `subchapter` / `chapter`) is preserved — only the schema home changes. (Note: this argument blends a TC-frozen application with a layer-classification application; both arguments lead to the same move, but they are distinct.)

#### `canonical_level` mapping dropped

The `chunk_types_vs_mechanisms` finding committed a `canonical_level` field on `SD.ChunkingUnit` mapping corpus-specific structural units (Söz, mesele, ayah, hashiye, etc.) to a universal 5-level hierarchy (chapter > subchapter > passage > paragraph > sentence). The current simplification drops this mapping. Two reasons:

- **SD is dropped** (no schema home).
- **The universal hierarchy is structurally wrong.** The user's correction is explicit: *"book must follow certain chapter rules. which is not the case."* Forcing every corpus into the 5-level ladder imposes structure that doesn't fit; the LLM infers corpus structure from text more flexibly than a fixed enum would.

The corpus mappings (Söz=chapter, mesele=subchapter, ayah=sentence with is_atomic=True, hashiye=paragraph attached_to="paragraph") remain useful as **documentation** of how the AI should think about each corpus, but they are not schema field values.

#### Before/after architecture contrast

| Aspect | Before (4-schema design) | After (3-layer schemas.py) |
|---|---|---|
| **Schema count** | 4 schemas + helper classes (SD + ChunkingUnit + EmbeddedLanguageProfile + PC + TC) | 3 layers (TC + Policy classes + PC) |
| **Who handles what** | Mixed: SD held both LLM-inferable facts (source_language) and human-decidable handling (embedded_languages policies) | Clean: each layer holds one kind of fact (LLM inference / user value judgment / operator knob) |
| **Language-coupling** | EmbeddedLanguage had per-language declarations (`language_code`) + Arabic-named policy values | Policy enum values are language/tradition-agnostic; corpus-specific choices live in the user's per-job instance, not in schema values |
| **Hierarchy assumption** | canonical_level imposed 5-level ladder on all corpora | No imposed hierarchy; AI infers structure from text |
| **TC delta** | +1 axis (chunking_granularity) | 0 axes (TC frozen unchanged) |

The "after" column is what `schemas.py` reflects today.

### 4. Item 2 — Policy-shaped scenarios catalog

The four filters for catalog membership:

1. **Structural shape.** Single-field `BaseModel` with a `Literal[N]` enum.
2. **Language-agnosticism.** Enum literals never name a specific language, tradition, or corpus.
3. **Authorial edge-case.** The phenomenon is something the author did (not translator-side, publication-side, or reader-side).
4. **LLM-can't-infer.** The handling decision is a human value judgment, not an inference (the LLM can detect the phenomenon but cannot decide preservation vs replacement vs annotation).

Each candidate below has been tested against all four filters.

#### Strong candidates (6) — all four filters pass with HIGH confidence

These are the immediate adoption targets. Each has a pydantic sketch ready for `schemas.py`.

**1. `SourceApparatusPolicy`** — how to handle the source's pre-existing apparatus (the author's marginal annotations or glosses). Nursi's *hashiye* are the canonical Nursi example; the Talmud's marginal commentary tradition and critical-edition apparatus criticus are analogous in other corpora.

```python
class SourceApparatusPolicy(BaseModel):
    """How to handle the source's pre-existing apparatus (author's marginal
    annotations, glosses). Edge case: Said Nursi's hashiye; Talmud's
    marginal commentary; critical-edition apparatus criticus."""
    policy: Literal[
        "drop",
        "translate-inline-bracketed",
        "translate-as-footnote",
        "preserve-as-source-channel",
    ] = "translate-as-footnote"
```

**Per-value worked examples.**

- **`drop`** — discard the author's marginalia entirely.
  - *Said Nursi anchor.* A casual paperback edition of Risale-i Nur omits the hashiye and presents only Nursi's main text.
  - *Cross-cultural example.* A trade-paperback edition of a classical text that strips critical apparatus; popular Penguin editions of biblical books without footnotes.

- **`translate-inline-bracketed`** — render marginalia inline in the target with bracket markers.
  - *Said Nursi anchor.* Hashiye inserted into the translation flow as bracketed asides: *"...[Hashiye: this point applies also to the situation of the believer in adversity]..."*
  - *Cross-cultural example.* Penguin Classics with translator-inserted bracketed glosses; some Quran translations that bracket explanatory expansions inside the verse.

- **`translate-as-footnote`** — render marginalia as target-language footnotes. The default.
  - *Said Nursi anchor.* The hashiye become numbered footnotes in the English edition, preserving the author's voice as a distinct annotation layer without interrupting the main text.
  - *Cross-cultural example.* Norton Critical Edition style; scholarly editions of biblical commentaries; M.A.S. Abdel Haleem's Quran translation with footnoted explanations.

- **`preserve-as-source-channel`** — preserve marginalia as a structurally distinct channel (sidebar, parallel column, distinct font).
  - *Said Nursi anchor.* The hashiye appear in a sidebar or smaller font running parallel to Nursi's main text, mirroring the source's manuscript layout.
  - *Cross-cultural example.* Talmud Bavli editions where main text and commentaries occupy distinct columns; sacred-text editions with patristic commentary in parallel apparatus.

**2. `VoiceMarkingPolicy`** — how to mark transitions between author voice and cited authorities (Quran, hadith, kalam authors) or student-voice additions (lahika letters). Same shape applies to rabbinic source-stacks with named attribution chains.

```python
class VoiceMarkingPolicy(BaseModel):
    """How to mark transitions between author voice and cited authorities
    or student-voice additions."""
    policy: Literal[
        "off",
        "as-in-original",
        "implicit-typographic",
        "explicit-attribution-inline",
        "scholarly-apparatus-marking",
    ] = "as-in-original"
```

**Per-value worked examples.**

- **`off`** — no marking. Author voice and citations blend into one flat narrative surface.
  - *Said Nursi anchor.* The English translation flows continuously without typographic, attributional, or apparatus marking — a reader encounters Quran citations, hadith, and Nursi's own prose at the same surface level.
  - *Cross-cultural example.* Vernacular translations targeting narrative flow where voice attribution would feel academic; popular religious paraphrases.

- **`as-in-original`** — preserve the source's own voice-marking conventions in the target. The default.
  - *Said Nursi anchor.* Nursi uses Arabic script for ayahs and Latin script for his Turkish prose; the English target mirrors this visual contrast (Arabic-script ayahs preserved; hashiye indented as Nursi indented them).
  - *Cross-cultural example.* Tanakh translations that preserve the source's typographic distinction between narrative and poetry sections; red-letter Bibles that mark Jesus's speech as the source typeset it.

- **`implicit-typographic`** — translator applies typographic conventions to mark voice transitions (italics for citations, indented blocks for marginalia, distinct fonts for embedded language).
  - *Said Nursi anchor.* Quranic citations rendered in italic; hashiye indented and set in smaller type; Persian Mevlana couplets in a serif italic distinct from main type — typographic conventions chosen by the translator regardless of how Nursi marked them.
  - *Cross-cultural example.* Standard scholarly editions of cross-tradition theological texts; academic biblical commentaries; Oxford World's Classics.

- **`explicit-attribution-inline`** — translator inserts explicit "as X says" attributions at voice transitions.
  - *Said Nursi anchor.* *"As the Quran says in Sūrah 36:53..."* precedes each ayah; *"Said Nursi here notes in the margin..."* precedes each hashiye.
  - *Cross-cultural example.* Critical editions with named-source inline attribution; teaching editions where every source-shift is explicitly tagged for the reader.

- **`scholarly-apparatus-marking`** — full apparatus with footnotes, sidebar attributions, source-marker sigla.
  - *Said Nursi anchor.* Every voice transition produces an apparatus criticus entry; the reader sees footnoted citation references, sigla for hashiye-vs-main-text, and bibliographic anchors for each cited authority.
  - *Cross-cultural example.* Norton Critical Editions; SBL Greek New Testament critical editions; Loeb Classical Library scholarly apparatus.

The first four values lie on a spectrum from least to most visible marking (`off` → `as-in-original` → `implicit-typographic` → `explicit-attribution-inline`); `scholarly-apparatus-marking` is the maximum end. `as-in-original` is the source-preserving baseline that aligns this Policy with the other strong candidates' default-preserve pattern (compare `NonMainLangPartsPolicy.preserve-original`; `HonorificsPolicy.preserve-original-script`; `SourceApparatusPolicy.preserve-as-source-channel`).

**3. `ArchaicRegisterPolicy`** — how to render archaic source language in the target translation.

**The edge case.** An author wrote in a register that has aged. Their vocabulary, syntax, and idioms were contemporary at authorship but feel old to current readers. When the translator renders this in the target language, they have to decide what to do with that age.

Nursi wrote in 1920s-30s Turkish that carries significant Ottoman-Turkish residue, especially in theological passages. A modern Turkish reader finds his vocabulary and sentence structures old-fashioned. When translating to English, the translator chooses: should the English also sound archaic (*"Verily, behold ye who believeth..."*), should it be fully modernized (*"Truly, look — those who believe..."*), should it be hybrid (theological vocabulary keeps an archaic feel; narrative prose is modern), or should it be modernized but with explicit archaism-flags (translator notes that mark "the source used an old word here")?

The same choice applies to translating Early Modern English (Shakespeare-era texts), Classical Arabic embedded in modern theological writing, Sanskrit in modern Indian-language texts, or any other corpus where the source's language has aged.

**Per-value worked examples.**

- **`preserve-archaic-throughout`** — keep the archaic register fully in the target.
  - *Said Nursi anchor.* Nursi's Ottoman-Turkish theological prose rendered in archaic English throughout: *"Verily, behold the believer who upon the path of certainty doth walk, who unto the divine names with assurance turneth..."*
  - *Cross-cultural example.* KJV Bible style for Hebrew/Aramaic source; Hakluyt Society editions of historical travel writing preserving period diction; Loeb's older English translations of Greek philosophy.
  - *Suits.* Scholarly editions and historicizing translations where the period feel is part of the meaning.

- **`modernize-fully`** — render everything in contemporary target language.
  - *Said Nursi anchor.* The same passage in fully modern English: *"Truly, look at how the believer walks the path of certainty, turning with assurance to the divine names..."*
  - *Cross-cultural example.* The Message paraphrase of the Bible; modern colloquial editions of Plato (Robin Waterfield translations); contemporary popular Sufi-poetry renderings (Coleman Barks–style Rumi).
  - *Suits.* Accessibility-first translations for general readers. Carries some no-smoothing-policy risk (smoothing of archaic forms violates faithful-rendering preservation).

- **`hybrid-by-register-domain`** — preserve archaic feel where it carries semantic weight; modernize where archaic English would be needlessly ornate. The default.
  - *Said Nursi anchor.* Theological vocabulary (*iman, takvim, marifet*) keeps its weight in transliteration or archaic-register equivalent; Nursi's narrative analogies render in modern English without *"thee/thou."* Result: *"The believer (sahib-i iman) walks with certainty along the path, turning to the divine names with the assurance that comes from knowing them."*
  - *Cross-cultural example.* Penguin Classics of Plato — philosophical terminology preserved (eudaimonia, logos); narrative prose modernized. NRSV Bible style. Norton Critical editions that preserve period theological vocabulary while modernizing narrative.
  - *Suits.* The most general case — composes positively with the Layer-2 register-alternation preservation policy.

- **`mark-archaisms-explicitly`** — use modern target language throughout but mark places where the source was archaic.
  - *Said Nursi anchor.* Modern English throughout; Ottoman-Turkish theological vocabulary appears in italic + footnote: *"the believer's *iman*¹..."* with footnote glossing the term and noting its archaic-but-precise sense.
  - *Cross-cultural example.* Language-learning editions; ALA-LC scholarly editions where archaisms are explicitly typographically marked; pedagogical critical editions for students.
  - *Suits.* Language-learning purposes and study-editions where the reader is expected to engage the archaism as data, not as register-feel.

```python
class ArchaicRegisterPolicy(BaseModel):
    """How to render archaic source-language register in the target translation."""
    policy: Literal[
        "preserve-archaic-throughout",
        "modernize-fully",
        "hybrid-by-register-domain",
        "mark-archaisms-explicitly",
    ] = "hybrid-by-register-domain"
```

**Inheritance note.** This class carries the `source_temporal_register` field originally proposed in the edge_cases finding (which routed it to the now-dropped `SourceDescriptor`). The field's semantics survived the SD drop by re-homing as a Policy class — this is the one concrete homeless residual the new architecture absorbs.

**4. `HonorificsPolicy`** — how to render theological honorifics that follow names. The Islamic *SAW / AS / RA / PBUH* family, the Jewish *ZT"L / RA / OBM* family, and analogous conventions in other traditions all share the same handling-decision structure. The enum literals are language-agnostic — *"preserve-original-script"* works for any source script, not just Arabic.

```python
class HonorificsPolicy(BaseModel):
    """How to render theological honorifics that follow names."""
    policy: Literal[
        "preserve-original-script",
        "transliterate-with-original",
        "translate-meaning",
        "abbreviate-translated",
        "drop",
    ] = "transliterate-with-original"
```

**Per-value worked examples.**

- **`preserve-original-script`** — keep the honorific in its original script.
  - *Said Nursi anchor.* *"Resul-i Ekrem ﷺ buyurmuştur"* preserved with the Arabic ﷺ glyph after the Prophet's name; *"Hazret-i Ali (kerremallâhu vechehû)"* preserves the parenthesized Arabic honorific.
  - *Cross-cultural example.* Hebrew Bible editions preserving ז״ל / זצ״ל after rabbinic names; Sanskrit editions preserving devanagari śrī before names; East-Asian Buddhist editions preserving 仏 (bul/butsu) glyphs.
  - *Suits.* Editions for source-culture-fluent readers; in-tradition devotional texts.

- **`transliterate-with-original`** — transliterate the honorific in Latin script alongside the original. The default.
  - *Said Nursi anchor.* *"The Prophet (sallallāhu ʿalayhi wa-sallam ﷺ)"* rendered with both Romanized transliteration and the original glyph.
  - *Cross-cultural example.* Encyclopedia of Islam style; scholarly Hindu studies editions that pair devanagari with transliterated honorifics; SBL biblical editions that show Hebrew + transliteration for proper-noun honorifics.
  - *Suits.* Scholarly editions; bilingual study editions; readers comfortable with both scripts.

- **`translate-meaning`** — render the honorific's meaning fully in the target language.
  - *Said Nursi anchor.* *"The Prophet, peace and blessings be upon him"* — the full English meaning rendered after each Prophet reference.
  - *Cross-cultural example.* Most popular Islamic-history books for general audiences; Tarif Khalidi Quran translation style; popular Hindu texts that translate *śrī* as "blessed" or "revered."
  - *Suits.* General-reader editions; introductory non-academic texts; translations targeting readers without source-tradition fluency.

- **`abbreviate-translated`** — use the established target-language abbreviation.
  - *Said Nursi anchor.* *"The Prophet (PBUH)"* — using the conventional English abbreviation.
  - *Cross-cultural example.* Mass-market Islamic-studies books; Western journalism on Islam; popular interfaith dialogue publications.
  - *Suits.* Texts where compactness matters and readers recognize the abbreviation; popular religious-studies books.

- **`drop`** — omit the honorific entirely.
  - *Said Nursi anchor.* *"The Prophet said..."* — no honorific marking. Suits academic prose where editorial style mandates omission.
  - *Cross-cultural example.* Academic religious-studies monographs; Encyclopedia Britannica articles; secular comparative-religion textbooks.
  - *Suits.* Academic neutral-voice editions; comparative-religion scholarship where preserving honorifics would imply confessional commitment.

**5. `FormulaicOpeningPolicy`** — how to render formulaic openings. The Islamic Bismillah, the Jewish Shema, Christian invocations, Vedic mantras, and similar dedicatory formulae all fit the same handling pattern.

```python
class FormulaicOpeningPolicy(BaseModel):
    """How to render formulaic openings (invocations, basmala, dedicatory
    formulae)."""
    policy: Literal[
        "preserve-original-with-translation",
        "transliterate-with-translation",
        "translate-only",
        "preserve-original-untranslated",
    ] = "preserve-original-with-translation"
```

**Per-value worked examples.**

- **`preserve-original-with-translation`** — keep the original formula plus translation. The default.
  - *Said Nursi anchor.* *"بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ — In the name of Allah, the Most Compassionate, the Most Merciful"* opens each major section, with both the Arabic glyph block and the English meaning.
  - *Cross-cultural example.* Tanakh editions that preserve Hebrew *Shema Yisrael* with English translation; Sanskrit editions preserving devanagari mantras with translation; Catholic missals preserving Latin formulae with vernacular.
  - *Suits.* General-purpose translations that respect liturgical/devotional weight while remaining accessible.

- **`transliterate-with-translation`** — transliterate in Latin script + translation.
  - *Said Nursi anchor.* *"Bismillāhi r-raḥmāni r-raḥīm — In the name of Allah, the Most Compassionate, the Most Merciful"*
  - *Cross-cultural example.* Academic editions of liturgical texts; scholarly Vedic editions transliterating mantras; Reform Jewish prayer books pairing transliterated Hebrew with English.
  - *Suits.* Scholarly editions where source-script reproduction is impractical; readers comfortable with transliteration but without source-script.

- **`translate-only`** — render only the meaning in target language.
  - *Said Nursi anchor.* *"In the name of Allah, the Most Compassionate, the Most Merciful"* — without the Arabic glyphs or transliteration.
  - *Cross-cultural example.* Popular English-language editions of religious texts targeting non-specialist readers; trade-paperback editions of Sufi poetry.
  - *Suits.* Accessibility-first translations; readers without source-tradition familiarity.

- **`preserve-original-untranslated`** — preserve the original formula with no translation.
  - *Said Nursi anchor.* *"بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"* preserved as-is, untranslated, on the assumption that the reader recognizes the basmala by sight.
  - *Cross-cultural example.* Editions targeting religiously-fluent readers; in-tradition prayer books; Hebrew prayer-book reprints assuming Shema-recognition.
  - *Suits.* In-tradition devotional editions; readers for whom the formula's recognition IS the rendering.

**6. `EmbeddedPoetryPolicy`** — how to render embedded poetry, distinct from prose embedded language. Mevlana couplets embedded in Nursi's prose; Tanakh psalms in prose-Bible commentary; Sanskrit slokas in Hindu prose all need different render decisions (verse vs prose vs facing-original) than what `NonMainLangPartsPolicy` provides for prose quotes.

```python
class EmbeddedPoetryPolicy(BaseModel):
    """How to render embedded poetry, distinct from prose embedded language
    (which NonMainLangPartsPolicy governs)."""
    policy: Literal[
        "preserve-original-with-prose-gloss",
        "translate-as-verse",
        "translate-as-prose",
        "facing-original-with-meter-notes",
    ] = "preserve-original-with-prose-gloss"
```

**Per-value worked examples.**

- **`preserve-original-with-prose-gloss`** — preserve the original poetry; follow with a prose gloss in the target. The default.
  - *Said Nursi anchor.* A Mevlana couplet preserved in Persian script, followed by an English prose paragraph explaining its meaning and how Nursi uses it: *"بشنو از نی چون حکایت می‌کند / از جدایی‌ها شکایت می‌کند — Listen to the reed as it tells its tale, complaining of separations. Nursi here invokes Mevlana's opening to anchor his point that..."*
  - *Cross-cultural example.* Loeb Classical Library editions where Greek verse appears with English prose translation on the facing page; scholarly editions of Hebrew poetry in biblical commentaries; academic editions of Sanskrit ślokas with prose gloss.
  - *Suits.* The most faithful default — preserves poetic identity while ensuring meaning transmits.

- **`translate-as-verse`** — render the embedded poetry as poetry in the target.
  - *Said Nursi anchor.* Mevlana couplets rendered in English rhymed verse (or English free verse approximating the couplet structure): *"Listen as the reed laments / its tale of distance and lament."*
  - *Cross-cultural example.* Coleman Barks's Rumi translations; Robert Alter's poetic translations of the Hebrew Bible; A.K. Ramanujan's poetic translations of South Indian devotional verse.
  - *Suits.* Editions targeting readers for whom verse-form recognition is part of the experience; literary translations.

- **`translate-as-prose`** — render embedded poetry as prose in the target.
  - *Said Nursi anchor.* A Mevlana couplet rendered as a paragraph of English prose, integrating into Nursi's surrounding text without verse markup: *"Listen to the reed as it tells of separations and complains."*
  - *Cross-cultural example.* Penguin Classics editions that prose-translate verse for accessibility; trade-paperback translations of Iranian classical poetry; popular-edition Bible Psalms in prose paragraphs.
  - *Suits.* Accessibility-first translations; reader unfamiliar with verse conventions; texts where the verse is illustrative not load-bearing.

- **`facing-original-with-meter-notes`** — preserve original verse with target verse on facing page, with metrical notes.
  - *Said Nursi anchor.* A bilingual edition with the Persian couplet on the verso and an English verse equivalent on the recto, plus a footnote on the original meter (*"hazaj-i muthamman maḥdhūf"*) and how the English approximates it.
  - *Cross-cultural example.* Loeb Classical Library; bilingual editions of Pushkin; scholarly editions of Hafez; Penguin parallel-text editions of Dante.
  - *Suits.* Scholarly editions; readers studying the poetic form itself; comparative-literature editions.

#### Co-application note

**Policy classes co-apply per text span.** A Bismillah is BOTH a formulaic opening (governed by `FormulaicOpeningPolicy`) AND a non-main-language phrase (governed by `NonMainLangPartsPolicy`); both policies' values apply to their respective concerns without conflict. A Mevlana couplet is BOTH embedded poetry (governed by `EmbeddedPoetryPolicy`) AND a non-main-language phrase (governed by `NonMainLangPartsPolicy`); same independent co-application. The Policy classes do not compete; each governs its own concern. If practical translation work surfaces ambiguity from co-application, see Open Questions §Refinement Triggers.

#### Moderate candidates (4) — pass with filter caveats

**7. `TransliterationStandardPolicy`** — which transliteration convention to use when rendering source script in target script. Caveat: transliteration is partly translator-side (a render convention), not purely authorial.

```python
class TransliterationStandardPolicy(BaseModel):
    policy: Literal[
        "scholarly-standard",
        "popular-standard",
        "phonetic",
        "diacritic-stripped",
    ] = "scholarly-standard"
```

**Per-value worked examples.**

- **`scholarly-standard`** — full diacritics per academic convention (ALA-LC, DIN-31635, IAST).
  - *Said Nursi anchor.* Nursi rendered as *"Bedīʿuzzamān Saʿīd Nūrsī"*; Quranic terms with full Arabic diacritics (*"al-raḥmān al-raḥīm"*).
  - *Cross-cultural example.* Encyclopedia of Islam; scholarly journal articles; academic monographs; IAST-compliant Sanskrit transliteration in Hindu-studies scholarship.

- **`popular-standard`** — established public-facing transliteration without full diacritics.
  - *Said Nursi anchor.* *"Bediuzzaman Said Nursi"*; *"Quran"*; *"iman"* without diacritics.
  - *Cross-cultural example.* Trade-paperback editions; popular Islamic books; general-readership Hindu-studies works.

- **`phonetic`** — simplified-to-target-language phonetics for readability.
  - *Said Nursi anchor.* *"Bediyuzzaman Said Noorsee"* — closer to English pronunciation cues for readers without Turkish/Arabic exposure.
  - *Cross-cultural example.* Children's introductions to world religions; pronunciation-guide editions; popular media transliterations.

- **`diacritic-stripped`** — like scholarly but without diacritics; suits constrained typography.
  - *Said Nursi anchor.* *"Bediuzzaman Said Nursi"* rendered without ī / ʿ marks.
  - *Cross-cultural example.* Web editions where typography doesn't support diacritics; ASCII-only databases; SMS-era theological discussion forums.

**8. `PriorTranslationStancePolicy`** — stance toward established prior translations of the same corpus (Şükran Vahide; Hüseyin Akarsu for Nursi; KJV vs NIV for Bible). Caveat: a `list[PriorRef]` companion structure would live separately — this Policy class only carries the *stance* choice.

```python
class PriorTranslationStancePolicy(BaseModel):
    stance: Literal[
        "independent",
        "honor-terminology",
        "extend-with-revisions",
        "explicit-divergence-noted",
        "collate-and-cite",
    ] = "independent"
```

**Per-value worked examples.**

- **`independent`** — translate from scratch; treat priors as background reference only.
  - *Said Nursi anchor.* New Risale-i Nur translation that does not consult Şükran Vahide or Hüseyin Akarsu during drafting; renders each passage on its own structural reading.
  - *Cross-cultural example.* Robert Alter's Hebrew Bible — explicitly independent of King James and JPS; Stephen Mitchell's Bhagavad Gita translation independent of earlier scholarly editions.

- **`honor-terminology`** — preserve key terminology choices from accepted prior translations.
  - *Said Nursi anchor.* Translation that preserves Vahide's English rendering of Nursi's key terms (e.g., *haqiqat* → "reality"; *iman* → "faith") for consistency with established Nursi-readership.
  - *Cross-cultural example.* Newer NIV revisions preserving KJV-tradition terminology where possible (*"believer"* over alternatives); ESV's deference to RSV terminology choices.

- **`extend-with-revisions`** — build on a prior translation, revising where new scholarship demands.
  - *Said Nursi anchor.* A revised edition of Vahide that updates specific passages where Vahide's choices have been superseded by subsequent scholarly work on Nursi.
  - *Cross-cultural example.* NRSV's relationship to RSV; New JPS's relationship to the original JPS Tanakh.

- **`explicit-divergence-noted`** — translate independently but explicitly flag divergence from established priors.
  - *Said Nursi anchor.* New translation that footnotes each significant divergence from Vahide and Akarsu, explaining the chosen alternative.
  - *Cross-cultural example.* Robert Alter's Bible footnotes that note KJV / RSV divergences with reasoning; Coleman Barks's notes where he diverges from Nicholson's Rumi.

- **`collate-and-cite`** — present multiple prior renderings alongside the new translation as a scholarly collation.
  - *Said Nursi anchor.* Critical edition presenting Vahide's, Akarsu's, and the new translator's renderings side-by-side for key passages.
  - *Cross-cultural example.* Variorum editions of Shakespeare; scholarly collated editions of the Apostolic Fathers; the New English Translation of the Septuagint's parallel-version apparatus.

**9. `AnachronismHandlingPolicy`** — handling source content that was contemporary at authorship but is anachronistic for current readers (Nursi's kalam terms once-familiar-now-obscure; place-names since changed). Caveat: overlaps with `ArchaicRegisterPolicy` at the boundary (when does archaism become anachronism?).

```python
class AnachronismHandlingPolicy(BaseModel):
    policy: Literal[
        "preserve-with-footnote",
        "inline-gloss",
        "modernize-equivalent",
        "drop-and-replace-current",
    ] = "inline-gloss"
```

**Per-value worked examples.**

**What "anachronism" means here.** A reference that was current when the author wrote but no longer exists or no longer means what it meant — institutions, political offices, administrative units, scientific frameworks, currency, military formations, religious-institutional positions. Distinct from archaic *language* (handled by `ArchaicRegisterPolicy`); this is about archaic *referents*. Nursi's text contains many: references to the **Şeyhülislam** (Ottoman state's highest Islamic religious authority, abolished 1924); the **Darü'l-Hikmet'il-İslamiye** (Ottoman House of Islamic Wisdom where Nursi taught, dissolved with the caliphate); specific Ottoman **vilayet** (province) names and boundaries that have since changed; **altın lira** (gold-backed Ottoman currency) sums; specific Eastern Front WWI engagements he participated in.

- **`preserve-with-footnote`** — keep the anachronism in the target; footnote it for modern readers.
  - *Said Nursi anchor.* *"Şeyhülislam"* preserved in transliteration; footnote explains it was the highest Islamic religious authority of the Ottoman state, with administrative + scholarly functions, until the office was abolished in 1924 as part of the secularization reforms.
  - *Cross-cultural example.* Penguin Classics of Renaissance texts that preserve period institutional terms ("Privy Council," "Star Chamber") with explanatory footnotes; scholarly editions of Augustine that preserve "comes Africae" with footnote on the late-Roman provincial office.

- **`inline-gloss`** — preserve the anachronism with a brief in-text gloss. The default.
  - *Said Nursi anchor.* *"...the Şeyhülislam (the Ottoman state's highest Islamic religious authority, an office since abolished)..."* — inline rather than footnoted.
  - *Cross-cultural example.* Trade-paperback historical novels that inline-gloss period offices ("the bailiff, a royal judicial officer"); popular biblical translations that inline-gloss obsolete weights and measures ("a shekel of silver, worth about four days' wages").

- **`modernize-equivalent`** — substitute a current-equivalent term.
  - *Said Nursi anchor.* *"Şeyhülislam"* rendered as *"the Grand Mufti"* or *"the chief religious authority"* without further note. Risk: the analogy's force may shift (the Şeyhülislam was a *state* office with administrative power, not a purely advisory religious authority — modernization loses that).
  - *Cross-cultural example.* Mass-market modernized translations that render "centurion" as "captain"; popular Augustine paraphrases that render Roman provincial titles as modern administrative equivalents.

- **`drop-and-replace-current`** — drop the historical reference; replace with a current-day equivalent or generic descriptor.
  - *Said Nursi anchor.* References to *"Darü'l-Hikmet'il-İslamiye"* replaced with *"a contemporary Islamic scholarly institution"* — the specific historical institution is dropped; the function it served is generalized. Highest information loss; suits very accessibility-focused editions.
  - *Cross-cultural example.* The Message paraphrase of biblical political references with contemporary US-political equivalents; popular paraphrases of Augustine that replace Roman-era civic allusions with modern-Western ones.

**10. `CitationReferenceFormatPolicy`** — how to render cross-reference notation (sura:ayah; book:ch:v; canto:line). Caveat: use-case is narrow (only matters for corpora with formal citation conventions).

```python
class CitationReferenceFormatPolicy(BaseModel):
    policy: Literal[
        "preserve-source-format",
        "standardize-canonical",
        "both-with-cross-reference",
        "footnoted-only",
    ] = "preserve-source-format"
```

**Per-value worked examples.**

- **`preserve-source-format`** — keep the source's own citation format. The default.
  - *Said Nursi anchor.* Quranic citations preserved as Nursi wrote them — *"Yâsîn sûresi, 53. âyet"* renders as *"Yāsīn Surah, 53rd verse"* mirroring his format.
  - *Cross-cultural example.* Talmud editions preserving folio:line reference notation (Berakhot 2a:7); Sanskrit editions preserving canto:śloka notation (Bhagavad Gītā 2:47).

- **`standardize-canonical`** — convert source citations to the standardized format of the target tradition.
  - *Said Nursi anchor.* Quranic citations rendered in standardized sura:ayah format (e.g., *"Quran 36:53"*) regardless of how Nursi formatted them.
  - *Cross-cultural example.* Standard SBL citation format for biblical references in academic publications (*"Gen 1:1"*); IAST-citation-format conversion for Sanskrit references.

- **`both-with-cross-reference`** — provide both source format and standardized format.
  - *Said Nursi anchor.* *"Yâsîn 53 (Quran 36:53)"* rendered with both Nursi's source citation and the standardized format.
  - *Cross-cultural example.* Bilingual scholarly editions providing both source-original and target-standard citation forms; cross-tradition comparative editions.

- **`footnoted-only`** — render citations as footnote references rather than inline.
  - *Said Nursi anchor.* Inline references become superscript footnote numbers (¹); the actual citation appears in footnotes (*"¹ Yāsīn 53 / Quran 36:53"*).
  - *Cross-cultural example.* Academic monographs that footnote all biblical / Quranic citations rather than inline-citing; literary editions where main-text inline citations would clutter.

#### Deferred / out-of-shape (5)

Each has an explicit revival trigger.

- **`ScriptDirectionPolicy`** (edge-case #14). Surface rendering (bidi RTL embedded in LTR), not authorial. Revival trigger: when output rendering reaches the bidirectional-display stage.
- **`PassageTypologyPolicy`** (edge-case #7). Typology label per chunk, not handling strategy. Revival trigger: if a per-chunk typology mechanism is committed.
- **Consumption-mode / reading-session policies** (edge-cases #9 + #10). Reader-side, not authorial. Revival trigger: when reader-side context becomes load-bearing for translation choices beyond TC.A4.
- **`OutputFinalityPolicy`** (edge-case #12). Pipeline-side / output-status, not authorial. Revival trigger: when downstream pipeline distinguishes finality levels (draft / final / teaching).
- **`RelayTranslationPolicy`** (edge-case #5). Carries `relay_chain: list[LanguageHop]` structure that breaks the pure single-field shape. Revival trigger: when a relay-translation use case becomes active (Comprehenslate's current scope is direct Turkish→English).

### 5. The schemas.py current shape

For reference, the current `schemas.py` is:

```python
from typing import Literal
from pydantic import BaseModel


class TranslationConfig(BaseModel):
    """User-facing translation strategy."""
    reader_level:      Literal["very_basic", "daily", "conversational", "advanced", "native"]            = "conversational"
    domain_expertise:  Literal["lay", "aware", "educated", "trained", "expert"]                          = "aware"
    source_culture:    Literal["outsider", "acquainted", "familiar", "heritage", "source-native"]        = "acquainted"
    purpose:           Literal["scholarly", "devotional", "casual", "language-learning", "performance"]  = "casual"
    source_fidelity:   Literal["foreignized-max", "foreignized", "balanced", "lightly-domesticated"]     = "balanced"
    form_preservation: Literal["off", "minimal", "light", "standard", "maximum"]                         = "standard"
    scaffolding:       Literal["off", "minimal", "standard", "rich", "scholarly"]                        = "minimal"
    analysis_depth:    Literal["none", "surface", "standard", "deep", "scholarly"]                       = "none"


class NonMainLangPartsPolicy(BaseModel):
    """Policy for quotes, mentions, and references in a non-main language."""
    policy: Literal[
        "preserve-original",
        "preserve-original-and-add-translation-as-a-note",
        "replace-original-with-translation",
        "replace-original-with-translation-add-original-as-a-note",
        "replace-original-with-infamous-translation",
    ] = "preserve-original-and-add-translation-as-a-note"


class PipelineConfig(BaseModel):
    """Runtime engine knobs. Not user-facing translation strategy."""
    chunking_budget: int | None = None
    chunking_granularity: Literal[
        "sentence", "paragraph", "passage", "subchapter", "chapter"
    ] | None = None
    chunking_mechanism_override: Literal[
        "structural", "harmony-tier-aware", "passage-typology-aware",
        "llm-detected", "fixed-budget-with-snap", "hybrid",
    ] | None = None
```

If the 6 strong candidates from §4 are adopted, the Policy layer grows from 1 to 7 classes alongside TC and PC.

---

## Inherited Commitments Re-test

The Synthesis Trigger in `_branch.md` named four substrates (the current `schemas.py` plus 3 prior findings). Each prior finding's load-bearing commitments are re-tested below.

### From `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md`

| Commitment | Re-test status | Evidence |
|---|---|---|
| `chunking_granularity: Literal[5]` on `TranslationConfig` | **RE-TESTED — commitment found INVALID** | Structural contradiction: chunking granularity is operational (PC layer), not strategic (TC layer). User moved it to PC explicitly. C1 (TC-frozen) plus architectural reclassification under FP2 both reject the TC placement. |
| `SourceDescriptor.ChunkingUnit.canonical_level` field | **RE-TESTED — commitment found INVALID** | Imposes universal 5-level hierarchy not present in all corpora. User's correction: *"book must follow certain chapter rules. which is not the case."* SD itself is dropped. |
| Corpus mappings (Söz=chapter, mesele=subchapter, ayah=sentence with is_atomic, hashiye=paragraph attached_to) | **RE-TESTED — commitment found INVALID at schema location** | Useful as documentation of how the AI should think about each corpus, but not as schema field values. SD dropped. |
| The 5-literal `chunking_granularity` value set (sentence / paragraph / passage / subchapter / chapter) | **RE-TESTED — commitment confirmed** | Values preserved on `PipelineConfig.chunking_granularity`. The enum content was sound; only the schema home was wrong. |
| The 6-literal `chunking_mechanism_override` set on PC | **RE-TESTED — commitment confirmed** | Preserved unchanged in `schemas.py`. |
| A6 cascade rejection (≥light forbids non-harmony-aware mechanism overrides) | **INHERITED-WITHOUT-RE-TEST** | Out of this inquiry's scope; chunking finding owns the cross-cutting cascade. |
| MC1 + MC2 maintenance-candidate promotion (LOOP_DIAGNOSE finding origin) | **INHERITED-WITHOUT-RE-TEST** | Out of scope; gate was a future branch-test on a non-chunking inquiry, not this one. |

### From `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`

| Commitment | Re-test status | Evidence |
|---|---|---|
| Split-placement principle (*"schema ownership matches data ownership"*) | **RE-TESTED — commitment confirmed but frame revised** | Principle preserved as FP1. Architecture refined from 3-schema (SD + PC + TC) to 3-LAYER (TC + Policy + PC). FP2 (*"Don't declare what the LLM can infer"*) refines what counts as "data the schema must own." The principle survives in its narrowed application. |
| Three-operation chunking category | **INHERITED-WITHOUT-RE-TEST** | Out of scope; chunking finding owns the category. |
| Hybrid harmony-aware as AI default chunking mechanism | **RE-TESTED — commitment confirmed** | Preserved as PC's hidden default behind `chunking_mechanism_override: None`. |
| Tier 1-2 preservation as HARD constraint | **INHERITED-WITHOUT-RE-TEST** | Out of scope; chunking finding owns the cross-cutting constraint. |
| A4-driven defaults pattern | **RE-TESTED — commitment confirmed** | TC.A4 still drives downstream defaults; pattern intact (and now applied to Policy-class default selection too). |
| `SourceDescriptor` as a paper schema with `source_chunking_units` field | **RE-TESTED — commitment found INVALID** | SD dropped per user. The `source_chunking_units` mechanism (declared corpus-natural units) rejected as "not logical" by user. |

### From `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md`

| Commitment | Re-test status | Evidence |
|---|---|---|
| `TranslationConfig` gains 0 new fields | **RE-TESTED — commitment confirmed** | TC remains frozen at 8 axes. |
| 4 SD additions: `source_language_fluency`, `source_edition`, `source_temporal_register`, `embedded_languages: list[EmbeddedLanguagePolicy]` | **RE-TESTED — commitment found INVALID at schema location** | SD dropped. Per-field sub-statuses below. |
| sub-status: `source_language_fluency` | **deferred** | Not load-bearing for current Nursi work; revival trigger in Open Questions. |
| sub-status: `source_edition` | **dropped** | LLM-irrelevant for translation operation. |
| sub-status: `source_temporal_register` | **re-homed as `ArchaicRegisterPolicy`** | Matches Policy shape; surfaced as strong candidate in §4. |
| sub-status: `embedded_languages: list[EmbeddedLanguagePolicy]` | **replaced by `NonMainLangPartsPolicy`** | Per-language plumbing replaced by single language-agnostic Policy. |
| `EmbeddedLanguagePolicy` 4-literal `transliteration_policy` + Arabic-named `quranic_citation_policy` | **RE-TESTED — commitment found INVALID** | Per-language declaration replaced; language-named values dropped per language-agnosticism filter (C6). |
| Edge-cases #1, #6, #7 already-routed via `ChunkingUnit` | **RE-TESTED — commitment found INVALID at routing** | ChunkingUnit dropped with SD. New routings: #1 → `NonMainLangPartsPolicy`; #6 → `SourceApparatusPolicy` candidate (§4); #7 deferred (not policy-shaped). |
| Cross-axis conflict check (0 hard conflicts) | **RE-TESTED — commitment confirmed for surviving routes** | The surviving Policy candidates re-pass the conflict-check pattern. |
| A3 `source_culture` stays as-is (non-modification) | **RE-TESTED — commitment confirmed** | TC unchanged. |
| UseContext as schema deferred | **RE-TESTED — commitment confirmed** | Still deferred; aligns with anti-bloat. |

---

## Next Actions

### MUST

- **What:** Insert a Correction Notice at the top of `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md`. The notice text: *"**Correction (2026-06-15):** This finding's central schema-shape commitments — `chunking_granularity` on TC; SD.ChunkingUnit `canonical_level` field; corpus mappings as schema content — are corrected by `devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/finding.md` per the FP2 principle ('Don't declare what the LLM can infer'). The 5 literal granularity values plus the chunking_mechanism_override 6-literal set are preserved on PipelineConfig. The corpus mappings remain useful as documentation but not as schema field values."*
  - **Who:** the runner of any subsequent inquiry that touches chunking or schemas.
  - **Gate:** observable — when next chunking-related or schemas-related inquiry begins.
  - **Why:** prevents the corrected commitments from being silently inherited by future work.

- **What:** Insert a Correction Notice at the top of `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`. The notice text: *"**Correction (2026-06-15):** `SourceDescriptor`'s paper-schema commitment is INVALID per `devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/finding.md`. The split-placement principle is preserved but the architecture is 3-LAYER (TC + Policy classes + PC), not 3-schema (SD + PC + TC). FP2 ('Don't declare what the LLM can infer') refines what counts as schema-owned data."*
  - **Who:** same as above.
  - **Gate:** observable — when next chunking-related inquiry begins.
  - **Why:** preserves the split-placement principle visibility while flagging the SD INVALIDation.

- **What:** Insert a Correction Notice at the top of `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md`. The notice text: *"**Correction (2026-06-15):** The 4 `SourceDescriptor` additions are INVALID at schema location per `devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/finding.md`. Per-field: `source_language_fluency` deferred; `source_edition` dropped; `source_temporal_register` re-homed as `ArchaicRegisterPolicy`; `embedded_languages` replaced by language-agnostic `NonMainLangPartsPolicy`. Edge-cases #1, #6, #7 routings via ChunkingUnit are INVALID; new routings: #1 → NonMainLangPartsPolicy; #6 → SourceApparatusPolicy candidate; #7 deferred."*
  - **Who:** same as above.
  - **Gate:** observable — when next inquiry references the 14 edge-case routings.
  - **Why:** prevents the invalid SD routings from being silently inherited.

- **What:** Adopt the strong Policy candidates from §4 into `schemas.py` after user review.
  - **Who:** user / developer.
  - **Gate:** condition-bound — when the user deliberates which strong candidates to adopt now (decision is per-candidate based on whether the edge-case is active for current translation work).
  - **Why:** `schemas.py` currently has only `NonMainLangPartsPolicy`; the 6 strong candidates are load-bearing for active Nursi-corpus work (especially `SourceApparatusPolicy` for hashiye and `ArchaicRegisterPolicy` for Ottoman-Turkish residue).

### COULD

- **What:** Document the FP2 LLM-inferable test predicate as a module-level docstring or developer-facing comment in `schemas.py`.
  - **Who:** developer.
  - **Gate:** condition-bound — when next schema field is being considered.
  - **Why:** in-code documentation makes the principle visible to future contributors and prevents schema additions that violate it.

- **What:** Promote FP2 to a project-wide schema-style convention with a brief style guide document.
  - **Who:** project maintainer.
  - **Gate:** condition-bound — when project-wide schema-style guide is written or when 3+ inquiries reference FP2 as load-bearing.
  - **Why:** AE1 assembly emergent — FP2 generalizes beyond schemas.py to any AI-assisted system's schema design.
  - **Depends-on:** MUST item *"Adopt the strong Policy candidates"*. This COULD is GATED — do not act until the MUST resolves (because the project-wide convention is best documented after the schema layer has its initial Policy adoption pattern stabilized). OVERRIDE not warranted at this time.

### DEFERRED

- **What:** Revive `source_language_fluency` field placement decision.
  - **Gate:** observable — if A3 `source_culture` produces ambiguous assignments due to language-fluency conflation in actual translation work.
  - **Why if revived:** add as a `Literal[N]` enum on a new `ReaderFluencyPolicy` class, or revisit TC modification, depending on how the ambiguity surfaces.

- **What:** Branch-test MC1 (Candidate-Self-Consistency sub-axis) + MC2 (Comparative-Pattern Test perspective) on a non-chunking-related inquiry.
  - **Gate:** observable — next inquiry not related to chunking.
  - **Why if revived:** evidence accumulation for promoting MC1 and MC2 to canonical td-critique and sense-making sub-axes per the chunk_types_vs_mechanisms finding's promotion strategy.

- **What:** Extend the Policy catalog to non-Islamic theological-translation corpora (Tanakh; Bible; Sanskrit-Hindu; Pali Buddhist; Christian patristic).
  - **Gate:** condition-bound — when Comprehenslate scope expands to non-Islamic corpora.
  - **Why if revived:** completeness frontier; current catalog filtered through Nursi-load-bearing-ness; cross-corpus extension may surface additional Policy candidates.

- **What:** Pressure-test FP2 against a rare-language corpus (Aramaic, Coptic, Sumerian, Akkadian, Ge'ez).
  - **Gate:** observable — when Comprehenslate touches a corpus whose source language has weak LLM detection reliability, or as a standalone research probe.
  - **Why if revived:** FP2's calibration-dependence on current-LLM-capability is untested at the rare-language edge; the principle may need refinement (or supplementary declarative fields) for languages LLMs handle weakly.

---

## Reasoning

The structurally non-obvious decisions had alternatives that were considered and rejected. The rejections matter — they show why the deliverable lands where it does.

**Why FP2 is named as a new principle rather than absorbed into FP1.** The chunking finding's *"schema ownership matches data ownership"* is preserved as FP1 because it correctly states the load-bearing relation. But FP1 alone leaves *"data the schema must own"* unspecified. The current simplification needed the narrowing — *"data the LLM cannot infer."* That narrowing is operationally distinct from FP1's ownership claim. Naming it as FP2 makes the narrowing explicit; embedding it in FP1 would lose its operational form (the integration-time predicate).

**Why the architecture is 3-LAYER, not 3-SCHEMA.** The chunking finding committed three schemas (SD + PC + TC). The current simplification has three layers (TC + Policy + PC) with the Policy layer holding multiple sibling classes. The semantic shift is from "named-schema-per-data-kind" to "named-layer-per-decision-axis." Under FP2, what differentiates Policy classes from each other isn't their data shape (they're all the same shape) but the per-edge-case decision they govern. That makes them a sibling-class family within a layer, not a schema per edge-case.

**Why drop SourceDescriptor instead of refining it.** Considered: keep SD with only the human-decidable handling fields (`embedded_languages_policy`; `source_temporal_register`) and drop only the LLM-inferable facts. Rejected because: (a) the user explicitly said *"we dont need SourceDescriptor"* — taking that at the architecture level, not just at the per-field level, is honest; (b) the surviving handling fields fit better as standalone Policy classes (each governing one edge-case, flatly composable) than as SD attributes (which would mix per-corpus declaration with per-field policy); (c) Policy classes generalize cross-corpus while SD-as-corpus-declaration is per-corpus. The Policy-class direction has greater fertility.

**Why language-agnosticism is a cross-policy principle, not specific to NonMainLangPartsPolicy.** The user's correction was generalized: *"it shoudl have been language agnostic."* Test of generalization: would any Policy class benefit from naming a specific language in its values? Consider `HonorificsPolicy` — a value like *"use-saw-not-pbuh"* would couple the schema to Islamic tradition. A language-agnostic alternative (*"preserve-original-script"*) generalizes to other traditions without semantic loss. The cross-policy generalization holds.

**Why the corpus mappings remain useful as documentation, not as schema content.** The `chunk_types_vs_mechanisms` finding committed Söz=chapter, mesele=subchapter, ayah=sentence, hashiye=paragraph as schema field values. Under the current simplification, the AI infers structure from text — so the mappings as schema content are obsolete. But they remain useful as *documentation* of how the AI should think about each corpus when training, prompting, or debugging. The "INVALID at schema location" verdict draws this distinction; the concept survives, the schema location does not.

**Why the alternative intervention shapes for correction propagation (REORGANIZE-WITHOUT-ADDING; REPAIR-in-place) were rejected.** Considered as alternatives to ADD-CONTENT (Correction Notices at the top of impacted findings). Both rejected on structural grounds. REORGANIZE-WITHOUT-ADDING relies on readers checking `_state.md` Relationships chains — a three-step navigation — when the Correction Notice is one step at point-of-entry. REPAIR-in-place destroys the findings-are-snapshots convention used across the project (the chunk_types_vs_mechanisms finding from one day prior set the precedent of archiving discipline outputs while keeping `finding.md` intact). Critique's strengthened-prosecution test on both alternatives confirmed the rejections.

**Why the INVALID verdicts on prior commitments are not too aggressive.** Critique's adversarial test constructed the strongest preservation case for each INVALID verdict and found that each preservation case fails on structural grounds (C1 TC-frozen; C2 SD-dropped; the user's explicit rejection of the universal hierarchy). The verdicts cite structural contradictions with the current architecture, not precedent or convention. The user-stated concern about over-aggressiveness was honestly tested and dismissed on substance.

**Why moderate candidates were not promoted to strong.** Each moderate candidate has a specific filter caveat that distinguishes it from a strong candidate. `TransliterationStandardPolicy` is partly translator-side (filter 3 partial). `PriorTranslationStancePolicy` has list-companion-structure (filter 1 near-miss). `AnachronismHandlingPolicy` overlaps with `ArchaicRegisterPolicy`. `CitationReferenceFormatPolicy` has narrow use-case. Promoting these to strong without addressing the caveats would understate the filter discipline.

**Why the 5 deferred candidates were not killed.** Killing would lose the conceptual entry point for the phenomena (script direction; passage typology; reader-mode; output finality; relay translation). Each carries a revival trigger so a future inquiry knows when to re-open. Deferred-with-revival-trigger preserves the option without committing the implementation.

---

## Open Questions

### Monitoring

- **`ArchaicRegisterPolicy` 4-literal sufficiency.** If `ArchaicRegisterPolicy` is adopted, monitor whether the 4 values are sufficient for actual Nursi translation work. Refinement trigger: if a 5th distinct strategy emerges during translation.

### Blocked

(None currently — all in-scope decisions adjudicated.)

### Research Frontiers

- **Cross-corpus Policy catalog completeness.** Item 2's catalog was filtered through Nursi-load-bearing-ness. Non-Islamic theological-translation corpora (Tanakh; Bible; Sanskrit-Hindu; Pali Buddhist; Christian patristic) may surface additional Policy candidates. Frontier: a survey inquiry covering non-Islamic theological-translation corpora.

- **LLM-inferability decay at rare languages.** FP2 assumes current-LLM-capability for source-language detection. Rare/dead languages (Aramaic; Coptic; Sumerian; Akkadian; Ge'ez) may require declarative fields the current architecture omits. Frontier: an inquiry that pressure-tests FP2 against a rare-language corpus.

- **FP2 as a project-wide rule.** AE1 assembly emergent (from Innovation, sustained at Critique). Whether FP2 generalizes beyond schemas.py to other AI-assisted system schemas in Comprehenslate or beyond is an open architectural question. Frontier: when the project-wide schema-style guide is written, FP2 is a candidate principle.

### Refinement Triggers

- **`source_language_fluency` revival.** Refinement trigger: if A3 `source_culture` produces ambiguous assignments due to language-fluency conflation in actual translation work (e.g., a reader who is `source-native` culturally but reads no Arabic — the conflation forces a wrong A3 choice when the text contains Arabic embeddings).

- **Policy-class organization.** If `schemas.py` grows beyond ~10 Policy classes, consider import-organization or sub-module split (e.g., `schemas/policies/source_apparatus.py`).

- **`PriorTranslationStancePolicy` adoption.** Adopt only if a `list[PriorRef]` companion structure can be cleanly added without complicating the Policy class itself.

- **Policy-class co-application precedence.** If multiple Policy classes co-apply to the same source text span and produce ambiguous render outputs in actual translation work (e.g., a Bismillah governed by both `FormulaicOpeningPolicy` and `NonMainLangPartsPolicy` with conflicting render preferences), document precedence rules — or evaluate whether the policies' value choices remain independent on close inspection.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
/traverse

explain why /Users/ns/Desktop/projects/comprehenslate/schemas.py makes a lot more sense. and also what other scenarios , policies like NonMainLangPartsPolicy exists? give me list of them
```

</details>
