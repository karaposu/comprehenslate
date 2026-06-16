# Innovation — translation_config_axes

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_14-14__translation_config_axes/_branch.md` (with prior outputs: `surfacing.md`, `sensemaking.md`, `decomposition.md` in the same folder)

---

## Phase 1 — Seed

### Methodology-Mode Consideration

**Inherited mode** (from seed framing): **Standard default** (balanced 4G+3F; elaborate the committed direction; produce confident output for the open design points).

The seed framing is the decomposition's "Frontier handed to Innovation" section — 5 candidate-generation points within an inquiry whose architectural commitments are already settled at sensemaking SV6. The framing is neither contrarian-rethink nor depth-iteration; it asks Innovation to generate alternatives at specific open design points, then have critique select.

**Alternative mode considered:** **Generator-weighted exploration** (4 Generators carry the load; Framers light).

**What follows under the alternative:** Generator-weighted would emphasize Combination + Absence Recognition + Domain Transfer + Extrapolation to enumerate many candidate names / structures per generation point. This would yield more raw candidates but might neglect Framer-level checks — does this candidate name work under all evaluation conditions (developer reading the pydantic schema, translator using the system, LLM agent configuring itself, end-user reader receiving the translation)? Naming refinement and structural alternatives need both volume (Generator strength) and viability checks (Framer strength).

**Decision:** **Default to the inherited Standard mode.** The 5 generation points need both Generators (to produce candidates) and Framers (to test against evaluation conditions). The Standard default's balance fits.

### Seeds (one per generation point handed by decomposition)

| # | Seed | Seed type |
|---|---|---|
| S1 | Final name of the envelope-with-selective-override pattern (D6 / P3) | Question + Dissatisfaction (provisional name flagged as low-confidence by sensemaking) |
| S2 | Per-axis name refinements for A1–A8 | Question (user's sketched names are workable but not finalized) |
| S3 | Family naming — alternatives to Reader / Purpose / Strategy / Depth | Question (provisional meta-grouping vocabulary) |
| S4 | Default-bearing principle alternatives (conservative-bias is committed; what alternatives exist?) | Constraint (defaults are calibration-dependent) |
| S5 | A4 Purpose axis — categorical / partially-ordinal / preset-bundle-driven / hybrid (pattern association open) | Question |

The seeds share a common substrate: open design points within a settled architectural commitment (8 axes in 4 families across 4 layers, with envelope pattern at A1).

---

## Phase 2 — Generate

### Generator 1: Combination

#### Generic variation (Seeds 1, 2)
Combine the project's existing vocabulary tracks. The project corpus uses both Western translation-theory terms (Skopos, foreignization, register) and Islamic-rhetoric terms (nazm, ihlas, hasr, istilzam). Combination produces **bi-vocabulary axis names** — every axis has both a developer-facing name (English, schema-natural) and a translator-facing name (drawn from translation theory or Islamic rhetoric where applicable).

Example:
- A1 RCL — developer name `reader_competence` / translator name `reader_fluency_profile`
- A6 Form-Preservation Strength — developer name `form_preservation` / translator name `nazm_preservation_strength`

This is a Phase-2-internal combination of two vocabulary tracks already in the project's proximity.

#### Focused variation (Seed 1 — envelope pattern naming specifically)
Combine **CEFR's "Common Reference Levels" structure** with the project's **harmony_layer.md Tier system**. The pattern name candidates that emerge from this combination:
- `compound-level axis` (level = CEFR analog; compound = Tier-like aggregation)
- `headline-with-tiered-overrides` (headline = CEFR top-level; tiered overrides = Tier-style sub-decisions)

#### Contrarian variation (Seed 5 — Purpose axis structure)
Combine **Purpose axis** with **NOT-axis** (preset bundle). What emerges is **Purpose-as-bundle-selector** rather than Purpose-as-ordinal-level. The user picks a Purpose (`scholarly`, `devotional`, `casual`) and that PICK is also a preset for the other 7 axes. The Purpose axis becomes a meta-axis — it's both a configuration unit AND a bundle-selector.

---

### Generator 2: Absence Recognition

#### Patch-level absence (Seeds 1–3)
**Missing: a "preview" or "round-trip example" mechanism.** Across all 5 generation points, there's no mechanism for a user to SEE what the translation output would look like at a specific axis-value combination before committing. Naming refinements (Seeds 1, 2, 3) and the categorical-vs-ordinal Purpose question (Seed 5) would be much easier to evaluate with a small reference output per axis-value combination.

Patch-level absence: a **reference-example field** per axis level, showing 1-2 sentences of translated text representing what that level produces. This is a content addition to the per-axis spec, not a structural change.

#### Patch-level absence (Seed 4 — defaults)
**Missing: a default-justification field per default value.** The conservative-bias principle is stated at the framework level but each axis's specific default value isn't justified per-axis yet. Patch: add a `default_rationale` field per axis.

#### Redesign-level absence — "What if designed from scratch today?"
**The framework lacks a CASE-FRAME PRESET LAYER between the user and the 8 axes.** A user thinking "I'm translating Risale-i Nur for a casual English reader who knows nothing about Islamic terminology" doesn't naturally decompose into 8 axis values. They have a CASE in mind. The framework, designed from scratch today, would have:

- **Layer 1A (top)**: case-frame presets — named scenarios with all 8 axes pre-populated, expressed in user-natural language
- **Layer 1B (underneath)**: the 8 axes themselves, individually overridable from the preset

The 8 axes still exist, but the user's primary interface is the case-frame preset.

#### Redesign-level absence — "What is the project already doing in a less articulated way?"

Looking at the `.env.example`, the project ALREADY has a partial case-frame layer in disguise: `AUDIENCE_LEVEL=native | late_learner | late_learner_simple` is a case-frame ("the audience is native English speakers" / "late learners" etc.), and `DEPTH_PROFILE=surface | standard | deep | scholarly` is also a case-frame for purpose. These are PRESET-VALUE LABELS, not pure axes. So the case-frame preset layer is ALREADY partly present in narrative form in `.env.example`; the absence isn't of the concept but of its formalization.

---

### Generator 3: Domain Transfer

#### Native-domain source (Seeds 2, 3)
**Source domain: Halliday's register theory (field / tenor / mode).** This is the canonical translation-theory triad for describing communicative situations. Applied as alternatives:
- Family name candidates: `Field` (what the text is about — relates to Domain Expertise) / `Tenor` (relationship between participants — relates to Reader and Purpose families) / `Mode` (medium and rhetorical role — relates to Strategy family).

The Halliday triad doesn't cleanly map to 4 families but suggests a 3-family alternative: **{Field, Tenor, Mode} + Analysis Depth** as a 4th outside the triad.

#### Native-domain source (Seed 5 — Purpose pattern)
**Source domain: Skopos theory's text-typology (informative / expressive / operative + audiomedial).** Reiss's text-typology suggests Purpose categories aren't strictly ordinal — they're typological. This supports keeping A4 as CATEGORICAL (not ordinal).

#### Deliberately-different source (Seeds 1, 2)
**Source domain: Music notation.** A musical score has multiple layers: time signature (global), key signature (global, with per-bar accidentals), dynamics (per-passage, propagating until changed), tempo markings (per-passage). The pattern of "global signature with per-instance accidentals" is the envelope-with-selective-override pattern under a different name. Naming candidates from music:
- `key-signature axis` (global; per-instance accidentals are sub-field overrides)
- `voicing axis` (the headline voicing; per-note exceptions are overrides)

#### Deliberately-different source (Seed 4 — defaults)
**Source domain: car insurance pricing tiers.** Insurance has: base policy (the headline) + optional riders (overrides) + auto-calculated risk factors (auto-detected from input). The pattern of "base + riders + auto-factors" parallels Comprehenslate's "8 axes + overrides + source-detection." Insurance pricing also has CONSERVATIVE-DEFAULT defaults (the cheapest policy assumes the worst risks). This validates the conservative-bias-defaults principle as a cross-domain pattern.

#### Deliberately-different source (Seeds 1, 2, 3)
**Source domain: Unix-style configuration (env vars + dotfiles).** `.env.example` is already in this domain. The pattern: flat key-value pairs with optional grouping by prefix. Naming follows ALL_CAPS_WITH_UNDERSCORES. Candidate names for axes if Unix style adopted:
- `READER_LEVEL` / `DOMAIN_EXPERTISE` / `SOURCE_CULTURE` / `PURPOSE` / `FIDELITY` / `FORM_PRESERVATION` / `SCAFFOLDING` / `ANALYSIS_DEPTH`

#### Deliberately-different source (Seed 5 — preset bundles)
**Source domain: video-editing software presets (color grading LUTs).** A LUT is a named bundle of color-grading parameters; the user picks one and can then nudge individual sliders. This is exactly the proposed CASE-FRAME PRESET pattern from Absence Recognition. Naming: presets / LUTs / templates / case-frames / scenarios.

---

### Generator 4: Extrapolation

#### Generic variation (1-year horizon)
In 1 year, Comprehenslate may have **3-5 target languages** instead of just English. Axis CONCEPTS need to stay stable; LEVEL DEFINITIONS will vary per-language. Extrapolation predicts: the inquiry's commitment to language-agnosticism at concept level is correct. No structural change needed at axis layer; level-enumeration inquiry (next inquiry) needs to handle per-language level definitions.

#### Focused variation (5-year horizon)
In 5 years, LLMs will likely **auto-detect more source properties** (genre, era, register profile, source culture). The SOURCE-DESCRIPTION layer expands; some axes that currently exist as user-facing might absorb into source-detection. Candidates:
- A3 Source-Culture Proximity might shift from "user declares reader's source-culture-proximity" to "LLM detects mismatch between source culture and detected reader profile from a reader description." User axis count may drop.
- A6 Form-Preservation Strength might auto-tune to source's form-density (poetic source → auto-default to higher form-preservation).

Implication for THIS inquiry: the 8-axis count is a current-snapshot, not permanent. Build to accommodate axes graduating to auto-detection over time.

#### Contrarian variation (10-year horizon)
In 10 years, the configuration interface itself may be **entirely replaced by natural-language specification**. The user says "translate this for my mother-in-law to read on a beach" or "translate this for a doctoral dissertation footnote"; the LLM extracts axis values from the spec. No user-visible axes at all. The 8 axes become INTERNAL STATE, not user interface.

Implication: the axis NAMES become less critical (only the LLM reads them); the axis CONCEPTS become MORE critical (they must support LLM-extraction from free-form user descriptions). This favors short, semantically-clear axis names over user-facing-pretty names.

---

### Framer 1: Lens Shifting

#### Generic variation
Evaluate axis names under condition "**user is a developer building the system**." Vocabulary check: words like `axis`, `level`, `enum`, `Optional[]` are natural. ✓ Current names pass.

#### Focused variation
Evaluate axis names under condition "**user is a non-developer translator**." Vocabulary check: `axis`, `level`, `pydantic` are alien; `register`, `fidelity`, `purpose`, `scaffolding` are translator-natural; `Form-Preservation Strength` is awkward. Implication: shorter / translator-natural names work better:
- A6 `Form-Preservation Strength` → `Form Preservation` (drop "Strength")
- A1 `Reader Competence Level (RCL)` → `Reader Level` or `Reader Profile`
- A2 `Domain Expertise` → keep
- A3 `Source-Culture Proximity` → `Source Culture` (drop "Proximity")
- A4 `Purpose / Use-case` → `Purpose`
- A5 `Source-Fidelity Stance` → `Fidelity` or `Source Fidelity`
- A7 `Scaffolding Density` → `Scaffolding`
- A8 `Analysis Depth` → keep

#### Contrarian variation
Evaluate axis names under condition "**user is an LLM agent self-configuring**." LLMs prefer semantically-loaded short noun-phrases that pair well with JSON schema descriptions. Implication: names should be 1-2 words; schema-key names should be snake_case; the verbose "Stance" / "Strength" / "Density" suffixes add length without semantic gain. Current sensemaking names are fine if streamlined.

#### Lens-shifting summary
Three lenses point to overlapping cleanup: drop redundant suffixes ("Stance," "Strength," "Density," "Proximity," "Level"). The developer lens accepts current names; the translator and LLM lenses prefer the streamlined versions. Mid-point: streamline names for clarity AND keep developer-natural schema keys.

---

### Framer 2: Constraint Manipulation

#### ADD direction — generic
**Add constraint: "Every axis name ≤ 3 words."** Drives toward:
- A1: `Reader Level` (2)
- A2: `Domain Expertise` (2)
- A3: `Source Culture` (2)
- A4: `Purpose` (1)
- A5: `Source Fidelity` (2)
- A6: `Form Preservation` (2)
- A7: `Scaffolding Density` (2) or just `Scaffolding` (1)
- A8: `Analysis Depth` (2)

Constraint exposes that current names have variable verbosity (3-word `Reader Competence Level` next to 1-word `Scaffolding`).

#### ADD direction — focused
**Add constraint: "Every axis name must work in 3 target languages (English, Russian, Japanese)."** This is the language-agnosticism stress test concretized. Most names translate cleanly:
- `Purpose` → пурпус (cyrillic transliterates) — fine as a config key
- `Fidelity` → точность (Russian native) — works as a translated KEY but the CONCEPT is universal
- `Form Preservation` → сохранение формы (Russian) — works

The constraint surfaces no failures; current naming is universal at the concept level. PASSES the test.

#### ADD direction — contrarian
**Add constraint: "Every axis must be expressible as a yes/no question the user is asked."** This forces a UX where axes become a wizard:
- A1: "Is your reader a fluent English speaker?" — but this loses the 5-level granularity
- A4: "Is your purpose scholarly?" — loses the categorical breadth
- A6: "Should rhythm and structure be preserved?" — works as yes/no but loses Tier gradation

The constraint forces axes into yes/no, which loses information. Implication: axes are NOT yes/no questions; they ARE multi-level. The current ordinal/categorical pattern is correct.

#### REMOVE direction — generic
**Remove constraint: "8 axes."** What's possible?
- Collapse Strategy family (A5+A6+A7) into ONE `Strategy` envelope axis with sub-fields. Total = 6 axes (A1, A2, A3, A4, Strategy-envelope, A8). Trades fewer axes for more sub-fields per axis.
- Collapse Reader family (A1+A2+A3) into ONE `Reader Profile` envelope axis. Total = 6 axes (Reader-envelope, A4, A5, A6, A7, A8). Also viable.
- Aggressive collapse: combine both → 4 axes (Reader-envelope, Purpose, Strategy-envelope, Depth). This is the FAMILY-AS-AXIS reduction.

The 4-axis reduction maps 1:1 to the 4 families. Tradeoff: each family-axis becomes an envelope axis with 3+ sub-fields, RCL's sub-fields go inside Reader-envelope's sub-fields (nested envelope). Schema gets complex but UX simplifies.

#### REMOVE direction — focused
**Remove constraint: "language-agnostic."** What if axes are allowed to be language-specific? Then RCL.idiom-recognition can have ENGLISH-rooted level definitions ("kick the bucket"-style examples). This works for an English-target-only system, but multilingual deployments lose. The constraint was correctly committed; removal is not viable.

#### REMOVE direction — contrarian
**Remove constraint: "axes are ordinal/categorical with enum levels."** What if axes are FREE-TEXT user descriptions instead? E.g., A1 RCL becomes `reader_description: str = "ESL graduate student with rusty academic vocabulary."` The LLM reads the description and decides. This is the Extrapolation 10-year-horizon scenario. ACTIONABLE NOW as a "free-form override" field that supplements (not replaces) the enum axes.

---

### Framer 3: Inversion (with depth-iteration)

#### Level 1 — Component inversion
**"Axes are user-facing"** → **"Axes are LLM-facing."** A workaround: keep the 8 axes but write descriptions for the LLM, not the user. UI surfaces preset bundles; the LLM internally maps to the 8 axes.

#### Level 2 — System inversion
**"User CHOOSES axis values"** → **"User DESCRIBES the situation; system derives axis values."** This is a different interface paradigm — config-by-selection vs config-by-description. Both can coexist (description-first with axis-override fallback). System-level statement: the CONFIGURATION PARADIGM changes from "fill out a form" to "tell me what you need."

#### Level 3 — Root-cause inversion
**"Configuration is selection from a fixed schema"** → **"Configuration is dialogue."** A back-and-forth where the LLM asks clarifying questions until it has enough to make consistent choices. The 8 axes become internal scoring dimensions, not user interface. Root level: configuration IS NOT static schema selection; it's an interactive dialogue with the LLM as configuration partner.

#### Multi-axis system-level check
- **Existence-axis inversion**: "axes have count = 8" → "axes have count = 0; only Purpose remains; all other axes derived from Purpose + auto-detected source properties." This is a different system-level statement reached through the existence-axis. Could the count be ZERO of all-but-one? Test: if only Purpose is user-facing, can other axes be derived from `{Purpose, source-detection, conservative-bias defaults}`? Mostly yes — except Source-Culture Proximity (user-side identity) which doesn't derive from Purpose. So count=1 fails; count=2 (Purpose + Reader-Profile) might work. This is an alternative system-level claim.

- **Identity-axis inversion**: "axes are config dimensions" → "axes are SPEC OF SUB-MODELS." Each axis is a contract spec: "this is what we promise about how the translator handles this dimension." Configuration becomes API specification.

Three system-level statements compete:
1. Configuration is dialogue (depth-3 from primary)
2. Configuration is bundle selection at count=1-2 (existence-axis)
3. Configuration is sub-model API specification (identity-axis)

Each has merit; choosing among them is a critique-stage decision, not innovation.

---

### Mechanism map summary

| Mechanism | Variations applied | Seeds touched |
|---|---|---|
| Lens Shifting (Framer) | 3 (developer / translator / LLM lenses) | S1, S2, S3 |
| Combination (Generator) | 3 (bi-vocab / CEFR×Tier / Purpose×non-axis) | S1, S2, S5 |
| Inversion (Framer) | 3 (component / system / root) + 2 (multi-axis) | S1, S2, S5 |
| Constraint Manipulation (Framer) | 6 (3 ADD + 3 REMOVE) | S2, S3, S4, S5 |
| Absence Recognition (Generator) | 4 (2 patch + 2 redesign incl. bidirectional) | S1, S2, S3, S4 |
| Domain Transfer (Generator) | 6 (Halliday native; Skopos native; music; insurance; Unix; LUT) | S1, S2, S3, S4, S5 |
| Extrapolation (Generator) | 3 (1-year / 5-year / 10-year) | S5, S1 |

**Coverage:** Generators applied: 4/4. Framers applied: 3/3. Full coverage achieved.

**Convergence signals:**
- **Convergence 1**: streamlining axis names (drop "Stance," "Strength," "Density," "Proximity," "Level" suffixes) — pointed at by Lens Shifting (3 variations), Constraint Manipulation ADD (3-word constraint), Extrapolation contrarian (LLM-extraction friendliness). **3+ mechanisms converge — HIGH confidence.**
- **Convergence 2**: case-frame preset layer above the 8 axes — pointed at by Absence Recognition redesign-level, Domain Transfer (LUT video-editing source), Inversion Level 2 (user-describes-situation). **3+ mechanisms converge — HIGH confidence.**
- **Convergence 3**: A4 Purpose stays categorical (not ordinal) — pointed at by Domain Transfer (Skopos text-typology), Combination contrarian (Purpose-as-bundle-selector), Inversion multi-axis existence-axis. **3+ mechanisms converge — HIGH confidence.**

---

## Inherited Frame Audit

### Seed-level central assumption

**"The answer is a SET OF AXES (ordinal/categorical config dimensions) as the user-facing configuration unit."**

This is inherited from the inquiry's framing (user's sketch) and sensemaking's SV6 commitment.

### Step (iii) — Challenge scan for seed-level

Does any candidate explicitly challenge "axes are the user-facing configuration unit"?
- **Inversion Level 2**: "user describes situation; system derives axes" — challenges the UX paradigm (axes still exist but become INTERNAL).
- **Inversion Level 3**: "configuration is dialogue" — challenges that configuration is static-schema-selection at all.
- **Absence Recognition redesign-level**: "the framework lacks a case-frame preset layer between user and axes" — challenges axes-as-primary-UI.
- **Extrapolation contrarian (10-year)**: "natural-language spec replaces axes entirely" — challenges axes as a long-term interface.
- **Constraint Manipulation REMOVE (contrarian)**: "remove the ordinal/categorical constraint" — opens free-form description fields.
- **Domain Transfer LUT**: presets above axes.

Multiple candidates explicitly challenge the seed's central assumption. **Audit DOES NOT FIRE at seed level.**

### Piece-level commitments

| Piece | Commitment | Challenged by | Verdict |
|---|---|---|---|
| P1 (4-layer architecture) | "4 layers" | Constraint Manipulation REMOVE (collapse to fewer); Inversion multi-axis (existence-axis 0-axis case) | Challenged ✓ |
| P2 (8 axes) | "8 axes" | Constraint Manipulation REMOVE (collapse to 4 family-axes / 6 mixed-collapse / 2 minimal); Extrapolation 5-year (axes drop as auto-detection grows) | Challenged ✓ |
| P3 (envelope pattern) | "Envelope pattern as RCL's structure" | Domain Transfer (music-notation key-signature; LUT preset); Combination (preset-bundle alternative) | Challenged ✓ |
| P4 (4 families) | "Reader / Purpose / Strategy / Depth" | Domain Transfer (Halliday's Field / Tenor / Mode triad as alternative) | Challenged ✓ |
| P5 (POLICY layer separate) | "Axis-vs-policy distinction" | Constraint Manipulation REMOVE (collapse axis-vs-policy — but tested earlier and rejected) | Challenged ✓ |
| P6 (specific scope) | "Defer levels / pydantic / etc." | Lens Shifting (under what condition is the deferral wrong? — answer: if level definitions are needed to TEST orthogonality, deferring them is wrong — surfaces a real tension) | Challenged ✓ |

All piece-level commitments have at least one explicit challenge in the candidate set. **Audit DOES NOT FIRE at piece level.**

### Override status

No overrides needed. The audit is satisfied without firing. Proceed to Phase 3 Test.

---

## Phase 3 — Test

### 5-test cycle per surviving candidate cluster

I cluster the candidates into discrete proposals and run each through the 5-test cycle.

#### Candidate Cluster A — **Streamline axis names**

**Proposal:** Adopt streamlined names dropping redundant suffixes:
- A1: `Reader Level` (or `Reader Profile`)
- A2: `Domain Expertise`
- A3: `Source Culture`
- A4: `Purpose`
- A5: `Source Fidelity`
- A6: `Form Preservation`
- A7: `Scaffolding`
- A8: `Analysis Depth`

Schema-key counterparts: snake_case versions.

| Test | Verdict | Reasoning |
|---|---|---|
| Novelty | **PASS (moderate)** | Not radical novelty; refinement of sensemaking's working names. Genuinely new vs raw sketch in the user input. |
| Scrutiny survival | **PASS** | Strongest objection: "Reader Level is too vague; CEFR-style A1-C2 is more concrete." Reply: the AXIS name is the dimension's identity; the LEVEL ENUM (next inquiry) contains the concrete labels. Different layers. Survives. |
| Fertility | **PASS** | Opens cleaner schema design + better UX. Pairs naturally with developer / translator / LLM consumption. |
| Actionability | **PASS** | Direct action: replace verbose names in P2 spec. Immediately implementable in the deliverable. |
| Mechanism independence | **PASS** | Reached via Lens Shifting (translator + LLM lenses) AND Constraint Manipulation ADD (≤ 3 words) AND Extrapolation contrarian (LLM-friendly). Independent paths converge. |

**Disposition: ACTIONABLE.**

---

#### Candidate Cluster B — **Case-frame preset layer above the 8 axes**

**Proposal:** Add a **Layer 1A** above the 8 axes: a small catalog of named **case-frame presets** ("scenarios") with all 8 axis values pre-populated, expressed in user-natural language. The 8 axes remain at Layer 1B, individually overridable from the chosen preset.

Example presets (sketched only; actual catalog out-of-scope for this inquiry):
- `casual-english-reader` — RCL=conversational, Source-Culture=outsider, Scaffolding=rich, Fidelity=balanced, etc.
- `scholarly-english-reader` — RCL=advanced, Domain=specialist, Scaffolding=scholarly, Analysis-Depth=scholarly, etc.
- `language-learning-english-reader` — RCL=daily, Scaffolding=rich, Form-Preservation=light, etc.
- `devotional-source-native-reader` — RCL=native, Source-Culture=source-native, Scaffolding=minimal, etc.

| Test | Verdict | Reasoning |
|---|---|---|
| Novelty | **PASS** | The case-frame preset layer is structurally new vs the 8-axis-only sketch. The `.env.example` has partial preset values but not as a separate addressable layer. |
| Scrutiny survival | **PASS** | Strongest objection: "Presets violate orthogonality — they bundle axis values that may not always co-occur." Reply: presets are a UX SHORTCUT, not a replacement for axis orthogonality; the user can ALWAYS override any axis individually. Orthogonality is preserved at the axis layer; presets are at a higher layer. Survives. |
| Fertility | **PASS HIGH** | Opens a major UX direction: presets become the primary user interface; axes are for power users / edge cases. Also enables A4 Purpose to drive default-derivation for OTHER axes through the preset mechanism (resolving frontier D2 partially). |
| Actionability | **PARTIAL** | Direct action requires defining the preset catalog, which is OUT OF SCOPE for this inquiry (deferred per C7). But the LAYER ITSELF can be acknowledged in P1 (architecture) as Layer 1A. |
| Mechanism independence | **PASS** | Reached via Absence Recognition (redesign-level), Domain Transfer (LUT video-editing), Inversion Level 2 (user-describes-situation). Three independent mechanisms converge. |

**Disposition: ACTIONABLE at architectural level; DEFERRED for catalog definition.** Recommend: P1's 4-layer architecture upgrades to **5 layers** — adding **Layer 1A: case-frame presets** above the existing Layer 1B (user-facing axes). The preset catalog itself is deferred to a future inquiry.

**Re-test trigger note:** This proposal's content implies that **P1 architecture might need to change from 4 to 5 layers**. The existing sensemaking SV6's 4-layer commitment should be re-tested before final assembly. (See "RE-TEST TRIGGERS for re-assembly" below.)

---

#### Candidate Cluster C — **Envelope pattern naming alternatives**

**Proposal candidates for the pattern name (D6 resolution):**
1. `envelope-with-selective-override` (sensemaking's provisional)
2. `headline-with-sub-field-overrides`
3. `bundled-axis`
4. `compound-axis`
5. `composite-axis`
6. `aggregate-axis`
7. `parent-child-axis`
8. `multi-faceted-axis`
9. `key-signature axis` (music-notation domain transfer)
10. `tiered-headline axis`
11. `nested axis`

| Test | Verdict | Reasoning |
|---|---|---|
| Novelty | **N/A (selection problem, not novelty problem)** | All candidate names exist; this is choice among options. |
| Scrutiny survival | Per-candidate: `composite-axis` survives best — short, semantically clear (composite = made of parts), schema-natural; doesn't import unfamiliar domain (unlike music's "key-signature"); doesn't suggest hierarchy (unlike "parent-child"). |
| Fertility | `composite-axis` opens: future axes named "composite" trigger the envelope semantics. Good schema-vocabulary fertility. |
| Actionability | All candidates immediately actionable; this is critique's choice. |
| Mechanism independence | `composite-axis` reached via Combination (bi-vocab) + Constraint Manipulation ADD (≤ 3 words) + Lens Shifting (developer + LLM lenses agree). |

**Disposition: ACTIONABLE — recommend `composite-axis` (or `compound-axis` as runner-up) as the final name; critique selects.**

The full candidate list is preserved for critique-stage selection. The recommended candidate has the strongest mechanism independence convergence.

---

#### Candidate Cluster D — **Family naming alternatives**

**Proposal candidates for the 4 families:**
1. `Reader / Purpose / Strategy / Depth` (sensemaking's working set)
2. `About-the-Reader / About-the-Purpose / About-the-Method / About-the-Surfaced` (descriptive)
3. `Audience / Use / Approach / Layer` (single-word)
4. `Field / Tenor / Mode / Layer` (Halliday triad + Depth)

| Test | Verdict | Reasoning |
|---|---|---|
| Novelty | All candidates moderately novel vs the user's implicit family idea. |
| Scrutiny survival | Halliday's `Field / Tenor / Mode` doesn't cleanly fit — Field is text-content, but Comprehenslate's families are user-axis groupings, not source-content properties. **Halliday fails as family names.** The working `Reader / Purpose / Strategy / Depth` survives. |
| Fertility | `Reader / Purpose / Strategy / Depth` fertile for documentation; meta-grouping is navigational only, so simplicity wins. |
| Actionability | Working names immediately actionable. |
| Mechanism independence | The working set is reached via direct sensemaking convergence; alternatives challenge but don't beat it. |

**Disposition: ACTIONABLE — keep `Reader / Purpose / Strategy / Depth`.** The Halliday alternative is rejected as semantically misaligned with the actual axis groupings.

---

#### Candidate Cluster E — **A4 Purpose pattern: categorical**

**Proposal:** A4 Purpose remains **categorical** (not ordinal), with categorical-typed enum levels.

| Test | Verdict | Reasoning |
|---|---|---|
| Novelty | Confirms sensemaking SV6; not novel itself but settles the pattern. |
| Scrutiny survival | Strongest objection: "Purpose categories have an implicit ordering — casual is less than scholarly." Reply: ordering depends on what AXIS you'd be ranking on (depth? formality? rigor?). The categories represent QUALITATIVELY DIFFERENT USES, not points on a single dimension. Skopos's text-typology supports this. Survives. |
| Fertility | Categorical opens: Purpose can drive distinct DEFAULT PROFILES for other axes (each Purpose category → different default values). |
| Actionability | Direct action: P2.4 pattern association = categorical. |
| Mechanism independence | Reached via Domain Transfer (Skopos text-typology) + Combination (Purpose-as-bundle-selector) + Inversion multi-axis (existence-axis tested 0/1/2 alternatives). |

**Disposition: ACTIONABLE — A4 is categorical.**

---

#### Candidate Cluster F — **Default-bearing principle alternatives**

**Proposal candidates for the default-bearing principle:**
1. **Conservative-bias** (sensemaking's committed: more preservation, scaffolding, depth) — user dials DOWN
2. **Typical-use bias** (defaults match the typical user; calibration-dependent) — fits mature stage
3. **Minimal-defaults** (no defaults; user MUST set everything) — high specification burden
4. **Preset-driven** (defaults flow from a chosen preset / Purpose category)
5. **Hybrid: conservative-bias headline + preset-driven derivation** (when preset chosen, preset overrides conservative-bias; otherwise conservative-bias holds)

| Test | Verdict | Reasoning |
|---|---|---|
| Novelty | Candidates 4, 5 are novel beyond sensemaking; 1, 2, 3 are documented options. |
| Scrutiny survival | Candidate 5 (hybrid) survives strongest. Conservative-bias alone leaves no smart-default mechanism when user picks Purpose=scholarly; preset-driven alone leaves no fallback when no preset matches. Hybrid covers both. |
| Fertility | Candidate 5 opens: composable default-derivation, where multiple defaults compose by precedence (preset > Purpose > conservative-bias). |
| Actionability | Candidate 5 actionable as principle-statement; implementation deferred. |
| Mechanism independence | Reached via Combination (case-frame presets + conservative-bias) + Domain Transfer (insurance pricing's base + riders + auto-factors). |

**Disposition: ACTIONABLE — upgrade to hybrid principle.** The committed conservative-bias is preserved as the FALLBACK; preset-driven and Purpose-driven defaults override when applicable. This resolves frontier D2 partially and pairs naturally with Cluster B's case-frame preset layer.

---

### Axis coverage check

Axes the candidate set varies along:
- **Naming axis** — covered (Cluster A axis names; Cluster C pattern name; Cluster D family names)
- **Architectural axis** — covered (Cluster B adds Layer 1A; Cluster F upgrades default-principle)
- **Interface paradigm axis** — covered (axes-as-form vs description-vs-presets vs dialogue)
- **Vocabulary axis** — covered (developer / translator / LLM lenses)
- **Cardinality / pattern axis** — covered (Cluster E A4 categorical confirmed; Constraint Manipulation REMOVE explored 4-axis vs 8-axis collapse)
- **Default-derivation axis** — covered (Cluster F hybrid principle)

The candidate set varies along multiple orthogonal axes. **PASS.**

### Per-row mechanism-trace

Each of the 5 generation points (S1–S5) has at least one mechanism-trace:
- S1 (envelope pattern naming): Combination + Domain Transfer + Constraint Manipulation ADD → **Cluster C** ✓
- S2 (per-axis naming): Lens Shifting + Constraint Manipulation ADD + Extrapolation contrarian → **Cluster A** ✓
- S3 (family naming): Domain Transfer (Halliday) + Combination → **Cluster D** ✓
- S4 (default-bearing principle): Combination + Domain Transfer (insurance) → **Cluster F** ✓
- S5 (A4 Purpose pattern): Domain Transfer (Skopos) + Inversion multi-axis → **Cluster E** ✓

Plus emergent **Cluster B** (case-frame preset layer) — not a direct seed but emerges from multiple mechanisms; this is the **assembly-check emergent candidate**.

All 5 generation-point seeds have mechanism-trace. **PASS.**

### Mechanism Independence — Shared-input detection

Convergences identified:
1. **Streamlined axis names**: Lens Shifting (translator + LLM) + Constraint Manipulation ADD (≤ 3 words) + Extrapolation contrarian — three mechanisms converge.
   - Shared input check: all three operate on the inherited frame "axis names should be concise and semantically clear." This is partially shared upstream (sensemaking didn't commit to verbosity).
   - Independent grounding: Lens Shifting's translator lens is independent (drawn from user-side empathy); Constraint Manipulation's ≤3-word rule is design-side; Extrapolation is future-state. Three different groundings.
   - **Convergence is INDEPENDENT, not spurious.** HIGH confidence.

2. **Case-frame preset layer**: Absence Recognition redesign-level + Domain Transfer (LUT) + Inversion Level 2 — three mechanisms.
   - Shared input check: all three notice the gap between user mental model ("a scenario I want translated") and the axis interface. This shared NOTICING is the seed of the candidate.
   - But: Absence Recognition reads it as a missing structural layer; Domain Transfer reads it as a cross-domain pattern; Inversion reads it as a different UI paradigm. Three different VIEWS of the same insight.
   - **Convergence is INDEPENDENT.** HIGH confidence.

3. **A4 Purpose categorical**: Domain Transfer (Skopos) + Combination (Purpose-as-bundle-selector) + Inversion multi-axis — three mechanisms.
   - Shared input check: all three respect Skopos's text-typology (which is in the project's surfaced theoretical anchors).
   - Could the convergence be spurious from shared Skopos input? Test by inverting: "what if Skopos's typology is wrong here?" If wrong, Purpose might be ordinal (casual < general < deep). But ordinal Purpose fails the scholarly-wanting-easy-read counter-example tested in sensemaking. So Skopos is correctly applied. **Convergence is INDEPENDENT.**

No spurious convergence detected. **PASS.**

---

## Assembly Check (emergent candidates from combinations)

Examining the surviving candidates jointly:

### Emergent assembly E1 — **Streamlined names + 5-layer architecture (with case-frame presets) + hybrid default-principle**

**Combination of clusters A + B + F.** Three independently-derived candidates assemble into one coherent framework upgrade:
- Layer 1A (NEW): case-frame presets — named scenarios, primary UX
- Layer 1B (existing): 8 axes with streamlined names — power-user / edge-case interface
- Default principle: hybrid (preset → Purpose-driven → conservative-bias) — composable defaults

The assembly is more valuable than any single piece — it's a complete UX-and-architecture upgrade vs sensemaking SV6.

**Test the assembly:**
- Coherence: ✓ (the layers compose cleanly; preset selection populates axis defaults; axis overrides still work)
- Backwards-compatible with sensemaking SV6: ✓ (the 8 axes remain; preset layer is additive; default principle extends conservative-bias)
- New scope concerns: introduces preset catalog definition as a NEW deferred item (was implicit; now explicit)
- Architectural impact: P1 framework needs to upgrade from 4 layers to 5 layers

**Disposition: ACTIONABLE with RE-TEST TRIGGER.** The assembly is the recommended innovation output. But the upgrade from 4-layer to 5-layer architecture is a CONTENT CHANGE to a sensemaking commitment, requiring re-test in critique.

### Emergent assembly E2 — **Free-form description fallback as escape hatch**

**Combination of Constraint Manipulation REMOVE-contrarian + Extrapolation 10-year horizon.** A `notes` or `free_form_description` field at the configuration schema level, where users can describe special needs that don't map to axis values. The LLM consumes this alongside axis values. Resolves frontier D4 (escape hatch).

**Disposition: ACTIONABLE for inclusion as P6's escape-hatch design recommendation.** Implementation deferred.

---

## RE-TEST TRIGGERS for re-assembly

Outputs whose content has implications for already-committed claims in sensemaking SV6:

1. **Emergent assembly E1 upgrades 4-layer to 5-layer architecture.** The sensemaking commitment of "4 layers" needs re-test. Affected claim: SV6 LAYER 1 USER-FACING AXES = single layer. Re-test: should there be a sub-layer (Layer 1A presets, Layer 1B axes)? Verdict: **proposed re-test in critique stage.**

2. **Cluster F upgrades default-bearing principle from "conservative-bias" to "hybrid (preset → Purpose → conservative-bias)."** Affected claim: sensemaking's "conservative-bias at early calibration phase." Verdict: the hybrid is an EXTENSION not a replacement — re-test as compatibility check, not as overwrite.

3. **Cluster A streamlines axis names**, modifying P2 specifications. Affected claim: provisional axis names in SV6's table. Verdict: NAMING refinement was explicitly in scope (P3 handles D6 for the pattern; analogous refinement of axis names is in scope as critique selection). Not a problematic re-test.

---

## Output dispositions

| Cluster | Disposition | Notes |
|---|---|---|
| A — Streamlined axis names | **ACTIONABLE** | Apply to P2 in critique selection |
| B — Case-frame preset layer (Layer 1A) | **ACTIONABLE (architectural) + DEFERRED (catalog)** | Upgrade P1 to 5 layers; catalog defined later |
| C — Envelope pattern name (recommend `composite-axis`) | **ACTIONABLE** | Critique selects from candidate list |
| D — Family names (keep working set) | **ACTIONABLE** | Confirms sensemaking; rejects Halliday alternative |
| E — A4 Purpose categorical | **ACTIONABLE** | Confirms sensemaking; resolves S5 |
| F — Hybrid default principle | **ACTIONABLE** | Extends sensemaking's conservative-bias |
| Emergent E1 — 5-layer + streamlined + hybrid assembly | **ACTIONABLE + RE-TEST TRIGGER** | Architectural upgrade; critique re-tests sensemaking SV6 |
| Emergent E2 — Free-form description fallback | **ACTIONABLE — note as P6 deferred design** | Resolves frontier D4 |

### Research frontiers preserved

- **RF1**: The 8-axis count vs 4-axis-via-envelope-collapse — Constraint Manipulation REMOVE-generic surfaced a viable alternative (collapse Reader+Strategy families into envelope axes). Sensemaking justified 8 axes via ergonomic + orthogonality reasoning, but this alternative shows another route exists. RESEARCH FRONTIER: revisit after first round of real-user feedback; current commitment (8 axes) holds.
- **RF2**: The configuration-as-dialogue Level 3 inversion — a more radical interface paradigm than even Layer 1A presets. Not actionable now (too speculative), but preserved as a long-horizon design direction. RESEARCH FRONTIER.

---

## Mechanism Coverage Telemetry

- **Generators applied:** 4/4 (Combination, Absence Recognition, Domain Transfer, Extrapolation)
- **Framers applied:** 3/3 (Lens Shifting, Constraint Manipulation, Inversion)
- **Total candidate variations produced:** ~28 (across 7 mechanisms × ~3-4 variations each); clustered into 6 main + 2 emergent
- **Convergence:** YES — 3 distinct innovation directions, each reached via 3+ independent mechanisms
- **Survivors tested:** 8/8 (Clusters A-F + 2 emergent assemblies)
- **Inherited Frame Audit:** PASSED (seed-level and all piece-level commitments challenged)
- **Failure modes observed:** None
  - NOT Premature Evaluation (testing followed full generation)
  - NOT Single-Mechanism Trap (4G + 3F applied)
  - NOT Early Frame Lock (multiple mechanisms applied per generation point)
  - NOT Innovation Without Grounding (every candidate cluster tested via 5-test cycle)
  - NOT Mechanism Exhaustion (all 7 mechanisms produced viable output)
  - NOT Survival Bias (the most uncomfortable candidates — 5-layer architecture upgrade, free-form description fallback — explicitly tested and selected)

**Overall: PROCEED with RE-TEST TRIGGER for the architectural upgrade in Cluster B / Emergent E1.**

---

## Handoff to Critique

Critique should adjudicate:

1. **Cluster B / Emergent E1 — the 4-layer → 5-layer architectural upgrade.** This contradicts sensemaking SV6's 4-layer commitment. Critique should re-test whether case-frame presets are a NEW layer (Layer 1A) or a content-piece within Layer 1, or an out-of-scope add-on. RE-TEST TRIGGER fires.

2. **Cluster C — final name selection for the envelope pattern.** Recommended: `composite-axis`. Critique should select from the 11-candidate list (or refine).

3. **Cluster A — axis name refinements.** Apply streamlined names or keep verbose? Critique selects.

4. **Cluster F — hybrid default principle.** Critique validates the extension of "conservative-bias" to "hybrid (preset → Purpose → conservative-bias)."

5. **Cluster D — family names.** Critique confirms `Reader / Purpose / Strategy / Depth`.

6. **Cluster E — A4 Purpose categorical confirmation.** Critique confirms.

7. **Cluster RF1 — 8 vs 4 axis count.** Research frontier; critique acknowledges as long-horizon item, not active candidate.

8. **Cluster RF2 — configuration-as-dialogue paradigm.** Research frontier; not active.

9. **Emergent E2 — free-form description fallback.** Critique decides whether to recommend in P6.
