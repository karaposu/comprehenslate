## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_20-50__swiftui_v0_keychain_and_subtask_enumeration/_branch.md`

Upstream outputs in same folder: `articulate_simple.md` + `surfacing.md`.

Sensemaking commits to:
- (I1) Storage Strategy Decision Matrix (5 options × 4 axes) + recommended approach with explicit threat-model reasoning (no Keychain rubber-stamp)
- F2 frontier flag (KeyStore protocol in v0?), F1 (Settings scene in v0?), F5 (sandbox in v0?)
- (I2) Pruned subtask enumeration to a file-level build-checklist (per "execution-planning" motivation)
- v0 "days" timeline validation
- Inherited Commitments Re-test against Mac-app finding's 5-layer architecture

---

# Sensemaking

---

## SV1 — Baseline Understanding

The user is challenging the v0.5 Keychain commitment in the suggested phasing ("is Keychain required? why not paste-each-session? where to save it?") and asking for an enumeration of v0 SwiftUI subtasks. Two separable questions — one about a security/architecture decision, one about scope/decomposition.

Initial read: the user wants (a) a defended recommendation on storage strategy with the option space made explicit, not a default-to-Keychain answer; and (b) a concrete actionable list of subtasks they could work through to ship v0.

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1** — v0 ships in "days," not weeks.
- **C2** — BYO API key (no server-side storage; no account/login model).
- **C3** — Mac-native, Apple Silicon arm64-only.
- **C4** — Cross-platform is OUT (Mac-only commitment from prior finding).
- **C5** — The user IS the developer AND the initial v0 user (personal use first).
- **C6** — v0 lacks any distribution scaffold (no notarization, no DMG, no signed installer) — by inheritance from "days" timeline and lack of v0 mention of these.
- **C7** — v0 substrate exclusions: no pause/resume; no project model; no Keychain.
- **C8** — Storage option must remain viable when sandboxed (because notarization for v0.5+ distribution requires Hardened Runtime + benefits from Sandbox).
- **C9** — 5-layer architecture inherited (Project shell / Config / Execution / Reading & output / Quality).

### Key Insights

- **KI1** — The "common pattern" anchor (R4 #41 — Mac apps use Keychain for secrets; UserDefaults for secrets is rare) is **social convention, not structural** evidence. It survives only by precedent.
- **KI2** — The actual structural security delta (R6 #54) is **at-rest encryption**: UserDefaults stores the key in plaintext at `~/Library/Preferences/<bundle-id>.plist`; Keychain encrypts at-rest with per-Mac key + per-app ACL. THIS is structural evidence.
- **KI3** — Backup channels (R2 #21, R6 #60) matter: plaintext UserDefaults plists travel in Time Machine + iCloud-backup-of-Mac unencrypted; Keychain items travel encrypted.
- **KI4** — Paste-each-session (R1 #3) is a **different category** from persistence options — it sidesteps the storage question rather than answering it. It is a first-class option, not a degenerate.
- **KI5** — v0 has two distinct threat regimes: (a) dev-self-testing (single-user dev Mac, attacker = self/own malware) — minimal risk; (b) distributed-to-others (attacker = arbitrary) — significant risk. The Keychain recommendation is **phase-dependent**.
- **KI6** — A `KeyStore` protocol (~10 lines) decouples storage decision from UI bindings, making v0→v0.5 storage swap mechanical (replace impl, no UI changes).
- **KI7** — The v0 "days" target is fragile: 199 surfaced items include ~50-80 core/sub for v0; the upper bound is ~2-3 days of focused work AT THE FILE LEVEL.
- **KI8** — Settings scene vs inline key field is a UX axis, separable from the storage axis. Inline works for solo-dev; Settings is desirable when there's >1 setting to put in it (v0.5+ adds target-lang preferences, model selection, "use Keychain" toggle).
- **KI9** — Sandbox-on-day-1 has small upfront cost (1 capability toggle + 1 entitlement) and prevents downstream rework when adding sandbox later (which would require re-testing every file op + entitlement).

### Structural Points

- **SP1** — 5 viable storage approaches for BYO key on macOS:
  - A: Paste-each-session (in-memory; KeyStore returns nil at launch)
  - B: UserDefaults via `@AppStorage` (plaintext plist)
  - C: Keychain Services (encrypted; per-app ACL)
  - D: Application Support file (self-rolled JSON file)
  - E: Environment variable read at launch (dev-only)
- **SP2** — 4-axis evaluation matrix per option: Security × UX × Persistence × Portability
- **SP3** — `KeyStore` protocol shape: `protocol KeyStore { func get() -> String?; func set(_ key: String); func clear() }` + per-impl variations
- **SP4** — v0 component mapping to 5-layer architecture:
  - Project shell → `ComprehenslateApp.swift`
  - Config → `KeyStore.swift` + `@AppStorage("target_lang")` for target language
  - Execution → `ClaudeClient.swift` + `URLSession` + `Task`
  - Reading & output → `ContentView.swift` (source/translation panes + save)
  - Quality → `TranslationError.swift` + `.alert` modifier
- **SP5** — v0 subtask groups (4 stages): Xcode-setup → File-creation → Wiring → Run-and-test
- **SP6** — v0 needs 6-7 files: `ComprehenslateApp.swift` / `ContentView.swift` / `ClaudeClient.swift` / `KeyStore.swift` / `Models.swift` / `TranslationError.swift` (+ auto-managed `Assets.xcassets` / `.entitlements`)

### Foundational Principles

- **FP1** — Asymmetric failure: under-storing key is a recoverable inconvenience (re-paste); over-storing in plaintext under threat model that doesn't tolerate plaintext is a non-recoverable security regression. At v0 dev-self, the asymmetry **favors UserDefaults**: plaintext is the developer's accepted risk.
- **FP2** — Simplicity-bias for v0: any abstraction must justify itself within v0 scope OR via cheap-now / expensive-later economics.
- **FP3** — Decouple decisions: storage strategy ≠ UI shape; `KeyStore` protocol enables the decoupling.
- **FP4** — The 5-layer architecture (inherited) is the right grouping for *component placement*, NOT the right grouping for *build-checklist ordering*.
- **FP5** — "Common pattern" arguments are NOT structural; they require independent validation against the specific threat model.
- **FP6** — User's methodological-rigor motivation (per articulate_simple Item I1 MultiDepth WHY-axis) — the answer should **defend recommendations**, not assert them by precedent.

### Meaning-Nodes

- **MN1** — Storage Strategy Decision Matrix (5 × 4 grid)
- **MN2** — `KeyStore` protocol as v0 architectural decoupler
- **MN3** — v0 subtask DAG (4 stages; ~50-60 leaf subtasks)
- **MN4** — "The SwiftUI onion" — App → Scene → ContentView → safeAreaInset + toolbar → state hooks → networking
- **MN5** — Threat model dichotomy: dev-self vs distributed-to-others
- **MN6** — Phase-dependent recommendation (v0 ≠ v0.5 ≠ v1) — security calculus changes per phase

---

### Meta-Inspection (post-SV2) — H4 + H5

- **H4 (concept names):** "KeyStore protocol" — is this a project-actual term or a loop-coined neologism? It is loop-coined HERE; not yet committed to in the prior Mac-app finding. But it's a thin syntactic abstraction matching standard Swift naming conventions (e.g., `URLSessionStore`, `KeychainStore` patterns common in iOS/Mac code); user-language alignment is acceptable.
- **H5 (motivating examples):** the storage-strategy decision rests on TWO motivating examples — Raycast/BoltAI/MacGPT all using Keychain (prior art, R4 #31-33). Is the broader pattern just those examples, or a general principle? Sensemaking treats them as supporting "common pattern" (KI1), and KI1 is explicitly demoted to social-not-structural. The motivating examples are honored as anchors for the social-convention claim, not for the structural-security claim.

## SV2 — Anchor-Informed Understanding

After anchors:

**I1 collapses** into: 5 viable storage options × 4 evaluation axes = decision matrix. The Keychain commitment in the substrate is justified for the *distributed* threat model but **over-engineered for the v0 dev-self regime**. A `KeyStore` protocol introduced in v0 decouples the decision from the UI, so v0.5 Keychain swap becomes a 1-file change. The "common pattern" anchor doesn't survive structural test.

**I2 collapses** into: v0 has ~50-60 file-level subtasks organized as Xcode-setup → file-creation → wiring → run-and-test, mapped to the inherited 5-layer architecture. "Days" target is achievable if Settings scene is deferred to v0.5 and Keychain is deferred to v0.5.

---

## Phase 2 — Perspective Checking

### Technical / Logical

- Keychain Services API is fiddly (CFTypeRef-heavy, error-prone) — typically 30-80 lines of Swift wrapper code, non-trivial for v0
- UserDefaults via `@AppStorage("api_key")` is **1 line** — trivial
- Paste-each-session is **0 storage lines** — even simpler
- KeyStore protocol abstraction: ~10 lines protocol + ~5-50 lines per impl
- URLSession async/await is straightforward; Anthropic API is well-documented (no novel work)
- App Sandbox + Network Client entitlement: 2 toggles in Xcode + 1 build = trivial
- Hardened Runtime + Notarization is a 4-8 hour investment, BUT not needed for v0 (dev-only)

### Human / User (the developer)

- For v0 self-testing: paste-each-session is fine but ANNOYING — re-paste every launch, ~30 sec friction per dev session
- For v0 self-testing: paste-once + UserDefaults remember is the ergonomic default
- Keychain at v0 adds first-time-system-prompt UX (modal "Allow Comprehenslate to access Keychain?") for zero security benefit at this stage
- Settings scene in v0 is overkill — single key field works inline; the user explicitly signaled scope-minimization motivation
- The user signaled methodological-rigor — recommendation must defend, not rubber-stamp

### Strategic / Long-term

- The storage decision affects ALL downstream phases — but ONLY because the v0.5 phasing was *designed* to swap to Keychain
- KeyStore protocol in v0: v0.5 swap becomes 1-file replacement; no UI rewiring
- No KeyStore protocol: every UI binding to the key must be touched at v0.5
- **Strategic verdict: introduce KeyStore protocol in v0**; the ~10-line abstraction pays for itself within one phase

### Risk / Failure

- Risk without KeyStore protocol: v0.5 swap is invasive (touches ContentView, Settings, any future provider key bindings)
- Risk of paste-each-session in v0: developer re-pastes every launch (annoying, not security-critical)
- Risk of UserDefaults in v0: plaintext key in plist; IF developer Mac is compromised, key leaks. BUT this is also true of any unencrypted file the developer holds (.env, terminal history, etc.). The threshold "is your Mac compromised?" applies broadly — not specific to this app
- Risk of Keychain in v0: 30-80 lines of wrapping code + first-time modal UX + zero v0 security benefit
- Risk of distribution-readiness gap: v0 AS-IS shipped to other users WITH UserDefaults plaintext = real risk for THEM. But v0 has no distribution mechanism (no notarized DMG); shipping to others would require deliberate v0.5+ work
- **Distribution mitigation:** v0 is dev-only **by absence of distribution scaffold**. The gap is structural, not policy

### Resource / Feasibility

- v0 "days" target: ~50-60 file-level subtasks × ~15-20 min avg = ~12-20 hours = **2-3 days focused work** ✓
- Adding Keychain at v0: +2-4 hours → pushes upper bound to ~3 days
- Adding KeyStore protocol: +30 min → trivial
- Adding Settings scene at v0: +2-4 hours → could push toward 1 week
- Notarization at v0: +4-8 hours → definitely not v0
- **Feasibility verdict: v0 fits "days" IF Keychain + Settings + notarization all deferred to v0.5+**

### Ethical / Systemic

- BYO key model = user owns the security tradeoff; developer's job is to NOT make it worse
- Plaintext UserDefaults for a *distributed* app would be ethically questionable — recipients might not realize the risk
- For solo-dev v0: ethical concern minimal (developer accepts own risk)
- **Ethics verdict:** recommendation is ethically clean IF v0 is explicitly dev-only AND if v0.5 commits to encrypted storage before distribution

### Definitional / Internal Consistency

- "Common pattern" anchor (KI1): social — would NOT survive structural test on threat-model grounds
- "Security at-rest" anchor (KI2): structural — applies to threat models that include disk-readers
- The two anchors converge on Keychain for distribution; diverge for v0 dev-self
- The 5-layer architecture is structural and maps cleanly to v0 components — internally consistent

### Definitional / Frame-exit Completeness

**Gating predicate check:** does the inquiry's commitments include terms inherited from prior findings used across ≥2 distinct values WITHIN this inquiry's committed structures? The inherited terms are "v0," "Keychain," "UserDefaults" — but they appear as concrete options or phase-labels, NOT as multi-value typed taxonomies populating multi-row tables/ladders. The Storage Strategy Decision Matrix IS a multi-row structure, but its values are options the inquiry GENERATES, not inherited multi-value terms. **Gating does NOT fire.** Skip the four meta-categories.

### Phase / Calibration-State

**REQUIRED** — the inquiry involves a rule that depends on calibration state.

- The "common pattern" recommendation depends on calibration = "we are a shipping product with real users." At v0 (pre-distribution), this calibration is NOT present
- The Keychain recommendation depends on threat-model state = "attacker is not the user." At v0 dev-self, threat-actor = user-themselves; doesn't apply
- The 5-layer architecture depends on calibration = "v1 product." At v0, architecture is aspirational; v0 builds *toward* it but doesn't satisfy the calibration yet
- **Conclusion: the recommendation MUST phase-condition.** Cannot give a single "use Keychain" answer; the answer is "v0: KeyStore protocol + UserDefaults default; v0.5: same protocol, Keychain impl"

### Self-reference

- Sensemaking is evaluating a Mac-app design decision; the conceptual frameworks (Swift / SwiftUI / Keychain / Mac threat models) are external to sensemaking's framework
- **Skip** — no self-reference concern

---

### Meta-Inspection (post-SV3) — H1, H2, H3, H7

- **H1 (candidate set):** the 5 storage options (A-E) — are any of them the same thing? B (UserDefaults) and D (Application Support file) are distinct (different APIs, different file locations, different sandbox behavior). A (paste-each-session) is structurally distinct from all persisted options. C (Keychain) is its own category. E (environment variable) is dev-only and distinct from runtime-loaded options. Candidates are genuinely distinct.
- **H2 (frame scope):** is the frame too narrow? Are there storage options outside the 5 considered? "1Password CLI integration" (R4 #42) was tagged SIDE/LOW; "iCloud Keychain sync of an item" (R1 #10) is a variation of C; "encrypted file with user passphrase" (R1 #8) is a variation of D with a passphrase UX cost; "macOS keychain types other than Login" (R3 #30) are sub-options of C. All sub-options collapse to the 5 categories. Frame is appropriate.
- **H3 (question framing):** the user phrased the question as "keychain is required or not?" — but the more useful frame is "where to save it?" (the user's own reframe — articulate_simple Item I1 MQ1 "reframe-the-question"). Sensemaking honors this reframe; the deliverable centers on the matrix, not on the yes/no.
- **H7 (phase/calibration state):** already addressed — recommendation phase-conditions explicitly.

## SV3 — Multi-Perspective Understanding

Phase 2 surfaces:

1. The Keychain decision is **phase-dependent**, not absolute. v0 (dev-self) doesn't justify Keychain; v0.5+ (distributed) does
2. The KeyStore protocol decouples the phase transition — recommended **in v0**
3. The "common pattern" anchor doesn't survive structural test (KI1 demoted)
4. v0 "days" target is achievable IF Keychain + Settings deferred to v0.5
5. Settings scene → DEFERRED to v0.5
6. Sandbox → ON in v0 (cheap; prevents downstream rework)
7. v0 deliverable for I2 = file-level build-checklist (not high-level components)

Open questions for ambiguity collapse:

- Which storage backing does v0's KeyStore use by default? (UserDefaults vs paste-each-session)
- Should the build-checklist be flat or grouped by stage?
- Does the inherited 5-layer architecture map cleanly to v0 files? (Yes per SP4 — confirm via Ambiguity Collapse)

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1 — What is the actual threat model for v0?

**Strongest counter-interpretation:** v0 might be shared with friends or shown to others early; treating it as "dev-only" assumes a behavior the developer might not stick to.

**Why counter fails (structural grounds):** v0 has **no distribution mechanism**. No code-signing for distribution (just personal-team signing), no notarization, no DMG, no installer. A v0 .app bundle physically cannot be casually shared — recipients hit Gatekeeper warnings on opening, the binary won't run cleanly on their Mac without dev tools setup. Even if the developer manually copies the .app to a friend, the friend's Mac will refuse to launch it without ad-hoc unblocking. The structural argument: v0 = dev-self **by absence of distribution scaffold**, not by policy declaration.

**Confidence:** HIGH

**Resolution:** v0's threat model is single-user dev Mac. Attacker model = "developer's own Mac is compromised" — same threshold as any other unencrypted file the developer holds.

**Fixed:** v0 threat model.
**No longer allowed:** assuming v0 must defend against external attackers.
**Depends on this:** storage backing choice; "common pattern" anchor demoted to phase-dependent.
**Conceptual shift:** Keychain is not mandatory at v0; the structural security delta is moot when only the developer has access.

### Ambiguity 2 — Does the "common pattern" justify Keychain at v0?

**Strongest counter-interpretation:** Yes — following Mac-app convention reduces user surprise; the convention IS the de-facto standard so deviating creates downstream friction (users expect to manage keys via Settings + Keychain).

**Why counter fails (structural grounds):** v0's user is the developer themselves. The developer is NOT surprised by deviation from convention; the convention argument only applies to the eventual distributed product (v0.5+), not to v0. Citing precedent ("Mac apps use Keychain") is not structural evidence per the spec's Clean-Resolution-Trap corrective.

**Confidence:** HIGH

**Resolution:** "common pattern" doesn't justify Keychain at v0. It justifies Keychain at v0.5+ (distributed).

**Fixed:** anchor strength — common-pattern arguments require explicit phase-conditioning.
**No longer allowed:** rubber-stamping Keychain because "everyone does it."
**Depends on this:** storage choice; opens space for paste-each-session and UserDefaults at v0.
**Conceptual shift:** methodological-rigor motivation honored.

### Ambiguity 3 — Should v0 introduce the `KeyStore` protocol?

**Strongest counter-interpretation:** No — YAGNI at v0; `@AppStorage("api_key")` inline in views works. The protocol is over-engineering for an MVP.

**Why counter fails (structural grounds):** The entire v0.5 phasing assumes a Keychain swap. Without a protocol, every UI binding that touches the key (SecureField in v0; Settings field in v0.5; multi-provider key bindings in v1) needs to be re-wired. With the protocol, the swap is a single-file replacement. Protocol cost: ~10 lines. Without-protocol cost at v0.5: ~30-50 lines of UI re-wiring + risk of missing a binding. Structural economics favor the protocol.

**Confidence:** HIGH

**Resolution:** YES — introduce `KeyStore` protocol in v0.

**Fixed:** v0 architecture includes KeyStore protocol.
**No longer allowed:** inline `@AppStorage("api_key")` in views (must go through KeyStore).
**Depends on this:** ContentView binding pattern (via KeyStore); v0.5 Keychain swap (mechanical).
**Conceptual shift:** small protocol layer at v0 pays large dividends at v0.5+.

### Ambiguity 4 — What's the v0 `KeyStore` implementation backing?

**Strongest counter-interpretation:** paste-each-session (in-memory only, no persistence). The security-prudent choice: no plaintext at rest anywhere. The dev can paste once per work session; that's not unreasonable friction.

**Why counter fails (structural grounds):** paste-each-session is acceptable and has real merit — but at the cost of repeated dev-iteration friction. The dev will run many test translations; each fresh launch re-pastes. UserDefaults trades the at-rest-plaintext risk for ergonomic dev iteration. For dev-self threat model, the plaintext-at-rest IS the developer's own risk to accept. **However**, the counter has structural merit — it's not eliminated, just not selected as default.

**Confidence:** MEDIUM — both options are structurally defensible for v0; the choice is a values tradeoff (security-prudence vs ergonomic-default), not a structural winner.

**Resolution:** v0 KeyStore backing = **UserDefaults `@AppStorage` by default**, with paste-each-session offered as an *alternative implementation* (one-line swap). The Storage Strategy Decision Matrix presents both for the user to choose.

**Fixed:** v0 default ships with `@AppStorage`-backed `KeyStore`.
**No longer allowed:** Keychain at v0 (deferred to v0.5).
**Depends on this:** Settings UI deferred to v0.5; v0.5 swap mechanical via protocol.
**Conceptual shift:** explicit two-impl offering honors the security-prudence motivation without imposing it.

### Ambiguity 5 — Settings scene in v0?

**Strongest counter-interpretation:** Yes — Mac-app conventions expect a Settings scene; v0 is the right time to lay it down so v0.5 doesn't need to retrofit.

**Why counter fails (structural grounds):** A Settings scene adds 2-4 hours (Settings { ... } + Form + Section + per-setting bindings). At v0 with a single key field already inline in main UI's `safeAreaInset`, **there's nothing to put in Settings**. The scene becomes valuable at v0.5 when there's: target-language preferences, model selection, output directory default, "use Keychain" toggle, multi-provider keys. Adding it at v0 is a 2-4 hour cost for a scene with one field; deferral cost at v0.5 is the same 2-4 hours when there are 4-6 fields to populate.

**Confidence:** HIGH

**Resolution:** NO Settings scene in v0; inline key field in main UI. Settings scene introduced in v0.5.

**Fixed:** v0 has no separate Settings scene.
**No longer allowed:** adding Settings panel to v0.
**Depends on this:** v0 timeline saves 2-4 hours; v0.5 scope explicitly includes Settings scene.
**Conceptual shift:** scope-minimization honored.

### Ambiguity 6 — Sandbox in v0?

**Strongest counter-interpretation:** No — unsandboxed v0 is simpler; turn on sandbox at v0.5+ when distributing.

**Why counter fails (structural grounds):** turning sandbox ON later requires re-testing every file operation, every entitlement, every URL the app touches — surprise sandbox failures at v0.5+ are real (e.g., NSSavePanel behaves differently sandboxed; file URLs need security-scoped bookmarks). Starting sandboxed at v0 forces the code to work correctly under sandbox from day 1. v0's required capabilities are minimal: only Network Client (for LLM API calls). Toggling sandbox + adding network entitlement: 5-minute Xcode operation. Savings: zero downstream rework at v0.5+ for sandbox surprises.

**Confidence:** HIGH

**Resolution:** v0 IS sandboxed (App Sandbox capability ON; Network Client entitlement enabled).

**Fixed:** v0 sandbox state.
**No longer allowed:** unsandboxed v0; surprise sandbox failures at v0.5+.
**Depends on this:** entitlements file; build settings.
**Conceptual shift:** small upfront cost prevents downstream rework.

### Ambiguity 7 — Build-checklist granularity for I2 enumeration?

**Strongest counter-interpretation:** A high-level component list (8-10 boxes — "Networking layer," "View layer," "Settings layer") is more elegant and easier to read.

**Why counter fails (structural grounds):** The user's WHY-axis motivation is "execution-planning + make-the-abstraction-concrete" (from articulate_simple). High-level boxes don't translate to executable next steps. "Build the networking layer" is not actionable; "create `ClaudeClient.swift` containing `func translate(source:target:key:) async throws -> String`" IS actionable. The user wants to BUILD, not understand at high level. The deliverable shape is file-level subtasks with explicit dependencies.

**Confidence:** HIGH

**Resolution:** file-level subtasks with explicit dependencies; organized in 4 stages: Xcode-setup → File-creation → Wiring → Run-and-test.

**Fixed:** v0 deliverable shape = file-level build-checklist.
**No longer allowed:** high-level abstractions as the deliverable.
**Depends on this:** I2 enumeration granularity.
**Conceptual shift:** deliverable shape committed.

---

### Load-bearing concept test (Phase 3 refinement)

- **`KeyStore` protocol** — Phase 5 stabilization candidate. Sub-aspects:
  - proxy-vs-structural: real structural distinction (decouples persistence from UI); not a proxy
  - discoverability: usage requires conscious application (ContentView accesses key via injected KeyStore; not magic)
  - user-language alignment: matches Swift idioms (`-Store` suffix is common); user-recognizable
- **"Phase-dependent recommendation"** — KI5 + MN6. Sub-aspects:
  - proxy-vs-structural: structural — phases differ in threat model; not arbitrary
  - discoverability: requires the finding to state phase-conditioning explicitly; OK if the Decision Matrix labels per-phase recommendations

### Specific-vs-pattern recognition cue

KI1 (the "common pattern" demotion) is built from 3 specific examples (Raycast, BoltAI, MacGPT) — are these specific or pattern? They are SPECIFIC examples of the broader convention "Mac apps store credentials in Keychain." The demotion to social-not-structural applies to the broader convention, not just to the 3 examples — so the cue is OK; the demotion holds at the pattern level.

## SV4 — Clarified Understanding

After ambiguity collapse:

1. **v0 threat model = single-user dev Mac** (NOT distributed) — structural by absence of distribution scaffold
2. **"Common pattern" doesn't justify Keychain at v0** — demoted to phase-dependent
3. **KeyStore protocol introduced in v0** — ~10 lines decouples storage from UI
4. **v0 KeyStore default backing = UserDefaults `@AppStorage`**; paste-each-session offered as 1-line alternative impl
5. **NO Settings scene in v0** — inline key field; Settings deferred to v0.5
6. **Sandbox ON in v0** + Network Client entitlement
7. **I2 deliverable = file-level build-checklist** in 4 stages: Xcode-setup → File-creation → Wiring → Run-and-test

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed Variables

- v0 threat model: single-user dev Mac
- v0 sandbox state: ON (App Sandbox + Network Client entitlement)
- v0 storage architecture: `KeyStore` protocol + UserDefaults default impl
- v0 UI shape: inline key field in main UI; no Settings scene
- v0 deliverable shape (I2): file-level build-checklist in 4 stages
- v0 timeline: 2-3 days focused work (validated against subtask count)
- Inherited 5-layer architecture: honored; v0 components map to layers per SP4

### Eliminated Options

- Keychain backing in v0
- Settings scene in v0
- Unsandboxed v0
- High-level component list as I2 deliverable
- Notarization in v0
- Multi-provider client in v0 (deferred to v1)
- Local LLM in v0 (deferred to v2)
- Cross-platform abstraction (out of scope by C4)

### Remaining Paths

- v0 ships with UserDefaults default backing through KeyStore protocol
- v0 offers paste-each-session as alternative impl (developer's choice)
- The Storage Strategy Decision Matrix becomes part of the finding's deliverable
- I2 build-checklist gets organized into ~50-60 file-level subtasks

## SV5 — Constrained Understanding

The inquiry stabilizes to two committed deliverables:

**I1 deliverable shape:**
- Storage Strategy Decision Matrix (5 options × 4 axes; security × UX × persistence × portability)
- Recommended approach: `KeyStore` protocol + UserDefaults v0 impl
- Explicit threat-model reasoning (dev-self vs distributed)
- Per-phase recommendation table (v0 / v0.5 / v1 / v1.5 / v2)
- Sandbox-on-day-1 decision noted as part of the same I1 frame

**I2 deliverable shape:**
- v0 build-checklist (4 stages × ~12-15 subtasks/stage)
- File-level granularity with explicit per-subtask dependency
- Maps to inherited 5-layer architecture (SP4)
- Excludes pause/resume + project model + Keychain + Settings + notarization (all deferred per substrate + ambiguity resolutions)

**Phase boundaries clarified (output for /traverse Next-Phase pointers):**
- v0 = dev-self runnable (working translation flow; UserDefaults-backed key)
- v0.5 = persistence polish (Keychain swap via KeyStore protocol; Settings scene; fileImporter)
- v1 = distribution + multi-provider + 3-tier triage v1 features + FileDocument package
- v1.5 = reading screen + multi-translation collation
- v2 = local LLM + Quick Look + iCloud Drive

---

## Phase 5 — Conceptual Stabilization

### Inherited Commitments Re-test

| Prior commitment (from `2026-06-15_16-48__comprehenslate_mac_app_design/finding.md`) | Verdict | Note |
|---|---|---|
| 5-layer architecture (Project shell / Config / Execution / Reading & output / Quality) | CONFIRMED | v0 components map cleanly per SP4; no architecture revision needed |
| Mac-native + Apple Silicon (arm64) commitment | CONFIRMED | v0 is arm64-only by build setting |
| Project-as-data-model commitment | DEFERRED to v1 | v0 doesn't violate, just doesn't yet honor (intentional per phasing — `.compldoc` FileDocument package is v1) |
| 3-tier triage (essential / differentiating / deferrable) | DEFERRED to v1 | v0 contains v1's "essential" tier primitives only (translate + save); the triage system itself is v1+ |
| 10 principle-derived features | DEFERRED to v1+ | v0 implements 0 of 10 (intentional — they're v1+ per phasing) |
| BYO API key model | REFINED at v0 (CONFIRMED for shape) | v0 implements BYO via KeyStore + UserDefaults default; AE1 prior synthesis flag (from `2026-06-15_19-17__user_research_persona_validation` finding) re-surfaces — does NOT block v0 (dev-self); should be re-tested before v1 (distributed) |
| Mac-native typography for reading screen | DEFERRED to v1.5 | v0 uses default TextEditor (acceptable for v0 single-translation scope) |
| AE2 3-tier triage re-tier needed (prior synthesis flag) | NOT TRIGGERED at v0 | v0 doesn't trigger the triage system; v1 inquiry should adjudicate |

### Accommodation trigger check

Did new perspectives keep producing destabilizing anchors forcing model revision? **NO** — Phase 2 perspectives produced new anchors (phase-dependence; KeyStore protocol economics; sandbox-cheap-now-expensive-later) that *refined* the model; Phase 3 ambiguity collapse resolved 7 ambiguities each with structural counter-test. The model converged cleanly. Accommodation trigger NOT FIRED.

### Failure mode self-check

| Mode | Fired? | Note |
|---|---|---|
| Status Quo Bias | NO | Inquiry challenged the inherited Keychain commitment with structural grounds; resolution differs from substrate (KeyStore protocol + UserDefaults at v0, deferring Keychain to v0.5) |
| Premature Stabilization (early-clarity-arrival axis) | NO | Phase 2 produced 7 new anchors; 7 ambiguities resolved with explicit counter-tests; SV1→SV6 delta is substantial |
| Premature Stabilization (model-misfit axis) | NO | No revision pattern; model converged on first pass through phases |
| Anchor Dominance | NO | Recommendation rests on 5+ anchors (KI1 demotion + KI2 structural delta + KI5 phase-dep + KI6 protocol-decoupler + FP1 asymmetric failure); removing any single anchor leaves the recommendation supported |
| Perspective Blindness | NO | Risk/Failure perspective surfaced distinct anchors (distribution-readiness gap); Resource/Feasibility surfaced timeline-fragility anchor; Phase/Calibration-State perspective surfaced phase-dep anchor — none of these would have appeared from Technical/Logical alone |
| Clean Resolution Trap | NO | Ambiguity 4 explicitly noted as MEDIUM confidence with the counter retaining structural merit |
| Self-Reference Blindness | NO | Sensemaking framework is external to Mac-app design framework |

## SV6 — Stabilized Model

### The committed model

**(1) Storage strategy for v0 BYO API key** is decomposed as:
- A 5-option × 4-axis Decision Matrix (Section in finding)
- The right choice is PHASE-DEPENDENT
- For v0 (single-user dev Mac, no distribution scaffold): UserDefaults `@AppStorage` is the right backing; Keychain is over-engineered
- The `KeyStore` protocol (~10 lines) is introduced **in v0** to decouple the storage from the UI, making v0→v0.5 swap a 1-file change
- Paste-each-session is offered as an alternative `KeyStore` impl the developer can choose for security-prudence
- Per-phase recommendation: v0 = UserDefaults default; v0.5 = Keychain swap (mechanical); v1+ = Keychain + multi-provider

**(2) SwiftUI v0 subtasks** are decomposed as:
- ~50-60 file-level subtasks in 4 stages
- Stage 1: Xcode-setup (~10-12 subtasks; new project, signing, capabilities, entitlements, arm64, deployment target)
- Stage 2: File-creation (~15-20 subtasks; 6-7 .swift files with stubbed content)
- Stage 3: Wiring (~15-20 subtasks; connect state, networking, error handling, UI flow)
- Stage 4: Run-and-test (~5-8 subtasks; compile, fix warnings, paste key, translate sample, save .md, verify)
- Mapped to inherited 5-layer architecture (Project shell / Config / Execution / Reading & output / Quality)
- Excludes: pause/resume, project model, Keychain, Settings scene, notarization, multi-provider, local LLM, FileDocument, reading-screen typography (all deferred per their respective phases)

**(3) v0 timeline** = 2-3 days focused work; achievable with above exclusions.

**(4) Three phase-boundary frontier decisions resolved:**
- F1 Settings scene in v0? → **NO** (deferred to v0.5)
- F2 KeyStore protocol in v0? → **YES** (introduced in v0)
- F5 Sandbox in v0? → **YES** (App Sandbox + Network Client entitlement)

**(5) Inherited 5-layer architecture is honored** — v0 components map cleanly to layers; no re-architecture needed.

**(6) Methodological motivation honored** — recommendation is defended on structural grounds (threat-model + KeyStore-as-decoupler + asymmetric-failure economics); the "common pattern" anchor is explicitly demoted to social-convention.

### Difference from SV1

SV1 read the question as a yes/no Keychain decision + a flat enumeration request. SV6 reframes:
- I1 is a 5-option decision matrix with phase-dependent recommendations + an architectural protocol decision (KeyStore in v0)
- I2 is a file-level build-checklist organized by stage, not a flat list
- The decision is structurally defended (not convention-driven)
- v0 timeline is validated against subtask count
- The Mac-app finding's 5-layer architecture survives the v0 phasing intact

### Saturation indicators

- **Perspective saturation:** 8 perspectives applied; the last 2 (Definitional/Internal Consistency + Phase/Calibration-State) produced new substantive anchors (KI5 phase-dep). Not saturated — but adding a 9th perspective (e.g., Long-term Maintenance) would likely confirm rather than expand. Acceptable stopping point.
- **Ambiguity resolution ratio:** 7 ambiguities identified; 7 resolved (5 HIGH confidence; 1 MEDIUM with explicit counter-retention; 1 HIGH). Ratio: 7/7. Healthy.
- **SV delta:** SV1→SV6 is substantial — reframed from yes/no to matrix; reframed from flat list to staged checklist; introduced KeyStore protocol commitment; phase-conditioned all storage recommendations.
- **Anchor diversity:** 9 constraints + 9 key insights + 6 structural points + 6 foundational principles + 6 meaning-nodes; from 8 perspectives. Healthy diversity.

### Verdict

**PROCEED.**

Telemetry: SV6 stable; 7 ambiguities resolved; 6 failure modes checked NONE fired; 0 frontier flags remaining unresolved; ready for Decomposition.
