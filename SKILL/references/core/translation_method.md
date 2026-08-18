# Translation Method — How the Whole Translation Runs

This file is the **governing method** for a comprehenslate translation: the ordered passes every translation runs through, from first reading the source to delivering the finished target text. It is meant to be the spine of `SKILL.md`'s translate step.

Keep this separate from the layers it draws on. The **method** (this file) is *how the translation runs*. The **harmony layer** (`harmony_layer.md`), the **config calibration** (`config_base_source.md`), the **policies** (`policy_config_base_source.md`), and the **case catalog** (`case_catalog.md`) are *things individual passes consult* — they are not the method itself.

---

## The core principle: comprehend before you style

Meaning is settled **first**, in its own pass, before any reader-facing style choice is in view. Style can distort *comprehension* when the two are decided together — so they are kept apart: understand what the source actually says, lock it, and only then decide how to render it for this reader.

---

## The passes

### Pass 1 — Meaning Lock (config-blind)

Render each sentence with strict semantic fidelity — **without the `TranslationConfig` in view**. No meaning added, removed, or altered. This produces the "accurate but choppy" version. It is the foundation that cannot be violated.

Run it config-blind on purpose: if the reader-style settings (`reader_level`, `source_fidelity`, register, etc.) are visible here, they bias what you *understand* the source to mean — you round a precise word to an easier sense because the reader is "basic," or you flatten an ornate structure that was actually carrying meaning. Comprehension must be settled from the source's own construction alone.

- **Sentence-level.** Sentence boundaries are structural meaning; do not merge or split.
- **Resolve word-sense from the local construction** (the genitive, the plausibility of the reading), not from the surrounding metaphor's momentum and not from a config-driven preference.
- The output of this pass is a locked meaning, not a finished translation. Do not concrete anything yet.

### Pass 2 — Harmony Map

Analyze the source's inter-sentence relationships and classify each connection — phonetic echo between sentence endings, grammatical parallelism, shared-root cohesion, chiastic (mirror) structure, escalation/de-escalation rhythm, contrast pairing, implied question-answer flow. This produces the "harmony blueprint."

This pass consults `harmony_layer.md` — the cohesion taxonomy and the Tier 1–4 preservation policy (which relationships must be preserved, which are sacrificeable, and under what conditions).

### Pass 3 — Target Reconstruction

Now — and only now — bring in the reader-facing choices and reconstruct in the target language, on top of the locked meaning:

- the **`TranslationConfig`** (per `config_base_source.md`): which words and registers are usable for this reader;
- the **policies** (per `policy_config_base_source.md`), if the user requested them;
- the **case catalog** (`case_catalog.md`): if the source resembles any niche meaning-carrying pattern, handle it with extra care;
- the **harmony blueprint** from Pass 2: recreate equivalent relationships using the target language's own native cohesion devices.

You may change *how* a meaning is expressed, but never *what* meaning is expressed. This is the pass that concretes the translation.

### Pass 4 — Whole-draft Verification (config-independent)

After the full draft is assembled, re-read the whole translation against the source and run the always-run checks, regardless of config:

- Was any source content dropped?
- Was anything invented or added?
- Were sentence boundaries preserved?
- Did the large-scale structure survive?

Fix any failure before delivering. These are the config-*independent* checks. Reader-keyed checks — is this word too hard *for this reader*? is the register right for the purpose? — ride Pass 3's config and are not repeated here.

---

## Hard constraints (hold across all passes)

- Anything that changes semantic content is forbidden.
- Adding information not present in the original is forbidden.
- Removing information present in the original is forbidden.
- Merging two sentences into one is forbidden (sentence boundaries are structural meaning).
- Splitting one sentence into two is forbidden, for the same reason.
- Changing the logical relationship between sentences (cause→effect becoming effect→cause) is forbidden.

## What is permitted (in Pass 3 only)

- Choosing between synonyms to create phonetic harmony in the target language.
- Adjusting word order within a sentence where the target grammar allows multiple valid orders.
- Using the target language's natural transitional devices (provided they add no meaning).
- Matching sentence-length ratios, and preserving parallelism where the original echoed itself.

---

## Chunking

Long sources are processed in model-sized chunks (per `SKILL.md`'s chunking rules), because a model's attention to detail degrades when it does too much at once. The passes run **bracketed by whole-text work**:

- **Front bracket (whole source):** Pass 1 comprehension + a first Pass 2 harmony read over the entire source, so per-chunk work is done against the whole document's meaning and structure.
- **Middle (per chunk):** Pass 1 → Pass 2 → Pass 3 on each chunk, snapping chunk edges to sentence/paragraph boundaries.
- **Back bracket (whole draft):** Pass 4 verification over the reassembled whole.

---

## Enforcement note (honest scope)

This file is a **method specification the model reads.** On its own, an instruction to "run these passes in order" is a strong nudge but not a guarantee — a model can still collapse the passes into one forward motion. The passes are *physically* enforced only when the engine runs them as **separate calls** (a config-blind meaning-lock call whose output feeds a reconstruction call, plus per-chunk calls and a verification call). Until that engine layer exists, this method is the strongest prose form of the intended process, and the ordered/named passes here raise adherence well above a flat "apply everything at once" instruction.
