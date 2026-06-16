---
status: active
model: claude-opus-4-7
effort: unknown
refines: devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/finding.md
revised: 2026-06-16
---

# Finding: SwiftUI v0 — API-key storage strategy + build subtasks

## Post-conclusion Correction Notice (2026-06-16)

This finding inherited its product framing from the prior Mac-app design finding, which scoped the product to religious / theological texts. That framing was incorrect — Comprehenslate is a generic translation product per `SKILL/SKILL.md` ("works for any source document; treat the calibration corpus as a tuning anchor, not the product's scope"). The religion-scoped framing was diagnosed at `devdocs/inquiries/2026-06-16_09-08__loop_diagnose__persona_religion_overfit/finding.md`.

**What was preserved:** the entire substantive content of this finding — the v0 Storage Strategy Decision Matrix, the KeyStore protocol + UserDefaultsBacking / InMemoryBacking design, the sandbox-on-day-1 decision, the 45 file-level build subtasks across 4 stages, the 3 emergent observations (KeyStore-as-transition-primitive; sandbox-broader-than-reasoned; v1-as-distribution-gate-for-AE1/AE2), the per-phase storage recommendation table, and the phase roadmap. All decisions are domain-neutral and apply to any translation product, generic or calibration-corpus-specific.

**What was edited surgically:** the "Why we're discussing this" framing paragraph (the product description); the example Swift `ClaudeClient` prompt's "theological or technical terms" instruction (broadened to "specialized terminology and technical terms"); the v1.5 reading-screen scope description (broadened from "Quranic citation rendering, theological-text register support" to generalized mixed-script + register-alternation cases).

The Swift code, the Xcode setup subtasks, the wiring instructions, and the run-and-test verification path are entirely unchanged — they're already domain-neutral.

---

## Changes from Prior

**Prior path:** `devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/finding.md`

**Revision trigger:** User asked to dive deep into the v0 SwiftUI phasing that was produced as conversation context after the prior Mac-app design inquiry concluded. The user specifically questioned the v0.5 → Keychain commitment ("is Keychain required? why not paste-each-session? maybe the question is where to save it?") and asked for an enumeration of SwiftUI subtasks.

**What's preserved:**
- The 5-layer architecture commitment (Project shell / Config / Execution / Reading & output / Quality) from the Mac-app finding — v0's file structure maps cleanly to these layers.
- The Mac-native + Apple Silicon (arm64) commitment.
- The BYO API key model (no server-side storage; no account/login).

**What's changed:**
- The conversation-substrate v0.5 → Keychain commitment is **REFINED**, not rubber-stamped. v0 is now committed to introduce a `KeyStore` protocol so the v0 → v0.5 storage swap becomes mechanical, but the v0 backing is `UserDefaultsBacking` (not Keychain). Keychain swap moves to v0.5.
- The "common pattern that Mac apps use Keychain" anchor is explicitly demoted to social-not-structural; the recommendation rests on threat-model reasoning, not convention.
- v0 is committed to ship sandboxed (App Sandbox + Network Client entitlement) from day 1 — a small upfront cost that prevents downstream rework.

**What's new:**
- A 5-option × 4-axis Storage Strategy Decision Matrix (Security × UX × Persistence × Portability).
- A per-phase storage recommendation table (v0 / v0.5 / v1 / v1.5 / v2) with explicit transition mechanisms.
- A KeyStore protocol Swift code spec with two v0 implementations (UserDefaultsBacking default + InMemoryBacking paste-each-session alternative).
- A file-level build-checklist (~45 actionable subtasks in 4 stages: Xcode-setup / File-creation / Wiring / Run-and-test).
- Three emergent observations: (E1) KeyStore as transition primitive; (E2) sandbox-on-day-1 broader than initially reasoned; (E3) v1 is the first distribution phase, gating the persona-validation AE1/AE2 concerns.

**Migration:** None for existing artifacts. The prior Mac-app finding's commitments are honored; v0 implements its first concrete subset.

---

## Question

**From `_branch.md`:**

Two distinct items, kept separate but related:

**Item I1 — Re-examine the v0 Keychain commitment.** The conversation-substrate phasing recommended that v0 start with `UserDefaults` storage for the API key and v0.5 swap to Keychain. The user asks: is Keychain required at any phase, or is the deeper question "where to save the API key"? The user signals an anti-rubber-stamp motivation — defend the recommendation on structural grounds, don't just cite Mac-app convention.

**Item I2 — Enumerate the SwiftUI subtasks for v0.** The v0 description ("SwiftUI + URLSession + UserDefaults + plain String I/O → source / translate / save-as-md") is abstract. The user wants a concrete, actionable list of subtasks they can work through to build v0.

**Goal:** a finding the user can act on — for I1, a defended per-option recommendation with explicit threat-model reasoning; for I2, a file-level build-checklist with dependencies. Both items together form the v0 implementation guide.

**Synthesis-mode disclaimer.** This finding is a /traverse-synthesis (an automated cognitive loop's output), not empirical UX research. Storage UX assertions, time estimates, and the Swift code examples are structural reasoning based on platform facts + the user's stated context — not measured. The reader should compile the code at first integration to verify; the matrix's grading rests on documented macOS / Keychain / Sandbox behavior the reader should cross-check against Apple's developer documentation if a decision is high-stakes.

---

## Finding Summary

- **Storage strategy answer (I1).** The right question IS "where to save the API key," not "is Keychain required." Five viable options exist on macOS (Paste-each-session / UserDefaults / Keychain / Application Support file / Environment variable), and the right choice depends on threat model and persistence requirement.

- **v0 recommendation.** Introduce a `KeyStore` protocol (one Swift file, ~10 lines of protocol + ~60 lines of two backings); default backing is `UserDefaultsBacking` (the `@AppStorage` plaintext-in-plist path). The protocol layer is what makes the v0 → v0.5 Keychain swap mechanical — replace one class, no UI rewiring.

- **For the security-prudent developer**, an alternative `InMemoryBacking` (paste-each-session) is offered as a one-line swap — no plaintext at rest, but the developer re-pastes every launch.

- **Why not Keychain at v0.** Keychain is ~30-80 lines of `SecItemAdd` / `SecItemCopyMatching` boilerplate + a first-access modal prompt UX cost. v0's threat model is single-user dev Mac (the developer's own laptop, no distribution scaffold). At that threat model, the encryption-at-rest gain doesn't justify the complexity. Keychain becomes load-bearing at **v0.5** when distribution-readiness work begins.

- **Why not Keychain by default just because Mac apps use it.** The "common pattern" argument is social convention, not structural reasoning. It survives at v0.5+ (when v0.5 starts behaving like a real Mac app for real users), but not at v0 (where the user is the developer).

- **Sandbox-on-day-1.** v0 ships sandboxed (App Sandbox capability + Network Client entitlement) — small upfront cost, prevents a class of downstream surprises when v0.5+ adds file operations, Quick Look extensions, or iCloud Drive integration.

- **NO Settings scene in v0.** The inline key field in the main UI's bottom safeAreaInset is sufficient when there's only one setting to surface; v0.5 introduces Settings when there are 4-6 settings to populate it with.

- **Subtask answer (I2).** ~45 file-level subtasks in 4 stages: Xcode-setup (12) → File-creation (6) → Wiring (~18) → Run-and-test (~7). Six `.swift` files total (`ComprehenslateApp.swift`, `ContentView.swift`, `KeyStore.swift`, `ClaudeClient.swift`, `Models.swift`, `TranslationError.swift`), mapped to the inherited 5-layer architecture.

- **Timeline (extrapolated, not measured).** ~2-3 focused days for v0; achievable IF Keychain + Settings scene + notarization are all deferred to later phases.

- **Three emergent observations carried forward.**
  - **E1 KeyStore-as-transition-primitive.** The protocol is the architectural pivot for all storage transitions (v0 → v0.5 Keychain swap; v1 multi-provider keys). One small abstraction at v0 enables clean evolution.
  - **E2 Sandbox-on-day-1 broader than initially reasoned.** Beyond preventing sandbox-test rework, sandbox-from-v0 enables clean later integration of NSSavePanel security-scoped bookmarks, fileImporter, Quick Look extensions, and iCloud Drive coordination.
  - **E3 v1 is the first distribution phase.** Per the suggested roadmap, v1 introduces multi-provider distribution. The prior persona-validation finding flagged AE1 (BYO key model) and AE2 (3-tier triage) as synthesis-grade concerns requiring real-translator research **before** v1 commit. v0 + v0.5 are both dev-self and don't trigger these flags.

- **Reader's path.** Read sections 1 (storage decision rationale) + 2 (decision matrix) + 3 (per-phase recommendation) for I1. Read sections 4 (KeyStore code) + 5 (build-checklist) for I2. Read section 6 (inherited commitments re-test) + section 7 (phase roadmap) for the relationship to the broader product plan. Read the Open Questions section last.

---

## Finding

**Why we're discussing this.** The product (Comprehenslate, a general-purpose AI-assisted translation tool that uses LLMs to translate any source document into multiple target languages while preserving register, terminology, and structural form per a configurable `TranslationConfig`; currently calibrated against religious-philosophical prose such as Said Nursi's *Risale-i Nur* as its tuning anchor, but designed for any document) was sketched as a Mac-native app in a prior /traverse inquiry. That earlier finding committed to a 5-layer architecture and a Mac-native build target. After concluding, the conversation produced a suggested phasing for actually building the app: v0 in days, v0.5 in a week, v1+ in weeks-to-months. The phasing recommended starting with `UserDefaults` for the API key and swapping to Keychain at v0.5. The user pushed back — that's the inquiry this finding answers.

The finding has two main bodies (one per inquiry item) plus supporting material.

### 1. Storage strategy — the decision rationale

The user reframed the question correctly: it's not "is Keychain required?" but "where to save the API key?" The Keychain option is one answer among several. Five viable options exist for BYO API key storage on macOS:

- **Option A. Paste-each-session** — no persistence; the key is held in process memory while the app runs, gone on quit.
- **Option B. UserDefaults via `@AppStorage`** — persistent, one-line Swift, stored as plaintext in the per-app plist file.
- **Option C. Keychain Services** — persistent, encrypted at-rest with a per-Mac key, gated by a per-app access control list.
- **Option D. Application Support file** — a self-rolled JSON file in `~/Library/Application Support/<app>/`. Plaintext by default; can be encrypted with a user passphrase.
- **Option E. Environment variable** — read at launch from `ProcessInfo.processInfo.environment`. Never written to disk by the app, but only works for terminal- or Xcode-launched apps (GUI Finder launch doesn't inherit user shell environment).

The right choice depends on two factors:

**(a) Threat model.** v0's user is the developer themselves. There is no distribution scaffold yet — no notarized DMG, no signed installer, no Mac App Store target. A motivated developer COULD copy the `.app` bundle to a friend and have the friend right-click → Open to bypass Gatekeeper (the personal-team-signed binary will run with manual override), but this is intent + friction, not structural impossibility. For v0, the practical threat model is "is the developer's own Mac compromised?" — the same threshold that applies to any other unencrypted file the developer holds (.env files, terminal history, Xcode keychain).

**(b) Persistence requirement.** "Paste once per work session" is annoying but acceptable. "Paste once and remember" is the ergonomic default for daily use.

For v0 (single-user dev Mac), Option A or B both work. Option B (UserDefaults via `@AppStorage`) is the ergonomic default. Option A (paste-each-session) is the security-prudent alternative for developers who don't want plaintext key on disk.

**The "common pattern" rebuttal.** Many production Mac apps (Raycast AI, BoltAI, MacGPT) use Keychain for credentials. This convention is real, but it's social — not structural. The convention applies when the app is a distributed product with arbitrary users. At v0, the developer is not "arbitrary users" and is not surprised by deviation from convention. The convention argument re-applies starting at v0.5 (when distribution-readiness work begins).

### 2. Storage Strategy Decision Matrix

5 options × 4 axes. Threat-model assumptions for grading are stated below the matrix.

| Option | Security | UX | Persistence | Portability |
|---|---|---|---|---|
| **A. Paste-each-session** (in-memory only) | **Strong.** No plaintext at rest anywhere; key lives in process memory only while running; gone on quit. No backup-channel exposure. | **Annoying.** Paste on every launch (~10-30 sec friction per session); easy to forget; hostile to "open app, use immediately" flow. | **Zero.** Discarded on quit; no recovery; not portable. | **High.** Works regardless of sandbox; no platform-API tie; trivially portable to any language/platform. |
| **B. UserDefaults `@AppStorage`** | **Weak.** Plaintext plist. **In v0 (sandboxed):** stored inside the per-app container at `~/Library/Containers/<bundle-id>/Data/Library/Preferences/<bundle-id>.plist`. **In an unsandboxed app:** stored at `~/Library/Preferences/<bundle-id>.plist`. Either way, the file is plaintext; sandbox container provides additional per-app isolation (other sandboxed apps can't read in) but same-user processes running outside sandbox can. Time Machine backs the file up plaintext; explicit-opt-in iCloud sync via `NSUbiquitousKeyValueStore` would sync plaintext too. | **Best.** Paste once, remembered forever; `@AppStorage("key")` is one line of Swift; no modal prompts. | **High.** Persists indefinitely until cleared by user or app uninstall. | **High.** Works sandboxed (per-app domain is sandbox-aware); standard Foundation API; semantics translate well to other platforms. |
| **C. Keychain Services** | **Strong.** Encrypted at-rest with a per-Mac key (derived from the user's login keychain password). Per-app access control list gates which apps can read it. Time Machine backups travel encrypted; iCloud Keychain sync is opt-in per item. Optional Touch ID gating via `SecAccessControl`. First-access prompts a system modal one time, then silent. | **Acceptable but heavier.** Provides a "this is secure" affordance the user can verify (visible in Keychain Access.app). First-access modal is brief. UX surface is bigger if a real management UI is added (Settings panel + "Forget key" + maybe a "View in Keychain Access.app" affordance). | **Highest.** Persists across reinstalls (Login Keychain survives app deletion; user removes via Keychain Access.app). | **Adequate.** Works sandboxed with an optional `keychain-access-groups` entitlement for sharing. API is fiddly Swift wrapping — typically 30-80 lines of `SecItemAdd` / `SecItemCopyMatching` boilerplate around CFTypeRefs. Mac-only — Linux/Windows would need separate secret-store integration. |
| **D. Application Support file** (self-rolled JSON at `~/Library/Application Support/<app>/key.json`) | **Weak (default).** Plaintext JSON on disk unless app adds its own encryption layer. Sandbox isolates the path to the per-app container; file remains plaintext within. Adding encryption adds passphrase UX cost. | **Acceptable.** Paste once into Settings; file managed transparently; less ergonomic than `@AppStorage` (requires URL handling + Codable file I/O). | **High.** Persists until file deleted or user uninstalls; manual portability between Macs by copying the file. | **Adequate.** Sandbox provides per-app container path via `URL.applicationSupportDirectory`; pattern is platform-portable (analogous paths on Linux `$XDG_CONFIG_HOME` / Windows `%APPDATA%`). |
| **E. Environment variable** (read at launch via `ProcessInfo.processInfo.environment`) | **Strong.** Never written to disk by app; existence depends on launcher (terminal, Xcode scheme, launchd plist). Mac doesn't read user shell env on GUI Finder-launch by default — risk surface is launcher-controlled. | **Hostile to non-technical users.** Requires shell config (`~/.zshrc`) or Xcode scheme env-vars; can't be set from inside the app; user must edit a text file or open Xcode to change. | **Per-session.** Depends on launcher setting; not persistent across Mac reboots without shell-config persistence; reset per new terminal. | **Adequate.** Works for terminal-launched apps; pattern is universal across platforms; doesn't work cleanly for double-click Finder-launch without an env-injection hack like a `launchd.plist` user-agent. |

**Threat-model assumptions for grading.** "Plaintext on disk" risk applies when an adversary has read access to the user's home directory — malware running as the user, offline disk forensics on an unlocked disk, or stolen backup access. App Sandbox per-app container provides process-level isolation between sandboxed apps but does NOT encrypt the container at rest — the user themselves and same-user processes can read into per-app containers. The per-Mac Keychain encryption key derives from the user's login keychain password and is not retrievable without that password (or biometric unlock). iCloud sync of UserDefaults uses `NSUbiquitousKeyValueStore` (opt-in via Capabilities), not the standard `UserDefaults.standard` — defaulting to standard UserDefaults does not trigger iCloud sync.

### 3. Per-phase storage recommendation

| Phase | Recommended approach | Rationale |
|---|---|---|
| **v0** (days; dev-self) | `KeyStore` protocol + `UserDefaultsBacking` (default) **OR** `InMemoryBacking` (security-prudent alternative; one-line swap) | Threat model = single-user dev Mac; plaintext-at-rest risk is the developer's accepted risk. Matrix Option B is max-UX + High-persistence + High-portability for ergonomic dev iteration. Option A (`InMemoryBacking`) is the Strong-security alternative. The protocol layer makes the choice swappable and enables v0.5 transition with no UI rework. |
| **v0.5** (~1 week; persistence polish) | `KeyStore` protocol + `KeychainBacking` (replace one class) | Approaching distribution-readiness — start treating the threat model as "could ship to others." Matrix Option C Strong-security + Highest-persistence becomes worth the modal-prompt UX cost. Add a dedicated Settings scene now since there are >1 settings to put in it (target language, model selection, "use Keychain" toggle). |
| **v1** (weeks; distribution + multi-provider) | `KeyStore` protocol scaled to multi-provider (one Keychain entry per provider) | Multiple providers (Anthropic + OpenAI + others) each get a `KeychainBacking` instance keyed by provider name. Protocol scales: `KeyStore(provider: .anthropic)` / `KeyStore(provider: .openai)`. |
| **v1.5** (weeks; reading screen) | Unchanged from v1 | No storage delta — reading-screen typography work doesn't touch key storage. |
| **v2** (months; local LLM) | Unchanged from v1 for API keys; add `LocalLLMConfig` for model paths via Application Support file (Option D) | Local LLM doesn't need an API key for inference; model paths are configuration, not credentials. Option D (file) is correct for non-secret config. |

**Transition mechanism from v0 to v0.5 (specifically — the one most likely to surprise the developer):**

The swap happens in two layers.

(1) **Implement `KeychainBacking: KeyStoreBacking`** — 30-80 lines using `SecItemAdd` / `SecItemCopyMatching` / `SecItemDelete`. Keep it in a new file or extend `KeyStore.swift`.

(2) **Change the App-level wiring** — in `ComprehenslateApp.swift`, change:

```swift
@State private var keyStore = KeyStore(backing: UserDefaultsBacking())
```

to:

```swift
@State private var keyStore = KeyStore(backing: KeychainBacking())
```

(3) **Migration of the existing v0 key.** First v0.5 launch will find the Keychain entry empty (no key yet) but the v0 UserDefaults plist still holds the old key. Without migration the user has to re-paste. A clean migration is to do it ONCE at App launch, NOT in `KeyStore.init` (which doesn't know about backing types). The migration belongs at the App layer:

```swift
// In ComprehenslateApp.init or a .task modifier:
if let oldKey = UserDefaults.standard.string(forKey: "anthropic_api_key"), !oldKey.isEmpty {
    // 1. Write to Keychain via the new KeychainBacking
    let migratedStore = KeyStore(backing: KeychainBacking())
    migratedStore.apiKey = oldKey
    // 2. Delete from UserDefaults
    UserDefaults.standard.removeObject(forKey: "anthropic_api_key")
}
```

Run this once on first launch (gate with a `UserDefaults` flag like `migration_v0_5_done`). Verify by checking Keychain Access.app for the new entry and confirming the plist no longer contains the key.

### 4. KeyStore protocol + implementations (Swift code)

**Code disclaimer.** The code below is syntactically valid Swift 5.9+ targeting macOS 14+ and follows current SwiftUI Observable patterns. It has NOT been compiled by this synthesis. Treat as structural template; verify-by-compile at first integration. Specifically: confirm that the `@Observable` macro's expansion preserves `didSet` semantics correctly on the `apiKey` property (if it triggers an unnecessary `backing.write("")` call during init, wrap with an `isInitialized` flag).

**File: `KeyStore.swift`**

```swift
import Foundation
import Observation

@Observable
final class KeyStore {
    var apiKey: String {
        didSet { backing.write(apiKey) }
    }

    private let backing: KeyStoreBacking

    init(backing: KeyStoreBacking = UserDefaultsBacking()) {
        self.backing = backing
        self.apiKey = backing.read() ?? ""
    }

    func clear() {
        apiKey = ""
        backing.clear()
    }

    var hasKey: Bool { !apiKey.isEmpty }
}

protocol KeyStoreBacking {
    func read() -> String?
    func write(_ value: String)
    func clear()
}

// v0 DEFAULT: persistent via UserDefaults plist (plaintext, sandboxed container)
struct UserDefaultsBacking: KeyStoreBacking {
    private let key = "anthropic_api_key"

    func read() -> String? {
        UserDefaults.standard.string(forKey: key)
    }

    func write(_ value: String) {
        UserDefaults.standard.set(value, forKey: key)
    }

    func clear() {
        UserDefaults.standard.removeObject(forKey: key)
    }
}

// v0 ALTERNATIVE: in-memory only (paste-each-session)
final class InMemoryBacking: KeyStoreBacking {
    private var value: String?

    func read() -> String? { value }
    func write(_ value: String) { self.value = value }
    func clear() { value = nil }
}

// v0.5 STUB — implement at v0.5 swap, not v0:
//
// final class KeychainBacking: KeyStoreBacking {
//     private let service = Bundle.main.bundleIdentifier ?? "com.comprehenslate.app"
//     private let account = "anthropic_api_key"
//
//     func read() -> String? {
//         // SecItemCopyMatching with kSecClass: kSecClassGenericPassword
//         // service = service, account = account
//         // Return data decoded as UTF-8 String
//         return nil
//     }
//
//     func write(_ value: String) {
//         // Try SecItemUpdate first; if not found, SecItemAdd
//         // Set kSecAttrAccessible to kSecAttrAccessibleWhenUnlockedThisDeviceOnly
//     }
//
//     func clear() {
//         // SecItemDelete with service + account
//     }
// }
```

**Usage in `ComprehenslateApp.swift`:**

```swift
import SwiftUI

@main
struct ComprehenslateApp: App {
    @State private var keyStore = KeyStore()  // v0 default: UserDefaults backing

    // v0 alternative for security-prudent variant:
    // @State private var keyStore = KeyStore(backing: InMemoryBacking())

    // v0.5 swap (commented; uncomment when KeychainBacking implemented):
    // @State private var keyStore = KeyStore(backing: KeychainBacking())

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(keyStore)
        }
    }
}
```

**Design rationale.**
- `KeyStore` is annotated `@Observable` (from Swift's `Observation` framework, macOS 14+) so SwiftUI views can bind to its `apiKey` property using `@Bindable`.
- The `didSet` observer on `apiKey` propagates writes through the backing — keeps the UI binding simple.
- `KeyStoreBacking` is the swap point: change one line in `ComprehenslateApp.swift` to switch backings; the rest of the app (ContentView, ClaudeClient) is unchanged.
- `UserDefaultsBacking` is a `struct` (stateless wrapper around the `UserDefaults.standard` singleton); `InMemoryBacking` is a `class` (holds value in memory).
- Concurrency: `UserDefaults.standard` is thread-safe; `didSet` fires on whichever thread set `apiKey` (typically MainActor since the binding is from SwiftUI). Pasting a new key during an in-flight Translate call is safe — the in-flight task already captured the old key as a String value at call time; the next Translate uses the new key.

### 5. v0 build-checklist (45 file-level subtasks)

**Stage 1 — Xcode-setup (12 subtasks)**

1. Xcode → File → New → Project → macOS tab → App template → Next.
2. Product Name: `Comprehenslate`.
3. Team: select your Apple ID team (required even for local Run).
4. Organization Identifier: `com.eneskux` (or your preferred reverse-DNS) — yields Bundle Identifier `com.eneskux.Comprehenslate`.
5. Interface: SwiftUI.
6. Language: Swift.
7. Storage: None.
8. Tests: uncheck "Include Tests" (defer to a later phase).
9. Save project at a stable location (e.g., `~/Developer/Comprehenslate`).
10. Project navigator → Comprehenslate target → General tab → Minimum Deployment → macOS 14.0.
11. Build Settings tab → search "Architectures" → set "Architectures" to `arm64` (Apple Silicon only) — keeps the binary small and aligns with the prior Mac-app finding's commitment.
12. Signing & Capabilities tab → "+ Capability" → App Sandbox → enable → check "Outgoing Connections (Client)" inside the App Sandbox capability. (This is the sandbox-on-day-1 decision — the cost is tiny here; the benefit pays out across all v0.5+ filesystem features.)

(One-time addendum if shipping a binary later: drag a placeholder 1024×1024 PNG into `Assets.xcassets` → AppIcon → "App Store 1024pt" slot. Xcode auto-scales for other sizes. Skip for v0 if you're not distributing.)

After Stage 1: build (Cmd+B) should succeed with the empty SwiftUI template.

**Stage 2 — File creation (6 subtasks; one per file with stub content)**

13. Replace `ComprehenslateApp.swift` (Xcode-generated template) with the App entry shown in section 4 above — `@main struct ComprehenslateApp: App` holding `@State private var keyStore = KeyStore()`, with `WindowGroup { ContentView().environment(keyStore) }`.

14. Replace `ContentView.swift` with the skeleton structure: `struct ContentView: View` with `@Environment(KeyStore.self) private var keyStore` + `@State` properties for `sourceText`, `translatedText`, `targetLanguage`, `isTranslating`, `errorMessage` + a body returning `HSplitView { sourcePane; translationPane }` + a `.toolbar` modifier + a `.safeAreaInset(edge: .bottom)` modifier for the key field. (Detailed wiring in Stage 3.)

15. Create `KeyStore.swift` (Cmd+N → Swift File) containing the full code from section 4: `@Observable class KeyStore` + `protocol KeyStoreBacking` + `struct UserDefaultsBacking` + `class InMemoryBacking` + KeychainBacking commented stub.

16. Create `Models.swift` (Cmd+N → Swift File) containing the Codable types for the Anthropic Messages API: `struct ClaudeRequest { let model: String; let max_tokens: Int; let messages: [ClaudeMessage] }`, `struct ClaudeMessage { let role: String; let content: String }`, `struct ClaudeResponse { let content: [ClaudeContent] }`, `struct ClaudeContent { let type: String; let text: String }`. All four conform to `Codable` (or `Encodable` + `Decodable` selectively).

17. Create `ClaudeClient.swift` (Cmd+N → Swift File) containing: `final class ClaudeClient { func translate(source: String, target: String, key: String) async throws -> String { /* implementation in Stage 3 */ } }`. Instantiate from ContentView via `@State private var client = ClaudeClient()` — no `.shared` singleton needed for v0.

18. Create `TranslationError.swift` (Cmd+N → Swift File) containing: `enum TranslationError: LocalizedError { case missingKey, networkFailure(Error), apiError(status: Int, body: String?), invalidResponse, decoding(Error) }` with `var errorDescription: String? { ... }` mapping each case to a human-readable string.

**File-to-layer mapping (honors the inherited 5-layer architecture):**

| File | Layer |
|---|---|
| `ComprehenslateApp.swift` | Project shell |
| `KeyStore.swift` | Config |
| `ClaudeClient.swift`, `Models.swift` | Execution |
| `ContentView.swift` | Reading & output |
| `TranslationError.swift` | Quality |

**Stage 3 — Wiring (18 subtasks)**

State bindings in ContentView:

19. Add `@Environment(KeyStore.self) private var keyStore`.
20. Add `@State private var client = ClaudeClient()`.
21. Add `@State private var sourceText: String = ""`.
22. Add `@State private var translatedText: String = ""`.
23. Add `@State private var targetLanguage: String = "English"`.
24. Add `@State private var isTranslating: Bool = false`.
25. Add `@State private var errorMessage: String? = nil`.

Layout:

26. Wrap body in `HSplitView { ... }` for the side-by-side source / translation panes.
27. Left pane: `VStack { Text("Source").font(.headline); TextEditor(text: $sourceText).font(.system(.body, design: .serif)) }`.
28. Right pane: `VStack { HStack { Text("Translation").font(.headline); if isTranslating { ProgressView().scaleEffect(0.7) } }; TextEditor(text: $translatedText).font(.system(.body, design: .serif)) }`.
29. Add a `.toolbar` modifier with: `TextField("Target", text: $targetLanguage).frame(width: 120)`, a Translate `Button { Task { await translate() } }` disabled when `sourceText.isEmpty || !keyStore.hasKey || isTranslating`, and a "Save .md" `Button(action: saveAsMarkdown)` disabled when `translatedText.isEmpty`.

30. **Key-field binding (the gotcha).** Add the bottom safeAreaInset for the API key field. Since `@Environment(KeyStore.self)` gives an immutable reference but `SecureField` needs a `Binding<String>`, create a local `@Bindable` wrapper inside the view body (or in an extracted view) to project the binding properly. The correct pattern in SwiftUI / macOS 14+:

```swift
var body: some View {
    @Bindable var bindableKeyStore = keyStore  // local @Bindable from @Environment'd Observable
    return HSplitView {
        // ... source + translation panes ...
    }
    .toolbar { /* ... */ }
    .safeAreaInset(edge: .bottom) {
        VStack(spacing: 4) {
            if let err = errorMessage {
                Text(err).foregroundColor(.red).font(.caption)
            }
            HStack {
                SecureField("Anthropic API key (sk-ant-...)", text: $bindableKeyStore.apiKey)
                    .textFieldStyle(.roundedBorder)
                Button("Forget", role: .destructive) { keyStore.clear() }
            }
        }
        .padding(8)
    }
    .frame(minWidth: 900, minHeight: 600)
}
```

The `@Bindable var bindableKeyStore = keyStore` line creates a local Bindable wrapper from the environment-injected Observable, and `$bindableKeyStore.apiKey` then projects a usable `Binding<String>`. (A common first attempt is `text: Bindable(keyStore).apiKey`, but that gives back `String`, not `Binding<String>` — it won't compile. Use the local-var-with-`$` idiom instead.)

ContentView actions:

31. Implement `func translate() async`: set `isTranslating = true`, `errorMessage = nil`, `defer { isTranslating = false }`, then:

```swift
do {
    translatedText = try await client.translate(
        source: sourceText,
        target: targetLanguage,
        key: keyStore.apiKey
    )
} catch let e as TranslationError {
    errorMessage = e.errorDescription
} catch {
    errorMessage = error.localizedDescription
}
```

32. Implement `func saveAsMarkdown()`: instantiate `NSSavePanel()`, set `allowedContentTypes = [.init(filenameExtension: "md")!]`, set `nameFieldStringValue = "translation.md"`. On `.OK`, write `translatedText` to the chosen URL via `String.write(to:atomically:encoding:)`.

ClaudeClient implementation:

33. Implement `ClaudeClient.translate(source:target:key:)`:

```swift
var req = URLRequest(url: URL(string: "https://api.anthropic.com/v1/messages")!)
req.httpMethod = "POST"
req.setValue(key, forHTTPHeaderField: "x-api-key")
req.setValue("2023-06-01", forHTTPHeaderField: "anthropic-version")
req.setValue("application/json", forHTTPHeaderField: "Content-Type")

let prompt = """
Translate the following text to \(target). Preserve register, tone, and any \
specialized terminology or technical terms. Return only the translation, no commentary.

---
\(source)
"""

let body = ClaudeRequest(
    model: "claude-opus-4-8",
    max_tokens: 4096,
    messages: [ClaudeMessage(role: "user", content: prompt)]
)
req.httpBody = try JSONEncoder().encode(body)

let (data, response) = try await URLSession.shared.data(for: req)
if let http = response as? HTTPURLResponse, !(200..<300).contains(http.statusCode) {
    let bodyString = String(data: data, encoding: .utf8)
    throw TranslationError.apiError(status: http.statusCode, body: bodyString)
}
let decoded = try JSONDecoder().decode(ClaudeResponse.self, from: data)
return decoded.content.first?.text ?? ""
```

34. (Optional) increase the URLSession timeout if translation calls exceed 60 seconds — configure `URLSessionConfiguration` for long-running requests.

Error-type wiring:

35. Implement `TranslationError.errorDescription` mapping each case to a human-readable string:
- `.missingKey` → "Anthropic API key is missing — paste your key in the field below."
- `.networkFailure(let e)` → "Network failure: \(e.localizedDescription)"
- `.apiError(let status, let body)` → "Anthropic rejected the request (HTTP \(status))" (with body suffix if present)
- `.invalidResponse` → "Anthropic returned an unexpected response shape."
- `.decoding(let e)` → "Failed to decode the response: \(e.localizedDescription)"

36. Add the `.alert("Translation failed", isPresented: ...)` modifier to ContentView body, binding to a derived isPresented:

```swift
.alert("Translation failed", isPresented: Binding(
    get: { errorMessage != nil },
    set: { if !$0 { errorMessage = nil } }
)) {
    Button("OK") { }
} message: {
    Text(errorMessage ?? "")
}
```

**Stage 4 — Run-and-test (7 subtasks)**

37. Compile (Cmd+B). Resolve any warnings. Common gotchas: unused imports; the `@Environment(KeyStore.self)` initializer (this is the macOS 14+ syntax; older `@EnvironmentObject` patterns won't compile against the Observation framework's `@Observable`).

38. First run (Cmd+R). Verify the window appears with an empty source pane (left), empty translation pane (right), a toolbar with Target language field + Translate + Save buttons, and a bottom area with a masked SecureField + a Forget button.

39. Paste a real Anthropic API key (starts with `sk-ant-`) into the SecureField. Verify the field shows dots (masked). Verify the Translate button enables once both source text + key are present.

40. Type a short test sentence into the source pane (e.g., "Merhaba dünya." or "The quick brown fox jumps over the lazy dog.").

41. Click Translate. Verify the ProgressView spinner appears in the right pane's header, the translation appears in the right pane after the API responds (typically 2-5 seconds for short text), and the spinner disappears.

42. Failure-path test. Temporarily clear the API key field — verify the Translate button disables. Then re-enter a deliberately bad key (`sk-ant-invalid`) and click Translate — verify the error alert appears with a 401-mapped message.

43. Click Save .md. Verify NSSavePanel opens with the default filename "translation.md". Choose a save location. Verify the file exists at the chosen location and contents match the right pane.

44. Persistence verification. Quit the app (Cmd+Q) and relaunch (Cmd+R). The SecureField should be pre-filled with your previously pasted key (confirming `UserDefaultsBacking` persistence wiring). If using `InMemoryBacking` instead, the field will be empty after relaunch — verifies that backing too.

(45 implicit — debugging/iteration as needed.)

After Stage 4: v0 is shippable as a local dev tool.

### 6. Inherited Commitments Re-test

This finding inherits commitments from the prior Mac-app design finding. Each commitment is explicitly re-tested below.

- **Commitment:** 5-layer architecture (Project shell / Config / Execution / Reading & output / Quality).
- **Source:** `devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/finding.md`.
- **Re-test status:** RE-TESTED — commitment confirmed.
- **Evidence:** v0's 6 files map cleanly per the file-to-layer table in section 5. No architectural revision required at v0; the 5 layers are honored as soon as the first concrete component exists in each.

- **Commitment:** Mac-native + Apple Silicon (arm64).
- **Source:** Same prior finding.
- **Re-test status:** RE-TESTED — commitment confirmed.
- **Evidence:** v0 build setting committed to arm64-only per Stage 1 subtask 11.

- **Commitment:** Project-as-data-model (`.compldoc` FileDocument package format).
- **Source:** Same prior finding.
- **Re-test status:** INHERITED-WITHOUT-RE-TEST.
- **Reason:** v0 explicitly does not implement project-as-data-model — output is a plain `.md` file via `NSSavePanel`. The commitment is deferred to v1 per the suggested phasing. v0 doesn't violate the commitment, just hasn't reached it yet. Re-test happens at the v1 scoping inquiry.

- **Commitment:** 3-tier triage (essential / differentiating / deferrable feature classification).
- **Source:** Same prior finding.
- **Re-test status:** INHERITED-WITHOUT-RE-TEST.
- **Reason:** v0 implements only v1's "essential" tier primitives (translate + save). The triage system itself is v1+ scope. Re-test happens at the v1 scoping inquiry (which should also re-adjudicate AE2 — see Open Questions).

- **Commitment:** 10 principle-derived features (lineage view, Quality Policies, TM, glossary, harmony viz, etc.).
- **Source:** Same prior finding.
- **Re-test status:** INHERITED-WITHOUT-RE-TEST.
- **Reason:** v0 implements 0 of 10 features (intentional per phasing — features are v1+).

- **Commitment:** BYO API key model.
- **Source:** Same prior finding.
- **Re-test status:** RE-TESTED — commitment confirmed but frame revised.
- **Evidence:** v0 implements BYO via the new KeyStore protocol + UserDefaultsBacking default. The commitment SHAPE (user brings own key; no server-side storage; no account) is unchanged. The FRAME shift: the prior persona-validation finding flagged AE1 (BYO key as the synthesis-flagged single largest concern, with 4/5 synthetic personas critical). This v0 finding acknowledges AE1 but rules that v0's dev-self threat model doesn't trigger AE1's distributed-user concerns. AE1 re-test happens at v1.

- **Commitment:** Mac-native typography for the reading screen (NSTextView via NSViewRepresentable).
- **Source:** Same prior finding.
- **Re-test status:** INHERITED-WITHOUT-RE-TEST.
- **Reason:** v0 uses default `TextEditor` (acceptable for v0's single-translation scope). NSTextView interop committed for v1.5.

- **Commitment (from persona-validation finding):** AE1 — BYO key model is the single largest synthesis-flagged concern.
- **Source:** `devdocs/inquiries/2026-06-15_19-17__user_research_persona_validation/finding.md`.
- **Re-test status:** INHERITED-WITHOUT-RE-TEST.
- **Reason:** v0 dev-self threat model doesn't trigger AE1. The flag is propagated forward to v1 (see Next Actions / MUST).

- **Commitment (from persona-validation finding):** AE2 — 3-tier triage essential tier may need reshuffling.
- **Source:** Same persona-validation finding.
- **Re-test status:** INHERITED-WITHOUT-RE-TEST.
- **Reason:** v0 doesn't implement the triage system; v1 scoping inquiry should re-adjudicate.

### 7. Phase-boundary roadmap (suggested, not binding)

This roadmap is a **suggested progression**, NOT a binding spec. Each phase v0.5+ should be its own scoping inquiry at the appropriate time. The roadmap shows what's IN, what's OUT, and the transition mechanism per phase.

| Phase | Timeline (extrapolated; not measured) | IN scope | OUT scope (deferred from this phase) | Transition mechanism from prior phase |
|---|---|---|---|---|
| **v0** | 2-3 focused days | Source-to-translation flow end-to-end via Anthropic API; `KeyStore` protocol + `UserDefaultsBacking` default; SwiftUI inline UI (no Settings scene); App Sandbox ON + Network Client entitlement; 6 `.swift` files; arm64-only build. | Pause/resume; project model; Settings scene; Keychain swap; multi-provider; FileDocument; reading typography; local LLM; notarization; DMG. | (Initial phase; no prior to transition from.) |
| **v0.5** | ~1 week | Swap `UserDefaultsBacking` → `KeychainBacking` (mechanical 1-file change + ~5-line App-layer migration); add Settings scene (key management UI + target-language default + model selection); add `.fileImporter` to open `.md`/`.txt` source files; save-to-disk default location. | FileDocument package format; multi-provider; reading typography; local LLM; notarization. | Implement `KeychainBacking` class; update `ComprehenslateApp` wiring; add one-time UserDefaults→Keychain migration at App init; create `SettingsView.swift`; wire Settings scene into App body. |
| **v1** | weeks | FileDocument `.compldoc` package format; `Project` data model; Swift Concurrency `Task` for pause/resume mid-translation; multi-provider switching (Anthropic + OpenAI, configurable); v1 essential features per 3-tier triage; **AE1 + AE2 re-tested against real translator research** (see Next Actions / MUST). | Reading typography polish; local LLM; iCloud Drive; cross-platform. | Introduce `.compldoc` directory bundle FileDocument; refactor ContentView to consume Project; add provider switcher + per-provider KeyStore instances; conduct user research per persona-validation R1 onward route BEFORE distribution commit. |
| **v1.5** | weeks | Reading-screen typography (NSTextView via NSViewRepresentable for proper RTL, mixed-script citation rendering (e.g. embedded Arabic, Hebrew, or any non-Latin script within Latin-script body text), and register-alternation support (preserving archaic↔modern or formal↔colloquial shifts within a single document)); multi-translation collation view. | Local LLM; Quick Look extension; iCloud Drive. | Add ReadingView with NSTextView interop; add CollationView for multi-translation layout; integrate with Project document. |
| **v2** | months | Local LLM via llama.cpp Metal bindings (Apple Silicon-optimized inference); Quick Look extension for `.compldoc` files; iCloud Drive folder integration. | Cross-platform expansion (still Mac-only per inherited commitment); TestFlight beta; Mac App Store distribution. | Bundle llama.cpp framework; add LocalLLMSettings + model-path config (Application Support file per matrix Option D); add Quick Look extension target; add iCloud Drive entitlement. |

---

## Next Actions

### MUST

- **What:** Compile and run the v0 code at first integration; verify the corrected `@Bindable` pattern in section 5 subtask 30 actually compiles + binds correctly; verify the `@Observable` `didSet` on `apiKey` does not call `backing.write("")` during init (if it does, add an `isInitialized` flag guard).
- **Who:** The developer (you), at first build of v0.
- **Gate:** Observable — fires at the moment v0 is built for the first time.
- **Why:** The platform-specific code in this finding is structural template, not compiler-verified. Mechanism-Independence Quarantine applies (the finding's confidence in the Swift code rests on structural reasoning about Apple's documented APIs, not on direct verification). Verify-by-compile is the external anchor.

- **What:** Before any v1 distribution commit, conduct real translator user research per the persona-validation finding's onward route R1 (its research plan + interview script). Use the research to re-adjudicate AE1 (BYO key model) and AE2 (3-tier triage reshuffling).
- **Who:** The developer, ahead of the v1 scoping inquiry.
- **Gate:** Condition-bound — fires before the first v1 design commit; specifically before the v1 scoping inquiry runs.
- **Why:** v0 + v0.5 are dev-self by intent; v1 introduces distribution. AE1 and AE2 are synthesis-flagged concerns that explicitly require empirical evidence before being committed-against or dismissed at distribution scope. Skipping this step risks shipping v1 with the AE1 concerns the persona-validation synthesis surfaced.

### COULD

- **What:** Document the synthesis methodology learning A3 — "code in synthesis findings should be flagged with a verify-by-compile step in the reader's path" — as a project-level methodology note for future /traverse inquiries that produce code-as-output.
- **Who:** The user (or a future inquiry on /traverse methodology improvements).
- **Gate:** Time-bound — after 2-3 more /traverse inquiries surface the same issue, promote to a permanent methodology note.
- **Why:** This inquiry's Critique surfaced A3 as a recurring pattern. Documenting it prevents future inquiries from repeating the verification gap.

- **What:** Carry the KeyStore-as-transition-primitive design pattern (E1 emergent from section 4) into a project-level design-patterns document for future phase-transitioned components (e.g., LLM provider switching at v1; local-vs-API model selection at v2).
- **Who:** The developer, at future design decisions.
- **Gate:** Condition-bound — when designing any future component that faces v0→v0.5→v1 evolution, apply the same protocol + backing pattern.
- **Why:** E1 generalizes — any phase-transitioned component benefits from the same architectural shape.

- **What:** Carry the sandbox-on-day-1 principle (E2 emergent) into project conventions — default to sandbox-ON for new Mac app projects unless explicitly contraindicated.
- **Who:** The developer, on future Mac app starts.
- **Gate:** Condition-bound — applies to any new Mac project.
- **Why:** E2's concrete examples (NSSavePanel security-scoped bookmarks; fileImporter; Quick Look; iCloud Drive) all benefit; the principle generalizes beyond this specific project.

- **What:** Document the 5-option Storage Strategy Decision Matrix (section 2) as a reusable artifact for any future Mac app facing BYO API key storage decisions.
- **Who:** The developer (or a future cross-cutting design-patterns inquiry).
- **Gate:** Condition-bound — when starting a new Mac app with BYO credential storage.
- **Why:** The matrix has reuse value beyond Comprehenslate; storing it as a per-inquiry artifact alone loses the reuse.

### DEFERRED

- **What:** Scope a v0.5 phase inquiry covering Keychain swap + Settings scene + fileImporter + save-to-disk default.
- **Gate:** Condition-bound — fires when v0 is a working baseline and the user is ready to move toward distribution-readiness work.
- **Why (if revived):** Mechanical KeyStore impl swap is small in code-lines but big in surrounding UX work (Settings scene, key management, migration). A dedicated scoping inquiry adjudicates v0.5's specific scope without inheriting unverified assumptions from this finding's suggested roadmap.

- **What:** Scope a v1 distribution + multi-provider inquiry.
- **Gate:** Condition-bound — gated on v0.5 shipped AND on AE1/AE2 real-research findings (the MUST item above).
- **Why (if revived):** v1 is the first distribution phase; AE1 + AE2 must be adjudicated against empirical evidence before v1 spec commits.

- **What:** Scope a v1.5 reading-screen typography inquiry.
- **Gate:** Condition-bound — fires when v1 is shipped.
- **Why (if revived):** NSTextView interop is non-trivial and warrants its own scoping work.

- **What:** Scope a v2 local-LLM inquiry.
- **Gate:** Condition-bound — fires when v1.5 is shipped.
- **Why (if revived):** Months-out work; significant architectural decisions (model bundling; inference threading; Metal compute integration).

- **What:** Investigate cross-platform secret-store integration (Linux secret-service / Windows Credential Manager).
- **Gate:** Condition-bound — fires only if and when the Mac-only commitment is relaxed and cross-platform expansion is scoped.
- **Why (if revived):** The `KeyStore` protocol shape generalizes; the new work is per-platform backing implementation.

---

## Reasoning

**Why "where to save it" is the right reframe of the user's question.** The user asked "is Keychain required?" but the matrix in section 2 makes clear that Keychain is one of 5 viable options. Treating the question as binary (Keychain yes/no) hides the option space. The user's own phrasing ("maybe the question is where to save it") was the correct reframe; the finding's structure follows that reframe.

**Why UserDefaults default for v0 (and not paste-each-session).** The Sensemaking discipline considered paste-each-session as a defensible alternative at MEDIUM confidence — the security-prudent argument is real (no plaintext at rest anywhere) and the counter (paste-per-launch friction) is real too. The finding's choice: offer both via the same protocol; default to UserDefaults (ergonomic) since the dev-self threat model accepts the plaintext risk; document paste-each-session as a one-line swap for the security-prudent variant. The reader can pick. Innovation's piece-level Inversion-candidate considered calendar-driven phasing (use whatever is fastest at each phase) and rejected it on structural grounds — threat-model is structural, calendar is arbitrary.

**Why Keychain is rejected at v0 (and not just rubber-stamped from v0.5+).** Three reasons. First, Keychain Services API is fiddly Swift wrapping — typically 30-80 lines around `SecItemAdd`/`SecItemCopyMatching` CFTypeRef boilerplate — non-trivial for v0's tight budget. Second, the first-access modal adds UX friction that buys nothing at dev-self (the developer is not surprised). Third, the "common pattern" justification (Mac apps use Keychain) is social convention, not structural reasoning — it passes the bar at v0.5+ (when the user becomes "anyone") but doesn't at v0 (when the user is "the developer"). The Sensemaking Phase 3 Ambiguity 2 explicitly tested this and concluded that "common pattern" arguments require phase-conditioning.

**Why the KeyStore protocol IS justified at v0 (even though some might call it YAGNI).** The whole v0.5 plan rests on a Keychain swap. Without a protocol, every UI binding that touches the key (the v0 SecureField; the v0.5 Settings field; v1's multi-provider key bindings) requires re-wiring at swap time. With the protocol, the swap is a one-file replacement. Cost: ~10 lines of protocol + ~60 lines of two backings. Benefit: zero UI re-wiring at v0.5 and v1. The economics favor the protocol.

**Why no Settings scene at v0.** The Sensemaking Phase 3 Ambiguity 5 tested this. A Settings scene adds 2-4 hours of work (Settings { ... } + Form + Section + per-setting bindings). At v0 with one setting (the key) — already presented inline in `safeAreaInset` — Settings would be a scene with one field. Settings becomes valuable at v0.5+ when there's 4-6 things (target language preferences, model selection, output directory default, "use Keychain" toggle, multi-provider keys). Building Settings at v0 is paying full cost for an empty scene.

**Why sandbox-on-day-1.** Sensemaking Phase 3 Ambiguity 6 tested this. Turning sandbox ON later requires re-testing every file operation, every entitlement, every URL the app touches — surprise sandbox failures at v0.5+ are real (NSSavePanel security-scoped bookmark behaviors; file URLs that need bookmark persistence; etc.). v0's required capabilities are minimal (just Network Client for the LLM API call). Toggling sandbox + adding the entitlement is a 5-minute Xcode operation. The savings is "zero downstream rework for sandbox surprises." The Innovation Phase 3.5 Assembly observation E2 broadens this — the principle covers NSSavePanel bookmarks, fileImporter, Quick Look extensions, iCloud Drive coordination at later phases.

**Why the dev-self threat model holds (with honesty about the leak path).** The Critique surfaced the right adversarial: a personal-team-signed .app CAN run on a friend's Mac with manual Gatekeeper override (right-click → Open). The structural claim "no distribution scaffold prevents distribution" is too strong. The honest framing: v0 is dev-self by **intent + practical friction**, not by structural impossibility. The developer who deliberately shares v0 with a naive recipient is choosing to expose them to the plaintext UserDefaults risk — an informed decision. The threat model boundary holds at the layer of intent.

**Why "common pattern" was explicitly demoted.** Innovation could have rubber-stamped "Mac apps use Keychain → therefore v0 should." The user signaled "anti-rubber-stamp" as a motivation in their original prompt; the Sensemaking discipline took this seriously. The common-pattern argument is real but social, and social conventions don't structurally require following them when the structural conditions (distribution; arbitrary users) aren't yet present.

**Why the persona-validation finding's AE1/AE2 flags are carried forward but not enforced at v0.** AE1 (BYO key as synthesis-flagged single largest concern) and AE2 (3-tier triage essential-tier may need reshuffling) come from the prior persona-validation /traverse finding. That finding flagged these as needing real-translator empirical evidence. v0 doesn't trigger them (dev-self); v0.5 doesn't trigger them (still dev-self); v1 is the first phase that triggers them (distribution). Forward-carrying ensures the flags reach the v1 scoping inquiry as MUST items rather than being silently absorbed.

**Why the 10-piece decomposition resolved to 7 sections + 4 appendix-style pieces in the finding.** The Decomposition's 10 pieces (P1 Methodology / P2 Matrix / P3 Per-phase / P4 Code / P5 Setup / P6 Files / P7 Wiring / P8 Test / P9 Inherited / P10 Roadmap) flow naturally into a reading order: methodology framing (in the synthesis disclaimer at the top) + matrix + per-phase + code + checklist + inherited + roadmap. P5-P8 (subtasks) merge into one Section 5 (the build-checklist) since the reader works through them as one continuous list. The decomposition boundary is preserved; only the presentation merges adjacent pieces.

**Why critique surfaced 4 REFINEs and 0 KILLs.** The Innovation outputs were structurally sound at the design level; the REFINEs were factual / syntactic corrections that the synthesis missed:
- P2's sandboxed UserDefaults plist path was wrong (Innovation said the unsandboxed location; the correct sandboxed path is inside the per-app container).
- P3's migration plan was mis-located in `KeyStore.init` (should be at App layer since KeyStore is backing-agnostic).
- P3's threat-model argument was too strong ("no distribution scaffold prevents distribution" — but it doesn't).
- P7's `Bindable(keyStore).apiKey` inline syntax was wrong (gives `String`, not `Binding<String>`; the local `@Bindable var` idiom is correct).
- E3's language was imprecise ("v0.5→v1 boundary" — but the gate is v1 entry; v0.5 is also dev-self).

All 4 REFINEs were applied at finding-write-time in sections 2, 3, 4, 5, 6, 7.

**No KILLs.** The 10 pieces survived because they were grounded in Sensemaking's commitments (which were themselves tested in Phase 2 + Phase 3 with explicit counter-tests). The Innovation discipline's piece-level Inversion-candidates at the 5 meta-decision pieces (P1, P2, P3, P9, P10) considered real alternatives and rejected them on structural grounds — not straw-man rejections.

---

## Open Questions

### Monitoring

- **Synthesis-vs-reality calibration.** When the MUST item (real translator user research before v1) completes, retrospectively compare its findings to this finding's synthesis-derived recommendations. The gap is a signal of LLM-bias in /traverse synthesis output. Useful for future inquiries' confidence calibration.

### Blocked

- **v1 storage strategy verdict.** Blocked until real translator research (the MUST item) yields evidence on whether BYO key model holds, OR whether AE1's flagged concerns require a redesign (e.g., managed API access with usage caps; team-license bundling).

- **v1 3-tier triage essential-tier composition.** Blocked until the same real-translator research adjudicates AE2 — specifically whether lineage view + Quality Policies + TM should move into v1's essential tier.

### Research Frontiers

- **`@Observable` `didSet` behavior at init.** Empirical question: does Swift 5.9+'s `@Observable` macro expansion preserve `didSet` semantics correctly when the property is set inside the class's own init? Apple's Observation framework documentation is the canonical source; verify-by-compile is the test.

- **Synthesis methodology — code in findings.** This inquiry's Critique surfaced A3 (untested-by-compile code is a recurring risk source). Worth a methodology meta-inquiry after 2-3 more /traverse runs surface the same pattern.

### Refinement Triggers

- **If the real translator user research surfaces evidence that the BYO API key model is broadly rejected by translators, AE1's concerns require re-design**, this finding's v0.5+ recommendations should be re-opened — specifically the assumption that v0.5 introduces Keychain swap rather than abandoning the BYO model in favor of managed access. Trigger: AE1-confirmed verdict in v1 scoping inquiry.

- **If empirical UX measurement of paste-each-session annoyance shows it's tolerable for daily-use translators**, the v0 default could shift from `UserDefaultsBacking` to `InMemoryBacking` (security-prudent variant). Trigger: measured UX data from real users in v0.5 / v1.

- **If cross-platform expansion (Windows / Linux) becomes scope**, this finding's Mac-only assumption is the refinement target — the `KeyStore` protocol's backing-list extends to platform-specific secret stores. Trigger: explicit scope-revision in a future inquiry.

- **If the prior Mac-app finding's 5-layer architecture is re-litigated** in a future inquiry, this finding's file-to-layer mapping is the dependent — section 5's mapping table re-opens. Trigger: a v1+ scoping inquiry that revises the layer commitments.

---

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
Suggested phasing:

  - v0 (days): SwiftUI + URLSession (LLM calls) + UserDefaults (API key, insecure but fine for personal testing) + plain
  String I/O. Get one source → one translation → one .md output working end-to-end. No pause/resume, no project model, no
  Keychain.
  - v0.5 (week): Swap UserDefaults → Keychain for the API key. Add fileImporter for source docs. Save to disk.
  - v1 (weeks): FileDocument .compldoc package format. Swift Concurrency Task for pause/resume. Multi-provider switching.
  3-tier triage features.
  - v1.5: Reading-screen typography (NSTextView via NSViewRepresentable). Multi-translation collation view.
  - v2: Local LLM via llama.cpp Metal bindings. Quick Look extension. iCloud Drive.

  The pieces aren't a monolith you build in parallel — they're an onion you grow from the inside. SwiftUI is the inside.

lets dive deep into this, for exmaple keychain is required or not? why not user just pastes his own key? maybe the question is where to save it? and also other components of this swiftUI , lets enumerate it's subtasks
```

</details>
