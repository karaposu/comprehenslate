# Critique — translation_failure_root_cause_diagnosis

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-03_23-30__translation_failure_root_cause_diagnosis/_branch.md`

Critique-target candidates: the 9 surviving outputs from `innovation.md` (S1–S9) + the Emergent Assembly + P1 (diagnosis communication itself). Coverage-gap check will surface S10 (polysemy disambiguation principle, latent in innovation but not elevated to a named survivor).

Stakes assessment: **HIGH** (framework changes touch all future translations; hard to fully revert). Default burden of proof: defense must demonstrate clear viability. Default lean: don't approve unless clearly viable.

---

## Phase 0 — Dimension Construction

### Extracted from sensemaking output

From sensemaking's anchors:
- **Constraints CON-1, CON-3:** failures real and pattern-consistent → demands a fix that addresses the *pattern*, not just instances.
- **Constraint CON-4:** text was short → disconfirms volume-based interventions.
- **Key insights KI-1, KI-2:** harmony_layer's tier system has an internal inconsistency → demands either repair or replacement at the structural level.
- **Key insight KI-3:** harmony report is structurally blind → demands the audit instrument be made register-sensitive.
- **Key insights KI-5, KI-6:** C1-misread as trigger; shared meta-cause across both failure types → demands trigger-coverage AND meta-level diagnostic mode.
- **Key insight KI-7:** lesson siloing as architectural property → demands at minimum a lightweight learning loop.
- **Foundational principles FP-1, FP-2:** principles ≠ failure modes; diagnostic mode is distinct from prescriptive mode → demands explicit failure-mode artifacts.
- **Meaning-nodes MN-1 through MN-6:** register pull-up, framework blindness, principle/failure-mode asymmetry, lesson siloing, C1-misread, metaphor-momentum → each must be addressed by some candidate.

### Evaluation dimensions (8 total: 6 default + 2 project-specific)

| # | Dimension | What it asks | Weight | Source |
|---|---|---|---|---|
| D1 | **Correctness** | Does the candidate address the actual diagnosed cause (not a plausible-sounding wrong cause)? | **5 (critical)** | Meaning-nodes + key insights |
| D2 | **Coherence** | Does it fit with existing framework's good parts without breaking them? | 3 (medium) | Structural points + constraints |
| D3 | **Feasibility** | Can the user actually implement this with their available time and resources? | 4 (high) | Constraints + foundational principles |
| D4 | **Completeness** | Does it address the relevant causal layer(s) the user needs to act on? | **4 (high)** | Meaning-nodes |
| D5 | **Robustness** | Does it work for FUTURE unknown failure modes, or only the observed ones? | 3 (medium-high) | Constraints + key insights |
| D6 | **Elegance** | Minimum sufficient intervention? Or over-engineered? | 2 (medium-low) | FP-3 (avoid over-engineering) |
| D7 | **Recurrence prevention** *(project-specific risk)* | Does it specifically prevent register pull-up + polysemy from recurring? | **5 (critical)** | Explicit user goal in _branch.md Goal section |
| D8 | **Trigger coverage** *(project-specific risk)* | Does it address the C1-misread proximate trigger, or only structural amplifiers? | 4 (high) | Sensemaking's 4-layer causal stack |

**Project-specific risk dimension check (Phase 0 refinement):** the candidate set involves project artifacts (`harmony_layer.md`, `notes.md`), operations (translation), and state (the diagnosis itself). D7 (recurrence prevention) and D8 (trigger coverage) are the project-specific risk axes; both included per the refinement note.

**Dimension validation:** Would a candidate passing all 8 dimensions perfectly actually solve the problem? YES — it would address the diagnosed cause (D1), fit the framework (D2), be implementable (D3), cover the relevant layers (D4), survive future failures (D5), avoid over-engineering (D6), prevent the documented recurrence (D7), and address the trigger (D8). Dimensions are sufficient.

---

## Phase 1 — Fitness Landscape

### Viable region

A candidate is in the viable region when it passes all **critical-weight** dimensions (D1, D4, D7) AND has acceptable feasibility (D3). It may have weaknesses on D2, D5, D6, or D8 — but those weaknesses are managed via refinement or composition, not via outright rejection.

### Dead region

A candidate is dead if it FAILS on any critical-weight dimension (D1, D4, D7). Specifically:
- Fails on D1 (Correctness) → doesn't address the diagnosed cause → dead regardless of other dimensions.
- Fails on D4 (Completeness) → misses an entire causal layer the user needs → dead unless composed with other candidates that cover the missing layer.
- Fails on D7 (Recurrence prevention) → doesn't prevent the documented failure → dead.

### Boundary regions

| Boundary | Characterization |
|---|---|
| **Strong correctness, weak feasibility** | Architecturally sound but too expensive to do now (e.g., S6, S7). Resolution: defer with revival trigger. |
| **Strong feasibility, partial completeness** | Cheap to do but covers only one layer (e.g., S8 alone, S9 alone). Resolution: compose with others. |
| **Strong recurrence prevention, weak robustness** | Catches the OBSERVED failures but not future ones (e.g., S2 without expansion mechanism). Resolution: pair with learning loop. |

### Unexplored regions

- **User-translator collaboration patterns** (e.g., "AI asks clarifying questions about audience before translating"). Not in the innovation candidate set. Could potentially address the trigger layer differently than S9.
- **Prompt-engineering-only interventions** (modify the AI's task prompt rather than framework docs). Out of scope per sensemaking's Frame-exit verdict (AI behavior in-scope-via-trigger, not as direct target). Intentional unexplored.
- **Source-text-pre-analysis** (require the AI to characterize source register before translating). Adjacent to S9 but distinct. Not in the candidate set; worth flagging as a future seed if S9 proves insufficient.

---

## Phase 2 — Adversarial Evaluation per Candidate

### S1 — Rules-with-violations reorganization

**Prosecution.** Killer objection: this requires REWRITING all existing principles in `notes.md` to fit the new structure. High overhead. User has already invested in the current principle format; restructuring loses that investment. Specification-gap probe: innovation said "preserved at the reading level" but did not specify the operational mechanism by which each entry's positive vs negative reading is rendered at the level the AI can act on. Worst realistic outcome: months of restructuring work; existing useful content gets mangled in translation to the new format.

**Defense.** Deepest strength: dissolves the principle/failure-mode artifactual split that the user intuited in their sub-question; unifies the framework structurally; serves both prescriptive and diagnostic cognitive modes from one structural artifact. Long-term cleaner and more maintainable. Aligns with the user's own framing intuition.

**Collision.** Defense wins on conceptual level. Prosecution wins on operational scope/cost. Resolution: apply S1 to NEW entries (the failure-mode catalog), leave existing principles alone, evolve over time. The scope-restricted version is feasible; the wholesale version is not.

**Dimension scoring.** D1: passes (addresses the principle/failure-mode asymmetry). D2: weak-as-wholesale, strong-as-scoped. D3: weak-as-wholesale, strong-as-scoped. D4: covers META layer. D5: strong (extensible structure). D6: strong. D7: indirect. D8: not directly.

**Verdict: REFINE.** Direction: apply rules-with-violations format only to new failure-modes catalog entries; mark wholesale application as a long-term research direction; do not rewrite existing principles in this round. Position: boundary region (strong D1/D5/D6, weak D3 unless scope-restricted).

---

### S2 — Berman's twelve as catalog seed

**Prosecution.** Killer objection: Berman's twelve are 40-year-old translation studies, designed for HUMAN translators of CLASSICAL EUROPEAN literary texts. AI failure modes may differ substantively. **User-perspective objection (per multi-axis prosecution depth):** the user is translating Said Nursi's Risale-i Nur specifically — an Islamic theological text in Ottoman Turkish with Arabic-Persian compounds. Berman wrote about classical European literary translation. Cultural-domain mismatch is real. Some of Berman's twelve may not apply at all; some AI-specific failures (metaphor-momentum override) match none of his twelve. **Specification-gap probe:** which of Berman's twelve apply to this user's specific corpus? Innovation said "register pull-up = ennoblement" but did not enumerate which of the other eleven fire. Worst realistic outcome: 12 entries imported wholesale, only 3-4 actually fire, the catalog gets diluted, user loses confidence in the catalog.

**Defense.** Deepest strength: avoids reinventing the wheel; provides external grounding (per FP-4); "register pull-up = ennoblement" is empirical validation that the failure mode is real, named, and recognized in established translation studies. Reduces self-reference blindness — the catalog isn't generated only from this one inquiry's findings. Berman's framework also has structure (he names mechanism, not just pattern); importing that discipline raises catalog-authoring quality.

**Collision.** Defense's external-grounding argument is strong; prosecution's cultural-domain-mismatch and specification-gap arguments are also strong. Resolution: Berman is a CHECKLIST for catalog authoring, not a wholesale import. For each of Berman's twelve, ask "has this failure pattern occurred or is likely to occur in my translations?"; include only the fired/likely ones; ADD AI-specific entries (metaphor-momentum override, audience-spec misinterpretation, transliteration over-application) that Berman doesn't cover.

**Dimension scoring.** D1: strong (addresses the META layer). D2: strong. D3: medium (requires filtering work). D4: strong (catalog as META-layer fix). D5: strong (extensible). D6: medium. D7: strong (catalog enables recurrence prevention via diagnostic mode). D8: indirect.

**Verdict: REFINE.** Direction: use Berman as a CHECKLIST during catalog authoring; include only the ones that have fired or are likely; add AI-specific entries that Berman doesn't cover; document which Berman entries were excluded and why. Position: boundary region (strong D1/D7 + medium D3 — refinement makes it viable).

---

### S3 + S9 — Skopos / audience-spec rule (composite)

**Prosecution.** Killer objection: adds friction at translation start; the user has to commit to skopos before AI begins. Many users will just say "translate it normally" without thinking through skopos. **Specific failure-case scenario (per multi-axis prosecution depth):** user passes "translate this for a general audience" — the skopos is under-specified; how does the rule handle this? **Specification-gap probe:** HOW does the framework enforce the skopos commitment? Does the AI refuse to translate without explicit skopos? Or default to a "neutral" skopos? Innovation didn't specify the enforcement mechanism. **User-perspective objection:** the user provided "C1 English speakers" as instructions — they may not want to be required to write a paragraph of skopos before each translation.

**Defense.** Deepest strength: directly addresses the C1-misread trigger (D8 critical-weight); skopos theory is well-established in translation studies (D5 external grounding); gives the AI a clear input-interpretation rule that the framework currently lacks. Targets the PROXIMATE layer of the causal stack — the only candidate that does so directly.

**Collision.** Defense wins on directness — this fix targets the actual trigger. Prosecution's friction objection is addressable: the rule can have a DEFAULT skopos ("match source register faithfully; preserve register alternation as Tier 1; do not interpret audience-capability descriptors as vocabulary-level licenses") that fires when user doesn't explicitly override. User only needs to specify skopos when they want a NON-DEFAULT skopos. Specification-gap addressed by the default-skopos refinement.

**Dimension scoring.** D1: strong. D2: strong (additive). D3: strong (one rule with default). D4: covers PROXIMATE layer (the only candidate that does). D5: strong (skopos is generalizable). D6: strong. D7: strong. D8: strong (the dedicated trigger-coverage candidate).

**Verdict: SURVIVE.** Refinement note: specify a default skopos so the rule doesn't require user opt-in; the rule fires by default with "match source register faithfully"; user can override per translation. Position: viable region (strong across all critical dimensions).

---

### S4 + S5 — Reorganize-without-adding + Multi-axis harmony report (composite)

**Prosecution.** Killer objection: the existing harmony report runs POST-translation; restructuring it doesn't catch failures DURING translation. Failures happen first, audit catches them after — there's a re-translation cost. **Specific failure-case scenario:** the audit detects "register pull-up flagged on 3 sections" but the user is unwilling to re-translate. The audit becomes a noise generator with no action path. **Specification-gap probe:** what are the EXACT required sections in the multi-axis report? Innovation listed candidates (Register Fidelity Audit, Markedness Audit, Per-Section Comparison, Failure-Mode Scan) but didn't specify the full schema. Worst realistic outcome: every translation produces flags; user ignores them; audit becomes a checkbox without behavioral consequence.

**Defense.** Deepest strength: reuses existing infrastructure (the harmony report at file-bottom already exists per E-45); very cheap; immediately deployable. Even if user ignores flags initially, the audit creates DOCUMENTATION of where failures occurred — feeds back to the documented-failure-trace practice (S8). Post-hoc safety net catches what pre-translation prevention (S9) misses.

**Collision.** Defense wins on feasibility and elegance. Prosecution's "post-hoc isn't pre-hoc" objection is real but addresses a DIFFERENT problem: pre-translation prevention is S9's job; post-translation detection is S4+S5's job. They're complementary. Specification-gap addressed by listing four required sections explicitly: (a) Tier-1 preservation (existing), (b) Register Fidelity Audit (new), (c) Markedness Audit (new), (d) Failure-Mode Scan referencing the catalog (new — depends on S2).

**Dimension scoring.** D1: strong (addresses STRUCTURAL layer's audit blindness). D2: strong (reuses existing instrument). D3: very strong (cheapest viable). D4: covers STRUCTURAL layer. D5: strong (sections extensible). D6: strong. D7: strong (audit catches recurrence). D8: indirect (post-hoc).

**Verdict: SURVIVE.** Refinement: specify the four required sections in the restructured harmony report. Position: viable region (strong D3 + D6, good across other dimensions).

---

### S6 — Memory→spec ingestion architecture

**Prosecution.** Killer objection: high engineering cost; uncertain marginal value at current translation volume; architectural addition with no immediate payoff. **Specific failure-case scenario:** the user does ~1 translation per week; in 6 months, perhaps 4 lessons accumulate in memory; the ingestion overhead vastly exceeds the per-lesson cost of just running a quick MVLw-style inquiry per failure. **User-perspective objection:** the user hasn't yet expressed willingness to invest in architectural work; the user's current expressed need is "fix what's broken now," not "build a learning system." Worst realistic outcome: significant engineering investment; few lessons accumulate; ingestion path is over-engineered for the actual flow rate.

**Defense.** Deepest strength: only mechanism that fully addresses the ARCHITECTURAL-layer cause (G-59 lesson siloing); essential for long-term learning capacity; prevents per-failure ad-hoc inquiries from compounding indefinitely.

**Collision.** Defense's "essential for long-term" is structurally true but timing-sensitive. Prosecution's "high cost, low immediate value at current volume" wins on current-state terms. Resolution: defer is the right disposition. But: a LIGHTWEIGHT alternative exists in the candidate set — S8 (documented-failure-trace practice) provides a NARRATIVE-form learning loop without architectural work. S8 partially substitutes for S6 at low cost.

**Dimension scoring.** D1: strong. D2: weak (architectural addition, not in current framework). D3: weak (high cost). D4: covers ARCHITECTURAL layer. D5: very strong (handles future unknown failures). D6: weak (heavy). D7: indirect (long-term). D8: not directly.

**Verdict: REFINE → DEFERRED with revival trigger.** Direction: park as the eventual architectural-layer fix; S8 provides lightweight near-term coverage of the same layer. Revival trigger: when ≥3 additional translation failures have been diagnosed via separate inquiries, the marginal cost of architectural investment becomes lower than per-failure inquiry cost. Position: boundary region (strong D1/D5 + weak D3 = boundary; deferral resolves it).

---

### S7 — Tier-system replacement

**Prosecution.** Killer objection: replacing the tier system requires re-categorizing every existing harmony component and re-authoring the tier-priority logic. High migration cost. **Specification-gap probe:** HOW is the proposed severity-based priority calibrated? Innovation didn't specify the severity metric. **Specific failure-case scenario:** during migration, the new severity-based system has its own calibration problems (severity is a different kind of fuzzy judgment than meaning-priority); the framework loses its working tier-prioritization without a clean replacement; user reverts to ad-hoc decisions. Worst realistic outcome: framework is in a worse state during the migration than before.

**Defense.** Deepest strength: the CLEANEST principle-level fix; eliminates the internal-inconsistency root cause rather than patching it. Long-term it's the right architecture.

**Collision.** Defense wins on long-term correctness; prosecution wins on migration cost and specification gap. The principal P2 candidate (REPAIR — upgrade register to Tier 1 with gating) achieves the same immediate effect at vastly lower cost.

**Dimension scoring.** D1: very strong (root-level fix). D2: weak (replaces existing). D3: very weak (high migration cost). D4: covers STRUCTURAL layer. D5: strong (clean structure). D6: weak (specification work). D7: strong. D8: indirect.

**Verdict: REFINE → RESEARCH FRONTIER.** Direction: not actionable now. Park for future revisit when the failure-modes catalog has matured and migration cost can be assessed against accumulated evidence. The principal P2 REPAIR provides the same short-term effect at much lower cost. Position: unexplored region for long-term architecture.

---

### S8 — Documented-failure-trace practice

**Prosecution.** Killer objection: keeping `eng.md` "as evidence" might confuse future users who expect a clean translation when they see `eng.md`. Documentation overhead. **Specific failure-case scenario:** someone (the user later; another reader; a future AI session) copies "corvée" or "Padishah" from `eng.md` thinking it's the right translation; the documented failure becomes a VECTOR for the failure's spread. **Specification-gap probe:** how is the file marked as a documented failure trace? A frontmatter? A header?

**Defense.** Deepest strength: turns the failure into a positive asset (calibration evidence); aligns with the framework's diagnostic-first reorganization (S2+); preserves the diagnostic value of the original. Provides a NARRATIVE-form lesson-loop that partially substitutes for the heavy S6 architecture. Cheapest possible intervention.

**Collision.** Defense wins. Prosecution's "vector for spread" concern is real but fully addressable by adding a clear marker at file-top ("⚠ DOCUMENTED FAILURE TRACE — see this diagnostic inquiry; do not use this translation as a source").

**Dimension scoring.** D1: strong (addresses ARCHITECTURAL layer in narrative form). D2: strong (additive). D3: very strong (trivial cost). D4: covers ARCHITECTURAL layer (lightweight). D5: medium (one entry isn't a learning system). D6: very strong. D7: indirect. D8: not directly.

**Verdict: SURVIVE.** Refinement: add a header to `eng.md` explicitly framing it as a documented failure trace; cross-reference this inquiry. Position: viable region (high D3 + D6, addresses ARCHITECTURAL via narrative substitution).

---

### S10 — Polysemy disambiguation principle (coverage-gap candidate elevated by critique)

**Critique-observed gap:** Innovation's surviving list (S1–S9) does not explicitly name the P4 piece's principal output (the polysemy-disambiguation principle for `notes.md`). The piece-level Inversion at P4 was performed and the DO-NOTHING alternative rejected, meaning ADD-CONTENT was retained — but this output wasn't elevated to a named survivor. Critique elevates it as S10 to address the polysemy failure type explicitly.

**Prosecution.** Polysemy is rarer than register pull-up; lower per-encounter incidence. Worst case: principle is authored but never fires because polysemy cases are rare in the user's near-term corpus. **Specification-gap probe:** how does the principle articulate the plausibility test (per the saved memory `feedback_translation_polysemy.md`)?

**Defense.** Deepest strength: the *nefer* case is a documented failure; principle covers a real failure type. Cheap to author (one principle + worked example + cross-reference to S2's "metaphor-momentum override" catalog entry). User's corpus (Said Nursi's Risale-i Nur with Arabic-Turkish-Persian compounds) has high polysemy density — the failure type will recur.

**Collision.** Defense wins (cheap, covers documented failure type, user-corpus-relevant). Prosecution's "rare" framing weakened by corpus-specific evidence.

**Dimension scoring.** D1: strong. D2: strong. D3: very strong (cheap). D4: covers PROXIMATE layer for polysemy. D5: medium. D6: strong. D7: strong (specifically prevents polysemy recurrence). D8: medium.

**Verdict: SURVIVE.** Refinement: explicit plausibility test (per the saved memory). Position: viable region.

---

### P1 — Diagnosis communication

**Prosecution.** Killer objection: the 4-layer causal stack might be over-structured; reality might be simpler ("the docs were missing things and the AI made one bad call"). **User-perspective objection:** the user asked a relatively direct question ("what went wrong?"); a 4-layer answer may feel like over-engineering. **Specification-gap probe:** how does the diagnosis communicate to a user who hasn't read the upstream sensemaking — i.e., to the user encountering this finding fresh?

**Defense.** Deepest strength: the 4-layer structure surfaces causes at different leverage points; user can choose where to intervene. The diagnosis directly answers the user's three named hypotheses (H1/H2/H3) and surfaces the two they didn't name (H4/H5). The watershed finding (harmony_layer's internal inconsistency) is structurally proven, not merely asserted.

**Collision.** Defense wins. The 4-layer structure is well-grounded in sensemaking and HELPS the user prioritize. Refinement: communication should be sized to user appetite — provide both a tight summary AND the full layered structure, so the user can read at their preferred depth.

**Dimension scoring.** D1: strong. D2: n/a (communication, not a fix). D3: strong (already drafted). D4: covers all 4 layers explicitly. D5: n/a. D6: medium (somewhat dense). D7: indirect. D8: covers H4 directly.

**Verdict: SURVIVE.** Refinement: provide both summary form and detailed form. Position: viable region.

---

### Emergent Assembly — "diagnostic-first framework with documented calibration"

Composite: P1 + S9 + S8 + (S4+S5) + S2 (refined to filtered Berman + AI-specific entries) + S10.

**Prosecution.** Killer objection: this is a coordinated multi-piece program. Coordinating ≥6 pieces is harder than implementing any one of them. **Specific failure-case scenario:** the user commits to the assembly, then partially implements (does S9 + S8 — the cheapest two; skips S2 and S4+S5 — more work); the framework now has a skopos rule + documented evidence but no failure-modes catalog or audit. The structural-layer cause is still present; the user has done HALF the fix and may conclude the fix doesn't work. **Specification-gap probe:** in what ORDER should the user implement the pieces?

**Defense.** Deepest strength: addresses all 4 causal layers from sensemaking without requiring heavy S6 engineering. Closed feedback loop in narrative form. The only candidate set that achieves full causal-layer coverage. Each piece is INDIVIDUALLY viable, so partial implementation still has value even if not full effect.

**Collision.** Defense wins on coverage. Prosecution's "partial implementation risk" is real but addressable by explicit ordering with rationale.

**Recommended implementation order:**
1. **S9 (skopos / audience-spec rule)** + **S10 (polysemy principle)** — proximate-layer fixes; cheap; high marginal recurrence-prevention value.
2. **S8 (documented-failure-trace practice)** — flag `eng.md` with header; trivial cost; immediate calibration value.
3. **P2 principal (register tier fix in harmony_layer.md)** — surgical edit; ~30 min work; structural-layer foundation.
4. **S4 + S5 (multi-axis harmony report restructure)** — reorganize existing instrument; couples with S2 below.
5. **S2 (failure-modes catalog seeded by filtered Berman + AI-specific entries)** — META-layer fix; largest single piece; couples with S4+S5.
6. **(Long-term)** S6 deferred; S7 research frontier; S1 wholesale application as research direction.

**Dimension scoring.** D1: very strong. D2: strong. D3: medium (multi-piece coordination). D4: very strong (all 4 layers covered). D5: strong. D6: medium. D7: very strong. D8: strong.

**Verdict: SURVIVE.** Refinement: provide the explicit implementation order above. Position: dominates the individual-survivor space; central viable region.

---

## Phase 3.5 — Assembly Check (cross-survivor)

Beyond the Emergent Assembly already in the candidate set, critique surfaces one additional sub-assembly:

### Sub-Assembly A — Minimum Viable Fix (MVF)

Subset of the Emergent Assembly: **S9 + S8 + S10 + P2-principal**. These four pieces alone constitute the cheapest viable response that touches the PROXIMATE layer (S9, S10) and the STRUCTURAL layer (P2) with lightweight ARCHITECTURAL-layer coverage (S8). Total estimated effort: ~2-4 hours.

- Drops: S2 (catalog authoring is the largest piece; can be deferred until ≥1 more failure is documented in narrative form).
- Drops: S4+S5 (audit reorganization is moderately costly; can be deferred until the catalog exists to reference).
- Risks: META-layer fix is deferred; no failure-mode-driven attention enables the diagnostic mode.

**Verdict on MVF: SURVIVE as a user-choice sub-option.** If the user wants minimum cost / maximum immediate effect, MVF is the right disposition. If the user wants the full diagnostic-first framework, the Emergent Assembly is the right disposition.

---

## Phase 4 — Coverage + Convergence Assessment

### Coverage map

**Causal-layer coverage (from sensemaking SV6):**
| Layer | Surviving candidates that address it |
|---|---|
| **PROXIMATE** (C1-misread, metaphor-momentum) | S9 ✓, S10 ✓ |
| **STRUCTURAL** (tier mis-classification, principle gaps, audit blindness) | P2-principal ✓, S4+S5 ✓; S7 deferred to RESEARCH FRONTIER |
| **META** (principle/failure-mode asymmetry; no diagnostic mode) | S2 ✓ (refined); S1 ✓ (scope-restricted to new entries) |
| **ARCHITECTURAL** (lesson siloing; no learning loop) | S8 ✓ (narrative-form lightweight); S6 deferred with revival trigger |

**All 4 causal layers have at least one SURVIVING candidate.**

**Failure-type coverage:**
| Failure type | Addressed by |
|---|---|
| Register pull-up | S2 catalog (refined); S4+S5 audit; S9 skopos rule (prevention); P2 tier fix |
| Polysemy mis-resolution (metaphor-momentum override) | S10; S2 catalog entry |
| Audience-spec misinterpretation | S9 skopos rule |
| Markedness inversion | S2 catalog (refined); included in S4+S5 markedness-audit section |
| Transliteration over-application | S2 catalog entry (if included) |

**All named failure types covered by at least one survivor.**

### Unexplored regions assessment

- **User-translator collaboration patterns:** unexplored but adjacent to S9. Could provide an alternative trigger-layer fix. NOT critical for this round; could be a future seed.
- **Prompt-engineering-only interventions:** intentionally out of scope per sensemaking's Frame-exit verdict.
- **Source-text-pre-analysis:** adjacent to S9; could complement it. Worth flagging as a future seed.

No unexplored regions are critical for the user's current goal.

### Convergence assessment

- **Has at least one candidate SURVIVE with no caveats on critical dimensions?** YES — S9 (with default skopos refinement) survives clean on D1, D4, D7, D8 (all critical-weight). The Emergent Assembly also survives clean. The MVF sub-assembly also survives clean.
- **Would two consecutive iterations produce candidates landing in new regions?** UNLIKELY. The candidate set is broad (9 individual + 1 assembly + 1 sub-assembly + 1 critique-elevated = 12 evaluated); innovation applied all 7 mechanisms with full variation coverage; the Inherited Frame Audit did not fire. Additional iterations would likely land in already-mapped regions.
- **Are unexplored regions topologically likely to contain viable candidates?** NO. The unexplored regions are either out-of-scope (prompt-engineering) or adjacent to already-mapped viable regions (collaboration patterns, source-text-pre-analysis as variants of S9's territory).
- **Accumulator shows decreasing rate of new information per iteration?** YES — innovation reported convergence with ≥3 mechanisms pointing at the failure-mode-catalog-first-class restructuring; critique confirmed via 12 candidates with consistent landscape positions.

**All convergence criteria met.**

### Signal: TERMINATE

Coverage sufficient. Convergence reached. Clean SURVIVE exists. Ranked survivors below.

---

## Ranked Survivors

| Rank | Candidate | Verdict | Position | Causal layer(s) addressed |
|---|---|---|---|---|
| 1 | **Emergent Assembly** (P1 + S9 + S10 + S8 + P2-principal + S4+S5 + S2-refined) | SURVIVE | Central viable region | All 4 layers |
| 2 | **MVF Sub-Assembly** (S9 + S10 + S8 + P2-principal) | SURVIVE | Viable region (minimum-viable) | PROXIMATE + STRUCTURAL + ARCHITECTURAL (narrative form) |
| 3 | **S9 — Skopos / audience-spec rule** | SURVIVE | Viable region | PROXIMATE |
| 4 | **S8 — Documented-failure-trace practice** | SURVIVE | Viable region | ARCHITECTURAL (lightweight) |
| 5 | **S4 + S5 — Multi-axis harmony report** | SURVIVE | Viable region | STRUCTURAL |
| 6 | **S10 — Polysemy disambiguation principle** | SURVIVE | Viable region | PROXIMATE (polysemy) |
| 7 | **P1 — Diagnosis communication** | SURVIVE | Viable region | (the inquiry's deliverable) |
| 8 | **P2-principal — Register tier fix** | SURVIVE (re-evaluated; component of MVF and Emergent Assembly) | Viable region | STRUCTURAL |
| 9 | **S2 — Berman seed (refined)** | REFINE → conditional SURVIVE | Boundary → viable after refinement | META |
| 10 | **S1 — Rules-with-violations (scope-restricted)** | REFINE | Boundary | META (long-term) |
| 11 | **S6 — Memory→spec architecture** | DEFERRED with revival trigger | Boundary (timing-blocked) | ARCHITECTURAL (full) |
| 12 | **S7 — Tier-system replacement** | RESEARCH FRONTIER | Unexplored long-term | STRUCTURAL (root-level) |

**No KILLs.** Every candidate either SURVIVEs, REFINEs to a viable form, or DEFERS to a revival trigger.

---

## Constructive Output Summary

**For the user:**

The diagnosis answers the original question (P1). The fix-program is multi-layered with clear ordering. Two user-choice paths:

**Path A — Minimum Viable Fix (~2-4 hours):** S9 + S10 + S8 + P2-principal. Catches the documented failures, prevents recurrence at the trigger layer, fixes the structural mis-classification, documents the failure as a calibration entry. Drops the META-layer fix and the full audit restructure; can be added later.

**Path B — Emergent Assembly (~1-2 days):** All of Path A + S4+S5 (audit restructure) + S2-refined (failure-modes catalog seeded by filtered Berman + AI-specific entries). Achieves the diagnostic-first framework with documented calibration; addresses all 4 causal layers; the framework becomes a learning system in narrative form.

**Future research:**
- S6 (architectural memory→spec ingestion): revival trigger = ≥3 additional translation failures diagnosed via separate inquiries.
- S7 (tier-system replacement): research frontier when catalog matures.
- S1 wholesale (rules-with-violations across all entries): research frontier; scope-restricted application proceeds now via S2.

---

## Convergence Telemetry

- **Dimension coverage:** 8 dimensions (6 default + 2 project-specific risk per Phase 0 refinement). All relevant; all discriminate (different candidates score differently per dimension). Weights assigned per stake level.
- **Adversarial strength:** STRONG. Every candidate received both prosecution and defense. Multi-axis prosecution applied where relevant (user-perspective objections, specific failure-case scenarios, specification-gap probes). Several candidates went to REFINE rather than easy SURVIVE; one (S6) deferred; one (S7) parked as RESEARCH FRONTIER. No easy passes.
- **Landscape stability:** STABLE. The 12 evaluated candidates cluster into 5 regions: viable (8 candidates), boundary-to-viable-via-refinement (2), boundary-deferred (1 — S6), unexplored-long-term (1 — S7). New candidates from an additional iteration would likely land in already-mapped regions.
- **Clean SURVIVE exists:** YES. S9 (with default skopos), S8, S10, P2-principal, the MVF sub-assembly, and the Emergent Assembly all survive clean on all critical-weight dimensions.
- **Failure modes observed:**
  - Wrong Dimensions: NO (dimensions extracted from sensemaking; project-specific axes included).
  - Rubber-stamping: NO (multiple REFINE verdicts; defense did not pass everything).
  - Nitpicking: NO (multiple SURVIVES; defense applied to every candidate; severity-weighted dimensions).
  - Dimension Blindness: NO (cross-referenced sensemaking perspectives; project-specific risk axes covered).
  - False Convergence: NO (convergence reached with clean SURVIVE present; ≥3 SURVIVE candidates).
  - Evaluation Drift: NO (same dimensions used across all candidates).
  - Self-Reference Collapse: NO (external grounding via empirical failure traces + translation-studies tradition).

### Overall verdict: **PROCEED**

All gates passed. Termination signal valid. Output ranked survivors with constructive direction.
