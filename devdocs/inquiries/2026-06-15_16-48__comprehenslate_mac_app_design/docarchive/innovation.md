# Innovation — comprehenslate_mac_app_design

## User Input

```text
/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/_branch.md

Upstream outputs in same folder: articulate_simple.md + surfacing.md + sensemaking.md + decomposition.md. Production-task mode — the decomposition's 10 pieces (P1-P10) are the seed structure; Innovation generates concrete content per piece:

[... 10 pieces P1-P10 listed; meta-decision pieces flagged: P1, P7, P8, P9 ...]

Save innovation output to: /Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/innovation.md
```

---

## Seed + Methodology-Mode Consideration

### Seed

The 10-piece decomposition from upstream (P1-P10) as a Production-task seed.

### Inherited methodology mode

**Standard default** (4G+3F balanced). Text signal: "Innovation generates concrete content per piece" + "be innovative heavy and logical" — no explicit contrarian / generator-weighted / depth-iteration signals.

### Alternative mode named

**Generator-weighted exploration** — would emphasize many varied features per layer with less framing rigor.

### What follows under the alternative

If Generator-weighted: per-layer feature lists would be denser (more items per tier) but with less filtering and less Inversion-testing. Candidate space becomes harder to triage downstream.

### Decision

**Default — Standard default.** Reason: Sensemaking SV6 already produced the structural substrate (5 layers + 3-tier triage); Innovation's job is to populate it with concrete, well-tested content. Balanced 4G+3F suits this. Generator-weighted would over-produce in volume but under-test for principle-conformance.

---

## Meta-Decision-Piece Classification

| Piece | Properties firing | Classification |
|---|---|---|
| P1 — Architectural commitments | (b) framing-semantic + (c) lesson-vocabulary (5-layer; Project-as-data-model; 3-tier triage; FP1-FP7) | **META-DECISION** |
| P2 — Project shell features | content-production within P1 frame | content-production |
| P3 — Configuration surface features | content-production within P1 frame | content-production |
| P4 — Execution engine features | content-production within P1 frame | content-production |
| P5 — Reading & output features | content-production within P1 frame | content-production |
| P6 — Quality & translation-craft features | content-production within P1 frame | content-production |
| P7 — 7 principle-derived features | (b) framing-semantic (selective-mapping commitment) | **META-DECISION** |
| P8 — MVP roadmap | (e) intervention-shape commitment (ADD-CONTENT roadmap) | **META-DECISION (property v)** |
| P9 — Inherited Re-test | (a) relationship-label commitment (RE-TESTED verdicts) | **META-DECISION** |
| P10 — Open Questions | content-production residuals | content-production |

P1, P7, P8, P9 require piece-level Inversion-candidates. P8's Inversion targets the intervention-shape axis.

---

## P1 — Architectural Commitments

### Principal Candidate (PC1)

#### Foundational Principles (FP1-FP7)

- **FP1.** Local-first by default. All project data on user's disk; iCloud sync is opt-in.
- **FP2.** BYO credentials. App holds no API keys server-side; storage is macOS Keychain.
- **FP3.** Native Mac patterns where they map naturally — document-based-app; menu bar; Keychain; system notifications; SwiftUI/AppKit conventions.
- **FP4.** Harmony-layer Tier 1-2 preservation is non-negotiable regardless of user config. A constant, not a feature toggle.
- **FP5.** The `schemas.py` 3-layer architecture (TC + Policy + PC) is the canonical configuration surface. UI exposes it; doesn't rewrite or hide it.
- **FP6.** The `SKILL.md` 5-step workflow is the canonical translation workflow. UI wraps it as native UX; doesn't bypass it.
- **FP7.** Don't declare what the LLM can infer (the principle from the schemas inquiry). The Mac app's intake doesn't ask the user for source language, chunking strategy, or any LLM-inferable fact.

#### Primary Data Model: Project

- Each **Project = one `.compldoc` directory bundle file** (macOS package extension).
- **Contents:** source documents + `TranslationConfig` instance + per-class Policy instances + `PipelineConfig` + provider/model + per-chunk state (each chunk as separate file) + outputs (MD/PDF) + glossary (SQLite) + translation memory (SQLite) + bookmarks + annotations + project metadata (title, target language, source-language detection, created/modified dates, word/chunk counts).
- **Atomically written per-chunk** — pause/resume + crash recovery resume from disk.
- **Visible in Finder** — user can move, rename, duplicate the bundle directly; Quick Look shows project summary.
- **Lifecycle operations:** list / create / open / rename / duplicate / archive.

#### 5-layer architecture spine

1. **Project shell** — lifecycle, persistence, Finder integration, project list view, new-project wizard.
2. **Configuration surface** — TC editor + Policy editor + PC editor + provider/model + Keychain; two-level config (app default + per-project override).
3. **Execution engine** — chunked orchestration, per-chunk persistence, pause/resume, multi-provider abstraction, crash recovery.
4. **Reading & output surface** — live reading, side-by-side alignment, exports.
5. **Quality & translation-craft surface** — terminology, glossary, harmony viz, lineage, multi-translation collation, principle-derived features.

#### 3-tier triage mechanism

- **ESSENTIAL** = MVP-critical or non-negotiable for v1 ship.
- **DIFFERENTIATING** = unique-to-Comprehenslate; surfaces the harmony-layer / translation-principles substrate.
- **DEFERRABLE** = nice-to-have; v3+ scope.

#### Cross-cutting concerns (orthogonal to layers)

| Concern | Implementation |
|---|---|
| Privacy | Local-first; Keychain-backed API key storage; no telemetry by default; opt-in anonymized stats |
| Performance | Streaming chunks (don't load whole book in memory); SwiftUI lazy lists for long translations; Swift concurrency for parallel calls; `OperationQueue` for background work |
| Accessibility | VoiceOver labels per UI element; Dynamic Type support; high-contrast mode; dark mode (native) |
| Mac-platform polish | Document-based-app (`.compldoc` as native file type); menu bar (File / Edit / View / Translate / Window / Help); system notifications; Spotlight indexing; share extension; keyboard shortcuts (cmd-T translate; cmd-P pause; cmd-R retry); window restoration; Quick Look extension |

#### Mechanism trace

Combination (FPs + data model + architecture + triage + cross-cutting) + Absence Recognition redesign-level (what would be missing if designed from scratch? answer: a unifying data-model abstraction → Project) + Inversion (PI1 below) + Domain Transfer (document-based-app pattern from macOS native UI traditions like Pages, Xcode, Final Cut Pro).

### Piece-level Inversion Candidate (PI1)

**Assumption reversed:** "5 layers + Project as primary data model + 3-tier triage" is the right architecture.

**Alternative:** "Single-flow, no-layer, no-Project, no-tier-triage architecture — just one big translation pipeline with all features available always."

**What follows:** simpler conceptual model; one app, one source document loaded, translate. No project juggling. No essential-vs-differentiating tiers. Everything in v1.

**5-test on PI1:**
- Novelty: medium (matches simple translation apps; DeepL desktop)
- Scrutiny survival: **WEAK** — fails for long-book translation (no pause/resume per project); fails for multi-document work; fails MVP feasibility (everything in v1 is too much scope); contradicts user-named "project selection logic."
- Fertility: low
- Actionability: medium-low (would require rewriting the whole architecture)
- Mechanism independence: only Inversion
- **Verdict: REJECTED.**

### 5-test on PC1

- Novelty: HIGH — the 5-layer + Project + triage triad is novel for theological-translation tools.
- Scrutiny survival: STRONG — multiple Sensemaking perspectives confirmed; Frame-exit tested 3-layer + 7-layer counters.
- Fertility: HIGH — generates per-layer pieces + roadmap + principle-derived cluster.
- Actionability: HIGH — implementable on macOS with native SwiftUI + document-based-app APIs.
- Mechanism independence: convergence from Combination + Absence Recognition + Domain Transfer + Inversion-as-rejected-test.
- **Verdict: ACTIONABLE.**

---

## P2 — Project Shell Layer Feature Triage

### Principal Candidate (PC2)

#### Essential

- **Project list view** — welcome screen showing all projects sorted by last-opened; thumbnail + title + language pair + progress %.
- **New-project wizard** — combines SKILL.md steps 1+2: drag source file → app auto-detects source language → user picks target language → empty project created.
- **Open / Rename / Duplicate / Archive** — standard Mac operations.
- **`.compldoc` bundle on disk** — user can move/rename in Finder; bundle is portable.
- **Project metadata** — title; source-language (LLM-inferred per FP7 + user override); target language; created/modified date; word/chunk counts; provider/model used.
- **Last-open quick-resume** — relaunch opens the last project (system standard).
- **Project workspace folder visible in Finder** — user can inspect raw chunks + config files.

#### Differentiating

- **Project templates** — corpus presets pre-load TC + Policy + PC defaults: Nursi preset; Bible preset; Quran preset; Tanakh preset; Vedic preset; etc.
- **Onboarding tutorial** — interactive walkthrough with a 200-word Nursi sample chunk; user sees TC effects on translation in real time.
- **Project import** — from JSON export of another translation tool; from a previous Comprehenslate version's format.
- **Recent files menu** — system standard.

#### Deferrable

- **Multi-document projects** — translate a book series as one project; cross-volume glossary; cross-volume TM.
- **Per-project encryption** — passphrase-protected `.compldoc` for sensitive religious-text work.
- **iCloud sync** — opt-in; respects local-first default.
- **Project archive / sharing** — compressed export; collaborator delivery.

**Mechanism trace:** Combination (user-named features + Mac document-app patterns) + Absence Recognition (project templates as onboarding accelerator) + Domain Transfer (Pages / Final Cut Pro / Xcode project models).

**5-test PC2:** Novelty medium-high; Scrutiny STRONG; Fertility HIGH (templates extend cross-corpus); Actionability HIGH; Mechanism independence (3+ converge). **ACTIONABLE.**

---

## P3 — Configuration Surface Layer Feature Triage

### Principal Candidate (PC3)

#### Essential

- **TC editor** — 8 axes shown as segmented controls or sliders; per-level explanation visible inline (from `config_base_source.md`); A4 purpose preset chips (one-click scholarly / devotional / casual / language-learning / performance).
- **Policy editor** — 7 Policy classes shown as cards; per-class on/off toggle + value selector (segmented control or dropdown).
- **PC editor** — `chunking_budget` (number); `chunking_granularity` (segmented); `chunking_mechanism_override` (advanced; hidden by default); `parallel_mode` (segmented); `parallel_batch_size` (number); `output_format` (segmented).
- **LLM provider/model picker** — per-provider API key field (Keychain-backed); per-provider model picker (Anthropic: opus/sonnet/haiku; OpenAI: gpt-4/5; Local: detected Ollama/LM Studio models).
- **App-level Settings** for default provider/model + **per-project Settings** for override.

#### Differentiating

- **Inline calibration text** — per-level explanation from `config_base_source.md` / `policy_config_base_source.md`, expandable disclosure triangle.
- **"Why this default" link** — opens the calibration doc passage in a side panel.
- **Per-policy preview** — sample chunk + dropdown for each policy value; show what each value produces on the sample, side-by-side.
- **Config preset save/load** — named bundles ("My-Nursi-Scholarly"; "Casual-Russian"); per-corpus templates can be saved + reused.
- **Config-diff comparison view** — compare two configs side-by-side; highlight differences.
- **Per-axis tri-state** — default / explicitly-set / explicitly-off (per user's "select/deselect" framing).

#### Deferrable

- Config A/B history (track which configs produced which outputs).
- Provider failover policy (Anthropic rate-limit → fall back to OpenAI; rule-based).
- Custom prompt templates per project (advanced).
- Per-Policy custom values (user-supplied literals beyond the schema enum — advanced).

**Mechanism trace:** Combination (schemas + calibration docs as UI substrate) + Lens Shifting (config as a teaching surface; preview-driven learning) + Absence Recognition (per-policy preview missing in standard LLM apps).

**5-test PC3: ACTIONABLE.**

---

## P4 — Execution Engine Layer Feature Triage

### Principal Candidate (PC4)

#### Essential

- **Chunked orchestration** — per `PC.chunking_granularity`; AI handles boundary detection per the hidden hybrid mechanism.
- **Per-chunk persistence** — each chunk atomically written as a file in the project bundle; resume-from-disk pattern.
- **Pause / Resume controls** — global per project.
- **Cancel-with-state-preservation** — stopping doesn't lose completed chunks.
- **Background continuation** — translation runs in a background queue; user can browse other windows; system notification on completion.
- **Crash recovery** — relaunch picks up from last persisted chunk.
- **Multi-provider abstraction** — Swift protocol with concrete adapters per provider.
- **Rate-limit handling** — request queue + exponential backoff.
- **Per-chunk retry** — on transient failure.
- **Status indicator** — in progress / paused / completed / failed per project.

#### Differentiating

- **Smart cache** — hash(source + config) → cached output; instant retrieval; no LLM call for repeats (huge cost savings on iterative work).
- **Cost prediction** — pre-translation estimate based on document size + TC config + model price; shown before user starts the translation.
- **Cumulative cost display** — running total per project + per session.
- **Local-LLM auto-discovery** — detect Ollama on `localhost:11434`; LM Studio at `localhost:1234`; auto-populate provider picker.
- **Parallel-mode controls** — surfaces `PC.parallel_mode` (off / intra-chapter / full); warns user about terminology-drift risk in "full" mode.
- **Token-usage display** — per chunk + cumulative.
- **Per-chunk timing capture** — helps debug slow models; populates a stats view.

#### Deferrable

- Model A/B compare (run same chunk through 2 models; compare side-by-side).
- Provider failover policy (rule-based or manual override).
- Power-aware throttling (slow on battery; full on AC).
- Per-chunk approval gate (manual review before commit; opt-in per project for scholarly workflow).
- Background scheduling (run overnight; specific time window).
- Per-provider system-prompt customization.

**Mechanism trace:** Combination + Constraint Manipulation (ADD: cost prediction as new constraint; REMOVE: implicit sequential constraint via parallel_mode) + Extrapolation (cost prediction extends as LLM-prices stabilize across providers).

**5-test PC4: ACTIONABLE.**

---

## P5 — Reading & Output Layer Feature Triage

### Principal Candidate (PC5)

#### Essential

- **Live reading view** — translation appears chunk-by-chunk as produced; auto-scroll to the latest chunk (toggleable).
- **Side-by-side source-target alignment** — paragraph-level; toggle between vertical-split and horizontal-split layout.
- **Export to MD** — default per `PC.output_format = "md"`; respects A7 scaffolding (markdown footnotes for `SourceApparatusPolicy.translate-as-footnote`, etc.).
- **Export to PDF** — typeset with footnotes, sidebars; choose page size + font.
- **Bookmark / scroll position persistence** — reopen at last reading position.

#### Differentiating

- **Bilingual side-by-side export** — source on left, target on right, paragraph-aligned, single document.
- **Translator-notes export** — notes as appendix or separate file.
- **Per-chunk analysis-depth explanation overlay** — toggle "explain this chunk" → shows the LLM's layered-meaning analysis at the depth set by `TC.A8`.
- **Reading-aloud TTS mode** — uses macOS native TTS (`AVSpeechSynthesizer`); per target language; karaoke-style highlight of current sentence.
- **Heatmap view** — chunk-level quality score visualized along the book; at-a-glance project health.
- **Search across source + target** — find a source word; jumps to source location + corresponding target location.

#### Deferrable

- Export to HTML (for web publishing).
- Export to ePub (for ebook readers).
- Export to plain text.
- Export to JSON (structured translation memory format).
- Export to LaTeX (for academic publications).
- BibTeX citation generation.
- Custom output template (user supplies template; AI fills).
- Print preview / direct print.

**Mechanism trace:** Combination + Domain Transfer (Kindle / Apple Books reading patterns) + Absence Recognition (heatmap + analysis-depth overlay are uncommon in translation tools).

**5-test PC5: ACTIONABLE.**

---

## P6 — Quality & Translation-Craft Layer Feature Triage

### Principal Candidate (PC6)

#### Essential

- **Terminology consistency checker** — same source word renders consistently across the book; flag deviations.
- **Per-project glossary** — term → preferred translation; pin during translation; enforces consistency.
- **Issue inbox** — chunks flagged for review (low quality score; idiom detected; cultural reference detected; harmony Tier 1-2 violation; terminology deviation).

#### Differentiating

- **Harmony-layer Tier 1-2 violation flagging** — per chunk; surfaces in issue inbox with the specific Tier-1 pattern that risks being broken.
- **Multi-translation collation** — Vahide / Akarsu / Comprehenslate side-by-side for the same passage (when prior translations are loaded as references).
- **Per-chunk lineage view** — which TC axes + Policy values produced this output; ethical-provenance feature for sacred-text translation.
- **Idiom-alert inbox** — source idioms detected without clean target equivalent; per-item: source idiom + LLM-suggested rendering + alternatives.
- **Cultural-reference inbox** — per `TC.A3 source_culture`; per-item: source reference + cultural context + rendering options.
- **Passage bookmarks** — mark source passages of interest; supports fihrist micro-to-macro mirroring tracking.
- **Embedded-language detection visualization** — highlight Arabic / Persian within Turkish source.
- **Honorific consistency tracking** — SAW / AS / RA rendering uniformity across the book.
- **Glossary suggestion** — LLM suggests terms to pin based on document analysis (extracts the most-repeated terms with translation variance).

#### Deferrable

- **Translation memory (TM)** — reuse prior translations of similar passages.
- **Cross-project TM** — share TM across projects in same corpus tradition.
- **Cross-section drift detector** — chapter 5 stylistic divergence from chapter 1.
- **Diff view** — compare retranslations of same chunk.
- **Per-chunk approve / reject / edit workflow** — scholarly editorial pattern.
- **Quality dashboard per project** — completion %, issue count, terminology drift over time.
- **Reverse-translation drift check** — translate target back to source; compare for drift; QA innovation.

**Mechanism trace:** Combination (extensive — pulls from translation principles + glossary patterns + harmony layer) + Domain Transfer (CAT tools: SDL Trados, OmegaT, memoQ) + Absence Recognition redesign-level (multi-translation collation + lineage view are novel for theological-translation tools).

**5-test PC6: ACTIONABLE.**

---

## P7 — 7 Translation-Principle-Derived Differentiating Features

### Principal Candidate (PC7)

| # | Feature | Principle of origin | Primary layer-home | UX description |
|---|---|---|---|---|
| 1 | **Harmony-layer visualization** | Harmony-layer Tier 1-2 preservation (from `harmony_layer.md`) | Quality | Interactive map of Tier 1-4 markers per chunk; click a marker → see which harmony pattern (e.g., implied question-answer flow; chiastic structure; phonetic echo) is preserved and which is lost. |
| 2 | **Multi-translation collation** | Multi-meaning preservation; collective interpretation (from `translation_principals.md`) | Quality | Side-by-side view: Vahide / Akarsu / Comprehenslate for the same passage; users can import other priors. |
| 3 | **Per-chunk lineage view** | Nazm preservation (word order as meaning) | Quality | Click any chunk → see (a) which `TC` axes + Policy values produced this output, (b) which word-order decisions the LLM made and why. The ethical-provenance audit feature. |
| 4 | **Per-chunk analysis-depth explanation overlay** | Layered meaning — sarahat / işaret / remiz / îma / telvih / telmih (from `translation_principals.md`) | Reading (overlay) | Toggle "explain this chunk" → shows the layered-meaning analysis at the depth set by `TC.A8`. |
| 5 | **Passage bookmarks (fihrist)** | Micro-to-macro mirroring — *insan as fihrist* (from `notes.md`) | Reading | Mark source passages as "fihrist anchors" → indexed view shows how the passage mirrors the whole document's themes. |
| 6 | **Idiom-alert inbox** | Idiom recognition (TC.A1.c sub-axis) | Quality | Inbox of source idioms detected without clean target-language equivalent; per-item: source idiom + LLM-suggested rendering + alternatives. |
| 7 | **Cultural-reference inbox** | Cultural reference recognition (TC.A1.e + A3) | Quality | Inbox of cultural allusions detected; per-item: source reference + cultural context + rendering options per `TC.A3 source_culture`. |

Cross-references to layer pieces:
- Features 1, 2, 3, 6, 7 are Quality-layer-resident — anchor inside P6's differentiating tier.
- Feature 4 is Reading-layer-resident (overlay) — anchor inside P5's differentiating tier.
- Feature 5 is Reading-layer-resident (bookmarks) + Quality-layer-resident (indexed view) — cross-layer.

### Piece-level Inversion Candidate (PI7) at framing-semantic axis

**Assumption reversed:** "the 7 selectively-mapped principle-derived features is the right cluster."

**Alternative:** "uniform mapping — every translation principle from `references/core/` gets a UI feature."

**What follows under uniform mapping:** more features per principle but many are meaningless as UI (ihlas-driven quality toggle? collective-interpretation rationale checkbox? sünuhat-style two-step processing controller?). Discussed and rejected in Sensemaking Ambiguity 3.

**5-test on PI7:**
- Novelty: medium
- Scrutiny survival: **WEAK** — Sensemaking already adjudicated; uniform mapping fails because some principles are intrinsic LLM behavior, not user controls.
- Fertility: low (over-extension)
- Verdict: **REJECTED.**

**5-test on PC7: ACTIONABLE.**

---

## P8 — MVP Roadmap

### Principal Candidate (PC8)

#### v1 (MVP) — Essential per layer + provider basics. ~3-6 months single-developer.

- **P1 commitments:** 5-layer architecture + Project as data model + `.compldoc` + cross-cutting baseline (privacy, performance baseline, basic accessibility, document-based-app + menu bar + system notifications).
- **P2 essential:** project list / create wizard / open / rename / duplicate / archive; `.compldoc` bundle; project metadata; quick-resume.
- **P3 essential:** TC editor (8 axes); Policy editor (7 Policy classes on/off + values); PC editor; provider/model picker; Keychain storage; two-level provider config.
- **P4 essential:** chunked orchestration; per-chunk persistence; pause/resume; cancel; background continuation; crash recovery; **2 providers (Anthropic + OpenAI)**; rate-limit handling; retry; status indicator.
- **P5 essential:** live reading view; side-by-side alignment; MD + PDF export; bookmark persistence.
- **P6 essential:** terminology consistency; per-project glossary; issue inbox.

#### v2 — Differentiating tier per layer + selected principle-derived features. ~6-12 months after v1.

- **P2 differentiating:** project templates (Nursi / Bible / Quran / Tanakh presets); onboarding tutorial with sample passage; recent files; project import.
- **P3 differentiating:** inline calibration text; "why this default" links; per-policy preview; config presets; config-diff view; tri-state axes.
- **P4 differentiating:** smart cache; cost prediction; cumulative cost display; **local-LLM auto-discovery (Ollama + LM Studio)**; parallel-mode controls; token-usage display.
- **P5 differentiating:** bilingual export; translator notes; analysis-depth overlay; TTS reading mode; heatmap view; search.
- **P6 differentiating:** all 7 principle-derived features (harmony viz; multi-translation collation; per-chunk lineage; idiom inbox; cultural inbox; passage bookmarks; embedded-lang viz; honorific tracking; glossary suggestion).
- Add cross-cutting: Spotlight integration; share extension; full keyboard shortcuts; full accessibility; **English UI + Arabic UI** (as RTL pipeline proof of i18n architecture).

#### v3+ — Deferrable tier + power-user surfaces.

- **P2 deferrable:** multi-document projects; per-project encryption; iCloud sync (opt-in); project sharing.
- **P3 deferrable:** config A/B history; provider failover policy; custom prompts; advanced policy custom values.
- **P4 deferrable:** model A/B compare; per-chunk approval gate; scheduling; power throttling; custom system prompts.
- **P5 deferrable:** HTML / ePub / plain / JSON / LaTeX / BibTeX exports; custom templates; print.
- **P6 deferrable:** translation memory (TM); cross-project TM; cross-section drift; diff view; review/edit workflow; quality dashboard; reverse-drift check.
- Cross-cutting: scripting (AppleScript / Shortcuts); plugin system; macOS Continuity; Touch Bar.
- Localization to French / Turkish / Persian / Bahasa / German / etc.

#### Cross-version dependencies

- Harmony visualization (v2 P6) depends on harmony-layer engine support being functional in v1.
- Smart cache (v2 P4) depends on per-chunk persistence (v1 P4).
- Local-LLM auto-discovery (v2 P4) depends on multi-provider abstraction (v1 P4).
- Multi-document projects (v3 P2) depend on cross-project TM design — coupled to TM (v3 P6).

### Piece-level Inversion Candidate (PI8) at intervention-shape axis

Property (v) fires (commits ADD-CONTENT MVP roadmap with v1/v2/v3+ phasing).

**Alternative shape A — REORGANIZE-WITHOUT-ADDING:** Don't propose a roadmap; just list all features by category. Let the user (developer) prioritize independently.

What follows: less prescriptive; relies on the user to do the prioritization work; loses the MVP-vs-stretch guidance.

5-test:
- Novelty: medium (a flat-list approach is common)
- Scrutiny survival: **WEAK** — user explicitly asked for design + asked "what else?" iteratively; the absence of MVP guidance leaves the design unactionable for a builder. Anti-bloat preference confirms MVP guidance is needed.
- Verdict: **REJECTED.**

**Alternative shape B — CONTRARIAN-RETHINK:** Question whether MVP-phasing is the right output. Maybe "permanent feature list with priority scores per item" is better than fixed versions.

What follows: priorities without commitments; user can re-prioritize anytime; no version commitments.

5-test:
- Novelty: medium
- Scrutiny survival: **WEAK** — versions provide concrete commitment moments aligned with development phases; priority scores without version anchors are abstract and don't help an actual build plan.
- Verdict: **REJECTED.**

**5-test on PC8: ACTIONABLE.**

---

## P9 — Inherited Commitments Re-test

### Principal Candidate (PC9)

| Commitment | Status | Structural evidence (which UI feature embodies the commitment) |
|---|---|---|
| 3-layer schema architecture (TC + Policy + PC) from `schemas.py` | **RE-TESTED — commitment confirmed** | Configuration surface layer (P3) directly exposes the 3 schemas as TC editor + Policy editor + PC editor sub-screens. Architecture unchanged; UI design respects it. |
| `SKILL.md` 5-step workflow | **RE-TESTED — commitment confirmed** | Mac UX flow maps the 5 steps to native UI: project list → new project wizard (combines steps 1+2) → language picker → config editor → translation execution → output. Direct alignment. |
| Harmony-layer Tier 1-2 preservation as non-negotiable | **RE-TESTED — commitment confirmed** | Quality layer (P6 differentiating) surfaces Tier 1-2 violation flagging as a USER-VISIBLE feature; the actual preservation behavior is INTRINSIC to the LLM and the UI cannot toggle it off. |
| Translation principles' "comprehensation" identity | **RE-TESTED — commitment confirmed but frame revised** | 7 principle-derived UI features (P7) carry the UI-mappable principles; non-UI-mappable principles (ihlas; collective interpretation; sünuhat; self-illuminating detection) remain intrinsic LLM behavior. The identity is preserved across both surfaces. |
| Anti-bloat principle (recurring across this session) | **RE-TESTED — commitment confirmed** | 5-layer architecture + 3-tier triage IS the anti-bloat discipline. MVP (v1) = essential only; v2 adds differentiating; v3+ adds deferrable. Nothing in v1 that isn't load-bearing. |
| FP2 "Don't declare what the LLM can infer" | **RE-TESTED — commitment confirmed and extended** | Mac app's intake (P2 new-project wizard + P3 config) doesn't ask for source language (auto-detected by LLM); doesn't ask for chunking strategy (LLM-handled per PC defaults); user is asked only for value judgments (target language, TC axes, Policy values). FP2 enforced in UI design. |

### Piece-level Inversion Candidate (PI9) at relationship-label axis

**Assumption reversed:** "RE-TESTED-confirmed verdicts should be propagated."

**Alternative:** leave priors un-flagged; don't propagate Re-test verdicts.

**5-test:** WEAK — Synthesis Trigger requires Re-test propagation per CONCLUDE protocol; skipping it would fail the protocol.

**Verdict: REJECTED.**

**5-test on PC9: ACTIONABLE.**

---

## P10 — Open Questions

### Principal Candidate (PC10)

#### Monitoring

- **Provider landscape evolution.** Track Apple Intelligence as a future provider (potential native macOS LLM); local LLM capability growth; rare-language LLM detection reliability.
- **Mac-platform API evolution.** SwiftUI document-based-app APIs; Swift concurrency; Keychain APIs — monitor for deprecations.

#### Blocked

None currently — design is complete.

#### Research Frontiers

- **Cross-corpus extension to non-Islamic theological corpora** (Tanakh; Bible; Sanskrit-Hindu; Pali Buddhist; Christian patristic). Same frontier flag as the prior `chunk_types_vs_mechanisms` inquiry. Adds corpus-specific project templates + Policy defaults + cultural-reference inbox calibration.
- **LLM-inferability decay at rare/dead languages** (Aramaic; Coptic; Sumerian; Akkadian; Ge'ez). May require Config-surface accommodations (e.g., a fallback "declare source language" toggle when LLM detection is unreliable).
- **The 7 principle-derived features may expand.** Are there others? Self-illuminating passage detection (currently intrinsic) could become user-controllable if a meaningful user decision emerges.

#### Refinement Triggers

- **Monetization model decision.** OUT-of-architecture-scope per Sensemaking Ambiguity 5. Trigger to address: when ready to ship v1. Options: Mac App Store one-time purchase; direct download with paid license; open-source; donation-ware. No UI surface impact regardless of choice (no signup/login UI required).
- **Mobile / iPad expansion.** Considered out of scope for this inquiry. Trigger: when v2 ships and project bundles can be device-portable. Options: Mac Catalyst port (auto-port the SwiftUI app); separate native iPad app (better touch UX).
- **App UI localization beyond English + Arabic.** English-only at v1; Arabic UI at v2 as RTL proof-of-pipeline. Trigger to expand: market demand from non-English-speaking translators.
- **Plugin system / scripting API.** Power-user feature; deferred to v3+. Trigger: when v3+ and evidence emerges of user demand for extensibility.

#### Open Questions Inherited from Prior Inquiries

- **Policy-class co-application precedence** (from `chunk_types_vs_mechanisms` inquiry's Open Questions). Re-surfaces here as a Configuration-surface UX consideration: how do co-applying Policy classes display in the Policy editor? Current default: show as independent toggles; the per-policy preview helps the user understand co-application effects.

**Mechanism trace:** Absence Recognition (gaps that the design intentionally leaves) + Extrapolation (LLM landscape evolution; mobile expansion trajectory).

**5-test PC10: ACTIONABLE.**

---

## Inherited Frame Audit (between Phase 2 and Phase 3)

### Seed-level central assumption

"The SV6 stabilized model from Sensemaking is the right substrate to elaborate; the 5-layer architecture + 3-tier triage + Project-as-data-model + 7-feature mapping should all be preserved."

### Piece-level commitments

| Piece | Load-bearing commitment | Property fired |
|---|---|---|
| P1 | 5-layer architecture + Project-as-data-model + 3-tier triage + 7 FPs | (b) framing-semantic + (c) lesson-vocabulary |
| P7 | Selective principle-to-UI mapping (7 features) | (b) framing-semantic |
| P8 | ADD-CONTENT MVP roadmap with v1/v2/v3+ phasing | (e) intervention-shape commitment |
| P9 | RE-TESTED-confirmed verdicts on 6 inherited commitments | (a) relationship-label |

### Step (iii) — Challenge scan

- **Seed-level central assumption:** PI1 (P1 Inversion) explicitly challenged the 5-layer + Project + triage triad via single-flow alternative. REJECTED structurally. ✓ challenged.
- **P1 commitment:** PI1 covers it. ✓
- **P7 commitment:** PI7 (uniform principle-mapping Inversion) challenged the selective mapping. REJECTED structurally. ✓
- **P8 commitment:** PI8 alternatives A (REORGANIZE-WITHOUT-ADDING) and B (CONTRARIAN-RETHINK with priority scores) both challenged the ADD-CONTENT shape. Both REJECTED. ✓
- **P9 commitment:** PI9 (don't-propagate Inversion) challenged the propagation requirement. REJECTED per CONCLUDE protocol. ✓

### Step (iv) — Firing condition

Audit **does NOT fire** — every load-bearing commitment has at least one explicit challenge in the candidate set. Proceed to Phase 3 Test (already conducted per-piece above).

---

## Phase 3 — Assembly Check

### Survivors combined

PC1 (substrate) + PC2-PC6 (per-layer feature triages) + PC7 (cross-layer principle cluster) + PC8 (roadmap) + PC9 (re-test) + PC10 (open questions) — 10 principal candidates, all ACTIONABLE.

### Emergent assembly candidates

**AE1 — "Comprehenslate Mac" as a positioning brand.** The Mac app is a discrete product wrapping the existing Comprehenslate system; distinguishable from any future "Comprehenslate Web" or "Comprehenslate Mobile." Branding/positioning insight that doesn't fit in any single piece.

5-test AE1: Novelty medium; Scrutiny STRONG (branding matters if multi-platform expansion is plausible); Fertility medium; Actionability medium; Mechanism independence medium. **Verdict: DEFERRED** — branding is downstream of v1 distribution decisions; revival trigger: when distribution channel is chosen.

**AE2 — The 3-tier triage as a user-visible teaching surface.** The app could surface its own design structure to users (Settings → "Roadmap" shows essential / differentiating / deferrable categorization). Makes the design's structure visible; the triage itself becomes a differentiator.

5-test AE2: Novelty HIGH; Scrutiny medium (could feel anti-marketing — showing users what they DON'T have); Fertility medium; Actionability medium; Mechanism independence low (only Combination + Inversion). **Verdict: DEFERRED** — interesting but possibly anti-marketing; revival trigger: if users ask "what features are coming?" frequently.

### Axis coverage check

| Axis | Variance |
|---|---|
| Content axis | PC1 names principles + architecture; PC2-PC6 populate per-layer content; PC7 cross-layer; PC10 residuals. |
| Intervention-shape axis | PC8 commits ADD-CONTENT MVP roadmap; PC5 (alternatives A + B) explored. |
| Scope axis | PC10 Open Questions includes cross-corpus extension; mobile expansion; localization. |
| Direction axis | PC9 commits to RE-TESTED-confirmed direction for all 6 priors (vs un-flagged). |

Multi-axis variance verified.

### Shared-input detection

Multiple PCs share inherited input from SV6 (5-layer architecture; 7-feature mapping; Project-as-data-model). Potential SPURIOUS convergence?

Adversarial test: invert SV6's central claim (PI1). PI1 REJECTED on structural grounds (long-book feasibility; user-explicit "project selection logic"). The convergence is **INDEPENDENT** (SV6 survives challenge), not SPURIOUS.

---

## Telemetry

### Standard

- **Generators applied:** 4/4 (Combination throughout; Absence Recognition redesign-level at P1/P3/P5/P6/P10; Domain Transfer at P1/P5/P6; Extrapolation at P10)
- **Framers applied:** 3/3 (Lens Shifting at P3; Constraint Manipulation ADD/REMOVE at P4; Inversion at P1/P7/P8/P9)
- **Convergence:** YES — 3+ mechanisms converge per PC
- **Survivors tested:** 10 PCs + 4 PIs + 2 AEs = 16 tested
- **Failure modes observed:** NONE (Premature Eval N; Single-Mech N; Early Frame Lock N; Innovation Without Grounding N; Mechanism Exhaustion N; Survival Bias N)

### Production-task additional telemetry

- **Per-piece mechanism log:**
  - P1: [Combination, AbsenceRec-redesign, Inversion, DomainTransfer]
  - P2: [Combination, AbsenceRec, DomainTransfer]
  - P3: [Combination, LensShifting, AbsenceRec]
  - P4: [Combination, ConstraintManip(ADD+REMOVE), Extrapolation]
  - P5: [Combination, DomainTransfer, AbsenceRec]
  - P6: [Combination, DomainTransfer, AbsenceRec-redesign]
  - P7: [Combination, AbsenceRec, Inversion:framing-semantic]
  - P8: [Combination, AbsenceRec, Inversion:intervention-shape]
  - P9: [Combination, Inversion]
  - P10: [AbsenceRec, Extrapolation]

- **Per-piece axis-distribution log (property-v pieces only):**
  - P8: [Inversion:intervention-shape, Combination:content]

- **Meta-decision-piece classification:**
  - P1 = meta-decision
  - P2-P6 = content-production
  - P7 = meta-decision
  - P8 = meta-decision
  - P9 = meta-decision
  - P10 = content-production

- **Piece-level Inversion compliance:**
  - P1 = satisfied (PI1 generated + tested)
  - P7 = satisfied (PI7 generated + tested)
  - P8 = satisfied (intervention-shape axis: alternatives A and B generated + tested)
  - P9 = satisfied (PI9 generated + tested)

### Verdict

**PROCEED.** Full coverage (4G + 3F); convergence on every PC via 3+ mechanisms; all 4 meta-decision pieces satisfied Piece-Level Inversion compliance; Inherited Frame Audit did NOT fire; Assembly check produced 2 deferred emergents. No failure modes observed.
