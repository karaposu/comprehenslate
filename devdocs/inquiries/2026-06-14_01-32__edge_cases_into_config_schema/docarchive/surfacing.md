# Surfacing — Edge-Cases into Config Schema

## User Input

Input file: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/_branch.md`
Articulation bundle: `articulate_simple.md` (same folder).
Synthesis priors: `devdocs/innovation/translation_config_edge_cases.md` + `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`.

---

## Mode + Entry Point + Reception

- **Mode:** mixed — artifact (the 14 edge-case candidates + 2 prior artifacts + 8 existing axes are enumerable) with possibility (the per-field routing decisions and field shapes are candidate-generated).
- **Entry point:** signal-first — explicit purpose received.
- **Territory specification:** explicit-bounded — the 14 candidates + 8 existing axes + chunking finding's split-placement commitments.
- **Sub-phase fired:** NO — territory is explicit-bounded; boundary-discovery skipped.
- **Purpose echo:** produce a per-field routing table (14 rows × decision columns) + resulting updated schema(s) + migration sequence; scoped to the chunking finding's split-placement architectural commitment.

---

## Traversal Trace

### Region R1 — The 14 edge-case candidates (the items to decide on)

Each is the unit of decision. Relevance is uniformly CORE — these are exactly what the inquiry adjudicates.

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 1 | `embedded_source_languages` — Arabic ayahs in Turkish prose; `list[EmbeddedLanguagePolicy]` | **core** | HIGH | PRE-ROUTED by chunking finding into `ChunkingUnit.is_atomic`; this inquiry inherits and may extend |
| 2 | `source_language` vs `source_culture` (A3-split) — `source_language_fluency: dict[language_code, fluency_level]` | **core** | HIGH | REFINES existing A3 axis, not adds new |
| 3 | `source_edition` — `source_edition: str \| EditionDescriptor` + `variant_handling` | **core** | HIGH | Source-property; SourceDescriptor candidate |
| 4 | `voice_disambiguation` — `Literal["off", "implicit-typographic", "explicit-attribution", "scholarly-apparatus"]` | **core** | HIGH | Could live on TranslationConfig (user-strategy) OR SourceDescriptor (source-property) |
| 5 | `relay_translation` — `relay_chain: list[LanguageHop] \| None` + `intermediate_fidelity_policy` | **core** | HIGH | Not applicable to current Nursi work (no relay); Group α/β/γ unassigned |
| 6 | `source_apparatus_handling` — `Literal["drop", "translate-inline", "translate-as-footnote", "preserve-as-source-channel"]` | **core** | HIGH | PRE-ROUTED by chunking finding into `ChunkingUnit.attached_to` (carries attachment); this inquiry decides if user-facing strategy enum is also needed |
| 7 | `passage_typology` — `passage_overrides: dict[PassageType, PartialConfig]` | **core** | HIGH | Sister-concept to chunking per chunking finding; declared orthogonal axis (chunking determines boundaries; typology labels TYPE per chunk) |
| 8 | `quranic_citation_special_status` — `quranic_citation_policy: Literal[...]` + `citation_attribution_format` | **core** | HIGH | Distinguished from #1; Quranic citation has established translation tradition (Yusuf Ali / Sahih / Asad etc.) |
| 9 | `consumption_mode` — `Literal["silent-personal", "aloud-personal", "communal-study", "recitation", "memorization", "performance-public"]` | **core** | HIGH | Reader-mode-of-use; UseContext candidate per Group γ |
| 10 | `reading_session_pattern` — `Literal["single-pass", "progressive-daily", "reference-lookup", "study-circle"]` | **core** | HIGH | UseContext candidate per Group γ |
| 11 | `prior_translation_relationship` — `prior_translations: list[PriorRef]` + `prior_translation_stance: Literal[...]` | **core** | HIGH | Translation-process concern; Group α/β/γ unassigned; interacts with A5 source_fidelity |
| 12 | `output_finality` — `Literal["final-shippable", "editor-draft", "teaching-draft", "research-preview"]` + `editorial_trust_threshold` | **core** | HIGH | UseContext candidate per Group γ |
| 13 | `source_temporal_register` — `Literal["preserve-archaic", "modernize-fully", "hybrid-by-register-domain", "mark-archaisms-explicitly"]` | **core** | HIGH | Source-property; SourceDescriptor candidate per Group α; interacts with A1 + A6 |
| 14 | `script_direction_handling` — `Literal["script-native", "transliterated-only", "block-separation", "facing-page"]` | **core** | HIGH | Surface/rendering; Group α/β/γ unassigned; may live on PipelineConfig or be internal |

### Region R2 — Edge-case innovation Assembly groups (the prior architectural proposal)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 15 | Group α — SourceDescriptor (what the source IS): proposed members #1, #2, #3, #4, #6, #8, #13 | **core** | HIGH | Direct routing proposal; this inquiry ratifies or refines |
| 16 | Group β — Section-heterogeneity / passage-typology keystone: proposed member #7; with passage-types, several Group α fields become passage-typable | **core** | HIGH | Keystone insight; integrates with chunking finding's `passage-typology-aware` strategy literal |
| 17 | Group γ — UseContext (how output is USED): proposed members #9, #10, #12 | **core** | HIGH | Direct routing proposal |
| 18 | Unassigned in Assembly groups: #5, #11, #14 | sub | HIGH | Innovation pass deferred their routing; this inquiry decides |

### Region R3 — Chunking finding's commitments that pre-route or pre-classify

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 19 | `ChunkingUnit.is_atomic` carries edge-case #1 | **core** | HIGH | Inherited commitment from chunking finding; routing already SETTLED |
| 20 | `ChunkingUnit.attached_to` carries edge-case #6 | **core** | HIGH | Inherited commitment; routing already SETTLED |
| 21 | Edge-case #7 declared orthogonal sister-concept to chunking | **core** | HIGH | Inherited disposition; informs Group β resolution |
| 22 | `SourceDescriptor` schema name + slot for `source_chunking_units` | **core** | HIGH | Schema home exists for Group α candidates |
| 23 | `PipelineConfig` schema name + slot for `chunking_budget` | sub | HIGH | Schema home exists for runtime-engineering candidates (e.g., #14 script direction may belong here) |
| 24 | TranslationConfig extended with `chunking_strategy` field | sub | HIGH | Precedent for adding to TranslationConfig (one new field, A4-driven default) |
| 25 | The split-placement architectural pattern itself (schema ownership matches data ownership) | **core** | HIGH | The decision framework this inquiry applies per field |

### Region R4 — Existing 8-axis TranslationConfig

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 26 | A1 reader_level | sub | HIGH | Interacts with #13 (archaic register affects comprehension) |
| 27 | A2 domain_expertise | side | MED | LOW interaction with all 14 |
| 28 | A3 source_culture | **core** | HIGH | #2 directly REFINES this axis (split into culture + language fluency) |
| 29 | A4 purpose | sub | HIGH | A4-driven defaults pattern applies to new fields where applicable |
| 30 | A5 source_fidelity | sub | HIGH | #11 (prior translation relationship) interacts with stance toward source |
| 31 | A6 form_preservation | sub | HIGH | #13 (temporal register) interacts (archaic forms are form to preserve or modernize) |
| 32 | A7 scaffolding | side | MED | #8 (quranic citation) interacts (citation footnoting depends on A7 budget) |
| 33 | A8 analysis_depth | side | MED | #11 (prior translations) interacts (exegetical history apparatus) |

### Region R5 — Cross-axis / cross-field interactions per edge-case

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 34 | #1 ↔ #8 — Quranic citation is one KIND of embedded source language with special policy | sub | HIGH | Need to decide: is #8 a sub-case of #1 or a separate axis? |
| 35 | #2 ↔ A3 — `source_language_fluency` is a refinement of A3 source_culture | **core** | HIGH | If A3 split: A3 keeps cultural-recognition; new field adds language-fluency dict |
| 36 | #13 ↔ A6 — Archaic forms are themselves form to preserve (Tier 3 register-consistency?) | sub | HIGH | Composes with A6 cascade |
| 37 | #11 ↔ A5 — Stance toward prior translators interacts with source-fidelity stance | sub | MED | E.g., honor-Vahide may bias toward foreignized lexical surface |
| 38 | #7 ↔ chunking_strategy — passage-typology-aware is one chunking strategy literal | **core** | HIGH | Chunking finding's resolution: orthogonal axes, with passage-typology-aware as the composition strategy |
| 39 | #14 ↔ A7 / A8 — script direction is rendering concern, sits below scaffolding/analysis surface | side | MED | May belong in PipelineConfig or internal rendering, not user-facing |
| 40 | #4 voice_disambiguation ↔ #6 source_apparatus_handling — Nursi's voice (author) vs hashiye (his own footnotes) vs lahika (student additions) | **core** | HIGH | Tightly coupled; may share implementation in SourceDescriptor |

### Region R6 — Anti-bloat as filter

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 41 | User pushed back against 280-line translation_config.py earlier in session | **core** | HIGH | Foundational signal: keep TranslationConfig MINIMAL |
| 42 | User asked to cut bloat from config_base_source.md mid-session | **core** | HIGH | Reinforces minimalism on user-facing surfaces |
| 43 | User accepted chunking finding's split-placement (added only `chunking_strategy` to TranslationConfig + 2 new schemas) | sub | HIGH | Precedent: 1 field added to TC, new schemas elsewhere is the pattern |
| 44 | Adding 14 fields to TranslationConfig would 3x the schema | **core** | HIGH | Operationalizes anti-bloat: most additions must NOT land on TC |

### Region R7 — In-flight 4_mesele observation point

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 45 | 4_mesele_en.md contains Arabic ayah citations | **core** | HIGH | #1 (embedded_source_languages) is load-bearing for this file NOW |
| 46 | 4_mesele uses Nursi's hashiye | sub | HIGH | #6 (source_apparatus_handling) relevant; ALREADY pre-routed by chunking finding |
| 47 | Diagnostic inquiry on `mukabilinde` direction-flip surfaced from 4_mesele | sub | HIGH | Signals polysemy work happening NOW; #11 prior-translation-relationship may emerge as need |
| 48 | 4_mesele_en uses Mesele-level chunking de-facto | sub | HIGH | Already covered by chunking finding's SourceDescriptor declaration |

### Region R8 — Schema home candidates (the routing target enumeration)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 49 | `TranslationConfig` — user-facing strategy on what the translation IS | **core** | HIGH | Existing schema; minimal additions per anti-bloat |
| 50 | `SourceDescriptor` — what the source IS; corpus-specific declarations | **core** | HIGH | Pre-committed by chunking finding |
| 51 | `UseContext` — how the output is USED downstream | **core** | HIGH | Proposed by Group γ; needs ratification |
| 52 | `PipelineConfig` — runtime engineering concerns | sub | HIGH | Pre-committed by chunking finding; can absorb rendering concerns like #14 |
| 53 | REFINE-existing-axis — modify A1-A8 enum, not add new field (only candidate: #2 → A3 split) | **core** | HIGH | Different shape of decision from "add new field" |
| 54 | Internal AI implementation — hidden from user (no schema field) | sub | MED | Last-resort if field doesn't deserve config surface |
| 55 | DEFERRED — explicit "not now; revive when X" | **core** | HIGH | The phased-plan exit for non-load-bearing-now |

### Region R9 — Decision categories per field

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 56 | ADD-NOW to TranslationConfig (load-bearing user-strategy axis; passes anti-bloat) | **core** | HIGH | The tightest filter |
| 57 | ADD-NOW to SourceDescriptor (source-property; corpus-specific) | **core** | HIGH | Most edge-cases route here |
| 58 | ADD-NOW to UseContext (how-used-downstream) | **core** | HIGH | Group γ members |
| 59 | ADD-NOW to PipelineConfig (runtime engineering) | sub | HIGH | Limited applicability |
| 60 | REFINE existing A1-A8 axis (only #2 candidate) | sub | HIGH | Modification, not addition |
| 61 | DEFER with revival trigger (sound concept but no use-case forcing it) | **core** | HIGH | Multiple candidates |
| 62 | REJECT entirely (concept doesn't earn schema surface) | side | MED | Rare; needs strong justification |
| 63 | ALREADY-ROUTED-BY-PRIOR (no decision needed; just ratify) | **core** | HIGH | #1, #6, #7 fall here per chunking finding |

---

## State Summary

### Territory + purpose echo

- **Territory:** 14 edge-case candidates + 8-axis TranslationConfig + chunking finding's split-placement commitments + edge-cases-innovation Assembly groups.
- **Purpose:** per-field routing table + updated schema(s) + migration sequence, honoring the chunking finding's split-placement architectural commitment and the user's anti-bloat constraint.

### Coverage map

| Region | Coverage | Aggregate relevance |
|---|---|---|
| R1 — 14 edge-cases | confirmed | uniformly core |
| R2 — Assembly groups | confirmed | core (with 3 unassigned to ratify) |
| R3 — chunking pre-routing | confirmed | core (3 cases SETTLED; precedent applies) |
| R4 — existing 8 axes | confirmed | mixed (A3 core for #2; others sub/side) |
| R5 — cross-field interactions | confirmed | core for tight couplings (#1↔#8; #4↔#6; #7↔chunking) |
| R6 — anti-bloat | confirmed | core (foundational filter) |
| R7 — 4_mesele observation | confirmed | core (#1 load-bearing NOW) |
| R8 — schema home options | confirmed | core (7 candidates per field) |
| R9 — decision categories | confirmed | core (7 decision types) |

### Concept-names list

- **Group α / β / γ** — Assembly check architectural-routing proposal from the edge-case innovation pass
- **SCHEMA-SCOPE-OF-DELIVERABLE** — articulate_simple's MQA-axis: literal (TC-only) vs architectural (multi-schema) reading
- **ALREADY-ROUTED-BY-PRIOR** — decision category for cases the chunking finding settled (#1, #6, #7)
- **REFINE-existing-axis** — distinct from add-new-field (only #2 candidate)
- **schema-home-routing** — the per-field mapping operation
- **passage-typable** — a property of fields that can be overridden per passage type (Group β implication)
- **3x-bloat threshold** — anti-bloat operational signal: adding 14 fields to TC would 3x the schema
- **pre-routing inheritance** — what this inquiry inherits from chunking finding without re-test (if confirmed)

### Frontier flags

Open questions surfacing raised but did not answer:

1. **Group γ ratification** — does UseContext deserve to be a real schema, or do its members (#9, #10, #12) land elsewhere?
2. **#11 placement** — innovation didn't assign; choose between TranslationConfig (user-strategy stance) / UseContext (how output will be used) / DEFER.
3. **#14 placement** — innovation didn't assign; choose between PipelineConfig (rendering) / internal / DEFER.
4. **#5 placement** — innovation didn't assign; relay translation is rare; likely DEFER but worth confirming.
5. **#2 shape** — A3 SPLIT (refine existing axis) vs A3-companion-field (new field). Choose between modification and addition shape.
6. **#4 vs #6 coupling** — share implementation in SourceDescriptor's `ChunkingUnit.attached_to` (chunking finding's solution for #6), or separate voice_disambiguation field?
7. **#8 vs #1 sub-case** — `quranic_citation_special_status` a sub-type of `embedded_source_languages` or a peer axis?
8. **Migration phase boundaries** — which fields are Phase 1 (load-bearing NOW for 4_mesele), Phase 2 (composes with existing for near-future), Phase 3 (deferred)?

### Workspace-populated status

- **populated:** true
- **populated-at:** 2026-06-14_01-38
- **extent:** R1-R9 traversed; 63 items tagged; 2 prior artifacts read in full; current TranslationConfig schema known.

---

## Telemetry

- **Mode:** mixed (artifact-dominant + possibility) | **Entry point:** signal-first
- **Cycles run:** 1 (single-pass traversal)
- **Items enumerated/tagged:** 63
- **Tag distribution:** core = 39; sub = 18; side = 6; umbrella = 0
- **Sub-phase fired:** NO
- **Convergence:** territory exhaustively traversed; no uncertain-relevance items filtered
- **Workspace-overload trigger:** NOT fired
- **Failure modes checked:** all 9 LAYER 1 modes — none fired
- **items_with_mtime:** 4 (4_mesele, edge-cases innovation md, chunking finding, TC schema) | **items_without_mtime:** 59 (possibility / conceptual items)

### Self-Assessment Verdict

**PROCEED**

63 items across 9 regions; 39 core-relevant; 8 frontier flags for downstream sensemaking. Synthesis priors fully read; pre-routing inheritance documented (3 cases settled). No LAYER 1 failure modes fired.
