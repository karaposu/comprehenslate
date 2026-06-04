# Comprehenslate — Version Roadmap

Each version is a working, usable module. Each builds on the previous. No version is throwaway — each adds a real capability.

---

## v0.1 — Basic Translation

The simplest thing that works. One paragraph in, one translation out.

**What it does:**
- Takes a paragraph of source text + target language
- Uses the system prompt (translation principles distilled from `notes.md`)
- Returns a `TranslatedSentence` with primary translation
- Audience level (native / late_learner / late_learner_simple) is respected
- Config loaded from `.env`

**What it does NOT do:**
- No multi-meaning / rich words (single best translation only)
- No comprehension stage
- No chunking (length-limited to what fits in one LLM call)
- No memory across calls

**What we build:**
- `prompts/system_prompt.py` — distilled translation philosophy
- `prompts/translate_instruction.py` — builds per-request instruction from config
- `llm.py` — `ComprehenslateLLM` class with `translate()` method, LangChain `with_structured_output`
- Simplified `TranslatedSentence` response model (no rich words yet)

**What already exists:** `config.py`, `models.py`, `memory.py` (unused at this version)

**Milestone:** `pip install comprehenslate` → translate a paragraph with audience-level control.

---

## v0.2 — Chunked Translation

Now we can handle long text. A chapter, an article, a full document.

**What it adds:**
- Semantic chunking — split by paragraph, section, or approximate page length
- Overlap between chunks to avoid cutting mid-sentence
- Sequential chunk processing — translate chunk by chunk
- Output is a list of `ChunkOutput` that can be concatenated

**What it does NOT do:**
- No memory/consistency between chunks (each chunk is independent)
- No comprehension stage
- No rich words yet

**What we build:**
- `chunking.py` — text splitter with semantic boundaries and configurable overlap
- Loop in `llm.py` that processes chunks sequentially

**Milestone:** Translate a 20-page document end-to-end.

---

## v0.3 — Rich Words & Multi-Meaning

Single chunks now return the full multi-meaning output.

**What it adds:**
- Full `RichWord` output — words with multiple valid meanings, each with confidence
- `AlternativeReading` — coherent sentence-level readings from combining different word meanings
- The LLM identifies which words are "rich" (carry multiple valid meanings in context)
- Audience notes explain why words were simplified or kept

**What it does NOT do:**
- No cross-chunk consistency yet
- No comprehension stage

**What we build:**
- Full `TranslatedSentence` response model (rich words + alternatives)
- Updated translation instruction prompt that asks for multi-meaning analysis
- Updated system prompt with word-choice analysis principles

**Milestone:** Translate a paragraph and see 3-5 alternative sentence readings with different word-meaning combinations.

---

## v0.4 — Comprehension Index (Incremental)

Cross-chunk consistency arrives. The Comprehension Index builds incrementally during translation.

**What it adds:**
- `TranslationMemory` (Comprehension Index) activates — builds chunk by chunk
- Lemma-based grouping with surface form → lemma reverse index
- Root stored as cross-reference
- Prompt View — compressed index injected into each chunk's LLM prompt
- Consistency: the LLM sees how words were translated in previous chunks
- Proper nouns glossary — strict enforcement
- Index saved to disk between chunks (resumable)

**What it does NOT do:**
- No separate comprehension stage — index builds during translation (incremental mode)
- No ambiguity detection pipeline

**What we build:**
- Activate `memory.py` (already built) — `ingest_chunk()`, `build_prompt_memory()`, `save()`/`load()`
- Connect memory to translation loop — inject Prompt View into each chunk's instruction
- Proper noun management

**Milestone:** Translate a 50-page book. Word X is translated consistently across all chapters. The index is saved as a reviewable JSON artifact.

---

## v0.5 — Comprehension Stage (Two-Stage Separation)

The founding vision implemented. Comprehend first, translate second.

**What it adds:**
- Stage 1: Comprehension pipeline — analyze entire text chunk by chunk BEFORE translation
  - Pre-step: meaning space lookup (index + optional lexicon + LLM knowledge)
  - Call 1: extract words (lemma, root, meanings described NOT translated) + detect ambiguities at 3 levels
  - Call 2: resolve ambiguities using previous context (immediate + generic + dynamic lookup)
- Stage 2: Translation — translate with the complete Comprehension Index from the start
- Every chapter has full-book awareness — no "early chapters are blind" problem
- Comprehension Index is a first-class artifact — reviewable, editable between stages
- `ComprehensionResult` with `AnalyzedWord` and `AmbiguityResolution` output

**What it does NOT do:**
- No human-in-the-loop editing of the index (the artifact is there but no UI/tooling)
- No attached lexicons yet
- No parallel processing

**What we build:**
- `comprehend.py` — the two-call comprehension pipeline per chunk
- `prompts/comprehend_instruction.py` — comprehension prompt (analyze, don't translate)
- Comprehension models in `models.py` (already built: `ComprehensionResult`, `AnalyzedWord`, `MeaningCandidate`)
- Ambiguity models: `Ambiguity`, `Interpretation`, `AmbiguityResolution`
- `ComprehenslateLLM.comprehend()` method alongside `translate()`
- Context builder: immediate context (recent pages) + generic context (compressed index) + dynamic lookup (root families)

**Milestone:** Comprehend a book → inspect the index → translate with full awareness. "Comprehend once, translate many" — same index used for English and Turkish translations.

---

## v0.6 — Context Sources & Lexicon Attachment

The system can be fed external knowledge to sharpen comprehension.

**What it adds:**
- Attachable context sources: lexicon, companion text, historical record, commentary
- Lexicon feeds into meaning space lookup (pre-step of comprehension)
- Context sources improve ambiguity resolution at deeper layers
- Configurable: which sources are attached, how they're weighted

**What we build:**
- `context_sources.py` — ingestion and indexing of attached materials
- Integration with comprehension pipeline — context sources feed into meaning space and resolution
- Source type tagging (lexicon, companion, historical, commentary, cultural corpus, authorial context)

**Milestone:** Comprehend a classical Arabic text with an attached classical dictionary. Meaning space is richer. Ambiguity resolution is more accurate.

---

## v0.7 — Output Formatting

The translated book is a readable artifact, not a JSON dump.

**What it adds:**
- Markdown output — clean, readable, with optional annotations
- Rich word annotations — expandable footnotes showing alternative meanings
- Consistency report — every word that was translated differently across the book, with contexts
- Side-by-side view (source + translation)

**What we build:**
- `output/markdown.py` — render `ChunkOutput` list into a formatted markdown document
- `output/report.py` — generate consistency report from the Comprehension Index
- Annotation rendering for rich words and alternative readings

**Milestone:** Translate a book → get a `.md` file you can read straight through, with footnotes for rich words.

---

## v0.8 — Parallel Processing

Speed. Long books don't have to be sequential.

**What it adds:**
- Chapter-threaded parallel processing — each chapter comprehended/translated in parallel
- Context sharing between parallel workers (shared Comprehension Index with locking)
- Naive parallel mode — split arbitrarily, merge results
- Configurable via `parallel_mode` in config

**What we build:**
- `parallel.py` — parallel chunk orchestration with shared index
- Merge logic for combining parallel chunk outputs into final book
- Context consistency across parallel workers

**Milestone:** A 300-page book comprehended and translated in parallel. Linear speedup.

---

## v0.9 — Harmony Layer

Preserving how the text feels, not just what it says.

**What it adds:**
- 3-pass harmony preservation (toggleable):
  - Pass 1: Meaning Lock — strict semantic fidelity
  - Pass 2: Harmony Map — analyze inter-sentence relationships in the original
  - Pass 3: Target Language Reconstruction — adjust translation to recreate equivalent harmony
- 4-tier harmony priority system (from `harmony_layer.md`)
- Harmony report — which relationships were preserved, which were sacrificed, why

**What we build:**
- `harmony.py` — the 3-pass system
- Harmony map data model — inter-sentence relationship classification
- Harmony report generator
- Integration with translation pipeline (runs after base translation)

**Milestone:** Translate a passage of classical text. The output reads naturally in the target language while preserving the argument structure, emotional arc, and contrast pairings of the original.

---

## v1.0 — Full Comprehenslate

Everything from the original spec, working together.

**What it adds:**
- PDF output + original format preservation
- Human-in-the-loop: edit the Comprehension Index between stages via export/import
- Custom depth profiles
- Poetic translation mode
- Quoted content handling (leave / translate / translate+preserve)
- Pre-built context bundles for common use cases
- API surface polished for external use

**Milestone:** The complete vision. Comprehend first. Translate second. Every feature from `how_config_should_be.md` operational.

---

## Summary

| Version | Key Capability | Depends On |
|---|---|---|
| v0.1 | Basic paragraph translation with audience level | — |
| v0.2 | Long document chunking | v0.1 |
| v0.3 | Rich words & multi-meaning per sentence | v0.1 |
| v0.4 | Comprehension Index (incremental, cross-chunk consistency) | v0.2 + v0.3 |
| v0.5 | Two-stage separation (comprehend then translate) | v0.4 |
| v0.6 | Attachable context sources & lexicons | v0.5 |
| v0.7 | Markdown output & consistency reports | v0.4 |
| v0.8 | Parallel processing | v0.5 |
| v0.9 | Harmony preservation layer | v0.5 |
| v1.0 | Full spec: PDF, human-in-the-loop, poetic mode, all config | v0.7 + v0.8 + v0.9 |
