## User Input

`_branch.md` + territory: MEASURE the edited `SKILL/SKILL.md` against the 6 prior findings (coverage per-point; the 5000-vs-3500 divergence; 3-Pass wired or not; verification-pass present or absent; enforcement strength). Artifact case. Save to this folder.

---

# Structural Surfacing — Artifact + Reasoning Anchor

**Mode:** artifact · **Entry point:** signal-first · **Territory:** explicit-bounded (the edited SKILL.md + 6 prior finding.md files + harmony_layer.md + schemas.py).

The whole inquiry turns on measured facts, not memory. The decisive findings (DF) are the core surfaced content.

## Measured facts — the current `SKILL/SKILL.md` (verbatim anchors)

**Chunking (Rules 7-8):**
> "7. **Chunking is NEccesary due to AI focus limit** — AI loses its attention to details and accurate translation when asked to do all at once … process texts in chunks. For Claude Opus 4.8 use chunks of Max ~5000 character (if there is sentence ending or paragrapgh ending you can strecth this up or down … not strict rule but approximation). For Claude Sonet use Max ~2500. For Fable 5, use max ~7000 char"
> "8. … inspect it in terms of lenght (chars,words) and based on model being used pring how many chunks will be used to the user."

**Step 5 translate process (the 4 ordered sub-instructions):**
> "1. First of all, The user's `TranslationConfig` choices … Start by use your understanding to map the given chunk text in target language with most accurate meaning and most loyality to given TranslationConfig selections. But dont concrete the translation due to next instructions will ofc effect them too."
> "2. If `with policies` … default Policy values … But dont concrete …"
> "3. … check case examples for niche situations from `references/core/case_catalog.md` … But dont concrete …"
> "4. The last step is The harmony-layer whcih effects if Harmony Map should applied or not and how and which ones, More details are in `references/core/harmony_layer.md`. Since this was last modifying layer U can concrete the translation now."

**Where the 3-Pass actually lives** — `harmony_layer.md` lines 3-9 (verbatim):
> "The idea is to create a translation mode that works in three passes: Pass 1 — Meaning Lock: Translate every sentence with strict semantic fidelity. No meaning added, removed, or altered … the foundation that cannot be violated. Pass 2 — Harmony Map … Pass 3 — Target Language Reconstruction …"

## Decisive Findings

**DF1 — Chunking is now PRESENT (was absent pre-edit).** `[core / HIGH]` SKILL.md now carries chunking (Rules 7-8) where the pre-edit SKILL had none. Source-character measure; snaps to sentence/paragraph ("you can strecth this up or down"); budget-gated (Rule 8 prints chunk count; short texts pass straight through). It is a **model-facing prose Rule**, not a separate engine call.

**DF2 — The number DIVERGES upward (5000 vs 3500).** `[core / HIGH]` SKILL.md sets Opus ~**5000** chars. Finding 06-37 set a ~**3,500 conservative floor** for Opus, held as a band (floor 3,500 / *demonstrated-safe* 4,345 / unknown above). **5000 sits ABOVE even the single demonstrated-safe point (4,345)** — i.e., *less* conservative than the finding's recommendation, on the unmeasured side of the band. Caveat: 06-37 explicitly quarantined the number as approximate / model-dependent / "not a threshold to hard-code," so 5000 is not "wrong" — but it is the opposite of the finding's *conservative-below-the-safe-point* posture.

**DF3 — Step 5 is no longer a flat one-motion list.** `[core / HIGH]` Finding 00-24 diagnosed the *old* Step 5 as "a flat list of things to apply all at once." The *new* Step 5 is a **4-layer ordered process** (config-map → policies → case_catalog → harmony), where every non-final layer says "**dont concrete** … next instructions will effect them" and the final (harmony) says "**you can concrete now**." This is a real structural change — it explicitly defers finalization, softening the collapse-in-one-motion failure the chain diagnosed.

**DF4 — BUT the 3-Pass is NOT wired as meaning-first / config-blind (THE crux).** `[core / HIGH]` Finding 00-24's fix = rewire Step 5 into the three ordered passes, **Meaning-Lock FIRST**, run **config-BLIND** ("without the style configuration in view, so style can't contaminate comprehension"), sentence-level. The new Step 5.1 does the OPPOSITE at the top: it maps meaning **bound to config** — "map … with most accurate meaning **and most loyality to given TranslationConfig selections**." Config leads; there is no config-blind Meaning-Lock step. The 3-Pass/harmony is demoted to the **LAST** layer (5.4). *Improvement over the 00-24 state:* 5.4 now names "Harmony Map" and points to harmony_layer.md as a step (00-24 found the old SKILL pulled that file "only for its Tier 1-4 preservation policy," orphaning the method). *Shortfall:* the governing structure is config-first, not meaning-first-config-blind — the exact constraint 00-24 said must hold is violated. → **root-cause fix = PARTIAL (gestured, not landed).**

**DF5 — The whole-draft VERIFICATION pass is MISSING.** `[core / HIGH]` Findings 01-09 (config-independent always-run post-draft checks: content-dropped? invented? sentence-boundaries preserved? large-scale structure survived?) and 04-48 (the "back bracket" — check the whole reassembled draft at the end) both call for a post-draft verification pass. SKILL.md has none — Step 5 ends at harmony "concrete now," with no second read-over. Rule 5 (Tier 1-2 non-negotiable) is *inside* the harmony layer, not a separate verification. → **01-09 / back-bracket = MISSING.**

**DF6 — Chunking-as-prose-Rule is the WEAK end of the enforcement gradient.** `[sub / HIGH]` Finding 04-12/04-48: a chunking instruction inside a single run is "a weak nudge the model can quietly ignore"; real enforcement "needs the engine — separate calls per chunk." SKILL.md's Rules 7-8 are exactly that prose nudge. This is the **strongest thing a `.md` file can do**; engine-level enforcement is inherently outside a prose file's reach. → not a "miss" so much as **covered at the honest ceiling of the SKILL layer**; the strong-end enforcement lives in the (unbuilt) engine.

**DF7 — The case_catalog is now wired.** `[sub / HIGH]` Step 5.3 checks `case_catalog.md` for niche cases — a NEW addition (the 139-case catalog just built). A genuine positive add, and the config-derived "agenda" half of 01-09's split (reader-keyed niche checks) partially rides here.

**DF8 — Broken reference.** `[side / HIGH]` SKILL.md line 34 lists `references/core/notes.md` as a file to read in Step 2; that file **does not exist** in the tree. The model would hit a missing file. (It is the file `case_catalog.md` was summarized from — likely removed/renamed.)

**DF9 — harmony_layer.md still bundles method + policy.** `[sub / MED]` 00-24 recommended restructuring harmony_layer.md so its 3-Pass *method* and its Tier *preservation-policy* are separable (so a future workflow can't import the policy while orphaning the method again). harmony_layer.md still bundles both (method at lines 3-9, Tier policy below). Not done — the structural precondition that enables the un-wiring is still present.

## The coverage scorecard (measured, per prior)

| Prior finding | Its "missing point" / recommendation | Covered by the edit? |
|---|---|---|
| **06-37** char-budget | source-char budget snapping to structure; ~3,500 conservative for Opus; band-not-cliff | **PARTIAL** — chunking + snap-to-structure landed; number set to 5000 (above the safe point, less conservative) |
| **04-48** mandatory chunking | budget-gated-always-on; chunk by structure; ~3,500 approximate | **COVERED (core mechanism)** — chunking present, budget-gated, snaps to structure |
| **04-12** enforcement gradient | prose = weak nudge; engine = real enforcer | **COVERED at the SKILL ceiling** — prose nudge done; engine-enforcement out of a .md's reach (correctly the honest limit) |
| **01-09** whole-draft verification | config-independent always-run post-draft checks (back bracket) | **MISSING** — no post-draft verification pass in SKILL.md |
| **00-24** wire the 3-Pass | rewire Step 5 to 3 ordered passes, Meaning-Lock FIRST, config-BLIND | **PARTIAL** — flat-list replaced by a deferred 4-layer process + harmony referenced as a step; but config leads (not meaning-first-config-blind), 3-Pass not the governing structure |
| **23-03** 7-error/one-pass/no-checkpoint | end one-motion generation; add a checkpoint | **PARTIAL** — one-motion softened ("dont concrete until end"); checkpoint still missing (= DF5) |

## Traversal Trace (thin)

| # | Region | Item(s) | Tag | Conf |
|---|--------|---------|-----|------|
| 1 | SKILL.md Rules 7-8 | chunking numbers/measure/enforcement | core | HIGH |
| 2 | SKILL.md Step 5.1-5.4 | the 4-layer translate process | core | HIGH |
| 3 | SKILL.md (whole) | absence of a post-draft verification pass | core | HIGH |
| 4 | SKILL.md 5.3 / line 34 | case_catalog wiring / broken notes.md ref | sub / side | HIGH |
| 5 | harmony_layer.md 3-9 | the 3-Pass method location | core | HIGH |
| 6 | 06-37 finding | ~3,500 band / snap-to-structure | core | HIGH |
| 7 | 00-24 finding | 3-Pass un-wired root cause; meaning-lock-config-blind fix | core | HIGH |
| 8 | 01-09 finding | config-independent post-draft checks | core | HIGH |
| 9 | 04-48 finding | budget-gated-always-on; prose=weak-nudge | core | HIGH |
| 10 | 04-12 finding | enforcement gradient | sub | HIGH |
| 11 | schemas.py PipelineConfig | chunking fields defined but not wired into SKILL.md workflow | side | MED |

## State Summary

- **Coverage map:** SKILL.md chunking = confirmed; SKILL.md Step 5 = confirmed; verification-pass region = confirmed-absent; the 6 findings = confirmed. No large unexplored region.
- **Concept-names:** meaning-lock-config-blind (00-24); back-bracket / whole-draft check (01-09/04-48); enforcement gradient (04-12); band-not-cliff / demonstrated-safe-4,345 (06-37); collapse-in-one-motion (23-03); method-vs-policy separability (00-24).
- **The headline the model measured:** the edit is **clearly BETTER than the pre-edit SKILL.md** (chunking added, one-motion softened, case_catalog + harmony referenced as steps) but only **PARTIALLY covers the inquiry recommendations** — three real shortfalls: (a) config leads instead of a config-blind Meaning-Lock (00-24 crux), (b) no whole-draft verification pass (01-09/back-bracket), (c) the chunk number is set *above* the conservative safe point (06-37).

## Frontier (open for downstream)

- **FF1 (the crux):** is Step 5.1's "map meaning **and** config together" a genuine regression against 00-24's config-blind-Meaning-Lock, or an acceptable in-one-file compromise? The 4-layer "dont concrete" defers finalization but never produces a config-blind locked-meaning foundation. (Sensemaking must adjudicate.)
- **FF2:** is 5000 (vs 3,500) a deliberate user override (the user set it; may have a reason / a different working corpus) or an oversight? The user edited this themselves — the number may reflect their own judgment, not a mistake.
- **FF3 (baseline):** better-or-worse is baseline-relative — span all three (vs pre-edit = better; vs recommendations = partial; vs ideal = the gap-list of DF4/DF5/DF2).
- **FF4:** the "dont concrete until the end" 4-layer ordering is itself a *prose-instruction* attempt at staging — per the enforcement gradient (04-12) it is a weak nudge; does it actually produce meaning-first behavior, or just narrate it in one motion (the very failure 00-24 named)?

## Telemetry

- Mode artifact / signal-first · cycles 3 · items enumerated 11 · tags: core 7, sub 3, side 1.
- Failure modes checked: missed-relevance (no — spanned SKILL.md + all 6 priors + refs), surfaced-irrelevance (no), territory-mis-binding (no), recency-bias (n/a — content-driven).
- items_with_mtime: 11 / items_without_mtime: 0.
- **Self-assessment: PROCEED** — the empirical anchor is measured and complete; the crux (DF4 config-first vs meaning-first-config-blind) and the missing verification pass (DF5) are the load-bearing facts for sensemaking. FLAG-worthy nuance carried to Warm: FF2 (the user set 5000 themselves — the "worse-on-the-number" reading must be held as *less-conservative-than-recommended*, not *mistake*, absent knowing their intent).
