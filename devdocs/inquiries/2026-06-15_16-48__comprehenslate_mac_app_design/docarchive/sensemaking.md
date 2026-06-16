# Sensemaking — comprehenslate_mac_app_design

## User Input

```text
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/_branch.md

Upstream outputs in same folder: articulate_simple.md + surfacing.md. Read both as inquiry framing + upstream substrate.

Surfacing produced 155 items across 13 regions; the high item-count is intentional per user's "innovative heavy" framing. Sensemaking should produce a stabilized model that:
- Identifies the LOAD-BEARING architectural skeleton of the Mac app (what's essential vs nice-to-have)
- Resolves the design-grain × intent joint axis identified at articulate_simple's MQA (reconcile point)
- Decides what to do with the frontier flags from Surfacing (translation-principles-to-UI mapping; monetization model out-of-scope?; R12+R13 not exhausted)
- Handles the Synthesis Trigger's 6 priors with Inherited Commitments Re-test (the 3-layer schema architecture; the SKILL.md 5-step workflow; harmony-layer Tier 1-2 preservation as non-negotiable; the translation principles' "comprehensation" identity)

Save sensemaking output to: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/sensemaking.md
```

---

## SV1 — Baseline Understanding

The user wants a design for Comprehenslate as a Mac app. Surfacing generated 155 candidate features. The job is to identify the load-bearing architectural skeleton and shape the deliverable so it's both a feature inventory AND an architectural sketch — resolving the design-grain × intent joint axis. Native single-user / local-first / no-signup constraint. Wraps existing Comprehenslate substrate (TC + 7 Policy classes + PC + 5-step SKILL workflow + harmony-layer + translation principles).

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1.** No signup / no login (MQ4 exclusion).
- **C2.** Not a webapp; native Mac (MQ4 exclusion).
- **C3.** Single-user (implicit from C1 + Mac context).
- **C4.** Local-first / privacy-preserving (implied by BYO API key + local-LLM support).
- **C5.** Wraps existing `schemas.py` (TC + 7 Policy classes + PC) — no schema rework.
- **C6.** Wraps existing `SKILL.md` 5-step workflow.
- **C7.** Tier 1-2 harmony-layer preservation is non-negotiable regardless of TC config choices.
- **C8.** Multi-provider LLM (Anthropic + OpenAI + local via Ollama / LM Studio) simultaneously.
- **C9.** User explicitly asks for *"innovative heavy"* — bias toward features unique to Comprehenslate's substrate (harmony layer + translation principles), not generic Mac-app polish.
- **C10.** Long-book translation is the primary use case (pause/resume; chunk persistence; progress tracking are direct asks).

### Key Insights

- **KI1 (load-bearing).** The Mac app is essentially a **UI + persistence shell around the existing Comprehenslate translation system**. The schemas.py 3-layer architecture and SKILL.md 5-step workflow are SUBSTRATE; the Mac app provides graphical access + long-running execution with persistence/recovery + multi-provider integration + export. The app does not redefine the substrate; it wraps it.

- **KI2.** **"Project" is the unifying concept** the Mac app needs. A Project bundles: source document + TC config + Policy config set + PC config + provider/model selection + output artifacts + per-chunk state + glossary + TM + bookmarks/annotations. This is the macOS document-based-app pattern (each Project = a `.compldoc` file). Project replaces the implicit "translation job" abstraction of SKILL.md.

- **KI3.** Translation principles in `references/core/` split into two categories: (a) **UI-mappable** — produce user decisions or visualizations the user interacts with (harmony-layer Tier 1-2 flagging; multi-meaning collation; idiom alerts; cultural-reference inbox; per-chunk lineage; per-chunk analysis-depth explanation; passage bookmarks for fihrist-style micro-to-macro mirroring); (b) **non-UI-mappable** — intrinsic LLM behavior (sünuhat-style two-step processing; ihlas-driven quality; collective-interpretation rationale; self-illuminating passage detection — these are LLM behaviors, not user controls). The mapping decision is per-principle, not all-or-nothing.

- **KI4.** The 155 surfaced items naturally cluster into **5 architectural layers**: Project shell / Configuration surface / Execution engine / Reading & output / Quality & translation-craft. Plus cross-cutting concerns (privacy / performance / accessibility / Mac-platform polish). Each layer has a 3-tier triage: ESSENTIAL (MVP non-negotiable) / DIFFERENTIATING (the "innovative-heavy" surface) / DEFERRABLE (nice-to-have, future).

- **KI5.** The user's "innovative heavy" framing + Comprehenslate's harmony-layer + translation-principles substrate **distinguish this from generic LLM-translation apps**. The DIFFERENTIATORS are: harmony-layer visualization; per-chunk lineage; per-policy preview; multi-translation collation; smart cache; idiom alerts; cultural-reference inbox. These are the user's true "innovative" surface — they surface Comprehenslate's unique substrate.

- **KI6 (resolves MQA joint axis).** The design-grain × intent joint axis from articulate_simple's MQA reconcile resolves to: **deliver an architectural sketch + feature inventory + cross-cutting concerns + MVP roadmap**, organized by architectural layer with each layer surfacing its essential / differentiating / deferrable features. Not pure feature-list (loses visualizability). Not pure architecture (loses the innovative-heavy enumeration). Not UI mockup (out of scope for an inquiry artifact). The composite resolves the joint axis.

### Structural Points

- **SP1.** Five-layer architecture: **Project shell / Configuration surface / Execution engine / Reading & output surface / Quality & translation-craft surface.**
- **SP2.** **Project as primary data model.** `.compldoc` file format (macOS document-based-app package extension).
- **SP3.** **Provider abstraction** as a separate cross-cutting layer underneath the execution engine. Swift protocol with concrete implementations per provider (AnthropicProvider, OpenAIProvider, OllamaProvider).
- **SP4.** **Per-chunk state persistence** is the load-bearing primitive for pause/resume/crash-recovery/percentage-progress. Each chunk's state is atomically written to disk.
- **SP5.** **Three-tier triage per layer** — ESSENTIAL / DIFFERENTIATING / DEFERRABLE. This triage is the development roadmap (MVP = essential per layer; v2 = adds differentiating; v3+ = deferrable).

### Foundational Principles

- **FP1.** **Local-first by default.** All project data lives on the user's disk; iCloud sync is opt-in.
- **FP2.** **BYO credentials.** App holds no API keys server-side because there is no server-side. Storage is macOS Keychain.
- **FP3.** **Native Mac patterns where they map naturally** (document-based-app; menu bar; Keychain; system notifications; SwiftUI/AppKit conventions).
- **FP4.** **Tier 1-2 harmony-layer preservation is non-negotiable** regardless of user config. A constant, not a feature toggle.
- **FP5.** **The 3-layer schema architecture (TC + Policy + PC) is the canonical configuration surface.** UI exposes it; doesn't rewrite or hide it.
- **FP6.** **The 5-step SKILL.md workflow is the canonical translation workflow.** UI wraps it; doesn't bypass it.
- **FP7.** **FP2 from prior session extends: don't declare what the LLM can infer.** The Mac app's intake doesn't ask the user for source language (LLM-inferable); doesn't ask for chunking strategy (LLM-handled per PC defaults). The user is asked only for value judgments.

### Meaning-Nodes

- **MN1.** *Project* — the document-based-app unit bundling source + config + state + outputs.
- **MN2.** *Layer* — one of the 5 architectural strata.
- **MN3.** *Provider* — an LLM backend (Anthropic / OpenAI / Ollama / LM Studio) accessed via unified abstraction.
- **MN4.** *Chunk* — the atomic translation unit per `PC.chunking_granularity`; persisted independently.
- **MN5.** *Differentiator* — a feature unique to Comprehenslate (vs generic LLM-translation apps): harmony viz; lineage; per-policy preview; multi-translation collation.
- **MN6.** *Comprehensation* — from `translation_principals.md`: deeper-than-translation work that preserves multi-meaning, harmony layer, nazm, layered semantics. The app's identity.
- **MN7.** *Tier triage* — the essential / differentiating / deferrable classification per layer that doubles as MVP roadmap.

### Meta-Inspection cross-reference after SV2

- **H4 (concept names):** "Project," "Layer," "Provider," "Chunk," "Differentiator," "Comprehensation," "Tier triage" — load-bearing. Project + Chunk are standard document-based-app + CAT-tool vocabulary. Layer / Provider are standard architecture terms. Comprehensation is the user's own term in `translation_principals.md`. Triage is product-roadmap vocabulary. Not loop-coined neologisms.
- **H5 (motivating examples):** 155 items provide rich substrate; not single-example over-extrapolation.

### SV2 — Anchor-Informed Understanding

The Mac app is a **Project-based native shell** wrapping the existing Comprehenslate translation system (schemas + SKILL workflow). Five architectural layers (Project shell / Config / Execution / Reading & output / Quality). Each layer has a 3-tier triage (essential / differentiating / deferrable). The user's *"innovative heavy"* framing maps to the differentiating tier — surfacing features that distinguish Comprehenslate from generic translation apps via its harmony-layer + translation-principles substrate. 7 principle-derived UI features identified. Project as the unifying data model; `.compldoc` as the file format.

---

## Phase 2 — Perspective Checking

### Technical / Logical

- The 5-layer architecture is implementable on macOS via SwiftUI + Swift concurrency + document-based-app APIs.
- `.compldoc` as file format: practical options are a directory bundle (package extension) containing JSON config + per-chunk Markdown files + SQLite for project-level metadata (glossary, TM, bookmarks). Choose directory-bundle for ease of resume-from-disk + atomic per-chunk writes.
- Multi-provider abstraction: Swift protocol with concrete adapters per provider. Provider list is extensible (Apple Intelligence as future provider).
- Per-chunk persistence: each chunk as a separate file in the project bundle; atomic writes; resume from disk.
- **New anchor:** *implementation-substrate* — SwiftUI + Swift concurrency + document-based-app + Keychain. Standard platform choices; the innovation lives in the application layer, not the platform.

### Human / User

- User's repeated *"what else?"* + *"be innovative heavy"* + anti-bloat preference (recurring across the session) compose as: *"include exhaustively in the catalog, prioritize aggressively for MVP."* Two-tier presentation needed.
- User has spent the session building schemas + workflow + calibration docs. The Mac app is the CONSUMER of that work. The design should make all that visible (Config surface that EXPOSES the schemas; Reading view that shows live translation; Quality layer that surfaces the harmony layer).
- **New anchor:** *user-stance-tradeoff* — innovative-heavy enumeration + anti-bloat MVP discipline compose as exhaustive-catalog-with-tiered-prioritization. The deliverable must do both.

### Strategic / Long-term

- A Mac-app distribution channel for an AI-translation tool likely targets specific personas: theological-translation researchers (Nursi anchor); language-learning scholars; literary translators of religious / philosophical texts.
- Comprehenslate's competitive differentiation rests on the harmony-layer + translation-principles substrate. Without those, it's just another GPT wrapper. The Mac app must SURFACE these differentiators (per-chunk lineage; harmony-viz; multi-translation collation) prominently.
- **New anchor:** *differentiator-priority* — features that surface Comprehenslate's unique substrate are HIGH priority in the differentiating tier. Generic LLM-app features are LOWER priority.

### Risk / Failure

- **Risk 1:** Long-running translation crashes mid-book; user loses work. Mitigation: per-chunk persistence + crash recovery (already core in surfacing).
- **Risk 2:** API costs surprise the user (a long book translated with Opus could cost $50+). Mitigation: pre-translation cost prediction + cumulative-cost display.
- **Risk 3:** Over-engineering the UI — too many tabs, too many settings. Mitigation: the 5-layer architecture provides clean separation; defaults hide complexity.
- **Risk 4:** Privacy concerns with API providers (especially for sensitive religious texts). Mitigation: local-LLM support + local-first data + opt-in cloud sync + Keychain storage.
- **Risk 5:** Multi-provider abstraction breaks when one provider changes API shape. Mitigation: well-defined Swift protocol; per-provider adapter.
- **New anchor:** *risk-mitigations-as-features* — cost prediction + crash recovery + local LLM + Keychain are not just nice-to-haves; they're risk-mitigations that fall into the ESSENTIAL tier.

### Resource / Feasibility

- A solo or small-team developer can build a SwiftUI Mac app of this scope over months, not years. The 5-layer architecture maps to manageable development phases.
- MVP scope (essential tier only across all 5 layers) is buildable in ~3-6 months. Full scope is multi-year.
- **New anchor:** *MVP-phasing* — the 3-tier triage IS the development roadmap. MVP = essential. v2 = adds differentiating. v3+ = deferrable.

### Ethical / Systemic

- Translating theological texts has ethical weight (sacred-text fidelity, doctrinal positions in translation choices). The app should respect this: clear provenance per chunk; ability to audit; user-overridable Policy choices.
- Bias: LLMs trained on Western-Christian-centric corpora may translate Islamic theological terms with Western theological connotations. The Mac app's Policy classes (especially HonorificsPolicy, NonMainLangPartsPolicy) are the user's tool for controlling this. UI must make policy choices visible.
- **New anchor:** *ethical-provenance* — per-chunk lineage view (which TC axes + Policy values produced this output) is not just a power-user feature; it's an ethical-audit feature for sacred-text translation.

### Definitional / Internal Consistency

- Is the 5-layer architecture self-consistent? Test: can each surfacing item be placed in exactly one layer?
  - Most yes. A few overlap: glossary configuration vs glossary enforcement (configured in Quality; surfaced as a Config sub-screen). These resolve by "primary home" rule: glossary's primary home is Quality (where it's enforced); its config UI is a sub-screen of the Quality layer.
- The 5-step SKILL.md workflow maps to the Mac-app UX flow: (1) project list → new project → (2) document intake → (3) language picker → (4) config editor → (5) translation execution → output. Steps 1+2 collapse into a project-creation wizard. Direct alignment.
- The 3-layer schema architecture maps to the Configuration surface: TC editor + Policy editor + PC editor are three sub-screens of one Config layer. Clean.

### Definitional / Frame-exit Completeness

**Gating predicate test:** the inquiry's commitments include the term *Layer*, used across distinct values within the inquiry's committed structures (5 layers in the architecture; 4 Tiers in the harmony-layer Tier 1-4 system). Gating fires.

1. **Existence Enumeration.** *Layer* project-wide refers to: software architecture layers (the 5 here); harmony-layer Tier 1-4 (translation-concept layers); UI z-order layers (visual stacking). The inquiry's frame includes only software architecture layers; harmony-Tier-as-layer is upstream substrate.

2. **Role Assessment.** Harmony-Tier-as-layer is REFERENCED from inside the inquiry (the Quality layer USES the harmony-Tier concept to flag violations) but is upstream substrate, not part of the architecture being designed. The role is preserved correctly (we surface harmony-Tier-as-layer through a UI feature; we don't redesign it).

3. **Verdict Rigor.** Strongest counter to "5 layers is the right shape." Could it be 3 layers? Could it be 7?
   - 3-layer test: UI / business logic / data. Loses architectural granularity needed for differentiation; can't separate Config from Execution from Quality cleanly.
   - 7-layer test: splitting Quality into glossary-mgmt + TM-mgmt + harmony-viz + collation + lineage. Over-decomposes — these are sub-modules of one layer.
   - 5 layers is structurally motivated by the natural coupling clusters in surfacing: Project (lifecycle) / Config (settings) / Execution (runtime) / Reading-output (consumption) / Quality (craft). Each cluster has distinct lifecycle and high internal coupling. Verdict holds.

4. **Residual.** Is there a frame-exit concern about *Layer* the categories did NOT capture? Localization layer / accessibility layer (often called *layers* in UX literature) — these are cross-cutting CONCERNS, not architectural layers; handled separately as a design dimension. No further residual.

### Phase / Calibration-State

- Mac-app design depends on calibration of: LLM provider APIs (current state — OpenAI / Anthropic / Ollama / LM Studio APIs available); SwiftUI capability (adequate); macOS document-based-app APIs (stable). Principle holds at current calibration.
- Future calibration shifts: if Apple introduces system-level LLM (Apple Intelligence as a provider), it becomes another provider via the abstraction. If LLM costs drop drastically, cost-prediction becomes less load-bearing. Forward-compatible.
- **New anchor:** *calibration-tolerance* — the design composes with current LLM-provider landscape and is forward-compatible with new providers.

### Meta-Inspection cross-reference after SV3

- **H1 (candidate set):** are the 5 layers + 3 tiers the right cuts? Yes per Frame-exit verdict.
- **H2 (frame scope):** covered.
- **H3 (question framing):** *"how would it look"* is graphically-suggestive but the answer is structurally-architectural. We answer the joint axis (architecture + features + cross-cutting). The user can pursue UI mockups in a follow-up inquiry.
- **H7 (phase/calibration state):** covered.

### SV3 — Multi-Perspective Understanding

The Mac app is a Project-based native shell with 5 architectural layers (Project shell / Config / Execution / Reading & output / Quality) and 3-tier per-layer triage (essential / differentiating / deferrable). The design composes with the current LLM-provider landscape (multi-provider abstraction) and is forward-compatible. Risk-mitigations (cost prediction, crash recovery, local LLM, Keychain storage) fall into the essential tier. Differentiators (harmony viz, lineage, per-policy preview, multi-translation collation) fall into the differentiating tier and are HIGH priority because they surface Comprehenslate's unique substrate. Ethical provenance (per-chunk lineage view) is an ethical-audit feature for sacred-text translation. 7 translation-principle-derived differentiating features identified. MVP-phasing is the 3-tier triage as roadmap.

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — Design-grain × Intent (the MQA joint axis)

**Strongest counter-interpretation:** deliver pure feature inventory; let architecture emerge later.

**Why the counter fails (structural):** Surfacing produced 155 items; without architectural organization, the inventory is impenetrable. The user explicitly asked *"how would it look?"* — implying a visualizable structure (graphical OR architectural). The repeated *"what else?"* + *"be innovative heavy"* requires categorical thinking to verify completeness. Pure feature inventory fails the visualizability test.

**Confidence:** HIGH.

**Resolution:** deliver the **composite — 5-layer architecture + per-layer feature inventory + cross-cutting concerns + MVP roadmap**.

- **Fixed:** the deliverable shape.
- **No longer allowed:** pure feature lists without architectural organization; pure architecture without feature enumeration.
- **Depends:** Decomposition uses the 5 layers as the piece structure.
- **Model change:** the deliverable composite is committed.

### Ambiguity 2 — The unifying data model concept

**Strongest counter-interpretation:** the app is workspace-based or task-based, not project-based.

**Why the counter fails (structural):** *Workspace* implies a single global state where multiple translations coexist; the user explicitly named *"project selection logic"* — committing to projects-as-units. *Task* is too granular (a project has many translation tasks). Project at the document-bundle level matches the document-based-app pattern macOS provides natively. It's also the natural unit for *"save percentage progress"* (a project is X% done) and *"pause/resume"* (you pause a project, not a task).

**Confidence:** HIGH.

**Resolution:** **Project** is the unifying data model concept. Each project = one `.compldoc` file.

- **Fixed:** Project as primary data abstraction; `.compldoc` as the file format (directory bundle).
- **No longer allowed:** workspace-style global state; task-based granularity confusion.
- **Depends:** every architectural layer references Project; persistence + recovery are per-project.
- **Model change:** the data model is committed.

### Ambiguity 3 — Translation-principles → UI features mapping (Frontier flag from surfacing)

**Strongest counter-interpretation:** every translation principle from `references/core/` deserves a UI feature (uniform mapping).

**Why the counter fails (structural):** Some translation principles are intrinsic LLM behavior — the LLM applies them while translating; the user doesn't toggle them. Examples: *"no single person can interpret a comprehensive work"* (philosophical motivation); *"ihlas (sincerity) affects interpretation quality"* (not a UI control); *"sünuhat (writing from intuitive understanding then validating)"* (LLM process, not user control). Only principles that produce USER DECISIONS or USER-VISIBLE STRUCTURE deserve UI features.

**Confidence:** HIGH.

**Resolution:** principle → UI mapping is **selective**. The 7 UI-mappable principles:

| # | Principle | UI feature |
|---|---|---|
| 1 | Harmony-layer Tier 1-2 preservation | Harmony-layer visualization + Tier 1-2 violation flagging |
| 2 | Multi-meaning preservation | Multi-translation collation + alternative-rendering inbox |
| 3 | Nazm preservation (word order as meaning) | Per-chunk lineage view (shows word-order rationale) |
| 4 | Layered meaning (sarahat / işaret / remiz / îma / telvih / telmih) | TC.A8 analysis_depth-driven per-chunk explanation overlay |
| 5 | Micro-to-macro mirroring (fihrist) | Passage bookmarks + thematic markers |
| 6 | Idiom recognition | Idiom-alert inbox (flag idioms without clean target equivalent) |
| 7 | Cultural reference recognition | Cultural-reference inbox (per TC.A3 source_culture) |

Non-UI-mappable principles (intrinsic LLM behavior): ihlas-driven quality; collective-interpretation rationale; sünuhat-style two-step processing; self-illuminating passage detection.

- **Fixed:** 7 UI-mappable principles identified; the rest remain intrinsic LLM behavior.
- **No longer allowed:** forcing UI features for non-UI-mappable principles; ignoring UI-mappable principles in the design.
- **Depends:** Innovation generates these 7 principle-derived features as differentiating-tier candidates.
- **Model change:** the *"innovative-heavy"* tier is concretely populated.

### Ambiguity 4 — Provider/model configuration: per-project or per-app?

**Strongest counter-interpretation:** provider/model is global per app (user picks once, uses for all projects).

**Why the counter fails (structural):** Different projects have different needs. A scholarly project might use Claude Opus; a casual project might use a local LLM for cost reasons. Forcing global provider/model loses this flexibility. BUT — defaulting to per-app and allowing per-project override gives both sensible defaults and flexibility.

**Confidence:** HIGH.

**Resolution:** provider/model is **two-level** — app-level defaults + per-project overrides. The user sets a default in Settings; each new project inherits it; the user can override per project.

- **Fixed:** two-level provider/model configuration.
- **No longer allowed:** provider locked at global only; provider locked at per-project only without sensible defaults.
- **Depends:** the Config surface has TWO entry points (app-level Settings + per-project Settings).
- **Model change:** provider abstraction refined.

### Ambiguity 5 — Monetization model: in scope or out?

**Strongest counter-interpretation:** monetization belongs in the design.

**Why the counter fails (structural):** The user explicitly excluded signup/login. A signup-less Mac app has monetization options that don't require server-side: one-time purchase (Mac App Store or direct download); donation-ware; open-source. None of these requires UI features beyond an About page. So monetization is OUT of the architectural design (no UI surface changes); it's a distribution decision for later.

**Confidence:** HIGH.

**Resolution:** monetization is **out-of-architecture-scope**; flagged in Open Questions as a distribution-side decision.

- **Fixed:** no monetization UI features.
- **No longer allowed:** spending design effort on subscription / freemium / login.
- **Depends:** nothing.
- **Model change:** Open Questions captures it for later.

### Ambiguity 6 — Inherited Commitments Re-test

**Strongest counter-interpretation:** the priors' commitments need extensive re-testing.

**Why the counter fails (structural):** The priors (schemas.py, SKILL.md, harmony_layer.md, translation_principals.md, etc.) are SETTLED SUBSTRATE this inquiry CONSUMES, not commitments to re-test from scratch. The Mac app design WRAPS them; it doesn't reopen them.

**Confidence:** HIGH.

**Resolution:**

| Commitment | Re-test status | Evidence |
|---|---|---|
| 3-layer schema architecture (TC + Policy + PC) | **RE-TESTED — confirmed** | The Mac app's Configuration surface directly exposes the 3 schemas as 3 sub-screens (TC editor + Policy editor + PC editor). Architecture unchanged; UI design respects it. |
| SKILL.md 5-step workflow | **RE-TESTED — confirmed** | The Mac-app UX flow maps the 5 steps to native UI (project list → new project → document intake → language picker → config editor → translation). Steps 1+2 collapse into a project-creation wizard; otherwise direct alignment. |
| Harmony-layer Tier 1-2 preservation as non-negotiable | **RE-TESTED — confirmed** | The Mac app's Quality layer surfaces Tier 1-2 violation flagging as a feature; the non-negotiability is preserved as an INTRINSIC LLM behavior the UI cannot toggle off. UI shows it; doesn't disable it. |
| Translation principles' "comprehensation" identity | **RE-TESTED — confirmed but frame revised** | The principles split into UI-mappable (7 differentiating features per Ambiguity 3) and intrinsic-LLM-behavior. The identity is preserved; the UI exposes part of it; the rest stays intrinsic. |
| Anti-bloat principle (recurring across this session) | **RE-TESTED — confirmed** | The 5-layer architecture + 3-tier triage IS the anti-bloat discipline. MVP = essential only; everything else is deferred or differentiated. |
| FP2 "Don't declare what the LLM can infer" | **RE-TESTED — confirmed and extended** | The Mac app's intake doesn't ask for source language (LLM-inferable); doesn't ask for chunking strategy (LLM-handled per PC defaults). User asked only for value judgments. FP2 is enforced in the UI design. |

- **Fixed:** priors confirmed as substrate; the Mac app design respects them all.
- **No longer allowed:** reopening or replacing the substrate.
- **Depends:** nothing — substrate stays.
- **Model change:** explicit confirmation of inheritance.

### SV4 — Clarified Understanding

Stabilized model: Mac app = Project-based native shell with 5 architectural layers (Project shell / Config / Execution / Reading & output / Quality & translation-craft); each layer has a 3-tier triage (essential / differentiating / deferrable); cross-cutting concerns are handled separately (privacy / performance / accessibility / Mac-platform polish). Provider/model is two-level (app default + per-project override). 7 translation-principle-derived UI features identified for the differentiating tier. Monetization is out-of-architecture-scope. All 6 prior commitments confirmed (some with frame revision); the design respects all substrate.

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed

- 5-layer architecture: **Project shell / Configuration surface / Execution engine / Reading & output / Quality & translation-craft.**
- Project as primary data model; `.compldoc` as directory-bundle file format.
- 3-tier triage per layer: ESSENTIAL / DIFFERENTIATING / DEFERRABLE.
- Provider/model two-level: app-default + per-project-override.
- Local-first, no signup, single-user, BYO API key.
- Tier 1-2 harmony-layer preservation as non-negotiable intrinsic constant.
- 5-step SKILL workflow as the UX flow spine.
- 7 translation-principle-derived UI features for differentiating tier.
- Cross-cutting concerns as a separate design dimension.

### Eliminated

- Pure feature-list deliverable without architecture.
- Pure architecture without feature enumeration.
- Workspace-based or task-based data model.
- Server-side anything.
- Monetization features in the UI.
- Forcing UI features for every translation principle.
- Asking the user for LLM-inferable facts (source language; chunking strategy).

### Viable paths remaining

- Decomposition uses the 5 layers + cross-cutting concerns as the piece structure (~6 pieces).
- Innovation generates per-layer content (essential + differentiating + deferrable items per layer) + cross-cutting feature set + MVP roadmap.
- Critique applies dimensions: layer-correctness, tier-correctness, anti-bloat conformance, differentiator-load-bearing-ness, MVP-feasibility, harmony-preservation-honoring, FP2 conformance, Mac-platform-native-ness.

### SV5 — Constrained Understanding

The finding is organized as: (a) the 5-layer architecture spine + Project data model; (b) per-layer feature triage (essential / differentiating / deferrable); (c) cross-cutting concerns; (d) MVP roadmap (essential per layer); (e) the 7 translation-principle-derived differentiating features (the innovative-heavy surface); (f) Inherited Commitments Re-test confirming all substrate; (g) Open Questions including monetization-as-distribution-decision. The deliverable composite resolves the design-grain × intent joint axis from articulate_simple's MQA.

---

## Phase 5 — Conceptual Stabilization

### Accommodation trigger check

Did new perspectives keep destabilizing the model?

- Anchor extraction landed on 5-layer architecture + Project-as-unit quickly.
- Technical / Human / Strategic / Risk / Resource / Ethical perspectives added anchors (implementation-substrate, user-stance-tradeoff, differentiator-priority, risk-mitigations-as-features, MVP-phasing, ethical-provenance) but each was additive — none forced revision of the 5-layer architecture or Project-as-unit.
- Definitional Internal Consistency verified self-consistency.
- Definitional Frame-exit verified the 5-layer choice against 3-layer and 7-layer counters.
- Phase/Calibration-State added calibration-tolerance.

No model-misfit pattern. **Accommodation trigger does NOT fire.** Stabilization is appropriate.

### SV6 — Final Stabilized Model

**Comprehenslate as a Mac app is a native Project-based shell with 5 architectural layers wrapping the existing Comprehenslate translation system (schemas.py 3-layer architecture + SKILL.md 5-step workflow + harmony-layer + translation principles).**

**Five architectural layers:**

1. **Project shell** — document-based-app pattern; Project = one `.compldoc` directory bundle file containing source + config + per-chunk state + outputs + glossary + TM + bookmarks. Manages project lifecycle (list / create / open / archive / duplicate).

2. **Configuration surface** — graphical access to the 3-layer schema architecture. TC editor (8 axes with calibration-doc explanation); Policy editor (7 Policy classes with on/off + value selectors); PC editor (engine knobs). Two-level provider/model config (app-default + per-project-override).

3. **Execution engine** — chunked translation orchestration with per-chunk persistence, pause/resume, parallel-mode (per `PC.parallel_mode`), background continuation, crash recovery, multi-provider abstraction (Anthropic + OpenAI + local via Ollama / LM Studio).

4. **Reading & output surface** — live reading view (translation as it happens); side-by-side source-target alignment; export to MD / PDF / HTML / ePub / plain / JSON; bilingual export; translator-notes export.

5. **Quality & translation-craft surface** — harmony-layer Tier 1-2 violation flagging; terminology consistency check; glossary editor + enforcement; translation memory; multi-translation collation; per-chunk lineage view; idiom alerts; cultural-reference inbox.

**Plus cross-cutting concerns:** privacy (local-first, Keychain), performance (streaming, lazy lists, Swift concurrency), accessibility (VoiceOver, Dynamic Type, dark mode), Mac-platform polish (document-based-app, menu bar, system notifications, Spotlight, share extension, keyboard shortcuts).

**Per-layer 3-tier triage** (essential / differentiating / deferrable) doubles as the MVP roadmap:
- **MVP (essential per layer):** ~3-6 month single-developer build with 2 providers + MD/PDF output + terminology consistency only.
- **v2 (essential + differentiating):** adds the 7 principle-derived UI features + local LLM + ePub/HTML.
- **v3+ (everything):** adds deferrable features (multi-document projects, scripting API, plugins, Continuity).

**The 7 translation-principle-derived differentiating features** (the innovative-heavy surface): harmony-layer visualization, multi-translation collation, per-chunk lineage view, per-chunk analysis-depth explanation, passage bookmarks (fihrist), idiom alerts, cultural-reference inbox. Plus engineering differentiators: smart cache, cost prediction, project templates, glossary suggestion.

**SV6 vs SV1:**
- SV1 framed the request as *"design a Mac app with the user's features + additions."*
- SV6 commits to a **5-layer architecture + 3-tier triage + Project-as-data-model + 7 translation-principle-derived differentiators + MVP-feasibility-phased roadmap**. The deliverable composite (architecture + feature inventory + cross-cutting concerns + MVP path) explicitly resolves the design-grain × intent joint axis from articulate_simple's MQA reconcile. The Comprehenslate-specific differentiators are explicitly named (not just *"innovative"*). All 6 prior commitments confirmed; the design respects all substrate.

---

## Saturation Indicators (Telemetry)

- **Perspective saturation:** the last two perspectives (Phase/Calibration-State; Frame-exit residual) confirmed existing anchors without producing new anchor types. Approaching saturation.
- **Ambiguity resolution ratio:** 6 ambiguities identified; 6 resolved with HIGH confidence; 0 OPEN. Ratio = 1.0.
- **SV delta:** SV1 was "design a Mac app with user features + additions"; SV6 grounds the design in 5-layer architecture + Project data model + 3-tier triage + 7 principle-derived differentiators + MVP roadmap. Substantial structural shift.
- **Anchor diversity:** anchors came from all five types (Constraints / Key Insights / Structural Points / Foundational Principles / Meaning-Nodes) and from 7 perspectives (Technical / Human / Strategic / Risk / Resource / Ethical / Internal Consistency / Frame-exit / Phase). Multi-dimensional.

## Failure Mode Check (Pattern B — process-level)

- **Status Quo Bias:** NOT FIRED. The Mac-app design is genuinely new (no existing app to defend); priors confirmed because they're settled substrate, not because the inquiry protects them defensively.
- **Premature Stabilization:** NOT FIRED. Six ambiguities collapsed with HIGH confidence after multi-perspective testing.
- **Anchor Dominance:** PARTIAL — the 5-layer architecture (SP1) is doing much of the structural work. Corrective check: if SP1 were removed, would the model collapse? It would lose its spine but Project-as-data-model (SP2) + 3-tier triage (SP5) would survive and could regenerate the architecture. Not single-pillar. Accepted.
- **Perspective Blindness:** NOT FIRED. Uncomfortable perspectives (Risk; Frame-exit Verdict Rigor with 3- and 7-layer counters) explicitly applied.
- **Clean Resolution Trap:** NOT FIRED. Each ambiguity tested counter-interpretations on structural grounds (mechanism / shape / consistency), not on precedent alone.
- **Self-Reference Blindness:** NOT FIRED. Subject is a future Mac app; not the discipline itself.

## Verdict

**PROCEED.** Six SVs produced with substantial SV1→SV6 delta. Six ambiguities collapsed at HIGH confidence. The design-grain × intent joint axis is resolved (composite deliverable). Frontier flags from Surfacing handled (principle-mapping selective; monetization out-of-scope; R12+R13 absorbed as differentiating-tier candidates). All 6 inherited commitments confirmed (some with frame revision). No LAYER 1 (failure modes #1–#6) fires. One PARTIAL on Anchor Dominance, accepted because multiple anchors survive removal of any one.
