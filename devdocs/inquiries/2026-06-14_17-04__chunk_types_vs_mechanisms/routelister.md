# Routelister — Chunk Types vs Mechanisms

## User Input

```text
territory: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/
goal: revise chunking_strategy enum per type-vs-mechanism distinction
```

---

## Map Header

- **Run mode:** root / project-space (breadth) | **Entry point:** fresh
- **Identities enumerated:** 12
- **Routes:** 6 teleological + 6 epistemic
- **High-priority count:** 5
- **Frontier flags:** 2

---

## Route Index

| # | Direction | grain | kind | engagement | Priority |
|---|---|---|---|---|---|
| R1 | Add Correction Notice to chunking finding citing this revision | project-space | epistemic | REFINE | HIGH |
| R2 | Add Update note to LOOP_DIAGNOSE finding (survived-intact too strong) | project-space | epistemic | REFINE | HIGH |
| R3 | Update `config_base_source.md` chunking section: `chunking_granularity` not `chunking_strategy` | project-space | epistemic | REFINE | HIGH |
| R4 | Implement `chunking_granularity` field on TC (replacing `chunking_strategy`) | project-space | teleological | DEVELOP | HIGH |
| R5 | Add `canonical_level` field to ChunkingUnit; declare Nursi-specific corpus mappings | project-space | teleological | DEVELOP | HIGH |
| R6 | Add `chunking_mechanism_override` to PipelineConfig | project-space | teleological | DEVELOP | MED |
| R7 | Document AI's default mechanism (hybrid harmony-aware) in code/docstring | project-space | teleological | DEVELOP | MED |
| R8 | Branch-test MC1 on next non-chunking-related inquiry's critique | project-space | epistemic | TEST | MED |
| R9 | Branch-test MC2 on next non-chunking-related inquiry's sensemaking | project-space | epistemic | TEST | MED |
| R10 | Promote MC1 to canonical td-critique spec after non-chunking branch-test | project-space | teleological | DEVELOP | LOW |
| R11 | Promote MC2 to canonical sense-making spec after non-chunking branch-test | project-space | teleological | DEVELOP | LOW |
| R12 | Update 4_mesele translation to use chunking_granularity (subchapter level for mesele) | project-space | teleological | DEVELOP | HIGH |

---

## Per-Route Records

### R1 — Correction Notice on chunking finding

- **Direction:** add a Correction Notice at the top of `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` citing this revision (chunking_strategy enum replaced by chunking_granularity; mechanism re-homed)
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** preserve original content as diagnostic-trail; add notice as new top section

### R2 — Update note on LOOP_DIAGNOSE finding

- **Direction:** add note to LOOP_DIAGNOSE finding Summary that the "chunking survived intact" framing was too strong; routings-correct claim stands
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** per P9 text

### R3 — Update config_base_source.md chunking section

- **Direction:** rewrite the chunking section to describe `chunking_granularity` (5 literals) instead of `chunking_strategy` (8 literals); document hidden default mechanism + PipelineConfig override; A4-defaults table revised per P5
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** bundle with R1 + R2 as finding-text-polish pass

### R4 — Implement chunking_granularity on TC

- **Direction:** replace `chunking_strategy` field with `chunking_granularity` in `translation_config.py`
- **Priority:** HIGH | **Confidence:** HIGH (no prior code shipped; clean replacement)
- **Guidance:** docstring per P1; bundle with R5 + R6 in single schema update

### R5 — Add canonical_level to ChunkingUnit + Nursi mappings

- **Direction:** add `canonical_level: Literal[...]` field to ChunkingUnit; declare Nursi-specific instance with mesele=subchapter, ayah=sentence (is_atomic), hashiye=paragraph (attached_to), etc.
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** gated on SD schema being created per chunking finding's MUST; bundle with R4

### R6 — Add chunking_mechanism_override to PipelineConfig

- **Direction:** add the optional override field per P3
- **Priority:** MED | **Confidence:** MED
- **Guidance:** gated on PipelineConfig schema being created per chunking finding's MUST; implement A6 cascade rejection at config-resolution time

### R7 — Document AI's default mechanism

- **Direction:** in code comments/docstrings, document the hybrid harmony-aware default 4-step mechanism (per P4)
- **Priority:** MED | **Confidence:** HIGH
- **Guidance:** can be code-doc or separate ai_pipeline_mechanism.md depending on project organization

### R8 — Branch-test MC1 on non-chunking inquiry

- **Direction:** apply the Candidate-Self-Consistency sub-axis on the next inquiry's critique that is NOT chunking-related, to extend evidence beyond two chunking-adjacent cases
- **Priority:** MED | **Confidence:** MED
- **Guidance:** evaluation gate per LOOP_DIAGNOSE MC1; if catches another issue: promote to canonical

### R9 — Branch-test MC2 on non-chunking inquiry

- **Direction:** apply the Comparative-Pattern Test perspective on the next inquiry's sensemaking that is NOT chunking-related
- **Priority:** MED | **Confidence:** MED
- **Guidance:** same as R8 for sense-making

### R10 — Promote MC1 to canonical td-critique

- **Direction:** add Candidate-Self-Consistency sub-axis to td-critique canonical spec
- **Priority:** LOW | **Confidence:** MED (gated on R8)

### R11 — Promote MC2 to canonical sense-making

- **Direction:** add Comparative-Pattern Test perspective to sense-making canonical spec
- **Priority:** LOW | **Confidence:** MED (gated on R9)

### R12 — Update 4_mesele translation

- **Direction:** when chunking_granularity is used in 4_mesele work, set to `subchapter` (mesele-level) per Nursi corpus declaration
- **Priority:** HIGH | **Confidence:** HIGH
- **Guidance:** depends on R4 + R5 shipping

---

## Excluded

| Candidate | Why excluded |
|---|---|
| KILLed Inversions | Rejected on structural grounds |
| Pipeline process artifacts | Process not direction |
| User's anti-bloat preference | Constraint, not route |

---

## Telemetry

- 12 identities; 6 teleological + 6 epistemic
- Engagement-type: 4 DEVELOP + 3 REFINE + 2 TEST + 2 DEVELOP (gated) + 1 TEST (alt path... wait recount)
- DEVELOP: R4, R5, R6, R7, R10, R11, R12 = 7
- REFINE: R1, R2, R3 = 3
- TEST: R8, R9 = 2
- HIGH-priority: 5 (R1, R2, R3, R4, R5, R12)... actually 6
- Frontier flags: 2 (R10, R11 — gated promotions)
- LAYER 1 + LAYER 2 failure modes: NONE fired

### Self-Assessment Verdict

**PROCEED**

Tight corrective bundle (R1+R2+R3+R4+R5+R12) propagates the revised schema end-to-end. Branch-test gates (R8, R9) extend MC validation beyond chunking-adjacent cases.
