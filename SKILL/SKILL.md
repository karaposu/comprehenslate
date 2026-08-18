---
name: comprehenslate
description: AI-assisted translation of any source document into a target language. Invoke when the user asks to translate a document.
---

# Comprehenslate — Translation Skill

Comprehenslate is a general-purpose translation skill: it produces an AI-assisted translation of any source document into a target language, parameterized by a structured `TranslationConfig`. It is currently calibrated against theological / layered religious-philosophical prose (especially Said Nursi's *Risale-i Nur*) as its initial corpus, but is designed for any document — treat the calibration corpus as a tuning anchor, not the product's scope.

The translation output is always **Markdown**.

---

## Workflow

When the user asks to translate something, run the steps below in order. Do not skip steps; do not run them out of order.

### Step 1 — Ask for the source document

Ask the user to point to the source document by path. Accept any file path.

If the user has already pointed to a source in the same message, skip to Step 2.

### Step 2 — Load all reference files

Before doing anything else, read the following files in full:

- `SKILL/references/config/schemas.py` — the authoritative schemas (`TranslationConfig` + Policy classes + `PipelineConfig`).
- `SKILL/references/config/config_base_source.md` — the calibration context for the 8 `TranslationConfig` axes (per-level definitions; cross-cultural examples; cross-axis interactions; modulation tables).
- `SKILL/references/config/policy_config_base_source.md` — the calibration context for the Policy layer (per-edge-case enums for recurring authorial value judgments).
- `SKILL/references/core/translation_method.md` — **the governing translation method**: the ordered passes (config-blind Meaning-Lock → Harmony Map → Target Reconstruction → Verification) that Step 5 runs as its spine.
- `SKILL/references/core/case_catalog.md` — the project's catalog of translation cases (niche meaning-carrying patterns to watch for).
- `SKILL/references/core/advanced_principles.md` — advanced translation principles.
- `SKILL/references/core/harmony_layer.md` — the harmony-layer specification (cause-effect chains, istilzam chains, Tier 1-4 preservation policies).


Then read the source document the user pointed to in Step 1.

### Step 3 — Ask for the target language

Ask the user **which language** the translation should be produced in. Accept any natural-language target (English, Russian, German, Indonesian, etc.).

If the user has already specified a target language in the same message, skip to Step 4.

### Step 4 — Present `TranslationConfig` options and let the user choose

Show the user the 8 axes of `TranslationConfig` as a numbered list with their available values and **mark the default for each**. Let the user pick values for as many or as few axes as they want. **Any axis the user does not specify uses its default.**

Present the axes in this exact form:

> *I'll translate using these eight strategic axes. Pick values for any you want to set; the rest will use defaults.*

| # | Axis | Values | Default |
|---|---|---|---|
| A1 | `reader_level` | `very_basic` / `daily` / `conversational` / `advanced` / `native` | `conversational` |
| A2 | `domain_expertise` | `lay` / `aware` / `educated` / `trained` / `expert` | `aware` |
| A3 | `source_culture` | `outsider` / `acquainted` / `familiar` / `heritage` / `source-native` | `acquainted` |
| A4 | `purpose` | `scholarly` / `devotional` / `casual` / `language-learning` / `performance` | `casual` |
| A5 | `source_fidelity` | `foreignized-max` / `foreignized` / `balanced` / `lightly-domesticated` | `balanced` |
| A6 | `form_preservation` | `off` / `minimal` / `light` / `standard` / `maximum` | `standard` |
| A7 | `scaffolding` | `off` / `minimal` / `standard` / `rich` / `scholarly` | `minimal` |
| A8 | `analysis_depth` | `none` / `surface` / `standard` / `deep` / `scholarly` | `none` |

Also offer: *"If you want Policy-level choices too (how to handle embedded non-main-language quotes, author marginalia, archaic register, honorifics, formulaic openings, embedded poetry, voice marking) — say `with policies` and I'll present those."* Only present the Policy options if the user requests them; otherwise use the Policy defaults from `schemas.py`.

After the user replies, construct the `TranslationConfig` instance using the user's chosen values plus defaults for everything else. Echo the resolved config back to the user briefly (one line per non-default value; one summary line for "all other axes default") so the user can see what was committed.

### Step 5 — Tell the user output format, then translate

Before producing the translation, send one short line:

> *"Translation will be produced in Markdown format."*

Then produce the translation by running the four-pass method in `references/core/translation_method.md`, in order. Do not collapse the passes into one motion; do not concrete the translation until Pass 3.

1. **Pass 1 — Meaning Lock (config-blind).** Render each sentence with strict semantic fidelity **without the `TranslationConfig` in view** — nothing added, removed, or altered. This is the "accurate but choppy" foundation. Running it config-blind is deliberate: if the reader-style settings are visible here, they distort what you *understand* the source to mean. Do not concrete yet.

2. **Pass 2 — Harmony Map.** Analyze the source's inter-sentence relationships (phonetic echo, parallelism, chiasmus, escalation/de-escalation, contrast pairs, implied question-answer flow) — the "harmony blueprint." Consult `references/core/harmony_layer.md` for the Tier 1–4 preservation policy (which relationships must be preserved vs. are sacrificeable). Do not concrete yet.

3. **Pass 3 — Target Reconstruction.** Now — and only now — reconstruct in the target language on top of the locked meaning, applying: the user's `TranslationConfig` choices (per `config_base_source.md`), which decide what words/registers are usable for this reader; the Policy values (per `policy_config_base_source.md`) if `with policies` was requested; the niche cases in `references/core/case_catalog.md` (if the source resembles any, translate it with extra care); and the Pass-2 harmony blueprint. You may change *how* a meaning is expressed, never *what*. **You may concrete the translation now.**

4. **Pass 4 — Whole-draft Verification (config-independent).** After the full draft, re-read the whole translation against the source: was any content dropped? invented? were sentence boundaries preserved? did the large-scale structure survive? Fix any failure before delivering.

(The full method — the hard constraints, the config-blindness rationale, and the chunking front/middle/back bracket — is in `references/core/translation_method.md`.)


The output is Markdown. Use Markdown's footnote syntax for any policy value that calls for footnotes (`SourceApparatusPolicy.translate-as-footnote`; `NonMainLangPartsPolicy.preserve-original-and-add-translation-as-a-note`; etc.). Use blockquotes for embedded poetry under `EmbeddedPoetryPolicy.preserve-original-with-prose-gloss`. Use italics for voice-marking under `VoiceMarkingPolicy.implicit-typographic`.

---

## Rules

1. **Always read all reference files before translating.** The calibration documents (`config_base_source.md`, `policy_config_base_source.md`) are not optional context — they define what each TC value and each Policy value means in practice. Skipping them produces miscalibrated translations.

2. **Never skip Step 1 or Step 3.** Do not begin translating until you have both a source document path and a target language.

3. **Default-on-unchosen.** When the user picks values for only some axes, the rest use defaults from `schemas.py`. Do not ask the user about every axis individually — let them pick what matters to them and default the rest.

4. **Always output Markdown.** Even if the user does not specify, the output is Markdown (the `PipelineConfig.output_format` default is `"md"`).

5. **Tier 1-2 harmony-layer preservation is non-negotiable.** Regardless of the user's TC choices, the harmony-layer Tier 1 (cause-effect chains, istilzam chains, etc.) and Tier 2 (high-priority chains) are preserved per `references/core/harmony_layer.md`.

6. **Echo the resolved config.** After Step 4, briefly tell the user what TC values you committed to. This lets them catch a misunderstood preference before the translation starts.

7. **Chunking is NEccesary due to AI focus limit** 
     AI loses its attention to details and accurate translation when asked to do all at once for one long text This is why we need to process texts in chunks..
     For Claude Opus 4.8 use chunks of Max ~5000 character (if there is sentence ending or paragrapgh ending you can strecth this up or down of course, it is not strict rule but approximation )
     For Claude Sonet use Max ~2500
     For Fable 5, use max ~7000 char

8.  Make sure when You receive a source text inspect it in terms of lenght (chars,words) and based on model being used pring how many chunks will be used to the user. 