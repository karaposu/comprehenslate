# Sensemaking — doc_internal_contradiction_cause_and_prevention

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-04_01-36__doc_internal_contradiction_cause_and_prevention/_branch.md`

Purpose: identify what causes the internal contradiction in `harmony_layer.md` (and the wider pattern of which it's an instance) and design an "easy" preventive mechanism. Inheriting from surfacing: central finding A-20 (the contradiction-pattern is WIDESPREAD across Tier 3 — ≥12 entries share the vulnerable authoring template); A-4 (static-tier-framework vs dynamic-meta-principle mismatch); A-22 (no procedural step linking principle to classifications).

---

## SV1 — Baseline Understanding (pre-analysis)

The user is drilling into one specific watershed finding from the prior inquiry — that `harmony_layer.md` contradicts itself on the register-as-alternation case. They want to understand WHY (cause) and PREVENT recurrence (mechanism), with the explicit "easy" constraint. Initial impression: probably the author wrote the principle abstractly and then made some object-level classifications without checking each one against the principle. Probably the prevention is some kind of cross-check step. Treat that as provisional and let the discipline work shape it.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **CON-1** The contradiction is empirically verifiable from the doc alone: reading the meta-principle and the register-at-Tier-3 classification with the register-as-alternation case in mind reveals the inconsistency. No external evidence needed.
- **CON-2** The contradiction-pattern is WIDESPREAD across Tier 3 — surfacing identified ≥12 entries sharing the same authoring template ("X — [positive aspect] but doesn't [meaning-claim]") and the same vulnerability (universal negative meaning-claim that's false for some sub-case). Not isolated.
- **CON-3** The user's prevention criterion is "easy" — operationalized in _branch.md's goal as: low overhead during normal authoring; user-applicable solo; no new tooling; doesn't require restructuring the doc's existing shape.
- **CON-4** The framework documents are user-maintained; the user authors and edits them directly.
- **CON-5** The doc's existing architecture (tier system with meta-principle + 4-tier classification + per-entry justifications) will not be torn out by this inquiry — the prior inquiry's S7 (tier-system replacement) is parked as RESEARCH FRONTIER specifically because the migration cost is too high for current scope.
- **CON-6** Inheritance from prior inquiry: MVF-4 (the surgical tier fix for the register case specifically) is a planned MUST. This inquiry's prevention mechanism must complement MVF-4, not replace it.

### Key Insights

- **KI-1** The single contradiction the user flagged (register) is ONE INSTANCE of a pattern that runs through nearly every Tier 3 entry. The diagnosis must operate at pattern level, not instance level — addressing only the register case would miss the structural cause.
- **KI-2** Every Tier 3 entry has the form "X — [positive aspect] but doesn't [meaning-claim]" with the negative claim asserted at UNIVERSAL scope. Negative claims at universal scope are particularly contradiction-prone because they invite counter-examples from sub-cases the author didn't enumerate. The authoring template itself is vulnerable.
- **KI-3** The doc states the meta-principle ("closer to meaning = higher tier") and the tier classifications separately, with no required procedural step linking them. The application of the principle to each entry is IMPLICIT — performed by the author in mental working memory at write-time, with no external check. Implicit application is governed by whatever mental model the author was running at write-time; the systematic byproduct is default-case anchoring.
- **KI-4** Default-case anchoring: when the author asked "does X carry meaning?" for each Tier 3 candidate, they probably ran the test on the DEFAULT or TYPICAL case of X (the most common usage). For "register consistency," the typical case is uniform formal/casual register; that case is correctly Tier 3. But sub-cases exist where the feature IS meaning-carrying (register-as-alternation), and those sub-cases got swept into the universal classification.
- **KI-5** The architectural cause is deeper than the procedural one: the meta-principle is CONTEXT-DEPENDENT (meaning-carrying-ness varies by source text), but the tier framework is CONTEXT-FIXED (static categories). The static framework can't directly represent context-dependence, so any single classification will be wrong for some context. This is the static-vs-dynamic mismatch. But: the architectural fix exceeds the "easy" criterion. The procedural fix is within the "easy" criterion.
- **KI-6** The principle-as-statement vs principle-as-test distinction (surfacing F-41) is the conceptual key to easy prevention. A principle stated as text lives in the author's working memory and gets applied implicitly. A principle implemented as a procedural test gets applied at every relevant entry, surviving the author's mental lapses and default-case anchoring. Converting the principle from statement to test is structurally the right intervention at the procedural layer.
- **KI-7** Prevention has two natural deployment modes: retroactive (one-time audit pass over existing Tier 3 entries to catch the ≥12 known contradictions) and prospective (authoring discipline applied to new entries going forward). The same scan-procedure works for both — retroactive is the prospective procedure applied at scale to existing content.

### Structural Points

- **SP-1** The doc has three structural sections relevant to the contradiction: (a) the meta-principle statement, (b) the four tier definitions (each tier's abstract characterization), (c) the per-component lists with justifications. The contradiction lives in (c); the principle that's violated lives in (a); the link between them is implicit.
- **SP-2** Tier 1 and Tier 2 entries follow a POSITIVE-claim pattern ("X — because [reason for meaning-carrying]"). The justifications are positive assertions of meaning-relevance. Lower contradiction-vulnerability.
- **SP-3** Tier 3 entries follow a NEGATIVE-claim pattern ("X — [positive aspect] but doesn't [meaning-claim]"). The justifications contain universal negative claims. Higher contradiction-vulnerability — every entry is one counter-example away from contradicting the doc's own ranking principle.
- **SP-4** Tier 4 entries follow a TECHNICAL-INFEASIBILITY pattern ("X — language-specific" / "untranslatable"). Different vulnerability shape; not directly comparable to Tier 3.
- **SP-5** The doc has no end-of-doc audit step or consistency-check pass. The doc's process model governs translation execution (3-pass), not doc-authoring.

### Foundational Principles

- **FP-1** A principle stated as advice functions differently from a principle implemented as a test. Stated-principles live in the author's working memory at write-time; tested-principles get applied procedurally. Documents that rely on stated-principles for consistency are vulnerable to the author's mental lapses and default-case anchoring.
- **FP-2** Static categorical frameworks cannot directly represent context-dependent properties. When the property is context-dependent but the categorical framework is static, the framework either (a) accommodates context-dependence via sub-case decomposition (each context becomes its own sub-category) OR (b) fails for non-default contexts. The accommodation is the engineering fix; the failure is the default.
- **FP-3** Negative claims at universal scope ("X doesn't do Y") are particularly contradiction-prone in technical documents because they invite counter-example. Defensive authoring scopes negative claims explicitly ("X doesn't do Y in case Z; in case W, X does do Y").
- **FP-4** Prevention mechanisms designed for "easy" application must respect specific constraints: low per-instance cost, no new tooling, user-solo-applicable, structurally non-disruptive to the existing doc. Heavier mechanisms (review workflows, automated consistency checkers) are out of scope.

### Meaning-Nodes

- **MN-1** Principle-as-statement vs principle-as-test
- **MN-2** Default-case anchoring (cognitive pattern producing universal-from-typical generalizations)
- **MN-3** Sub-case blindness (failure to enumerate sub-cases before classifying a category)
- **MN-4** Static-vs-dynamic mismatch (architectural cause)
- **MN-5** Negative-claim-at-universal-scope (the vulnerable authoring template at Tier 3)
- **MN-6** EXCEPT-WHEN clause (a mechanism that scopes negative claims)
- **MN-7** End-of-doc audit (one-pass scan for contradiction patterns)
- **MN-8** Counter-example seeking (per-entry authoring discipline)
- **MN-9** Widespread contradiction pattern (the fact that ≥12 Tier 3 entries share the same vulnerability)

### Meta-inspection after SV2 — H4 (concept names) and H5 (motivating examples)

- H4: concept-names introduced (principle-as-statement vs principle-as-test, default-case anchoring, sub-case blindness, etc.) are each grounded in either observable doc properties (the doc's structure verifies them) or established cognitive/specification-design literature. Real distinctions, not artifactual.
- H5: motivating examples = the register case (specific instance) + ≥12 Tier 3 entries (the pattern). Specific-vs-pattern flagged; addressed in Phase 3 (Ambiguity 4).

### SV2 — Anchor-Informed Understanding

The shape sharpens. The contradiction the user flagged is one instance of a widespread pattern (≥12 Tier 3 entries share the same vulnerability). The cause is multi-layer: a procedural cause (no required step links the meta-principle to per-entry classifications; implicit application produces default-case anchoring) and an architectural cause (static framework can't represent context-dependent principle). The procedural cause is fixable within the "easy" criterion; the architectural cause exceeds it (and is parked as the prior inquiry's RESEARCH FRONTIER). Prevention candidates concentrate around making the implicit application explicit: principle-as-test, EXCEPT-WHEN clauses, end-of-doc audit, counter-example seeking.

---

## Phase 2 — Perspective Checking

### Technical / Logical

The static-vs-dynamic mismatch is a genuine architectural issue. Even with a perfect author, a static framework cannot represent a context-dependent property without sub-case decomposition. **New anchor:** the framework CAN accommodate context-dependence via sub-case splits (each context becomes its own sub-classification). This is additive — it doesn't tear out the existing tier system; it refines individual entries. The architectural fix is therefore on a spectrum: light (sub-case splits per entry as needed) to heavy (full reorganization around context-aware classification). The light end fits the "easy" criterion.

### Human / User

The user wants "easy" prevention they can apply during normal authoring. They author the framework themselves. **New anchor:** the prevention's effectiveness depends on whether the user actually applies it during real authoring sessions. Mechanisms that require a separate review step (heavy cognitive switch) are less likely to be applied than mechanisms embedded in the writing flow itself. EXCEPT-WHEN clauses and per-entry test-application are embedded; end-of-doc audit is a separate step. Both have value; sequencing matters.

### Strategic / Long-term

If the prevention mechanism is applied prospectively (only to new entries), existing contradictions remain. If applied retroactively (to clean up existing Tier 3 entries), the doc gets a sweep through ≥12 entries, each potentially requiring sub-case decomposition. **New anchor:** the retroactive sweep IS the same procedure as the prospective audit. One-time application of the audit catches all current contradictions; ongoing application catches new ones. Retroactive sweep is bounded effort (≥12 entries × small effort per entry = manageable).

### Risk / Failure

- Risk A: the prevention mechanism is too cognitively heavy → user skips it → contradictions persist. Mitigation: prefer the lightest mechanism with adequate coverage.
- Risk B: prevention catches false positives (flags non-contradictions) → user ignores it → real contradictions slip through. Mitigation: the mechanism's signal-to-noise ratio must be high; vague "be careful" rules produce false positives.
- Risk C: prevention catches explicit contradictions but misses subtle ones. Mitigation: prevention covers the dominant pattern (universal negative claims); subtle cases need different mechanisms outside this inquiry's scope.
- Risk D: applying prevention retroactively cascades into a doc-rewrite. Mitigation: the retroactive sweep is bounded to ≥12 Tier 3 entries; not a doc-wide rewrite.

**New anchor:** the prevention's failure modes are themselves predictable, which means they can be designed against.

### Resource / Feasibility

| Candidate mechanism | Per-entry cost | Setup cost | Retro-applicable? | Easy criterion fit |
|---|---|---|---|---|
| EXCEPT-WHEN clause requirement | medium (must construct sub-case) | low (one rule) | yes (retro sweep) | medium-high |
| End-of-doc audit pass | none per-entry; ~5-15 min per audit | low (one procedure) | yes (one-time sweep) | high |
| Principle-as-test per entry | low (one sentence) | low (one rule) | yes | high |
| Counter-example seeking per entry | low-medium (mental check) | low | yes | medium-high |
| Sub-case decomposition required | high (real structural work) | low (one rule) | yes but expensive | medium |

**New anchor:** the cheapest-and-coverage-adequate combination is end-of-doc audit + principle-as-test per entry. EXCEPT-WHEN clauses are valuable but heavier; sub-case decomposition is for cases where audit/test reveals it's needed (on-demand, not by default).

### Ethical / Systemic

No ethical concerns. The framework is user-controlled; the prevention applies only to the user's own authoring.

### Definitional / Internal Consistency

The doc's meta-principle is itself context-conditional ("closer to meaning-carrying" varies by what the text does), but the tier framework treats meaning as context-independent (each feature is in one tier permanently). This is a definitional gap inside the doc. The contradiction the user flagged is one instance of the gap manifesting. The other Tier 3 entries are other instances of the same gap. The gap is the cause; the contradictions are symptoms. **New anchor:** the cause is one underlying gap, not 12 separate mistakes.

### Definitional / Frame-exit Completeness

Gating predicate: does the inquiry's frame inherit multi-value terms used across distinct propositions? Yes — "tier," "principle," "classification," "contradiction" are all used at multiple levels with distinct propositions.

**Existence enumeration for "tier":**
- (a) Tier 1/2/3/4 as static categories in `harmony_layer.md`
- (b) Tier as conceptual rank (the abstract notion of priority)
- (c) Tier as classification verdict (what the author commits per entry)
- (d) Tier in the abstract sense the meta-principle generates (the principle says "higher tier" without committing to a specific structure)

The inquiry's frame addresses (a) through (d) coherently within harmony_layer.md's existing tier system. No referent is excluded that the inquiry's coherence depends on.

**Role assessment:** all referents in scope.

**Verdict rigor:** the clean boundary between "easy prevention" (this inquiry's scope) and "architectural redesign" (out of scope; the prior inquiry's RESEARCH FRONTIER) is challenged by — what if no easy prevention adequately addresses the widespread pattern? Response: the procedural fix (principle-as-test + audit) doesn't require the architectural fix to be effective; it catches the symptom (contradictions) directly. The architectural fix remains the long-term ideal; the procedural fix is sufficient for "easy." Boundary survives.

**Residual:** no additional frame-exit concerns. Terminating recursion.

### Phase / Calibration-State

The framework is in early-development calibration state. Most Tier 3 entries were authored without specific cases having been tested. The contradictions only emerged when specific corpus encounters (e.g., Said Nursi's Risale-i Nur with register alternation) collided with the universal negative claims. **New anchor:** the framework's maturity affects prevention design — early-stage prevention must be lightweight because the framework hasn't yet accumulated enough use to justify heavier mechanisms. As the catalog of detected contradictions grows (the prior inquiry's EA-6 failure-modes catalog being one mechanism for this), prevention can evolve.

### Meta-inspection after SV3

- H1 (candidate set): the prevention candidates are EXCEPT-WHEN, end-of-doc audit, principle-as-test, counter-example seeking, sub-case decomposition. Are we missing types? Considering: automated tooling (scripts to scan docs) — excluded by "easy"; AI-assisted review — excluded by user-solo-applicable criterion; per-PR review process — excluded by user-solo-applicable. Candidate set adequately covers the lightweight space.
- H2 (frame scope): handled by Frame-exit Completeness.
- H3 (question framing): the user's phrasing "prevent this" is ambiguous between specific instance and pattern. Surfacing's FF-1 flagged this. Resolved in Phase 3 (Ambiguity 4) toward pattern-level.
- H7 (phase/calibration-state): handled above.
- H8 (self-reference): sensemaking concepts (anchors, principles, structure) overlap with framework concepts. External grounding via empirical verifiability: anyone can read the doc and see the contradictions. Self-reference risk is checked.

### SV3 — Multi-Perspective Understanding

The diagnosis is clearer. The cause is a single underlying gap (the meta-principle is stated separately from its application, with no procedural link, and the architecture is static where the principle is dynamic). This single gap manifests as ≥12 contradictions across Tier 3 entries. Prevention is feasible at the "easy" level: convert the principle from statement to test (per-entry), and add an end-of-doc audit (one-time sweep + ongoing). Architectural redesign remains the long-term ideal but is out of scope. Retroactive cleanup is bounded effort (≥12 entries). The prevention candidates cluster around making implicit application explicit.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: Is the cause primarily the AUTHOR (cognitive lapse) or the FRAMEWORK ARCHITECTURE (structural)?

**Strongest counter-interpretation:** the author wrote the doc and didn't think carefully enough about each Tier 3 entry. With a more careful author, the contradictions wouldn't have happened. The cause is personal, not structural.

**Why the counter fails (structural grounds):** the contradiction-pattern is WIDESPREAD — surfacing identified ≥12 Tier 3 entries sharing the same vulnerability shape. A careful author makes occasional mistakes; a pattern that runs through nearly every entry in a section indicates the structural shape of authoring made the mistake easy and systematic. Cognitive psychology supports this: default-case anchoring is a well-documented heuristic. Anyone authoring under the doc's existing architecture would produce the same kind of pattern. Plus: the absence of a procedural step linking the meta-principle to per-entry classifications (A-22 from surfacing) is an architectural feature, not a personal failing. The author was operating without a check the architecture should have provided.

**Confidence:** HIGH (≥12 instances is structural evidence; cognitive-psychology backing on default-case anchoring; observable architectural absence).

**Resolution:** the cause is **structural-procedural**. The author is a victim of the architecture, not the source of the bug. Prevention must target the architecture or the procedure, not the author's care.

**What is now fixed?** Cause is at the doc-authoring-process level, not the personal level. Prevention design proceeds accordingly.

**What is no longer allowed?** "Just be more careful" framings.

**What now depends on this choice?** All prevention recommendations target structural-procedural mechanisms.

**What changed in the conceptual model?** The diagnosis becomes structural; the prevention becomes mechanism-design.

---

### Ambiguity 2: Is "easy prevention" possible at all, or is the contradiction-vulnerability inherent to static classification systems (requiring architectural redesign)?

**Strongest counter-interpretation:** the only real fix is architectural — replace the static tier system with a context-aware classification scheme. Anything lighter is symptom treatment that leaves the underlying mismatch in place.

**Why the counter fails (structural grounds):** prevention doesn't need to ELIMINATE the architectural mismatch — it needs to CATCH the specific contradictions at authoring time before they ship. An end-of-doc audit and per-entry test-application catch each contradiction as it arises, without requiring the architectural overhaul. The architectural redesign (the prior inquiry's S7) is the right long-term direction; the easy prevention is the right short-term mitigation. They coexist: one prevents new contradictions immediately, the other (eventually) eliminates the architectural cause. Mechanism: per-entry test forces the author to enumerate context cases (does this feature carry meaning IN ALL CONTEXTS, IN NO CONTEXTS, or IN SOME CONTEXTS?); the third answer triggers sub-case decomposition for that specific entry. The architectural mismatch is bypassed via on-demand sub-case decomposition rather than systemic redesign.

**Confidence:** HIGH (the procedural fix is independent of the architectural one; the prior inquiry already adjudicated S7 as out of scope; mechanism preserves the existing doc shape).

**Resolution:** **easy prevention IS possible**; it doesn't replace the architectural fix but provides immediate value at low cost. The architectural fix remains a long-term RESEARCH FRONTIER (inherited from the prior inquiry).

**What is now fixed?** "Easy prevention" is a viable category of intervention; doesn't require waiting for the architectural fix.

**What is no longer allowed?** "Only architectural redesign works" framings.

**What now depends on this choice?** Prevention recommendations focus on lightweight per-entry and per-doc mechanisms.

**What changed in the conceptual model?** Procedural and architectural fixes are independent; the user can pursue procedural now and architectural later.

---

### Ambiguity 3: Does prevention apply RETROACTIVELY to existing entries or PROSPECTIVELY to new ones?

**Strongest counter-interpretation (retroactive-only):** the existing Tier 3 entries already contain ≥12 contradictions; without retroactive cleanup, the doc remains broken even if new entries are perfect.

**Strongest counter-interpretation (prospective-only):** retroactive cleanup requires rewriting ≥12 Tier 3 entries; that violates "easy."

**Why both single-sided framings fail:** retroactive-only doesn't prevent FUTURE contradictions in new entries; prospective-only leaves the current ones unchecked. The procedural mechanism (principle-as-test + audit) is the SAME procedure either way — applied to a new entry as it's authored, or applied to an existing entry during a sweep. Retroactive application is bounded effort: ≥12 entries × small effort per entry = ~30-60 minutes of focused work. That fits the "easy" criterion as a one-time cleanup. Prospective application is ongoing.

**Confidence:** HIGH (the procedure is shape-symmetric; retroactive effort is bounded; both modes are needed).

**Resolution:** **both apply, in different deployment modes**. Prospective: an authoring discipline applied to new entries. Retroactive: a one-time audit pass over existing Tier 3 entries.

**What is now fixed?** Prevention has both prospective and retroactive applications; both are within "easy."

**What is no longer allowed?** Single-mode framings.

**What now depends on this choice?** Recommendations include both an authoring-discipline (prospective) and a one-time-sweep (retroactive).

**What changed in the conceptual model?** The prevention is two-faced — the same mechanism, applied at two times.

---

### Ambiguity 4 (specific-vs-pattern check, per the cue): Is the user asking about THIS specific contradiction (register) or about the PATTERN it illustrates?

**Strongest counter-interpretation (specific-only):** the user's input says "lets dive deeper on this" and "prevent this" — referring grammatically to "this contradiction." Singular.

**Why the counter fails (structural grounds):** the user's goal in _branch.md is "knowing the cause + having an easy mechanism." A cause specific to one classification (register at Tier 3) is useless without generalization — the cause is the same for the other ≥11 contradictions surfacing identified. A prevention that catches only one specific contradiction is pointless once the surgical fix (the prior inquiry's MVF-4) is applied. The "easy way to prevent this" phrasing logically implies a mechanism that PREVENTS occurrences, plural — and "this" reads naturally as "this kind of contradiction." Plus: surfacing's central finding (A-20) is that the pattern is widespread, providing empirical grounding for pattern-level diagnosis.

**Confidence:** HIGH (the goal text logically requires generalization; surfacing's pattern finding is corroborated by ≥12 instances).

**Resolution:** **BOTH**. The specific contradiction is the worked example exposing the pattern; the broader pattern is what cause and prevention must address.

**What is now fixed?** Diagnosis and prevention both operate at pattern level; the register case is the worked example, not the whole scope.

**What is no longer allowed?** Treating this as a one-instance issue.

**What now depends on this choice?** Recommendations must address the widespread pattern, not just register.

**What changed in the conceptual model?** The scope of diagnosis and prevention is pattern-level.

---

### Ambiguity 5: What does "easy" mean operationally?

**Strongest counter-interpretation:** "easy" is too vague to make load-bearing decisions. Without a concrete threshold, the discipline can rationalize any mechanism as "easy."

**Why the counter fails (structural grounds):** "easy" is concretely scoped by the user's stated use case in _branch.md's goal — "applicable during normal authoring without heavy investment." Operationalize via the user's context: the user maintains the framework solo; doesn't have setup overhead for new tooling; can't switch to a heavy review workflow per edit. From these, "easy" decomposes into concrete criteria:
- Per-entry cost ≤ ~2 minutes of additional authoring effort
- Per-audit cost ≤ ~15 minutes for a one-time sweep
- No new tooling, scripts, or external dependencies
- User-solo-applicable (no review partner required)
- Doesn't restructure the existing doc shape

**Confidence:** MEDIUM (the criteria are concrete but the precise thresholds are judgment-dependent; the criteria are defensible).

**Resolution:** "easy" = the five concrete criteria above. Each prevention candidate is scored against them.

**What is now fixed?** "Easy" has concrete operational meaning, enabling discrimination among candidates.

**What is no longer allowed?** Rationalizing heavy mechanisms as "easy."

**What now depends on this choice?** Critique will use these criteria as evaluation dimensions.

**What changed in the conceptual model?** "Easy" is now a measurable criterion.

---

### Ambiguity 6: Is the deeper cause "principle-as-statement vs principle-as-test" (procedural) or "static-vs-dynamic architecture" (structural)?

**Strongest counter-interpretation:** both are real but only one is the TRUE cause; the other is downstream. Either the procedural choice generates the architecture (statement-not-test → static), or the architectural choice generates the procedure (static → can't be tested dynamically).

**Why the counter fails (structural grounds):** the two causes are STACKED, not in competition. The procedural cause ("principle-as-statement-not-test") is the immediate write-time mechanism that produces individual contradictions; the architectural cause ("static-framework-can't-represent-dynamic-principle") is the underlying conceptual mismatch that makes the procedural cause's effects systematic rather than random. Removing the procedural cause (by making principle-as-test) blocks new contradictions but leaves the architectural mismatch. Removing the architectural cause (by redesigning the framework) blocks contradictions at the root but requires migration. They operate at different layers; both are real causes; neither subsumes the other.

**Confidence:** HIGH (layer separation is well-defined; both causes have independent empirical evidence — the procedural cause from A-22, the architectural cause from A-4).

**Resolution:** **two-layer cause**. Procedural cause is the in-scope target for "easy" prevention; architectural cause is the out-of-scope long-term direction (the prior inquiry's S7).

**What is now fixed?** Cause has two layers; prevention operates at the procedural layer.

**What is no longer allowed?** Single-layer cause framings.

**What now depends on this choice?** Prevention is procedural; the architectural item remains in research frontier.

**What changed in the conceptual model?** Cause becomes a two-layer stack: procedural amplified by architectural.

---

### Load-bearing concept test (per the refinement note)

**Concept: "principle-as-statement vs principle-as-test."** Real structural distinction or convenient label?
- Counter: maybe the distinction is too abstract; the practical difference is just "say it more carefully."
- Why counter fails: the distinction is grounded in observable doc properties — the doc has the principle as a sentence (statement) and has no procedural step that runs it as a test (no test-application). Plus the distinction maps onto established practices in specification design (specification languages distinguish "axiom" from "verified property"). Real and grounded.

**Concept: "default-case anchoring."** Real cognitive pattern or speculation?
- Counter: maybe the author just chose the wrong tier; no need to invoke a heuristic.
- Why counter fails: ≥12 entries all chose the same kind of wrong-for-sub-case classification, all following the same "doesn't [meaning-claim]" template. The pattern is too systematic for random choice. Default-case anchoring is established in cognitive psychology (Tversky-Kahneman representativeness heuristic). The pattern fits the heuristic; the heuristic predicts the pattern.

**Concept: "widespread contradiction pattern."** Established or merely asserted?
- Counter: maybe surfacing only checked a few entries; the pattern might not extend across all of Tier 3.
- Why counter fails: surfacing examined all 12 Tier 3 entries individually (A-8 through A-19) and named the specific counter-case for each. The pattern is empirically demonstrated, not asserted.

**Concept: "end-of-doc audit."** Real mechanism or generic advice?
- Counter: "audit the doc" is vague; what's the specific procedure?
- Why counter fails: the audit has a specific operational form — scan for "doesn't [X]" universal-negative claims; for each, attempt to construct a counter-case; if a counter-case exists, the claim must be scoped. The procedure is reproducible.

### Specific-vs-pattern check (Ambiguity 4 above)

Resolved at pattern level. The register case is one example; the diagnosis and prevention target the pattern.

### SV4 — Clarified Understanding

The diagnosis stabilizes as a two-layer cause stack: procedural cause (principle-as-statement-not-test, producing default-case anchoring at write-time) amplified by architectural cause (static-vs-dynamic mismatch, making the procedural cause's effects systematic across the Tier 3 section). The procedural cause is in scope for "easy" prevention; the architectural cause is the prior inquiry's parked research frontier. Six ambiguities resolved (5 HIGH, 1 MEDIUM). Load-bearing concepts tested and confirmed. Prevention is two-faced (prospective + retroactive) and concentrated on lightweight mechanisms: principle-as-test per entry, EXCEPT-WHEN clauses for negative claims, end-of-doc audit. Heavier mechanisms (sub-case decomposition on every entry) are reserved for entries where the audit reveals the need.

---

## Phase 4 — Degrees-of-Freedom Reduction

### What is now fixed (locked anchors)

- The contradiction-pattern is widespread across Tier 3 (≥12 instances surfaced).
- The cause is structural-procedural (not personal carelessness): implicit application of the meta-principle, governed by default-case anchoring at write-time.
- The cause has two stacked layers: procedural (in-scope for prevention) + architectural (out of scope; long-term).
- Easy prevention is possible at the procedural layer.
- Prevention applies in two deployment modes (prospective + retroactive); same procedure either way.
- "Easy" means: ≤2 min per entry; ≤15 min per audit; no new tooling; user-solo-applicable; preserves doc shape.
- The architectural cause is inherited from the prior inquiry's S7 RESEARCH FRONTIER; this inquiry does not address it.

### What is eliminated (no longer viable interpretations)

- "Just be more careful" framings.
- "Only architectural redesign fixes this" framings.
- Single-instance scope (preventing only the register contradiction).
- Heavy prevention mechanisms (review workflows, automated tooling, AI-assisted consistency checking).
- Single-mode prevention (prospective-only or retroactive-only).

### What paths remain viable

- **P-1: Principle-as-test per entry.** Authoring discipline: for each new tier classification, explicitly apply the meta-principle as a test; record the answer.
- **P-2: EXCEPT-WHEN clauses for negative claims.** When a justification asserts "X doesn't do Y," require completion of "EXCEPT WHEN [sub-case]" or explicit "always; no exception exists because [reason]."
- **P-3: End-of-doc audit.** One-pass scan procedure: find all universal negative claims; for each, attempt counter-case construction; if successful, scope the claim or split into sub-cases.
- **P-4: Counter-example seeking per entry (lighter version of P-1).** Briefer authoring discipline: for each entry, briefly ask "can I think of a case where this classification would be wrong?"
- **P-5: On-demand sub-case decomposition.** When audit (P-3) reveals a contradiction, split the entry into sub-cases with separate classifications. Heavier; only triggered as needed.

### SV5 — Constrained Understanding

The solution space is structured. P-3 (end-of-doc audit) is the cheapest and broadest; P-1 (principle-as-test) is the embedded authoring version; P-2 (EXCEPT-WHEN) is the explicit-scope version; P-4 is the lightweight authoring discipline; P-5 is the on-demand sub-case fix triggered by P-3. They compose: P-1 + P-3 covers most cases (per-entry test + one-pass audit); P-2 sharpens individual entries; P-5 fires when audit finds positive contradictions. The recommended composite is P-1 + P-3 with P-5 on demand.

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Each perspective in Phase 2 refined the model without forcing replacement:
- Technical/Logical: refined toward "the framework can accommodate context-dependence via sub-case decomposition" (additive, not architectural overhaul).
- Human/User: refined toward "mechanisms embedded in writing flow > separate review steps."
- Strategic/Long-term: refined toward "retroactive sweep + prospective discipline together."
- Risk/Failure: refined toward "design the mechanism against its own failure modes."
- Resource/Feasibility: refined toward "cheapest combo is audit + per-entry test."
- Ethical/Systemic: no refinement needed.
- Definitional/Internal Consistency: produced the "single underlying gap manifests as N contradictions" framing.
- Frame-exit Completeness: refined the architectural-vs-procedural boundary.
- Phase/Calibration-State: refined toward "early-stage prevention is necessarily lightweight."

No perspective forced model REPLACEMENT. Model is stable.

### The stabilized conceptual model

**Cause (two layers, stacked):**

```
Layer 1 — Procedural (in-scope for prevention):
   The doc states the meta-principle and the tier classifications separately,
   with no required procedural step linking them.
   
   The application of the principle to each classification is IMPLICIT —
   performed by the author in mental working memory at write-time,
   without an external check.
   
   Implicit application is governed by DEFAULT-CASE ANCHORING:
   the author runs the principle on the typical/default case of each feature
   and produces a universal classification from a typical result.
   
   Result: ≥12 Tier 3 entries with negative meaning-claims at universal scope
   that fail for non-default sub-cases.
   
Layer 2 — Architectural (out of scope; inherited from prior inquiry's RESEARCH FRONTIER):
   The meta-principle is CONTEXT-DEPENDENT
   (meaning-carrying-ness varies by source text).
   The tier framework it generates is CONTEXT-FIXED
   (static categories that don't represent context).
   
   The architectural mismatch makes the procedural cause's effects
   SYSTEMATIC rather than random — any default-case anchoring produces
   a wrong-for-non-default classification, because the static framework
   cannot represent the non-default contexts at all.
   
   The architectural fix (S7 in the prior inquiry) is the long-term
   right answer; the procedural fix is the immediate one.
```

**Prevention (procedural, easy, two deployment modes):**

The procedural fix converts the meta-principle from a STATEMENT into a TEST that runs at every tier classification.

- **Prospective deployment (authoring discipline):** for each new tier classification, the author runs a one-line test: "By the meta-principle, does this feature carry meaning? Always / Sometimes (in what cases?) / Never?" If "Sometimes," the entry must split into sub-cases with separate tier assignments, OR add an EXCEPT-WHEN clause naming the sub-case, OR be re-stated as context-conditional.
- **Retroactive deployment (one-time audit pass):** sweep the existing Tier 3 section. For each entry containing a "doesn't [meaning-claim]" universal-negative assertion, attempt to construct a counter-case where the claim fails. If a counter-case is found, the entry is split or scoped. The sweep is bounded effort (~30-60 minutes for the ≥12 Tier 3 entries).

Both deployments use the same operational procedure. The mechanism meets the "easy" criteria: per-entry test ≤2 min; full audit ≤15-60 min one-time; no tooling; user-solo; preserves doc shape (adds clauses or sub-case splits within the existing structure).

**SV6 — Final Stabilized Model**

The contradiction in `harmony_layer.md` between the register-at-Tier-3 classification and the doc's own ranking principle is one instance of a widespread pattern: ≥12 Tier 3 entries share the same vulnerable authoring template (universal negative meaning-claims with no scope-qualifier) and would each contradict the ranking principle on appropriate sub-cases.

The cause is a two-layer stack: a procedural cause (the meta-principle is stated separately from its application with no required linking step, so the application is implicit and governed by default-case anchoring) amplified by an architectural cause (the framework's static-classification design cannot directly represent the meta-principle's context-dependent nature; this makes the procedural cause's effects systematic rather than random). The architectural cause is inherited from the prior inquiry's S7 RESEARCH FRONTIER and is out of scope for this inquiry's "easy" criterion.

Prevention is feasible at the procedural layer and meets the "easy" criterion via two mechanisms in one operational procedure: (a) principle-as-test per new entry (prospective authoring discipline; ≤2 min per entry) and (b) end-of-doc audit pass (retroactive sweep + ongoing maintenance check; ≤15-60 min per audit). When the audit or per-entry test reveals a contradiction, the entry is fixed by splitting into sub-cases OR adding EXCEPT-WHEN clauses OR being re-stated as context-conditional.

### How SV6 differs from SV1

- **SV1** expected: probably the author wrote the principle abstractly and made some object-level mistakes; probably some cross-check step prevents.
- **SV6** delivered: the contradiction is one of ≥12 in a widespread pattern; the cause is structural-procedural (default-case anchoring under implicit application); the cause is amplified by an architectural mismatch (in scope of the prior inquiry's research frontier, not this one); prevention is a two-faced procedure (prospective + retroactive) that converts the meta-principle from statement to test; the procedure meets concrete "easy" criteria.

### Saturation indicators

- **Perspective saturation:** the late perspectives (Resource/Feasibility, Definitional/Internal Consistency) produced refinement (composite-mechanism selection; single-gap framing) rather than new anchor types. Saturation reached.
- **Ambiguity resolution ratio:** 6/6 resolved (5 HIGH, 1 MEDIUM).
- **SV delta:** SV1 → SV6 shows clear structural shift — from "probably author + cross-check" to "two-layer cause stack with concrete procedural fix and architectural fix deferred." Healthy delta.
- **Anchor diversity:** anchors span all five types (constraints, key insights, structural points, foundational principles, meaning-nodes) and 9 perspective categories. Strong.

### Open frontiers (for downstream stages)

- **F-1** Whether prevention should be embedded into harmony_layer.md itself (as a procedural section) or maintained as an external authoring discipline. Sense-making did not adjudicate this; innovation can.
- **F-2** Whether to perform the retroactive sweep as part of this inquiry's deliverable OR to defer it as user-action. Either is viable; decision depends on user's available time.
- **F-3** Whether the prevention mechanism should be generalized to `notes.md` and `advanced_principles.md`. Surfacing flagged that they have different doc shapes with different vulnerabilities; prevention may need shape-specific variants. Sense-making did not address.
- **F-4** Whether the principle-as-test framing should be extended to OTHER principles in the framework (not just `harmony_layer.md`'s ranking principle). The framework has multiple meta-principles scattered across the three docs. Generalization is plausible but out of immediate scope.
