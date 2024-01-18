from pydantic import BaseModel, field_validator
from typing import List, Optional

class Character(BaseModel):
    player_class: str
    level: int
    fame: int
    place: int
    weapon: str
    ability: str
    armor: str
    ring: str
    stats: str
    last_seen: str
    server: str

class Player(BaseModel):
    name: str
    description: Optional[List[str]] = None
    characters_count: int
    skins: int
    exaltations: int
    fame: int
    rank: int
    account_fame: int
    guild: str
    guild_rank: str
    first_seen: str
    last_seen: str
    characters: Optional[List[Character]] = None

    @field_validator('name')
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Player name must not be empty')
        return v