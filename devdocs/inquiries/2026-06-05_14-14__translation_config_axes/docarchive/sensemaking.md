# Sensemaking — translation_config_axes

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_14-14__translation_config_axes/_branch.md` (with surfacing output at `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-05_14-14__translation_config_axes/surfacing.md`)

---

## SV1 — Baseline Understanding

The inquiry asks: what axes should the Comprehenslate translation-configuration framework be built on? The user has sketched 5 axes (RCL with 5 sub-fields, Feature Activation, Source-Fidelity Stance, Domain Expertise, Source-Culture Proximity) and explicitly asks for a from-scratch re-design.

My initial impression: the sketched set has visible problems — "Feature Activation" is heterogeneous and not really an axis, RCL has 5 sub-fields that don't cleanly collapse to one ordinal scale, Purpose/use-case is conspicuously missing despite being the obvious Skopos-theory anchor. The answer probably reorganizes the sketched 5 into something like 6–8 cleaner axes.

What I don't yet know at SV1: whether some of the user's sketched axes should be policy rather than axes; how to handle the RCL sub-fields without explosion; how Purpose interacts with Source-Fidelity; whether Form-Preservation is its own axis or derivative.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1.** Each axis must be language-agnostic at the concept level (works for any target language: Russian, Japanese, Arabic, English).
- **C2.** Each axis must support 3–5 selectable levels covering the full spectrum.
- **C3.** Each axis must have a sensible default.
- **C4.** Axes must be orthogonal — independent; no double-counting.
- **C5.** Full coverage — every reasonable user-side configuration need expressible as a combination of axis values.
- **C6.** No derivative output-properties as axes (output altitude, output syntactic complexity, output idiom literalness — these emerge from `{source + axes + policy}`).
- **C7.** This inquiry stops at axis identity; level values are next inquiry.
- **C8.** This inquiry stops at axis identity; pydantic translation is later inquiry.
- **C9.** Strong user preference (memory H1): register alternation is **always-on policy**, not a user-axis. The user has been burned by ornate-English-as-faux-fidelity.
- **C10.** Strong user preference (memory H2): polysemy resolution is grammar-driven (local construction trumps surrounding metaphor), not user-config-driven.
- **C11.** Defaults must be such that a typical user overrides only 1–2 axes from defaults.

### Key Insights

- **KI1.** The existing `.env.example` mixes layers — only 3–4 of its 10 knobs are translation-content axes (AUDIENCE_LEVEL, HARMONY_ENABLED, DEPTH_PROFILE, possibly POETIC_MODE); the rest are pipeline/system flags. This inquiry can clean the layer-mixing.
- **KI2.** The user distinguishes **reader-side** axes from **translator-strategic** axes implicitly. This is a meta-organization — axes split into FAMILIES.
- **KI3.** "Feature Activation" (B2) is not an axis — it's a list of heterogeneous toggles (harmony toggle, footnote toggle, transliteration toggle). Toggles aren't ordinal/level-based; this violates C2.
- **KI4.** Skopos theory (Vermeer/Reiss) + Region G's 8 purpose categories point to Purpose/Use-case as the conspicuous missing axis. The user's sketch has it as implicit; Skopos says it should be explicit.
- **KI5.** The existing DEPTH_PROFILE (4 levels: surface/standard/deep/scholarly) is a candidate axis distinct from Purpose — it controls how much interpretive material surfaces, regardless of why the user reads.
- **KI6.** Source-side properties (genre, era, source register profile) should be auto-detected with user override — not part of the user-facing axes.
- **KI7.** "Scaffolding Density" (annotation/footnote/parenthetical-gloss intensity) is a strong candidate axis that absorbs much of B2's heterogeneous toggles.
- **KI8.** RCL's 5 sub-fields are NOT cleanly ordinal across one scale. A non-native ESL professor can be high-vocabulary, low-idiom. Collapsing RCL to one ordinal scale loses orthogonality.
- **KI9.** But splitting RCL into 5 separate axes violates C11 — 5 axes is too many cognitive slots for users to consider.
- **KI10.** Compromise pattern: RCL stays as ONE axis with a HEADLINE level; sub-fields are individually OVERRIDABLE when needed, defaulting from the headline. (Provisional name: "envelope axis with selective override.")
- **KI11.** Multi-meaning preservation has theoretical centrality (project's core insight) BUT memory H2 says polysemy is grammar-resolved. So multi-meaning is POLICY (always preserve when grammar permits), not user-axis. The user CHOICE is downstream: HOW the preserved meanings are RENDERED (inline / footnote / parenthetical) — that's a Scaffolding-Density sub-decision.
- **KI12.** Form-preservation can be an axis if harmony_layer.md's Tier 1–4 system (with Tier 3 PRESERVE-WHEN/SACRIFICE-WHEN clauses) is read as level-dependent.

### Structural Points

- **SP1.** Axes can be classified into FAMILIES by what they're "about":
  - **Reader family** — properties of the intended reader (competence, domain expertise, source-culture proximity)
  - **Purpose family** — what the translation is for (use-case)
  - **Strategy family** — how the translator handles source-target distance (fidelity stance, scaffolding density, form-preservation)
  - **Depth family** — how much interpretive material to surface (analysis depth)
- **SP2.** "Feature Activation" was a category error; the underlying axes are Form-Preservation (about structure) and Scaffolding (about explanatory aids).
- **SP3.** Cross-axis relationships: Reader-axis values INFORM defaults for Strategy-axis values; Purpose informs Depth + Strategy defaults. But each axis remains independently OVERRIDABLE.
- **SP4.** The existing F-region knobs map onto the new axis families: F3→Reader, F2→Strategy(Form), F6→Depth; F4/F5 are derivative; F1/F7/F8/F9/F10 are system-flag layer.
- **SP5.** B5 (Source-Culture Proximity) and B1e (cultural-reference-recognition) are orthogonal via the competence-vs-identity distinction (the four-corners test: well-read insider; poorly-read insider; well-read outsider; uninitiated outsider — all exist).
- **SP6.** Domain Expertise and RCL are orthogonal (Hebrew Bible scholar with low English fluency; general-educated reader with no Bible knowledge — both conceivable).
- **SP7.** The envelope-with-selective-override pattern implies a HEADLINE level + optional SUB-LEVEL OVERRIDES. Pydantic-implementable as nested model with optional override fields.

### Foundational Principles

- **FP1.** The configuration framework configures INPUT to the system (who/why/strategy), not OUTPUT properties. (User Constraint 7.)
- **FP2.** Independence-of-axes is a stronger constraint than feature-richness. If splitting a concept into two axes creates a pair where adjusting one always implies adjusting the other, the split was wrong.
- **FP3.** Defaults are first-class. Every axis has a default; the user only specifies what they care about.
- **FP4.** Language-agnostic means the axis CONCEPT is target-language-independent. Examples in axis definitions may be English-rooted; the axis itself must operationalize for any language.
- **FP5.** User-side need-space + Translator-strategic space + Depth-of-analysis space = full user-facing configuration space. Source-side properties are AUTO-DETECTED (with optional override); they belong to a different layer.
- **FP6.** When a translation principle is unanimously prescribed by project values (e.g., register alternation; polysemy preservation via grammar; no smoothing of difficult nuances), it does NOT become an axis — it becomes always-on POLICY. Axes are for legitimate user-choice points.

### Meaning-Nodes

- **MN1.** AXIS = a user-facing configuration dimension with ordinal-or-categorical levels covering a defined spectrum, having a sensible default and orthogonal to other axes.
- **MN2.** POLICY = an always-on system rule grounded in the project's stated values.
- **MN3.** DERIVATIVE PROPERTY = an output feature that emerges from `{source + axes + policy}`; NOT a user-facing axis.
- **MN4.** FAMILY = a meta-grouping of axes by what they're "about." Navigational, not a configuration unit.
- **MN5.** ENVELOPE AXIS WITH SELECTIVE OVERRIDE = one user-facing axis whose headline level propagates sensible defaults to sub-fields; each sub-field is optionally overridable. (Provisional name; refine in critique.)
- **MN6.** USER-SIDE vs TRANSLATOR-STRATEGIC distinction — about-the-reader vs about-the-strategy. Reader/Domain/Source-Culture are reader-side; Fidelity/Form-Preservation/Scaffolding are translator-strategic.

### Meta-Inspection after SV2 (H4 concept names, H5 motivating examples)

- **H4 — concept names.** "AXIS" matches user vocabulary. "POLICY" is loop-coined — flag for user-language-alignment refinement in critique. "FAMILY" is loop-coined navigational meta-term. "ENVELOPE AXIS WITH SELECTIVE OVERRIDE" is loop-coined; the CONCEPT is the user's (RCL with sub-fields) but the NAME is provisional — refine.
- **H5 — motivating examples.** The motivating examples are the user's sketched 5 axes (B1–B5). Specific-vs-pattern check: are these specific 5 the whole pattern? Region D (9 user-side need-dimensions) + Region G (8 purpose categories) surface needs the sketched 5 don't cover (Purpose is absent; Scaffolding is conflated). The sketched 5 are SPECIFIC examples of a wider pattern with more axes. Confidence: HIGH.

### SV2 — Anchor-Informed Understanding

The inquiry's task is to design a CONFIGURATION SCHEMA where each axis is a user-facing dimension with ordinal-or-categorical levels, defaulted, orthogonal, language-agnostic, covering the user-side need-space without including derivative output-properties or always-on policy rules. The user's sketched 5 axes are a strong starting point with known gaps and overlaps:

- **Gaps:** Purpose / use-case is missing despite Skopos centrality. Scaffolding Density is conflated into "Feature Activation."
- **Overlaps that turn out to be real distinctions:** RCL.cultural-reference-recognition vs Source-Culture Proximity hold up as orthogonal via the competence-vs-identity distinction.
- **Misnamed structures:** "Feature Activation" is not an axis — it's a list of heterogeneous toggles. The underlying axes are Form-Preservation Strength (ordinal, tied to Tier 1–4) and Scaffolding Density (ordinal, annotation intensity).
- **Axis vs Policy distinction:** Register alternation, polysemy resolution, multi-meaning preservation are USER-PREFERENCE-INFORMED POLICIES, not user-axes. Strong user values (memory H1, H2) bias these toward always-on. Multi-meaning RENDERING (how preserved meanings surface) is a Scaffolding-Density sub-decision.
- **Headline-with-override structure:** RCL has 5 sub-fields. Splitting into 5 separate axes violates ergonomics; collapsing to one ordinal scale violates orthogonality. Compromise: one HEADLINE level + optional sub-field overrides.

Shape of the answer: 4–8 axes organized into 3–4 families (Reader / Purpose / Strategy / Depth), each with a default and a 3–5-level scale; an adjacent POLICY layer for always-on rules; a separate SOURCE-DESCRIPTION layer for source-side properties.

---

## Phase 2 — Perspective Checking

### Technical / Logical perspective

Each axis maps to one pydantic field. For RCL, the headline-with-override pattern is implementable as a nested model where the headline is one Literal-typed field and sub-overrides are `Optional[Literal[...]]` fields. For "Feature Activation," the heterogeneous toggles must EITHER split into multiple axes OR collapse into one ordinal — a bundle of toggles is not an axis.

**New anchors:**
- **T-A1.** Each axis maps to one pydantic field (potentially nested for envelope pattern).
- **T-A2.** Heterogeneous toggle-bundles cannot be axes — they split or collapse.
- **T-A3.** Source-side properties (genre, era, register profile of source) can be auto-detected with user-override field: `source_register: Auto | Literal[...] = "auto"`.

### Human / User perspective

The user explicitly designs for ergonomics: "Defaults reduce specification burden. A typical audience-spec overrides only 1–2 axes from defaults; the rest stays default." Typical user inputs are 1–3 axis overrides. Adding axes adds concept-load even when each call uses only 2.

**New anchors:**
- **H-A1.** Total axis count should be 4–8. Below 4 = under-expressive; above 8 = concept-fatigue (8 is the upper bound).
- **H-A2.** Some axes should bundle (RCL with sub-fields) rather than expose every fine-grained choice.
- **H-A3.** The user prefers SETTING things by stating WHO/WHY rather than HOW. Reader-family and Purpose-family axes are user-natural. Strategy-family axes are translator-language but the user wants them exposed.

### Strategic / Long-term perspective

What changes break the config schema over years?
- New target languages: idiom recognition is universally meaningful, vocabulary breadth has CEFR analogs but level thresholds differ. AXIS stays universal; level-to-content mapping is per-language.
- New genres on the source side: handled if source-properties are auto-detected with override.
- New use-cases: Purpose axis is enum + escape hatch; extensible.

**New anchors:**
- **S-A1.** Level enums within axes will grow over time. Axis count stays stable.
- **S-A2.** Per-language level-to-content mapping is downstream. The inquiry's "language-agnostic" constraint applies to AXIS CONCEPTS, not level definitions.
- **S-A3.** Source-side properties belong in a separate config layer (source-description with auto-detection), cleanly separated from user-axis layer.

### Risk / Failure perspective

What's the worst-case bad axis set?
- Axes that overlap such that the translator gets contradictory signals (RCL.idiom-high + Scaffolding=rich = "reader gets idioms" + "explain everything").
- Coverage gap (user wants a religious-text-tuned recitation translation — is Purpose=performance covered?).
- Hidden translator-policy exposed as axis (preserving nazm tied to harmony — confuses users).
- Wrong defaults that the typical user must always override.
- Premature commitment to uniform level count (some axes need 3, others 5).
- Confusing AXIS with FAMILY at the schema level.

**New anchors:**
- **R-A1.** Axes must combine sensibly across their value space; contradictory combos should be detected and either error or resolve via sensible-defaults heuristic.
- **R-A2.** The schema needs an escape hatch (free-form notes field at the schema level) for use-cases not enumerated.
- **R-A3.** Different axes have different level counts (3, 4, or 5) — uniform-5 is not required.
- **R-A4.** Family is meta-grouping; the configuration unit is the AXIS, not the FAMILY.

### Resource / Feasibility perspective

Each axis becomes prompt context for the AI translator. Too-abstract levels (just "balanced") give the AI insufficient guidance. Too-concrete levels (footnotes/1000 words = 2.3) over-determine. Levels need prose descriptions that operationalize as prompt instructions.

**New anchors:**
- **F-A1.** Axis levels must be operationalizable as PROMPT INSTRUCTIONS for the AI translator — each level needs a prose description (next inquiry).
- **F-A2.** The config→runtime mapping is downstream.

### Ethical / Systemic perspective

Defaults encode assumptions about the typical reader. `AUDIENCE_LEVEL=native` privileges native-English readers; CEFR imports a European framework; `Source-Culture Proximity=outsider` defaults to non-insider reading. For a project translating Said Nursi (Turkish→English) the natural default might actually be late_learner; defaults depend on the user's typical use-case.

**New anchors:**
- **E-A1.** Defaults are not culturally neutral. The user must consciously decide the typical reader.
- **E-A2.** The framework should allow users in different cultural contexts to configure without fighting defaults.

### Definitional / Internal Consistency perspective

- An axis "Multi-Meaning Preservation" with level "commit to one meaning" contradicts the project principle (`notes.md`, `translation_principals.md`) that "all meanings derived from a text are valid and intended... preserving all valid meanings rather than forcing one. Choosing a meaning is up to the user not to the translation system." Offering an axis where the user opts OUT of preservation contradicts the project's identity. **Not a valid user-axis** — always-on policy.
- An axis "Register Handling" with level "lift plain to ornate" contradicts memory H1's stance. **Not a valid user-axis** — always-on policy.
- An axis "Form Preservation Strength" with levels off/light/standard/strong is consistent with harmony_layer.md's Tier 1–4 system (already level-based via PRESERVE-WHEN/SACRIFICE-WHEN clauses). **Valid axis.**

### Definitional / Frame-exit Completeness perspective

Gating predicate: (i) inquiry inherits terms from prior project artifacts? YES (audience-level, depth-profile, fidelity-stance from `.env.example` and user sketch). (ii) used at ≥2 distinct values within this inquiry's committed structures? YES.

Apply the 4 meta-categories:

1. **Existence Enumeration.** What does "AXIS" refer to project-wide?
   - LAYER axis: USER-FACING CONFIGURATION AXIS (this inquiry) vs INTERNAL POLICY AXIS (always-on rules) vs SYSTEM/PIPELINE FLAG (chunking, parallel, output format). The `.env.example` currently mixes layers.
   - TYPE axis: harmony_layer.md uses "tier" for preservation-strength levels — those are TIER LEVELS within one axis, not separate user-axes.
   - PHASE axis: configuration axes are set ONCE per job; not per-chunk or per-sentence.
   - AGENT axis: all axes are USER-CONFIGURED. Source-side detection is system-set with user override.

2. **Role Assessment.** Out-of-frame referents:
   - **POLICY layer** (register handling, polysemy resolution, escalation pattern preservation): role is to encode project values as always-on rules. **Verdict: re-locate, not exclude.** Explicitly name this layer to mark what's NOT a user-axis.
   - **SYSTEM-FLAG layer** (chunking, parallel, output format): role is pipeline behavior. **Verdict: re-locate.** Explicitly distinguish from user-axes.
   - **SOURCE-DESCRIPTION layer** (genre, era, source register): role is describing the source. **Verdict: separate layer with auto-detection + user override.**

3. **Verdict Rigor.** Clean-boundary verdict on POLICY layer: strongest counter is "axes inform policy (scaffolding informs whether to footnote), so policy is axis-dependent." Test: scaffolding density IS a user-axis (the user chooses how much help); the POLICY is "preserve register" (always-on). These are decisions at different points. Structural ground: USER-AXIS is what the user chooses; POLICY is what the system always does regardless of user choice. **Verdict survives — HIGH confidence.**

   Clean-boundary on SYSTEM-FLAG: strongest counter is "PARALLEL_MODE affects translation quality through context loss." Test: parallel mode affects HOW the AI processes the source, not WHAT translation policy applies. **Verdict survives — HIGH confidence.**

4. **Residual / Coverage Justification.** Is there a frame-exit concern the categories missed? Yes: where source-side properties live. Resolved in step 2 — SOURCE-DESCRIPTION is a separate adjacent layer. Recursion terminates.

### Phase / Calibration-State perspective

Does the inquiry involve rules dependent on calibration the project has?

YES — DEFAULTS for each axis are calibration-dependent. The project has no real users yet (the user is still building it). Two readings of "what should defaults be":
- **Default-by-typical-use:** match the typical user's likely needs. But we don't know the typical user yet.
- **Default-by-conservative-bias:** err toward preservation (more form, more scaffolding, more depth). User specifies when they want less.

For an early-stage project, **conservative-bias is appropriate**: the system errs on the side of preserving meaning + providing scaffolding; users dial DOWN when they want less. As calibration matures (user feedback), defaults can shift.

**New anchors:**
- **P-A1.** At early-stage calibration: defaults are conservative-bias (more preservation, more scaffolding, more depth). Re-calibrate after feedback.
- **P-A2.** The CHOICE of defaults is calibration-dependent; the AXIS SET itself is not.

### Meta-Inspection after SV3 (H1 candidate set, H2 frame, H3 question framing, H7 phase/calibration)

- **H1 — candidate set convergence.** Test pairwise collapse for the emerging 8 axes (RCL, Domain Expertise, Source-Culture Proximity, Purpose, Source-Fidelity Stance, Form-Preservation Strength, Scaffolding Density, Analysis Depth):
  - RCL × Domain Expertise: orthogonal (general fluency vs domain knowledge).
  - RCL × Source-Culture Proximity: orthogonal (general fluency vs cultural identity).
  - Domain × Source-Culture: subtle but orthogonal (a Hebrew Bible scholar with no modern Israeli cultural exposure; a Turkish-family-member with no Quranic-scholarship — both real).
  - Purpose × Source-Fidelity: user already addressed ("closely coupled but conceptually distinct"). Confirmed.
  - Scaffolding × Source-Fidelity: orthogonal (foreignized-and-richly-scaffolded; foreignized-and-bare — both real).
  - Form-Preservation × Source-Fidelity: orthogonal (domesticated translation can preserve form via target-language poetics; foreignized translation can ignore form). Real.
  - Analysis Depth × Purpose: subtle but orthogonal (a scholarly user might want surface depth for one task; a casual user might want deep analysis to understand a passage).

  None collapse.

- **H2 — frame scope** (already done via Frame-exit Completeness): frame is USER-FACING CONFIGURATION AXES; POLICY, SOURCE-DESCRIPTION, SYSTEM-FLAG are out of scope but acknowledged.

- **H3 — question framing pre-bias.** Does the user's wording ("axes") pre-bias the answer? Alternative would be "switches and templates" or "preset bundles." But the user's framing is structurally appropriate — ordinal axes with defaults and overrides match the configuration-system pattern they want to build. Sub-check: does "Reader Competence Level" pre-bias by anchoring to a Western concept (CEFR)? The user mentions CEFR-equivalent concepts but the axis name is generic. Not pre-biased.

- **H7 — phase / calibration state** (already done): defaults are calibration-dependent; axis set is not.

### SV3 — Multi-Perspective Understanding

After perspective checking, the model shifts in four ways:

1. **Layer separation becomes explicit.** Translation configuration spans FOUR layers:
   - USER-FACING AXIS LAYER (this inquiry's scope)
   - POLICY LAYER (out of scope but adjacent — always-on rules)
   - SOURCE-DESCRIPTION LAYER (out of scope but adjacent — auto-detected source properties)
   - SYSTEM-FLAG LAYER (out of scope, far — pipeline knobs)

2. **Axis FAMILIES emerge.** Reader / Purpose / Strategy / Depth — navigational meta-groupings, not configuration units.

3. **Envelope-axis-with-selective-override pattern.** RCL stays as one axis with sub-field defaults derived from a headline level; sub-fields individually overridable when needed.

4. **Concrete candidate axis set: 8 axes:**
   - **A1 (Reader).** RCL — envelope with sub-field overrides for vocabulary, syntactic processing, idiom recognition, inference, cultural-reference recognition. ~5 headline levels.
   - **A2 (Reader).** Domain Expertise. 3 levels.
   - **A3 (Reader).** Source-Culture Proximity. 3 levels.
   - **A4 (Purpose).** Purpose / Use-case. ~5 levels.
   - **A5 (Strategy).** Source-Fidelity Stance. 3 levels.
   - **A6 (Strategy).** Form-Preservation Strength. ~5 levels (ties to Tier 1–4).
   - **A7 (Strategy).** Scaffolding Density. ~5 levels.
   - **A8 (Depth).** Analysis Depth. 4 levels.

5. **NOT axes (always-on POLICY):** multi-meaning preservation; register alternation; polysemy-via-grammar; nazm-as-meaning at Form-Preservation ≥ light.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: RCL as 1 axis with sub-fields vs 5 separate axes vs 1 collapsed ordinal scale

**Strongest counter-interpretation:** Split into 5 separate axes — each sub-field is empirically independent (a non-native ESL professor: high vocabulary, low idiom). Treating them as one bundled axis with sub-field overrides creates illusion of unity where there is genuine orthogonality. The user should set each independently.

**Why the counter fails (structural grounds):** Two grounds:
1. **Ergonomics** (anchor H-A1, C11). If 5 separate RCL axes exist, a typical user reasons about 5 fields just to describe one reader-aspect. This pushes total axis count from 8 to 12 — beyond the ergonomic upper bound.
2. **Empirical distribution.** The 5 sub-fields are CORRELATED in 95% of real users. A general-educated late-learner is typically not high-vocabulary-low-idiom; the joint distribution is highly clustered. The 5-axis split creates a configuration space of 5^5 = 3125 cells where most cells are empirically empty.

The envelope-with-selective-override pattern (RCL.overall as headline + per-sub-field `Optional[Level]`) preserves orthogonality WHERE NEEDED (the rare professor case CAN be expressed) without forcing it on the typical case. Structurally: one axis with optional sub-axes nested inside.

**Confidence:** HIGH.

**Resolution:** RCL is ONE user-facing axis with a headline level. Sub-fields are accessible as OPTIONAL OVERRIDES.

**What is now fixed:** RCL counts as ONE axis. Sub-fields are second-class fields, defaulted from the headline.

**What is no longer allowed:** Treating each RCL sub-field as a separate axis with its own default. Collapsing RCL to one ordinal with no sub-field access.

**What now depends on this choice:** The pydantic schema (nested model). The default values for sub-fields (derived from headline). The total axis count (RCL = 1, not 5).

**What changed in the conceptual model:** Introduces the ENVELOPE AXIS WITH SELECTIVE OVERRIDE pattern as a first-class structural concept.

---

### Ambiguity 2: Is "Feature Activation" (B2) an axis, multiple axes, or derivative?

**Strongest counter-interpretation:** Keep "Feature Activation" as multiple separate axes — `harmony_strength`, `footnote_enabled`, `transliteration_enabled` — because each is a distinct user choice with different semantics. Bundling them into "Scaffolding Density" forces a single ordinal where the user actually wants independent toggles.

**Why the counter fails (structural grounds):** Two grounds:
1. **The harmony layer is genuinely level-based** (Tier 1–4 system with PRESERVE-WHEN/SACRIFICE-WHEN clauses — `harmony_layer.md`) — it's an ordinal axis (Form-Preservation Strength), NOT a Scaffolding decision. Form-preservation is about whether the translation preserves source structure (nazm, rhythm, parallelism); it's not about adding explanatory glosses.
2. **Footnote and transliteration toggles ARE about scaffolding** — adding explanatory material at the surface. These two TOGETHER are points on one ordinal axis: how much help to provide. "off / minimal / standard / rich / scholarly" gives a sensible 5-level scale.

So "Feature Activation" actually decomposes into TWO axes (Form-Preservation Strength + Scaffolding Density), each independently meaningful. The user's bundling was a category error — Form-Preservation is about structural preservation; Scaffolding is about surface explanation.

**Confidence:** HIGH — decomposition aligns with the project's own Tier 1–4 system and with the user's distinction between "feature activation" and "Source-Fidelity Stance."

**Resolution:** B2 "Feature Activation" splits into TWO axes: Form-Preservation Strength (Tier-based) and Scaffolding Density (annotation/gloss intensity).

**What is now fixed:** Two separate axes from one sketched axis. F2 (HARMONY_ENABLED) upgrades from binary to multi-level (Form-Preservation Strength).

**What is no longer allowed:** Bundling footnote/transliteration/harmony into one axis.

**What now depends:** The total axis count. The mapping from `.env.example` knobs to new axes.

**What changed:** Recognition that "feature activation" was a category error; the underlying axes are Form-Preservation (structure) and Scaffolding (explanation).

---

### Ambiguity 3: Is "Purpose / Use-case" an axis or implicit driver?

**Strongest counter-interpretation:** Purpose should NOT be an axis. It's a meta-frame the user holds in their head; it implicitly biases all other axis defaults. Making Purpose a separate field doubles cognitive load (user sets Purpose AND sets other axes) when the right interface is to let Purpose drive defaults silently.

**Why the counter fails (structural grounds):** Two grounds:
1. **Skopos theory** (Vermeer/Reiss) — purpose is the PRIMARY determinant of translation strategy; treating it implicitly violates the principle. Region G's 8 purpose categories show purpose drives many decisions independently.
2. **Orthogonality from other axes** — the user explicitly says "Purpose is closely coupled to Source-Fidelity but conceptually distinct." If Purpose ONLY drives defaults silently, the user cannot independently set Purpose=scholarly + Fidelity=domesticated (a scholar wanting an easy-read). Orthogonality between Purpose and other axes is a feature.

The counter argues for Purpose as preset bundles. But the framework can support both: Purpose is an axis AND can drive defaults for other axes when the user doesn't specify them.

**Confidence:** HIGH — Skopos + orthogonality test both demand Purpose be a separate axis.

**Resolution:** Purpose / Use-case is a separate axis.

**What is now fixed:** Purpose is an axis. Total axis count gains one.

**What is no longer allowed:** Treating Purpose as implicit-only.

**What now depends:** The default-derivation mechanism may use Purpose to inform other axes' defaults — the "axis with derived defaults" pattern.

**What changed:** Skopos becomes structurally present via the Purpose axis. The framework gains a default-derivation pattern where Purpose's value shifts other axes' defaults.

---

### Ambiguity 4: Source-Culture Proximity (B5) vs RCL.cultural-reference-recognition (B1e)

**Strongest counter-interpretation:** B5 and B1e ARE redundant — both about cultural references. Having both is double-counting; pick one.

**Why the counter fails (structural grounds):** Four-corners test. The user already articulated the distinction (competence-based vs identity-based); the structural test is whether the joint distribution can be populated at all four corners:
1. Source-native + high cultural-reference-recognition (well-read cultural insider — Hayrettin Karaman reading Risale-i Nur)
2. Source-native + low cultural-reference-recognition (poorly-read cultural insider — average Turkish reader unfamiliar with Islamic terminology)
3. Outsider + high cultural-reference-recognition (Western academic specialist — non-Muslim scholar of Islamic thought)
4. Outsider + low cultural-reference-recognition (uninitiated outsider — Western reader new to Islamic texts)

All four corners are real. The axes are orthogonal. The translator-AI's decisions differ between corners: for case 3, the system can use untranslated terminology (specialist knows `nefs`) but might still need to flag cultural context (case 3 lacks the lived intuition of a source-native).

**Confidence:** HIGH — orthogonality holds via four-corners.

**Resolution:** Keep both. Source-Culture Proximity is one axis; cultural-reference-recognition stays as RCL sub-field.

**What is now fixed:** B5 is an axis; B1e is a sub-field of RCL. Both survive.

**What is no longer allowed:** Merging the two.

**What now depends:** The translator-AI's decision logic distinguishes "does the reader know the term?" (B1e) from "does the reader have cultural intuition?" (B5).

**What changed:** Reinforces the competence-vs-identity distinction as a structural feature.

---

### Ambiguity 5: Is Multi-Meaning Preservation an axis or always-on policy?

**Strongest counter-interpretation:** Multi-meaning preservation should be an axis with levels (commit-one / preserve-primary-with-note / preserve-all) because users vary in tolerance for textual complexity. A casual reader wants a single English sentence; a scholarly reader wants all the meanings preserved with notes.

**Why the counter fails (structural grounds):** Two grounds:
1. **Project value** (`notes.md`, `translation_principals.md`): "all meanings derived from a text are valid and intended, as long as they don't violate the grammatical rules and foundational principles of the language. This is a direct theoretical foundation for Comprehenslate's approach of preserving all valid meanings rather than forcing one. Choosing a meaning is up to the user not to the translation system." Translating this as "user CAN set commit-to-one" means the user is explicitly opting OUT of the project's stated value. The project says "preservation is what we do"; offering an axis to opt out contradicts project identity.
2. **Grammar-driven resolution** (memory H2): "local construction trumps." Whether multiple meanings are activated is decided by the local construction — not by user preference. The user's choice is downstream: HOW preserved meanings are RENDERED (inline / footnote / parenthetical) — that's a Scaffolding-Density sub-decision.

**Confidence:** HIGH — both project-value and grammatical-construction arguments converge.

**Resolution:** Multi-Meaning PRESERVATION is always-on POLICY (not an axis). Multi-Meaning RENDERING (how preserved meanings surface) is handled by Scaffolding Density's levels (low scaffolding → primary meaning with minimal note; high scaffolding → multiple meanings inline or footnoted).

**What is now fixed:** Multi-meaning preservation is policy, not axis.

**What is no longer allowed:** A "Multi-Meaning Preservation" axis with a "commit-one" level.

**What now depends:** Scaffolding Density's level definitions must include treatment of polysemous words.

**What changed:** Introduces the AXIS-vs-POLICY distinction concretely: project values that are UNANIMOUSLY prescribed become POLICY; user-choice points become AXES.

---

### Ambiguity 6: Is Form-Preservation Strength an axis or derivative?

**Strongest counter-interpretation:** Form-Preservation is derivative of `{Purpose + Source-Fidelity}`. A scholarly+foreignized translation should maximize form preservation; a casual+domesticated should minimize it. The axis is redundant.

**Why the counter fails (structural grounds):** Counter-example: a casual reader (Purpose=casual) reading a poetic source might want HIGH form preservation (they want to feel the rhythm) even though they don't want scholarly fidelity. Conversely, a scholar studying meaning might want LOW form preservation (just give the semantic content; don't waste effort on form). Form preservation is orthogonal to Purpose AND to Fidelity.

Plus: `harmony_layer.md` explicitly architecturalizes form-preservation as level-based (Tier 1–4 with PRESERVE-WHEN/SACRIFICE-WHEN clauses); the existing F2 HARMONY_ENABLED is binary, but the underlying system supports gradation.

**Confidence:** HIGH — orthogonality holds; Tier system supports level structure.

**Resolution:** Form-Preservation Strength is a separate axis. Levels: off / Tier-1-only / Tier-1+2 / Tier-1+2+3-judged / Tier-1+2+3-always (5 levels mapping to the harmony_layer.md Tier system).

**What is now fixed:** Form-Preservation Strength is an axis. F2 HARMONY_ENABLED upgrades to multi-level.

**What is no longer allowed:** Treating Form-Preservation as derivative.

**What now depends:** Connection between this axis and the Tier 1–4 system in harmony_layer.md.

**What changed:** Form-Preservation explicit as third orthogonal Strategy-family axis alongside Fidelity and Scaffolding.

---

### Ambiguity 7: Is Analysis Depth (F6 DEPTH_PROFILE) the same axis as Purpose?

**Strongest counter-interpretation:** Analysis Depth and Purpose are the same axis under different names. surface/standard/deep/scholarly maps 1:1 to casual/general/scholarly purpose categories.

**Why the counter fails (structural grounds):** Counter-example: a scholar might want LOW analysis depth (pure translation, no interpretive commentary) for a particular use; a casual reader might want HIGH analysis depth (they want to understand WHY the source says what it does, even though they're reading casually). Purpose answers "what are you USING the translation for?" Depth answers "how much interpretive material accompanies the translation?" These are independent.

Plus: F6 already has 4 levels distinct from any Purpose enumeration; the user's existing config recognizes them as separate.

**Confidence:** HIGH — orthogonality holds; existing config recognizes separation.

**Resolution:** Analysis Depth is a separate axis.

**What is now fixed:** Analysis Depth is an axis with 4 levels.

**What is no longer allowed:** Collapsing Depth into Purpose.

**What now depends:** The total axis count.

**What changed:** Recognition that "how much interpretive material accompanies the translation" is independent of "why the reader is reading."

---

### Ambiguity 8: Total axis count — 8 axes too many?

**Strongest counter-interpretation:** 8 axes is fine because the user said "specify only what you care about." The user only sets 1–2 in practice; the count is irrelevant.

**Why the counter partially holds and partially fails:** The user did say defaults reduce burden. BUT: even with defaults, the user must KNOW what each axis IS to decide whether to override. 8 axes is 8 concepts to learn. Concept-load matters even when each call uses only 2.

Pairwise collapse re-test (after Ambiguities 1–7):
- **Source-Culture Proximity × Domain Expertise:** "general cultural insider/outsider" vs "specialist in topic." Distinct (a Muslim ≠ a Quranic scholar). Don't collapse.
- **Form-Preservation × Source-Fidelity:** Could they collapse into "Source-Faithfulness" (lexicon + form together)? Pros: simpler. Cons: a heavily-foreignized translation can ignore form (keep foreign words but translate prose-flat); a heavily-domesticated translation can preserve form (use target poetics mirroring source poetics). Real translation choices distinguish these. **Don't collapse.**
- **Analysis Depth × Scaffolding Density:** Scaffolding is explanatory aids AT TEXT SURFACE (footnotes, glosses, parentheticals). Analysis Depth is interpretive COMMENTARY in separate sections (before/after the translation). A rich Scaffolding at surface Analysis Depth = lots of footnotes, no separate analysis section. A minimal Scaffolding at scholarly Analysis Depth = clean translation followed by analysis chapter. **Don't collapse**, though they interact in defaults.

**Confidence:** MEDIUM — 8 axes is structurally justified but ergonomically near the upper bound. Per anchor H-A1, the upper bound is 8. Acceptable but at the limit. If future usage feedback shows confusion, axes might consolidate.

**Resolution:** Final count is 8 axes in 4 families.

**What is now fixed:** 8 axes in 4 families (Reader: RCL, Domain, Source-Culture; Purpose: Purpose; Strategy: Fidelity, Form, Scaffolding; Depth: Analysis Depth).

**What is no longer allowed:** Adding axes without strong justification; collapsing below orthogonality boundaries.

**What now depends:** Defaults must be strong; the typical user touches 1–2.

**What changed:** FAMILY meta-grouping formalized as navigational aid, not a configuration unit.

---

### Ambiguity 9: Language-agnosticism — are the proposed axes truly language-agnostic?

**Strongest counter-interpretation:** RCL.vocabulary-breadth is tied to CEFR (European framework). Russian, Japanese, Arabic don't map cleanly to CEFR. The axis concept may be universal but the levels depend on language.

**Why the counter partially fails:** The axis CONCEPT (passive vocabulary size) IS universal across human languages. Every language has high-frequency vs low-frequency vocabulary. The LEVEL DEFINITIONS (what counts as "advanced" vocabulary) ARE language-specific. But this inquiry only commits to the AXIS CONCEPT, not the level definitions. The constraint is "axes are language-agnostic at the CONCEPT level," not "level definitions are language-agnostic."

Similarly: idiom recognition exists in every language; syntactic complexity exists in every language; inference is universal cognition.

Other axes to scrutinize:
- Source-Culture Proximity: "source-native" is well-defined for any source-culture. "Outsider" is well-defined. Language/culture-agnostic in concept.
- Purpose: Skopos categories (casual/scholarly/devotional/pedagogical/performance) are universal use-cases.
- Source-Fidelity, Form-Preservation, Scaffolding, Analysis Depth: all universal concepts.

**Confidence:** HIGH — axis concepts are universal; level definitions are per-language and per-source-culture (next inquiry).

**Resolution:** The proposed axis SET is language-agnostic at the concept level. Level enums may use universal labels (very_basic, daily, conversational, advanced, native); empirical thresholds for what counts at each level are per-language.

**What is now fixed:** Language-agnosticism constraint satisfied at axis-concept level.

**What is no longer allowed:** Coupling an axis CONCEPT to a single language's framework (e.g., "CEFR axis" would fail).

**What now depends:** Level definitions (next inquiry) must operationalize per-target-language.

---

### Ambiguity 10: Source-side configuration — where does source description live?

**Strongest counter-interpretation:** Source-side properties (genre, era, source register profile, source-culture) should be part of the user-facing configuration. The user might want to override auto-detection. So source-side properties ARE axes.

**Why the counter partially holds:** Source-side properties ARE configurable — the user CAN override detection. But they're not USER-AXES in the same sense as the 8 axes above. The 8 axes describe THE READER AND THE STRATEGY; source-side properties describe THE SOURCE. The mental model differs: "tell me about the reader / what they want" (user-axes) vs "here's what the source is" (source-description).

**Confidence:** HIGH — source-description is a separate layer.

**Resolution:** Source-description is a separate config LAYER (auto-detected with optional user override), NOT part of the 8 user-facing axes.

**What is now fixed:** Source-description is a separate layer (out of this inquiry's scope but documented as adjacent).

**What is no longer allowed:** Including source-side properties in the 8-axis set.

**What now depends:** Future work defines the source-description schema separately. The pydantic dataclass for user-axes is one model; source-description is another.

---

### Load-bearing concept test (per Phase 3 refinement note)

Load-bearing concepts that emerged:

1. **ENVELOPE AXIS WITH SELECTIVE OVERRIDE** (MN5, KI10) — coined-term. Test: domain-terminology-vs-external-default + user-language alignment.
   - Counter: "Does the user use this term?" The user does NOT use this exact term. But the user describes the PATTERN implicitly (RCL with sub-fields). The CONCEPT is in the user's vocabulary; the NAME is loop-coined. Possible better names: "HEADLINE AXIS WITH SUB-FIELD OVERRIDES" / "BUNDLED AXIS" / "COMPOUND AXIS."
   - **Verdict:** concept valid, NAME PROVISIONAL — refine in critique. Marked low-confidence-naming.

2. **AXIS vs POLICY distinction** (MN1, MN2, FP6) — drawn fresh.
   - Counter: "Could these be the same under different names?" No — AXIS is user-choice; POLICY is always-on regardless of user choice. The distinction is operational and grounded in memory H1+H2.
   - **Verdict:** HIGH confidence. Real structural distinction.

3. **FAMILY (Reader/Purpose/Strategy/Depth)** (MN4, SP1) — meta-grouping coined-term.
   - Counter: "Are these real divisions or just convenient labels?" Test: Reader = properties of the READER; Purpose = WHY translation; Strategy = HOW the translator handles distance; Depth = HOW MUCH interpretive material. Four real divisions. Could Depth merge into Strategy? Could Purpose merge into Reader? Tested against orthogonality in Ambiguities 3, 7 — they DON'T collapse, but FAMILY is meta-organization, not orthogonality unit.
   - **Verdict:** Family is NAVIGATIONAL meta-grouping. Survives but is LOWER-WEIGHT than the axes themselves.

4. **SOURCE-DESCRIPTION LAYER as adjacent but separate** (Ambiguity 10) — newly drawn.
   - Counter: "Could source-description be axes too?" Tested in Ambiguity 10 — no, mental model differs.
   - **Verdict:** HIGH confidence, documented as out-of-scope-but-adjacent.

### Specific-vs-pattern recognition cue (per Phase 3 refinement note)

The motivating examples are the user's sketched 5 axes (B1–B5). Are these the WHOLE PATTERN or just specific cases?

Test: the user's 5 axes are a STARTING SAMPLE. The full pattern includes:
- Purpose (missing from sketch but central in Skopos + Region G)
- Form-Preservation Strength (lurking inside B2 — recovered via decomposition)
- Scaffolding Density (the legitimate axis-form of B2 — recovered via decomposition)
- Analysis Depth (existing in F6 but not in sketch — recovered via inheritance)

The sketch was 5 specific examples of a wider pattern with 8 axes. The broader pattern is NOT covered by the 5 sketched axes alone.

**Verdict:** HIGH confidence — the 8-axis answer represents the broader pattern, not just the sketched 5.

### SV4 — Clarified Understanding

The translation configuration framework has FOUR LAYERS:

1. **USER-FACING AXIS LAYER** (this inquiry's scope) — 8 axes in 4 families.
2. **POLICY LAYER** (out of scope, adjacent) — always-on rules grounded in project values.
3. **SOURCE-DESCRIPTION LAYER** (out of scope, adjacent) — auto-detected source properties with optional user override.
4. **SYSTEM-FLAG LAYER** (out of scope, far) — pipeline knobs.

The USER-FACING AXIS LAYER consists of 8 axes:

**Reader family:**
- **A1.** Reader Competence Level (RCL) — envelope axis with sub-field overrides.
- **A2.** Domain Expertise.
- **A3.** Source-Culture Proximity.

**Purpose family:**
- **A4.** Purpose / Use-case.

**Strategy family:**
- **A5.** Source-Fidelity Stance.
- **A6.** Form-Preservation Strength.
- **A7.** Scaffolding Density.

**Depth family:**
- **A8.** Analysis Depth.

What is NOT an axis (becomes POLICY):
- Multi-meaning preservation (always-on; rendering choice handled by A7 Scaffolding).
- Register alternation preservation (always-on per memory H1).
- Polysemy resolution via local construction (always-on per memory H2 + project principles).
- Nazm-as-meaning preservation (active when A6 ≥ light).

Patterns introduced:
- **Envelope axis with selective override** (name provisional)
- **Axis vs Policy distinction**
- **Family meta-grouping** (navigational only)
- **Conservative-bias defaults at early calibration phase**

---

## Phase 4 — Degrees-of-Freedom Reduction

### Variables now fixed

- **Total axis count: 8** (in 4 families). Not 5 (sketched), not 4–6 (initial guess), not 1 (collapsed CEFR-style), not 5+3+3+5+3+5+5+4 (split-RCL maximalist).
- **RCL is ONE axis with the envelope pattern.** Not 5 separate axes; not 1 collapsed ordinal scale.
- **Feature Activation is NOT an axis** — it decomposes into Form-Preservation Strength + Scaffolding Density.
- **Purpose IS an axis** — not implicit driver, not bundled into Fidelity.
- **Source-Culture Proximity and RCL.cultural-reference-recognition coexist** — orthogonal via competence-vs-identity.
- **Multi-meaning preservation is POLICY**, not axis. Multi-meaning RENDERING handled by Scaffolding Density.
- **Register alternation and polysemy-via-grammar are POLICY** — not axes.
- **Source-description is a separate layer** — not part of the 8 axes.
- **System/pipeline flags are out of scope** — F1, F7, F8, F9, F10 do not become axes.
- **The axis SET is language-agnostic at the concept level.** Level definitions are per-language (next inquiry).
- **Each axis has a default; defaults are conservative-bias at early calibration phase** (more preservation, more scaffolding, more depth — user dials down).

### Options eliminated

- "Just keep the user's sketched 5 axes" — eliminated; sketched set misses Purpose, conflates Form/Scaffolding, omits Analysis Depth.
- "Collapse RCL to single ordinal scale like AUDIENCE_LEVEL" — eliminated; loses sub-field orthogonality.
- "Split RCL into 5 separate axes" — eliminated; explodes axis count beyond ergonomic bound.
- "Make Multi-Meaning Preservation an axis" — eliminated; contradicts project values.
- "Make register-handling a user-axis" — eliminated; contradicts memory feedback H1.
- "Bundle Source-Culture Proximity into RCL" — eliminated; orthogonal.
- "Treat Feature Activation as one axis" — eliminated; heterogeneous, must decompose.
- "Collapse Analysis Depth into Purpose" — eliminated; orthogonal.
- "Collapse Form-Preservation into Source-Fidelity (Source-Faithfulness)" — eliminated; real translation choices distinguish lexicon-fidelity from form-preservation.

### Paths remaining viable

- The 8-axis structure with the envelope pattern for RCL.
- Per-axis level definitions (next inquiry; out of this scope).
- Per-axis default selection at conservative-bias for early calibration phase (per-axis specifics in next inquiry).
- The pydantic dataclass design (next-next inquiry).
- Source-description schema (separate, future inquiry).
- POLICY layer documentation (separate, future inquiry — which always-on rules exist).

### SV5 — Constrained Understanding

The configuration framework is now constrained to:

- **8 axes** in **4 families** (Reader / Purpose / Strategy / Depth).
- **One layer** (USER-FACING AXIS LAYER); three other layers exist (POLICY, SOURCE-DESCRIPTION, SYSTEM-FLAG) but are out of scope, with the first two adjacent.
- **Envelope pattern** for RCL specifically (headline + optional sub-field overrides).
- **Conservative-bias defaults** at early calibration phase; user feedback shifts defaults later.
- **Language-agnostic at axis-concept level**; level definitions are per-language (future inquiry).
- **Orthogonality verified** for every relevant pair via the four-corners test.
- **Coverage verified** against user-side need-space (Region D) and use-case categories (Region G).

Remaining work (out of this inquiry's scope; marked for downstream):
- Naming refinement for "envelope axis with selective override" pattern.
- Per-axis level enumeration with prose descriptions.
- Per-axis default selection.
- POLICY layer enumeration (which always-on rules exist, why each).
- SOURCE-DESCRIPTION layer schema.
- Pydantic dataclass translation.

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Did new perspectives keep destabilizing the model? Tracking the revision pattern:

- **Phase 2 perspectives** produced anchors that REFINED the model (separating layers, identifying families, naming policy-vs-axis distinction). They did NOT force major revisions to the axis SET (count or identity).
- **Phase 3 ambiguity collapses** converged on consistent answers — each ambiguity resolved without forcing previous resolutions to revise.
- **No pattern of "patch and re-patch."** The model stabilized cleanly.

Accommodation trigger does NOT fire. The structural model fits the territory.

### Meta-Inspection final check (H6 model fit)

The 8-axis-in-4-families structure with policy / source-description / system-flag layers adjacent accommodates:
- All 10 frontier flags from surfacing
- All 8 ambiguities resolved in Phase 3
- The user's stated constraints (C1–C11)
- The user's stated values (memory H1, H2)
- The project's principles (notes.md, translation_principals.md, advanced_principles.md, harmony_layer.md)

The revision pattern was REFINEMENT (each ambiguity narrowing the model), not PATCHING (each perspective forcing a model overhaul).

### SV6 — Stabilized Model

The Comprehenslate translation-configuration framework is built on **8 user-facing axes organized into 4 families**, sitting on top of an always-on POLICY layer and adjacent to an auto-detected SOURCE-DESCRIPTION layer:

```
LAYER 1 — USER-FACING AXES (this inquiry's scope; 8 axes in 4 families):

  Reader family — properties of the intended reader:
    A1. RCL (Reader Competence Level)
        — envelope axis with sub-field overrides:
          - vocabulary breadth
          - syntactic processing capacity
          - idiom recognition
          - inference capacity
          - cultural-reference recognition
        — ~5 headline levels
    A2. Domain Expertise (~3 levels)
    A3. Source-Culture Proximity (~3 levels)

  Purpose family — what the translation is for:
    A4. Purpose / Use-case (~5 levels)

  Strategy family — how to handle source-target distance:
    A5. Source-Fidelity Stance (~3 levels)
    A6. Form-Preservation Strength (~5 levels; ties to harmony_layer.md Tier 1–4)
    A7. Scaffolding Density (~5 levels; subsumes footnote/transliteration/parenthetical decisions)

  Depth family — how much interpretive material to surface:
    A8. Analysis Depth (~4 levels; inherits from .env.example DEPTH_PROFILE)

LAYER 2 — POLICY (always-on; out of scope but adjacent):
  - Register alternation preservation (memory H1)
  - Polysemy resolution via local construction (memory H2)
  - Multi-meaning preservation when grammar permits
  - Nazm / structural meaning preservation (active when A6 ≥ light)
  - No smoothing of difficult nuances (per A2 principle)

LAYER 3 — SOURCE-DESCRIPTION (auto-detected with user override; out of scope but adjacent):
  - Source genre, era, register profile, source-culture

LAYER 4 — SYSTEM / PIPELINE FLAGS (out of scope, far):
  - Chunking strategy, parallel mode, output format, indexing
```

### Key patterns introduced

1. **Envelope axis with selective override** (provisional name; flag for critique to refine). Pattern: one axis with a HEADLINE level + optional sub-field overrides. Sub-field defaults derived from headline. Applies to RCL.
2. **Axis vs Policy distinction.** User-choice points become AXES. Project values unanimously prescribed become POLICY.
3. **Family meta-grouping.** Reader / Purpose / Strategy / Depth is navigational, not a configuration unit.
4. **Conservative-bias defaults at early calibration phase.** Defaults err toward preservation/scaffolding/depth; users dial down. Re-calibrate as user feedback accumulates.

### How SV6 differs from SV1

SV1 said: "the user has 5 sketched axes; some look right, some wrong. Feature Activation needs splitting; RCL might collapse; Purpose is missing."

SV6 commits to:
- **8 axes** (not 5), with **Purpose newly added** and **Form-Preservation Strength + Scaffolding Density** replacing the heterogeneous "Feature Activation."
- **RCL as envelope axis with selective overrides** — neither collapsed to one ordinal nor split to 5 separate axes.
- **4 families** as a navigational meta-grouping.
- **4-layer separation** (USER-AXIS / POLICY / SOURCE-DESCRIPTION / SYSTEM-FLAG) with only USER-AXIS in this inquiry's scope.
- **Policy layer made explicit** (register, polysemy, multi-meaning, nazm, no-smoothing) — distinguishes unanimously-prescribed project values from user-choice axes.
- **Conservative-bias defaults** at early calibration phase.
- **Language-agnostic at axis-concept level** confirmed.
- **Orthogonality verified** for every relevant pair via the four-corners test.

Frontier flags from surfacing all resolved or explicitly handed off:
- F1 (RCL decomposition) → envelope pattern
- F2 (Feature Activation heterogeneity) → split into Form-Preservation + Scaffolding
- F3 (Purpose as axis or driver) → separate axis
- F4 (B5 vs B1e orthogonality) → orthogonal via four-corners
- F5 (Multi-meaning as axis or policy) → policy; rendering handled by Scaffolding
- F6 (Form-Preservation as axis or derivative) → axis
- F7 (Depth vs Purpose) → separate axis
- F8 (Language-agnosticism stress test) → satisfied at concept level
- F9 (Default-bearing operationalization) → conservative-bias at early phase
- F10 (Source-side configuration) → separate adjacent layer

### Frontier flags handed to Decomposition

- **D1.** How does the system handle CONFLICTS between axis values at run time? (E.g., RCL=very_basic + Source-Fidelity=heavily_foreignized + Scaffolding=off — these point in incompatible directions.)
- **D2.** What is the per-axis default justification mechanism — is each default a separate sub-design, or do they come from a unified principle?
- **D3.** How do POLICY rules interact with axes? (E.g., always-on register-preservation interacts with Source-Fidelity Stance — does foreignization affect register handling, or is register handling independent?)
- **D4.** Where do edge-cases live? (Escape hatch for use-cases not expressible as axis-value combos.)
- **D5.** What does the envelope-axis-with-selective-override pattern look like as a typed structure? (Pydantic shape — defer further if next inquiry handles it.)
- **D6.** Naming refinement for "envelope axis with selective override" pattern.

These are decomposition-shaped questions — about the internal structure and relationships of the framework, not about whether the 8 axes are correct.

### Saturation indicators (telemetry)

- **Perspective saturation:** the last perspectives (Ethical, Phase/Calibration) produced NEW anchor types (defaults-as-cultural-encoding, calibration-state-dependence). Earlier perspectives still produced new TYPES (Technical → schema-shape; Strategic → temporal-stability). No premature saturation; the 7 perspectives + Frame-exit Completeness + Phase/Calibration produced diverse anchor types.
- **Ambiguity resolution ratio:** 10/10 ambiguities resolved (8 in Phase 3 + 2 in Phase 2's Frame-exit step). 0 OPEN.
- **SV delta:** SV6 differs structurally from SV1 in axis count (5→8), family meta-grouping (none → 4), layer-separation (implicit → explicit 4-layer), pattern introduced (none → envelope-with-overrides + axis-vs-policy + conservative-bias-defaults). Substantial structural shift.
- **Anchor diversity:** anchors drawn from all 5 types (constraints C1–C11; key insights KI1–KI12; structural points SP1–SP7; foundational principles FP1–FP6; meaning-nodes MN1–MN6) and from 8 perspectives. Diverse.

All four indicators show sufficiency. The model is stable; ready for decomposition.
