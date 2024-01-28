import aiohttp
from urllib.parse import urljoin, quote
from realmeye.constants import routes, HTTPResponseError

async def fetch_player_page(username: str, session: aiohttp.ClientSession) -> str:
    """Asynchronously retrieves the target username's RealmEye page."""
    safe_username = quote(username)
    url = urljoin(routes.base_player_url, safe_username)

    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            raise HTTPResponseError(f"Error: Received a non-200 response code ({response.status}).")
