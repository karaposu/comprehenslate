# Branch: comprehenslate_mac_app_design

## Source Input

```text
if comprehensate would be a mac app, how woudl it look?

it should have a field of adding user's own  api key and choosig model additionally i guess. and also document intake process should be done too. what other concepts would be needed?
saving output as pdf or md file too needed.  we would need a config menu where we can select or deselect all configs,  enable or disbale policies. 

what else . what other things would be needed?

i guess since we aim to be able translate long books we would also need conitnue and pause translation? this also means we should have a project selection logic. and we shoudl be able to save trasnlation process somewhere (since it is in chunks) and map it as percentage. and also some reading screen so user can see as translation goes on and he can read. 
it shoudl ssupport local llm models openai and antropic models at once. 
  what else . what other things would be needed?  be innovative heavy and logical 

there is not need for signup or login i think. it not a webapp after all.
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** Item 1 (Mac app design with user-listed features + innovative-additional features)
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

### Item 1 — design what Comprehenslate would look like as a Mac app

**Literal statement:** *"if comprehensate would be a mac app, how would it look? — design the Mac app including the features the user enumerated (api key + model choice, document intake, save-as-pdf/md, config menu with policy toggles, pause/continue, project selection, save progress as percentage, reading screen, support local/OpenAI/Anthropic LLMs simultaneously, no signup/login) and surface additional features I think would be needed (be innovative heavy and logical)."*

**Kinds of ask the statement carries (MQ1 verdict-axis ambiguities):**
- *design-grain* — feature inventory (just a list of components) vs architectural layout (how components relate to each other) vs UI/UX mockup (visual / interaction design with screens) vs PRD-style spec (requirements + priorities + edge cases)
- *innovation-depth* — comprehensive enumeration of all plausible features vs focus on novel/surprising features beyond commonplace ones vs prioritized roadmap with MVP-vs-stretch tiers
- *scope-of-"would"* — current-state design constrained by what's buildable now vs ideal-state vision vs MVP-first incremental design with growth path
- *treatment-of-user-listed-features* — confirm them as-is + add to them vs critique/refine them + propose alternatives + add to them vs absorb them as fixed constraints

**Action-endpoints the statement could be targeting (MQ3 intent-axis ambiguities):**
- decide-product-direction (commit to a vision for the Mac app's shape)
- enumerate-feature-set (gather a complete list of components for later prioritization)
- pressure-test-completeness (the repeated *"what else?"* signals user wants me to surface features they haven't thought of)
- get-an-implementation-spec (concrete enough to start building)

## Goal

### Item 1 — Mac app design

**Deliverable shape (Deconstruct):** design (specification of a system); kinds = feature inventory + architectural sketches + cross-cutting concerns + novel additions + screen / component list; bounds = the existing Comprehenslate translation system (`schemas.py` + `SKILL/SKILL.md` + reference docs in `SKILL/references/core/`); Mac as the platform (native, not webapp, no signup); intentionally innovative.

**Motivation-chain ambiguities (MultiDepth WHY-axis):**
- *vision-formation* — user is forming a product vision and wants me to flesh it out
- *gap-discovery* — user is trying to ensure they haven't missed essential features; three repeated *"what else?"* prompts signal this strongly
- *design-pressure-testing* — user wants to know if their current list is sufficient or has structural gaps
- *prototype-prep* — preparing to build a prototype and wanting design scope settled first
- *educational-self-survey* — user wants to understand the Mac-app design space for translation tools generally
- *competitor-positioning* — implicit; user wants the Mac app to be unique / best-in-class (signaled by *"innovative heavy"*)

**Context-need (MQ2):**
- *verdict:* `schemas.py` (the 3-layer architecture: TC + Policy classes + PC) and `SKILL/SKILL.md` (the translation workflow) are required substrate — the Mac app wraps these; `harmony_layer.md` and `translation_principals.md` are relevant for translation-feature design
- *kinds:* Mac-platform patterns (SwiftUI / AppKit / Catalyst; native file pickers; menu bar; keyboard shortcuts); LLM-app patterns (BYO API key UX; provider switching; cost-display); document-processing patterns (long-form reading apps like Books, Kindle, Calibre; LibreOffice-style document handling); long-running task patterns (download managers; render queues; background processing with system notifications)
- *stance:* feasibility-focused vs vision-focused vs comprehensive

**Explicit exclusions (MQ4 NOT-list):**
- no signup / login (authentication and user accounts excluded)
- not a webapp (web-stack-only designs excluded; native Mac only)
- implicitly: no multi-user / collaboration features
- implicitly: no cloud-sync server obligation (BYO API key + local LLM support signal local-first / privacy-preserving)

## Considered Articulations

### Item 1 — Mac app design
1. Design Comprehenslate as a Mac app by enumerating the full component set (the user's named ones + additional ones I surface), grouped architecturally — covering UI screens, background services, data model, LLM-provider abstraction, configuration surface, and recovery/persistence — with explicit cross-cutting concerns (privacy, performance, accessibility).
2. Sketch the Comprehenslate Mac app as a layered design — input layer (document intake; project management); configuration layer (TC axes; Policy toggles; LLM provider/model/keys/cost); execution layer (chunked translation engine with pause/resume; terminology consistency); output layer (save as PDF/MD; reading view; export formats) — surfacing 8-15 additional features beyond the user's list, with reasoning per addition.
3. Pressure-test the user's named feature set for completeness; propose additional features clustered by what makes a long-form-book-translation app excellent (terminology consistency / glossaries; side-by-side source-target comparison; translation memory / corpus reuse; passage bookmarking; review/edit workflow; quality flagging); flag which features are essential-MVP vs stretch.
4. Produce a feature catalog + UI screen list + architecture sketch + cross-cutting concerns (privacy/local-data; performance; recovery; accessibility; localization-of-the-app-itself) for the Comprehenslate Mac app, balancing the user's listed features with innovative additions specific to theological / long-form-prose translation (e.g., side-by-side ayah viewer; harmony-layer visualization; per-chapter glossary; cross-translation collation).

## Scope Check

**Item 1:** Question covers goal. The MQ1/MQ3 ambiguity space is bracketed by the Deconstruct bounds (existing Comprehenslate substrate + Mac platform). The MQ4 NOT-list (no signup, no webapp, implicit no-multi-user / no-cloud-sync-server) keeps the scope honest. Goal includes motivation surfacing (WHY-axis: vision / gap-discovery / pressure-testing / prototype-prep / education / positioning) AND deliverable shape (architectural sketch + feature inventory + novel additions + cross-cutting concerns) — the question covers both via the four considered articulations.

**Specific-vs-pattern check:** Item 1's user-listed features are *specific examples* (api key field; document intake; etc.) but the user explicitly asks *"what else?"* three times and *"be innovative heavy and logical"* — making clear the inquiry should address the BROADER PATTERN (the full Mac-app design space for theological-translation tools), not just the user's enumerated specifics. The user-listed features are seeds + constraints, not exhaustive scope.

Question covers goal.

## Synthesis Trigger

This inquiry synthesizes context from prior outputs and project state:

- `/Users/ns/Desktop/projects/comprehenslate/SKILL/references/config/schemas.py` — the authoritative 3-layer schema architecture (TC + 7 Policy classes + PC). The Mac app's configuration UI wraps these schemas directly.
- `/Users/ns/Desktop/projects/comprehenslate/SKILL/SKILL.md` — the 5-step translation workflow (ask source → load refs → ask target language → present TC options → translate to MD). The Mac app implements this workflow as native UI.
- `/Users/ns/Desktop/projects/comprehenslate/SKILL/references/config/config_base_source.md` — calibration context for the 8 TC axes. The Mac app's config panel needs to expose these calibrations to the user.
- `/Users/ns/Desktop/projects/comprehenslate/SKILL/references/config/policy_config_base_source.md` — calibration context for the 7 Policy classes. The Mac app's Policy panel needs the same.
- `/Users/ns/Desktop/projects/comprehenslate/SKILL/references/core/harmony_layer.md` — the harmony-layer Tier 1-4 preservation system. The Mac app may need a harmony-layer visualization for quality assurance.
- `/Users/ns/Desktop/projects/comprehenslate/SKILL/references/core/translation_principals.md` + `advanced_principles.md` — translation principles that constrain UI/feature decisions.

CONCLUDE will require an `## Inherited Commitments Re-test` section testing each inherited commitment (especially: 3-layer schema architecture as the config-UI substrate; SKILL.md 5-step workflow as the native-app workflow; harmony-layer Tier 1-2 preservation as a non-negotiable quality gate) with evidence cited or explicit flag.
