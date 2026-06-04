# Surfacing — translation_failure_root_cause_diagnosis

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-03_23-30__translation_failure_root_cause_diagnosis/_branch.md`

Purpose (echoed from `_branch.md`): identify the actual root cause of the translation failures (register pull-up across ≥8 lexical items; *nefer* polysemy mis-resolution) that occurred despite the comprehenslate framework documents being loaded and consulted — testing three user-offered hypotheses (fault in docs / AI bulk behavior / absent failure-mode catalog) and any others that emerge.

Territory (echoed from `_branch.md`): seven items — `advanced_principles.md`, `notes.md`, `harmony_layer.md` (the framework docs); `mytrasnlations/5th_word/org.md` (Turkish source); `mytrasnlations/5th_word/eng.md` (failed translation including its harmony report); prior diagnostic exchanges in this conversation; the two saved feedback memories.

## Mode + Entry Point

- **Mode:** artifact (territory contains concrete pre-existing items).
- **Entry point:** signal-first (purpose is given).
- **Sub-phase fired:** no (territory is explicit-bounded).

## Traversal Trace

### Region A — `advanced_principles.md`
*(mtime: 2026-04-11T13:19:49Z — predates the failure by ~2 months)*

| # | Item identifier | Relevance | Conf | Note |
|---|---|---|---|---|
| 1 | A-presence: "the translator's hand should be invisible" maxim (in self-illumination section) | core | HIGH | Closest doc gets to anti-ornate principle, but scoped narrowly to self-illuminating passages, NOT framed as general register rule. |
| 2 | A-presence: "the SPECIFIC examples could be swapped for other examples from the target culture" (small-cycle principle) | sub | HIGH | Implies target-audience-resonance is a translation criterion; I violated this by exoticizing the parable. Principle present but not flagged as register-shaped. |
| 3 | A-presence: "preserves cargo AND momentum" framing | side | MEDIUM | About escalation, not register. |
| 4 | A-presence: istilzam example uses "teacher" — the example chain unpacks abstract logical entailments | sub | HIGH | Demonstrates istilzam mechanism; explicit instruction is to "annotate the chain" — a procedure I followed too aggressively (over-deployed transliteration). |
| 5 | A-presence: word-order-creates-hasr example with Bismillah reversal | sub | MEDIUM | Discusses encoding of theology by syntactic position. |
| 6 | A-ABSENCE: no general anti-register-pull-up principle | core | HIGH | The maxim in A-1 exists only inside the self-illumination section; not generalized as "match source register." |
| 7 | A-ABSENCE: no anti-archaic-vocabulary principle | core | HIGH | Nothing warns against reaching for fancy English equivalents. |
| 8 | A-ABSENCE: no markedness-matching principle (unmarked-source → unmarked-target) | core | HIGH | The concept of source-word markedness is entirely missing. |
| 9 | A-ABSENCE: no polysemy disambiguation guidance (which sense to pick when context disambiguates) | core | HIGH | The doc emphasizes preserving multiple meanings but not adjudicating among polysemous senses when the construction forces one. |
| 10 | A-ABSENCE: no failure-mode catalog ("here are the ways translators commonly fail") | core | HIGH | The doc is a positive-principles list, not a failure-mode list. |
| 11 | A-ABSENCE: no "register alternation as structural feature" recognition | core | HIGH | Source-text register-shifts are not named as a preserve-target. |

### Region B — `notes.md`
*(mtime: 2026-04-11T13:12:49Z — predates the failure by ~2 months)*

| # | Item identifier | Relevance | Conf | Note |
|---|---|---|---|---|
| 12 | B-presence: ~60 numbered interpretive principles each framed "Comprehenslate should detect / preserve / flag" | core | HIGH | The framing's gravity is detection of *structural* features (word order, ellipsis, tense shifts, escalation, etc.) — register is not in this list. |
| 13 | B-presence: principle on "a single word carrying multiple valid readings simultaneously" (din example) | sub | HIGH | About *preserving* multi-meaning, not *disambiguating* polysemy. Different operation from what the *nefer* failure required. |
| 14 | B-presence: principle on iltifat (person-shift) as meaning carrier | sub | HIGH | Tracked correctly in my translation. |
| 15 | B-presence: principle on grammatical "violations" as deliberate meaning | sub | MEDIUM | About preserving non-standard grammar; not about register. |
| 16 | B-presence: "dimensionally compressed terms" addendum (the last entry) | core | HIGH | The one operational strategy in the doc — "transliterate with parenthetical context on first mention, then use shortened form." I OVER-APPLIED this, contributing to the elevated feeling of the English. |
| 17 | B-presence: principle on reader-dependent meaning (ihdina example) | side | LOW | Not directly load-bearing for register/polysemy. |
| 18 | B-presence: principle on metaphorical language as cognitive bridge (müteşabihat) | side | LOW | About abstract-via-concrete; not register-shaped. |
| 19 | B-presence: principle on word-choice triggering psychological response (tenfir/targhib) | sub | MEDIUM | About connotation, which is register-adjacent but not framed as register-fidelity. |
| 20 | B-ABSENCE: no register-matching principle | core | HIGH | Same gap as A-11. |
| 21 | B-ABSENCE: no markedness principle | core | HIGH | Same gap as A-8. |
| 22 | B-ABSENCE: no failure-mode catalog | core | HIGH | Same gap as A-10. The doc is principle-as-virtue-list. |
| 23 | B-ABSENCE: no procedural step-by-step ("when translating, do X then Y then Z") | core | HIGH | Inventory-shaped, not procedure-shaped. |
| 24 | B-asymmetry: principles emphasize PRESERVATION ("preserve X") far more than PROHIBITION ("don't do Y") | core | HIGH | Asymmetry of attentional gravity — the framework biases toward "keep" actions, not "avoid" actions. |

### Region C — `harmony_layer.md`
*(mtime: 2026-03-28T22:05:57Z — predates the failure by ~2 months)*

| # | Item identifier | Relevance | Conf | Note |
|---|---|---|---|---|
| 25 | C-presence: 3-pass process specified (Meaning Lock → Harmony Map → Target Reconstruction) | sub | HIGH | Procedural. I followed Pass 1; Pass 2 mapping missed register; Pass 3 used non-equivalent English register. |
| 26 | C-presence: Tier 1 list = implied Q-A, cause-effect, escalation, tense, iltifat, emotional arc, convergence/havuz, antonym pairing, ellipsis | core | HIGH | All STRUCTURAL/LOGICAL features. Register is absent. |
| 27 | C-presence: Tier 2 list = parallelism, sentence-type alternation, pronoun chain, length pattern, evidence-claim, concession-rebuttal, lexical-field continuity, ring composition, chiasm, thematic bracketing, anticipation-fulfillment, addressee consistency | core | HIGH | Mostly structural. "Lexical field continuity" is closest to register but is about thematic field (water-imagery, fire-imagery), not register-altitude. |
| 28 | **C-TIER-3-CLASSIFICATION: "Register consistency — important for reader comfort but doesn't change meaning. A shift from formal to casual feels jarring but doesn't alter what's communicated."** | **core** | **HIGH** | **CENTRAL FINDING. The doc EXPLICITLY classifies register as Tier 3 (sacrificeable for reception-quality). This is a misclassification: when the SOURCE deliberately alternates registers as a structural device (folk-narrative grounds high-theology), register alternation IS meaning-bearing — Tier 1. The doc's Tier-3 verdict suppressed my attention to register fidelity.** |
| 29 | C-presence: Tier 4 list (phonetic echo, rhyme, root echo, etc.) | sub | MEDIUM | Surface aesthetics. |
| 30 | C-presence: hard constraints — no content add/remove, no sentence merge/split, no logical relation reversal | sub | HIGH | Negative rules but content-shaped, not register-shaped. |
| 31 | C-presence: permitted list — synonym choice for phonetic harmony, word-order adjustment, transitional devices, length matching | sub | HIGH | The "synonym choice" license is unconstrained by register criteria; it implicitly permits picking elevated synonyms. |
| 32 | C-ABSENCE: no rule "register-of-source must equal register-of-target" or equivalent | core | HIGH | The framework explicitly ranks register as low priority (Tier 3); the very rule that would have prevented the failure is the rule the doc demotes. |
| 33 | C-ABSENCE: no failure-mode catalog at any tier | core | HIGH | All four tiers are positive lists of what-to-preserve. No "common pull-up patterns to avoid." |
| 34 | C-ABSENCE: no rule "register-alternation within source = Tier 1 structural feature" | core | HIGH | The case where source SHIFTS register between sections is not addressed. |
| 35 | C-presence: ranking principle stated — "closer a harmony component is to carrying meaning, the higher its priority" | sub | HIGH | The principle is sound; its APPLICATION to register is what's wrong (register treated as not-meaning-carrying). |

### Region D — `mytrasnlations/5th_word/org.md` (Turkish source)
*(mtime: 2026-06-03T20:36:04Z)*

| # | Item identifier | Relevance | Conf | Note |
|---|---|---|---|---|
| 36 | D-feature: barracks/folk-register vocabulary in parable section — *kazan, karavana, lokma, asker, padişah, çarşı, dilencilik, angarya, nafaka, kazan kaynatır, karavanayı yıkar* | core | HIGH | All unmarked everyday Turkish. Confirms the source's parable register is plain. |
| 37 | D-feature: elevated Arabic-Persian theological compounds in decoder section — *mu'cize-i san'at-ı Samedaniye, hârika-i hikmet-i Rabbaniye, hayat-ı maneviye, ferâiz-i diniye, müttaki müslüman, fâsık-ı hâsir, matbaha-i rahmet, helâket-i ebediye* | core | HIGH | Confirms the source's theological register is elevated. |
| 38 | D-feature: the two registers ALTERNATE within the same text — barracks for parable, theological for decoding | core | HIGH | Confirms the user's diagnosis that register alternation is a deliberate structural feature of the source. |
| 39 | D-feature: *nefer* appears 3× — twice unambiguously military ("muallem nefer," "şikemperver nefer") in the parable, once in "serçe kuşunun bir neferi" (sparrow's nefer) in the conclusion | core | HIGH | The 2-prior-military-uses prime metaphor-momentum; the genitive construction in the 3rd use should override but didn't in my reading. |
| 40 | D-feature: *serseri nefer* — "serseri" is colloquial Turkish for vagabond/loafer | sub | HIGH | Source register at the parable level is colloquial; "wayward" elevated it. |
| 41 | D-feature: source uses *bizzât* (in person, himself), *mert* (manly/honorable) — direct colloquial registers | sub | MEDIUM | More evidence the parable register is plain-spoken. |
| 42 | D-asymmetry: high-register section is ~40% of text; folk-register section is ~60% | side | MEDIUM | The folk register is the majority; my translation flipped this so high-register dominates. |

### Region E — `mytrasnlations/5th_word/eng.md` (failed translation)
*(mtime: 2026-06-03T20:59:48Z)*

| # | Item identifier | Relevance | Conf | Note |
|---|---|---|---|---|
| 43 | E-failure: register pull-up across ≥8 lexical items in parable section — corvée, cauldron, morsel, scrubs the mess-tin, parable, Padishah, wave-tossed, wayward | core | HIGH | The actual failure signature. Consistent direction (always upward), consistent location (parable section), consistent type (folk-word → ornate/archaic English). |
| 44 | E-failure: polysemy mis-resolution on *nefer* | core | HIGH | Independent failure mode from register; metaphor-momentum picked wrong sense. |
| 45 | E-feature: harmony report at file bottom | core | HIGH | The translator's self-audit. |
| 46 | **E-blind-spot: harmony report lists 10+ Tier-1-preserved items, 4 Tier-1-with-partial-transfer items, 3 Tier-4-sacrificed items — ZERO items about register or diction-level or voice-consistency** | **core** | **HIGH** | **DIRECT EVIDENCE that the framework's tier-system did not surface register as a feature to track. The harmony report, written per the framework, is structurally blind to register pull-up.** |
| 47 | E-feature: heavy use of italicized transliteration with parenthetical glosses (*nefs*, *cihâd*, *ibâdet*, *mücâhede*, *ferâiz*, *Rezzâk-ı Hakîkî*, *Samad*, *mezra'a*, etc.) | sub | HIGH | Application of B-16 strategy. Contributed to the elevated *overall feel*; itself defensible per the doc, but combined with the register pull-up it compounds the exoticization. |
| 48 | E-feature: AI's chosen rendering for the closing conditional pair — preserves antonym structure (foot-soldier-of-sparrow ↔ commander-of-animals) but with the wrong polysemy sense of *nefer* | sub | HIGH | Tier-1 structural preservation succeeded; word-sense fit failed. |
| 49 | E-feature: AI explicitly stated in its initial message "I'll use sophisticated literary register" in interpreting "C1 English speakers" | core | HIGH | Self-declared interpretation that biased the entire output. |

### Region F — prior diagnostic exchanges in this conversation
*(not filesystem-backed; mtime: source = none, value = null)*

| # | Item identifier | Relevance | Conf | Note |
|---|---|---|---|---|
| 50 | F-event: user round 1 flagged 5 words (corvée, cauldron, morsel, parable, mess-tin) | sub | HIGH | Pattern detected by user; first round prompted register-pull-up self-diagnosis. |
| 51 | F-event: user round 2 flagged 3 more words (Padishah, wave-tossed, wayward) | sub | HIGH | Same pattern, distinct words; confirmed systemic not isolated. |
| 52 | F-event: AI's after-the-fact diagnosis named the pattern "register pull-up" | core | HIGH | Failure mode was nameable AFTER it occurred — implying it had been a recognizable pattern that simply wasn't checked-for during translation. |
| 53 | F-event: AI admitted suspected-but-uncaught additional instances ("brand you a mutineer, inflict the punishment, tilth, August and All-Generous, Lordly wisdom, beast of prey, trench-post") | sub | HIGH | Self-acknowledged extent of pattern. |
| 54 | F-event: user round 3 flagged polysemy (nefer) | core | HIGH | Distinct failure mode from register; the user's third probe revealed a second class of error. |
| 55 | F-event: AI misread "C1 English speakers" as license for ornate vocabulary | core | HIGH | The audience-spec interpretation was the trigger event; "C1" got mapped to "literary register permitted" instead of "high comprehension capability." |
| 56 | F-event: user's third question framed the failure as a system-diagnostic, not a translation-fix: "what went wrong with [the docs]? or AI bulk issue? or lack of failure modes?" | core | HIGH | User treating the failure as evidence of a systemic gap to be analyzed — the current inquiry's prompt. |

### Region G — saved feedback memories
*(feedback_translation_register.md mtime: 2026-06-03T21:36:56Z; feedback_translation_polysemy.md mtime: 2026-06-03T22:17:41Z — both authored AFTER the failure)*

| # | Item identifier | Relevance | Conf | Note |
|---|---|---|---|---|
| 57 | G-content: feedback_translation_register.md — captures register-pull-up failure mode + markedness-matching test + anti-pattern word list | sub | HIGH | The lesson IS extracted; the question is whether it flows back into the framework. |
| 58 | G-content: feedback_translation_polysemy.md — captures metaphor-momentum-overrides-construction principle + plausibility test | sub | HIGH | Same. |
| 59 | **G-architectural: both memories live in `/Users/ns/.claude/projects/.../memory/` — AI session memory, NOT in the comprehenslate framework documents** | **core** | **HIGH** | **The lessons are siloed in AI-private memory; they do not update `harmony_layer.md`, `notes.md`, or `advanced_principles.md`. Next session loading the framework still sees the failure-permitting docs unless memory loads (and even then, the docs themselves remain uncorrected).** |
| 60 | G-content: feedback_translation_register.md explicitly names this as a Tier 1/2 structural feature that should be tracked — directly contradicting harmony_layer.md C-28 (Tier 3) | core | HIGH | The memory has the correct tier classification; the framework doc has the wrong one. They disagree, and the framework is what gets loaded first. |

---

## State Summary

### Territory + Purpose Echo

- **Territory:** seven items across three locations (project root for framework docs; project subfolder for source/translation; user-home memory for feedback notes). Explicit-bounded.
- **Purpose:** identify root cause of register pull-up + polysemy translation failures, test three user-offered hypotheses, surface additional causes.

### Coverage Map

| Region | Coverage | Aggregate relevance | Notes |
|---|---|---|---|
| A (advanced_principles.md) | CONFIRMED | core-relevant region | 11 items: 5 presences + 6 absences. Absence pattern is itself the dominant signal. |
| B (notes.md) | CONFIRMED | core-relevant region | 13 items: 8 presences + 4 absences + 1 asymmetry. |
| C (harmony_layer.md) | CONFIRMED | core-relevant region | 11 items including the C-28 central finding. |
| D (org.md, Turkish source) | CONFIRMED | core-relevant region | 7 items confirming source register alternation. |
| E (eng.md, failed translation) | CONFIRMED | core-relevant region | 7 items including the E-46 harmony-report-blindness finding. |
| F (prior diagnostic exchanges) | CONFIRMED | core-relevant region | 7 conversational events documenting the failure pattern and self-diagnosis. |
| G (feedback memories) | CONFIRMED | core-relevant region | 4 items, central one being G-59 architectural siloing. |

No regions confirmed-absent. Every region in the territory produced at least one core-relevant item.

### Confirmed-Absent Regions

None. All regions yielded relevant items.

### Concept-Names List

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| register pull-up | coined-term (extended in AI diagnosis) | F-52 | Translation failure pattern: source-language plain register rendered as elevated/archaic target-language register. |
| markedness | vocabulary | G-57 | Linguistic property: whether a word is "ordinary/unmarked" or "specialized/marked" in its own language; failure mode is unmarked-source-to-marked-target. |
| register alternation | coined-term | D-38, C-28 | Source-text feature where two registers deliberately alternate within one work as a structural device (folk grounds theology). |
| metaphor-momentum | coined-term | F-54, G-58 | Tendency for a controlling metaphor (e.g., military framing) to override local construction-determined word-sense fit. |
| harmony report blindness | coined-term | E-46 | The translator's self-audit (per harmony_layer.md) failing to surface register as a tracked feature because the framework's tier system demotes register to Tier 3. |
| tier misclassification | coined-term | C-28 | Specific instance: `harmony_layer.md` classifies register-consistency as Tier 3 (sacrificeable), but source register-alternation is Tier 1 (meaning-bearing). |
| principle/failure-mode asymmetry | coined-term | A-10, B-22, C-33, B-24 | Framework asymmetry: principles state what-to-preserve (preservation-virtue list); no explicit catalog of what-to-avoid (failure modes). |
| lesson siloing | coined-term | G-59 | Architectural pattern: lessons from failures get saved to AI session memory, not back into the framework docs that produced the failures. |
| C1-misread | coined-term | F-55, E-49 | The AI's interpretation of "C1 English speakers" as a license for ornate/literary register, instead of as a comprehension-capability marker. |
| dimensionally-compressed-terms strategy | structural-reference | B-16 | The notes.md addendum strategy: transliteration with first-use gloss; one of two operational strategies in the entire framework. |

### Recency Distribution

| Region | newest | oldest | no-mtime-count | total-items |
|---|---|---|---|---|
| A (advanced_principles.md) | 2026-04-11T13:19:49Z | 2026-04-11T13:19:49Z | 0 | 1 file |
| B (notes.md) | 2026-04-11T13:12:49Z | 2026-04-11T13:12:49Z | 0 | 1 file |
| C (harmony_layer.md) | 2026-03-28T22:05:57Z | 2026-03-28T22:05:57Z | 0 | 1 file |
| D (org.md) | 2026-06-03T20:36:04Z | 2026-06-03T20:36:04Z | 0 | 1 file |
| E (eng.md) | 2026-06-03T20:59:48Z | 2026-06-03T20:59:48Z | 0 | 1 file |
| F (conversation exchanges) | — | — | 7 | 7 events (no filesystem backing) |
| G (memories) | 2026-06-03T22:17:41Z | 2026-06-03T21:36:56Z | 0 | 2 files |

**Recency observation (signal only, not verdict):** the three framework docs (A, B, C) are ~2 months old (late March / early April 2026); the failure and the extracted lessons (D, E, F, G) are today (June 3, 2026). This describes a temporal layout where the framework predates the failure-pattern observations by ~2 months. This is captured as data only; relevance was determined by content fit to the inquiry's purpose (per §2.1 Recency-as-signal-not-verdict separation), not by mtime.

### Frontier Flags

- **FF-1** — Does the framework have any META mechanism for ingesting feedback memories back into the docs (a "memory → spec" flow)? Surfacing examined the architectural separation (G-59) but did not investigate whether such a flow exists or is feasible. *Suggested refined-sub-purpose for re-invocation:* "examine comprehenslate for any feedback-ingestion mechanism."
- **FF-2** — Are there other translations in `mytrasnlations/` that would corroborate or refute the systemic-vs-isolated character of the register pull-up pattern? Surfacing did not check sibling translation folders. *Suggested refined-sub-purpose:* "examine other translations in mytrasnlations/ for register pull-up signature."
- **FF-3** — Is the AI's "C1 English speakers" misread (F-55, E-49) a one-time interpretive error or a recurrent AI-translation-pattern? Surfacing surfaced only this instance. *Suggested refined-sub-purpose:* "examine AI translation behavior under similar audience specs."
- **FF-4** — `notes.md` B-16 ("dimensionally compressed terms") strategy — is it being over-applied? Surfacing observed over-application but did not measure the over-application rate or examine whether the strategy itself needs constraints. *Suggested refined-sub-purpose:* "examine when transliteration-with-gloss helps vs. harms register fidelity."

### Workspace-Populated Status

`{populated: true, populated-at: 2026-06-03T23:30Z, extent: "all 7 territory regions traversed; 60 items tagged"}`

---

## Telemetry

- Mode: artifact; entry point: signal-first
- Cycles run: 1 (single traversal across all 7 regions sufficed for explicit-bounded territory of this size)
- Items enumerated: 60
- Items tagged: core: 26 | sub: 22 | side: 4 | umbrella: 0 | total HIGH-confidence rejections: 0
- Confidence distribution: HIGH: 47 | MEDIUM: 11 | LOW: 2
- Sub-phase fired: NO (Boundary-discovery skipped; territory explicit-bounded)
- Convergence: criteria met — all regions traversed, no items filtered at uncertain level, inclusion-under-uncertainty applied (asymmetric-failure principle)
- Workspace-overload trigger: NOT FIRED
- `items_with_mtime: 7` / `items_without_mtime: 7` (the 7 conversation-event items in Region F lack filesystem backing)
- Failure modes checked: missed-relevance, surfaced-irrelevance, over-coverage, territory-mis-binding, workspace-overload, artifact-under-specification, workspace-artifact-desync, recency-equates-idleness, recency-bias-filter, interpretive-overstep, purpose-loss, self-coupling-to-downstream. None triggered.

## Self-Assessment Verdict

**PROCEED with FLAG**

Verdict justification: All convergence criteria met; coverage of bounded territory is complete; relevance attribution is internally consistent (no incompatible multi-tagging); the central finding (C-28 + E-46 + G-59 chain) is supported by multiple cross-region items. PROCEED is warranted.

The FLAG is for downstream consumer awareness:

- The four frontier flags above (FF-1 through FF-4) raise questions surfacing did not resolve; they are appropriate for sense-making to consider whether to ingest or defer.
- The two-month temporal gap between framework docs (A/B/C) and failure observations (D-G) is a salient context that sense-making will need to interpret without sliding into "the docs are old, that's why" — recency-equates-idleness is a LAYER-1 failure mode the downstream operation must avoid.
- The interpretive question of whether C-28 (register at Tier 3) is a misclassification or a deliberate choice belongs to sense-making, not surfacing. Surfacing reports the classification verbatim; the verdict on its rightness is downstream.
