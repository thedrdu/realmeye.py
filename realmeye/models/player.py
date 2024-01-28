from pydantic import BaseModel, field_validator
from typing import List, Optional

class Character(BaseModel):
    """A Character object to represent retrieved player character data."""
    character_class: str
    level: int
    fame: int
    place: int
    items: List[str]
    stats: str
    last_seen: Optional[str] = None

class Player(BaseModel):
    """A Player object to represent retrieved player data."""
    name: str
    description: Optional[List[str]] = None
    characters_count: Optional[int] = None
    skins: Optional[int] = None
    exaltations: Optional[int] = None
    fame: int
    rank: int
    account_fame: int
    guild: Optional[str] = None
    guild_rank: Optional[str] = None
    first_seen: Optional[str] = None
    created: Optional[str] = None
    last_seen: Optional[str] = None
    characters: Optional[List[Character]] = None

    @field_validator('name')
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Player name must not be empty')
        return v