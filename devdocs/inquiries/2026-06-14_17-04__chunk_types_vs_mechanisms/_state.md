# State: chunk_types_vs_mechanisms

## Flow-type
articulated-surfacing-routed

## Pipeline
A → Su → S → D → I → C → R (always)

## Progress
- [x] Articulate-Simple
- [x] Surfacing
- [x] Sensemaking
- [x] Decomposition
- [x] Innovation
- [x] Critique
- [x] Routelister
- [x] CONCLUDE

## Iteration
1

## Status
COMPLETE

## Next Discipline
—

## Relationships
- REFINES: devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/ (chunking_strategy enum under direct revision)
- VALIDATES: devdocs/inquiries/2026-06-14_02-29__loop_diagnose__sd_vs_tc_misrouting/ MC2 — this inquiry is MC2's first branch-test
- CHALLENGES: LOOP_DIAGNOSE's "chunking survived intact" claim
- RELATED: /Users/ns/Desktop/projects/comprehenslate/config_base_source.md (needs update)
- RELATED: /Users/ns/Desktop/projects/comprehenslate/translation_config.py (schema baseline)

## History
- 2026-06-14_17-07: Created. Question: revise chunking_strategy enum per type-vs-mechanism distinction (user identified category conflation — paragraph/sentence/passage/chapter/subchapter are TYPES; LLM-detected/fixed-budget-with-snap are MECHANISMS). Articulation: HIGH-PROCEED (1 item; 6 considered articulations: type-only-redesign / two-axis-explicit / type+hidden-mechanism / hierarchical / SD-corpus-extension / MC2-validation; flagged none). Synthesis Trigger: 2 priors (chunking finding under revision; LOOP_DIAGNOSE MC2 validated). MQA surface preserved TWO-AXIS-RECOGNITION openness.
- 2026-06-14_17-09: Surfacing complete. 9 regions; 46 items (36 core + 9 sub + 1 side). Key findings: (1) current 8-literal enum systematically mixes 3 types + 5 mechanisms; (2) user-named types form STRICT NESTING HIERARCHY (chapter > subchapter > passage > paragraph > sentence) — corpus-agnostic; (3) corpus-specific types exist beside canonical types (Nursi mesele; Bible verse; Quran ayah; Hindu sloka); (4) mechanisms sub-categorize into PRIMARY / CONSTRAINT / COMPOSITION; (5) SourceDescriptor.ChunkingUnit ALREADY separates name (TYPE) + detector (MECHANISM) + is_atomic (PROPERTY) + attached_to (RELATION) — the comparative pattern showing axis separation exists in substrate; (6) `hybrid` (chunking finding's recommended operational default) is a mechanism, not a type — currently misclassified; (7) MC2's evaluation gate is being MET right now (this inquiry IS the branch-test; MC2 IS catching an issue). 8 frontier flags including: LOOP_DIAGNOSE's "chunking survived intact" claim is now CHALLENGED. No LAYER 1 failures. PROCEED.
- 2026-06-14_20-05: Decomposition complete. 10 pieces; 7 interfaces; 4-level DAG. Critical path: P1 (TC chunking_granularity) → P2/P3/P4 (SD canonical_level + PipelineConfig override + default mechanism) → P5/P6 (A4 defaults + constraints) → P7/P8/P9 (Inherited Re-test + MC evidence + LOOP_DIAGNOSE note) → P10 (Migration). All 7 self-eval dimensions PASS. NONE failure modes fired. PROCEED.
- 2026-06-14_20-03: Sensemaking complete. 6 SVs. SV1→SV6 substantial delta (5-architectural-variants → 1 chosen architecture). 8 perspectives; Frame-exit Completeness produced source-structural-unit residual resolution. 6 ambiguities collapsed (4 HIGH + 2 MED). FINAL STABILIZED MODEL: TC's revised field is `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]` (corpus-agnostic hierarchical-ladder enum matching A1-A8 pattern; default `paragraph`); mechanism HIDDEN as AI implementation (default = hybrid harmony-aware per chunking finding); SD's ChunkingUnit gets `canonical_level` field mapping corpus-types to ladder positions (mesele≈subchapter; ayah≈sentence); PipelineConfig optionally exposes `chunking_mechanism_override` for advanced/eval use; A4 defaults revised to types-only. MC1 and MC2 from LOOP_DIAGNOSE BOTH would have caught this conflation — strong evidence for promotion. LOOP_DIAGNOSE's chunking-routings-correct claim STANDS; its "survived intact" framing was too strong — chunking_strategy enum had own field-internal conflation that chunking critique missed (same critique-stage failure pattern as edge-cases critique). Accommodation NOT fired. All 6 failure modes checked: 5 NONE; 1 PARTIAL (Self-Reference Blindness — mitigated by user-pushback trigger; LOOP_DIAGNOSE's claim being challenged honestly). Verdict: PROCEED.
- 2026-06-14_20-16: CONCLUDE complete. Finding written. Status COMPLETE. Answer: TC field is `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]` (default `paragraph`); mechanism HIDDEN as AI default (hybrid harmony-aware); SD.ChunkingUnit gets `canonical_level` field with corpus mappings (Nursi mesele=subchapter, ayah=sentence); PipelineConfig gets optional `chunking_mechanism_override` for advanced/eval use. Refines chunking finding (chunking_strategy enum replaced); corrects LOOP_DIAGNOSE's "survived intact" framing (too strong; routings-correct claim stands). MC1 + MC2 validated by independent second case. 6 discipline files archived to docarchive/; routelister.md + _route.md kept in root per routed-pipeline convention.
