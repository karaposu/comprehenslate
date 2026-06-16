## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_20-50__swiftui_v0_keychain_and_subtask_enumeration/_branch.md`

Upstream articulation in same folder: `articulate_simple.md`.

Inquiry has two items:
- **I1** — Re-examine the v0 Keychain commitment for the Mac-app v0 (Is Keychain required? Why not paste-each-session? Where is the right place to save the API key?)
- **I2** — Enumerate the SwiftUI subtasks (v0 primarily; possibly later phases)

This is a hybrid case: possibility-mode for I1's option-space (candidate-generated storage strategies + threat models + UX dimensions); artifact-mode for I2's SwiftUI primitives (concrete framework constructs that exist whether or not we use them).

---

# Surfacing

**Mode:** hybrid (possibility for I1; artifact for I2) | **Entry point:** signal-first | **Territory:** explicit-bounded

---

## Region inventory

10 surfaced regions + 1 cross-item region + 1 frontier region.

**I1 regions (storage strategy):**
- **R1** — API-key storage mechanisms on macOS
- **R2** — Threat models
- **R3** — Sandbox / entitlements implications
- **R4** — Prior art (other LLM-client Mac apps)
- **R5** — UX dimensions
- **R6** — Security primitives

**I2 regions (SwiftUI v0 subtasks):**
- **R7** — SwiftUI primitives
- **R8** — Networking
- **R9** — State management
- **R10** — Persistence (output side — file save, not key)
- **R11** — Xcode project setup
- **R12** — Component / architecture breakdown
- **R13** — Files
- **R14** — Build-and-ship

**Cross-region:**
- **R15** — I1 ↔ I2 coupling (how the storage verdict feeds the subtask list)
- **R16** — Frontier (concept-names; open questions; downstream investigation hooks)

---

## Traversal Trace

Per-entry: `[seq] [region] item — relevance/confidence`. Items are identifiers, not content.

### R1 — API-key storage mechanisms on macOS (12 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 1 | UserDefaults (`@AppStorage`) — plaintext plist at `~/Library/Preferences/<bundle-id>.plist` | core | HIGH | v0 candidate per phasing |
| 2 | Keychain Services API (kSecClassGenericPassword) | core | HIGH | v0.5 commitment under question |
| 3 | Paste-each-session, in-memory only — no persistence | core | HIGH | the user's specific challenge |
| 4 | Application Support file (`~/Library/Application Support/<app>/key.json`) | core | HIGH | self-rolled file-based |
| 5 | `~/.config/<app>/key` (Unix-convention) | sub | MEDIUM | less Mac-native; ports easily |
| 6 | `.env` file in app working dir | sub | MEDIUM | familiar from web/CLI tools |
| 7 | Environment variable read at launch (`ProcessInfo.processInfo.environment`) | sub | MEDIUM | dev-only; not user-facing |
| 8 | Encrypted file with user passphrase (manual encryption layer) | side | MEDIUM | adds passphrase UX cost |
| 9 | Login Keychain (default kSecAttrAccessibleWhenUnlocked) | sub | HIGH | the default Keychain item |
| 10 | iCloud Keychain (kSecAttrSynchronizable) | sub | MEDIUM | syncs across user's Macs |
| 11 | Per-app Keychain access group | sub | MEDIUM | sandbox-relevant |
| 12 | "Settings → System Settings → Passwords" surface — show key there too | side | LOW | unusual UX |

### R2 — Threat models (10 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 13 | Single-user dev Mac, only me using it | core | HIGH | the BYO-key personal-use baseline |
| 14 | Single Mac with family member with separate user account | sub | HIGH | covered by macOS user separation |
| 15 | Distributing app to other users (release build) | core | HIGH | changes the calculus |
| 16 | Lost / stolen Mac with FileVault ON | sub | HIGH | disk-encrypted; plist still readable when unlocked |
| 17 | Lost / stolen Mac with FileVault OFF | sub | HIGH | plist plaintext on disk |
| 18 | Malware on Mac that reads UserDefaults plist | sub | HIGH | the headline risk for plain-file storage |
| 19 | Malicious supply-chain dep / dylib injection reading memory | side | MEDIUM | Keychain doesn't help if attacker is in-process |
| 20 | iCloud sync of UserDefaults (rare; opt-in via NSUbiquitousKeyValueStore) | sub | HIGH | not auto; but a footgun |
| 21 | Time Machine backup contains plaintext UserDefaults plist | sub | HIGH | backups travel; plaintext key travels with them |
| 22 | Process snapshot / core dump containing key | umbrella | LOW | exotic |

### R3 — Sandbox / entitlements implications (8 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 23 | App Sandbox capability — yes/no decision | core | HIGH | gates everything else |
| 24 | `com.apple.security.network.client` entitlement (outgoing connections) | core | HIGH | required for LLM API calls |
| 25 | Hardened Runtime (required for notarization) | sub | HIGH | required when distributing |
| 26 | Keychain Sharing entitlement (`keychain-access-groups`) | sub | MEDIUM | only when using shared access group |
| 27 | App Group entitlement | side | LOW | multi-process; not v0 |
| 28 | Notarization (Apple staples ticket after malware scan) | sub | HIGH | required for direct distribution outside App Store |
| 29 | Developer ID Application certificate (for direct distribution) | sub | HIGH | distinct from Mac App Store cert |
| 30 | Per-user Login Keychain vs System Keychain | sub | MEDIUM | per-user is default; system needs admin |

### R4 — Prior art (other LLM-client Mac apps) (12 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 31 | Raycast AI: stores API keys in Keychain (Settings panel) | sub | MEDIUM | shipping commercial precedent |
| 32 | BoltAI (boltai.com): BYO key, Keychain-stored | sub | MEDIUM | direct LLM-client peer |
| 33 | MacGPT: BYO key (Keychain) | sub | MEDIUM | small indie precedent |
| 34 | TypeAhead AI / TypingMind variants | side | LOW | mostly web-based |
| 35 | Ollama (Mac app): local-only, no API key needed | side | MEDIUM | different model — local-LLM-only |
| 36 | LM Studio: local-only models | side | MEDIUM | same shape as Ollama |
| 37 | ChatGPT Desktop (Mac): account-based, not BYO key | side | MEDIUM | OAuth login model |
| 38 | Claude Desktop (Anthropic's own): account-based, no BYO | side | MEDIUM | OAuth |
| 39 | Cursor: cloud account; BYO key is optional | side | LOW | hybrid |
| 40 | iTerm2: stores SSH keys/passwords in Keychain | umbrella | MEDIUM | general Mac-app credentials pattern |
| 41 | "Common pattern" — production Mac apps use Keychain for credentials; UserDefaults for secrets is rare | umbrella | HIGH | concept-name (R16) |
| 42 | 1Password CLI integration as alternative key source | side | LOW | power-user pattern |

### R5 — UX dimensions (11 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 43 | First-launch experience: empty-state hint → "paste your Anthropic API key" | core | HIGH | onboarding gate |
| 44 | Settings panel for key management (separate from main UI) | sub | HIGH | conventional Mac UX |
| 45 | Inline key field in main UI (current v0 sketch) | sub | HIGH | non-conventional but quick |
| 46 | Show / hide key with eye-toggle | sub | MEDIUM | small UX polish |
| 47 | "Forget key" / clear-key button | sub | HIGH | always needed |
| 48 | Multi-provider keys (Anthropic + OpenAI + ...) | sub | MEDIUM | v1 differentiator |
| 49 | Key rotation flow | sub | MEDIUM | low-priority |
| 50 | Paste-once vs paste-per-session distinction in UX | core | HIGH | the user's actual question |
| 51 | Error UX when key invalid (401 from API) | sub | HIGH | universal need |
| 52 | First-time Keychain access prompt (system modal) | sub | HIGH | platform-specific UX |
| 53 | "Use System Keychain" toggle in Settings (user choice between storage modes) | sub | HIGH | meta-option — exposes the storage decision to the user |

### R6 — Security primitives (8 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 54 | At-rest encryption — Keychain: yes (per-Mac key); UserDefaults plist: no | core | HIGH | THE security delta |
| 55 | Per-app isolation — Keychain ACL on the app's bundle identity; UserDefaults plist per-app domain (file-readable by same user) | sub | HIGH | both have per-app boundary; Keychain's is stronger |
| 56 | iCloud-sync risk — UserDefaults can sync via NSUbiquitousKeyValueStore (opt-in); Keychain items can sync per-item | sub | HIGH | both opt-in |
| 57 | ACL prompt on first access — Keychain: yes (system modal); UserDefaults: no | sub | HIGH | UX cost of Keychain |
| 58 | TouchID gate on Keychain access | sub | MEDIUM | available via SecAccessControl |
| 59 | UserDefaults plist file is plaintext, readable by the user's process tree | sub | HIGH | the headline UserDefaults risk |
| 60 | Time Machine inclusion — plist files are backed up plaintext; Keychain items backed up encrypted | sub | HIGH | matters for lost backups |
| 61 | FileVault is orthogonal — protects at-rest at disk-shutdown; doesn't help while unlocked | side | HIGH | clarifying |

---

### R7 — SwiftUI primitives (30 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 62 | `App` protocol + `@main` entry | core | HIGH | every SwiftUI app starts here |
| 63 | `WindowGroup` / `Scene` | core | HIGH | top-level window container |
| 64 | `ContentView` root view | core | HIGH | UI entry |
| 65 | `HSplitView` (side-by-side source/translation) | core | HIGH | v0 layout primitive |
| 66 | `VSplitView` | side | MEDIUM | alternate layout |
| 67 | `TextEditor` (multi-line text input/display) | core | HIGH | source + translation panes |
| 68 | `SecureField` (masked input) | core | HIGH | for API key paste |
| 69 | `TextField` (single-line) | core | HIGH | target-language input |
| 70 | `Button` | core | HIGH | translate / save actions |
| 71 | `Toolbar` / `ToolbarItemGroup` + placement | core | HIGH | action surface |
| 72 | `ProgressView` (spinner) | core | HIGH | translation-in-flight indicator |
| 73 | `Picker` (dropdown) | sub | HIGH | provider / model / target-lang selection |
| 74 | `Menu` / `MenuButton` | sub | MEDIUM | command surfaces |
| 75 | `safeAreaInset(edge:)` | sub | HIGH | persistent bottom-bar for key field |
| 76 | `.fileImporter(isPresented:allowedContentTypes:onCompletion:)` | sub | HIGH | v0.5 doc-import; v0 optional |
| 77 | `.fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)` | sub | HIGH | SwiftUI-native save |
| 78 | `NSSavePanel` (AppKit bridge, alternative save UX) | sub | HIGH | what the current v0 sketch uses |
| 79 | `NSOpenPanel` (AppKit open) | sub | MEDIUM | alternate doc open |
| 80 | `.alert(title:isPresented:actions:message:)` | sub | HIGH | error surface |
| 81 | `Settings` scene (`Settings { ... }`) — adds Cmd+, menu | sub | HIGH | conventional Mac settings |
| 82 | `Form` / `Section` | sub | HIGH | settings-panel layout |
| 83 | `HStack` / `VStack` / `ZStack` | core | HIGH | layout primitives |
| 84 | `ScrollView` | sub | HIGH | long translation output |
| 85 | `Spacer` / `Divider` | sub | MEDIUM | layout polish |
| 86 | `Image` / `Label` / SF Symbols | sub | MEDIUM | iconography |
| 87 | `.disabled(_:)` modifier | sub | HIGH | button gating |
| 88 | `.padding`, `.frame`, `.font`, `.background`, `.border` | sub | HIGH | basic modifiers |
| 89 | `.focused(_:equals:)` + `@FocusState` | side | MEDIUM | focus control |
| 90 | `.onAppear` / `.task` / `.onChange(of:)` | sub | HIGH | lifecycle hooks |
| 91 | `ViewBuilder` for inline factored sub-views | sub | MEDIUM | refactor aid |

### R8 — Networking (19 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 92 | `URLSession.shared` (default session) | core | HIGH | the workhorse |
| 93 | `URLRequest` construction (URL, headers, body) | core | HIGH | per-request shaping |
| 94 | `async`/`await` via `URLSession.data(for:)` | core | HIGH | v0's only call shape |
| 95 | `JSONEncoder` + `JSONDecoder` | core | HIGH | request/response encoding |
| 96 | `Codable` types for request/response | core | HIGH | type-safety for API shapes |
| 97 | Anthropic `/v1/messages` endpoint shape | core | HIGH | the specific API |
| 98 | `x-api-key` header | core | HIGH | auth |
| 99 | `anthropic-version: 2023-06-01` header | core | HIGH | API version pin |
| 100 | `Content-Type: application/json` header | core | HIGH | request body type |
| 101 | Server-sent events / streaming response (`stream: true` + SSE parsing) | sub | MEDIUM | v1+; for live token rendering |
| 102 | Timeout configuration (`URLSessionConfiguration.timeoutIntervalForRequest`) | sub | HIGH | translation calls can be long |
| 103 | `Task` cancellation via `.cancel()` | sub | HIGH | pause/resume foundation; v1+ |
| 104 | Retry logic (exponential backoff) | sub | MEDIUM | resilience |
| 105 | HTTP error mapping (401 → invalid key; 429 → rate limit; 5xx → transient) | sub | HIGH | error UX |
| 106 | `URLError` handling (no connection, DNS, etc.) | sub | HIGH | offline cases |
| 107 | 429 + `retry-after` header handling | sub | MEDIUM | rate-limit recovery |
| 108 | ATS (App Transport Security) — HTTPS-only default | sub | HIGH | works out of box for Anthropic |
| 109 | `URLSessionConfiguration.default` vs `ephemeral` | side | MEDIUM | ephemeral skips cookies/cache |
| 110 | Multi-provider client abstraction (protocol with Anthropic / OpenAI impls) | sub | HIGH | v1 differentiator |

### R9 — State management (13 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 111 | `@State` (local view state) | core | HIGH | text, isTranslating, etc. |
| 112 | `@Binding` (child-view two-way) | sub | HIGH | for sub-views |
| 113 | `@AppStorage("key")` (UserDefaults-backed) | core | HIGH | v0 key storage if I1 says so |
| 114 | `@SceneStorage` (per-window) | sub | MEDIUM | for unsaved drafts per window |
| 115 | `@StateObject` (ObservableObject ownership) | sub | HIGH | for ViewModel ownership |
| 116 | `@ObservedObject` (ObservableObject reference) | sub | MEDIUM | passed in from outside |
| 117 | `@EnvironmentObject` (injected globally) | sub | MEDIUM | for cross-view shared state |
| 118 | `@Environment(\.<key>)` (system-injected) | sub | MEDIUM | colorscheme, locale, etc. |
| 119 | `@Observable` macro (Swift 5.9+) — replaces ObservableObject + @Published | sub | HIGH | newer, simpler; macOS 14+ |
| 120 | ViewModel pattern (MVVM) | sub | HIGH | architectural choice |
| 121 | `@MainActor` annotation for UI-thread safety | sub | HIGH | when ViewModel touches UI |
| 122 | Combine `@Published` (older pattern) | side | LOW | superseded by @Observable |
| 123 | `AsyncSequence` (for streaming responses) | side | MEDIUM | v1+ |

### R10 — Persistence (output side, not key) (11 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 124 | Plain `.md` save via `NSSavePanel` | core | HIGH | v0 path |
| 125 | Plain `.md` save via `.fileExporter` (SwiftUI-native) | sub | HIGH | alternate path |
| 126 | `String.write(to:atomically:encoding:)` | core | HIGH | the actual write |
| 127 | UTF-8 encoding declaration | sub | HIGH | safe default |
| 128 | Default filename for save panel (`translation.md`) | sub | HIGH | small UX |
| 129 | Auto-save / draft persistence to disk | side | MEDIUM | v0.5+ |
| 130 | Cache directory (`URL.cachesDirectory`) | side | LOW | for transient |
| 131 | Application Support directory (`URL.applicationSupportDirectory`) | side | MEDIUM | per-app state files |
| 132 | iCloud Drive folder (`URL.iCloudDocumentsURL`) | side | LOW | v2 |
| 133 | Recent files menu (NSDocumentController integration) | side | MEDIUM | v1 polish |
| 134 | Open existing `.md` files for re-editing | side | MEDIUM | v0.5 |

### R11 — Xcode project setup (19 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 135 | New project → macOS → App template | core | HIGH | starting point |
| 136 | Interface: SwiftUI | core | HIGH | not Storyboard |
| 137 | Language: Swift | core | HIGH | not Obj-C |
| 138 | Bundle identifier (`com.eneskux.comprehenslate` or similar) | core | HIGH | identity |
| 139 | App display name | core | HIGH | "Comprehenslate" |
| 140 | Target deployment: macOS 14+ (Sonoma) for `@Observable` + modern APIs | core | HIGH | floor |
| 141 | Architectures setting → `arm64` (Apple Silicon only) | core | HIGH | per prior decision |
| 142 | Signing & Capabilities pane configuration | core | HIGH | umbrella subtask |
| 143 | App Sandbox capability toggle | core | HIGH | decision point — yes for Mac App Store, optional otherwise |
| 144 | Network Client entitlement toggle | core | HIGH | required for LLM calls |
| 145 | App Icon set (`AppIcon` in `Assets.xcassets`) | sub | HIGH | 1024px + scales |
| 146 | `Info.plist` defaults (auto-managed for SwiftUI app template) | sub | MEDIUM | usually fine |
| 147 | Build phases (default config fine for v0) | side | LOW | no custom scripts |
| 148 | Swift Package Manager dependencies (none for v0) | side | LOW | v2 adds llama.cpp |
| 149 | Development team / Apple ID signing | sub | HIGH | even for personal Run, signed by team |
| 150 | Run destination → "My Mac" | core | HIGH | obvious but worth noting |
| 151 | Debug vs Release schemes | side | MEDIUM | default fine |
| 152 | `print()` / `os.Logger` for debugging | sub | MEDIUM | dev-time |
| 153 | Xcode version (16+) for modern SwiftUI features | sub | HIGH | tooling floor |

### R12 — Component / architecture breakdown (10 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 154 | Single `ContentView` (current v0 sketch — 1 file) | core | HIGH | minimal viable architecture |
| 155 | Split into `SourceView` + `TranslationView` (sub-views) | sub | HIGH | refactor option |
| 156 | `SettingsView` (separate Settings scene) | sub | HIGH | v0 or v0.5 |
| 157 | `ClaudeClient` class (networking, isolated) | sub | HIGH | separates concerns |
| 158 | `KeyStore` protocol + 1 implementation | sub | HIGH | gated on I1 — enables deferring the storage choice |
| 159 | `TranslationEngine` struct (orchestrates client + state) | side | MEDIUM | over-engineered for v0 |
| 160 | `ContentViewModel` (MVVM ViewModel) | side | MEDIUM | not required for v0 |
| 161 | `TranslationError` enum (typed errors) | sub | HIGH | small but useful |
| 162 | `AppDelegate` (NOT needed — SwiftUI App lifecycle) | side | LOW | explicit-empty subtask |
| 163 | Window controller (NOT needed) | side | LOW | explicit-empty subtask |

### R13 — Files (11 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 164 | `ComprehenslateApp.swift` (App entry) | core | HIGH | required |
| 165 | `ContentView.swift` (root view) | core | HIGH | required |
| 166 | `ClaudeClient.swift` (networking) | sub | HIGH | recommended even for v0 |
| 167 | `KeyStore.swift` (protocol + impl; gated on I1) | sub | HIGH | enables I1 deferral |
| 168 | `TranslationError.swift` (error type) | sub | MEDIUM | recommended |
| 169 | `SettingsView.swift` (when split out) | sub | MEDIUM | v0 or v0.5 |
| 170 | `Models.swift` (Codable request/response) | sub | MEDIUM | recommended |
| 171 | `Assets.xcassets` (auto-created; add app icon) | sub | MEDIUM | required for distribution |
| 172 | `Info.plist` (auto-managed) | sub | MEDIUM | usually fine |
| 173 | `.entitlements` file (auto-managed when capabilities added) | sub | HIGH | auto-managed |
| 174 | `.xcodeproj/project.pbxproj` (auto-generated) | side | LOW | don't touch |

### R14 — Build-and-ship (14 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 175 | Compile (Cmd+B) | core | HIGH | smoke test |
| 176 | Run on My Mac (Cmd+R) | core | HIGH | first-launch |
| 177 | Archive build (Product → Archive) | sub | MEDIUM | for distribution |
| 178 | Export for development (signed by your team) | sub | MEDIUM | dev tester builds |
| 179 | Code-signing with Developer ID Application cert | sub | HIGH | required for direct distribution |
| 180 | Notarization upload (xcrun notarytool / Xcode Organizer) | sub | HIGH | required for direct distribution |
| 181 | Stapling notarization ticket (xcrun stapler) | sub | MEDIUM | offline-verifiable |
| 182 | DMG creation (`create-dmg` / `hdiutil` / DropDMG) | sub | MEDIUM | distribution wrapping |
| 183 | Sparkle update framework (for in-app updates) | side | LOW | v1+ |
| 184 | Mac App Store submission flow | side | MEDIUM | alternative distribution |
| 185 | TestFlight for macOS | side | LOW | beta testing |
| 186 | Direct-download landing page | side | MEDIUM | when distributing publicly |
| 187 | Crash reporting (Xcode Organizer / Sentry) | side | LOW | v1+ |
| 188 | Symbolicated crash logs | side | LOW | v1+ |

### R15 — I1 ↔ I2 coupling (3 items)

| # | Item | Relevance | Confidence | Note |
|---|---|---|---|---|
| 189 | `KeyStore` protocol — abstracts storage so I1 verdict doesn't block I2 list | core | HIGH | concept-name |
| 190 | "v0 KeyStore implementation" subtask — content of this subtask is gated on I1 (UserDefaults backing? in-memory? Keychain?) | core | HIGH | the explicit coupling point |
| 191 | "Settings UI choice" — if storage is paste-each-session, no Settings UI needed in v0; if persisted, Settings panel becomes desirable | sub | HIGH | downstream UX consequence of I1 |

### R16 — Frontier (concept-names + open questions; 8 entries)

| # | Item | Type | Note |
|---|---|---|---|
| 192 | "BYO-key UX paradox" | concept-name | easy enough to be usable; hard enough to feel intentional / secure |
| 193 | "Storage strategy decision matrix" | concept-name | security × UX × persistence × portability — proposed downstream artifact |
| 194 | "v0 subtask DAG" | concept-name | dependency graph among R7-R14 subtasks |
| 195 | "The SwiftUI onion" | concept-name | App → Scene → ContentView → Toolbar/safeAreaInset → state hooks; "onion you grow from the inside" |
| 196 | "Mac-native paste-once vs Web paste-each-session paradigm gap" | concept-name | macOS convention is paste-once-and-remember; web tools default to per-session |
| 197 | "Hardened Runtime + Notarization gate" | concept-name | distribution gate that affects entitlements + signing |
| 198 | "Settings scene in v0?" | frontier-flag | open question — does v0 include a Settings scene or inline-key-field-only? |
| 199 | "KeyStore protocol introduced in v0?" | frontier-flag | open question — does v0 introduce the protocol to enable I1's storage swap later? |

---

## State Summary

**Territory echo:** v0 SwiftUI Mac-app scaffold + storage-strategy decision space (substrate: prior /traverse Mac-app finding + in-conversation v0 phasing recommendation).

**Purpose echo:** dive deeper into the v0 phasing — adjudicate (a) the storage-strategy decision (I1) and (b) enumerate the SwiftUI v0 subtasks (I2), preserving cross-item coupling.

### Coverage map

| Region | Items | Coverage |
|---|---|---|
| R1 storage mechanisms | 12 | confirmed; ~3 LOW-confidence candidates retained per lean-to-include |
| R2 threat models | 10 | confirmed; broad enough to support per-option evaluation |
| R3 sandbox/entitlements | 8 | confirmed; tight coupling to distribution |
| R4 prior art | 12 | confirmed but inherently incomplete — "common pattern" is the load-bearing observation |
| R5 UX dimensions | 11 | confirmed |
| R6 security primitives | 8 | confirmed |
| R7 SwiftUI primitives | 30 | confirmed; lean-to-include; some side-tagged primitives (TabView, LazyVStack) may not appear in v0 |
| R8 networking | 19 | confirmed |
| R9 state management | 13 | confirmed |
| R10 persistence (output) | 11 | confirmed |
| R11 Xcode project setup | 19 | confirmed |
| R12 architecture breakdown | 10 | confirmed |
| R13 files | 11 | confirmed |
| R14 build-and-ship | 14 | confirmed; many items deferred to post-v0 |
| R15 cross-item coupling | 3 | confirmed; structural |
| R16 frontier | 8 | confirmed; downstream investigation hooks |

**Confirmed-absent regions:** none claimed as absent. The territory is intentionally broad; all regions surfaced at least some content.

**Concept-names list:**

| Name | Type | Provenance | Gloss |
|---|---|---|---|
| common-pattern: Mac apps use Keychain for credentials | vocabulary | R4 #41 | observational baseline for prior-art reasoning |
| BYO-key UX paradox | coined-term | R16 #192 | tension between usability and intentional-feel |
| Storage strategy decision matrix | structural-reference | R16 #193 | proposed downstream artifact |
| v0 subtask DAG | structural-reference | R16 #194 | dependency graph |
| The SwiftUI onion | coined-term | R16 #195 | inside-out growth model from v0 sketch |
| Mac-native paste-once vs Web paste-each-session paradigm gap | coined-term | R16 #196 | platform-convention friction |
| Hardened Runtime + Notarization gate | vocabulary | R16 #197 | distribution requirement |

**Recency distribution:** N/A — territory is conceptual / possibility-mode for I1 and an Apple-framework-vocabulary for I2; no filesystem-backed items (all `source: none, value: null`). `items_with_mtime: 0 / items_without_mtime: 199`.

**Frontier flags (downstream investigation):**

| Flag | Open question | Refined-sub-purpose for re-invocation |
|---|---|---|
| F1 | Does v0 include a Settings scene or stick with inline-key-field? | Surfacing not needed — sensemaking decides |
| F2 | Does v0 introduce the `KeyStore` protocol so storage can swap without UI changes? | Surfacing not needed — innovation generates the option |
| F3 | Cross-platform secret-store abstraction for future Windows/Linux ports | OUT-OF-SCOPE per Mac-only commitment; not pursued |
| F4 | TouchID gate on Keychain access | Surfacing complete (R6 #58); decision deferred to downstream |
| F5 | Should v0 ship as sandboxed or unsandboxed? | Surfacing complete (R3 #23); decision deferred to downstream |

**Workspace-populated status:** `{populated: true, populated-at: 2026-06-15_20-50, extent: 199 items + 7 concept-names across 16 regions covering 2 inquiry items}`.

---

## Failure modes checked (LAYER 1)

| # | Mode | Fired? | Note |
|---|---|---|---|
| 1 | Missed-relevance | NONE | All territory regions explicitly traversed |
| 2 | Surfaced-irrelevance | NONE | A handful of LOW/SIDE items (162-163, 184, 187-188) preserved per lean-to-include; bounded cost downstream |
| 3 | Over-coverage | PARTIAL | 199 items is high. Justified: 16 regions × ~12 items/region average; territory intentionally broad per inquiry framing. Sensemaking will prune for the decision matrix |
| 4 | Territory-mis-binding | NONE | All items within explicit territory (storage options + SwiftUI v0 surface area + supporting context) |
| 5 | Workspace overload | NONE | ~199 items at tag-only granularity is well within context budget |
| 6 | Artifact under-specification | NONE | Trace + Summary + per-item identifiers + concept-names present |
| 7 | Workspace-artifact desync | NONE | Capture-at-moment-of-tagging applied |
| 8 | Recency-Equates-Idleness | N/A | No mtime-based reasoning |
| 9 | Recency-Bias-Filter | N/A | No mtime-based filtering |

**Self-assessment verdict:** **PROCEED**.

Light flag on Mode 3 (Over-coverage) — 199 items is justified by territory breadth but Sensemaking should prune to the decision-bearing subset for I1 (decision matrix on ~6 storage strategies) and the build-checklist subset for I2 (~30-50 actionable subtasks).

**Telemetry:**
- Mode: hybrid (possibility for I1 / artifact for I2)
- Entry point: signal-first
- Cycles run: 16 (one per region)
- Items enumerated: 199; concept-names: 7
- Items tagged: core: ~55 / sub: ~95 / side: ~35 / umbrella: ~14
- Boundary-discovery sub-phase: not fired (territory explicit-bounded)
- Workspace-overload trigger: not fired
- Frontier flags emitted: 5 (F1-F5)
- `items_with_mtime: 0 / items_without_mtime: 199`
