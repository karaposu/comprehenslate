# Branch: user_research_persona_validation

## Source Input

```text
User research / persona validation (interview translators)    project-space    epistemic    INVESTIGATE-FRONTIER    MED 

do this
```

## Articulation Reference

- **File:** `devdocs/inquiries/2026-06-15_19-17__user_research_persona_validation/articulate_simple.md`
- **Itemize count:** 1
- **Per-item identifiers:** Item 1 (act on R8 from prior Mac-app design inquiry)
- **Verdict:** HIGH-PROCEED
- **Flagged conditions:** none

## Question

### Item 1 — Act on R8 "User research / persona validation (interview translators)"

**Literal statement:** *"User research / persona validation (interview translators) — do this"* — the input invokes route R8 from the prior `comprehenslate_mac_app_design` inquiry's routelister (route signature: project-space × epistemic × INVESTIGATE-FRONTIER × MED priority).

**Kinds of ask the statement carries (MQ1 verdict-axis ambiguities):**
- *deliverable-mode* — produce a research PLAN (interview script + recruitment criteria + analysis framework) the user executes externally / produce a SIMULATED persona-validation report (AI synthesizes hypothetical translator personas and walks them through the Mac-app design) / produce BOTH (hybrid: plan + synthetic-preview)
- *depth-of-research* — lightweight (3-5 sketched personas + key concerns) vs structured (formal interview protocol + analysis rubric + recruitment-screening + expected-deliverables map) vs comprehensive (everything needed to actually conduct + analyze a real interview series)
- *AI-as-substitute* — AI ROLE-PLAYS translator personas and answers design-critique questions as them (synthetic user research; first-pass design-validation when real interviews aren't available) OR AI designs a PROCESS the user runs with real translators later (research-plan-as-instrument)

**Action-endpoints the statement could be targeting (MQ3 intent-axis ambiguities):**
- produce-actionable-research-plan (user takes plan + conducts real interviews later)
- produce-simulated-personas (AI synthesizes likely translator types + concerns for immediate design-validation feedback)
- pressure-test-the-Mac-app-design via simulated translator perspectives (find weak spots; verify differentiator surface is what real theological translators would value)
- identify-what-the-design-is-missing-or-mis-targeting by examining persona-specific needs

## Goal

### Item 1 — user research / persona validation

**Deliverable shape (Deconstruct):** depends on deliverable-mode resolution; plausible shapes are (a) research plan (interview-protocol artifact), (b) synthetic persona-validation report, or (c) hybrid (plan + simulated preview). Kinds = interview protocol + persona profiles + analysis rubric + pressure-test report + gap inventory + recruitment-criteria spec + design-feedback memo. Bounds = the prior Mac-app design finding as the design under validation + `SKILL/references/core/` for translator-substrate assumptions + theological-translation researchers as target persona space + **AI cannot conduct real interviews** (hard structural bound on deliverable shape).

**Motivation-chain ambiguities (MultiDepth WHY-axis):**
- *design-validation* — ensure the Mac app fits real translator workflows; reduce v1 risk before committing to build (R1 in route-map depends on R7 + R8 + R9 completing)
- *gap-discovery* — find features the design misses by examining persona-specific needs
- *recruitment-planning* — know what kind of users to seek when real research starts
- *AI-as-pragmatic-substitute* — use AI synthesis to produce best-effort first-pass when real interviews aren't yet available; surface to user as preview before they invest in real research
- *educational-self-survey* — understand the user-research design space for niche-professional-tool validation generally
- *build-confidence-in-design-choices* — verify the differentiator surface (harmony viz; lineage; collation; principle-derived features) is what real theological translators would value

**Context-need (MQ2):**
- *verdict:* prior `comprehenslate_mac_app_design/finding.md` is the design under validation; `SKILL/references/core/` shows substrate-assumed translator (Nursi-focused; theological; scholarly-leaning)
- *kinds:* research-method patterns (semi-structured interviews; persona validation; jobs-to-be-done; design probes); CAT-tool-user research; academic translation-studies as research subjects; persona-design conventions for niche-professional tools
- *stance:* rigorous-empirical (real interviews gold-standard; AI simulation impossible substitute and shouldn't be claimed) vs pragmatic-substitute (AI synthesis useful first-pass when real interviews unavailable) vs both-with-disclaimer (offer both; flag simulation as synthetic)

**Explicit (and structural) exclusions (MQ4 NOT-list):**
- **AI cannot actually conduct interviews** with real translators — any "results" must be either a plan for someone else to execute, or synthetic personas AI generates from substrate. Structural limit, not user-stated, but load-bearing.
- Implicitly excluded: claiming synthetic personas are empirically validated — they're best-effort syntheses from substrate, not data.
- Out of scope: redesigning the Mac app based on findings (that's a follow-up inquiry).
- Out of scope: providing actual contact info / recruitment channels (criteria only).

## Considered Articulations

### Item 1 — Act on R8 user research / persona validation
1. Produce a complete user-research / persona-validation PLAN — interview script with question categories; recruitment criteria (3-5 translator personas to target — Risale-i Nur Vahide-tradition scholar; Talmud translator; Quran-translation editor; literary Sufi translator; comparative-theology academic); analysis framework; expected-deliverables map — that the user can execute when they recruit real translators later.
2. Produce a SIMULATED persona-validation report — AI synthesizes 4-6 hypothetical theological-translator personas based on the substrate (`references/core/` + Mac-app design); walks each persona through the Mac-app design at key decision points (TC config; Policy choices; live reading; harmony viz; lineage view); reports likely reactions / pain points / feature priorities — explicitly flagged as synthetic for design-validation-only use, not as empirical findings.
3. Produce BOTH the research plan AND a synthetic preview — plan for real execution; simulation demonstrates what insights the process might generate AND provides immediate design feedback. Two-tier deliverable: actionable-plan + best-effort-preview.
4. Pressure-test the Mac-app design via simulated translator perspectives — generate persona-specific critiques of the design: which features each persona would prioritize vs ignore; what's missing; what would feel wrong. Output is a gap-and-misalignment inventory anchored to the personas, not a research plan.

## Scope Check

**Item 1:** Question covers goal. The MQ1/MQ3 ambiguity space is bracketed by Deconstruct bounds (prior Mac-app finding + references/core/ substrate + AI-can't-interview structural limit). The MQ4 NOT-list keeps scope honest. Goal includes motivation surfacing (WHY-axis: design-validation / gap-discovery / recruitment-planning / pragmatic-substitute / educational / build-confidence) and deliverable shape (plan / simulation / hybrid / pressure-test report). Question covers both via the 4 considered articulations.

**Specific-vs-pattern check:** the input invokes a SPECIFIC route (R8 from a specific prior inquiry). The inquiry addresses that specific route, not the broader "how to do user research in general." Acting on R8 = acting on the route's stated purpose (validate the Mac-app design with translator personas) within the substrate constraints.

## Synthesis Trigger

This inquiry synthesizes context from the prior `comprehenslate_mac_app_design` inquiry:

- `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/finding.md` — the Mac-app design under validation; carries commitments about 5-layer architecture, 3-tier triage, 10 principle-derived features, v1 MVP scope (3-9mo single-developer with 3 concurrent providers).
- `/Users/ns/Desktop/projects/comprehenslate/devdocs/inquiries/2026-06-15_16-48__comprehenslate_mac_app_design/routelister.md` — the route field that named R8 specifically.
- `/Users/ns/Desktop/projects/comprehenslate/SKILL/references/core/translation_principals.md` + `advanced_principles.md` + `notes.md` — the substrate that shapes which translator personas the system assumes (Nursi-focused; theological; scholarly-leaning).
- `/Users/ns/Desktop/projects/comprehenslate/SKILL/references/config/policy_config_base_source.md` — the Policy-layer features the user-research would specifically validate.

CONCLUDE will require an `## Inherited Commitments Re-test` section testing the prior commitments against the persona-validation findings — specifically: do the prior commitments (5-layer architecture; the 10 principle-derived features; the 3-tier triage's prioritization) hold up under simulated translator perspectives, or does the validation reveal that any commitment was wrong / mis-prioritized?
