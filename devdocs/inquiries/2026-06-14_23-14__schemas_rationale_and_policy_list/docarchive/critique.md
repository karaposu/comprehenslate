# Critique — schemas_rationale_and_policy_list

## User Input

```text
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/_branch.md

Upstream outputs in same folder: articulate_simple.md + surfacing.md + sensemaking.md + decomposition.md + innovation.md. Innovation's 6 principal candidates (PC1-PC6) + 1 Assembly emergent (AE1) are the candidates to evaluate.

The inquiry's Synthesis Trigger names 3 prior findings that are being corrected — Critique must adversarially test whether the INVALID verdicts in PC4 are sound (could they be too aggressive?) and whether the alternative-shape rejections in PC5 are honest (or did they get easy treatment because they're inversion-candidates rather than principal candidates?).

Save critique output to: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-14_23-14__schemas_rationale_and_policy_list/critique.md
```

---

## Phase 0 — Dimension Construction

### Extracted from sensemaking + decomposition substrate

Load-bearing principles, constraints, and meaning-nodes that ground the dimensions:

- FP2 — *Don't declare what the LLM can infer.*
- FP1 frame-revised — *Schema ownership matches data ownership.*
- C1 — TC is frozen (8 axes, unchanged).
- C2 — SourceDescriptor is dropped.
- C6 — Language-agnosticism applies cross-policy.
- MN1 — Authorial edge-case as structural category.
- The user-stated concern from the inquiry framing: PC4's INVALID verdicts adversarially tested; PC5's alternative-shape rejections honesty-tested.

### Dimensions

| # | Dimension | Weight | Source | Success criteria |
|---|---|---|---|---|
| D1 | **FP2 Conformance** | CRITICAL | SV6 stabilized model | Substance-level: no candidate proposes schema content for LLM-inferable facts; FP2 applied consistently per case |
| D2 | **TC-Frozen Conformance** | CRITICAL | C1 + user explicit | External-anchor (`translation_config.py` + schemas.py): no candidate adds fields to TranslationConfig |
| D3 | **Frame-Premise: FP2 itself** | CRITICAL | Frame-premise refinement (test inherited frame) | What-if-wrong probe: does FP2 survive its own inversion? |
| D4 | **User-Pushback Fidelity** | HIGH | Session-transcript quotes (external anchor) | Each candidate aligns with the user's verbatim corrections; quotes match |
| D5 | **Language-Agnosticism** | HIGH | C6 | Substance-level: every Policy enum literal is tradition-free, language-free |
| D6 | **Authorial-Edge-Case Category** | HIGH | MN1 | Substance-level: every strong-candidate Policy governs an authorial edge-case (not translator / publication / reader-side) |
| D7 | **Frame-Premise: INVALID verdicts** | HIGH | User-stated inquiry concern | Each INVALID verdict in PC4 cites structural evidence (not precedent alone); could-be-RE-TESTED-instead probe runs |
| D8 | **Alternative-Shape Honesty (PC5)** | HIGH | User-stated inquiry concern | Strongest case for each rejected alternative shape is constructed; rejection survives the strengthened case |
| D9 | **Correction-Propagation Reach** | HIGH | Project-specific risk (3 priors named) | Each impacted prior gets explicit Correction Notice; no silent inheritance possible |
| D10 | **Anti-Bloat** | HIGH | FP3 + recurring user preference | Candidate set size reasonable; deferrals carry revival triggers |
| D11 | **Correctness** | HIGH | Default | Candidates answer the two items the inquiry framed |
| D12 | **Coherence** | HIGH | Default | Candidates compose with existing schemas.py and project state |
| D13 | **Calibration-State Awareness** | MED | Sensemaking Phase/Calibration-State perspective | Calibration-dependence on current-LLM-capability is acknowledged |
| D14 | **Frame-Premise: Policy-as-layer** | MED | Frame-premise refinement | Tests whether "Policy" is a structurally distinct schema-kind, not a naming pattern |

### Dimension validation

Cross-reference against sensemaking's perspectives:
- Technical/Logical → D1 + D11
- Human/User → D4
- Strategic → D9 + D10
- Risk → D9
- Resource → D10
- Definitional/Internal Consistency → D1 + D5 + D6
- Definitional/Frame-exit → D3 + D7 + D14
- Phase/Calibration-State → D13

All upstream perspectives covered. **Dimension Blindness check: NOT FIRED.**

### Frame-premise test (per refinement note)

Load-bearing premises of the inherited frame:

1. **FP2 is a sound principle (not tautological with FP1).** What-if-wrong: if FP2 is just a restatement of FP1, the architecture collapses to the chunking_deep_dive's prior 3-schema design. Counter-evidence to look for: a candidate field where FP1 alone (without FP2) generates the right schema decision. → Probed at D3.

2. **The 3-layer architecture (TC / Policy / PC) is structurally distinct, not a naming pattern.** What-if-wrong: if Policy is just "small TC fields with smaller scope," then the right answer is to add the 6 strong candidates' fields to TC, not a separate Policy layer. Counter-evidence: D14 probes this.

3. **The Inherited Commitments Re-test verdicts are sound, not over-aggressive.** What-if-wrong: the INVALID verdicts on prior commitments could be too strong; the priors' commitments might be RE-TESTED-with-frame-revised (preserved) instead. → Probed at D7 (specifically per user-stated concern).

### External-anchor dimension requirement

External anchors available:
- User's verbatim corrections in the session — applies to D4.
- `translation_config.py` (the empirical pre-existing artifact) — applies to D2.
- `schemas.py` (the empirical current artifact) — applies to D1 and D14.
- The 3 prior findings (canonical source text) — applies to D7.

External-anchor criteria fire at D2, D4, D7. Non-internal-consistency claims are externally grounded.

### Failure-mode checks at Phase 0

- **#1 Wrong Dimensions:** NOT FIRED — dimensions derived from sensemaking output, weights match purpose-fitness.
- **#4 Dimension Blindness:** NOT FIRED — all upstream perspectives have at least one dimension.
- **#8 Axis Absence:** NOT FIRED — user-stated concerns (D7 + D8) are explicit dimensions; failure axes from upstream covered.

---

## Phase 1 — Fitness Landscape

- **Viable region:** candidates that pass all CRITICAL (D1, D2, D3) and HIGH dimensions with at most 1 minor caveat.
- **Dead region:** candidates that fail D1 (FP2 conformance) or D2 (TC-frozen) or D3 (FP2 itself fails inversion test). Also dead: candidates that contradict User-Pushback Fidelity (D4) on a load-bearing user quote.
- **Boundary region:** candidates that pass CRITICAL but have caveats on HIGH dimensions (e.g., Language-Agnosticism partial on a moderate Policy candidate).
- **Unexplored region:** cross-corpus Policy candidates (PC6 flags this as Research Frontier — not unexplored in the unflagged sense; just explicitly out of scope this inquiry).

---

## Phase 2 — Adversarial Evaluation

### PC1 — Conceptual substrate (FP2 + 3-layer architecture + 4 filters)

**Prosecution:**

- **D3 Frame-Premise (FP2 itself):** Is FP2 actually new, or is it tautological with FP1? Construct the strongest case: *"Don't declare what the LLM can infer"* could be read as just *"schemas should hold useful information"* — the FP1 statement of schema-ownership already captures this. Counter to this: FP1 doesn't supply the operational predicate "can the LLM derive this?" — FP1 leaves "useful information" unspecified. FP2 narrows the definition concretely, identifying LLM-inference as the test. The substance test: apply FP1 alone to `source_language` → ambiguous (depends on what counts as "data the schema owns"). Apply FP1 + FP2 → `source_language` is LLM-inferable → drop. The FP2 contribution is non-trivial. **PASSES D3.**
- **D4 User-Pushback Fidelity:** PC1 quotes the user's verbatim correction ("*we dont need SourceDescriptor*"). Quote matches session transcript. **PASSES D4.**
- **D1 FP2 Conformance (substance-axis):** Self-application — does FP2's text itself belong in `schemas.py`? No — it's a developer-facing rule. Self-application is consistent (FP2 isn't proposing itself as a schema field). **PASSES D1.**
- **D14 Frame-Premise (Policy-as-layer):** Is Policy structurally distinct from TC? The architecture table shows distinct decision-axis / defaults-driver / consumer per layer. Substance check: can a candidate Policy class be re-routed to TC without loss? Test on NonMainLangPartsPolicy: if added to TC as `non_main_lang_handling: Literal[...]`, TC grows to 9 axes (violates C1 / D2). The structural distinction is enforced by C1's TC-frozen constraint. **PASSES D14.**
- **Multi-axis (specification-gap):** the LLM-inferable test predicate is named operationally — *"at integration time, ask: 'Can the LLM derive this value from the source text plus the rest of the config?'"* Not left implicit. **PASSES.**

**Defense:** PC1 is the load-bearing conceptual substrate; multiple downstream pieces inherit from it. The 4-filter set operationalizes FP2 for the Item 2 catalog. The architecture table makes the 3-layer split concrete.

**Collision:** Defense holds. No critical-weight failure.

**Verdict: SURVIVE.** No caveats.

---

### PC2 — Item 1 rationale narrative

**Prosecution:**

- **D11 Correctness:** Does the narrative answer "why does schemas.py make more sense"? Yes — it applies FP2 to each dropped class and shows architectural before/after.
- **D4 User-Pushback Fidelity:** Each user correction is quoted. **PASSES D4.**
- **Multi-axis (substance-axis, FP2 application consistency):** Apply FP2 verbatim to each dropped class in the narrative:
  - SD drop: FP2 test → can LLM derive source_language? Yes → drop. ✓ Consistent application.
  - per-language EmbeddedLanguage drop: FP2 test → can LLM derive embedded-language detection? Yes → drop. ✓ Consistent.
  - `chunking_granularity` off TC: this isn't a pure FP2 application — it's TC-frozen (C1) plus an architectural reclassification (chunking as operational, not strategic). The narrative blends two principles. **CAVEAT: the narrative would be cleaner if it separated FP2 applications (SD, EmbeddedLanguage) from C1-and-architectural applications (chunking_granularity move).**
  - `canonical_level` drop: FP2 test → can LLM derive corpus hierarchy? Mostly yes for clear corpora; ambiguous for atypical structures. Plus user explicit rejection of universal hierarchy. The drop is over-determined (FP2 + user-quote + structural fit). Narrative correctly cites the user-quote primarily. ✓
- **Multi-axis (specific failure case):** what if a reader doesn't know the 4-schema design? CAVEAT: narrative is finding-internal; finding template supplies surrounding context, so this is bounded.

**Defense:** The narrative has principle-anchor (FP2), citation discipline (user-quotes), and architectural contrast (before/after). It addresses the rationale at the right level.

**Collision:** The caveat (blended principles at `chunking_granularity` move) is minor. Defense survives prosecution.

**Verdict: SURVIVE with CAVEAT.** Constructive output: when writing the finding's Item 1 section, separate the "FP2 application" sub-section from the "C1 + architectural reclassification" sub-section when explaining chunking_granularity's move.

---

### PC3 — Item 2 Policy-list catalog

**Prosecution (per-candidate substance-axis on D5 + D6):**

| Candidate | Filter substance-test | Verdict |
|---|---|---|
| `SourceApparatusPolicy` | All 4 filters pass on substance. "preserve-as-source-channel" literal slightly opaque. | SURVIVE-with-minor-CAVEAT |
| `VoiceMarkingPolicy` | All 4 pass. "implicit-typographic" default carries convention-dependence. | SURVIVE |
| `ArchaicRegisterPolicy` | All 4 pass. Carries homeless `source_temporal_register` field. Overlap with #9 AnachronismHandlingPolicy. | SURVIVE-with-CAVEAT |
| `HonorificsPolicy` | Substance probe on "preserve-original-script" — does this leak language? No: "original-script" is structural (whichever script the source uses), not "Arabic-script." Language-agnostic. | SURVIVE |
| `FormulaicOpeningPolicy` | All 4 pass. CAVEAT: formulaic openings are often in non-main language (Bismillah in Arabic-embedded-in-Turkish). Co-application with NonMainLangPartsPolicy is functional, not conflicting — both apply to their concern (opening-handling vs language-handling). | SURVIVE-with-CAVEAT |
| `EmbeddedPoetryPolicy` | Similar co-application caveat as FormulaicOpening. | SURVIVE-with-CAVEAT |
| `TransliterationStandardPolicy` (moderate) | Authorial PARTIAL acknowledged (transliteration is partly translator-side). | SURVIVE-as-moderate |
| `PriorTranslationStancePolicy` (moderate) | list[PriorRef] companion structure breaks pure shape; caveat acknowledged. | SURVIVE-as-moderate |
| `AnachronismHandlingPolicy` (moderate) | Overlap with ArchaicRegister acknowledged. | SURVIVE-as-moderate |
| `CitationReferenceFormatPolicy` (moderate) | Use-case narrow; caveat acknowledged. | SURVIVE-as-moderate |
| ScriptDirectionPolicy (deferred) | Surface-rendering not authorial — defer reason structurally correct. | DEFER (sustained) |
| PassageTypologyPolicy (deferred) | Not policy-shaped (typology label, not strategy) — structurally correct. | DEFER (sustained) |
| Consumption/Reading policies (deferred) | Reader-side, not authorial — correct. | DEFER (sustained) |
| OutputFinalityPolicy (deferred) | Pipeline-side — correct. | DEFER (sustained) |
| RelayTranslationPolicy (deferred) | Chain structure breaks shape; current scope is direct — correct. | DEFER (sustained) |

**Multi-axis (user-perspective objection):** Does the catalog's size violate Anti-Bloat (D10)? 6 strong + 4 moderate + 5 deferred = 15 entries. But strong candidates are the immediate adoption targets (~6 classes alongside NonMainLangPartsPolicy). User's anti-bloat preference is on what gets ADOPTED, not on what gets CATALOGED with reasoning. The deferred entries are protective documentation (revival triggers prevent re-litigation). **PASSES D10.**

**Multi-axis (specification-gap):** Co-application of Policy classes (NonMainLangParts + FormulaicOpening on Bismillah; NonMainLangParts + EmbeddedPoetry on Mevlana couplet) — how does the AI know which precedence to apply? Both apply to their respective concern (the Bismillah is BOTH a formulaic opening AND non-main-language; both policies' values can be honored simultaneously without conflict). The caveat surfaces at PC6 as a Refinement Trigger candidate. **PARTIAL — needs a note in the catalog intro.**

**Defense:** 15 candidates with concrete pydantic sketches for strong; per-candidate filter verdicts; revival triggers per defer. The catalog is principle-anchored (4 filters applied per row) and operationally complete.

**Collision:** No KILL; multiple minor CAVEATs about co-application boundaries. Constructive output: brief note in the catalog intro acknowledging co-application — Policy classes are independent of each other; the same source text span can be governed by multiple Policy classes simultaneously (each addressing its own concern).

**Verdict: SURVIVE with CAVEAT.** Constructive output: in the finding's Item 2 section intro, add one sentence: *"Policy classes co-apply per text span — a Bismillah is both a formulaic opening (governed by `FormulaicOpeningPolicy`) and a non-main-language phrase (governed by `NonMainLangPartsPolicy`); both policies' values apply to their respective concerns without conflict."*

---

### PC4 — Inherited Commitments Re-test (user-flagged concern: are INVALID verdicts too aggressive?)

**Prosecution targeting the user-stated concern:**

For each INVALID verdict, construct the strongest case for "this should be RE-TESTED-with-frame-revised (preserved) instead" and test it:

**INVALID-1: `chunking_granularity: Literal[5]` on TC.**
- Strongest case for preservation: TC.chunking_granularity could be preserved if "chunking_granularity is a strategic choice (TC) when the user picks granularity per job, and operational (PC) when the operator tunes it" — i.e., the field could live on both layers with sub-meanings.
- Counter: this would violate C1 (TC frozen) AND duplicate the field. The user's *"translation_config is good as it is"* makes C1 a hard constraint. Dual-placement also violates Anti-Bloat (D10). INVALID survives the strengthened preservation case.

**INVALID-2: SD.ChunkingUnit `canonical_level`.**
- Strongest case for preservation: SD could be re-introduced ONLY for corpora with clear hierarchical structure (Nursi, Quran, Bible) and dropped for corpora without (Tanakh narrative; haiku). The field becomes corpus-conditional.
- Counter: this re-introduces SD, contradicting C2 (user explicit drop). Plus the corpus-conditional shape is itself the hierarchy-imposition problem the user rejected — *"book must follow certain chapter rules. which is not the case"*. INVALID survives.

**INVALID-3: Corpus mappings as schema content.**
- Strongest case for preservation: mappings could be preserved if SD is preserved.
- Counter: SD is dropped (C2). Mappings can live as documentation (chunking_deep_dive finding body + new finding application examples) — they're preserved as concept, just not as schema field values. The INVALID verdict is precisely "INVALID at schema location" (not "INVALID as concept"). Verdict's scope is honest.

**External-anchor sub-axis (D4 + D7):** Each verdict cites structural evidence:
- INVALID-1 cites "chunking granularity is operational, not strategic" — structural.
- INVALID-2 cites "imposes universal hierarchy not present in all corpora" + user verbatim quote — structural + externally anchored.
- INVALID-3 cites "useful as docs but not schema content" — structural plus FP2 application.

None of the INVALID verdicts rest on precedent alone. **PASSES D7.**

**Multi-axis (specific failure case):** what if a future inquiry needs the corpus mappings as schema content? Counter: the mappings remain accessible in the chunking_deep_dive finding's body (which stands as historical record) and in the new finding's application examples. Not lost.

**Defense:** Each INVALID has structural grounding; user-pushback fidelity is verified by quote-matching; the strongest preservation cases were constructed and failed against C1/C2 plus structural contradictions with the current architecture.

**Collision:** The INVALID verdicts survive the strengthened-prosecution case. The user-stated concern is honestly addressed — the verdicts are NOT too aggressive.

**Verdict: SURVIVE.** No caveats. The user-stated concern is dismissed on substance.

---

### PC5 — Next Actions (user-flagged concern: are alternative-shape rejections honest?)

**Prosecution targeting the user-stated concern:**

PC5 commits ADD-CONTENT (Correction Notices) + REPAIR-on-priors (via Notice insertion at the top of each impacted finding). Innovation explored two alternative shapes (REORGANIZE-WITHOUT-ADDING; REPAIR-in-place) and rejected both. Are the rejections honest?

**Strengthen the REORGANIZE-WITHOUT-ADDING case:**

> *"Don't modify prior findings at all. The new finding's `corrects:` frontmatter plus `_state.md` Relationships at each prior signal the correction. The Comprehenslate project has a Relationships convention specifically for this. Findings are snapshots-of-thinking; modifying them — even with a clearly-marked Correction Notice — sets a precedent that future inquiries can also modify priors, eroding the snapshot convention. Visibility concern is overstated because the project's reading-pattern is via inquiry-index, not via search."*

Test:
- Does the project actually have a Relationships convention strong enough to handle this? Yes — `_state.md` Relationships field is the standard.
- Is the visibility concern overstated? Test: a future contributor (or even the current user 3 weeks from now) opening `chunk_types_vs_mechanisms/finding.md` directly (via grep for "SourceDescriptor", via direct path, via IDE jump-to-definition) would see the INVALID commitments without the Correction Notice. The Relationships-navigation chain (open finding → check related _state.md → read Relationships section → find SUPERSEDED BY → open the new finding) is three steps. The Correction Notice at the top of the finding is one step.
- Does the project's reading-pattern favor inquiry-index over direct path? Mixed — direct-path access is common when an inquiry references an artifact by path (e.g., this critique cites `devdocs/inquiries/2026-06-14_17-04__chunk_types_vs_mechanisms/finding.md` by path).
- Conclusion: visibility concern is real; REORGANIZE rejection is honest.

**Strengthen the REPAIR-in-place case:**

> *"Rewrite the INVALID sections of the priors directly. Original text moves to docarchive/ so historical access is preserved. Main path has no stale information. This produces definitively correct documents."*

Test:
- Is there a project precedent for REPAIR-in-place on findings? The chunk_types_vs_mechanisms inquiry (just one cycle ago) used docarchive/ for discipline outputs but kept finding.md intact. This is the precedent.
- Does findings-are-snapshots convention apply? Yes — findings document a moment of understanding. Rewriting them retroactively conflates current understanding with prior reasoning.
- Conclusion: REPAIR-in-place rejection is honest. The project's precedent supports keeping finding.md intact (with Correction Notice at top, not in-place rewrite).

**External-anchor sub-axis (D4):** PC5's correction-notice text is concrete and quotes structural evidence. The MUST actions identify specific file paths. No hand-waving.

**Multi-axis (specification-gap):** Does PC5 specify HOW the Correction Notice gets inserted (manual edit by next runner; via a tool)? It says "the runner of any subsequent inquiry" — observable gate, not specified mechanism. CAVEAT: minor; the user can manually insert or instruct a runner to do so. Not blocking.

**Defense:** PC5's intervention-shape commitment was tested against TWO alternative shapes per the Intervention-Shape-Axis Inversion rule. Both alternatives were strengthened and tested. Both rejections survive the strengthened cases. The user-stated concern about "easy treatment" is honestly addressed.

**Collision:** PC5's intervention-shape commitment is the load-bearing choice. No KILL or REFINE.

**Verdict: SURVIVE.** No caveats. The user-stated concern is dismissed on substance.

---

### PC6 — Open Questions

**Prosecution:**

- **Completeness:** are all open questions covered? The 3 PC6 surfaces (calibration-gate; cross-corpus; source_language_fluency revival) match Sensemaking's Open flags + Surfacing's R7 frontier. Missing: an open question about Policy-class co-application precedence (raised at PC3 prosecution). **PARTIAL — REFINE.**
- **Substance:** each open question has a revival/refinement trigger; D10 Anti-Bloat satisfied.

**Defense:** standard finding-template Open Questions; gates are observable.

**Collision:** Defense holds with one minor REFINE — add a fourth open question.

**Verdict: REFINE.** Constructive output: add a 4th Refinement Trigger to PC6: *"`PolicyCoApplicationPolicy` or precedence rules — if multiple Policy classes co-apply to the same source text span and produce ambiguous render outputs in actual translation work, document precedence rules (or evaluate whether the policies' value choices are independent on close inspection)."*

---

### AE1 — Assembly emergent (LLM-inferable test as project-wide rule)

**Prosecution:**

- **D14 Frame-Premise (Policy-as-layer):** Does FP2 generalize beyond schemas.py? Test: would FP2 apply to a hypothetical logging-config schema? Yes — "don't ask the user to declare what the LLM can infer from the system state" is a user-input principle, not schemas.py-specific.
- **Specific failure case:** if a future schema needs a borderline-LLM-inferable field, FP2 might over-restrict. Counter: FP2 is a rule of thumb with explicit cases-of-doubt handling — the integration-time predicate produces "no" decisions for clear LLM-inferable cases and goes to user judgment for borderline. Not absolute.
- **Multi-axis (specification-gap):** how does FP2 get adopted project-wide? Innovation's verdict was DEFERRED with revival trigger ("when project-wide schema-style guide is written or 3+ inquiries reference FP2 as load-bearing"). The deferral is appropriate — promotion gate is concrete.

**Defense:** AE1 is covered by PC5's COULD action (document the FP2 test predicate at module level). Promoting from schemas.py-specific to project-wide is a single-inquiry future task.

**Collision:** No KILL. DEFERRED status sustained.

**Verdict: DEFERRED (sustaining Innovation verdict).** Revival trigger remains as stated.

---

## Phase 3 — Verdict Summary + Constructive Output

| Candidate | Verdict | Constructive Output |
|---|---|---|
| **PC1** Conceptual substrate | SURVIVE | None |
| **PC2** Item 1 rationale narrative | SURVIVE-with-CAVEAT | Separate FP2-application from C1-and-architectural-reclassification when narrating `chunking_granularity` move |
| **PC3** Item 2 catalog | SURVIVE-with-CAVEAT | Add a brief intro sentence on Policy co-application (multiple policies can apply to the same text span; each governs its own concern) |
| **PC4** Inherited Commitments Re-test | SURVIVE | None — INVALID verdicts honestly survive strengthened-preservation prosecution |
| **PC5** Next Actions | SURVIVE | None — REORGANIZE-WITHOUT-ADDING and REPAIR-in-place rejections honestly survive strengthened cases |
| **PC6** Open Questions | REFINE | Add 4th Refinement Trigger: Policy-class co-application precedence rules if real-translation ambiguity surfaces |
| **AE1** Assembly emergent (FP2 project-wide) | DEFERRED | Revival trigger sustained from Innovation |

**Distribution:** 5 SURVIVE (2 with minor CAVEAT) + 1 REFINE + 1 DEFERRED. Zero KILLs.

### User-stated-concern resolution

1. **PC4 INVALID verdicts (concern: too aggressive?)** — Tested with strengthened-preservation prosecution. All three INVALID verdicts survived. Each cites structural evidence (FP2 + user-quote + architectural contradiction), not precedent alone. The user-stated concern is **dismissed on substance — verdicts are not too aggressive.**

2. **PC5 alternative-shape rejections (concern: easy treatment because they're inversion-candidates?)** — Tested with strengthened cases for both REORGANIZE-WITHOUT-ADDING and REPAIR-in-place. Both rejections survived. The strengthened cases brought project-precedent and reading-pattern arguments to bear; both were honestly answered. The user-stated concern is **dismissed on substance — rejections are honest, not easy.**

---

## Phase 3.5 — Assembly Check

Combining the SURVIVE / REFINE survivors, the finding holds together as: PC1 substrate → PC2 + PC3 application → PC4 + PC5 corrective reach → PC6 residuals. No new assembly emergent at Critique stage beyond AE1 (which was already raised at Innovation and sustained DEFERRED).

The minor CAVEATs (PC2 + PC3) and REFINE (PC6) are write-time refinements at finding production — no candidate needs to return to Innovation for re-generation.

---

## Phase 4 — Coverage + Convergence Assessment

### Coverage map

- **Per-candidate:** 14 dimensions evaluated per candidate (full adversarial coverage, given the finding has Synthesis Trigger + corrective reach).
- **Per-solution-space:** all 7 candidates (PC1-PC6 + AE1) positioned on the landscape. The fitness landscape shows a tight cluster in the viable region (5 SURVIVE) plus one boundary entry (PC6 REFINE) plus one deferred entry (AE1).

### Convergence

- At least one SURVIVE with no critical-dimension caveat: YES — PC1, PC4, PC5 are clean SURVIVE.
- Landscape stability: YES — single iteration produced stable positioning.
- Unexplored regions: cross-corpus Policy candidates (intentionally deferred via PC6 Research Frontier, not unexplored-in-the-failure sense).
- Accumulator: this is iteration 1; convergence is reached at this iteration.

### Mechanism-Independence Quarantine check

Do surviving candidates' evidence include ≥1 external-anchor sub-type?

- PC1: schemas.py (empirical artifact) ✓
- PC2: user verbatim quotes (canonical source text) ✓
- PC3: schemas.py + 14-edge-case innovation pass artifact ✓
- PC4: 3 prior findings (canonical source text) + user quotes ✓
- PC5: 3 prior finding paths (empirical artifact) + concrete notice text ✓
- PC6: Sensemaking + Surfacing artifacts ✓

**Quarantine NOT triggered.** All surviving candidates cite external anchors.

### Failure mode scan

| Mode | Status | Notes |
|---|---|---|
| #1 Wrong Dimensions | NOT FIRED | Dimensions extracted from sensemaking output and validated |
| #2 Rubber-Stamping | NOT FIRED | Each candidate received specific prosecution; the user-stated concerns generated their own dimensions (D7, D8); strengthened-prosecution cases applied at PC4 and PC5 |
| #3 Nitpicking | NOT FIRED | No KILL; the CAVEATs are minor and don't block SURVIVE |
| #4 Dimension Blindness | NOT FIRED | Cross-reference against sensemaking perspectives covered |
| #5 False Convergence | NOT FIRED | Multiple clean SURVIVE; landscape stable; coverage sufficient |
| #6 Evaluation Drift | N/A | Single iteration |
| #7 Self-Reference Collapse | NOT FIRED | Subject is schemas.py, not critique |
| #8 Axis Absence | NOT FIRED | User-stated concerns (D7, D8) explicitly dimensional |
| #9 External-Grounding Absence | NOT FIRED | All surviving candidates cite external anchors |

### Signal

**TERMINATE.** Coverage sufficient; convergence reached; 5 SURVIVE candidates ranked alongside 1 REFINE (light refinement) and 1 DEFERRED (revival-triggered). No iteration needed.

---

## Convergence Telemetry

- **Dimension coverage:** 14 dimensions, 6 default + 8 problem-specific (D2, D3, D4, D5, D6, D7, D8, D14)
- **Adversarial strength:** STRONG — user-stated concerns generated their own dimensions; strengthened-prosecution cases applied at PC4 and PC5; substance-axis prosecution applied per Phase 0 substance-criteria; external-anchor sub-axis fired at D2, D4, D7
- **Landscape stability:** STABLE
- **Clean SURVIVE exists:** YES (PC1, PC4, PC5 all clean; PC2 + PC3 SURVIVE with minor CAVEATs)
- **Failure modes observed:** NONE
- **Overall: PROCEED.**
