# Sensemaking — intervention_locus_and_shape_check

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-04_02-15__intervention_locus_and_shape_check/_branch.md`

Purpose: confirm or refute "in-doc addition to `harmony_layer.md`" as the right intervention locus, enumerate alternatives, identify when each alternative would be the right choice. Inheriting from surfacing: the prior inquiries operated with INCOMPLETE framework knowledge (treated 3 of ~10 .md files at project root). New locus candidates: D-L4 `translation_principals.md` (73K), D-L5 `terminology.md` (declares term-definition authority), D-L6 `how_config_should_be.md` (config locus), D-L12 code-level changes.

---

## SV1 — Baseline Understanding (pre-analysis)

The user is sanity-checking a recommendation. The most likely answer is "yes, in-doc addition is right" because the contradiction empirically lives in `harmony_layer.md` and that's where the fix logically belongs. But surfacing surfaced unexpected scope-expansion via the framework-knowledge-gap finding. So the answer might be "yes but with supplementary loci you didn't know about." Treat the surfacing finding seriously rather than smoothing it away.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **CON-1** The specific contradiction (Tier 3 register-consistency classification vs the doc's own ranking principle) empirically lives in `harmony_layer.md`. Its location is fixed.
- **CON-2** The user originally bounded the framework territory to 3 docs in their initial instruction ("read only the files i mentioned: notes.md, advanced_principles.md, and harmony_layer.md"). The prior inquiries respected that bound.
- **CON-3** Surfacing revealed the project root has 10 .md files plus a Python package (`comprehenslate/`) — substantially larger framework than the prior inquiries treated.
- **CON-4** `terminology.md` explicitly declares authority on term definitions: "If a design doc uses a term differently from this file, this file wins." This is a doc-stated locus-authority rule.
- **CON-5** The "easy" criterion from the prior inquiry 2 still applies — any supplementary locus updates must remain low-overhead.
- **CON-6** The user's question is a BINARY frame-check ("addition to harmony_layer.md OR different?") — the deliverable is a YES/NO with structural reasoning + alternative enumeration.

### Key Insights

- **KI-1** The prior recommendation is CORRECT for the diagnosed issue. The contradiction is in `harmony_layer.md`; fixing the contradiction requires editing `harmony_layer.md`. No alternative locus is better for the specific issue. This is the YES half of the answer.
- **KI-2** The prior recommendation may be INCOMPLETE in scope. Surfacing revealed supplementary loci the prior inquiries didn't engage with: `terminology.md` for sub-case naming (it declares its own authority on definitions); `how_config_should_be.md` for audience-spec config (if S9 from prior inquiry 1's audience-spec rule is config-shaped rather than principle-shaped); `translation_principals.md` for principle authorship (if it's the authoritative principles doc, not `notes.md`). The recommendation's completeness depends on whether the user wants the bare-minimum fix or the cross-locus discipline.
- **KI-3** The EA-7 per-entry trigger from the prior inquiry 2 ("any entry that derives a classification from a stated principle in the same doc") fires ONLY in `harmony_layer.md`. Other docs have different shapes: `notes.md` and `translation_principals.md` are flat principle lists (no classification framework); `terminology.md` is term definitions; `how_config_should_be.md` is config; `advanced_principles.md` is worked examples. None has the principle/classification split that `harmony_layer.md`'s tier system has. The recommendation's primary locus is structurally correct.
- **KI-4** Locus depends on DECISION TYPE, not just file location. Term-definition decisions belong in `terminology.md` (per its declared authority); config decisions belong in `how_config_should_be.md`; procedural-discipline decisions belong in `harmony_layer.md`; principle authorship belongs in whichever is the authoritative principles file. The locus question is multi-dimensional, not single-file.
- **KI-5** The user's "or different?" is invitational but not necessarily expansive. They may want confirmation of the primary recommendation OR they may want the supplementary loci surfaced. Sensemaking should surface BOTH and let the user choose, not pre-commit on their behalf.
- **KI-6** The framework-knowledge-gap (prior inquiries treated 3 of 10 docs) was partly a USER-INSTRUCTED scope (the user bounded the territory at the start) and partly an AI scoping omission (the AI didn't surface "are there more files I should consider?" before bounding the discipline work). Neither is fully blameworthy; both are correctable now.
- **KI-7** The framework includes a CODE project (`comprehenslate/` package with classes like `TranslationMemory`). Code-level changes are a future-consideration locus — not in immediate scope but worth flagging for the user's awareness when the relevant code is built.

### Structural Points

- **SP-1** Project root organization: 10 .md files (the framework docs) + a Python package + supporting files. Each .md file has a distinct role.
- **SP-2** Doc-role taxonomy (from sampling):
  - `harmony_layer.md`: tier system + ranking principle (procedural priority spec).
  - `notes.md`: ~60 flat principles ("Comprehenslate should detect X").
  - `translation_principals.md`: ~60-90 principles (overlapping with notes.md; 73K vs notes.md's ~38K — possibly the authoritative version).
  - `advanced_principles.md`: worked examples elaborating principles.
  - `terminology.md`: canonical term definitions (declares own authority).
  - `how_config_should_be.md`: config spec for code (audience levels, format options, etc.).
  - `roadmap.md`: project trajectory.
  - `README.md`, `advanced.md`, `my_notes.md`: less clearly load-bearing for the framework.
- **SP-3** Locus dimensions: (a) file-level — which doc gets edited; (b) decision-type-level — which kind of decision is being made (procedural / definitional / config / principle-author); (c) scope-level — specific contradiction / pattern in one doc / cross-doc framework consistency.
- **SP-4** The EA-7 per-entry trigger evaluated against each doc: fires only in `harmony_layer.md` because only it has the principle/classification structural pattern. Other docs are pattern-absent → mechanism doesn't apply.

### Foundational Principles

- **FP-1** A specific intervention should match the specific problem's location. The contradiction is in `harmony_layer.md`; the fix belongs in `harmony_layer.md`. Cross-doc interventions are appropriate when the problem crosses docs.
- **FP-2** Doc-stated authority hierarchies should be respected. When a doc declares "I am authoritative on X" (as `terminology.md` does for term definitions), decisions of type X should land there, even if another doc could nominally host them.
- **FP-3** Frame-check questions like the user's ("is X right or different?") deserve YES-WITH-CAVEATS answers when caveats exist, not unqualified YES or NO. The user is asking for confidence-checking; honesty about completeness scope matters.
- **FP-4** When the territory was previously under-scoped (3 of 10 docs treated), surfacing the gap is the right move — even if the originally-bounded recommendation remains correct. The user gets to decide whether to act on the expanded scope.

### Meaning-Nodes

- **MN-1** In-doc primary locus (= `harmony_layer.md` for this issue)
- **MN-2** Supplementary loci (= `terminology.md` for sub-case naming, `how_config_should_be.md` for audience config, possibly `translation_principals.md` for principle authority)
- **MN-3** Decision-type locus (term-def vs principle vs config vs procedure — each maps to a different file)
- **MN-4** Doc-authority hierarchy (terminology.md wins on definitions per its own claim)
- **MN-5** Framework-knowledge-gap (the prior inquiries' 3-of-10 scope; correctable now)
- **MN-6** Scope-expansion question (does the user want cross-doc consistency discipline beyond harmony_layer.md?)
- **MN-7** YES-WITH-CAVEATS answer shape (not just yes/no)

### Meta-inspection after SV2 — H4 (concept names) and H5 (motivating examples)

- H4: concept-names introduced (decision-type locus, doc-authority hierarchy, framework-knowledge-gap, supplementary loci) — each grounded in observable doc-content (terminology.md's stated authority; ls of project root; the EA-7 trigger evaluation).
- H5: motivating examples = (a) the original Tier 3 contradiction (still primary); (b) the additional doc files discovered by surfacing (the scope-expansion driver). Specific-vs-pattern flag: addressed in Phase 3 (Ambiguity 6).

### SV2 — Anchor-Informed Understanding

The answer is YES with structural caveats. YES because the contradiction empirically lives in `harmony_layer.md` and the prior recommendation's primary locus is right. WITH CAVEATS because surfacing revealed the framework is larger than the prior inquiries treated; supplementary loci exist where parts of the broader prevention discipline could also land (`terminology.md` for sub-case naming; `how_config_should_be.md` for audience-spec config; possibly `translation_principals.md` for principle authority). The user should know about these supplementary loci to make an informed decision about scope, but the core recommendation remains correct.

---

## Phase 2 — Perspective Checking

### Technical / Logical

The contradiction empirically lives in `harmony_layer.md`'s tier section. Logically, fixing the contradiction requires editing `harmony_layer.md`. The EA-7 per-entry trigger from prior inquiry 2 evaluates each doc by the structural pattern (principle/classification split). Evaluating each doc:
- `harmony_layer.md`: pattern FIRES (meta-principle + tier classifications) → in-scope for procedural prevention.
- `notes.md`: pattern ABSENT (flat principle list, no classification framework) → out of scope.
- `translation_principals.md`: pattern ABSENT (flat principle list) → out of scope.
- `advanced_principles.md`: pattern ABSENT (worked examples) → out of scope.
- `terminology.md`: pattern ABSENT (term definitions) → out of scope for the EA-7 mechanism, BUT relevant for sub-case naming decisions per FP-2.
- `how_config_should_be.md`: pattern ABSENT (config spec) → out of scope for procedural prevention, BUT relevant for audience-spec config per CON-4.

**New anchor:** the prevention mechanism's primary locus is structurally correct (only `harmony_layer.md` has the firing pattern); the supplementary loci serve OTHER decision types, not the EA-7 mechanism's domain.

### Human / User

The user's question phrasing ("or different?") is invitational — they want to confirm the recommendation or be told about alternatives. The user did NOT ask for scope expansion explicitly; they asked for confidence in the recommendation. **New anchor:** the deliverable shape should be YES-WITH-CAVEATS (confirm the recommendation + surface the supplementary loci + let the user decide how far to go). Not pre-committing on their behalf respects the user's agency.

### Strategic / Long-term

If the recommendation is implemented only in `harmony_layer.md`, future contradictions in the supplementary-locus dimensions (term definitions in `terminology.md`; config in `how_config_should_be.md`) remain unprotected. But each of those dimensions has its own consistency problem class — not the principle/classification split that the EA-7 mechanism is designed for. Treating them under the same mechanism would be a category error.

**New anchor:** strategic completeness requires recognizing that different decision-type loci need different consistency mechanisms. The procedural mechanism is right for `harmony_layer.md`'s pattern; other loci may need their own mechanisms in future inquiries.

### Risk / Failure

- Risk A: implementing only in `harmony_layer.md` leaves the sub-case names ("register-as-style," "register-as-alternation") undefined in the canonical-terms doc — a future reader could find inconsistencies between docs.
- Risk B: scope-expanding to all 10 docs over-broadens the inquiry and violates the user's original bound.
- Risk C: the user thinks "in-doc to harmony_layer.md" is the complete answer when supplementary loci also need touching.

Mitigation for all three: the deliverable explicitly surfaces the supplementary loci as OPTIONAL companions to the primary recommendation. The user decides which to touch.

**New anchor:** the failure modes can be designed against by transparent surfacing of the locus dimensions.

### Resource / Feasibility

- Primary recommendation (in-doc edits to `harmony_layer.md`): bounded effort (~15-30 min day-one + sweep, per prior inquiry 2's MVD).
- Supplementary locus: sub-case naming in `terminology.md`: ~5 min (a small terminology entry).
- Supplementary locus: audience-spec rule in `how_config_should_be.md`: ~5-10 min (add to config spec).
- Investigate `translation_principals.md` for authoritative status: 5-10 min one-time (sample the file; compare with notes.md).
- All within "easy" criterion as composite.

**New anchor:** the supplementary loci are individually cheap; the composite remains "easy."

### Ethical / Systemic

The user maintains the framework solo and authored the original territory bound. Surfacing the scope expansion respects their agency (they get to decide); imposing the expansion would not.

### Definitional / Internal Consistency

The prior inquiries' use of "framework" referred to 3 docs. Surfacing's evidence (10 docs at project root + code project) reveals a wider "framework." The prior inquiries' recommendations are CONSISTENT within the 3-doc frame; expansion to 10 docs is ADDITIVE, not invalidating. The wider "framework" includes the narrower one as a subset.

**New anchor:** the prior recommendations stand; the supplementary loci are additions, not revisions.

### Definitional / Frame-exit Completeness

Gating predicate FIRES: the inquiry's frame inherits multi-value terms used across distinct propositions. Multi-value terms: "framework" (3-doc vs 10-doc vs 10-doc+code), "locus" (file-level vs decision-type-level vs scope-level), "intervention" (edit vs addition vs new file).

**Existence Enumeration for "framework":**
- (a) `framework` = 3 docs (prior inquiries' usage)
- (b) `framework` = 10 docs at project root (surfacing's discovery)
- (c) `framework` = 10 docs + Python code project (project-wide)
- (d) `framework` = the conceptual design (across docs, code, AI prompts)

The inquiry's frame addresses (a) and (b); (c) is partially in scope (acknowledged as future consideration); (d) is conceptual abstraction without direct intervention locus.

**Role Assessment:** for the locus question, (b) is the load-bearing frame (the project root .md files are the user-modifiable framework documents). (c) is RE-LOCATED to "future consideration when code is built." (d) is not actionable.

**Verdict Rigor:** the clean boundary "(b) is the in-scope frame; (c) is future" is challenged by — what if the code is the runtime carrier of the tier system and editing the doc without updating the code creates drift? Response: the code's tier-system implementation status is unknown (terminology.md mentions related classes but not specifically a tier-system implementation). The drift risk is real but speculative; flagging it as a future consideration is appropriate; treating it as in-scope now would exceed the inquiry's purpose.

**Residual Coverage:** is there any frame-exit concern not captured? The "framework" term might also include the AI's system prompts (the AI itself being part of the comprehenslate translation system). But that's user-inaccessible (architecturally) and was already adjudicated out of scope in prior inquiries.

### Phase / Calibration-State

The inquiry is calibration-checking the prior inquiries' recommendation. The framework's maturity is part of the picture: it's actively being built (mtimes show edits up to April 2026). Prevention recommendations that align with the wider framework (cross-reference terminology.md, update config spec) carry less drift risk than recommendations that touch only one doc.

**New anchor:** as the framework matures, the supplementary-loci discipline becomes more important. Early-now is a good time to land the multi-locus pattern even at small cost.

### Meta-inspection after SV3

- H1 (candidate set): the locus candidates are (1) `harmony_layer.md` primary, (2) `terminology.md` sub-case naming, (3) `how_config_should_be.md` audience-spec config, (4) `translation_principals.md` principle authority (pending investigation), (5) code-level (future). Each is in scope as a possibility; user decides which to act on. No new locus surfaces upon reflection.
- H2 (frame scope): handled by Frame-exit Completeness.
- H3 (question framing): "or different?" is ambiguous between "is the recommendation wrong?" and "what else should I know?" Resolved by giving YES-WITH-CAVEATS shape.
- H7 (phase/calibration-state): handled.
- H8 (self-reference): I'm evaluating my own prior recommendations. External grounding: the additional doc files are empirically verifiable by `ls`; surfacing found them. The supplementary-loci recommendations are anchored to those docs' stated authority claims (terminology.md) and their actual content (how_config_should_be.md's audience-spec config), not to internal sensemaking reasoning. Self-reference is checked.

### SV3 — Multi-Perspective Understanding

The diagnosis sharpens. The user's question gets the answer: YES, in-doc edit to `harmony_layer.md` is right for the diagnosed contradiction. The recommendation is consistent within the 3-doc frame the prior inquiries used. WITH the caveat that the framework is wider than the prior inquiries treated; supplementary loci exist where parts of the broader prevention discipline can also land (`terminology.md` for sub-case naming per its own stated authority; `how_config_should_be.md` for audience-spec config per its config-role; possibly `translation_principals.md` for principle authority pending investigation; code-level as future consideration). The user decides scope.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: Does the surfacing discovery (10 docs, not 3) INVALIDATE the prior recommendation?

**Strongest counter-interpretation:** The prior recommendation was based on incomplete information; with the complete picture, it should be revised or rejected.

**Why the counter fails (structural grounds):** The specific contradiction the prior recommendation addresses empirically lives in `harmony_layer.md`. Adding more docs to the territory doesn't move the contradiction. The contradiction's location is invariant under territory expansion. The recommendation correctly targets the location where the issue lives; expanding the territory adds CONTEXT but doesn't change WHERE the fix belongs for THIS issue. Additionally, the EA-7 per-entry trigger evaluation confirms that the procedural prevention mechanism fires only in `harmony_layer.md` (other docs lack the principle/classification structural pattern). The mechanism's primary locus is structurally correct, not just by-default.

**Confidence:** HIGH.

**Resolution:** The prior recommendation REMAINS CORRECT for the diagnosed contradiction. The surfacing finding ADDS to the picture (supplementary loci exist) without invalidating the core.

**What is now fixed?** The YES half of the answer to the user's binary question is stable.

**What is no longer allowed?** Framings that treat the surfacing finding as invalidating the prior recommendation.

**What now depends on this choice?** All recommendations build on the confirmed primary locus.

**What changed in the conceptual model?** The recommendation is correct primary; supplementary expansion is additive.

---

### Ambiguity 2: Is the prior recommendation COMPLETE, or are supplementary loci required?

**Strongest counter-interpretation:** The prior recommendation addresses the procedural cause completely; supplementary loci are speculative additions without empirical justification.

**Why the counter fails (structural grounds):** Two empirical evidences justify supplementary loci. (1) `terminology.md` explicitly declares its own authority on term definitions ("If a design doc uses a term differently from this file, this file wins"). The prior inquiry's proposed sub-case naming ("register-as-style," "register-as-alternation") is a term-definition act; per terminology.md's own rule, the sub-case names belong there. (2) `how_config_should_be.md` is the config-locus for translation behavior (it defines audience levels: Native / late learner / late learner simple / poetic). The prior inquiry 1's S9 audience-spec rule is partly a config concern (CEFR-level handling); per the config locus, S9's config-level component belongs there. Both supplementary loci are anchored to OBSERVABLE properties of the additional docs, not to speculative additions.

**Confidence:** HIGH.

**Resolution:** The prior recommendation is COMPLETE for the procedural prevention discipline IN `harmony_layer.md`; it is INCOMPLETE for the cross-locus framework hygiene (sub-case naming + audience-spec config). The completeness depends on which scope the user wants.

**What is now fixed?** The recommendation has two completeness levels: complete-for-harmony_layer.md / complete-for-cross-locus.

**What is no longer allowed?** Treating the prior recommendation as exhaustively complete.

**What now depends on this choice?** The user gets to choose which completeness level they want.

**What changed in the conceptual model?** Completeness is scope-dependent, not absolute.

---

### Ambiguity 3: Does the user WANT scope expansion to the supplementary loci?

**Strongest counter (yes-expand):** The user's "or different?" invites alternatives; the supplementary loci are alternatives; surface them.

**Strongest counter (no-stay-bounded):** The user originally bounded the territory to 3 docs; respecting that bound is appropriate; don't push expansion they didn't ask for.

**Why neither single-side framing fully succeeds:** "yes-expand" risks imposing scope; "no-stay-bounded" risks hiding information the user might want. The user's question is ambiguous on intent.

**Resolution:** SURFACE the choice. Present the primary recommendation as confirmed-correct AND surface the supplementary loci as optional companions with explicit per-locus reasoning. Let the user pick which to act on. This respects both the user's agency and the surfacing finding's importance.

**Confidence:** HIGH (the surface-the-choice resolution respects both concerns).

**What is now fixed?** The deliverable shape: confirm primary + surface supplementary + let user decide.

**What is no longer allowed?** Pre-committing on the user's behalf in either direction.

**What now depends on this choice?** The deliverable structure (primary + supplementary + user-choice).

**What changed in the conceptual model?** The answer is structured as YES + ALSO HERE ARE OPTIONS.

---

### Ambiguity 4: Is the locus question file-level OR decision-type-level?

**Strongest counter (file-level only):** Locus is about which file gets edited; that's the user's actual operational question.

**Why the counter fails (structural grounds):** `terminology.md`'s declared authority on term definitions makes the locus question partly decision-type-driven. A term-definition decision (like naming "register-as-style" vs "register-as-alternation") belongs in `terminology.md` per the doc's own rule, regardless of which file the broader procedural mechanism lives in. The locus is determined jointly by file-organization AND decision-type. Both axes matter.

**Confidence:** HIGH.

**Resolution:** The locus question has BOTH axes: file-level (which doc gets the edit) and decision-type-level (what kind of decision is being made determines which file is appropriate). For the procedural mechanism: file = `harmony_layer.md` (where the contradiction is + where the pattern fires). For sub-case naming: file = `terminology.md` (where definitions are canonical). For audience-spec config: file = `how_config_should_be.md` (where translation config is set).

**What is now fixed?** Locus is multi-dimensional; each decision-type maps to a different file.

**What is no longer allowed?** Single-file-locus framings.

**What now depends on this choice?** The supplementary-loci recommendations are organized by decision type.

**What changed in the conceptual model?** Locus = (decision-type → file) mapping.

---

### Ambiguity 5: Does the code project need updates as part of this intervention?

**Strongest counter (yes-code-too):** `terminology.md` mentions classes like `TranslationMemory` in `memory.py`. The framework is partly implemented. Fixing the doc without updating the code creates drift.

**Why the counter has weight:** code-doc drift is a real risk in projects with both.

**Why the counter doesn't fully succeed:** The code's tier-system implementation status is unknown — terminology.md describes data structures (Comprehension Index, Prompt View) and pipeline stages, but not specifically a tier-system carrier. The drift risk is speculative-pending-investigation. And: the user's question was scoped to doc-level intervention; engaging with code is out of immediate scope.

**Resolution:** Code-level updates are a FUTURE CONSIDERATION (when the tier-system implementation status is known; when the code is built or being maintained). Flagged for user awareness but not in the immediate intervention scope.

**Confidence:** MEDIUM (the resolution is judgment-dependent on whether the code currently implements the tier system; the cautious path is to defer).

**What is now fixed?** Code-level intervention is FLAGGED, not RECOMMENDED.

**What is no longer allowed?** Treating code-level updates as either fully in-scope or fully ignored.

**What now depends on this choice?** A future-consideration entry in Next Actions / Open Questions.

**What changed in the conceptual model?** Code becomes a flagged future-consideration locus.

---

### Ambiguity 6 (specific-vs-pattern check): Does the locus answer apply only to the specific contradiction OR to the broader pattern?

**Strongest counter (specific-only):** The user named a specific contradiction (register at Tier 3); the answer is specific to that case.

**Strongest counter (pattern):** The prior inquiry 2 surfaced ≥12 instances of the pattern; addressing only one is missing the diagnosed pattern.

**Why neither single-side framing fully succeeds:** The user's question is ABOUT the specific case; but the answer SHOULD address the pattern because the pattern is what the prevention discipline catches.

**Resolution:** The locus answer applies to BOTH. For the specific contradiction: primary locus = `harmony_layer.md` (where the contradiction is). For the pattern: primary locus = `harmony_layer.md` (where the pattern fires; only doc with the principle/classification split). The locus is the same; the case is one instance of the pattern. The answer is unified across both.

**Confidence:** HIGH.

**What is now fixed?** Locus is the same for specific and pattern (`harmony_layer.md` primary).

**What is no longer allowed?** Treating specific and pattern as having different loci.

**What now depends on this choice?** The recommendation handles both at once.

---

### Load-bearing concept tests

**Concept: "Decision-type locus" (decisions land in different docs based on type, not just availability).**
- Counter: maybe all framework decisions could live in one big doc; decision-type-locus is over-abstraction.
- Why counter fails: terminology.md DECLARES its own authority on term definitions. The user has already imposed a decision-type-locus pattern in their own framework. The concept is anchored in the user's own doc-organization, not in sensemaking abstraction.

**Concept: "Doc-stated authority hierarchy."**
- Counter: maybe `terminology.md`'s authority declaration is decorative, not load-bearing.
- Why counter fails: the declaration is in the file's own header text and explicitly resolves cross-doc disagreements ("this file wins"). It's load-bearing.

**Concept: "Framework-knowledge-gap" (prior inquiries treated 3 of 10 docs).**
- Counter: maybe the 3 docs ARE the framework and the others are peripheral.
- Why counter doesn't fully succeed: at least 3 of the 7 additional docs are clearly framework-relevant (`translation_principals.md` is principles; `terminology.md` is canonical terms; `how_config_should_be.md` is config spec). The others may be peripheral, but the core 3-of-7 additional docs are framework-relevant.

**Concept: "YES-WITH-CAVEATS deliverable shape."**
- Counter: maybe a clean YES or NO is what the user wants.
- Why counter fails: the user's question is a frame-check ("or different?"); they're explicitly inviting alternatives. The YES-WITH-CAVEATS shape respects the invitation.

---

### SV4 — Clarified Understanding

The answer to the user's binary question is YES (in-doc edit to `harmony_layer.md` is right for the diagnosed issue) with structural caveats: the recommendation is COMPLETE for the procedural prevention discipline in `harmony_layer.md`, but the surfacing finding revealed supplementary loci (`terminology.md` for sub-case naming per its declared authority; `how_config_should_be.md` for audience-spec config; possibly `translation_principals.md` for principle authority pending investigation; code-level as future consideration). The user decides which supplementary loci to act on. The locus question is multi-dimensional — file-level + decision-type-level + scope-level — and the answer addresses each.

---

## Phase 4 — Degrees-of-Freedom Reduction

### What is now fixed

- The prior recommendation is CORRECT for the diagnosed contradiction (in-doc edit to `harmony_layer.md`).
- The framework includes ~10 docs + code project (not 3 docs as prior inquiries treated).
- Supplementary loci exist where parts of the broader hygiene discipline can land: `terminology.md` (sub-case naming, per its declared authority); `how_config_should_be.md` (audience-spec config); possibly `translation_principals.md` (principle authority pending investigation).
- The EA-7 per-entry trigger fires only in `harmony_layer.md`; other docs lack the structural pattern.
- The deliverable shape is YES-WITH-CAVEATS: confirm primary + surface supplementary + let user decide.
- Code-level updates are FUTURE CONSIDERATION, not immediate-scope.
- "Easy" criterion still applies; supplementary loci are individually cheap.

### What is eliminated

- "The recommendation is wrong" framing.
- "The recommendation is exhaustively complete" framing (ignores supplementary loci).
- "The user must extend to all 10 docs" framing (respects user's original bound).
- "The user must stay bounded to 3 docs" framing (ignores surfacing).
- Single-file-locus framings (the locus is multi-dimensional).
- Pre-committing on the user's behalf about scope.

### What paths remain viable

- **Path A — Minimum (primary only):** edit `harmony_layer.md` per prior inquiry 2's MVD/Full Emergent Assembly. The supplementary loci are noted as future considerations.
- **Path B — Primary + supplementary 1 (terminology):** Path A + add sub-case naming to `terminology.md`. ~5 additional minutes.
- **Path C — Primary + supplementary 2 (config):** Path A + add audience-spec rule to `how_config_should_be.md`. ~5-10 additional minutes.
- **Path D — Primary + investigate translation_principals.md:** Path A + sample `translation_principals.md` to determine if it's the authoritative principles doc; if so, mirror the principles additions there too.
- **Path E — Composite (primary + all supplementary):** A + B + C + D. ~30-45 additional minutes total beyond Path A.
- **Path F — Defer code-level:** all paths flag code-level changes as future consideration; not addressed now.

### SV5 — Constrained Understanding

The solution space is structured around scope choice. Path A is the minimum (matches the prior inquiries' recommendation exactly). Path E is the most complete (touches all surfaced supplementary loci). Paths B / C / D are intermediate. All meet the "easy" criterion individually and as composite. The user picks based on the depth of framework consistency they want to maintain.

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Each perspective in Phase 2 refined the model without forcing replacement. Technical/Logical produced the EA-7 trigger evaluation (confirmed primary locus is structurally correct). Definitional/Internal Consistency produced the "additive not invalidating" framing (resolved the surfacing-vs-prior tension). Frame-exit Completeness produced the multi-value "framework" decomposition. No perspective destabilized the model; each refined it. Accommodation trigger NOT FIRED.

### The stabilized conceptual model

The user's binary question "addition to `harmony_layer.md` OR different?" gets the answer:

**YES, in-doc edit to `harmony_layer.md` is right.** It is the primary intervention locus for the diagnosed tier-system contradiction. The contradiction empirically lives there; the prevention mechanism (per the EA-7 trigger) structurally applies there and only there among the framework docs.

**AND ALSO, supplementary loci exist** that the prior inquiries did not engage with (because they bounded the territory to 3 docs at the user's original instruction). The supplementary loci serve different decision types:

```
Decision type                        Locus                            Why
──────────────────────────────────  ────────────────────────────────  ────────────────────────────────
Procedural prevention (this issue)  harmony_layer.md                 Where the contradiction lives;
                                                                      where the EA-7 trigger fires.
Sub-case term naming                 terminology.md                   Doc declares authority on term
("register-as-style" vs                                               definitions: "this file wins."
 "register-as-alternation")
Audience-spec rule (config)          how_config_should_be.md          Doc is the canonical config-locus
(from prior inquiry 1's S9)                                           for audience-level handling.
Principle authorship                 (translation_principals.md       Investigate first; this file may
(from prior inquiry 1's S2-S10)       OR notes.md)                    be the authoritative principles
                                                                      doc (73K vs notes.md's ~38K).
Code-level tier-system carrier       comprehenslate/ package          FUTURE CONSIDERATION; not in
                                                                      immediate scope.
```

**The user picks the scope.** Path A = primary only (just `harmony_layer.md`); Path B/C/D = primary + one supplementary; Path E = primary + all supplementary. All within "easy" criterion as composite.

### SV6 — Final Stabilized Model

YES, in-doc edit to `harmony_layer.md` is the right intervention for the diagnosed contradiction. The recommendation is structurally correct as the PRIMARY locus.

The recommendation may be INCOMPLETE in scope because surfacing revealed the framework comprises ~10 docs + a code project (not the 3 docs the prior inquiries treated, which was the user's original territory bound). Supplementary loci where parts of the broader hygiene discipline can also land:
- **`terminology.md`** for sub-case naming, per its declared authority on definitions.
- **`how_config_should_be.md`** for the audience-spec rule's config-level component, per its config locus.
- **`translation_principals.md`** for principle authorship — investigate first whether this 73K file is the authoritative principles doc; if yes, prior inquiry 1's added principles may need to mirror there.
- **Code-level** as future consideration when the tier system's implementation status is engaged.

The deliverable shape is YES-WITH-CAVEATS: the user gets a confirmed primary recommendation + a transparent enumeration of supplementary loci + the choice of which to act on. No pre-committing on the user's behalf about scope.

### How SV6 differs from SV1

- **SV1** expected: probably yes, the recommendation is right; alternatives might exist.
- **SV6** delivered: YES, primary recommendation correct; 3-4 supplementary loci surfaced via the framework-knowledge-gap finding; 5-path scope-choice structure; locus is multi-dimensional (file + decision-type + scope); code-level deferred as future consideration. The answer is structured around scope choice, not just yes/no.

### Saturation indicators

- **Perspective saturation:** later perspectives (Definitional/Internal Consistency, Frame-exit Completeness, Phase/Calibration-State) each refined the model rather than introducing new anchor types. Saturation reached.
- **Ambiguity resolution ratio:** 6/6 resolved (5 HIGH, 1 MEDIUM).
- **SV delta:** SV1 → SV6 went from "probably yes" to "yes with multi-axis caveats + scope-choice structure." Healthy delta.
- **Anchor diversity:** spans all five types and 9 perspectives.

### Open frontiers (for downstream stages)

- **F-1** Investigate `translation_principals.md` vs `notes.md` to determine authoritative principles file. Surfacing flagged but didn't resolve.
- **F-2** Whether the cross-doc framework-consistency discipline (consistency across all 10 docs) warrants its own future inquiry. The current inquiry doesn't address it.
- **F-3** Whether the code-level tier-system carrier (if any) needs alignment when the doc fix lands. Future consideration.
- **F-4** Whether `advanced.md`, `my_notes.md`, `roadmap.md`, `README.md` (the docs not yet examined) have any locus relevance for the supplementary discipline. Surfacing did not deep-read.
