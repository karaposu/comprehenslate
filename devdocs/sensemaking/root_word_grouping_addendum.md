# Addendum: Don't Blindly Trust LLM for Root Extraction

The sensemaking analysis eliminated external morphological analyzers too aggressively. Correction:

## The Issue

LLMs can:
- Hallucinate roots for rare words
- Be inconsistent across calls (same word, different root)
- Get ambiguous cases wrong with no way to validate

Trusting the LLM blindly for root/lemma extraction is risky for production-quality translation.

## Revised Position

- **V1 (now):** LLM-provided lemma. Zero dependencies, good enough to start. Accept the risk.
- **V2 (later):** Pluggable lemma extraction. Support external analyzers (CAMeL Tools, Farasa, etc.) as an option. The user configures which backend to use.

## Architectural Implication

Lemma extraction should be behind an interface:

```python
class LemmaExtractor(Protocol):
    def extract(self, word: str, language: str) -> str: ...

class LLMProvidedLemma:
    """V1: trust LLM output"""
    ...

class CAMeLToolsLemma:
    """V2: use CAMeL Tools for Arabic"""
    ...
```

The translation memory doesn't care where the lemma comes from. It just receives a string grouping key.

## What Changed

- External morphological analyzers are NOT eliminated — they're deferred.
- The design must keep the door open for them via a pluggable interface.
- "Zero external dependencies" is a V1 constraint, not a permanent architectural principle.
