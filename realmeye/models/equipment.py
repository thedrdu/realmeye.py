from pydantic import BaseModel
from typing import List, Optional

class Equipment(BaseModel):
    """A Guild object to represent retrieved guild data."""
    name: str
    sprite_url: Optional[str] = None
    projectile_urls: Optional[List[str]] = None
    description: Optional[str] = None
