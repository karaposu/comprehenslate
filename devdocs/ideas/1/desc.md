# Four Data Structures Across Two Stages

Comprehenslate operates in two completely separate stages: **Comprehend**, then **Translate**. Each stage has its own LLM calls, its own prompts, its own output models. The comprehension stage produces a standalone artifact — the **Comprehension Index** — which the translation stage consumes.

Four data structures serve these two stages:

| Structure | Stage | Role |
|---|---|---|
| **A: Comprehension Index** | Produced by Stage 1, consumed by Stage 2 | The book's complete word-meaning map — a first-class, reviewable artifact |
| **B: Prompt Injection View** | Used within Stage 2 | Compressed, filtered snapshot of A for each translation chunk |
| **C: Translation Output** | Produced by Stage 2 | Rich per-sentence translations with multi-meaning preservation |
| **D: Comprehension Output** | Produced by Stage 1 | Per-chunk word analysis that feeds into A |

---

## The Two Stages

```
STAGE 1: COMPREHEND (analyze chunk by chunk → build index)

  Chunk 1 → LLM(analyze) → ComprehensionResult (D) → Index grows
  Chunk 2 → LLM(analyze) → ComprehensionResult (D) → Index grows
  ...
  Chunk N → LLM(analyze) → ComprehensionResult (D) → Index complete

  Output: Comprehension Index (A) — saved to disk as a standalone artifact
  ─────────────────────────────────────────────────────────────────────

STAGE 2: TRANSLATE (translate chunk by chunk, reading the complete index)

  Index (A) + Chunk 1 → filter → Prompt View (B) → LLM(translate) → ChunkOutput (C)
  Index (A) + Chunk 2 → filter → Prompt View (B) → LLM(translate) → ChunkOutput (C)
  ...
  Index (A) + Chunk N → filter → Prompt View (B) → LLM(translate) → ChunkOutput (C)

  Output: Translated book (collection of C)
```

The stages are completely decoupled. Stage 1 does NOT translate. Stage 2 does NOT analyze. The Comprehension Index is the bridge between them.

---

## Key Distinction: Lemma vs. Root

**Lemma** = the dictionary headword. The form you'd look up in a dictionary. This is the PRIMARY grouping key.
- Turkish: "kitaplar" (books) → lemma "kitap" (book). Same word, different inflection. GROUPED.
- Turkish: "kitaplık" (bookcase) → lemma "kitaplık". Different word, different meaning. NOT GROUPED with "kitap".
- Arabic: "يكتبون" (they write) → lemma "كتب" (to write). Same verb, different conjugation. GROUPED.
- Arabic: "كاتب" (writer) → lemma "كاتب". Different word. NOT GROUPED with "كتاب" (book).

**Root** = the derivational base. In Arabic, the trilateral consonant skeleton. In Turkish, the stem before derivational suffixes.
- Arabic: كتاب (book), كاتب (writer), مكتبة (library) all share root ك-ت-ب. Related but DIFFERENT words.
- Turkish: kitap, kitaplık, kitapçı all share base "kitap". Related but DIFFERENT words.

**Why this matters:** Grouping by root collapses "book" and "writer" and "library" into one index entry. Catastrophic for translation quality. Grouping by lemma keeps them separate.

**Root is stored as a cross-reference** for future root-family awareness, but is NOT the grouping key.

---

## Structure D: Comprehension Output (Stage 1 result)

**What it is:** The per-chunk analysis produced by the comprehension LLM call. It identifies every significant word, its lemma, root, and all valid meanings in context. It does NOT translate anything — meanings are described in source-language terms.

**When it's created:** By the LLM during Stage 1, one per chunk.

**When it's read:** Immediately after creation, to populate the Comprehension Index (A). Then stored as part of the analysis record.

**What it looks like:**

```python
class MeaningCandidate(BaseModel):
    id: str                    # "m1", "m2", etc.
    description: str           # meaning in source-language terms, NOT translated
    confidence: float          # how likely this meaning is in this context

class AnalyzedWord(BaseModel):
    word: str                  # surface form as it appears in text
    lemma: str                 # dictionary headword (grouping key)
    root: str | None           # derivational root
    position: int              # position in sentence
    meanings: list[MeaningCandidate]

class ComprehensionResult(BaseModel):
    source: str                # original sentence
    analyzed_words: list[AnalyzedWord]

class ComprehensionChunkOutput(BaseModel):
    sentences: list[ComprehensionResult]
    chapter: int | None
    chunk_index: int
```

**Key property:** No translations. The description field says "to set forth an example" or "to strike physically" — it describes meaning, it doesn't render it in a target language. This is language-pair-independent. The same index serves translation into ANY target language.

**Size:** Smaller than translation output per chunk. No alternative readings, no sentence-level translations, no audience notes. Just word-level analysis.

---

## Structure A: The Comprehension Index

**What it is:** The book's complete word-meaning map. A standalone, reviewable, editable artifact produced by Stage 1. Think of it as a dictionary built specifically for THIS book.

**When it's written:** During Stage 1 — grows chunk by chunk as comprehension results are ingested.

**When it's read:**
- By a human reviewer between Stage 1 and Stage 2 (to inspect, correct, lock entries)
- By Stage 2's prompt builder (to create the filtered prompt view for each translation chunk)
- Between sessions (to resume work)
- To translate the same book into another language (comprehend once, translate many)

**What it looks like:**

```python
class IndexedMeaning(BaseModel):
    id: str                    # "m1", "m2", etc.
    description: str           # meaning described (not translated)
    confidence: float          # how likely in context

class WordContext(BaseModel):
    sentence_source: str       # full original sentence where this word appeared
    chapter: int | None
    sentence_num: int
    meanings_in_context: list[IndexedMeaning]  # all valid meanings HERE

class WordEntry(BaseModel):
    lemma: str                 # dictionary headword: "كتاب" or "kitap"
    root: str | None           # derivational root: "ك-ت-ب"
    surface_forms: list[str]   # all inflected forms seen: ["كتاب", "كتب", "الكتاب"]
    contexts: list[WordContext]  # every sentence where this word appeared

class ComprehensionIndex(BaseModel):
    entries: dict[str, WordEntry]       # keyed by lemma
    surface_to_lemma: dict[str, str]    # reverse index: surface form → lemma
    root_families: dict[str, list[str]] # root → [lemmas] cross-reference
    proper_nouns: dict[str, str]        # strict glossary: "حسين" → "Husayn"
```

**Size:** Grows throughout Stage 1. For a 300-page book: potentially thousands of entries, each with multiple contexts. Could be megabytes of JSON. This is fine — it lives on disk.

**Key property:** It's a first-class artifact, not hidden plumbing. The user can:
- Open it and browse every word the system identified
- See every meaning each word carried in every context
- Correct wrong lemma assignments before translation
- Lock proper noun spellings
- Add meanings the LLM missed
- Share it with a scholar for review
- Reuse it to translate the same book into multiple languages

**Lookup strategy (two-path):**

1. Surface form exact match → `surface_to_lemma["يكتبون"]` → lemma "كتب" → entry found
2. No surface match → word wasn't identified during comprehension. Stage 2 handles it gracefully (translates without index support, flags for review).

---

## Structure B: The Prompt Injection View (Stage 2 input)

**What it is:** A compressed, filtered snapshot of the Comprehension Index (A), designed to fit inside an LLM prompt alongside the system prompt, source chunk, and translation instruction.

**When it's created:** Fresh for every translation chunk. Before translating chunk N, we scan chunk N's source text, find which words from the index appear in it, and build a compact summary.

**When it's read:** By the LLM, once, during translation of that chunk. Then discarded.

**What it looks like:**

```python
class MeaningSummary(BaseModel):
    description: str           # meaning described
    frequency: int             # how many times this meaning appeared across the book
    chapters: list[str]        # where it appeared: ["ch.1", "ch.4", "ch.7"]

class IndexHint(BaseModel):
    lemma: str                 # dictionary headword
    known_forms: list[str]     # surface forms: ["كتاب", "كتب", "الكتاب"]
    meanings: list[MeaningSummary]

class PromptIndex(BaseModel):
    hints: list[IndexHint]
    proper_nouns: dict[str, str]  # always included, always enforced
```

**Size:** Proportional to the current chunk's vocabulary, NOT the book's total vocabulary. Typically 1,500-5,000 tokens. Fits in any context window.

**What gets compressed vs. what gets dropped:**

| Index has | Prompt injection gets |
|---|---|
| Full sentence for every context | Dropped — meanings summarized without full sentences |
| Every context listed individually | Grouped by meaning, with frequency count |
| All meanings per context | Deduplicated across contexts |
| Chapter/sentence numbers | Collapsed to "ch.1, ch.4, ch.7" |
| Words not in current chunk | Dropped entirely |
| Root cross-references | Dropped |

**What it looks like rendered in a prompt:**

```
=== Comprehension Index for This Section ===

كتاب [lemma] (forms: كتاب، كتب، الكتاب):
  - "a physical book/volume" — 12 occurrences (ch.1-9)
  - "scripture/divine writing" — 3 occurrences (ch.2, ch.5, ch.8)

تقوى [lemma] (forms: تقوى، اتقوا، يتقون، المتقين):
  - "consciousness/awareness of God" — 12 occurrences (ch.1-9)
  - "self-restraint as provision" — 2 occurrences (ch.4, ch.6)

=== Proper Nouns (always use exactly) ===
حسين → Husayn
المدينة → Medina
```

**Key property:** It gives the LLM the book's full meaning landscape for the words in the current chunk — without the LLM having to discover these meanings itself. The comprehension work is already done.

---

## Structure C: The Translation Output (Stage 2 result)

**What it is:** The rich, per-sentence translation result that preserves all meanings, all alternative readings, and all word-level decisions.

**When it's created:** By the LLM during Stage 2, one per chunk.

**When it's read:** By the user (exploring alternative meanings) and by the output formatter (rendering the final book).

**What it looks like:**

```python
class WordMeaning(BaseModel):
    id: str                    # "m1", "m2", etc.
    translation: str           # the translated word/phrase for this meaning
    confidence: float          # how likely this meaning is in context
    chosen: bool               # whether selected for primary translation

class RichWord(BaseModel):
    word: str                  # surface form as it appears in text
    lemma: str                 # dictionary headword (grouping key)
    root: str | None           # derivational root
    position: int              # position in sentence
    meanings: list[WordMeaning]  # all valid meanings with translations

class AlternativeReading(BaseModel):
    combination: dict[str, str]  # {word: meaning_id} for each rich word
    translation: str             # full sentence under this combination
    coherence: float             # how well these meanings work together

class TranslatedSentence(BaseModel):
    source: str                # original sentence
    primary_translation: str   # best-fit translation
    rich_words: list[RichWord]
    alternative_readings: list[AlternativeReading]
    audience_notes: str | None

class ChunkOutput(BaseModel):
    sentences: list[TranslatedSentence]
    chapter: int | None
    chunk_index: int
```

**Key difference from Structure D:** Structure D (comprehension) describes meanings without translating them. Structure C (translation) renders those meanings into the target language and produces full sentence translations.

**Size:** Proportional to the chunk being translated. Rich, detailed, potentially large — but it's output, not input. No context window constraint.

---

## How They Interact

```
STAGE 1: COMPREHEND

  Source      ┌──────────┐     Structure D          Structure A
  Chunks ────▶│   LLM    │────▶ Comprehension  ────▶ Comprehension
              │ (analyze)│      Result               Index
              └──────────┘     (per chunk)           (grows on disk)
                                                         │
                                                         ▼
                                                   [SAVE TO DISK]
                                                   [Human review]
                                                   [Edit / correct]

  ─────────────────────────────────────────────────────────────────

STAGE 2: TRANSLATE

  Structure A                Structure B
  Comprehension    filter    Prompt
  Index ──────────────────▶  Index     ──┐
  (from disk)                (per chunk)  │
                                          │    ┌──────────┐     Structure C
  Source                                  ├───▶│   LLM    │────▶ Translation
  Chunks ─────────────────────────────────┘    │(translate)│      Output
                                               └──────────┘     (per chunk)
```

### Stage 1 cycle (per chunk):

1. **Send** source chunk + comprehension instruction → LLM
2. **Receive** ComprehensionResult (Structure D)
3. **Extract** from D: for each `AnalyzedWord`, upsert into A:
   - Create or find `WordEntry` by lemma
   - Add surface form to `surface_forms`
   - Add root to `root_families` cross-reference
   - Append `WordContext` with meanings
4. **Save** Structure A to disk
5. **Store** Structure D as part of the analysis record

### Between stages:

- Comprehension Index (A) is complete and saved to disk
- Human reviewer can inspect, edit, correct the index
- Index can be exported, shared, versioned
- Same index can serve translation into multiple target languages

### Stage 2 cycle (per chunk):

1. **Load** Structure A from disk
2. **Scan** source chunk for tokens, look up each via `surface_to_lemma`
3. **Filter** A → B (only matched lemmas, compressed)
4. **Send** B + system prompt + source chunk + translation instruction → LLM
5. **Receive** ChunkOutput (Structure C)
6. **Save** Structure C as part of the translated book

---

## Why Complete Separation Matters

### vs. single-pass incremental translation

| | Incremental (single pass) | Separated (comprehend → translate) |
|---|---|---|
| Chapter 1 knowledge | None — translates blind | Full book — index is complete |
| Consistency | Builds over time, early chapters drift | Uniform from the start |
| Need pass 2? | Yes, to fix blind early chapters | No — one pass is enough |
| Total LLM cost | 2 translation passes | 1 cheap comprehension + 1 translation |
| Reviewable artifact | No | Yes — index is inspectable between stages |
| Multi-language | Redo everything per language | Comprehend once, translate to any language |
| Human-in-the-loop | After translation only | Between stages — correct before translating |

### Why four structures, not fewer

- Using Index (A) as prompt injection → the prompt explodes. A 300-page book's index won't fit in any context window.
- Using Prompt View (B) as the index → you lose information. The compressed view drops contexts, confidence scores, and detailed meanings.
- Using Translation Output (C) as the index → it's per-sentence and target-language-specific. Can't reuse for another language.
- Using Comprehension Output (D) directly in translation → it's per-chunk raw analysis, not indexed by lemma. No grouping, no deduplication.

Each structure exists because its consumer has different needs:

| Structure | Stage | Consumer | Needs | Keyed by |
|---|---|---|---|---|
| D: Comprehension Output | 1 → A | Index builder | Raw per-chunk word analysis | Sentence position |
| A: Comprehension Index | 1 → 2 | Humans, prompt builder, future translations | Complete, persistent, reviewable | Lemma |
| B: Prompt Index | 2 | The LLM during translation | Compact, relevant to current chunk | Lemma (filtered) |
| C: Translation Output | 2 → user | The reader of the translation | Rich, sentence-centric, explorable | Sentence position |

Four views. Two stages. One underlying reality: the meaning of the source text.
