# Surfacing — Chunk Types vs Mechanisms

## User Input

Input: `_branch.md` + `articulate_simple.md`. Synthesis priors: chunking finding (under revision) + LOOP_DIAGNOSE finding (MC2 first branch-test).

---

## Mode + Entry Point + Reception

- **Mode:** artifact-dominant — territory contains the chunking finding's current 8-literal enum + LOOP_DIAGNOSE MC2 + the existing TC + the existing SD's ChunkingUnit shape; some possibility (the new enum design).
- **Entry point:** signal-first — explicit purpose received.
- **Territory specification:** explicit-bounded — the chunking_strategy enum redesign scope.
- **Sub-phase fired:** NO.
- **Purpose echo:** revise the chunking_strategy enum based on type-vs-mechanism distinction; validate LOOP_DIAGNOSE MC2 in the process.

---

## Traversal Trace

### Region R1 — The current 8-literal enum (under revision)

| # | Item | Category (per user) | Relevance | Note |
|---|---|---|---|---|
| 1 | `source-structural-unit` | TYPE (uses corpus's declared unit) | **core** | The category-membership of this literal is ambiguous — it names a type-finding-rule, but resolves to a type per SD |
| 2 | `paragraph` | TYPE ✓ | **core** | User-approved type |
| 3 | `sentence` | TYPE ✓ | **core** | User-approved type |
| 4 | `harmony-tier-aware` | MECHANISM | **core** | User didn't name it explicitly but by their logic it's a mechanism (HOW to detect: respect Tier 1 chains) |
| 5 | `passage-typology-aware` | MECHANISM | **core** | User-approved `passage` AS A TYPE but `passage-typology-aware` is a STRATEGY (classify type + chunk per type) — mechanism |
| 6 | `LLM-detected` | MECHANISM (user-rejected) | **core** | Explicit MQ4 exclusion |
| 7 | `fixed-budget-with-snap` | MECHANISM (user-rejected) | **core** | Explicit MQ4 exclusion |
| 8 | `hybrid` | MECHANISM (compound) | **core** | A combination-of-mechanisms; clearly not a type |

**Pattern visible:** 3 types (paragraph, sentence, source-structural-unit) + 5 mechanisms (the rest). The enum systematically mixes the two axes.

### Region R2 — User-named "fundamental" types

| # | Item | Relevance | Note |
|---|---|---|---|
| 9 | sentence | **core** | Granularity: smallest semantic unit |
| 10 | paragraph | **core** | Granularity: blank-line-bounded prose unit |
| 11 | passage | **core** | Granularity: thematic prose unit (potentially multi-paragraph) |
| 12 | subchapter | **core** | Granularity: numbered sub-section |
| 13 | chapter | **core** | Granularity: top-level structural unit |

**Pattern visible:** these form a STRICT NESTING HIERARCHY by granularity — chapter > subchapter > passage > paragraph > sentence. The hierarchy is corpus-agnostic (works for most prose corpora).

### Region R3 — Corpus-specific types (already declared in SourceDescriptor)

| # | Item | Relevance | Note |
|---|---|---|---|
| 14 | Nursi corpus units: mesele / paragraph / ayah (atomic) / hashiye (attached) — declared via `SourceDescriptor.source_chunking_units: list[ChunkingUnit]` per chunking finding | **core** | The SD already separates `ChunkingUnit.name` (TYPE) from `ChunkingUnit.detector` (MECHANISM) and `ChunkingUnit.is_atomic` (PROPERTY) |
| 15 | Bible analog: verse / pericope / chapter / book | sub | Pattern transfer |
| 16 | Quran analog: ayah / ruku / hizb / juz / sura | sub | Pattern transfer |
| 17 | Hindu scripture: sloka / adhyaya | sub | Pattern transfer |

**Pattern visible:** corpus-specific types exist BESIDE canonical types (paragraph/sentence/passage/...). Mesele is Nursi's term for "subchapter-like sub-argument unit." Ayah is "sentence-like atomic verse unit."

### Region R4 — Mechanisms (the orthogonal axis)

| # | Item | Relevance | Note |
|---|---|---|---|
| 18 | structural-detection (regex on punctuation / blank-lines / heading markers) | **core** | Free; deterministic; produces sentence/paragraph/heading-derived types |
| 19 | LLM-detected (single-pass LLM identifies boundaries) | **core** | LLM-based; produces any type; needs prompt context |
| 20 | harmony-tier-aware (preserve Tier 1 chains while chunking) | **core** | LLM-based with harmony_layer context; CONSTRAINT MECHANISM not a TYPE |
| 21 | passage-typology-aware (classify passage type + chunk per type) | **core** | Two-pass LLM mechanism; produces passage-type-labeled chunks |
| 22 | fixed-budget-with-snap (token budget bounded; snap to nearest structural unit) | **core** | Free; deterministic; mechanism for runtime-constrained chunking |
| 23 | hybrid (structural baseline + LLM-as-judge for ambiguous regions) | **core** | The chunking finding's recommended OPERATIONAL DEFAULT — it's a mechanism, not a type |
| 24 | corpus-specific-detector (the ChunkingUnit.detector callable per SD declaration) | **core** | Already exists in SD as a mechanism slot |

**Pattern visible:** mechanisms form a separate enumeration. The chunking finding's recommended `hybrid` is a mechanism, not a type — currently misclassified in the same enum as types.

### Region R5 — LOOP_DIAGNOSE MC2 (Comparative-Pattern Test perspective)

| # | Item | Relevance | Note |
|---|---|---|---|
| 25 | MC2 spec: "When the inquiry commits a structural decision (schema home, axis assignment, routing), explicitly compare each candidate against the existing pattern of analogous decisions in the target scheme" | **core** | The exact test the user just performed independently |
| 26 | MC2 evaluation gate: "Branch-test on the next bulk-edge-case inquiry. Observe whether the new perspective fires per structural decision and whether it surfaces any routing inconsistency. If fired and catches: PROMOTE" | **core** | This inquiry IS that branch-test. The test FIRED (user comparison: A1-A8 don't mix axes; chunking_strategy does) and CAUGHT the conflation. Evidence for MC2 promotion |
| 27 | User's reasoning shape: "paragraph yes — this is good (TYPE); LLM detected doesn't make sense (HOW to determine) — different axes" | **core** | The user's mental model is exactly Comparative-Pattern Test. They compared each literal against the others and noticed they aren't on one axis |

**Pattern visible:** the user just demonstrated MC2 in action without naming it. This inquiry's existence provides strong evidence that MC2 catches a real category of failure — even without spec change, human application of MC2 catches what the loop's official disciplines missed.

### Region R6 — Existing TC axes as comparative evidence

| # | Item | Relevance | Note |
|---|---|---|---|
| 28 | A1 reader_level: very_basic / daily / conversational / advanced / native — pure ordinal granularity of READER capability | **core** | Single axis: reader-capability-level |
| 29 | A4 purpose: scholarly / devotional / casual / language-learning / performance — pure use-case classes | **core** | Single axis: use-case-class |
| 30 | A5 source_fidelity: foreignized-max / foreignized / balanced / lightly-domesticated — pure ordinal positional on a spectrum | **core** | Single axis: strategy-position |
| 31 | A6 form_preservation: off / minimal / light / standard / maximum — pure ordinal preservation-level | **core** | Single axis: preservation-level |

**Pattern visible:** NONE of A1-A8 mix two axes within one field. Each axis has a coherent single dimension. Chunking_strategy's mixed-axis design is structurally inconsistent with the rest of TC.

### Region R7 — SourceDescriptor.ChunkingUnit existing structure (informative)

| # | Item | Relevance | Note |
|---|---|---|---|
| 32 | `ChunkingUnit.name: str` — the TYPE label ("mesele", "paragraph", "ayah") | **core** | SD already has a type-axis slot per declared unit |
| 33 | `ChunkingUnit.detector: ChunkingDetector` — the MECHANISM (how to find this unit) | **core** | SD already has a mechanism-axis slot per declared unit |
| 34 | `ChunkingUnit.is_atomic: bool` — a PROPERTY of the unit | **core** | Third axis: per-unit property (parallel to type and mechanism) |
| 35 | `ChunkingUnit.attached_to: str \| None` — a RELATIONAL PROPERTY | **core** | Fourth axis: relational property |

**Pattern visible:** SD's existing ChunkingUnit shape ALREADY separates type from mechanism from property from relation. The chunking finding's `chunking_strategy` field on TC did NOT inherit this separation — it merged type and mechanism into one enum. SD's shape is the comparative pattern that catches the misdesign.

### Region R8 — Schema-shape candidates (possibility — to be evaluated downstream)

| # | Item | Relevance | Note |
|---|---|---|---|
| 36 | Single field `chunking_type: Literal[...]` (TC) + mechanism hidden as internal AI choice | **core** | Variant 3 candidate |
| 37 | Two fields `chunking_type` + `chunking_mechanism` on TC | **core** | Variant 2 candidate |
| 38 | Single hierarchical `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]` (TC) | **core** | Variant 4 candidate; explicit granularity ladder |
| 39 | TC has type field; corpus-specific types declared in SD; the TC enum includes `corpus-declared-top-unit` literal that resolves via SD | **core** | Variant 5 candidate; integrates with existing SD |
| 40 | Delete the field entirely; mechanism is internal; chunk type is implicit from SD's top declared unit | sub | More radical variant |

### Region R9 — Cross-axis interactions (which mechanism produces which type)

| # | Item | Relevance | Note |
|---|---|---|---|
| 41 | structural-detection PRODUCES paragraph, sentence, heading-derived types | sub | Many-to-one mechanism-to-type |
| 42 | LLM-detected can PRODUCE any type the prompt specifies | sub | Universal mechanism |
| 43 | harmony-tier-aware is a CONSTRAINT on output, not a type-producer (works alongside another mechanism) | **core** | A modifier, not a primary mechanism — different kind of mechanism |
| 44 | fixed-budget-with-snap is a CONSTRAINT mechanism (size cap) that snaps to a TYPE | sub | Constraint + selection |
| 45 | hybrid is a COMPOSITION of mechanisms | sub | Meta-mechanism |
| 46 | corpus-specific-detector (SD's ChunkingUnit.detector) PRODUCES the named declared unit | **core** | One-to-one mechanism-to-declared-type |

**Pattern visible:** mechanisms have sub-categories: PRIMARY (produces chunks) / CONSTRAINT (modifies primary's output) / COMPOSITION (combines multiple). The user-rejected literals were a mix of these.

---

## State Summary

### Coverage map

| Region | Coverage | Aggregate relevance |
|---|---|---|
| R1 — current 8-literal enum | confirmed | core (8 items; categorical-membership analyzed per literal) |
| R2 — user-named types | confirmed | core (5 types forming nesting hierarchy) |
| R3 — corpus-specific types | confirmed | core (Nursi + Bible + Quran + Hindu analogs) |
| R4 — mechanisms | confirmed | core (7 mechanisms; sub-categorized PRIMARY/CONSTRAINT/COMPOSITION) |
| R5 — LOOP_DIAGNOSE MC2 | confirmed | core (this inquiry is MC2's first branch-test) |
| R6 — existing TC axes comparative | confirmed | core (none mix axes — chunking_strategy violates the pattern) |
| R7 — SD's existing ChunkingUnit | confirmed | core (already separates type/mechanism/property — informative precedent) |
| R8 — schema-shape candidates | confirmed | core (5 candidates) |
| R9 — cross-axis interactions | confirmed | core (mechanism sub-categories surfaced) |

### Concept-names list

- **type-vs-mechanism conflation** — the category error in chunking_strategy enum
- **nesting hierarchy of chunk types** — chapter > subchapter > passage > paragraph > sentence (corpus-agnostic ladder)
- **corpus-specific types beside canonical types** — Nursi: mesele; Bible: verse/pericope; Quran: ayah/ruku/hizb/juz; Hindu: sloka
- **mechanism sub-categories** — PRIMARY (produces) / CONSTRAINT (modifies) / COMPOSITION (combines)
- **MC2 first branch-test** — this inquiry validates the Comparative-Pattern Test perspective from LOOP_DIAGNOSE
- **SD's ChunkingUnit pattern** — name (TYPE) + detector (MECHANISM) + is_atomic (PROPERTY) + attached_to (RELATION) — the comparative pattern showing axis separation already exists in the substrate
- **TC mixed-axis violation** — chunking_strategy is the ONLY field in TC that mixes axes; A1-A8 are clean
- **`hybrid` misclassified** — currently labeled as a strategy literal but is a mechanism-composition; the chunking finding's recommended operational default is mechanism, not type
- **TWO-AXIS-RECOGNITION** — the MQA-surface axis preserved from articulate_simple

### Frontier flags

1. **Schema-shape decision:** 5 viable candidates (R8 #36-#40); sensemaking must adjudicate which the right architecture is.
2. **Hybrid's home:** the recommended operational default `hybrid` is a mechanism; where does it live in the revised schema?
3. **Mechanism user-visibility:** should user pick mechanism (Variant 2) or AI choose internally (Variant 3)?
4. **Hierarchical-ladder vs flat-enum:** chunk types form a strict nesting hierarchy (R2); should the schema encode this (Variant 4) or treat as flat enum?
5. **SourceDescriptor integration:** the existing ChunkingUnit name/detector split (R7) is informative; should TC's revised field directly reference SD's declared units, or maintain a corpus-agnostic canonical set, or both?
6. **A4-driven defaults revision:** the chunking finding's A4 matrix had mechanism-literals as defaults (scholarly → `harmony-tier-aware`); revised A4 defaults need to specify either type only or type + mechanism.
7. **The chunking finding's "survived intact" claim from LOOP_DIAGNOSE is now CHALLENGED.** LOOP_DIAGNOSE said chunking commitments survived; this inquiry shows chunking_strategy has a conflation. LOOP_DIAGNOSE attribution may need revision (the chunking critique missed THIS conflation too — same critique stage as edge-cases critique missed the SD-vs-TC conflation).
8. **MC2's evaluation gate is being met right now.** Per LOOP_DIAGNOSE evaluation gate: "if MC2 fires and catches at least one issue: PROMOTE." This inquiry IS the branch-test and MC2 IS catching an issue. The maintenance candidate's evidence strengthens.

---

## Telemetry

- Mode: artifact-dominant + possibility | Entry: signal-first
- Items tagged: 46
- Tag distribution: 36 core + 9 sub + 1 side
- Cycles: 1
- Convergence: YES
- LAYER 1 failure modes: NONE fired

### Self-Assessment Verdict

**PROCEED**

Strong evidence base: every literal in the current enum categorized; nesting hierarchy of types surfaced; mechanism sub-categories identified; SD's existing pattern provides comparative evidence; MC2 evaluation gate is being met. 8 frontier flags for sensemaking including the recursive observation that LOOP_DIAGNOSE's "chunking survived intact" claim is now challenged.
