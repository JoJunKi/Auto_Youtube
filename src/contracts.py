from dataclasses import dataclass, field


@dataclass
class PriceSnapshot:
    ticker: str
    session_date: str
    regular_return_pct: float
    after_hours_return_pct: float | None = None


@dataclass
class StoryPacket:
    story_id: str
    category: str
    title: str
    evidence: list[str] = field(default_factory=list)
    tickers: list[str] = field(default_factory=list)
    prices: list[PriceSnapshot] = field(default_factory=list)


@dataclass
class PublishMetadata:
    title: str
    description: str
    tags: list[str]
    hashtags: list[str]
