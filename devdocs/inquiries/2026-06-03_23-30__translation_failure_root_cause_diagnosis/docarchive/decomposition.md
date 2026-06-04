# Decomposition — translation_failure_root_cause_diagnosis

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-03_23-30__translation_failure_root_cause_diagnosis/_branch.md`

Whole-to-be-decomposed: the action program implied by sensemaking's SV6 (the 4-layer causal stack: PROXIMATE / STRUCTURAL / META / ARCHITECTURAL, plus the user-hypothesis verdicts and the two added causes H4/H5). The program covers both the diagnosis communication (the inquiry's primary deliverable) and the fix-paths that follow from the diagnosis (the user's stated use case: "improve the comprehenslate framework so future translations don't repeat these failures").

---

## Step 1 — Perceive Coupling Topology

### Elements in the whole

| # | Element |
|---|---|
| e1 | Communicate the 4-layer causal model and hypothesis verdicts to the user |
| e2 | Fix the active mis-classification of register in `harmony_layer.md`'s tier system |
| e3 | Add a register-matching principle to `notes.md` |
| e4 | Add a markedness-matching principle to `notes.md` |
| e5 | Add a polysemy-disambiguation principle to `notes.md` |
| e6 | Specify what a failure-mode entry IS (catalog structure: fields, format) |
| e7 | Decide where the failure-mode catalog LIVES (new file vs section in existing docs) |
| e8 | Author the initial failure-mode entries (register pull-up, metaphor-momentum override, markedness inversion, audience-spec misinterpretation, transliteration over-application) |
| e9 | Specify how audience-spec descriptors ("C1 English speakers," "for academics," etc.) should be interpreted |
| e10 | Add a per-section register audit step to `harmony_layer.md`'s 3-pass process |
| e11 | Design the trigger criterion for memory→spec ingestion (when does AI-extracted lesson become a doc edit?) |
| e12 | Design the ingestion process (who reviews, what edits land where) |
| e13 | Design a validation test (how to confirm fixes actually prevent recurrence) |
| e14 | Decide what to do with the existing `eng.md` (leave as documented evidence vs rewrite) |

### Coupling assessment (pairwise — "change one, must the other change?")

Strong coupling clusters:

- **Cluster I — register repair**: e2 ↔ e3 ↔ e10. If the tier system's register classification changes (e2), the principle (e3) and the audit step (e10) must align. Cutting between these creates contradiction across docs.
- **Cluster II — failure-modes catalog**: e6 ↔ e7 ↔ e8. Structure, location, and content are tightly coupled. Catalog structure (e6) determines what entry format (e8) looks like; location (e7) determines how entries are referenced from other docs.
- **Cluster III — memory→spec architecture**: e11 ↔ e12. Trigger and process are mutually defining.

Moderate coupling:

- e3 — e6/e8: principle text and failure-mode text reference each other (each failure mode is a "violation of principle X via pattern Y"). Loose: each can be drafted in parallel as long as cross-references are added at the end.
- e9 — e3: audience-spec rule references the register-matching principle for output behavior.
- e9 — e8: audience-spec misinterpretation IS one of the named failure modes; the catalog entry references the rule.
- e10 — e6/e8: audit step checks signatures from the catalog.
- e4 — e3: markedness-matching is closely related to register-matching but addresses a distinct dimension (word-level marked/unmarked status vs section-level register altitude). Could be combined as one extended principle or kept as siblings.
- e5 — e8: polysemy principle has a paired failure mode (metaphor-momentum override) in the catalog.

Weak coupling / independent:

- e1 (diagnosis communication) is independent of all fix-paths — it conveys what sensemaking already produced.
- e14 (eng.md disposition) is a standalone decision.
- e13 (validation) depends on the fixes being done but doesn't reshape any of them.

### Coupling map (visual)

```
                            ┌─────────────────────────────────────┐
                            │   e1 — DIAGNOSIS COMMUNICATION      │
                            │   (independent; gateway)             │
                            └────────────────┬────────────────────┘
                                             │ informs user's prioritization
            ┌────────────────────────────────┼────────────────────────────────┐
            ▼                                ▼                                ▼
  ┌─────────────────────┐       ┌────────────────────────┐       ┌────────────────────────┐
  │  Cluster I —        │       │  e9 — AUDIENCE-SPEC    │       │  Cluster III —         │
  │  REGISTER REPAIR    │       │  INTERPRETATION RULE   │       │  MEMORY→SPEC ARCH      │
  │                     │       │  (independent rule;    │       │                        │
  │  e2 (tier fix) ◄─┐  │       │   references e3)       │       │  e11 (trigger)         │
  │      │           │  │       └──────┬─────────────────┘       │    │                   │
  │      ▼           │  │              │ ref                     │    │ mutually-          │
  │  e3 (register-   │  │              ▼                         │    │ defining           │
  │      matching)   │  │  ┌──────────────────────────┐           │    ▼                   │
  │      │           │  │  │  Cluster II —            │           │  e12 (ingestion)       │
  │      ▼           │  │  │  FAILURE-MODES CATALOG   │◄──────────┤    (loose connection  │
  │  e4 (markedness) │  │  │                          │           │     to all clusters; │
  │      │           │  │  │  e6 (structure) ◄────┐   │           │     no execution     │
  │      ▼           │  │  │      │              │   │           │     dependency)      │
  │  e10 (audit step)│──┼──┼──►   ▼              │   │           └────────────────────────┘
  │                  │  │  │  e7 (location)      │   │
  └──────────────────┘  │  │      │              │   │
                        │  │      ▼              │   │
  ┌──────────────────┐  │  │  e8 (initial entries)│  │
  │  e5 (polysemy    │──┼──┼──►   │              │   │
  │     disambig)    │  │  │      ▼              │   │
  │                  │  │  │   (cross-refs to    │   │
  └──────────────────┘  │  │    e3, e4, e5, e9)  │   │
                        │  │                     │   │
                        │  └─────────────────────┘   │
                        │                            │
                        └────────────────────────────┘

  ┌────────────────────────┐       ┌────────────────────────┐
  │  e13 — VALIDATION TEST │◄──────│  e14 — ENG.MD          │
  │  (depends on most;     │       │  DISPOSITION           │
  │   feedback to clusters)│       │  (small decision;      │
  └────────────────────────┘       │   feeds informed by e13)│
                                   └────────────────────────┘
```

Major clusters: I (register repair), II (failure-modes catalog), III (memory→spec). Independent: e1, e9, e14, e13. Cross-cluster moderate ties: e3↔e8, e9↔e3, e9↔e8, e10↔e8.

---

## Step 2 — Detect Boundaries (Top-Down)

Cutting at the weakest-coupling valleys:

- **Boundary B1**: between e1 (diagnosis communication) and everything else. e1 has zero downstream content dependency; it conveys the existing sensemaking output. Single-point clean cut.
- **Boundary B2**: between Cluster I (register repair) and Cluster II (failure-modes catalog). They reference each other through cross-references but their internal structures are independent (one is a tier-system reorganization; the other is a new catalog). Diffuse boundary; clean if cross-references are listed.
- **Boundary B3**: between e9 (audience-spec rule) and everything else. e9 references e3 once and appears as a failure-mode entry once. Otherwise independent.
- **Boundary B4**: between Cluster III (memory→spec arch) and the doc-edit work. No execution dependency — the architecture is about FUTURE updates, not this round of updates. Optional / deferrable.
- **Boundary B5**: between e13 (validation) and the fix-pieces. e13 consumes-from-all, contributes-back-to-all-only-if-fail. Single-point clean cut on the forward direction.
- **Boundary B6**: between e14 (eng.md disposition) and everything else. Small standalone decision.
- **Boundary B7**: between e5 (polysemy) and Cluster I. e5 addresses a different failure type (polysemy, not register). Independent principle.

Initial piece candidates:

| Candidate | Composition |
|---|---|
| **P1** | e1 (diagnosis communication) |
| **P2** | e2 (tier fix in harmony_layer.md) |
| **P3** | e3 + e4 (register-matching + markedness principles; tightly related) |
| **P4** | e5 (polysemy disambiguation principle) |
| **P5** | e6 + e7 + e8 (failure-modes catalog: structure + location + initial entries) |
| **P6** | e9 (audience-spec interpretation rule) |
| **P7** | e10 (per-section register audit step) |
| **P8** | e11 + e12 (memory→spec architecture) |
| **P9** | e13 (validation test) |
| **P10** | e14 (eng.md disposition) |

10 pieces from top-down boundary detection.

---

## Step 3 — Validate Boundaries (Bottom-Up Check)

Irreducible atoms (operations a single focused pass can perform):

| Atom | Description |
|---|---|
| a1 | Author one paragraph explaining the 4-layer causal model |
| a2 | Edit one line/section of `harmony_layer.md` to change register's tier |
| a3 | Author register-matching principle text + worked example |
| a4 | Author markedness-matching principle text + worked example |
| a5 | Author polysemy-disambiguation principle text + worked example |
| a6 | Specify catalog entry fields (name / signature / mechanism / corrective / examples) |
| a7 | Decide catalog location (new file path or section anchor in existing doc) |
| a8 | Author one failure-mode entry (one of register pull-up / metaphor-momentum / markedness inversion / audience-spec misinterpretation / transliteration over-application) |
| a9 | Author audience-spec interpretation rule text + examples |
| a10 | Specify audit step location (where in 3-pass process) + checks + re-pass trigger |
| a11 | Specify memory→spec trigger criterion |
| a12 | Specify ingestion process (review path) |
| a13 | Design validation test (test translation + success criteria) |
| a14 | Make the eng.md decision (keep / rewrite / patch) |

Atom-to-piece mapping check:

- P1 = {a1} ✓ atoms group naturally
- P2 = {a2} ✓
- P3 = {a3, a4} ✓ (both about word-choice fidelity at register level)
- P4 = {a5} ✓
- P5 = {a6, a7, a8 × 5} ✓ (structure + location + initial entries; a8 fires once per entry)
- P6 = {a9} ✓
- P7 = {a10} ✓
- P8 = {a11, a12} ✓
- P9 = {a13} ✓
- P10 = {a14} ✓

No atoms split across pieces. No atoms missing from a piece. **Top-down and bottom-up agree.**

**Boundary confidence: HIGH across all 10 pieces.**

One refinement consideration: P5's a8 fires 5 times (one per initial entry). Should each entry be its own piece? Decision: keep as one piece because the entries share structure (a6) and location (a7); decomposing each entry separately would over-decompose (failure mode #5). If Innovation discovers that one specific entry is dramatically more complex than the others, DV2 can split that one entry into its own piece.

---

## Step 4 — Express as Question Tree

### P1 — How should the diagnosis be communicated to the user?

**Verification criteria:**
- [ ] 4-layer causal model (PROXIMATE / STRUCTURAL / META / ARCHITECTURAL) is stated explicitly
- [ ] Verdicts on H1 / H2 / H3 are given with reasons (H1 CONFIRMED with what; H2 MOSTLY FALSE with why; H3 CONFIRMED with how it differs from principles)
- [ ] H4 (audience-spec interpretation as proximate trigger) and H5 (lesson siloing) are surfaced as causes the user didn't name
- [ ] The watershed finding (`harmony_layer.md` self-contradicting on register-as-alternation) is highlighted with the doc's own ranking principle quoted
- [ ] The user's sub-question ("don't principles count as failure modes?") gets a definite NO with the cognitive-role argument
- [ ] The fix-paths are listed at a high level (cheap-and-immediate vs architectural) so the user can prioritize

### P2 — How should the register tier classification in `harmony_layer.md` be corrected?

**Verification criteria:**
- [ ] Decision: split register into "register-as-style" (Tier 3) and "register-as-alternation" (Tier 1) — OR — upgrade register to Tier 1 with a gating condition ("when source exhibits register alternation as a structural device")
- [ ] The specific text edit to `harmony_layer.md` is specified at line-level granularity
- [ ] The internal inconsistency is resolved: the doc's own ranking principle ("the closer a harmony component is to carrying meaning, the higher its priority") no longer contradicts the classification
- [ ] Downstream effect on the harmony-report content is traced: what new entries appear when the audit (P7) runs on a register-alternating source

### P3 — What register-matching and markedness-matching principles should be added to `notes.md`?

**Verification criteria:**
- [ ] Register-matching principle text: definition of register, source-target fidelity rule, with-vs-without framing
- [ ] Markedness-matching principle text: definition of markedness, unmarked→unmarked / marked→marked test, anti-pattern word list (corvée, Padishah, etc.)
- [ ] Worked example for each principle in the style of `advanced_principles.md` (concrete passage; analysis with the principle; analysis without)
- [ ] Cross-references to relevant failure-mode entries in P5
- [ ] Alignment with P2's tier classification verified (no contradiction)

### P4 — What polysemy-disambiguation principle should be added to `notes.md`?

**Verification criteria:**
- [ ] Principle text: local construction adjudicates the sense (genitive, agreement, plausibility); metaphor-momentum is a known override trap
- [ ] Plausibility-test sub-rule: can the referent actually do what the metaphor-sense requires? (Sparrows have no army.)
- [ ] Worked example (the *nefer* case or analog)
- [ ] Cross-reference to the metaphor-momentum failure-mode entry in P5

### P5 — How should the failure-modes catalog be structured and what initial entries should it contain?

**Verification criteria:**
- [ ] Entry structure specified: required fields (name; recognition signature; structural mechanism; corrective; related principle(s); concrete examples)
- [ ] Catalog location decided: new file (e.g., `failure_modes.md`) OR new section in `harmony_layer.md` OR new section in `notes.md`. Reasoning documented.
- [ ] Cross-reference scheme specified: how failure modes link to principles they violate, and vice versa
- [ ] Five initial entries authored:
  - [ ] Register pull-up
  - [ ] Metaphor-momentum override (polysemy)
  - [ ] Markedness inversion
  - [ ] Audience-spec misinterpretation
  - [ ] Transliteration over-application
- [ ] Catalog is shaped to be EXTENSIBLE — adding a new entry doesn't require restructuring

### P6 — How should audience-spec descriptors be interpreted by the translator?

**Verification criteria:**
- [ ] Rule for capability-level markers (CEFR levels: A1/A2/B1/B2/C1/C2): what each licenses (vocabulary complexity, syntactic complexity) and what it does NOT license (matching source register that's elevated)
- [ ] Rule for audience-type descriptors ("for academics," "for children," "for general readers"): how to interpret each
- [ ] Explicit anti-rule: capability-level markers are about TARGET-READER CAPABILITY, not about source-register-license. C1 means "the reader can handle complex English"; it does NOT mean "translate into elevated English regardless of source register"
- [ ] Handoff: the rule defers to the register-matching principle (P3) for actual register decisions
- [ ] Worked example: the C1 misread case (this inquiry's trigger event), shown with-vs-without the rule

### P7 — How should a per-section register audit step be added to `harmony_layer.md`'s 3-pass process?

**Verification criteria:**
- [ ] Audit step location specified: within Pass 2 (Harmony Map), between Pass 2 and Pass 3, or as new Pass 4. Reasoning documented.
- [ ] Audit checks specified: per-section register identification (folk / colloquial / neutral / elevated / theological); flagging when target translation's section register doesn't match source's section register; flagging register-alternation patterns in source
- [ ] Re-pass trigger specified: when does an audit failure cause a Pass 3 re-pass?
- [ ] Integration with the harmony report: the audit results appear as a section in the harmony report at file bottom
- [ ] Consistency with P2's tier classification verified

### P8 — What architecture supports memory→spec feedback ingestion?

**Verification criteria:**
- [ ] Trigger criterion specified: when does an AI-extracted feedback memory become a doc edit candidate? (≥N memories of same type? user-initiated review? per-session review?)
- [ ] Ingestion process specified: who reviews (user? AI under user supervision?); what edits land where (which docs, which sections)
- [ ] Safety check: ingestion doesn't break existing principles (collision detection)
- [ ] Decision documented: pursue now, defer until N more failures, or skip
- [ ] If deferred: success criterion for triggering the architectural work

### P9 — How should the fixes be validated as preventing recurrence?

**Verification criteria:**
- [ ] Test translation source specified (could be a sibling Risale-i Nur word, or a fresh source with similar register-alternation structure)
- [ ] Success criteria: P7's audit step flags register pull-up when present; no register pull-up in test translations after fixes; P4's polysemy rule prevents *nefer*-class mis-resolutions
- [ ] Failure criteria: same failure pattern recurs → fixes are incomplete → DV2 trigger
- [ ] Test process: who runs the test, with what configuration

### P10 — What happens to the existing `eng.md` translation?

**Verification criteria:**
- [ ] Decision: leave as documented failure evidence / rewrite with fixes applied / patch only the flagged words
- [ ] Reasoning: which option best serves the user's purpose (the user is using the failure as a system-diagnostic, not asking for a clean translation; leaving as evidence has value)
- [ ] If rewrite chosen: scope (full re-translation? targeted word swaps?)
- [ ] If leave-as-evidence: the harmony report's blindness becomes part of the documented failure trace

---

## Step 5 — Map Interfaces

| Source | Target | What flows | Direction |
|---|---|---|---|
| P1 | User | the 4-layer causal model + verdicts + fix-paths overview | one-way (output to user) |
| User | P2–P10 | prioritization choice (which fixes to pursue, in what order) | one-way (after reading P1) |
| P2 | P3 | tier classification commitment (register-as-alternation Tier 1) — P3's register-matching principle must align | one-way data dependency |
| P2 | P7 | tier classification commitment — P7's audit step needs to know register is at Tier 1 to flag it | one-way data dependency |
| P3 | P5 | register-matching principle text — referenced by the "register pull-up" failure-mode entry as the violated principle | one-way (reference) |
| P3 | P6 | register-matching principle text — referenced by P6's anti-rule ("audience-spec descriptors don't license register changes; see register-matching principle") | one-way (reference) |
| P4 | P5 | polysemy-disambiguation principle — referenced by the "metaphor-momentum override" failure-mode entry | one-way (reference) |
| P5 | P7 | failure-mode signatures — audit step needs the recognition signatures to know what to look for | one-way data dependency |
| P5 | P8 | catalog structure — the memory→spec flow needs to know what entry format new failures will take on ingestion | one-way data dependency |
| P6 | P3 | audience-spec rule references register-matching principle | one-way (reference) |
| P6 | P5 | audience-spec misinterpretation IS one of the named failure modes | one-way (reference) |
| P9 | All P2-P7 | validation result — if validation fails, the failed pieces need DV2 revision | feedback loop |
| P9 | P10 | validation outcome informs whether eng.md should be rewritten | one-way |
| P8 | (future) | architecture supports FUTURE ingestion; no in-inquiry consumer | one-way (deferred) |

### Assumptions-not-data check (Step 5 refinement)

What does each piece ASSUME about what others provide?

- **P3 assumes** P2 has settled the split-vs-upgrade question. If P3 starts before P2 commits, P3's principle text might say "match source register exactly" (assuming Tier 1) when P2 ends up choosing a different formulation. Mitigation: P3 starts only after P2 commits, OR P3 is drafted parametrically with the tier-classification choice pulled in at the end.
- **P5 assumes** the failure-mode entries can reference principles by stable names. If P3 renames or restructures, P5's references break. Mitigation: agree on principle names before authoring P5 entries.
- **P7 assumes** P5's catalog has machine-recognizable signatures (or human-readable patterns the audit can check). If P5's catalog is purely narrative without recognition signatures, P7's audit has nothing operational to check. Mitigation: P5's entry structure (verified in P5's checklist) explicitly includes "recognition signature" as a required field.
- **P9 assumes** P2-P7 produce concrete testable changes. Without specifics, P9's test design has nothing to test. Mitigation: P9 depends on P2-P7 completing.
- **P10 assumes** P1 has clarified what the user wants the eng.md to BE (evidence vs clean translation). Mitigation: P10 follows P1.
- **P6 assumes** future audience-spec markers are CEFR-shaped or English-prose-shaped. If users pass arbitrary descriptors ("for someone like my grandmother"), the rule needs a fallback. Mitigation: P6's rule includes a fallback clause for non-standard descriptors.

These assumptions are surfaced, not hidden. Hidden coupling risk is bounded.

---

## Step 6 — Order by Dependency

### Dependency-ordered execution plan

**LEVEL 0 — Must come first:**
- **P1 (diagnosis communication)** — the user reads this and decides which fix-paths to pursue. All downstream work is contingent on the user's prioritization.

**LEVEL 1 — Parallel after P1; no inter-dependencies among themselves:**
- **P2 (tier fix)** — highest-leverage cheap fix. No upstream dependencies.
- **P6 (audience-spec rule)** — independent rule. References P3 (a later level) by name; that reference can be added once P3 settles.
- **P8 (memory→spec architecture)** — optional / deferrable. Can be designed in parallel or skipped per user choice.
- **P10 (eng.md disposition)** — standalone decision after P1.

**LEVEL 2 — After P2:**
- **P3 (register + markedness principles)** — depends on P2's tier-classification choice.
- **P4 (polysemy principle)** — independent of P2 (different failure type). Could be at Level 1, but kept here for grouping with related principle work.

**LEVEL 3 — After P3 (and P4):**
- **P5 (failure-modes catalog)** — depends on P3's principles (for the "violated principle" references) and P4's polysemy principle (for the metaphor-momentum entry). Once P3 and P4 settle, P5 can author the catalog.

**LEVEL 4 — After P2 and P5:**
- **P7 (audit step)** — depends on P2's tier classification (knows what to flag at what tier) and P5's failure-mode signatures (knows what patterns to look for).

**LEVEL 5 — After all relevant fixes:**
- **P9 (validation)** — depends on P2, P3, P4, P5, P6, P7 being done. P8 is optional / not on this critical path.

**LEVEL 6 — Final (depends on P9):**
- **P10's final form** — if P9 succeeds, the disposition decision is informed; if P9 fails, DV2 fires and some Level 2–4 pieces redo.

### Visual dependency order

```
LVL 0: P1 (diagnosis communication)
        │
        ▼
LVL 1: ┌─── P2 ───┐  ┌─ P6 ─┐  ┌─ P8 ─┐  ┌─ P10 (initial) ─┐
       │ (tier)   │  │(C1) │  │(arch)│  │  (disposition)   │
       └────┬─────┘  └──┬──┘  └──────┘  └──────────────────┘
            │           │
            ▼           │
LVL 2: ┌─── P3 ───┐  ┌─ P4 ─┐
       │(principles)  │(polysemy)
       └────┬──────┘  └──┬──┘
            │            │
            └─────┬──────┘
                  ▼
LVL 3:    ┌──── P5 ─────┐
          │ (failure-    │
          │  modes       │
          │  catalog)    │
          └──────┬───────┘
                 │
                 ▼
LVL 4:    ┌──── P7 ─────┐ (uses P2 + P5)
          │ (audit step) │
          └──────┬───────┘
                 │
                 ▼
LVL 5:    ┌──── P9 ──────────┐
          │  (validation)     │
          │  pass → continue  │
          │  fail → DV2       │
          └────────┬──────────┘
                   │
                   ▼
LVL 6:    ┌── P10 (final) ──┐
          │   (informed by   │
          │    P9 outcome)   │
          └──────────────────┘
```

Critical path: P1 → P2 → P3 → P5 → P7 → P9 → P10. Five levels deep on the critical path (excluding the parallel paths).

---

## Step 7 — Self-Evaluate

### Minimum 3-dimension evaluation

| Dimension | Check | Verdict |
|---|---|---|
| **Independence** | Each piece's question is answerable without reading sibling pieces (except through defined interfaces) | **PASS** — each piece's question (P1 through P10) is independently scope-defined; cross-piece references go through the interface map. |
| **Completeness** | No aspect of the whole (4-layer causal stack + diagnosis communication + validation) falls through the gaps | **PASS** — the 4 layers map to pieces (PROXIMATE → P6; STRUCTURAL → P2/P3/P7; META → P4/P5; ARCHITECTURAL → P8) + P1 (communication) + P9 (validation) + P10 (specific-case disposition). All covered. |
| **Reassembly** | Pieces + interfaces reconstruct the original problem | **PASS** — when all 10 pieces are answered with their verification criteria met, the result is: (a) the user understands the root cause [P1]; (b) the framework has corrected register classification [P2], filled the doc-level principle gaps [P3/P4], gained a diagnostic mode via failure-modes catalog [P5], gained an audience-spec interpretation rule [P6], gained a per-section audit step [P7], potentially gained a learning-loop architecture [P8], been validated [P9], and the specific failed translation has a defined disposition [P10]. The original problem ("what went wrong and how to fix it") is solved. |

### Full 7-dimension evaluation (because this is a substantive multi-layer fix program)

| Dimension | Check | Verdict |
|---|---|---|
| **Independence** | Per above | PASS |
| **Completeness** | Per above | PASS |
| **Reassembly** | Per above | PASS |
| **Tractability** | Each piece small enough for a single focused pass? | **PASS with note** — P5 is the largest (catalog structure + location + 5 initial entries). It's still single-focused-pass-shaped because the entries share structure, but it's larger than the others. P8 is the next largest if pursued. Acceptable spread. |
| **Interface clarity** | Cross-piece flows explicit, no hidden dependencies | **PASS** — the interface map in Step 5 lists each flow; the Assumptions-not-data check surfaced and mitigated 6 latent assumptions. |
| **Balance** | Complexity roughly proportional, no single 80%-piece | **PASS** — rough size distribution: P1 (S), P2 (XS), P3 (M), P4 (S), P5 (L), P6 (S), P7 (M), P8 (L, optional), P9 (M), P10 (XS). Largest pieces (P5, P8) are ~3× the smallest, not 10×. No 80%-piece. |
| **Confidence** | Top-down and bottom-up agree on boundaries | **PASS** — Step 3 verified atom-to-piece mapping with no splits or merges needed. HIGH confidence on all 10 boundaries. |

### Determination-mechanism piece check (Step 7 refinement)

Load-bearing concepts whose use depends on a runtime determination:

| Concept | Runtime determination | Determination-mechanism piece |
|---|---|---|
| "Register pull-up" | Does this translation exhibit register pull-up? | **P7** (audit step) — checks signatures from P5's catalog |
| "Register-as-alternation" | Does this source exhibit register alternation as a structural device? | **P7** (audit checks alternation pattern) + **P2** (defines the tier gating that activates the alternation handling) |
| "Audience-spec interpretation" | What does THIS audience descriptor (e.g., "C1 English speakers") mean? | **P6** (interpretation rule for capability-level + audience-type descriptors) |
| "Memory→spec ingestion trigger" | Has the threshold been met for a memory to become a doc edit? | **P8** (trigger criterion specified, if pursued) |
| "Polysemy sense fit" | Which sense of a polysemous word fits the local construction? | **P4** (construction-arbitrates rule + plausibility test) |

All runtime determinations have explicit determination-mechanism pieces. No determination is assumed-without-mechanism. PASS.

### Failure-mode self-check

| Failure mode | Risk | Mitigation status |
|---|---|---|
| 1. Premature decomposition | Decomposing before sensemaking clarified the whole | NO — sensemaking SV6 was produced and is the input. |
| 2. Wrong boundaries | Cutting through high-coupling regions | NO — boundaries cut at low-coupling valleys per coupling map; bottom-up validation agreed. |
| 3. Hidden coupling | Pieces look independent but share unstated assumptions | LOW — Assumptions-not-data check surfaced 6 potential hidden couplings; each mitigated by sequencing or explicit interface fields. |
| 4. Missing pieces | Whole's aspects fall through gaps | NO — Completeness check confirmed all 4 causal layers + communication + validation + disposition are covered. |
| 5. Over-decomposition | Pieces too small to be coherent | LOW — P5's 5 initial entries kept as one piece (sharing structure + location); not split. |
| 6. Ignoring dependencies | Wrong execution order causes rework | NO — explicit dependency ordering (Level 0 through Level 6); critical path identified. |
| 7. Imbalanced decomposition | One piece is 80% | NO — balance check passed; rough spread XS/S/M/L without 80%-pieces. |

No failure modes triggered.

---

## Final Deliverable Summary

| # | Piece | Question | Level |
|---|---|---|---|
| **P1** | Diagnosis communication | How should the 4-layer causal model + hypothesis verdicts be communicated to the user? | 0 |
| **P2** | Tier fix | How should `harmony_layer.md`'s register tier classification be corrected to remove the internal inconsistency? | 1 |
| **P3** | Register + markedness principles | What register-matching and markedness-matching principles should be added to `notes.md`? | 2 |
| **P4** | Polysemy principle | What polysemy-disambiguation principle should be added to `notes.md`? | 2 |
| **P5** | Failure-modes catalog | How should the failure-modes catalog be structured, where should it live, and what initial entries should it contain? | 3 |
| **P6** | Audience-spec rule | How should audience-spec descriptors (CEFR levels; audience-type descriptors) be interpreted by the translator? | 1 |
| **P7** | Audit step | How should a per-section register audit step be added to `harmony_layer.md`'s 3-pass process? | 4 |
| **P8** | Memory→spec architecture | What architecture supports memory→spec feedback ingestion (optional / long-term)? | 1 (parallel, deferrable) |
| **P9** | Validation | How should the fixes be validated as preventing recurrence? | 5 |
| **P10** | Eng.md disposition | What happens to the existing `eng.md` translation? | 1 initial / 6 final |

10 pieces; 6 levels; critical path = 6 levels deep. All pieces have verification criteria. All interfaces explicit. All assumptions surfaced.

**Decomposition verdict: PROCEED.** The whole has been partitioned into tractable independently-coherent pieces with explicit interfaces and dependency ordering. Downstream stages (Innovation, Critique) can operate on these pieces.
