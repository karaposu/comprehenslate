# Surfacing — a1_vocabulary_breadth_levels

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_15-34__a1_vocabulary_breadth_levels/_branch.md`

## Mode + Entry Point

- **Mode:** hybrid (`artifact` for prior finding + project corpus + user seed; `possibility` for established vocabulary-level frameworks + concept-space candidates + distinguishing-logic candidates)
- **Entry point:** `signal-first` (purpose is given explicitly: define 5 levels for vocabulary-breadth)
- **Territory specification:** `explicit-bounded` for artifact regions; `abstract-bounded` for possibility regions
- **Boundary-discovery sub-phase:** SKIPPED (territory is pre-specified)

## Purpose Echo

Define the 5 ordinal levels for the vocabulary-breadth sub-field of A1 Reader Level (per the prior `translation_config_axes` finding) — names, concepts, distinguishing logic, examples, language-agnostic at the concept level. Scope: vocabulary-breadth ONLY (not the other 4 sub-fields of A1, not the other 7 axes).

## Territory Echo

Bounded territory consists of:

- **Region A** — prior inquiry's finding for A1 Reader Level + vocabulary-breadth sub-field (1 item)
- **Region B** — user's seed naming + user's prior framing fragments (3 items)
- **Region C** — established vocabulary-level frameworks (12 items)
- **Region D** — existing project knobs / commitments (3 items)
- **Region E** — vocabulary-breadth concept space (7 items)
- **Region F** — distinguishing-logic candidates (6 items)
- **Region G** — auto-memory feedback signals (2 items)
- **Region H** — concrete vocabulary examples (word pairs across registers) (8 items)
- **Region I** — adjacent-level boundary candidates (4 items)
- **Region J** — translator-AI operationalization (3 items)

---

## Traversal Trace

| # | Region | Item ID | Verdict | Conf | Recency annotation | Step note |
|---|---|---|---|---|---|---|
| 1 | A | A1. `translation_config_axes/finding.md` — A1 Reader Level spec including vocabulary-breadth sub-field's concept ("how many words the reader recognizes (passive vocabulary)") | core | HIGH | `{source: filesystem, value: 2026-06-05T15:21:28Z}` | the inherited commitment; vocabulary-breadth is about RECOGNITION not PRODUCTION |
| 2 | B | B1. User's seed naming: `very_basic | daily | conversational | advanced | native` (5 ordinal levels) | core | HIGH | `{source: filesystem, value: 2026-06-05T15:35:17Z}` | starting candidate; validate or refine |
| 3 | B | B2. User's word-pair example from prior inquiry: "high-breadth reader recognizes 'ratiocination' or 'ostensibly'; low-breadth needs 'reasoning' or 'apparently'" | core | HIGH | `{source: filesystem, value: 2026-06-05T15:35:17Z}` | concrete example pair illustrating the high vs low end of the spectrum |
| 4 | B | B3. User's "backpacker level conversational knowledge" framing (from `my_notes.md`) | core | HIGH | `{source: filesystem, value: 2026-03-28T21:12:18Z}` | informs the conversational level: someone who can carry conversation but misses idioms / register subtleties |
| 5 | C | C1. CEFR (Common European Framework of Reference) — A1 / A2 / B1 / B2 / C1 / C2 (6 levels of language proficiency, including vocabulary) | core | HIGH | `{source: none, value: null}` | the most established international framework; structurally a 6-level scale; widely understood across languages |
| 6 | C | C2. ACTFL proficiency guidelines — Novice / Intermediate / Advanced / Superior / Distinguished (5 levels, US foreign-language teaching) | core | HIGH | `{source: none, value: null}` | exactly 5 levels — direct structural reference for the inquiry's 5-level commitment |
| 7 | C | C3. ILR (Interagency Language Roundtable) — 0 (No Proficiency) / 1 (Elementary) / 2 (Limited Working) / 3 (Professional Working) / 4 (Full Professional) / 5 (Native or Bilingual) (6 levels, US government scale) | core | MEDIUM | `{source: none, value: null}` | another 6-level scale; informs the high end (Level 5 "native or bilingual") |
| 8 | C | C4. Graded readers in language pedagogy — Penguin Readers Levels 1–6, Oxford Bookworms Stages 1–6 (concrete vocabulary-controlled reading materials) | sub | HIGH | `{source: none, value: null}` | each level specifies word-count limits (e.g., Stage 1 = 400 headwords, Stage 6 = 2500 headwords); concrete operationalization |
| 9 | C | C5. Lexile reading levels — quantitative reading framework | sub | MEDIUM | `{source: none, value: null}` | quantitative but vocabulary is one of two factors (the other is sentence length); less directly aligned to vocabulary-breadth alone |
| 10 | C | C6. Flesch-Kincaid readability scores | side | LOW | `{source: none, value: null}` | mostly syntactic (sentence length + syllables per word); less about vocabulary breadth per se |
| 11 | C | C7. Zipf's law / word frequency distributions — universal long-tail pattern of word usage in any natural language | core | HIGH | `{source: none, value: null}` | the language-agnostic empirical basis: every language has high-frequency vs low-frequency vocabulary; the levels can be defined as frequency-band tiers |
| 12 | C | C8. BNC / COCA / OEC frequency bands — empirical English-vocabulary frequency lists | sub | MEDIUM | `{source: none, value: null}` | useful for English examples but language-specific; the concept (frequency bands) is universal, the specific bands are not |
| 13 | C | C9. GSL / AWL / NGSL — General Service List / Academic Word List / New General Service List (pedagogical English word lists) | sub | HIGH | `{source: none, value: null}` | concrete English-vocabulary operationalizations; e.g., NGSL ~2800 words cover ~92% of general English text |
| 14 | C | C10. Schmitt's Vocabulary Levels Test — measures receptive vocabulary size at 2000 / 3000 / 5000 / 10000 frequency bands | sub | MEDIUM | `{source: none, value: null}` | direct operationalization of receptive vocabulary size; bands per-language |
| 15 | C | C11. Receptive vs productive vocabulary literature — the well-established asymmetry that recognition exceeds production by 2–3x typically | core | HIGH | `{source: none, value: null}` | the prior finding's A1 explicitly committed to RECEPTIVE (recognition) vocabulary; this constrains how levels are defined (what one understands, not what one can produce) |
| 16 | C | C12. L1 acquisition curves — what children know at what age (e.g., 5-year-old natives ~5000 receptive words; 18-year-old educated ~20000+) | side | MEDIUM | `{source: none, value: null}` | informs the low end (very_basic = child-like vocabulary recognition) but not the system's primary user — adults at various levels |
| 17 | D | D1. `.env.example` — `AUDIENCE_LEVEL = native | late_learner | late_learner_simple` (existing 3-level enum) | core | HIGH | `{source: filesystem, value: 2026-03-29T15:55:57Z}` | existing project commitment; the new 5-level enum should be backwards-mappable (which late_learner level maps to which new level) |
| 18 | D | D2. prior `translation_config_axes/finding.md` — A1 cardinality "5 headline levels (proposed)"; composite-axis pattern; per-sub-field overrides | core | HIGH | `{source: filesystem, value: 2026-06-05T15:21:28Z}` | duplicate of A1 but called out separately for cross-region linkage |
| 19 | D | D3. `my_notes.md` — "backpacker level conversational knowledge ... won't understand idioms" | sub | HIGH | `{source: filesystem, value: 2026-03-28T21:12:18Z}` | informs the conversational level boundary; though idiom-recognition is a separate sub-field, the user's framing here mentions conversational + idiom-limit together |
| 20 | E | E1. Receptive vocabulary size (number of words recognized) — measurable via Schmitt's test or similar | core | HIGH | `{source: none, value: null}` | primary concept the field operationalizes |
| 21 | E | E2. Word frequency tier the reader is comfortable with (top 500? top 5000? top 20000?) | core | HIGH | `{source: none, value: null}` | the most direct operationalization; language-agnostic in concept (any language has frequency tiers) |
| 22 | E | E3. Lexical density tolerance | sub | MEDIUM | `{source: none, value: null}` | how many low-frequency words per sentence the reader tolerates without breakdown |
| 23 | E | E4. Register tier (everyday / colloquial / journalistic / literary / technical / archaic) | core | HIGH | `{source: none, value: null}` | vocabulary-breadth has a register dimension — high-breadth readers handle archaic / literary; low-breadth readers stick to everyday |
| 24 | E | E5. Word concreteness vs abstractness tolerance | sub | LOW | `{source: none, value: null}` | weakly related; more about abstract-argument processing than vocabulary breadth per se |
| 25 | E | E6. Etymological transparency — in English, Germanic vs Latinate/Greek tendency at higher registers | sub | MEDIUM | `{source: none, value: null}` | English-specific phenomenon; analogues exist in other languages (e.g., Sino-Japanese vs native Japanese vocabulary registers in Japanese); the CONCEPT is universal even if the realization is language-specific |
| 26 | E | E7. Specialized vocabulary tolerance — technical / archaic / dialectal | core | HIGH | `{source: none, value: null}` | the highest level should accommodate this; lower levels should require translator to gloss or substitute |
| 27 | F | F1. Frequency-tier-based distinguishing logic — each level corresponds to a frequency band (e.g., very_basic = top 500 words; native = no frequency restriction) | core | HIGH | `{source: none, value: null}` | clean operational logic; language-agnostic at concept; bands per-language |
| 28 | F | F2. Reader-profile-based logic — each level corresponds to a TYPE OF READER (e.g., very_basic = small child / brand-new learner; native = educated adult native speaker) | core | HIGH | `{source: none, value: null}` | intuitive logic that translates to prompt instructions; the user's seed names (very_basic / daily / conversational / advanced / native) implicitly use this logic |
| 29 | F | F3. Substitution-test logic — at each level, what kind of word would the translator REPLACE with a simpler version, and at what level does the substitution stop? | core | HIGH | `{source: none, value: null}` | THIS is how the translator-AI operationalizes the level — substitution is the runtime action |
| 30 | F | F4. Affordance-based logic — at each level, what reading tasks can the reader perform (e.g., follow a newspaper article? read literary fiction? handle technical text?) | sub | MEDIUM | `{source: none, value: null}` | useful for level descriptions; less directly operational |
| 31 | F | F5. Register-tier logic — each level corresponds to a register ceiling (very_basic = casual conversation only; native = any register including archaic literary) | core | HIGH | `{source: none, value: null}` | overlap with F1; register and frequency are correlated |
| 32 | F | F6. Coverage-based logic — what % of typical text the reader can decode without lookups (e.g., very_basic = 80% of children's text; native = 95%+ of any text) | sub | HIGH | `{source: none, value: null}` | empirical operationalization; ties to corpora |
| 33 | G | G1. `feedback_translation_register.md` — register fidelity rule (don't pull plain registers up to ornate) | core | HIGH | `{source: filesystem, value: 2026-06-03T21:36:56Z}` | constrains how levels interact with translator behavior — at low levels, register-preservation policy may FORCE the translator to use simpler vocabulary even when the source has high register; this needs to be acknowledged but the POLICY-vs-axis interaction is mostly out of scope |
| 34 | G | G2. `feedback_translation_polysemy.md` — local-construction trumps for sense selection | side | LOW | `{source: filesystem, value: 2026-06-03T22:17:41Z}` | tangential; polysemy is about sense disambiguation not vocabulary breadth |
| 35 | H | H1. ratiocination / ostensibly (high) vs reasoning / apparently (mid-low) — user's example pair | core | HIGH | `{source: none, value: null}` | concrete example pair; "reasoning" and "apparently" are conversational-or-daily-level English; "ratiocination" and "ostensibly" are advanced-or-native-level |
| 36 | H | H2. purchase (advanced) vs buy (daily); endeavor (advanced) vs try (daily); ameliorate (advanced) vs improve (daily) | core | HIGH | `{source: none, value: null}` | the classic Latinate/Germanic register pairs in English; informs the advanced-vs-daily distinction |
| 37 | H | H3. transubstantiation (advanced/specialized) vs change (very_basic); eschatology (specialized) vs end-times (advanced) vs ending (daily) | sub | HIGH | `{source: none, value: null}` | specialized-religious vocabulary spectrum; the boundary between "specialist requires domain expertise (A2)" and "specialist requires high vocabulary-breadth (A1)" matters |
| 38 | H | H4. anon (archaic) vs soon (daily); verily (archaic) vs truly (daily); thee (archaic) vs you (very_basic) | sub | HIGH | `{source: none, value: null}` | archaic register; native-level readers handle these; lower levels don't |
| 38b | H | H5. myocardial infarction (technical) vs heart attack (daily) | core | HIGH | `{source: none, value: null}` | classic technical-vs-lay pair; raises the A1 (vocabulary breadth) vs A2 (domain expertise) boundary question |
| 39 | H | H6. go / have / do / be (highest frequency function words) | sub | MEDIUM | `{source: none, value: null}` | the very_basic floor — words even the lowest-breadth reader knows |
| 40 | H | H7. carry / remember / decide (mid-frequency content words) | sub | MEDIUM | `{source: none, value: null}` | the daily zone — words a backpacker-level reader uses |
| 41 | H | H8. transport / recollect / ascertain (lower-frequency content words) | core | HIGH | `{source: none, value: null}` | the advanced zone — words an educated reader knows but a daily-level reader may need translated |
| 42 | I | I1. very_basic → daily boundary: shift from "child / very-early-learner vocabulary" to "everyday adult-functional vocabulary" | core | HIGH | `{source: none, value: null}` | first boundary; conceptually the transition from learner-pidgin to functional |
| 43 | I | I2. daily → conversational boundary: shift from "everyday vocabulary used to function" to "vocabulary an educated adult uses in casual but informed conversation" | core | HIGH | `{source: none, value: null}` | second boundary; subtle — daily and conversational may merge in some readings; needs sensemaking work |
| 44 | I | I3. conversational → advanced boundary: shift from "spoken/conversational register" to "written/educated register including Latinate and abstract vocabulary" | core | HIGH | `{source: none, value: null}` | third boundary; this is where Latinate / Greek-derived / academic vocabulary enters |
| 45 | I | I4. advanced → native boundary: shift from "well-educated reader handles formal vocabulary" to "anyone-can-read-anything — archaic, dialectal, specialist, literary" | core | HIGH | `{source: none, value: null}` | fourth boundary; the highest level; subsumes everything plus archaic / dialectal / specialist that even an educated non-native might miss |
| 46 | J | J1. Translator-AI prompt instruction per level (each level's prose description becomes part of the prompt context) | sub | HIGH | `{source: none, value: null}` | the per-level prose is what operationalizes; needs to be writable directly into the level definition |
| 47 | J | J2. Substitution choices per level (at very_basic, replace `ratiocination` → `careful thinking`; at advanced, keep `ratiocination` as-is) | core | HIGH | `{source: none, value: null}` | the runtime translator action — substitute when target level < word's level |
| 48 | J | J3. Level-vs-source-content interaction: when source has technical vocabulary (e.g., Quranic-Arabic terms) and target level is low, what happens? Does the translator gloss, substitute, footnote, or upgrade the audience level? | sub | HIGH | `{source: none, value: null}` | mostly out of scope (interacts with A7 Scaffolding + POLICY layer) but worth flagging for sensemaking |

---

## State Summary

### Coverage map

| Region | Coverage | Aggregate verdict | Notes |
|---|---|---|---|
| A — prior finding | confirmed | core | the A1 + vocabulary-breadth section read |
| B — user input | confirmed | core (3/3) | seed naming + word-pair example + backpacker framing |
| C — established frameworks | confirmed | core (5 core, 5 sub, 1 side, 1 low) | CEFR (6-level), ACTFL (5-level), ILR (6-level), graded readers, Zipf, frequency-lists, corpora |
| D — project knobs | confirmed | core (2 core, 1 sub) | existing AUDIENCE_LEVEL + prior finding A1 + my_notes |
| E — concept space | confirmed | core (4 core, 3 sub) | size / frequency / lexical-density / register / concreteness / etymological-transparency / specialist |
| F — distinguishing logic | confirmed | core (4 core, 2 sub) | frequency / reader-profile / substitution-test / affordance / register / coverage |
| G — auto-memory | confirmed | mixed (1 core, 1 side) | register-policy directly informs; polysemy tangential |
| H — concrete examples | confirmed | core (5 core, 4 sub) | word pairs across registers / specialties / archaic |
| I — level boundaries | confirmed | core (4/4) | very_basic→daily, daily→conversational, conversational→advanced, advanced→native |
| J — operationalization | confirmed | core (1 core, 2 sub) | prompt instructions, substitution actions, source-level interaction |

### Confirmed-absent regions

None. Every region produced at least one relevant item.

### Concept-names list

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| vocabulary-breadth | structural-reference | A1 (prior finding) | the sub-field being operationalized |
| RECEPTIVE vocabulary | vocabulary | C11, A1 | what one understands, not what one says — committed at prior finding |
| frequency band | vocabulary | C7, C8, C10, F1 | a tier of words ranked by usage frequency |
| Zipf's law | vocabulary | C7 | universal long-tail vocabulary distribution |
| CEFR | vocabulary | C1 | 6-level European language framework |
| ACTFL | vocabulary | C2 | 5-level US foreign-language teaching framework |
| ILR | vocabulary | C3 | 6-level US government language scale |
| register tier | vocabulary | E4, F5 | everyday / colloquial / journalistic / literary / technical / archaic |
| Latinate vs Germanic | vocabulary | E6, H2 | English-specific register marker via etymology |
| substitution-test logic | coined-term | F3, J2 | the operational logic — at each level, what kind of word does the translator replace? |
| frequency-tier logic | coined-term | F1 | each level = a frequency band |
| reader-profile logic | coined-term | F2 | each level = a type of reader |
| coverage-based logic | coined-term | F6 | each level = % of typical text decodable without lookup |
| receptive-vs-productive asymmetry | vocabulary | C11 | recognition exceeds production by ~2-3x in typical learners |
| backpacker level | coined-term | B3, my_notes.md | the user's framing for conversational-tier readers |
| graded readers | vocabulary | C4 | language-pedagogy concrete vocabulary-controlled materials (Penguin / Oxford Bookworms) |
| A1 (CEFR level) | vocabulary | C1 | label collision with A1 (Reader Level axis in this project); needs clarification in writing |

### Recency distribution

| Region | Newest | Oldest | No-mtime-count | Total-items |
|---|---|---|---|---|
| A | 2026-06-05T15:21:28Z | 2026-06-05T15:21:28Z | 0 | 1 |
| B | 2026-06-05T15:35:17Z | 2026-03-28T21:12:18Z | 0 | 3 |
| C | — | — | 12 | 12 |
| D | 2026-06-05T15:21:28Z | 2026-03-28T21:12:18Z | 0 | 3 |
| E | — | — | 7 | 7 |
| F | — | — | 6 | 6 |
| G | 2026-06-03T22:17:41Z | 2026-06-03T21:36:56Z | 0 | 2 |
| H | — | — | 9 | 9 |
| I | — | — | 4 | 4 |
| J | — | — | 3 | 3 |

Recency is descriptive only per the spec; it does not adjudicate relevance.

### Frontier flags

These questions surfaced during traversal but were not resolved at the surfacing layer. They belong to downstream cognitive operations:

1. **Distinguishing-logic choice.** Multiple competing logics surfaced (F1 frequency-band, F2 reader-profile, F3 substitution-test, F4 affordance, F5 register-tier, F6 coverage). Should the levels be defined by ONE PRIMARY LOGIC with the others as cross-checks? Or by a COMBINATION? Sensemaking should adjudicate.

2. **Level-name validation.** The user's seed `very_basic | daily | conversational | advanced | native` is intuitive (uses reader-profile logic) but several frameworks (CEFR, ACTFL, ILR) use abstract level labels (A1/A2, Novice/Intermediate, 0/1/2/3/4/5). Should the inquiry stick with reader-profile names or switch to abstract labels? Sensemaking should adjudicate.

3. **Boundary subtlety: daily vs conversational.** The two seem close — "daily" suggests functional everyday vocabulary; "conversational" suggests educated-adult informal speech. Are these distinct enough to warrant two separate levels, or do they collapse? Sensemaking should test.

4. **Where does technical / specialist vocabulary live — A1 (vocabulary-breadth) or A2 (Domain Expertise)?** A reader knowing `myocardial infarction` could be either a high-A1 native English speaker OR an A1-medium reader with high A2 medical expertise. The two cases differ. The boundary between A1.specialist and A2 needs clarification.

5. **Backwards mapping to existing AUDIENCE_LEVEL.** The existing `.env.example` has 3 levels: `native | late_learner | late_learner_simple`. Does this map cleanly to a subset of the new 5 levels? (e.g., native → native; late_learner → conversational; late_learner_simple → daily or very_basic?) Migration-discipline question for the next inquiry, but worth flagging now.

6. **Language-agnosticism stress test specifically for vocabulary-breadth.** Frequency tiers exist in every language; register tiers exist in every language; but the SPECIFIC thresholds (what counts as "advanced vocabulary" in Russian vs Japanese vs English) differ. The level CONCEPT should be definable language-agnostically; level THRESHOLDS are per-language. This was settled at the prior inquiry's meta-level; this inquiry must verify it holds for the 5 specific levels.

7. **Receptive vs productive constraint.** All levels must be defined in RECEPTIVE terms (what the reader UNDERSTANDS when encountered). Definitions that slip into productive terms ("can use this vocabulary in writing") are out of scope per the prior finding's commitment.

8. **Specialized technical vocabulary's frequency-band trap.** A word like `eschatology` is low-frequency BUT high-register-AND-domain. A high-vocabulary-breadth reader might not know it (unless they're domain-expert); a domain-expert might know it without high general vocabulary. Frequency-band logic alone misses this; register/domain dimensions are needed.

### Workspace-populated status

`{populated: true, populated-at: 2026-06-05T15:42:00Z, extent: "10 regions, 48 items surfaced; territory traversed at sufficient resolution for 5-level definition"}`

### Re-invocation parameters

None requested. Sensemaking should be able to proceed without additional surfacing.

---

## Telemetry

- **Mode:** hybrid (artifact + possibility)
- **Entry point:** signal-first
- **Cycles run:** 10 (one per region)
- **Items enumerated:** 48
- **Items tagged at each relevance level:** core: 30 — sub: 14 — side: 4 — umbrella: 0
- **Confidence distribution:** HIGH: 37 — MEDIUM: 9 — LOW: 2
- **Sub-phase fired:** Boundary-discovery NO (territory explicit-bounded)
- **Convergence:** REACHED — all 10 regions traversed; no items filtered at uncertain-relevance; only HIGH-confidence rejection allowed (none in this run)
- **Workspace-overload trigger:** NOT fired
- **Failure modes checked:** Missed-relevance — none detected; Surfaced-irrelevance — bounded (side-tagged items remain for downstream filtering); Over-coverage — within budget; Territory-mis-binding — not detected (vocabulary-breadth scope honored; other sub-fields explicitly out of scope); Workspace overload — not approached; Artifact under-specification — schema fields populated; Workspace-artifact desync — captured at moment of tagging; Recency-Equates-Idleness — no item demoted on mtime grounds; Recency-Bias-Filter — none filtered on mtime; Interpretive-overstep — no cross-item relational structure (left to sensemaking); Purpose-loss — purpose held throughout
- **`items_with_mtime`:** 9 — **`items_without_mtime`:** 39
- **Self-assessment verdict:** **PROCEED**

---

## Self-Assessment

**Verdict: PROCEED.**

The 10-region territory was traversed at sufficient resolution. The prior finding's A1 commitments (composite-axis, recognition not production, language-agnostic at concept level) were brought into the workspace as inherited frame. The user's seed naming + word-pair examples were captured as the starting candidate set. Five established vocabulary-level frameworks (CEFR, ACTFL, ILR, graded readers, frequency-list pedagogy) were surfaced as theoretical and operational anchors — ACTFL stands out as the only one with exactly 5 levels. Six distinguishing-logic candidates (frequency-tier, reader-profile, substitution-test, affordance, register-tier, coverage-based) were enumerated for sensemaking to adjudicate. Four boundary regions (very_basic→daily, daily→conversational, conversational→advanced, advanced→native) were flagged for sensemaking to clarify. Concrete vocabulary examples spanning register, etymology, technicality, and archaicness were captured.

Eight frontier flags handed to sensemaking: distinguishing-logic choice; level-name validation; boundary subtlety (daily vs conversational); A1-vs-A2 boundary for specialist vocabulary; backwards mapping to existing AUDIENCE_LEVEL; language-agnosticism stress test; receptive-vs-productive constraint discipline; specialized-vocabulary frequency-band trap.

Scope discipline maintained: all 4 other A1 sub-fields are explicitly absent from the workspace (idiom-recognition, syntactic-processing-capacity, inference-capacity, cultural-reference-recognition were not surfaced beyond noting their separate-axis status). Other axes A2–A8 are absent except for the A1-vs-A2 boundary question (which is structural, not content). Pydantic shape and runtime conflict resolution are absent.

Ready for sensemaking.
