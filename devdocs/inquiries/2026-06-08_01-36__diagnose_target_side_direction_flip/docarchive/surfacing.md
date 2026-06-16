# Surfacing — diagnose_target_side_direction_flip

## User Input
`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-08_01-36__diagnose_target_side_direction_flip/_branch.md`

---

## Mode + Entry Point

- **Mode:** mixed (`artifact` — existing framework artifacts to enumerate; `possibility` — candidate failure-mode names + candidate prevention mechanisms + candidate fix locations)
- **Entry-point:** `signal-first` (specific purpose: diagnose target-side direction-flip failure mode)
- **Territory:** `explicit-bounded` (5 artifacts: `harmony_layer.md`, `notes.md`, `advanced_principles.md`, `config_base_source.md` canonical Layer 1 spec v1.0, `translation_principals.md`; + the specific translation `4_mesele_en.md` containing the failure)
- **Boundary-discovery sub-phase:** skipped
- **Prior-artifact:** none
- **Prior-workspace:** none

---

## Traversal Trace

### Region 1: The specific failure (anchor case)

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 1.1 | Source phrase `Herkesin İman mukabilinde... Davası başına açılmış` | core | HIGH | the actual Turkish |
| 1.2 | Source meaning: "with each person's Faith put up as the counter-stake, a Case (=lawsuit) has been opened" — barter/courtroom metaphor | core | HIGH | |
| 1.3 | `mukabil` = facing / in-exchange-for / put-up-against / counter-stake (NOT in-opposition-to) | core | HIGH | the load-bearing lexeme |
| 1.4 | Target rendering: `set against his Faith` | core | HIGH | the actual English |
| 1.5 | Target's PRIMARY natural English reading: "in opposition to / hostile to his Faith" | core | HIGH | the false reading |
| 1.6 | Target's SECONDARY natural English reading: "with his Faith as the counter-stake" (barter sense, but minority reading in English) | sub | HIGH | the intended-but-buried reading |
| 1.7 | The error vector: target rendering opened a sense (oppositional) the source does not admit | core | HIGH | the failure-mode signature |
| 1.8 | The OPPOSITE-direction property: not just "ambiguous" but "ambiguous in the OPPOSITE direction" | core | HIGH | this is what makes it bad vs. tolerable |
| 1.9 | The English idiom that did the damage: phrasal preposition "set against" — has dual senses, one of which is the inverse | core | HIGH | |
| 1.10 | The error is NOT at Pass 1 Meaning Lock — `mukabil` was correctly understood | core | HIGH | rules out source-side comprehension failure |
| 1.11 | The error IS at Pass 3 Target Reconstruction — chosen target phrase admitted unintended sense | core | HIGH | locates the failure in the methodology |

### Region 2: harmony_layer.md — what's there + what's missing

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 2.1 | 3-Pass methodology: Pass 1 Meaning Lock → Pass 2 Harmony Map → Pass 3 Target Reconstruction | core | HIGH | the operational frame |
| 2.2 | Pass 3 rule: "you may change HOW a meaning is expressed, but never WHAT meaning is expressed" | core | HIGH | the canonical check — but it MISSED this case |
| 2.3 | Hard constraint: "Anything that changes semantic content is forbidden" | core | HIGH | could have caught it if interpreted maximally |
| 2.4 | Hard constraint: "Adding information not present in the original is forbidden" | core | HIGH | KEY ITEM — opening an opposite-sense reading IS adding information (negation) that wasn't in source |
| 2.5 | Hard constraint: "Removing information present in the original is forbidden" | core | HIGH | |
| 2.6 | Tier 1 entry: "Cause-effect chaining — because reversing or obscuring causality changes what the text argues" | sub | HIGH | adjacent but not this case — that's about source-side causality |
| 2.7 | Tier 1 entry: "Antonym pairing — because contrast pairs define each other" | sub | HIGH | adjacent — about source-side contrast structure |
| 2.8 | Tier 4 entry: "Genre convention adherence — this should actually follow the TARGET language's genre conventions" | sub | HIGH | this is the only mention of target-language sensitivity, but it's about genre not semantics |
| 2.9 | Pass 3 permitted operations list ("Choosing between synonyms... adjusting word order...") | core | HIGH | the list of what Pass 3 CAN do — but NO forbidden-list for Pass 3 specifically |
| 2.10 | **GAP**: hard constraints address SOURCE-side preservation; no explicit constraint about TARGET-side accidental sense addition | core | HIGH | the structural gap |
| 2.11 | **GAP**: 3-Pass methodology checks "did Pass 3 preserve the source meaning?" but not "does Pass 3's target rendering open a reading source doesn't admit?" | core | HIGH | the check is unidirectional |
| 2.12 | **GAP**: no Pass 4 "Reverse-Read check" — read the target as if you don't know the source, see what readings it admits | core | HIGH | candidate prevention mechanism |
| 2.13 | "How the system works in practice": tier-conflict adjudication described, but only for source-internal conflicts | sub | HIGH | doesn't cover source-vs-target false-friend |

### Region 3: notes.md — what's there + what's missing

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 3.1 | "On a single word carrying multiple valid readings simultaneously" (din = judgment + religion) | core | HIGH | SOURCE-side multi-meaning preservation |
| 3.2 | "On polysemy and the local-construction trump" — local construction picks sense; if construction permits multiple, preserve all | core | HIGH | the most-relevant existing principle — but DIRECTION IS INVERSE |
| 3.3 | "Plausibility test as backstop: a candidate sense whose referent cannot do what the metaphor-sense requires fails" | core | HIGH | adjacent — about source-side sense-selection |
| 3.4 | "Scope: word-level polysemy; phrase-level multi-meaning is a separate concern" | sub | HIGH | acknowledges a scope limit |
| 3.5 | "On the same pronoun referring to multiple audiences simultaneously" | side | MEDIUM | source-side |
| 3.6 | "On grammatical indefiniteness encoding two opposite meanings" | sub | HIGH | adjacent — source-side dual-sense |
| 3.7 | "On deletion (hazf) creating universality through silence" | side | MEDIUM | source-side |
| 3.8 | "On hidden logical chains between sentences (lüzum chains)" | side | MEDIUM | source-side |
| 3.9 | "On polysemy and the local-construction trump" → **STRUCTURAL INVERSE of what's needed here**: that principle says "when SOURCE word has multiple senses, local construction picks the sense the SOURCE intends." The MISSING principle would say: "when TARGET rendering accidentally admits a sense the SOURCE does not, target-side disambiguation REMOVES the false sense." | core | HIGH | the gap diagnosis |
| 3.10 | **GAP**: notes.md addresses SOURCE-side polysemy preservation extensively; addresses TARGET-side accidental polysemy ZERO times | core | HIGH | the artifact's blind spot |
| 3.11 | **GAP**: no principle named for "target-side direction-flip" or "target-side false-friend" or "target accidentally admits opposite sense" | core | HIGH | naming gap |
| 3.12 | Extra Notes Layer entry on "dimensionally compressed terms" — addresses TARGET-side decompression strategy but for SOURCE compression, not for TARGET-side accidental sense expansion | sub | HIGH | adjacent operational template — target-side decompression IS addressed for some cases |

### Region 4: advanced_principles.md — what's there + what's missing

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 4.1 | Pass 3 example: cycles-of-rest analogy — "preserves cargo AND momentum" | core | HIGH | about preserving source effect via target |
| 4.2 | Self-illuminating text principle (Bismillah example) — "translation must preserve self-sufficiency" | core | HIGH | source-side property |
| 4.3 | Word-order encoding theology (hasr in Bismillah) — "the word order IS the theology" | core | HIGH | source-side structural meaning |
| 4.4 | Istilzam chains (Rahman → Rezzak → Rızk → Beka → Vücud → İlim/İrade/Kudret → Hayat) — "translating the surface without translating its depth is like photocopying a seed" | core | HIGH | source-side compression preservation |
| 4.5 | Istilzam English example: "teacher" → students/knowledge/ignorance/difference/communication/language/shared reality/time | sub | HIGH | how the same principle works in English |
| 4.6 | **GAP**: every principle here is about ENSURING target carries source's hidden structures. None address PREVENTING target from accidentally carrying NON-source structures (like an opposite-direction reading). | core | HIGH | structural inverse |
| 4.7 | The principle is forward-only: source → target preservation. No mention of target → source reverse-check. | core | HIGH | |

### Region 5: config_base_source.md (canonical Layer 1 spec v1.0) — what's there + what's missing

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 5.1 | 5 always-on policies (Layer 2): multi-meaning preservation / register-alternation preservation / polysemy-via-local-construction / nazm preservation / no-smoothing | core | HIGH | enumerated as Layer 2 invariants |
| 5.2 | Multi-meaning preservation policy: "When source word's local construction permits multiple simultaneously-valid senses, preserve both" | core | HIGH | SOURCE-side |
| 5.3 | Polysemy-via-local-construction policy: "Local grammatical construction selects intended sense; not surrounding metaphor's momentum" | core | HIGH | SOURCE-side |
| 5.4 | No-smoothing policy: "Translating away awkward/uncomfortable nuance to make output 'cleaner' is corruption; smoothing introduces worse error than awkwardness" | core | HIGH | RELATED — smoothing IS one cause of target-side leakage (my "set against" was a smoothing of "in-exchange-for" into idiomatic English) |
| 5.5 | 5 × 8 policy interaction map — all 40 cells documented | sub | HIGH | the cells for "target-side false-friend" don't exist because the policy itself doesn't exist |
| 5.6 | A5 lightly-domesticated stance: "narrow target-naturalization where source-fidelity isn't load-bearing" — used in 4_mesele translation | core | HIGH | the operative config — the offending rendering was a target-naturalization that crossed the load-bearing line |
| 5.7 | A5 disfavored-action: TARGET-LANGUAGE-EQUIVALENT — at lightly-domesticated, permissible in narrow cases | sub | HIGH | this is the action class that produced the failure |
| 5.8 | DOMESTICATE-disfavored cross-cutting policy: "PRESERVE-CULTURAL-SPECIFICITY over DOMESTICATE-CULTURAL-FRAME / ANGLICIZE-HONORIFICS / TARGET-LANGUAGE-EQUIVALENT" | core | HIGH | the policy is meant to prevent over-naturalization; "set against" is over-naturalization that violated this in spirit |
| 5.9 | **GAP**: no Layer 2 policy named for "target-side direction-flip prevention" / "target-side accidental polysemy" / "no opposite-sense leakage" | core | HIGH | candidate v1.1 increment |
| 5.10 | Versioning + Changelog system in place; refinement triggers documented including "If real translations reveal the per-passage [...]" — this case is exactly such a refinement trigger | core | HIGH | the framework anticipates this kind of gap |

### Region 6: translation_principals.md — what's there + what's missing

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 6.1 | "no single person can properly interpret a comprehensive work" — collective reading | sub | MEDIUM | meta-principle |
| 6.2 | "all meanings derived from a text are valid and intended, as long as they don't violate the grammatical rules and foundational principles of the language" | core | HIGH | KEY ITEM — the inverse statement: target meanings the AUTHOR did NOT validly intend should NOT appear in translation |
| 6.3 | "Choosing a meaning is up to the user not to the translation system" | core | HIGH | the user gets all valid source meanings — but a target-side false-friend gives the user an INVALID meaning (one author didn't intend) |
| 6.4 | "leaving a lesser evil to avoid it causes a greater evil" (no-smoothing) | sub | HIGH | related |
| 6.5 | "rhetoric is not a mere decoration but as a fundamental carrier of meaning" | side | MEDIUM | |
| 6.6 | **GAP**: same as the other artifacts — every principle is about preserving source-side meaning; none about preventing target-side false additions | core | HIGH | the global pattern across artifacts |

### Region 7: Possibility-mode — candidate names for the failure mode

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 7.1 | "target-side accidental polysemy" | core | HIGH | inverse of source-side polysemy preservation; symmetric vocabulary |
| 7.2 | "target-side false-friend" | core | HIGH | borrows from linguistics term for cross-language similar-words-different-meanings; here applied to target-internal ambiguity |
| 7.3 | "direction-flip leakage" | sub | HIGH | captures the OPPOSITE-direction property (worse than mere ambiguity) |
| 7.4 | "target opens a sense source doesn't admit" | sub | HIGH | precise but verbose |
| 7.5 | "target-side opposite-sense leakage" | sub | HIGH | precise + names the worst case |
| 7.6 | "Pass-3 reverse-read failure" | sub | HIGH | locates the failure in 3-Pass methodology |
| 7.7 | "unintended target reading" / "unintended polysemy in target" | side | MEDIUM | generic |
| 7.8 | "directional flip" (Nursi-specific term for it) | side | MEDIUM | from the actual error |
| 7.9 | Settled candidate: **"target-side accidental polysemy with direction-flip subcase"** | core | HIGH | combines naming clarity + emphasis on worst case |

### Region 8: Possibility-mode — candidate prevention mechanisms

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 8.1 | **Reverse-Read check** (proposed Pass 4) — read the target rendering as if you don't know the source; enumerate the readings it admits; if any reading not in source set OR if any reading is OPPOSITE-direction, re-render | core | HIGH | the canonical fix |
| 8.2 | **Opposite-direction sanity check** — explicit "does target admit a reading in opposite direction to source?" check | core | HIGH | the maximum-severity subcase check |
| 8.3 | **Hard-constraint refinement** in harmony_layer.md — "Anything that changes semantic content is forbidden, INCLUDING target rendering that admits a sense source doesn't admit" | core | HIGH | extends existing principle |
| 8.4 | **New principle in notes.md** — "On target-side accidental polysemy and direction-flip risk" as inverse/counterpart to "On polysemy and the local-construction trump" | core | HIGH | the most natural home |
| 8.5 | **New Layer 2 always-on policy** in canonical spec (v1.1 increment) — "Target-side opposite-sense leakage prevention" | sub | HIGH | most invasive option |
| 8.6 | **Pre-emptive target-language phrase blacklist** — common English phrases with directional dual senses (set against / standing against / for vs. against / with vs. without) | side | MEDIUM | hard to maintain; specific |
| 8.7 | **Mandatory question at Pass 3**: "Does my target rendering admit a reading the source doesn't? Especially: an opposite-direction reading?" | core | HIGH | translator-facing operational form |
| 8.8 | **Pre-mortem at Pass 3**: read each rendered phrase imagining you're a target-reader unfamiliar with source — what's the most natural reading? Does it match source? | core | HIGH | concrete procedure |
| 8.9 | Settled candidate-architecture: **Pass 3.5 Reverse-Read check** + **notes.md principle entry** + **harmony_layer.md hard-constraint refinement** + **canonical spec v1.1 increment to Layer 2 policy list** — composite fix | core | HIGH | belt-and-suspenders |

### Region 9: WHY the existing principles missed this case (gap analysis)

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 9.1 | The 3-Pass methodology's Pass 3 check is "did target preserve source meaning?" — UNIDIRECTIONAL | core | HIGH | the structural property of the failure |
| 9.2 | The check needed is "did target add unintended meaning?" — REVERSE-direction | core | HIGH | the missing direction |
| 9.3 | The polysemy-via-local-construction policy is about SOURCE-side disambiguation; doesn't address TARGET-side accidental polysemy | core | HIGH | |
| 9.4 | The multi-meaning preservation policy is about SOURCE-side multi-sense preservation; doesn't address target-side multi-sense PREVENTION | core | HIGH | |
| 9.5 | The hard constraint "Anything that changes semantic content is forbidden" COULD have caught it if maximally interpreted — but the translator (me) didn't interpret "set against" as "changing semantic content" because the in-exchange-for sense IS available; the opposite sense was a SIDE EFFECT | core | HIGH | the failure mode is "the chosen wording technically preserves a valid reading but ALSO admits an invalid reading" |
| 9.6 | The "Adding information not present in the original is forbidden" constraint COULD have caught it — opening a negation/opposition reading IS adding information — but the constraint was understood as "don't insert content not in source" not "don't let target wording carry content not in source as a side effect" | core | HIGH | the constraint exists but its scope was too narrow |
| 9.7 | The no-smoothing policy is about RETAINING source-awkwardness, not about FILTERING target-language smoothness that introduces false readings | sub | HIGH | adjacent but inverse |
| 9.8 | DOMESTICATE-disfavored policy: the lightly-domesticated A5 stance permits NARROW target-naturalization; "set against" was a target-naturalization that crossed into the load-bearing zone (the courtroom-metaphor's directional semantics) without the policy firing | core | HIGH | the policy didn't fire because there's no operational test for "did this naturalization cross into load-bearing semantics?" |
| 9.9 | Summary: the existing principles all operate on SOURCE → TARGET (preserve). The missing principle operates on TARGET → SOURCE (verify by reverse-reading). | core | HIGH | the structural diagnosis |

### Region 10: Which artifact owns the fix — locating it

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 10.1 | `notes.md` — most natural home for a new PRINCIPLE entry ("On target-side accidental polysemy as inverse counterpart to source-side polysemy preservation") | core | HIGH | matches notes.md's existing entry style |
| 10.2 | `harmony_layer.md` — most natural home for a HARD-CONSTRAINT refinement (extend "Adding information is forbidden" to cover target-side incidental sense-leakage) | core | HIGH | matches hard-constraints section style |
| 10.3 | `harmony_layer.md` — most natural home for a Pass 3.5 Reverse-Read check (extend 3-Pass methodology) | core | HIGH | extends 3-Pass methodology |
| 10.4 | `advanced_principles.md` — most natural home for an OPERATIONAL example of the principle in action | sub | HIGH | matches advanced_principles.md's "show the principle via concrete example" style |
| 10.5 | `config_base_source.md` (canonical Layer 1 spec) — most natural home for a Layer 2 always-on policy addition (v1.1 increment) | sub | HIGH | most invasive; v1.1 Changelog entry triggered |
| 10.6 | The user's question specifically: harmony_layer.md or notes.md? — **answer: BOTH**, with primary home in notes.md (principle entry) and secondary anchor in harmony_layer.md (hard-constraint refinement + Pass 3.5 check) | core | HIGH | the direct answer |
| 10.7 | Layered fix architecture: notes.md = principle (the WHY/WHAT); harmony_layer.md = hard constraint + Pass 3.5 check (the OPERATIONAL HOW); canonical spec = Layer 2 policy entry (the INVARIANT) | core | HIGH | composes the artifacts |

### Region 11: Companion failure case — deathbed-room (different mode)

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 11.1 | The deathbed-room failure: `sekerat` (death-agonies, a STATE/MOMENT) rendered as `deathbed-room` (a physical location compound that doesn't exist in English) | sub | HIGH | different failure mode |
| 11.2 | This is a DIFFERENT failure mode: over-naturalization of a SOURCE-SPECIFIC TECHNICAL TERM + conflation of state with location | sub | HIGH | not target-side direction-flip |
| 11.3 | Existing principle that addresses this case: KEEP-SOURCE-TERM-WITH-GLOSS for load-bearing source-specific terms | sub | HIGH | already in framework |
| 11.4 | The deathbed-room failure is a failure to APPLY an existing principle (A2=lay + A3=outsider didn't trigger KEEP-SOURCE-TERM-WITH-GLOSS for `sekerat`); the set-against failure is a failure to HAVE an applicable principle | core | HIGH | the structural distinction |
| 11.5 | Out of scope for this inquiry; frontier flag for separate inquiry on "load-bearing technical term identification at Pass 3 + when to use KEEP-SOURCE-TERM-WITH-GLOSS" | sub | HIGH | |

### Region 12: Cross-language linguistics — adjacent concepts

| # | Item identifier | Tag | Confidence | Note |
|---|---|---|---|---|
| 12.1 | "False friends" in linguistics: words that look/sound similar across languages but mean different things | sub | HIGH | adjacent concept; usually applied source-to-target word-level |
| 12.2 | Here: target-INTERNAL "false friend" — target phrase has multiple senses, one matches source, one is INVERSE | sub | HIGH | novel application |
| 12.3 | Cognitive linguistics: "schema mismatch" — source frame doesn't map cleanly to target frame | side | MEDIUM | |
| 12.4 | Translation studies: "semantic shift" — meaning drifts in translation | side | MEDIUM | |
| 12.5 | The user's stored memory: "feedback_translation_polysemy" — local construction picks sense | core | HIGH | already documented in user's memory; needs INVERSE counterpart |
| 12.6 | The user's stored memory: "feedback_translation_register" — don't pull plain source registers up into ornate English | sub | HIGH | adjacent — about register-fidelity; "set against" was a register-level over-naturalization that crossed into semantic territory |

---

## State Summary

### Territory specification echo
Explicit-bounded: 5 framework artifacts (harmony_layer.md / notes.md / advanced_principles.md / config_base_source.md canonical spec v1.0 / translation_principals.md) + the offending translation (4_mesele_en.md) + adjacent linguistics concepts (cross-language false friends / target-internal polysemy / semantic schema mismatch). Mixed mode (artifact-enumeration + possibility-mode candidate generation for failure-mode names + prevention mechanisms + fix locations).

### Purpose specification echo
Diagnose the framework mechanism that failed to catch the `set against his Faith` mistranslation (target-side direction-flip from "in exchange for" to "in opposition to"). Locate the gap in specific artifact parts. Propose a concrete prevention mechanism. Structurally answer the user's harmony_layer-vs-notes question.

### Coverage map

| Region | Coverage | Aggregate relevance |
|---|---|---|
| R1 specific failure (anchor) | confirmed | core |
| R2 harmony_layer.md what's there + missing | confirmed | core |
| R3 notes.md what's there + missing | confirmed | core |
| R4 advanced_principles.md what's there + missing | confirmed | core |
| R5 canonical Layer 1 spec what's there + missing | confirmed | core |
| R6 translation_principals.md what's there + missing | confirmed | sub |
| R7 candidate names for failure mode | confirmed | core |
| R8 candidate prevention mechanisms | confirmed | core |
| R9 gap analysis (WHY existing principles missed) | confirmed | core |
| R10 which artifact owns the fix | confirmed | core |
| R11 companion deathbed-room case | confirmed | sub (out of scope; frontier-flagged) |
| R12 cross-language linguistics adjacent concepts | confirmed | side |

### Confirmed-absent regions
- "Pass 3 forbidden-list" — no list of forbidden Pass 3 operations exists in harmony_layer.md (only a permitted-list).
- "Target → source reverse check" — does not exist anywhere in the framework.
- "Target-side polysemy prevention" — explicitly absent from all artifacts.
- "Layer 2 policy on target-side false-friend" — not in the 5 always-on policies.

### Concept-names list

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| target-side accidental polysemy | coined-term | R7.1, R7.9 | the failure-mode name |
| direction-flip leakage | coined-term | R7.3, R7.5 | the worst-case subset (target opens OPPOSITE direction) |
| target opens a sense source doesn't admit | descriptive | R7.4 | precise but verbose form |
| Reverse-Read check | coined-term | R8.1 | proposed Pass 3.5 check |
| Opposite-direction sanity check | coined-term | R8.2 | the maximum-severity subcase check |
| Pass 3.5 Reverse-Read | coined-term | R8.9 | composite name for the methodology extension |
| target-side false-friend | coined-term | R7.2, R12.2 | borrows linguistics term applied target-internally |
| `mukabil` | vocabulary | R1.3 | the Turkish lexeme whose semantics got flipped |
| `set against` | vocabulary | R1.4, R1.9 | the offending English phrase |
| local-construction trump | structural-reference | R3.2 | the existing INVERSE principle in notes.md |
| 3-Pass methodology | structural-reference | R2.1 | the operational frame whose Pass 3 check missed this case |
| harmony_layer hard-constraint refinement | coined-term | R10.2, R8.3 | proposed fix location 1 |
| notes.md principle entry | coined-term | R10.1, R8.4 | proposed fix location 2 |
| Layer 2 policy increment | coined-term | R10.5, R8.5 | proposed fix location 3 (v1.1 increment) |

### Frontier flags

- **FF1** Sensemaking needs to settle whether the fix lives in ONE artifact or in MULTIPLE (layered fix) — leaning toward layered per R10.7.
- **FF2** Sensemaking needs to settle on a CANONICAL NAME for the failure mode — leaning toward "target-side accidental polysemy with direction-flip subcase" per R7.9.
- **FF3** Sensemaking needs to settle whether the canonical Layer 1 spec v1.0 → v1.1 increment is necessary (adding a 6th Layer 2 policy) OR whether the fix lives entirely in notes.md / harmony_layer.md (operational layer) without policy-level increment.
- **FF4** Decomposition needs to express the Pass 3.5 Reverse-Read check as a concrete procedure the AI translator can execute at runtime.
- **FF5** Innovation may surface a more elegant unified principle that doesn't need belt-and-suspenders layered fix — possibility space worth exploring.
- **FF6** The companion deathbed-room case is OUT OF SCOPE but flagged for separate inquiry (different failure mode; failure to APPLY existing principle vs failure to HAVE applicable principle).
- **FF7** The user's stored memory `feedback_translation_polysemy` should be updated to include this INVERSE counterpart if the fix lands.
- **FF8** The English-side blacklist option (R8.6) is rejected by surfacing as un-maintainable; sensemaking can confirm.

### Workspace-populated status
`{populated: true, populated-at: 2026-06-08_01-43, extent: 12 regions, ~90 items, 8 frontier flags}`

### Re-invocation parameters (optional)
None — single-pass coverage sufficient for sensemaking handoff.

---

## Telemetry

- Mode: mixed (artifact + possibility)
- Entry-point: signal-first
- Cycles run: 1 (single-pass)
- Items enumerated: ~90
- Items tagged at each relevance level: core ≈ 60; sub ≈ 20; side ≈ 8; umbrella ≈ 2 (LOW)
- Sub-phase fired: NO (explicit-bounded)
- Convergence: territory exhaustively traversed; uncertain-relevance items included with umbrella tag
- Workspace-overload trigger: NOT fired
- Failure modes checked: missed-relevance (mitigated by inclusion-default; possibility-mode covered candidate generation), surfaced-irrelevance (acceptable), over-coverage (managed), territory-mis-binding (no), workspace overload (no), artifact under-specification (no), workspace-artifact desync (no), recency-Equates-Idleness (N/A — all artifacts current), recency-Bias-Filter (N/A), interpretive-overstep (avoided — relational diagnosis deferred to sensemaking), purpose-loss (no), self-coupling-to-downstream (no)
- `items_with_mtime`: 5 (the framework artifacts) — `items_without_mtime`: ~85 (possibility-mode candidates)
- Self-assessment verdict: **PROCEED**
