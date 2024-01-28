import aiohttp
from urllib.parse import urljoin, quote
from realmeye.constants import routes, HTTPResponseError

async def fetch_guild_page(guild_name: str, session: aiohttp.ClientSession) -> str:
    """Asynchronously retrieves the target guild's RealmEye page."""
    safe_guild_name = quote(guild_name)
    url = urljoin(routes.base_guild_url, safe_guild_name)

    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            raise HTTPResponseError(f"Error: Received a non-200 response code ({response.status}).")