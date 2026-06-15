---
status: active
model: claude-opus-4-7[1m]
effort: max
---
# Finding: Chunking Deep-Dive

## Question

From `_branch.md`:

> "what about chunking, lets dive deep about this. how it should work, why it is important, what chunking options are feasible as config, LLM based chunking possible? ..."

The user is asking about **chunking** in Comprehenslate — the AI-assisted translation system being built around the Said Nursi *Risale-i Nur* corpus (a layered Turkish religious-theological text with embedded Arabic and Persian). The trailing "..." invites additional facets the user has in mind but didn't articulate.

The articulated framing (preserved as the inquiry's openness) treats this as a deep-dive deliverable spanning four levels: **conceptual** (what chunking IS in Comprehenslate), **algorithmic** (what mechanisms exist), **architectural** (where chunking lives in the schemas), and **AI-prompt-context** (what an LLM-based chunker is fed). The deep-dive operates at the first three; AI-prompt design is downstream.

The goal: a finding that ships with operational substance — comprehensive enough to act on, structured to match the existing 8-axis configuration framework, anti-bloat per the user's session preferences.

## Finding Summary

- **"Chunking" is not one operation — it conflates three.** (i) **Source segmentation** divides the source text into translation units; (ii) **LLM-context-window management** fits chunks into Anthropic API calls within the token budget; (iii) **Config-application granularity** is the unit at which `TranslationConfig` values apply. They share the chunk object, which is why the word collapses them.

- **The three operations live in three different schemas.** Source segmentation declares **corpus-specific source-natural-units** on `SourceDescriptor` (Nursi declares mesele / paragraph / ayah-atom; Bible would declare verse / pericope; Quran declares ayah / ruku / hizb / juz). LLM-context budget lives on `PipelineConfig` (a runtime concern). User-facing strategy lives on `TranslationConfig` as a new field `chunking_strategy` — a corpus-agnostic enum of 8 literals.

- **Chunking is the GRANULARITY MECHANISM for all 8 existing axes, not a 9th parallel axis.** Adding it as a 9th axis (the user's initial framing) forces a category-shape mismatch because the three operations have different schema owners. The split-placement is the structurally-motivated answer.

- **The strategy enum has 8 literals: `source-structural-unit` / `paragraph` / `sentence` / `harmony-tier-aware` / `passage-typology-aware` / `LLM-detected` / `fixed-budget-with-snap` / `hybrid`.** Defaults are A4-driven, matching the existing A4-defaults pattern for A5-A8: scholarly → `harmony-tier-aware`; devotional → `source-structural-unit`; casual → `paragraph`; language-learning → `sentence`; performance → `source-structural-unit`. When no purpose is set, default is `paragraph`.

- **Three hard constraints on any chunker output.** (1) Tier 1-2 preservation per `harmony_layer.md` — chunker output that breaks a Tier 1 entry (e.g., Nursi's istilzam chain `Rahman → Rezzak → Rızk → Beka → Vücud → İlim/İrade/Kudret → Hayat`) is rejected. (2) Multi-meaning chunk-size lower bound — when a polysemous source word's disambiguation depends on the local construction, the chunk must contain both. (3) A6 form_preservation activation-gate cascade — when `A6 ≥ light`, the chunker MUST be harmony-aware; below, simpler strategies are permitted.

- **LLM-based chunking is feasible at one-shot pre-processing scale; not at per-translation runtime.** Cost estimate: roughly $10–$45 per Risale-i-Nur-sized corpus pass with Opus depending on approach. Output is cacheable across config-tweak re-translations because chunk boundaries are config-independent.

- **Recommended operational default: `hybrid` harmony-aware.** Four steps: structural baseline (`source-structural-unit` for Nursi = mesele) → heuristic scan for Tier-1-ambiguous regions → LLM-as-judge on flagged regions only → fall back to structural where the LLM is uncertain. Empirical validation on the Nursi corpus is a deferred MUST before production use.

- **Asymmetric-failure direction matters.** Under-chunking (oversize chunks that overflow LLM context → silent truncation = information loss) is structurally worse than over-chunking (extra LLM calls but all information preserved). The chunker MUST over-chunk under uncertainty.

- **The design generalizes to other multilingual religious-theological corpora.** Bible / Quran / Hindu scriptures use different source-natural-units (verse / ayah / sloka) but the same placement and strategy-enum categories. Generalization absorbs corpus variance via the `SourceDescriptor.source_chunking_units` per-corpus declaration.

- **A handful of operational gaps need closing as MUST follow-up work,** in this order: empirical validation on Nursi; Tier-1-preservation enforcement mechanism; A6-cascade-vs-user-override precedence rule; LLM-judge confidence-threshold spec; heuristic false-negative mitigation. Each has concrete refinement direction in Next Actions below.

## Finding

### Why this matters (the goal context)

The Comprehenslate project is building an AI-assisted translation system whose primary corpus is Said Nursi's *Risale-i Nur* — roughly 6,000 pages of layered Turkish theological prose embedded with Arabic Quranic citations, Persian Sufi couplets, and Nursi's own marginal annotations (the *hashiye*). Across recent inquiries, the project has settled an 8-axis `TranslationConfig` (reader-level, domain-expertise, source-culture, purpose, source-fidelity, form-preservation, scaffolding, analysis-depth — captured in `config_base_source.md`) and a candidate edge-case schema with 14 fields covering multi-language and multi-voice source phenomena (in `devdocs/innovation/translation_config_edge_cases.md`). Neither artifact says anything about how the source text is divided into translation units. That is the gap this finding addresses.

The user's question arrived with four facets: how chunking should work, why it matters, what config options exist, and whether LLM-based chunking is feasible. The trailing "..." invited additional facets. Each facet is answered below, after a section that disaggregates what "chunking" actually means in this project.

### 1. What chunking IS in Comprehenslate (the three-operation category)

The word "chunking" in everyday usage (especially in RAG-style LLM literature) typically means "splitting source text into LLM-context-sized pieces." That framing is incomplete here. In Comprehenslate, three structurally distinct operations share the chunk object and get conflated under one word.

**Operation (i) — Source segmentation.** Divides the source text into translation units. Driven by source structure: paragraphs, *mesele* divisions (Nursi's numbered sub-arguments), ayah boundaries inside Arabic citations, *hashiye* attachments, embedded-language atoms. Operates at **indexing time** — a one-shot pass per corpus, cached. The unit it produces is the "chunk" — a contiguous source span with optional metadata (type label, attached apparatus, embedded-atom markers).

**Operation (ii) — LLM-context-window management.** Fits source chunks into Anthropic API calls within the token budget. Driven by the model's context limit (roughly 200,000 tokens for Claude Opus). Operates at **runtime** — once per translation request. The unit it consumes is "as many chunks as fit in this call, plus the translator-AI's system prompt and config context."

**Operation (iii) — Config-application granularity.** The unit at which `TranslationConfig` values apply. Driven by user-strategy needs: per-document config versus per-passage overrides (the `passage_typology` edge-case candidate from the earlier innovation pass). Operates at **config-resolution time** — when the AI reads its config for a specific chunk. The unit it governs is "this chunk inherits the document-level config plus any passage-typed overrides."

**Why these three look like one operation.** All three either produce or consume chunks. Operation (i) produces them; operation (ii) consumes them; operation (iii) is governed per chunk. The shared object hides the distinction.

**Why disaggregation matters.** A solution that addresses only (ii) — the RAG framing — leaves (i) and (iii) unspecified. The multi-meaning preservation policy (a Layer-2 always-on policy already settled in the project) puts a chunk-size lower bound that operates at runtime; this binding has no home if chunking is treated only as source segmentation. And the user's existing edge-case innovation surfaced `passage_typology` (#7 in `translation_config_edge_cases.md`) which presupposes per-chunk config overrides — that's operation (iii). Without disaggregating, this finding could not connect to the existing project commitments cleanly.

### 2. Why chunking is important

Five concrete reasons, in roughly descending operational urgency:

**LLM context-window limits.** The full Risale-i Nur corpus is approximately 3 million tokens of source text. Opus's 200K context window holds about 1/15th of that, before counting system prompt + config + apparatus context. Without chunking, full-document translation is impossible.

**Translation-unit consistency.** When the AI translates chunk-by-chunk, terminology and register choices propagate across chunks. A poorly-chosen boundary mid-paragraph forces the AI to re-decide register on each side; a well-chosen boundary at the natural unit (e.g., a complete *mesele*) gives the AI a coherent unit to optimize across.

**Config-application granularity.** The 8-axis `TranslationConfig` is set per document today. Real source texts mix passage types (Sufi anecdote vs *kalam* argument vs Quranic citation vs *qissa* parable) that may warrant different translation strategies. Chunking is the granularity at which per-passage overrides become possible — without it, the override question has no operational answer.

**Tier-1 form-as-meaning preservation.** The project's foundational principle (`harmony_layer.md`) commits that structural form *is* meaning at Tier 1: a cause-effect chain like `Rahman → Rezzak → Rızk → Beka → Vücud → İlim/İrade/Kudret → Hayat` carries argumentative content in its structure, not just its words. A chunker that splits such a chain breaks meaning. This is the hardest constraint chunking must respect.

**LLM cost and latency.** Many small chunks mean many LLM calls; few large chunks risk overflow and silent truncation. The economic feasibility of LLM-based chunking depends entirely on whether the chunking pass can be one-shot pre-processing (amortized across many translations) rather than per-translation runtime.

### 3. Where chunking lives (the split-placement decision)

The user's question — "what chunking options are feasible as config" — naturally implies a 9th axis on `TranslationConfig`. The structurally-correct answer is different.

Each of the three operations lives in the schema that owns its inputs:

```python
# SourceDescriptor — corpus-specific source declarations
class ChunkingUnit(BaseModel):
    name: str                    # "mesele", "paragraph", "ayah", "hashiye"
    detector: ChunkingDetector   # how to find this unit in the source
    nesting_level: int           # 0 = top, 1 = sub of top, etc.
    is_atomic: bool              # if True, never split (e.g., embedded ayah)
    attached_to: str | None      # e.g., hashiye attached to its referent

class SourceDescriptor(BaseModel):
    source_chunking_units: list[ChunkingUnit]
    # ... other source properties from the edge-case innovation

# PipelineConfig — runtime engineering concerns
class PipelineConfig(BaseModel):
    chunking_budget: int | None = None  # tokens per LLM call; None = use model default

# TranslationConfig — user-facing strategy (extends the existing 8 axes)
class TranslationConfig(BaseModel):
    # ... existing 8 axes (reader_level, domain_expertise, ..., analysis_depth) ...
    chunking_strategy: Literal[
        "source-structural-unit", "paragraph", "sentence",
        "harmony-tier-aware", "passage-typology-aware",
        "LLM-detected", "fixed-budget-with-snap", "hybrid"
    ] = "paragraph"
```

**Why split-placement over the 9th-axis framing.** Three structural arguments:

*Schema ownership matches data ownership.* Source-natural-units are properties of the source (each corpus declares its own); putting them on `TranslationConfig` would force every translation-config to redeclare source structure. `SourceDescriptor` is the natural home.

*Runtime-vs-design separation.* `chunking_budget` depends on the LLM API in use, not on user translation strategy. It should not contaminate `TranslationConfig`, which captures translation-strategy choices.

*Generalization absorbs corpus variance.* When Comprehenslate extends beyond Nursi to other corpora — Quran translation projects, Bible projects, Hindu scripture projects — each has different source-natural-units (verse / ayah / sloka / pericope). The corpus-specific units belong on `SourceDescriptor` (declared per corpus). The corpus-agnostic strategy enum stays on `TranslationConfig`.

**The deeper insight.** Chunking is the *granularity mechanism* for all 8 axes — it defines the unit at which `TranslationConfig` values apply. It is a lateral dimension crossing all axes, not a parallel axis. The 9th-axis framing forces a category-shape mismatch the split-placement avoids.

**Caveat (from the critique pass).** `SourceDescriptor` and `PipelineConfig` are not yet implemented schemas. They were proposed in the recent edge-case innovation (assembly check identified them as the Group α / β / γ split). The placement decided here is structurally correct but conditional on those schemas actually being built. The implementation cascade in Next Actions sequences this dependency.

### 4. What chunking options exist (the strategy enum and A4-driven defaults)

The `chunking_strategy` field on `TranslationConfig` exposes 8 literals. The table below summarizes each: what mechanism it uses, what it costs, and what quality profile it offers on Nursi-style theological prose.

| Literal | Mechanism | Cost | Quality fit |
|---|---|---|---|
| `source-structural-unit` | Use `SourceDescriptor`'s declared units at the top nesting level | Free | High for sources with strong structural units (Nursi mesele; Bible verse; Quran ayah) |
| `paragraph` | Split at paragraph boundaries (blank-line or `\n\n`) | Free | Medium; may split istilzam chains spanning paragraphs |
| `sentence` | Split at sentence boundaries (punctuation-aware) | Free | Low for theological Sufi prose; better for language-learning |
| `harmony-tier-aware` | Detect Tier 1 chains; ensure no boundary splits a Tier 1 entry | LLM-based, one-shot, cacheable | Highest preservation; recommended for `A6 ≥ light` |
| `passage-typology-aware` | Identify passage type (Sufi-anecdote / kalam / Quranic-citation / qissa / dialogue / prayer-formula) and chunk per type | LLM-based, two-pass | High for editions needing passage-type-aware translation strategy |
| `LLM-detected` | Single LLM call: "identify natural boundaries" with `harmony_layer` Tier 1-2 prompt context | LLM-based, cacheable | Medium-high; depends on LLM and prompt context |
| `fixed-budget-with-snap` | Token-budget-bounded chunks; boundaries snap to nearest structural unit | Free | Medium; respects LLM context AND structural boundaries |
| `hybrid` | Structural baseline + LLM-as-judge for Tier-1-ambiguous cuts; fall back to structural where LLM is uncertain | LLM-based but bounded (~20% of corpus) | High; operational default |

**A4-driven defaults.** Following the existing pattern where `A4 purpose` drives defaults for `A5 source_fidelity` through `A8 analysis_depth` (see `config_base_source.md`), `chunking_strategy` inherits A4-driven defaults:

| `A4 purpose` | Default `chunking_strategy` | Why |
|---|---|---|
| `scholarly` | `harmony-tier-aware` | Maximum Tier 1-2 preservation; per-call cost amortized over study sessions |
| `devotional` | `source-structural-unit` | Devotional readers engage at the natural source unit (mesele-by-mesele; ayah-by-ayah) |
| `casual` | `paragraph` | Sufficient for general access; cheapest |
| `language-learning` | `sentence` | Sentence-level source-target alignment matches pedagogical need |
| `performance` | `source-structural-unit` | Performance (recitation) follows source structural divisions (stanza, sura) |

**Default when no purpose is set:** `paragraph` (via the existing A4 chain that defaults to `casual`). The cheap, broadly-applicable strategy is the safe fallback. Users explicitly upgrade to `harmony-tier-aware` or `hybrid` when correctness matters more than cost.

**The mesele-level baseline.** The user's current manual workflow (visible in `mytrasnlations/asayi_musa/4_mesele_en.md`) chunks at the mesele level. The Nursi corpus's `SourceDescriptor` declaration should have Mesele as `nesting_level=0`, paragraph as `nesting_level=1`, and embedded ayahs as `is_atomic=True`. This formalizes the user's de-facto practice rather than displacing it.

### 5. Cross-cutting constraints

The chunker, regardless of which strategy is chosen, must respect three constraints ranked by strictness.

**Constraint 1 — Tier 1-2 preservation (HARD; absolute).** Chunker output that breaks a Tier 1 entry from `harmony_layer.md` is rejected. Tier 1 entries (13 total) include cause-effect chains, hidden syllogisms, conditional chains, semantic escalation/de-escalation, the *havuz* convergence pattern, ellipsis patterns, emotional arcs, tense consistency, person-voice threading with *iltifat* shifts, and antonym pairing. Tier 2 entries (12 total) — grammatical parallelism, ring composition, chiastic structure, pronoun chains, clause-length patterning — are strongly preserved but may be sacrificed for chunk-size feasibility.

**Constraint 2 — Multi-meaning chunk-size lower bound (runtime invariant).** When the source contains polysemy whose disambiguation depends on the local construction (the Layer-2 always-on multi-meaning preservation policy), the chunk must be large enough to contain both the polysemous word and its disambiguating construction. The chunker may merge chunks at runtime to satisfy this.

**Constraint 3 — A6 activation-gate cascade (config-level filter).** When `A6 form_preservation ≥ light`, the chunker MUST be harmony-aware (one of `harmony-tier-aware`, `hybrid`, or `LLM-detected` with harmony-layer prompt context). When `A6 = off` or `minimal`, simpler strategies (`paragraph`, `sentence`, `source-structural-unit`, `fixed-budget-with-snap`) are permitted. This cascade follows the existing A6 activation-gate semantics that fires the full 3-Pass methodology at `light` and above.

**Cascade interaction.** When `A6 ≥ light` and the user has explicitly set a non-harmony-aware `chunking_strategy`, the cascade wins. The user receives a warning explaining the constraint and may lower A6 if a simpler chunker is desired. The precedence is: Tier 1 hard constraint (absolute) → multi-meaning lower bound (runtime merge) → A6 cascade (config-level filter, cascade-wins).

**Asymmetric-failure direction.** Under-chunking — chunks too large that exceed LLM context — is structurally worse than over-chunking. Under-chunking leads to silent context overflow and arbitrary truncation, which is information loss in the dark. Over-chunking produces extra LLM calls but preserves all information. The chunker MUST over-chunk under uncertainty.

### 6. LLM-based chunking — is it feasible?

The user asked directly. The answer is **YES at one-shot pre-processing scale; NO at per-translation runtime.**

**Cost estimate** (Risale-i Nur corpus ≈ 6,000 pages × ≈ 500 tokens/page ≈ 3 million source tokens; assuming Opus pricing around $15 per million input tokens — this rate needs canonical verification against current Anthropic pricing as of inquiry date):

| Approach | Cost per corpus pass | Latency | Notes |
|---|---|---|---|
| `LLM-detected` single-pass | ≈ $45 | hours, one-shot | Prompt context adds about 5K tokens × N calls |
| `harmony-tier-aware` single-pass | ≈ $50 | hours, one-shot | Slightly richer prompt context |
| `hybrid` (recommended) | **≈ $10–20** | hours, one-shot | LLM fires only on Tier-1-ambiguous regions (typically <20% of corpus) |
| `passage-typology-aware` two-pass | ≈ $90 | hours, one-shot | Classify type + chunk per type |

Output tokens (the chunker's decisions) add a smaller but non-zero cost the table above does not include — this should be added in a follow-up pass on the cost analysis.

**All approaches are cacheable** across config tweaks. Chunk boundaries are config-independent, so the chunker runs once per source-edition; subsequent translations with different configs reuse the cached boundaries. This is what makes the cost manageable — one-shot $10–20 amortizes across dozens of translation runs.

**Per-translation runtime is infeasible.** Running an LLM-based chunking pass on every translation request would add hours of latency. Chunking must be a one-shot pre-processing step with cached output.

**Recommended approach: `hybrid` harmony-aware.** The four steps:

1. **Structural baseline pass** — apply `source-structural-unit` (Nursi: mesele); free, fast.
2. **Tier-1-ambiguity scan** — a regex-style heuristic detects candidate boundaries spanning cause-effect connectives, syllogism patterns, or conditional chains; free, fast; flags ambiguous regions.
3. **LLM-as-judge on flagged regions** — for each flagged region, send the LLM a prompt that includes `harmony_layer.md` Tier 1-2 reference and asks: "Does this region contain a Tier 1 chain that the proposed boundary would split? Decide MERGE / KEEP / SPLIT-DIFFERENTLY."
4. **Fall back to structural** where LLM confidence is low — defer to the structural baseline from step 1.

The hybrid mechanism is the architectural center of this finding — every other element (placement, strategy enum, constraints, failure-mode mitigations, cross-axis interactions) orbits it.

**Empirical validation (deferred MUST).** Before production use, the hybrid approach must be validated on the Nursi corpus:

1. Build a gold-standard set of 20–50 mesele units with manually-marked correct chunking boundaries.
2. Run three strategies comparatively: `source-structural-unit` alone, `hybrid`, and `harmony-tier-aware`.
3. Metrics: boundary precision/recall against gold; Tier-1-chain preservation rate; LLM-as-judge agreement with gold at flagged regions.
4. Pass criteria: ≥95% Tier-1-chain preservation (no false-splits); ≥80% boundary precision; ≥90% LLM-judge agreement at flagged regions.
5. **Failure recovery path.** If hybrid fails, fall back to `source-structural-unit` (mesele) as the Nursi-specific default and treat hybrid as a research frontier. If `source-structural-unit` alone passes the criteria, hybrid may be overkill — downgrade the recommendation to source-structural-unit and frontier-flag hybrid.

**Open mechanism gaps in the hybrid approach** (each appears as a MUST refinement in Next Actions):

- The LLM-judge return format and the confidence threshold for falling back to structural are not yet specified.
- The heuristic step 2 may miss ambiguous regions (false negatives) — without a catch-all mechanism, a Tier 1 chain could silently split through the heuristic gap. The recommended catch-all: a post-chunker Tier-1-preservation validation pass that re-routes failures to the LLM-judge. This same mechanism doubles as the Tier 1 hard-constraint enforcement (Constraint 1 above), so the two gaps close together.

### 7. Cross-axis interactions

Chunking interacts with the existing 8 axes and with the 14 edge-case candidates from the earlier innovation pass. The interactions worth surfacing:

| Axis / edge-case | Signal | What it means for chunking |
|---|---|---|
| `A4 purpose` | HIGH | Drives the per-strategy defaults (table in section 4 above) |
| `A6 form_preservation` | HIGH | The activation-gate cascade (Constraint 3 above) |
| `A8 analysis_depth` | HIGH | Analysis-section granularity often matches chunking granularity at deep+ levels |
| edge-case `embedded_source_languages` | HIGH | Embedded foreign-language quotations (Arabic ayahs in Turkish prose) are atomic — the `ChunkingUnit.is_atomic` field prevents splitting |
| edge-case `source_apparatus_handling` | HIGH | Nursi's hashiye must travel with its referent chunk — the `ChunkingUnit.attached_to` field carries the link |
| edge-case `passage_typology` | VERY HIGH | Sister concepts. Chunking determines boundaries; passage typology labels TYPE per chunk. They are two orthogonal axes, not one. The `passage-typology-aware` strategy literal is the composition (chunk-by-type) |
| edge-case `voice_disambiguation` | MED | Voice clusters (Nursi → cited authority → Nursi's commentary on the citation) should co-locate; the LLM-judge step should learn these patterns |

The remaining edge-cases (`source_language vs source_culture`, `source_edition`, `relay_translation`, `consumption_mode`, and so on) have LOW chunking-interaction signal and are not addressed here.

### 8. Failure modes and how the recommended approach mitigates them

The earlier surfacing pass identified 10 concrete chunking failure modes from the Nursi corpus. The hybrid harmony-aware mechanism mitigates each:

| # | Failure mode | Severity | Mitigation in hybrid |
|---|---|---|---|
| 1 | Tier 1 chain split (e.g., istilzam chain) | HARD constraint | LLM-as-judge step detects chain spanning boundary; merges chunks |
| 2 | Polysemy disambiguation context split | Runtime invariant | Multi-meaning lower bound requires polysemy + disambiguator co-presence (Constraint 2) |
| 3 | Embedded ayah split across chunks | HARD constraint (atom) | `ChunkingUnit.is_atomic` prevents split; structural baseline respects atoms |
| 4 | Hashiye orphan (footnote separated from referent) | Cohesion | `ChunkingUnit.attached_to` carries attachment |
| 5 | Orphan honorific ("Hazret-i" stranded on chunk before its named person) | Cohesion | LLM-as-judge detects orphan-honorific patterns; merges |
| 6 | Iltifat (person/voice shift) interrupted at boundary | HARD constraint (Tier 1 person-voice threading + iltifat) | LLM-as-judge detects iltifat patterns; treats as Tier 1 chain |
| 7 | Voice-cluster split (Nursi → Quran citation → Nursi commentary) | Cohesion | LLM-as-judge detects voice-cluster patterns |
| 8 | Over-chunking (too small; loses argument context) | Size | Multi-meaning lower bound + minimum-chunk-size heuristic |
| 9 | Under-chunking (too large; overflows LLM context) | Size — **asymmetric-failure worse** | `chunking_budget` enforces upper bound; chunker MUST not exceed |
| 10 | Cross-chunk reference unresolved ("as mentioned in the Birinci Mesele") | Cross-reference | A7 apparatus channel re-includes reference; chunker carries cross-reference metadata; PARTIAL mitigation |

Four of these mitigations (rows 1, 5, 6, 7) depend on LLM-judge reliability — the empirical validation must specifically test these modes.

Two failure modes are deferred as research frontiers: cross-document chunking (when one translation spans multiple Nursi works, like a thematic anthology), and multi-language passage interaction beyond the atomic case (Turkish + Arabic + Persian co-occurring in patterns more complex than embedded ayah).

### 9. Pattern-level applicability

The chunking design generalizes to multilingual religious-theological translation broadly. Bible translation has verse/pericope/chapter structure; Quran translation has ayah/ruku/hizb/juz; Hindu scripture has sloka/adhyaya. The corpus-specific source-natural-units belong on `SourceDescriptor` per corpus. The corpus-agnostic strategy enum, the A4-driven defaults pattern, the harmony-layer-aware constraint cascade, and the hybrid LLM mechanism all transfer. When Comprehenslate adds a second corpus, this generalization claim should be empirically verified — flagged in Open Questions below.

## Next Actions

### MUST

- **What:** Run the empirical validation plan on the Nursi corpus.
  **Who:** project author + Nursi-familiar reviewer to build the gold-standard set.
  **Gate:** observable — before any production translation uses LLM-based chunking.
  **Why:** This converts the LLM-based feasibility verdict from conditional to confirmed (or downgrades the recommendation to `source-structural-unit` if hybrid fails the pass criteria).

- **What:** Specify the Tier-1-preservation enforcement mechanism as a post-chunker validation pass that re-routes failures to the LLM-judge or falls back to `harmony-tier-aware`.
  **Who:** chunker implementation step (when it begins).
  **Gate:** observable — when the chunker is implemented.
  **Why:** Without this, Constraint 1 (the HARD constraint) is stated but not enforced; this same pass simultaneously addresses the heuristic-false-negative gap in the hybrid step 2.

- **What:** Codify the cascade-vs-user-override precedence rule (A6 cascade wins at `A6 ≥ light`; user receives warning with option to lower A6).
  **Who:** chunker config-resolution implementation.
  **Gate:** observable — when `chunking_strategy` interacts with A6 at config-resolution time.
  **Why:** Without this, the precedence conflict between user-explicit strategy and cascade is unresolved at runtime.

- **What:** Specify the LLM-judge confidence-return format and the fall-back threshold.
  **Who:** hybrid mechanism implementation step.
  **Gate:** observable — when the hybrid mechanism's step 3 is implemented.
  **Why:** Without this, the "fall back to structural where LLM is uncertain" rule has no operational threshold. Recommended sketch: `{decision: MERGE | KEEP | SPLIT, confidence: 0.0–1.0}` returned by the LLM; fall back when confidence < 0.7. The exact threshold should be calibrated during empirical validation.

- **What:** Add the heuristic false-negative mitigation (the post-chunker Tier-1-preservation validation pass above doubles as this mitigation when bundled).
  **Who:** chunker implementation step.
  **Gate:** observable — when the hybrid mechanism's step 2 heuristic is implemented.
  **Why:** Without a catch-all mechanism, a Tier 1 chain could silently split through a heuristic miss. Bundling with the Tier-1-enforcement pass closes both gaps with one mechanism.

- **What:** Complete the cost analysis with output-token cost; verify the assumed Opus pricing against current Anthropic pricing as of the inquiry date.
  **Who:** finding-polish pass.
  **Gate:** time-bound — before the finding is referenced as canonical cost evidence.
  **Why:** The current cost estimate uses input-token-only and an assumed rate. Production cost decisions need verified numbers.

- **What:** Build out the dependent schemas the placement decision rests on — `SourceDescriptor` (with `source_chunking_units` field) and `PipelineConfig` (with `chunking_budget`) — and extend `TranslationConfig` with the `chunking_strategy` field.
  **Who:** schema implementation step (when the edge-case innovation's Group α `SourceDescriptor` inquiry runs and ships).
  **Gate:** condition-bound — when the edge-case innovation is actually built. The chunking design's implementation can begin once those schemas exist.
  **Why:** The placement decision committed here is conditional on these schemas existing.

- **What:** Declare the Nursi corpus's `SourceDescriptor` with Mesele as `nesting_level=0`, paragraph as `nesting_level=1`, and embedded ayahs as `is_atomic=True`.
  **Who:** schema implementation step + Nursi-familiar reviewer.
  **Gate:** observable — when `SourceDescriptor` is implemented and Nursi-specific instance is created.
  **Why:** This formalizes the user's de-facto mesele-level practice as the Nursi-specific default, honoring the FORMALIZATION-phase framing this inquiry adopted.

- **What:** Implement the `ChunkingUnit.is_atomic` and `ChunkingUnit.attached_to` fields to integrate edge-case #1 (`embedded_source_languages`) and edge-case #6 (`source_apparatus_handling`) with chunking.
  **Who:** `SourceDescriptor` schema implementation step.
  **Gate:** observable — when `ChunkingUnit` is implemented; this is the same step as the Nursi declaration above.
  **Why:** These fields mitigate failure modes 3 (embedded ayah split) and 4 (hashiye orphan), both HARD-constraint or cohesion-class failures.

- **What:** Quote `notes.md` multi-meaning policy and at least 2-3 `harmony_layer.md` Tier 1 entries verbatim in the finding's load-bearing claim sites.
  **Who:** finding-polish pass.
  **Gate:** time-bound — bundle with the cost-analysis completion + pricing verification.
  **Why:** The critique's External-Grounding Absence flag is partial; quoting the canonical sources verbatim at load-bearing claims lifts the mechanism-independence quarantine.

### COULD

- **What:** Implement the caching architecture for chunker output (keyed by source-hash + chunker-version; invalidate on source-edition change).
  **Who:** chunker implementation step.
  **Gate:** condition-bound — when LLM-based chunking is first used.
  **Why:** Caching is what makes the $10–20 cost amortize across many translation runs. Simple file-cache sufficient initially; KV-store later if multiple installations emerge.
  **Depends-on:** MUST item "empirical validation passes." This COULD is GATED — do not invest in cache architecture until validation confirms the LLM-based approach is the operational default.

- **What:** Codify the passage_typology × chunking orthogonality explicitly (chunking determines boundaries; passage_typology labels TYPE per chunk).
  **Who:** the `passage_typology` edge-case finding when it is reified into a real proposal.
  **Gate:** condition-bound — when `passage_typology` is reified beyond the edge-case innovation pass.
  **Why:** Prevents future conflation of sister concepts.
  **Depends-on:** MUST item "schema build-out." This COULD is GATED — passage_typology depends on the same schema cascade.

- **What:** A4 finding maintenance pass — add the `chunking_strategy` column to the existing A4 matrix; bundle with the existing pending A6/A7/A8 naming-refinement notes from prior findings.
  **Who:** A4 finding maintainer.
  **Gate:** condition-bound — at the next A4 maintenance pass.
  **Why:** Keeps the A4 matrix internally consistent across all dependent axes. Ride the same pass that the A6, A7, A8 findings already flagged.

- **What:** Develop the voice-cluster pattern recognition in the LLM-judge prompt context.
  **Who:** chunker implementation step (LLM-judge prompt design).
  **Gate:** condition-bound — when the hybrid mechanism's LLM-judge step is implemented.
  **Why:** Mitigates failure mode 7 (voice-cluster split); cross-references edge-case #4 (`voice_disambiguation`).
  **Depends-on:** MUST item "hybrid mechanism implementation." This COULD is GATED — voice-cluster awareness composes with the LLM-judge.

- **What:** Codify the staged sequencing for follow-up work (empirical validation FIRST; deferred items as separate downstream inquiries; REFINE targets that should land in this finding).
  **Who:** CONCLUDE (this step).
  **Gate:** observable — at the time of writing this finding.
  **Why:** Critique's Assembly-3 REFINE flagged that single-package bundling reduces ability to partially close work. The Next Actions structure here implements the sequencing.

### DEFERRED

- **What:** 3-category UX collapse for `chunking_strategy` (the simpler `structural` / `harmony-aware` / `LLM-based` enum).
  **Gate:** revival trigger — ≥3 inquiries where users default-accept `chunking_strategy` without tuning, indicating the 8-literal precision isn't being used.
  **Why (if revived):** Simpler user surface; less tuning precision needed.

- **What:** Cross-document chunking design (when one translation spans multiple Nursi works in a thematic anthology).
  **Gate:** revival trigger — when a thematic-anthology use case actually emerges.
  **Why (if revived):** Current model is single-document-scoped; thematic anthology breaks the assumption.

- **What:** Multi-language passage interaction beyond the embedded-ayah atomic case (Turkish + Arabic + Persian co-occurring in non-atomic patterns).
  **Gate:** revival trigger — when a polyglot use case emerges beyond the atomic case.
  **Why (if revived):** Current `is_atomic` field handles the atomic case; non-atomic polyglot patterns need a broader strategy.

- **What:** Generalization-to-broader-pattern verification on a second corpus (Bible, Quran, Hindu scripture).
  **Gate:** condition-bound — when Comprehenslate adds a second corpus.
  **Why (if revived):** Verifies that the split-placement + strategy enum + A4-defaults pattern actually transfers cleanly.

## Reasoning

The structurally non-obvious decisions in this finding had alternatives that were considered and rejected. The rejections matter — they show why the deliverable lands where it does.

**Why three operations, not one.** The single-operation framing (chunking = source segmentation only) was the natural simplification — the user's question hinted at it, and the RAG literature pushes it. It was rejected on structural grounds. The multi-meaning preservation policy (already a Layer-2 always-on policy in the project) puts a chunk-size lower bound that operates at runtime, binding to LLM-context decisions, not source-declaration decisions. If chunking were a single operation owned by source segmentation, this binding has no schema home. The disaggregation was necessary to keep the existing policy's runtime semantics coherent.

**Why split-placement, not a 9th axis.** The 9th-axis framing matches the user's initial wording and was the natural simplification on the user side. It was rejected on three structural grounds, each independently sufficient: schema ownership (source-natural-units are source properties), runtime-vs-design separation (chunking budget is engineering concern, not translation strategy), and corpus generalization (different corpora have different source-units, and the split absorbs the variance cleanly). The 9th-axis framing would have forced a category-shape mismatch that scaled poorly to non-Nursi corpora.

**Why hybrid, not pure LLM or pure structural.** Two alternatives were tested. Pure structural (`source-structural-unit` alone) was rejected because Nursi's istilzam chains can span multiple mesele, which structural chunking would split — though this conditional rejection is empirically verifiable, and the failure recovery path in the validation plan explicitly downgrades the recommendation to pure structural if structural alone passes the criteria. Pure LLM (`LLM-detected` or `harmony-tier-aware` single-pass) was retained as a viable enum literal but rejected as the recommended default because hybrid achieves comparable quality at roughly half the cost by firing the LLM only on heuristic-flagged regions.

**Why a 9th-axis-style strategy enum but on a split-schema home.** The strategy enum *content* (8 literals + A4-driven defaults) replicates the pattern of the existing 8 axes (each axis has an enum + per-A4-purpose defaults + cross-axis interactions). This pattern-consistency was a deliberate design choice — it keeps the new chunking surface familiar to anyone who has worked with the existing axes. The deliberate non-replication is the placement (split across three schemas, not 9th axis on TranslationConfig).

**The Tier 1 hard constraint stayed absolute.** The alternative — making the constraint advisory — was considered and rejected because it would contradict the existing `harmony_layer.md` foundational commitment that Tier 1 form *is* meaning. The hard-constraint stance inherits from existing project policy and cannot be reversed without a separate finding that re-opens harmony_layer.

**Why the FORMALIZATION framing.** The user's existing manual workflow chunks at mesele level (visible in `4_mesele_en.md`). The alternative framing — design chunking from scratch without honoring the implicit practice — would have produced a competing default. The chosen framing makes the de-facto practice into the Nursi-specific default declaration, and the recommended approach is structured so the user's existing intuition is preserved as the structural baseline of the hybrid mechanism.

**External-grounding partial.** The critique flagged that some load-bearing claims (Tier 1 preservation; multi-meaning policy) cite the canonical sources structurally without quoting them verbatim. This is documented as a MUST refinement that the finding-polish pass should close before the finding is referenced as canonical evidence. The mechanism-independence status is partial-validated; verbatim quotes lift it to validated.

**The critique's two REFINE candidates landed as Next Actions, not as KILLs.** Both REFINEs (P4 enforcement mechanism + cascade resolution; P5 confidence threshold + heuristic false-negative + pricing verification) carry concrete refinement directions. The structural commitments survive; the operational specifications need closing. This is why no candidate was KILLed — every candidate held on structural grounds, with specific operational gaps that close as MUST work.

## Open Questions

### Monitoring

- After the empirical validation runs, observe whether the pass criteria (≥95% Tier-1 preservation, ≥80% boundary precision, ≥90% LLM-judge agreement) hold. If they do, the recommendation stands; if not, the recommendation downgrades to `source-structural-unit` and hybrid moves to research frontier.
- After the first 5 translations using the chunker, observe whether the per-page cost estimates hold in production (the $10–20 per Risale-i-Nur estimate is one-shot; per-translation marginal cost depends on caching effectiveness).
- After the first chunker QA pass on actual Nursi material, observe whether the 10 failure modes are exhaustive at this resolution. New modes may emerge that the inquiry's surfacing pass didn't catch.

### Blocked

- Empirical validation depends on `SourceDescriptor` being implemented first (so the Nursi declaration can be made and tested against). Cannot complete the MUST validation until the edge-case innovation's Group α inquiry ships.
- The voice_disambiguation × chunking COULD depends on edge-case #4 being reified beyond the innovation-pass candidate state.

### Research Frontiers

- **3-category UX collapse for `chunking_strategy`.** Worth investigating if usage data shows tuning isn't happening. No known threshold yet; revival trigger is observable.
- **Cross-document chunking.** Required when a translation spans multiple Nursi works (thematic anthology pattern). No current use case forces it.
- **Multi-language passage interaction beyond atoms.** Required when polyglot patterns more complex than embedded-ayah emerge. No current use case forces it.
- **Generalization verification.** When a second corpus is added (Quran, Bible, Hindu scripture), the placement-and-strategy-enum design needs empirical verification on that corpus. Long-horizon.

### Refinement Triggers

- If real translations reveal that the chunker's per-page output systematically over- or under-shoots the operational guidance, revise the per-strategy mechanism without changing the qualitative structure.
- If `source-structural-unit` alone passes the empirical validation pass criteria, downgrade the recommendation from `hybrid` to `source-structural-unit` and move hybrid to research frontier.
- If the cascade-vs-user-override warning produces user friction (users repeatedly lower A6 to permit simpler chunking), revisit the cascade-wins precedence and consider a user-explicit-wins variant.
- If the post-chunker Tier-1-preservation validation pass produces excessive false-positives (rejecting chunker output that's actually fine), revisit the validation pass's strictness.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
what about chunking , lets dive deep about this. how it should work, why it is importnat , what chunking options are feasible as config, LLM based chuking possible? ...
```

</details>
