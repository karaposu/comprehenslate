# Comprehenslate Terminology

Canonical definitions for terms used across the project. If a design doc uses a term differently from this file, this file wins.

---

## Pipeline Stages

### Comprehension (Stage 1)
The process of analyzing source text to build understanding WITHOUT translating. Operates chunk by chunk. Produces the Comprehension Index. Contains three sub-steps: meaning space lookup → extract & detect → resolve with context.

**Not:** the general English word "comprehension." In Comprehenslate, a page is "comprehended" only when the 4-point criterion is met (see: Comprehended).

### Translation (Stage 2)
The process of rendering understood meanings into a target language. Operates chunk by chunk with the complete Comprehension Index available. Produces Translation Output.

**Not:** a synonym for the entire Comprehenslate pipeline. Translation is only Stage 2 — it cannot run without Stage 1 completing first (unless in fallback mode with `indexing_enabled=False`).

### Comprehended
A page is comprehended when:
1. All significant words have been analyzed (lemma, root, meanings)
2. All ambiguities have been detected (word, sentence, sense levels)
3. All ambiguities have been processed (resolved with interpretations OR flagged unresolvable)
4. The page's contribution is ready to merge into the Comprehension Index

"Comprehended" means "the space of valid readings has been mapped." Not "I know exactly what this means."

---

## Data Structures

### Comprehension Index
The book's complete word-meaning map. A standalone, persistent, reviewable artifact produced by Stage 1. Keyed by lemma. Contains every significant word, its surface forms, root, and every meaning it carried in every context across the book.

**Not:** a database index. Not a book's table of contents. Think of it as a dictionary built specifically for THIS book.

**Previously called:** translation memory, glossary, Structure A, meaning index. These names are retired.

**Code:** `TranslationMemory` class in `memory.py` (class name predates the rename — the concept is Comprehension Index).

### Prompt View
A compressed, filtered snapshot of the Comprehension Index, built fresh for each chunk. Contains only entries relevant to the current chunk's vocabulary. Designed to fit inside an LLM prompt.

**Not:** the full index. It's lossy on purpose — drops detailed contexts, confidence scores, and irrelevant entries to stay within context window limits.

**Previously called:** prompt injection view, prompt memory, PromptIndex, PromptMemory, Structure B. These names are retired.

**Code:** `PromptMemory` class in `memory.py`.

### Comprehension Output
The per-chunk analysis produced by Stage 1's LLM calls. Contains analyzed words (lemma, root, meanings described in source language) and ambiguity resolutions. Feeds into the Comprehension Index.

**Not:** a translation. Meanings are described, not translated. Language-pair-independent.

**Previously called:** Structure D, ComprehensionResult.

**Code:** `ComprehensionChunkOutput` / `ComprehensionResult` in `models.py`.

### Translation Output
The per-chunk translation produced by Stage 2's LLM calls. Contains translated sentences with rich words, alternative readings, and audience notes. This is what the reader sees.

**Not:** a raw translation. It's a structured, explorable result with multi-meaning preservation.

**Previously called:** sentence output, Structure C, ChunkOutput.

**Code:** `ChunkOutput` / `TranslatedSentence` in `models.py`.

---

## Linguistic Concepts

### Lemma
The dictionary headword of a word. The form you would look up in a dictionary. The PRIMARY grouping key for the Comprehension Index.

- "kitaplar" (books) → lemma "kitap"
- "يكتبون" (they write) → lemma "كتب"
- "kitaplık" (bookcase) → lemma "kitaplık" (NOT "kitap" — different word)

**Not:** the root. Lemma groups inflections (same word, different form). Root groups derivations (related but different words). See: Root.

### Root
The derivational base of a word. In Arabic, the trilateral consonant skeleton (e.g., ك-ت-ب). In Turkish, the stem before derivational suffixes.

Stored in the Comprehension Index as a cross-reference. NOT used as a grouping key — that's the lemma's job. Used during comprehension for dynamic context lookups ("show me all words from root family ك-ت-ب").

**Not:** the grouping key. Root-level grouping would collapse "book," "writer," and "library" into one entry.

### Surface Form
The exact spelling of a word as it appears in the source text. Multiple surface forms can map to the same lemma: "كتاب", "الكتاب", "كتب" all map to lemma "كتاب".

The Comprehension Index maintains a reverse index: surface form → lemma.

### Meaning
A word-level concept. One possible semantic value a word carries in a specific context. A word may have multiple valid meanings simultaneously.

In Stage 1 (comprehension): meanings are described in source-language terms (e.g., "to set forth an example"). See: MeaningCandidate.

In Stage 2 (translation): meanings are rendered in the target language (e.g., "set forth"). See: WordMeaning.

**Not:** an interpretation. Meanings are word-level. Interpretations are ambiguity-level. See: Interpretation.

### Rich Word
A word identified as carrying multiple valid meanings in a specific context. Not every word is rich — common particles, prepositions, and unambiguous nouns are not flagged as rich words. Only words where the context permits more than one valid reading.

Rich words are the unit of multi-meaning preservation. Each rich word in the Translation Output lists all valid meanings with confidence scores, and the reader can explore alternative sentence readings by switching between them.

### Meaning Space
The set of all known possible meanings of a word, assembled BEFORE the LLM analyzes a page. Built from three sources in priority order:

1. **Comprehension Index** — if this word appeared earlier in the book, its known meanings are already recorded
2. **Attached lexicon** — if the user provided a domain/era-specific dictionary
3. **LLM's built-in knowledge** — general fallback

The meaning space is fed to Call 1 of the comprehension pipeline so the LLM can detect ambiguities. The LLM cannot detect that a word is ambiguous unless it knows the word HAS other meanings.

**Not:** the final meaning analysis. The meaning space is input to comprehension. The actual meanings-in-context are the output.

---

## Comprehension Pipeline

### Extract & Detect (Call 1)
The first LLM call in the comprehension pipeline. Receives the source page + meaning space per word. Produces: analyzed words (lemma, root, meanings) and detected ambiguities at three levels. Does NOT receive previous book context — detection is unbiased.

### Resolve (Call 2)
The second LLM call in the comprehension pipeline. Receives the source page + Call 1's output + layered previous context. Resolves ambiguities by generating interpretations. Updates word meanings based on context.

### Ambiguity
Something unclear in the text. Detected at three levels:

- **Word-level:** a word has multiple valid dictionary meanings and the sentence doesn't fully disambiguate
- **Sentence-level:** the sentence structure allows multiple valid parses (who does what to whom, scope of modifiers)
- **Sense-level:** the overall meaning or purpose of a passage is unclear (literal vs. metaphorical, rhetorical intent)

### Interpretation
One possible reading of a detected ambiguity. An ambiguity may have multiple valid interpretations. Each interpretation has a confidence level and optional supporting context.

**Not:** a meaning. Meanings are word-level. Interpretations are ambiguity-level and may span word, sentence, or sense scope. An interpretation may involve multiple word meanings working together.

### Resolution (of an ambiguity)
The process of generating all valid interpretations for a detected ambiguity. Resolution does NOT mean "picking one answer." It means "enumerating the space of valid readings with confidence levels."

An ambiguity is "resolved" when all valid interpretations have been listed. An ambiguity is "unresolvable" when current context cannot narrow the readings — it's explicitly flagged with reasoning.

### Previous Context
Information from earlier pages used during Call 2 to resolve ambiguities. Three layers:

- **Immediate context:** last 5-10 pages of detailed Comprehension Output (recent analyses)
- **Generic context:** compressed whole-book Comprehension Index built so far (summary-level)
- **Dynamic lookup:** targeted queries against the index (e.g., "how has this root family been used?")

---

## Configuration

### Audience Level
Who the translation is for. Affects vocabulary and idiom usage in Stage 2.

- **Native:** idioms, rare words, domain-specific terms allowed
- **Late learner:** no idioms or rare words; standard vocabulary only
- **Late learner simple:** daily-use vocabulary only; simplest possible expression

### Depth Profile
How deeply the comprehension pipeline analyzes the text. Affects which layers of meaning extraction are active.

- **Surface:** word-level analysis only, primary meanings
- **Standard:** word + sentence-level analysis
- **Deep:** word + sentence + passage-level analysis
- **Scholarly:** all analysis layers active, maximum depth

### Indexing Enabled
Whether Stage 1 (comprehension) runs before Stage 2 (translation).

- **True (default):** full two-stage pipeline. Comprehend the entire text first, then translate with full index.
- **False (fallback):** single-pass translation with incremental memory building. Faster but lower quality — early chapters lack context.

---

## Arabic Rhetoric (Belagat)

These terms come from classical Arabic sciences of rhetoric. They inform the system prompt and the analysis Comprehenslate performs at deeper depth profiles. Not required for basic usage.

### Belagat (بلاغة)
Rhetoric/eloquence. The science of effective expression. In Comprehenslate, belagat analysis examines HOW something is said, not just WHAT is said.

### I'caz (إعجاز)
Inimitability. The quality of a text being impossible to replicate. In Comprehenslate, i'caz analysis examines what makes a text's expression unique and irreplaceable.

### Meani (علم المعاني)
The science of meaning through structure. How sentence structure, word order, omission, and emphasis shape meaning. Why a question instead of a statement? Why passive instead of active? This maps to sentence-level and sense-level ambiguity detection.

### Beyan (علم البيان)
The science of figurative language. Metaphor (istiare), simile (teşbih), metonymy (kinaye). How non-literal language operates.

### Bedi (علم البديع)
The science of aesthetic beauty. Wordplay, parallelism, rhythmic balance, phonetic patterns. The surface beauty layer.

### Iltifat
Grammatical person shift as a deliberate rhetorical device. When a text shifts from third person to second person mid-passage, marking an emotional threshold.

### Hasr
Restriction/exclusivity through word order. When grammatical reordering signals "only this, nothing else."

### Nazm
Structural arrangement as meaning carrier. The principle that word order and structure are not decorative but carry meaning that changes if the order changes.
