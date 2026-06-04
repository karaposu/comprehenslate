# Sensemaking — translation_failure_root_cause_diagnosis

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-03_23-30__translation_failure_root_cause_diagnosis/_branch.md`

Purpose: identify the root cause of the translation failures (register pull-up across 8+ words; *nefer* polysemy mis-resolution) and test three user-offered hypotheses (fault in docs / AI bulk behavior / absent failure-mode catalog).

Workspace inherited from `surfacing.md`: 60 items across 7 regions; central findings C-28 (Tier-3 misclassification), E-46 (harmony report register-blind), G-59 (lesson siloing); 4 frontier flags.

---

## SV1 — Baseline Understanding (pre-analysis)

The user invokes /MVLw to diagnose why the translation failed despite the comprehenslate framework being loaded and consulted. The initial impression: probably the documents had gaps the AI couldn't fill. Three named hypotheses — docs / AI-bulk / failure-modes — need to be tested, plus other causes that may emerge. The likely shape of the answer is "the docs are missing things X and Y." That's the working hypothesis going in; treat it as provisional.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **CON-1** The translation failures are real and documented (≥8 register pull-up instances; 1 polysemy mis-resolution).
- **CON-2** The framework docs (advanced_principles.md, notes.md, harmony_layer.md) were loaded and consulted before the translation.
- **CON-3** The failure pattern is consistent: always upward register direction, always in the parable-narrative section (not the high-theology section), always toward marked/archaic English equivalents.
- **CON-4** The text translated was short (~70 lines, ~9 paragraphs) — disconfirms volume-based "bulk translation" framing on its face.
- **CON-5** The framework predates the failure observations by ~2 months (mtime evidence); the docs cannot have been written with knowledge of these specific failure patterns.
- **CON-6** Lessons extracted post-failure live in `/Users/ns/.claude/projects/.../memory/` — separate location from the framework docs.

### Key Insights

- **KI-1** `harmony_layer.md` actively classifies "register consistency" as Tier 3 (sacrificeable) — see C-28. This is not an *absence* of guidance; it's an *active demotion* of the relevant feature.
- **KI-2** `harmony_layer.md`'s OWN ranking principle ("the closer a harmony component is to carrying meaning, the higher its priority") implies register-when-it-alternates should be Tier 1, because alternation IS meaning-carrying. The doc CONTRADICTS ITSELF on this case.
- **KI-3** The harmony report at the bottom of `eng.md` (E-46) has zero register-related entries — the framework's self-audit instrument is structurally blind to register failures because its tier system tells it not to look.
- **KI-4** "Register pull-up" is a *pattern* that emerges from the interaction of multiple individually-defensible choices: "use sophisticated vocabulary" + "preserve source meaning" + "C1 audience" → ornate English. No single principle in the docs predicts this combinatorial failure.
- **KI-5** The AI's interpretation of "C1 English speakers" as a license for elevated vocabulary (F-55, E-49) is the proximate trigger; without this misread, the register pull-up would not have fired with the same force.
- **KI-6** Both failures (register + polysemy) share a meta-cause: the framework lacks an explicit failure-mode catalog. Each failure has its own proximate trigger (C1-misread for register; metaphor-momentum for *nefer*) but the diagnostic capability to NAME these patterns before they fire is absent at the framework level.
- **KI-7** Lessons-saved-to-AI-memory (G-59) is an architectural property: the framework has no ingestion path for its own failures. The framework cannot LEARN from its own breakdowns; only the AI session memory learns, and only for the next session of the same agent.

### Structural Points

- **SP-1** Three doc layers in the framework: `advanced_principles.md` (worked examples), `notes.md` (~60 principles), `harmony_layer.md` (3-pass + 4-tier system). Roles: examples, vocabulary, operational priority.
- **SP-2** Three gap-classes across the docs: (a) no register-matching principle, (b) no polysemy-disambiguation principle, (c) no failure-mode catalog.
- **SP-3** The harmony report inside `eng.md` is intended as the self-audit instrument. Its content is determined by the tier system in `harmony_layer.md`. When the tier system misclassifies a feature, the audit can't see it.
- **SP-4** Memory-vs-docs split: AI-extracted lessons live at `/Users/ns/.claude/projects/...`; framework lives at `/Users/ns/Desktop/projects/comprehenslate/`. No flow between them.
- **SP-5** Two failure types — register pull-up (pattern-shaped, cross-many-words) and polysemy mis-resolution (single-word-sense-shaped). Different proximate causes, shared meta-cause.

### Foundational Principles

- **FP-1** Principles state what GOOD output looks like (prescriptive). Failure modes state what TYPICAL BAD output looks like (diagnostic). These engage different cognitive operations and are not substitutes.
- **FP-2** A framework that names failures explicitly enables a *diagnostic mode* of attention; a framework that names only positives leaves the operator in *prescriptive mode* throughout, missing pattern-recognition opportunities.
- **FP-3** A framework that doesn't ingest its own failures will repeat them. Learning systems need a feedback loop; static documents do not learn.
- **FP-4** External grounding is the corrective for self-reference blindness when a meta-discipline analyzes a sibling discipline.

### Meaning-Nodes

- **MN-1** "Register pull-up" — the central named pattern; the failure type.
- **MN-2** "Framework blindness" — the architectural property of the framework that allows a known pattern to pass unnamed.
- **MN-3** "Principle/failure-mode asymmetry" — the cognitive-role distinction the framework collapses.
- **MN-4** "Lesson siloing" — the architectural pattern where failures generate memory but not spec updates.
- **MN-5** "C1-misread" — the proximate trigger for the register pull-up; the audience-spec interpretation step the framework leaves under-specified.
- **MN-6** "Metaphor-momentum" — the proximate trigger for the polysemy mis-resolution; a second failure type the framework doesn't name.

### Meta-inspection after SV2 — H4 (concept names) and H5 (motivating examples)

- H4 check: "register pull-up," "framework blindness," "lesson siloing," "C1-misread," "metaphor-momentum" — are these real structural distinctions or convenient labels? Each is anchored in observable evidence (specific words in `eng.md`; specific sections in framework docs; specific filesystem layout). Concept-name commitments are taken forward with HIGH confidence.
- H5 check: the 8 register words + 1 polysemy word are the motivating examples. Specific-vs-pattern flag raised — addressed in Phase 3 below (Ambiguity 6).

### SV2 — Anchor-Informed Understanding

The shape sharpens: the failure is multi-layer. PROXIMATE layer = the AI's audience-spec interpretation step (C1-misread). STRUCTURAL layer = the docs' specific gaps PLUS one active mis-classification (register as Tier 3). META layer = the framework's choice to be a positive-principle list rather than including a failure-mode catalog. ARCHITECTURAL layer = the framework's lack of a feedback ingestion path. The user's three hypotheses correctly target the structural and meta layers but don't name the proximate trigger or the architectural pattern. The "bulk translation" hypothesis (H2) doesn't fit the size evidence (~70 lines is not bulk).

---

## Phase 2 — Perspective Checking

### Technical / Logical

The docs ARE missing specific principles — empirically observable in their absences (A-6, A-7, A-8, A-9, B-20, B-21, B-22, C-32, C-33, C-34). The harmony report's structural blindness (E-46) is a fact: the report has 0 register-related entries despite the failure happening in 8+ places. Logically: if the framework had a register-fidelity rule, the harmony report's Pass 2 (Harmony Map) would have surfaced register alternation as a Tier 1 feature; the AI would have known to preserve it in Pass 3. **New anchor:** the framework's process model has the right shape (3-pass), but the content of what gets mapped at Pass 2 is governed by the tier system, which misclassifies register.

### Human / User

The user's question carries a sub-question: "we have principles and how translation should be logic, they don't count as failure modes?" The user has an intuition that principles ARE somehow protective. **New anchor:** the user is partially right — principles imply negative consequences for ignoring them. But there's a real cognitive-role difference between prescriptive principles ("preserve word order") and diagnostic failure modes ("register pull-up: tendency to render plain folk-vocabulary with marked-English equivalents — corvée, cauldron, morsel, etc."). When DOING a task, the operator is in prescriptive mode (attention on what to achieve); a separate diagnostic pass is needed to scan for recurring failure patterns. The framework collapses this distinction.

### Strategic / Long-term

If lessons stay siloed in AI memory, the framework as the user reads it stays unchanged. Future translations by future sessions (or future AI versions) will repeat the same failures. **New anchor:** the framework's value as a document depends on its ability to encode learning. A document that doesn't update from feedback is a snapshot, not a system. The user's investment in writing principles is depreciated by the absence of a feedback ingestion path.

### Risk / Failure

- Risk A: Treating this as an isolated translation issue → patch this `eng.md`, lose the diagnostic.
- Risk B: Adding too many failure modes → framework becomes a checklist, loses generative power.
- Risk C: Over-correcting the docs without addressing the AI trigger → next misread (not C1, something else) produces a new failure type.
- Risk D: Building a memory-ingestion flow without testing whether it actually closes the loop.

**New anchor:** "the right fix" is not one fix; it's a coordinated multi-layer intervention with each layer doing its own job. Doc fixes catch known patterns; failure-mode catalog enables diagnostic mode; audience-spec interpretation rules catch trigger events; memory→spec flow catches unknown patterns over time.

### Resource / Feasibility

- Reclassifying register in `harmony_layer.md`: cheap (small edit to one file).
- Adding a failure-modes section: moderate (need to author the patterns; each pattern is ~½ page).
- Specifying audience-spec interpretation: cheap-to-moderate (one rule, but needs care).
- Memory→spec ingestion flow: high (architectural; requires both authoring discipline and tooling).

**New anchor:** the cheap fixes have high marginal value because they address documented failures with specific known correctives. The expensive fix (memory→spec) has high long-term value but isn't blocking. Sequencing matters.

### Ethical / Systemic

The user is treating their own framework as a system to improve — this is system-thinking, not blame-deflection. The AI must mirror this stance: the AI's own behavior IS part of the system; the diagnosis must include "the AI did X" without retreating into "I'm just an AI." **New anchor:** intellectually-honest diagnosis names the proximate trigger as AI-behavior even when that's uncomfortable. The framework can be fixed; the AI's behavior on the next session can be biased toward the right interpretation by what the framework names explicitly. Naming the failure mode in the framework IS the corrective for the AI behavior on future runs.

### Definitional / Internal Consistency

`harmony_layer.md`'s ranking principle: "the closer a harmony component is to carrying meaning, the higher its priority." Apply this to the register-alternation case: source uses register-alternation as a structural device (folk register grounds high-theology register; concreteness grounds abstraction). This is meaning-carrying. By the doc's own principle, register-alternation should be Tier 1. But the doc places register at Tier 3 ("doesn't change meaning"). **Definition contradicts itself on this case.** The Tier 3 verdict is correct for register-as-style; the doc fails to distinguish register-as-alternation. **New anchor:** the internal inconsistency is structural evidence that the framework's tier system needs a refinement, not just an addition.

### Definitional / Frame-exit Completeness

Gating predicate fires: the inquiry's frame inherits multi-value terms ("translation," "register," "principle," "failure mode," "framework") used across distinct propositions.

**Existence Enumeration for "register"** (project-wide):
- (a) Source-text register (the Turkish original's register alternation)
- (b) Target-text register (the English translation's register)
- (c) Register-alternation as a deliberate authorial device
- (d) Register-classification in the framework's tier system
- (e) The AI's internal register-selection mechanism

The inquiry's frame addresses (a) through (d). It treats (e) as an externalized "trigger event" (the C1-misread), not as a directly-examined object.

**Role Assessment for (e):** is the AI's internal mechanism load-bearing for the diagnosis? YES — it's the proximate cause. RE-LOCATE: (e) belongs in the "trigger / proximate layer" of the diagnosis, not in the "framework artifact" layer. The framework-level fixes can bias the AI's behavior on future runs (by naming the failure mode the AI should avoid), but the framework cannot reach into the AI's interpretation step directly. Both the framework-level fix AND the framework's explicit failure-mode naming are real interventions on (e), even though (e) is conceptually outside the framework.

**Verdict Rigor:** the "clean boundary" of treating AI as a black-box trigger is challenged by — could framework changes ACTUALLY prevent the AI failure, or does the AI need its own training? Structural argument FOR framework efficacy: I now have feedback memories that name these failure modes; with those memories loaded, I would catch them at translation time. If the FRAMEWORK named them upfront, the AI would catch them on first contact. The framework-level fix has empirical support (the post-hoc memory works; the pre-hoc framework would work the same way). The clean boundary survives Verdict Rigor.

**Residual / Coverage Justification:** is there a frame-exit concern not captured? The inquiry's frame currently treats AI behavior as in-scope-via-trigger but excludes AI training as out-of-scope. This is intentional bounding (the user controls the framework, not the model training). Terminating recursion.

### Phase / Calibration-State

The framework is in early-development calibration state. Some failure modes can only be named AFTER they fire (the C1-misread couldn't have been authored into the framework before any C1-misread had been observed). The framework's maturity is itself a calibration variable. **New anchor:** the framework needs an explicit "early-calibration" protocol — a mechanism for naming new failure modes AS they emerge, without waiting for a major rewrite. This is the architectural change (memory→spec ingestion) from a different angle.

### Meta-inspection after SV3

- **H1 (candidate set):** the three user hypotheses (H1: docs, H2: AI bulk, H3: failure modes) are not MECE. H3 overlaps with H1 (failure modes ARE a kind of doc content). H2 is mostly false (size evidence). The candidate set must expand to: H1 (docs), H3 (failure modes — but separately from H1), H4 (audience-spec interpretation as a process-step the framework leaves under-specified), H5 (lesson siloing / no learning loop). H2 contracts to a related true finding: no per-section register audit.
- **H2 (frame scope):** Frame-exit completeness handled above; AI behavior is in-scope-via-trigger.
- **H3 (question framing):** "what went wrong with the docs?" is the user's framing. It pre-biases toward H1. The sensemaking surfaced H4 and H5 to counteract this; documented here so downstream stages know the question's pre-bias was checked.
- **H7 (phase/calibration state):** handled above (framework maturity is calibration-shaped).
- **H8 (self-reference):** sensemaking and the translation framework share conceptual language (anchors, structure, multi-perspective). External grounding: empirical failure traces; user's downstream-confirmed-relevance signal; translation-studies tradition (register-shift, markedness are established concepts in Newmark / Nida / Vermeer). The framework-misclassifies-register finding is corroborated by external sources, not only by sensemaking-flavored reasoning. Self-reference risk is checked.

### SV3 — Multi-Perspective Understanding

The diagnosis now has clearer texture. The framework's tier system contains an *internal inconsistency*, not just a *gap*: harmony_layer's own ranking principle implies register-alternation should be Tier 1, but the doc places register at Tier 3. The cognitive-role distinction between principles (prescriptive) and failure modes (diagnostic) is irreducible: the user's intuition that principles imply failure modes is partly right but practically insufficient — they engage different attention modes. The candidate set expands from H1/H2/H3 to H1/H3/H4/H5, with H2 contracting to "no per-section audit." Sequencing of fixes matters: cheap doc edits first; expensive architectural change second.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: Is the C1-misread the primary cause, or is the framework's tier-3 register classification the primary cause?

**Strongest counter-interpretation:** the C1-misread is the whole cause. If the AI had interpreted "C1 English speakers" correctly (as a capability marker, not a vocabulary license), no register pull-up would have happened, framework gaps or not.

**Why the counter fails (structural grounds):** the framework's tier system MISCLASSIFIES register (C-28). Even if the AI had interpreted "C1" perfectly, the AI's self-audit (the harmony report) would still not surface register issues, because the tier system tells it register is Tier 3 (sacrificeable). Evidence: the harmony report at the bottom of `eng.md` (E-46) has zero register-related entries even though I (the author) ran it post-translation with full attention. The blindness is in the framework, not in the AI's interpretation step. Structural mechanism: the harmony report's content is generated FROM the tier system; tier-3 features get listed under "Tier 4 sacrificed" or omitted; register is at Tier 3 so it gets silently omitted from the audit. The C1-misread is a *trigger*; the framework gap is an *amplifier that allows the trigger to produce undetected outputs*. Both are real; the framework gap has more leverage because it catches many possible triggers, not just C1-misread.

**Confidence:** HIGH (the framework gap is documented in 4+ surfacing items: C-28, E-46, A-10, B-22).

**Resolution:** Multi-layer causation. C1-misread = PROXIMATE trigger. Framework's tier-3 register classification = STRUCTURAL amplifier. The framework gap is the higher-leverage intervention point.

**What is now fixed?** "Proximate vs structural cause" as distinct categories in the diagnosis; the framework's tier system as a cause, not just an absence.

**What is no longer allowed?** Single-cause framings ("just the AI made one wrong choice" OR "just the docs are missing things").

**What now depends on this choice?** All subsequent recommendations: doc fixes target the structural amplifier; audience-spec rules target the proximate trigger; both are needed.

**What changed in the conceptual model?** The diagnosis becomes a stack, not a list.

---

### Ambiguity 2: Do "principles" and "failure modes" overlap enough that the framework can claim to have failure modes implicitly?

**Strongest counter-interpretation:** the principle "preserve word order" implies the failure mode "don't break word order." Therefore the framework already has failure modes — they're embedded as the negative of each positive principle.

**Why the counter fails (structural grounds):** the cognitive roles differ along multiple axes — (1) **attention direction**: principles are *prescriptive* (read while doing the task, attention on what to achieve); failure modes are *diagnostic* (read after / as checklist, attention on what typically goes wrong). The operator engaged in a task cannot simultaneously run a comprehensive check across all positive principles; the cognitive budget goes to the doing-mode. A separate diagnostic pass (with its own list) is what enables the check. (2) **pattern naming**: failure modes name MULTI-PRINCIPLE INTERACTIONS that no single positive principle predicts. Register pull-up emerges from "use sophisticated vocabulary" (a vague positive value) + "preserve source meaning" (a principle) + "C1 audience" (an audience spec) interacting in a misread way. NO single positive principle in the framework predicts this combinatorial failure. Only an EXPLICITLY NAMED failure mode ("register pull-up: AI tendency to render plain folk-vocabulary with marked-English equivalents — corvée, cauldron, morsel, etc.") can surface it. (3) **empirical evidence**: the framework HAS positive principles that, if followed, would have prevented register pull-up (small-cycle examples should be culturally adaptable to target audience — A-2). Yet the failure happened. Therefore positive principles did not function as failure modes in this case — empirical disconfirmation of the counter.

**Confidence:** HIGH (structural cognitive-role argument + multi-principle-interaction argument + empirical disconfirmation).

**Resolution:** Principles do NOT count as failure modes for practical purposes. They are complementary cognitive instruments. The framework needs BOTH.

**What is now fixed?** The user's sub-question gets a definite answer: no, principles don't substitute for failure modes; the framework needs a separate failure-mode catalog.

**What is no longer allowed?** "The framework already implies these failures via its positive principles" — disconfirmed.

**What now depends on this choice?** The recommendation to add an explicit failure-modes section, separate from the principles, is structurally required.

**What changed in the conceptual model?** "Failure modes catalog" becomes a load-bearing recommendation, not an optional addition.

---

### Ambiguity 3: Was bulk translation a factor (the user's H2)?

**Strongest counter-interpretation:** the AI did translate in one continuous pass without per-paragraph audit. That's "bulk" in some sense. So H2 is partly true.

**Why the counter fails (structural grounds):** the user's H2 framing specifies bulk-as-volume ("bulk translation all pages?"). Volume is the user's stated dimension. Text size: ~70 lines, ~9 paragraphs. That is not bulk. The user explicitly notes this ("there are not so much text, not like 20 pages"). The volume-based hypothesis is disconfirmed by the size evidence. The "translated in one pass without per-section audit" is a different finding — it's about process structure, not volume. Reframe: not "bulk translation issue" but "absence of per-section register audit step in the framework's process model." This is a real finding that belongs in the H1 (docs gaps) or H4 (process-step under-specified) categories, not in H2.

**Confidence:** HIGH (size evidence is empirical; reframing of the related finding is structurally clean).

**Resolution:** H2 (bulk-as-volume) = MOSTLY FALSE. Related true finding: the framework's 3-pass process model doesn't specify a per-section register audit. RE-LOCATE this finding under H1 (docs gaps) as a process-shaped gap.

**What is now fixed?** The bulk hypothesis is closed; its kernel of truth is re-located to the docs-gaps layer.

**What is no longer allowed?** Treating H2 as an explanatory hypothesis at the meta level.

**What now depends on this choice?** Recommendations no longer include "translate page-by-page" as a corrective.

**What changed in the conceptual model?** One of the three user hypotheses is closed out cleanly; the diagnosis sharpens.

---

### Ambiguity 4: Is the framework's classification of register as Tier 3 a defensible early-calibration choice or a structural error?

**Strongest counter-interpretation:** harmony_layer.md says register is Tier 3 because "register consistency … doesn't change meaning." That's true for some cases — a translator can shift formal/casual without altering propositional content. The Tier 3 verdict is defensibly correct for register-as-style.

**Why the counter fails (structural grounds):** the doc's own ranking principle states "the closer a harmony component is to carrying meaning, the higher its priority." Test this principle against the register-alternation case: source uses register alternation as a structural device (folk register grounds the parable; theological register marks the decoder). The folk-grounds-theology pattern IS the parable's rhetorical move — concreteness providing tangible footing for abstraction. When the translation flattens this alternation, the rhetorical move is lost; that IS a meaning loss. By the doc's own principle, register-when-it-alternates should be Tier 1. The Tier 3 verdict applies only to register-as-style-uniformity; it FAILS to distinguish register-as-alternation. The doc misses a sub-category and applies the wrong tier to the missed sub-category. **The internal inconsistency (doc contradicts its own ranking principle on this case) is the structural argument.** This is independent evidence beyond "the failure happened" — it's an in-doc proof.

**Confidence:** HIGH (the internal inconsistency is verifiable from the doc alone; the empirical failure corroborates).

**Resolution:** Tier 3 classification is correct for register-as-style; WRONG for register-as-alternation. The framework needs to split the concept (or upgrade register to Tier 1 when alternation is detected).

**What is now fixed?** "Register-as-alternation is Tier 1" is the corrected classification.

**What is no longer allowed?** Treating all register concerns as Tier 3.

**What now depends on this choice?** The recommendation to edit harmony_layer.md's tier list is structurally required by the doc's own ranking principle, not just by external evidence.

**What changed in the conceptual model?** The fix is not adding a new principle to a list; it's fixing an internal inconsistency the doc already has.

---

### Ambiguity 5: Does fixing the docs prevent recurrence, or does the framework need an architectural addition (memory→spec ingestion flow)?

**Strongest counter-interpretation:** fix the docs once and recurrence is prevented for these specific patterns. Architectural change is overkill.

**Why the counter fails (structural grounds):** the framework's value depends on its ability to absorb new failure modes as they emerge. Translation has indefinitely many possible failure types (register pull-up was unknown before; metaphor-momentum override was unknown before; future failures will be unknown until they fire). A static document, even after this round of fixes, will go stale relative to the failure types that emerge next. Empirical evidence: this very inquiry exists because lessons saved to AI memory (G-57, G-58) don't flow back to the framework (G-59). Without a feedback path, the framework's "knowledge" is owned by the AI's session memory, which is volatile across sessions and not user-readable. The framework loses learning-capability. **Mechanism**: every future failure becomes a separate diagnostic inquiry; the framework never converges toward completeness. **Counter-counter**: the architectural cost is real (memory→spec flow needs tooling and discipline). Resolution accepts this cost but acknowledges that without it, fixes stay one-off.

**Confidence:** MEDIUM (the architectural argument is sound; the engineering effort is real; the practical priority is the user's call).

**Resolution:** BOTH layers needed. Doc fixes are necessary (close the known gaps); architectural change is necessary for long-term framework viability. Sequence: doc fixes first (cheap, high marginal value); architectural change second (high cost, high long-term value).

**What is now fixed?** "One-time doc patches" as a complete solution is closed.

**What is no longer allowed?** Treating this failure as a one-off bug.

**What now depends on this choice?** Recommendations include both immediate doc fixes AND a longer-term architectural recommendation.

**What changed in the conceptual model?** The fix becomes a two-tier program: immediate + architectural.

---

### Ambiguity 6 (specific-vs-pattern check, per the cue): Are the 8 register words + 1 polysemy word the WHOLE problem, or a few cases of a wider pattern?

**Strongest counter-interpretation:** these specific words ARE the problem. Fix them, move on. There's no wider pattern beyond the documented instances.

**Why the counter fails (structural grounds):** the AI itself suspected more (F-53: "brand you a mutineer, inflict the punishment, tilth, August and All-Generous, Lordly wisdom, beast of prey, trench-post"). Even if the user hasn't flagged these, they're the same class. The register pull-up has three-dimensional consistency: consistent direction (always upward), consistent location (parable register only), consistent type (folk → ornate/archaic English). Three-dimensional consistency = pattern, not isolated incidents. Also: "register-shift" (or "register-mismatch") is an established concept in translation studies (Newmark, Nida). The pattern exists empirically beyond this one translation. **Mechanism**: the AI's bias toward elevated vocabulary on "C1" audiences is a re-firing trigger; without a named failure mode in the framework to catch it, the pattern WILL fire on the next translation too.

**Confidence:** HIGH (three-dimensional consistency + AI's own admission of suspected-but-uncaught instances + external corroboration from translation studies).

**Resolution:** The 8+1 words are SPECIFIC EXAMPLES of a wider pattern. The diagnosis must address the pattern, not just the instances. The pattern names "register pull-up" (for the 8) and "metaphor-momentum override" (for nefer).

**What is now fixed?** The diagnosis operates at pattern level, not instance level.

**What is no longer allowed?** Treating this as an isolated translation issue.

**What now depends on this choice?** Recommendations must address pattern-level fixes (failure-mode catalog) not just instance-level fixes (this translation's word swaps).

**What changed in the conceptual model?** The motivating examples are evidence for the pattern, not the pattern itself.

---

### Load-bearing concept test (per the refinement note)

**Concept: "register pull-up."** Does this term represent a real structural distinction, or is it an incidental label invented for these examples?
- Counter: maybe it's just "I used fancy words." No structural phenomenon.
- Why counter fails: three-dimensional consistency (Ambiguity 6); external corroboration (translation-studies "register-shift" tradition); diagnostic utility (the term predicted suspected-but-uncaught instances correctly per F-53). The concept is structurally real.

**Concept: "framework blindness."** Real or metaphor?
- Counter: maybe just an absence claim dressed up as a property.
- Why counter fails: the framework actively MIS-classifies (Tier 3 register), not merely omits. Active mis-classification has different remediation requirements than mere absence. The metaphor "blindness" is anchored to a real structural property.

**Concept: "C1-misread."** Real failure mode or incidental misinterpretation?
- Counter: maybe just one bad interpretation; no general phenomenon.
- Why counter fails: audience-spec misinterpretation is a recurring AI behavior class (this is one instance; other AI translation work shows similar interpretive over-reaches on similar audience specs). Concept survives.

**Concept: "lesson siloing."** Architectural property or just current location of two memory files?
- Counter: maybe the two memory files just happen to be there; not a structural pattern.
- Why counter fails: the framework has no documented ingestion path. The location is structurally determined by the absence of a flow, not by coincidence. Architectural property is real.

---

### SV4 — Clarified Understanding

The diagnosis is now multi-layered with each layer's structural argument made explicit and counter-tested. Six causal-test pairs resolved at HIGH confidence (one at MEDIUM, on the architectural cost). The framework has an internal inconsistency (the Tier 3 register classification contradicts the doc's own ranking principle), specific gaps (no register-matching, markedness, polysemy, failure-mode rules), and an architectural property (lesson siloing) that ensures recurrence. The AI's C1-misread is the proximate trigger; the framework's amplification is the structural cause. The user's three hypotheses expand to a five-cause stack with one (H2) closed and four active.

---

## Phase 4 — Degrees-of-Freedom Reduction

### What is now fixed (locked anchors)

- The translation failures (register pull-up + *nefer* polysemy) are real, documented, pattern-shaped — not isolated.
- The framework's tier system contains an internal inconsistency on register-as-alternation.
- The framework's self-audit (harmony report) is structurally blind to register because of the tier-3 classification.
- The framework lacks an explicit failure-mode catalog.
- The framework lacks a memory→spec ingestion flow; lessons live in AI-private memory.
- Principles do not substitute for failure modes (cognitive-role argument + empirical disconfirmation).
- The AI's audience-spec interpretation step (C1-misread for register; metaphor-momentum for *nefer*) is the proximate trigger layer.
- Bulk translation (volume-based) is not a primary cause.

### What is eliminated (no longer viable interpretations)

- Single-layer-cause framings ("just the docs" or "just the AI" or "just the absence of failure modes").
- "Bulk translation" as a primary cause.
- "Principles already imply failure modes; no separate catalog needed" — disconfirmed.
- "Fix this translation's words and move on" — pattern-level fix is required.
- "One-time doc patch fully prevents recurrence" — architectural flow needed for unknown future patterns.

### What paths remain viable

- **Path A — Immediate doc fixes:**
  - Edit `harmony_layer.md` to split register into "register-as-style" (Tier 3) and "register-as-alternation" (Tier 1), or to add a sub-rule "register-as-alternation IS meaning-carrying when source alternates."
  - Add a failure-modes section to `harmony_layer.md` (or as a sibling file) with the named patterns: register pull-up, metaphor-momentum override, markedness inversion, C1-misread as audience-spec failure.
  - Add a register-matching / markedness-matching principle to `notes.md`.
  - Add a polysemy-disambiguation rule ("local construction picks the sense; metaphor-momentum is a known override trap") to `notes.md`.

- **Path B — Process-step additions:**
  - Specify a per-section register audit step in the harmony-layer's 3-pass process (between Pass 2 and Pass 3).
  - Specify an audience-spec interpretation rule (what "C1 English speakers" means — capability marker, not vocabulary license).

- **Path C — Architectural addition:**
  - Design a memory→spec ingestion flow so AI-extracted lessons (the feedback memories at `/Users/ns/.claude/projects/.../memory/`) can update the framework documents over time.

### SV5 — Constrained Understanding

The solution space is now structured. Path A is cheap and addresses documented gaps. Path B addresses process under-specification. Path C addresses architectural learning. The diagnosis's recommendation set is a coordinated multi-path program, not a single fix. The sequencing is A first (high marginal value, low cost), B second (specific process additions), C third (high cost, high long-term value).

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Did each new perspective in Phase 2 destabilize the model and force patching, or did they refine it cleanly? Review:
- Technical/Logical: refined (added "tier system governs harmony report content").
- Human/User: refined (sharpened the principle/failure-mode distinction).
- Strategic/Long-term: refined (added lesson-siloing as architectural property).
- Risk/Failure: refined (added sequencing constraint).
- Resource/Feasibility: refined (added cost-benefit sequencing).
- Ethical/Systemic: refined (anchored the AI-behavior-as-in-scope decision).
- Definitional/Internal Consistency: this was the WATERSHED — the internal-inconsistency finding shifted the diagnosis from "missing principles" to "self-contradicting framework." Not a destabilization that required patching; a refinement that sharpened the central finding.
- Definitional/Frame-exit: refined (locked the AI-as-trigger-not-target boundary).
- Phase/Calibration-State: refined (added framework-maturity as a calibration variable, motivating Path C).

No perspective forced model REPLACEMENT (the accommodation trigger would fire). Each refined. Model is stable.

### The stabilized conceptual model

The translation failures (register pull-up across 8+ words + *nefer* polysemy mis-resolution) are produced by a **four-layer causal stack**:

```
PROXIMATE  ─ AI's audience-spec interpretation (C1-misread; metaphor-momentum)
             │  triggers the failure but is amplified by →
STRUCTURAL ─ Framework gaps & internal inconsistency
             │  ▸ harmony_layer.md classifies register as Tier 3
             │    (contradicts its own ranking principle for the
             │     register-as-alternation sub-case)
             │  ▸ notes.md / advanced_principles.md lack register-matching,
             │    markedness-matching, polysemy-disambiguation rules
             │  ▸ the harmony-report self-audit is blind to register
             │    because tier system tells it not to look
             │  enabled by →
META       ─ Framework is a positive-principle list, not a diagnostic catalog
             │  ▸ no explicit failure-mode list
             │  ▸ principles are prescriptive; failure modes are diagnostic;
             │    different cognitive operations
             │  ▸ failure modes name multi-principle interactions
             │    no single principle predicts
             │  perpetuated by →
ARCHITECTURAL ─ No memory→spec ingestion flow
              ▸ AI-extracted lessons live in session memory
              ▸ docs do not absorb learning from failures
              ▸ framework cannot converge toward completeness
              ▸ each future failure becomes a separate diagnostic inquiry
```

Against the user's three hypotheses:

| User hypothesis | Verdict | Notes |
|---|---|---|
| **H1** — fault in `advanced_principles.md`, `notes.md`, `harmony_layer.md` | **CONFIRMED** | Specific gaps + active mis-classification of register at Tier 3. |
| **H2** — AI bulk translation issue | **MOSTLY FALSE** | Text was short. Related true finding (no per-section audit) re-located under H1. |
| **H3** — lack of failure modes | **CONFIRMED** | Principles do NOT count as failure modes; cognitive roles differ; multi-principle interactions need explicit naming. The user's sub-question gets a definite "no." |

Plus two causes the user's hypotheses didn't name:

| Added cause | Verdict | Notes |
|---|---|---|
| **H4** — audience-spec interpretation step under-specified | **CONFIRMED** | The C1-misread is the proximate trigger; the framework has no rule for interpreting audience-level descriptors. |
| **H5** — lesson siloing / no learning loop | **CONFIRMED** | Lessons live in AI memory, not in docs. Architectural cause of recurrence. |

### SV6 — Final Stabilized Model

The root cause of the translation failures is a **multi-layer causal stack** where the user's three hypotheses correctly identify two layers (H1 docs + H3 failure modes), miss the proximate-trigger layer (H4 audience-spec interpretation) and the architectural layer (H5 lesson siloing), and overstate the volume-based hypothesis (H2 closed).

The single most surgical structural finding is that `harmony_layer.md` contradicts its own ranking principle on the register-as-alternation case — the framework actively misclassifies the very feature whose preservation would have prevented the failure. This is a self-contained correction (the doc's own principle proves the correction; no external authority needed).

The single most leveraged architectural finding is that the framework has no mechanism to absorb failures into its own documents — every failure becomes either a one-off translation fix or a feedback memory that doesn't propagate.

The user's sub-question ("don't principles count as failure modes?") gets a definite NO at HIGH confidence: principles are prescriptive (read while doing); failure modes are diagnostic (read as a separate scan); they engage different attention modes and name different things (failure modes name MULTI-PRINCIPLE INTERACTIONS no single positive principle predicts).

### How SV6 differs from SV1

- **SV1** expected: probably the docs were missing things; figure out which.
- **SV6** delivered: a four-layer causal stack with two user-hypothesis confirmations (H1, H3), one user-hypothesis closure (H2 mostly false), two added causes the user didn't name (H4, H5), one internal-inconsistency finding inside the framework itself, and a sequenced recommendation set (A: doc fixes, B: process additions, C: architectural addition) with explicit cost-benefit ordering. The diagnosis moved from "the docs are missing things" (linear gap-list) to "the framework misclassifies the relevant feature AND lacks a diagnostic mode AND lacks a learning loop" (architectural and stack-shaped diagnosis).

### Saturation indicators

- **Perspective saturation:** the last three perspectives (Resource/Feasibility, Ethical/Systemic, Definitional/Internal Consistency) each introduced new anchor types (sequencing constraint, stance commitment, internal-inconsistency proof). Perspectives were NOT saturated mid-way; the model accumulated structure through the end. Saturation reached by the close of Phase 2.
- **Ambiguity resolution ratio:** 6/6 ambiguities resolved at HIGH or MEDIUM confidence; none left open.
- **SV delta:** SV1 → SV6 shows a structural shift from one-dimensional gap-list to four-layer causal stack with sequenced fixes. Healthy delta.
- **Anchor diversity:** anchors span all five types (constraints, key insights, structural points, foundational principles, meaning-nodes) and 9 perspective categories. Diversity strong.

### Open frontiers (for downstream stages)

- **F-1** Whether the user wants to pursue Path C (memory→spec ingestion flow) — engineering investment decision. Sensemaking surfaces the option; the user decides.
- **F-2** Whether other translations in `mytrasnlations/` show the same register-pull-up signature (corroborates pattern-vs-instance). Surfacing flagged this (FF-2); sensemaking did not absorb it.
- **F-3** The specific WORDING of the failure-modes section (Phase 1 of Path A) — names, structures, scoping. Sensemaking commits to "a failure-modes section exists" but not to its content. Innovation stage's job.
- **F-4** Whether Path B's per-section register audit should be a new sub-phase in harmony_layer's 3-pass model or a sub-step inside Pass 2. Architectural detail. Innovation stage's job.
