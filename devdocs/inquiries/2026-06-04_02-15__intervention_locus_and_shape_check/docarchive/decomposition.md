# Decomposition — intervention_locus_and_shape_check

## User Input

`/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-04_02-15__intervention_locus_and_shape_check/_branch.md`

Whole-to-be-decomposed: the YES-WITH-CAVEATS answer to the user's binary frame-check question. From sensemaking's SV6: confirm the primary locus (in-doc edit to `harmony_layer.md`) with structural reasoning (EA-7 trigger evaluation); communicate the framework-knowledge-gap finding (10 docs not 3); surface supplementary loci with per-locus reasoning; present a scope-choice structure with default recommendation; flag future considerations.

---

## Step 1 — Perceive Coupling Topology

### Elements in the whole

| # | Element |
|---|---|
| e1 | Confirm the YES — explain why in-doc edit to `harmony_layer.md` is structurally correct as primary locus |
| e2 | State the EA-7 trigger evaluation result — mechanism's pattern fires only in `harmony_layer.md` (structurally, not by-default) |
| e3 | Communicate the framework-knowledge-gap finding (10 .md files at project root; prior inquiries treated 3) with non-blaming framing (user-instructed bound + AI scoping omission, both correctable now) |
| e4 | Surface supplementary locus 1: `terminology.md` for sub-case naming, with reasoning from terminology.md's declared authority on definitions |
| e5 | Surface supplementary locus 2: `how_config_should_be.md` for audience-spec config (from prior inquiry 1's S9), with reasoning from the config-locus role |
| e6 | Surface supplementary locus 3 (pending investigation): `translation_principals.md` for principle authority, with the investigation question stated |
| e7 | Present the 5-path scope-choice structure (A primary-only / B/C/D primary+one supplementary / E primary+all supplementary) with per-path effort estimates |
| e8 | Recommend a default path with reasoning |
| e9 | Flag code-level changes as future consideration (when tier-system implementation status is engaged) |
| e10 | Investigation note: translation_principals.md vs notes.md authority — what to sample, what to compare, what to ask the user |
| e11 | Note other not-deep-read docs (`advanced.md`, `my_notes.md`, `README.md`, `roadmap.md`) as possible future scope-expansion targets |

### Coupling assessment

Strong coupling clusters:

- **Cluster A — Primary YES with structural reasoning**: e1 ↔ e2. The YES (e1) and its structural justification via the EA-7 trigger evaluation (e2) form one cohesive confirmation.
- **Cluster B — Supplementary loci**: e4 ↔ e5 ↔ e6. The three supplementary loci share a structure (file + decision type + reasoning) and serve the same purpose (transparent enumeration of where else the work could land).
- **Cluster C — Scope-choice with default**: e7 ↔ e8. The 5-path structure and the default recommendation are tightly linked — the default is what's recommended from the paths.
- **Cluster D — Future considerations and investigations**: e9 ↔ e10 ↔ e11. Three small flag/note items at the end of the deliverable.

Moderate coupling:

- Cluster A → Cluster B: the supplementary loci are framed against the primary; the user sees them as additions to the primary, not replacements.
- e3 (framework-knowledge-gap) → Cluster B: the gap finding is WHY the supplementary loci exist; communicating one without the other leaves the reader confused.
- Cluster B → Cluster C: the paths are organized around the loci.
- Cluster C → Cluster D: the investigation note (e10) affects the path D recommendation if translation_principals.md proves authoritative.

Weak coupling / independent:

- e11 (other not-deep-read docs) is loosely coupled to everything else.

### Coupling map (visual)

```
                ┌─────────────────────────────────────────┐
                │  Cluster A — PRIMARY YES                 │
                │   e1 (YES confirmation)                  │
                │   e2 (EA-7 trigger evaluation)           │
                └────────────────┬────────────────────────┘
                                 │ sets primary frame
                                 ▼
                ┌─────────────────────────────────────────┐
                │   e3 — FRAMEWORK-KNOWLEDGE-GAP           │
                │   (non-blaming framing of the           │
                │    surfacing discovery)                  │
                └────────────────┬────────────────────────┘
                                 │ explains why supplementary
                                 ▼
                ┌─────────────────────────────────────────┐
                │  Cluster B — SUPPLEMENTARY LOCI          │
                │   e4 (terminology.md sub-case naming)    │
                │   e5 (how_config_should_be.md audience)  │
                │   e6 (translation_principals.md authority│
                │       — pending investigation)           │
                └────────────────┬────────────────────────┘
                                 │ structures choice
                                 ▼
                ┌─────────────────────────────────────────┐
                │  Cluster C — SCOPE-CHOICE                │
                │   e7 (5-path structure)                  │
                │   e8 (default recommendation)            │
                └────────────────┬────────────────────────┘
                                 │ surfaces future-work
                                 ▼
                ┌─────────────────────────────────────────┐
                │  Cluster D — FUTURE CONSIDERATIONS       │
                │   e9 (code-level)                        │
                │   e10 (investigation procedure)          │
                │   e11 (other not-deep-read docs)         │
                └─────────────────────────────────────────┘
```

---

## Step 2 — Detect Boundaries (Top-Down)

Cutting at low-coupling valleys:

- **B1**: between Cluster A and e3 (framework-knowledge-gap). Clean single-point — A is the YES, e3 is the explanation of why MORE is being surfaced.
- **B2**: between e3 and Cluster B. Clean single-point — e3 sets the explanatory frame, Cluster B is the actual content of the supplementary loci.
- **B3**: between Cluster B and Cluster C. Diffuse — the paths in C reference the loci in B by name but are structurally distinct (paths are user-choice options; loci are file destinations).
- **B4**: between Cluster C and Cluster D. Clean single-point — C is the scope-choice deliverable; D is the future-flag tail.

Initial piece candidates:

| Candidate | Composition |
|---|---|
| **P1** | Cluster A (e1 + e2 — primary YES with structural reasoning) |
| **P2** | e3 (framework-knowledge-gap explanation) |
| **P3** | Cluster B (e4 + e5 + e6 — supplementary loci with per-locus reasoning) |
| **P4** | Cluster C (e7 + e8 — scope-choice + default) |
| **P5** | Cluster D (e9 + e10 + e11 — future considerations + investigations + not-deep-read docs) |

5 pieces from top-down boundary detection.

---

## Step 3 — Validate Boundaries (Bottom-Up Check)

Irreducible atoms:

| Atom | Description |
|---|---|
| a1 | Write the YES confirmation sentence |
| a2 | Write the EA-7 trigger evaluation result (mechanism fires only in harmony_layer.md) |
| a3 | Write the framework-knowledge-gap finding with non-blaming framing |
| a4 | Write the terminology.md supplementary-locus entry (with its declared-authority reasoning) |
| a5 | Write the how_config_should_be.md supplementary-locus entry (with its config-role reasoning) |
| a6 | Write the translation_principals.md supplementary-locus entry (with the investigation question) |
| a7 | Define each of the 5 paths (A through E) with their composition and effort estimate |
| a8 | Recommend a default path with reasoning |
| a9 | Write the code-level future-consideration flag |
| a10 | Write the translation_principals.md investigation procedure |
| a11 | Note other not-deep-read docs as future scope-expansion targets |

Atom-to-piece mapping:

- P1 = {a1, a2} ✓
- P2 = {a3} ✓
- P3 = {a4, a5, a6} ✓
- P4 = {a7, a8} ✓
- P5 = {a9, a10, a11} ✓

No atoms split across pieces; no atoms missing. **Top-down and bottom-up agree.**

**Boundary confidence: HIGH across all 5 pieces.**

---

## Step 4 — Express as Question Tree

### P1 — How should the YES be confirmed with its structural reasoning?

**Verification criteria:**
- [ ] The YES is stated clearly: "in-doc edit to `harmony_layer.md` is the right primary intervention locus."
- [ ] The structural reason is cited: the contradiction empirically lives in `harmony_layer.md`'s tier section.
- [ ] The EA-7 trigger evaluation result is included: the mechanism's pattern (principle/classification split) fires only in `harmony_layer.md` among the framework docs; the primary locus is structurally correct, not just by-default.
- [ ] The user can act on this with no ambiguity about the primary recommendation.

### P2 — How should the framework-knowledge-gap finding be communicated?

**Verification criteria:**
- [ ] Surfacing's discovery is stated: project root has 10 .md files; prior inquiries treated 3.
- [ ] The reason is acknowledged: the user's original instruction bounded the territory ("read only these three"); the prior inquiries respected that bound.
- [ ] The framing is non-blaming: AI scoping omission (didn't surface "are there more files I should consider?") is also acknowledged; both are correctable now.
- [ ] The finding is framed as ADDITIVE — the prior recommendations remain correct within the 3-doc frame; expansion is supplementary, not invalidating.

### P3 — How should the supplementary loci be presented with per-locus reasoning?

**Verification criteria:**
- [ ] `terminology.md` identified as supplementary locus for sub-case naming. Reasoning: terminology.md declares its own authority on definitions ("If a design doc uses a term differently from this file, this file wins"); the sub-case names ("register-as-style," "register-as-alternation") are term-definition acts.
- [ ] `how_config_should_be.md` identified as supplementary locus for audience-spec config (from prior inquiry 1's S9). Reasoning: it's the canonical config-locus for translation behavior (defines audience levels: Native / late learner / late learner simple / poetic).
- [ ] `translation_principals.md` flagged as supplementary locus for principle authority — PENDING investigation. The investigation question: is this 73K file the authoritative principles doc (with notes.md as derivative)?
- [ ] Each locus is mapped to a DECISION TYPE (term-def / config / principle-auth) so the user understands WHY it's a supplementary locus, not just THAT it is.

### P4 — How should the 5-path scope-choice structure be presented with a default recommendation?

**Verification criteria:**
- [ ] Path A defined: primary only (in-doc edits to `harmony_layer.md` per prior inquiry 2's MVD/Full Emergent Assembly). Effort: ~15-30 min day-one + 15-60 min retroactive sweep. The supplementary loci are noted as future considerations.
- [ ] Path B defined: A + terminology.md sub-case naming. +~5 min.
- [ ] Path C defined: A + how_config_should_be.md audience-spec config. +~5-10 min.
- [ ] Path D defined: A + investigate translation_principals.md authority. +~10 min one-time investigation.
- [ ] Path E defined: A + all supplementary. ~30-45 min additional total.
- [ ] A default path is recommended with reasoning. The recommendation respects the "easy" criterion and provides a sensible starting point.
- [ ] All paths are within "easy" criterion as composite.

### P5 — What future considerations and investigation notes should be flagged?

**Verification criteria:**
- [ ] Code-level changes flagged as future consideration: when the tier system's code-side implementation status is engaged (currently unknown).
- [ ] The translation_principals.md investigation procedure is specified: sample the file's structure + compare with notes.md + ask user which is authoritative.
- [ ] Other not-deep-read docs (`advanced.md`, `my_notes.md`, `README.md`, `roadmap.md`) flagged as possible future scope-expansion targets — surfacing did not deep-read these.
- [ ] Each future item has a revival trigger so the user knows when it becomes actionable.

---

## Step 5 — Map Interfaces

| Source | Target | What flows | Direction |
|---|---|---|---|
| P1 | User | Primary YES + structural reasoning | one-way (output) |
| P1 | P3 | Sets the primary frame against which supplementary loci are positioned | one-way |
| P2 | User | Framework-knowledge-gap explanation | one-way (output) |
| P2 | P3 | Explains why supplementary loci exist | one-way data dependency |
| P3 | User | Supplementary loci enumeration with reasoning | one-way (output) |
| P3 | P4 | The loci structure the path composition | one-way data dependency |
| P4 | User | Scope-choice structure with default recommendation | one-way (output) |
| P4 | P5 | The path D contains an investigation that P5 specifies | one-way |
| P5 | User | Future-considerations and investigation flags | one-way (output) |

### Assumptions-not-data check

- **P3 assumes** terminology.md's declared authority is load-bearing (the doc's own claim is honored in practice). Verifiable by user. Low risk; the assumption is grounded in the doc's own text.
- **P3 assumes** how_config_should_be.md is the canonical config-locus for translation behavior. Verifiable by user. Low risk; the file's content and name confirm.
- **P3 assumes** translation_principals.md's authority status is investigable (the user can determine which file is authoritative). High likelihood; the user authors both.
- **P4 assumes** all paths meet "easy" criterion as composite. Verified in sensemaking; low risk.
- **P5 assumes** code-level changes are a future consideration (not immediate); verified in sensemaking via the "unknown tier-system implementation status" finding.

All assumptions surfaced; mitigated by transparency.

---

## Step 6 — Order by Dependency

**LEVEL 0 — Parallel (both set the frame):**
- **P1 (primary YES with structural reasoning)**
- **P2 (framework-knowledge-gap explanation)**

**LEVEL 1 — After L0:**
- **P3 (supplementary loci with reasoning)** — depends on P1 (sets the primary) + P2 (explains why more loci exist).

**LEVEL 2 — After P3:**
- **P4 (5-path scope-choice + default)** — depends on P3 (the paths reference the loci by name).
- **P5 (future considerations + investigations)** — depends on P4 (path D's investigation is one of P5's specifications) but can be assembled in parallel since P4 only references P5's investigation, doesn't depend on P5's full content.

Critical path: P1/P2 → P3 → P4. 3 levels.

### Visual

```
LVL 0:    ┌── P1 ──┐  ┌── P2 ──┐
          │(YES)   │  │(gap)   │
          └────┬───┘  └───┬────┘
               │          │
               └────┬─────┘
                    ▼
LVL 1:    ┌──── P3 ─────┐
          │(supplementary│
          │   loci)      │
          └──────┬───────┘
                 │
          ┌──────┴──────┐
          ▼             ▼
LVL 2:  P4              P5
       (paths +        (future
        default)        + investig.)
```

---

## Step 7 — Self-Evaluate

### Minimum 3-dimension evaluation

| Dimension | Check | Verdict |
|---|---|---|
| **Independence** | Each piece is answerable without reading sibling pieces (except through interfaces) | **PASS** — each piece has its own scope; cross-piece flows are explicit. |
| **Completeness** | No aspect of the whole falls through gaps | **PASS** — covers YES confirmation [P1], gap explanation [P2], supplementary loci [P3], scope choice [P4], future considerations [P5]. |
| **Reassembly** | Pieces + interfaces reconstruct the whole | **PASS** — together they form the YES-WITH-CAVEATS deliverable; user gets confirmation, the surfacing-finding explanation, the locus enumeration, the choice structure, and the future-flags. |

### Full 7-dimension evaluation

| Dimension | Check | Verdict |
|---|---|---|
| **Independence** | Per above | PASS |
| **Completeness** | Per above | PASS |
| **Reassembly** | Per above | PASS |
| **Tractability** | Each piece single-focused-pass shaped | **PASS** — P3 is the largest (3 loci to enumerate); others are smaller. P3 still single-pass-shaped. |
| **Interface clarity** | Cross-piece flows explicit | **PASS** — 9 interfaces listed; 5 assumptions surfaced. |
| **Balance** | Complexity proportional | **PASS** — P3 is ~2-3× the smallest; no 80%-one-piece. |
| **Confidence** | Top-down + bottom-up agree | **PASS** — Step 3 atom validation confirmed all 5 boundaries at HIGH confidence. |

### Determination-mechanism piece check

| Concept | Runtime determination | Determination-mechanism piece |
|---|---|---|
| "Primary locus structural correctness" | Does the mechanism's pattern fire in `harmony_layer.md`? | **P1** (EA-7 trigger evaluation result) |
| "Supplementary-locus relevance" | Does this doc declare authority on the decision type? | **P3** (per-locus reasoning) |
| "User's preferred scope" | Which path does the user want? | **P4** (5-path structure surfaces the choice) |
| "translation_principals.md authority status" | Is it the authoritative principles doc? | **P5** (investigation procedure) |
| "Code-level engagement readiness" | Is the tier system implemented in code? | **P5** (future-consideration flag) |

All runtime determinations addressed. PASS.

### Failure-mode self-check

| Failure mode | Status |
|---|---|
| 1. Premature decomposition | NO — sensemaking SV6 clarified the whole. |
| 2. Wrong boundaries | NO — cut at low-coupling valleys; bottom-up agreed. |
| 3. Hidden coupling | LOW — 5 assumptions surfaced; each mitigated. |
| 4. Missing pieces | NO — completeness check passed. |
| 5. Over-decomposition | NO — 5 pieces; no trivial fragments. |
| 6. Ignoring dependencies | NO — explicit 3-level order. |
| 7. Imbalanced | NO — P3 ~2-3× the smallest. |

No failure modes triggered.

---

## Final Deliverable Summary

| # | Piece | Question | Level |
|---|---|---|---|
| **P1** | Primary YES with structural reasoning | How is the YES confirmed (in-doc edit to `harmony_layer.md` is primary locus) with structural reasoning (EA-7 trigger evaluation)? | 0 |
| **P2** | Framework-knowledge-gap explanation | How is the surfacing discovery (10 docs not 3) communicated non-blamingly and framed as additive? | 0 |
| **P3** | Supplementary loci with per-locus reasoning | How are the supplementary loci (terminology.md / how_config_should_be.md / translation_principals.md pending) presented with their per-locus reasoning? | 1 |
| **P4** | Scope-choice structure with default | How is the 5-path scope-choice structure presented with a default recommendation? | 2 |
| **P5** | Future considerations and investigations | How are code-level future considerations, the translation_principals.md investigation procedure, and not-deep-read docs flagged? | 2 |

5 pieces; 3 levels; critical path = 3 levels deep. All pieces have verification criteria. All interfaces explicit. All assumptions surfaced.

**Decomposition verdict: PROCEED.**
