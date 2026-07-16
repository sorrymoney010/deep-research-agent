from dataclasses import dataclass, field
from enum import Enum
from typing import List
import uuid

class SourceTier(str, Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    INTERPRETATION = "interpretation"
    SPECULATION = "speculation"

@dataclass
class Citation:
    title: str
    url: str = ""
    snippet: str = ""
    tier: SourceTier = SourceTier.SECONDARY
    author: str = ""

@dataclass
class Claim:
    text: str
    citations: List[Citation] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    confidence: float = 0.0
    verified: bool = False
    disputed: bool = False
    interpretation: bool = False

@dataclass
class Perspective:
    group: str
    interpretation: str
    based_on: List[str] = field(default_factory=list)

@dataclass
class ResearchState(dict):
    pass
