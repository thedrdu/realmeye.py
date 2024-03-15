from typing import Optional
from bs4 import BeautifulSoup
from realmeye.models import Equipment

def parse_equipment_data(html_data: str) -> Optional[Equipment]:
    """Parses the raw HTML from an equipment's RealmEye Wiki page to retrieve equipment data."""
    soup = BeautifulSoup(html_data, 'html.parser')

    wiki_page = soup.find('div', class_='wiki-page')
    
    tds = wiki_page.find_all('td')

    sprite_url = "https:" + tds[0].img['src'] if tds[0].find('img') else None
    projectile_url = "https:" + tds[1].img['src'] if tds[1].find('img') else None
    description = tds[2].get_text(strip=True) if len(tds) > 2 else None


    return Equipment(
        name=tds[0].img['alt'] if tds[0].find('img') else "Unknown", 
        sprite_url=sprite_url, 
        projectile_url=projectile_url, 
        description=description
    )