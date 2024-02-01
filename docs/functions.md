# Functions

`realmeye.py` provides powerful functions to allow developers to retrieve RealmEye data in a simplified format.

## get_player_data()

`get_player_data()` attempts to retrieve data for a specified player. If the player's RealmEye page is found, the function returns a Player object containing the visible information on the target player's RealmEye page. Otherwise, it returns None.

### Example Usage

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


## get_guild_data()

`get_guild_data()` attempts to retrieve data for a specified guild. If the guild's RealmEye page is found, the function returns a Guild object containing the visible information on the target guild's RealmEye page. Otherwise, it returns None.

### Example Usage

```py
import asyncio
from realmeye import get_guild_data

async def main():
    guild = await get_guild_data("TowerJanitors")
    print_guild_info(guild)

if __name__ == '__main__':
    asyncio.run(main())
```