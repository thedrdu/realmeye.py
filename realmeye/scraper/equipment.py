import aiohttp
from urllib.parse import urljoin, quote
from realmeye.constants import routes, HTTPResponseError

async def fetch_equipment_page(equipment_name: str, session: aiohttp.ClientSession) -> str:
    """Asynchronously retrieves the target equipment's RealmEye Wiki page."""
    safe_formatted_equipment_name = quote(equipment_name).replace("'", "_")
    url = urljoin(routes.base_equipment_url, safe_formatted_equipment_name)

    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            raise HTTPResponseError(f"Error: Received a non-200 response code ({response.status}).")