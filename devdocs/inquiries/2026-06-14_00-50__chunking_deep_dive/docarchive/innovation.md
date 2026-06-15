# Innovation — Chunking Deep-Dive

## User Input

Input file: `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/_branch.md`
Upstream: `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md` in same folder. The decomposition's 7 pieces (P1-P7) are the seed structure. Production-task mode.

---

## Seed + Methodology Mode

**Production-task mode.** Seed = piece-list inherited from upstream. Innovation generates text per piece.

**Inherited mode: Standard default** (balanced 4G+3F; elaborate the committed direction). Alternative considered: **Contrarian-rethink (Framer-weighted)** — would challenge SV6 wholesale rather than elaborate. Under the alternative the deliverable becomes a frontier-survey, not ship-ready text. **Decision: Standard default.** Sensemaking SV3→SV6 absorbed substantial shifts; the model converged with high anchor diversity. Per-piece Inversion-candidates (at property-(v) pieces) provide the contrarian-rethink channel without requiring a mode switch.

**Meta-decision-piece classification:** ALL 7 pieces (P1-P7) are meta-decision. Each fires property (v) (intervention-shape commitment). Per the Piece-Level Inversion Rule + Intervention-Shape-Axis Inversion, EACH must produce a principal candidate + an intervention-shape-axis Inversion-candidate, both 5-tested.

**Inherited Frame Audit:** SV6's central assumption is multi-type (Belief + Design choice + Constraint). Per tie-breaker, default Inversion + Constraint Manipulation REMOVE + Absence Recognition redesign-level apply. These fold into the per-piece Inversion-candidates at P1 (Belief), P2 (Design choice), P4 (Constraint). Orchestration NOT required externally — handled by per-piece rule.

---

## Per-piece Candidates

### P1 — Three-operation category

**Principal.**

"Chunking" in Comprehenslate is a CATEGORY covering THREE distinct operations conflated in everyday usage:

- **(i) Source segmentation** — dividing the source TEXT into translation units (chunks). Driven by source structure: paragraphs, mesele divisions, ayah boundaries, hashiye attachments, embedded-language atoms. Operates at INDEXING TIME (one-shot per corpus, cached). Output: contiguous source spans with optional metadata.
- **(ii) LLM-context-window management** — fitting source chunks into LLM API calls within token budget. Driven by Anthropic API context limits (~200k tokens for Opus). Operates at RUNTIME (per translation request). Output: an in-budget bundle of chunks + prompt context.
- **(iii) Config-application granularity** — the unit at which `TranslationConfig` values apply. Driven by user-strategy needs: per-document config vs per-passage override (per edge-case #7 passage_typology). Operates at CONFIG-RESOLUTION TIME. Output: this-chunk's effective config (document-level + any passage-typed overrides).

**Why conflated under one word.** All three operations PRODUCE OR CONSUME chunks. (i) produces; (ii) consumes; (iii) governs per. The shared object (the chunk) masks the distinct operations.

**Why disaggregation matters.** A solution addressing only (ii) (the typical RAG framing) leaves (i) and (iii) unaddressed. A single 9th-axis spec forces a category-shape mismatch with three different schema owners.

**Inter-operation relationships.** (i) feeds (ii) and (iii). (ii) and (iii) interact via the chunk (each LLM call consumes chunks AND inherits per-chunk config). The three are partially independent: segmentation strategy can change without affecting context budget; config granularity can change without changing segmentation.

**Inversion-candidate (intervention-shape axis).**

Alternative shape: **REORGANIZE-WITHOUT-ADDING.** Treat "chunking" as ONE operation (source segmentation only). What SV6 calls operations (ii) and (iii) are DOWNSTREAM CONSEQUENCES of (i)'s output, not independent operations.

What follows: simpler deliverable; collapse three schemas to one home (SourceDescriptor); user loses independent control over LLM-budget vs source-segmentation; multi-meaning runtime invariant has no schema home.

5-test: novel YES; scrutiny survival WEAK (multi-meaning policy's runtime invariant requires SCHEMA-level binding to chunk size, set at runtime not at source-declaration time); fertility low; actionability simpler but loses user control; mechanism-independence single (only Inversion reaches it).

**Verdict: KILL Inversion. Principal SURVIVES.**

### P2 — Split placement across three schemas

**Principal.**

Each chunking operation lives in the schema that owns its inputs:

| Operation | Schema | Field |
|---|---|---|
| (i) Source segmentation | `SourceDescriptor` | `source_chunking_units: list[ChunkingUnit]` |
| (ii) LLM-context management | `PipelineConfig` | `chunking_budget: int \| None` |
| (iii) Config-application granularity | `TranslationConfig` | `chunking_strategy: Literal[...]` |

**Field signatures (sketch):**

```python
class ChunkingUnit(BaseModel):
    name: str                  # "mesele", "paragraph", "ayah", "hashiye"
    detector: ChunkingDetector # how to find this unit in source
    nesting_level: int         # 0 = top, 1 = sub of top, etc.
    is_atomic: bool            # if True, never split (e.g., embedded ayah)
    attached_to: str | None    # e.g., hashiye attached-to-referent

class SourceDescriptor(BaseModel):
    source_chunking_units: list[ChunkingUnit]
    # ... other source properties

class PipelineConfig(BaseModel):
    chunking_budget: int | None = None  # tokens per LLM call

class TranslationConfig(BaseModel):
    # ... existing 8 axes ...
    chunking_strategy: Literal[
        "source-structural-unit", "paragraph", "sentence",
        "harmony-tier-aware", "passage-typology-aware",
        "LLM-detected", "fixed-budget-with-snap", "hybrid"
    ] = "paragraph"
```

**Why split, not monolithic 9th axis (three structural arguments):**

1. **Schema ownership matches data ownership.** Source-natural-units are SOURCE PROPERTIES (corpus-specific). Putting them on TranslationConfig forces every translation-config to redeclare source structure. SourceDescriptor is the natural home.
2. **Runtime-vs-design separation.** `chunking_budget` is RUNTIME ENGINEERING (depends on the LLM API in use); it shouldn't contaminate TranslationConfig (translation strategy choices).
3. **Generalization absorbs corpus variance.** Bible (verse/pericope), Quran (ayah/ruku/hizb/juz), Hindu (sloka/adhyaya), Nursi (mesele) all have different source-natural-units. The corpus-specific units belong on SourceDescriptor (declared per corpus); the corpus-agnostic strategy stays on TranslationConfig.

**Granularity-of-config insight.** Chunking is the GRANULARITY MECHANISM for all 8 axes — it defines the unit at which TranslationConfig values apply. This is a LATERAL dimension crossing all axes, not a parallel axis.

**Inversion-candidate (intervention-shape axis).**

Alternative shape: **ADD-CONTENT (monolithic 9th axis).** All chunking concerns folded into a single TranslationConfig literal field; source-natural-units become internal implementation per literal.

What follows: matches user's initial framing ("what chunking options are feasible as config"); simpler short-term; loses architectural distinctions for downstream uses (passage-typology overrides per edge #7); source-natural-units become not-user-controllable; runtime budget pollutes user-facing TranslationConfig.

5-test: novel-relative-to-SV6 YES but matches user's initial framing; scrutiny survival WEAK (the three structural arguments above each refute on structural grounds); fertility low; mechanism-independence single (Inversion only; Definitional/Internal perspective explicitly rejected it in sensemaking).

**Verdict: KILL Inversion. Principal SURVIVES.**

### P3 — Strategy enum + A4-driven defaults

**Principal.**

**Strategy enum** (8 literals on `TranslationConfig.chunking_strategy`):

| Literal | Mechanism | Cost | Quality fit |
|---|---|---|---|
| `source-structural-unit` | Use SourceDescriptor's declared units at top nesting_level | Free | High for source with strong structural units (Nursi mesele; Bible verse; Quran ayah) |
| `paragraph` | Split at paragraph boundaries (blank-line / `\n\n`) | Free | Medium; may split istilzam chains spanning paragraphs |
| `sentence` | Split at sentence boundaries (punctuation-aware) | Free | Low for theological Sufi prose; higher for language-learning |
| `harmony-tier-aware` | Detect Tier 1 chains; ensure no boundary splits a Tier 1 entry | LLM-based one-shot; cacheable | Highest preservation; recommended for A6 ≥ `light` |
| `passage-typology-aware` | Identify passage type (Sufi-anecdote / kalam / Quranic-citation / qissa / dialogue / prayer-formula) per chunk; chunk per type | LLM-based two-pass | High for editions needing passage-type strategy |
| `LLM-detected` | Single-pass LLM: "identify natural boundaries" + harmony_layer Tier 1-2 context | LLM-based; cacheable | Medium-High; depends on LLM + prompt context |
| `fixed-budget-with-snap` | Token-budget-bounded chunks; boundary snaps to nearest structural unit | Free | Medium; respects LLM context AND structural boundaries |
| `hybrid` | Structural baseline + LLM-as-judge for Tier-1-ambiguous cuts; fall back to structural where LLM uncertain | LLM-based but bounded (~20% of corpus) | High; operational default per SV6 |

**A4-driven defaults:**

| A4 purpose | Default chunking_strategy | Reasoning |
|---|---|---|
| `scholarly` | `harmony-tier-aware` | Maximum Tier 1-2 preservation; per-call cost amortized over study sessions |
| `devotional` | `source-structural-unit` | Reader engages at natural source unit (mesele-by-mesele; ayah-by-ayah) |
| `casual` | `paragraph` | Sufficient for general access; cheapest |
| `language-learning` | `sentence` | Sentence-level source-target alignment matches pedagogical need |
| `performance` | `source-structural-unit` | Performance follows source structural divisions (stanza, sura) |

**Pattern-level applicability.** Literals are corpus-AGNOSTIC. `source-structural-unit` for Nursi = mesele; for Bible = verse; for Quran = ayah; for Hindu scripture = sloka. The corpus-specific mapping happens via `SourceDescriptor.source_chunking_units`.

**Default-when-A4-silent = `paragraph`** (via A4 chain → `casual` → `paragraph`). Cheap, broadly-applicable; users explicitly upgrade to `harmony-tier-aware` / `hybrid` when correctness matters more than cost.

**Mesele-level baseline (de-facto user practice).** Nursi-specific default: `source-structural-unit` with Mesele as the top nesting_level unit. This honors the user's implicit workflow (per 4_mesele_en.md observation).

**Inversion-candidate (intervention-shape axis).**

Alternative shape: **REORGANIZE-WITHOUT-ADDING.** Collapse 8 literals to 3 categories: `structural` / `harmony-aware` / `LLM-based`.

What follows: simpler user surface; less tuning precision. The A4-driven defaults already provide good-defaults for the majority; 8-literal precision matters for the minority who tune.

5-test: novel medium; scrutiny survival PARTIAL (collapse loses handle-axis precision for tuners; but minority tuner case may be rare); fertility medium; actionability for majority-default-accepters HIGHER with collapse; mechanism-independence reached also via Constraint Manipulation ADD (constrain enum size).

**Verdict: REFINE Inversion (not KILL).** Keep 8-literal as principal; note 3-category collapse as UX-frontier candidate for future calibration.

### P4 — Cross-cutting constraints

**Principal.**

**Three constraints on chunker output, ranked by strictness:**

**Constraint 1 — Tier 1-2 preservation (HARD; ABSOLUTE).** Chunker output that breaks a Tier 1 entry (cause-effect chain, hidden syllogism, ellipsis pattern, conditional chain, semantic escalation, convergence/havuz, emotional arc, tense consistency, person-voice threading + iltifat, antonym pairing — 13 entries) is REJECTED. Tier 2 entries (grammatical parallelism, ring composition, chiastic structure, pronoun chains, clause-length patterning, evidence-claim rhythm, concession-rebuttal, thematic bracketing — 12 entries) are STRONGLY PRESERVED but may be sacrificed for chunk-size feasibility.

**Constraint 2 — Multi-meaning chunk-size lower bound (RUNTIME INVARIANT).** When the source contains polysemy whose disambiguation depends on the local construction (Layer-2 always-on policy #1), the chunk MUST contain BOTH the polysemous word AND its disambiguating construction. Operationally: minimum chunk = smallest semantic unit containing both (often a clause or paragraph). Chunker may MERGE chunks at runtime to satisfy this.

**Constraint 3 — A6 activation-gate cascade (CONFIG-LEVEL FILTER).** When `A6 form_preservation ≥ light`, the chunker MUST be harmony-tier-aware (one of: `harmony-tier-aware`, `hybrid`, or `LLM-detected` with harmony-layer prompt context). When `A6 = off` or `minimal`, simpler strategies (`paragraph`, `sentence`, `source-structural-unit`, `fixed-budget-with-snap`) are permitted.

**Cascade interactions.** Ranked priority: (1) Tier 1 hard constraint is absolute; (2) Multi-meaning lower bound is runtime invariant; (3) A6 cascade is config-level filter. Constraint 3 filters strategy choices; constraints 1+2 apply to outputs of any chosen strategy.

**Asymmetric-failure direction.** Under-chunking (oversize chunks exceeding LLM context) is STRUCTURALLY WORSE than over-chunking. Under-chunk → silent context-overflow → arbitrary truncation = information-loss-in-the-dark. Over-chunk → extra LLM calls, all information preserved. Chunker MUST over-chunk under uncertainty.

**Inversion-candidate (intervention-shape axis).**

Alternative shape: **DO-NOTHING (advisory constraints).** Mark all three as advisory, not enforced.

What follows: faster implementation; user opt-in to strict mode. BUT: Tier 1 preservation is harmony_layer.md's NON-NEGOTIABLE commitment; making it advisory CONTRADICTS existing project policy.

5-test: novel YES; scrutiny survival WEAK (Tier 1 hard-constraint stance is inherited from existing policy; reversing requires a separate finding); fertility low; actionability easier short-term, quality cost long-term.

**Verdict: KILL Inversion. Principal SURVIVES.**

### P5 — LLM feasibility + recommended hybrid + empirical validation

**Principal.**

**Feasibility verdict: YES at one-shot pre-processing scale; NO at per-translation runtime.**

**Cost analysis** (Risale-i Nur ~6000 pages × ~500 tokens/page ≈ 3M source tokens; Opus ~$15/M input tokens assumed):

| Approach | Cost per corpus pass | Latency | Notes |
|---|---|---|---|
| `LLM-detected` single-pass | ~$45 | hours, one-shot | Prompt context ~5K tokens × N calls |
| `harmony-tier-aware` single-pass | ~$50 | hours, one-shot | Slightly richer prompt context |
| **`hybrid` (recommended)** | **~$10-20** | hours, one-shot | LLM fires only on Tier-1-ambiguous regions (~20% of corpus) |
| `passage-typology-aware` two-pass | ~$90 | hours, one-shot | Classify + chunk per type |

All approaches CACHEABLE across config tweaks (boundaries are config-independent). One-time cost amortized across many translation runs.

**Per-translation-runtime feasibility: NO.** Running LLM-based chunking on every translation request would add hours of latency per request. Chunking MUST be a one-shot pre-processing step with cached output.

**Recommended approach: `hybrid` harmony-aware.**

Mechanism:
1. **Structural baseline pass.** Apply `source-structural-unit` strategy (Nursi: mesele). Free, fast. Produces candidate chunks.
2. **Tier-1-ambiguity scan.** Heuristic check (regex-style detection of cause-effect connectives spanning candidate boundaries; syllogism patterns; conditional chains). Free, fast. Flags ambiguous regions.
3. **LLM-as-judge for ambiguous regions.** For each flagged region, send LLM a prompt: "this region may contain a Tier 1 chain spanning the proposed boundary; decide MERGE / KEEP / SPLIT-DIFFERENTLY." LLM context includes harmony_layer.md Tier 1-2 reference.
4. **Fall-back to structural.** Where LLM is uncertain (LOW confidence), defer to step 1's structural baseline.

Cost dominated by step 1 (free) + step 3 (LLM, bounded to ambiguous fraction). Net: ~$10-20 per Risale-i Nur pass; one-shot; cacheable.

**Empirical validation plan (deferred MUST).**

1. **Gold-standard set.** Manually mark 20-50 mesele units with the correct chunking (author with deep Nursi familiarity).
2. **Comparative run.** Run `source-structural-unit`, `hybrid`, and `harmony-tier-aware` on those units; compare to gold.
3. **Metrics.** Boundary precision/recall; Tier-1-chain preservation rate; LLM-as-judge agreement with gold at flagged regions.
4. **Pass criteria.** ≥95% Tier-1 preservation (no false-splits); ≥80% boundary precision; ≥90% LLM-judge agreement at flagged regions.
5. **Failure recovery.** If `hybrid` fails pass criteria, fall back to `source-structural-unit` (Mesele) as the Nursi-specific default; mark `hybrid` as research-frontier.

**Distinction: (a) technical feasibility = unambiguous YES** (LLMs can identify boundaries); **(b) economic + qualitative feasibility = conditional** on empirical validation passing.

**Inversion-candidate (intervention-shape axis).**

Alternative shape: **CONTRARIAN-RETHINK (no-LLM).** `source-structural-unit` alone is sufficient; LLM-based chunking is overkill.

What follows: NO LLM-based chunking; rely entirely on declared source-structural-units. Cost $0. Latency none. Quality depends on whether Nursi's istilzam chains span multiple mesele.

Empirical question: do Nursi's istilzam chains typically appear WITHIN a single mesele or SPAN mesele? If within: `source-structural-unit` is sufficient and `hybrid` is overkill. If across: `source-structural-unit` fails Tier 1 preservation and `hybrid` is required.

5-test: novel YES; scrutiny survival MEDIUM (depends on empirical answer); fertility HIGH (opens "is hybrid actually needed?" question); actionability simpler if validated; mechanism-independence reached also via Constraint Manipulation REMOVE.

**Verdict: REFINE Inversion (not KILL).** Empirical validation plan should be COMPARATIVE: `source-structural-unit` alone vs `hybrid` vs `harmony-tier-aware`. If `source-structural-unit` alone passes pass-criteria, downgrade recommendation to `source-structural-unit` + frontier-flag `hybrid` as future-frontier. Frontier flag preserved in finding's Open Questions.

### P6 — Cross-axis interaction matrix

**Principal.**

**A1-A8 × chunking interaction:**

| Axis | Signal | Specifics |
|---|---|---|
| A1 reader_level | LOW | Chunking happens upstream of reader-level decisions |
| A2 domain_expertise | LOW | Same |
| A3 source_culture | LOW | Cultural recognition is per-reference, not per-chunk |
| **A4 purpose** | **HIGH** | A4-driven defaults matrix (see P3) — primary chunking-strategy driver |
| A5 source_fidelity | MED | Foreignized-max + edge-case #1 atom-preservation interact at chunking time |
| **A6 form_preservation** | **HIGH** | Activation-gate cascade at A6 ≥ `light` requires harmony-tier-aware (see P4) |
| A7 scaffolding | MED | Apparatus-per-chunk density depends on A7; cross-chunk footnotes possible at high A7 |
| **A8 analysis_depth** | **HIGH** | A8 deep+ analysis-per-major-passage maps to chunks; analysis section granularity ~ chunking granularity |

**Edge-case candidate × chunking interaction:**

| Edge-case | Signal | Specifics |
|---|---|---|
| #1 `embedded_source_languages` | HIGH | Chunker must treat embedded foreign-language quotation as ATOMIC (Arabic ayah inside Turkish paragraph cannot split). `SourceDescriptor.source_chunking_units` includes `is_atomic` flag |
| #2 `source_language vs source_culture` | LOW | — |
| #3 `source_edition` | LOW | Different editions may declare different `source_chunking_units` |
| #4 `voice_disambiguation` | MED | Voice clusters ideally co-locate; chunker considers voice continuity at boundary decision |
| #5 `relay_translation` | LOW | — |
| #6 `source_apparatus_handling` | HIGH | Nursi's hashiye must travel with its referent chunk. `ChunkingUnit.attached_to` field carries the link |
| **#7 `passage_typology`** | **VERY HIGH** | Sister concepts. Resolution: chunking determines BOUNDARIES; passage_typology determines TYPE per chunk. Two orthogonal axes. The `passage-typology-aware` strategy literal is the specific composition |
| #8 `quranic_citation_special_status` | HIGH | Quranic citations have established ayah boundaries; chunker respects them within citation |
| #9 `consumption_mode` | MED | Communal-study → section-level chunks; memorization → smaller |
| #10-#14 | LOW | — |

**Inversion-candidate (intervention-shape axis).**

Alternative shape: **DO-NOTHING (no matrix).** Cross-axis interactions are either obvious or non-existent; derive per-need.

What follows: simpler finding; user-derived from per-piece narratives. BUT: 3 HIGH-signal axis interactions + 4 HIGH edge-case interactions + 1 VERY-HIGH (passage_typology) are non-trivial; omitting silently leaves implicit commitments.

5-test: novel LOW; scrutiny survival WEAK; fertility LOW.

**Verdict: KILL Inversion. Principal SURVIVES.**

### P7 — Failure modes with mitigations

**Principal.**

**10 failure modes from surfacing R8, classified + mitigated:**

| # | Failure mode | Severity class | Mitigation in `hybrid` |
|---|---|---|---|
| 1 | Tier 1 chain split (istilzam etc.) | HARD-CONSTRAINT | LLM-as-judge step 3 detects chain spanning boundary; merges chunks |
| 2 | Polysemy disambiguation context split | RUNTIME INVARIANT | Multi-meaning lower bound (P4-2) requires polysemy + disambiguator co-presence |
| 3 | Embedded ayah split across chunks | HARD-CONSTRAINT (atom) | `ChunkingUnit.is_atomic` prevents split; structural baseline respects atoms |
| 4 | Hashiye orphan (footnote separated from referent) | COHESION | `ChunkingUnit.attached_to` carries attachment |
| 5 | Orphan honorific ("Hazret-i" stranded) | COHESION | LLM-as-judge detects orphan-honorific patterns; merges |
| 6 | Iltifat interrupted at boundary | HARD-CONSTRAINT (Tier 1 person-voice + iltifat) | LLM-as-judge detects iltifat patterns; treats as Tier 1 chain |
| 7 | Voice-cluster split (Nursi → citation → commentary) | COHESION | LLM-as-judge detects voice-cluster patterns; cross-references P6 edge #4 |
| 8 | Over-chunking (too small) | SIZE | Multi-meaning lower bound + minimum-chunk heuristic; runtime warn |
| 9 | Under-chunking (too large) | SIZE — ASYMMETRIC-FAILURE WORSE | `chunking_budget` enforces upper bound; chunker MUST not exceed |
| 10 | Cross-chunk reference unresolved | CROSS-REFERENCE | A7 apparatus channel re-includes reference; chunker carries cross-ref metadata; PARTIAL mitigation only |

**Asymmetric-failure direction respected.** Under-chunking flagged worse than over-chunking; `chunking_budget` enforces upper-bound strictly; lower-bound is softer (runtime merge permitted).

**Unaddressed failure modes (deferred research frontier):**
- Cross-document chunking (thematic anthology spanning multiple Nursi works)
- Multi-language passage interaction (Turkish + Arabic + Persian in same chunk beyond #1 atom case)

**Inversion-candidate (intervention-shape axis).**

Alternative shape: **REORGANIZE-WITHOUT-ADDING (collapse P7 into P4).** Failure modes derivable from constraints in P4; no separate list needed.

What follows: shorter finding. BUT: per-mode mitigation mapping is non-trivial (Tier-1 vs cohesion vs size vs cross-reference have DIFFERENT mitigation channels); collapsing loses auditable mitigation traceability for chunker QA.

5-test: novel medium; scrutiny survival MEDIUM (collapsing is defensible but operational use favors explicit list); fertility low; actionability HIGHER with explicit list for chunker QA.

**Verdict: REFINE Inversion (not KILL).** Keep P7 as explicit list; note in P4 that the constraints are the structural source of the failure modes.

---

## Assembly Check

After per-piece testing, examine surviving candidates jointly. Three emergent insights:

**Emergent 1: The `hybrid` mechanism IS the architectural center.** P5 owns the recommendation; P3 names the literal; P4 constrains it; P7 lists failures it mitigates; P6 cross-references it. The hybrid harmony-aware chunker is the central organizing concept — all other pieces orbit it. **Finding structure should foreground the hybrid mechanism** (probably in the Finding section after the three-operation conceptual frame).

**Emergent 2: Three-schema split + strategy enum + A4 defaults TOGETHER REPLICATE the existing 8-axis pattern.** The same pattern (per-axis enum + A4-driven defaults + cross-axis interactions) that organizes the 8 axes also organizes this new chunking layer. **Framework-consistency argument** — chunking fits the existing schema-design idiom cleanly.

**Emergent 3: P5's empirical validation plan + P7's deferred research items combine into ONE follow-up work package.** A future inquiry should: (a) build the gold-standard set; (b) run comparative empirical validation across `source-structural-unit` / `hybrid` / `harmony-tier-aware`; (c) close the deferred research items (cross-document chunking + multi-language passages). Single inquiry, not three.

---

## Inherited Frame Audit (post-generation)

Each meta-decision piece challenged its commitment via per-piece Inversion. The audit's seed-level central assumption (SV6's three-operation + split-placement + hard-constraints + LLM-feasibility + hybrid recommendation) was challenged: P1 Inversion (single-operation) → KILL; P2 Inversion (monolithic 9th-axis) → KILL; P4 Inversion (advisory constraints) → KILL; P5 Inversion (no-LLM) → REFINE (added comparative-validation requirement). Orchestration NOT required externally — the per-piece rule handled it.

---

## Failure-mode check

| Failure mode | Status |
|---|---|
| Premature evaluation | NO — each candidate has 5-test cycle |
| Single-mechanism trap | NO — all 7 mechanisms applied across pieces |
| Early frame lock | NO — Inversion-candidates explicitly challenged committed direction per piece |
| Innovation without grounding | NO — each candidate tested |
| Mechanism exhaustion | NO |
| Survival bias | NO — P3 and P5 and P7 inversion-candidates actually REFINED principal (3-category UX frontier; comparative-validation requirement; constraints-are-source note) |

---

## Telemetry

- **Generators applied: 4/4** (Combination [P1, P3, P6]; Absence Recognition patch + redesign [P5, P7]; Domain Transfer [P3, P5]; Extrapolation [P5])
- **Framers applied: 3/3** (Lens Shifting [P3]; Constraint Manipulation ADD + REMOVE [P4, P5 inversion]; Inversion system-level + per-piece intervention-shape axis [all 7])
- **Full coverage achieved.**
- **Convergence: YES** — `hybrid` harmony-aware mechanism converges as architectural center (Emergent 1; reached via 3+ mechanisms).
- **Survivors tested: 14** (7 principal + 7 inversion).
- **Per-piece mechanism log:**
  - P1: `[Combination:content, Inversion:intervention-shape]`
  - P2: `[Combination:content, Domain-Transfer:content, Inversion:intervention-shape]`
  - P3: `[Combination:content, Domain-Transfer:content, Constraint-Manipulation:content, Lens-Shifting:content, Inversion:intervention-shape]`
  - P4: `[Constraint-Manipulation-ADD:content, Inversion:intervention-shape]`
  - P5: `[Absence-Recognition-patch+redesign:content, Domain-Transfer:content, Extrapolation:content, Inversion:intervention-shape]`
  - P6: `[Combination:content, Inversion:intervention-shape]`
  - P7: `[Absence-Recognition-patch:content, Inversion:intervention-shape]`
- **Meta-decision-piece classification:** 7/7 meta-decision; 7/7 property-(v) fires.
- **Piece-level Inversion compliance:** 7/7 satisfied (axis = intervention-shape per piece).
- **Output disposition:**
  - **ACTIONABLE** — 4 principals (P1, P2, P4, P6) — multi-source convergent; clean.
  - **REFINE-ACCEPTED** — 3 inversions (P3 3-category UX frontier flagged; P5 comparative-validation added; P7 constraints-source noted) — refinements integrated into principal.
  - **KILL** — 4 inversions (P1, P2, P4, P6) — rejected on structural grounds.
- **Failure modes observed:** none.
- **Overall: PROCEED.**
