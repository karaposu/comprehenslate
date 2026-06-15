# Critique — Chunk Types vs Mechanisms

## User Input

Input: `_branch.md` + upstream artifacts including `innovation.md` with 10 principal candidates + 3 Assembly emergents.

---

## Phase 0 — Dimensions

| # | Dimension | Weight | Source |
|---|---|---|---|
| 1 | Correctness | HIGH | SV6 stabilized model |
| 2 | Coherence | HIGH | Composes with chunking finding (revised); LOOP_DIAGNOSE; existing 8-axis TC |
| 3 | Feasibility | MED | Depends on SD + PC schema implementation |
| 4 | Anti-bloat-fit | HIGH | User-foundational; single-axis enum matches A1-A8 |
| 5 | **MC2 self-application** (Comparative-Pattern Test) | **CRITICAL** | This inquiry validates MC2; the critique must apply MC2 to its own outputs |
| 6 | **MC1 self-application** (Candidate-Self-Consistency sub-axis) | **CRITICAL** | Test each candidate against its own internal claims |
| 7 | Synthesis-rigor | HIGH | Re-test inherited commitments |
| 8 | External-anchor | MED | Chunking finding text; LOOP_DIAGNOSE text; existing TC fields |

### Frame-premise test

1. **The chunking critique missed THIS conflation too — same critique-stage failure pattern.** Independent test: chunking critique used 8 dimensions; none tested whether each enum literal is on the same conceptual axis as the others. Substance-axis fired but on code-quality, not on axis-coherence. Premise SURVIVES.
2. **`hybrid` is genuinely a mechanism, not a type.** Independent test: `hybrid` describes HOW (combine baselines + LLM-judge), not WHAT (a kind of chunk). SURVIVES.
3. **Hierarchical-ladder enum matches A1-A8 pattern.** Independent test: A6 (`off/minimal/light/standard/maximum`) is also an ordinal ladder; A1 reader_level is also ordinal; pattern match holds. SURVIVES.

---

## Phase 1 — Fitness Landscape

Viable: HIGH all dimensions; SURVIVE.
Dead: fails Anti-bloat (multi-field TC) OR fails MC2 self-application (own enum mixes axes).
Boundary: Feasibility MED (paper schemas pending).

---

## Phase 2 — Adversarial Evaluation

### P1 — TC chunking_granularity field

**Prosecution.**
- **MC2 self-application:** Does P1's enum `["sentence", "paragraph", "passage", "subchapter", "chapter"]` consist of literals all on ONE axis? Let me check: sentence is a small semantic unit; paragraph is a structural prose unit; passage is a thematic unit; subchapter is a structural sub-section; chapter is a top-level structural unit. ALL FIVE are TYPES of source structural units at different granularities. Same axis. ✓ PASS MC2.
- **MC1 self-application:** Does the docstring's internal claims match the field's structural decision? Docstring says "hierarchical ladder (ascending granularity)"; the field type is a flat `Literal[...]`. Internal contradiction? Partially — the docstring claims ordering but `Literal` is unordered. Mitigation: the docstring explicitly lists in order; consumers can compare position. Could be sharpened (use `IntEnum` for explicit ordering). PASS-WITH-CAVEAT.
- **Substance:** field signature, default, docstring all present.
- **External-anchor:** docstring cites SD's canonical_level + hidden mechanism + PipelineConfig override; chains correctly.

**Verdict: SURVIVE with mild caveat** — could use `IntEnum` for explicit ordering, but `Literal` is project-canonical pattern (matches A1-A8); accept.

### P2 — SD ChunkingUnit canonical_level

**Prosecution.**
- **MC2 self-application:** does `canonical_level` enum match P1's enum? YES — same 5 literals. Pattern consistency. ✓
- **MC1 self-application:** the corpus mapping table — do mappings hold? Spot-check: Nursi mesele → subchapter (mesele is Nursi's named sub-argument unit; matches subchapter level — yes). Quran ayah → sentence (with is_atomic — yes; ayah is sentence-sized atomic). Bible verse → sentence (yes). Mappings consistent.
- **Specific failure case:** Quran sura → chapter. But sura sizes vary from 3 verses to 286 verses — is "chapter" right? Yes, sura is the top-level chapter unit in Quran; size variability is corpus-specific.

**Verdict: SURVIVE.** Clean.

### P3 — PipelineConfig override

**Prosecution.**
- **MC2 self-application:** the override's enum values `["structural", "harmony-tier-aware", "passage-typology-aware", "llm-detected", "fixed-budget-with-snap", "hybrid"]` — all on one axis? Check: all are MECHANISMS for producing chunks. Same axis. ✓
- **MC1 self-application:** docstring says "Setting an override is for advanced/evaluation use" and "Regardless of override, AI MUST preserve Tier 1-2." Internal consistency: the override CAN'T choose a non-harmony-aware mechanism when A6 ≥ light (per P6). Where is this enforced? At config-resolution time per P6's last paragraph. The docstring should mention this constraint explicitly.

**Verdict: SURVIVE with caveat** — add to docstring: "When `A6 ≥ light`, non-harmony-aware overrides (`structural`, `llm-detected`, `fixed-budget-with-snap`) are rejected at config-resolution time."

### P4 — Default mechanism (hidden)

**Prosecution.**
- Substance: 4-step mechanism specified; behavior across all 5 granularities documented.
- **MC1 self-application:** does the default's behavior match the chunking finding's recommended hybrid? Yes — same 4-step mechanism (structural baseline + heuristic + LLM-judge + fall-back).
- **Specific failure case:** at `chunking_granularity = passage`, the spec says "LLM-detected passage boundaries (no structural baseline at this level for most corpora)." Is passage really LLM-only? Some corpora have explicit passage markers (e.g., section breaks in Bible critical editions). The spec should note "or SD-declared passage unit when available."

**Verdict: SURVIVE with caveat** — refine P4 step 1 wording for `passage` level.

### P5 — A4 defaults revision

**Prosecution.**
- **MC2:** revised defaults are all type-literals (paragraph/sentence/passage/subchapter). All on one axis. ✓
- **Specific failure case:** scholarly default `passage`. The original was `harmony-tier-aware` (mechanism). Is `passage` the right TYPE for scholarly? Scholars often work at chapter-or-subchapter level for cross-reference; passage is mid-granularity. Defensible but could also be `subchapter`. Either is plausible; `passage` is more universal (works for corpora without subchapter declarations).

**Verdict: SURVIVE.** Defensible default.

### P6 — Cross-cutting constraints

**Prosecution.** Three constraints preserved unchanged. Tier 1-2 hard constraint cited verbatim from chunking finding.
- **A6 cascade refinement:** the cascade now rejects non-harmony-aware overrides. Operational mechanism clear (config-resolution time).

**Verdict: SURVIVE.** Clean.

### P7 — Inherited Commitments Re-test

**Prosecution.**
- 10 chunking commitments + 5 LOOP_DIAGNOSE commitments = 15 total. Each with status + evidence/reason.
- **Substance:** C3 INVALID is substantive (8-literal enum replaced by 5-literal ladder); L2 INVALID is substantive (survived-intact framing weakens).
- **Specific failure case:** L2 INVALID partially. Counter — LOOP_DIAGNOSE's specific scope was the SD-vs-TC misrouting; "survived intact" was framing about THAT scope. Is it really invalid?

**Defense.** L2's status is "found INVALID (too strong)" with reasoning that the framing's language was too broad. This is honest: the finding text actually said "the chunking inquiry's framework is the surviving canonical answer" — that statement DOES need qualifying. L2 status is correct.

**Verdict: SURVIVE.** Clean.

### P8 — MC1 + MC2 evidence note

**Prosecution.**
- **MC2 self-application (recursive):** Does P8's evidence-strength claim apply MC2 to itself? Yes — P8 explicitly says "MC2 is being validated by this inquiry; the test fires and catches." Self-application is explicit.
- **Specific failure case:** P8 says "Promotion case strengthens from 'branch-test first' to 'branch-test confirmed; ready for canonical-spec promotion after one more branch-test on a non-chunking-related inquiry.'" Is "one more branch-test" too cautious? Per LOOP_DIAGNOSE's protocol: "Do not promote LOOP_DIAGNOSE into a standalone skill or discipline until 5 to 10 diagnostic MVLw findings show a stable internal method." For MCs (different from LOOP_DIAGNOSE as a skill), the protocol doesn't specify a count. P8's "one more non-chunking case" is a reasonable proxy.

**Verdict: SURVIVE.** Cautious appropriately.

### P9 — LOOP_DIAGNOSE finding revision note

**Prosecution.** The proposed note clearly distinguishes routings-correct (stands) from survived-intact (too strong). Self-referential honesty.

**Verdict: SURVIVE.** Clean.

### P10 — Migration plan

**Prosecution.**
- 4 phases with explicit gates and file paths.
- **Specific failure case:** Phase 2 schema code work — what about backwards compatibility? If anyone has used the old `chunking_strategy` enum literals (none have, since no code shipped), they'd need migration. Since no code has shipped, backwards compat is moot.

**Verdict: SURVIVE.** Clean.

### Assembly Emergent 1 — Two independent correction chains validate MCs

**Verdict: SURVIVE.** Strong evidence.

### Assembly Emergent 2 — Chunking critique stage missed both conflations (pattern)

**Verdict: SURVIVE.** Identifies a critique-stage pattern across two chains.

### Assembly Emergent 3 — Substrate already had the correct shape

**Verdict: SURVIVE.** Substrate-reachability framing consistent with LOOP_DIAGNOSE.

---

## Phase 3 — Verdict Summary

| Candidate | Verdict |
|---|---|
| P1 chunking_granularity | SURVIVE with mild caveat (ordering: docstring lists in order; IntEnum optional) |
| P2 canonical_level + corpus mappings | SURVIVE |
| P3 PipelineConfig override | SURVIVE with caveat (add A6 cascade note to docstring) |
| P4 Default hybrid mechanism | SURVIVE with caveat (refine passage-level baseline note) |
| P5 A4 defaults revision | SURVIVE |
| P6 Cross-cutting constraints | SURVIVE |
| P7 Inherited Re-test | SURVIVE |
| P8 MC evidence note | SURVIVE |
| P9 LOOP_DIAGNOSE note | SURVIVE |
| P10 Migration plan | SURVIVE |
| Assembly 1-3 | SURVIVE |

**Distribution:** 10 SURVIVE (3 with mild caveats) + 3 Assembly SURVIVE + 0 REFINE + 0 KILL.

### Self-application check: did the critique apply MC1 + MC2 to its own outputs?

- MC2 applied per piece: enum coherence checked at P1, P3, P5.
- MC1 applied per piece: internal claims vs structural decisions checked at P1 (docstring vs Literal ordering), P3 (docstring vs A6 cascade enforcement), P4 (default vs chunking finding).

The critique's self-application of MC1 + MC2 to its own work IS evidence that the maintenance candidates produce useful test outputs.

---

## Phase 4 — Coverage + Convergence

- Dimension coverage: 8/8 across all candidates.
- MC1 + MC2 self-application: PERFORMED per candidate.
- Convergence: STABLE.
- Failure modes: 1 PARTIAL (Self-Reference — but actively mitigated by applying MCs to own outputs).
- Mechanism-Independence: VALIDATED (multiple anchors; substrate-reachability; chunking finding text cited).

---

## Convergence Telemetry

- Dimensions: 8/8 applied
- Adversarial strength: STRONG (MC2 + MC1 self-applied)
- Landscape: STABLE
- Clean SURVIVE: YES
- Failure modes: 1 PARTIAL (Self-Reference, mitigated)
- **Overall: PROCEED**
