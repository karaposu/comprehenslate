# Innovation — translation_failure_root_cause_diagnosis

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-03_23-30__translation_failure_root_cause_diagnosis/_branch.md`

Inheritance from upstream: `surfacing.md` (60 items, 7 regions, central findings C-28/E-46/G-59), `sensemaking.md` (4-layer causal stack PROXIMATE→STRUCTURAL→META→ARCHITECTURAL; 5 added causes H1-H5), `decomposition.md` (10 pieces P1–P10; 3 strong-coupling clusters; 6-level critical path).

---

## Phase 1 — Seed

### Seed statement

**Seed:** What novel approaches exist for repairing the comprehenslate framework so that future translations don't reproduce the register pull-up and polysemy failures observed in `mytrasnlations/5th_word/eng.md`? The seed is a Gap + Dissatisfaction + Question composite: a gap (no failure-mode catalog in the framework), a dissatisfaction (the framework's tier system actively miscalibrates the relevant feature), and a question (what shape of intervention has the most leverage across the 4 causal layers + 10 piece-list?).

### Methodology-Mode Consideration

- **Inherited mode (from seed framing):** **Standard default** (4G + 3F balanced). Text signals: the seed is to "elaborate the committed direction" — decomposition has already produced a piece-list; innovation's job is to produce viable approaches for those pieces.
- **Alternative mode named:** **Contrarian-rethink** (Framer-weighted). Under this alternative, the seed would not be "how to repair the framework given the diagnosis" but "is the diagnosis itself the right frame? Should we question whether the framework should exist as a document at all?"
- **What follows under the alternative:** the candidate space would shift toward dissolving the framework into something else — embedding failure modes into the AI's prompt directly, or replacing the framework with a runtime test harness that runs after each translation, or abandoning the "principles + failure modes" split entirely for a different conceptual organization. The candidates would be fewer in number but more architecturally disruptive.
- **Decision:** **Default — proceed with Standard default mode.** Reasoning: sensemaking's 6-ambiguity adversarial pass already exercised contrarian framings (each ambiguity-collapse pair stated the strongest counter-interpretation on structural grounds; 5 of 6 resolved at HIGH confidence). Adding another contrarian-rethink layer would re-litigate settled adjudications. Standard default is appropriate. The contrarian voice is preserved within Standard default via Inversion mechanism + the Inherited Frame Audit + per-mechanism contrarian variations.
- **Compliance flag:** seed-time-methodology-mode considered; alternative named; default chosen with structural reason.

---

## Phase 2 — Generate

I'll apply all 7 mechanisms to the seed, producing variations (generic / focused / contrarian where applicable). Then apply Piece-Level Inversion at meta-decision pieces. Then run the Inherited Frame Audit before Phase 3.

### Mechanism 1 — Lens Shifting (Framer)

**Generic variation.** Shift the framing from "the framework documents principles for the translator to follow" to "the framework is a diagnostic instrument the translator runs against output." Under the original frame, register is sacrificeable because the translator's attention is on positive principles. Under the diagnostic-instrument frame, the framework's primary value is in what it can DETECT, not what it can DIRECT — and failure modes become the framework's primary content.

**Focused variation.** Shift from "C1 audience specifies vocabulary level" to "C1 audience specifies reader capability; vocabulary level is determined by source-register-fidelity." Same words ("C1 English speakers"), entirely different operational meaning. This is the proximate-trigger fix expressed as a lens shift.

**Contrarian variation.** Shift from "the framework lives in three docs" to "the framework lives partly in docs and partly in the AI's calibration state (memory + prompt)." Under this lens, the lesson-siloing finding (G-59) is reframed: the AI memory IS part of the framework, just an under-specified part. The architectural fix isn't "make memory flow to docs" but "make the AI-state portion of the framework first-class."

### Mechanism 2 — Combination (Generator)

**Generic variation.** Combine "principle-list" + "failure-modes catalog" → **rules-with-violations**: each principle is paired with at least one named failure mode that's its known violation pattern, so the doc reads both directions (positive + negative) per entry.

**Focused variation.** Combine "harmony report at file bottom" + "register audit" + "markedness audit" → **multi-axis harmony report**: the existing harmony report (which currently lists Tier 1 preservations + Tier 4 sacrifices) gets two new sections — Register Fidelity Audit and Markedness Audit — so the audit instrument itself is what surfaces the failures.

**Contrarian / native-domain variation.** Combine **Antoine Berman's "twelve deforming tendencies"** (an existing 12-entry failure-mode catalog FROM translation studies, c. 1985, that names "ennoblement" — register pull-up — as one of the twelve) with comprehenslate's harmony-tier system → **import Berman's tendencies as the seed for the failure-modes catalog**. Register pull-up is already known to translation studies; the framework's gap is in not having absorbed an established catalog. Cross-mechanism: this is also Domain Transfer (native-domain).

### Mechanism 3 — Inversion (Framer)

**Level-1 inversion.** "Framework documents principles" → "Framework documents failures." Component-level. Improvement but not structural.

**Level-2 inversion (depth-check applied).** "Framework's primary content is positive-principle-list" → "Framework's primary content is a failure-mode taxonomy; principles describe what 'absence-of-failure' looks like." System-level. This restructures the entire framework's primary organizing logic.

**Level-3 inversion (root-cause-level).** "Framework needs principles AND failure modes" → "The principle/failure-mode distinction is the wrong abstraction; both are patterns; the framework should organize by patterns, each with positive and negative readings on the same entry." This dissolves the distinction the user's sub-question hinted at — the user intuited that principles "should" count as failure modes; the level-3 inversion takes their intuition seriously.

**Multi-axis check.**
- *Existence-axis inversion:* what if the framework has ZERO documented principles and ONLY documented failure modes? Result: a minimal framework that's pure-diagnostic. The translator translates from their own training; the framework only catches mistakes. Surprisingly viable — and it matches how aviation checklists work.
- *Identity-axis inversion:* what is the framework FUNDAMENTALLY? Currently treated as "a document of how-to-translate guidance." Inverted identity: "the framework is the calibration record of a learning system." Under this identity, principles and failure modes are both calibration entries; the doc evolves with each translation.

**Three-variation grouping:**
- Generic: add failure-modes alongside principles (low-disruption Level 1)
- Focused: reorganize the framework's primary content around failure modes; principles describe absences (Level 2)
- Contrarian: dissolve the distinction; both are "patterns"; reorganize fundamentally (Level 3 + Multi-axis identity)

### Mechanism 4 — Constraint Manipulation (Framer)

**ADD-direction variations.**
- *Generic ADD:* "every principle must have at least one named failure mode paired with it." Forces the catalog to be authored alongside; eliminates the principle/failure-mode asymmetry the framework currently has.
- *Focused ADD:* "the harmony report at file-bottom must contain at least one entry per failure-mode category (or explicit 'not observed' for that category)." Forces the audit step to actually run all categories; prevents silent omission of register from the report (the E-46 finding).
- *Contrarian ADD:* "no translation is considered complete until ALL named failure modes have been actively scanned-for (passing or failing)." Forces failure-mode-catalog completeness to be a translation-completion gate. Heavy but structurally clean.

**REMOVE-direction variations.**
- *Generic REMOVE:* "remove the 4-tier ranking from `harmony_layer.md`; all features are equally meaning-bearing unless flagged otherwise." Eliminates the tier-misclassification problem at the root by removing the tier system itself. Loses the priority-conflict-resolution mechanism the tier system provides.
- *Focused REMOVE:* "remove the assumption that the framework is exhaustive; allow it to be incremental." This unlocks the architectural addition (memory→spec) by reducing the bar for what counts as a doc edit.
- *Contrarian REMOVE:* "remove the framework as a separate document; embed it directly into a translation skill the AI loads at start-of-task." Eliminates lesson-siloing by eliminating the lesson-vs-skill split.

**Bidirectional compliance:** both ADD and REMOVE directions covered above with 3 variations each.

### Mechanism 5 — Absence Recognition (Generator)

**Patch-level absences (gaps in current design).**
- A1: no register-matching principle in `notes.md`.
- A2: no markedness-matching principle.
- A3: no polysemy-disambiguation rule in `notes.md`.
- A4: no failure-mode entry for "register pull-up" anywhere in the framework.
- A5: no entry for "metaphor-momentum override" (polysemy failure).
- A6: no rule for interpreting audience-spec descriptors ("C1 English speakers," etc.).
- A7: no per-section register audit step in `harmony_layer.md`'s 3-pass process.
- A8: no `Tier 1 — register-as-alternation` entry in the tier system.
- A9: no cross-reference between `notes.md`'s principles and any failure-mode catalog (because the catalog doesn't exist).
- A10: no calibration-state property on the framework (no record of "what has this framework learned about?").

**Redesign-level absences (what would exist if designed from scratch).**
- R1: a failure-mode taxonomy would be a first-class structural component (per Inversion Level 2).
- R2: each entry (whether principle or failure mode) would have a paired positive/negative reading (per Inversion Level 3).
- R3: the framework would have an explicit calibration-state section listing failures it has absorbed.
- R4: the harmony-report instrument would be auto-generated from the failure-mode catalog (audit categories = catalog categories).
- R5: a feedback-ingestion-path would be specified architecturally (when AI memory accumulates ≥N entries of type T, propose a doc edit).

**Bidirectional check — what's already present in different form.**
- P1: the framework ALREADY does partial failure-mode flagging via the harmony report's "Tier 1 with partial transfer" and "Tier 4 sacrificed" entries. These are failure-mode-shaped but unnamed and uncatalogued.
- P2: `notes.md`'s last addendum ("dimensionally compressed terms") is ALREADY a strategy specification, not a principle. The framework HAS strategy-shaped content; it just hasn't been categorized.
- P3: `harmony_layer.md`'s ranking principle ("closer-to-meaning = higher priority") IS the logical seed of a failure-mode framework — "violating the ranking by demoting a meaning-carrier" is a failure pattern.
- P4: the harmony report at file-bottom is ALREADY an audit instrument. It just inherits its categories from the tier system, which is what makes it register-blind.
- P5: the AI's saved feedback memories ARE failure-mode entries in narrative form. The memory files have names, signatures, mechanisms, correctives — i.e., the catalog entry structure is already implicit in the memories themselves.

**Three-variation grouping:**
- Generic: fill patch-level absences (A1-A10) directly — straightforward gap-filling
- Focused: harvest the redesign-level absences (R1-R5) into a coordinated structural refactor
- Contrarian: recognize that the framework already has failure-mode content in latent form (P1-P5); the "absence" is one of EXPLICIT CATEGORIZATION, not of content. The fix is to recategorize and surface, not to author from scratch.

### Mechanism 6 — Domain Transfer (Generator)

**Native-domain source — Translation studies.**
- *Antoine Berman, "La traduction et la lettre, ou l'auberge du lointain" (1985):* twelve named "deforming tendencies" — rationalization, clarification, expansion, ennoblement (= register pull-up!), qualitative impoverishment, quantitative impoverishment, destruction of rhythms, destruction of underlying networks of signification, destruction of linguistic patternings, destruction of vernacular networks/exoticization, destruction of expressions/idioms, effacement of superimposition of languages. **Direct import:** comprehenslate's failure-mode catalog seed = Berman's twelve, named in English with worked translation-studies examples. Register pull-up (Berman's "ennoblement"), exoticization (Berman's "destruction of vernacular"), and several others are already named in translation studies' canonical literature.
- *Lawrence Venuti, "The Translator's Invisibility" (1995):* the "domestication / foreignization" dimension — register pull-up is a form of over-domestication when the target reader is mis-modeled. **Import:** the framework needs an explicit "target-domestication-level" parameter that the translator commits to.
- *Hans Vermeer, "Skopos theory":* every translation has a `skopos` (purpose) that determines methodology. The C1 misread is fundamentally a skopos-mis-specification: the user gave a target-audience-capability spec, the AI interpreted it as a target-register spec. **Import:** the framework needs explicit `skopos` adjudication at translation start.

**Cross-domain source — Software engineering.**
- *Code review checklist (e.g., Google's `eng-practices`):* explicit lists of named bug patterns, each with recognition signature + corrective. **Import:** failure-mode catalog as a code-review-style checklist.
- *Static analysis rule databases (e.g., ESLint rules, RuboCop cops):* each rule has a name, a recognized bad pattern, an explanation of why it's bad, a correct alternative. **Import:** entry structure for the catalog (name / signature / mechanism / corrective / example).

**Cross-domain source — Aviation safety.**
- *Checklist culture (Atul Gawande, "The Checklist Manifesto"):* simple, named, ordered, must-be-completed-before-action. Aviation has reduced certain accident classes 90%+ via checklists. **Import:** the harmony report becomes a mandatory pre-flight-style checklist; "did you check register?" is a checkable item.

**Cross-domain source — Medicine.**
- *Differential diagnosis:* given an observed failure, enumerate possible causes in order of likelihood, rule out by evidence. **Import:** the framework could include a "translation-failure differential" guide — given a flagged passage, what failure modes might have produced it?

**Three-variation grouping:**
- Generic: import code-review-style entry structure for the catalog (mechanism-agnostic)
- Focused: import Berman's twelve as the catalog seed (native-domain match; high specificity)
- Contrarian: import aviation checklist culture wholesale — mandatory pre-completion check with named items the translator MUST clear

### Mechanism 7 — Extrapolation (Generator)

**Short-term (1 year).** With current framework state (no failure modes, lessons siloed), every translation by an AI will repeat the same register pull-up class. The user will keep diagnosing per-translation failures. Number of AI-private feedback memories grows; framework documents stay static. Recurrence cost compounds.

**Medium-term (5 years).** AI translation tools will have absorbed ad-hoc failure-mode lists from their training data and from accumulated session memory. Frameworks like comprehenslate that DON'T explicitly name failure modes become bypass-able (the AI uses its own implicit catalog instead). Frameworks that DO explicitly name failure modes become reusable calibration layers across AI versions.

**Long-term (10 years).** Translation framework design converges on a structural pattern: explicit failure-mode taxonomies, audit instruments per failure mode, calibration-state records. The frameworks that survived are the ones that absorbed failure modes structurally; the frameworks that stayed as positive-principle lists became historical curiosities.

**Three-variation grouping:**
- Generic: trend continues without intervention → recurrence is permanent (status quo extrapolation)
- Focused: the AI memory siloing problem gets WORSE as memory architectures grow; intervening now is cheaper than intervening later (calibration-debt extrapolation)
- Contrarian: extrapolate the OPPOSITE — what if AI translation training catches register pull-up natively (because training data accumulates examples)? Then the framework's intervention may be obsoleted by training-side fixes. Counter to this contrarian: training-side fixes are slow, not user-controllable, and the framework gives the user agency NOW.

---

### Piece-Level Inversion at Meta-Decision Pieces

For each meta-decision piece from decomposition, apply Piece-Level Inversion (per the refinement note); for pieces firing property (v), use Intervention-Shape-Axis Inversion specifically.

**P2 (tier fix) — property (v): REPAIR shape.**
- Principal candidate: edit `harmony_layer.md` to split register into "register-as-style" (Tier 3) and "register-as-alternation" (Tier 1), OR upgrade register to Tier 1 with gating.
- *Intervention-shape Inversion:* alternative shape = **CONTRARIAN-RETHINK**. The tier system itself may be the wrong abstraction. What follows: replace tiers with a failure-mode-based prioritization (a feature gets attention if it has a named failure mode at the relevant severity). Tier 3 register fails this test (no register failure mode exists yet → no attention); after adding the register-pull-up failure mode, register gets attention by default. The tier system becomes obsolete.
- 5-test cycle:
  - Novelty: HIGH. The tier system is being replaced wholesale, not patched.
  - Scrutiny survival: counter — "the tier system also handles ranking when multiple Tier 1 features conflict; without it, what arbitrates?" Response: failure-mode-severity provides ranking via a different axis (high-severity failure mode wins over low-severity, regardless of feature). Counter survives but is less elegant.
  - Fertility: HIGH. Opens questions about severity calibration, multi-failure-mode features.
  - Actionability: MEDIUM. Requires more work than the REPAIR option.
  - Mechanism independence: convergent with Inversion Level 2 (system-level), Constraint REMOVE-direction (remove tier ranking), Combination (rules-with-violations).

**P3 (register + markedness principles) — property (v): ADD-CONTENT shape.**
- Principal candidate: author register-matching + markedness-matching principles for `notes.md`.
- *Intervention-shape Inversion:* alternative shape = **REORGANIZE-WITHOUT-ADDING**. What if the principles already exist in latent form (per Absence Recognition P3) and just need to be made explicit? Specifically: `harmony_layer.md`'s own ranking principle ALREADY implies register-matching (any meaning-bearing feature must be preserved). Rather than ADD a new principle, REORGANIZE `notes.md` to surface this implication. What follows: a shorter doc set; less duplication; risk that the implication is too indirect for the AI to act on.
- 5-test cycle:
  - Novelty: MEDIUM. Reorganization is less disruptive than addition.
  - Scrutiny survival: counter — "implications don't function the same way as explicit principles for AI behavior (per the cognitive-role argument in sensemaking)." This counter is structurally strong. Reorganization alone doesn't fix the principle-vs-failure-mode distinction.
  - Fertility: LOW. Doesn't open much.
  - Actionability: HIGH. Cheap.
  - Mechanism independence: only Absence Recognition direction "already-present-in-different-form" converges. Other mechanisms point to ADD-CONTENT.
- *Verdict:* REJECT the Inversion; keep principal ADD-CONTENT. The cognitive-role argument from sensemaking forecloses the reorganization-only path.

**P4 (polysemy principle) — property (v): ADD-CONTENT shape.**
- Principal candidate: author polysemy-disambiguation principle for `notes.md`.
- *Intervention-shape Inversion:* alternative shape = **DO-NOTHING**. The *nefer* case is one instance; polysemy mis-resolution is rare relative to register pull-up; the cost of adding may exceed the value. What follows: leave polysemy uncovered; rely on AI catching it case-by-case. Risk: more polysemy failures.
- 5-test cycle:
  - Novelty: LOW (DO-NOTHING is the trivial alternative).
  - Scrutiny survival: counter — "polysemy is not a rare failure type in Risale-i Nur translation specifically; the user is translating Said Nursi where Arabic-Turkish-Persian compound words with multiple senses are common." Counter strong. DO-NOTHING is not viable for this user.
  - Fertility: low.
  - Actionability: trivial.
- *Verdict:* REJECT the Inversion; keep ADD-CONTENT.

**P5 (failure-modes catalog) — property (c) lesson-vocabulary + property (v) ADD-CONTENT shape.**
- Principal candidate: structure + location + 5 initial entries for the catalog.
- *Intervention-shape Inversion:* alternative shape = **CONTRARIAN-RETHINK**. What if the catalog should not be static but dynamic — generated per-translation from the harmony report's failure flags? Each translation produces a "failure trace"; over time, the trace accumulates into the catalog. What follows: the catalog grows organically with use; no need to pre-author Berman's twelve; the cost is that early translations have no catalog to consult.
- 5-test cycle:
  - Novelty: HIGH (dynamic catalog is structurally different).
  - Scrutiny survival: counter — "this still requires SOMETHING (the harmony report) to know what to flag; the failure-mode names have to be authored somewhere for the report to use them. So a seed catalog is still needed; the dynamic part is the addition of new entries over time." Counter strong. The dynamic-only interpretation fails; the dynamic-plus-seed interpretation survives.
  - Fertility: HIGH. Opens the memory→spec architecture question.
  - Actionability: MEDIUM. Requires both the seed catalog AND the dynamic mechanism.
  - Mechanism independence: convergent with Constraint Manip ADD ("every translation must contribute one failure-trace entry"), Extrapolation (calibration-state grows), Absence Recognition redesign-level (calibration record as first-class).
- *Verdict:* the Inversion REFINES the principal: catalog = seed entries (static) + accumulation mechanism (dynamic) + memory→spec ingestion path (architectural).

**P7 (audit step) — property (v): ADD-DIMENSION shape.**
- Principal candidate: add a per-section register audit step to harmony_layer's 3-pass process.
- *Intervention-shape Inversion:* alternative shape = **REORGANIZE-WITHOUT-ADDING**. The existing harmony report at file-bottom IS the audit instrument. Rather than add a new pass, reorganize the existing report's required content so register is mandatory. What follows: no new pass; the existing instrument gains required-coverage rules.
- 5-test cycle:
  - Novelty: MEDIUM.
  - Scrutiny survival: counter — "the existing report runs AFTER translation; a per-section audit could run DURING translation. The timing differs." Response: the existing report is the post-hoc check; adding required content keeps the same timing but expands coverage. The pre-translation check (different timing) is a separate intervention that could be added on top. Both can coexist.
  - Fertility: HIGH. Reuses existing infrastructure.
  - Actionability: HIGH. Cheap restructure vs new pass.
  - Mechanism independence: convergent with Absence Recognition "already-present-in-different-form" (the report IS the audit), Combination "multi-axis harmony report."
- *Verdict:* REFINE the principal: the audit step is REORGANIZE-WITHOUT-ADDING applied to the harmony report's required content, not a new Pass 4.

**P8 (memory→spec architecture) — property (v): ADD-DIMENSION shape.**
- Principal candidate: design memory→spec ingestion architecture.
- *Intervention-shape Inversion:* alternative shape = **DO-NOTHING / DEFER**. The architectural cost is high; the immediate value uncertain; the doc fixes alone may handle known patterns. What follows: skip P8 entirely for this round; revisit when ≥N more failure types accumulate in AI memory.
- 5-test cycle:
  - Novelty: LOW (DEFER is the obvious alternative).
  - Scrutiny survival: counter — "if not pursued, the lesson-siloing pattern continues; framework cannot learn from FUTURE unknown failures." Response: this is true but the marginal cost is one inquiry per future failure (like this inquiry). Until volume grows, per-failure handling is cheaper than architectural investment. Counter survives partially: depends on the user's projected translation volume.
  - Fertility: LOW (DEFER opens nothing new now).
  - Actionability: HIGH. Trivial: skip.
  - Mechanism independence: convergent with Extrapolation contrarian variation ("training-side fixes may obsolete this").
- *Verdict:* The Inversion (DEFER) is structurally viable. **Both branches are valid alternatives the user can choose between.** Mark P8 as a user-decision point: pursue now OR defer with revival trigger.

**P10 (eng.md disposition) — property (b): framing-semantic.**
- Principal candidate: decide whether to leave `eng.md` as documented evidence vs rewrite.
- *Piece-level Inversion (content-axis, since property (b) not (v)):* assumption being reversed = "the eng.md is BAD output (failed translation)." Inverted assumption: the eng.md is GOOD diagnostic evidence (a documented failure trace). What follows: leaving it as-is has positive value beyond "we haven't fixed it yet"; it's an exhibit. Rewriting destroys the exhibit.
- 5-test cycle: Novelty MEDIUM. Survival: HIGH (reframes the disposition decision). Fertility: high (suggests a "documented failure traces" practice for the framework). Actionability: high. Mechanism independence: convergent with Combination ("AI memory + framework = system that learns from documented failures").
- *Verdict:* the Inversion REFINES the decision toward "leave as documented evidence; add a note framing it as such."

**Piece-Level Inversion compliance summary:**
- P2: satisfied (Intervention-shape Inversion generated, tested, refined principal)
- P3: satisfied (Inversion generated and rejected with structural reason)
- P4: satisfied (Inversion generated and rejected with structural reason)
- P5: satisfied (Inversion generated, refined principal)
- P7: satisfied (Inversion generated, refined principal)
- P8: satisfied (Inversion generated; both branches valid — user decision point)
- P10: satisfied (Inversion generated, refined principal)
- P1, P6, P9 not classified as meta-decision pieces firing property (v); P1 is property (b) framing-semantic but its "framing" is just communicating the diagnosis — Inversion-marked-inapplicable: P1's role is to communicate sensemaking's output verbatim, not to commit a frame the rest depends on at the framework level. P6 fires property (v) ADD-CONTENT; Inversion alternative = DO-NOTHING (rely on AI to interpret audience specs case-by-case). 5-test: Survival counter — "the C1 misread happened, will happen again without rule." Survives. REJECT Inversion; keep ADD-CONTENT. P9 is content-production (per the decomposition note); skip.

---

### Inherited Frame Audit

**Step (i) — Seed-level central assumption identification.** Reading the seed framing + upstream sensemaking + decomposition: the seed's strongest load-bearing belief is **"the comprehenslate framework documents are the right locus of intervention for preventing failure recurrence."** This is inherited from decomposition's piece-list (all 10 pieces target docs/process; none target alternative loci like prompt engineering, AI training, or runtime test harnesses).

A secondary central assumption: **"principles and failure modes are fundamentally different cognitive instruments."** Inherited from sensemaking's Ambiguity 2 resolution.

A tertiary central assumption: **"AI behavior is in-scope-via-trigger but out-of-scope as a direct target."** Inherited from sensemaking's Frame-exit Completeness verdict.

**Step (ii) — Piece-level load-bearing commitments.** Decomposition assigned intervention shapes to each meta-decision piece (P2: REPAIR; P3/P4/P5/P6: ADD-CONTENT; P7/P8: ADD-DIMENSION; P10: framing-semantic). The Piece-Level Inversion (above) has already challenged each shape commitment.

**Step (iii) — Challenge scan.** Examine the candidate set for explicit challenges to each assumption:

- **Seed-level assumption 1 (framework docs as locus):** Challenged by:
  - Lens Shifting contrarian variation: "framework lives partly in AI calibration state (memory + prompt)."
  - Constraint Manipulation contrarian REMOVE: "embed the framework directly into a translation skill the AI loads at start-of-task; eliminate the doc/skill split."
  - Domain Transfer (Vermeer skopos theory): the locus shifts to the AI's `skopos` interpretation step, not the doc.
  - Inversion contrarian (level 3): "the framework should organize by patterns, each with positive and negative readings on the same entry" — challenges the structure but not the doc-locus assumption directly. Partial only.
  - Extrapolation contrarian: "training-side fixes may obsolete framework-level intervention." Challenges the locus.
  - VERDICT: ≥3 candidates explicitly challenge the doc-locus assumption. Audit does NOT fire on assumption 1.

- **Seed-level assumption 2 (principle vs failure mode distinct):** Challenged by:
  - Inversion Level 3: "dissolve the distinction; both are patterns."
  - Combination generic variation: "rules-with-violations" merges them.
  - Absence Recognition contrarian (already-present-in-different-form): the framework already has failure-mode-shaped content (in the harmony report); the distinction is partly artifactual.
  - VERDICT: ≥3 candidates explicitly challenge. Audit does NOT fire on assumption 2.

- **Seed-level assumption 3 (AI behavior is in-scope-via-trigger only):** Challenged by:
  - Lens Shifting focused variation: "C1 misread is a skopos-mis-specification" — moves AI's interpretation step into scope as a directly-addressed target via the audience-spec rule (P6).
  - Lens Shifting contrarian: "framework lives partly in AI calibration state" — moves AI state directly into framework scope.
  - VERDICT: 2 candidates explicitly challenge. Audit does NOT fire on assumption 3 (≥1 challenge is the threshold).

**Step (iv) — Firing condition.** None of the seed-level assumptions have un-challenged status. **Audit does NOT fire.** No orchestration needed. Proceed directly to Phase 3 Test.

---

## Phase 3 — Test (5-test cycle on candidates worth testing)

Not every candidate needs full testing; the key survivors emerged through the mechanism work + piece-level Inversion. Testing the top survivors:

### S1 — "Rules-with-violations" reorganization (Combination + Inversion Level 3)

Each entry in the framework (whether currently a principle in `notes.md` or a failure mode in the new catalog) is restructured as a *pattern* with both positive and negative readings. The principle-vs-failure-mode distinction is preserved at the reading level (positive reading = principle; negative reading = failure mode) but the structural distinction at the doc level is dissolved.

- **Novelty:** HIGH. The framework's primary content-organization changes structurally.
- **Scrutiny survival:** Strongest counter — "this conflates two cognitive instruments that sensemaking established are distinct." Response: the distinction is preserved at the READING level (each entry has a positive reading the translator consults while doing + a negative reading the translator consults while auditing). The COGNITIVE ROLES are preserved; the STRUCTURAL ORGANIZATION unifies. Counter weakens. Survives.
- **Fertility:** HIGH. Opens questions about how to author entries, how to render them for different consumption modes (doing vs auditing).
- **Actionability:** MEDIUM. Requires authoring discipline; existing principles need conversion.
- **Mechanism independence:** convergent with Combination, Inversion Level 3, Absence Recognition contrarian. ROBUST.

**Disposition:** **ACTIONABLE (with refinement).** But: requires a doc-set restructure that exceeds the user's "cheap immediate fix" criterion. Better deployment: apply S1 to NEW entries (failure-mode catalog initial entries), leave existing principles unchanged, evolve over time. → **ACTIONABLE-INCREMENTAL**.

### S2 — Berman's twelve as catalog seed (Domain Transfer focused)

Import Antoine Berman's "twelve deforming tendencies" as the initial entries for the failure-modes catalog. "Ennoblement" = register pull-up; "exoticization" = transliteration over-application; "rationalization" / "clarification" — related to the AI's over-explanation tendency.

- **Novelty:** MEDIUM (the catalog is novel for this project; the catalog content is borrowed from established literature). Net: medium.
- **Scrutiny survival:** Strongest counter — "Berman's tendencies are designed for human translators; AI failure patterns may differ in important ways. Some of his twelve may not apply; some AI failures may not match any of his twelve." Response: ground-truth check — register pull-up (=ennoblement) DID match; metaphor-momentum override doesn't cleanly fit any of his twelve; markedness inversion partly fits "exoticization" but with reversed direction. Conclusion: import Berman's twelve as a SEED, then add AI-specific entries on top. Survives.
- **Fertility:** HIGH. Berman's framework has structure (he names mechanism, not just pattern); importing the mechanism-naming discipline raises the quality of new entries.
- **Actionability:** HIGH. Berman's twelve are already authored; project just needs to adapt them.
- **Mechanism independence:** convergent with Combination contrarian (cross-mechanism), Absence Recognition focused.

**Disposition:** **ACTIONABLE.**

### S3 — Skopos adjudication rule (Domain Transfer native, Lens Shifting focused)

At translation start, the framework requires the AI to commit to a `skopos` (purpose specification) — what the translation is for, who it serves, what register fidelity it commits to. The C1 misread becomes impossible because the AI is forced to make `skopos` explicit before translating.

- **Novelty:** HIGH. Skopos theory is established in translation studies but not in this project's framework.
- **Scrutiny survival:** Strongest counter — "this adds friction; the user already wrote 'C1 English speakers' as their skopos." Response: the C1 spec was ambiguous (capability vs vocabulary-level); the skopos adjudication is precisely about resolving such ambiguity. The friction is the value. Survives.
- **Fertility:** HIGH. Opens a whole skopos-handling layer in the framework.
- **Actionability:** MEDIUM. Requires authoring rule + worked examples.
- **Mechanism independence:** convergent with Lens Shifting focused, Domain Transfer native, the P6 piece-level work.

**Disposition:** **ACTIONABLE.**

### S4 — Reorganize-without-adding for P7 audit (P7 piece-level Inversion)

The per-section register audit doesn't need a new Pass 4. Reorganize the existing harmony report at file-bottom to require register coverage (and markedness coverage, and any catalog-defined coverage). The audit instrument already exists; expand its required content.

- **Novelty:** MEDIUM.
- **Scrutiny survival:** Strongest counter — "pre-translation audit (different timing) would catch failures earlier; post-hoc audit catches them after the work is done." Response: post-hoc audit + revision still costs less than a new pre-translation pass + the existing pass structure. The framework can later add pre-translation audit if post-hoc proves insufficient. Survives.
- **Fertility:** MEDIUM.
- **Actionability:** VERY HIGH. Cheapest viable structural fix.
- **Mechanism independence:** convergent with Absence Recognition "already-present-in-different-form," Combination focused.

**Disposition:** **ACTIONABLE.**

### S5 — Multi-axis harmony report (Combination focused)

Extend the harmony report's content from "Tier 1 preserved / Tier 1 partial / Tier 4 sacrificed" to add explicit sections: Register Fidelity Audit, Markedness Audit, Per-Section Comparison, Failure-Mode Scan. Each section is a required check.

- **Novelty:** MEDIUM.
- **Scrutiny survival:** counter — "longer report = more overhead per translation." Response: yes, but the overhead IS the value (it surfaces failures). Survives.
- **Fertility:** HIGH. Each section is extensible as new failure modes are named.
- **Actionability:** HIGH (paired with S4).
- **Mechanism independence:** convergent with S4, Absence Recognition redesign, Constraint Manipulation focused ADD.

**Disposition:** **ACTIONABLE.** Strongly couples with S4 (they're the same intervention from different angles).

### S6 — Memory→spec ingestion architecture (P8)

Design the architectural feedback loop so AI-extracted lessons flow back to docs.

- **Novelty:** HIGH for this project (architectural addition).
- **Scrutiny survival:** counter — "high engineering cost; uncertain marginal value for current translation volume." Response: cost-benefit is genuine. Survives but at MEDIUM confidence.
- **Fertility:** HIGH long-term.
- **Actionability:** MEDIUM (requires user buy-in on the engineering cost).
- **Mechanism independence:** convergent with Extrapolation, Absence Recognition redesign.

**Disposition:** **DEFERRED with revival trigger.** Revival trigger: when ≥3 additional translation failures have been diagnosed via ad-hoc inquiries, the marginal cost of one more inquiry > the architectural cost. Promote to ACTIONABLE.

### S7 — Tier-system replacement (P2 Intervention-Shape Inversion CONTRARIAN-RETHINK)

Replace harmony_layer.md's 4-tier ranking with failure-mode-severity prioritization.

- **Novelty:** HIGH.
- **Scrutiny survival:** Strongest counter — "the tier system also handles ranking when multiple Tier 1 features conflict; without it, what arbitrates?" Response: failure-mode-severity provides ranking via a different axis. Survives but introduces a new specification need (severity calibration).
- **Fertility:** HIGH (opens severity work) but ALSO HIGH RISK (breaks an existing structure that has SOME working parts).
- **Actionability:** LOWER than the P2 principal (REPAIR).
- **Mechanism independence:** convergent with Inversion Level 2, Constraint REMOVE-direction.

**Disposition:** **RESEARCH FRONTIER.** The contrarian rethink is structurally clean but the migration cost is high, and the principal REPAIR fixes the immediate failure. Park as a research direction the user can revisit.

### S8 — Documented-failure-trace practice (P10 Inversion)

Leave `eng.md` as documented failure evidence; add a brief note framing it as such; treat it as the framework's first calibration entry.

- **Novelty:** MEDIUM.
- **Scrutiny survival:** counter — "what if user just wants a clean translation?" Response: the user explicitly asked for a system-diagnostic, not a clean translation. Survives. (And if user later wants a clean translation, a fresh translation against the fixed framework provides one.)
- **Fertility:** HIGH (establishes the "documented failure traces" practice for the framework).
- **Actionability:** VERY HIGH. Lowest possible effort (one note added).
- **Mechanism independence:** convergent with Absence Recognition redesign (calibration record as first-class), Lens Shifting contrarian (framework lives partly in such artifacts).

**Disposition:** **ACTIONABLE.**

### S9 — Audience-spec interpretation rule (P6)

The audience-spec rule directly preventing C1-misread.

- **Novelty:** MEDIUM.
- **Scrutiny survival:** strong (no good counter; the misread was directly caused by absence of this rule).
- **Fertility:** MEDIUM (specific to audience-spec interpretation).
- **Actionability:** HIGH.
- **Mechanism independence:** convergent with Lens Shifting focused, Domain Transfer native (skopos), the P6 piece-level work.

**Disposition:** **ACTIONABLE.**

---

## Assembly Check

What architecture emerges when survivors are combined?

**Emergent architecture: "diagnostic-first framework with documented calibration."**

The combination of S2 (Berman seed) + S4 (audit-via-reorganize) + S5 (multi-axis harmony report) + S8 (documented failure traces) + S9 (skopos/audience rule) produces a coordinated transformation:

1. **Failure-mode catalog** seeded by Berman's twelve + AI-specific entries = the framework's diagnostic backbone (S2)
2. **Harmony report** restructured to require coverage of catalog categories per translation = the audit instrument (S4 + S5)
3. **Audience-spec / skopos rule** = the input-interpretation layer that prevents trigger events (S9)
4. **Documented failure traces** = the calibration record, with `eng.md` as the first entry (S8)

The emergent property: the framework becomes a **closed feedback loop in narrative form** — translations produce harmony reports; reports contain failure-mode scan results; failure-mode-positive translations become documented traces; traces feed future catalog entries. The architecture works WITHOUT S6 (the heavy memory→spec engineering) because the loop is human-authored rather than automated. S6 becomes an OPTIONAL optimization of an already-working loop.

This emergent architecture is more powerful than any single survivor and addresses all four causal layers from sensemaking:
- PROXIMATE → S9 (audience-spec rule)
- STRUCTURAL → S2 + S4 + S5 (catalog + audit + report)
- META → S2 (failure-mode catalog as first-class)
- ARCHITECTURAL → S8 (documented traces as the lightweight learning loop)

And it composes with S1 (rules-with-violations) for the long-term reorganization, and with S7 (tier-system replacement) deferred as research frontier.

**Assembly verdict: emergent architecture survives all 5 tests, dominates the individual-survivor space, and produces a coordinated multi-layer fix program.**

---

## Per-Row Mechanism Trace (Production-task Telemetry)

| Piece | Mechanisms applied | Axis (where property v fires) | Meta-decision classification | Piece-Level Inversion compliance |
|---|---|---|---|---|
| P1 | Lens Shifting:content | n/a | meta (b) framing-semantic | Inversion-marked-inapplicable: P1 communicates sensemaking verbatim; no frame the rest depends on |
| P2 | Inversion:intervention-shape, Constraint REMOVE:intervention-shape, Combination:content | intervention-shape | meta (v) | satisfied; CONTRARIAN-RETHINK Inversion generated and tested → REFINE principal toward S7 (parked as RESEARCH FRONTIER); principal REPAIR retained |
| P3 | Absence patch:content, Inversion:intervention-shape | intervention-shape | meta (v) | satisfied; REORGANIZE Inversion generated and rejected |
| P4 | Absence patch:content, Inversion:intervention-shape | intervention-shape | meta (v) | satisfied; DO-NOTHING Inversion generated and rejected |
| P5 | Domain Transfer:content, Combination:content, Inversion:intervention-shape, Extrapolation:content | intervention-shape | meta (c)+(v) | satisfied; CONTRARIAN dynamic-catalog Inversion REFINED principal (catalog = seed + accumulation + ingestion) |
| P6 | Lens Shifting:content, Domain Transfer:content, Inversion:intervention-shape | intervention-shape | meta (v) | satisfied; DO-NOTHING Inversion generated and rejected |
| P7 | Combination:content, Absence "already-present":content, Inversion:intervention-shape | intervention-shape | meta (v) | satisfied; REORGANIZE-WITHOUT-ADDING Inversion REFINED principal |
| P8 | Extrapolation:content, Inversion:intervention-shape | intervention-shape | meta (v) | satisfied; DEFER Inversion VALIDATED → user decision point (both branches viable) |
| P9 | n/a | n/a | content-production | n/a |
| P10 | Inversion:content | content | meta (b) | satisfied; documented-evidence Inversion REFINED principal |

---

## Mechanism Coverage Telemetry

- Generators applied: 4 / 4 (Combination ✓, Absence Recognition ✓ with both directions and both levels, Domain Transfer ✓ with native-domain source, Extrapolation ✓)
- Framers applied: 3 / 3 (Lens Shifting ✓, Constraint Manipulation ✓ with both ADD and REMOVE, Inversion ✓ with depth-check + multi-axis)
- Convergence: **YES — ≥3 mechanisms converge on the failure-mode-catalog-first-class restructuring** (Combination + Domain Transfer + Inversion Level 2 + Absence Recognition redesign-level + Extrapolation all point at this). HIGH confidence.
- Survivors tested: 9 / 9 (all S1–S9 received 5-test cycle)
- Failure modes observed: NONE
  - Premature evaluation: NO (mechanisms applied before testing)
  - Single-mechanism trap: NO (all 7 applied)
  - Early frame lock: NO (multiple variations per mechanism; Inversion went to Level 3)
  - Innovation without grounding: NO (every survivor tested + dispositioned)
  - Mechanism exhaustion: NO (≥7 survivors)
  - Survival bias: NO (uncomfortable outputs like S7 [tier-system replacement] and S6 [architectural] given fair test; S7 RESEARCH-FRONTIER'd not killed)
- Inherited Frame Audit: did NOT fire (all three central assumptions explicitly challenged by ≥1 candidate)
- Methodology-mode-consideration: compliant (inherited Standard default named; Contrarian-rethink alternative considered; default retained with reason)
- Piece-Level Inversion compliance: 10/10 pieces handled (7 satisfied; 3 inapplicable with structural reason)

### Overall verdict

**PROCEED.** All coverage gates passed. Convergence achieved. The emergent architecture from Assembly Check provides a coordinated multi-layer fix program that maps to all 4 causal layers from sensemaking. Ready for Critique stage.

### Disposition summary

| Candidate | Disposition |
|---|---|
| S1 — rules-with-violations | ACTIONABLE-INCREMENTAL (apply to new entries, evolve over time) |
| S2 — Berman's twelve as catalog seed | ACTIONABLE |
| S3 — skopos adjudication rule | ACTIONABLE (sub-component of S9) |
| S4 — reorganize-without-adding for P7 audit | ACTIONABLE |
| S5 — multi-axis harmony report | ACTIONABLE (couples with S4) |
| S6 — memory→spec ingestion architecture | DEFERRED with revival trigger (≥3 more failure inquiries → promote to ACTIONABLE) |
| S7 — tier-system replacement | RESEARCH FRONTIER |
| S8 — documented-failure-trace practice | ACTIONABLE |
| S9 — audience-spec / skopos rule (P6) | ACTIONABLE |
| Emergent assembly | ACTIONABLE as the recommended coordinated program |
