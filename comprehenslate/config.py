from __future__ import annotations

import os
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from dotenv import load_dotenv


class AudienceLevel(str, Enum):
    NATIVE = "native"
    LATE_LEARNER = "late_learner"
    LATE_LEARNER_SIMPLE = "late_learner_simple"


class QuotedContentMode(str, Enum):
    LEAVE = "leave"
    TRANSLATE = "translate"
    TRANSLATE_AND_PRESERVE = "translate_and_preserve"


class DepthProfile(str, Enum):
    SURFACE = "surface"
    STANDARD = "standard"
    DEEP = "deep"
    SCHOLARLY = "scholarly"


class ChunkingStrategy(str, Enum):
    SEMANTIC_CHAPTER = "semantic_chapter"
    SEMANTIC_SECTION = "semantic_section"
    SEMANTIC_PAGE = "semantic_page"
    HEURISTIC_OVERLAPPING = "heuristic_overlapping"


class ParallelMode(str, Enum):
    NONE = "none"
    CHAPTER_THREADED = "chapter_threaded"
    NAIVE = "naive"


class OutputFormat(str, Enum):
    MARKDOWN = "md"
    PDF = "pdf"


def _bool(val: str | None, default: bool = False) -> bool:
    if val is None:
        return default
    return val.strip().lower() in ("1", "true", "yes", "on")


@dataclass
class Config:
    indexing_enabled: bool = True
    harmony_enabled: bool = False
    audience_level: AudienceLevel = AudienceLevel.NATIVE
    poetic_mode: bool = False
    quoted_content: QuotedContentMode = QuotedContentMode.TRANSLATE_AND_PRESERVE
    depth_profile: DepthProfile = DepthProfile.STANDARD
    chunking_strategy: ChunkingStrategy = ChunkingStrategy.SEMANTIC_SECTION
    parallel_mode: ParallelMode = ParallelMode.NONE
    output_format: OutputFormat = OutputFormat.MARKDOWN
    preserve_original_format: bool = False

    @classmethod
    def from_env(cls, env_path: str | Path | None = None) -> Config:
        load_dotenv(env_path or ".env")

        return cls(
            indexing_enabled=_bool(os.getenv("INDEXING_ENABLED"), default=True),
            harmony_enabled=_bool(os.getenv("HARMONY_ENABLED"), default=False),
            audience_level=AudienceLevel(os.getenv("AUDIENCE_LEVEL", "native")),
            poetic_mode=_bool(os.getenv("POETIC_MODE"), default=False),
            quoted_content=QuotedContentMode(os.getenv("QUOTED_CONTENT", "translate_and_preserve")),
            depth_profile=DepthProfile(os.getenv("DEPTH_PROFILE", "standard")),
            chunking_strategy=ChunkingStrategy(os.getenv("CHUNKING_STRATEGY", "semantic_section")),
            parallel_mode=ParallelMode(os.getenv("PARALLEL_MODE", "none")),
            output_format=OutputFormat(os.getenv("OUTPUT_FORMAT", "md")),
            preserve_original_format=_bool(os.getenv("PRESERVE_ORIGINAL_FORMAT"), default=False),
        )
