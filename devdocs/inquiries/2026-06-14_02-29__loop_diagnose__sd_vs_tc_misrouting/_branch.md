# Branch: Loop Diagnose — SD vs TC Misrouting

## Source Input

The user's raw request, preserved verbatim. Also lives in `articulate_simple.md`'s `## User Input` section.

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

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-14_02-29__loop_diagnose__sd_vs_tc_misrouting/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** I1
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

**Item I1** — Use LOOP_DIAGNOSE to diagnose what went wrong in the loop chain that produced the SourceDescriptor-vs-TranslationConfig misrouting visible in the conversation correction snippet. Given the user pointed at the chunking finding as the chain's starting reference but the actual misrouting was committed in the downstream edge-cases-into-config-schema inquiry, the diagnostic scope is the chain — chunking established the principle ("schema ownership matches data ownership") → edge-cases applied it (incorrectly, conflating *facts-about-the-source* with *strategies-for-handling-the-source*) → conversation correction revealed the misapplication.

**MQ1 verdict-axis identified-ambiguities (what kinds of asks the statement carries):**
- `loop_diagnose-following-protocol` — formal LOOP_DIAGNOSE inquiry per the spec; failure hypotheses + maintenance candidates + diagnostic verdict.
- `single-inquiry-diagnosis` — diagnose ONLY the chunking finding (user pointed at it).
- `chain-diagnosis` — diagnose the CHAIN (chunking established principle → edge-cases applied it → conversation corrected).
- `principle-articulation-diagnosis` — investigate whether "schema ownership matches data ownership" was sharp enough to prevent downstream misapplication.
- `critique-stage-diagnosis` — investigate why the edge-cases inquiry's td-critique phase didn't catch the misrouting.
- `meta-loop-diagnosis` — investigate whether the loop framework is structurally capable of catching the facts-about-X vs strategies-about-X conflation.

**MQ3 intent-axis identified-ambiguities (what action-endpoints are plausible):**
- `identify-the-stage-where-misrouting-was-locked-in`
- `identify-principle-ambiguity-source`
- `produce-maintenance-candidates`
- `learn-from-pattern` (the facts-vs-strategies conflation)
- `validate-the-conversation-correction-is-structurally-grounded`
- `produce-evaluation-gates`

**MQA — surface (irreducible overlap content).** The user pointed at the chunking finding as the chain's reference, but the conversation snippet corrects fields proposed in a DOWNSTREAM inquiry (`devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/`). The chunking finding's own routings (#1 / #6 / #7) are correct applications of its principle; the misrouting was committed in the edge-cases inquiry's per-field decision table. The diagnostic scope is therefore the CHAIN, not a single inquiry. The downstream pipeline must span the chain and distinguish *principle ambiguity* (chunking's potential issue) from *application failure* (edge-cases' inquiry issue) from *critique blind-spot* (edge-cases' critique missed it). All three possibilities must be examined.

## Goal

**Deconstruct tuple:**
- **deliverable:** /aMVLwr finding compiled from 7 discipline artifacts, structured per LOOP_DIAGNOSE's required output sections — Correction Chain Summary + Failure Hypotheses (each with affected-stage / shortcoming-type / per-source evidence / confidence / why-not-stronger / maintenance-candidate / evaluation-gate) + Failure Attribution Summary table + Maintenance Candidates + Diagnostic Verdict.
- **kinds:** `[diagnose-stage (which discipline / loop-step locked in the misrouting) + diagnose-principle (was the principle articulation sufficient?) + propose-maintenance (specific spec changes with evaluation gates) + verdict (ACTIONABLE / PARTIAL / INCONCLUSIVE)]`
- **bounds:** scoped to the chunking finding + edge-cases-into-config-schema finding chain + the conversation correction snippet + the existing 8-axis TC pattern as comparative evidence. NOT a broad loop-framework rewrite. NOT a redefinition of the schema-ownership principle from scratch.

**MultiDepth WHY-axis identified-purpose-motivation-ambiguities:**
- `learn-from-mistake` — understand the failure so it doesn't recur.
- `improve-the-loop-framework` — produce specific maintenance candidates.
- `validate-correction-is-structurally-grounded` — confirm the conversation correction holds up to formal scrutiny.
- `understand-conflation-pattern` — diagnose facts-about-X vs strategies-about-X as a pattern the loop may exhibit elsewhere.
- `practical-application-now` — secondary motivation: the corrected routing should land in proper findings, even though LOOP_DIAGNOSE is meant to be diagnostic.
- `framework-completeness-check` — is the loop structurally CAPABLE of catching this kind of error?
- `prevent-recurrence-in-future-inquiries` — particularly future bulk-edge-case applications of the same principle.

**MQ2 context-need identified-ambiguities:**
- **verdict sub-axis:** `[the chunking finding (where SourceDescriptor + the principle were introduced) / the edge-cases-into-config-schema finding (where 3 of 4 SD additions were misrouted) / the archived discipline outputs from BOTH inquiries (per LOOP_DIAGNOSE step 2: do not diagnose from finding.md alone) / the original conversation correction (already in context) / the existing 8-axis TC schema as comparative evidence — A1/A2/A3 demonstrate the correct reader-property routing pattern]`
- **kinds sub-axis:** `[diagnose-by-protocol (LOOP_DIAGNOSE-shaped output) / diagnose-by-stage (which discipline / loop-step failed?) / diagnose-by-principle (was the principle wrong, ambiguous, or correctly stated but mis-applied?) / produce-maintenance-candidates (specific changes with evaluation gates)]`
- **stance sub-axis:** `[treat conversation correction as comparative evidence vs ground truth — LOOP_DIAGNOSE guardrail says comparative / blame attribution mixed vs locked to specific discipline — LOOP_DIAGNOSE guardrail allows mixed / propose source edits vs monitoring-questions — LOOP_DIAGNOSE guardrail prefers monitoring unless evidence is strong]`

**MQ4 boundary-axis identified-ambiguities:** explicit-empty. (Substrate-level guardrails from LOOP_DIAGNOSE itself apply: do not treat corrected_path as ground truth; do not collapse all failures to discipline failures; do not propose broad rewrites from one correction chain.)

## Considered Articulations

**Item I1** — variant-set from Rephrase:

1. **Single-inquiry-stage diagnosis (chunking finding only).** Read only the chunking finding's archived discipline outputs; identify where its principle articulation was ambiguous enough to enable downstream misapplication. Conversation correction is `corrected_path` proxy.

2. **Chain diagnosis (chunking + edge-cases, both archived outputs).** Read BOTH inquiries' archived discipline outputs. Distinguish principle ambiguity (chunking) from application failure (edge-cases) from critique blind-spot (edge-cases' critique). Conversation correction is `corrected_path` proxy.

3. **Critique-stage-focused diagnosis.** Focus on why edge-cases' td-critique didn't catch the misrouting. Missing dimension? Missing prosecution sub-axis? Frame-premise not tested? Output: critique-stage failure hypotheses + td-critique spec changes.

4. **Principle-articulation diagnosis.** Focus on whether "schema ownership matches data ownership" is sufficient to disambiguate facts-about-X from strategies-about-X. Output: principle failure hypothesis + sharpened-principle maintenance candidate.

5. **Meta-loop diagnosis.** Investigate whether the loop framework is structurally capable of catching facts-vs-strategies conflation; per LOOP_DIAGNOSE guardrail, entertain failure at loop-framing / orchestration / principle-library level. Output: meta-loop failure hypothesis + structural maintenance candidate.

6. **Implementation-corrective diagnosis (impure form).** Diagnose AND produce corrected routing table for the affected fields (`source_language_fluency` → TC; `source_temporal_register` → TC; `quranic_citation_policy` → TC; `source_edition` → SD). Blends LOOP_DIAGNOSE with constructive output; pushes against LOOP_DIAGNOSE's diagnose-not-fix guardrail.

## Scope Check

**Question covers goal:** YES — with the CHAIN-SCOPE-OF-DIAGNOSIS openness preserved by MQA's surface (the chain is the diagnostic scope; downstream pipeline must distinguish principle ambiguity from application failure from critique blind-spot).

**IN-scope (per Deconstruct bounds):** chunking finding + edge-cases-into-config-schema finding + their archived discipline outputs; the conversation correction snippet; the existing 8-axis TC pattern as comparative evidence; LOOP_DIAGNOSE-protocol-shaped diagnostic output.

**OUT-of-scope:** broad loop-framework rewrites (LOOP_DIAGNOSE guardrail); principle redefinition from scratch (the principle "schema ownership matches data ownership" itself is comparative evidence, not the subject of rewrite — though sharpening it IS in scope); spec changes that aren't tied to evidence from this correction chain.

**Specific-vs-pattern check:** The question is about THIS SPECIFIC misrouting (3 fields misrouted in edge-cases inquiry). Should the diagnosis address only these specific cases, or generalize to the deeper pattern (facts-about-X vs strategies-about-X conflation)? Both readings are valid; the MultiDepth WHY-axis (`understand-conflation-pattern`) signals the user wants pattern-level lessons, not just specific-case correction. The diagnosis addresses the BROADER PATTERN with these 3 fields as the motivating examples — consistent with the sense-making "Specific-vs-pattern recognition cue" refinement note (when motivating examples drive a key insight, explicitly test whether the concept fits a wider pattern).

## Correction Chain (per LOOP_DIAGNOSE protocol Step 1)

- **Prior path** (normalized — weak / wrong / incomplete result): `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/` is the inquiry where the misrouting was concretely committed (in the per-field decision table; in the SourceDescriptor pydantic code; in the cross-axis conflict check that did not flag the conflation). The user pointed at `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/` as the chain's starting reference; this earlier inquiry established the principle and the schemas but did NOT itself commit the misrouting (its own routings #1/#6/#7 are correct). Both inquiries are in the prior chain; the misrouting is concretely in the downstream one.

- **Corrected path** (later improved direction; treated as comparative evidence, not ground truth): the conversation correction snippet itself (preserved verbatim above and in `articulate_simple.md`'s User Input). No separate "corrected inquiry folder" exists; the corrected direction is the inline conversation. The diagnostic pipeline treats this as the comparative-evidence equivalent of a `corrected_path`.

- **Human correction:** the user's pushback `"this doesnt make sense no? why SourceDescriptor has such field? it feels like translationconfig field"` triggered the AI's reconsideration. The AI's resulting conversation correction (the snippet shown) is the corrected direction. The PRIMARY correction signal is the user's pushback; the AI's snippet is the response.

- **Optional context:** existing 8-axis `TranslationConfig` (`config_base_source.md` + `translation_config.py`) — A1 reader_level, A2 domain_expertise, A3 source_culture are reader-properties on TC, establishing the correct routing pattern that `source_language_fluency` should have followed.

- **Diagnostic goal:** evidence-backed failure hypotheses + maintenance candidates with evaluation gates. Per LOOP_DIAGNOSE protocol: do not treat the corrected direction as ground truth; allow mixed attribution; prefer monitoring questions over broad spec rewrites; produce only candidates the evidence justifies.

## Required Reads (per LOOP_DIAGNOSE protocol Step 2)

For both inquiry folders, read `_branch.md`, `_state.md`, `finding.md`, root discipline outputs if present, and `docarchive/` discipline outputs if present.

- **Prior chain inquiry 1:** `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/` — `_branch.md`, `_state.md`, `finding.md`, `_route.md`, all 7 files in `docarchive/` (articulate_simple.md, surfacing.md, sensemaking.md, decomposition.md, innovation.md, critique.md, routelister.md).
- **Prior chain inquiry 2:** `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/` — same set of files.
- **Comparative evidence:** `config_base_source.md` (A1/A2/A3 reader-properties on TC); `translation_config.py` (current schema).
- **Correction signal:** the conversation snippet provided in raw input (already preserved in `articulate_simple.md` and in this file's Source Input section).

Per LOOP_DIAGNOSE: "Do not diagnose from `finding.md` alone when discipline outputs are available." The archived discipline outputs of the edge-cases inquiry specifically — its sensemaking.md, innovation.md, critique.md — are where the misrouting was first locked in and not caught.

## Diagnostic Constraints (per LOOP_DIAGNOSE protocol Step 3)

- Treat the human correction (user's pushback + AI's snippet) as comparative evidence, not ground truth.
- Treat the conversation correction as comparative evidence, not ground truth — even though the correction came from the AI itself, the structural argument it makes must be independently tested.
- Prefer evidence-backed hypotheses over exact root-cause claims.
- Allow mixed or unknown attribution when evidence does not isolate one discipline.
- Produce maintenance candidates only when the diagnosis gives enough evidence to justify them.
- Per protocol Step 5 guardrails: do not propose broad fundamentals rewrites from this one correction chain; do not promote LOOP_DIAGNOSE into a standalone skill; do not collapse all failures into discipline failures (loop framing / orchestration / context elicitation / principle library may be the real failure surface).

## Synthesis Trigger

This inquiry consumes 2 prior inquiry outputs (the chunking finding chain + the edge-cases-into-config-schema chain) as the diagnostic substrate. Per the Synthesis Trigger requirement, the resulting finding will include an `## Inherited Commitments Re-test` section that names each commitment carried forward and either re-tests it with cited evidence or explicitly flags it as inherited-without-re-test with a reason.

- `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` — commits to: three-operation chunking category; split-placement across `SourceDescriptor` + `PipelineConfig` + `TranslationConfig`; the "schema ownership matches data ownership" decision principle; #1 → ChunkingUnit.is_atomic; #6 → ChunkingUnit.attached_to; #7 → orthogonal sister-concept. These commitments are inherited; the principle commitment is the central one this diagnostic must re-test.
- `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md` — commits to: 14-row per-field decision table with TC delta = 0; 4 ADD-now-to-SourceDescriptor (source_language_fluency / source_edition / source_temporal_register / quranic_citation_policy-as-EmbeddedLanguagePolicy-property); 7 DEFER; 2 non-modifications; phased migration. Of these, 3 of the 4 SourceDescriptor additions are exactly what the conversation correction refutes — these commitments must be re-tested and likely INVALIDATED or REVISED in this finding.

## Relationships

- DIAGNOSES: `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/` (where the misrouting was concretely committed)
- DIAGNOSES: `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/` (where the principle that enabled the misapplication was established; correctness of the principle articulation is itself in scope)
- COMPARES WITH: the conversation correction (inline; treated as comparative evidence per LOOP_DIAGNOSE)
- RELATED: `/Users/ns/Desktop/projects/comprehenslate/config_base_source.md` (comparative evidence — A1/A2/A3 reader-property routing on TC)
- RELATED: `/Users/ns/Desktop/projects/comprehenslate/translation_config.py` (current schema baseline)
