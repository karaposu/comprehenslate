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
- `SKILL/references/core/translation_principals.md` — the project's translation principles.
- `SKILL/references/core/advanced_principles.md` — advanced translation principles.
- `SKILL/references/core/harmony_layer.md` — the harmony-layer specification (cause-effect chains, istilzam chains, Tier 1-4 preservation policies).
- `SKILL/references/core/notes.md` — project notes.

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

Then produce the translation. Apply:

- The user's `TranslationConfig` choices (per `config_base_source.md` calibration).
- Default Policy values from `schemas.py` (or the user's overrides if `with policies` was requested; per `policy_config_base_source.md` calibration).
- The translation principles from `references/core/translation_principals.md` and `references/core/advanced_principles.md`.
- The harmony-layer Tier 1-4 preservation policy from `references/core/harmony_layer.md` (Tier 1-2 are NON-NEGOTIABLE hard constraints regardless of other config choices).
- Any project notes from `references/core/notes.md`.

The output is Markdown. Use Markdown's footnote syntax for any policy value that calls for footnotes (`SourceApparatusPolicy.translate-as-footnote`; `NonMainLangPartsPolicy.preserve-original-and-add-translation-as-a-note`; etc.). Use blockquotes for embedded poetry under `EmbeddedPoetryPolicy.preserve-original-with-prose-gloss`. Use italics for voice-marking under `VoiceMarkingPolicy.implicit-typographic`.

---

## Rules

1. **Always read all reference files before translating.** The calibration documents (`config_base_source.md`, `policy_config_base_source.md`) are not optional context — they define what each TC value and each Policy value means in practice. Skipping them produces miscalibrated translations.

2. **Never skip Step 1 or Step 3.** Do not begin translating until you have both a source document path and a target language.

3. **Default-on-unchosen.** When the user picks values for only some axes, the rest use defaults from `schemas.py`. Do not ask the user about every axis individually — let them pick what matters to them and default the rest.

4. **Always output Markdown.** Even if the user does not specify, the output is Markdown (the `PipelineConfig.output_format` default is `"md"`).

5. **Tier 1-2 harmony-layer preservation is non-negotiable.** Regardless of the user's TC choices, the harmony-layer Tier 1 (cause-effect chains, istilzam chains, etc.) and Tier 2 (high-priority chains) are preserved per `references/core/harmony_layer.md`.

6. **Echo the resolved config.** After Step 4, briefly tell the user what TC values you committed to. This lets them catch a misunderstood preference before the translation starts.
