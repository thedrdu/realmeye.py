# Guild

## Overview

The `Guild` class in `realmeye.py` is designed to represent guild data retrieved from a RealmEye guild page. The `Guild` class also uses integral `Member` objects to represent the visible attributes of members of a guild.

### Definition

```py
class Member(BaseModel):
    """A Member object to represent retrieved guild member data."""
    name: str
    guild_rank: str
    fame: int
    star_rank: int
    characters: int
    last_seen: Optional[str]
    server: Optional[str]

class Guild(BaseModel):
    """A Guild object to represent retrieved guild data."""
    name: str
    description: Optional[List[str]] = None
    member_count: int
    members: List[Member]
    characters: int
    fame: int
    active_server: str
```
