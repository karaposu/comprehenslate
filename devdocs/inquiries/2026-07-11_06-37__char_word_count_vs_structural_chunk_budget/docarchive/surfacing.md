## User Input

Territory = (A) the three+ real translation files in `mytrasnlations/asayi_musa/` (+ any other pairs) — MEASURE them; (B) the prior findings this inquiry re-tests (04-48 chunk-by-structure + quarantine; the two 06-14 chunking findings); (C) `schemas.py` chunking_budget unit; (D) reasoning region: char-vs-word-vs-token stability + the confound (what 2 data points can bear) + replace-vs-complement (size budget vs harmony snapping); (E) the coined term "comprehenslation integrity". Purpose: surface the evidence on whether char/word count beats structural units as the budget unit, what the real examples establish (confound honestly surfaced), which measure is best, what comprehenslation integrity is, and whether a size budget replaces or complements harmony snapping. Full branch: `_branch.md`.

---

# Surfacing Artifact — signal-first, artifact case (+ reasoning sub-region)

## Traversal Trace

| # | Region | Items | Relevance | Conf |
|---|---|---|---|---|
| 1 | (A) real files — locate | `mytrasnlations/` (typo confirmed as the real dir name); `asayi_musa/` holds 4 files; `5th_word/` holds a 2nd pair | core | HIGH |
| 2 | (A) real files — MEASURE | the size table below (measured with python, unicode chars) | **core** | HIGH |
| 3 | (A) confound — `mistakes.md` | the failure log for ikinci_huccet — documents the actual errors | **core** | HIGH |
| 4 | (A) 3rd data point | `5th_word/org.md`+`eng.md` — a 2nd small example | core | HIGH |
| 5 | (A) genre/density confound | footnote density near-identical across the two asayi_musa texts | sub | HIGH |
| 6 | (B) prior 04-48 | recommended chunk-by-structure; quarantined ~3500 as reasoned-not-measured | core | HIGH |
| 7 | (B/C) 06-14 + schemas.py | `chunking_budget:int\|None` (untyped, no unit doc); `chunking_granularity` separate; `fixed-budget-with-snap` already a mechanism option | **core** | HIGH |
| 8 | (D) measure reasoning | char vs word vs token stability; source-side vs output-side | core | MED |
| 9 | (D) confound reasoning | what n=2–3 with size-correlated outcome can bear | **core** | HIGH |
| 10 | (E) coined term | "comprehenslation" grep-absent elsewhere → newly coined | sub | HIGH |

## The measurements (DF1 — the empirical anchor, corrected)

| example | SOURCE chars | OUTPUT chars | src→out ratio | words (out) | ~tok (out, c/4) | user judgment |
|---|---|---|---|---|---|---|
| **4_mesele** | 4,345 (`4_mesele.md`, Turkish) | 7,080 (`4_mesele_en.md`) | 1.63× | 1,213 | ~1,770 | **GOOD** |
| **5th_word** | 4,148 (`org.md`) | 6,164 (`eng.md`) | 1.49× | 1,105 | ~1,541 | (not stated; same small regime) |
| **ikinci_huccet** | **ABSENT** (no source file present; user says "~11,000") | **28,330** (`ikinci_huccet_en.md`) | — (2.57× if src≈11k) | 5,194 | ~7,082 | **FAILED** |

**What the numbers actually say (vs the user's framing):**
- The user's **"3500"** ≈ the **4_mesele SOURCE** (actually **4,345** chars — right ballpark, ~24% under). So "3500" is a source-side figure drawn from the good example.
- The user's **"~11,000 char" for ikinci_huccet does NOT match** the actual `_en` file (**28,330** chars). Most likely "11,000" is the (absent) **Turkish source** length, and the **translation over-expanded to 28,330** — a **2.57× ratio** versus the healthy **1.49–1.63×** of the two good examples. That over-expansion is itself a candidate **failure symptom** (the model padding/elaborating), not just "a long input."
- **Directionally the user is right:** two good examples at ~4,100–4,300 source chars; one failure at (claimed) ~11,000 source / 28,330 output. Small succeeded, big failed. But the exact numbers are loose and the **counted side is ambiguous** (source vs output).

## The confound, made concrete (DF2 — the decisive finding)

`mistakes.md` (the user's own error log for the FAILED ikinci_huccet translation) documents these error types:
- **Register error:** "allegorical" used — "not easy word, in our config it is obvious this word shouldn't be used." → a **config/register-adherence** failure (the SKILL's register principle not applied).
- **Word-sense/meaning errors:** *lisan-ı hal / lisan-ı kal* collapsed into "gibberish" (the body-language vs voiced-language distinction lost); *iş* → "work" when it means attention/care; *esbab* → "secondary causes" (bad); *şahıs* → "figure" (should be persona/entity). → **Meaning-Lock (3-Pass Pass-1) / polysemy** failures.
- **Fluency/awkwardness errors:** "some one thing among," "no one lacking a boundless wisdom… can poke a finger" (confusing, "maybe comma is missing"). → **harmony/naturalness** failures.

**These are principle-NOT-fired / collapse-in-one-motion errors** — the SAME class the prior chain (`2026-07-10_23-03` + `2026-07-11_00-24`) attributed to the **un-wired 3-Pass**, NOT distinctively "the model skipped instructions because the text was long." The failure's **mechanism is therefore ambiguous** between:
- **(A) adherence-decay-under-load** — a bigger working-set → the model drops the register/meaning principles; and
- **(B) the un-wired-3-Pass** — the principles are never systematically applied; the short texts *survived on the model's native capacity* and the long one didn't.
The two are **indistinguishable in this data** (success perfectly correlates with size). The user's own closing question in `mistakes.md` — *"was SKILL folder content followed well or not, what happened??"* — is exactly this adherence question.

## Supporting confound reads

- **DF3 — genre/density similarity.** Both asayi_musa texts are allegorical theological dialogues with near-identical footnote density (4_mesele_en: 8 marks / 7,080 chars ≈ 1 per 885; ikinci_huccet_en: 32 / 28,330 ≈ 1 per 885). They differ mainly in **length (≈4×)**, which *directionally* supports "length is the salient difference" — but does not resolve mechanism (still n=2).
- **DF4 — what 2–3 size-correlated points can bear.** Legitimately: an **existence proof** ("a text this big failed; texts this small did not") + a **rough direction** (bigger → more likely to fail). NOT: a **validated threshold** (no failure observed near 3,500 to locate a cliff), and NOT the **mechanism** (length vs method confounded). "3,500" is a defensible **conservative anchor** from the good example's source size — stronger than the prior finding's "zero evidence," weaker than "the proven cutoff."

## The measure + the config reality (DF5–DF7)

- **DF5 — char vs word vs token.** The three examples' source→output char ratios (1.49, 1.63) are fairly stable → **character count is a reasonably stable cross-text measure** for this corpus, and the more legible/language-robust one. **Words** are less stable across the Turkish source (agglutinative — fewer, longer words: 4_mesele 6.8 char/word) vs English output (~5.2 char/word). **Tokens** are the most model-faithful (load actually scales with tokens) but the least human-legible, and Turkish tokenizes to more tokens/char than English. So: **characters = stable + legible proxy; tokens = truest to model load but opaque; words = weakest.**
- **DF6 — the config field is UNTYPED.** `schemas.py:126` is `chunking_budget: int | None = None` — **no unit is documented** (prior work merely *assumed* tokens). So the user's char proposal does not fight an existing char-vs-token schema decision; it would simply **define what that int counts**. Low-friction.
- **DF7 — size-budget and structural-snapping already COEXIST in the schema, and the dispute partly dissolves.** `chunking_budget` (a size) and `chunking_granularity` (the structural ladder) are **separate fields**, and `chunking_mechanism_override` **already lists `fixed-budget-with-snap`**. That mechanism *is* the reconciliation: **the budget (in chars) sets the target size; structure sets where the cut lands (snap to the nearest harmony boundary ≤ budget).** The prior finding itself said "chunk by structure, *snapping to harmony boundaries*." So "char-count vs structure" is a **false either/or** — the honest form is **char-BUDGET + structural-SNAP**, which is already a designed option. The user's real, correct correction is narrower: **the SIZE TARGET should be a stable unit (chars), not a structural level** — because a structural level's size varies too much to be a reliable *target*.

## Concept (DF8)

- **"comprehenslation integrity"** — grep-confirmed **newly coined** (appears only in this inquiry's own files). From context: **comprehension + translation fidelity held together under load** — the outcome the budget protects. "Comprehenslate" is the project's own name (comprehension-translation fusion), so "comprehenslation" = the project's core act; "integrity" = it staying whole. **Adjacent existing concepts:** harmony_layer's Tier-1/2 preservation; the "collapse-in-one-motion" failure mode (23-03); the "transformation working-set" (04-48). The term usefully **names the protected quantity** the whole chunking effort serves.

## State Summary

- **Territory:** the real translation corpus (`mytrasnlations/`), the prior findings (04-48, 06-14×2), `schemas.py`, + reasoning region.
- **Coverage:** A/B/C confirmed; D (reasoning) covered; E confirmed. Confirmed-absent: no ikinci_huccet SOURCE file; no pre-existing use of "comprehenslation."
- **Concept-names:** comprehenslation-integrity (coined) · fixed-budget-with-snap (schemas mechanism) · transformation-working-set (04-48) · chunking_budget-is-untyped · source-side-vs-output-side-budget · over-expansion-2.57× · collapse-in-one-motion (prior).

## Decisive Findings (compressed)

- **DF1** the numbers: 4_mesele src 4,345 / out 7,080 (GOOD); 5th_word src 4,148 / out 6,164 (unjudged, small); ikinci_huccet out 28,330 (FAILED), source absent. User's "3500"≈source of the good one; "11000"≠the 28,330 output (likely the absent source; translation over-expanded 2.57×).
- **DF2 (KEY)** `mistakes.md` shows the failure's errors are register + word-sense + fluency = **principle-not-fired / un-wired-3-Pass class**, not distinctively length-skipping → **mechanism confounded** (length-decay vs method-absence indistinguishable at n=2).
- **DF3** the two texts are same-genre, same-density → length is the main visible difference (directional support for the user), but doesn't resolve mechanism.
- **DF4** 2–3 size-correlated points ⇒ existence-proof + direction, NOT a validated threshold or a mechanism; 3,500 = defensible conservative anchor.
- **DF5** characters = stable + legible proxy; tokens = truest-to-load but opaque + TR/EN asymmetric; words = weakest.
- **DF6** `chunking_budget:int|None` is UNTYPED → char proposal just *defines the int*, low friction.
- **DF7** char-BUDGET + structural-SNAP already coexist (`fixed-budget-with-snap`); "char vs structure" is a false either/or — the user's valid narrower point is that the SIZE TARGET should be a stable unit, not a variable structural level.
- **DF8** "comprehenslation integrity" = newly coined; names the comprehension+translation fidelity the budget protects; adjacent to Tier-1/2 preservation + collapse-in-one-motion.

## Frontier Flags

- **FF1 (central)** — the mechanism confound: does size CAUSE the failure (adherence-decay) or merely CORRELATE (un-wired-3-Pass, short-text-survives)? `mistakes.md` error-types lean method; genre-similarity leans length. Sensemaking must adjudicate honestly — likely "both, entangled," carrying the 04-48 complementary-not-rival result.
- **FF2** — source-side vs output-side budget: the user's 3,500 is source-side, but the failed one's over-expansion is output-side; the "working-set" spans both. Which side does the budget count?
- **FF3** — the measure choice (char vs word vs token) + per-model scaling (lower for smaller models = a per-model char budget).
- **FF4** — is `5th_word` a success? A stated judgment would make it a 2nd success data point (~4,148 source) and firm up the "small succeeds" side.
- **FF5** — the 2.57× over-expansion as an independent failure symptom (does the model over-elaborate when overloaded?) worth its own attention.

## Telemetry

- Mode: artifact + reasoning sub-region · entry: signal-first · cycles: 3 · items: ~24 · core: 8, sub: 3.
- Measurements done with tools (python unicode char counts + wc-equivalent), not estimated.
- Boundary-discovery: not fired (explicit-bounded).
- Workspace-overload: not hit.
- Failure modes checked: Missed-relevance (mitigated — found the un-requested `mistakes.md` + `5th_word` 3rd pair) · Surfaced-irrelevance (none) · Recency-not-used-as-verdict (mtimes noted: ikinci_huccet + mistakes are Jul-10, the recent failed run; 4_mesele Jun-07 — did NOT gate relevance).
- **Verdict: FLAG** — surfacing substantially REFRAMES the inquiry: (1) the user's numbers are directionally right but loose and count an ambiguous side; (2) the confound is SEVERE and now concrete (`mistakes.md` errors are un-wired-3-Pass-class, not length-specific); (3) "char vs structure" is a false either/or — the real, defensible correction is "the size TARGET should be a stable unit (chars), snapping to structure," which the schema ALREADY supports (`fixed-budget-with-snap`). Weight relocates to the mechanism-confound (FF1) + the target-unit reframe (DF7).
