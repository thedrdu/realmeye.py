from pydantic import BaseModel, field_validator
from typing import List, Optional

class Member(BaseModel):
    name: str
    guild_rank: str
    fame: int
    star_rank: int
    characters: int

class Guild(BaseModel):
    name: str
    description: Optional[str] = None
    members: List[Member]
    characters: int
    fame: int
    fame_rank: int
    active_server: str
    active_server_rank: str

    @field_validator('name')
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Guild name must not be empty')
        return v