# Surfacing — schemas_rationale_and_policy_list

## User Input

```text
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/_branch.md

The articulation bundle is at the same folder's articulate_simple.md. Read both _branch.md and articulate_simple.md as inquiry framing.

The Synthesis Trigger declares 4 priors that should be read as territory:
1. /Users/ns/Desktop/projects/comprehenslate/schemas.py (the current 3-class authoritative schema — the artifact Item 1 explains)
2. /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md (the 4-schema architecture the user has now simplified past)
3. /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md (origin of split-placement principle)
4. /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md (14-edge-case territory for Item 2's policy list)

Save surfacing output to: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/surfacing.md
```

---

## Setup

- **Mode:** `artifact` (territory contains existing items: 3 prior findings + the schemas.py file + the edge-case innovation pass).
- **Entry point:** `signal-first` (the inquiry's purpose is given: Item 1 wants rationale for schemas.py's simplification; Item 2 wants list of NonMainLangPartsPolicy-shaped scenarios in theological-translation territory).
- **Territory:** `explicit-bounded` — 4 declared priors + schemas.py + the edge-case innovation pass (`devdocs/innovation/translation_config_edge_cases.md`) implicitly included as the source of the 14-candidate list referenced by the edge-cases finding.
- **Boundary-discovery:** skipped (territory is explicit-bounded).

---

## Traversal Trace

### R1 — schemas.py classes (current authoritative file)

| # | Item | Relevance | Confidence | Step note |
|---|---|---|---|---|
| 1 | `TranslationConfig` — 8 axes unchanged (reader_level / domain_expertise / source_culture / purpose / source_fidelity / form_preservation / scaffolding / analysis_depth) | core | HIGH | The thing-that-stayed-the-same; load-bearing for Item 1 (TC frozen) |
| 2 | `NonMainLangPartsPolicy` — single `policy` field; Literal[5] enum (preserve-original / preserve-original-and-add-translation-as-a-note / replace-original-with-translation / replace-original-with-translation-add-original-as-a-note / replace-original-with-infamous-translation); default `preserve-original-and-add-translation-as-a-note` | core | HIGH | Template for Item 2; subject of explanation in Item 1 |
| 3 | `PipelineConfig` — `chunking_budget: int \| None`; `chunking_granularity: Literal[5] \| None`; `chunking_mechanism_override: Literal[6] \| None` | core | HIGH | New home for chunking_granularity (moved off TC); load-bearing for Item 1 |
| 4 | `NonMainLangPartsPolicy` docstring's edge-case note: "one chapter can have canon language A while another chapter has canon language B; and a single chapter can carry two canon languages" | core | HIGH | Captures the recurring authorial edge-case the policy governs |

### R2 — Prior 4-schema proposal (what got simplified past)

| # | Item | Relevance | Confidence | Step note |
|---|---|---|---|---|
| 5 | `SourceDescriptor` class with `corpus_name` + `source_language` + `chunking_units: list[ChunkingUnit]` + `source_edition` + `embedded_languages: list[EmbeddedLanguagePolicy]` + `source_temporal_register` | core | HIGH | The dropped class — Item 1 must explain why |
| 6 | `ChunkingUnit` class with `canonical_level: Literal[5]` mapping corpus-types to universal ladder | core | HIGH | Dropped — the "book must follow chapter rules" criticism |
| 7 | `EmbeddedLanguage` class (single embedded-language declaration) + `EmbeddedLanguageProfile` wrapper | core | HIGH | Replaced by NonMainLangPartsPolicy; explains the shape-shift |
| 8 | `chunking_granularity` field as a TC axis (the chunk_types_vs_mechanisms finding's central commitment) | core | HIGH | Moved off TC entirely; on PC now |
| 9 | `source_edition` field on SD | sub | HIGH | Dropped; "not needed" per user — light dropping signal |
| 10 | `quranic_citation_policy` as Arabic-specific field with values like `preserve-arabic-with-gloss` | core | HIGH | Replaced by language-agnostic policy — Item 1 must explain shift to language-agnosticism |
| 11 | `source_temporal_register` field on SD (had been ratified Phase 2; now homeless) | sub | MEDIUM | Open residual from earlier turn — flagged for Item 1's residual-issues coverage |

### R3 — Split-placement principle and corrections

| # | Item | Relevance | Confidence | Step note |
|---|---|---|---|---|
| 12 | "Schema ownership matches data ownership" principle (chunking finding §3) | core | HIGH | The load-bearing principle — Item 1 anchors here |
| 13 | Three-schema split: SD = source facts / PC = runtime engineering / TC = user strategy | core | HIGH | Origin of the split; Item 1 traces how schemas.py refines it |
| 14 | User's correction: "LLM just needs to know what lang translation happens [to], and with what config. so we dont need SourceDescriptor" | core | HIGH | The killer move — Item 1's central insight |
| 15 | User's correction: "book must follow certain chapter rules. which is not the case" + "chunking_units: list[ChunkingUnit] is not logical" | core | HIGH | Rejection of imposed universal hierarchy on SD |
| 16 | User's correction: "embedded_languages... shouldnt be there too, it should be in another dataclass" | core | HIGH | Routing correction that became NonMainLangPartsPolicy |
| 17 | User's correction: "doesnt makes sense bc it says arabic, it shoudl have been language agnostic" | core | HIGH | Language-agnosticism principle |
| 18 | User's anti-bloat preference (recurring across recent inquiries: 280-line config simplified to 10 lines; config_base_source.md bloat cut; TC delta = 0 in edge-cases finding) | core | HIGH | Constraint on Item 2's list (don't propose 14 new classes) |

### R4 — 14-edge-case territory (Item 2's source)

| # | Item | Relevance | Confidence | Step note |
|---|---|---|---|---|
| 19 | Edge-case #1 `embedded_source_languages` (Arabic ayahs in Turkish; Persian couplets; transliterated formulae) — now subsumed by NonMainLangPartsPolicy | core | HIGH | Already-routed; serves as the prototypical NonMainLangParts case |
| 20 | Edge-case #4 `voice_disambiguation` — author voice vs cited authorities vs hashiye vs student additions; 4-literal enum (off / implicit-typographic / explicit-attribution / scholarly-apparatus) | core | HIGH | Fits NonMainLangParts shape: enum-of-strategies for recurring authorial edge-case |
| 21 | Edge-case #6 `source_apparatus_handling` — author's marginalia/hashiye; 4-literal enum (drop / translate-inline / translate-as-footnote / preserve-as-source-channel) | core | HIGH | Strong shape-match candidate for Item 2 |
| 22 | Edge-case #8 `quranic_citation_special_status` — 4-literal enum (translate-only / arabic-plus-translation / established-translation-reference / translator-own-version) | core | HIGH | Subsumed by NonMainLangPartsPolicy's `replace-original-with-infamous-translation` value but still a distinct sub-case to surface |
| 23 | Edge-case #13 `source_temporal_register` — 4-literal enum (preserve-archaic / modernize-fully / hybrid-by-register-domain / mark-archaisms-explicitly) | core | HIGH | Strong shape-match: authorial edge-case (archaic source) governed by enum of strategies |
| 24 | Edge-case #14 `script_direction_handling` (bidi RTL embedded in LTR) — 4-literal enum (script-native / transliterated-only / block-separation / facing-page) | core | HIGH | Borderline (surface/rendering more than authorial), but enum shape fits |
| 25 | Edge-case #11 `prior_translation_relationship` — stance enum (independent / honor-terminology / extend-with-revisions / explicit-divergence-noted / collate-and-cite) | sub | HIGH | Partial fit: has the policy enum but also needs a list[PriorRef]; shape carries extra structure |
| 26 | Edge-case #12 `output_finality` — 4-literal enum (final-shippable / editor-draft / teaching-draft / research-preview) | sub | MEDIUM | Output-side rather than authorial-edge-case; partial shape match |
| 27 | Edge-case #5 `relay_translation` — has policy enum + relay_chain list; structurally complex | side | HIGH | Doesn't fit the simple-enum shape; carries extra structure |
| 28 | Edge-case #7 `passage_typology` — passage-type labels rather than handling strategies | side | HIGH | Doesn't fit the policy-as-strategy shape; it's a TYPE label not a strategy choice |
| 29 | Edge-case #9 `consumption_mode` and #10 `reading_session_pattern` — reader-side enums, not authorial-edge-case handling | side | HIGH | Doesn't fit NonMainLangParts shape (no authorial edge-case being handled) |
| 30 | Edge-case #2 `source_language_fluency` and #3 `source_edition` — descriptor-shaped, not policy-shaped | side | HIGH | Doesn't fit the strategy-enum shape; also impacted by user's SD-drop |

### R5 — chunk_types_vs_mechanisms finding's commitments (now superseded in key places)

| # | Item | Relevance | Confidence | Step note |
|---|---|---|---|---|
| 31 | `chunking_granularity` 5-literal enum (sentence / paragraph / passage / subchapter / chapter) | sub | HIGH | Preserved as values but moved off TC to PC |
| 32 | SD.ChunkingUnit `canonical_level` field + Nursi mappings (Söz=chapter, mesele=subchapter, ayah=sentence-atomic, hashiye=paragraph-attached) | sub | HIGH | Dropped; corpus-mapping mechanism rejected with chunking_units |
| 33 | PipelineConfig `chunking_mechanism_override` field (6-literal enum: structural / harmony-tier-aware / passage-typology-aware / llm-detected / fixed-budget-with-snap / hybrid) | sub | HIGH | Still present in schemas.py — preserved unchanged |
| 34 | Hybrid harmony-aware as AI default mechanism | sub | HIGH | Preserved as hidden default per chunking finding's commitment |
| 35 | A6 cascade rejection (≥light forbids non-harmony-aware mechanism overrides) | side | MEDIUM | Operational rule; preserved by reference but not yet enforced in code |

### R6 — NonMainLangPartsPolicy pattern shape (Item 2 template)

| # | Item | Relevance | Confidence | Step note |
|---|---|---|---|---|
| 36 | Pattern: small Literal[] enum field on a single-field BaseModel governing a recurring authorial edge-case | core | HIGH | The shape Item 2 catalogs against |
| 37 | 2D vocabulary structure: {preserve, replace} × {-, +note as annotation} + special-case (infamous-translation) | core | HIGH | Suggests other policies may decompose similarly |
| 38 | Language-agnosticism: values don't name a specific language (no "arabic" / "quranic" in literal values) | core | HIGH | Generalizes; other policies should follow same principle |
| 39 | Corpus-agnosticism: works for any corpus with multi-language source content | core | HIGH | Consistent with TC's corpus-agnostic axes |
| 40 | Single class per recurring edge-case (not a dict-of-policies; not a wrapper-with-list) — flat composability with sibling policies in schemas.py | core | HIGH | Tells Item 2 how to shape its catalog entries |

### R7 — Theological-translation phenomena beyond the 14 edge-cases

| # | Item | Relevance | Confidence | Step note |
|---|---|---|---|---|
| 41 | Honorifics (SAW, AS, RA, ASW for Islamic; ZT"L, RA, OBM for Jewish; etc.) — recurring authorial-edge-case with strategy choice | sub | HIGH | Strong shape-match; not in the 14 |
| 42 | Formulaic openings (Bismillah, Shema, invocations) — recurring authorial-edge-case | sub | HIGH | Strong shape-match; not in the 14 |
| 43 | Embedded poetry/verse (Mevlana couplets, Tanakh psalms, Sanskrit slokas) — distinct from prose embedded-language case | sub | HIGH | Adjacent to #1 but the rendering decision differs |
| 44 | Numbering/reference notation (sura:ayah; book:chapter:verse; canto:line) — recurring authorial-edge-case for cross-references | sub | MEDIUM | Could fit; values may be too corpus-specific |
| 45 | Transliteration standard (ALA-LC vs DIN-31635 vs Encyclopedia-of-Islam-2nd vs popular) — recurring choice when source is non-Latin script | sub | MEDIUM | Fits enum shape; possibly orthogonal to NonMainLangPartsPolicy |
| 46 | Anachronism handling (kalam terms assumed familiar in 1920s but obscure today; place names; technical theological vocabulary) — recurring authorial-time gap | side | MEDIUM | Fits but overlaps with source_temporal_register |
| 47 | Sigla / abbreviations (manuscript-tradition conventions, critical-apparatus marks) | umbrella | LOW | Could be policy or could be descriptor; uncertain subtype |
| 48 | Genre-specific apparatus differences (kalam argument vs Sufi narrative vs tafsir gloss) — different render conventions per genre | umbrella | LOW | Could be policy-shaped or could fold into passage_typology direction |

### R8 — Existing schemas.py fields (constraint check)

| # | Item | Relevance | Confidence | Step note |
|---|---|---|---|---|
| 49 | TC's 8 axes (frozen) — anything Item 2 proposes must not duplicate these | sub | HIGH | Constraint check; A3 source_culture overlaps with potential corpus-context policies |
| 50 | PC's 3 fields (runtime knobs) — anything Item 2 proposes must not be a runtime knob | sub | HIGH | Constraint check |
| 51 | TC.A4 purpose driving downstream defaults (scholarly / devotional / casual / language-learning / performance) — policies may want to read A4 for defaults | side | MEDIUM | Composition signal |

### R9 — User constraints active in this session

| # | Item | Relevance | Confidence | Step note |
|---|---|---|---|---|
| 52 | TC frozen — no new fields on TranslationConfig | core | HIGH | Hard constraint on Item 2 |
| 53 | SD dropped — no SourceDescriptor; corpus-facts not declared in schemas.py | core | HIGH | Hard constraint on Item 2 |
| 54 | EmbeddedLanguage dropped — single language-agnostic policy class replaced it | core | HIGH | Tells Item 2 how to shape language-handling policies (don't list per-language) |
| 55 | Anti-bloat — list should be filtered by real need + shape-fit, not exhaustive | core | HIGH | Constraint on Item 2's length |
| 56 | "Translation happens regardless of source language via LLMs" — LLM-capability assumption | core | HIGH | Item 1 must articulate this; Item 2 constrained by it (don't list LLM-needs-to-know-X policies) |

---

## State Summary

### Territory specification (echo)

The 4 declared priors + schemas.py + the implicit `devdocs/innovation/translation_config_edge_cases.md` (the source-of-truth for the 14-candidate descriptions referenced by the edge-cases finding).

### Purpose specification (echo)

Two-strand purpose carried in `_branch.md`:
- **Item 1** — explain why schemas.py (3-class simplification) makes more sense than the prior 4-schema proposal. Bias: rationale-explanation; depth open; comparison-target open.
- **Item 2** — list NonMainLangPartsPolicy-shaped scenarios in the theological-translation territory. Bias: enum-of-strategies-for-recurring-authorial-edge-case pattern.

### Coverage map

| Region | Coverage | Aggregate relevance | Notes |
|---|---|---|---|
| R1 schemas.py classes | confirmed | core | All 3 classes + edge-case docstring note enumerated |
| R2 dropped-from-4-schema design | confirmed | core | 7 dropped/changed items enumerated |
| R3 split-placement + corrections | confirmed | core | Principle + 5 user-correction quotes captured |
| R4 14-edge-case territory | confirmed | mixed | All 14 evaluated against NonMainLangParts shape |
| R5 chunk_types_vs_mechanisms commitments | confirmed | sub | Status-shift documented per item |
| R6 NonMainLangPartsPolicy pattern shape | confirmed | core | 5 structural features extracted |
| R7 phenomena beyond the 14 | scanned | sub | 8 candidates surfaced; not exhaustive — could expand |
| R8 existing schemas.py fields (constraint check) | confirmed | sub | All 3 classes' field-coverage checked |
| R9 user constraints in this session | confirmed | core | 5 active constraints enumerated |

### Confirmed-absent regions

None. No region was traversed and found empty of relevant items.

### Concept-names list

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| schema-ownership-matches-data-ownership | structural-reference | R3 #12 | The chunking finding's load-bearing routing principle |
| split-placement | structural-reference | R3 #13 | The three-schema architecture (SD / PC / TC) by data-ownership |
| TC-delta-zero | coined-term | R8 #18 | The user-foundational rule that TC is frozen |
| NonMainLangParts-shape | coined-term | R6 #36 | The pattern: single-field BaseModel with Literal[] enum governing recurring authorial edge-case |
| language-agnosticism | structural-reference | R3 #17 | Policy values don't name specific languages |
| LLM-handles-source-language | structural-reference | R3 #14 | The killer simplification that dropped SD |
| recurring-authorial-edge-case | coined-term | R6 #36 | The class of phenomena NonMainLangParts-shape governs |
| hashiye | vocabulary | R4 #21 | Author's marginal annotations (Nursi-specific term) |
| mesele | vocabulary | R5 #32 | Nursi-specific sub-argument unit (now dropped from schema) |
| ayah-atomicity | vocabulary | R5 #32 | The "don't split Quranic verse across chunks" preservation |
| infamous-translation | coined-term | R1 #2 | NonMainLangPartsPolicy's value for "use the accepted famous rendering" |
| anti-bloat | structural-reference | R3 #18 | Recurring user preference visible across recent inquiries |

### Recency distribution

| Region | Newest | Oldest | No-mtime-count | Total |
|---|---|---|---|---|
| R1 (schemas.py file) | 2026-06-14 ~23:09 | 2026-06-14 ~23:09 | 0 | 1 file (3 classes + 1 docstring note) |
| R2-R5 (referenced findings) | 2026-06-14 evening (chunk_types_vs_mechanisms) | 2026-06-14 morning (chunking_deep_dive) | 0 | 3 finding files |
| R6-R9 | n/a (conceptual items extracted) | n/a | many | conceptual items, no filesystem backing |

Note: recency annotation is signal only — not used to filter or weight relevance (per the references' §2.1 refinement note).

### Frontier flags

- **R7 is scanned, not exhausted.** I enumerated 8 phenomena beyond the 14 edge-cases, but theological-translation territory is broader than this — particularly across non-Islamic corpora (Tanakh / Bible / Sanskrit-Hindu / Pali Buddhist / Christian patristics). If the inquiry needs cross-corpus completeness for Item 2, a refined-sub-purpose pass focused on non-Islamic corpora would extend coverage.
- **Edge-case #2 `source_language_fluency` routing is residual** — with SD dropped, this field has no obvious home in schemas.py. The user didn't explicitly drop the fluency concept (only the SD class). Flagged for Sensemaking to decide whether it surfaces as a policy or stays dropped.
- **`source_temporal_register` routing is residual** — was Phase 2 on SD; SD now gone; user noted last turn "drop it, or move to PC?" Flagged for Sensemaking's home-routing decision (also a candidate for Item 2's list as ArchaicRegisterPolicy).
- **Pattern-fit border cases:** edge-case #14 (script_direction) and #11 (prior_translation_relationship) are partial shape-matches; Critique will need to adjudicate whether the catalog includes them.

### Workspace-populated status

`{populated: true, populated-at: 2026-06-15_05-04, extent: "9 regions traversed; 56 items enumerated; 26 core + 17 sub + 5 side + 2 umbrella + 6 conceptual-anchor items"}`

### Re-invocation parameters (optional)

None recommended for this iteration. A future iteration focused on cross-corpus completeness for Item 2 could refine to `purpose=NonMainLangParts-shape phenomena in non-Islamic theological corpora`.

---

## Telemetry

- **Mode:** `artifact` + entry-point `signal-first`.
- **Cycles run:** 9 (one per region).
- **Items enumerated:** 56 surfaced items + 12 concept-names.
- **Items tagged at each relevance level:** core = 26; sub = 17; side = 5; umbrella = 2; conceptual (concept-names list) = 12.
- **Sub-phase fired:** no (territory was explicit-bounded).
- **Convergence criteria status:** territory exhaustively traversed at current resolution; no items filtered at uncertain-relevance level (umbrella items kept with LOW confidence); items rejected only on HIGH-confidence rejection.
- **Workspace-overload trigger:** not fired.
- **Failure modes checked:**
  - Mode 1 (Missed-relevance): NOT FIRED (all 9 regions traversed)
  - Mode 2 (Surfaced-irrelevance): NOT FIRED (downstream filtering can handle if any side items aren't useful)
  - Mode 3 (Over-coverage): NOT FIRED (ratio: 26 core / 56 total ≈ 46% — substantive signal density)
  - Mode 4 (Territory-mis-binding): NOT FIRED (all items within declared territory + reasonable concept-anchor extraction)
  - Mode 5 (Workspace overload): NOT FIRED
  - Mode 6 (Artifact under-specification): NOT FIRED (all required fields present)
  - Mode 7 (Workspace-artifact desync): NOT FIRED (capture-at-moment-of-tagging applied)
  - Mode 8 (Recency-Equates-Idleness): NOT FIRED (recency captured as signal-only, not used as relevance verdict)
  - Mode 9 (Recency-Bias-Filter): NOT FIRED (no filtering by mtime)
- **`items_with_mtime` / `items_without_mtime`:** 4 with mtime (file-backed items in R1+R2-R5); 52 without (conceptual items + concept-anchor extractions) — large fraction of conceptual items is expected for a finding-synthesis inquiry.

---

## Self-Assessment Verdict

**PROCEED**

All convergence criteria met. No LAYER 1 failure modes fired. Frontier flags raised (R7 cross-corpus completeness; #2 + #13 routing residuals; #14 + #11 border-cases) are appropriate handoff signals to Sensemaking, not coverage defects.
