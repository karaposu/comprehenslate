# Innovation — Chunk Types vs Mechanisms

## User Input

Input: `_branch.md` + upstream artifacts. Production-task mode; 10 LOOP_DIAGNOSE-shaped pieces; per-piece intervention-shape Inversion-candidates.

---

## Methodology Mode

Standard default. Alternative (Contrarian-rethink) rejected: SV6 stabilized with multiple perspective shifts already absorbed; per-piece Inversion provides contrarian channel. All 10 pieces meta-decision; all property-(v) fires.

---

## P1 — TC `chunking_granularity` field spec

**Principal.**

```python
class TranslationConfig(BaseModel):
    # ... existing 8 axes ...
    chunking_granularity: Literal[
        "sentence",
        "paragraph",
        "passage",
        "subchapter",
        "chapter",
    ] = "paragraph"
    """The granularity at which translation operates.

    Hierarchical ladder (ascending granularity):
    - `sentence` — smallest semantic unit; fine-grained; matches A1 language-learning use
    - `paragraph` — blank-line-bounded prose unit; common default
    - `passage` — thematic prose unit, potentially multi-paragraph
    - `subchapter` — numbered sub-section (Nursi mesele maps here; Quran ruku-equivalent)
    - `chapter` — top-level structural unit

    The AI's mechanism for producing chunks of this granularity is hidden by default
    (hybrid harmony-aware: structural baseline + heuristic + LLM-as-judge for
    Tier-1-ambiguous regions). Advanced users may override via PipelineConfig.

    Corpus-specific names: when SourceDescriptor declares a ChunkingUnit whose
    `canonical_level` matches the chosen granularity, the AI uses the declared name
    (e.g., "mesele" instead of "subchapter" for Nursi).
    """
```

**Inversion-candidate.** Alternative shape: **Keep flat list, add a `chunking_mechanism` separate field** (Variant 2 from articulate_simple). Killed by sensemaking Ambiguity 1: mechanism is implementation, no user-value; anti-bloat violated; matches no A1-A8 pattern. **Verdict: KILL.**

---

## P2 — SD `ChunkingUnit.canonical_level` addition

**Principal.**

```python
class ChunkingUnit(BaseModel):
    name: str                       # corpus-declared name: "mesele", "ayah", "paragraph"
    detector: ChunkingDetector      # mechanism: how to find this unit in source
    canonical_level: Literal[       # NEW: maps to TC's chunking_granularity enum
        "sentence",
        "paragraph",
        "passage",
        "subchapter",
        "chapter",
    ]
    is_atomic: bool = False
    attached_to: str | None = None
```

**Corpus mappings (Nursi-anchored):**

| Corpus | Declared Unit | canonical_level |
|---|---|---|
| Nursi | Söz (book chapter) | `chapter` |
| Nursi | Söz internal section / Mektup | `subchapter` |
| Nursi | mesele (sub-argument) | `subchapter` |
| Nursi | paragraph | `paragraph` |
| Nursi | ayah (embedded Quranic citation) | `sentence` (with `is_atomic=True`) |
| Nursi | hashiye | `paragraph` (with `attached_to="paragraph"`) |
| Bible | book | `chapter` |
| Bible | chapter | `subchapter` |
| Bible | pericope | `passage` |
| Bible | verse | `sentence` |
| Quran | sura | `chapter` |
| Quran | hizb / juz | `subchapter` |
| Quran | ruku | `passage` |
| Quran | ayah | `sentence` |
| Hindu | adhyaya | `subchapter` |
| Hindu | sloka | `sentence` |

**When AI translates with `chunking_granularity = subchapter` on Nursi corpus:** uses mesele as the unit name in output (since mesele is declared at `subchapter` level for Nursi).

**Inversion-candidate.** Alternative shape: **Skip canonical_level; AI infers mapping from name semantics.** Killed: inference is fragile; explicit declaration is one-line per unit and gives deterministic AI behavior. **Verdict: KILL.**

---

## P3 — PipelineConfig optional mechanism override

**Principal.**

```python
class PipelineConfig(BaseModel):
    # ... existing fields ...
    chunking_budget: int | None = None  # from chunking finding
    chunking_mechanism_override: Literal[
        "structural",           # paragraph/sentence boundary detection; no LLM
        "harmony-tier-aware",   # LLM-based; respects Tier 1 chains
        "passage-typology-aware",  # two-pass: classify + chunk per type
        "llm-detected",         # single-pass LLM boundary detection
        "fixed-budget-with-snap",  # token budget + snap to structural unit
        "hybrid",               # default — structural baseline + heuristic + LLM-as-judge
    ] | None = None
    """Override the AI's default mechanism for chunk production.

    `None` (default) — AI uses `hybrid` harmony-aware: structural baseline + 
    Tier-1-ambiguity heuristic + LLM-as-judge for flagged regions + fall-back to 
    structural where LLM uncertain.

    Setting an override is for advanced/evaluation use (e.g., comparing hybrid 
    vs structural-only on a corpus). Regardless of override, the AI MUST preserve 
    Tier 1-2 (the hard constraint applies to chunker output, not to mechanism).
    """
```

**Inversion-candidate.** Alternative shape: **Don't expose mechanism on PipelineConfig at all** (truly internal). Killed: empirical validation per chunking finding's deferred MUST requires mechanism comparison; without override the eval is impossible. **Verdict: KILL.**

---

## P4 — Default mechanism (hidden) — hybrid harmony-aware

**Principal.**

The chunking finding's recommended `hybrid` harmony-aware mechanism survives unchanged as the AI's default. Four-step operation:

1. Structural baseline pass using the SD's declared unit at the chosen `canonical_level` (or paragraph if no SD declaration).
2. Tier-1-ambiguity heuristic scan (regex-style detection of cause-effect connectives, conditional chains, semantic-escalation patterns spanning candidate boundaries).
3. LLM-as-judge on flagged regions only — prompt context includes `harmony_layer.md` Tier 1-2 reference; returns `{decision: MERGE | KEEP | SPLIT, confidence: 0.0-1.0}`.
4. Fall back to structural baseline where LLM confidence < 0.7.

**Behavior across granularities:**
- `sentence` — structural sentence boundaries + harmony-tier-aware check for Tier 1 chains spanning sentence boundaries (merges sentences if needed)
- `paragraph` — same pattern at paragraph boundaries
- `passage` — LLM-detected passage boundaries (no structural baseline at this level for most corpora) + harmony-tier-aware
- `subchapter` — SD's declared subchapter-level unit (mesele for Nursi) + harmony-tier-aware
- `chapter` — SD's declared chapter-level unit

**Inversion-candidate.** Alternative shape: **Default = structural-only (no LLM)**. Killed by chunking finding's empirical analysis: structural-only risks Tier 1 chain splits in Nursi's istilzam chains spanning paragraphs. **Verdict: KILL.**

---

## P5 — A4-driven defaults revision

**Principal.**

| A4 purpose | Old default (8-literal mixed enum) | New default (chunking_granularity) | Reasoning |
|---|---|---|---|
| scholarly | `harmony-tier-aware` (mechanism) | `passage` | Scholars work at thematic-passage level; mechanism is hybrid harmony-aware (default) |
| devotional | `source-structural-unit` | `subchapter` | Devotional readers engage at natural source-unit level (Nursi mesele; Bible chapter-as-subchapter) |
| casual | `paragraph` | `paragraph` | Unchanged |
| language-learning | `sentence` | `sentence` | Unchanged |
| performance | `source-structural-unit` | `subchapter` (or `passage`) | Performance follows declared structural units; subchapter is safest default |

**Default when A4 silent:** `paragraph` (chain through casual). Unchanged.

**Inversion-candidate.** Alternative shape: **Drop A4 defaults entirely; require explicit user choice.** Killed: A4-driven defaults is the project's established pattern (preserved per chunking finding A6 in P9 below). **Verdict: KILL.**

---

## P6 — Cross-cutting constraints preservation

**Principal.**

All three cross-cutting constraints from the chunking finding survive the redesign UNCHANGED:

1. **Tier 1-2 preservation (HARD; absolute).** Applies to AI's mechanism output regardless of `chunking_granularity` choice or `chunking_mechanism_override`. The mechanism MUST not break a Tier 1 entry.
2. **Multi-meaning chunk-size lower bound (runtime invariant).** When polysemy's disambiguation requires local-construction co-presence, the chunk must contain both — AI may merge below user's chosen granularity if needed.
3. **A6 activation-gate cascade.** When `A6 ≥ light`, the mechanism MUST be harmony-tier-aware (the default hybrid satisfies this; override values `structural` / `llm-detected` / `fixed-budget-with-snap` are REJECTED at config-resolution time when A6 ≥ light).

**Asymmetric-failure direction:** under-chunking (chunks too large) is still worse than over-chunking. Mechanism MUST over-chunk under uncertainty.

**Inversion-candidate.** Alternative shape: **Soften Tier 1 constraint** to "preserve when possible." Killed by harmony_layer foundational commitment. **Verdict: KILL.**

---

## P7 — Inherited Commitments Re-test

**Principal.**

### From the chunking finding

| # | Commitment | Status | Evidence |
|---|---|---|---|
| C1 | Three-operation chunking category | RE-TESTED — confirmed | Source segmentation / LLM-context / config-application all still distinct |
| C2 | Split placement (SD / PC / TC) | RE-TESTED — confirmed | Preserved; this inquiry refines TC's chunking field only |
| C3 | `chunking_strategy` 8-literal enum on TC | RE-TESTED — **commitment found INVALID** | Replaced by `chunking_granularity` 5-literal hierarchical ladder. The 5 mechanism literals are re-homed (default: hidden; advanced: PipelineConfig override) |
| C4 | Hybrid harmony-aware as recommended operational default | RE-TESTED — confirmed but RE-HOMED | Survives as AI's default mechanism; no longer a TC enum literal |
| C5 | A4-driven defaults | RE-TESTED — confirmed with revision | Defaults updated per P5 to reference types not mechanisms |
| C6 | Three hard constraints (Tier 1-2 / multi-meaning / A6 cascade) | RE-TESTED — confirmed | Preserved unchanged (P6) |
| C7 | A6 activation-gate cascade (A6 ≥ light → harmony-aware required) | RE-TESTED — confirmed with refinement | Now operates on PipelineConfig.chunking_mechanism_override — rejects non-harmony-aware values when A6 ≥ light |
| C8 | Asymmetric-failure direction (under-chunking worse) | RE-TESTED — confirmed | Preserved |
| C9 | Empirical validation plan (Nursi corpus) | RE-TESTED — confirmed with REVISION | Comparison set updates: `structural` vs `hybrid` vs `harmony-tier-aware` as PipelineConfig override values (not as TC literals) |
| C10 | Generalization to broader pattern (Bible/Quran/Hindu) | RE-TESTED — confirmed with strengthening | The canonical_level field (P2) makes the generalization concrete and verifiable per corpus |

### From LOOP_DIAGNOSE finding

| # | Commitment | Status | Evidence |
|---|---|---|---|
| L1 | Chunking finding's per-field routings (#1, #6, #7) are correct | RE-TESTED — confirmed | The routings stand. This inquiry's revision is about chunking_strategy field's internal enum, not the SD routings |
| L2 | "Chunking finding survived intact" framing | RE-TESTED — **commitment found INVALID (too strong)** | The chunking_strategy enum had its own type-vs-mechanism conflation that the chunking critique missed. The routings-correct claim survives; the survived-intact framing weakens |
| L3 | MC1 (Candidate-Self-Consistency sub-axis) is a strong maintenance candidate | RE-TESTED — confirmed with strengthening | MC1 would have caught chunking_strategy's conflation too (the literals make incompatible internal claims about what axis they're on) |
| L4 | MC2 (Comparative-Pattern Test perspective) is a strong maintenance candidate | RE-TESTED — confirmed with strengthening | This inquiry IS MC2's first branch-test. MC2 catches the conflation (chunking_strategy doesn't match A1-A8 single-axis pattern). MC2 promotion case strengthens |
| L5 | Diagnostic verdict ACTIONABLE | RE-TESTED — confirmed | MC1 + MC2 evidence base grows; promotion case stronger |

**Inversion-candidate.** Alternative shape: **Skip re-test (trust priors).** Killed by Synthesis Trigger protocol. **Verdict: KILL.**

---

## P8 — MC1 + MC2 evidence note (LOOP_DIAGNOSE branch-test outcome)

**Principal.**

This inquiry's existence and outcome strengthen LOOP_DIAGNOSE's two strong maintenance candidates:

**MC1 (Candidate-Self-Consistency sub-axis in td-critique).** Would have caught the chunking_strategy conflation. The 8 literals make incompatible internal claims: `paragraph` claims to name a structural unit; `LLM-detected` claims to name a detection mechanism; these are different ontological categories. Substance-axis prosecution applying each literal's own definition against the enum's axis would have surfaced the conflation. Evidence-strength: HIGH (smoking-gun is now TWO independent cases — edge-cases P3 docstring vs chunking_strategy enum literals).

**MC2 (Comparative-Pattern Test perspective in sense-making).** This inquiry IS its first branch-test. The test fired (compare chunking_strategy against A1-A8) and caught the conflation (none of A1-A8 mix axes; chunking_strategy does). The user performed exactly this comparison in their pushback. Evidence-strength: HIGH; MC2's evaluation gate is being MET.

**Promotion case:** strengthen from "branch-test first" to "branch-test confirmed on independent case; ready for canonical-spec promotion after one more branch-test on a non-chunking-related inquiry." Two of two correction chains have produced applicable cases.

**Inversion-candidate.** Alternative shape: **Wait for more branch-tests before stating evidence-strength change.** Killed: the inquiry's existence IS the branch-test; recording its outcome is appropriate. **Verdict: KILL.**

---

## P9 — LOOP_DIAGNOSE finding revision note

**Principal.**

Add a note to `devdocs/inquiries/2026-06-14_02-29__loop_diagnose__sd_vs_tc_misrouting/finding.md` at the Finding Summary level:

> **Update from follow-up inquiry (`devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/`):** The chunking finding's per-field routings (#1, #6, #7) survive — this finding's L1 claim stands. BUT the chunking finding's `chunking_strategy` enum had its own type-vs-mechanism conflation that the chunking critique stage missed. The "survived intact" framing in this finding's Summary was too strong; chunking's routings are correct but chunking_strategy enum is being revised in the follow-up inquiry. Same critique-stage failure pattern as edge-cases critique (no principle-application-correctness dimension; substance-axis missed internal contradiction). MC1 and MC2 are strengthened by this independent case.

**Inversion-candidate.** Alternative shape: **Leave LOOP_DIAGNOSE finding unchanged** (its scope was bounded to SD-vs-TC). Killed: the framing claim ("chunking survived intact") was specifically too strong and merits correction; honest scoping note prevents future readers from mis-citing it. **Verdict: KILL.**

---

## P10 — Migration plan

**Principal.**

### Phase 1 — Documentation updates (no code)

| Action | File | Gate |
|---|---|---|
| Add Correction Notice at top of chunking finding citing this inquiry's revision | `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` | Observable — when this finding is referenced |
| Add Update note to LOOP_DIAGNOSE finding Summary (per P9) | `devdocs/inquiries/2026-06-14_02-29__loop_diagnose__sd_vs_tc_misrouting/finding.md` | Same |
| Update `config_base_source.md` chunking section to describe `chunking_granularity` instead of `chunking_strategy` | `config_base_source.md` | Same |

### Phase 2 — Schema code

| Action | File | Gate |
|---|---|---|
| Replace `chunking_strategy` field with `chunking_granularity` in TC | `translation_config.py` | When schema code work begins |
| Add `canonical_level` field to ChunkingUnit | `source_descriptor.py` (when created per chunking finding's MUST) | When SD schema is implemented |
| Add `chunking_mechanism_override` field to PipelineConfig | `pipeline_config.py` (when created per chunking finding's MUST) | Same |
| Document AI's default mechanism (hidden) in code docstring | TC or AI-pipeline code | Same |

### Phase 3 — Translation work

| Action | Gate |
|---|---|
| Update 4_mesele translation to use chunking_granularity (subchapter for mesele-level work) | When schema code lands |
| Empirical validation per chunking finding's deferred MUST — comparison now: `structural` vs `hybrid` vs `harmony-tier-aware` as PipelineConfig overrides | When validation work runs |

### Phase 4 — Discipline-spec updates

| Action | Gate |
|---|---|
| Promote MC1 (Candidate-Self-Consistency sub-axis) to td-critique canonical spec | Condition-bound — after one more branch-test on non-chunking-related inquiry |
| Promote MC2 (Comparative-Pattern Test perspective) to sense-making canonical spec | Same |

**Inversion-candidate.** Alternative shape: **All-at-once migration** (do every phase simultaneously). Killed: phases have natural dependencies (schema code depends on SD/PC creation per chunking finding MUSTs). **Verdict: KILL.**

---

## Assembly Check

The 10 principals jointly form a complete revised architecture + Synthesis Re-test + meta-output + migration plan. Three emergent insights:

**Emergent 1: Both LOOP_DIAGNOSE MCs are now backed by TWO independent correction chains** (edge-cases SD-vs-TC + chunking type-vs-mechanism). Each chain provided distinct smoking-gun evidence (docstring contradiction for MC1's first case; enum literal categorical mismatch for MC1's second case). Promotion case crosses from "first branch-test" to "two-case validated."

**Emergent 2: The chunking critique stage missed BOTH conflations** (the edge-cases inquiry's misrouting was missed by edge-cases critique; the chunking_strategy enum conflation was missed by chunking critique). This is a critique-stage pattern, not coincidence. Strengthens the case that MC1's missing-dimension problem is the load-bearing structural gap in td-critique.

**Emergent 3: Schema substrate (SD's existing ChunkingUnit shape) was the correct comparative-pattern target.** SD's ChunkingUnit already separates name/detector/property/relation. TC's chunking_strategy should have inherited the same separation pattern but didn't. The substrate ALREADY had the correct shape; the new TC field didn't mirror it. Same substrate-reachability framing as LOOP_DIAGNOSE.

---

## Failure-mode check

NONE fired across 6 modes.

---

## Telemetry

- Generators: 4/4 + Framers: 3/3. Full coverage.
- Convergence: YES (the hierarchical-ladder + hidden-mechanism solution reached via multiple mechanisms).
- Survivors tested: 20 (10 principal + 10 inversion).
- Disposition: 10 ACTIONABLE principals + 10 KILL inversions.
- Failure modes: 0.
- Overall: PROCEED.
