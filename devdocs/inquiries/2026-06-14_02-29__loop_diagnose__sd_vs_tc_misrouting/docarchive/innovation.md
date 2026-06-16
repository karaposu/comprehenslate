# Innovation — Loop Diagnose: SD vs TC Misrouting

## User Input

Input: `_branch.md` + upstream `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md`. Production-task mode; 11 LOOP_DIAGNOSE-shaped pieces. Per piece: principal candidate + intervention-shape-axis Inversion-candidate.

---

## Methodology Mode

Standard default. Alternative (Contrarian-rethink) rejected: sensemaking SV6 + Frame-exit Completeness insight already absorbed structural shifts; per-piece Inversion-candidates provide contrarian channel. All 11 pieces meta-decision; all property-(v) fires (intervention-shape commitment for diagnostic output).

---

## P1 — Correction Chain Summary

**Principal.**

- **Prior path 1:** `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/` — where the "schema ownership matches data ownership" principle was articulated (line 113 of `finding.md` verbatim: *"Source-natural-units are properties of the source ... SourceDescriptor is the natural home"*). The chunking finding's own per-field routings (#1 → `ChunkingUnit.is_atomic`; #6 → `ChunkingUnit.attached_to`; #7 → orthogonal sister-concept) are CORRECT applications of its own principle. No misrouting in chunking finding itself.

- **Prior path 2:** `devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/` — where the misrouting was concretely committed. The per-field decision table routed 4 fields to `SourceDescriptor`: `source_language_fluency`, `source_edition`, `source_temporal_register`, `quranic_citation_policy`. Of these, **3 of 4 are misrouted** (`source_edition` is correct).

- **Corrected direction** (comparative evidence per LOOP_DIAGNOSE; NOT ground truth): the conversation correction snippet (preserved verbatim in `_branch.md` Source Input). Used a comparative-pattern argument: A1 `reader_level` / A2 `domain_expertise` / A3 `source_culture` are reader-properties on `TranslationConfig`; `source_language_fluency` fits that pattern exactly. The correction re-routed: `source_language_fluency` → TC; `source_temporal_register` → TC; `quranic_citation_policy` → TC; `source_edition` → SD (unchanged).

- **Human correction signal:** the user's pushback *"this doesnt make sense no? why SourceDescriptor has such field? it feels like translationconfig field"* triggered AI reconsideration. The AI's snippet is the response.

- **What changed from prior result to corrected direction:** 3 of the 4 `SourceDescriptor` additions in the edge-cases finding were re-classified as `TranslationConfig` additions, on the basis that they describe reader-properties or user-strategies, not source-facts.

**Inversion-candidate.** Alternative shape: omit the Correction Chain Summary section (LOOP_DIAGNOSE protocol step skipped). 5-test: novel NO; scrutiny WEAK (protocol-required section). **Verdict: KILL.**

---

## P2 — Failure Hypothesis 1: edge-cases sensemaking SV6 locked-in misrouting

**Principal.**

**Affected stage:** Sensemaking (edge-cases inquiry's stage 3 Ambiguity Collapse → SV6 stabilized model).

**Shortcoming type:** Frame-exit Completeness perspective applied on wrong axis. Sensemaking fired the Frame-exit Completeness perspective (on "chunk has 6 project-wide referents") but did NOT apply it to "Group α SourceDescriptor membership has 3 distinct referent types" (source-facts vs reader-properties-referencing-source vs strategies-for-handling-source). The perspective's machinery existed; the right axis to test wasn't selected.

**Evidence from prior inquiry (edge-cases):** Sensemaking SV6 stabilized "4 ADD-now to SourceDescriptor: #2 + #3 + #8 + #13" without testing each member against the source-facts/reader-properties/strategies distinction. Ambiguity 4's resolution committed `source_language_fluency` → SD with reasoning "A3 keeps its existing meaning; the new field captures language-fluency" — a reasoning that CONTRADICTS itself (if the field refines A3, and A3 is on TC, then the field should be on TC).

**Evidence from human correction:** User's intuition immediately matched `source_language_fluency` to the A1/A2/A3 pattern (reader-properties on TC). The sensemaking did not perform this match.

**Evidence from corrected direction:** AI's snippet uses precisely the comparative-pattern argument that Frame-exit Completeness perspective would have produced if applied to Group α membership.

**Confidence:** HIGH — multiple artifacts converge (the SV6 stabilization is the locus; the docstring contradiction is internal; the comparative pattern was reachable).

**Why not stronger:** Frame-exit Completeness application is a judgment call; the perspective DID fire (on chunking axis) so it's not "perspective blindness" — it's "perspective application to wrong axis." Calling this a stage failure is partly judgment.

**Maintenance candidate:** MC2 (comparative-pattern test as explicit sensemaking perspective) — see P7.

**Evaluation gate:** on the next bulk-edge-case inquiry, observe whether Frame-exit Completeness is applied to each candidate's distinct referent-type; observe whether the comparative-pattern test fires per routing decision.

**Inversion-candidate.** Alternative shape: attribute primary failure to a different stage (e.g., decomposition, where P3's question "What does each SourceDescriptor addition look like?" presupposed SD as home). 5-test: novel YES; scrutiny MED — decomposition's piece-question is an artifact of sensemaking's SV6, not an independent locus. The decomposition encoded the misrouting but didn't introduce it. **Verdict: KILL (attribute to sensemaking primary; decomposition derives).**

---

## P3 — Failure Hypothesis 2: edge-cases critique missed principle-application correctness

**Principal.**

**Affected stage:** Critique (edge-cases inquiry's Phase 2 Adversarial Evaluation → P3 verdict).

**Shortcoming type:** Missing dimension + substance-axis prosecution miss. The critique used 8 dimensions (Correctness / Coherence / Feasibility / Robustness / Completeness / Anti-bloat-fit / Synthesis-rigor / External-anchor compliance) but none explicitly tests "does this routing decision apply the inherited principle correctly?" Substance-axis prosecution did fire on P3 but tested code-quality and composability, NOT the candidate's own internal claims against its own decision.

**Evidence from prior inquiry (edge-cases):** Critique's P3 verdict was SURVIVE clean with no caveat (`critique.md` "P3 (SourceDescriptor code) ... Verdict: SURVIVE. Clean — no refinements needed beyond what's documented inline"). The **smoking gun**: P3's docstring for `source_language_fluency` explicitly states *"Refines A3 source_culture by adding the fluency dimension WITHOUT modifying A3"*. A3 lives on `TranslationConfig`. A field that "refines A3" living on `SourceDescriptor` is internally inconsistent. The substance-axis prosecution did not apply this internal claim against the routing.

**Evidence from human correction:** The correction's argument (compare to A1/A2/A3 routing pattern) is precisely what the missing critique dimension would have produced.

**Evidence from corrected direction:** AI's snippet exposed the conflation by reading the candidate's own behavior (the docstring) — the same internal-evidence reading that substance-axis prosecution should have performed.

**Confidence:** HIGH — the docstring-vs-routing internal contradiction is a smoking gun; the missing-dimension claim is supported by enumeration of the 8 dimensions actually used.

**Why not stronger:** Substance-vs-Label success criteria refinement note at Phase 0 says substance-level criterion is required when dimension tests load-bearing claims. The critique's Correctness dimension HAD a substance-level criterion stated ("candidate text instantiates the SV6 model"). The criterion fired but produced a PASS — because the SV6 model itself contained the misrouting. The dimension performed correctly given its frame; the frame inherited the SV6 error.

**Maintenance candidate:** MC1 (substance-axis sub-axis sharpening) — see P6.

**Evaluation gate:** on the next bulk-edge-case inquiry's critique, observe whether the substance-axis sub-axis applies candidate's own internal claims (docstrings, justifications, named-pattern references) as tests against the candidate's structural decisions.

**Inversion-candidate.** Alternative shape: attribute primary failure to the Frame-premise test inside critique (which DID fire on 3 SV6 premises; all SURVIVE). 5-test: novel YES; scrutiny WEAK — the Frame-premise test tested abstract premises (split-placement extends; anti-bloat trumps; DEFERs don't break), not per-field application of the principle. Adding a per-field principle-application test would require the missing dimension, which is exactly MC1. **Verdict: KILL (Frame-premise test fired but tested the wrong premises; the missing dimension is the load-bearing finding).**

---

## P4 — Failure Hypothesis 3: chunking principle anchored too specifically (CONTRIBUTORY)

**Principal.**

**Affected stage:** Chunking finding's principle articulation (sensemaking SV6 + Finding section 3).

**Shortcoming type:** Principle anchored to specific case without explicit abstraction. The chunking finding stated *"Source-natural-units are properties of the source"* (line 113). The principle is correct as stated. But it stopped at "source-natural-units" — a specific case (corpus-declaration data) — and did not abstract to "facts about the source vs reader-properties-referencing-source vs strategies-for-handling-source." Downstream had to make the abstraction; it conflated.

**Evidence from prior inquiry (chunking):** No section of the chunking finding explicitly distinguishes the three categories. The principle is stated for source-natural-units; the downstream applications (`chunking_strategy` → TC; `chunking_budget` → PC) are derived case-by-case, not from an explicit abstract rule.

**Evidence from human correction:** AI's snippet PROPOSES the explicit distinction *"facts about the source vs strategies-for-handling-source"* — this is what was implicit and not articulated.

**Evidence from corrected direction:** the corrected routing is derivable from the explicit distinction (source-facts → SD; reader-properties → TC; strategies → TC).

**Confidence:** MED — principle-articulation responsibility is contributory, not sole. The edge-cases inquiry had enough substrate (the 8-axis comparative pattern) to catch the misrouting without sharper principle articulation. Sharper principle would have helped but is not a load-bearing fix.

**Why not stronger:** The principle as STATED is correct; sharpening it requires evidence beyond one correction chain (per LOOP_DIAGNOSE guardrail). Treating principle-under-sharpening as a primary failure would over-claim.

**Maintenance candidate:** MC3 (principle sharpening; gated) — see P8.

**Evaluation gate:** revival trigger — when a second correction chain involves a similar facts-vs-strategies conflation, promote principle sharpening from gated to actionable.

**Inversion-candidate.** Alternative shape: ELEVATE to primary hypothesis (chunking finding is responsible). 5-test: novel NO; scrutiny WEAK — substrate-reachability argument prosecutes this (the edge-cases inquiry had everything it needed). **Verdict: KILL (chunking principle is contributory not primary).**

---

## P5 — Failure Attribution Summary

**Principal.**

| Affected stage | Shortcoming type | Evidence strength | Confidence | Candidate action |
|---|---|---:|---:|---|
| edge-cases inquiry — sensemaking (Stage 3 → SV6) | Frame-exit Completeness applied on wrong axis (about chunking, not about Group α membership-types) | strong | HIGH | MC2 — comparative-pattern perspective |
| edge-cases inquiry — critique (Phase 2 Adversarial → P3 verdict) | Missing dimension + substance-axis prosecution didn't apply candidate's own claims against its own decision (smoking gun: docstring-vs-routing contradiction) | strong | HIGH | MC1 — substance-axis sub-axis sharpening |
| chunking inquiry — finding section 3 principle articulation | Anchored to specific case (source-natural-units); abstraction to facts-vs-strategies implicit | medium | MED (contributory) | MC3 — principle sharpening (gated) |

**Inversion-candidate.** Alternative shape: produce single-attribution table (force one primary stage). 5-test: novel NO; scrutiny WEAK (LOOP_DIAGNOSE explicitly allows mixed attribution). **Verdict: KILL.**

---

## P6 — Maintenance Candidate 1: substance-axis sub-axis sharpening in td-critique

**Principal.**

- **What:** add a sub-axis to the Multi-axis prosecution depth check at Phase 2 of the td-critique spec (`/Users/ns/.claude/skills/td-critique/references/td-critique.md`). Sub-axis name: **Candidate-Self-Consistency sub-axis**. When the candidate text contains internal claims (docstrings, justifications, named-pattern references, comparison-to-existing-pattern statements), construct at least one prosecution that applies those internal claims against the candidate's structural decisions (routing, schema home, axis assignment).
- **File affected:** `/Users/ns/.claude/skills/td-critique/references/td-critique.md` — adds a ~5-10-line refinement note at Phase 2 Adversarial Evaluation, next to the existing Substance-axis prosecution sub-axis.
- **Risk class:** LOW. Additive refinement note; no existing behavior changes; well-aligned with the existing Substance-vs-Label success criteria refinement at Phase 0.
- **Expected benefit:** catches docstring-vs-routing-type internal contradictions; would have caught the edge-cases P3 misrouting on the smoking-gun docstring "Refines A3."
- **Evaluation gate:** on the next bulk-edge-case inquiry's critique, observe whether the new sub-axis is applied and whether it catches at least one internal-contradiction-shaped issue. If applied and caught: PROMOTE. If applied and no issues exist to catch (clean candidate set): MONITOR for next opportunity. If not applied: defect in adoption; investigate.
- **Should it become a branch experiment?** YES — applied on the next correction-chain-similar inquiry as a branch test before promoting to the canonical spec.

**Inversion-candidate.** Alternative shape: ADD-CONTENT to existing Substance-axis prosecution instead of new sub-axis. 5-test: novel MED; scrutiny PARTIAL — could be folded in but new sub-axis name (Candidate-Self-Consistency) makes the move discoverable. **Verdict: REFINE-accepted (could be implemented either way; sub-axis name preferred for discoverability).**

---

## P7 — Maintenance Candidate 2: comparative-pattern perspective in sense-making

**Principal.**

- **What:** add a perspective to the Phase 2 Perspective Checking list in `/Users/ns/.claude/skills/sense-making/references/sensemaking.md`. Perspective name: **Comparative-Pattern Test perspective**. When the inquiry commits a structural decision (schema home, axis assignment, routing of a new field into an existing scheme), explicitly compare each candidate against the existing pattern of analogous decisions in the target scheme. If the new field's shape doesn't match the existing pattern, the routing requires explicit defense (not just principle-derivation).
- **File affected:** `/Users/ns/.claude/skills/sense-making/references/sensemaking.md` — adds a ~10-15-line perspective entry next to existing Definitional / Internal Consistency and Definitional / Frame-exit Completeness perspectives.
- **Risk class:** LOW. Additive perspective; explicit pattern-comparison is already present in spirit (the Specific-vs-pattern recognition cue at Phase 3) but not as a structural-decision-routing test.
- **Expected benefit:** catches schema-home-routing-type conflations like the edge-cases misrouting by forcing comparison to A1/A2/A3 reader-property pattern, A5/A6 strategy-enum pattern. Would have caught all 3 misrouted fields.
- **Evaluation gate:** on the next bulk-edge-case inquiry's sensemaking, observe whether the Comparative-Pattern Test perspective fires per structural decision and whether it surfaces any routing inconsistency. If fired and catches: PROMOTE. If fired no catches (clean candidate set): MONITOR. If not fired: defect in adoption.
- **Should it become a branch experiment?** YES — branch test on next correction-chain-similar inquiry.

**Inversion-candidate.** Alternative shape: extend the Specific-vs-pattern recognition cue at Phase 3 instead of new perspective at Phase 2. 5-test: novel MED; scrutiny PARTIAL — the cue is about whether a key insight generalizes to a wider pattern; the new perspective is about whether a structural decision matches an existing routing pattern. Different operations. **Verdict: KILL (different operation; new perspective is the load-bearing addition).**

---

## P8 — Maintenance Candidate 3: principle sharpening in chunking finding (GATED)

**Principal.**

- **What:** add an inline refinement to the chunking finding (`devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` section 3) that explicitly states: *"The principle distinguishes three categories: (a) facts about the source (corpus declarations) → SourceDescriptor; (b) reader-properties (including reader-properties that reference source languages) → TranslationConfig; (c) user strategies for handling source properties → TranslationConfig. The chunking case applies (a)."*
- **File affected:** `devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md` — inline addition; not a structural change.
- **Risk class:** LOW (inline; reversible).
- **Expected benefit:** prevents downstream over-generalization from "source-natural-units" to "anything source-related."
- **Evaluation gate:** GATED — revival trigger is a second correction chain involving a similar facts-vs-strategies conflation. Per LOOP_DIAGNOSE guardrail ("Do not propose broad fundamentals rewrites from one weak correction chain"), defer canonical principle sharpening until a second instance shows the pattern.
- **Should it become a branch experiment?** NO — defer to revival trigger; not branched now.

**Inversion-candidate.** Alternative shape: PROMOTE-NOW (not gate; apply principle sharpening immediately). 5-test: novel NO; scrutiny WEAK (LOOP_DIAGNOSE explicit guardrail against broad rewrites from one chain). **Verdict: KILL.**

---

## P9 — Inherited Commitments Re-test (Synthesis Trigger)

**Principal.**

### From the chunking finding (`devdocs/inquiries/2026-06-14_00-50__chunking_deep_dive/finding.md`)

| # | Commitment | Status | Evidence / Reason |
|---|---|---|---|
| A1 | "Schema ownership matches data ownership" principle | RE-TESTED — confirmed BUT FRAME REVISED | Principle correct as stated; abstraction to facts-vs-strategies was implicit and produced downstream conflation. Frame revised: principle anchored to source-natural-units; needs sharpening per MC3 (gated) |
| A2 | Three-operation chunking category | RE-TESTED — confirmed | Out of this inquiry's scope as a target; survives unchanged |
| A3 | Split placement across SourceDescriptor + PipelineConfig + TranslationConfig | RE-TESTED — confirmed | The split itself survives; the application to specific fields (edge-cases inquiry) is where the failure occurred, not the split itself |
| A4 | #1 → ChunkingUnit.is_atomic; #6 → ChunkingUnit.attached_to; #7 → orthogonal | RE-TESTED — confirmed | These specific routings are correct |

### From the edge-cases-into-config-schema finding (`devdocs/inquiries/2026-06-14_01-32__edge_cases_into_config_schema/finding.md`)

| # | Commitment | Status | Evidence / Reason |
|---|---|---|---|
| B1 | The 14 edge-case candidates as bounded set | RE-TESTED — confirmed | Scope unchanged |
| B2 | TranslationConfig delta = 0 | RE-TESTED — commitment found INVALID | Conversation correction shows 3 fields belong on TC; TC delta is not 0 |
| B3 | 3 ALREADY-ROUTED (#1, #6, #7) inherit from chunking | RE-TESTED — confirmed | Inherited routings are correct |
| B4 | 4 ADD-now to SourceDescriptor: #2 source_language_fluency / #3 source_edition / #8 quranic_citation_policy / #13 source_temporal_register | RE-TESTED — commitment found INVALID for 3 of 4 | Only #3 source_edition stays on SD (genuinely a source fact). #2, #8, #13 → TC. See P11 corrected routing |
| B5 | 7 DEFER with revival triggers | RE-TESTED — confirmed | Revival triggers unaffected by this diagnostic |
| B6 | 2 non-modifications (A3 stays as-is; UseContext deferred as schema) | RE-TESTED — confirmed | Both non-modifications hold; #2's "add beside A3" reasoning was correct in intent but the "beside" was on the wrong schema |
| B7 | Cross-axis conflict check: 0 hard conflicts, 2 docs notes | RE-TESTED — frame revised | The conflict check passed because the routing's internal contradiction (docstring-vs-routing) wasn't tested. Conflicts-by-existing-axis-pattern is a new category surfaced by this diagnostic |
| B8 | EmbeddedLanguagePolicy carrying quranic_citation_policy | RE-TESTED — commitment found INVALID | Conversation correction explicitly identified this as the conflation site ("bundling a strategy choice inside a source-property declaration") |
| B9 | Phase 2 SourceDescriptor implementation gates on chunking finding's SD MUST | RE-TESTED — confirmed | Implementation gate holds; what gets implemented is revised per P11 |
| B10 | Pattern-level applicability to Bible/Quran/Hindu corpora | INHERITED-WITHOUT-RE-TEST | Out of scope; pattern-applicability claim depends on the corrected routing being tested across corpora |

**Inversion-candidate.** Alternative: skip per-commitment re-test (just declare "inherited and revised where needed"). **Verdict: KILL** — Synthesis Trigger explicitly requires per-commitment re-test.

---

## P10 — Diagnostic Verdict

**Principal.**

**Overall:** ACTIONABLE.

- **Best-supported diagnosis:** Hypothesis 2 (edge-cases critique missed principle-application correctness; substance-axis prosecution didn't apply candidate's own claims against its own decision). The smoking gun (docstring-vs-routing internal contradiction in `source_language_fluency`) is concrete; the missing-dimension claim is supported by direct enumeration of the 8 dimensions used. PRIMARY with HIGH confidence, jointly with Hypothesis 1.

- **Strongest maintenance candidate:** MC1 (Candidate-Self-Consistency sub-axis in td-critique). Concrete; small refinement note; testable evaluation gate; would have caught the smoking-gun docstring contradiction.

- **Main uncertainty:** the relative weight between Hypothesis 1 (sensemaking SV6) and Hypothesis 2 (critique). Both fired at HIGH confidence; attribution is jointly primary. Further correction chains would help distinguish.

- **Recommended next step:** branch-test MC1 (substance-axis sub-axis sharpening) and MC2 (Comparative-Pattern Test perspective) on the next bulk-edge-case inquiry. If both fire and catch at least one issue each, promote to canonical spec. MC3 (principle sharpening in chunking finding) stays gated pending a second correction chain.

**Inversion-candidate.** Alternative: PARTIAL or INCONCLUSIVE verdict (defer source edits). 5-test: novel MED; scrutiny WEAK — MC1 and MC2 have concrete shapes + evaluation gates; ACTIONABLE is warranted. **Verdict: KILL.**

---

## P11 — Corrected routing (secondary constructive per WHY-axis `practical-application-now`)

**Principal.**

The 4 fields edge-cases finding misrouted to SourceDescriptor, with the corrected routing:

| # | Field | Original (edge-cases inquiry) | Corrected (per conversation correction) | Reasoning |
|---|---|---|---|---|
| 2 | `source_language_fluency: dict[str, FluencyLevel]` | SourceDescriptor | **TranslationConfig** | Reader-property — matches A1/A2/A3 pattern. The reader has fluency in source languages; the source doesn't have fluency. The edge-cases P3 docstring "Refines A3" already names the correct home (A3 is on TC). |
| 3 | `source_edition: str \| None` | SourceDescriptor | **SourceDescriptor** ✓ | Genuine source fact (which printing this is). Stays. |
| 8 | `quranic_citation_policy: Literal[...]` | SourceDescriptor (inside EmbeddedLanguagePolicy) | **TranslationConfig** (or new apparatus axis) | Strategy enum for citation rendering. The FACT that Quranic citations are embedded → SD's `embedded_languages: list[str]`; the STRATEGY for how to render → TC. |
| 13 | `source_temporal_register: Literal["preserve-archaic", "modernize-fully", "hybrid-by-register-domain", "mark-archaisms-explicitly"]` | SourceDescriptor | **TranslationConfig** | Strategy enum (verbs of handling: preserve/modernize/hybrid/mark) — parallel to A5 source_fidelity. The FACT that the source has archaic register → could be a SD declaration (e.g., `source_archaism_present: bool` or implicit in `source_edition`); the STRATEGY for handling → TC. |

**Revised totals:**
- **TranslationConfig delta:** +3 new fields (`source_language_fluency`, `source_temporal_register`, `quranic_citation_policy`) — not +0 as the edge-cases finding claimed.
- **SourceDescriptor delta:** +1 (`source_edition`) + optional `embedded_languages: list[str]` (just the facts) — not +4 as the edge-cases finding claimed.

This corrected routing is the secondary constructive output. Per LOOP_DIAGNOSE protocol, the primary output is the diagnostic (P1-P10). The constructive output is included to address the user's WHY-axis `practical-application-now`.

**Inversion-candidate.** Alternative shape: omit P11 entirely (LOOP_DIAGNOSE is diagnostic, not constructive). 5-test: novel YES; scrutiny PARTIAL — protocol-pure but user's WHY-axis explicitly motivates constructive output now. **Verdict: REFINE-accepted — include but mark as secondary.**

---

## Assembly Check

Survivors jointly form a complete LOOP_DIAGNOSE-protocol-compliant finding plus secondary corrected routing. Three emergent insights:

**Emergent 1: Substrate-reachability is the diagnostic frame's anchor.** The conversation correction used only substrate available to the original inquiries; this proves the failure is "missing test against available information," not "missing information." All maintenance candidates target test-mechanisms (substance-axis sub-axis; comparative-pattern perspective), not new information sources.

**Emergent 2: The two strong MCs (MC1 + MC2) are complementary, not redundant.** MC1 catches internal contradictions (candidate's own claims vs candidate's own decision). MC2 catches external-pattern mismatches (decision vs existing pattern in target schema). The edge-cases misrouting failed BOTH tests; a future inquiry's misrouting might fail only one. Branch-test both.

**Emergent 3: Self-Reference Blindness is partially mitigated, partially structural.** LOOP_DIAGNOSE's protocol explicitly addresses the self-reference issue (comparative-evidence framing for the corrected direction); but the AI doing both the original inquiries and the diagnostic introduces a partial blind spot. Mitigation: user pushback was the trigger; the AI's diagnostic role is to systematize the user's intuition, not to validate itself. This emergent insight should be noted in Finding's Reasoning.

---

## Failure-mode check

- Premature evaluation: NO. Single-mechanism trap: NO. Early frame lock: NO. Innovation without grounding: NO. Mechanism exhaustion: NO. Survival bias: NO (3 KILL inversions; 2 REFINE-accepted with notes).

---

## Telemetry

- Generators: 4/4 (Combination, Absence Recognition, Domain Transfer, Extrapolation). Framers: 3/3 (Lens Shifting, Constraint Manipulation, Inversion).
- Convergence: YES (MC1 + MC2 reached via multiple mechanisms).
- Survivors tested: 22 (11 principal + 11 inversion).
- Disposition: 11 ACTIONABLE principals + 2 REFINE-accepted inversions (P6, P11) + 9 KILL inversions.
- Per-piece compliance: 11/11 satisfied.
- Failure modes: 0.
- Overall: PROCEED.
