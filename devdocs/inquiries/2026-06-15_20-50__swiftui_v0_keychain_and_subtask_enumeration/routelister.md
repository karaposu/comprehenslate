## User Input

**Territory:** `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_20-50__swiftui_v0_keychain_and_subtask_enumeration/` — this inquiry's artifacts (`_branch.md` + `articulate_simple.md` + `surfacing.md` + `sensemaking.md` + `decomposition.md` + `innovation.md` + `critique.md`).

**Goal:** dive deep into the v0 SwiftUI phasing per the user's request — Item I1 (storage strategy: paste vs UserDefaults vs Keychain; where to save; KeyStore protocol decision) + Item I2 (enumerate SwiftUI subtasks for v0); produce a finding the user can act on (build v0 from).

---

# Routelister — Route-Map

**Mode:** root / project-space (breadth) | **Entry:** fresh | **Run:** 1

## Map Header

- **Identities enumerated:** 16
- **High-priority count:** 3
- **Routes by kind:** 9 teleological + 7 epistemic
- **Frontier flags:** 2 (R5 user research gates v1; R16 cross-platform secret-store currently OOS)

---

## Route Index

| # | Direction | grain | kind | engagement-type | Priority |
|---|---|---|---|---|---|
| R1 | Build v0 from the finding | project-space | teleological | DEVELOP | HIGH |
| R2 | Verify P4 + P7 code by compile-and-fix at first integration | project-space | epistemic | TEST | HIGH |
| R3 | Choose KeyStore backing variant (UserDefaults default vs InMemory paste-each-session) | project-space | teleological | DEVELOP | MED |
| R4 | Scope a v0.5 phase inquiry when ready (Keychain swap + Settings scene + fileImporter) | project-space | teleological | PURSUE-SEED | MED |
| R5 | Conduct real translator user research before v1 distribution commit | project-space | teleological | INVESTIGATE-FRONTIER | HIGH |
| R6 | Re-test AE1 BYO key model at v1 (against real-translator evidence) | project-space | epistemic | TEST | MED |
| R7 | Re-test AE2 3-tier triage at v1 (lineage view + Quality Policies + TM tier placement) | project-space | epistemic | TEST | MED |
| R8 | Scope a v1 distribution + multi-provider inquiry | project-space | teleological | PURSUE-SEED | MED |
| R9 | Scope a v1.5 reading-screen typography inquiry (NSTextView interop) | project-space | teleological | PURSUE-SEED | LOW |
| R10 | Scope a v2 local-LLM inquiry (llama.cpp Metal bindings) | project-space | teleological | PURSUE-SEED | LOW |
| R11 | Document the synthesis methodology learning A3 (untested-by-compile code is recurring risk source) | project-space | epistemic | CONSOLIDATE | LOW |
| R12 | Carry forward "KeyStore as transition primitive" pattern (E1) | project-space | epistemic | CONSOLIDATE | LOW |
| R13 | Carry forward "sandbox-on-day-1 broader than reasoned" pattern (E2) | project-space | epistemic | CONSOLIDATE | LOW |
| R14 | Compare synthesis recommendations to real user research findings (calibrate LLM-bias) | project-space | epistemic | DIAGNOSE | LOW |
| R15 | Document the 5-option storage matrix as a reusable artifact for future Mac apps | project-space | epistemic | CONSOLIDATE | LOW |
| R16 | Investigate cross-platform secret-store if cross-platform expansion gets scoped | project-space | teleological | INVESTIGATE-FRONTIER | LOW |

---

## Per-route records

### R1 — Build v0 from the finding

- **Direction:** the v0 build-checklist (P5 Xcode-setup + P6 file creation + P7 wiring + P8 run-and-test)
- **Goal:** the user produces a working v0 SwiftUI app that translates source text and saves output
- **grain:** project-space
- **kind:** teleological
- **engagement-type:** DEVELOP
- **Movement:** execute the 45 file-level subtasks sequentially per the finding
- **WHY:** the user's articulate_simple "execution-planning" + "make-the-abstraction-concrete" motivations terminate in this action; the entire inquiry's deliverable converges here
- **Priority:** HIGH — primary onward action; gates all other routes
- **Confidence:** HIGH — subtasks are concrete; checklist is the synthesis output
- **Guidance Mode:** compact
  - "follow P5 → P6 → P7 → P8 sequentially" (because Decomposition's L4-L6 dependency chain is sequential)
  - "apply Critique REFINEs INLINE while building" (specifically: P7's Bindable inline syntax fix at the SecureField wiring)
- **Depth-link:** none (not yet drilled)

### R2 — Verify P4 + P7 code by compile-and-fix at first integration

- **Direction:** the Mechanism-Independence Quarantine on the platform-specific code claims
- **Goal:** confirm that the KeyStore protocol code (P4) + ContentView wiring (P7) actually compile under Swift 5.9 / macOS 14+
- **grain:** project-space
- **kind:** epistemic
- **engagement-type:** TEST
- **Movement:** compile the code; resolve errors; verify behavior at runtime
- **WHY:** Critique's Phase 4 flagged Mechanism-Independence Quarantine — convergence on platform claims was reached via structural reasoning alone; the user is the external verifier
- **Priority:** HIGH — couples to R1; the verify step IS part of executing R1 but listed separately because it's epistemic (sharpening the understanding the recommendations rest on)
- **Confidence:** HIGH — the verification mechanism (compile) is well-defined
- **Guidance Mode:** compact
  - "verify @Observable didSet at init does NOT call backing.write("") on empty key" (because P4 caveat surfaced this concern)
  - "verify the corrected @Bindable inline pattern works in ContentView body" (because P7 REFINE applied)
  - "verify sandboxed UserDefaults plist actually lives at ~/Library/Containers/<bundle>/Data/Library/Preferences/<bundle>.plist" (because P2 REFINE corrected the path)
- **Depth-link:** none

### R3 — Choose KeyStore backing variant

- **Direction:** the personal-use choice between `UserDefaultsBacking` (default; persistent; plaintext-at-rest accepted) vs `InMemoryBacking` (paste-each-session; no persistence; security-prudent)
- **Goal:** the user makes an informed personal preference per their threat-model comfort and ergonomic preference
- **grain:** project-space
- **kind:** teleological
- **engagement-type:** DEVELOP
- **Movement:** decide which backing to instantiate in `ComprehenslateApp.swift`; one-line change
- **WHY:** the Decision Matrix surfaces both options as defensible at v0; the user owns the personal-preference tradeoff
- **Priority:** MED — load-bearing but downstream of R1's "start building"; can be revised at any time (one-line swap)
- **Confidence:** HIGH — both options are documented; choice is preference-based
- **Guidance Mode:** compact
  - "if you accept plaintext-at-rest for your own dev Mac, use UserDefaultsBacking (default); paste once" (the ergonomic path)
  - "if you prefer no plaintext anywhere, use InMemoryBacking; paste each launch" (the security-prudent path)
- **Depth-link:** none

### R4 — Scope a v0.5 phase inquiry when ready

- **Direction:** the v0.5 phase scope (Keychain swap + Settings scene + fileImporter + save-to-disk default)
- **Goal:** when v0 ships and the user is ready to move toward distribution-readiness, scope v0.5 as its own /traverse inquiry rather than inheriting it from this finding
- **grain:** project-space
- **kind:** teleological
- **engagement-type:** PURSUE-SEED — v0.5 is seeded in P10 but not committed in detail
- **Movement:** when v0 is working, invoke /traverse with a v0.5 question (e.g., "scope v0.5: Keychain swap + Settings + fileImporter")
- **WHY:** P10's "suggested progression, not binding spec" reframe (per E3 absorption) makes v0.5 a future inquiry, not a forward-commitment
- **Priority:** MED — gates v0.5 progress but only when v0 is shipped
- **Confidence:** MED — v0.5 scope is sketched but not validated
- **Guidance Mode:** compact
  - "wait for v0 to be a working baseline before scoping v0.5" (because the v0.5 specifics depend on v0 lessons learned)
  - "use the KeyStore protocol's swap-point as the architectural starting position for v0.5's first commitment" (because E1 emergent: KeyStore IS the transition primitive)
- **Depth-link:** none

### R5 — Conduct real translator user research before v1 distribution commit

- **Direction:** the empirical user research plan (from prior persona-validation finding's R1 onward route)
- **Goal:** validate the synthesis-flagged concerns (AE1 BYO key; AE2 3-tier triage) with real translators BEFORE committing to v1 distribution
- **grain:** project-space
- **kind:** teleological
- **engagement-type:** INVESTIGATE-FRONTIER
- **Movement:** execute the research plan documented in the persona-validation finding (recruit translators; conduct interviews; synthesize findings)
- **WHY:** Critique Phase 3.5 Assembly observation E3 — v1 is the first distribution phase; AE1/AE2 must be adjudicated against real-translator evidence before v1; v0 + v0.5 are dev-self and don't trigger the gate
- **Priority:** HIGH — gates the v1 build commit; significant lead time required for real research
- **Confidence:** HIGH — the persona-validation finding documents the research plan
- **Guidance Mode:** compact
  - "see devdocs/inquiries/2026-06-15_19-17__user_research_persona_validation/finding.md for the research plan + interview script + recruitment criteria"
- **Depth-link:** the persona-validation finding's R1 onward route
- **Frontier flag:** YES — significant work; needs scoping inquiry to plan execution

### R6 — Re-test AE1 BYO key model at v1

- **Direction:** the persona-validation finding's AE1 synthesis flag (BYO key as single largest mis-commitment; 4/5 personas critical)
- **Goal:** determine whether AE1 holds under real-translator evidence; if yes, redesign storage model BEFORE v1 ships
- **grain:** project-space
- **kind:** epistemic
- **engagement-type:** TEST — validate AE1 against real evidence
- **Movement:** as part of R5's research, include AE1 as one of the test questions; adjudicate based on findings
- **WHY:** v1 introduces distribution; AE1 concerns the BYO key model under distribution; ungated v1 build risks the AE1 issues materializing
- **Priority:** MED — depends on R5; can't fire independently
- **Confidence:** HIGH — the test mechanism is real interviews
- **Guidance Mode:** compact
  - "include AE1 in R5's interview script as 'how would you feel about bringing your own API key for this kind of tool?'"
- **Depth-link:** AE1 in persona-validation finding

### R7 — Re-test AE2 3-tier triage at v1

- **Direction:** the persona-validation finding's AE2 synthesis flag (3-tier triage essential-tier may need reshuffling — lineage view + Quality Policies + TM should move earlier)
- **Goal:** determine whether the v1 "essential" tier composition needs revision per real-translator priorities
- **grain:** project-space
- **kind:** epistemic
- **engagement-type:** TEST — validate AE2 against real evidence
- **Movement:** as part of R5's research, include AE2 as a feature-prioritization question
- **WHY:** v1's essential-tier composition shapes the v1 spec; AE2 surfaces concern that the synthesis-derived essential tier may not match translator needs
- **Priority:** MED — depends on R5
- **Confidence:** HIGH — test mechanism is real interviews
- **Guidance Mode:** compact
  - "include AE2 in R5's interview as 'rank these features by importance for your daily work'"
- **Depth-link:** AE2 in persona-validation finding

### R8 — Scope a v1 distribution + multi-provider inquiry

- **Direction:** the v1 phase scope (FileDocument `.compldoc` + pause/resume + multi-provider + 3-tier triage essential features + notarization + DMG)
- **Goal:** scope v1 as its own /traverse inquiry, informed by R5/R6/R7 real-research findings
- **grain:** project-space
- **kind:** teleological
- **engagement-type:** PURSUE-SEED
- **Movement:** when v0.5 is shipped + R5 research is complete, invoke /traverse with a v1 question
- **WHY:** P10's roadmap is suggestive; v1 is the first distribution-touching phase; scoping is a separate concern
- **Priority:** MED — gated on R4 (v0.5 done) + R5 (research done)
- **Confidence:** MED — v1 scope is the largest and least specified
- **Guidance Mode:** compact
  - "include R6 + R7 verdicts as inputs to the v1 scoping inquiry"
- **Depth-link:** none

### R9 — Scope a v1.5 reading-screen typography inquiry

- **Direction:** the reading-screen typography work (NSTextView via NSViewRepresentable for proper RTL + Quranic citation rendering + theological register support)
- **Goal:** plan the v1.5 typography polish as its own /traverse inquiry
- **grain:** project-space
- **kind:** teleological
- **engagement-type:** PURSUE-SEED — v1.5 is sketched in P10 but not detailed
- **Movement:** when v1 is shipped, invoke /traverse with a v1.5 question
- **WHY:** P10 roadmap places reading-screen typography at v1.5; specific work is non-trivial (NSTextView interop has known SwiftUI integration challenges)
- **Priority:** LOW — late-phase
- **Confidence:** MED — v1.5 needs further detail than P10 provides
- **Guidance Mode:** none
- **Depth-link:** none

### R10 — Scope a v2 local-LLM inquiry

- **Direction:** the local LLM work (llama.cpp Metal bindings for Apple Silicon; CoreML + Neural Engine path)
- **Goal:** plan v2 as its own /traverse inquiry
- **grain:** project-space
- **kind:** teleological
- **engagement-type:** PURSUE-SEED
- **Movement:** when v1.5 is shipped, invoke /traverse with a v2 question
- **WHY:** v2 is months out; significant architectural work (model bundling, inference threading, memory management)
- **Priority:** LOW — late-phase
- **Confidence:** LOW — v2 scope is the least defined
- **Guidance Mode:** none
- **Depth-link:** none

### R11 — Document the synthesis methodology learning A3

- **Direction:** the meta-finding from Critique Phase 3.5 Assembly observation A3 — "untested-by-compile code in synthesis findings is a recurring risk source"
- **Goal:** capture this as a methodology lesson for future /traverse inquiries that produce code-as-output
- **grain:** project-space
- **kind:** epistemic
- **engagement-type:** CONSOLIDATE — aggregate into a documented methodology pattern
- **Movement:** add a note to future Innovation/Critique runs producing code: "include compile-then-fix step in finding's reader's path"
- **WHY:** this inquiry surfaced A3 organically; documenting it prevents future inquiries from repeating the verification gap
- **Priority:** LOW — methodology meta; doesn't block current work
- **Confidence:** MED — A3 is one instance; pattern would solidify with 2+ instances
- **Guidance Mode:** none
- **Depth-link:** Critique Phase 3.5 A3

### R12 — Carry forward "KeyStore as transition primitive" pattern

- **Direction:** the E1 emergent — protocol-based abstraction as the swap-point for phase-transitioned implementations
- **Goal:** make this pattern available as a design heuristic for future phase-transitioned components
- **grain:** project-space
- **kind:** epistemic
- **engagement-type:** CONSOLIDATE
- **Movement:** when designing future phase-transitioned components (e.g., LLM provider switch at v1; model-source switch at v2), apply the same protocol+backing pattern
- **WHY:** E1's substance generalizes — any component facing v0→v0.5→v1 evolution benefits from the same architectural shape
- **Priority:** LOW — design heuristic; activates on future design work
- **Confidence:** MED — pattern is one instance; would solidify with reuse
- **Guidance Mode:** none
- **Depth-link:** E1 in innovation.md

### R13 — Carry forward "sandbox-on-day-1 broader than reasoned" pattern

- **Direction:** the E2 emergent — sandbox-from-v0 prevents a class of downstream surprises broader than the immediate reasoning enumerated
- **Goal:** make this principle available for future Mac app projects
- **grain:** project-space
- **kind:** epistemic
- **engagement-type:** CONSOLIDATE
- **Movement:** when starting a new Mac app project, default to sandbox-ON unless explicitly contraindicated
- **WHY:** E2's specific examples (NSSavePanel security-scoped bookmarks; fileImporter; Quick Look; iCloud Drive) all benefit from sandbox-from-day-1; the principle generalizes
- **Priority:** LOW — design heuristic
- **Confidence:** HIGH — concrete examples are well-grounded
- **Guidance Mode:** none
- **Depth-link:** E2 in innovation.md

### R14 — Compare synthesis recommendations to real user research findings

- **Direction:** the calibration check — when R5 research is complete, compare its findings to this finding's synthesis-derived recommendations
- **Goal:** measure synthesis-bias against real evidence; calibrate future synthesis confidence
- **grain:** project-space
- **kind:** epistemic
- **engagement-type:** DIAGNOSE — investigate the gap between synthesis and reality
- **Movement:** when R5 yields data, retrospectively compare against this finding's I1/I2 recommendations + the persona-validation finding's matrix verdicts
- **WHY:** synthesis-vs-reality calibration is itself a learning loop for /traverse methodology
- **Priority:** LOW — long-term methodology improvement
- **Confidence:** MED — depends on R5 happening
- **Guidance Mode:** none
- **Depth-link:** none

### R15 — Document the 5-option storage matrix as a reusable artifact

- **Direction:** the P2 Decision Matrix — extractable from this inquiry for reuse in any future Mac app facing BYO API key storage
- **Goal:** make the matrix available as a reusable template
- **grain:** project-space
- **kind:** epistemic
- **engagement-type:** CONSOLIDATE
- **Movement:** copy the P2 matrix to a project-wide design-patterns document (if such exists; otherwise to SKILL/ references)
- **WHY:** the matrix has reuse value across Mac apps; storing it as a per-inquiry artifact loses the reuse
- **Priority:** LOW — methodology surplus
- **Confidence:** MED — matrix is concrete but reuse pathway not yet defined
- **Guidance Mode:** none
- **Depth-link:** P2 in innovation.md (with corrected sandboxed plist path applied)

### R16 — Investigate cross-platform secret-store if cross-platform expansion gets scoped

- **Direction:** the cross-platform abstraction (Linux secret-service via libsecret; Windows Credential Manager) for the KeyStore protocol
- **Goal:** prepare for the eventuality that the Mac-only commitment is relaxed and the app expands to Linux/Windows
- **grain:** project-space
- **kind:** teleological
- **engagement-type:** INVESTIGATE-FRONTIER — explore an identified-but-unentered territory
- **Movement:** when cross-platform is in scope, design new KeyStore backings for each platform; the existing protocol shape should generalize
- **WHY:** the Mac-only commitment is structural-not-temporal; if it relaxes, the KeyStore protocol is the right starting point per E1
- **Priority:** LOW — speculative; OOS until cross-platform is scoped
- **Confidence:** LOW — cross-platform isn't currently scope
- **Guidance Mode:** none
- **Depth-link:** none
- **Frontier flag:** YES — explicitly OOS at present; document the route for future scope-revision

---

## Excluded section

Candidate-concepts considered but not routed (with reasons):

| Candidate | Reason for exclusion |
|---|---|
| Apply Critique REFINEs to finding | DONE at CONCLUDE write-time application (per Critique signal). Not an outstanding route. |
| Re-litigate the storage strategy decision | Innovation generated + tested Inversion-candidates; Critique surfaced no new evidence to reopen. Engaging would yield no new direction. |
| Implement the KeychainKeyStore Swift code at v0 | OOS — Sensemaking Ambiguity 4 resolved this to v0.5 scope. Internal to v0.5 inquiry (R4). |
| Add a fileImporter to v0 | OOS — Sensemaking Ambiguity 5 + 6 placed this in v0.5 scope. Internal to R4. |
| Add a Settings scene to v0 | OOS — Sensemaking Ambiguity 5 placed this in v0.5 scope. Internal to R4. |
| Optimize translation prompt for Claude | OOS — prompt engineering is a separate concern; the v0 prompt is functional per P7 subtask 35. |
| Implement notarization + DMG packaging | OOS — v1+ scope per P10. Internal to R8. |
| Add unit tests | OOS — tests were unchecked in P5 subtask 8. v0 explicitly defers tests. Could become its own route later but not at this iteration. |
| Implement multi-window support | OOS — not surfaced in any prior. Out of inquiry frame. |

---

## Telemetry

- **Mode:** root / project-space (breadth)
- **Entry point:** fresh (no prior `_route.md` for this inquiry)
- **Identities enumerated:** 16
- **Routes by kind:** 9 teleological + 7 epistemic
- **High-priority routes:** 3 (R1 build v0; R2 verify-by-compile; R5 user research before v1)
- **Frontier flags:** 2 (R5 user research; R16 cross-platform)
- **Individuations made:** 16 distinct concept-identities; 0 merges performed; 0 splits at this run
- **Uncertain individuations:** 0 (all 16 identities clean)
- **Stale entries:** 0 (fresh entry; nothing to mark stale)
- **Convergence status:** CONVERGED — sweep cycle yielded no new identities after second pass; 199 surfaced items reduce to 16 onward routes at the inquiry-output grain
- **LAYER 1 failure modes checked:**
  - Over-merge: NONE — each identity is distinct (verified by inspecting whether engaging it would advance/sharpen something the other identities don't)
  - Under-coverage: NONE — territory swept exhaustively; Excluded section captures non-routes
  - Wrong-grain: NONE — listed identities not manifestations; depth-signals where appropriate
  - Goal-loss: NONE — every route ties back to "act on the v0 SwiftUI phasing finding"
  - Type-misassignment: NONE — each route's kind+engagement-type matches the membership test
  - Index-drift: N/A — fresh entry; no prior state to drift from
- **LAYER 2 failure modes checked:**
  - Selection-creep: NONE — no route is presented as "the move to take"; Priority is attributive
  - Process-coupling: NONE — routes don't reference /traverse process state; they reference territory + future actions
  - Description-collapse: NONE — all routes are prescriptive (engage X by doing Y), not descriptive
  - Manifestation-dump: NONE — breadth grain held; manifestations folded into identities

**Self-assessment verdict: PROCEED**

The route-field is complete; the inquiry has produced its onward direction-set; CONCLUDE may proceed with the finding having a clear path forward through 3 HIGH-priority routes (R1 build; R2 verify; R5 research) and 13 lower-priority routes.
