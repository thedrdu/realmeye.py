import aiohttp
import asyncio
from realmeye.scraper import fetch_player_page
from realmeye.parser import parse_player_data

async def get_player_data(username: str, session=None):
    async with session or aiohttp.ClientSession() as session:
        html_data = await fetch_player_page(username, session)
        player = parse_player_data(html_data)
        return player