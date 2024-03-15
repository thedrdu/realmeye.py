from pydantic import BaseModel, field_validator
from typing import List, Optional

class Equipment(BaseModel):
    """A Guild object to represent retrieved guild data."""
    name: str
    sprite_url: str
    projectile_url: Optional[str] = None
    description: Optional[str] = None
