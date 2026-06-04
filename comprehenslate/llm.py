"""LLM integration layer. Wires system prompt + instruction + structured output together."""

from __future__ import annotations

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage

from comprehenslate.config import Config
from comprehenslate.memory import PromptMemory, TranslationMemory
from comprehenslate.models import ChunkOutput, TranslatedSentence
from comprehenslate.prompts.system_prompt import build_system_prompt
from comprehenslate.prompts.translate_instruction import build_instruction


class ComprehenslateLLM:
    """Translation engine. Takes a LangChain chat model, wires prompts and structured output."""

    def __init__(self, model: BaseChatModel, config: Config | None = None):
        self.model = model
        self.config = config or Config()
        self.system_prompt = build_system_prompt(self.config)

    def translate_sentence(
        self,
        text: str,
        target_language: str,
        prompt_memory: PromptMemory | None = None,
    ) -> TranslatedSentence:
        """Translate a short text (paragraph or less). Returns a single TranslatedSentence."""
        instruction = build_instruction(text, target_language, prompt_memory)

        structured_model = self.model.with_structured_output(TranslatedSentence)
        result = structured_model.invoke([
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=instruction),
        ])
        return result

    def translate_chunk(
        self,
        text: str,
        target_language: str,
        prompt_memory: PromptMemory | None = None,
        chapter: int | None = None,
        chunk_index: int = 0,
    ) -> ChunkOutput:
        """Translate a chunk of text. Returns a ChunkOutput with multiple sentences."""
        instruction = build_instruction(text, target_language, prompt_memory)

        structured_model = self.model.with_structured_output(ChunkOutput)
        result = structured_model.invoke([
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=instruction),
        ])
        result.chapter = chapter
        result.chunk_index = chunk_index
        return result

    def translate_book(
        self,
        chunks: list[str],
        target_language: str,
        memory: TranslationMemory | None = None,
        chapters: list[int | None] | None = None,
    ) -> list[ChunkOutput]:
        """Translate a list of chunks sequentially, building memory incrementally.

        If memory is provided, each chunk's Prompt View is built from it and
        the memory is updated after each chunk is translated.
        """
        if memory is None:
            memory = TranslationMemory()

        if chapters is None:
            chapters = [None] * len(chunks)

        results: list[ChunkOutput] = []

        for i, (chunk_text, chapter) in enumerate(zip(chunks, chapters)):
            # Build prompt view from memory for this chunk's vocabulary
            tokens = chunk_text.split()
            prompt_memory = memory.build_prompt_memory(tokens)

            # Translate
            chunk_output = self.translate_chunk(
                text=chunk_text,
                target_language=target_language,
                prompt_memory=prompt_memory,
                chapter=chapter,
                chunk_index=i,
            )

            # Update memory with what we learned
            memory.ingest_chunk(chunk_output)

            results.append(chunk_output)

        return results
