# Player

## Overview

The `Player` class in `realmeye.py` is designed to represent individual player data retrieved from a RealmEye player page. The `Player` class also uses integral `Character` objects to represent the visible characters associated with a player.

### Definition

```py
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
```
