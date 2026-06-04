# Structural Exploration: Translation Memory & Glossary System

**Mode:** Artifact exploration (the territory is a concrete design document)
**Entry point:** Frontier-first (broad scan before probing)

---

## Cycle 1 — Broad Scan

### What was scanned

The full `glossary_how.md` document: 362 lines, 7 major sections, covering the translation memory system from problem statement through future considerations.

### Major regions found

| # | Region | Lines | Density |
|---|--------|-------|---------|
| 1 | Problem statement | 1-17 | Low — clean, well-defined |
| 2 | Consistency vs. multi-meaning tension | 20-28 | Low — conceptual framing |
| 3 | Contextual translation memory solution | 32-61 | Medium — format + LLM instruction |
| 4 | Growth mechanism | 65-76 | Low — incremental build lifecycle |
| 5 | Multi-meaning preservation per sentence | 79-189 | High — structured output, combinatorics, storage schema |
| 6 | Edge cases (8 total) | 192-263 | High — 8 sub-regions, each with options and recommendations |
| 7 | Second pass / retranslation | 266-325 | Medium — two-pass vs. indexing comparison |
| 8 | Future considerations | 329-362 | Low — sketch-level items |

### Signals detected

1. **High density in region 5** — the multi-meaning section has a JSON schema, combinatorial analysis, UX description, and glossary feedback loop. More developed than other sections. But also most assumptions.
2. **Tension between regions 3 and 5** — region 3 describes memory as "per-word translation history." Region 5 describes memory as "per-word with all meanings including unchosen ones." These are different data shapes. Which is the actual design?
3. **Absence: no data model** — despite a JSON example in region 5, there's no formal Pydantic model or schema definition. The document describes what should be stored but not how it's structured in code.
4. **Absence: no prompt design** — the document says "inject memory into the instruction prompt" but doesn't specify how. How much memory fits? What format does the LLM receive it in? How is it different from the system prompt?
5. **Edge case 6 (morphological variants)** is flagged but unresolved — root-based matching is a hard dependency on Arabic NLP tooling. This could be a blocker.
6. **The second pass section lacks mechanics** — it describes WHAT changes but not HOW the system decides what to retranslate. Does it retranslate everything? Only sentences where memory changed? Only sentences containing words whose meanings expanded?

### Frontier state after cycle 1

Advancing. The document's conceptual structure is mapped. The boundaries between sections are clear. But the depth within each section varies wildly — some are well-thought-through, others are sketches.

---

## Cycle 2 — Probe: The Data Shape Tension (Signal 2)

### What was probed

The conflict between region 3's "translation memory" and region 5's "multi-meaning output."

### Findings

There are actually **three distinct data structures** hiding in this document, not one:

**Structure A: Translation Memory (per-word, cross-chunk)**
```
word → [
  {context, sentence, chosen_translation, chapter, sentence_num}
]
```
Purpose: consistency across chunks. Injected into prompt. Grows chunk by chunk.

**Structure B: Sentence Output (per-sentence, single-chunk)**
```
sentence → {
  source, primary_translation,
  rich_words: [{word, meanings: [{id, translation, chosen, confidence}]}],
  alternative_readings: [{combination, translation, coherence}]
}
```
Purpose: multi-meaning preservation. Stored as the translation output. Generated per-sentence.

**Structure C: Enriched Translation Memory (hybrid)**
```
word → [
  {context, sentence, chosen_translation, also_valid: [...], chapter, sentence_num}
]
```
Purpose: structure A enriched with structure B's "also valid" meanings. This is what region 5 describes as feeding back into the glossary.

The document conflates these. Structure A is what gets injected into prompts (it must be compact). Structure B is the output format (it can be rich). Structure C is the persistent storage (it accumulates everything). They have different size constraints, different lifecycles, and different consumers.

### Resolution

These are three views of the same underlying data, not three separate systems:
- **Storage** is Structure C (everything, all meanings, all contexts)
- **Prompt injection** is a compressed view of Structure C (only relevant words, only key translations, fits in context window)
- **Output** is Structure B (full detail per sentence, stored alongside the translated text)

### Confidence: Confirmed — this is a real design gap that needs explicit modeling.

---

## Cycle 3 — Probe: Prompt Injection Mechanics (Signal 4)

### What was probed

How does translation memory actually get into the LLM prompt? What are the constraints?

### Findings

**Context window budget:**
A typical LLM call for Comprehenslate would contain:
- System prompt (~2000-4000 tokens, the translation philosophy from notes.md)
- Translation memory injection (~??? tokens)
- Source chunk to translate (~1000-3000 tokens per page)
- Instruction (~200-500 tokens)
- Response space (the structured output, ~2000-5000 tokens per page)

For a 128K context model, that leaves roughly 100K+ tokens for translation memory. For a 32K model, about 20K. For a 8K model, this approach may not work at all.

**A 300-page book might accumulate:**
- ~500-2000 unique significant words
- Each with 1-5 context entries
- Each context entry: ~50-100 tokens (sentence + translation + notes)
- Total: 25,000 to 1,000,000 tokens

This WILL exceed context windows for substantial books. The edge case 1 solutions (relevance filtering, frequency cutoff, compression, tiered memory) aren't optional — they're required for any real book.

**The relevance filtering approach is the most promising:**
Before translating chunk N, scan its source text, extract all words, match against the memory, include only matching entries. This naturally keeps the injection proportional to chunk size, not book size.

### What's still unknown

- What's the actual format the LLM receives? Markdown table? Numbered list? JSON? The format affects how well the LLM uses it.
- Should the memory be in the system message or the user message? System message is more "authoritative" but user message is more flexible.
- How does the LLM signal back "I used a different translation for this word"? This needs to be in the response model so the memory can be updated.

### Confidence: Scanned — the problem is understood but the solution format is undesigned.

---

## Cycle 4 — Probe: Second Pass Mechanics (Signal 6)

### What was probed

How does the second pass actually work? What triggers retranslation?

### Findings

The document says "retranslate with the full translation memory" but doesn't specify the retranslation scope. Three options:

**Option A: Retranslate everything**
- Run the entire book through again, every sentence
- Simplest. Most expensive (doubles cost). Guaranteed comprehensive.
- The memory is now complete, so every sentence gets full-book awareness.
- Many sentences will produce identical translations — wasted work.

**Option B: Retranslate only affected sentences**
- Compare pass 1 memory at time of translation vs. final memory
- A sentence in chapter 3 was translated when the memory had 50 entries. The final memory has 500. Were any of the 450 new entries relevant to that sentence?
- If yes → retranslate. If no → keep pass 1 translation.
- Much cheaper. But requires diff logic.

**Option C: Retranslate only sentences with rich words whose meaning range expanded**
- Track which words gained new meanings after each chapter
- Only retranslate sentences containing those words
- Most surgical. But might miss indirect effects (a word's meaning didn't change, but a related word's meaning changed, affecting the sentence's overall reading).

**The pragmatic answer for v1 is Option A** — retranslate everything. The cost is 2x but the logic is zero. Optimization (Options B/C) can come later when we understand which sentences actually change.

### What's still unknown

- Does pass 2 also update the memory? Could pass 2 discover NEW meanings that pass 1 missed? If so, do we need pass 3?
- In practice, how many sentences actually change between pass 1 and pass 2? This determines whether optimization is even worth building.
- Should pass 2 have access to pass 1's output (the translations) as well as the memory? Seeing what was previously chosen might anchor the LLM's decisions differently than starting fresh.

### Confidence: Scanned — the concept is clear but mechanics are undesigned. Option A is the v1 path.

---

## Cycle 5 — Probe: Morphological Variants (Signal 5)

### What was probed

Edge case 6: grouping words by root across morphological variants.

### Findings

This is a bigger deal than the document suggests. In Arabic:
- A single root (e.g., ك-ت-ب k-t-b) can produce 30+ surface forms
- "كتاب" (kitāb, book), "كاتب" (kātib, writer), "مكتوب" (maktūb, written), "كتب" (kataba, he wrote), "يكتبون" (yaktubūn, they write), etc.
- Surface matching would treat these as completely separate words
- But they're the same conceptual root — translation of one informs translation of others

**Without root grouping, the translation memory is fragmented.** The LLM translating chapter 10 doesn't know that "مكتوب" is related to "كتاب" from chapter 1.

**However:** The LLM itself probably knows Arabic morphology. An alternative to building a root extraction pipeline is to ask the LLM to identify roots as part of the translation output. Each rich word in the response model could include a `root` field. The memory groups by root using LLM-provided root information.

**This is cheaper than building/integrating an Arabic morphological analyzer.** The LLM already does this work implicitly. Making it explicit in the response model is a small addition.

**Risk:** LLM root extraction may be inconsistent. Different calls might assign different roots to the same word. Need validation.

### Confidence: Scanned — the LLM-as-root-extractor approach is viable but unvalidated.

---

## Cycle 6 — Jump Scan: What's Missing Entirely

### Deliberate scan in a different direction

Scanned for things the document doesn't discuss at all — confirmed absences and genuine gaps.

### Confirmed absences (topics outside scope, correctly excluded)

- UI/frontend concerns — correct, this is a backend/module design
- Specific LLM prompts — correct, that's Node 2's job, not this document's
- Pricing/cost modeling — out of scope for a design doc

### Genuine gaps (topics that SHOULD be here but aren't)

**Gap 1: Persistence format for the translation memory**
The document shows JSON for the sentence output but never specifies how the translation memory itself is stored. Is it a JSON file? SQLite database? In-memory dict serialized to disk? For a 300-page book translated over multiple sessions, the memory must persist between runs. This is unaddressed.

**Gap 2: Book structure awareness**
The document talks about "chunks" but never discusses how chunks relate to the book's actual structure (chapters, sections, paragraphs, verses). The translation memory records "chapter 3, sentence 14" but how does the system know chapter boundaries? Is the book pre-parsed into a structure? What input format does the system expect?

**Gap 3: Source text input format**
What format is the book in? Plain text? PDF? DOCX? HTML? Each has different parsing challenges. The document assumes clean text is available but doesn't discuss how it gets there.

**Gap 4: Language pair specification**
The examples are all Arabic → English but the document never discusses whether the memory system is language-pair specific. Does a memory built for Arabic → English work for Arabic → Turkish? Probably not — the translations are target-language specific. But the source word entries and meanings might be reusable.

**Gap 5: Concurrency in parallel processing**
The roadmap mentions parallel batch processing (chapter-threaded and naive). If multiple chunks are translated in parallel, how does the translation memory work? Chunk 5 and chunk 6 are being translated simultaneously — neither has the other's memory contributions. This creates a consistency gap that the document's linear model doesn't address.

**Gap 6: Memory initialization — cold start vs. warm start**
The document describes memory starting empty. But what if the user has domain knowledge? A scholar translating the Quran already knows that "تقوى" should be "God-consciousness" in most contexts. There should be a way to pre-seed the memory with known translations, either from a previous translation project or from expert input. The "human-in-the-loop" section mentions this briefly but doesn't design it.

---

## Convergence Assessment

- **Frontier stability:** Stable. The jump scan found gaps but no new major regions. The document's territory is fully mapped.
- **Declining discovery rate:** Yes. Cycles 5-6 produced refinements and gaps, not new structural features.
- **Bounded gaps:** All 6 gaps are bounded — they sit between explored regions and can be interpolated. No uncharted voids.

**Convergence: achieved.**

---

## Final Deliverable — The Structural Map

### 1. Territory Overview

| Region | Resolution | Status |
|--------|-----------|--------|
| Problem statement | Coarse | Well-defined, no gaps |
| Consistency vs. multi-meaning tension | Coarse | Clean conceptual framing |
| Translation memory solution | Medium | Core concept solid, data shape needs splitting |
| Growth mechanism | Coarse | Lifecycle clear, mechanics undesigned |
| Multi-meaning per sentence | Fine | Most developed region, has JSON schema |
| Edge cases | Medium | 8 cases identified, most with options, few with firm decisions |
| Second pass | Medium | Concept clear, mechanics undesigned |
| Future considerations | Coarse | Sketch-level, correctly deferred |

### 2. Inventory — What Exists in Each Region

**Problem statement:** Three concrete failure modes (terminology drift, tone drift, entity inconsistency). Well-illustrated with Arabic examples.

**Tension:** Clean binary distinction (arbitrary drift vs. contextual variation). The framing that makes the rest of the document possible.

**Solution:** Per-word translation history with context. LLM instruction template. The "provide history, don't enforce" principle.

**Growth:** Three-step lifecycle (empty → incremental → complete). Connection to indexing as "seed."

**Multi-meaning:** Rich word identification, meaning enumeration, coherent combination generation, JSON storage schema, reader UX description, combinatorial explosion handling.

**Edge cases:**
1. Memory too large → 4 solutions (relevance filtering, frequency cutoff, compression, tiered)
2. LLM disagrees → trust + log + consistency report (recommended)
3. Better translation found later → flag for revision (recommended)
4. Proper nouns → two-tier system: strict glossary + contextual memory
5. Multi-word expressions → track phrases as units
6. Morphological variants → 3 options (surface v1, root-based v2, hybrid)
7. Audience level interaction → memory provides history, audience instruction overrides complexity
8. Chapter vs. book context → auto-promote after 3+ chunk appearances

**Second pass:** Pass 1 = discovery (builds memory), pass 2 = refinement (full memory from start). Comparison table vs. indexing. When-to-skip criteria.

**Future:** Reusable memory across books, human-in-the-loop editing, indexing coexistence, consistency report.

### 3. Signal Log

| Signal | Probed? | Finding |
|--------|---------|---------|
| Data shape tension (3 structures hiding as 1) | Yes | Three distinct views needed: storage (full), prompt injection (compressed), output (per-sentence). Design gap confirmed. |
| Prompt injection mechanics | Yes | Context window is a hard constraint. Relevance filtering is required, not optional. Format and message placement undesigned. |
| Second pass mechanics | Yes | Three options (retranslate all / affected only / rich-word only). Option A for v1. |
| Morphological variants | Yes | LLM-as-root-extractor is viable alternative to Arabic NLP dependency. Unvalidated. |
| Missing persistence format | Detected, deferred | How memory is stored between sessions is unaddressed. |
| Missing book structure awareness | Detected, deferred | How the system knows chapter boundaries is unaddressed. |

### 4. Confidence Map

| Region | Confidence |
|--------|-----------|
| Problem statement | **Confirmed** — well-defined, no ambiguity |
| Consistency vs. multi-meaning tension | **Confirmed** — clean framing, no gaps |
| Translation memory core concept | **Confirmed** — the "history not enforcement" principle is solid |
| Translation memory data shape | **Scanned** — three structures identified but not formally modeled |
| Prompt injection format | **Unknown** — what format, where in the message, how compressed |
| Growth lifecycle | **Scanned** — lifecycle clear, extraction step unspecified (how do we get words + translations out of LLM output?) |
| Multi-meaning sentence output | **Confirmed** — JSON schema exists, combinatorial handling specified |
| Edge case resolutions | **Scanned** — options listed for each, recommendations given for some, no firm design |
| Second pass concept | **Confirmed** — clear and well-argued |
| Second pass mechanics | **Inferred** — Option A (retranslate all) for v1, but undesigned |
| Memory persistence | **Unknown** — file format, storage strategy unaddressed |
| Book structure parsing | **Unknown** — how the system ingests and structures a book |
| Source text format | **Unknown** — what input formats are supported |
| Language pair specificity | **Unknown** — whether memory is reusable across target languages |
| Parallel processing interaction | **Unknown** — how memory works when chunks are translated concurrently |
| Memory initialization | **Inferred** — pre-seeding mentioned but not designed |

### 5. Frontier State

The frontier is **stable**. The document's conceptual territory is fully mapped. No structural surprises remain at this resolution.

The unknowns are all at the **implementation edge** — they're questions that arise when you try to build this, not questions about what the system should do conceptually. The document is a strong conceptual design with implementation gaps, which is expected at this stage.

### 6. Gaps and Recommendations

**If further exploration is warranted, probe these in order:**

1. **Data model formalization** — Define the three structures (storage, prompt injection, output) as Pydantic models. This is the bridge to implementation.

2. **Prompt injection format** — Experiment with different formats (markdown table, numbered list, structured text) and measure LLM response quality. This is empirical, not design.

3. **Memory persistence** — Choose a storage format. JSON file is simplest. SQLite if queries are needed. This is a straightforward engineering decision.

4. **Book ingestion** — Define supported input formats and how chapter/section structure is detected. This is a prerequisite for chunking.

5. **Morphological root extraction** — Test the LLM-as-root-extractor approach with real Arabic text. Validate consistency across calls.

6. **Parallel processing memory** — Design how memory works when chunks are translated concurrently. This can be deferred until parallel processing is implemented (Node 5).
