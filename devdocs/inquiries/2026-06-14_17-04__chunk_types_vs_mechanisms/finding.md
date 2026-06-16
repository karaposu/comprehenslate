---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md
corrects: devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md
---
# Finding: Chunk Types vs Mechanisms

## Changes from Prior

**Prior paths:**
- `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` — the chunking finding whose `chunking_strategy` enum is being revised.
- `devdocs/inquiries/2026-06-14_02-29__loop_diagnose__sd_vs_tc_misrouting/finding.md` — LOOP_DIAGNOSE finding whose "chunking survived intact" framing is being narrowed.

**Revision trigger.** User pushback in conversation. After reading the chunking finding's `chunking_strategy` enum, the user observed: *"Paragraph yes — this is good. Sentence yes — this is good. Passage, Chapter, Subchapter — these are fundamental ones. LLM detected, fixed budget etc doesn't make sense — bc they are how to determine the chunk, but we are talking about what kind of chunks exist."* The pushback identified a category conflation: the 8-literal enum merged TYPES (what kind of chunks exist) with MECHANISMS (how to find chunks) on a single field.

**What's preserved.** The chunking finding's split-placement architecture (SourceDescriptor / PipelineConfig / TranslationConfig). The three hard constraints (Tier 1-2 preservation; multi-meaning chunk-size lower bound; A6 activation-gate cascade). The recommended hybrid harmony-aware mechanism (re-homed as AI default, not a TC literal). The asymmetric-failure direction (under-chunking worse). The A4-driven defaults pattern. The chunking finding's per-field routings #1, #6, #7 (LOOP_DIAGNOSE confirmed these are correct).

**What's changed.** The `chunking_strategy` 8-literal enum on TranslationConfig is replaced by `chunking_granularity` — a 5-literal hierarchical ladder (`sentence` → `paragraph` → `passage` → `subchapter` → `chapter`). The 5 mechanism literals from the old enum (`harmony-tier-aware`, `passage-typology-aware`, `LLM-detected`, `fixed-budget-with-snap`, `hybrid`) are re-homed: default mechanism (hybrid harmony-aware) is hidden as AI implementation; advanced users may optionally override via PipelineConfig. SourceDescriptor's `ChunkingUnit` gains a `canonical_level` field mapping corpus-specific types (mesele, ayah, etc.) to the canonical ladder. A4-driven defaults are updated to use type literals only.

**What's new.** A concrete revised pydantic schema for TC, SD, and PipelineConfig. Per-corpus canonical_level mapping for Nursi, Bible, Quran, Hindu corpora. Validation of two LOOP_DIAGNOSE maintenance candidates (MC1 Candidate-Self-Consistency sub-axis; MC2 Comparative-Pattern Test perspective) on an independent case. A note that LOOP_DIAGNOSE's "chunking survived intact" framing was too strong — chunking routings stand, but chunking_strategy enum had its own internal conflation that the chunking critique stage missed (same critique-stage failure pattern as edge-cases critique).

**Migration.** Phase 1 — finding-text updates (chunking finding correction notice; LOOP_DIAGNOSE finding note; `config_base_source.md` chunking section). Phase 2 — schema code: replace `chunking_strategy` with `chunking_granularity` on TC; add `canonical_level` to ChunkingUnit; add `chunking_mechanism_override` to PipelineConfig. Phase 3 — 4_mesele translation work uses `chunking_granularity = "subchapter"` (Nursi mesele level). Phase 4 — branch-test MC1 + MC2 on a non-chunking-related inquiry before promoting to canonical specs.

## Question

From `_branch.md`:

> The user identifies a category conflation in the chunking finding's `chunking_strategy` enum: some literals (`paragraph`, `sentence`) name TYPES of chunks; others (`LLM-detected`, `fixed-budget-with-snap`) name MECHANISMS for finding chunks. The user explicitly approves paragraph + sentence + passage + chapter + subchapter as "fundamental" types and explicitly rejects LLM-detected + fixed-budget as "how to determine the chunk." The user requests a deep-dive into the updated logic.

The goal: revise the chunking schema to separate type from mechanism cleanly, matching the existing A1-A8 pattern in TranslationConfig (each axis a single coherent dimension). Validate the LOOP_DIAGNOSE maintenance candidates (MC1, MC2) by applying them — independently — to this case as evidence for canonical promotion.

## Finding Summary

- **The `chunking_strategy` 8-literal enum had a type-vs-mechanism conflation.** Three literals (`source-structural-unit`, `paragraph`, `sentence`) named TYPES of chunks; five literals (`harmony-tier-aware`, `passage-typology-aware`, `LLM-detected`, `fixed-budget-with-snap`, `hybrid`) named MECHANISMS for finding chunks. These are different ontological categories merged into one field.

- **TC's revised field is `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"] = "paragraph"`.** A clean corpus-agnostic hierarchical ladder. Ascending granularity from sentence (smallest) to chapter (largest). The shape matches the existing A1-A8 pattern (every axis a single coherent dimension; A6 is the closest analog as an ordinal preservation-level ladder).

- **Mechanism is hidden as AI implementation.** Default mechanism = the chunking finding's recommended hybrid harmony-aware approach: structural baseline at the chosen granularity + Tier-1-ambiguity heuristic + LLM-as-judge for flagged regions + fall back to structural where LLM uncertain. The AI applies this regardless of user choice. Users do not pick mechanism in normal use.

- **PipelineConfig optionally exposes mechanism override for advanced/eval use.** `chunking_mechanism_override: Literal["structural", "harmony-tier-aware", "passage-typology-aware", "llm-detected", "fixed-budget-with-snap", "hybrid"] | None = None`. None means use the default hybrid. Override values support empirical validation per chunking finding's deferred MUST. When `A6 ≥ light`, non-harmony-aware overrides are rejected at config-resolution time (A6 cascade preserved).

- **SourceDescriptor's `ChunkingUnit` gains a `canonical_level` field** that maps corpus-specific declared units to TC's canonical ladder. Nursi `mesele` → `subchapter`; Quran `ayah` → `sentence` (with `is_atomic=True`); Bible `verse` → `sentence`; Hindu `sloka` → `sentence`. When the AI translates with `chunking_granularity = subchapter` on Nursi corpus, output uses the declared name "mesele" rather than "subchapter."

- **A4-driven defaults are updated to type literals only.** Scholarly → `passage`; devotional → `subchapter` (works for Nursi mesele, Bible chapter-as-subchapter); casual → `paragraph` (unchanged); language-learning → `sentence` (unchanged); performance → `subchapter`. When A4 is silent, default chains through casual to `paragraph`.

- **Cross-cutting constraints survive unchanged.** Tier 1-2 preservation (HARD; absolute, applies to chunker output regardless of mechanism). Multi-meaning chunk-size lower bound (runtime invariant). A6 activation-gate cascade (now operates on PipelineConfig.chunking_mechanism_override, rejecting non-harmony-aware values when A6 ≥ light). Asymmetric-failure direction unchanged (under-chunking worse).

- **The chunking finding's recommended hybrid harmony-aware mechanism survives unchanged in behavior.** It is no longer a TC literal but the AI's hidden default. Same 4-step operation (structural baseline + heuristic + LLM-as-judge + fall-back). Same cost characteristics. Same empirical validation plan from the chunking finding — but the comparison set shifts: `structural` vs `hybrid` vs `harmony-tier-aware` are now PipelineConfig override values rather than TC literals.

- **Two LOOP_DIAGNOSE maintenance candidates are validated by this inquiry's existence.** **MC1** (Candidate-Self-Consistency sub-axis in td-critique) would have caught the conflation: the 8 enum literals make incompatible internal claims about what axis they describe — substance-axis prosecution applying each literal's own definition would have surfaced the categorical mismatch. **MC2** (Comparative-Pattern Test perspective in sense-making) would have caught it too: comparing `chunking_strategy` against A1-A8 shows that none of A1-A8 mix axes within one field; the user's pushback was exactly this comparative-pattern check. Two independent correction chains (edge-cases SD-vs-TC + chunking type-vs-mechanism) now back both MCs.

- **LOOP_DIAGNOSE's "chunking survived intact" framing was too strong.** The chunking finding's per-field routings (#1, #6, #7) survive — LOOP_DIAGNOSE's L1 claim stands. But the chunking finding's `chunking_strategy` enum had its own field-internal conflation that the chunking critique stage missed (no principle-application-correctness dimension; substance-axis missed the categorical mismatch). Same critique-stage failure pattern that LOOP_DIAGNOSE diagnosed in the edge-cases critique.

## Finding

### Why this matters (the goal context)

The Comprehenslate project has been progressively settling its translation configuration framework over several inquiries: the 8-axis TranslationConfig in earlier work; the chunking deep-dive that added `chunking_strategy` as a 9th axis with split-placement architecture; the edge-cases-into-config-schema inquiry that handled 14 edge-case fields; the LOOP_DIAGNOSE inquiry that diagnosed an SD-vs-TC misrouting in the edge-cases work.

The user noticed, on reading the chunking_strategy enum, that its 8 literals were not all on the same conceptual axis. Some named structural unit types (paragraph, sentence); others named mechanisms for finding chunks (LLM-detected, fixed-budget-with-snap). This is the same category-error pattern that LOOP_DIAGNOSE identified for the SD-vs-TC routing case: two distinct conceptual axes merged into one place.

The user's question is structural: produce a clean schema with the two axes separated. The inquiry's answer is operational: a hierarchical-ladder TYPE field on TC, mechanism hidden as AI implementation (with optional override on PipelineConfig), corpus-specific types mapped via SD's existing ChunkingUnit shape — all matching the existing A1-A8 single-axis pattern.

### 1. The conflation in the chunking_strategy enum

The chunking finding's `chunking_strategy: Literal[...]` field had 8 literals. Categorizing each by what it actually names:

| Old literal | What it actually names | Axis |
|---|---|---|
| `source-structural-unit` | A type-finding rule that resolves to a TYPE per SD declaration | TYPE (indirect) |
| `paragraph` | A TYPE of chunk (blank-line-bounded prose unit) | TYPE |
| `sentence` | A TYPE of chunk (smallest semantic unit) | TYPE |
| `harmony-tier-aware` | A MECHANISM (LLM-based; respects Tier 1 chains) | MECHANISM |
| `passage-typology-aware` | A MECHANISM (two-pass: classify type + chunk per type) | MECHANISM |
| `LLM-detected` | A MECHANISM (LLM identifies boundaries) | MECHANISM |
| `fixed-budget-with-snap` | A MECHANISM (token budget + snap to structural unit) | MECHANISM |
| `hybrid` | A COMPOSITION mechanism (combines multiple mechanisms) | MECHANISM |

Three types + five mechanisms in one enum. The user explicitly named the conflation: *"they are how to determine the chunk, but we are talking about what kind of chunks exist."*

This is the same category-error pattern that LOOP_DIAGNOSE diagnosed for the SD-vs-TC misrouting (where source-facts were merged with reader-properties and strategies in one schema home). Different conceptual axes should not be merged into one field — none of A1-A8 do this; the pattern is consistent across the existing schema.

### 2. The revised TC field — `chunking_granularity`

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
    - `sentence` — smallest semantic unit; fine-grained
    - `paragraph` — blank-line-bounded prose unit; common default
    - `passage` — thematic prose unit, potentially multi-paragraph
    - `subchapter` — numbered sub-section (Nursi mesele maps here;
       Bible chapter-as-subchapter; Quran hizb/juz)
    - `chapter` — top-level structural unit

    The AI's mechanism for producing chunks of this granularity is hidden
    by default (hybrid harmony-aware per the chunking finding). Advanced
    users may override via PipelineConfig.chunking_mechanism_override.

    Corpus-specific names: when SourceDescriptor declares a ChunkingUnit
    whose canonical_level matches the chosen granularity, the AI uses the
    declared name in output (e.g., 'mesele' instead of 'subchapter' for Nursi).
    """
```

The five literals form a strict nesting hierarchy by size: a chapter contains subchapters; a subchapter contains passages; a passage contains paragraphs; a paragraph contains sentences. This ordering is corpus-agnostic and matches how the user listed the literals in their pushback.

The shape matches A1-A8's existing pattern. A6 `form_preservation` is the closest analog — it is also an ordinal ladder (`off / minimal / light / standard / maximum`) where each level has a meaningful position relative to its neighbors. A1 `reader_level` is also ordinal. The chunking field now fits this pattern; chunking_strategy did not.

### 3. The default mechanism — hidden, hybrid harmony-aware

The chunking finding's recommended hybrid harmony-aware mechanism survives behaviorally unchanged. It is no longer a TC literal; it is the AI's default mechanism, applied regardless of the user's `chunking_granularity` choice.

Four-step operation:

1. **Structural baseline pass** using the SD's declared unit at the chosen `canonical_level`, or paragraph if no SD declaration exists at that level.
2. **Tier-1-ambiguity heuristic scan** — fast regex-style detection of cause-effect connectives, conditional chains, semantic-escalation patterns spanning candidate boundaries.
3. **LLM-as-judge on flagged regions only** — prompt context includes `harmony_layer.md` Tier 1-2 reference; returns `{decision: MERGE | KEEP | SPLIT, confidence: 0.0-1.0}`.
4. **Fall back to structural baseline** where LLM confidence < 0.7.

This is identical to the chunking finding's recommended approach in section 6 of that finding. The cost characteristics remain ~$10-20 per Risale-i-Nur-sized corpus with Opus, one-shot, cacheable. The empirical-validation plan from the chunking finding still applies; the comparison set is just expressed differently (PipelineConfig override values instead of TC literals).

### 4. The PipelineConfig mechanism override (optional)

```python
class PipelineConfig(BaseModel):
    # ... existing fields ...
    chunking_budget: int | None = None  # from chunking finding
    chunking_mechanism_override: Literal[
        "structural",
        "harmony-tier-aware",
        "passage-typology-aware",
        "llm-detected",
        "fixed-budget-with-snap",
        "hybrid",
    ] | None = None
    """Override the AI's default mechanism for chunk production.

    `None` (default) — AI uses `hybrid` harmony-aware (the recommended default).

    Setting an override is for advanced/evaluation use (e.g., comparing
    `hybrid` vs `structural` on a corpus for empirical validation).

    When `A6 ≥ light`, non-harmony-aware overrides (`structural`,
    `llm-detected`, `fixed-budget-with-snap`) are rejected at
    config-resolution time per the A6 activation-gate cascade.
    """
```

This field supports the chunking finding's deferred MUST item — comparative empirical validation of mechanisms on Nursi corpus. The user does not normally need this knob; it is for evaluation and advanced use.

### 5. The SourceDescriptor `canonical_level` field

```python
class ChunkingUnit(BaseModel):
    name: str                       # corpus-declared name
    detector: ChunkingDetector      # mechanism per declaration
    canonical_level: Literal[       # NEW: maps to TC's chunking_granularity
        "sentence",
        "paragraph",
        "passage",
        "subchapter",
        "chapter",
    ]
    is_atomic: bool = False
    attached_to: str | None = None
```

The `ChunkingUnit` already separated TYPE (name) from MECHANISM (detector) from PROPERTY (is_atomic) from RELATION (attached_to). The `canonical_level` field adds the mapping to TC's canonical ladder, completing the link.

**Per-corpus mappings:**

| Corpus | Declared unit | canonical_level | Notes |
|---|---|---|---|
| Nursi | Söz | `chapter` | top-level work |
| Nursi | Mektup (Letter) | `subchapter` | within Mektubat |
| Nursi | mesele | `subchapter` | numbered sub-arguments |
| Nursi | paragraph | `paragraph` | within mesele |
| Nursi | ayah (embedded Quranic citation) | `sentence` (is_atomic=True) | atomic; never split |
| Nursi | hashiye | `paragraph` (attached_to="paragraph") | travels with referent |
| Bible | book | `chapter` | top-level book |
| Bible | chapter | `subchapter` | within book |
| Bible | pericope | `passage` | thematic unit |
| Bible | verse | `sentence` | atomic-ish verse |
| Quran | sura | `chapter` | top-level chapter (size varies) |
| Quran | hizb / juz | `subchapter` | reading-unit divisions |
| Quran | ruku | `passage` | thematic group |
| Quran | ayah | `sentence` | atomic verse |
| Hindu | adhyaya | `subchapter` | numbered chapter |
| Hindu | sloka | `sentence` | atomic verse |

When the AI translates Nursi with `chunking_granularity = "subchapter"`, it sees the SD declaration for `mesele` at `canonical_level = "subchapter"` and uses "mesele" as the unit name in any output (apparatus, navigation, structural references). The user's chosen granularity is corpus-agnostic; the displayed name is corpus-specific.

### 6. A4-driven defaults revised

The chunking finding's A4-driven defaults referenced mechanism-literals (e.g., scholarly → `harmony-tier-aware`). Revised to reference type-literals only:

| A4 purpose | Old default | New default | Reasoning |
|---|---|---|---|
| `scholarly` | `harmony-tier-aware` (mechanism) | `passage` | Scholars work at thematic-passage level; mechanism is hybrid harmony-aware (the AI default) |
| `devotional` | `source-structural-unit` | `subchapter` | Devotional readers engage at natural source-unit level (Nursi mesele; Bible chapter-as-subchapter) |
| `casual` | `paragraph` | `paragraph` | Unchanged |
| `language-learning` | `sentence` | `sentence` | Unchanged |
| `performance` | `source-structural-unit` | `subchapter` | Performance follows declared structural units |

Default when A4 silent: `paragraph` (chains through casual). Unchanged.

### 7. Cross-cutting constraints

All three cross-cutting constraints from the chunking finding survive the redesign:

1. **Tier 1-2 preservation (HARD).** Chunker output that breaks a Tier 1 entry from `harmony_layer.md` is rejected. Applies to AI's mechanism output regardless of `chunking_granularity` or any PipelineConfig override.

2. **Multi-meaning chunk-size lower bound (runtime invariant).** When source contains polysemy whose disambiguation depends on local construction, the chunk must contain both. The AI may merge chunks below the user's chosen granularity to satisfy this.

3. **A6 activation-gate cascade.** When `A6 ≥ light`, the mechanism MUST be harmony-tier-aware. The default `hybrid` satisfies this. Non-harmony-aware PipelineConfig overrides (`structural`, `llm-detected`, `fixed-budget-with-snap`) are rejected at config-resolution time when A6 ≥ light. The user receives a warning explaining the constraint with the option to lower A6.

Asymmetric-failure direction unchanged: under-chunking (chunks too large) is structurally worse than over-chunking. The mechanism MUST over-chunk under uncertainty.

### 8. LOOP_DIAGNOSE maintenance candidates validated

This inquiry's existence and outcome strengthen both maintenance candidates from the LOOP_DIAGNOSE finding.

**MC1 (Candidate-Self-Consistency sub-axis in td-critique).** Would have caught the chunking_strategy conflation. The 8 literals make incompatible internal claims about what axis they describe — `paragraph` claims to name a structural unit; `LLM-detected` claims to name a detection mechanism; these are different ontological categories. Substance-axis prosecution applying each literal's own definition against the enum's claimed axis would have surfaced the categorical mismatch. Evidence-strength: HIGH. Now backed by TWO independent smoking-gun cases (edge-cases P3 docstring vs chunking_strategy enum literals).

**MC2 (Comparative-Pattern Test perspective in sense-making).** This inquiry IS its first cross-domain branch-test, and the test fired and caught the conflation. The user performed exactly the comparative-pattern check that MC2 describes: comparing `chunking_strategy` against A1-A8 and noticing that A1-A8 don't mix axes while chunking_strategy does. Evidence-strength: HIGH; MC2's evaluation gate is being MET. Two of two correction chains have produced applicable cases.

**Promotion case.** Both MCs now have evidence from two independent inquiries. Recommended next step: one more branch-test on a non-chunking-related inquiry (per the Routelister R8/R9 routes) before promoting to canonical specs. This provides three-case validation (edge-cases SD-vs-TC + chunking type-vs-mechanism + a future non-chunking case) before changing the canonical td-critique and sense-making specs.

### 9. LOOP_DIAGNOSE's "chunking survived intact" framing was too strong

The LOOP_DIAGNOSE finding said: *"The chunking inquiry's framework is the surviving canonical answer; the LOOP_DIAGNOSE only touched the edge-cases inquiry's downstream misapplication."* This framing was too broad.

The chunking finding's per-field routings (#1, #6, #7) survive — LOOP_DIAGNOSE's L1 claim stands and is confirmed by this inquiry's re-test. But the chunking finding's `chunking_strategy` enum had its own field-internal conflation that the chunking critique stage missed. Same critique-stage failure pattern that LOOP_DIAGNOSE diagnosed in the edge-cases critique (no principle-application-correctness dimension; substance-axis missed an internal categorical mismatch).

The corrective: add a note to LOOP_DIAGNOSE's finding (per Routelister R2) explicitly distinguishing routings-correct (stands) from survived-intact (too strong). The MC1+MC2 evidence base strengthens because of this case.

## Inherited Commitments Re-test

(See section 7 of the Finding above. The Synthesis Trigger requires per-commitment re-test.)

In summary: 10 chunking finding commitments re-tested (8 confirmed; 1 confirmed-with-revision; 1 INVALID — the `chunking_strategy` 8-literal enum, replaced). 5 LOOP_DIAGNOSE commitments re-tested (3 confirmed-with-strengthening; 1 confirmed; 1 INVALID — the "survived intact" framing). No commitment silently absorbed.

## Next Actions

### MUST

- **What.** Add a Correction Notice at the top of the chunking finding (`devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`) citing this revision. Note that `chunking_strategy` is replaced by `chunking_granularity` (5-literal hierarchical ladder) and the 5 mechanism literals are re-homed (default: hidden; advanced: PipelineConfig override).
  **Who.** Finding-text maintenance.
  **Gate.** Time-bound — before this finding is referenced as canonical.
  **Why.** Future readers should see the revision; preserve original content as diagnostic-trail.

- **What.** Add an Update note to the LOOP_DIAGNOSE finding (`devdocs/inquiries/2026-06-14_02-29__loop_diagnose__sd_vs_tc_misrouting/finding.md`) Summary distinguishing routings-correct (stands) from survived-intact (too strong).
  **Who.** Finding-text maintenance.
  **Gate.** Time-bound — bundle with chunking finding correction notice.
  **Why.** The "survived intact" framing was too broad; honest scoping prevents mis-citation.

- **What.** Update the chunking section of `config_base_source.md` to describe `chunking_granularity` (5-literal hierarchical ladder), the hidden default mechanism, the PipelineConfig override option, the SD `canonical_level` field, and the revised A4-driven defaults.
  **Who.** Documentation maintenance.
  **Gate.** Time-bound — bundle with finding-text updates.
  **Why.** `config_base_source.md` is the AI's calibration context; it must reflect the revised schema.

- **What.** Replace `chunking_strategy` field with `chunking_granularity` in `translation_config.py`.
  **Who.** Schema implementation.
  **Gate.** Observable — when schema code work begins.
  **Why.** Brings the implementation in line with the revised design.

- **What.** Add `canonical_level: Literal[...]` field to `ChunkingUnit` in `source_descriptor.py` (when that file is created per the chunking finding's MUST item). Declare the Nursi-specific corpus mappings (mesele=subchapter, ayah=sentence with is_atomic, hashiye=paragraph with attached_to, paragraph=paragraph, Söz=chapter).
  **Who.** Schema implementation + Nursi-familiar reviewer.
  **Gate.** Condition-bound — when SourceDescriptor schema is created.
  **Why.** Completes the type-to-corpus mapping; unblocks the 4_mesele translation work using mesele-level chunking.

- **What.** Add `chunking_mechanism_override: Literal[...] | None = None` field to `PipelineConfig` (when that file is created per the chunking finding's MUST item). Implement A6 cascade rejection at config-resolution time.
  **Who.** Schema implementation.
  **Gate.** Condition-bound — when PipelineConfig is created.
  **Why.** Supports empirical-validation work (comparing mechanisms) and advanced use.

- **What.** Update the in-flight 4_mesele translation work to use `chunking_granularity = "subchapter"` (which resolves to "mesele" via Nursi SD declaration).
  **Who.** Translation workflow.
  **Gate.** Condition-bound — depends on schema-code MUSTs.
  **Why.** Propagates the correction to actual translation work end-to-end.

### COULD

- **What.** Branch-test MC1 (Candidate-Self-Consistency sub-axis) on the next non-chunking-related inquiry's critique.
  **Who.** Future inquiry's critique stage.
  **Gate.** Condition-bound — when such an inquiry runs.
  **Why.** Extends MC1 validation beyond chunking-adjacent cases; provides three-case evidence before canonical promotion.

- **What.** Branch-test MC2 (Comparative-Pattern Test perspective) on the next non-chunking-related inquiry's sensemaking.
  **Who.** Future inquiry's sensemaking stage.
  **Gate.** Condition-bound — when such an inquiry runs.
  **Why.** Same as MC1 branch-test for sense-making.

- **What.** Promote MC1 to the canonical td-critique spec after a successful non-chunking branch-test.
  **Who.** td-critique spec maintainer.
  **Gate.** Condition-bound — when MC1's non-chunking branch-test catches at least one issue.
  **Why.** Promotion with three-case evidence (edge-cases + chunking + one more) is more robust than two-case.
  **Depends-on.** COULD item "Branch-test MC1 on non-chunking inquiry." This COULD is GATED.

- **What.** Promote MC2 to the canonical sense-making spec after a successful non-chunking branch-test.
  **Who.** sense-making spec maintainer.
  **Gate.** Condition-bound — when MC2's non-chunking branch-test catches at least one issue.
  **Why.** Same as MC1 promotion.
  **Depends-on.** COULD item "Branch-test MC2 on non-chunking inquiry." This COULD is GATED.

### DEFERRED

- **What.** Use `IntEnum` instead of `Literal` for `chunking_granularity` to encode the hierarchical ordering at the type-system level.
  **Gate.** Revival trigger — if downstream code needs to compare granularities programmatically (e.g., "is the chunk smaller than subchapter?") and current docstring-based ordering proves insufficient.
  **Why (if revived).** Type-safe ordering. Currently a Literal works because A1-A8 use Literal; pattern-consistency favors Literal now.

- **What.** Empirical validation of chunking mechanisms on Nursi corpus (`structural` vs `hybrid` vs `harmony-tier-aware` via PipelineConfig override).
  **Gate.** Condition-bound — per the chunking finding's deferred MUST item.
  **Why (if revived).** Confirms the hybrid harmony-aware default's quality; informs whether `structural` is enough.

## Reasoning

The structurally non-obvious decisions in this finding had alternatives that were considered and rejected.

**Why a hierarchical ladder, not a flat enum.** The user listed paragraph + sentence + passage + chapter + subchapter without explicit ordering, but the SET forms a strict nesting hierarchy by granularity. A flat enum loses this ordering. The existing A6 axis (`off / minimal / light / standard / maximum`) is also a strict ordinal ladder; using the same shape for chunking matches the existing pattern. A hierarchical ladder also enables future ordering-based behavior (e.g., "use granularity finer than the chosen one if Tier 1 demands").

**Why mechanism is hidden, not user-visible.** Three reasons: (1) user value is low — most users have no basis to choose between LLM-detected and harmony-tier-aware; the right default (hybrid harmony-aware) is uniform across reasonable use cases. (2) Anti-bloat — 5 mechanism literals on a user-facing field violate the user's preference for minimal user surfaces, with no offsetting user-value gain. (3) Pattern consistency — none of A1-A8 expose mechanism on the user-config surface; mechanism is implementation. The PipelineConfig override exists for advanced/evaluation needs without contaminating the main user-config surface.

**Why corpus-specific types live on SourceDescriptor, not TranslationConfig.** Corpus-specific types (mesele, ayah, sloka) are corpus properties (per chunking finding's split-placement principle). Routing them through TC's user-facing enum reintroduces the SD-vs-TC conflation that LOOP_DIAGNOSE diagnosed. The clean separation: TC's enum is corpus-agnostic canonical; SD declares per-corpus types via existing ChunkingUnit and maps to canonical via the new `canonical_level` field.

**Why the chunking finding's hybrid mechanism is preserved unchanged in behavior.** The chunking finding's recommended hybrid harmony-aware approach is structurally correct — it preserves Tier 1, integrates with the SD-declared structural units, is cacheable, and has been argued for at length. The redesign re-homes hybrid (from a TC literal to the AI's hidden default) without altering its operation. The empirical validation plan still applies; the comparison set is just expressed as PipelineConfig overrides rather than TC literals.

**Why this isn't a meta-loop framework failure.** The LOOP_DIAGNOSE finding's analysis of the chunking critique's failure pattern (no principle-application-correctness dimension; substance-axis missed internal contradictions) applies here too. The chunking critique stage missed THIS conflation just as the edge-cases critique missed the SD-vs-TC conflation. Same critique-stage pattern across two cases. The framework's disciplines are structurally capable; the application is what fails. MC1 and MC2 from LOOP_DIAGNOSE both target this pattern; both are now backed by two independent cases.

**Why the LOOP_DIAGNOSE "survived intact" framing weakens.** LOOP_DIAGNOSE specifically attributed the SD-vs-TC misrouting to the edge-cases inquiry and confirmed chunking's per-field routings as correct. That attribution stands. But the finding's broader framing ("the chunking inquiry's framework is the surviving canonical answer") was too sweeping — chunking_strategy enum was a different KIND of failure than the routings (field-internal conflation rather than misrouting between schemas), and the chunking critique missed it. The corrective is a narrow note distinguishing routings-correct (stands) from survived-intact (too strong), per Routelister R2.

**Self-Reference Blindness — actively mitigated.** This is the second consecutive inquiry where the AI's prior work is being critically re-examined. The mitigation pattern: user pushback is the trigger (not AI self-discovery); the AI's role is to systematize the user's intuition; the critique stage explicitly applies MC1 + MC2 to its own outputs (the Candidate-Self-Consistency check fires on this inquiry's own enum literals; the Comparative-Pattern Test fires on this inquiry's own field shape). Residual blind spot: aspects neither pushed back on nor independently verified may carry undetected error.

## Open Questions

### Monitoring

- After the schema code lands, observe whether the `chunking_granularity` hierarchical-ladder shape produces sensible AI behavior in 4_mesele translation (e.g., does `subchapter` properly resolve to "mesele" in output?).
- After the SD `canonical_level` field is declared for Nursi corpus, observe whether the AI correctly uses "mesele" instead of "subchapter" in apparatus/output text.
- After the next non-chunking inquiry runs MC1 or MC2 branch-test, observe whether the maintenance candidate catches an issue. If yes: promotion case strengthens further.

### Blocked

- Phase 2 schema code is blocked until the chunking finding's SourceDescriptor and PipelineConfig MUSTs ship.
- MC promotion to canonical specs is blocked on a non-chunking-related branch-test.
- Empirical validation of mechanisms is blocked on schema code + Nursi-familiar gold-standard preparation.

### Research Frontiers

- Whether `IntEnum` for granularity ordering would provide enough value to switch from `Literal`. Currently the pattern-consistency argument favors Literal; future code-ergonomics issues might revisit.
- Whether other inquiries in the project's history have similar type-vs-mechanism conflations that have not yet been challenged. An audit per Routelister could be valuable but is currently low-priority.
- Whether the hierarchical ladder should include levels above `chapter` (e.g., `book`, `corpus`) for multi-document use. The current scope is single-document; multi-document is deferred per the chunking finding's deferred research items.

### Refinement Triggers

- If a non-chunking branch-test of MC1 or MC2 catches a third independent case, promote to canonical spec immediately (don't wait for further evidence).
- If the AI's default hybrid mechanism produces issues at specific `chunking_granularity` levels (e.g., `passage` produces inconsistent boundaries), revisit the default behavior per granularity.
- If a corpus is added whose natural units don't map cleanly to the canonical ladder (e.g., a corpus with only `book` and `paragraph` levels), revisit whether canonical_level needs an `unmapped` / `corpus-specific` literal.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
I think these are bad 

Paragraph yes  this is good
Sentence yes this is good
Passage
Chapter
Subchapter


These are fundemanral ones i guess

Llm detected 
Fixed budget etc doesnt make snese

Bc they are how to determine the chunk, but we are talking about what kind of chunks exist

Lets dive deep into this updated logic
```

</details>
