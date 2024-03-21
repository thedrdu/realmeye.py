# realmeye.py

[![Discord](https://img.shields.io/discord/1220512271126630461?color=7289DA)](https://discord.gg/7hDnTB9jjE)

API wrapper for RealmEye written in Python.

This package aims to provide an abstracted, easy-to-use and fully type-hinted API wrapper for developers, in order to gather player and guild information from RealmEye.

Documentation: https://thedrdu.github.io/realmeye.py/

Currently, `realmeye.py` can be installed directly from [GitHub](https://github.com/thedrdu/realmeye.py) via the following command:

```
pip install git+https://github.com/thedrdu/realmeye.py
```

![realmeye.py](./docs/assets/realmeye.png)

## Example Usage
```py
import asyncio
from realmeye import get_player_data

async def main():
    player = await get_player_data("KatsFan")
    print(len(player.characters))
    print(player.description)

    guild = await get_guild_data("TowerJanitors")
    print(guild.active_server)
    
    equipment = await get_equipment_data("Valor")
    print(equipment.sprite_url)

if __name__ == '__main__':
    asyncio.run(main())
```
Output:
```
6
['Hello!', 'I play on Steam', 'I took a break, came back and urgles are still annoying']
USEast2
https://i.imgur.com/bLCPbmU.png
```

## Requirements
* [Python3.8 or newer](https://www.python.org/downloads/)
* [aiohttp](https://docs.aiohttp.org/en/stable/)
* [pydantic](https://docs.pydantic.dev/latest/)
* [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)

This README will be updated with more information as progress on this package continues.
