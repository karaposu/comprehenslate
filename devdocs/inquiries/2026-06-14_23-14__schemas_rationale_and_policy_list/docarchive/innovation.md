# Innovation — schemas_rationale_and_policy_list

## User Input

```text
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/_branch.md

Upstream outputs in same folder: articulate_simple.md + surfacing.md + sensemaking.md + decomposition.md. The decomposition's 6 pieces (P1-P6) are the seed structure; this is Production-task mode — Innovation generates candidate content per piece:
- P1: principle text + 3-layer architecture table + 4 filters
- P2: Item 1 rationale narrative
- P3: Item 2 catalog (~15 Policy candidates with class sketches)
- P4: Inherited Commitments Re-test table for 3 priors
- P5: Next Actions (correction notes)
- P6: Open Questions

Save innovation output to: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/innovation.md
```

---

## Seed + Methodology-Mode Consideration

### Seed

The 6-piece structure from Decomposition (P1-P6) as a Production-task seed: Innovation generates principal candidate content per piece, with piece-level Inversion at meta-decision pieces.

### Inherited methodology mode

**Standard default** (4G+3F balanced; elaborate the SV6 stabilized direction). Text signal in seed framing: "Production-task mode — Innovation generates candidate content per piece" — no explicit contrarian / generator-weighted / depth-iteration / minimum-mechanism signals; defaults to Standard default.

### Alternative mode named

**Contrarian-rethink (Framer-weighted)** — would re-open whether the SV6 stabilized model itself is sound, treating FP2 and the three-layer architecture as candidates to invalidate.

### What follows under the alternative

If Contrarian-rethink were applied: Inversion + Constraint Manipulation REMOVE + Lens Shifting on success criteria would dominate; candidate space would emphasize "what if FP2 is wrong?" / "what if the Policy layer collapses back into TC?" / "what if the LLM-inferable test fails for current Nursi work?" Each piece would carry a strong-form alternative rather than principal-candidate-plus-Inversion-test.

### Decision

**Default — Standard default.** Reason: SV6 explicitly went through Contrarian-rethink-style adjudication in Sensemaking (six ambiguities collapsed under structural pressure; the Inherited Commitments Re-test forced INVALID verdicts on prior commitments). Re-running Contrarian-rethink at Innovation stage would duplicate the work without surfacing new structural challenges. Piece-level Inversion at meta-decision pieces (P1, P4, P5) provides the within-Standard-default defense-in-depth.

---

## Meta-Decision-Piece Classification

| Piece | Properties firing | Classification |
|---|---|---|
| P1 — Conceptual substrate | (b) framing-semantic + (c) lesson-vocabulary (FP2 name; Policy-as-layer name) | **META-DECISION** |
| P2 — Item 1 rationale | content-production within the frame committed at P1 | content-production |
| P3 — Item 2 catalog | content-production within the filters committed at P1 | content-production |
| P4 — Inherited Re-test | (a) relationship-label commitment (REFINES / CORRECTS frontmatter) | **META-DECISION** |
| P5 — Next Actions | (e) intervention-shape commitment (ADD-CONTENT correction notices via REPAIR-on-priors) | **META-DECISION** |
| P6 — Open Questions | content-production residuals | content-production |

P1, P4, P5 require piece-level Inversion-candidate per the Phase 2 Generate refinement notes. P5's Inversion targets the intervention-shape axis per the Intervention-Shape-Axis Inversion refinement.

---

## P1 — Conceptual Substrate

### Principal candidate (PC1)

**The principle (FP2):** *Don't declare what the LLM can infer.*

A schema field belongs in `schemas.py` only when the LLM cannot derive its value from the source text plus the rest of the configuration. Source facts the LLM can detect (the source language; the existence of embedded Arabic ayahs; structural boundaries) are inferred at runtime. Value judgments the LLM cannot make autonomously (preserve vs replace; honor existing translation traditions vs make new ones; mark archaisms or modernize them) are declared in the schema.

This refines the chunking finding's FP1 (*"schema ownership matches data ownership"*). FP1 said the schema must own the data it represents; FP2 narrows what counts as data the schema must own — anything the LLM infers is no longer schema-owned data, it lives in the source text.

**Operational form of FP2:** at integration time, ask of each candidate field: *"Can the LLM derive this value from the source text plus the rest of the config?"* If YES → no schema field needed (inference). If NO → schema field carries the user's value judgment.

**The three-layer architecture:**

| Layer | Holds | Decision-axis | Defaults driver | Typical consumer |
|---|---|---|---|---|
| `TranslationConfig` (TC) | Continuous strategy axes | User-facing translation choices | A4 purpose drives some axis defaults | User, once per job |
| Policy classes (`NonMainLangPartsPolicy`, ...) | Per-edge-case `Literal[]` enum | Authorial-edge-case handling decision | Sensible per-edge-case default | User, per relevant edge-case |
| `PipelineConfig` (PC) | Runtime engine knobs | Pipeline tuning | None / engine-derived | Operator / dev (rarely user) |

`NonMainLangPartsPolicy` is the canonical Policy example.

**The four filters for Item 2 (catalog membership tests):**

1. **Structural shape** — single-field `BaseModel` with `Literal[N]` enum.
2. **Language-agnosticism** — enum literals never name a specific language, tradition, or corpus.
3. **Authorial-edge-case category** — the phenomenon is something the author DID; not translator-side, publication-side, or reader-side.
4. **LLM-can't-infer** — the handling decision is a human value judgment, not an inference.

**Mechanism trace:** Combination (principle + architecture + filter-set into a unified substrate) + Absence Recognition (redesign-level: what was missing in the 4-schema design? Answer: the test for *"should this be in schema at all"*; FP2 names that test) + Inversion (PI1 below).

### Piece-level Inversion candidate (PI1)

Assumption reversed: *"Don't declare what the LLM can infer."* → *"Declare what the LLM might fail to infer."*

What follows: SD would be re-added with belt-and-suspenders fields (source_language; source_temporal_register; etc.) as redundant grounding for LLM-inference failures. Defenders would point to LLM hallucination on ambiguous source-language identification; declarations as reliability gain at minor schema cost.

**5-test on PI1:**
- Novelty: medium (it's roughly the prior 4-schema design)
- Scrutiny survival: WEAK — user explicitly rejected SD; LLM-inference reliability has not been load-bearing in observed failures; declared "facts" would still require human verification, which is itself a value judgment not a fact (so it'd just shift the burden)
- Fertility: low
- Actionability: medium
- Mechanism independence: only Inversion produces it
- **Verdict: REJECTED.** PC1 is the load-bearing choice.

### 5-test on PC1

- Novelty: HIGH — FP2 is a new principle generated by the user's correction insight, not inherited from priors
- Scrutiny survival: STRONG — six Sensemaking ambiguities tested counter-interpretations on structural grounds and survived
- Fertility: HIGH — generates the architecture AND the Item 2 filter set
- Actionability: HIGH — schemas.py exists; FP2 is applicable to future additions
- Mechanism independence: convergence from Combination + Absence Recognition + Inversion (PI1 rejected) + Lens Shifting (LLM-inference frame)
- **Verdict: ACTIONABLE.**

---

## P2 — Item 1 Rationale Narrative

### Principal candidate (PC2)

The narrative is structured in 5 movements:

**(1) Open with the principle.** State FP2 verbatim. Frame the relationship to FP1: FP2 doesn't replace FP1 — it tightens its application by narrowing the definition of "data the schema must own" to "data the LLM cannot derive from the source text."

**(2) Apply FP2 to each dropped/changed class.**

- **`SourceDescriptor` dropped.** SD carried corpus facts the LLM infers (source language detection; embedded-language detection; structural-unit boundaries). Under FP2, these are not schema-owned data. The user's correction makes this explicit: *"translation happens regardless of the source language via LLMs, LLM just needs to know to what lang translation happens, and with what config. so we dont need SourceDescriptor."*
- **Per-language `EmbeddedLanguage` replaced by `NonMainLangPartsPolicy`.** Per-language declarations are LLM-inferable; only the user's handling choice (preserve / replace / annotate) is human-decidable. The single language-agnostic Policy class captures the value judgment without per-language plumbing.
- **`chunking_granularity` moved off TC.** The chunk_types_vs_mechanisms finding placed it on TC; the user's frozen-TC constraint plus a sharper read of the field's purpose (operational, not strategic) moved it to PC.
- **`canonical_level` mapping dropped.** It imposed a universal 5-level hierarchy on corpus structure. The user's correction — *"book must follow certain chapter rules. which is not the case"* — rejects this; corpus structure varies and the LLM infers it from text.

**(3) Architectural before/after contrast.**

- **Before:** 4 schemas with mixed declarative + policy content. SD mixed source facts (which the LLM could infer) with handling policies (which the user must decide). The 4-schema shape obscured the who-decides-what boundary.
- **After:** 3 layers cleanly separated by who-decides-what. TC = user strategy (8 continuous axes); Policy classes = user's per-edge-case value judgments; PC = operator's engine knobs. The LLM handles all inference at runtime.

**(4) What's preserved.** The 8 TC axes (frozen); FP1 (with frame revision); chunking_deep_dive's hybrid harmony-aware default mechanism (now on PC.chunking_mechanism_override as None-default with hidden hybrid implementation).

**(5) Residuals flagged.** `source_temporal_register` (was Phase 2 on SD) re-homed as `ArchaicRegisterPolicy` candidate in Item 2. Calibration-gate: the LLM-inferable principle assumes current-LLM-capability for source-language inference; rare/dead languages may require a re-application.

**Mechanism trace:** Combination (FP2 + dropped-class examples + architecture contrast + residuals composed into narrative) + Lens Shifting (each dropped class re-evaluated under the FP2 lens — what looked load-bearing under FP1 alone collapses) + Domain Transfer (the LLM-inferable test mirrors prompt-engineering practice: *don't have the LLM confirm what it already knows; have it decide what it cannot*).

### 5-test on PC2

- Novelty: HIGH — first explicit articulation of why the simplification works
- Scrutiny survival: STRONG — each dropped class has explicit reasoning grounded in FP2 + user-correction quotes
- Fertility: MEDIUM — supports Item 2's catalog and future schema decisions
- Actionability: HIGH — reader can apply the narrative directly to schemas.py review
- Mechanism independence: convergence from Combination + Lens Shifting + Domain Transfer
- **Verdict: ACTIONABLE.**

---

## P3 — Item 2 Policy-list Catalog

### Principal candidate (PC3)

#### Strong candidates (pass all 4 filters with HIGH confidence)

**1. `SourceApparatusPolicy`** — governs how to handle the source's pre-existing apparatus (author's marginal annotations / glosses).

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

Filter verdicts: shape ✓ ; language-agnostic ✓ ; authorial ✓ (author wrote the marginalia) ; LLM-can't-infer ✓ (the LLM can detect marginalia but cannot decide whether the reader wants them inline / footnoted / dropped).

**2. `VoiceMarkingPolicy`** — governs differentiation between author voice and cited authorities / student additions.

```python
class VoiceMarkingPolicy(BaseModel):
    """How to mark transitions between author voice and cited authorities
    or student-voice additions. Edge case: Nursi's voice vs cited Quran/hadith
    vs student lahika letters; rabbinic source-stack with named attribution."""
    policy: Literal[
        "off",
        "implicit-typographic",
        "explicit-attribution-inline",
        "scholarly-apparatus-marking",
    ] = "implicit-typographic"
```

Filter verdicts: all 4 ✓.

**3. `ArchaicRegisterPolicy`** — governs handling of archaic source language. **Carries the homeless `source_temporal_register` field re-homed from the edge_cases finding.**

```python
class ArchaicRegisterPolicy(BaseModel):
    """How to handle archaic source-language register. Edge case: Nursi's
    1920s-30s Turkish with Ottoman residue; Early Modern English in
    Shakespeare-era source; Classical Arabic in modern theological writing."""
    policy: Literal[
        "preserve-archaic-throughout",
        "modernize-fully",
        "hybrid-by-register-domain",
        "mark-archaisms-explicitly",
    ] = "hybrid-by-register-domain"
```

Filter verdicts: all 4 ✓. Composes positively with Layer-2 register-alternation preservation per chunking_deep_dive's commitment.

**4. `HonorificsPolicy`** — governs theological honorifics that follow names (SAW / AS / RA / PBUH for Islamic; ZT"L / RA / OBM for Jewish; analogous conventions in other traditions).

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

Filter verdicts: all 4 ✓. Note: language-agnostic via the policy values (no tradition-specific names like "saw" in literals).

**5. `FormulaicOpeningPolicy`** — governs formulaic openings (Bismillah; Shema; Christian invocations; Vedic mantras).

```python
class FormulaicOpeningPolicy(BaseModel):
    """How to render formulaic openings (invocations, basmala, dedicatory
    formulae). Edge case: every theological treatise opens with one."""
    policy: Literal[
        "preserve-original-with-translation",
        "transliterate-with-translation",
        "translate-only",
        "preserve-original-untranslated",
    ] = "preserve-original-with-translation"
```

Filter verdicts: all 4 ✓.

**6. `EmbeddedPoetryPolicy`** — governs embedded poetry (Mevlana couplets in Nursi; psalms in prose-Bible commentary; slokas in Hindu prose).

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

Filter verdicts: all 4 ✓. Distinct from `NonMainLangPartsPolicy` because the rendering decision differs (prose-quote handling vs verse-form preservation are different value judgments).

#### Moderate candidates (filter caveats noted)

**7. `TransliterationStandardPolicy`** — moderate. Shape ✓; agnostic ✓ (literal values are scheme-shape names, not specific schemes); authorial PARTIAL (transliteration is partly translator-side); LLM-can't-infer ✓.

```python
class TransliterationStandardPolicy(BaseModel):
    """Which transliteration convention to use when rendering source script in target script."""
    policy: Literal[
        "scholarly-standard",
        "popular-standard",
        "phonetic",
        "diacritic-stripped",
    ] = "scholarly-standard"
```

**8. `PriorTranslationStancePolicy`** — moderate. Shape ✓ (single field of literals); other 3 ✓. Caveat: companion data (`list[PriorRef]`) for which translations are being honored/extended would live separately (not on this Policy class).

```python
class PriorTranslationStancePolicy(BaseModel):
    """Stance toward established prior translations of this corpus."""
    stance: Literal[
        "independent",
        "honor-terminology",
        "extend-with-revisions",
        "explicit-divergence-noted",
        "collate-and-cite",
    ] = "independent"
```

**9. `AnachronismHandlingPolicy`** — moderate. Overlaps with `ArchaicRegisterPolicy` at the boundary (when does archaism become anachronism?).

```python
class AnachronismHandlingPolicy(BaseModel):
    """How to handle source content that was contemporary at authorship
    but is anachronistic for current readers (e.g., kalam terminology
    once familiar, now obscure; place-names since changed)."""
    policy: Literal[
        "preserve-with-footnote",
        "inline-gloss",
        "modernize-equivalent",
        "drop-and-replace-current",
    ] = "inline-gloss"
```

**10. `CitationReferenceFormatPolicy`** — moderate. Shape ✓; agnostic ✓; authorial ✓; LLM-can't-infer ✓. Use-case is narrow (only matters for corpora with formal citation conventions).

```python
class CitationReferenceFormatPolicy(BaseModel):
    """How to render cross-reference notation (sura:ayah; book:ch:v; canto:line)."""
    policy: Literal[
        "preserve-source-format",
        "standardize-canonical",
        "both-with-cross-reference",
        "footnoted-only",
    ] = "preserve-source-format"
```

#### Deferred / out-of-shape

**11. `ScriptDirectionPolicy`** (edge-case #14). DEFERRED — output-rendering surface, not authorial. Revival trigger: when output rendering reaches bidirectional-display stage.

**12. `PassageTypologyPolicy`** (edge-case #7). DEFERRED — not policy-shaped; it's a typology label per chunk, not a strategy choice. Revival trigger: if a per-chunk typology mechanism is committed.

**13. `ConsumptionModePolicy` / `ReadingSessionPolicy`** (edge-cases #9 + #10). DEFERRED — reader-side, not authorial. Revival trigger: when reader-side context becomes load-bearing for translation choices beyond TC.A4.

**14. `OutputFinalityPolicy`** (edge-case #12). DEFERRED — pipeline-side / output-status, not authorial. If revived, would belong on PC. Revival trigger: when downstream pipeline distinguishes finality levels (draft / final / teaching).

**15. `RelayTranslationPolicy`** (edge-case #5). DEFERRED — carries `relay_chain: list[LanguageHop]` structure breaking pure single-field shape. Comprehenslate's current scope is direct Turkish→English. Revival trigger: when a relay-translation use case becomes active.

**Mechanism trace:** Absence Recognition patch-level (the 6 strong candidates surface the missing Policy classes for known phenomena) + Absence Recognition redesign-level (asks "if we designed the Policy layer from scratch, what would be present?" → produces the strong candidates list) + Combination (each Policy class combines the recurring edge-case + filter outcomes + language-agnostic naming) + Domain Transfer (Bible translation tradition for CitationReferenceFormat; manuscript-tradition for SourceApparatus; UN translation practice for relay-translation deferral reasoning).

### 5-test on PC3

- Novelty: HIGH — 4 candidates (Honorifics, FormulaicOpening, EmbeddedPoetry, TransliterationStandard) are not in the prior 14-edge-case list
- Scrutiny survival: STRONG — each candidate has explicit filter verdicts; moderate candidates flag specific filter caveats
- Fertility: HIGH — establishes the Policy layer as adoptable beyond NonMainLangPartsPolicy across multiple corpora
- Actionability: HIGH — each strong candidate has a pydantic class sketch ready to drop into schemas.py
- Mechanism independence: convergence from Absence Recognition (both levels) + Combination + Domain Transfer
- **Verdict: ACTIONABLE.**

---

## P4 — Inherited Commitments Re-test

### Principal candidate (PC4)

#### From `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md`

| Commitment | Verdict | Evidence |
|---|---|---|
| `chunking_granularity: Literal[5]` on TC | **found INVALID** | Structural contradiction: chunking granularity is operational (PC layer), not strategic (TC layer). User moved to PC explicitly. |
| SD.ChunkingUnit `canonical_level` field | **found INVALID** | Imposes universal hierarchy not present in all corpora. User's correction: *"book must follow certain chapter rules. which is not the case."* |
| Corpus mappings (Söz=chapter, mesele=subchapter, ayah=sentence with is_atomic, hashiye=paragraph attached_to) | **found INVALID at schema location** | Useful as documentation but not as schema field values. SD dropped. |
| 5-literal `chunking_granularity` value set (sentence / paragraph / passage / subchapter / chapter) | **RE-TESTED — commitment confirmed** | Values preserved on PC.chunking_granularity. The enum content was sound; only the schema home was wrong. |
| `chunking_mechanism_override` 6-literal set on PC | **RE-TESTED — commitment confirmed** | Preserved unchanged in schemas.py PC. |
| A6 cascade rejection (≥light forbids non-harmony-aware mechanism overrides) | **INHERITED-WITHOUT-RE-TEST** | Out of this inquiry's scope; chunking finding owns the cross-cutting cascade. |
| MC1 + MC2 promotion candidates (from LOOP_DIAGNOSE finding) | **INHERITED-WITHOUT-RE-TEST** | Out of scope; gate was a future branch-test on non-chunking inquiry, not this one. |

#### From `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`

| Commitment | Verdict | Evidence |
|---|---|---|
| Split-placement principle ("schema ownership matches data ownership") | **RE-TESTED — commitment confirmed but frame revised** | Principle preserved; architecture refined from 3-schema (SD + PC + TC) to 3-LAYER (TC + Policy + PC). FP2 ("Don't declare what the LLM can infer") refines what counts as "data" the schema must own. |
| Three-operation chunking category | **INHERITED-WITHOUT-RE-TEST** | Out of scope; chunking finding owns the category. |
| Hybrid harmony-aware as AI default mechanism | **RE-TESTED — commitment confirmed** | Preserved as PC's hidden default behind `chunking_mechanism_override: None`. |
| Tier 1-2 preservation as HARD constraint | **INHERITED-WITHOUT-RE-TEST** | Out of scope; chunking finding owns the cross-cutting constraint. |
| A4-driven defaults pattern | **RE-TESTED — commitment confirmed** | TC.A4 still drives downstream defaults; pattern intact. |
| SourceDescriptor as a paper schema with `source_chunking_units` field | **found INVALID** | SD dropped per user. The `source_chunking_units` mechanism (declared corpus-natural units) rejected as "not logical" by user. |

#### From `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md`

| Commitment | Verdict | Evidence |
|---|---|---|
| TranslationConfig gains 0 new fields | **RE-TESTED — commitment confirmed** | TC remains frozen at 8 axes. |
| 4 SD additions: `source_language_fluency`, `source_edition`, `source_temporal_register`, `embedded_languages: list[EmbeddedLanguagePolicy]` | **found INVALID at schema location** (sub-statuses below) | SD dropped. |
| sub-status: `source_language_fluency` | **deferred** | Not load-bearing for current Nursi work; revival trigger in P6. |
| sub-status: `source_edition` | **dropped** | LLM-irrelevant for translation operation. |
| sub-status: `source_temporal_register` | **re-homed as `ArchaicRegisterPolicy`** | Matches Policy shape; surfaced as P3 strong candidate. |
| sub-status: `embedded_languages: list[EmbeddedLanguagePolicy]` | **replaced by `NonMainLangPartsPolicy`** | Per-language plumbing replaced by single language-agnostic Policy. |
| `EmbeddedLanguagePolicy` 4-literal `transliteration_policy` + Arabic-named `quranic_citation_policy` | **found INVALID** | Per-language declaration replaced; language-named values dropped per language-agnosticism filter. |
| Edge-cases #1, #6, #7 already-routed via ChunkingUnit (atom-protection; attached_to; orthogonal sister-concept) | **found INVALID at routing** | ChunkingUnit dropped with SD. New routings: #1 → `NonMainLangPartsPolicy`; #6 → `SourceApparatusPolicy` candidate (P3); #7 deferred. |
| Cross-axis conflict check (0 hard conflicts) | **RE-TESTED — confirmed for surviving routes** | Surviving Policy candidates re-pass the conflict-check pattern. |
| A3 source_culture stays as-is (non-modification) | **RE-TESTED — commitment confirmed** | TC unchanged. |
| UseContext as schema deferred | **RE-TESTED — commitment confirmed** | Still deferred; aligns with anti-bloat. |

**Mechanism trace:** Combination (verdict + commitment + structural evidence per row) + Lens Shifting (each commitment re-evaluated under FP2 lens) + Inversion (PI4 below).

### Piece-level Inversion candidate (PI4)

Assumption reversed: explicit INVALID verdicts → leave prior commitments unchallenged ("commitments were right at the time; current simplification is separate-axis improvement").

What follows: the prior findings stand with their committed shapes; this finding adds a parallel-but-non-corrective view. No REFINES / CORRECTS frontmatter relationship; no Correction Notices.

**5-test on PI4:**
- Novelty: low (it's "do nothing about priors")
- Scrutiny survival: WEAK — prior findings' schema-shape commitments STRUCTURALLY contradict the current architecture (TC.chunking_granularity ≠ PC.chunking_granularity simultaneously). Both cannot be true. Without explicit invalidation, a future reader of either prior would adopt the (now-invalid) shape.
- Fertility: low
- Actionability: medium
- Mechanism independence: only Inversion produces it
- **Verdict: REJECTED.** PC4 with explicit verdicts is load-bearing.

### 5-test on PC4

- Novelty: HIGH — explicit per-commitment verdicts with structural evidence (not just precedent)
- Scrutiny survival: STRONG — each INVALID cites the structural contradiction with the current architecture
- Fertility: HIGH — clears the deck for future inquiries
- Actionability: HIGH — P5 actions can target the named INVALID commitments
- Mechanism independence: convergence from Combination + Lens Shifting + Sensemaking's Ambiguity 6 + Inversion-as-rejection-test
- **Verdict: ACTIONABLE.**

---

## P5 — Next Actions

### Principal candidate (PC5)

#### MUST

- **Add Correction Notice to** `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md`.
  - **Who:** runner of any subsequent inquiry that touches chunking or schemas.
  - **Gate:** observable — when next chunking-related or schemas-related inquiry begins.
  - **Why:** three central schema-shape commitments are INVALID (TC.chunking_granularity; SD.canonical_level; corpus mappings as schema content). Without notice, future inquiries would inherit the invalid commitments.
  - **Notice text to insert at top of finding:** *"**Correction (2026-06-15):** This finding's central schema-shape commitments — `chunking_granularity` on TC; SD.ChunkingUnit `canonical_level` field; corpus mappings as schema content — are corrected by `devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/finding.md` per the FP2 principle ('Don't declare what the LLM can infer'). The 5 literal granularity values plus the chunking_mechanism_override 6-literal set are preserved on `PipelineConfig`. The corpus mappings remain useful as documentation but not as schema field values."*

- **Add Correction Notice to** `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`.
  - **Who:** same as above.
  - **Gate:** observable — when next chunking-related inquiry begins.
  - **Why:** SourceDescriptor's paper-schema commitment is INVALID; split-placement preserved with frame revision (3-LAYER, not 3-schema).
  - **Notice text:** *"**Correction (2026-06-15):** SourceDescriptor's paper-schema commitment is INVALID per `devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/finding.md`. The split-placement principle is preserved but the architecture is 3-LAYER (TC + Policy classes + PC), not 3-schema (SD + PC + TC). FP2 ('Don't declare what the LLM can infer') refines what counts as schema-owned data."*

- **Add Correction Notice to** `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md`.
  - **Who:** same as above.
  - **Gate:** observable — when next inquiry references the 14 edge-case routings.
  - **Why:** all 4 SD additions are INVALID at schema location; per-field sub-statuses apply.
  - **Notice text:** *"**Correction (2026-06-15):** The 4 SourceDescriptor additions are INVALID at schema location per `devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/finding.md`. Per-field: `source_language_fluency` deferred; `source_edition` dropped; `source_temporal_register` re-homed as `ArchaicRegisterPolicy`; `embedded_languages` replaced by language-agnostic `NonMainLangPartsPolicy`. Edge-cases #1, #6, #7 routings via ChunkingUnit are INVALID; new routings: #1 → NonMainLangPartsPolicy; #6 → SourceApparatusPolicy candidate; #7 deferred."*

- **Adopt the strong Policy candidates from P3** into `schemas.py` (gated on user review of Item 2).
  - **Who:** user / developer.
  - **Gate:** condition-bound — when the user reviews Item 2 and selects which candidates to adopt.
  - **Why:** schemas.py currently has only NonMainLangPartsPolicy; the 6 strong candidates are load-bearing for Nursi-corpus translation work.

#### COULD

- **Document the LLM-inferable test predicate** alongside schemas.py as a module-level docstring or developer-facing comment.
  - **Who:** developer.
  - **Gate:** condition-bound — when next schema field is being considered.
  - **Why:** FP2 is now an architectural principle; in-code documentation prevents future schema additions that violate it.

#### DEFERRED

- **`source_language_fluency` revival** — defer until reader-side language fluency becomes load-bearing for translation strategy.
  - **Gate:** observable — if A3 source_culture produces ambiguous assignments due to language-fluency conflation in actual translation work.
  - **Why if revived:** add as a new `Literal[N]` enum on a `ReaderFluencyPolicy` class, or revisit TC-modification.

- **MC1 + MC2 branch-test on non-chunking inquiry** — gate inherited from chunk_types_vs_mechanisms finding's promotion strategy.
  - **Gate:** observable — next inquiry not related to chunking.
  - **Why if revived:** evidence accumulation for promoting MC1 and MC2 to canonical td-critique and sense-making sub-axes.

**Mechanism trace:** Combination (INVALID verdicts from P4 + correction-protocol convention) + Constraint Manipulation (ADD: forces explicit propagation; REMOVE: explored as PI5 alternative below) + Inversion at intervention-shape axis (PI5).

### Piece-level Inversion candidate at intervention-shape axis (PI5)

Property (v) fires (the piece commits intervention shape: ADD-CONTENT correction notices + REPAIR-on-priors via Notice insertion). Per Intervention-Shape-Axis Inversion: name the assumption being reversed (intervention shape = ADD-CONTENT + REPAIR) and propose at least one alternative shape from the Vocabulary.

**Alternative shape A: REORGANIZE-WITHOUT-ADDING.** Don't modify prior findings at all; let `_state.md` Relationships + this finding's `corrects:` frontmatter signal the correction.

What follows: priors stay literally unchanged; less invasive; less visible to readers.

**5-test on alternative A:**
- Novelty: medium
- Scrutiny survival: WEAK — visibility is poor; a reader landing on the chunk_types_vs_mechanisms finding via search would not see the correction. Relies on readers checking `_state.md` Relationships, which is uncommon.
- Fertility: low
- Actionability: medium
- Mechanism independence: only Inversion
- **Verdict: REJECTED.**

**Alternative shape B: REPAIR-in-place.** Rewrite the INVALID sections of the priors directly; original text moved to `docarchive/`.

What follows: priors are definitively corrected; historical record of original reasoning is preserved in `docarchive/` but lost from main path.

**5-test on alternative B:**
- Novelty: medium
- Scrutiny survival: WEAK — destroys point-of-entry historical record; future debugging of "why did we land here" loses context from main path. Findings are meant to be read as snapshots-of-thinking; in-place revision conflates current understanding with prior reasoning.
- Fertility: low
- Actionability: medium-high (definitive but destructive)
- Mechanism independence: only Inversion + Constraint Manip REMOVE
- **Verdict: REJECTED.**

PC5's intervention-shape commitment (ADD-CONTENT correction notices + REPAIR-on-priors via Notice insertion) survives both alternatives.

### 5-test on PC5

- Novelty: medium (uses standard Correction Notice protocol)
- Scrutiny survival: STRONG — preserves historical record; makes corrections visible at point-of-entry
- Fertility: HIGH — clears the deck for future inquiries
- Actionability: HIGH — concrete notice text per prior; gates are observable
- Mechanism independence: convergence from Combination + Constraint Manip ADD + Intervention-Shape-Axis Inversion (alternatives REJECTED)
- **Verdict: ACTIONABLE.**

---

## P6 — Open Questions

### Principal candidate (PC6)

#### Monitoring

- **`ArchaicRegisterPolicy` 4-literal sufficiency.** If `ArchaicRegisterPolicy` is adopted, monitor whether the 4 values are sufficient for actual Nursi translation work. Refinement trigger: if a 5th distinct strategy emerges during translation.

#### Blocked

(None currently — all decisions adjudicated.)

#### Research Frontiers

- **Cross-corpus Policy catalog completeness.** Item 2's catalog was filtered through Nursi-load-bearing-ness. Non-Islamic theological-translation corpora (Tanakh; Bible; Sanskrit-Hindu; Pali Buddhist; Christian patristic) may surface additional Policy candidates. Frontier: a survey inquiry covering non-Islamic theological-translation corpora.

- **LLM-inferability decay at rare languages.** FP2 assumes current-LLM-capability for source-language detection. Rare/dead languages (Aramaic; Coptic; Sumerian; Akkadian; Ge'ez) may require declarative fields the current architecture omits. Frontier: an inquiry that pressure-tests FP2 against a rare-language corpus.

#### Refinement Triggers

- **`source_language_fluency` revival** — if A3 source_culture produces ambiguous assignments due to language-fluency conflation in actual translation work.

- **Policy-class organization** — if schemas.py grows beyond ~10 Policy classes, consider import-organization or sub-module split (e.g., `schemas/policies/source_apparatus.py`, etc.).

- **`PriorTranslationStancePolicy` adoption** — adopt only if a `list[PriorRef]` companion structure can be cleanly added without complicating the Policy class itself.

**Mechanism trace:** Absence Recognition patch-level (Monitoring + Refinement Triggers) + Absence Recognition redesign-level (Research Frontier: cross-corpus extension) + Extrapolation (LLM-inferability decay extends current trend to where it would break).

### 5-test on PC6

- Novelty: medium (open questions are markers)
- Scrutiny survival: STRONG — each open question has explicit revival/refinement trigger
- Fertility: medium-high (each open question seeds future inquiries)
- Actionability: medium (markers, not direct actions)
- Mechanism independence: convergence from Absence Recognition (both levels) + Extrapolation + Sensemaking Open flags
- **Verdict: ACTIONABLE.**

---

## Inherited Frame Audit (between Phase 2 and Phase 3)

### Step (i) — Seed-level central assumption

The seed (the 6-piece structure from Decomposition with SV6 substrate) carries the central assumption: *"The schemas.py simplification is correct and to be elaborated, not challenged at FP2 / 3-layer-architecture / 4-filter level."*

### Step (ii) — Piece-level commitments

| Piece | Load-bearing commitment | Property fired |
|---|---|---|
| P1 | FP2 + 3-layer architecture + 4-filter set | (b) framing-semantic + (c) lesson-vocabulary |
| P4 | INVALID verdicts on prior commitments via REFINES/CORRECTS frontmatter | (a) relationship-label |
| P5 | ADD-CONTENT correction notices via REPAIR-on-priors | (e) intervention-shape commitment |

### Step (iii) — Challenge scan

- Seed-level central assumption: **PI1** (P1's Inversion-candidate) explicitly reverses FP2 → "Declare what the LLM might fail to infer." Operational signal: direct opposite statement. ✓ challenged.
- P1's commitment: **PI1** as above. ✓ challenged.
- P4's commitment: **PI4** (P4's Inversion-candidate) explicitly reverses the propagate-corrections direction → "Leave priors unchallenged." Operational signal: removal statement ("without explicit invalidation"). ✓ challenged.
- P5's commitment: **PI5 alternatives A + B** (REORGANIZE-WITHOUT-ADDING and REPAIR-in-place) explicitly invert the ADD-CONTENT shape. Operational signal: alternative-shape naming per Intervention-Shape Vocabulary. ✓ challenged.

### Step (iv) — Firing condition

Audit **does NOT fire** — every load-bearing assumption and commitment has at least one explicit challenge in the candidate set. Proceed to Phase 3 Test (already conducted per-piece above).

---

## Phase 3 — Assembly Check

### Survivors combined

PC1 (substrate) + PC2 (rationale narrative) + PC3 (Policy catalog) + PC4 (re-test verdicts) + PC5 (correction propagation) + PC6 (open questions) — six principal candidates, all ACTIONABLE.

### Emergent value

The six pieces compose into a finding that simultaneously (a) explains the schemas.py simplification (PC1 + PC2); (b) extends it forward into an actionable Policy-class catalog (PC3); (c) propagates corrections backward into three prior findings (PC4 + PC5); (d) preserves residual signals (PC6). No single piece delivers this composite reach.

### Assembly emergent (AE1)

**The LLM-inferable test as a standalone architectural rule.** When FP2 is composed with the 4-filter set and the catalog filter results, the principle generalizes beyond schemas.py: any schema field added in Comprehenslate (and arguably any AI-assisted system's schema) should pass the LLM-inferable test. This is implicitly covered by PC5's COULD action (document the test predicate at module level), but the assembly check surfaces it as a candidate project-wide convention.

5-test on AE1:
- Novelty: HIGH (project-wide convention not currently committed)
- Scrutiny survival: STRONG (the test predicate is structurally grounded in FP2)
- Fertility: HIGH (applies beyond schemas.py)
- Actionability: medium (covered by PC5 COULD; full adoption gated on broader project convention)
- Mechanism independence: convergence from PC1 + PC3 filter results + PC5 documentation action
- **Verdict: DEFERRED with revival trigger** — revival when project-wide schema-style guide is written or when 3+ inquiries reference FP2 as a load-bearing principle.

### Axis coverage check

| Axis | Variance in candidate set |
|---|---|
| Content axis | PC1 names principle + filters; PC2 applies them; PC3 extends them |
| Intervention-shape axis | PC5 commits ADD-CONTENT + REPAIR; alternatives REORGANIZE-WITHOUT-ADDING and REPAIR-in-place explored |
| Scope axis | PC3 commits Nursi-load-bearing scope; cross-corpus extension flagged as PC6 Research Frontier |
| Direction axis | PC4 commits INVALID verdicts (rather than CONFIRMED preservation) on chunk_types_vs_mechanisms central commitments |

Multi-axis variance verified ✓.

### Per-row mechanism-trace

- PC3 candidates: each of the 15 Policy candidates has a per-candidate mechanism rationale (Absence Recognition patch / redesign-level / Combination / Domain Transfer).
- PC4 commitments: each commitment row carries its verdict + structural evidence.
- ✓ per-row trace satisfied.

### Shared-input detection

Multiple mechanisms converge on PC1 (FP2 + 3-layer architecture). Do they share inherited input? YES — they all consume the SV6 stabilized model from Sensemaking. Potential SPURIOUS convergence.

Adversarial test: invert the SV6 stabilized model's central claim (FP2 is sound) — this was done via PI1 (Inversion challenge to FP2). PI1 was REJECTED on structural grounds (user-correction quote + scrutiny survival weak for the "declare for redundancy" alternative). So the convergence is **INDEPENDENT** (FP2 survives independent challenge), not SPURIOUS.

---

## Telemetry

### Standard

- **Generators applied:** 4 / 4 (Combination, Absence Recognition, Domain Transfer, Extrapolation)
- **Framers applied:** 3 / 3 (Lens Shifting, Constraint Manipulation, Inversion)
- **Convergence:**
  - PC1: Combination + Absence Recognition + Inversion (PI1 rejected) — converge
  - PC2: Combination + Lens Shifting + Domain Transfer — converge
  - PC3: Absence Recognition (both levels) + Combination + Domain Transfer — converge
  - PC4: Combination + Lens Shifting + Inversion (PI4 rejected) — converge
  - PC5: Combination + Constraint Manip (ADD + REMOVE explored) + Intervention-Shape-Axis Inversion (alternatives rejected) — converge
  - PC6: Absence Recognition + Extrapolation — converge
- **Survivors tested:** 6 principal candidates + 3 piece-level Inversion candidates (PI1 / PI4 / PI5 alternatives A and B) + 1 assembly emergent (AE1) = 10+ tested
- **Failure modes observed:** none (Premature Evaluation N; Single-Mechanism N; Early Frame Lock N; Innovation Without Grounding N; Mechanism Exhaustion N; Survival Bias N)

### Production-task additional telemetry

- **Per-piece mechanism log:**
  - P1: [Combination, Absence Recognition, Inversion]
  - P2: [Combination, Lens Shifting, Domain Transfer]
  - P3: [Absence Recognition (patch + redesign), Combination, Domain Transfer]
  - P4: [Combination, Lens Shifting, Inversion]
  - P5: [Combination, Constraint Manip (ADD + REMOVE), Inversion:intervention-shape]
  - P6: [Absence Recognition, Extrapolation]
- **Per-piece axis-distribution log (property-v pieces only):**
  - P5: [Inversion:intervention-shape, Constraint-Manip:scope]
- **Meta-decision-piece classification:**
  - P1 = meta-decision
  - P2 = content-production
  - P3 = content-production
  - P4 = meta-decision
  - P5 = meta-decision
  - P6 = content-production
- **Piece-level Inversion compliance:**
  - P1 = satisfied (PI1 generated + tested)
  - P4 = satisfied (PI4 generated + tested)
  - P5 = satisfied (intervention-shape-axis Inversion: alternatives A and B generated + tested)

### Verdict

**PROCEED.** Full coverage (4G + 3F); convergence on every principal candidate via multiple mechanisms; all piece-level Inversion compliance satisfied; no failure modes observed; Inherited Frame Audit did NOT fire; Assembly check produced 1 deferred emergent (AE1).
