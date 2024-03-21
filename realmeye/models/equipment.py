from pydantic import BaseModel
from typing import List, Optional

class Equipment(BaseModel):
    """An Equipment object to represent retrieved equipment data."""
    name: str
    sprite_urls: Optional[List[str]] = None
    projectile_urls: Optional[List[str]] = None
    description: Optional[str] = None
