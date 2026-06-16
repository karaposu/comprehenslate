---
status: active
model: claude-opus-4-7[1m]
effort: max
refines: devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md
corrects: devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md
---
# Finding: Loop Diagnose — SD vs TC Misrouting

## Changes from Prior

**Prior paths:**
- `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` (synthesis prior — where the "schema ownership matches data ownership" principle was articulated)
- `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md` (synthesis prior — where 3 of 4 SourceDescriptor additions were misrouted)

**Revision trigger:** User conversation correction. The user pushed back on the routing of `source_language_fluency` to `SourceDescriptor` ("it feels like translationconfig field"). The AI's reconsideration produced a snippet identifying the misrouting in three of four `SourceDescriptor` additions. The user invoked LOOP_DIAGNOSE to diagnose what went wrong in the loop chain that produced the error.

**What's preserved.** The chunking finding's own routings (#1 → `ChunkingUnit.is_atomic`, #6 → `ChunkingUnit.attached_to`, #7 → orthogonal sister-concept) are correct applications of its principle — they survive unchanged. The edge-cases inquiry's split-placement architecture, its 7 DEFER decisions, its 2 non-modifications, and the routing of `source_edition` to SourceDescriptor all survive unchanged.

**What's changed.** Three commitments in the edge-cases finding are INVALIDATED: `TranslationConfig` delta = 0; `source_language_fluency` / `source_temporal_register` / `quranic_citation_policy` routed to SourceDescriptor; `EmbeddedLanguagePolicy` carrying `quranic_citation_policy`. The chunking finding's principle is frame-revised: the principle as stated is correct, but its scope was anchored to "source-natural-units" specifically without explicit abstraction to "facts about the source vs reader-properties referencing source vs strategies for handling source." Sharpening the principle stays GATED pending a second correction-chain instance.

**What's new.** Three failure hypotheses with mixed attribution (PRIMARY × 2 + CONTRIBUTORY × 1). Two strong maintenance candidates with concrete shapes + evaluation gates: MC1 a Candidate-Self-Consistency sub-axis in the td-critique spec; MC2 a Comparative-Pattern Test perspective in the sense-making spec. One gated contributory maintenance candidate (principle sharpening in chunking finding). A corrected per-field routing table for the 4 misrouted fields.

**Migration.** Code: `translation_config.py` gains 3 new TC fields; `source_descriptor.py` is created with a SourceDescriptor stub containing source-facts only. The Phase 2 work the edge-cases finding committed to SourceDescriptor is redistributed: only `source_edition` (and optional `embedded_languages: list[str]` as facts) actually lands on SD; the other 3 fields land on TC. Finding-text: the edge-cases finding gets a Correction Notice at its top citing this diagnostic; the chunking finding gets a small inline note acknowledging the principle's scope. The in-flight 4_mesele translation work uses the corrected schema.

## Question

From `_branch.md`:

> Use LOOP_DIAGNOSE to diagnose what went wrong in the loop chain that produced the SourceDescriptor-vs-TranslationConfig misrouting visible in the conversation correction snippet. Given the user pointed at the chunking finding as the chain's starting reference but the actual misrouting was committed in the downstream edge-cases-into-config-schema inquiry, the diagnostic scope is the chain — chunking established the principle ("schema ownership matches data ownership") → edge-cases applied it (incorrectly, conflating facts-about-the-source with strategies-for-handling-the-source) → conversation correction revealed the misapplication.

The goal: produce evidence-backed failure hypotheses, attribute the failure across the chain with mixed attribution allowed, and propose maintenance candidates with concrete evaluation gates — while respecting LOOP_DIAGNOSE's guardrails (conversation correction is comparative evidence, not ground truth; no broad rewrites from one correction chain; allow mixed or unknown attribution).

## Finding Summary

- **The misrouting was NOT at the chunking finding.** The chunking finding's principle ("Schema ownership matches data ownership. Source-natural-units are properties of the source ... SourceDescriptor is the natural home" — finding.md line 113, verbatim) is correctly stated. Its own per-field routings (#1, #6, #7) are correct applications. The chunking finding contributes to the failure only by anchoring the principle to "source-natural-units" specifically without abstracting it to "facts vs reader-properties vs strategies."

- **The misrouting was committed in the edge-cases-into-config-schema inquiry at sensemaking SV6**, where Ambiguity 4's resolution committed `source_language_fluency` → SourceDescriptor with reasoning that contradicted itself ("A3 keeps its existing meaning; the new field captures language-fluency" — but A3 lives on TranslationConfig). The Frame-exit Completeness perspective fired in that inquiry's sensemaking — but on the wrong axis (about chunking, not about Group α SourceDescriptor membership types).

- **The edge-cases critique failed to catch the misrouting** despite the smoking gun being present in the candidate's own text. The P3 docstring for `source_language_fluency` explicitly says "Refines A3 source_culture by adding the fluency dimension WITHOUT modifying A3." A3 lives on `TranslationConfig`. A field that "refines A3" routed to `SourceDescriptor` is internally inconsistent. The substance-axis prosecution did not apply the candidate's own internal claims (the docstring) against the candidate's own decision (the SourceDescriptor routing). None of the 8 critique dimensions explicitly tests "does this routing apply the inherited principle correctly?"

- **The substrate for catching the error was available to the original inquiries.** The existing 8-axis schema in `config_base_source.md` shows A1 reader_level, A2 domain_expertise, A3 source_culture all as reader-properties on `TranslationConfig` — the exact comparative pattern that `source_language_fluency` should have matched. The user's pushback used this pattern; the loop did not. The failure is "missing test against available information," not "missing information."

- **Two strong maintenance candidates with concrete evaluation gates.** **MC1** adds a Candidate-Self-Consistency sub-axis to the td-critique spec's Multi-axis prosecution depth check: when a candidate's text contains internal claims (docstrings, named-pattern references, justifications), construct at least one prosecution that applies those internal claims against the candidate's structural decisions. **MC2** adds a Comparative-Pattern Test perspective to the sense-making spec's Phase 2 perspective list: when an inquiry commits a structural-routing decision, explicitly compare each candidate against the existing pattern of analogous decisions in the target schema. Both have low risk (additive refinement notes), concrete evaluation gates (branch-test on next bulk-edge-case inquiry; observe whether they fire and catch at least one issue), and should become branch experiments before being promoted to canonical specs.

- **One gated contributory maintenance candidate.** **MC3** would sharpen the chunking finding's principle to explicitly distinguish facts about the source from reader-properties from strategies. It is GATED pending a second correction chain involving the same conflation pattern (per LOOP_DIAGNOSE guardrail against broad rewrites from one chain).

- **Corrected per-field routing.** Of the 4 edge-cases that the previous inquiry routed to `SourceDescriptor`: `source_edition` stays on SourceDescriptor (genuine source fact); `source_language_fluency` moves to TranslationConfig (reader-property); `source_temporal_register` moves to TranslationConfig (strategy enum); `quranic_citation_policy` moves to TranslationConfig (strategy enum). The corrected TranslationConfig delta is +3 fields, not 0.

- **Diagnostic Verdict: ACTIONABLE.** At least one maintenance candidate (MC1) has enough evidence and a concrete evaluation gate. The recommended next step is branch-testing MC1 and MC2 on the next bulk-edge-case inquiry. MC3 stays gated.

- **Self-Reference Blindness partial mitigation acknowledged.** The AI is running disciplines on its own prior outputs. LOOP_DIAGNOSE's comparative-evidence framing (treating the conversation correction as evidence, not ground truth) plus the user-pushback trigger plus the Frame-exit Completeness perspective applied to a different axis than the original inquiry used together provide partial mitigation. Residual blind spot: the AI's reasoning may protect aspects the user did not push back on.

## Finding

### Why this matters (the goal context)

The Comprehenslate project is building an AI-assisted translation system. Three recent inquiries have run in sequence: the chunking deep-dive (which established a split-placement architecture across `SourceDescriptor` + `PipelineConfig` + `TranslationConfig` based on the principle "schema ownership matches data ownership"), the edge-cases-into-config-schema inquiry (which applied that principle to 14 edge-case candidates and produced a per-field decision table), and this LOOP_DIAGNOSE inquiry (which diagnoses why the second inquiry misrouted three of four `SourceDescriptor` additions despite running the full /aMVLwr loop and producing a clean critique).

The user's pushback in conversation ("this doesn't make sense — `source_language_fluency` feels like a `TranslationConfig` field") triggered an AI reconsideration that re-routed three fields. The user then invoked LOOP_DIAGNOSE to ask not "what's the right routing?" but "why did the loop fail?" — a diagnostic question about the loop framework itself.

This finding's value is structural: it identifies the specific failure loci, proposes specific spec changes with branch-test evaluation gates, and respects the LOOP_DIAGNOSE protocol's guardrails (no broad rewrites; conversation correction as comparative evidence; mixed attribution allowed).

### 1. Correction Chain Summary

**Prior path 1 — chunking deep-dive** (`devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/`). The principle was articulated at finding.md line 113, verbatim: *"Schema ownership matches data ownership. Source-natural-units are properties of the source (each corpus declares its own); putting them on `TranslationConfig` would force every translation-config to redeclare source structure. `SourceDescriptor` is the natural home."* The same finding's section 3 introduced `chunking_strategy` on TranslationConfig (correctly) and `chunking_budget` on PipelineConfig (correctly). Per-field routings #1, #6, #7 are correct.

**Prior path 2 — edge-cases-into-config-schema** (`devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/`). The per-field decision table headlined "TranslationConfig delta = 0; 4 ADD-now to SourceDescriptor." The four `SourceDescriptor` additions were `source_language_fluency`, `source_edition`, `source_temporal_register`, and `quranic_citation_policy` (as a property within `EmbeddedLanguagePolicy`). The inquiry's P3 code sketches included a docstring for `source_language_fluency` that read *"Refines A3 source_culture by adding the fluency dimension WITHOUT modifying A3."*

**Corrected direction** (comparative evidence per LOOP_DIAGNOSE; NOT ground truth). The conversation correction snippet (preserved verbatim in `_branch.md` Source Input) used a comparative-pattern argument: A1 `reader_level` / A2 `domain_expertise` / A3 `source_culture` are reader-properties on `TranslationConfig`; `source_language_fluency` fits that pattern exactly. The snippet re-routed: `source_language_fluency` → TC; `source_temporal_register` → TC; `quranic_citation_policy` → TC (or apparatus axis); `source_edition` → SD (unchanged). The snippet named the conflation: *"this source HAS embedded Arabic (source property → SD) vs how the translator should RENDER embedded Arabic (strategy → TC)."*

**Human correction signal.** The user's pushback — *"this doesnt make sense no? why SourceDescriptor has such field? it feels like translationconfig field"* — triggered the AI's reconsideration. The user did not invoke the chunking finding's principle in their pushback; they invoked their own mental model of where reader-properties live. This is structurally important: the user's intuition matched the existing 8-axis pattern, and the loop's structured tests did not.

**What changed from prior result to corrected direction.** Three of the four `SourceDescriptor` additions in the edge-cases finding were re-classified as `TranslationConfig` additions. The TC delta is +3, not 0. The SD delta is +1 (just `source_edition`) plus an optional `embedded_languages: list[str]` for the FACTS of which languages are embedded — separate from the STRATEGIES for handling them.

### 2. Failure Hypothesis 1 — Edge-cases sensemaking SV6 locked in the misrouting

**Affected stage:** Sensemaking, specifically the edge-cases inquiry's stage 3 Ambiguity Collapse that produced SV6.

**Shortcoming type:** Frame-exit Completeness perspective applied on the wrong axis. The perspective DID fire in the inquiry (the inquiry's sensemaking.md states *"Frame-exit Completeness GATING fired (chunk has 6 project-wide referents)"*). But it fired on the chunking-axis question (what does "chunk" refer to project-wide?) and not on the Group α membership-types question (what kinds of fields are bundled together in the "Group α SourceDescriptor" cluster?). The perspective's machinery existed; the relevant axis to test wasn't selected.

**Evidence from prior inquiry (edge-cases sensemaking).** Ambiguity 4's resolution committed `source_language_fluency` → SourceDescriptor with reasoning *"A3 keeps its existing meaning; the new field captures language-fluency"*. This reasoning is internally inconsistent: if A3 keeps its meaning (and A3 lives on TC), and the new field captures a dimension that refines A3, the new field should live where A3 lives. The sensemaking did not surface this internal contradiction.

**Evidence from human correction.** The user's intuition immediately matched `source_language_fluency` to the A1/A2/A3 reader-property pattern on TranslationConfig — a comparative-pattern check that the sensemaking did not perform.

**Evidence from corrected direction.** The AI's snippet used precisely the comparative-pattern argument that Frame-exit Completeness perspective would have produced if applied to Group α membership.

**Confidence: HIGH.** Three artifacts converge: the SV6 commitment is the locus where the routing was first locked in; the internal contradiction in the SV6 reasoning is concrete; the comparative pattern was reachable from substrate available at sensemaking time.

**Why not stronger.** Frame-exit Completeness application is a judgment call. The perspective DID fire, just on a different axis. Calling this a stage failure is partly judgment about which axis the perspective should have prioritized. A reviewer could read this as application-prioritization rather than stage-failure.

**Maintenance candidate:** MC2 (Comparative-Pattern Test perspective) — see section 6.

**Evaluation gate.** On the next bulk-edge-case inquiry's sensemaking, observe whether Frame-exit Completeness is applied to each candidate's distinct referent-type. Observe whether the new Comparative-Pattern Test perspective fires per routing decision. If MC2 fires and catches at least one issue: promote. If MC2 fires with no catches (clean candidate set): monitor. If MC2 does not fire: investigate adoption failure.

### 3. Failure Hypothesis 2 — Edge-cases critique missed principle-application correctness

**Affected stage:** Critique, specifically the edge-cases inquiry's Phase 2 Adversarial Evaluation of P3 (the SourceDescriptor code sketches).

**Shortcoming type:** Missing dimension + substance-axis prosecution miss. The critique used eight dimensions: Correctness, Coherence, Feasibility, Robustness, Completeness, Anti-bloat-fit, Synthesis-rigor, External-anchor compliance. None of these dimensions explicitly tests "does this routing decision apply the inherited principle correctly?" Substance-axis prosecution did fire on P3 — but it tested code-quality and composability ("concrete pydantic code; type-safe; pattern-matches existing schema design"), not the candidate's own internal claims against its own decision.

**Evidence from prior inquiry (edge-cases critique).** The critique's P3 verdict was *"SURVIVE. Clean — no refinements needed beyond what's documented inline."* The smoking gun is internal: P3's docstring for `source_language_fluency` explicitly states *"Refines A3 source_culture by adding the fluency dimension WITHOUT modifying A3."* A3 lives on TranslationConfig. A field that "refines A3" living on `SourceDescriptor` is internally inconsistent. The substance-axis prosecution did not apply this internal claim against the routing decision.

**Evidence from human correction.** The user's argument was a comparative pattern check (A1/A2/A3 are reader-properties on TC; this fits that pattern). This is precisely the kind of test the missing critique dimension would have produced.

**Evidence from corrected direction.** The AI's snippet exposed the conflation by reading the candidate's own behavior (the docstring) — the same internal-evidence reading that substance-axis prosecution should have performed.

**Confidence: HIGH.** The docstring-vs-routing internal contradiction is a smoking gun. The missing-dimension claim is supported by direct enumeration of the eight dimensions actually used.

**Why not stronger.** The Substance-vs-Label success criteria refinement at Phase 0 of td-critique says substance-level criterion is required when a dimension tests load-bearing claims. The critique's Correctness dimension HAD a substance-level criterion ("candidate text instantiates the SV6 model"). The criterion fired but produced a PASS — because the SV6 model itself contained the misrouting. The dimension performed correctly given its frame; the frame inherited the SV6 error. This means the failure is at the dimension *set* level (missing a principle-application-correctness dimension), not at the dimension *execution* level.

**Maintenance candidate:** MC1 (Candidate-Self-Consistency sub-axis) — see section 6.

**Evaluation gate.** On the next bulk-edge-case inquiry's critique, observe whether the new Candidate-Self-Consistency sub-axis is applied. Specifically, observe whether the sub-axis catches any internal-contradiction-shaped issue (docstring vs decision; named-pattern reference vs routing; justification vs structure). If applied and caught: promote. If applied with no catches (clean candidate set): monitor. If not applied: investigate adoption failure.

### 4. Failure Hypothesis 3 — Chunking principle anchored too specifically (CONTRIBUTORY)

**Affected stage:** Chunking finding's principle articulation (sensemaking SV6 commitment + finding.md section 3).

**Shortcoming type:** Principle anchored to a specific case without explicit abstraction. The principle as stated — *"Source-natural-units are properties of the source ... SourceDescriptor is the natural home"* — is correct. But it stopped at "source-natural-units," a specific case (corpus-declaration data). It did not explicitly abstract to "facts about the source vs reader-properties referencing source vs strategies for handling source." Downstream inquiries had to make the abstraction themselves. The edge-cases inquiry over-generalized: it expanded "source-natural-units" to "anything source-related," conflating three distinct categories.

**Evidence from prior inquiry (chunking).** No section of the chunking finding explicitly distinguishes the three categories. The principle is stated for source-natural-units; the downstream applications (`chunking_strategy` → TC; `chunking_budget` → PC) are derived case-by-case in the finding, not from an explicit abstract rule.

**Evidence from human correction.** The AI's conversation snippet proposes the explicit distinction *"facts about the source vs strategies-for-handling-source"* — this is exactly what was implicit and not articulated in the chunking finding.

**Evidence from corrected direction.** The corrected routing is derivable from the explicit distinction (source-facts → SD; reader-properties → TC; strategies → TC).

**Confidence: MED (contributory, not primary).** Principle-articulation responsibility is contributory because the edge-cases inquiry had substrate sufficient to catch the misrouting without sharper principle articulation (the 8-axis comparative pattern was available). Sharpening the principle would have helped but is not load-bearing.

**Why not stronger.** The principle AS STATED is correct. Sharpening it requires evidence beyond one correction chain (per LOOP_DIAGNOSE guardrail). Treating principle-under-sharpening as a primary failure would over-claim.

**Maintenance candidate:** MC3 (principle sharpening; GATED) — see section 6.

**Evaluation gate.** Revival trigger: when a second correction chain involves a similar facts-vs-strategies conflation. At that point, promote principle sharpening from gated to actionable. Until then, do not modify the chunking finding's principle text.

### 5. Failure Attribution Summary

| Affected stage | Shortcoming type | Evidence strength | Confidence | Candidate action |
|---|---|---|---|---|
| edge-cases inquiry — sensemaking (Stage 3 → SV6) | Frame-exit Completeness applied on wrong axis (about chunking, not about Group α membership-types) | strong | HIGH | MC2 — Comparative-Pattern Test perspective |
| edge-cases inquiry — critique (Phase 2 Adversarial → P3 verdict) | Missing dimension + substance-axis prosecution didn't apply candidate's own claims against its own decision (smoking gun: docstring-vs-routing contradiction) | strong | HIGH | MC1 — Candidate-Self-Consistency sub-axis |
| chunking inquiry — finding section 3 principle articulation | Anchored to specific case (source-natural-units); abstraction to facts-vs-strategies implicit | medium | MED (contributory) | MC3 — principle sharpening (gated) |

Mixed attribution per LOOP_DIAGNOSE allowance. The two PRIMARY failures (HIGH confidence) are at the edge-cases inquiry's sensemaking and critique stages. The CONTRIBUTORY failure (MED confidence) is at the chunking finding's principle articulation. The framework's disciplines are structurally capable; this is a stage-application failure, not a meta-loop failure.

### 6. Maintenance Candidates

#### MC1 — Candidate-Self-Consistency sub-axis in td-critique (strong evidence)

**What to change.** Add a sub-axis to the Multi-axis prosecution depth check at Phase 2 of the td-critique spec (`/Users/ns/.claude/skills/td-critique/references/td-critique.md`). The sub-axis name: **Candidate-Self-Consistency**. When the candidate text contains internal claims (docstrings, justifications, named-pattern references, comparison-to-existing-pattern statements), construct at least one prosecution that applies those internal claims against the candidate's structural decisions (routing, schema home, axis assignment, parameter choice).

**File affected.** `/Users/ns/.claude/skills/td-critique/references/td-critique.md` — adds a ~5-10-line refinement note at Phase 2 Adversarial Evaluation, alongside the existing Substance-axis prosecution sub-axis.

**Risk class.** LOW. Additive refinement note; no existing behavior changes; well-aligned with the existing Substance-vs-Label success criteria refinement at Phase 0.

**Expected benefit.** Catches docstring-vs-routing-type internal contradictions. Would have caught the edge-cases P3 misrouting via the smoking-gun docstring "Refines A3."

**Evaluation gate.** Branch-test on the next bulk-edge-case inquiry's critique. Observe whether the new sub-axis is applied and whether it catches at least one internal-contradiction-shaped issue. If applied and caught: PROMOTE to canonical spec. If applied with no catches (clean candidate set): MONITOR for next opportunity. If not applied: investigate adoption failure.

**Should it become a branch experiment?** YES — branch-test on the next correction-chain-similar inquiry before promoting to the canonical spec.

#### MC2 — Comparative-Pattern Test perspective in sense-making (strong evidence)

**What to change.** Add a perspective to the Phase 2 Perspective Checking list in `/Users/ns/.claude/skills/sense-making/references/sensemaking.md`. The perspective name: **Comparative-Pattern Test**. When the inquiry commits a structural decision (schema home, axis assignment, routing of a new field into an existing scheme), explicitly compare each candidate against the existing pattern of analogous decisions in the target scheme. If the new field's shape doesn't match the existing pattern, the routing requires explicit defense — not just principle-derivation.

**File affected.** `/Users/ns/.claude/skills/sense-making/references/sensemaking.md` — adds a ~10-15-line perspective entry next to the existing Definitional / Internal Consistency and Definitional / Frame-exit Completeness perspectives.

**Risk class.** LOW. Additive perspective; explicit pattern-comparison is already present in spirit (the Specific-vs-pattern recognition cue at Phase 3) but not as a structural-decision-routing test.

**Expected benefit.** Catches schema-home-routing conflations like the edge-cases misrouting by forcing comparison against existing patterns (A1/A2/A3 reader-properties on TC; A5/A6 strategy-enum pattern). Would have caught all three misrouted fields.

**Evaluation gate.** Branch-test on the next bulk-edge-case inquiry's sensemaking. Observe whether the new perspective fires per structural decision and whether it surfaces any routing inconsistency. If fired and catches: PROMOTE. If fired with no catches (clean candidate set): MONITOR. If not fired: investigate adoption failure.

**Should it become a branch experiment?** YES.

#### MC3 — Principle sharpening in chunking finding (GATED)

**What to change.** Add an inline refinement to the chunking finding (`devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` section 3, near line 113) that explicitly states: *"The principle distinguishes three categories: (a) facts about the source (corpus declarations) → SourceDescriptor; (b) reader-properties (including reader-properties that reference source languages) → TranslationConfig; (c) user strategies for handling source properties → TranslationConfig. The chunking case applies (a)."*

**File affected.** `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` — inline addition; not a structural change.

**Risk class.** LOW (inline; reversible).

**Expected benefit.** Prevents downstream over-generalization from "source-natural-units" to "anything source-related."

**Evaluation gate.** GATED. Revival trigger: a second correction chain involving a similar facts-vs-strategies conflation. Per LOOP_DIAGNOSE guardrail ("Do not propose broad fundamentals rewrites from one weak correction chain"), defer canonical principle sharpening until a second instance shows the pattern.

**Should it become a branch experiment?** NO — defer to revival trigger; not branched now.

### 7. Corrected per-field routing (secondary constructive)

The edge-cases finding's per-field decision table had four entries routed to `SourceDescriptor`. The conversation correction re-classified three of them. The corrected routing:

| # | Field | Original (edge-cases finding) | Corrected | Reasoning |
|---|---|---|---|---|
| 2 | `source_language_fluency: dict[str, FluencyLevel]` | SourceDescriptor | **TranslationConfig** | Reader-property. Matches A1/A2/A3 pattern. The reader has fluency in source languages; the source text doesn't have fluency. The edge-cases P3 docstring "Refines A3" already names the correct home (A3 is on TC). |
| 3 | `source_edition: str \| None` | SourceDescriptor | **SourceDescriptor** ✓ | Genuine source fact (which printing this is). Stays. |
| 8 | `quranic_citation_policy: Literal[...]` | SourceDescriptor (inside `EmbeddedLanguagePolicy`) | **TranslationConfig** (or new apparatus axis) | Strategy enum for citation rendering. The FACT that Quranic citations are embedded → SD's `embedded_languages: list[str]`; the STRATEGY for how to render → TC. |
| 13 | `source_temporal_register: Literal["preserve-archaic", "modernize-fully", "hybrid-by-register-domain", "mark-archaisms-explicitly"]` | SourceDescriptor | **TranslationConfig** | Strategy enum (verbs of handling: preserve / modernize / hybrid / mark) — parallel to A5 source_fidelity. The FACT that the source has archaic register could be a SD declaration (e.g., `source_archaism_present: bool` or implicit in `source_edition`); the STRATEGY for handling → TC. (Optional SD-fact companion fields noted as future-frontier per critique caveat.) |

**Revised totals.** `TranslationConfig` delta: +3 new fields (`source_language_fluency`, `source_temporal_register`, `quranic_citation_policy`) — not +0 as the edge-cases finding claimed. `SourceDescriptor` delta: +1 (`source_edition`) plus an optional `embedded_languages: list[str]` carrying just the facts. The `EmbeddedLanguagePolicy` helper class is no longer needed: its `language_code` and `transliteration_policy` and `quranic_citation_policy` parts split (facts → SD's `embedded_languages`; strategies → TC fields).

This is the secondary constructive output addressing the user's WHY-axis `practical-application-now`. The primary output of this finding remains the diagnostic.

## Inherited Commitments Re-test

From the chunking finding (`devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`):

- **"Schema ownership matches data ownership" principle** — RE-TESTED, commitment confirmed but frame revised. Principle correct as stated; downstream over-generalization is what produced the failure; sharpening gated per MC3.
- **Three-operation chunking category** — INHERITED-WITHOUT-RE-TEST. Out of this inquiry's scope.
- **Split placement across SourceDescriptor + PipelineConfig + TranslationConfig** — RE-TESTED, confirmed. Split itself survives; the application to specific fields (edge-cases inquiry) is where the failure occurred, not the split.
- **Per-field routings #1, #6, #7** — RE-TESTED, confirmed. Correct applications.

From the edge-cases-into-config-schema finding (`devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md`):

- **The 14 edge-case candidates as bounded set** — RE-TESTED, confirmed.
- **TranslationConfig delta = 0** — RE-TESTED, **commitment found INVALID**. Corrected: TC delta = +3.
- **3 ALREADY-ROUTED (#1, #6, #7) inherit from chunking** — RE-TESTED, confirmed.
- **4 ADD-now to SourceDescriptor** — RE-TESTED, **commitment found INVALID for 3 of 4**. Only `source_edition` stays on SD.
- **7 DEFER with revival triggers** — RE-TESTED, confirmed. (Possible routing-when-revived adjustments per Open Questions.)
- **2 non-modifications (A3 stays; UseContext deferred)** — RE-TESTED, confirmed. Both non-modifications hold; #2's "add beside A3" reasoning was correct in intent but the "beside" was on the wrong schema.
- **Cross-axis conflict check: 0 hard conflicts, 2 docs notes** — RE-TESTED, frame revised. The check passed because the routing's internal contradiction wasn't tested. Conflicts-by-existing-axis-pattern is a new failure-category surfaced by this diagnostic.
- **EmbeddedLanguagePolicy carrying quranic_citation_policy** — RE-TESTED, **commitment found INVALID**. The conversation correction explicitly identified this as the conflation site.
- **Phase 2 SourceDescriptor implementation gates on chunking finding's SD MUST** — RE-TESTED, confirmed. Gate holds; what gets implemented is revised per section 7 above.
- **Pattern-level applicability to other corpora** — INHERITED-WITHOUT-RE-TEST. Out of this inquiry's scope; pattern-applicability claim depends on the corrected routing being tested across corpora.

## Next Actions

### MUST

- **What.** Apply the corrected routing to schema files: add three new TC fields (`source_language_fluency`, `source_temporal_register`, `quranic_citation_policy`) to `translation_config.py`; create `source_descriptor.py` with a SourceDescriptor stub containing `source_chunking_units` (from chunking finding), `source_edition`, and `embedded_languages: list[str]` (facts only).
  **Who.** Schema implementation step.
  **Gate.** Condition-bound — when the chunking finding's SourceDescriptor MUST item ships, this re-routing is applied alongside.
  **Why.** The misrouting must be undone before further work depends on it. The in-flight 4_mesele translation needs the corrected schema.

- **What.** Update the edge-cases-into-config-schema finding text (`devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md`) with a Correction Notice at the top citing this diagnostic. Revise the per-field decision table, the TC-delta-0 headline, and the affected sections (the four SD additions; the Inherited Commitments Re-test section if present; the EmbeddedLanguagePolicy code sketch).
  **Who.** Finding-text maintenance step.
  **Gate.** Observable — when this diagnostic finding is referenced as canonical.
  **Why.** The edge-cases finding is the closest thing to canonical truth on the schema; leaving the misrouting in place is high-risk for future readers. Preserve original content as diagnostic-trail.

- **What.** Update the chunking finding text (`devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`) with a small inline note at section 3 near line 113 acknowledging that the principle's scope is anchored to source-natural-units and that the abstraction to facts-vs-strategies-vs-reader-properties is gated per MC3.
  **Who.** Finding-text maintenance step.
  **Gate.** Observable — when this diagnostic finding is referenced.
  **Why.** Prevents future over-generalization. Small inline note; not a principle rewrite.

- **What.** Update the in-flight 4_mesele translation work to use the corrected schema once the schema files are updated.
  **Who.** Translation workflow step.
  **Gate.** Condition-bound — depends on schema-file MUST shipping.
  **Why.** The original misrouting would have applied to 4_mesele; the correction must propagate end-to-end.

### COULD

- **What.** Branch-test MC1 (Candidate-Self-Consistency sub-axis) on the next bulk-edge-case inquiry's critique.
  **Who.** Future inquiry's critique stage.
  **Gate.** Condition-bound — when next bulk-edge-case inquiry runs.
  **Why.** Validate MC1 catches at least one internal-contradiction-shaped issue before canonical promotion.
  **Depends-on.** MUST item "schema file updates" is independent (different scope); this COULD has no MUST dependency in this finding.

- **What.** Branch-test MC2 (Comparative-Pattern Test perspective) on the next bulk-edge-case inquiry's sensemaking.
  **Who.** Future inquiry's sensemaking stage.
  **Gate.** Condition-bound — when next bulk-edge-case inquiry runs.
  **Why.** Validate MC2 catches at least one pattern-mismatch issue before canonical promotion.

- **What.** Promote MC1 to the canonical td-critique spec after a successful branch test.
  **Who.** td-critique spec maintainer.
  **Gate.** Condition-bound — when MC1's branch test catches at least one issue.
  **Why.** Make the test part of the discipline's standard machinery.
  **Depends-on.** MUST item: none in this finding. COULD item "Branch-test MC1" is the gate. This COULD is GATED — do not promote until branch-test succeeds.

- **What.** Promote MC2 to the canonical sense-making spec after a successful branch test.
  **Who.** sense-making spec maintainer.
  **Gate.** Condition-bound — when MC2's branch test catches at least one issue.
  **Why.** Make the perspective part of the discipline's standard machinery.
  **Depends-on.** COULD item "Branch-test MC2." This COULD is GATED — do not promote until branch-test succeeds.

- **What.** Re-examine the 7 DEFER fields from the edge-cases finding under the corrected facts-vs-strategies distinction. Some revival-when-fired routings may shift from SD to TC (or vice versa).
  **Who.** Future review of edge-cases finding's DEFER list.
  **Gate.** Time-bound — at next maintenance pass of the edge-cases finding.
  **Why.** The misrouting may have propagated to revival-trigger framing.

- **What.** Audit other recent inquiries (outside the chunking + edge-cases chain) for facts-vs-strategies conflation patterns.
  **Who.** Light audit step.
  **Gate.** Time-bound — before MC3 promotion is considered.
  **Why.** If the pattern is widespread, MC3 promotion case strengthens; if isolated, MC3 stays gated.

### DEFERRED

- **What.** Sharpen the chunking finding's principle to explicitly distinguish facts about the source / reader-properties / strategies.
  **Gate.** Revival trigger — second correction chain involving the same facts-vs-strategies conflation.
  **Why (if revived).** Prevents future over-generalization at canonical-principle level.

- **What.** Codify LOOP_DIAGNOSE as a permanent skill (currently a protocol wrapper around /aMVLwr).
  **Gate.** Count-based — after 5-10 LOOP_DIAGNOSE runs show stable internal method (per protocol Step 5 guardrail). This is run #1.
  **Why (if revived).** Preserves the LOOP_DIAGNOSE pattern beyond protocol wrapper.

- **What.** Investigate whether SourceDescriptor should carry FACT-side companion fields to TC strategy fields (e.g., `source_archaism_present: bool` companion to `source_temporal_register`).
  **Gate.** Condition-bound — during SourceDescriptor implementation.
  **Why (if revived).** Sharpens the facts-vs-strategies model.

- **What.** Document the "perspective applied on wrong axis" failure pattern as a sense-making meta-failure example.
  **Gate.** Time-bound — bundle with MC2 promotion to sense-making spec.
  **Why (if revived).** The pattern is structurally distinct from Perspective Blindness ("perspective not applied"); this is "perspective applied wrong."

- **What.** Document the "substance-axis didn't apply candidate's own claims" failure pattern as a td-critique meta-failure example.
  **Gate.** Time-bound — bundle with MC1 promotion to td-critique spec.
  **Why (if revived).** Inverse-companion of MC1 (the MC catches it going forward; the failure-mode entry helps recognize it retrospectively).

## Reasoning

The structurally non-obvious decisions in this diagnostic finding had alternatives that were considered and rejected.

**Why mixed attribution, not single-stage attribution.** A single-stage attribution would have collapsed PRIMARY responsibility into either sensemaking SV6 or critique or chunking's principle. None of those single-stage attributions survives prosecution: chunking's own routings are correct (so it's not solely responsible); critique alone can't catch frame-level errors its dimensions don't probe (so it's load-bearing but not solely responsible); sensemaking alone might have caught it with Frame-exit Completeness applied to the right axis (so it's load-bearing but not solely responsible). The mixed attribution is structurally honest, per LOOP_DIAGNOSE's explicit allowance for mixed attribution.

**Why the conversation correction is comparative evidence, not ground truth.** Per LOOP_DIAGNOSE Step 5 guardrail. The conversation correction is the AI's own response to user pushback; treating it as ground truth would invert the loop's accountability (the AI grading its own homework). Treating it as comparative evidence forces the diagnostic to independently re-test the corrected direction via Frame-exit Completeness applied to a different axis (Group α membership-types) than the original inquiry used. That re-test independently confirmed the correction — without relying on the snippet's authority.

**Why MC1 and MC2 are not redundant.** MC1 catches internal contradictions (candidate's own claims vs candidate's own decision). MC2 catches external-pattern mismatches (decision vs existing pattern in target schema). The edge-cases misrouting failed both tests — a docstring-vs-routing contradiction (MC1 territory) and a pattern-mismatch against A1/A2/A3 (MC2 territory). A future misrouting might fail only one. The two MCs cover different test mechanisms; branch-testing both is appropriate.

**Why MC3 is gated, not promoted now.** Per LOOP_DIAGNOSE guardrail against broad rewrites from one correction chain. The chunking finding's principle as stated is correct; sharpening it is value-add but is not load-bearing for fixing THIS misrouting (the edge-cases inquiry had substrate to catch the error). Promoting MC3 from one chain would over-claim. Gating with a revival trigger (second instance of the pattern) preserves the path without committing now.

**Why ACTIONABLE not PARTIAL or INCONCLUSIVE.** ACTIONABLE requires at least one MC with concrete shape + evaluation gate. MC1 and MC2 both qualify: specific file paths, named features ("Candidate-Self-Consistency sub-axis"; "Comparative-Pattern Test perspective"), low risk class, observable evaluation gates (catches at least one issue on branch-test).

**Self-Reference Blindness — partial mitigation acknowledged.** This inquiry is the AI running disciplines on its own prior outputs. LOOP_DIAGNOSE's comparative-evidence framing (treating the conversation correction as evidence, not ground truth) plus the user-pushback trigger plus the independent Frame-exit Completeness re-test on a different axis together provide partial mitigation. The residual blind spot: the AI's reasoning may protect aspects the user didn't push back on. This is structural to the situation; the user's pushback was specifically about `source_language_fluency`; the diagnostic generalizes to all four SD additions and to the broader chain. Aspects neither pushed back on nor independently verified may carry undetected error.

**The substrate-reachability framing.** The conversation correction used only substrate available to the original inquiries (the A1/A2/A3 pattern in `config_base_source.md`; the P3 docstring within the edge-cases inquiry itself). No new external information was needed. This means the failure is "missing test against available information," not "missing information." All maintenance candidates target test-mechanisms (sub-axes; perspectives), not new information sources. This framing also explains why the MCs are LOW-risk additions: they don't require new substrate, only new tests on existing substrate.

## Open Questions

### Monitoring

- After MC1 + MC2 branch-tests run, observe whether they fire and whether they catch any issues. If both fire and catch: high evidence for promotion. If one fires and one doesn't: investigate adoption.
- After the corrected schema lands in code, observe whether the in-flight 4_mesele translation produces results consistent with the new routing (e.g., does `source_language_fluency` produce sensible reader-level-driven behavior at translation time?).
- After re-examining the 7 DEFER fields under the corrected distinction, observe whether any revival-when-fired routings need to be revised.

### Blocked

- Phase 2 schema implementation depends on the chunking finding's SourceDescriptor MUST shipping. This LOOP_DIAGNOSE finding's corrective propagation (Next Actions MUST items) is blocked on that same gate.
- MC3 promotion is blocked on a second correction-chain instance.
- Codifying LOOP_DIAGNOSE as a permanent skill is blocked on 5-10 run count.

### Research Frontiers

- Whether the facts-vs-strategies conflation pattern is general across the loop's behavior or specific to schema-routing decisions. Audit of other recent inquiries (per COULD item) will inform.
- Whether SourceDescriptor should carry FACT-side companions to TC strategy fields (e.g., `source_archaism_present` alongside `source_temporal_register`). Mentioned in P11 critique caveat; future-frontier.
- Whether the "perspective applied on wrong axis" failure pattern (Frame-exit Completeness fired on chunking, not on Group α membership) is a distinct failure mode worth promoting to the sense-making failure-mode catalog. Bundle with MC2 promotion.

### Refinement Triggers

- If MC1 or MC2 branch-tests catch issues that this diagnostic didn't anticipate, revise this finding's evidence-strength claims.
- If a second correction chain emerges with a facts-vs-strategies conflation pattern, promote MC3 from gated to actionable.
- If the corrected schema produces practical issues at translation time (e.g., redundancy between SD facts and TC strategies), revisit P11's caveat about SD-fact companion fields.
- If the audit of other recent inquiries surfaces multiple instances of facts-vs-strategies conflation, escalate MC3 promotion case.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
in 
devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md

u said later 

You're right. I got that wrong.

  The principle is "schema ownership matches data ownership." Look at what TranslationConfig already holds — reader_level,
  domain_expertise, source_culture. Those describe the reader (or the reader's relationship to the source). They're on TranslationConfig
  because per-translation-job the user picks "which reader is this for?"
  
  source_language_fluency fits that pattern exactly. It describes the reader (their fluency in Arabic/Persian/etc.), not the source text.
  The source text doesn't have fluency; the reader does. → belongs on TranslationConfig.

  Re-examining the other three:

  - source_edition — genuinely a property of the source text itself (which printing this is). → SourceDescriptor. ✓
  - source_temporal_register — the field as I wrote it is the user's STRATEGY enum (preserve-archaic / modernize-fully / 
  hybrid-by-register-domain / mark-archaisms-explicitly). That's parallel to A5 source_fidelity (foreignize-vs-domesticate strategy). →
  belongs on TranslationConfig.
  - quranic_citation_policy — same shape: a strategy enum for how to render Quranic citations. → belongs on TranslationConfig (or on an
  A8-style apparatus axis). I bundled it inside EmbeddedLanguagePolicy, but that put a strategy choice inside a source-property 
  declaration, which is exactly the conflation you're pointing at.

  What I conflated: "this source HAS embedded Arabic" (source property → SD) with "how the translator should RENDER embedded Arabic"
  (strategy → TC).

  The clean split:

  SourceDescriptor (facts about the corpus):
  - source_chunking_units (existing from chunking finding)
  - source_edition
  - embedded_languages: list[str] — just the FACT that Arabic/Persian are embedded, with atom-protection flags



use devdocs/loop_diagnose.md
```

</details>

---

## Diagnostic Verdict

**Overall:** ACTIONABLE

- **Best-supported diagnosis:** Hypothesis 2 (edge-cases critique missed principle-application correctness; substance-axis prosecution didn't apply candidate's own claims against its own decision). The smoking gun — the P3 docstring "Refines A3" vs the SD routing — is concrete. The missing-dimension claim is supported by direct enumeration of the eight dimensions actually used. PRIMARY at HIGH confidence, jointly with Hypothesis 1.

- **Strongest maintenance candidate:** MC1 (Candidate-Self-Consistency sub-axis in td-critique). Concrete; small refinement note; testable evaluation gate; would have caught the smoking-gun docstring contradiction.

- **Main uncertainty:** the relative weight between Hypothesis 1 (sensemaking SV6) and Hypothesis 2 (critique). Both fire at HIGH confidence; attribution is jointly PRIMARY. Further correction chains would help distinguish.

- **Recommended next step:** branch-test MC1 and MC2 on the next bulk-edge-case inquiry. If both fire and catch at least one issue each, promote to canonical specs. MC3 (principle sharpening) stays gated pending a second correction chain.
