# Translation Method (OLD / Alternative) — Config-First 4-Layer Approach

This is the **original** translation approach — the process currently written inline in `SKILL.md`'s Step 5. It is kept here as an **alternative** to `translation_method.md` (the config-blind, meaning-first 3-Pass method), so the two can be run against the same source and their end results **cross-checked**.

**The one-line difference:**
- **This method (old):** maps meaning **with the `TranslationConfig` in view from the first step** — config-first — through four ordered layers that defer finalization ("don't concrete until the end") but never lock meaning config-blind.
- **`translation_method.md` (new):** locks meaning **config-blind, first** (Pass 1), maps harmony (Pass 2), then applies config / policies / case-catalog / harmony in a reconstruction pass (Pass 3), plus a whole-draft verification (Pass 4) — meaning-first.

Both defer finalization; they differ on **whether comprehension happens before or alongside the reader-style config**. Use this file when you want to translate a source the old way and compare it against the new way.

---

## The method (verbatim from `SKILL.md` Step 5)

### Step 5 — Tell the user output format, then translate

Before producing the translation, send one short line:

> *"Translation will be produced in Markdown format."*

Then produce the translation by using these following instructions:

1. First of all,  The user's `TranslationConfig` choices (per `config_base_source.md` calibration). This matters a lot  because it effects what words are usable in the target language and which are not usable.  Start by use your understanding to map the given chunk text in target language with most accurate meaning and most loyality to given TranslationConfig selections.  But dont concrete the translation due to next instructions will ofc effect them too. 

2.  If `with policies` was requested default Policy values from `schemas.py` (or the user's overrides if `with policies` was requested; per `policy_config_base_source.md` calibration).  But dont concrete the translation due to next instructions will ofc effect them too. 

3. - Make sure during translation check case examples for niche situations from `references/core/case_catalog.md` . These are translation rule of thumbs for specific niche but important cases. If any souce material resembles any of these cases you should pay extra attention using translation.  But dont concrete the translation due to next instructions will ofc effect them too. 


4.  The last step is  The harmony-layer whcih effects if  Harmony Map should applied or not and how and which ones, More details are in  `references/core/harmony_layer.md`.   Since this was last modifying layer U can concrete the translation now. 
