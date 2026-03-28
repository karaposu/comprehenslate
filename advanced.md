# Advanced Comprehenslate

**Six layers deep. Context-aware. Configurable.**

Advanced Comprehenslate extends the core Comprehenslate engine with a structured meaning extraction framework based on six classical layers of textual meaning. It also introduces contextual source attachment, allowing users to provide supplementary materials that inform and sharpen the analysis at every layer.

---

## The Six Layers of Meaning

Every text encodes meaning at multiple depths. Most translators operate at Layer 1. Advanced Comprehenslate can reach all six.

### Layer 1: Sarahat (Explicit Statement)

The literal, surface meaning. The words directly say what they mean.

**Example:** "The army marched north." This means exactly what it says. The army moved in a northward direction.

**What the engine does:** Identifies the primary dictionary meaning of each word and produces a direct, literal translation.

### Layer 2: İşaret (Indication)

The text points toward something without saying it outright. The meaning is logically necessary but unstated.

**Example:** "He walked through the storm without shelter." The text never says he got wet, but it is logically indicated. A translator who renders only the literal words misses the communicated reality.

**What the engine does:** Identifies logical consequences and necessary implications that follow from the explicit statement. Annotates what the text communicates without directly saying.

### Layer 3: Remiz (Symbolic Hint)

A coded or symbolic reference. The text uses a word or image that carries known symbolic weight within its cultural or literary tradition.

**Example:** "Darkness" used to hint at ignorance. "Light" used to represent guidance. These are not metaphors the author invented; they are established symbolic codes within a tradition.

**What the engine does:** Cross-references words and images against known symbolic conventions of the source language and tradition. Flags symbolic meanings and explains their cultural weight. This is where attached context sources become especially valuable, as symbolic conventions vary across traditions and eras.

### Layer 4: Îma (Implication through Structure)

Meaning carried not by the words themselves, but by how they are arranged. Why a sentence is phrased as a question instead of a statement. Why a word is placed at the beginning instead of the end. Why passive voice is used instead of active.

**Example:** In Arabic, bringing the object before the verb can imply exclusivity (hasr). Phrasing a known fact as a question can imply astonishment or rebuke. These structural choices are invisible to standard translation.

**What the engine does:** Analyzes word order, sentence structure, grammatical voice, and syntactic choices. Explains what meaning these structural decisions carry. This layer is deeply connected to the belagat analysis in core Comprehenslate, particularly the science of Meani (علم المعاني).

### Layer 5: Telvih (Allusion)

An indirect meaning that requires multiple mental steps to reach. The author plants a seed that the reader must follow through a chain of associations to arrive at the intended meaning.

**Example:** A text mentions "the companions of the elephant" without further explanation. The informed reader must connect this to the historical event (Abraha's army marching on Mecca with elephants), then understand what that event symbolizes, and then apply that symbolism to the current context. The meaning is three steps removed from the words.

**What the engine does:** Traces chains of association from the text outward. Maps each step in the allusion chain and presents the full reasoning path to the user. Attached context sources (historical records, commentaries) dramatically improve accuracy at this layer.

### Layer 6: Telmih (Reference)

The text references another known text, event, person, or concept. Understanding requires the reader to recognize the reference and import its full context.

**Example:** A single word or phrase that echoes a well-known verse, proverb, or historical moment. The meaning of the current text is incomplete without understanding what it references and why.

**What the engine does:** Identifies cross-references to other texts and known events. Retrieves the referenced material (from attached context sources or its own knowledge base) and explains how the reference enriches or alters the meaning of the current passage.

---

## Configurable Layer Depth

Users can configure which layers the engine analyzes, either by selecting a preset profile or by manually toggling individual layers.

| Profile | Active Layers | Use Case |
|---|---|---|
| **Literal** | 1 | Quick, surface-level translation |
| **Contextual** | 1, 2 | General translation with implied meanings |
| **Cultural** | 1, 2, 3 | Translation with symbolic and cultural awareness |
| **Structural** | 1, 2, 3, 4 | Deep analysis including rhetorical structure |
| **Scholarly** | 1, 2, 3, 4, 5 | Academic-grade analysis with allusion tracing |
| **Complete** | 1, 2, 3, 4, 5, 6 | Full six-layer extraction with cross-referencing |

Users can also create custom profiles, for example activating Layers 1, 2, and 4 only, for a translation that captures literal meaning, implications, and structural rhetoric without diving into symbolism or allusion.

---

## Contextual Source Attachment

Real-world texts do not exist in isolation. Their meaning is shaped by surrounding knowledge: historical events, companion texts, cultural conventions, authorial biography, and more. Advanced Comprehenslate allows users to attach supplementary context sources that the engine uses to sharpen its analysis across all six layers.

### How It Works

Users can attach one or more context sources to any text before running the analysis. Each source is tagged with a type so the engine knows how to use it:

| Source Type | Description | Example |
|---|---|---|
| **Companion Text** | Related primary texts by the same or adjacent authors | Hadith collections attached to Quranic text |
| **Historical Record** | Events, dates, and circumstances surrounding the text | Asbab al-Nuzul (reasons of revelation) for Quranic verses |
| **Commentary** | Existing scholarly interpretations and analyses | Classical tafsir works, literary criticism |
| **Lexicon** | Specialized dictionaries or word databases for the era/domain | Classical Arabic root dictionaries, legal term glossaries |
| **Cultural Corpus** | Poetry, proverbs, speeches from the same era/culture | Pre-Islamic Arabic poetry for understanding Quranic vocabulary |
| **Authorial Context** | Information about the author's life, intent, and circumstances | Biographical records, author's other works |

### How Context Sources Improve Each Layer

**Layer 1 (Sarahat):** A specialized lexicon ensures the engine picks the correct era-appropriate meaning of a word, not the modern default.

**Layer 2 (İşaret):** Historical records help the engine understand what was logically implied given the circumstances. What was obvious to the original audience may be invisible to a modern reader without context.

**Layer 3 (Remiz):** A cultural corpus reveals which symbols and images carried specific weight in the text's era. "Light" and "darkness" may have precise, codified meanings in one tradition that differ from another.

**Layer 4 (Îma):** Commentary sources can confirm or reveal structural choices that carry meaning. Why a verse uses plural instead of singular, why a particular grammatical form was chosen.

**Layer 5 (Telvih):** Without historical records and cultural corpus, allusion chains are nearly impossible to trace. Context sources provide the missing links in the association chain.

**Layer 6 (Telmih):** Companion texts and cultural corpus are essential. The engine cannot recognize a reference to another text if it has never seen that text.

### Example: Quranic Translation with Context

A user wants to analyze Surah Al-Baqarah with full six-layer depth. They attach:

- Sahih al-Bukhari and Sahih Muslim (Companion Text)
- Asbab al-Nuzul by al-Wahidi (Historical Record)
- Tafsir al-Tabari (Commentary)
- Lisan al-Arab by Ibn Manzur (Lexicon)
- Mu'allaqat and pre-Islamic poetry (Cultural Corpus)

The engine now operates with a rich contextual foundation. When it encounters a word with multiple root meanings, the lexicon and cultural corpus help resolve which meaning was active in 7th-century Arabic. When it encounters an allusion, the historical record and companion texts help trace it. When it encounters a structural choice, the commentary confirms the rhetorical intent.

Without these sources, the engine still functions, but at reduced accuracy for Layers 3-6. The analysis output clearly indicates which findings were supported by attached context and which were inferred without it.

---

## Output Structure

For each passage analyzed, Advanced Comprehenslate produces a layered output:

```
Passage: [Original text]

Layer 1 - Sarahat (Explicit):
  Translation: [Literal translation]

Layer 2 - İşaret (Indicated):
  Implications: [What the text logically implies without stating]

Layer 3 - Remiz (Symbolic):
  Symbols identified: [Word/phrase → symbolic meaning]
  Cultural basis: [Source or tradition behind the symbolism]

Layer 4 - Îma (Structural):
  Structural choices: [What the arrangement communicates]
  Belagat notes: [Meani/Beyan/Bedi analysis]

Layer 5 - Telvih (Allusion):
  Allusion chain: [Step-by-step path from text to intended meaning]
  Context sources used: [Which attached sources informed this]

Layer 6 - Telmih (Reference):
  References found: [What other texts/events are referenced]
  Impact on meaning: [How the reference changes interpretation]

Confidence: [How supported each layer's findings are]
Context coverage: [Which layers had sufficient context, which did not]
```

---

## Relationship to Core Comprehenslate

Advanced Comprehenslate builds on top of the core engine. The two-phase architecture (Comprehension → Translation) remains the foundation. The six-layer framework operates within Phase 1 (Comprehension), providing a structured methodology for the meaning index. Contextual source attachment feeds into both phases, enriching comprehension and improving translation accuracy.

```
┌─────────────────────────────────────────────────────────┐
│                    Source Material                       │
│              + Attached Context Sources                  │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│              PHASE 1: COMPREHENSION                     │
│                                                         │
│  ┌────────────────────────────────────────────────────┐ │
│  │         Six-Layer Meaning Extraction               │ │
│  │                                                    │ │
│  │  L1 Sarahat ──► L2 İşaret ──► L3 Remiz            │ │
│  │       │              │             │               │ │
│  │       ▼              ▼             ▼               │ │
│  │  L4 Îma ──────► L5 Telvih ──► L6 Telmih           │ │
│  └──────────────────────┬─────────────────────────────┘ │
│                         │                               │
│  ┌──────────────┐  ┌────┴───────┐  ┌────────────────┐  │
│  │  Synonym &   │  │  Meaning   │  │  Belagat &     │  │
│  │  Word Choice │  │  Index     │  │  I'caz         │  │
│  └──────────────┘  └────┬───────┘  └────────────────┘  │
└─────────────────────────┼───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              PHASE 2: TRANSLATION                       │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌────────────────┐  │
│  │  Sentence    │  │  Multi-     │  │  Word Choice   │  │
│  │  Translator  │──│  Meaning    │──│  Annotator     │  │
│  │              │  │  Combiner   │  │                │  │
│  └─────────────┘  └─────────────┘  └────────────────┘  │
│                         │                               │
│                         ▼                               │
│             ┌───────────────────────┐                    │
│             │   Layered Annotated   │                    │
│             │   Output (L1-L6)      │                    │
│             └───────────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

---

## Roadmap

- [ ] Six-layer extraction engine (L1-L6)
- [ ] Configurable layer profiles (presets and custom)
- [ ] Context source attachment and ingestion pipeline
- [ ] Context source types: Companion Text, Historical Record, Commentary
- [ ] Context source types: Lexicon, Cultural Corpus, Authorial Context
- [ ] Per-layer confidence scoring
- [ ] Context coverage reporting (which layers had sufficient sources)
- [ ] Layered output format with collapsible depth view
- [ ] Integration with core Comprehenslate belagat and synonym analysis
- [ ] Pre-built context bundles for common use cases (Quranic studies, legal texts)
- [ ] User interface for attaching, tagging, and managing context sources
- [ ] API support for programmatic context attachment

---

*Advanced Comprehenslate: because meaning lives at depths most translators never reach.*