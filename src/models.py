from dataclasses import dataclass

from typing import Optional

@dataclass
class Article:
    title: str
    source: str
    published_at: str
    content: Optional[str] = None

