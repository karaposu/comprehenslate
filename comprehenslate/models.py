from __future__ import annotations

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Structure D: Comprehension Output (Stage 1)
# ---------------------------------------------------------------------------


class MeaningCandidate(BaseModel):
    id: str = Field(description="Short identifier, e.g. 'm1', 'm2'")
    description: str = Field(description="Meaning described in source-language terms, NOT translated")
    confidence: float = Field(ge=0, le=1, description="How likely this meaning is in this context")


class AnalyzedWord(BaseModel):
    word: str = Field(description="Surface form as it appears in the source text")
    lemma: str = Field(description="Dictionary headword — the grouping key")
    root: str | None = Field(default=None, description="Derivational root, stored for cross-reference")
    position: int = Field(description="Word position in the sentence")
    meanings: list[MeaningCandidate] = Field(description="All valid meanings in this context")


class ComprehensionResult(BaseModel):
    source: str = Field(description="Original sentence in source language")
    analyzed_words: list[AnalyzedWord] = Field(
        default_factory=list,
        description="Significant words with their lemma, root, and meaning analysis",
    )


class ComprehensionChunkOutput(BaseModel):
    sentences: list[ComprehensionResult]
    chapter: int | None = None
    chunk_index: int = 0


# ---------------------------------------------------------------------------
# Structure C: Translation Output (Stage 2)
# ---------------------------------------------------------------------------


class WordMeaning(BaseModel):
    id: str = Field(description="Short identifier, e.g. 'm1', 'm2'")
    translation: str = Field(description="The translated word/phrase for this meaning")
    confidence: float = Field(ge=0, le=1, description="How likely this meaning is in context")
    chosen: bool = Field(description="Whether this meaning was selected for the primary translation")


class RichWord(BaseModel):
    word: str = Field(description="Surface form as it appears in the source text")
    lemma: str = Field(description="Dictionary headword — the grouping key for translation memory")
    root: str | None = Field(default=None, description="Derivational root, stored for future indexing")
    position: int = Field(description="Word position in the sentence")
    meanings: list[WordMeaning] = Field(description="All valid meanings in this context")


class AlternativeReading(BaseModel):
    combination: dict[str, str] = Field(
        description="Map of rich word surface form to chosen meaning id for this reading"
    )
    translation: str = Field(description="Full sentence translation under this meaning combination")
    coherence: float = Field(ge=0, le=1, description="How well the meanings work together as a sentence")


class TranslatedSentence(BaseModel):
    source: str = Field(description="Original sentence in source language")
    primary_translation: str = Field(description="Best-fit translation")
    rich_words: list[RichWord] = Field(
        default_factory=list,
        description="Words carrying multiple valid meanings in this context",
    )
    alternative_readings: list[AlternativeReading] = Field(
        default_factory=list,
        description="Coherent sentence-level readings from combining different word meanings",
    )
    audience_notes: str | None = Field(
        default=None,
        description="Why certain words were simplified or kept based on audience level",
    )


class ChunkOutput(BaseModel):
    sentences: list[TranslatedSentence]
    chapter: int | None = None
    chunk_index: int = 0
