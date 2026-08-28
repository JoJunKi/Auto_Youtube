import re

from contracts import PublishMetadata, StoryPacket


def _clean(value: str) -> str:
    return re.sub(r"[^0-9A-Za-z가-힣_]", "", value)


def build_metadata(title: str, packets: list[StoryPacket], platform: str) -> PublishMetadata:
    """Create metadata only from packets referenced by the rendered video segment."""
    tickers = sorted({ticker for packet in packets for ticker in packet.tickers})
    categories = list(dict.fromkeys(packet.category for packet in packets))
    tags = list(dict.fromkeys(["미국증시", "미국주식", *categories, *tickers]))
    hashtags = [_clean(tag) for tag in tags if _clean(tag)][:8]
    summary = "\n".join(f"- {packet.title}" for packet in packets[:3])
    description = f"오늘의 핵심 내용\n{summary}\n\n" + " ".join(f"#{tag}" for tag in hashtags)
    if platform == "youtube_short":
        description += " #Shorts"
    elif platform == "instagram_reel":
        description += " #릴스"
    return PublishMetadata(title=title[:100], description=description,
                           tags=tags[:15], hashtags=hashtags)
