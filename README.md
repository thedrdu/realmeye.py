# realmeye.py

API wrapper for RealmEye written in Python.

This package aims to provide an abstracted, easy-to-use and fully type-hinted API wrapper for developers, in order to gather player and guild information from RealmEye.

## Example Usage
```py
import asyncio
from realmeye import get_player_data

async def main():
    player = await get_player_data("KatsFan")
    print(len(player.characters))
    print(player.name)

if __name__ == '__main__':
    asyncio.run(main())

```
Output:
```
8
KatsFan
```

## Requirements
* Python3.8 or newer
* aiohttp
* pydantic (and pydantic-settings)
* beautifulsoup4

This README will be updated with more information as progress on this package continues.