# Sensemaking: How Comprehension Works

---

## SV1 — Baseline Understanding

The user is designing Stage 1 (Comprehension) as a multi-step pipeline that processes a page of text. The steps involve: pre-analysis (extract lemma, root per word), ambiguity detection at three levels (word, sentence, sense), loading layered previous context to resolve ambiguities, and then resolving ambiguities by generating possible interpretations. There's also a foundational question: what does "comprehended" even mean? When is comprehension done?

---

## Phase 1 — Cognitive Anchor Extraction

### Constraints

- **C1:** Comprehension operates on one page/chunk at a time but has access to previous context.
- **C2:** Comprehension does NOT translate — it produces understanding described in source-language terms.
- **C3:** The output must feed into the Comprehension Index (Structure A) — lemma, root, meanings, contexts.
- **C4:** Previous context is layered: immediate (last 5-10 pages) + generic (summary/TOC-like index of the whole book so far).

### Key Insights

- **K1:** The user is describing comprehension as three sub-stages: EXTRACT → DETECT AMBIGUITY → RESOLVE WITH CONTEXT. This is a pipeline, not a single LLM call.
- **K2:** Ambiguity exists at three levels, each requiring different resolution strategies:
  - **Word-level:** a word has multiple dictionary meanings. Resolution = which meaning(s) are active here.
  - **Sentence-level:** the sentence structure is ambiguous (who does what to whom, scope of modifiers). Resolution = which parse(s) are valid.
  - **Sense-level:** the overall meaning/intent of the passage is unclear (is this literal or metaphorical? is this a command or a question? what is the author's purpose?). Resolution = which interpretation(s) fit.
- **K3:** "Resolving" an ambiguity does NOT mean picking one answer — it means generating all valid interpretations with confidence levels. This is consistent with Comprehenslate's multi-meaning philosophy.
- **K4:** Previous context is the key resolver. Without it, many ambiguities are unresolvable. With it, the system can say "this word was used in meaning X on page 3 and meaning Y on page 15, and here on page 20 the context matches X."
- **K5:** The question "what does comprehended mean?" is the deepest anchor. Without a definition, the pipeline has no completion criterion.

### Structural Points

- **S1:** The pipeline has a clear sequence: Extract → Detect → Load Context → Resolve.
- **S2:** Previous context has two tiers: immediate (detailed, last 5-10 pages) and generic (compressed, whole-book-so-far summary).
- **S3:** The Comprehension Index (Structure A) serves double duty: it IS the generic previous context for future pages. As you comprehend page 20, the index built from pages 1-19 IS your generic context.
- **S4:** Each level of ambiguity maps to a different grain of analysis and a different resolution strategy.

### Foundational Principles

- **F1:** From `notes.md`: "the beauty and meaning of a text appears in its totality. When you break it into parts, the overall coherence can vanish." This means page-level comprehension is inherently incomplete — it needs the book-level context (previous context) to be accurate.
- **F2:** From `notes.md`: "all meanings derived from a text are valid and intended, as long as they don't violate the grammatical rules and foundational principles of the language." Resolution means enumerating valid interpretations, not choosing one.
- **F3:** From `notes.md`: "a text is self-illuminating if it contains its own interpretive key." Some ambiguities resolve within the page itself. Others require previous context. Others may not resolve until later pages — and that's OK.

### Meaning-Nodes

- **M1:** "Comprehended" = every significant word has been analyzed for lemma, root, and meanings; every ambiguity has been detected; every resolvable ambiguity has been resolved into interpretations; unresolvable ambiguities are explicitly flagged as open.
- **M2:** Previous context is not just "what came before" — it's a structured, queryable resource that the comprehension system uses to resolve ambiguities. It's dynamic and layered.
- **M3:** The comprehension pipeline is a funnel: raw text → structured words → detected ambiguities → resolved interpretations.

---

## SV2 — Anchor-Informed Understanding

Comprehension is a four-step pipeline:

```
1. PRE-ANALYSIS    → extract words, lemma, root
2. AMBIGUITY DETECTION → find what's unclear at word/sentence/sense levels
3. CONTEXT LOADING → bring in previous context (immediate + generic)
4. RESOLUTION      → generate interpretations for each ambiguity using context
```

The definition of "comprehended": a page is comprehended when every ambiguity has been either resolved (interpretations generated) or explicitly marked as unresolvable with current context.

Previous context is the Comprehension Index itself — pages 1 through N-1 build the index, and page N reads that index as its context.

---

## Phase 2 — Perspective Checking

### Technical / Logical

**How many LLM calls per page?**

The pipeline has four steps. Options:
- **One call:** Send everything at once — "analyze this page, detect ambiguities, here's previous context, resolve them." Simplest but the LLM may skip steps or do them shallowly.
- **Two calls:** Call 1: pre-analysis + ambiguity detection (no context needed). Call 2: load context + resolve (context injected). This is cleaner — detection happens without context bias, then resolution happens with context.
- **Three+ calls:** Each step is a separate call. Most thorough but expensive.

New anchor: **Two calls is the sweet spot for v1.** Call 1 detects without context (unbiased). Call 2 resolves with context (informed). More calls can come later for deeper analysis.

**Previous context as layered input:**

The user described two layers:
- Immediate: last 5-10 pages, detailed. This is the raw ComprehensionResults from recent pages.
- Generic: whole-book summary + TOC-like index. This is the compressed Comprehension Index — the same compression logic as Structure B (Prompt View).

New anchor: **Immediate context = recent ComprehensionResults (Structures D). Generic context = compressed Comprehension Index (like Structure B).** Both already exist in our data model. No new structures needed.

**The "similar words" dynamic lookup:**

The user said previous context "can look up similar words and how they were used." This means during resolution, the system can query the index: "show me every time a word from the same root family appeared" or "show me every time a word with a similar meaning appeared." This is where `root_families` becomes active — not for grouping, but for querying related words during comprehension.

New anchor: **Root families become active during comprehension, not translation.** The `root_families` cross-reference in the index is used during Stage 1 to find related words for disambiguation. This is the first real use of the root field.

### Human / User

The user reviewing the comprehension output wants to see:
- "Here are the ambiguities I found"
- "Here's how I resolved each one, and why"
- "Here are the ones I couldn't resolve — you may need to help"

New anchor: **Ambiguities should be first-class objects in the output, not hidden inside word meanings.** The user should see a list of detected ambiguities with their resolutions, not just final meanings.

### Strategic / Long-term

The comprehension pipeline is the core intellectual engine of Comprehenslate. The translation step is comparatively mechanical — "express this understood meaning in another language." The comprehension step is where the value lives.

Building comprehension as a well-defined pipeline (extract → detect → load → resolve) means each step can be improved independently. Better ambiguity detection. Richer context loading. Smarter resolution. Each is a separate concern.

### Risk / Failure

- **Risk:** LLM may not reliably separate "detect ambiguity" from "resolve ambiguity." Given text and context together, it may jump to resolution without proper detection.
- **Mitigation:** Two-call approach. Call 1 has NO context, so the LLM can only detect, not resolve. Call 2 gets context and is told to resolve.

- **Risk:** Immediate context (5-10 pages of raw analysis) may be too large for the prompt.
- **Mitigation:** Compress immediate context similarly to generic context but with more detail. Or use a sliding window with overlap.

- **Risk:** "Sense-level ambiguity" is vague. What counts as a sense-level ambiguity vs. just a hard sentence?
- **Mitigation:** Define it precisely — see ambiguity collapse below.

### Definitional / Consistency

Does this pipeline contradict the two-stage separation? No — this IS Stage 1 in detail. The sensemaking on two-stage separation said "Stage 1 analyzes chunk by chunk." This pipeline defines HOW each chunk is analyzed.

Does this change `ComprehensionResult` in models.py? Yes — the current model only has `AnalyzedWord`. It needs to also capture detected ambiguities and their resolutions as separate output objects.

---

## SV3 — Multi-Perspective Understanding

Major expansions:

1. **Comprehension is a two-call pipeline per page:** Call 1 (extract + detect, no context) → Call 2 (resolve with context). This separation prevents context bias during detection.

2. **Previous context uses existing structures:** Immediate = recent Structure D outputs. Generic = compressed Structure A (like Structure B). No new data models needed for context itself.

3. **Root families activate during comprehension.** The cross-reference becomes useful HERE — querying related words to help resolve ambiguities. This is the first real use of the root field.

4. **Ambiguities are first-class output objects.** Not hidden inside word meanings — they're detected, described, and resolved (or marked unresolvable) as explicit items the user can review.

5. **The definition of "comprehended"** is becoming clearer: it's not "I understand everything perfectly." It's "I've detected every ambiguity, resolved what I can with available context, and explicitly flagged what I can't."

---

## Phase 3 — Ambiguity Collapse

### Ambiguity 1: What are the three levels of ambiguity exactly?

**Resolution:**

**Word-level ambiguity:** A single word has multiple valid dictionary meanings in this context. The surrounding sentence doesn't fully disambiguate.
- Example: "ضرب" could mean "struck," "set forth," or "traveled." The sentence grammar allows multiple readings.
- Resolution: list all valid meanings with confidence. Context from previous pages may narrow it ("this author always uses ضرب to mean 'set forth' in parable contexts").

**Sentence-level ambiguity:** The sentence structure allows multiple valid parses — different subjects, objects, scope of modifiers, or grammatical relationships.
- Example: "He told the man who was standing to sit" — did he tell the standing man to sit, or did he tell the man while he himself was standing?
- Example: Arabic sentences where word order flexibility creates genuine structural ambiguity about who acts on whom.
- Resolution: list all valid structural parses. Previous context may reveal which structure the author typically uses.

**Sense-level ambiguity:** The overall meaning or purpose of a passage is unclear — literal vs. metaphorical, rhetorical intent, register, what the author is trying to achieve.
- Example: "Is this sentence a genuine question or a rhetorical device expressing impossibility?" (from `notes.md`: كَيْفَ "how" functioning as both question and denial)
- Example: "Is this passage literal description or allegory?"
- Resolution: list all valid interpretive frames. Previous context (how has the author used similar devices before?) helps, but sense-level ambiguities are often the hardest to resolve and may remain open.

**What is now fixed?** Three levels with clear definitions and examples. Each maps to a different grain: word, sentence, passage.

**What is no longer allowed?** Treating ambiguity as a single flat concept. The detection prompt must ask for all three levels separately.

**What now depends on this choice?** The comprehension output model needs an `Ambiguity` object with a `level` field (word/sentence/sense).

---

### Ambiguity 2: What does "resolved" mean for an ambiguity?

The user said: "solving means creating possible interpretations."

**Resolution:** An ambiguity is "resolved" when:
- All valid interpretations have been enumerated
- Each interpretation has a confidence level
- If context supports one interpretation strongly, it's marked as primary
- If context doesn't disambiguate, all interpretations remain open with similar confidence

"Resolved" does NOT mean "picked one answer." It means "mapped the space of valid readings."

An ambiguity is "unresolvable with current context" when:
- The text itself is genuinely ambiguous (by design or accident)
- No previous context helps narrow it
- Future pages might resolve it (forward reference)

**What is now fixed?** Resolution = enumeration of interpretations, not selection of one.

**What is no longer allowed?** Forcing a single interpretation. An ambiguity with three equally valid readings stays as three readings.

**What now depends on this choice?** The output model needs `Interpretation` objects per ambiguity, each with confidence.

---

### Ambiguity 3: What does "comprehended" mean?

This is the foundational question. When is a page "done" being comprehended?

**Resolution:** A page is comprehended when:

1. **Every significant word** has been analyzed: lemma, root, and at least one valid meaning identified.
2. **Every ambiguity has been detected** at all three levels (word, sentence, sense).
3. **Every detected ambiguity has been processed:** either resolved (interpretations generated with confidence) or explicitly marked as unresolvable with reasoning.
4. **The page's contribution to the index is complete:** all word entries, contexts, and meanings are ready to be merged into the Comprehension Index.

Comprehension is NOT:
- Certainty ("I know exactly what this means") — multi-meaning is expected
- Translation ("I can express this in another language") — that's Stage 2
- Agreement ("this is THE interpretation") — multiple valid readings coexist

Comprehension IS:
- Awareness ("I know what this could mean, at every level")
- Completeness ("I haven't missed any significant word or ambiguity")
- Honesty ("I've flagged what I can't resolve")

**What is now fixed?** A four-point completion criterion for comprehension.

**What is no longer allowed?** Declaring a page "comprehended" without processing ambiguities. Pre-analysis alone is not comprehension.

**What changed?** Comprehension has a testable definition. You can check: are all words analyzed? Are all ambiguities detected? Are all ambiguities processed? Is the index updated? If yes to all four → comprehended.

---

### Ambiguity 4: How does previous context work practically?

The user described two layers: immediate (last 5-10 pages) and generic (summary/TOC-like). How do these map to existing structures?

**Resolution:**

**Immediate context** = the last N `ComprehensionResult` outputs (Structure D) from recent pages. These are detailed — every word, every meaning, every ambiguity from nearby pages. Controlled by a sliding window (default: last 5-10 pages). Sent to the LLM in Call 2 as detailed reference.

**Generic context** = a compressed view of the entire Comprehension Index (Structure A) built so far. Similar to Structure B (Prompt View) but used for comprehension, not translation. Contains: all lemmas encountered, their most common meanings, frequency across the book, root family mappings. This is the "TOC-like" overview.

**Dynamic lookup** = during resolution, the system can query the index for specific information: "show me all words from root family ك-ت-ب and how they were used." This is a targeted query, not a bulk inclusion. The `root_families` cross-reference enables this.

**What is now fixed?** Previous context = immediate (recent Structure D) + generic (compressed Structure A) + dynamic lookup (targeted queries against A).

**What is no longer allowed?** Sending the entire index as context. It must be compressed and filtered.

**What now depends on this choice?** A `build_comprehension_context()` method on the Comprehension Index that produces the layered context for a given page.

---

## SV4 — Clarified Understanding

The comprehension pipeline for one page:

```
PRE-STEP: Meaning Space Lookup (system, no LLM call)
  - Scan source page for tokens
  - Check Comprehension Index: has this word been seen before? What meanings were found?
  - Check attached lexicon (if any): what meanings does this word have in this era/domain?
  - Produce a "meaning space" for each word: all known possible meanings
  Purpose: the LLM can't detect that a word is ambiguous unless it knows the
           word HAS other meanings. This step provides that knowledge.

  ↓

CALL 1: Extract & Detect (with meaning space, WITHOUT book context — unbiased)
  Input:  source page + meaning space per word
  Output: analyzed words (lemma, root, meanings) + detected ambiguities at 3 levels
  Key:    the LLM knows what each word CAN mean (from meaning space)
          but doesn't know how the AUTHOR has used it (no book context yet)

  ↓

CONTEXT LOADING (system, between calls)
  - Immediate: last 5-10 pages of ComprehensionResults
  - Generic: compressed Comprehension Index (whole book so far)
  - Dynamic: targeted lookups (root families, specific lemmas)

  ↓

CALL 2: Resolve (with previous book context)
  Input:  source page + Call 1 output + layered previous context
  Output: resolved ambiguities (interpretations with confidence) + updated word meanings
```

The distinction between meaning space (pre-step) and previous context (between calls):
- **Meaning space** = what a word CAN mean (dictionary knowledge, prior index entries). Answers: "what are the possibilities?"
- **Previous context** = how the AUTHOR has used words in this book. Answers: "which possibilities are most likely HERE?"

Call 1 gets meaning space so it can detect ambiguities properly. Call 2 gets book context so it can resolve them. Detection is informed but unbiased. Resolution is contextual.

**Where does the meaning space come from?**

1. **The Comprehension Index (pages already analyzed).** If "ضرب" appeared on page 3 with meanings m1, m2, m3, the index already knows its range. This is the primary source — the book is its own best dictionary.

2. **An attached lexicon (optional).** For words appearing for the first time, or for specialized/classical vocabulary where the LLM's built-in knowledge may be insufficient. This maps to the "Lexicon" context source type from `advanced.md` — specialized dictionaries for the era/domain (e.g., classical Arabic root dictionaries, legal term glossaries).

3. **The LLM's built-in knowledge (fallback).** For common words with no index entry and no attached lexicon, the LLM's training data covers the meaning space. This is the least reliable source for specialized texts but sufficient for general vocabulary.

The system tries sources in order: index first (most reliable for this book), then lexicon (most reliable for this domain), then LLM knowledge (general fallback).

A page is "comprehended" when:
1. All significant words analyzed (lemma, root, meanings)
2. All ambiguities detected (word, sentence, sense levels)
3. All ambiguities processed (resolved with interpretations OR flagged as unresolvable)
4. Page contribution ready for index merge

---

## Phase 4 — Degrees-of-Freedom Reduction

### Fixed Variables

| Variable | Fixed Value |
|---|---|
| Steps per page | Pre-step (meaning space lookup) + 2 LLM calls |
| Meaning space sources | Index (primary) → attached lexicon (optional) → LLM knowledge (fallback) |
| Ambiguity levels | 3 (word, sentence, sense) |
| Call 1 input | Source page + meaning space per word (NO book context) |
| Call 2 input | Source page + Call 1 output + layered previous context |
| Previous context layers | 3 (immediate, generic, dynamic lookup) |
| Immediate context window | Last 5-10 pages of ComprehensionResults |
| Generic context source | Compressed Comprehension Index |
| Resolution definition | Enumerate interpretations with confidence, not pick one |
| Comprehension definition | 4-point criterion (words analyzed, ambiguities detected, ambiguities processed, index ready) |
| Root families usage | Active during comprehension for dynamic lookup |

### Eliminated Options

- Single LLM call for everything (too shallow, context biases detection)
- Three+ calls per page (too expensive for v1)
- Sending full index as context (too large)
- Resolution = picking one answer (violates multi-meaning philosophy)
- Comprehension = certainty (wrong definition)
- Expecting LLM to detect ambiguity without knowing meaning space (can't detect what it doesn't know exists)

### Remaining Viable Path

One open question: **what new models are needed?**

The current `ComprehensionResult` only has `AnalyzedWord`. It needs:
- `Ambiguity` — a detected ambiguity with level, description, and location
- `Interpretation` — one possible reading of an ambiguity, with confidence
- `AmbiguityResolution` — an ambiguity paired with its interpretations and status (resolved/unresolvable)

---

## SV5 — Constrained Understanding

The comprehension output model expands:

```python
class Ambiguity(BaseModel):
    level: str              # "word" | "sentence" | "sense"
    description: str        # what's ambiguous
    location: str           # which word/sentence/passage
    source_text: str        # the relevant text

class Interpretation(BaseModel):
    id: str                 # "i1", "i2", etc.
    reading: str            # what this interpretation says
    confidence: float       # how supported by context
    supporting_context: str | None  # what in previous context supports this

class AmbiguityResolution(BaseModel):
    ambiguity: Ambiguity
    status: str             # "resolved" | "unresolvable"
    interpretations: list[Interpretation]
    reasoning: str          # why these interpretations, why this status

class ComprehensionResult(BaseModel):
    source: str
    analyzed_words: list[AnalyzedWord]
    ambiguities: list[AmbiguityResolution]  # NEW
```

---

## SV6 — Stabilized Model

### Final Conceptual Model

**Comprehension is a pre-step + two-call pipeline per page:**

**Pre-step — Meaning Space Lookup (system, no LLM):**
- Scan source page for tokens
- For each word, look up what it CAN mean:
  1. Check Comprehension Index (has this word been seen before in this book?)
  2. Check attached lexicon if available (era/domain-specific dictionary)
  3. Fall back to LLM's built-in knowledge for unknown words
- Produce a meaning space: all known possible meanings per word
- Purpose: the LLM can't detect ambiguity in a word unless it knows the word has other meanings

**Call 1 — Extract & Detect (with meaning space, WITHOUT book context — unbiased):**
- LLM receives: source page + meaning space per word
- Pre-analyze every significant word: surface form, lemma, root, all valid meanings
- Detect ambiguities at three levels:
  - **Word:** a word has multiple valid meanings that the sentence doesn't disambiguate
  - **Sentence:** the sentence structure allows multiple valid parses
  - **Sense:** the passage's overall meaning/intent is unclear (literal vs. metaphorical, rhetorical purpose)
- Key: the LLM knows what each word CAN mean but not how the author HAS used it

**Between calls — Context Loading (system):**
- **Immediate:** last 5-10 pages of detailed analysis (recent ComprehensionResults)
- **Generic:** compressed whole-book index (similar to Structure B compression)
- **Dynamic:** targeted queries against the index — e.g., "how has root family ك-ت-ب been used so far?" This is where `root_families` becomes active.

**Call 2 — Resolve (informed by book context):**
- For each detected ambiguity, generate all valid interpretations using previous context
- Assign confidence to each interpretation
- Mark unresolvable ambiguities explicitly with reasoning
- Update word meanings based on resolution (context may narrow or expand meanings)

**A page is "comprehended" when:**
1. All significant words analyzed (lemma, root, meanings)
2. All ambiguities detected at all three levels
3. All ambiguities processed (resolved with interpretations OR flagged unresolvable)
4. Page contribution merged into the Comprehension Index

**"Comprehended" = the space of valid readings has been mapped.** Not "I know what this means" but "I know everything this COULD mean, and I've used all available context to assess which readings are most supported."

### How SV6 Differs from SV1

SV1 had a vague sequence: "extract, detect ambiguity, use context, resolve." SV6 has:
- A meaning space pre-step that feeds known meanings to the LLM BEFORE detection (the LLM can't detect ambiguity in what it doesn't know exists)
- Meaning space sourced from: index (primary) → attached lexicon (optional) → LLM knowledge (fallback)
- A precise two-call pipeline with clear separation (detect with meaning space but without book context, resolve with book context)
- Three defined levels of ambiguity with examples and distinct resolution strategies
- Layered previous context (immediate + generic + dynamic) mapped to existing data structures
- A testable four-point definition of "comprehended"
- Resolution defined as "enumerate interpretations" not "pick one answer"
- Root families activated for the first time — used in comprehension's dynamic context lookup
- A concrete model expansion (Ambiguity, Interpretation, AmbiguityResolution added to ComprehensionResult)
