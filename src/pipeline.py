from dataclasses import dataclass
from enum import Enum
from typing import Protocol

from contracts import PublishMetadata, StoryPacket


class Stage(str, Enum):
    INGEST = "ingest"
    PROCESS = "process"
    SCRIPT = "script"
    VALIDATE = "validate"
    CHARTS = "charts"
    TTS = "tts"
    RENDER = "render"
    UPLOAD_LONG = "upload_long"
    SPLIT_SHORTS = "split_shorts"
    UPLOAD_SHORTS = "upload_shorts"
    UPLOAD_REELS = "upload_reels"


class Collector(Protocol):
    def collect(self, cutoff_at: str) -> list[dict]: ...


class ScriptWriter(Protocol):
    def write(self, packets: list[StoryPacket]) -> dict: ...


class Publisher(Protocol):
    def publish(self, media_path: str, metadata: PublishMetadata) -> dict: ...


@dataclass
class PipelineResult:
    stage: Stage
    status: str
    receipt: dict


def run_pipeline(collectors: list[Collector], writer: ScriptWriter,
                 publishers: dict[str, Publisher], upload_date: str) -> list[PipelineResult]:
    """Public orchestration outline; private adapters provide the implementations."""
    results: list[PipelineResult] = []
    # 1) collect and normalize evidence
    # 2) group stories and attach one canonical market snapshot
    # 3) write dialogue and deterministically validate price sentences
    # 4) create charts, TTS and long-form video
    # 5) split topic blocks into Shorts/Reels
    # 6) derive metadata from each video's actual script range and publish
    return results
