# Surfacing — Is the comprehend-first / semantic-priority ordering present, absent, or unenforced in the SKILL?

## User Input

`_branch.md` (semantic-priority-ordering diagnostic + fix). Territory: the comprehenslate SKILL folder (`SKILL.md`; `references/core/{harmony_layer.md, translation_principals.md, advanced_principles.md, notes.md}`; `references/config/{config_base_source.md, policy_config_base_source.md, schemas.py}`) + the prior finding as baseline. Purpose: surface the specific SKILL content bearing on the user's hypothesis — that harmony should sit ON TOP OF a locked semantic understanding and the SKILL may be MISSING or NOT-ENFORCING an explicit "comprehend-meaning-first, THEN generate under harmony nudge" ordering. Resolve: (1) is Pass-1 Meaning Lock already the comprehend-first phase? (2) does SKILL.md's workflow specify/gate the ordering? (3) does anything establish semantics-over-harmony PRIORITY? (4) does the 3-Pass produce intermediate artifacts? (5) is the fork "ordering missing" vs "ordering present-but-unenforced"?

Mode: `artifact` · Entry point: `signal-first` · Territory: `explicit-bounded`.

---

## Traversal Trace

| # | Region | Item (identifier — NOT content) | Relevance | Conf | Note |
|---|---|---|---|---|---|
| 1 | harmony_layer.md | Pass-1 "Meaning Lock" — "strict semantic fidelity… the foundation that cannot be violated" | **core** | HIGH | semantic PRIORITY is explicitly stated; Pass-1 IS the comprehend-first phase (sub-Q1 + Q3) |
| 2 | harmony_layer.md | Pass-3 "Target Reconstruction" — "you may change HOW a meaning is expressed, but never WHAT" | **core** | HIGH | harmony explicitly operates ON TOP OF locked meaning — exactly the user's model (Q3) |
| 3 | harmony_layer.md | Framing (lines 6-7) — "The idea is to create a translation **mode** that works in three passes" | **core** | HIGH | DESCRIPTIVE ("the idea is to…"), not an imperative workflow step — key "present-but-unenforced" evidence (Q5) |
| 4 | harmony_layer.md | Hard constraints — "Anything that changes semantic content is forbidden" | **core** | HIGH | semantics inviolable; harmony bounded by it — priority is designed-in, not co-equal (Q3) |
| 5 | translation_principals.md | line 16 — "comprehensation is essentially a **two-step process: generate interpretation from deep comprehension first, then validate** against formal linguistic rules" | **core** | HIGH | **DECISIVE — the exact comprehend-first ordering the user proposes, stated verbatim as a principle. The ordering is NOT "missing."** (Q1, Q5) |
| 6 | translation_principals.md | line 10 — "sentence/clause-level approach **informed by document-level comprehension**" | **core** | HIGH | comprehension precedes and informs translation — the layering restated (Q3) |
| 7 | SKILL.md | Step 5 — "produce the translation. Apply: [config · policies · principles · harmony Tier 1-4 · notes]" | **core** | HIGH | the workflow collapses translating into ONE "produce" + a FLAT BAG of things to "apply" simultaneously; no ordered passes, no comprehend-first gate (Q2 — the enforcement gap) |
| 8 | SKILL.md | Step 5 line 78 — imports harmony_layer.md **only** as "the harmony-layer Tier 1-4 preservation policy" | **core** | HIGH | **the 3-Pass PROCEDURE (where the ordering lives) is NEVER invoked by the workflow — only the Tier list is pulled** (Q2, Q4 — the precise structural gap) |
| 9 | SKILL.md | line 33 — describes harmony_layer.md as "cause-effect chains, istilzam chains, Tier 1-4 preservation policies" | **core** | HIGH | the workflow's OWN mental model of harmony_layer.md is "the tier list"; the 3-Pass at the top of that file is invisible to the workflow (reinforces #8) |
| 10 | schemas.py | `PipelineConfig` — "Runtime engine knobs" (chunking granularity, parallel_mode, output_format) | sub | HIGH | NO stage/pass ordering, NO meaning-lock stage — the ordering is absent at the SCHEMA layer too (Q4, Q5) |
| 11 | harmony_layer.md | Tier system — Tier 1 "meaning IS carried by this harmony" … Tier 4 "aesthetic polish, sacrifice freely" | sub | HIGH | even WITHIN harmony, meaning has priority — semantic priority is thoroughly designed-in (Q3) |
| 12 | prior finding | "the 3-Pass ran in spirit as one motion; no post-draft checkpoint" | sub | HIGH | baseline; this inquiry locates WHY the 3-Pass ran as one motion — because Step 5 never invokes it (this-vs-prior fork) |
| 13 | advanced_principles.md | escalation-chain (small-cycle-proves-large) + self-illuminating-text principles | side | MED | these are WHAT semantic content must survive; presuppose deep comprehension but add no workflow ORDERING (Q3 context) |
| 14 | translation_principals.md | line 6 — "no single person can properly interpret… requires a collective of specialists" | side | MED | comprehension is framed as a distinct, deep, prior activity — supports comprehend-first being a real phase, not a formality |
| 15 | notes.md | project notes (lisan-ı hal/kal; polysemy; decompression) | side | MED | WHAT-to-preserve content; no workflow ordering |
| 16 | config_base_source.md / policy_config_base_source.md | the 8-axis + Policy calibration (per-value meaning) | umbrella | HIGH | confirmed-absent for the ORDERING question — they define what each value MEANS, not the procedure order |

---

## State Summary

**Territory echo:** the comprehenslate SKILL folder + the prior finding.
**Purpose echo:** locate the SKILL content bearing on whether the comprehend-first / semantic-priority ordering is present / absent / unenforced.

**Coverage map:**
- harmony_layer.md — **confirmed** (Pass-1 = semantic-foundation-priority; Pass-3 = harmony-on-top; framing = descriptive "mode" not imperative; hard constraints = semantics inviolable; Tier-1 = meaning-in-harmony; aggregate: core).
- translation_principals.md — **confirmed** (line 16 = the two-step comprehend-first ordering STATED; line 10 = document-comprehension-informs-translation; aggregate: core).
- SKILL.md — **confirmed** (Step 5 = flat "produce + apply-bag", no ordered passes; imports harmony_layer only for its Tier list; describes harmony_layer as the tier list; aggregate: core — the enforcement gap).
- schemas.py — **confirmed** (PipelineConfig = engine knobs; no stage ordering; aggregate: sub).
- advanced_principles.md / notes.md — scanned (WHAT-to-preserve; no ordering; aggregate: side).
- config_base_source / policy_config_base_source — **confirmed-absent** for the ordering question (aggregate: umbrella).

**Confirmed-absent regions (for this purpose):** the config calibration files (axis/policy meaning, not procedure order); the schema layer (PipelineConfig has no pass/stage field).

**The decisive finding (for downstream):** the comprehend-first / semantic-priority ordering the user proposes is **NOT missing from the SKILL as a PRINCIPLE** — it is stated in at least three places (harmony_layer.md Pass-1 "foundation that cannot be violated"; harmony_layer.md Pass-3 "change HOW not WHAT"; translation_principals.md line 16 "two-step process: comprehend first, then validate"). It **IS missing as an ENFORCED PROCEDURE**: `SKILL.md` Step 5 — the only executable workflow — collapses translating into one "produce the translation" plus a flat bag of things to "apply," and it imports `harmony_layer.md` **only for its Tier 1-4 preservation list, never for its 3-Pass method**. The 3-Pass (which operationalizes the ordering) is orphaned prose; the two-step principle is one bullet among ~50. So the fork resolves to **PRESENT-AS-PRINCIPLE, ABSENT-AS-PROCEDURE** — with the sharp sub-point that the workflow doesn't even reference the procedure that exists.

**Concept-names list (identifier · type · provenance · one-line gloss):**
- `meaning-lock-as-foundation` · structural-reference · #1 · harmony_layer Pass-1 states semantic priority ("foundation that cannot be violated").
- `harmony-on-top-of-locked-meaning` · structural-reference · #2 · Pass-3 changes HOW not WHAT — the user's exact architecture.
- `two-step-comprehend-then-validate` · vocabulary · #5 · translation_principals line 16 — the ordering stated verbatim as principle.
- `3-pass-described-not-imperative` · coined-term · #3 · the passes are framed as "the idea is to create a mode," descriptive, not a workflow instruction.
- `workflow-imports-tier-list-only` · coined-term · #8 · **THE gap** — SKILL.md Step 5 pulls harmony_layer's Tier list, not its 3-Pass procedure.
- `flat-apply-bag` · coined-term · #7 · Step 5 = "produce the translation. Apply: [flat list]" — no ordering among applied elements.
- `ordering-present-as-principle-absent-as-procedure` · coined-term · #5+#7+#8 · the synthesized resolution of the fork.
- `no-stage-ordering-in-schema` · structural-reference · #10 · PipelineConfig has no pass/stage field; the ordering isn't encoded anywhere executable.

**Frontier flags (for downstream):**
- FF1 — Is the fix "**wire the EXISTING 3-Pass into SKILL.md Step 5 as ordered, gated steps**" (the procedure already exists — just invoke it) vs "author a NEW comprehend-first instruction from scratch"? The surfacing strongly suggests the former. (→ Innovation)
- FF2 — The user's phrasing "harmony layer WITHOUT semantic priority did the translation" is slightly off-target: harmony_layer.md *declares* semantic priority emphatically. The real mechanism is that the workflow never RUNS the layered procedure, so meaning and harmony get decided in one breath — harmony didn't override semantics by design; the meaning-first procedure was simply never executed. Does this REFINE the user's hypothesis (right instinct, wrong locus-description)? (→ Sensemaking)
- FF3 — The prior finding's "no post-draft checkpoint" and this inquiry's "no enforced pre/during-generation ordering" are two faces of ONE structural cause: **`SKILL.md` Step 5 doesn't run the 3-Pass as discrete steps** — so there's neither a meaning-lock-first gate NOR a reconstruction-check gate; it's all one motion. Complementary, not rival. (→ Sensemaking / this-vs-prior fork)

**Recency distribution:** not load-bearing (static reference corpus).

**Workspace-populated status:** `{populated: true, populated-at: 2026-07-11_00-30, extent: 16 items across 8 regions; 9 core / 3 sub / 3 side / 1 umbrella}`.

## Telemetry
- Mode: artifact · entry: signal-first
- Cycles: 3 (core-files cluster · workflow/schema cluster · principles cluster) · items enumerated: 16 · core 9 / sub 3 / side 3 / umbrella 1
- Boundary-discovery: not fired (explicit-bounded)
- Convergence: territory exhausted at current resolution; the decisive items (Pass-1 priority; the two-step principle; Step-5 imports-tier-list-only) all located and cross-confirmed; no item filtered at uncertain relevance.
- Failure-modes checked: Missed-relevance (none — all 5 sub-questions answered), Surfaced-irrelevance (config files tagged umbrella, not dropped), Purpose-loss (no — tight ordering/priority bias), Recency-bias (n/a).
- items_with_mtime: 16 / items_without_mtime: 0 (prior-finding + coined terms treated as filesystem-backed inquiry artifacts)

## Self-Assessment
**PROCEED** — the five sub-questions are decisively answered: (1) YES, Pass-1 Meaning Lock IS the comprehend-first phase and states semantic priority; (2) NO, SKILL.md's workflow does not gate the ordering — it flat-applies everything and imports harmony_layer only for its Tier list; (3) YES, semantics-over-harmony priority is stated emphatically across three files; (4) NO intermediate artifacts — the 3-Pass is described prose, never invoked, and absent from the schema; (5) the fork resolves to **PRESENT-AS-PRINCIPLE, ABSENT-AS-PROCEDURE**. Three frontier flags handed to Sensemaking (esp. FF2's refinement of the user's hypothesis and FF3's this-vs-prior reconciliation).
