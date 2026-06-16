# Innovation — Edge-Cases into Config Schema

## User Input

Input: `_branch.md` + upstream `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md` in same folder. Decomposition's 7 pieces (P1-P7) are the seed structure. Production-task mode.

---

## Seed + Methodology Mode

**Production-task mode.** Seed = piece-list from decomposition; Innovation generates text per piece.

**Mode: Standard default** (balanced 4G+3F; elaborate committed direction). Alternative considered: Contrarian-rethink (would challenge SV6 wholesale). Rejected: sensemaking SV3→SV6 already absorbed substantial shifts (Frame-exit Completeness produced 2D-decision refinement); model converged with high anchor diversity. Per-piece Inversion-candidates at intervention-shape axis provide the contrarian channel per piece.

**Meta-decision-piece classification:** ALL 7 pieces meta-decision; ALL fire property (v) intervention-shape. Per Piece-Level Inversion Rule + Intervention-Shape-Axis Inversion, EACH produces principal + inversion-candidate, both 5-tested.

---

## P1 — Per-field decision table (the spine)

**Principal.**

| # | Field | Outcome | Schema home | Phase | Notes |
|---|---|---|---|---|---|
| 1 | `embedded_source_languages` | ALREADY-ROUTED | `SourceDescriptor.ChunkingUnit.is_atomic` (atom carrier) + `SourceDescriptor.embedded_languages: list[EmbeddedLanguagePolicy]` | Phase 1 | Inherits from chunking finding §7. Atomic flag protects Arabic ayahs from splitting |
| 2 | `source_language_fluency` | ADD-now | `SourceDescriptor.source_language_fluency: dict[str, FluencyLevel]` | Phase 2 | Add BESIDE A3 (do NOT split A3). A3 conflation is real but breaking change; this adds the fluency dimension non-destructively |
| 3 | `source_edition` | ADD-now (light) | `SourceDescriptor.source_edition: str \| None` | Phase 2 | Minimal str field now; promote to `EditionDescriptor` when variant-tracking matters |
| 4 | `voice_disambiguation` | DEFER | — | Phase 3 | Pre-routing via #6's `attached_to` covers Nursi+hashiye; lahika case not load-bearing now |
| 5 | `relay_translation` | DEFER | — | Phase 3 | Not in current source→target Turkish→English scope |
| 6 | `source_apparatus_handling` | ALREADY-ROUTED | `SourceDescriptor.ChunkingUnit.attached_to` | Phase 1 | Inherits. Hashiye travels with referent chunk |
| 7 | `passage_typology` | ALREADY-DISPOSED (orthogonal) | `TranslationConfig.chunking_strategy` literal `passage-typology-aware` | Phase 1 | Disposed by chunking finding §7 as orthogonal sister-concept (chunking → BOUNDARIES; typology → TYPE per chunk) |
| 8 | `quranic_citation_special_status` | ADD-now (as policy in #1) | `SourceDescriptor.EmbeddedLanguagePolicy.quranic_citation_policy` | Phase 2 | Property WITHIN #1's policy list, NOT separate top-level field. Set only when language is Arabic AND segments are Quranic citations |
| 9 | `consumption_mode` | DEFER | — | Phase 3 | UseContext schema not committed; deferred |
| 10 | `reading_session_pattern` | DEFER | — | Phase 3 | Same as #9 |
| 11 | `prior_translation_relationship` | DEFER | — | Phase 3 | No Vahide/Akarsu-comparison work in flight |
| 12 | `output_finality` | DEFER | — | Phase 3 | Downstream pipeline doesn't yet distinguish finality levels |
| 13 | `source_temporal_register` | ADD-now (light) | `SourceDescriptor.source_temporal_register: Literal[...]` | Phase 2 | Nursi corpus is archaic Turkish (1920s-30s Ottoman residue); concrete now |
| 14 | `script_direction_handling` | DEFER | — | Phase 3 | Rendering concern; deferred to apparatus-edition phase |

**Distribution:** 3 ALREADY-ROUTED / 4 ADD-now / 7 DEFER / 0 REJECT.

**Headline:** **TranslationConfig delta = 0 new fields.** All adds land on `SourceDescriptor` (or sub-types).

**Inversion-candidate (intervention-shape axis).**

Alternative shape: **ADD-CONTENT with TC additions.** Route #2, #4, #11, #12, #14 to TranslationConfig as user-facing strategy choices. TC grows from 8 to 13.

5-test: novel NO (this IS the surface reading of the user's "fields?" phrasing); scrutiny WEAK (anti-bloat + chunking-finding's schema-ownership principle both prosecute); fertility low; actionability simpler short-term but costly long-term.

**Verdict: KILL. Principal SURVIVES.**

---

## P2 — Inherited-commitment re-test

**Principal.**

### Prior A — `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`

| # | Inherited commitment | Re-test status | Evidence |
|---|---|---|---|
| A1 | Three-operation chunking category | RE-TESTED — confirmed | Category survived this inquiry's perspective check; no edge-case forced a 4th operation or collapsed to fewer |
| A2 | Split placement across `SourceDescriptor` + `PipelineConfig` + `TranslationConfig` | RE-TESTED — confirmed | Foundational to this inquiry's routing. Schema-ownership principle applied per field; produced TC delta = 0 |
| A3 | #1 `embedded_source_languages` → `ChunkingUnit.is_atomic` | RE-TESTED — confirmed | Ratified as ALREADY-ROUTED; field carries atom-preservation semantic |
| A4 | #6 `source_apparatus_handling` → `ChunkingUnit.attached_to` | RE-TESTED — confirmed | Ratified as ALREADY-ROUTED; field carries hashiye→referent linkage |
| A5 | #7 `passage_typology` → orthogonal sister-concept (chunking = BOUNDARIES; typology = TYPE per chunk) | RE-TESTED — confirmed | Ratified; `passage-typology-aware` strategy literal IS the composition |
| A6 | A4-driven defaults pattern (purpose drives downstream-axis defaults) | INHERITED-WITHOUT-RE-TEST | Reason: this inquiry adds zero TC fields; the pattern doesn't apply because no new axes inherit it |
| A7 | Tier 1-2 preservation as HARD constraint | RE-TESTED — confirmed | Cross-axis conflict check (P6) verified none of the 4 SourceDescriptor additions break Tier 1-2 |
| A8 | Hybrid harmony-aware chunker as operational default | INHERITED-WITHOUT-RE-TEST | Reason: out of this inquiry's scope (chunking strategy choice); only the 14-edge-cases routing is in scope here |
| A9 | A6 activation-gate cascade (≥`light` → harmony-aware required) | INHERITED-WITHOUT-RE-TEST | Reason: out of scope; chunking finding owns the cascade; this inquiry doesn't touch A6 semantics |

### Prior B — `devdocs/innovation/translation_config_edge_cases.md`

| # | Inherited commitment | Re-test status | Evidence |
|---|---|---|---|
| B1 | The 14 edge-case candidates as the bounded set for synthesis | RE-TESTED — confirmed | Inquiry scope explicitly bounded to these 14 |
| B2 | Group α — SourceDescriptor proposed members (#1, #2, #3, #4, #6, #8, #13) | RE-TESTED — frame revised | Group α direction confirmed BUT membership refined: #1 + #6 are routed via `ChunkingUnit` sub-fields (not top-level SD); #4 deferred (not load-bearing); #2 + #3 + #8 + #13 ratified as SD top-level additions |
| B3 | Group β — passage-typology keystone (#7) | RE-TESTED — frame revised | Confirmed as orthogonal to chunking per Prior A's A5; not a separate "group" needing schema home — #7 is its own settled disposition |
| B4 | Group γ — UseContext proposed members (#9, #10, #12) | RE-TESTED — INVALID for schema commitment | Group γ as schema commitment DROPPED. Reason: 3-new-schemas-in-2-consecutive-inquiries violates user's incremental-addition pacing + anti-bloat. Members → individual DEFER with revival triggers |
| B5 | The chunking precedent's split-placement justification (schema ownership matches data ownership) | RE-TESTED — confirmed | Applied as decision framework throughout this inquiry's per-field routing |

**Compliance with Synthesis Trigger requirement:** every inherited commitment carries an explicit status (RE-TESTED with evidence, or INHERITED-WITHOUT-RE-TEST with reason). No silent absorption.

**Inversion-candidate (intervention-shape axis).** Alternative: **DO-NOTHING** — trust the priors; skip re-test.

5-test: novel NO; scrutiny WEAK (CONCLUDE protocol explicitly requires re-test under Synthesis Trigger); fertility low.

**Verdict: KILL. Principal SURVIVES.**

---

## P3 — SourceDescriptor addition sketches

**Principal.**

```python
from typing import Literal
from pydantic import BaseModel

FluencyLevel = Literal["none", "basic", "reading-only", "fluent", "native"]


class EmbeddedLanguagePolicy(BaseModel):
    """Per-embedded-language declaration on a SourceDescriptor.
    
    Composes with the chunking finding's ChunkingUnit (which carries is_atomic
    at the chunking level); this class carries per-language POLICY semantics.
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
    """Set ONLY when language_code='ar' AND embedded segments are Quranic citations.
    Carries edge-case #8 'quranic_citation_special_status' as a policy property of #1.
    """


class SourceDescriptor(BaseModel):
    """Corpus-specific source declarations.
    
    Builds on the chunking finding's SourceDescriptor stub (which committed
    source_chunking_units). This inquiry adds 4 fields capturing source properties
    beyond chunk boundaries.
    """
    
    # ALREADY COMMITTED by chunking finding:
    source_chunking_units: list  # list[ChunkingUnit]
    
    # PHASE 2 ADDITIONS from this inquiry:
    
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
    1928 lithograph vs 1956 Latinized printing of Nursi), promote to a structured
    EditionDescriptor in a follow-up inquiry.
    
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
    
    Cross-references:
    - Composes with Layer-2 register-alternation preservation policy.
    - 'modernize-fully' carries no-smoothing-policy risk; use with care, NOT default.
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
    
    Carries edge-cases #1 (parent) and #8 (quranic_citation_policy property).
    """
```

**Corpus-applicability:** all 4 fields are pattern-level. Bible / Quran / Hindu scripture corpora would specify their own fluency dict, edition, register, and embedded-language policies. The schema doesn't hard-code Nursi-specific values.

**Inversion-candidate (intervention-shape axis).** Alternative: **REORGANIZE-WITHOUT-ADDING** — fold all 4 into one big `SourceDescriptor.source_metadata: dict[str, Any]`.

5-test: novel MED; scrutiny WEAK (loses type-safety, pydantic validation, schema-discoverability; project's pydantic-first discipline broken); fertility low.

**Verdict: KILL. Principal SURVIVES.**

---

## P4 — DEFER revival-trigger specifications

**Principal.**

Each deferral carries a concrete revival trigger — observable, time-bound, or condition-bound. Vague gates ("eventually," "when appropriate") are not used.

| # | Field | Reason for deferral | Revival trigger |
|---|---|---|---|
| 4 | `voice_disambiguation` | Pre-routing via #6's `ChunkingUnit.attached_to` covers Nursi+hashiye case. No real translation case yet needs explicit voice-rendering beyond that | **Condition-bound:** when a translation case needs explicit voice-rendering distinct from hashiye attachment (e.g., lahika letters interleaved with author voice + cited authority; or extended-citation paragraphs where Nursi's voice resumes mid-paragraph) |
| 5 | `relay_translation` | Comprehenslate's current scope is direct Turkish→English. No relay use-case in flight | **Condition-bound:** when target language is added without a translator available with source-language fluency, forcing source→intermediate→target chain |
| 9 | `consumption_mode` | UseContext schema not committed (per P5 N2); individual modes deferred | **Observable:** when a downstream consumer (renderer / UI / validator) actually distinguishes between silent / aloud / dersane / recitation / memorization in its output behavior |
| 10 | `reading_session_pattern` | UseContext schema not committed; pattern not consumed now | **Observable:** when a downstream consumer (index generator / navigation tool) actually distinguishes between single-pass / progressive-daily / reference-lookup / study-circle patterns |
| 11 | `prior_translation_relationship` | No third translation iteration in scope; no Vahide / Akarsu / Tahşiye comparison work in flight | **Condition-bound:** when a translation iteration explicitly positions vs prior translators (e.g., user feedback like "this should honor Vahide's `iman` rendering") |
| 12 | `output_finality` | UseContext schema not committed; downstream pipeline doesn't distinguish | **Observable:** when downstream pipeline behavior actually differs by finality level (e.g., editor-draft includes flagged interpretive choices; final-shippable doesn't) |
| 14 | `script_direction_handling` | Rendering concern; current outputs are body-text only without bidirectional apparatus | **Condition-bound:** when output rendering reaches apparatus-edition stage with bidirectional RTL Arabic display |

When ANY trigger fires, a follow-up inquiry promotes the field from DEFERRED to ADD-now and decides its schema home at that time.

**Inversion-candidate (intervention-shape axis).** Alternative: **DO-NOTHING** — defer silently; no triggers.

5-test: novel NO; scrutiny WEAK (without triggers, deferrals become permanent silent omissions; the chunking inquiry's pattern was explicit triggers); fertility low.

**Verdict: KILL. Principal SURVIVES.**

---

## P5 — Non-modification commitments

**Principal.**

Two explicit "do not do this" commitments documented to prevent silent drift.

### N1 — A3 `source_culture` stays as-is

Do not split A3 into `source_culture` + `source_language` (as edge-case innovation #2 initially suggested).

**Reasoning:**
- A3 is a settled axis with prose in `config_base_source.md` written assuming current meaning (5-level lived-cultural-fluency gradient: `outsider / acquainted / familiar / heritage / source-native`).
- Splitting would force `config_base_source.md` prose rewrite + breaking schema change + migration of existing translation configs.
- The conflation A3 carries (culture and language-fluency in one axis) is real but addressable by **adding beside**: `SourceDescriptor.source_language_fluency` captures the language-fluency dimension without breaking A3.
- Per anti-bloat principle + chunking finding's pattern (one structural change per inquiry, not bulk refactor).

**Revival trigger for revisiting A3:** if real translation cases produce ambiguous A3 assignments (e.g., a reader is `source-native` culturally but `none` in fluency, and the conflation forces a wrong choice), open a follow-up inquiry to refactor A3.

### N2 — UseContext NOT committed as schema

Do not commit `UseContext` as a new schema in this inquiry.

**Reasoning:**
- The chunking finding already committed two new schemas (`SourceDescriptor` + `PipelineConfig`). Committing `UseContext` here would be the THIRD new schema in two consecutive inquiries.
- User's pacing pattern (visible across recent inquiries) is one structural decision per inquiry, not bulk schema explosion.
- Group γ members (#9, #10, #12) are not load-bearing for current Nursi work.
- Each Group γ member has its individual revival trigger (per P4).

**Revival trigger for UseContext as schema:** when ≥2 of {#9 `consumption_mode`, #10 `reading_session_pattern`, #12 `output_finality`} simultaneously have their individual revival triggers fire, re-open the UseContext schema commitment.

**Inversion-candidate (intervention-shape axis).** Alternative: **ADD-CONTENT** — commit UseContext now; commit A3-split now.

What follows: more comprehensive but 3 new schemas + 1 axis modification in one inquiry; violates the user's pacing pattern.

5-test: novel NO; scrutiny WEAK (anti-bloat + incremental-addition pacing both prosecute); fertility low.

**Verdict: KILL. Principal SURVIVES.**

---

## P6 — Cross-axis conflict check

**Principal.**

The 4 SourceDescriptor additions (#2, #3, #8, #13) checked against the existing 8 axes + 5 always-on Layer-2 policies + chunking commitments.

### Per-axis check (A1-A8)

| Axis | #2 `source_language_fluency` | #3 `source_edition` | #8 `quranic_citation_policy` | #13 `source_temporal_register` |
|---|---|---|---|---|
| A1 reader_level | NO conflict; complementary (low fluency in embedded language may limit reader access) | NO conflict | NO conflict | **INTERACTION** — archaic register affects A1 reader-level recognition (docs note recommended) |
| A2 domain_expertise | NO conflict | NO conflict | NO conflict | NO conflict |
| A3 source_culture | **INTERACTION** — refines A3 by adding fluency dimension; A3 stays unchanged | NO conflict | NO conflict | NO conflict |
| A4 purpose | NO conflict | NO conflict | **INTERACTION** — devotional purpose biases toward `arabic-plus-translation`; scholarly toward `established-translation-reference` | NO conflict |
| A5 source_fidelity | NO conflict | NO conflict | **INTERACTION** — foreignized-max → `arabic-plus-translation`; lightly-domesticated → `established-translation-reference` | **INTERACTION** — foreignized-max biases `preserve-archaic`; lightly-domesticated biases `modernize-fully` |
| A6 form_preservation | NO conflict | NO conflict | NO conflict | **INTERACTION** — archaic register is a form layer; A6 ≥ standard would lean toward `preserve-archaic` |
| A7 scaffolding | NO conflict | NO conflict | **INTERACTION** — Quranic citations want footnoting density tied to A7 budget | NO conflict |
| A8 analysis_depth | NO conflict | **INTERACTION** — edition variant noted at A8 deep+ analysis | **INTERACTION** — exegetical history of citations at A8 scholarly | NO conflict |

### Per-Layer-2-policy check

| Policy | #2 | #3 | #8 | #13 |
|---|---|---|---|---|
| Multi-meaning preservation | — | — | — | — |
| Register-alternation preservation | — | — | — | **POSITIVE COMPOSITION** — temporal register IS a register; alternation between archaic theological vocab and modern narrative is exactly what this policy preserves. `hybrid-by-register-domain` default composes naturally |
| Polysemy disambiguation via local construction | — | — | — | — |
| Nazm preservation | — | — | — | — |
| No-smoothing | — | — | — | **CAUTION** — `modernize-fully` option may smooth archaic forms; **docs note recommended** advising "use modernize-fully with care; it is not the default precisely because it can violate no-smoothing" |

### Per-chunking-commitment check

| Chunking commitment | Composability |
|---|---|
| Split-placement (`SourceDescriptor` / `PipelineConfig` / `TranslationConfig`) | All 4 additions COMPOSE — adds to SourceDescriptor exactly as the precedent prescribes |
| `ChunkingUnit` schema | All 4 NO conflict — additions sit at SourceDescriptor top level (#2, #3, #13) or inside `EmbeddedLanguagePolicy` (#8); none collide with ChunkingUnit fields |
| `chunking_strategy` enum | All 4 NO conflict — chunking_strategy lives on TranslationConfig; additions live on SourceDescriptor |
| A6 activation-gate cascade (≥`light` → harmony-aware required) | All 4 NO conflict — additions are SOURCE properties; cascade operates on chunker strategy choice |

### Conclusion

**No hard conflicts.** Two docs notes flagged:
1. `#13 source_temporal_register` composes positively with register-alternation preservation policy (documentation should make the composition explicit).
2. `#13 modernize-fully` carries no-smoothing-policy caution (documentation should warn).

Eight axis-interactions documented (not conflicts; just downstream-relevant relationships to note).

**Inversion-candidate (intervention-shape axis).** Alternative: **DO-NOTHING** — skip the conflict check.

5-test: novel NO; scrutiny WEAK (chunking finding's process showed conflict-check matters; skipping re-introduces silent breakages); fertility low.

**Verdict: KILL. Principal SURVIVES.**

---

## P7 — Migration phase sequencing

**Principal.**

### Phase 1 — Ratify pre-routing (documentation; no schema work)

| Action | What it unblocks | Gate |
|---|---|---|
| Document that edge-case #1 is satisfied by chunking finding's `ChunkingUnit.is_atomic` + this inquiry's `EmbeddedLanguagePolicy` | Arabic ayah handling in 4_mesele and future Nursi translations | Observable — when SourceDescriptor schema is implemented per chunking finding's MUST |
| Document that #6 is satisfied by chunking finding's `ChunkingUnit.attached_to` | Hashiye handling | Same as above |
| Document that #7 is satisfied by chunking finding's `chunking_strategy: passage-typology-aware` literal | Per-passage strategy work | Same as above |

### Phase 2 — SourceDescriptor additions (4 fields + 1 helper class)

| Action | Gate | Why |
|---|---|---|
| Implement `EmbeddedLanguagePolicy` BaseModel with `language_code` + `transliteration_policy` + `quranic_citation_policy` | Condition-bound — SourceDescriptor schema exists (chunking finding's MUST item) | Carries #1 parent semantics + #8 Quranic policy. Requires SourceDescriptor to host it |
| Add `source_language_fluency: dict[str, FluencyLevel] = {}` to SourceDescriptor | Same gate | Refines A3 by adding fluency dimension without modifying A3 |
| Add `source_edition: str \| None = None` to SourceDescriptor | Same gate | Minimal str field; promote to `EditionDescriptor` when variant-tracking matters (revival trigger: when multi-edition corpus added or variants explicitly compared) |
| Add `source_temporal_register: Literal[...] = "hybrid-by-register-domain"` to SourceDescriptor | Same gate | Concrete for Nursi corpus; documents archaic-register handling |
| Add `embedded_languages: list[EmbeddedLanguagePolicy] = []` to SourceDescriptor | Same gate | Container for the `EmbeddedLanguagePolicy` entries |
| Declare Nursi-specific SourceDescriptor instance with these 4 fields populated | Condition-bound — Nursi corpus is being processed | Demonstrates Phase 2 with concrete values |

### Phase 3 — DEFER with revival triggers

Reference P4 table. Each of 7 deferred fields (#4, #5, #9, #10, #11, #12, #14) has a concrete revival trigger. When any trigger fires, a follow-up inquiry promotes that field.

### Non-migrations (per P5)

| Non-action | Reason |
|---|---|
| A3 stays as-is. No schema change | Adding beside A3 (#2) handles the conflation non-destructively |
| UseContext NOT created as schema | 3 new schemas in 2 consecutive inquiries violates pacing pattern; revival trigger: ≥2 of {#9, #10, #12} fire individually |

### Total schema-delta from this inquiry

- **TranslationConfig:** **0 new fields.**
- **SourceDescriptor:** **4 new fields** (`source_language_fluency`, `source_edition`, `source_temporal_register`, `embedded_languages`) + 1 helper BaseModel (`EmbeddedLanguagePolicy`).
- **PipelineConfig:** 0 changes.
- **New schemas:** 0.

**Inversion-candidate (intervention-shape axis).** Alternative: **ADD-CONTENT (all-at-once migration)** — implement all 3 phases simultaneously.

5-test: novel NO; scrutiny WEAK (Phase 1 depends on SourceDescriptor existence — chunking-finding MUST not yet shipped; Phase 2 cannot precede Phase 1's documentation; all-at-once produces large untested change set); fertility low.

**Verdict: KILL. Principal SURVIVES.**

---

## Assembly Check

Examine the 7 principal survivors jointly. Three emergent insights:

**Emergent 1 — The 4 SourceDescriptor additions compose into a coherent "source-description schema layer."** `EmbeddedLanguagePolicy` (carrying #1, #8) + `source_language_fluency` (#2) + `source_edition` (#3) + `source_temporal_register` (#13) all describe SOURCE PROPERTIES. Together they give the chunking finding's SourceDescriptor stub its first substantive shape beyond `source_chunking_units`. The chunking finding committed the schema name; this inquiry fills out its body.

**Emergent 2 — The 7 DEFER decisions + UseContext non-commitment + A3-stays-as-is together form a "conservative pacing pattern" matching the user's session-level preferences.** Net effect (TC delta = 0; 4 SourceDescriptor additions; 7 deferrals with explicit triggers; 2 documented non-modifications) is consistent with the user's anti-bloat + one-structural-decision-per-inquiry pattern observed across recent inquiries.

**Emergent 3 — The decision pattern from this inquiry is reusable as a template for future bulk-edge-case inquiries.** The 2D decision shape (outcome × schema-home) + revival-trigger requirement + cross-axis-conflict-check + Inherited-Commitments-Re-test is a generalizable approach to "synthesize prior candidates into settled decisions" that future inquiries can apply.

---

## Failure-mode check

| Mode | Status |
|---|---|
| Premature evaluation | NO — each candidate 5-tested |
| Single-mechanism trap | NO — 7 mechanisms applied across pieces |
| Early frame lock | NO — Inversion-candidates challenged each piece's committed direction |
| Innovation without grounding | NO — each candidate grounded in substrate |
| Mechanism exhaustion | NO |
| Survival bias | NO — Inversion-candidates explicit-tested; none survived (all KILL) but the KILL reasoning is structural-grounds-based, not comfort-based |

---

## Per-piece compliance log (Property-(v) pieces)

| Piece | Property fired | Inversion axis | Status |
|---|---|---|---|
| P1 | 4 + 5 | intervention-shape (ADD-CONTENT with TC additions) | satisfied — KILL |
| P2 | 1 + 5 | intervention-shape (DO-NOTHING skip re-test) | satisfied — KILL |
| P3 | 5 | intervention-shape (REORGANIZE into dict[str, Any]) | satisfied — KILL |
| P4 | 4 + 5 | intervention-shape (DO-NOTHING no triggers) | satisfied — KILL |
| P5 | 2 + 5 | intervention-shape (ADD-CONTENT commit UseContext + A3-split) | satisfied — KILL |
| P6 | 4 + 5 | intervention-shape (DO-NOTHING skip check) | satisfied — KILL |
| P7 | 5 | intervention-shape (ADD-CONTENT all-at-once) | satisfied — KILL |

7/7 piece-level Inversion compliance satisfied.

---

## Telemetry

- **Generators applied: 4/4** (Combination [P1 — 14 fields × 7 outcomes]; Absence Recognition [P5 explicit non-modifications; P4 DEFER triggers fill the absence of routing]; Domain Transfer [pydantic + schema-design patterns]; Extrapolation [P4 revival triggers extrapolate from current state])
- **Framers applied: 3/3** (Lens Shifting [P1 literal vs architectural reading]; Constraint Manipulation [anti-bloat ADD + chunking-precedent ADD]; Inversion [per-piece intervention-shape])
- **Full coverage achieved.**
- **Convergence: YES** — principal candidates converge on "TC delta = 0; SD delta = 4; 7 DEFER" pattern reached via 3+ mechanisms.
- **Survivors tested: 14** (7 principal + 7 inversion).
- **Per-piece mechanism log:**
  - P1: `[Combination:content, Lens-Shifting:content, Inversion:intervention-shape]`
  - P2: `[Domain-Transfer:content (Synthesis re-test pattern), Inversion:intervention-shape]`
  - P3: `[Domain-Transfer:content (pydantic patterns), Inversion:intervention-shape]`
  - P4: `[Absence-Recognition:content, Extrapolation:content, Inversion:intervention-shape]`
  - P5: `[Absence-Recognition:content, Inversion:intervention-shape]`
  - P6: `[Constraint-Manipulation-ADD:content, Inversion:intervention-shape]`
  - P7: `[Combination:content, Inversion:intervention-shape]`
- **Meta-decision-piece classification:** 7/7 meta-decision; 7/7 property-(v) fires.
- **Piece-level Inversion compliance:** 7/7 satisfied.
- **Output disposition:** 7 ACTIONABLE principals; 7 KILL inversions.
- **Failure modes observed:** none.
- **Overall: PROCEED.**
