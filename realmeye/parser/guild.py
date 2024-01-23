from typing import Optional
from bs4 import BeautifulSoup
from realmeye.models import Guild

def parse_guild_data(html_data: str) -> Optional[Guild]:
    """Parses the raw HTML from a guild's RealmEye page to retrieve guild data."""
    soup = BeautifulSoup(html_data, 'html.parser')
    
    if not soup.find('span', class_="entity-name"): # can't think of a better way to check if the query was successful
        return None

    name = soup.find("span", class_="entity-name").get_text()

    summary_table = soup.find("table", class_="summary")
    guild_info = {}

    for tr in summary_table.find_all("tr"):
        key = tr.find_all("td")[0].text.strip()
        value = tr.find_all("td")[1].text.strip()
        guild_info[key] = value

    description = soup.find("div", class_="well description")
    description_lines = [line.get_text() for line in description.find_all("div", class_="description-line")] if description else []

    # ranking data saved, maybe add rank attributes later?
    return Guild(
        name=name,
        description=description_lines,
        member_count=int(guild_info.get('Members')),
        characters=int(guild_info.get('Characters')),
        fame=int(guild_info.get('Fame').split()[0]), 
        active_server=guild_info.get('Most active on').split()[0],   
    )