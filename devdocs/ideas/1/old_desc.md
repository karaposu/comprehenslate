# Three Data Structures, Not One

The translation memory looks like a single thing — "remember how we translated words" — but it's actually three distinct data structures with different shapes, sizes, lifecycles, and consumers.

---

## Key Distinction: Lemma vs. Root

Before diving into the structures, a critical design decision:

**Lemma** = the dictionary headword. The form you'd look up in a dictionary. This is the PRIMARY grouping key.
- Turkish: "kitaplar" (books) → lemma "kitap" (book). Same word, different inflection. GROUPED.
- Turkish: "kitaplık" (bookcase) → lemma "kitaplık". Different word, different meaning. NOT GROUPED with "kitap".
- Arabic: "يكتبون" (they write) → lemma "كتب" (to write). Same verb, different conjugation. GROUPED.
- Arabic: "كاتب" (writer) → lemma "كاتب". Different word. NOT GROUPED with "كتاب" (book).

**Root** = the derivational base. In Arabic, the trilateral consonant skeleton. In Turkish, the stem before derivational suffixes.
- Arabic: كتاب (book), كاتب (writer), مكتبة (library) all share root ك-ت-ب. Related but DIFFERENT words.
- Turkish: kitap, kitaplık, kitapçı all share base "kitap". Related but DIFFERENT words.

**Why this matters:** Grouping by root collapses "book" and "writer" and "library" into one memory entry. The LLM would see "this root was translated as 'book' before" when it's looking at "writer." Catastrophic for translation quality.

Grouping by lemma keeps them separate — each is its own dictionary entry with its own translation history. Inflected forms (plurals, conjugations, case markings) correctly merge into their headword.

**Root is stored but not used for grouping in v1.** It's collected for future Phase 1 indexing where root-family awareness is valuable. The `root` field is a cross-reference, not an identity key.

---

## Structure A: The Storage Layer

**What it is:** The complete, persistent record of every word encountered, every meaning it carried, every context it appeared in, and every translation decision made across the entire book.

**When it's written:** After each chunk is translated. New entries are added, existing entries gain new contexts.

**When it's read:** Between sessions (to resume translation), at the end of the book (to generate reports), and at the start of pass 2 (the full knowledge base).

**What it looks like:**

```python
class WordMeaning(BaseModel):
    id: str                    # "m1", "m2", etc.
    translation: str           # "God-consciousness"
    confidence: float          # 0.85
    chosen: bool               # was this the primary choice?

class WordEncounter(BaseModel):
    sentence_source: str       # full original sentence
    sentence_translation: str  # the primary translation of that sentence
    chapter: int
    sentence_num: int
    chosen_meaning: str        # which meaning id was used
    all_valid_meanings: list[WordMeaning]  # ALL meanings valid here, not just chosen

class WordEntry(BaseModel):
    lemma: str                 # dictionary headword: "كتاب" or "kitap"
    root: str | None           # derivational root: "ك-ت-ب" (stored, not used for grouping)
    surface_forms: set[str]    # all inflected forms seen: {"كتاب", "كتب", "الكتاب", ...}
    encounters: list[WordEncounter]

class TranslationMemory(BaseModel):
    entries: dict[str, WordEntry]       # keyed by lemma (dictionary headword)
    surface_to_lemma: dict[str, str]    # reverse index: surface form → lemma
    root_families: dict[str, list[str]] # root → [lemmas] cross-reference (stored, inactive in v1)
    proper_nouns: dict[str, str]        # strict glossary: "حسين" → "Husayn"
```

**Size:** Grows throughout translation. For a 300-page book: potentially thousands of entries, each with multiple encounters. Could be megabytes of JSON. This is fine — it lives on disk, not in a prompt.

**Key property:** It never loses information. Every encounter, every meaning, every decision is preserved. It's the source of truth that the other two structures are derived from.

**Lookup strategy (two-path, pre-LLM):**

1. Surface form exact match → `surface_to_lemma["يكتبون"]` → lemma "كتب" → entry found
2. No surface match → word is new. Sent to LLM without memory. LLM returns lemma in response. Stored for next time.

---

## Structure B: The Prompt Injection View

**What it is:** A compressed, filtered snapshot of Structure A, designed to fit inside an LLM prompt alongside the system prompt, source chunk, and instruction.

**When it's created:** Fresh for every chunk. Before translating chunk N, we scan chunk N's source text, find which words from the memory appear in it (via `surface_to_lemma` lookup), and build a compact summary of just those lemmas' translation history.

**When it's read:** By the LLM, once, during translation of that chunk. Then discarded.

**What it looks like:**

```python
class MemoryHint(BaseModel):
    lemma: str                    # dictionary headword: "كتاب"
    known_forms: list[str]        # surface forms seen before: ["كتاب", "كتب", "الكتاب"]
    previous_translations: list[PreviousTranslation]

class PreviousTranslation(BaseModel):
    translation: str              # "book"
    context_summary: str          # "physical object contexts (ch.1, ch.4, ch.7)"
    frequency: int                # how many times this meaning was used

class PromptMemory(BaseModel):
    hints: list[MemoryHint]
    proper_nouns: dict[str, str]  # always included, always enforced
```

**Size:** Proportional to the current chunk's vocabulary, NOT the book's total vocabulary. A chunk with 200 unique words might match 30-50 lemma entries in the memory. Each entry is compressed to ~50-100 tokens. Total: 1,500-5,000 tokens. Fits comfortably in any context window.

**What gets compressed vs. what gets dropped:**

| Storage has | Prompt injection gets |
|---|---|
| Full sentence for every encounter | Short context summary |
| Every encounter listed individually | Grouped by meaning, with frequency count |
| All valid meanings per encounter | Only meanings that were actually chosen + most common "also valid" |
| Chapter/sentence numbers | Collapsed to "ch.1, ch.4, ch.7" |
| Confidence scores | Dropped — the LLM doesn't need these |
| Lemmas not relevant to current chunk | Dropped entirely |
| Root cross-references | Dropped — not used in v1 |

**What it looks like rendered in a prompt:**

```
=== Translation Memory for This Section ===

كتاب [lemma] (forms seen: كتاب، كتب، الكتاب):
  - "book" — used 12 times (physical object contexts, ch.1-9)
  - "scripture" — used 3 times (religious text contexts, ch.2, ch.5, ch.8)

تقوى [lemma] (forms seen: تقوى، اتقوا، يتقون، المتقين):
  - "God-consciousness" — used 12 times (spiritual awareness contexts, ch.1-9)
  - "mindful restraint" — used 2 times (journey/provision contexts, ch.4, ch.6)

=== Proper Nouns (always use exactly) ===
حسين → Husayn
المدينة → Medina
```

**Key property:** It's lossy on purpose. The LLM doesn't need the full history — it needs enough to make consistent decisions. The compression is designed to fit in a prompt while preserving the information that actually affects translation quality.

---

## Structure C: The Sentence Output

**What it is:** The rich, per-sentence translation result that preserves all meanings, all alternative readings, and all word-level decisions.

**When it's created:** By the LLM, as the response to each translation call. This IS the structured output from `with_structured_output`.

**When it's read:** By the user (exploring alternative meanings), by the system (extracting new entries for Structure A), and by the output formatter (rendering the final book).

**What it looks like:**

```python
class RichWord(BaseModel):
    word: str                     # surface form as it appears in text
    lemma: str                    # dictionary headword (grouping key)
    root: str | None              # derivational root (stored for future use)
    position: int                 # position in sentence
    meanings: list[WordMeaning]   # all valid meanings with confidence

class AlternativeReading(BaseModel):
    combination: dict[str, str]   # {word: meaning_id} for each rich word
    translation: str              # the full sentence under this combination
    coherence: float              # how well these meanings work together

class TranslatedSentence(BaseModel):
    source: str                   # original sentence
    primary_translation: str      # best-fit translation
    rich_words: list[RichWord]    # words with multiple valid meanings
    alternative_readings: list[AlternativeReading]  # coherent combinations
    audience_notes: str | None    # why certain words were simplified/kept

class ChunkOutput(BaseModel):
    sentences: list[TranslatedSentence]
    chapter: int | None
    chunk_index: int
```

**Size:** Proportional to the chunk being translated, not the book. Rich, detailed, potentially large — but it's output, not input. No context window constraint.

**Key property:** This is what the user sees and what feeds back into Structure A. After each chunk is translated, we iterate over the `TranslatedSentence` results, extract each `RichWord` with its `lemma` and meanings, and upsert into the storage layer — adding the surface form to the lemma's `surface_forms` set and appending a new `WordEncounter`.

---

## How They Interact

```
                    ┌─────────────────────────┐
                    │   Structure A: Storage   │
                    │   (full, persistent,     │
                    │    keyed by lemma)        │
                    └─────┬──────────┬─────────┘
                          │          ▲
              filter by   │          │ extract lemma +
              lemma match │          │ meanings + surface forms
                          │          │
                          ▼          │
┌──────────────────────────┐    ┌──────────────────────────┐
│ Structure B: Prompt View │    │ Structure C: Sentence    │
│ (compressed, per-chunk,  │    │ Output (rich, per-chunk, │
│  grouped by lemma)       │    │  returned by LLM call)   │
└──────────┬───────────────┘    └──────────▲───────────────┘
           │                               │
           │         ┌──────────┐          │
           └────────▶│   LLM    │──────────┘
                     │   Call   │
                     └──────────┘
```

**The cycle for each chunk:**

1. **Read** Structure A from disk
2. **Scan** source chunk for tokens, look up each via `surface_to_lemma`
3. **Filter** Structure A → Structure B (only matched lemmas, compressed)
4. **Send** Structure B + system prompt + source chunk + instruction → LLM
5. **Receive** Structure C (rich sentence output with lemma + root per rich word)
6. **Extract** from Structure C: for each `RichWord`, upsert into Structure A:
   - Add surface form to lemma's `surface_forms`
   - Add root to `root_families` cross-reference
   - Append new `WordEncounter` with all meanings
7. **Save** Structure A to disk
8. **Save** Structure C as part of the book output

---

## Why This Separation Matters

**If you try to use one structure for everything:**

- Using Storage (A) as prompt injection → the prompt explodes. A 300-page book's memory won't fit in any context window.
- Using Prompt View (B) as storage → you lose information. The compressed view drops encounter details, confidence scores, and unchosen meanings. You can't reconstruct the full history from it.
- Using Sentence Output (C) as storage → it's per-sentence, not per-word. To find all occurrences of a lemma you'd have to scan every sentence output in the entire book. No indexing, no grouping, no efficient lookup.
- Using Storage (A) as output → the user sees a word-centric view, not a sentence-centric view. They want to read sentences and drill into word meanings, not browse a dictionary.

Each structure exists because its consumer has different needs:

| Structure | Consumer | Needs | Keyed by |
|---|---|---|---|
| A: Storage | The system between chunks | Complete, persistent, indexed | Lemma |
| B: Prompt View | The LLM during translation | Compact, relevant to current chunk | Lemma (filtered) |
| C: Sentence Output | The user reading the translation | Rich, sentence-centric, explorable | Sentence position |

Three views. One underlying reality. Separate models because separate constraints.
