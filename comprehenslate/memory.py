"""Translation memory with lemma-based lookup.

Three views of the same reality:
- TranslationMemory (Structure A): full persistent storage, keyed by lemma
- PromptMemory (Structure B): compressed per-chunk view for LLM prompt injection
- ChunkOutput / RichWord (Structure C): defined in models.py, feeds back into A
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from pydantic import BaseModel, Field

from comprehenslate.models import ChunkOutput, RichWord, WordMeaning


# ---------------------------------------------------------------------------
# Structure A: Storage Layer
# ---------------------------------------------------------------------------


class WordEncounter(BaseModel):
    sentence_source: str
    sentence_translation: str
    chapter: int | None = None
    sentence_num: int = 0
    chosen_meaning: str = Field(description="The meaning id that was selected")
    all_valid_meanings: list[WordMeaning] = Field(default_factory=list)


class WordEntry(BaseModel):
    lemma: str
    root: str | None = None
    surface_forms: list[str] = Field(default_factory=list)
    encounters: list[WordEncounter] = Field(default_factory=list)

    def add_surface_form(self, form: str) -> None:
        if form not in self.surface_forms:
            self.surface_forms.append(form)


class TranslationMemory(BaseModel):
    entries: dict[str, WordEntry] = Field(default_factory=dict)
    surface_to_lemma: dict[str, str] = Field(default_factory=dict)
    root_families: dict[str, list[str]] = Field(default_factory=dict)
    proper_nouns: dict[str, str] = Field(default_factory=dict)

    # -- Lookup ---------------------------------------------------------------

    def lookup(self, surface_form: str) -> WordEntry | None:
        """Two-path lookup: surface form → lemma → entry."""
        lemma = self.surface_to_lemma.get(surface_form)
        if lemma is not None:
            return self.entries.get(lemma)
        return None

    def lookup_lemma(self, lemma: str) -> WordEntry | None:
        return self.entries.get(lemma)

    def known_surface_forms(self) -> set[str]:
        return set(self.surface_to_lemma.keys())

    # -- Ingestion from LLM output (Structure C → Structure A) ---------------

    def ingest_chunk(self, chunk: ChunkOutput) -> None:
        """Extract rich words from a translated chunk and update the memory."""
        for sent in chunk.sentences:
            for rw in sent.rich_words:
                self._ingest_rich_word(
                    rich_word=rw,
                    sentence_source=sent.source,
                    sentence_translation=sent.primary_translation,
                    chapter=chunk.chapter,
                    sentence_num=chunk.sentences.index(sent),
                )

    def _ingest_rich_word(
        self,
        rich_word: RichWord,
        sentence_source: str,
        sentence_translation: str,
        chapter: int | None,
        sentence_num: int,
    ) -> None:
        lemma = rich_word.lemma
        entry = self.entries.get(lemma)

        if entry is None:
            entry = WordEntry(lemma=lemma, root=rich_word.root)
            self.entries[lemma] = entry
        elif entry.root is None and rich_word.root is not None:
            entry.root = rich_word.root

        entry.add_surface_form(rich_word.word)
        self.surface_to_lemma[rich_word.word] = lemma

        # Update root families cross-reference
        if rich_word.root is not None:
            family = self.root_families.setdefault(rich_word.root, [])
            if lemma not in family:
                family.append(lemma)

        # Find which meaning was chosen
        chosen_id = ""
        for m in rich_word.meanings:
            if m.chosen:
                chosen_id = m.id
                break

        entry.encounters.append(
            WordEncounter(
                sentence_source=sentence_source,
                sentence_translation=sentence_translation,
                chapter=chapter,
                sentence_num=sentence_num,
                chosen_meaning=chosen_id,
                all_valid_meanings=rich_word.meanings,
            )
        )

    # -- Proper nouns ---------------------------------------------------------

    def add_proper_noun(self, source: str, target: str) -> None:
        self.proper_nouns[source] = target

    # -- Build prompt view (Structure A → Structure B) ------------------------

    def build_prompt_memory(self, source_tokens: list[str]) -> PromptMemory:
        """Filter and compress memory to only lemmas relevant to the given tokens."""
        matched_lemmas: set[str] = set()
        for token in source_tokens:
            lemma = self.surface_to_lemma.get(token)
            if lemma is not None:
                matched_lemmas.add(lemma)

        hints: list[MemoryHint] = []
        for lemma in sorted(matched_lemmas):
            entry = self.entries[lemma]
            hints.append(_compress_entry(entry))

        return PromptMemory(hints=hints, proper_nouns=self.proper_nouns)

    # -- Persistence ----------------------------------------------------------

    def save(self, path: str | Path) -> None:
        Path(path).write_text(self.model_dump_json(indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str | Path) -> TranslationMemory:
        text = Path(path).read_text(encoding="utf-8")
        return cls.model_validate_json(text)


# ---------------------------------------------------------------------------
# Structure B: Prompt Injection View
# ---------------------------------------------------------------------------


class PreviousTranslation(BaseModel):
    translation: str
    context_summary: str
    frequency: int


class MemoryHint(BaseModel):
    lemma: str
    known_forms: list[str] = Field(default_factory=list)
    previous_translations: list[PreviousTranslation] = Field(default_factory=list)


class PromptMemory(BaseModel):
    hints: list[MemoryHint] = Field(default_factory=list)
    proper_nouns: dict[str, str] = Field(default_factory=dict)

    def render(self) -> str:
        """Render the prompt memory as human-readable text for LLM injection."""
        if not self.hints and not self.proper_nouns:
            return ""

        lines: list[str] = []

        if self.hints:
            lines.append("=== Translation Memory for This Section ===")
            lines.append("")
            for hint in self.hints:
                forms = ", ".join(hint.known_forms) if hint.known_forms else hint.lemma
                lines.append(f"{hint.lemma} [lemma] (forms seen: {forms}):")
                for pt in hint.previous_translations:
                    lines.append(
                        f'  - "{pt.translation}" — used {pt.frequency} time(s) '
                        f"({pt.context_summary})"
                    )
                lines.append("")

        if self.proper_nouns:
            lines.append("=== Proper Nouns (always use exactly) ===")
            for source, target in sorted(self.proper_nouns.items()):
                lines.append(f"{source} → {target}")
            lines.append("")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Compression: Structure A entry → Structure B hint
# ---------------------------------------------------------------------------


def _compress_entry(entry: WordEntry) -> MemoryHint:
    """Compress a full WordEntry into a compact MemoryHint for prompt injection."""
    # Group encounters by chosen translation
    translation_groups: dict[str, list[WordEncounter]] = {}
    for enc in entry.encounters:
        # Find the chosen meaning's translation text
        chosen_text = ""
        for m in enc.all_valid_meanings:
            if m.id == enc.chosen_meaning:
                chosen_text = m.translation
                break
        if chosen_text:
            translation_groups.setdefault(chosen_text, []).append(enc)

    previous: list[PreviousTranslation] = []
    for translation, encounters in translation_groups.items():
        # Build context summary: collect chapters
        chapters: list[str] = []
        for enc in encounters:
            ch = f"ch.{enc.chapter}" if enc.chapter is not None else "?"
            if ch not in chapters:
                chapters.append(ch)
        context_summary = ", ".join(chapters)

        previous.append(
            PreviousTranslation(
                translation=translation,
                context_summary=context_summary,
                frequency=len(encounters),
            )
        )

    # Sort by frequency descending
    previous.sort(key=lambda p: p.frequency, reverse=True)

    return MemoryHint(
        lemma=entry.lemma,
        known_forms=list(entry.surface_forms),
        previous_translations=previous,
    )
