# Surfacing — Loop Diagnose: SD vs TC Misrouting

## User Input

Input file: `_branch.md` (Correction Chain declares 2 prior inquiry chains + inline conversation correction).
Articulation bundle: `articulate_simple.md` (HIGH-PROCEED).
Required reads per LOOP_DIAGNOSE Step 2: archived discipline outputs of both prior inquiries.

---

## Mode + Entry Point + Reception

- **Mode:** artifact-dominant — territory contains concrete archived discipline outputs from 2 prior inquiry chains + concrete schema files. Some possibility (failure hypotheses generated).
- **Entry point:** signal-first — diagnostic purpose explicit.
- **Territory specification:** explicit-bounded — the two inquiry folders + conversation correction + comparative-evidence files (`config_base_source.md`, `translation_config.py`).
- **Sub-phase fired:** NO.
- **Purpose echo:** identify where in the chain (chunking principle articulation → edge-cases application → edge-cases critique) the SD-vs-TC misrouting was locked in and not caught; produce evidence-backed failure hypotheses + maintenance candidates.

---

## Traversal Trace

### Region R1 — The principle as articulated in the chunking finding (anchor evidence)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 1 | Chunking finding line 113 verbatim: *"Schema ownership matches data ownership. Source-natural-units are properties of the source ... SourceDescriptor is the natural home"* | **core** | HIGH | The principle is anchored to **source-natural-units specifically**, not abstracted to "any source-fact." This anchoring is the principle-articulation evidence |
| 2 | Chunking finding line 115: *"chunking_budget depends on the LLM API in use, not on user translation strategy. It should not contaminate TranslationConfig, which captures translation-strategy choices"* | **core** | HIGH | The TC characterization is "translation-strategy choices" — a strong, specific framing. This framing was AVAILABLE for the edge-cases inquiry to test against |
| 3 | Chunking finding §3 routings: `source_chunking_units` → SD; `chunking_strategy` → TC; `chunking_budget` → PC | **core** | HIGH | All three routings in chunking finding are CORRECT applications. No misrouting in chunking finding itself |
| 4 | Chunking finding §3 "deeper insight": *"Chunking is the granularity mechanism for all 8 axes — it defines the unit at which TranslationConfig values apply"* | sub | HIGH | This insight reinforces the principle but is chunking-specific |

### Region R2 — The misrouting as committed in the edge-cases inquiry

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 5 | Edge-cases finding's per-field decision table: 4 SourceDescriptor additions — `source_language_fluency`, `source_edition`, `source_temporal_register`, `quranic_citation_policy` | **core** | HIGH | 3 of 4 misrouted per conversation correction (`source_edition` is correct) |
| 6 | Edge-cases finding's P3 code sketches: `SourceDescriptor.source_language_fluency: dict[str, FluencyLevel]` with example `{"tr": "native", "ar": "reading-only"}` | **core** | HIGH | The example is patently about THE READER (a Turkish reader who reads Arabic only). The code itself is reader-property-shaped but was routed to source-descriptor |
| 7 | Edge-cases finding's P3 docstring for `source_language_fluency`: *"Refines A3 source_culture by adding the fluency dimension WITHOUT modifying A3"* | **core** | HIGH | The docstring EXPLICITLY says it refines A3 — A3 lives on TranslationConfig. Refining a TC field by adding to SD is structurally inconsistent. This is a direct internal contradiction that critique didn't catch |
| 8 | Edge-cases finding's P3 `source_temporal_register: Literal["preserve-archaic", "modernize-fully", "hybrid-by-register-domain", "mark-archaisms-explicitly"]` | **core** | HIGH | The literals are STRATEGY choices (verbs of handling: preserve / modernize / hybrid / mark). The field shape matches A5 source_fidelity exactly |
| 9 | Edge-cases finding's P3 `EmbeddedLanguagePolicy.quranic_citation_policy` | **core** | HIGH | Bundling a strategy enum INSIDE a source-property declaration is structurally inconsistent — the AI noted this itself in conversation correction |

### Region R3 — Existing 8-axis TC pattern (comparative evidence)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 10 | `A1 reader_level: Literal["very_basic", "daily", "conversational", "advanced", "native"]` on `TranslationConfig` | **core** | HIGH | Pure reader-property → TC. Pattern source_language_fluency should have followed |
| 11 | `A2 domain_expertise: Literal["lay", "aware", "educated", "trained", "expert"]` on TC | **core** | HIGH | Pure reader-property → TC |
| 12 | `A3 source_culture: Literal["outsider", "acquainted", "familiar", "heritage", "source-native"]` on TC | **core** | HIGH | Reader's relationship-to-source property → TC. The exact paradigm source_language_fluency should have matched |
| 13 | `A5 source_fidelity: Literal["foreignized-max", "foreignized", "balanced", "lightly-domesticated"]` on TC | **core** | HIGH | Strategy enum for handling source → TC. The exact paradigm `source_temporal_register` (a strategy enum) should have matched |
| 14 | `A6 form_preservation`, `A7 scaffolding`, `A8 analysis_depth` — all strategy-shaped enums on TC | sub | HIGH | Reinforces the pattern: strategy enums → TC |

### Region R4 — Edge-cases inquiry's critique stage (where misrouting should have been caught)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 15 | Critique's 8 dimensions: Correctness, Coherence, Feasibility, Robustness, Completeness, Anti-bloat-fit, Synthesis-rigor, External-anchor compliance | **core** | HIGH | **NO dimension explicitly tests "does this routing decision actually apply the inherited principle correctly?"** Correctness asks "does it solve the problem" not "does it correctly apply the principle being inherited" |
| 16 | Critique's Frame-premise test on 3 SV6 premises: split-placement-extends; anti-bloat-trumps-comprehensiveness; DEFERs-don't-break-current-work | **core** | HIGH | All 3 premises were declared "SURVIVE" but the test was abstract. The premise "split-placement extends uniformly to the 14 edge-cases" was NEVER tested by applying it to the specific source-property-vs-strategy distinction |
| 17 | Critique's P3 (SourceDescriptor code) evaluation: "concrete pydantic code; type-safe; pattern-matches existing schema design ... Composability with chunking finding's SourceDescriptor noted explicitly" | **core** | HIGH | The critique focused on code-quality and composition, NOT on whether each field actually belonged in SD. Substance-axis test was about "is the code substantive" not "is the routing substantive" |
| 18 | Critique's substance-axis prosecution for P3: missed the contradiction in #7 above (docstring says "refines A3" while routing to SD) | **core** | HIGH | This is the smoking gun. The substance-axis prosecution didn't apply the candidate's own claims (refining A3) against its own routing (to SD) |
| 19 | Critique's verdict on P3: SURVIVE clean — no caveat | **core** | HIGH | The critique cleanly approved the misrouting |
| 20 | Critique's verdict on P6 (cross-axis check): SURVIVE with caveat (missing additions × additions interactions) | sub | MED | The cross-axis check examined axis-interactions but did NOT test whether each addition was in the right schema home |

### Region R5 — Edge-cases inquiry's earlier stages (where misrouting was first proposed and not flagged)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 21 | Edge-cases sensemaking SV6: "4 ADD-now-to-SourceDescriptor: #2 + #3 + #8 + #13" — this is where the routing was first locked in | **core** | HIGH | SV6 stabilized the misrouting; no later stage challenged it |
| 22 | Edge-cases sensemaking ambiguity 4 (#2 A3 split): resolved as "add to SourceDescriptor — `source_language_fluency`" with reasoning "A3 keeps its existing meaning; the new field captures language-fluency" | **core** | HIGH | The sensemaking resolution itself contradicts the principle: A3 is on TC; if the new field "refines A3" it should be on TC, not SD. The contradiction was present at sensemaking, propagated through |
| 23 | Edge-cases innovation P3 principal candidate: produced the EmbeddedLanguagePolicy + 4 SD field sketches | **core** | HIGH | Innovation didn't catch the misrouting; per-piece Inversion-candidates at intervention-shape axis didn't test schema-home axis |
| 24 | Edge-cases innovation's per-piece Inversion-candidate for P3: REORGANIZE-WITHOUT-ADDING (fold into single dict[str, Any]) | sub | HIGH | The Inversion-axis was "structure of additions" not "schema home of additions." Inversion missed the relevant axis |
| 25 | Edge-cases decomposition's P3 question: "What does each SourceDescriptor addition look like as a pydantic field signature?" | **core** | HIGH | The piece's question PRESUPPOSES SourceDescriptor as the home. The decomposition itself encoded the misrouting into the piece structure |

### Region R6 — Chunking finding's stages (where principle was articulated; check whether it was sharp enough)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 26 | Chunking sensemaking SV3 → SV6: produced the principle from the Definitional/Internal-Consistency perspective | sub | HIGH | Principle was derived from a specific case (chunking); the abstraction to "any source-fact" was not explicit |
| 27 | Chunking critique's dimensions: 8 dimensions including Pattern-consistency (project-specific risk) | sub | MED | Pattern-consistency dimension tested whether the routing fits existing patterns. Could have explicitly tested principle-application correctness but framing was "matches existing schema-design idiom" |
| 28 | Chunking finding's "deeper insight": chunking is "granularity mechanism" — the abstraction stayed chunking-specific | sub | HIGH | The principle was never abstracted in chunking finding to a general "facts about X vs strategies for X" form |

### Region R7 — Conversation correction signal (comparative evidence; NOT ground truth per LOOP_DIAGNOSE)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 29 | User pushback: *"this doesnt make sense no? why SourceDescriptor has such field? it feels like translationconfig field"* | **core** | HIGH | The PRIMARY correction signal. Triggered the AI's reconsideration |
| 30 | AI's snippet correction: identifies that A1/A2/A3 are reader-properties on TC, and `source_language_fluency` fits that pattern | **core** | HIGH | The structural argument the snippet makes (compare to existing pattern A1/A2/A3) was AVAILABLE during the original inquiries. No new evidence emerged in conversation — the corrective insight was reachable from the existing substrate |
| 31 | AI's self-diagnosis: *"What I conflated: 'this source HAS embedded Arabic' (source property → SD) with 'how the translator should RENDER embedded Arabic' (strategy → TC)"* | **core** | HIGH | Names the conflation pattern: facts-about-X (source) vs strategies-about-handling-X. This is the pattern the loop failed to articulate as a distinguishing test |

### Region R8 — Failure-mode candidates (possibility — to be sharpened in sensemaking)

| # | Item | Relevance | Conf | Note |
|---|---|---|---|---|
| 32 | **Principle under-sharpening (chunking finding):** principle articulated only for specific case (source-natural-units), not abstracted to facts-vs-strategies. Downstream had to make abstraction itself; abstraction conflated | **core** | HIGH | Hypothesis 1 candidate |
| 33 | **Critique dimension gap (edge-cases inquiry):** no dimension explicitly tested "does this routing apply the inherited principle correctly?" | **core** | HIGH | Hypothesis 2 candidate |
| 34 | **Substance-axis prosecution miss (edge-cases inquiry):** the substance-axis test on P3 didn't apply candidate's own claims (refines-A3 docstring) against its own routing (to SD) | **core** | HIGH | Hypothesis 3 candidate |
| 35 | **Decomposition encoded the misrouting (edge-cases inquiry):** P3's question presupposed SD as the home; no piece tested schema-home assignment | **core** | HIGH | Hypothesis 4 candidate |
| 36 | **Inherited Frame Audit weakness:** the audit fires at piece-level but the per-piece Inversion-axis chosen (intervention-shape) didn't include schema-home axis | sub | MED | Hypothesis 5 candidate |
| 37 | **Comparative-pattern test missing:** no stage explicitly compared each new field's shape to the existing 8-axis TC pattern (A1/A2/A3 reader-properties on TC) | **core** | HIGH | Hypothesis 6 candidate — strong because the AI's conversation correction USED this exact comparison and reached the right conclusion in one move |

---

## State Summary

### Territory + purpose echo

- **Territory:** chunking finding chain + edge-cases-into-config-schema finding chain + conversation correction + comparative-evidence files.
- **Purpose:** identify where in the chain the SD-vs-TC misrouting was locked in; produce LOOP_DIAGNOSE failure hypotheses + maintenance candidates.

### Coverage map

| Region | Coverage | Aggregate relevance |
|---|---|---|
| R1 — principle in chunking finding | confirmed | core (principle articulated correctly for specific case; not abstracted) |
| R2 — misrouting in edge-cases finding | confirmed | core (4 SD additions; 3 misrouted; internal contradiction in #7) |
| R3 — existing 8-axis pattern (comparative) | confirmed | core (A1/A2/A3 reader-properties on TC; A5 strategy enum on TC — the patterns the misrouted fields should have matched) |
| R4 — edge-cases critique stage | confirmed | core (8 dimensions; no principle-application-correctness dimension; substance-axis missed the docstring contradiction) |
| R5 — edge-cases earlier stages | confirmed | core (misrouting first proposed in sensemaking SV6; encoded into decomposition's P3 question) |
| R6 — chunking finding earlier stages | confirmed | sub-to-core (principle articulated specifically; abstraction not made; chunking critique didn't generalize the test) |
| R7 — conversation correction | confirmed | core (uses A1/A2/A3 pattern comparison; insight reachable from substrate) |
| R8 — failure-mode candidates | confirmed possibility | core (6 hypotheses with HIGH/MED confidence pending sensemaking) |

### Concept-names list

- **principle anchoring** — chunking finding's principle articulated to a specific case (source-natural-units); not abstracted to "any source-fact vs any user-strategy"
- **facts-vs-strategies conflation** — the deep pattern: confusing "this source HAS X" with "the user wants to handle X this way"
- **internal contradiction missed by substance-axis** — P3 docstring says "refines A3" while routing to SD; substance-axis prosecution didn't apply candidate's own claims against its own decision
- **decomposition-encoded misrouting** — P3's question presupposed the schema home; later stages couldn't unmake the encoding
- **comparative-pattern test missing** — no critique dimension compared new fields against existing 8-axis routing patterns
- **principle-application-correctness** — a missing dimension/test in the loop's checking machinery
- **CHAIN-SCOPE-OF-DIAGNOSIS** (from articulate_simple) — the diagnostic scope is the chain, not a single inquiry
- **reachable-from-substrate** — the conversation correction used only substrate already present in the inquiries; no new evidence was needed; the correction was within the inquiries' reach but they didn't reach it

### Frontier flags

Open questions for sensemaking:

1. **Hypothesis attribution:** is the failure primarily principle-under-sharpening (R6 chunking), application-failure (R5 edge-cases sensemaking), or critique-blind-spot (R4 edge-cases critique)? Or mixed?
2. **Substance-axis prosecution refinement:** could a sharpened substance-axis sub-rule ("apply candidate's own internal claims as test for its routing") have caught the misrouting? Evaluation gate?
3. **Comparative-pattern test:** should a new critique dimension or sensemaking perspective explicitly test "does this routing match the comparative pattern of existing fields in the target schema"?
4. **Principle abstraction:** should principles articulated in foundational findings be required to state both the specific case AND the abstract form?
5. **Decomposition piece-question audit:** should decomposition explicitly mark pieces whose questions presuppose a routing decision, and surface that presupposition to critique?
6. **Loop framework completeness:** is the loop structurally capable of catching this kind of error, or is the framework blind to it? (Per LOOP_DIAGNOSE: allow attribution to loop framing.)
7. **Maintenance candidate selection:** which 1-2 candidates have strongest evidence and concrete evaluation gates?

### Workspace-populated status

- populated: true | populated-at: 2026-06-14_02-35 | extent: R1-R8 traversed; 37 items tagged; chunking finding line 113 quoted verbatim; comparative evidence enumerated.

---

## Telemetry

- **Mode:** artifact-dominant + possibility | **Entry point:** signal-first
- **Cycles run:** 1
- **Items tagged:** 37
- **Tag distribution:** core = 27; sub = 9; side = 0; umbrella = 0; LOW-confidence = 0
- **Sub-phase fired:** NO
- **Failure modes checked (LAYER 1):** all 9 — NONE fired
- **items_with_mtime:** 5 (chunking finding; edge-cases finding; config_base_source; translation_config.py; conversation correction is in-context not on disk) | **items_without_mtime:** 32 (possibility items + verbatim quote items)

### Self-Assessment Verdict

**PROCEED**

Strong evidence base: chunking finding's principle quoted verbatim (line 113); 3 misrouting cases concrete with internal-contradiction smoking-gun (item 7 docstring-vs-routing contradiction); 6 hypothesis candidates with HIGH-MED confidence; LOOP_DIAGNOSE guardrails respected (conversation correction treated as comparative evidence; attribution allows mixed; substrate-reachability noted to prevent ground-truth-inversion).
