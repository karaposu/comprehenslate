---
status: active
model: claude-opus-4-7
effort: max
revised: 2026-06-16
---

# Finding: comprehenslate_mac_app_design

## Post-conclusion Correction Notice (2026-06-16)

This finding was written with framing that scoped the product to religious / theological texts (specifically Said Nursi's *Risale-i Nur* and related religious-philosophical corpora). That framing was **incorrect** — Comprehenslate is a generic translation product per `SKILL/SKILL.md` (*"works for any source document; treat the calibration corpus as a tuning anchor, not the product's scope"*). The religion-scoped framing was diagnosed at `devdocs/inquiries/2026-06-16_09-08__loop_diagnose__persona_religion_overfit/finding.md` as substrate-domain conflation.

**What was preserved:** the entire substantive content of this finding — the 5-layer architecture (Project shell / Config / Execution / Reading & output / Quality), the Project-as-data-model commitment, the 3-tier triage, the 10 principle-derived features, the MVP roadmap, and the 19 onward routes. All architectural decisions are domain-neutral and remain valid.

**What was edited surgically:** the opening framing sentence; the project-templates list (broadened to include literary, legal, medical, academic, journalism, and AV translation alongside the religious-text presets); references to *"sacred-text translation"* and *"religious-text work"* (generalized); the research-subjects list (broadened to translators across domains, not only theological-translation researchers); the DEFERRED action that read *"when Comprehenslate scope expands beyond Risale-i Nur"* (reframed — scope already covers any document; the action is about expanding the **template library** beyond the initial calibration corpus); the *"Cross-corpus extension to non-Islamic theological corpora"* phrasing.

The finding is otherwise unchanged. The persona-validation re-test verdicts at `devdocs/inquiries/2026-06-16_09-08__loop_diagnose__persona_religion_overfit/finding.md` apply to this finding's MVP-roadmap MUST item "Run user research with 5-10 [translators across domains]" — that re-running is what produces the corrected persona set, not these in-place framing edits.

---

## Question

From `_branch.md`: *"if comprehensate would be a mac app, how would it look?"* with the user enumerating features (BYO API key + model choice, document intake, save-as-PDF/MD, config menu with policy toggles, pause/continue, project selection, percentage progress, reading screen, multi-provider LLM support, no signup/login) and asking *"what other concepts would be needed?"* three times with *"be innovative heavy and logical"* — a design ask that resolves to **architectural sketch + feature inventory + cross-cutting concerns + MVP roadmap**, organized so the answer simultaneously visualizes the system, enumerates features (user-listed + surfaced innovations), respects user exclusions (no signup/login; not webapp), and provides a buildable path forward.

**Goal:** produce a design composite that lets the user (a) see Comprehenslate as a Mac app at a glance, (b) verify completeness against their repeated *"what else?"* prompts, (c) understand which features are MVP-critical vs differentiating vs future, and (d) act on it — either to commission a build or to refine the design further.

---

## Finding Summary

- **Comprehenslate as a Mac app is a native Project-based shell wrapping the existing translation system** (the `schemas.py` 3-layer architecture + the `SKILL.md` 5-step workflow + harmony-layer + translation principles). The Mac app does not redefine the substrate — it provides graphical access, long-running execution with persistence, multi-provider integration, and export.

- **The design is organized as 5 architectural layers.** Project shell (lifecycle + `.compldoc` file format) / Configuration surface (TC + Policy + PC editors) / Execution engine (chunked orchestration + pause/resume + multi-provider) / Reading & output surface (live reading + exports) / Quality & translation-craft surface (terminology + glossary + principle-derived features). Five clusters emerged from coupling analysis across 155 surfaced items; alternatives at 3-layer and 7-layer were tested and rejected on structural grounds.

- **Each layer carries a 3-tier triage that doubles as the MVP roadmap:** ESSENTIAL (MVP-critical or non-negotiable) / DIFFERENTIATING (surfaces Comprehenslate's harmony-layer and translation-principles substrate; the "innovative heavy" surface the user asked for) / DEFERRABLE (nice-to-have, v3+). v1 estimate: 3-9 months single-developer (widened from initial 3-6mo per Critique).

- **Project is the unifying data model.** Each project is one `.compldoc` directory bundle (macOS document-based-app pattern) containing the source document + `TranslationConfig` + per-Policy-class instances + `PipelineConfig` + provider/model + per-chunk state (atomic writes) + outputs + glossary + translation memory + bookmarks + annotations + metadata. The bundle is visible in Finder; user can move, rename, duplicate it.

- **Multi-provider LLM abstraction supports Anthropic + OpenAI + local LLM (Ollama / LM Studio) concurrently at v1** — per the user's *"at once"* framing. The Swift `LLMProvider` protocol is forward-compatible with future providers (Apple Intelligence).

- **The differentiating surface includes ~10 translation-principle-derived UI features** that distinguish Comprehenslate from generic LLM-translation apps: harmony-layer visualization; multi-translation collation; per-chunk lineage view; per-chunk analysis-depth explanation overlay; passage bookmarks (fihrist); idiom-alert inbox; cultural-reference inbox; alternative-renderings per chunk; rhetorical-device detection; escalation-chain detection. (Expanded from 7 to ~10 per Critique's principle-mapping completeness audit.)

- **Cross-cutting concerns are committed in P1 architectural commitments:** privacy (local-first; Keychain-backed API keys; no telemetry by default); performance (streaming chunks; SwiftUI lazy lists; Swift concurrency); accessibility (VoiceOver; Dynamic Type; high-contrast; dark mode); Mac-platform polish (document-based-app; menu bar; system notifications; Spotlight; share extension; keyboard shortcuts).

- **All 7 foundational principles are load-bearing:** FP1 local-first; FP2 BYO credentials (Keychain); FP3 native Mac patterns where they map; FP4 harmony-layer Tier 1-2 preservation as non-negotiable (intrinsic LLM behavior, not user-toggleable); FP5 the `schemas.py` 3-layer architecture as canonical config surface; FP6 the `SKILL.md` 5-step workflow as canonical UX spine; FP7 *"don't declare what the LLM can infer"* — the Mac app's intake doesn't ask the user for source language, chunking strategy, or any LLM-inferable fact. User is asked only for value judgments.

- **All 6 inherited substrate commitments confirmed.** The Mac app design wraps and respects every prior commitment (the schema architecture, the workflow, the harmony layer, the translation-principles identity, the anti-bloat preference, and FP2). One commitment carries a frame revision (the "comprehensation" identity splits into UI-mappable principles and intrinsic LLM-behavior principles).

- **Monetization is out-of-architecture-scope.** A signup-less Mac app's monetization (one-time purchase / Mac App Store / direct download / open-source / donation-ware) requires no UI features beyond an About page; flagged in Open Questions for distribution decision.

---

## Finding

### Why we are even discussing this (small surrounding context)

Comprehenslate is a general-purpose AI-assisted translation system that produces a translation of any source document into a target language. It is currently calibrated against Said Nursi's *Risale-i Nur* and related layered religious-philosophical prose as its initial corpus, but is designed for any document — the calibration corpus is a tuning anchor, not the product's scope (per `SKILL/SKILL.md`). Across this session the project consolidated its substrate: a 3-layer schema architecture in `schemas.py` (`TranslationConfig` with 8 axes + 7 Policy classes + `PipelineConfig` with engine knobs), a 5-step workflow in `SKILL/SKILL.md`, calibration documents (`config_base_source.md`, `policy_config_base_source.md`), and translation-principle documents (`harmony_layer.md`, `translation_principals.md`, `advanced_principles.md`). With the substrate stabilized, the user asked: *"if comprehensate would be a mac app, how would it look?"* — anchoring the inquiry on a specific platform (native Mac, not webapp; no signup) and naming features (BYO API key + model choice; document intake; save-as-PDF/MD; config menu with policy toggles; pause/continue; project selection; chunked progress; reading screen; multi-provider LLM support). The repeated *"what else?"* + *"be innovative heavy and logical"* signaled that the user wanted (a) exhaustive enumeration so they could verify completeness, and (b) features specific to Comprehenslate's harmony-layer and translation-principles substrate that would distinguish it from generic LLM-translation apps.

This finding answers the design ask as a composite — architectural sketch + per-layer feature triage + cross-cutting concerns + MVP roadmap — so a reader can both see the system and pick up its build plan.

### 1. The architectural spine — 5 layers + Project as data model

The Mac app is organized around **5 architectural layers**:

1. **Project shell** — lifecycle, persistence, Finder integration. Manages projects (list / create / open / rename / duplicate / archive). Each project is one `.compldoc` directory bundle.
2. **Configuration surface** — graphical access to the 3-layer schema architecture. TC editor (8 axes); Policy editor (7 Policy classes); PC editor (engine knobs); LLM provider/model picker; two-level provider config (app-default + per-project-override).
3. **Execution engine** — chunked translation orchestration with per-chunk persistence, pause/resume, parallel-mode, background continuation, crash recovery, multi-provider abstraction.
4. **Reading & output surface** — live reading view (translation as it happens); side-by-side source-target alignment; exports (MD / PDF / and more in later versions).
5. **Quality & translation-craft surface** — terminology consistency; glossary; translation memory; harmony-layer visualization; per-chunk lineage view; multi-translation collation; idiom and cultural-reference inboxes; principle-derived UI features.

**Project is the unifying data model.** Each project = one `.compldoc` file (macOS document-based-app package extension). The bundle contains:

- Source document(s)
- `TranslationConfig` instance (the user's TC choices)
- Per-class `Policy` instances (NonMainLangPartsPolicy, SourceApparatusPolicy, VoiceMarkingPolicy, etc.)
- `PipelineConfig` instance (engine knobs)
- Provider/model selection
- Per-chunk translation state (each chunk atomically written as a separate file)
- Outputs (MD / PDF rendered)
- Glossary (SQLite)
- Translation memory (SQLite)
- Bookmarks and annotations
- Project metadata (title, target language, source-language detection, created/modified, word/chunk counts, provider/model used)

The bundle is visible in Finder; the user can move, rename, or duplicate it without going through the app.

**Three-tier triage per layer** — each layer carries ESSENTIAL (MVP-critical or non-negotiable) / DIFFERENTIATING (surfaces Comprehenslate's substrate) / DEFERRABLE (nice-to-have) features. The triage doubles as the MVP roadmap (see §5).

**Cross-cutting concerns** (orthogonal to layers):

| Concern | Implementation |
|---|---|
| Privacy | Local-first; macOS Keychain-backed API key storage; no telemetry by default; opt-in anonymized stats |
| Performance | Streaming chunks (don't load whole book in memory); SwiftUI lazy lists; Swift concurrency for parallel calls; `OperationQueue` for background |
| Accessibility | VoiceOver labels; Dynamic Type support; high-contrast mode; dark mode (native) |
| Mac-platform polish | Document-based-app pattern (`.compldoc`); menu bar; system notifications; Spotlight indexing; share extension; keyboard shortcuts (cmd-T translate; cmd-P pause; cmd-R retry); window restoration; Quick Look extension |

**Foundational principles (FP1-FP7):**

- **FP1.** Local-first by default. iCloud sync is opt-in.
- **FP2.** BYO credentials. App holds no API keys server-side; storage is macOS Keychain.
- **FP3.** Native Mac patterns where they map naturally.
- **FP4.** Harmony-layer Tier 1-2 preservation is non-negotiable — a constant, not a feature toggle. (Intrinsic LLM behavior; UI cannot disable it.)
- **FP5.** The `schemas.py` 3-layer architecture is the canonical configuration surface. UI exposes it; doesn't rewrite or hide it.
- **FP6.** The `SKILL.md` 5-step workflow is the canonical translation workflow. UI wraps it as native UX; doesn't bypass it.
- **FP7.** Don't declare what the LLM can infer. The Mac app's intake doesn't ask the user for source language, chunking strategy, or any LLM-inferable fact. User is asked only for value judgments.

### 2. Per-layer feature triage

The full per-layer feature lists (essential / differentiating / deferrable) are below. The roadmap (§5) ties them to versions.

#### 2.1 Project shell layer

**Essential.** Project list view (welcome screen with all projects + thumbnail + language pair + progress %); new-project wizard (drag source → app auto-detects language → user picks target → empty project); open / rename / duplicate / archive; `.compldoc` directory bundle; project metadata (title; source-language auto-detected + user override; target language; word/chunk counts); last-open quick-resume; workspace folder visible in Finder.

**Differentiating.** Project templates (per-corpus presets that pre-load TC + Policy + PC defaults appropriate to the source — initial set covers literary novel translation, legal/contract translation, medical / clinical translation, academic-paper translation, journalism translation, AV-subtitling translation, MT-post-editing, plus religious-text presets such as Risale-i Nur, Bible, Quran, Tanakh, and Vedic, reflecting the project's calibration corpus); onboarding tutorial (interactive walkthrough with a 200-word sample passage drawn from whatever preset the user selects); project import (from JSON of another tool); recent-files menu.

**Deferrable.** Multi-document projects (a book series as one project); per-project encryption (passphrase-protected `.compldoc`); iCloud sync (opt-in); project archive / sharing.

#### 2.2 Configuration surface layer

**Essential.** TC editor (8 axes as segmented controls or sliders; per-level explanation visible inline from `config_base_source.md`; A4 purpose preset chips for one-click scholarly/devotional/casual/language-learning/performance); Policy editor (7 Policy classes as cards with on/off + value selector); PC editor (chunking_budget; chunking_granularity; chunking_mechanism_override hidden by default; parallel_mode; parallel_batch_size; output_format); LLM provider/model picker (per-provider API key + model picker); app-level Settings (default provider/model) + per-project Settings (override).

**Differentiating.** Inline calibration text (per-level explanations from `config_base_source.md` / `policy_config_base_source.md`); "Why this default" link (opens calibration doc passage); per-policy preview (sample chunk + dropdown for each policy value; shows what each value produces); config preset save/load (named bundles like "My-Nursi-Scholarly"); config-diff comparison view; per-axis tri-state (default / explicitly-set / explicitly-off).

**Deferrable.** Config A/B history; provider failover policy (rule-based); custom prompt templates per project; per-Policy class custom values (advanced).

#### 2.3 Execution engine layer

**Essential.** Chunked orchestration (per `PC.chunking_granularity`); per-chunk persistence (atomic file writes); pause / resume controls; cancel-with-state-preservation; background continuation (translation runs while user does other things; system notification when complete); crash recovery (relaunch picks up from last chunk); **multi-provider abstraction with Anthropic + OpenAI + local LLM (Ollama / LM Studio) at v1** (per user's *"at once"* framing — moved from differentiating to essential per Critique REFINE); rate-limit handling (queue + exponential backoff); per-chunk retry; status indicator (in-progress / paused / completed / failed).

**Differentiating.** Smart cache (hash of source + config → cached output; no LLM call for repeats); cost prediction (pre-translation estimate); cumulative cost display (running total per project + per session); local-LLM auto-discovery (detect Ollama on `localhost:11434`; LM Studio at `localhost:1234`); parallel-mode controls (surfaces `PC.parallel_mode` with terminology-drift warning); token-usage display; per-chunk timing capture.

**Deferrable.** Model A/B compare; provider failover policy; power-aware throttling; per-chunk approval gate; background scheduling; per-provider system-prompt customization.

#### 2.4 Reading & output layer

**Essential.** Live reading view (translation appears chunk-by-chunk; auto-scroll toggleable); side-by-side source-target alignment (paragraph-level; vertical or horizontal split); export to MD (default per `PC.output_format`); export to PDF (with footnotes per A7 scaffolding); bookmark / scroll position persistence.

**Differentiating.** Bilingual side-by-side export; translator-notes export; per-chunk analysis-depth explanation overlay (per `TC.A8`); reading-aloud TTS mode (via macOS `AVSpeechSynthesizer`); heatmap view (chunk-level quality score visualized); search across source + target.

**Deferrable.** Export to HTML, ePub, plain, JSON, LaTeX; BibTeX citation generation; custom output template; print preview / direct print.

#### 2.5 Quality & translation-craft layer

**Essential.** Terminology consistency checker; per-project glossary; issue inbox (flagged chunks).

**Differentiating.** Harmony-layer Tier 1-2 violation flagging; multi-translation collation (Vahide / Akarsu / Comprehenslate side-by-side); per-chunk lineage view (which TC axes + Policy values produced this output — ethical-provenance feature for any high-stakes translation work where reviewers need to audit how the rendering was reached); idiom-alert inbox; cultural-reference inbox; passage bookmarks; embedded-language detection visualization; honorific consistency tracking; glossary suggestion (LLM-suggested terms to pin).

**Deferrable.** Translation memory (TM); cross-project TM; cross-section drift detector; diff view; per-chunk approve/reject/edit workflow; quality dashboard per project; reverse-translation drift check.

### 3. The ~10 translation-principle-derived differentiating features (the "innovative heavy" surface)

These are the features that distinguish Comprehenslate from generic LLM-translation apps because they surface the project's unique substrate (`harmony_layer.md`, `translation_principals.md`, `advanced_principles.md`, `notes.md`). Expanded from 7 to ~10 per Critique's principle-mapping completeness audit.

| # | Feature | Principle of origin | Layer | UX description |
|---|---|---|---|---|
| 1 | Harmony-layer visualization | Tier 1-2 preservation (`harmony_layer.md`) | Quality | Interactive map of Tier 1-4 markers per chunk; click a marker → see which harmony pattern is preserved or lost |
| 2 | Multi-translation collation | Multi-meaning preservation; collective interpretation | Quality | Side-by-side: Vahide / Akarsu / Comprehenslate (and any other priors imported) for the same passage |
| 3 | Per-chunk lineage view | Nazm preservation (word order as meaning) | Quality | Click any chunk → see which TC axes + Policy values produced this output; the ethical-provenance audit feature |
| 4 | Per-chunk analysis-depth explanation overlay | Layered meaning (sarahat / işaret / remiz / îma / telvih / telmih) | Reading | Toggle "explain this chunk" → shows layered-meaning analysis at depth set by `TC.A8` |
| 5 | Passage bookmarks (fihrist) | Micro-to-macro mirroring (*insan as fihrist*) | Reading | Mark passages as fihrist anchors → indexed view shows how each mirrors the whole document's themes |
| 6 | Idiom-alert inbox | Idiom recognition (`TC.A1.c`) | Quality | Inbox of source idioms without clean target equivalent; per-item: source + LLM rendering + alternatives |
| 7 | Cultural-reference inbox | Cultural reference recognition (`TC.A1.e` + A3) | Quality | Inbox of allusions; per-item: source + cultural context + rendering options per A3 source_culture |
| 8 | **Alternative-renderings per chunk** *(added per Critique)* | *"All meanings derived from a text are valid... choosing a meaning is up to the user"* | Quality | Each chunk shows 1-3 LLM-identified valid renderings; user picks |
| 9 | **Rhetorical-device detection** *(added per Critique)* | *"Rhetoric is a fundamental carrier of meaning"* (belagat) | Quality | Per-chunk rhetorical-device markers (chiasmus / antimetabole / alliteration); click → see device type + what's preserved |
| 10 | **Escalation-chain detection** *(added per Critique)* | Small-cycle-proves-large-cycle (`advanced_principles.md`) | Quality | Chain markers across chunks; *"this passage uses escalation; pattern and final claim non-negotiable; small examples can adapt"* |

Three further candidates (self-illuminating passage flagging; grammatical-anomaly-as-deliberate alerts; meaningful-omission flagging) are noted in Open Questions for potential addition when the surface stabilizes.

### 4. Cross-cutting concerns

Restated for clarity (these appear at the architectural-spine level, not per-layer):

**Privacy.** All project data lives on the user's disk by default. API keys are stored in macOS Keychain. No telemetry by default; optional opt-in anonymized usage stats. Per-project encryption (deferred to v3+) for sensitive work where the source itself is confidential — legal discovery material, medical records, pre-publication manuscripts, religiously-sensitive content, or any other corpus the user wants protected at rest.

**Performance.** Streaming chunks rather than full-book loading. SwiftUI lazy lists for long translation views. Swift concurrency for parallel LLM calls. `OperationQueue` for background work. Per-chunk timing capture to debug slow models.

**Accessibility.** VoiceOver labels on every UI element. Dynamic Type support. High-contrast mode. Native dark mode.

**Mac-platform polish.** Document-based-app pattern as the foundational interaction model. Menu bar (File / Edit / View / Translate / Window / Help). System notifications (translation complete, chunk failed, quota approaching). Spotlight indexing of project metadata. Share extension (right-click any text file in Finder → "Translate with Comprehenslate"). Keyboard shortcuts (cmd-T, cmd-P, cmd-R, etc.). Window restoration. Quick Look extension for previewing `.compldoc` files in Finder.

### 5. MVP roadmap

**v1 (MVP) — Essential per layer + multi-provider with 3 providers. ~3-9 months single-developer.** *(Estimate widened from initial 3-6mo per Critique REFINE based on aggregate effort across layers; experienced single dev should hit closer to 3-6mo, less experienced 6-9mo.)*

- Architectural commitments (5-layer + Project + `.compldoc` + cross-cutting baseline + FP1-FP7)
- Project shell essential
- Configuration surface essential
- Execution engine essential **with 3 providers (Anthropic + OpenAI + local LLM via Ollama / LM Studio)** at v1 per user's *"at once"* framing
- Reading & output essential (MD + PDF export)
- Quality & translation-craft essential (terminology consistency + glossary + issue inbox)
- Cross-cutting baseline (privacy / performance / basic accessibility / document-based-app / menu bar / system notifications)

**v2 — Differentiating tier per layer + the 10 principle-derived UI features + extended exports.**

- Project templates (Nursi / Bible / Quran / Tanakh / Vedic presets); onboarding tutorial; recent files; project import
- Inline calibration text; "why this default" links; per-policy preview; config presets; config-diff view; tri-state axes
- Smart cache; cost prediction; cumulative cost display; **local-LLM auto-discovery (UX polish)** (basic local-LLM support shipped v1); parallel-mode controls; token-usage display
- Bilingual export; translator notes; analysis-depth overlay; TTS reading mode; heatmap view; search
- All 10 principle-derived features (harmony viz; multi-translation collation; per-chunk lineage; analysis-depth overlay; fihrist bookmarks; idiom inbox; cultural inbox; alternative-renderings; rhetorical-device detection; escalation-chain detection)
- Spotlight integration; share extension; full keyboard shortcuts; full accessibility; English UI + Arabic UI (RTL pipeline proof)

**v3+ — Deferrable tier + power-user surfaces.**

- Multi-document projects; per-project encryption; iCloud sync (opt-in); project sharing
- Config A/B history; provider failover; custom prompts; advanced policy custom values
- Model A/B compare; per-chunk approval gate; scheduling; power throttling; custom system prompts
- HTML / ePub / plain / JSON / LaTeX / BibTeX exports; custom templates; print
- TM; cross-project TM; cross-section drift; diff view; review/edit workflow; quality dashboard; reverse-drift check
- Scripting (AppleScript / Shortcuts); plugin system; Continuity; Touch Bar
- Additional principle-derived features (self-illuminating passage flagging; grammatical-anomaly alerts; meaningful-omission flagging)
- Localization beyond English + Arabic (French / Turkish / Persian / Bahasa / German)

**Cross-version dependencies:**

- Harmony visualization (v2) depends on harmony-layer engine support functional in v1.
- Smart cache (v2) depends on per-chunk persistence (v1).
- Multi-document projects (v3) depend on cross-project TM design — coupled with TM (v3).

---

## Inherited Commitments Re-test

The Synthesis Trigger in `_branch.md` named 6 substrate priors. Each prior's load-bearing commitments are re-tested below.

| Commitment | Re-test status | Structural evidence (which UI feature embodies the commitment) |
|---|---|---|
| 3-layer schema architecture (TC + Policy + PC) from `schemas.py` | **RE-TESTED — commitment confirmed** | Configuration surface layer directly exposes the 3 schemas as 3 sub-screens (TC editor + Policy editor + PC editor). Architecture unchanged; UI design respects it. |
| `SKILL.md` 5-step workflow | **RE-TESTED — commitment confirmed** | Mac UX flow maps the 5 steps to native UI (project list → new-project wizard combining steps 1+2 → language picker → config editor → translation execution → output). Direct alignment. |
| Harmony-layer Tier 1-2 preservation as non-negotiable (`harmony_layer.md`) | **RE-TESTED — commitment confirmed** | Quality layer (v2 differentiating) surfaces Tier 1-2 violation flagging as a USER-VISIBLE feature; the actual preservation behavior is INTRINSIC LLM behavior the UI cannot toggle off. The flagging is visualization; the preservation is constant. |
| Translation principles' "comprehensation" identity (`translation_principals.md` + `advanced_principles.md` + `notes.md`) | **RE-TESTED — commitment confirmed but frame revised** | The principles split into UI-mappable (10 features in §3 of the finding — was 7, expanded per Critique) and intrinsic-LLM-behavior (ihlas; collective interpretation; sünuhat; etc. — these remain LLM behaviors, not user controls). The identity is preserved across both surfaces. |
| Anti-bloat principle (recurring across this session) | **RE-TESTED — commitment confirmed** | 5-layer architecture + 3-tier triage IS the anti-bloat discipline. MVP (v1) = essential only; v2 adds differentiating; v3+ adds deferrable. Nothing in v1 that isn't load-bearing. The catalog is large but tiered. |
| FP2 (= FP7 here) — *"Don't declare what the LLM can infer"* (from prior `schemas_rationale_and_policy_list` finding) | **RE-TESTED — commitment confirmed and extended** | The Mac app's intake (new-project wizard + config) doesn't ask for source language (auto-detected by LLM); doesn't ask for chunking strategy (LLM-handled per PC defaults); user is asked only for value judgments (target language; TC axes; Policy values). Principle enforced in UI design. |

---

## Next Actions

### MUST

- **Design the `.compldoc` file format spec.**
  - **Who:** developer / project lead.
  - **Gate:** condition-bound — before v1 implementation begins.
  - **Why:** every architectural layer depends on `.compldoc` structure; without this spec, all 5 layers stall. Per-chunk file naming + atomicity rules + config JSON schema + glossary/TM SQLite schema all need definition.

- **Implement the `LLMProvider` Swift protocol + adapters for Anthropic + OpenAI + Ollama / LM Studio (local).**
  - **Who:** developer.
  - **Gate:** condition-bound — before Execution engine implementation.
  - **Why:** PC4 essential tier requires multi-provider abstraction; user's *"at once"* framing makes 3 providers a v1 commitment per Critique REFINE. Protocol must accommodate future Apple Intelligence as a fourth adapter.

- **Produce UI/UX mockups for the 5 architectural layers.**
  - **Who:** designer (or developer with design hat).
  - **Gate:** condition-bound — before v1 code implementation.
  - **Why:** the finding deferred UI mockups to a follow-up; validating the architectural decisions visually before code reduces rework. Validate against Apple Human Interface Guidelines; test with 3-5 sample users spanning the product's applicability scope (e.g., a literary translator, a legal/medical translator, an academic translator, and one religious-text translator from the calibration corpus).

- **Run a cost-validation pass.**
  - **Who:** developer / business owner.
  - **Gate:** condition-bound — before public launch / monetization commitment.
  - **Why:** for each provider × model, compute estimated tokens × per-token cost × full-Risale-i-Nur-corpus size; report cost ranges; validate that the cost model is realistic for the target user. Informs monetization decision (COULD below).

- **Build v1 MVP per the §5 roadmap.**
  - **Who:** developer.
  - **Gate:** condition-bound — after the four MUST actions above are complete.
  - **Why:** the primary onward action; the Mac app's existence presupposes v1 implementation. Estimated 3-9 months single-developer.

### COULD

- **Document the FP2 LLM-inferable test predicate in the codebase as an architectural-decision-record (ADR).**
  - **Who:** developer.
  - **Gate:** condition-bound — when v1 schema fields are being added.
  - **Why:** prevents future schema additions that violate FP2. Cross-references the prior `schemas_rationale_and_policy_list` finding's documentation.

- **Pick monetization model + distribution channel.**
  - **Who:** business owner / project lead.
  - **Gate:** condition-bound — before public launch.
  - **Why:** required pre-launch; no UI surface impact regardless of choice (no signup/login).
  - **Depends-on:** MUST item *"Run a cost-validation pass."* GATED — set monetization after cost ranges are known.

- **Run user research with 5-10 translators spanning Comprehenslate's documented applicability scope** — at minimum 1-2 from the calibration corpus (religious-text translators) plus translators from literary, legal/contract, medical, academic-paper, journalism, and AV-subtitling domains. (Per the persona-validation diagnostic at `devdocs/inquiries/2026-06-16_09-08__loop_diagnose__persona_religion_overfit/finding.md`, the prior recommendation of "theological-translation researchers" was substrate-domain-conflated and undercovered the product's applicability scope.)**
  - **Who:** developer with research hat / designer.
  - **Gate:** condition-bound — in parallel with UI mockups (MUST).
  - **Why:** validates persona assumptions; surfaces unstated needs; reduces v1 risk.

### DEFERRED

- **Build v2 (differentiating tier + ~10 principle-derived features + extended exports).**
  - **Gate:** condition-bound — after v1 ships.
  - **Why if revived:** unlocks the "innovative heavy" surface that distinguishes Comprehenslate from generic LLM-translation tools.

- **Build v3+ (deferrable tier + power-user surfaces).**
  - **Gate:** condition-bound — after v2 ships + specific user demand for individual deferrable features.
  - **Why if revived:** completes the catalog for power users and scholarly workflows.

- **Expand the project-template library beyond the initial calibration corpus.** Currently the differentiating-tier template list already covers literary, legal/contract, medical, academic-paper, journalism, AV-subtitling, MT-post-editing, plus the religious-text presets that match the calibration corpus (Risale-i Nur, Bible, Quran, Tanakh, Vedic); this deferred work adds templates for less-common domains as evidence of user need accumulates (patent translation, pharmaceutical regulatory, software localization, game localization, specific historical-document periods, Pali Buddhist, Christian patristic, etc.).
  - **Gate:** condition-bound — observed user demand for the specific template OR research evidence that a particular domain's calibration significantly diverges from existing presets.
  - **Why if revived:** continues the template-library buildout; the per-template work is bounded (one TC + Policy + PC default set per template, plus a sample passage).

- **Implement `schemas.py`-aware migration tooling.**
  - **Gate:** observable — when `schemas.py` schema change is committed.
  - **Why if revived:** prevents silent breakage when schemas evolve; necessary for long-lived projects.

- **Mobile / iPad expansion decision (Catalyst port vs native iPad app).**
  - **Gate:** condition-bound — when v2 ships and project bundles are stable enough to be device-portable.

- **App UI localization beyond English** (Arabic at v2; French / Turkish / Persian / Bahasa / German at v3+).
  - **Gate:** observable — market demand from non-English-speaking translators.

- **Plugin / scripting API.**
  - **Gate:** observable — 3+ users requesting extensibility.

- **Apply the architectural pattern to other Comprehenslate products** (hypothetical Comprehenslate-Web or Comprehenslate-Mobile — the AE1 emergent).
  - **Gate:** condition-bound — when multi-platform expansion is on the roadmap (post-v2).

- **Add a user-visible roadmap surface** (the AE2 emergent — show users the 3-tier triage as an in-app roadmap page).
  - **Gate:** observable — 3+ users asking "when will X feature ship?"

- **Policy-class co-application precedence UX.**
  - **Gate:** observable — user confusion observed when co-applying policies (e.g., Bismillah governed by both `FormulaicOpeningPolicy` AND `NonMainLangPartsPolicy`).
  - **Why if revived:** prevents user confusion; inherited Open Question from the prior `chunk_types_vs_mechanisms` inquiry.

---

## Reasoning

The structurally non-obvious decisions had alternatives that were considered and rejected. The rejections show why the deliverable lands where it does.

**Why 5 layers and not 3 or 7.** A 3-layer architecture (UI / business logic / data) loses the granularity needed to separate Configuration from Execution from Quality cleanly. A 7-layer architecture over-decomposes — splitting Quality into 4-5 sub-modules (glossary; TM; harmony viz; collation; lineage) creates sibling sub-modules that share UI surface and data dependencies; their natural place is sub-modules of one Quality layer. 5 layers is structurally motivated by the natural coupling clusters in surfacing's 155 items: Project (lifecycle); Config (settings); Execution (runtime); Reading-output (consumption); Quality (craft). Each cluster has distinct lifecycle and high internal coupling.

**Why Project (and not Workspace or Task) is the data model.** *Workspace* implies a single global state where multiple translations coexist; the user explicitly named *"project selection logic"* — committing to projects-as-units. *Task* is too granular (a project has many translation tasks). Project at the document-bundle level matches the macOS document-based-app pattern; it's the natural unit for "save percentage progress" (a project is X% done) and "pause/resume" (you pause a project, not a task).

**Why selective principle-to-UI mapping (not uniform mapping).** Some translation principles are intrinsic LLM behavior — the LLM applies them while translating; the user doesn't toggle them (ihlas-driven quality; collective interpretation rationale; sünuhat-style two-step processing; self-illuminating detection at the LLM-behavior level). Forcing UI features for these would be meaningless. Only principles producing USER DECISIONS or USER-VISIBLE STRUCTURE deserve UI features. The 10 features in §3 of the finding pass this test.

**Why local LLM is v1 essential and not v2 differentiating.** Initial Innovation placed local LLM in v2 (after Anthropic + OpenAI v1). Critique surfaced a user-pushback-fidelity violation: the user explicitly said *"it shoudl ssupport local llm models openai and antropic models at once."* "At once" implies concurrent v1 support. Pushing local to v2 contradicts the user's explicit framing. Moved to v1 essential per the REFINE.

**Why the principle-derived feature count expanded from 7 to ~10.** Innovation surfaced 7 features. Critique audited `references/core/` principles against UI-mappability and surfaced 3-6 additional UI-mappable principles missed: alternative-renderings per chunk (multi-meaning at chunk level — distinct from multi-translator collation); rhetorical-device detection (belagat-specific); escalation-chain detection (from `advanced_principles.md`). Optionally: self-illuminating passage flagging; grammatical-anomaly alerts; meaningful-omission flagging. Expanded to 10 with the three optional listed as Open Questions.

**Why MVP estimate widened from 3-6mo to 3-9mo.** Initial Innovation gave 3-6 months single-developer. Critique aggregated effort estimates per layer: P1 design (~2 weeks) + P2 essential (~3 weeks) + P3 essential (~4 weeks) + P4 essential (~10 weeks for Execution including multi-provider) + P5 essential (~3 weeks) + P6 essential (~2 weeks) + cross-cutting (~3 weeks) ≈ 27 weeks ≈ 6 months tight for experienced developer; 9 months realistic for less experienced. Widened to 3-9mo to honestly reflect skill variance.

**Why monetization is out-of-architecture-scope.** A signup-less Mac app's monetization options (Mac App Store one-time purchase; direct download with paid license; open-source; donation-ware) require no UI features beyond an About page. Monetization is a distribution decision for later; the architecture is the same regardless of which monetization path is chosen.

**Why UI/UX mockups are a MUST but the finding doesn't contain them.** The articulate_simple MQA reconciled deliverable-grain × intent into the composite (architecture + feature inventory + cross-cutting + roadmap). UI mockups are a separate grain (visual / interaction design) better suited to a follow-up design pass after architectural commitments are agreed. Producing mockups inside this finding would dilute the architectural focus.

**Why 7 foundational principles and not fewer.** Per-FP load-bearing test: removing any of FP1-FP7 would allow an incorrect design choice (FP1 removed → cloud-first OK; FP2 removed → server-side credentials OK; FP3 removed → web-app-like patterns OK; FP4 removed → harmony toggleable; FP5 removed → schemas rewritten; FP6 removed → workflow bypassed; FP7 removed → user asked for LLM-inferable facts). All 7 are load-bearing.

---

## Open Questions

### Monitoring

- **Provider landscape evolution.** Track Apple Intelligence as a future provider (potential native macOS LLM); local LLM capability growth (Llama / DeepSeek / Mistral updates); rare-language LLM detection reliability.
- **Mac-platform API evolution.** SwiftUI document-based-app APIs; Swift concurrency primitives; Keychain APIs — monitor for deprecations.

### Blocked

None — design is complete.

### Research Frontiers

- **Cross-corpus calibration extension beyond the initial calibration corpus.** Same frontier flag as the prior `chunk_types_vs_mechanisms` inquiry. Adds corpus-specific (or genre-specific) project templates + Policy defaults + cultural-reference inbox calibration — covers other religious traditions (Tanakh / Bible / Vedic / Pali Buddhist / Christian patristic) and also non-religious domains (literary periods, legal sub-genres, medical sub-specialties, etc.) as the project's calibration broadens.
- **LLM-inferability decay at rare/dead languages** (Aramaic; Coptic; Sumerian; Akkadian; Ge'ez). May require Config-surface accommodations (e.g., a fallback "declare source language" toggle when LLM detection is unreliable).
- **Additional principle-derived features** (self-illuminating passage flagging; grammatical-anomaly-as-deliberate alerts; meaningful-omission flagging). These were classified as intrinsic-or-borderline at Sensemaking + Critique; could be promoted to UI-mappable in a future inquiry if user decisions emerge.

### Refinement Triggers

- **Monetization model decision.** OUT-of-architecture-scope. Trigger: when ready to ship v1. Options: Mac App Store one-time purchase; direct download with paid license; open-source; donation-ware. No UI surface impact regardless.
- **Mobile / iPad expansion.** Trigger: when v2 ships and project bundles are device-portable. Options: Mac Catalyst port (auto-port the SwiftUI app); separate native iPad app (touch-optimal).
- **App UI localization beyond English + Arabic.** English-only at v1; Arabic at v2 as RTL pipeline proof. Trigger to expand to French / Turkish / Persian: market demand from non-English-speaking translators.
- **Plugin / scripting API.** Power-user feature; deferred. Trigger: 3+ users requesting extensibility.
- **`schemas.py`-aware migration tooling.** Trigger: when `schemas.py` schema change is committed.
- **User-visible roadmap surface** (AE2). Trigger: 3+ users asking "when will X feature ship?"
- **Architectural pattern extension to other Comprehenslate products** (AE1). Trigger: when multi-platform expansion is on the roadmap.
- **Policy-class co-application precedence UX.** Trigger: user confusion observed when co-applying policies in practice.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
/traverse

if comprehensate would be a mac app, how woudl it look?

it should have a field of adding user's own  api key and choosig model additionally i guess. and also document intake process should be done too. what other concepts would be needed?
saving output as pdf or md file too needed.  we would need a config menu where we can select or deselect all configs,  enable or disbale policies. 

what else . what other things would be needed?

i guess since we aim to be able translate long books we would also need conitnue and pause translation? this also means we should have a project selection logic. and we shoudl be able to save trasnlation process somewhere (since it is in chunks) and map it as percentage. and also some reading screen so user can see as translation goes on and he can read. 
it shoudl ssupport local llm models openai and antropic models at once. 
  what else . what other things would be needed?  be innovative heavy and logical 

there is not need for signup or login i think. it not a webapp after all.
```

</details>
