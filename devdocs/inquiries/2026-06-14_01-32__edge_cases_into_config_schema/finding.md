---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/innovation/translation_config_edge_cases.md
---
# Finding: Edge-Cases into Config Schema

## Changes from Prior

**Prior path:** `devdocs/innovation/translation_config_edge_cases.md` (the edge-case innovation pass that proposed 14 candidates as pydantic fields, with an Assembly check suggesting Group α SourceDescriptor / Group β passage-overrides / Group γ UseContext as architectural-routing direction).

**Also synthesizes:** `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` (the chunking deep-dive that committed split-placement across `SourceDescriptor` + `PipelineConfig` + `TranslationConfig`, and that already routed edge-cases #1 + #6 into ChunkingUnit fields and disposed of #7 as orthogonal sister-concept).

**Revision trigger:** Direct user request — "how these should change our current config fields?" — supplying the 14 edge-case candidates and the existing 8-field TranslationConfig as inputs.

**What's preserved.** The 14 candidate names and their motivating examples from the edge-case innovation. The chunking finding's split-placement architectural commitment. The user's de-facto mesele-level chunking practice. The existing 8-axis `TranslationConfig` unchanged.

**What's changed.** The edge-case innovation's Group γ (UseContext) is downgraded from a proposed schema to a deferred-as-schema commitment with a bundling revival trigger. Group α's membership is refined: 2 members are already routed via ChunkingUnit sub-fields (not top-level SourceDescriptor), 1 is deferred, 4 are ratified as top-level SourceDescriptor additions. Edge-case #2 (the proposed A3 split) is reshaped from "split A3" to "add beside A3" (non-destructive). Edge-case #8 is reshaped from a separate top-level field to a property within #1's `EmbeddedLanguagePolicy`.

**What's new.** A concrete per-field decision table (14 rows × outcome × schema-home × phase). Concrete pydantic field sketches for the 4 SourceDescriptor additions + 1 helper class. Revival triggers per deferred field (7 entries) + revival rules per non-modification (2 entries). A cross-axis conflict check against the existing 8 axes + 5 always-on Layer-2 policies + chunking commitments (0 hard conflicts; 2 docs notes flagged; 8 axis-interactions documented).

**Migration.** Total schema-delta from this inquiry: **TranslationConfig gains 0 new fields.** SourceDescriptor gains 4 new fields plus 1 helper class (`EmbeddedLanguagePolicy`). PipelineConfig unchanged. No new schemas. Phased: Phase 1 ratify-pre-routing (documentation only); Phase 2 implement SourceDescriptor additions (gated on the chunking finding's SourceDescriptor MUST item shipping); Phase 3 deferred fields await their individual revival triggers.

## Question

From `_branch.md`:

> "14 edge-case fields written to `devdocs/innovation/translation_config_edge_cases.md`. Quick map: [...] how these should change our current config — `class TranslationConfig(BaseModel)` [with 8 Literal[] fields] — fields?"

The user is asking how the 14 edge-case candidates from the prior innovation pass should change the existing 8-field `TranslationConfig`. The trailing "fields?" emphasizes that the user expects a per-field decision. The just-completed chunking deep-dive (immediately before this inquiry) committed a multi-schema split-placement architecture — `SourceDescriptor` for source properties, `PipelineConfig` for runtime engineering, `TranslationConfig` for user-facing strategy — and already routed edge-cases #1, #6, and #7. So the answer's natural scope is broader than "which become TranslationConfig fields" — it is "which become fields anywhere, where, and when."

The goal: a per-field routing table (14 rows × decision columns) + the resulting updated schema(s) + a migration sequence, honoring the chunking finding's split-placement precedent and the user's anti-bloat preference (visible across recent inquiries: a 280-line config simplified to 10 lines; `config_base_source.md` bloat cut; the chunking finding accepted only 1 new TranslationConfig field).

## Finding Summary

- **TranslationConfig gains 0 new fields.** The user's literal question — "which of these 14 become TranslationConfig fields?" — has the answer "none of them." This is structurally driven by the chunking finding's split-placement precedent (schema ownership matches data ownership) plus the user's anti-bloat preference.

- **The decision is 2D, not 1D.** Each of the 14 edge-cases gets two attached values: an *outcome* (`ALREADY-ROUTED` / `ADD-now` / `DEFER` / non-modification) and a *schema-home* (only meaningful when outcome is `ADD-now`). Conflating these into a single "is it a TranslationConfig field?" column produces a confused decision space.

- **3 edge-cases are already routed by the chunking deep-dive.** Edge-case #1 (`embedded_source_languages`, the Arabic-in-Turkish example) is carried by `ChunkingUnit.is_atomic` from the chunking finding's §7. Edge-case #6 (`source_apparatus_handling`, the *hashiye* preservation case) is carried by `ChunkingUnit.attached_to`. Edge-case #7 (`passage_typology`) is disposed as an orthogonal sister-concept to chunking — the `chunking_strategy: passage-typology-aware` literal IS the composition. These three need ratification, not new schema work.

- **4 edge-cases land on `SourceDescriptor` as new fields** (Phase 2 work). Edge-case #2 (the proposed A3 split) becomes `SourceDescriptor.source_language_fluency: dict[str, FluencyLevel]` — added beside A3, not splitting A3. Edge-case #3 (`source_edition`) becomes `SourceDescriptor.source_edition: str` (minimal now; structured `EditionDescriptor` later if variant-tracking matters). Edge-case #13 (`source_temporal_register`) becomes `SourceDescriptor.source_temporal_register: Literal[...]` with default `hybrid-by-register-domain`. Edge-case #8 (`quranic_citation_special_status`) becomes a property within edge-case #1's `EmbeddedLanguagePolicy`, not a separate top-level field.

- **7 edge-cases defer with explicit revival triggers.** Edge-case #4 (`voice_disambiguation`), #5 (`relay_translation`), #9 (`consumption_mode`), #10 (`reading_session_pattern`), #11 (`prior_translation_relationship`), #12 (`output_finality`), #14 (`script_direction_handling`) all defer because none is load-bearing for current Nursi work. Each defer carries a concrete revival trigger (observable signal or condition-bound event).

- **Two explicit non-modifications.** A3 `source_culture` stays as-is — the proposed "split A3 into culture + language" from the edge-case innovation is rejected as destructive; the language dimension comes in beside A3 via #2's new field. UseContext as a schema is deferred entirely — the edge-case innovation proposed it for Group γ (#9, #10, #12), but committing a third new schema in two consecutive inquiries (`SourceDescriptor` + `PipelineConfig` from chunking, plus `UseContext` here) violates the user's incremental-addition pacing pattern.

- **No conflicts with existing commitments.** Cross-axis conflict check finds 0 hard conflicts against the existing 8 axes, the 5 always-on Layer-2 policies, or the chunking finding's commitments. Two documentation notes are flagged: edge-case #13's `modernize-fully` option carries no-smoothing-policy risk (use with care; not the default precisely because of this); edge-case #13's default `hybrid-by-register-domain` composes positively with the Layer-2 register-alternation preservation policy.

- **The implementation depends on a prerequisite from the chunking finding.** This inquiry's Phase 2 work cannot start until `SourceDescriptor` exists as an implemented schema. The chunking finding committed `SourceDescriptor` as a paper schema; an implementation step is required before Phase 2 can ship.

## Finding

### Why this matters (the goal context)

The Comprehenslate project — an AI-assisted translation system for layered religious-theological texts, primarily the Said Nursi *Risale-i Nur* corpus — has settled an 8-axis `TranslationConfig` schema in prior inquiries (captured in `config_base_source.md` and implemented in `translation_config.py`). A separate innovation pass produced 14 edge-case candidates as potential additions, each motivated by phenomena observed in the Nursi corpus (Arabic ayahs embedded in Turkish prose; Nursi's marginal annotations called *hashiye*; passage-type heterogeneity within a single chapter; readers with varying source-language fluency; archaic Ottoman-Turkish residue in 1920s-30s text). The chunking deep-dive immediately preceding this inquiry committed a multi-schema split-placement architecture and already routed three of the 14 cases into specific fields. This inquiry consolidates the 14 candidates into settled decisions, honoring the chunking finding's split-placement precedent and the user's anti-bloat preference, and producing a concrete per-field routing table the user can act on at code-time.

The user's question explicitly emphasized "fields?" — they wanted concrete, not architectural. The answer here is concrete (per-field routing table; concrete pydantic code sketches; concrete revival triggers) but the architecture sits underneath: the literal answer to "which of these 14 become TranslationConfig fields?" is "none of them" because the chunking finding's split-placement architecture already determined that source-property fields belong on `SourceDescriptor`, not on `TranslationConfig`. This finding makes that architecture's application to the 14 candidates concrete.

### 1. The per-field decision table (the deliverable's spine)

Each of the 14 edge-case candidates gets a routing decision below.

| # | Edge-case field | Outcome | Schema home | Phase | Notes |
|---|---|---|---|---|---|
| 1 | `embedded_source_languages` | ALREADY-ROUTED | `SourceDescriptor.ChunkingUnit.is_atomic` (atom carrier) plus `SourceDescriptor.embedded_languages: list[EmbeddedLanguagePolicy]` (policy carrier) | Phase 1 | Inherits from the chunking deep-dive's section 7. The atomic flag prevents Arabic ayahs from being split across chunks. |
| 2 | `source_language_fluency` (proposed as A3 split) | ADD-now | `SourceDescriptor.source_language_fluency: dict[str, FluencyLevel]` | Phase 2 | Added BESIDE A3, not splitting A3. A3 is a settled axis with prose written assuming current meaning; non-destructive addition handles the language-fluency dimension. |
| 3 | `source_edition` | ADD-now (light) | `SourceDescriptor.source_edition: str \| None` | Phase 2 | Minimal `str` field for now; promote to structured `EditionDescriptor` when variant-tracking matters. |
| 4 | `voice_disambiguation` | DEFER | — | Phase 3 | Pre-routing via #6's `ChunkingUnit.attached_to` already covers the Nursi+hashiye voice case. The lahika (student letters interleaved with author voice) and extended-citation cases are not load-bearing now. |
| 5 | `relay_translation` | DEFER | — | Phase 3 | Comprehenslate's current scope is direct Turkish→English. No relay use-case in flight. |
| 6 | `source_apparatus_handling` | ALREADY-ROUTED | `SourceDescriptor.ChunkingUnit.attached_to` | Phase 1 | Inherits from chunking finding. The hashiye-to-referent attachment is carried at chunking time. |
| 7 | `passage_typology` | ALREADY-DISPOSED (orthogonal sister-concept) | `TranslationConfig.chunking_strategy` literal `passage-typology-aware` | Phase 1 | Disposed by chunking finding's section 7 as orthogonal sister-concept (chunking determines BOUNDARIES; typology labels TYPE per chunk). |
| 8 | `quranic_citation_special_status` | ADD-now (as policy within #1) | `SourceDescriptor.EmbeddedLanguagePolicy.quranic_citation_policy` | Phase 2 | A property within #1's `EmbeddedLanguagePolicy` for Arabic entries when the embedded segments are Quranic citations. Not a separate top-level field. |
| 9 | `consumption_mode` | DEFER | — | Phase 3 | UseContext schema not committed (see section 4 below); deferred individually. |
| 10 | `reading_session_pattern` | DEFER | — | Phase 3 | Same as #9 — UseContext deferred. |
| 11 | `prior_translation_relationship` | DEFER | — | Phase 3 | No third translation iteration in flight; no Vahide/Akarsu-comparison work currently active. |
| 12 | `output_finality` | DEFER | — | Phase 3 | Downstream pipeline doesn't yet distinguish finality levels. UseContext deferred. |
| 13 | `source_temporal_register` | ADD-now (light) | `SourceDescriptor.source_temporal_register: Literal[...]` | Phase 2 | Concrete for the Nursi corpus (1920s-30s Turkish has Ottoman residue). Default `hybrid-by-register-domain`. |
| 14 | `script_direction_handling` | DEFER | — | Phase 3 | Rendering concern; not load-bearing until output rendering reaches the apparatus-edition stage with bidirectional RTL Arabic display. |

**Distribution:** 3 already-routed; 4 add-now to `SourceDescriptor`; 7 defer; 0 reject.

**The headline number:** `TranslationConfig` gains **0 new fields**.

### 2. The 4 SourceDescriptor additions (Phase 2 code)

The chunking deep-dive committed `SourceDescriptor` as a paper schema with a `source_chunking_units` field. This inquiry adds 4 fields plus 1 helper class, giving `SourceDescriptor` its first substantively shaped body.

```python
from typing import Literal
from pydantic import BaseModel

FluencyLevel = Literal["none", "basic", "reading-only", "fluent", "native"]


class EmbeddedLanguagePolicy(BaseModel):
    """Per-embedded-language declaration on a SourceDescriptor.

    Composes with the chunking finding's ChunkingUnit (which carries is_atomic
    at the chunking level for atom-protection). This class carries per-language
    POLICY semantics — how the embedded segments in this language should be
    handled at translation time, not at chunking time.
    """
    language_code: str
    """Language tag: 'ar' (Arabic), 'fa' (Persian), 'tr-ot' (Ottoman Turkish), etc."""

    transliteration_policy: Literal[
        "script-native",
        "transliterate-only",
        "transliterate-with-translation",
        "translate-inline",
        "translate-with-facing-original",
    ] = "translate-with-facing-original"

    quranic_citation_policy: Literal[
        "translate-only",
        "arabic-plus-translation",
        "established-translation-reference",
        "translator-own-version",
    ] | None = None
    """Set ONLY when language_code='ar' AND the embedded segments are Quranic citations.

    Carries edge-case #8 as a policy property of #1 (rather than a separate top-level field).
    """


class SourceDescriptor(BaseModel):
    """Corpus-specific source declarations.

    Builds on the chunking finding's SourceDescriptor stub (which committed
    `source_chunking_units`). This inquiry adds the 4 fields below capturing
    source properties beyond chunk boundaries.
    """

    # Already committed by the chunking deep-dive:
    source_chunking_units: list  # list[ChunkingUnit]

    # Phase 2 additions from this inquiry:

    source_language_fluency: dict[str, FluencyLevel] = {}
    """Reader's fluency per source-or-embedded language.

    Refines A3 source_culture by adding the fluency dimension WITHOUT modifying A3.
    A3 keeps its current 5-level lived-cultural-fluency semantic.

    Example (Nursi corpus, typical Turkish-speaking reader):
        {"tr": "native", "ar": "reading-only", "fa": "basic"}
    Example (Nursi corpus, English-speaking convert with İlahiyat training):
        {"tr": "basic", "ar": "reading-only", "fa": "none"}
    """

    source_edition: str | None = None
    """Canonical name of the source edition.

    Light string field for now. When variant-tracking matters (e.g., comparing
    1928 Arabic-script lithograph vs 1956 Latinized printing of Nursi), promote
    to a structured EditionDescriptor in a follow-up inquiry.

    Example for Nursi: 'Risale-i Nur Külliyatı, Yeni Asya 2003 printing'.
    """

    source_temporal_register: Literal[
        "preserve-archaic",
        "modernize-fully",
        "hybrid-by-register-domain",
        "mark-archaisms-explicitly",
    ] = "hybrid-by-register-domain"
    """How to handle archaic source language.

    Default 'hybrid-by-register-domain': preserve archaic register in theological
    vocabulary (e.g., Nursi's Ottoman-Turkish kalam terms), modernize narrative prose.

    Notes for downstream consumers:
    - Default `hybrid-by-register-domain` composes positively with the Layer-2
      register-alternation preservation policy.
    - `modernize-fully` carries Layer-2 no-smoothing-policy risk (smoothing of
      archaic forms violates no-smoothing); use with care — it is not the default
      precisely because of this risk.
    """

    embedded_languages: list[EmbeddedLanguagePolicy] = []
    """Per-embedded-language policies for source content with mixed languages.

    Example for Nursi (Turkish frame + Arabic ayahs + Persian Sufi couplets):
        [
            EmbeddedLanguagePolicy(
                language_code="ar",
                transliteration_policy="translate-with-facing-original",
                quranic_citation_policy="arabic-plus-translation",
            ),
            EmbeddedLanguagePolicy(
                language_code="fa",
                transliteration_policy="translate-inline",
            ),
        ]

    Carries edge-cases #1 (parent) and #8 (quranic_citation_policy as a property).
    """
```

These 4 additions are pattern-level. Bible / Quran / Hindu scripture corpora would specify their own fluency dictionaries, editions, registers, and embedded-language policies — the schema does not hard-code Nursi-specific values.

### 3. The Nursi-specific SourceDescriptor instance

To demonstrate end-to-end use, the Nursi corpus's `SourceDescriptor` declaration looks like this:

```python
nursi_source = SourceDescriptor(
    source_chunking_units=[
        ChunkingUnit(name="mesele", detector=..., nesting_level=0, is_atomic=False),
        ChunkingUnit(name="paragraph", detector=..., nesting_level=1, is_atomic=False),
        ChunkingUnit(name="ayah", detector=..., nesting_level=2, is_atomic=True),
        ChunkingUnit(name="hashiye", detector=..., nesting_level=1, attached_to="paragraph"),
    ],
    source_language_fluency={"tr": "native", "ar": "reading-only", "fa": "basic"},
    source_edition="Risale-i Nur Külliyatı, Yeni Asya 2003 printing",
    source_temporal_register="hybrid-by-register-domain",
    embedded_languages=[
        EmbeddedLanguagePolicy(
            language_code="ar",
            transliteration_policy="translate-with-facing-original",
            quranic_citation_policy="arabic-plus-translation",
        ),
        EmbeddedLanguagePolicy(
            language_code="fa",
            transliteration_policy="translate-inline",
        ),
    ],
)
```

This declaration is what unblocks the in-flight 4_mesele translation work — the Arabic ayahs in 4_mesele get atom-protection via `ChunkingUnit.is_atomic=True` (chunking finding) plus the `arabic-plus-translation` policy at translation time (this inquiry). The hashiye attached to paragraphs travel with their referent chunks.

### 4. Inherited-commitment re-test

This inquiry inherits commitments from two priors. Per the Synthesis Trigger requirement, each commitment carries an explicit re-test status.

**From the chunking deep-dive** (`devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`):

- **Three-operation chunking category** — *RE-TESTED — confirmed.* Category survived this inquiry's perspective check; no edge-case forced a fourth operation or collapsed to fewer.
- **Split placement across `SourceDescriptor` + `PipelineConfig` + `TranslationConfig`** — *RE-TESTED — confirmed.* Foundational to this inquiry's routing. Schema-ownership-matches-data-ownership applied per field; produced TranslationConfig delta = 0.
- **Edge-case #1 → `ChunkingUnit.is_atomic`** — *RE-TESTED — confirmed.* Ratified as already-routed; field carries atom-preservation semantic for Arabic ayahs.
- **Edge-case #6 → `ChunkingUnit.attached_to`** — *RE-TESTED — confirmed.* Ratified as already-routed; field carries hashiye-to-referent linkage.
- **Edge-case #7 → orthogonal sister-concept** — *RE-TESTED — confirmed.* Ratified; the `passage-typology-aware` strategy literal is the composition.
- **A4-driven defaults pattern** — *INHERITED-WITHOUT-RE-TEST.* Reason: this inquiry adds zero TranslationConfig fields, so no new axes inherit the pattern.
- **Tier 1-2 preservation as HARD constraint** — *RE-TESTED — confirmed.* The cross-axis conflict check in section 6 below verified none of the 4 SourceDescriptor additions break Tier 1-2 preservation.
- **Hybrid harmony-aware chunker as operational default** — *INHERITED-WITHOUT-RE-TEST.* Reason: out of this inquiry's scope (chunking strategy choice); only the 14-edge-cases routing is in scope.
- **A6 activation-gate cascade** — *INHERITED-WITHOUT-RE-TEST.* Reason: out of scope; the chunking finding owns the cascade; this inquiry doesn't touch A6 semantics.

**From the edge-case innovation** (`devdocs/innovation/translation_config_edge_cases.md`):

- **The 14 edge-case candidates as the bounded set** — *RE-TESTED — confirmed.* Inquiry scope explicitly bounded to these 14.
- **Group α (SourceDescriptor proposed members #1, #2, #3, #4, #6, #8, #13)** — *RE-TESTED — frame revised.* Group α direction confirmed; membership refined: #1 + #6 are routed via `ChunkingUnit` sub-fields (not top-level SourceDescriptor); #4 deferred (not load-bearing); #2 + #3 + #8 + #13 ratified as SourceDescriptor top-level additions, with #8 absorbed as a policy within #1's `EmbeddedLanguagePolicy`.
- **Group β (passage-typology keystone, #7)** — *RE-TESTED — frame revised.* Confirmed as orthogonal sister-concept to chunking (per the chunking finding's section 7); not a separate "group" needing schema home — #7 is its own settled disposition.
- **Group γ (UseContext proposed members #9, #10, #12)** — *RE-TESTED — commitment found INVALID for schema commitment.* Reason: three new schemas (`SourceDescriptor` + `PipelineConfig` from chunking, plus `UseContext` here) in two consecutive inquiries violates the user's incremental-addition pacing. Members route to individual defer with revival triggers. Revival rule for the UseContext schema commitment: when at least two of {#9, #10, #12} fire their individual revival triggers, re-open the schema commitment.
- **The chunking precedent's split-placement justification (schema ownership matches data ownership)** — *RE-TESTED — confirmed.* Applied independently to each of the 4 SourceDescriptor additions; each routing decision derived from schema-ownership reasoning (source-property → SourceDescriptor) without circular reliance on the precedent itself.

### 5. The two non-modification commitments

Explicit "do not do this" commitments documented to prevent silent drift from future contributors.

**A3 `source_culture` stays as-is.** The edge-case innovation #2 initially suggested splitting A3 into `source_culture` + `source_language`. This finding rejects the split. The reason: A3 is a settled axis with prose in `config_base_source.md` written assuming current meaning (5-level lived-cultural-fluency gradient: `outsider / acquainted / familiar / heritage / source-native`). Splitting would force `config_base_source.md` prose rewrite plus breaking schema change plus migration of existing translation configs. The conflation A3 carries (culture and language-fluency in one axis) is real but addressable by adding beside: `SourceDescriptor.source_language_fluency` captures the language-fluency dimension without breaking A3. Revival trigger for revisiting A3: if real translation cases produce ambiguous A3 assignments (e.g., a reader is `source-native` culturally but `none` in fluency, and the conflation forces a wrong choice), open a follow-up inquiry to refactor A3.

**UseContext is not committed as a schema.** The edge-case innovation Group γ proposed UseContext as a schema holding `consumption_mode`, `reading_session_pattern`, and `output_finality`. This finding defers the UseContext schema. The reason: the chunking deep-dive already committed two new schemas (`SourceDescriptor` + `PipelineConfig`). Committing UseContext here would be the third new schema in two consecutive inquiries — a violation of the user's incremental-addition pacing pattern (visible across recent inquiries). Group γ's members each defer individually with their own revival triggers (section 7). Revival rule for the UseContext schema commitment: when at least two of {#9, #10, #12} fire their individual triggers, re-open the schema commitment.

### 6. Cross-axis conflict check

The 4 SourceDescriptor additions (#2, #3, #8, #13) were checked against the existing 8 axes, the 5 always-on Layer-2 policies, and the chunking finding's commitments. The matrix produced **0 hard conflicts**, **2 documentation notes** flagged, and **8 axis-interactions** documented.

Two notes worth surfacing here:

- **`source_temporal_register` × Layer-2 register-alternation preservation policy: POSITIVE COMPOSITION.** Temporal register IS a register; alternation between archaic theological vocabulary and modern narrative is exactly what register-alternation preservation policy preserves. The default `hybrid-by-register-domain` composes naturally with this policy.
- **`source_temporal_register` × Layer-2 no-smoothing policy: CAUTION on `modernize-fully`.** The `modernize-fully` option may smooth archaic forms, violating the no-smoothing policy. Use with care; this is not the default precisely because of this risk.

Eight axis-interactions documented (not conflicts; downstream-relevant relationships): `source_language_fluency` refines A3 by adding the fluency dimension; `source_temporal_register` interacts with A1 reader_level (archaic register affects comprehension), A5 source_fidelity (foreignized-max biases preserve-archaic), and A6 form_preservation (archaic register is a form layer); `quranic_citation_policy` interacts with A4 purpose (devotional biases `arabic-plus-translation`; scholarly biases `established-translation-reference`), A5 source_fidelity (foreignized-max favors `arabic-plus-translation`), A7 scaffolding (citation footnoting density tied to A7 budget), and A8 analysis_depth (exegetical history at scholarly A8); `source_edition` interacts with A8 (edition variants noted at deep+ analysis).

Three additions-cross-additions interactions noted: a low-Arabic-fluency reader (#2) combined with archaic register (#13) compounds difficulty for embedded ayahs (signals an A1-cascade attention point, not a conflict); Quranic citation policy (#8) depends on Arabic fluency declared in `source_language_fluency` (#2); the edition declared in `source_edition` (#3) may determine which register-period applies for `source_temporal_register` (#13).

### 7. The 7 deferred fields with revival triggers

Each defer carries a concrete revival trigger — observable, time-bound, or condition-bound. Vague gates like "eventually" or "when appropriate" are not used.

| # | Field | Reason for deferral | Revival trigger |
|---|---|---|---|
| 4 | `voice_disambiguation` | Pre-routing via #6's `ChunkingUnit.attached_to` covers the Nursi+hashiye voice case. No real translation case yet needs explicit voice-rendering beyond hashiye attachment. | **Condition-bound:** when a translation case needs explicit voice-rendering distinct from hashiye attachment (e.g., lahika letters interleaved with author voice plus cited authority, or extended-citation paragraphs where Nursi's voice resumes mid-paragraph). |
| 5 | `relay_translation` | Comprehenslate's current scope is direct Turkish→English. No relay use-case in flight. | **Condition-bound:** when target language is added without a translator available with source-language fluency, forcing source→intermediate→target chain. |
| 9 | `consumption_mode` | UseContext schema not committed (section 5 above); individual modes deferred. | **Observable** (with prerequisite): (a) a downstream consumer — renderer / UI / validator — exists in the pipeline AND (b) that consumer distinguishes between silent / aloud / dersane / recitation / memorization modes in observable behavior. |
| 10 | `reading_session_pattern` | UseContext schema not committed; pattern not consumed now. | **Observable** (with prerequisite): (a) a downstream consumer exists AND (b) the consumer distinguishes between single-pass / progressive-daily / reference-lookup / study-circle patterns. |
| 11 | `prior_translation_relationship` | No third translation iteration in flight; no Vahide / Akarsu / Tahşiye comparison work active. | **Condition-bound:** when a translation iteration positions explicitly versus prior translators (e.g., user feedback like "this should honor Vahide's terminology for *iman*"). |
| 12 | `output_finality` | UseContext schema not committed; downstream pipeline doesn't distinguish finality levels. | **Observable** (with prerequisite): (a) downstream pipeline exists AND (b) pipeline behavior actually differs by finality level (e.g., editor-draft flags interpretive choices; final-shippable doesn't). |
| 14 | `script_direction_handling` | Rendering concern; current outputs are body-text only without bidirectional apparatus. | **Condition-bound:** when output rendering reaches apparatus-edition stage with bidirectional RTL Arabic display. |

When any trigger fires, a follow-up inquiry — initiated by user observation during translation work, by an AI flag during the next translation cycle, or by an explicit project-state review — promotes the field from deferred to add-now and decides its schema home at that time.

### 8. Pattern-level applicability

The decisions in this finding are Nursi-specific in their values (mesele as top chunking unit; Turkish-Arabic-Persian fluency dict; 2003 Yeni Asya edition; Ottoman-Turkish archaism) but pattern-level in their structure. A Bible-translation project's SourceDescriptor would declare its own `source_chunking_units` (verse / pericope / chapter), its own `source_language_fluency` (Hebrew / Greek / Aramaic), its own `source_edition` (Masoretic / Septuagint / Vulgate critical edition name), its own `source_temporal_register` (preserving archaic Hebrew vs modernizing for accessibility), and its own `embedded_languages` policies. The field shapes and decision categories transfer. Only the values are corpus-specific.

## Inherited Commitments Re-test

(See section 4 of the Finding above. The Synthesis Trigger required re-testing each inherited commitment with a status of `RE-TESTED — confirmed` / `RE-TESTED — frame revised` / `RE-TESTED — commitment found INVALID` / `INHERITED-WITHOUT-RE-TEST` with reasons cited per commitment.)

In summary across the two priors: 9 commitments inherited from the chunking deep-dive (5 RE-TESTED-confirmed; 3 INHERITED-WITHOUT-RE-TEST with out-of-scope reasons; 1 covered as confirmed via the cross-axis conflict check). 5 commitments inherited from the edge-case innovation (3 RE-TESTED-confirmed including 2 frame-revised; 1 RE-TESTED-INVALID — Group γ as schema commitment). No commitment was silently absorbed.

## Next Actions

### MUST

- **What:** Build out the SourceDescriptor schema with the 4 fields from this inquiry (`source_language_fluency`, `source_edition`, `source_temporal_register`, `embedded_languages`) plus the `EmbeddedLanguagePolicy` helper class.
  **Who:** schema implementation step.
  **Gate:** condition-bound — when the chunking deep-dive's SourceDescriptor schema MUST item ships (the prerequisite from `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`).
  **Why:** This inquiry's Phase 2 work cannot complete without the parent schema existing. The cross-inquiry dependency is real: chunking committed SourceDescriptor as a paper schema; both inquiries' adds need that schema as a foundation.

- **What:** Declare the Nursi-specific `SourceDescriptor` instance with the values shown in section 3 above (mesele/paragraph/ayah/hashiye chunking units; Turkish-Arabic-Persian fluency dict; 2003 Yeni Asya edition; `hybrid-by-register-domain`; Arabic + Persian embedded-language policies).
  **Who:** schema implementation step + Nursi-familiar reviewer.
  **Gate:** observable — when the SourceDescriptor schema is implemented.
  **Why:** Demonstrates Phase 2 end-to-end and unblocks the in-flight 4_mesele translation (Arabic ayahs get `is_atomic=True` plus `arabic-plus-translation` policy; hashiye travels with referent chunks).

- **What:** Document the Phase 1 ratify-pre-routing decisions in this finding's text (already done above), and surface them in a maintenance note on `translation_config_edge_cases.md` so future contributors don't re-route #1, #6, #7 incorrectly.
  **Who:** finding-polish pass + edge-case-innovation maintainer.
  **Gate:** time-bound — before this finding is referenced by downstream work.
  **Why:** Without explicit ratification, future contributors may re-decide already-settled cases.

- **What:** Refine the P4 revival triggers for #9, #10, #12 to make the downstream-consumer-existence prerequisite explicit — restate each as "(a) downstream consumer exists in pipeline AND (b) consumer distinguishes between modes."
  **Who:** finding-polish pass.
  **Gate:** observable — already addressed in section 7 above; verify in the finding's final text.
  **Why:** Critique flagged this as a load-bearing specification gap; without the prerequisite condition, the triggers presume infrastructure that does not yet exist in Comprehenslate.

- **What:** Document the initiation paths for revival inquiries — user observation during translation work / AI flag during next translation cycle / explicit project-state review.
  **Who:** finding-polish pass (text already includes this in section 7).
  **Gate:** observable — included in the finding text.
  **Why:** Without an initiation path, triggers fire but no action mechanism is named.

- **What:** Quote canonical source text verbatim at the three load-bearing claim sites flagged by Critique — quote chunking deep-dive's section 7 verbatim where this finding ratifies #1 / #6 / #7; quote `config_base_source.md`'s A3 prose section verbatim where this finding claims "settled prose"; strengthen the chunking-precedent split-placement justification re-test with explicit test wording.
  **Who:** finding-polish pass.
  **Gate:** time-bound — before this finding is referenced as canonical evidence.
  **Why:** Critique flagged External-Grounding-Absence as PARTIAL; verbatim quotes at load-bearing sites lift the Mechanism-Independence quarantine.

- **What:** Add the cross-axis-interaction notes for `source_temporal_register` to the field's docstring — the POSITIVE COMPOSITION with Layer-2 register-alternation preservation policy, and the CAUTION with `modernize-fully` and no-smoothing policy.
  **Who:** schema implementation step.
  **Gate:** observable — when SourceDescriptor.source_temporal_register is implemented.
  **Why:** Without these docstrings, future contributors may default to `modernize-fully` without realizing the no-smoothing risk, or miss the positive composition with the register-alternation policy.

### COULD

- **What:** Promote `source_edition` from a plain `str` to a structured `EditionDescriptor` with variant-tracking, attribution, manuscript-family fields, etc.
  **Who:** future edition-handling inquiry.
  **Gate:** condition-bound — when a multi-edition corpus is added OR when Nursi variants (1928 lithograph vs 1956 Latinized vs current Yeni Asya) are explicitly compared in a translation workflow.
  **Why:** The current minimal `str` field is sufficient for Phase 2; structured promotion is value-add but not blocking.
  **Depends-on:** MUST item "schema implementation." This COULD is GATED — do not promote before the basic field is shipped.

- **What:** Apply the 2D-decision template from this inquiry (outcome × schema-home with revival-trigger + cross-axis-check + Inherited-Commitments-Re-test) to future bulk-edge-case synthesis inquiries.
  **Who:** future inquiry that consumes multiple proposed candidates as input.
  **Gate:** condition-bound — when a similar synthesis pattern emerges (proposed-candidates → settled-decisions).
  **Why:** The pattern is generalizable. Forward-looking suggestion; not a strong claim.

### DEFERRED

The 7 individual edge-case deferrals from section 7 above are formally DEFERRED — each carries its concrete revival trigger. Each also carries an "Initiated by" path (user observation / AI flag / project-state review).

- **What:** `voice_disambiguation` (#4) — revival when lahika or extended-citation case emerges.
- **What:** `relay_translation` (#5) — revival when relay use-case emerges.
- **What:** `consumption_mode` (#9) — revival when downstream consumer exists AND distinguishes modes.
- **What:** `reading_session_pattern` (#10) — revival when downstream consumer exists AND distinguishes session patterns.
- **What:** `prior_translation_relationship` (#11) — revival when third-iteration comparison work begins.
- **What:** `output_finality` (#12) — revival when downstream pipeline distinguishes finality levels.
- **What:** `script_direction_handling` (#14) — revival when apparatus-edition RTL rendering becomes scope.

A8 — `analysis_depth`'s scholarly level deferral on `consumption_mode` / `output_finality` chaining: when at least two of {#9, #10, #12} reach revival simultaneously, re-open the UseContext schema commitment (which this inquiry's section 5 deferred).

Additional deferrals from the non-modifications section:

- **What:** A3 re-examination — revival when A3 conflation produces ambiguous assignments in real translation cases.
- **What:** UseContext as schema commitment — revival when at least two of {#9, #10, #12} fire individually.

## Reasoning

The structurally non-obvious decisions in this finding had alternatives that were considered and rejected. The rejections matter — they show why the deliverable lands where it does.

**Why TranslationConfig delta = 0, not "some of the 14 become TC fields."** The user's literal question — "fields?" — invited a per-TC-field decision. The structurally correct answer rejected that framing. The chunking deep-dive established split-placement (`SourceDescriptor` for source properties, `PipelineConfig` for runtime engineering, `TranslationConfig` for user-facing strategy choices). The 4 added fields here all describe SOURCE properties (language fluency, edition, archaism, embedded languages) — they belong on `SourceDescriptor`, not `TranslationConfig`. The 7 deferred fields, if revived, would mostly land on a UseContext schema or on PipelineConfig — also not `TranslationConfig`. The literal answer to "which become TC fields?" is "none of them," and this is structurally driven, not arbitrary.

**Why "add beside A3," not "split A3."** The edge-case innovation #2 initially proposed splitting A3 into `source_culture` + `source_language`. The split was rejected as destructive. A3 is a settled axis with prose in `config_base_source.md` written assuming current meaning. Splitting would force prose rewrite + breaking schema change + migration. The conflation A3 carries (culture and language-fluency) is real but addressable by adding beside — `SourceDescriptor.source_language_fluency` captures the language dimension without modifying A3. The non-destructive path was chosen.

**Why UseContext was deferred as a schema.** The edge-case innovation Group γ proposed UseContext as a schema holding `consumption_mode` / `reading_session_pattern` / `output_finality`. The deferral was structurally motivated. The chunking deep-dive already committed two new schemas. Committing UseContext here would be the third new schema in two consecutive inquiries — a violation of the user's incremental-addition pacing pattern (visible across recent inquiries: a 280-line config simplified to 10 lines; `config_base_source.md` bloat cut; the chunking finding accepted only one new TranslationConfig field). Each Group γ member defers individually with revival triggers; the UseContext schema commitment has its own bundling revival rule (when at least two members fire).

**Why edge-case #8 became a property within #1, not a separate top-level field.** Quranic citation handling structurally is one kind of embedded-language policy. The Arabic embedded segments in Nursi include both Quranic citations (with established translation tradition: Yusuf Ali / Sahih International / Asad / Pickthall) and non-Quranic phrases (Arabic kalam terms, formulae). The `quranic_citation_policy` belongs as a property on the Arabic `EmbeddedLanguagePolicy` entry, set only when the embedded segments are Quranic citations. Making it a separate top-level field would create a category-shape mismatch.

**Why each defer carries an explicit revival trigger.** The chunking deep-dive established the pattern of explicit triggers (not vague "eventually" gates). Without triggers, deferrals become permanent silent omissions. The triggers are observable, time-bound, or condition-bound per the protocol style rule.

**External-grounding partial.** The critique flagged that some load-bearing claims (the chunking finding's section 7 for inherited routings; `config_base_source.md`'s A3 prose for "settled prose" claim) cite the canonical sources structurally without quoting them verbatim. This is documented as a MUST refinement in Next Actions — the finding-polish pass closes the gap.

**The cross-inquiry dependency.** This inquiry's Phase 2 work depends on the chunking deep-dive's `SourceDescriptor` schema MUST item shipping. This is real, not artificial — both inquiries' edits need the parent schema as a foundation. Routelister's R22 surfaced this prominently; CONCLUDE documents it as the gating dependency.

## Open Questions

### Monitoring

- After the SourceDescriptor schema implementation step ships (from the chunking deep-dive's MUST), observe whether the field signatures sketched here in section 2 hold under the chunking finding's own ChunkingUnit work. If divergences emerge (e.g., chunking implements ChunkingUnit differently than this inquiry assumes), this finding's section 2 code needs revision before Phase 2 ships.
- After the first translations using the Nursi-specific SourceDescriptor instance, observe whether the cross-axis interactions documented in section 6 hold in practice (e.g., does `source_temporal_register: hybrid-by-register-domain` actually compose with register-alternation preservation correctly?).
- After 2-3 translation iterations, observe whether any of the 7 deferred fields' revival triggers actually fire. If they fire, opening a follow-up inquiry per the initiation paths in section 7 is the next step.

### Blocked

- Phase 2 implementation (Next Actions MUST items) is blocked until the chunking deep-dive's `SourceDescriptor` schema MUST ships. The cross-inquiry dependency is real.
- The UseContext schema commitment is blocked on the bundling rule (at least 2 of {#9, #10, #12} firing).
- The EditionDescriptor promotion COULD is blocked on the variant-tracking trigger.

### Research Frontiers

- The 2D-decision template (outcome × schema-home with revival-trigger + cross-axis-check + Inherited-Commitments-Re-test) suggested as reusable for future bulk-edge-case inquiries. Forward-looking; no known path; depends on similar synthesis patterns emerging.
- A3 re-examination (if conflation produces ambiguity) is a research frontier in the sense that whether the conflation actually causes real problems is empirically unknown until more translations run.

### Refinement Triggers

- If real translation cases produce ambiguous A3 assignments (a reader is `source-native` culturally but `none` in fluency), revisit A3 as a refactor candidate.
- If the chunking deep-dive's SourceDescriptor implementation diverges from what this inquiry sketches (different ChunkingUnit shape, different EmbeddedLanguagePolicy hosting, etc.), this finding's section 2 + 3 code needs to be reconciled.
- If `source_temporal_register: modernize-fully` is used in practice and the no-smoothing policy is observed to fire, the CAUTION in the docstring may need to be upgraded to a hard validation rule.
- If at least two of {#9, #10, #12} reach revival, re-open the UseContext schema commitment (deferred non-modification N2).

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
14 edge-case fields written to devdocs/innovation/translation_config_edge_cases.md. Quick map:

  Multi-lingual / multi-layer source — (1) embedded_source_languages (your Arabic-in-Turkish example), (2) split source_language from
  source_culture (an A3-conflation fix), (3) source_edition (which printing/manuscript).

  Voice / authority / textual layer — (4) voice_disambiguation (Nursi's own writing vs. citations vs. hashiye vs. lahika), (5)
  relay_translation (source→intermediate→target chains), (6) source_apparatus_handling (Nursi's hashiye preservation).

  Passage heterogeneity — (7) passage_typology (different passages, different configs in one chapter), (8) quranic_citation_special_status
  (Quranic citation ≠ Persian-couplet embedding).

  Reader mode-of-use — (9) consumption_mode (silent / aloud / dersane / recitation / memorization), (10) reading_session_pattern
  (single-pass vs. progressive-daily vs. reference vs. study-circle).

  Translation-process / output — (11) prior_translation_relationship (honor / extend / diverge from Vahide / Akarsu etc.), (12)
  output_finality (ship-ready vs. editor-draft vs. teaching-draft).

  Source-time — (13) source_temporal_register (Ottoman archaism: preserve / modernize / hybrid).

  Surface — (14) script_direction_handling (RTL Arabic embedded in LTR English target).

how these should change our current config

class TranslationConfig(BaseModel):
      reader_level:      Literal["very_basic", "daily", "conversational", "advanced", "native"]         = "conversational"
      domain_expertise:  Literal["lay", "aware", "educated", "trained", "expert"]                       = "aware"
      source_culture:    Literal["outsider", "acquainted", "familiar", "heritage", "source-native"]     = "acquainted"
      purpose:           Literal["scholarly", "devotional", "casual", "language-learning", "performance"] = "casual"
      source_fidelity:   Literal["foreignized-max", "foreignized", "balanced", "lightly-domesticated"]  = "balanced"
      form_preservation: Literal["off", "minimal", "light", "standard", "maximum"]                      = "standard"
      scaffolding:       Literal["off", "minimal", "standard", "rich", "scholarly"]                     = "minimal"
      analysis_depth:    Literal["none", "surface", "standard", "deep", "scholarly"]                    = "none"

fields?
```

</details>





batarya, sajr aleti,  fan motoru,  dwin ekran