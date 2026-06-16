# Sensemaking — schemas_rationale_and_policy_list

## User Input

```text
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/_branch.md

Upstream outputs in same folder: articulate_simple.md + surfacing.md. Read both as inquiry framing + upstream substrate. The Synthesis Trigger declared in _branch.md names 4 priors (schemas.py + 3 finding files) that must be re-tested per the inquiry's Inherited Commitments work — Sensemaking must do the re-testing, not just record the inheritance. Of particular concern: the chunk_types_vs_mechanisms finding's central commitments (chunking_granularity on TC; SD.canonical_level; corpus mappings) have been simplified past by the user — Sensemaking must determine commitment statuses (RE-TESTED confirmed / confirmed-but-frame-revised / found-INVALID).

Save sensemaking output to: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/sensemaking.md
```

---

## SV1 — Baseline Understanding

The user wants two things: a rationale explaining why their three-class `schemas.py` is better than the four-schema design they iterated past, plus a list of Policy classes shaped like `NonMainLangPartsPolicy`. The simplification feels right because it stops the schema from declaring facts the LLM can infer, and pushes the schema toward what the LLM actually needs at translation time: user strategy choices (TC), value judgments for recurring authorial edge-cases (small Policy classes), and engine knobs (PC). Item 2's list should be filtered through this same principle.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1.** TC is frozen — no new fields on `TranslationConfig`. (User explicit, this session.)
- **C2.** `SourceDescriptor` is dropped — no corpus-facts schema. (User explicit, this session.)
- **C3.** `EmbeddedLanguage` (prior class) is replaced by language-agnostic `NonMainLangPartsPolicy`.
- **C4.** `PipelineConfig` stays as the runtime-engine layer; `chunking_granularity` now lives here as a `Literal[5] | None` field.
- **C5.** Anti-bloat — Item 2's list must be filtered by real need, not exhaustive enumeration of theoretical candidates.
- **C6.** Language-agnosticism — Policy enum literals must not name specific languages or traditions (no "arabic", "quranic", "yusuf-ali" in values).
- **C7.** Synthesis Trigger requires re-testing chunk_types_vs_mechanisms and chunking_deep_dive and edge_cases_into_config_schema commitments with explicit verdicts.

### Key Insights

- **KI1 (load-bearing).** The LLM doesn't need source-language declarations to translate. The user's correction — *"translation happens regardless of the source language via LLMs, LLM just needs to know to what lang translation happens, and with what config. so we dont need SourceDescriptor"* — eliminates the need for SD as a corpus-facts schema. This is the simplification's central move.
- **KI2.** The four-schema design carried schemas FOR DECLARATIONS that LLMs make obsolete. The simplification asks at each candidate schema: "what value does this add to the LLM beyond what the LLM derives from the source text itself?"
- **KI3.** The split-placement principle ("schema ownership matches data ownership", from the chunking finding §3) is preserved but the "data the schema needs to own" has narrowed because the LLM handles more inference than the chunking finding's design assumed.
- **KI4.** Policy classes (NonMainLangPartsPolicy-shape) are a NEW THIRD KIND of schema, distinct from both TC (continuous strategy axes) and PC (engine knobs). They govern recurring authorial edge-cases where the LLM can detect the phenomenon but cannot autonomously decide HOW to handle it — the handling is a value judgment requiring user input.
- **KI5.** The chunk_types_vs_mechanisms finding's central schema-shape commitments are now INVALID at the schema-shape level. Two specifically: `chunking_granularity` belongs to runtime concerns (PC), not user strategy (TC); and `SD.canonical_level` imposed a universal hierarchy that doesn't fit corpus reality (the user's "book must follow certain chapter rules. which is not the case" rejection).

### Structural Points

- **SP1.** Three-layer schema architecture: TC (user-facing strategy axes) / Policy classes (per-edge-case enums) / PC (engine knobs).
- **SP2.** Each Policy class is the simplest possible structural shape: a single-field BaseModel with a Literal[N] enum.
- **SP3.** Policy values follow a 2D pattern when applicable: {preserve, replace} × {–, +note as annotation} + special-case slots (e.g., `replace-original-with-infamous-translation` for the "use accepted famous rendering" case).
- **SP4.** Policy classes sit flat as siblings of TC and PC, not nested inside a wrapper class.

### Foundational Principles

- **FP1.** "Schema ownership matches data ownership" (inherited from chunking finding §3 line 113) — confirmed but refined: "data" excludes anything the LLM can infer.
- **FP2 (NEW).** "Don't declare what the LLM can infer." This is the load-bearing new principle that generates the simplification. Its formal form is the LLM-inferable test: a candidate field belongs in the schema only if the LLM cannot derive its value from the source text + the rest of the configuration.
- **FP3.** Anti-bloat — bias against adding schema classes; bias toward dropping classes when the LLM-inferable test fires.
- **FP4.** Each Policy class governs ONE recurring authorial edge-case (not multiple); composability is at the schema-collection level (the user uses several Policy classes alongside one TC), not the class level.

### Meaning-Nodes

- **MN1.** *Authorial edge-case* — a phenomenon the author of the source text DID (embedded language; marginalia; archaic register; honorifics; voice changes; formulaic openings; embedded poetry; cross-references) that the translator must handle, where the handling is a value judgment requiring user input.
- **MN2.** *LLM-inferable vs human-decidable* — the test that gates schema membership. Inferable facts (the source language; chunk boundaries; existence of embedded Arabic) belong to the LLM and need no schema declaration. Decidable choices (preserve vs replace; honor existing translation traditions vs make new ones; flag every interpretive choice vs commit) require schema-carried user input.
- **MN3.** *Policy* as a schema-layer distinct from TC's strategy axes and PC's engine knobs.
- **MN4.** *Language-agnosticism* — Policy values describe what to do (the handling decision), not which specific language to do it on (the corpus-bound instance).

### Meta-Inspection cross-reference after SV2

- **H4 (concept names):** "authorial edge-case", "LLM-inferable vs human-decidable", and "Policy as a layer" are load-bearing terms newly stabilized here. They will be tested in Phase 3 below.
- **H5 (motivating examples):** the architecture is currently grounded in ONE example (NonMainLangPartsPolicy). The Specific-vs-pattern recognition cue fires — Phase 3 must explicitly test "is this Policy layer real, or is NonMainLangPartsPolicy a one-off?"

### SV2 — Anchor-Informed Understanding

Beyond SV1: the schemas.py simplification rests on a new foundational principle — *"Don't declare what the LLM can infer"* (FP2) — that refines the chunking finding's split-placement principle. The four-schema design carried SourceDescriptor as a corpus-facts schema; corpus facts (source language; embedded-language detection; structural unit boundaries) are LLM-inferable. What the LLM cannot infer is the user's value judgment on how to HANDLE recurring authorial edge-cases. That distinction generates the three-layer architecture: TC for the user's broad strategy choices (the 8 axes); Policy classes for per-edge-case value judgments (NonMainLangPartsPolicy and siblings); PC for engine knobs (chunking budget, mechanism override). Item 2's list catalogs *"recurring authorial edge-cases needing human value judgment"* filtered through C5 (anti-bloat) and C6 (language-agnosticism).

---

## Phase 2 — Perspective Checking

### Technical / Logical

- The three-class architecture is implementable as written; pydantic supports flat composition of `BaseModel` subclasses.
- Policy classes compose flatly; no nesting wrapper required.
- The LLM-inferable test is operationalizable as a runtime predicate: at integration time, ask *"does this field tell the LLM something it couldn't derive from the source text + the other config?"*
- **New anchor:** *implementation-gate* — each new Policy class must pass the LLM-inferable test before being added to schemas.py.

### Human / User

- The user wrote schemas.py directly after four turns of correction. Their mental model is shaped by what they pushed against. The rationale should echo their framing, not re-invent it.
- Recurring user values across this session: anti-bloat; not declaring what LLMs handle; language-agnosticism. These appear across multiple inquiries.
- **New anchor:** *user-language alignment* — "Policy" matches the user's own vocabulary (the user named `NonMainLangPartsPolicy` with "Policy" suffix; the prior edge-cases finding used "EmbeddedLanguagePolicy" with same suffix; both stable). The term "Policy" is not loop-coined.

### Strategic / Long-term

- Pattern from the edge_cases_into_config_schema finding: of 14 candidates, the user ratified 4 ADD-now + 3 already-routed + 7 DEFER. Default user pattern is heavy deferral.
- If Item 2 lists 10 Policy candidates, the user will likely adopt the strongest 2–3 immediately and defer the rest with revival triggers.
- **New anchor:** *list-strategy* — Item 2's list should be ranked by Nursi-load-bearing-ness, with explicit defer-vs-adopt verdicts and revival triggers for defers (matching the edge-cases finding's pattern).

### Risk / Failure

- **Risk-1.** Listing too many candidates → bloat the Policy layer (violates C5).
- **Risk-2.** Listing language-specific values in proposed policies → repeat the language-agnosticism violation (violates C6).
- **Risk-3.** Surfacing the rationale too narrowly → the explanation becomes "this specific simplification was right" instead of "here is the principle that generates this architecture, applicable forward."
- **Risk-4.** Reopening the user's drop of SD → triggers MQ4 NOT-list violation from `_branch.md`.
- **New anchor:** *rationale-shape* — the Item 1 explanation must be principle-grounded, not feature-by-feature comparison.

### Resource / Feasibility

- The inquiry is conversational; deliverable is text. No code-implementation gates.
- Both items fit in one finding with two sections.
- **New anchor:** *deliverable-shape* — one finding, two sections, each addressing one item, with shared principle-anchor in section 1.

### Definitional / Internal Consistency

- The four-schema design routed `source_temporal_register` + `source_edition` + `source_language_fluency` + `embedded_languages` to SD. Dropping SD orphans those.
- Apply the LLM-inferable test to each orphan:
  - **`source_language` and `source_language_age`** (proposed in earlier turn as freeform fields): LLM-inferable from source text. Consistent with SD-drop.
  - **`source_edition`**: LLM-irrelevant for translation operations (the LLM works on the text it receives, not the metadata about which printing it came from). Consistent with SD-drop.
  - **`source_language_fluency`**: this is reader-side (carries reader's fluency), so it would have been TC-shaped per the SD-vs-TC correction inquiry. But TC is now frozen, and the field is not load-bearing for current Nursi work. Status: defer.
  - **`source_temporal_register`**: VALUE JUDGMENT (preserve archaic vs modernize). This is exactly the LLM-cannot-infer category. It should have a home — and it fits the NonMainLangPartsPolicy shape: a single-field BaseModel with Literal[4] enum governing the recurring authorial edge-case of archaic source language.
- **New anchor:** *routing-residual* — `source_temporal_register` is currently homeless but is structurally a Policy class. It feeds Item 2 directly as `ArchaicRegisterPolicy`.

### Definitional / Frame-exit Completeness

**Gating predicate:** does the inquiry's commitments include terms inherited from prior findings, framing-level commitments, or upstream taxonomies AND used across ≥2 distinct values/levels WITHIN the inquiry's own committed structures? YES — the term "schema" is used at three distinct values/levels (TC / Policy / PC are three distinct schema-types in the new architecture). The perspective fires.

1. **Existence Enumeration.** Project-wide referents of "schema" include: pydantic BaseModel classes (in `schemas.py`); JSON-Schema config documents; database schemas (if any); the project's pre-existing config prose (`config_base_source.md`); the chunking finding's paper SourceDescriptor schema; the edge-cases finding's paper `EmbeddedLanguagePolicy` shape. The inquiry's frame includes only pydantic schemas (TC + Policy + PC).

2. **Role Assessment.** Out-of-frame referents — paper SD schema; paper EmbeddedLanguagePolicy; config_base_source.md prose — play a role: they shaped the trajectory the simplification corrects. They are load-bearing as antecedents. Corrective: not bring them into the current frame, but reference them as antecedents in Item 1's rationale (already planned). Operation coherence is preserved.

3. **Verdict Rigor.** Test the strongest counter to the "SD is dropped" verdict: *"but SD captured corpus-specific facts that no future LLM can reliably infer."* Structural test: a corpus with novel embedded language (a 15th-century Bosnian text mixing Old Church Slavonic, Arabic, Turkish). Can the LLM identify the embedded languages without declaration? Current LLMs detect language with high accuracy. Can the LLM infer the user's handling preference? No — handling is a value judgment. The structural test confirms the verdict: SD-as-corpus-facts is LLM-inferable; SD-as-handling-policies is human-decidable. The handling pieces survive as Policy classes; the facts pieces drop. Verdict holds.

4. **Residual / Coverage Justification.** Is there a frame-exit concern about "schema" the named categories did NOT capture? The Policy schema-type is NEW — not in prior findings. Concern: does this term match user vocabulary? Test: user named `NonMainLangPartsPolicy` with "Policy" suffix; edge-cases finding used "EmbeddedLanguagePolicy" with same suffix. Consistent. No further residual.

### Phase / Calibration-State

Does the schemas.py architecture depend on calibration the project has? Yes: the LLM's capability to infer source language reliably. Current state (Opus 4.7 used in this session): high reliability for major languages, moderate for rare ones. Future corpora with rare/dead languages (Aramaic, Coptic, Sumerian) may require some declarative fields the current architecture omits.

- **New anchor:** *calibration-gate* — the LLM-inferable principle assumes current-LLM-capability for the corpus languages in scope (Turkish + embedded Arabic + Persian). If the project later targets corpora with languages LLMs handle weakly, the principle may require re-application.

### Meta-Inspection cross-reference after SV3

- **H1 (candidate set):** is the candidate set for Item 2 right? Need cross-candidate unity check — are some of the proposed Policy classes actually the same underlying thing? Phase 3 will test.
- **H2 (frame scope):** covered by Frame-exit Completeness above.
- **H3 (question framing):** the user's word was "policies like NonMainLangPartsPolicy". The "like" is being read as structural-shape-match. Alternative reading: domain-similar (other multi-language scenarios). The articulation surfaced both. I will use the structural-shape-match reading because (a) the literal "like" + the user's anti-bloat preference + (b) the user wrote NonMainLangPartsPolicy from scratch as a clean small-enum shape, signalling the shape is what they want replicated. Phase 3 will test the alternative reading explicitly.
- **H7 (phase/calibration state):** covered by Phase perspective above.

### SV3 — Multi-Perspective Understanding

Beyond SV2: the simplification's principle generates a three-layer architecture (TC strategy / Policy edge-cases / PC engine), and Item 2's list is generated by applying the LLM-inferable test plus the language-agnostic test plus the structural-shape test to the broader theological-translation edge-case territory. Multiple homeless residuals from prior inquiries surface as candidate Policy classes — `source_temporal_register` (now `ArchaicRegisterPolicy`) specifically is a strong direct fit. The deliverable is one finding with two sections, principle-grounded in section 1, list-strategy-applied in section 2. The architecture relies on current-LLM-capability calibration for major languages.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — Is "Policy" a structurally real third schema-type, or a naming convention?

**Strongest counter-interpretation:** *"Policy" is just NonMainLangPartsPolicy and similar — they're loose siblings that happen to share a suffix. There's no meaningful three-layer architecture; there's just TC + PC + some helper classes.*

**Why the counter fails (structural):** The user wrote `NonMainLangPartsPolicy` as a separate class rather than adding to TC or PC. The class carries a distinct kind of fact: a value judgment about a recurring authorial edge-case. The user's prior correction *"embedded_languages... shouldnt be there too, it should be in another dataclass"* specifies a separate-class location precisely because the existing categories (TC strategy axes; PC engine knobs) don't fit. The structural distinction is real:

| Schema-kind | What it holds | Decision-axis | Defaults driver | Typical consumer |
|---|---|---|---|---|
| TC | Continuous strategy axes | User-facing translation choices | A4 purpose-driven (some axes) | User (per job) |
| Policy | Per-edge-case enum | Authorial edge-case handling decisions | Sensible per-edge-case defaults | User (with edge-case awareness) |
| PC | Engine knobs | Runtime / pipeline tuning | None / engine-derived | Operator / dev (rarely user) |

These three columns differ on every row. The structural distinction is load-bearing.

**Confidence:** HIGH.

**Resolution:** Policy is a structurally real third schema-type with distinct role.

- **Fixed:** the three-layer architecture (TC / Policy / PC).
- **No longer allowed:** collapsing Policy classes into TC or PC; treating Policy as a naming convention.
- **Depends:** Item 2's list-strategy treats policies as a flat family of siblings.
- **Model change:** the architecture is three-LAYER, not just three-CLASSES.

### Ambiguity 2 — What test gates schema membership?

**Strongest counter-interpretation:** *Classify by frequency — fields for phenomena that appear often enough in real translation work.*

**Why the counter fails (structural):** Frequency is a SIGNAL of relevance but not the right test for schema-membership. A high-frequency phenomenon the LLM handles autonomously (punctuation conventions; word-order normalization; sentence-tokenization) still doesn't need a schema field. The structural test is: *can the LLM make this decision without user input, given the source text and the rest of the config?* If yes (inference) → no schema needed. If no (value judgment) → schema needed. Frequency only matters insofar as it determines whether providing user-input plumbing is worthwhile.

**Confidence:** HIGH.

**Resolution:** "LLM-inferable vs human-decidable" is the schema-membership test.

- **Fixed:** the test predicate.
- **No longer allowed:** adding schema fields for LLM-inferable facts (source language detection; chunk boundaries; existence of embedded foreign segments; structural-unit names).
- **Depends:** Item 2's list applies this test to every candidate.
- **Model change:** the test is now an architectural principle future additions must obey.

### Ambiguity 3 — Does language-agnosticism apply only to NonMainLangPartsPolicy or as cross-policy principle?

**Strongest counter-interpretation:** *NonMainLangPartsPolicy needed language-agnosticism because it spans languages; other policies might legitimately name a specific language or tradition (e.g., a HonorificsPolicy might validly have a `quranic-tradition` value).*

**Why the counter fails (structural):** The user's correction was generalized — *"it shoudl have been language agnostic."* The reasoning generalizes: a value name with a language/tradition in it is corpus-bound, and Policy classes are meant to be reusable across corpora at the schema level (instances per job can still be Nursi-specific or Quran-specific). The test: would the same value name work for a different corpus? `render-via-tradition` works for Quran (Yusuf Ali), Bible (KJV), Talmud (Soncino); `use-yusuf-ali` doesn't generalize. The language/tradition is a property of the JOB instance, not of the SCHEMA values.

**Confidence:** HIGH.

**Resolution:** Language-agnosticism applies to all Policy classes.

- **Fixed:** Policy enum literals never name specific languages, traditions, or corpora.
- **No longer allowed:** values like `preserve-arabic-with-gloss`, `use-yusuf-ali`, `render-as-quranic-citation`.
- **Depends:** Item 2's proposed policies must follow this principle.
- **Model change:** language-agnosticism becomes a cross-cutting design constraint at the Policy layer.

### Ambiguity 4 — Is "authorial edge-case" a load-bearing structural category, or a fuzzy label? (H4 Load-bearing concept test)

**Strongest counter-interpretation:** *"Authorial edge-case" is fuzzy — any recurring thing in the source text could be called an edge-case. The label is descriptive but not structural.*

**Why the counter fails (structural):** The distinguishing structural feature is that the phenomenon was an **authorial choice** (the AUTHOR did something requiring a handling decision) — not an emergent property of the language and not a translator-side or publication-side concern. Examples:

- An author choosing to embed Arabic ayahs IS an authorial choice (Nursi did this; Mevlana didn't).
- The author's marginalia (hashiye in Nursi; glosses in Talmud) IS authorial.
- The author's choice to write in archaic register at theological moments IS authorial.
- Punctuation conventions are NOT authorial — they're language/copyist properties (translator-side handles).
- Page layout, font choices ARE NOT authorial — they're publication-side.
- The reader's silent-vs-aloud consumption preference IS NOT authorial — it's reader-side.

The category is structural: it bounds Item 2's list by excluding translator-side, publication-side, and reader-side concerns.

**Confidence:** HIGH.

**Resolution:** "Authorial edge-case" is a real structural category with a defined boundary.

- **Fixed:** Policy classes govern authorial edge-cases.
- **No longer allowed:** confusing translator-side (translation strategy → TC), publication-side (out of schema scope), or reader-side (TC.A4 captures some of this; rest deferred) concerns with authorial edge-cases.
- **Depends:** Item 2's filter applies this category.
- **Model change:** the catalog has a structural boundary, not a fuzzy boundary.

### Ambiguity 5 — Specific-vs-pattern: is the Policy layer a real pattern or a one-off from NonMainLangPartsPolicy? (H5 Specific-vs-pattern recognition cue)

**Strongest counter-interpretation:** *Only one Policy class exists currently. The "Policy layer" might be over-extrapolation — NonMainLangPartsPolicy might be sui generis (the only authorial edge-case where the LLM can detect the phenomenon but cannot decide handling).*

**Why the counter fails (structural):** The 14-edge-case innovation pass already surfaced multiple phenomena with the same shape: voice_disambiguation (#4), source_apparatus_handling (#6), source_temporal_register (#13), passage_typology (#7 — partial). Each is an authorial edge-case where the LLM can detect the phenomenon (it can detect voice changes, marginalia, archaic vocabulary) but cannot decide handling without user value judgment. The pattern is real. Additionally, beyond the 14, theological-translation territory carries honorifics (SAW/AS/RA; ZT"L/OBM), formulaic openings (Bismillah/Shema), embedded poetry (Mevlana couplets vs prose Arabic), each with the same shape.

**Confidence:** HIGH.

**Resolution:** The Policy layer is a real pattern, not a one-off.

- **Fixed:** the pattern generalizes; Item 2 can produce a substantive list.
- **No longer allowed:** treating Policy as exhaustive at one class.
- **Depends:** Item 2's list strength rests on this commitment.
- **Model change:** the architecture is genuinely three-layer with the Policy layer expecting multiple instances.

### Ambiguity 6 — Inherited Commitments Re-test (required by Synthesis Trigger)

The chunk_types_vs_mechanisms finding's central schema-shape commitments are at stake. The chunking_deep_dive's split-placement and the edge_cases finding's SD additions are also at stake.

**Strongest counter-interpretation (for preserving the chunk_types_vs_mechanisms commitments):** *the commitments were right at the time; the current simplification is a separate-axis improvement that doesn't invalidate prior work.*

**Why the counter fails (structural):** The chunk_types_vs_mechanisms finding made schema-shape decisions that the user's simplification structurally CONTRADICTS at the schema-shape level. They cannot both be true simultaneously. Specifically:

- **(a) `chunking_granularity` on TC** — The chunk_types_vs_mechanisms finding committed it to TC. The user moved it to PC explicitly. Structural contradiction: TC's purpose is user strategy axes; chunking is now classified as operational (PC). Status: **commitment found INVALID at schema-home level**; the 5-literal values are preserved as the enum content on PC.
- **(b) `SD.canonical_level` mapping corpus types to universal hierarchy** — The chunk_types_vs_mechanisms finding committed a 5-literal hierarchical ladder with corpus mappings. The user rejected the universal hierarchy: *"book must follow certain chapter rules. which is not the case"* + dropped chunking_units list. Structural contradiction: imposed hierarchy ≠ corpus reality. Status: **commitment found INVALID**.
- **(c) Corpus mappings on SD (Söz=chapter, mesele=subchapter, ayah=sentence with is_atomic, hashiye=paragraph attached_to)** — The chunk_types_vs_mechanisms finding committed these as schema content. With SD dropped, these have no schema home. Status: **commitment found INVALID at schema location**; the mappings may still be documentation but not schema field values.

For the chunking_deep_dive's split-placement principle: the principle holds but the architecture has refined. Status: **RE-TESTED — confirmed but frame revised.** The three schemas are now TC + Policy + PC, not SD + PC + TC. The principle ("schema ownership matches data ownership") is preserved; the application has changed because "data" excludes LLM-inferable facts.

For the edge_cases finding's 4 SourceDescriptor additions: all carried on SD, which is now dropped. Status: **commitments found INVALID at schema location**. Sub-statuses:
- `source_language_fluency` → defer (not load-bearing for current Nursi work; was reader-side, doesn't fit current architecture cleanly).
- `source_edition` → drop (LLM-irrelevant per FP2).
- `source_temporal_register` → re-home as `ArchaicRegisterPolicy` (fits Policy layer shape).
- `embedded_languages: list[EmbeddedLanguagePolicy]` → replaced by `NonMainLangPartsPolicy` (the single language-agnostic Policy class).

**Confidence:** HIGH on all INVALID determinations; HIGH on the chunking_deep_dive preservation-with-frame-revision.

**Resolution:** The inheritance status table is now explicit; the finding's Inherited Commitments Re-test section will lay it out per commitment.

- **Fixed:** verdicts per inherited commitment.
- **No longer allowed:** silently inheriting the INVALID commitments; pretending the chunk_types_vs_mechanisms finding's schema-shape decisions are still load-bearing.
- **Depends:** Next Actions in the finding must include correction notes to the impacted prior findings (REFINES + CORRECTS frontmatter).
- **Model change:** the inquiry is a corrective finding with reach back into 3 priors.

### SV4 — Clarified Understanding

The schemas.py simplification rests on the load-bearing FP2 principle: *"Don't declare what the LLM can infer."* This generates a three-layer architecture: TC (user strategy axes, frozen at 8) + Policy classes (per-edge-case enums for recurring authorial value judgments) + PC (engine knobs). NonMainLangPartsPolicy is the first instance of the Policy layer. Item 2's list catalogs other Policy-shaped scenarios, filtered through (1) structural shape (single-field BaseModel with Literal[] enum), (2) language-agnosticism (no language/tradition names in values), (3) authorial-edge-case category (not translator-side / publication-side / reader-side), (4) LLM-can't-infer (human value judgment required). Multiple prior commitments are now found INVALID and the finding must propagate corrections.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed

- Three-layer architecture: TC (strategy) / Policy (per-edge-case) / PC (engine).
- TC delta = 0.
- Policy classes are single-field `BaseModel` with `Literal[N]` enum.
- Policy values are language/tradition-agnostic.
- Policies govern authorial edge-cases requiring human value judgment.
- LLM-inferable test gates schema-membership.
- Item 1 delivers a principle-grounded rationale.
- Item 2 delivers a filtered, ranked list with adopt/defer verdicts and revival triggers.

### Eliminated

- Adding a fourth schema kind alongside TC / Policy / PC.
- Reviving `SourceDescriptor`.
- Reviving a per-language `EmbeddedLanguage` class (replaced by single language-agnostic `NonMainLangPartsPolicy`).
- Adding `chunking_granularity` to TC (it lives on PC).
- Adding `canonical_level` mapping to any schema.
- Naming languages/traditions in Policy enum values.
- Listing every theological-translation phenomenon — must filter.
- Pretending the chunk_types_vs_mechanisms TC.chunking_granularity + SD.canonical_level commitments are still load-bearing.

### Viable paths remaining

**For Item 1 (rationale):** principle-grounded explanation organized as:
1. The new principle (FP2: don't declare what the LLM can infer).
2. The three-layer architecture it generates.
3. What it simplified past (with the dropped-commitments table).
4. The residual issues (calibration-gate; homeless source_temporal_register being re-homed as ArchaicRegisterPolicy).

**For Item 2 (list):** filtered catalog of Policy-shaped scenarios.

Strong candidates (high Nursi load-bearing, clean shape-fit):
- `SourceApparatusPolicy` (author marginalia handling; from edge-case #6)
- `VoiceMarkingPolicy` (author-vs-cited voice differentiation; from edge-case #4)
- `ArchaicRegisterPolicy` (handling archaic source language; from edge-case #13 + homeless residual)
- `HonorificsPolicy` (theological honorifics: SAW/AS/RA/PBUH; ZT"L/OBM; etc.; beyond the 14)
- `FormulaicOpeningPolicy` (Bismillah/Shema/invocations; beyond the 14)
- `EmbeddedPoetryPolicy` (Mevlana couplets, psalms, slokas — distinct render decision from prose embedded language; beyond the 14)

Moderate candidates (shape-fit good but lower load-bearing or composition concerns):
- `TransliterationStandardPolicy` (ALA-LC / DIN-31635 / popular)
- `PriorTranslationStancePolicy` (independent / honor-terminology / extend-with-revisions / divergence-noted / collate; from edge-case #11 — but carries list[PriorRef] which breaks pure-policy shape)
- `AnachronismHandlingPolicy` (kalam terms; obscure references — overlaps `ArchaicRegisterPolicy`)
- `CitationReferenceFormatPolicy` (sura:ayah; book:ch:v; canto:line — potentially too corpus-specific)

Deferred / out-of-shape (don't fit the Policy pattern):
- `ScriptDirectionPolicy` (edge-case #14 — rendering surface, not authorial)
- `PassageTypologyPolicy` (edge-case #7 — typology label, not handling strategy)
- `ConsumptionModePolicy` / `ReadingSessionPolicy` (edge-cases #9, #10 — reader-side)
- `OutputFinalityPolicy` (edge-case #12 — pipeline-side)
- `RelayTranslationPolicy` (edge-case #5 — carries chain structure breaking shape)
- Per-corpus mappings / SD-revival — eliminated by C2.

### SV5 — Constrained Understanding

The finding has two sections matching the two items. Section 1 explains the LLM-inferable principle, the three-layer architecture, and the dropped-commitments table. Section 2 provides 6 strong Policy candidates + 4 moderate + 5 defers, each with shape-fit verdict and rationale. The finding inherits commitments from three prior findings: chunk_types_vs_mechanisms (most schema-shape commitments INVALID); chunking_deep_dive (preserved with frame revision); edge_cases_into_config_schema (most INVALID at schema location, with re-routing notes). The corrective reach is documented in the Inherited Commitments Re-test section and reflected in REFINES / CORRECTS frontmatter.

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Did new perspectives keep destabilizing the model? Reviewing the perspectives:

- Technical perspective confirmed implementability — no destabilization.
- Human perspective confirmed user-language alignment — no destabilization.
- Strategic perspective added list-ranking strategy — additive, not destabilizing.
- Risk perspective added constraints — additive.
- Resource perspective added deliverable shape — additive.
- Definitional Internal Consistency surfaced source_temporal_register routing residual — additive (fed Item 2).
- Definitional Frame-exit Completeness surfaced fourth-schema-kind concern but resolved (Policy is structurally real) — no destabilization.
- Phase / Calibration-State added calibration-gate constraint — additive.

No model-misfit pattern. Accommodation trigger does not fire. Stabilization is appropriate.

### Final stabilized model (SV6)

**The schemas.py architecture rests on a new foundational principle: "Don't declare what the LLM can infer."** This principle refines the chunking finding's split-placement principle ("schema ownership matches data ownership"). The "data" the schema needs to own has narrowed because modern LLMs infer source-language facts, embedded-language detection, and structural boundaries that the four-schema design assumed would be declared.

**The principle generates a three-layer architecture:**

1. **TranslationConfig (TC)** — the user's broad strategy choices. Continuous-axis Literal[] enums on what the translation should be like (reader level / domain expertise / source culture / purpose / fidelity / form preservation / scaffolding / analysis depth). Frozen at 8 axes. Defaults A4-purpose-driven where applicable. The user picks once per job.

2. **Policy classes** — per-edge-case enums for recurring authorial value judgments. Each is a single-field BaseModel with a `Literal[N]` enum. Values are language/tradition-agnostic. Each Policy class governs ONE authorial edge-case the LLM cannot autonomously decide (because handling is a human value judgment, not an inference). NonMainLangPartsPolicy is the first instance; the catalog generalizes.

3. **PipelineConfig (PC)** — engine knobs the operator tunes (rarely user). Token budgets; chunking granularity (`Literal[5] | None`); chunking mechanism override.

**Item 2's list applies four filters to the theological-translation edge-case territory:** (a) structural shape (single-field BaseModel + Literal[] enum); (b) language-agnosticism (no language/tradition in values); (c) authorial edge-case category (not translator/publication/reader-side); (d) LLM-can't-infer (handling is value judgment).

**Inherited commitments are RE-TESTED:** chunk_types_vs_mechanisms's TC.chunking_granularity + SD.canonical_level + corpus mappings are INVALID (schema-shape contradictions with current architecture); chunking_deep_dive's split-placement principle is CONFIRMED with frame revision (three layers TC/Policy/PC, not three schemas SD/PC/TC); edge_cases's 4 SD additions are INVALID at schema location with sub-statuses (defer / drop / re-home / replaced).

### SV6 — Stabilized Model

**SV6 in one paragraph:** The schemas.py simplification is generated by a new foundational principle (*"Don't declare what the LLM can infer"*) that refines the chunking finding's split-placement principle. The data the schema needs to own has narrowed because LLMs handle inference that prior designs assumed would be declared. What remains in schema is what the LLM cannot autonomously decide: TC for user strategy, Policy classes for recurring authorial-edge-case value judgments, PC for engine knobs. The architecture is three-LAYER, with Policy as a structurally real third schema-kind, not a naming convention. Item 2's list filters the theological-translation edge-case territory through structural shape + language-agnosticism + authorial-edge-case + LLM-can't-infer, producing ~6 strong candidates + 4 moderate + 5 deferred. The finding has substantial corrective reach into three prior findings (most acutely the chunk_types_vs_mechanisms finding's schema-shape commitments which are found INVALID).

**How SV6 differs from SV1:**
- SV1 framed the request as "explain the design + list similar candidates."
- SV6 grounds the answer in a NEW principle (LLM-inferable) that subsumes and refines the prior split-placement principle.
- SV6 identifies that BOTH items derive from the same principle — section 1 names the principle; section 2 applies it.
- SV6 makes the corrective reach explicit (three prior findings impacted with explicit INVALID / CONFIRMED-with-frame-revision verdicts).
- SV6 commits to the "Policy" layer as a structurally real third schema-kind, not a naming pattern.

---

## Saturation Indicators (Telemetry)

- **Perspective saturation:** the last two perspectives (Phase / Calibration-State; Frame-exit Completeness's residual step) confirmed existing anchors without producing new anchor types. Approaching saturation.
- **Ambiguity resolution ratio:** 6 ambiguities identified; 6 resolved with HIGH confidence; 0 OPEN. Ratio = 1.0.
- **SV delta:** SV1 was "explain + list" framing; SV6 grounds both items in the LLM-inferable principle and identifies the architecture as three-LAYER with Policy as a structurally real schema-kind. Substantial structural shift.
- **Anchor diversity:** anchors came from all five types (Constraints / Key Insights / Structural Points / Foundational Principles / Meaning-Nodes) and from multiple perspectives (Technical / Human / Strategic / Risk / Resource / Internal Consistency / Frame-exit / Phase). Multi-dimensional.

## Failure Mode Check (Pattern B — process-level)

- **Status Quo Bias:** NOT FIRED. The chunk_types_vs_mechanisms commitments are findings the inquiry is INVALIDATING — the discipline did not protect them defensively.
- **Premature Stabilization:** NOT FIRED. Six ambiguities collapsed with HIGH confidence after multi-perspective testing; the Accommodation trigger did not fire.
- **Anchor Dominance:** PARTIAL FIRE — the LLM-inferable principle (FP2) is doing a lot of work. Corrective check: if FP2 were removed, the model would collapse to the chunking finding's prior split-placement (still load-bearing). The architecture has multiple anchors (FP1, FP2, FP3, SP1, MN1, MN2, MN3, MN4), but FP2 is the load-bearing one for this inquiry's central move. This is accepted because the inquiry is about WHY the simplification happened — FP2 IS the answer; centering it is correct.
- **Perspective Blindness:** NOT FIRED. The uncomfortable perspectives (Risk; Frame-exit Completeness Verdict Rigor) were explicitly applied.
- **Clean Resolution Trap:** NOT FIRED. Each ambiguity's resolution was tested on structural grounds (mechanism / shape / consistency), not on precedent alone.
- **Self-Reference Blindness:** NOT FIRED. The inquiry is about a CODE artifact (`schemas.py`), not about Sensemaking itself.

## Verdict

**PROCEED.** Six SVs produced with substantial delta from SV1. Six ambiguities collapsed at HIGH confidence. No LAYER 1 (failure modes #1-6) fires. One PARTIAL flag on Anchor Dominance, mitigated by the inquiry's principle-anchored nature. Inherited Commitments Re-test produced explicit verdicts for the Synthesis Trigger's three priors.
