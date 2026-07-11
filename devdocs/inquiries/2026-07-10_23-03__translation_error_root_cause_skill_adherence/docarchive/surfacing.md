# Surfacing — Governing SKILL clauses for the 7 translation errors

## User Input

`_branch.md` (root-cause diagnostic). Territory (artifact case): the comprehenslate SKILL folder (SKILL.md; references/config/{config_base_source.md, policy_config_base_source.md, schemas.py}; references/core/{translation_principals.md, advanced_principles.md, harmony_layer.md, notes.md}); user-memory (register-fidelity, polysemy); the produced translation (mytrasnlations/asayi_musa/ikinci_huccet_en.md); source Turkish (content0020.xhtml). Purpose: draw into attention the SPECIFIC governing clauses each of the 7 named errors should have been caught by, so the diagnosis checks adherence against actual text rather than asserting.

Mode: `artifact` · Entry point: `signal-first` · Territory: `explicit-bounded` (Boundary-discovery sub-phase skipped).

---

## Traversal Trace

| # | Region | Item (identifier — NOT content) | Relevance | Conf | Note |
|---|---|---|---|---|---|
| 1 | config_base_source.md | A1 `conversational` › vocabulary_breadth: "common Latinate enters; EXCLUDES dense academic (`ratiocination`,`ostensibly`), literary-archaic" | **core** | HIGH | governs err-1 (allegorical) |
| 2 | config_base_source.md | A1 `conversational` › syntactic_processing: "multi-clause LINEAR; loses thread on nested subordination"; restructuring-test SPLIT/UNEMBED/LINEARIZE/RESOLVE-GARDEN-PATHS | **core** | HIGH | governs err-5 (no one lacking…can), err-4 (some one thing among) |
| 3 | config_base_source.md | §"5 always-on Layer-2 policies" › #3 Polysemy disambiguation via local construction ("local construction picks sense, NOT surrounding momentum") | **core** | HIGH | governs err-6 (iş→work) |
| 4 | config_base_source.md | §"5 always-on policies" › #5 No-smoothing ("prefer slight target awkwardness over loss; do not smooth") + its DUAL (don't over-produce) | **core** | HIGH | governs err-2a (omission), err-7 (over-translation) |
| 5 | config_base_source.md | §"5 always-on policies" › #2 Register-alternation ("do not flatten plain→ornate; C1 ≠ vocabulary display") | **core** | HIGH | governs err-1 (allegorical), register axis |
| 6 | config_base_source.md | A5 `lightly-domesticated` ("naturalization where NOT load-bearing; load-bearing terms preserved w/ gloss") + A2 `lay` PARAPHRASE-IN-LAYMAN-TERMS | sub | HIGH | governs err-7 (esbab), err-1 |
| 7 | config_base_source.md | §"Per-axis order of consultation" ("A1/A5/A6/A7 read at EVERY reference/choice/passage") | **core** | HIGH | process: consult-per-choice mandated but unverified |
| 8 | config_base_source.md | A1 `conversational` › inference_capacity ("2-step; loses nested") | side | MED | supports err-5 |
| 9 | harmony_layer.md | Pass 1 "Meaning Lock" hard constraints: "Removing information present in the original is FORBIDDEN / Adding information … FORBIDDEN" | **core** | HIGH | governs err-2a (omission), err-7 (over-add) |
| 10 | harmony_layer.md | 3-Pass methodology (Meaning Lock → Harmony Map → Target Reconstruction) as discrete passes | **core** | HIGH | process: passes NAMED but not enforced as gates |
| 11 | harmony_layer.md | Tier-1 "Ellipsis patterns"; Pass-3 permitted-vs-forbidden (naturalness allowed, meaning-change forbidden) | sub | MED | target-naturalness license for err-4/err-5 |
| 12 | translation_principals.md | "abandoning a small evil → greater evil: omitting a difficult/uncomfortable nuance to make it 'cleaner' … is a form of corruption" | **core** | HIGH | governs err-2a (omission) |
| 13 | translation_principals.md | "dimensionally-compressed terms" + delalet-i iltizamiye ("commander vs leader vs guide implies different attribute sets") | sub | MED | governs err-3 (figure vs person/character) |
| 14 | advanced_principles.md | Self-illuminating / word-order-as-meaning (hasr); "the internal wiring must survive" | side | MED | context for err-2b (lisan-ı hal clause logic) |
| 15 | notes.md | lisan-ı hal / lisan-ı kal appears verbatim ("lisan-ı hali, lisan-ı kal suretinde") in the hasr/tevhid discussion | **core** | HIGH | governs err-2b (the device is documented) |
| 16 | notes.md | polysemy "din" (multi-sense) + Extra-Notes "dimensionally compressed beyond target capacity" decompression strategy | sub | HIGH | governs err-6, err-3 |
| 17 | memory | feedback_translation_polysemy ("local construction picks sense; plausibility backstop; momentum does not override") | **core** | HIGH | governs err-6 (iş) |
| 18 | memory | feedback_translation_register ("don't pull plain registers into ornate/archaic; C1 ≠ vocabulary display") | **core** | HIGH | governs err-1 (allegorical) |
| 19 | SKILL.md | Workflow Step 5 "produce the translation" — a SINGLE monolithic emit; no post-draft verify/QA step | **core** | HIGH | process: the systemic gap candidate |
| 20 | SKILL.md | Rules 1 & 5 ("always read all reference files"; "Tier 1-2 non-negotiable") | sub | MED | read-mandate present; application-check absent |
| 21 | ikinci_huccet_en.md | error loci: "allegorical dialogue…mute tongue…actual speech" (para 1); "figure"; "some one thing among"; "no one lacking…can"; "no work out of me"/"find work"; "on behalf of secondary causes" | **core** | HIGH | the 7 defects in the output |
| 22 | content0020.xhtml | source loci: "basit avamın fehmine gelecek bir muhavere-i temsiliye…lisan-ı hali, lisan-ı kal suretinde"; "bir şahıs farzediyoruz"; "mevcudat-ı âlemden bir şeye Rab"; "…sahibi olmayan bize parmak karıştıramaz"; "sen benden iş bulamazsın"; "esbab namına" | **core** | HIGH | the 7 source phrases |
| 23 | policy_config_base_source.md | 7 Policy classes (NonMainLang, SourceApparatus, Honorifics, …) | umbrella | HIGH | confirmed-absent for THIS purpose (errors are not policy-layer) |
| 24 | schemas.py | TranslationConfig / Policy / Pipeline schemas | umbrella | HIGH | confirmed-absent (config values not in dispute) |

---

## State Summary

**Territory echo:** comprehenslate SKILL folder + memories + produced translation + source Turkish.
**Purpose echo:** surface the specific governing clause per error, for adherence-checking.

**Coverage map:**
- config_base_source.md — **confirmed** (A1 vocab+syntax, A5, policies #2/#3/#5, per-axis-consultation all located; aggregate: core).
- harmony_layer.md — **confirmed** (Pass-1 no-remove/no-add, 3-Pass methodology, Tier-1 ellipsis; aggregate: core).
- translation_principals.md — **confirmed** (omission-as-corruption; dimensional-compression/iltizamiye; aggregate: core/sub).
- advanced_principles.md — scanned (self-illuminating / word-order; aggregate: side).
- notes.md — **confirmed** (lisan-ı hal/kal verbatim; polysemy; decompression; aggregate: core/sub).
- SKILL.md — **confirmed** (workflow single-pass emit; read-mandate; aggregate: core — the process gap).
- memory — **confirmed** (register + polysemy feedback; aggregate: core).
- ikinci_huccet_en.md / content0020.xhtml — **confirmed** (7 error loci ↔ 7 source loci paired).

**Confirmed-absent regions (for this purpose):** policy_config_base_source.md; schemas.py — the 7 errors are register/syntax/word-sense/omission failures, none policy-layer or schema-value disputes.

**Concept-names list (identifier · type · provenance · one-line gloss):**
- `A1-conversational-vocab-exclusion` · vocabulary · #1 · dense-academic words excluded → "allegorical" is on the wrong side of the line.
- `A1-conversational-syntax-linear` · vocabulary · #2 · nested negation / center-embedding to be restructured → "no one lacking…can".
- `policy-3-local-construction` · structural-reference · #3,#17 · construction picks the sense, not the metaphor's momentum → "iş"=foothold not "work".
- `policy-5-no-smoothing` · structural-reference · #4 · no removal, no over-production; awkwardness-preserving not awkwardness-creating.
- `policy-2-register-alternation` · structural-reference · #5,#18 · plain source stays plain; C1 ≠ vocabulary display → "allegorical".
- `pass1-meaning-lock-no-remove` · structural-reference · #9,#12 · removing source info is forbidden → dropped "basit avamın fehmine gelecek".
- `three-pass-not-enforced` · coined-term · #10,#19 · the corrective passes exist in harmony_layer but SKILL.md's Step 5 emits in one shot with no gate.
- `lisan-hal-kal-documented` · vocabulary · #15 · the device is in notes.md; the murky rendering wasn't checked against it.
- `dimensional-compression-iltizamiye` · vocabulary · #13,#16 · word choice activates attribute-sets → "figure" vs "person/character".
- `single-pass-emit-gap` · coined-term · #19 · **systemic root-cause candidate**: no verification pass between draft and output.

**Frontier flags (for downstream):**
- FF1 — Is the systemic cause the *absence of a verification pass*, or *reading-without-operationalizing* (knowledge present, not indexed to render-time), or *both*? (→ Sensemaking / Decomposition.)
- FF2 — Which errors are genuine SKILL-violations vs defensible judgment-calls the user still dislikes (err-7 esbab; err-2b lisan-ı hal clarity)? (→ Critique.)
- FF3 — Does the SKILL *contain but fail to enforce* every antidote (early read of Trace suggests YES for 6/7)? (→ Sensemaking anchor.)

**Recency distribution:** not load-bearing here (static reference corpus); mtime not used to weight. All items `source: filesystem` except the two coined-terms (`source: none`).

**Workspace-populated status:** `{populated: true, populated-at: 2026-07-10_23-07, extent: 24 items across 10 regions; 12 core / 5 sub / 3 side / 4 umbrella}`.

## Telemetry
- Mode: artifact · entry: signal-first
- Cycles: 4 (one per region-cluster) · items enumerated: 24 · core 12 / sub 5 / side 3 / umbrella 4
- Boundary-discovery: not fired (explicit-bounded)
- Convergence: territory exhausted at current resolution; no item filtered at uncertain-relevance; umbrella items (policy/schema) rejected only at HIGH-confidence-absence.
- Workspace-overload: not triggered.
- Failure-modes checked: Missed-relevance (none — every error has ≥1 located clause), Surfaced-irrelevance (policy/schema tagged umbrella not dropped), Purpose-loss (no — tight error↔clause bias).
- items_with_mtime: 22 / items_without_mtime: 2

## Self-Assessment
**PROCEED** — every one of the 7 errors has at least one located governing clause (the strongest surfaced pattern: the SKILL demonstrably *contains* the antidote to 6–7 of 7); the process-gap region (SKILL.md single-pass emit + un-enforced 3-Pass) is surfaced as the systemic candidate. Three frontier flags handed to Warm/Sensemaking.
