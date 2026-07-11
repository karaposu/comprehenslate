# Surfacing — What principles/policies exist, and does firing-time cleanly apply to each?

## User Input

`_branch.md` (firing-time categorization diagnostic + design). Territory: the comprehenslate SKILL's principle/policy corpus (`SKILL.md`; `references/core/{harmony_layer.md, translation_principals.md, advanced_principles.md, notes.md}`; `references/config/schemas.py` Policy classes) + the two prior findings. Purpose: enumerate the specific principles/policies that would be tagged with firing-time (`fireable_at_first_pass` = can fire during generation to get it right the first time; `fireable_at_second_pass` = needs a finished draft to check against; maybe both), and gather evidence on the two forks — (Fork 1) inert-metadata vs operational-driver; (Fork 2) does firing-time cleanly apply to each heterogeneous artifact. Sub-questions: (1) enumerate the corpus — homogeneous or heterogeneous?; (2) is firing-time cleanly decidable per entry?; (3) inert-vs-operational evidence; (4) does the Tier system already classify?; (5) do the prior finding's two gates map onto first/second pass?

Mode: `artifact` · Entry point: `signal-first` · Territory: `explicit-bounded`.

---

## Traversal Trace

| # | Region | Item (identifier — NOT content) | Relevance | Conf | Note |
|---|---|---|---|---|---|
| 1 | harmony_layer.md | The 3-Pass method (Meaning Lock → Harmony Map → Target Reconstruction) | **core** | HIGH | the two gates live here; Pass-1 = generation-foundation, Pass-3 = reconstruction; 3 moments vs the proposed 2 tags |
| 2 | harmony_layer.md | Tier 1 — non-negotiable meaning-carrying harmony (~13 entries: implied Q-A flow, cause-effect chaining, escalation/de-escalation, iltifat, havuz-convergence, antonym pairing, ellipsis, …) | **core** | HIGH | preserve-WEIGHT classification already exists; each is first-pass-holdable AND second-pass-checkable → mostly BOTH |
| 3 | harmony_layer.md | Tier 2 — high-priority comprehension-supporting harmony (~12 entries: grammatical parallelism, ring composition, chiasmus, thematic bracketing, …) | **core** | HIGH | same dual character; weight-tier ≠ firing-time |
| 4 | harmony_layer.md | Tier 3 — context-dependent harmony (PRESERVE-WHEN/SACRIFICE-WHEN: register consistency, synonym chaining, particle threading, …) | **core** | HIGH | ALREADY carries a second classification axis (context-condition); firing-time would be a THIRD axis |
| 5 | harmony_layer.md | Tier 4 — aesthetic/sacrificeable (referenced) + the hard constraints (no meaning-change, no add/remove, no merge/split sentence, no logic-reversal) | sub | HIGH | the hard constraints are near-mechanical second-pass checks (esp. omission = "no remove") |
| 6 | translation_principals.md | The ~80 "On X" analytical-detection principles ("detect when the text does X → preserve/annotate it": iltifat, nazm, istilzam, tense-as-meaning, restriction-as-liberation, …) | **core** | HIGH | **the largest bloc; these are COMPREHENSION-time (fire while reading the source), arguably a phase BEFORE generation — neither first-pass-generate nor second-pass-check** |
| 7 | translation_principals.md | Methodological meta-principles: line 16 "two-step: comprehend first, then validate"; line 10 "sentence/clause-level informed by document-level"; line 18 "preserve all valid meanings" | **core** | HIGH | line 16 IS the first/second-pass distinction stated as principle; these are meta (about the process, not tagged BY it) |
| 7b | translation_principals.md | line 96 — the no-smoothing rule ("omitting an uncomfortable nuance to make it cleaner is corruption; don't smooth away") | **core** | HIGH | the user-referenced always-on policy; DUAL — hold while writing AND check after; also lives in notes.md:86 |
| 8 | notes.md | line 313 — polysemy: "local construction picks the sense; plausibility backstop" (the "work" vs "foothold" case the user cites) | **core** | HIGH | clearly first-pass-fireable (pick right sense while writing) AND second-pass-checkable; the user's own example of a dual principle |
| 9 | notes.md | line 317 — decompression (dimensionally-compressed term → render one dimension + transliterate + parenthetical) | sub | MED | first-pass rendering strategy; checkable after |
| 10 | notes.md | The "On X" list (overlaps translation_principals.md heavily — near-duplicate corpus) | sub | MED | notes.md and translation_principals.md substantially duplicate; tagging would hit both |
| 11 | advanced_principles.md | Escalation-chain (small-cycle-proves-large) | **core** | HIGH | comprehension-time detection + generation-time preservation + check — spans ALL phases |
| 12 | advanced_principles.md | Self-illuminating-text principle (passage explains itself; don't add footnotes) | sub | HIGH | first-pass constraint (don't over-explain while writing) + second-pass check (did I add crutches?) |
| 13 | advanced_principles.md | istilzam (single word → entailment chain, e.g. Rahman → 7 attributes) | sub | HIGH | comprehension-time detection primarily |
| 14 | schemas.py | Policy classes (SourceApparatusPolicy, NonMainLangPartsPolicy, ArchaicRegisterPolicy, HonorificsPolicy, FormulaicOpeningsPolicy, EmbeddedPoetryPolicy, VoiceMarkingPolicy, …) | **core** | HIGH | config-driven RENDERING decisions (footnote vs inline, preserve-original vs translate); almost all DUAL + low-stakes — render per policy while writing, trivially check after |
| 15 | schemas.py | TranslationConfig axes A1-A8 (reader_level, domain_expertise, …) | sub | HIGH | these are config INPUTS that principles fire relative to (A1=conversational is what "allegorical" should have been held against), not themselves taggable principles |
| 16 | SKILL.md | Step 5 "produce the translation. Apply: [flat bag]" (line 73) + Rule 1 "read all reference files" | sub | HIGH | baseline: the flat bag is where first/second-pass sequencing is absent; the prior inquiry's fix |
| 17 | prior finding 2026-07-11_00-24 | the two gates (generation-time meaning-lock + post-draft check) + the un-run 3-Pass | **core** | HIGH | first-pass ↔ gate 1; second-pass ↔ gate 2 → the tags formalize this finding (with a 2-vs-3 granularity caveat) |
| 18 | prior finding 2026-07-10_23-03 | the "dual-shaped principles" correction (fire at generation OR at check) | **core** | HIGH | the premise; confirms dual is real — and surfacing shows dual is the MAJORITY, not the exception |

---

## State Summary

**Territory echo:** the comprehenslate SKILL's principle/policy corpus + the two prior findings.
**Purpose echo:** enumerate what would be tagged with firing-time, and whether firing-time cleanly applies.

**Coverage map:**
- harmony_layer.md — **confirmed** (3-Pass; Tier 1-4; hard constraints; core).
- translation_principals.md — **confirmed** (the ~80 "On X" detection principles + the methodological meta-principles + the no-smoothing rule; core).
- notes.md — **confirmed** (near-duplicate of translation_principals' "On X" list + polysemy line 313 + decompression line 317; sub/core).
- advanced_principles.md — **confirmed** (escalation-chain, self-illuminating-text, Bismillah/hasr, istilzam; core/sub).
- schemas.py — **confirmed** (Policy classes = config-driven rendering; TranslationConfig axes = inputs, not taggable; core/sub).
- SKILL.md — **confirmed** (Step 5 flat bag; the sequencing-absence baseline; sub).
- prior findings — **confirmed** (the two gates; the dual-shaped premise; core).

**The decisive findings (for downstream):**

- **DF1 — the corpus is deeply HETEROGENEOUS (≥4 kinds), and "firing-time" applies differently to each.** (A) **Harmony components** (harmony_layer.md Tier 1-4) — structural features to preserve; (B) **analytical-detection principles** (~80 "On X" in translation_principals.md / notes.md + advanced_principles) — "detect that the source does X"; (C) **policies** (schemas.py) — config-driven rendering decisions; (D) **methodological meta-principles** (two-step, no-smoothing, preserve-all-valid-meanings, sentence-informed-by-document). Tagging "the principles/policies" is not tagging one homogeneous list.

- **DF2 — DUAL ("both") is the COMMON case, not the exception.** Most harmony components (Tier 1-3) and most detection principles can be *held while writing* (first-pass) AND *verified against the draft* (second-pass). The user's tentative "maybe both" undersells it: **both is the majority**. A binary partition in which most entries land in "both" is a weak discriminator — it does not carve the corpus into two useful sets.

- **DF3 — the two-category scheme appears to be MISSING A PHASE: comprehension.** The largest bloc — the ~80 "On X" detection principles (item 6) + escalation-chain + istilzam — fire at **comprehension time** (while reading the *source*), which is neither "generation" (first pass) nor "check" (second pass). The real pipeline has **≥3 moments**: comprehend/analyze the source → generate the draft → check the draft. The prior finding's 3-Pass also has **3 passes**. A **2-category** firing-time tag has a granularity mismatch with both the 3-phase pipeline and the 3-Pass method. (Reading "first pass" broadly as "everything up to the draft" = comprehend+generate would rescue the 2-category scheme — but that conflates the very comprehend-vs-generate distinction the prior inquiries worked to separate.)

- **DF4 — the Tier system already classifies harmony components, on an ORTHOGONAL axis.** Tier 1-4 sorts by preserve-**weight** (how costly to lose), not firing-**time** (when it can act). Tier 3 adds a **context-condition** axis (PRESERVE-WHEN/SACRIFICE-WHEN). So firing-time would be a **new, orthogonal** axis (not a duplicate) — but it means a harmony component would carry **three** classification axes (weight + context-condition + firing-time). Metadata load is a real cost to weigh.

- **DF5 — Fork 1 leans OPERATIONAL-OR-LITTLE-VALUE, with a self-undercutting twist.** The tag earns its keep only by *driving the two gates* — the first-pass set becomes what Pass-1/generation must hold; the second-pass set becomes the auto-generated Pass-3 check-agenda. As inert documentation it adds little beyond the Tier system. BUT (from DF2) because most principles are "both," the auto-generated second-pass check-agenda would be **nearly the whole corpus** — which fails to deliver the *small, focused* check-agenda that is the value proposition. The genuinely second-pass-**dominant** items are few and mostly the near-mechanical hard-constraint checks (item 5: omission-diff, no-add, no-merge/split).

- **DF6 — the prior finding's two gates DO map onto first/second pass (formalization confirmed), with the 2-vs-3 caveat.** Gate 1 (generation-time meaning-lock) ↔ fireable_at_first_pass; gate 2 (post-draft check) ↔ fireable_at_second_pass. So the tags *are* a formalization of the prior finding — but the 3-Pass has three moments (lock / map / reconstruct) and the tag has two, so the mapping is lossy where it matters (is Pass-3 harmony reconstruction "first pass" or a distinct third moment?).

**Concept-names list (identifier · type · provenance · gloss):**
- `heterogeneous-corpus` · coined · DF1 · four kinds (harmony components / detection principles / policies / meta-principles) tag differently.
- `both-is-the-majority` · coined · DF2 · most principles are dual-fireable, weakening a binary partition.
- `missing-comprehension-phase` · coined · DF3 · the ~80 detection principles fire at comprehension, a third moment the 2-tag scheme omits.
- `firing-time-orthogonal-to-tier` · structural-reference · DF4 · Tier = weight; firing-time = when; a new axis, not a duplicate.
- `check-agenda-too-large` · coined · DF5 · because most are "both," the auto-generated second-pass agenda ≈ the whole corpus.
- `tags-formalize-the-two-gates` · structural-reference · DF6 · first/second ↔ gate1/gate2, with a 2-vs-3-pass granularity caveat.
- `second-pass-dominant-few` · coined · DF5 · the genuinely check-only items are few (the near-mechanical hard constraints).

**Frontier flags (for downstream):**
- FF1 — Should the scheme be **3-phase** (comprehend / generate / check) instead of 2, to fit the actual pipeline + the 3-Pass? Or is 2 deliberately coarse and sufficient? (→ Sensemaking / Innovation)
- FF2 — Given "both is the majority" (DF2), is the *useful* output not a per-principle partition but the **identification of the second-pass-DOMINANT minority** (the small check-agenda)? I.e., tag not "can it fire at second pass" but "must it wait for second pass" (reliability-of-firing, not possibility). (→ Innovation)
- FF3 — Does the tag add value beyond the **already-designed 3-Pass wiring** from the prior inquiry, or is it that wiring's metadata layer (the thing that tells Pass-1 what to hold and Pass-3 what to check)? Fork 1 hinges here. (→ Sensemaking / Critique)
- FF4 — Scope: policies (item 14) are almost all low-stakes "both"; the meta-principles (item 7) are about the process, not tagged by it. Should tagging be restricted to the substantive **harmony components + detection principles**, excluding policies and meta-principles? (→ Decomposition)

**Recency distribution:** not load-bearing (static reference corpus).

**Workspace-populated status:** `{populated: true, populated-at: 2026-07-11_01-16, extent: 18 items across 7 regions; 11 core / 5 sub / 2 baseline-core}`.

## Telemetry
- Mode: artifact · entry: signal-first
- Cycles: 4 (harmony_layer cluster · translation_principals/notes cluster · advanced_principles cluster · schemas/SKILL/priors cluster) · items enumerated: 18 · core 11 / sub 5 / baseline 2
- Boundary-discovery: not fired (explicit-bounded)
- Convergence: territory swept at identity resolution; the corpus's heterogeneity + the dual-majority + the missing-comprehension-phase are all located and cross-confirmed; no item filtered at uncertain relevance.
- Failure-modes checked: Missed-relevance (none — all 5 sub-questions answered), Surfaced-irrelevance (TranslationConfig axes tagged sub as inputs-not-principles, not dropped), Purpose-loss (no — tight firing-time bias), Recency-bias (n/a static).
- items_with_mtime: 18 / items_without_mtime: 0 (filesystem-backed corpus)
- Self-assessment: **PROCEED** — the five sub-questions are decisively answered: (1) heterogeneous, ≥4 kinds; (2) firing-time is NOT cleanly decidable as a clean partition — dual is the majority and a comprehension phase is missing; (3) inert-vs-operational leans operational-or-little-value with the check-agenda-too-large twist; (4) the Tier system already classifies but on an orthogonal axis; (5) the two gates DO map onto first/second pass, formalizing the prior finding, with a 2-vs-3 granularity caveat. Four frontier flags handed downstream (esp. FF2's "tag must-wait-for-second-pass, not can-fire-at-second-pass" reframe).
