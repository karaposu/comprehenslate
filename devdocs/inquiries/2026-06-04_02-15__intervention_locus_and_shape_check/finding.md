---
status: active
model: claude-opus-4-7[1m]
effort: max
---
# Finding: intervention_locus_and_shape_check

## Question

From `_branch.md`. The user has been through two prior diagnostic inquiries — translation_failure_root_cause_diagnosis at `devdocs/inquiries/2026-06-03_23-30__translation_failure_root_cause_diagnosis/finding.md` and doc_internal_contradiction_cause_and_prevention at `devdocs/inquiries/2026-06-04_01-36__doc_internal_contradiction_cause_and_prevention/finding.md` — both of which recommended additions/edits to `harmony_layer.md` (and related framework docs) as the intervention. The user is sanity-checking: is in-doc addition to `harmony_layer.md` the right intervention shape and locus, or is something different warranted?

Two clauses joined by "or":
1. **Is in-doc addition to `harmony_layer.md` the right intervention?** Structural reasoning + evidence for or against.
2. **What alternative loci/shapes exist?** Complete enumeration with dispositions; criteria for when each alternative would be right.

The goal in `_branch.md`: clarity (definitive answer with structural reasoning, not vague affirmation), coverage (alternatives surfaced systematically), honesty (don't just confirm the prior recommendation — actually re-test it). The user wants confidence to commit to implementation, not blanket reassurance.

## Finding Summary

- **YES, in-doc addition/edit to `harmony_layer.md` is the right primary intervention.** The diagnosed contradiction empirically lives in `harmony_layer.md`'s tier section; fixing it requires editing that file. The procedural prevention mechanism from the prior inquiry 2 (the per-entry test from MVD-1 + the audit checklist from MVD-2) has a structural trigger ("any entry that derives a classification from a stated principle in the same doc"); that trigger fires only in `harmony_layer.md` among the framework docs. The primary locus is structurally correct, not just by-default.

- **But: surfacing revealed the framework is bigger than the prior inquiries treated.** The user's original instruction bounded the territory to three docs (`harmony_layer.md`, `notes.md`, `advanced_principles.md`). The project root actually has 10 .md files plus a Python code package (`comprehenslate/`). The prior inquiries respected the user's stated bound; they were correct within the 3-doc frame. The wider 10-doc frame is additive, not invalidating.

- **Three supplementary loci surface** when the wider frame is considered. They serve different decision types — file-level + decision-type-level — so they don't redirect the primary recommendation but complement it:
  - `terminology.md` — for sub-case naming ("register-as-style," "register-as-alternation"). The doc declares its own authority on definitions ("If a design doc uses a term differently from this file, this file wins"). Sub-case naming is a term-definition act, so per the doc's own rule, the names belong there too.
  - `how_config_should_be.md` — for the audience-spec rule from the first inquiry's S9. This file is the canonical config-locus for translation behavior (defines audience levels: Native / late learner / late learner simple / poetic). The S9 rule's config-level component fits here.
  - `translation_principals.md` — for principle authorship. This is a 73K file overlapping with `notes.md` (~38K); it may be the authoritative principles doc with `notes.md` as derivative. Status pending investigation — sample the file structure + compare with `notes.md` + ask the user which is authoritative.

- **The user picks the scope.** Five paths exist on a minimum-to-maximum spectrum. The default recommendation is Path B with explicit alternative defaults. All paths within "easy" criterion (per the prior inquiry 2's operationalization) as composite.

- **Code-level changes are flagged as future consideration.** `terminology.md` mentions actual classes (`TranslationMemory` in `memory.py`); the framework has a code project being built. If the tier system is implemented in code, the doc fix should align with code; currently the tier system's implementation status is unknown. Future-flag, not immediate-scope.

- **Other docs not deep-read:** `advanced.md`, `my_notes.md`, `README.md`, `roadmap.md`. Surfacing did not examine these. Possible future scope-expansion targets if the user wants broader framework-consistency discipline.

## Finding

The user asked a frame-check question after two prior inquiries proposed adding to `harmony_layer.md`. This finding's job is to validate that recommendation against the full intervention-locus possibility space and surface anything the prior inquiries missed. The answer is YES-WITH-CAVEATS — YES on the primary recommendation, plus three supplementary loci the prior inquiries didn't engage with because the original territory was bounded to three docs.

### 1. Why YES is right

The diagnosed contradiction (`harmony_layer.md` classifies "register consistency" at Tier 3 but its own ranking principle implies register-as-alternation should be Tier 1) empirically lives in `harmony_layer.md`'s tier section. The fix's location is fixed by the location of the problem. There is no alternative locus that lets you fix this contradiction without editing `harmony_layer.md`.

The prior inquiry 2's procedural prevention mechanism (the per-entry test + audit checklist that catches the widespread Tier 3 vulnerable-template pattern) has a structural trigger: "any entry that derives a classification from a stated principle in the same doc." Evaluating each framework doc against the trigger:

- `harmony_layer.md` — fires (meta-principle + 4-tier classifications)
- `notes.md` — does not fire (flat principle list; no classification framework)
- `translation_principals.md` — does not fire (flat principle list, same shape as notes.md)
- `advanced_principles.md` — does not fire (worked examples)
- `terminology.md` — does not fire (term definitions)
- `how_config_should_be.md` — does not fire (config spec)

The mechanism's primary locus is `harmony_layer.md` not by default but because that's the only framework doc with the structural pattern. The recommendation is right.

### 2. The framework is wider than the prior inquiries treated

The user's first message in the original chain said "read only the files i mentioned: notes.md, advanced_principles.md, and harmony_layer.md." Both prior inquiries respected that bound. They produced recommendations consistent within the 3-doc frame.

The project root actually has 10 .md files plus a Python package. The seven docs the prior inquiries didn't engage with: `translation_principals.md` (73K — likely authoritative principles file), `terminology.md` (canonical terms with declared authority), `how_config_should_be.md` (config spec), `roadmap.md` (project trajectory), `README.md` (project intro), `advanced.md` (unread), `my_notes.md` (small informal notes). Plus the `comprehenslate/` Python package implementing some of the framework's logic.

This is not a blame finding. The user bounded the territory; the AI respected the bound; the bound was reasonable for the failure-diagnosis question. The wider scope only became relevant when the question shifted to "is the recommended locus right, or are there alternatives?" — at which point the AI should have surfaced "let me check what else lives at the project root" before answering. That happened here. The discovery is additive to the prior recommendations, not invalidating.

### 3. Three supplementary loci

The wider frame surfaces three additional places where parts of the broader prevention discipline can land. Each maps to a different decision type:

- **`terminology.md` — sub-case naming (term-definition decision).** When prior inquiry 2's mechanism splits a contradicting Tier 3 entry into sub-cases (e.g., "register-as-style" vs. "register-as-alternation"), the sub-case names are term-definition acts. Per `terminology.md`'s own declared rule ("If a design doc uses a term differently from this file, this file wins"), the canonical names belong there. The `harmony_layer.md` entries can reference the canonical names defined in `terminology.md`.

- **`how_config_should_be.md` — audience-spec config (config decision).** Prior inquiry 1 recommended an audience-spec interpretation rule (S9 — interpret "C1 English speakers" as capability, not vocabulary license). The S9 rule has a doc-level component (the principle in `notes.md`) AND a config-level component (the default `skopos` setting). `how_config_should_be.md` is the canonical config-locus for translation behavior (it defines audience levels: Native / late learner / late learner simple / poetic). The S9 rule's config-level component fits there.

- **`translation_principals.md` — principle authority (pending investigation).** This 73K file at the project root overlaps heavily with `notes.md` (~38K). Spelled "principals" (matches the user's typo pattern), suggesting user authorship. Sampling confirmed structural overlap (same principle entries: iltifat, multi-meaning preservation, micro-to-macro mirroring). If this is the authoritative principles doc with `notes.md` as derivative, the prior inquiry 1's principle additions (register-matching, polysemy-disambiguation) may belong here too. Investigation procedure: sample the full file + compare with `notes.md` + ask the user which is authoritative.

### 4. Scope choice (sliding scale, default callout)

```
↓ less ─────────────────────────────────────────────────── more →

Path A: primary only (= prior inquiry 2's MVD/Full Emergent Assembly)
        ~15-30 min day-one + 15-60 min retroactive sweep
        in-doc edits to harmony_layer.md per MVD-1, MVD-2, MVD-3
        Use this if you want the minimum that addresses the diagnosed issue.

Path B: A + terminology.md sub-case naming  ← recommended default
        +~5 min
        Add canonical names for sub-cases the prior inquiry's MVF-4 splits.
        Recommended because terminology.md's declared authority is the
        strongest empirical claim among the supplementary loci.

Path C: A + how_config_should_be.md audience-spec config
        +~5-10 min
        Use this if prior inquiry 1's S9 audience-spec rule is high priority.
        Choose over B if your translation work makes C1-misread-class
        errors more common than terminology drift.

Path D: A + investigate translation_principals.md authority
        +~10 min one-time investigation
        Use this if you suspect notes.md is a stale derivative.
        Investigation: sample + compare + decide which is authoritative.

Path E: A + all supplementary (B + C + D)
        ~30-45 min additional total
        Use this if you want comprehensive framework-consistency now.

↑ less ─────────────────────────────────────────────────── more →
```

### 5. What is intentionally NOT in this finding

- **Code-level changes.** The `comprehenslate/` Python package may carry parts of the framework's logic. If the tier system is implemented in code, the doc fix should align. Currently the implementation status is unknown. Flagged as future consideration; not addressed now.
- **Deep-read of `advanced.md`, `my_notes.md`, `README.md`, `roadmap.md`.** Surfacing did not examine these. They may contain framework-relevant content; possible future scope-expansion targets.
- **Architectural Layer-2 fix.** Inherited from prior inquiry 1's S7 RESEARCH FRONTIER. Unchanged.
- **Cross-doc framework-consistency discipline** beyond the EA-7 per-entry trigger. The prior inquiry 2's mechanism doesn't apply outside `harmony_layer.md`. Cross-doc consistency (e.g., notes.md not contradicting translation_principals.md) is a different class of problem; separate inquiry if user wants it.

## Next Actions

### MUST

- **What:** Decide which path (A through E) you want to pursue. **Who:** the user. **Gate:** observable — the decision is communicated (verbally, or by acting on a path). **Why:** the supplementary loci recommendations are scope-choice-dependent; downstream actions assume a path is picked.

- **What:** Whichever path you pick, implement Path A's primary component first — the prior inquiry 2's MVD-1 (meta-principle edit) + MVD-2 (Doc Consistency Audit section) + MVD-3 (retroactive sweep). **Who:** the user. **Gate:** observable — `harmony_layer.md` shows the meta-principle edit; the Doc Consistency Audit section exists; the retroactive sweep has run over the ≥12 Tier 3 entries. **Why:** Path A is the foundation; all higher paths build on it.

### COULD

- **What:** If Path B or E — add canonical sub-case names ("register-as-style," "register-as-alternation," and any other sub-cases the audit reveals) to `terminology.md`. **Who:** the user. **Gate:** observable — `terminology.md` includes the new entries. **Why:** preserves doc-stated authority hierarchy; prevents term-drift between `harmony_layer.md` and `terminology.md`. **Depends-on:** MUST item "Path A primary implementation" — sub-case names follow from the audit's results. This COULD is GATED — do not act until Path A's audit identifies the sub-cases.

- **What:** If Path C or E — add the audience-spec interpretation rule (prior inquiry 1's S9) to `how_config_should_be.md` as a config-level default. **Who:** the user. **Gate:** observable — `how_config_should_be.md` includes the audience-spec default rule. **Why:** addresses the proximate trigger (C1-misread) at the config layer in addition to the principle layer. **Depends-on:** prior inquiry 1's S9 doc-level rule should also be added to `notes.md` (per that inquiry's MUST item). This COULD compounds with that prior MUST.

- **What:** If Path D or E — investigate `translation_principals.md` authority status: read the file fully, compare structurally with `notes.md`, decide which is authoritative, document the decision. **Who:** the user (or the AI if user requests). **Gate:** observable — a one-line note recorded somewhere (e.g., in `README.md` or in a new `framework_authority.md`) stating which file is authoritative. **Why:** prior inquiry 1's principle additions may need to mirror into `translation_principals.md` if that's the authoritative file. **Depends-on:** none; can run in parallel with Path A.

- **What:** Optional — request the AI to investigate `translation_principals.md` now (Option β from critique's scope-of-delivery question) instead of deferring. **Who:** the user opts in. **Gate:** observable — the user requests it; the AI samples + compares + reports. **Why:** if the user wants the complete picture in one delivery rather than as follow-up, this option exists.

### DEFERRED

- **What:** Engage with code-level tier-system implementation (the `comprehenslate/` package). **Gate:** condition-bound — revival fires when the tier system's code-side implementation status is known (sample `comprehenslate/`'s code to check; or user reports). **Why (if revived):** prevent doc-code drift if the code carries the tier system at runtime.

- **What:** Deep-read of `advanced.md`, `my_notes.md`, `README.md`, `roadmap.md` for possible framework-consistency expansion. **Gate:** condition-bound — revival when the user wants broader framework-consistency beyond `harmony_layer.md`'s tier system + the three supplementary loci. **Why (if revived):** these docs may contain framework-relevant content that the current inquiry didn't engage with.

- **What:** A future inquiry on cross-doc framework-consistency discipline (e.g., ensuring `notes.md` and `translation_principals.md` don't contradict each other). **Gate:** condition-bound — revival when the user encounters a cross-doc consistency issue or when the framework has matured enough that this becomes a recurring problem. **Why (if revived):** the EA-7 per-entry trigger doesn't catch cross-doc inconsistencies; a different mechanism is needed.

## Reasoning

The diagnosis arrived through five disciplined passes plus inheritance from two prior inquiries. The reasoning below explains why the YES-WITH-CAVEATS answer holds over the alternatives.

### Why YES (the primary recommendation) survived

Sensemaking's Phase 3 (Ambiguity Collapse) tested the counter-interpretation that the surfacing discovery (10 docs not 3) might invalidate the prior recommendation. The counter failed on structural grounds: the contradiction's location is invariant under territory expansion. The contradiction empirically lives in `harmony_layer.md`'s tier section; adding more docs to the territory doesn't move the contradiction. Additionally, the EA-7 trigger evaluation confirmed the prevention mechanism's primary locus is structurally correct — only `harmony_layer.md` has the principle/classification split structural pattern the mechanism is designed to catch. The recommendation is right, not just default.

### Why the supplementary loci are real

Two empirical evidences anchor the supplementary loci:

1. **`terminology.md` explicitly declares its own authority on term definitions.** The doc's opening text: "If a design doc uses a term differently from this file, this file wins." This is a doc-stated locus-authority rule. The sub-case names ("register-as-style," "register-as-alternation") that prior inquiry 2's mechanism produces are term-definition acts; per the doc's own rule, they belong in `terminology.md` regardless of which other doc could nominally host them.

2. **`how_config_should_be.md` is the canonical config-locus for translation behavior.** Its content defines audience levels (Native / late learner / late learner simple / poetic) and other config switches. Prior inquiry 1's S9 audience-spec rule has a config-level component (default skopos handling); that component belongs in the config locus, not just in the doc-level principle.

A third supplementary locus (`translation_principals.md`) is flagged pending investigation. Sampled content overlaps with `notes.md` — same principles in expanded form. If it's the authoritative principles doc, prior inquiry 1's principle additions may need to mirror there. The investigation is bounded (~10 min) and can run in parallel with Path A.

### Why the code-level changes are deferred, not addressed

`terminology.md` mentions actual classes (`TranslationMemory` in `memory.py`). This means the framework includes a code project. But: the tier system's specific code-side implementation status is unknown without engaging the code; engaging the code is out of the user's question's scope. Deferring is the cautious path. If the user wants the code-level investigation, it can be a future inquiry.

### Why the user picks the scope, not the AI

The user explicitly stated in `_branch.md`'s goal section: "the user decides whether to proceed with the prior inquiries' recommendations as-is or pivot to a different intervention." Imposing a scope on the user's behalf violates that stated value. Surfacing the choice + recommending a sensible default + naming when alternative defaults would be preferred — this respects user agency.

The default recommendation is Path B (primary + terminology.md sub-case naming) because terminology.md's declared authority is the strongest empirical claim among the supplementary loci, and the cost (~5 additional minutes) is trivial. Path A and Path C are explicitly named as alternative defaults with reasoning for when each would be preferred. The user is not forced toward Path B; the default is a starting point.

### What survived adversarial evaluation

Critique tested 7 candidates against 8 evaluation dimensions (6 default + 2 project-specific: scope-honesty and user-agency). All 7 survived; 2 received refinements (S4 sliding-scale presentation gained an explicit default callout; S5 default recommendation gained explicit alternative-default callouts). 0 candidates were killed. The deliverable's shape is robust across the candidate space.

Critique also surfaced a meta-level scope-of-delivery question: should the AI investigate `translation_principals.md` NOW or defer? The recommendation is Option α (deliver now; investigation as follow-up if user wants) — respects the user's question-answering loop without arbitrarily expanding scope. Option β (investigate first) is offered in Next Actions as a user-opt-in.

## Open Questions

### Monitoring

- After path implementation, does the harmony report's audit (per prior inquiry 2's MVD-2) actually flag contradictions when they occur? Observable after the next substantive edit to `harmony_layer.md`.
- If Path B/E is chosen, do the canonical sub-case names in `terminology.md` get referenced from `harmony_layer.md`, or do the docs drift apart? Observable after ~2-3 edit cycles.

### Blocked

- The code-level engagement is blocked on knowing the tier system's implementation status in the `comprehenslate/` package. Until that's investigated, code-level work cannot be specified.

### Research Frontiers

- Cross-doc framework-consistency discipline (mechanisms that catch inconsistencies BETWEEN docs, not just within a single doc). The EA-7 mechanism doesn't address this; a different mechanism is needed. Frontier.
- Whether the framework-knowledge-gap pattern (treating 3 of N relevant docs) recurs in future inquiries. If yes, a standard "framework boundary verification" step in MVLw inquiries might be useful.

### Refinement Triggers

- If `translation_principals.md` turns out to be the authoritative principles doc (per Path D investigation), prior inquiry 1's principle additions (register-matching, polysemy-disambiguation, audience-spec rule) need to mirror there. Trigger: completion of Path D investigation.
- If user feedback after Path A implementation indicates the supplementary loci would have been useful (e.g., term drift between docs), Path B/C/E becomes retroactively higher priority. Trigger: observable in user feedback.

## Source Input

<details>
<summary>Raw user input for this finding</summary>

```text
u said Layer 2 — Structural (the amplifier in the documents). Two structural defects in the framework allowed the proximate trigger to produce undetected failures. The first defect is an active misclassification: harmony_layer.md classifies "register consistency" as Tier 3 ("important for reader comfort but doesn't change meaning"). The doc's own ranking principle states that the closer a harmony component is to carrying meaning, the higher its priority. When source text uses register-alternation as a structural device — when plain folk diction grounds elevated theology, as the Fifth Word does — register IS meaning-carrying. By the doc's own principle, register-as-alternation should be Tier 1. The doc fails to distinguish register-as-style (which is Tier 3 correctly) from register-as-alternation (which should be Tier 1). The misclassification is an in-doc proof of internal inconsistency, not just an absence of guidance. The second defect: the harmony report at the bottom of the translation file (the framework's self-audit instrument) has zero register-related entries. Its content is generated from the tier system, so when the tier system silently demotes a feature, the audit silently omits it. The audit is structurally blind to the failure mode that occurred — the framework cannot see what its own classification told it not to look for.

so the solution is to make an addition to harmonly_layer.md ? or different?
```

</details>
