from pydantic import BaseModel, field_validator
from typing import List, Optional
from .equipment import Equipment

class Character(BaseModel):
    """A Character object to represent retrieved player character data."""
    character_class: str
    level: Optional[int] = 20
    fame: int
    place: int
    items: List[Equipment]
    stats: str
    last_seen: Optional[str] = None