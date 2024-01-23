from typing import Optional
from bs4 import BeautifulSoup
from realmeye.models import Guild, Member

def parse_guild_data(html_data: str) -> Optional[Guild]:
    """Parses the raw HTML from a guild's RealmEye page to retrieve guild data."""
    soup = BeautifulSoup(html_data, 'html.parser')
    
    if not soup.find('span', class_="entity-name"): # can't think of a better way to check if the query was successful
        return None

    guild_name = soup.find("span", class_="entity-name").get_text()

    summary_table = soup.find("table", class_="summary")
    guild_info = {}

    for tr in summary_table.find_all("tr"):
        key = tr.find_all("td")[0].text.strip()
        value = tr.find_all("td")[1].text.strip()
        guild_info[key] = value

    description = soup.find("div", class_="well description")
    description_lines = [line.get_text() for line in description.find_all("div", class_="description-line")] if description else []
    
    
    # now we need to parse the member data
    members = []
    table = soup.find("table", id="e")
    for row in table.find_all("tr")[1:]:
        cols = row.find_all("td")
        
        player_name = cols[0].get_text(strip=True)
        if player_name == 'Private': # maybe change this to just have a partial Member object later
            continue
        guild_rank = cols[1].get_text(strip=True)
        fame = cols[2].get_text(strip=True)
        star_rank = cols[3].get_text(strip=True)
        characters = cols[4].get_text(strip=True)
        last_seen = cols[5].get_text(strip=True)
        server = cols[6].get_text(strip=True)

        fame = int(fame) if fame.isdigit() else None
        star_rank = int(star_rank) if star_rank.isdigit() else None
        characters = int(characters) if characters.isdigit() else None

        members.append(Member(
            name=player_name,
            guild_rank=guild_rank,
            fame=int(fame),
            star_rank=int(star_rank),
            characters=int(characters),
            last_seen=last_seen,
            server=server
        ))
    
    # ranking data saved, maybe add rank attributes later?
    return Guild(
        name=guild_name,
        description=description_lines,
        member_count=int(guild_info.get('Members')),
        members=members,
        characters=int(guild_info.get('Characters')),
        fame=int(guild_info.get('Fame').split()[0]), 
        active_server=guild_info.get('Most active on').split()[0],   
    )