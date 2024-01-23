import aiohttp
import asyncio
from typing import Optional
from realmeye.scraper import fetch_player_page, fetch_guild_page
from realmeye.parser import parse_player_data, parse_guild_data
from realmeye.models import Player, Guild

async def get_player_data(username: str, session: Optional[aiohttp.ClientSession] = None) -> Optional[Player]:
    """Returns a Player object if found, otherwise returns None."""
    async with session or aiohttp.ClientSession() as session:
        html_data = await fetch_player_page(username, session)
        player = parse_player_data(html_data)
        return player

async def get_guild_data(guild_name: str, session: Optional[aiohttp.ClientSession] = None) -> Optional[Guild]:
    """Returns a Guild object if found, otherwise returns None."""
    async with session or aiohttp.ClientSession() as session:
        html_data = await fetch_guild_page(guild_name, session)
        guild = parse_guild_data(html_data)
        return guild