# Sensemaking — Chunk Types vs Mechanisms

## User Input

`_branch.md` + `articulate_simple.md` + `surfacing.md`. Synthesis priors: chunking finding (under revision) + LOOP_DIAGNOSE finding (MC2 first branch-test).

---

## SV1 — Baseline

The chunking finding's `chunking_strategy` 8-literal enum on `TranslationConfig` mixes two conceptual axes: TYPES (what kind of chunks exist — sentence/paragraph/passage/...) and MECHANISMS (how to find chunks — LLM-detected/fixed-budget/hybrid/...). The user identified the conflation; this inquiry must produce a revised schema. The LOOP_DIAGNOSE MC2 (Comparative-Pattern Test perspective) is being branch-tested by this inquiry's existence.

---

## Phase 1 — Cognitive Anchor Extraction

**Constraints:**
- **C1** — Split-placement architecture (SourceDescriptor / PipelineConfig / TranslationConfig) is preserved (LOOP_DIAGNOSE confirmed).
- **C2** — Existing TC axes A1-A8 are clean single-axis fields; the revised chunking field must match this pattern.
- **C3** — `SourceDescriptor.ChunkingUnit` already separates type (name) from mechanism (detector) from property (is_atomic) from relation (attached_to). The substrate already encodes the separation in SD; TC's chunking_strategy violated it.
- **C4** — Anti-bloat: user prefers minimal user-facing surfaces; 5+ field additions to TC for a single concern is over.
- **C5** — Tier 1-2 preservation hard constraint must survive the redesign.
- **C6** — A4-driven defaults pattern must survive (per chunking finding); but the matrix entries referencing mechanism-literals (`harmony-tier-aware`, etc.) need re-homing.

**Key Insights:**
- **K1** — The conflation is categorically the same as the LOOP_DIAGNOSE-diagnosed facts-vs-strategies conflation. Both merged two distinct conceptual axes into one field. **The chunking finding's "survived intact" claim from LOOP_DIAGNOSE is now CHALLENGED.** Chunking has its own conflation that the chunking critique missed — same critique-stage failure as edge-cases critique.
- **K2** — User-named types form a STRICT NESTING HIERARCHY (chapter > subchapter > passage > paragraph > sentence). This is a corpus-agnostic granularity ladder. A hierarchical-ladder enum (`chunking_granularity`) is structurally meaningful, not arbitrary.
- **K3** — SourceDescriptor's existing `ChunkingUnit.name` + `ChunkingUnit.detector` separation IS the type-vs-mechanism distinction already implemented. The revised TC field should align with SD's pattern, not invent a new one.
- **K4** — Hybrid (the chunking finding's recommended operational default) is a MECHANISM. It needs a home. Where it lands depends on whether mechanism is exposed as user-config or hidden as AI implementation.
- **K5** — User asked "what kind of chunks exist" — the question is ontological, not procedural. The user wants a clean TYPE enum. Mechanism is HOW to produce the types and is downstream of the type decision.
- **K6** — The 5 mechanism literals don't all sit on one mechanism axis cleanly either. `harmony-tier-aware` is a CONSTRAINT modifier (applies on top of another mechanism); `hybrid` is a COMPOSITION (combines mechanisms); `LLM-detected` and `fixed-budget-with-snap` are PRIMARY mechanisms. So even if mechanism becomes a separate axis, it has internal sub-structure.

**Structural Points:**
- **S1** — The right schema-shape has THREE candidate architectures that survive structural scrutiny: (a) TYPE only on TC with mechanism HIDDEN as AI-pipeline implementation; (b) TYPE only on TC with mechanism explicitly on a DIFFERENT schema (PipelineConfig — runtime mechanism is a pipeline concern); (c) TYPE and MECHANISM both on TC as two separate fields.
- **S2** — Variant 5 (TC has canonical types + SD provides corpus-specific) is the integration with existing substrate. SD's ChunkingUnit already declares corpus-types per corpus; TC's enum needs to either (i) reference SD's top-level declared unit OR (ii) have a generic enum that the AI maps to the closest declared SD unit.
- **S3** — Variant 4 (hierarchical-ladder) and the canonical type list converge: chapter / subchapter / passage / paragraph / sentence ARE the canonical user-named ladder. The user's intuition matched the ladder shape directly.
- **S4** — The chunking finding's A4-driven defaults table needs revision: defaults that named mechanism-literals (scholarly → `harmony-tier-aware`) need to be re-expressed as either (i) type defaults only (scholarly → `passage`?) or (ii) type + mechanism defaults.
- **S5** — MC2 is being VALIDATED by this inquiry's existence. The user performed exactly the comparative-pattern check that MC2 describes: comparing each literal against the others and against existing TC axes, noticing that chunking_strategy violates the pattern. This is strong evidence for MC2 promotion.

**Foundational Principles:**
- **P1** — Schema ownership matches data ownership (from chunking finding; survives — this inquiry doesn't invalidate it, just sharpens its application).
- **P2** — TC fields should match the existing pattern of A1-A8 (single coherent axis per field). This is the rule that catches chunking_strategy's conflation.
- **P3** — Anti-bloat: minimize user-facing surface; prefer hidden internal mechanism over user-exposed unless user-choice is meaningful.
- **P4** — Substrate-reachability (from LOOP_DIAGNOSE): the conversation correction used existing substrate; here the user did too — they compared chunking_strategy against the existing TC pattern.

**Meaning-Nodes:**
- **M1 — chunk type** — what kind of unit; categorical / hierarchical.
- **M2 — chunking mechanism** — how to find/produce the unit; algorithmic.
- **M3 — granularity ladder** — the hierarchical ordering of types by size: chapter > subchapter > passage > paragraph > sentence.
- **M4 — corpus-specific type** — declared per-corpus via SD (mesele, ayah, sloka) beside canonical types.
- **M5 — primary/constraint/composition mechanism** — three sub-categories of mechanism.
- **M6 — hybrid-as-mechanism** — the chunking finding's recommended operational default needs a new home.
- **M7 — LOOP_DIAGNOSE chunking-survived claim challenged** — chunking has its own conflation that survived its own critique.

### SV2

The chunking_strategy enum mixed type + mechanism. The user wants a clean separation. The revised schema must (a) expose a clean chunk-TYPE field that matches the existing A1-A8 pattern, (b) decide where MECHANISM lives (hidden internal vs explicit TC field vs PipelineConfig field), (c) integrate with SD's existing ChunkingUnit name/detector split, (d) preserve the A4-driven defaults pattern (with revised matrix entries), (e) preserve the recommended hybrid approach's value (with a new home for "hybrid" as mechanism). MC2 is being validated.

---

## Phase 2 — Perspective Checking

**Technical / Logical.** Pydantic supports both flat enums (`Literal[...]`) and 2-field schemas cleanly. The simpler is better unless 2-field provides distinct user value. Hidden mechanism (Variant 3) shifts the choice to AI implementation — but AI needs a way to decide; the harmony-tier-aware default behavior (preserve Tier 1) is non-negotiable per C5. So mechanism isn't really hidden; it's just NOT user-configurable.
→ **A1** — Mechanism's choice has a non-trivial default (harmony-aware structural + LLM-judge for ambiguous). The AI applies this. Whether the USER can override is the question; the AI's default behavior is constant.

**Human / User.** User asked "what kind of chunks exist" — wants ontological clarity. User did not ask "give me a knob for mechanism." User cares about TYPE choice; mechanism is plumbing.
→ **A2** — User-visible field should be TYPE only. Mechanism should be either hidden or on a different schema (PipelineConfig) that advanced users can tune.

**Strategic / Long-term.** When Comprehenslate adds a second corpus (Bible, Quran), the corpus declares its own types via SD. TC's type field needs to be either canonical (sentence/paragraph/passage/subchapter/chapter — corpus-agnostic) OR a reference to SD's declared types. The cleanest pattern: TC's enum is canonical; SD's declared corpus-types are MAPPED to canonical types (Nursi's mesele ≈ subchapter; Quran's ayah ≈ sentence).
→ **A3** — TC enum is corpus-agnostic canonical ladder; SD maps corpus-specific types to canonical positions.

**Risk / Failure.** If mechanism becomes a user-visible TC field, anti-bloat suffers (5+ mechanism literals expose internal complexity). If mechanism is hidden but the AI's default mechanism doesn't preserve Tier 1, the hard constraint breaks. The risk is in the IMPLEMENTATION of the default mechanism, not in user-config.
→ **A4** — Hidden mechanism is safer if the default mechanism is harmony-tier-aware + structural baseline + LLM-as-judge for ambiguous regions (the chunking finding's recommended hybrid). The AI ALWAYS does this. User doesn't pick.

**Resource / Feasibility.** Both variants (2-field vs 1-field-with-hidden-mechanism) are implementable. The 1-field variant is simpler; 2-field adds a configuration surface that needs documentation, defaults, validation.
→ **A5** — 1-field is cheaper to build and document.

**Definitional / Internal Consistency.** Compare against A1-A8: each is a single coherent axis with a single semantic. The chunking_strategy field's revised form must match. `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]` matches the pattern exactly (A6's `off/minimal/light/standard/maximum` is the closest analog — an ordinal ladder of preservation; this would be an ordinal ladder of granularity).
→ **A6** — Hierarchical-ladder type field (Variant 4) matches the existing A1-A8 pattern most closely.

**Definitional / Frame-exit Completeness.** Gating predicate: this inquiry inherits terms from chunking finding (chunking_strategy / hybrid / harmony-tier-aware) used across multiple values. GATING FIRES.

1. **Existence Enumeration.** What does "chunk" refer to project-wide?
   - the user-named canonical types (sentence/paragraph/passage/subchapter/chapter) — granularity-ladder positions
   - corpus-specific types declared in SD (mesele, ayah, sloka)
   - LLM-context chunks (token-budget-bounded; produced by mechanism not by type — a runtime concern)
   - config-application chunks (the unit at which TranslationConfig applies — per chunking finding section 1 operation iii)
   
2. **Role Assessment.** All four referents are relevant. The corpus-types (SD) and canonical types (TC) are the user-visible TYPE axis. LLM-context chunks are a MECHANISM concern (PipelineConfig). Config-application chunks ARE the chosen type (when user picks `paragraph`, the config applies per-paragraph).

3. **Verdict Rigor.** Counter to the proposed revision: "mechanism is needed by user to choose between hybrid vs harmony-aware vs structural for cost reasons." Counter fails: cost concerns belong on PipelineConfig (which already has chunking_budget); user-strategy belongs on TC. Cost-vs-quality tuning of mechanism is a PipelineConfig concern.

4. **Residual.** Is there a frame-exit concern not captured? **Yes** — the `source-structural-unit` literal in the old enum was a TYPE-FINDING-RULE (use whatever SD declares as top-level). Under the revised type ladder, "source-structural-unit" doesn't have a clean position (it's a meta-reference, not a fixed level). The handling: TC's type field uses the canonical ladder; the AI's mapping logic says "if the corpus declares a unit at level X, prefer the declared unit name over the canonical name."
→ **A7** — Source-structural-unit becomes implicit; the AI prefers SD's declared name when available, falls back to canonical ladder otherwise.

**Phase / Calibration-State.** Framework-closure-stage-plus-plus. This inquiry refines a recent chunking finding before code lands. Calibration urgency: HIGH (correction before propagation).
→ **A8** — Cheap to fix now; expensive to fix after code lands.

### SV3

After 8 perspectives, the model crystallizes:
1. TC's field is `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]` — a clean hierarchical-ladder enum matching A1-A8 pattern.
2. Mechanism is HIDDEN — AI applies a default (structural baseline + harmony-tier-aware constraint + LLM-as-judge for ambiguous regions). User does NOT pick mechanism.
3. Cost/quality tuning of mechanism (LLM-judge or not, budget bounds) lives on PipelineConfig.
4. Corpus-specific types declared in SD are MAPPED to canonical ladder positions (Nursi mesele ≈ subchapter; Quran ayah ≈ sentence). The AI prefers SD's declared name when producing output.
5. The chunking finding's recommended hybrid approach IS the AI's default mechanism — not a user-visible choice.
6. A4 defaults revised: scholarly → `passage` or `subchapter` (whichever the source declares); devotional → use corpus's natural unit; casual → `paragraph`; language-learning → `sentence`; performance → use corpus's natural unit.
7. MC2 is being validated: the user's intuition matched MC2's described test exactly.

**Meta-Inspection at SV3:** H1 candidate set — are the 5 variants really distinct? Variant 1 (type-only-redesign) and Variant 4 (hierarchical-ladder) converge: Variant 4 IS Variant 1 with the explicit hierarchical structure. Variant 5 (SD-corpus-extension) is complementary — it's not an alternative but an integration the chosen variant must include. The viable set narrows to: Variant 1/4 (merged) + Variant 2 (two-axis) + Variant 3 (hidden mechanism). Variant 6 (MC2 validation) is meta — it's the inquiry's framing, not a schema-shape variant.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: Type-only vs two-axis schema

**Counter-interpretation:** Two-axis (Variant 2) — both type AND mechanism on TC, both user-visible.

**Why counter fails (structural):**
- Mechanism's USER VALUE is low: most users don't have a basis to choose between LLM-detected and harmony-tier-aware; the right default (harmony-aware with hybrid composition) is uniform across reasonable use cases.
- Anti-bloat (C4): 5 mechanism literals exposed to user violates user's preference; mechanism complexity has no offsetting user value.
- A4-driven defaults already handle the use-case-driven default; user doesn't need a second knob.
- Comparison to A1-A8: NONE of them expose mechanism. Form_preservation has off/minimal/light/standard/maximum — it's a preservation-LEVEL not a preservation-MECHANISM. The pattern says mechanism is implementation, not config.

**Confidence:** HIGH.

**Resolution:** TC has ONE field (chunk type only). Mechanism is hidden as AI implementation. Cost/budget tuning of mechanism (if needed by power users) lives on PipelineConfig.

### Ambiguity 2: Flat enum vs hierarchical-ladder enum

**Counter-interpretation:** Flat enum — list types unordered (paragraph, sentence, passage, ...).

**Why counter fails:** The user's listing was IMPLICITLY HIERARCHICAL (paragraph, sentence, passage, chapter, subchapter — they listed from medium to small to medium-large to large to medium-large; even if user wasn't deliberate, the SET forms a strict nesting hierarchy when ordered by granularity). Flat enums lose this ordering. Hierarchical-ladder enums (like A6 `off/minimal/light/standard/maximum`) match the existing TC pattern: each level has a meaningful position relative to others.

**Confidence:** HIGH.

**Resolution:** Hierarchical-ladder enum: `Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]`. Ordering is ASCENDING granularity (sentence is smallest; chapter is largest).

### Ambiguity 3: Where does `hybrid` live in the revised schema?

**Counter-interpretation:** Keep `hybrid` as a TC literal (it's the recommended operational default).

**Why counter fails:** `hybrid` is a mechanism-composition, not a type. Putting it in the type field reintroduces the original conflation. The chunking finding's recommended hybrid approach is the AI's DEFAULT MECHANISM — it operates regardless of which type the user chose. It's the implementation of "how to produce chunks of the requested type while respecting Tier 1-2."

**Confidence:** HIGH.

**Resolution:** `hybrid` is not a TC literal. It's the AI's default mechanism for producing chunks of any chosen type. Documented in `config_base_source.md` chunking section as "default mechanism: hybrid harmony-aware." If PipelineConfig exposes mechanism for advanced tuning, `hybrid` is one of the values there.

### Ambiguity 4: Corpus-specific types in TC enum vs SD declaration

**Counter-interpretation:** TC enum includes corpus-specific types directly: `Literal["mesele", "ayah", "verse", "paragraph", ...]`.

**Why counter fails:** Corpus-specific types are corpus-properties (per chunking finding's split-placement). Putting them in TC's user-strategy enum re-introduces the SD-vs-TC conflation that LOOP_DIAGNOSE diagnosed. The clean separation: TC enum is corpus-agnostic canonical; SD declares per-corpus types and the AI maps.

**Confidence:** HIGH.

**Resolution:** TC's enum: `Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]`. SD's `source_chunking_units` declares per-corpus types with `canonical_level` field added: `class ChunkingUnit(BaseModel): name: str; detector: ChunkingDetector; canonical_level: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]; is_atomic: bool; attached_to: str | None`. AI uses SD's declared name in output, mapped to the chosen TC level.

### Ambiguity 5: Mechanism user-visible (PipelineConfig) vs internal

**Counter-interpretation:** Mechanism is internal, no PipelineConfig field needed.

**Why partial:** Most users don't tune mechanism. Power users (e.g., when testing different chunking approaches for empirical validation per chunking finding's deferred MUST) might want to.

**Resolution:** Mechanism is INTERNAL by default. PipelineConfig can optionally expose a `chunking_mechanism_override: Literal["structural", "llm-detected", "harmony-tier-aware", "hybrid"] | None = None` for advanced/eval use. The override is opt-in; AI's default behavior is `hybrid` (per chunking finding recommendation).

### Ambiguity 6: Does this case invalidate LOOP_DIAGNOSE's "chunking survived intact" claim?

**Counter-interpretation:** No — LOOP_DIAGNOSE was diagnosing the SD-vs-TC misrouting in the edge-cases inquiry; it wasn't auditing the chunking finding for OTHER conflations.

**Why partly right:** LOOP_DIAGNOSE's scope was the SD-vs-TC misrouting; it correctly attributed that failure away from chunking. It didn't promise chunking had no other issues.

**But also:** LOOP_DIAGNOSE's finding text said "The chunking finding's own per-field routings (#1, #6, #7) are correct applications. No misrouting in chunking finding itself." This statement is true for the routings; but it doesn't address the conflation IN the chunking_strategy enum (which is a different type of failure — not routing but field-internal conflation). The "survived intact" framing was too strong.

**Confidence:** MED.

**Resolution:** LOOP_DIAGNOSE's chunking-routings-correct claim STANDS. The chunking finding's `chunking_strategy` enum HAS a separate type-vs-mechanism conflation that LOOP_DIAGNOSE did not examine. The chunking finding's critique stage missed THIS conflation too — same critique-stage failure as edge-cases critique. **MC1 (Candidate-Self-Consistency sub-axis) and MC2 (Comparative-Pattern Test perspective) would have BOTH caught the chunking_strategy conflation:** MC1 because the enum's literals make incompatible internal claims (some name types, some name mechanisms); MC2 because comparing chunking_strategy against A1-A8 shows it doesn't match the pattern. Strong additional evidence for both MCs.

### SV4

**Clear:**
- TC's revised field: `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]` with default `paragraph` (from A4 chain to casual).
- Mechanism HIDDEN; AI's default is hybrid harmony-aware (per chunking finding).
- SD's ChunkingUnit gets a `canonical_level` field linking to TC's ladder.
- PipelineConfig optionally exposes mechanism override for advanced/eval use.
- A4 defaults revised per type-only.
- Both LOOP_DIAGNOSE MCs (MC1 + MC2) would have caught this; strong evidence for promotion.
- LOOP_DIAGNOSE's chunking-routings-correct claim survives; its "chunking survived intact" framing was too strong — chunking_strategy enum has its own conflation.

**No longer viable:**
- Two-axis TC schema (mechanism as user-visible TC field).
- Flat enum (loses hierarchical structure).
- `hybrid` as a type literal.
- Corpus-specific types directly in TC enum.

---

## Phase 4 — DOF Reduction

**Fixed:**
- TC field name: `chunking_granularity`.
- TC enum: 5 literals (sentence / paragraph / passage / subchapter / chapter).
- Default: `paragraph` (A4 chain to casual).
- Mechanism: hidden by default; default = hybrid harmony-aware.
- SD addition: `ChunkingUnit.canonical_level: Literal[...]`.
- PipelineConfig optional `chunking_mechanism_override: Literal[...] | None = None`.

**Eliminated:**
- Two-axis TC schema.
- Flat enum.
- `hybrid` / `LLM-detected` / `fixed-budget-with-snap` / `harmony-tier-aware` / `passage-typology-aware` as TC literals.
- Corpus-specific types directly in TC.

**Viable paths remaining:**
- Variant 1+4 (type-only hierarchical-ladder) merged with Variant 5 (SD-corpus-mapping integration). SURVIVES as the chosen architecture.
- Variant 2 (two-axis) KILLED.
- Variant 3 (hidden mechanism) ABSORBED into the chosen architecture.
- Variant 6 (MC2 validation) is the inquiry's meta-framing.

### SV5

Solution space organized as:
1. **TC schema:** `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]` with A4-driven defaults.
2. **Default mechanism (hidden):** hybrid harmony-aware per chunking finding's recommendation. AI applies regardless of user choice.
3. **SD integration:** `ChunkingUnit` gets `canonical_level` field; AI uses SD's declared name when producing output, mapped to user's chosen granularity.
4. **PipelineConfig:** optional `chunking_mechanism_override` for advanced tuning.
5. **A4 default revision:** scholarly → passage / devotional → use corpus's natural unit (at subchapter level for Nursi mesele) / casual → paragraph / language-learning → sentence / performance → use corpus's natural unit.
6. **Cross-cutting:** Tier 1-2 preservation hard constraint applies to AI's mechanism regardless of granularity choice.
7. **Meta-output:** MC1 + MC2 strengthened evidence; LOOP_DIAGNOSE finding gets a note that chunking_strategy enum had its own conflation (the chunking-routings-correct claim survives; the "survived intact" framing weakens).

---

## Phase 5 — Conceptual Stabilization

**Accommodation trigger check:** Did perspectives destabilize? Each perspective reinforced and refined; Frame-exit Completeness produced the source-structural-unit residual resolution (A7); no destabilization. Accommodation NOT fired.

### SV6 — Stabilized model

**The chunking_strategy field is replaced by `chunking_granularity: Literal["sentence", "paragraph", "passage", "subchapter", "chapter"]` — a corpus-agnostic hierarchical-ladder enum matching the existing A1-A8 pattern. Mechanism is hidden as AI implementation (default: hybrid harmony-aware per the chunking finding's recommendation). SourceDescriptor's `ChunkingUnit` gets a `canonical_level` field mapping corpus-specific declared types (mesele, ayah, etc.) to the canonical ladder. PipelineConfig optionally exposes a `chunking_mechanism_override` for advanced tuning. A4-driven defaults are revised to use only types. The chunking finding's recommended hybrid harmony-aware mechanism survives as the AI's default — same operational behavior, different schema home. MC1 and MC2 from LOOP_DIAGNOSE would have BOTH caught this conflation; strong evidence for their promotion. LOOP_DIAGNOSE's claim that chunking's routings are correct stands; its "survived intact" framing was too strong — the chunking_strategy enum had its own field-internal conflation that the chunking critique missed.**

### SV6 vs SV1 delta

SV1 framed the question as "fix the bad literals." SV6 reframes: the conflation is the same category-error pattern LOOP_DIAGNOSE diagnosed; the resolution is a clean hierarchical-ladder type enum on TC + hidden mechanism + SD canonical-level mapping + PipelineConfig override option + A4-default revision. MC2 is validated in real-time. The chunking finding text and LOOP_DIAGNOSE finding text both need notes.

---

## Telemetry

- 8 perspectives applied; convergence by SV3.
- 6 ambiguities resolved (4 HIGH + 2 MED).
- 8 A-anchors + 6 constraints + 7 insights + 5 structural points + 4 principles + 7 meaning-nodes.
- SV delta: substantial (5-architectural-variants → 1 chosen architecture).

### Failure-mode check
- Status Quo Bias: NO — chunking finding's design is being actively revised.
- Premature Stabilization: NO — SV3 added Frame-exit Completeness insight; SV4 narrowed.
- Anchor Dominance: NO — multiple anchors load-bearing.
- Perspective Blindness: NO — uncomfortable Frame-exit Completeness applied.
- Clean Resolution Trap: NO — each ambiguity has counter + structural why-counter-fails.
- Self-Reference Blindness: PARTIAL — this inquiry validates MC2 (its own substrate); LOOP_DIAGNOSE's claim is being challenged. The self-reference is acknowledged: the AI's diagnostic loop is being applied to the AI's own prior diagnostic loop. Mitigation: the user's pushback is what triggered this; the AI's role is to systematize.

### Verdict

**PROCEED to Decomposition.**

The stabilized model has 7 components (TC field; default mechanism; SD field addition; PipelineConfig optional override; A4 defaults; cross-cutting Tier 1-2; meta-output for MC validation + LOOP_DIAGNOSE note). Decomposition partitions accordingly.
