# Comprehenslate

**A highly configurable, long-context translation skill that preserves the layered meaning ordinary translation flattens.**

Comprehenslate translates any source document into any target language, parameterized by a structured `TranslationConfig`. It is calibrated against dense, layered religious-philosophical prose (Said Nursi's *Risale-i Nur*) as a tuning anchor — but it is general-purpose, not scoped to that corpus.

---

## The gap it fills

Machine translation and quick human translation optimize for fluent, dictionary-level equivalence — and in doing so they **flatten everything that isn't the literal words**: register, word order, rhetorical form, deliberate omissions, culture-bound terms, and meaning encoded in several layers at once. Comprehenslate is built for texts where those layers *are* the content (scripture, philosophy, poetry, law, literary prose). Two things make it different:

- **Configurable, not one-size.** A single `TranslationConfig` (8 strategic axes) plus an opt-in Policy layer (7 policies) tunes the translation to a specific reader, purpose, and fidelity — the same source can be rendered as a scholarly edition or a casual read from the same skill.
- **Long-context aware.** Long sources are processed in model-sized chunks so quality doesn't degrade as length grows, and two dedicated safeguards protect meaning: a **139-case catalog** of niche meaning-carrying patterns (`SKILL/references/core/case_catalog.md`) and a **harmony layer** that enforces structural preservation (`SKILL/references/core/harmony_layer.md`).

---

## How it works

1. Point to a **source document** and a **target language**.
2. Choose `TranslationConfig` values — or accept the defaults (any axis you don't set uses its default).
3. The translation is built through **four ordered layers**, each refining the previous one:
   1. **Config mapping** — the TC choices decide which target-language words and registers are usable.
   2. **Policies** *(opt-in)* — how to handle embedded quotes, author marginalia, honorifics, archaic register, etc.
   3. **Case catalog** — 139 niche patterns to detect and preserve when the source resembles one.
   4. **Harmony layer** — a final pass enforcing Tier 1–4 structural preservation (Tier 1–2 are non-negotiable regardless of config).
4. Output is **Markdown** by default.

---

## Configuration

### `TranslationConfig` — the 8 strategic axes (user-facing)

These are the knobs the user sets. Each is independent; unset axes use their default.

| # | Axis | What it controls | Values (default in **bold**) |
|---|------|------------------|------------------------------|
| 1 | `reader_level` | Target reader's **language proficiency** — how simple or advanced the target vocabulary and syntax should be. | `very_basic` / `daily` / **`conversational`** / `advanced` / `native` |
| 2 | `domain_expertise` | Reader's **subject-matter knowledge** — how much technical/domain terminology can stand unexplained. | `lay` / **`aware`** / `educated` / `trained` / `expert` |
| 3 | `source_culture` | Reader's **familiarity with the source culture** — how much culturally-specific material can be left un-glossed. | `outsider` / **`acquainted`** / `familiar` / `heritage` / `source-native` |
| 4 | `purpose` | **Why the translation exists** — shapes the whole methodology. | `scholarly` / `devotional` / **`casual`** / `language-learning` / `performance` |
| 5 | `source_fidelity` | **Foreign texture vs. domestication** — keep the source's strangeness, or render it as fluent target idiom. | `foreignized-max` / `foreignized` / **`balanced`** / `lightly-domesticated` |
| 6 | `form_preservation` | How much of the **source's form and structure** to carry across. | `off` / `minimal` / `light` / **`standard`** / `maximum` |
| 7 | `scaffolding` | How much **reader-helping apparatus** (intros, bridges, notes) to add around the translation. | `off` / **`minimal`** / `standard` / `rich` / `scholarly` |
| 8 | `analysis_depth` | How much **interpretive analysis/commentary** to include alongside the translation. | **`none`** / `surface` / `standard` / `deep` / `scholarly` |

The precise per-level meaning of each value (with cross-cultural examples and cross-axis interactions) lives in `SKILL/references/config/config_base_source.md`.

### Policy layer — 7 opt-in policies

Recurring authorial-value judgments. Presented only if the user asks for them (`with policies`); otherwise the defaults below apply. Full calibration in `SKILL/references/config/policy_config_base_source.md`.

| Policy | What it decides | Default |
|--------|-----------------|---------|
| `NonMainLangPartsPolicy` | Quotes/mentions/references in a **non-main language** | `preserve-original-and-add-translation-as-a-note` |
| `SourceApparatusPolicy` | The source's **pre-existing apparatus** (author marginalia, glosses) | `translate-as-footnote` |
| `VoiceMarkingPolicy` | Marking transitions between **author voice** and cited authorities/added voices | `as-in-original` |
| `ArchaicRegisterPolicy` | Rendering **archaic source-language register** | `hybrid-by-register-domain` |
| `HonorificsPolicy` | Deferential/relational **honorifics** attached to names | `transliterate-with-original` |
| `FormulaicOpeningPolicy` | **Formulaic openings** (invocations, dedications, ritual/legal preambles) | `preserve-original-with-translation` |
| `EmbeddedPoetryPolicy` | **Embedded poetry** within prose | `preserve-original-with-prose-gloss` |

### `PipelineConfig` — runtime engine knobs (not translation strategy)

How the pipeline runs, independent of *what* the translation should read like.

| Knob | What it does | Default |
|------|--------------|---------|
| `chunking_budget` | Target chunk size for long-context splitting (source characters). | `None` (engine default) |
| `chunking_granularity` | Structural unit a chunk snaps to: `sentence` … `chapter`. | `None` |
| `chunking_mechanism_override` | How chunks are cut: `structural` / `harmony-tier-aware` / `fixed-budget-with-snap` / `hybrid` / … | `None` |
| `parallel_mode` | `off` (sequential, best consistency) / `intra-chapter` / `full` (fastest, risks terminology drift). | `off` |
| `parallel_batch_size` | Max concurrent model calls when parallel. | `None` |
| `output_format` | `md` / `html` / `plain` / `json`. | `md` |

---

## Chunking (long-context handling)

Models lose attention to detail when asked to translate a long text all at once, so the source is split into model-sized chunks (stretched to the nearest sentence/paragraph boundary). Approximate budgets per model:

| Model | Approx. chunk size |
|-------|--------------------|
| Claude Opus 4.8 | ~5,000 characters |
| Claude Sonnet | ~2,500 characters |
| Fable 5 | ~7,000 characters |

Before translating, the skill reports how many chunks a given source will take.

---

## Roadmap

**1. Second pass — whole-text consistency & harmony.**
Today the source is translated chunk by chunk. A planned second pass will run over the *finished* draft to unify terminology, register, and the harmony layer **across the entire document**, so consistency holds end-to-end rather than only within a single chunk.

**2. Next — per-word contextual sense (semantics from usage, not the dictionary).**
A later version will let **each word earn a fine-tuned meaning derived from how it is actually used** — its purpose and semantics in the surrounding source text — and translate from *that* derived sense, instead of a flat, context-less dictionary equivalent. The unit of fidelity moves from "the dictionary gloss of the word" to "what this word means *here*."

---

## Repository layout

```
SKILL/
  SKILL.md                              # the skill's workflow + rules
  references/
    config/
      schemas.py                        # TranslationConfig + Policy classes + PipelineConfig
      config_base_source.md             # calibration for the 8 TC axes
      policy_config_base_source.md       # calibration for the Policy layer
    core/
      case_catalog.md                   # 139 niche meaning-carrying cases
      advanced_principles.md            # advanced translation principles
      harmony_layer.md                  # Tier 1–4 structural preservation spec
```
