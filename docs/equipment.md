# Equipment

## Overview

The `Equipment` class in `realmeye.py` is designed to represent equipment item data retrieved from a RealmEye Wiki page.

### Definition

```py
class Equipment(BaseModel):
    """A Guild object to represent retrieved guild data."""
    name: str
    sprite_url: str
    projectile_urls: Optional[List[str]] = None
    description: Optional[str] = None

```
