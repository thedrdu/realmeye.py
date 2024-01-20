from typing import Optional
from bs4 import BeautifulSoup
from realmeye.models import Player, Character

def parse_player_data(html_data: str) -> Optional[Player]:
    """Parses the raw HTML from a user's RealmEye page to retrieve player data."""
    soup = BeautifulSoup(html_data, 'html.parser')
    
    if soup.find("ul", class_="player-not-found"):
        return None
    
    name = soup.find("span", class_="entity-name").get_text()

    description = soup.find("div", class_="well description").find_all("div", class_="description-line")
    description = [line.get_text() for line in description]

    summary_table = soup.find("table", class_="summary")
    player_info = {}

    for tr in summary_table.find_all("tr"):
        key = tr.find_all("td")[0].text.strip()
        value_td = tr.find_all("td")[1]

        numeric_span = value_td.find("span", class_="numeric")
        if numeric_span:
            value = numeric_span.text.strip()
        elif value_td.find("a"):
            value = value_td.find("a").text.strip()
        elif value_td.find("div"):
            value = value_td.get_text(separator=" ", strip=True)
        else:
            value = value_td.text.strip()

        player_info[key] = value
    
    
    # now we retrieve the character data(if it exists)
    characters = []

    thead = soup.find('thead')
    if thead:
        headers = [th.get_text(strip=True) for th in thead.find_all('th')]
        tbody = soup.find('tbody')
        if tbody:
            for row in tbody.find_all('tr'):
                cells = row.find_all('td')
                row_data = dict()

                for header, cell in zip(headers, cells):
                    if header:
                        if header == 'Equipment':
                            items = []
                            for item in cell.find_all('span', class_='item'):
                                title = item.get('title')
                                if title:
                                    items.append(title)
                                else:
                                    items.append("Empty slot")
                            row_data[header] = items
                        elif header == 'Stats':
                            stats = cell.find('span', class_='player-stats').text if cell.find('span', class_='player-stats') else None
                            row_data[header] = stats
                        elif header == 'Last seen':
                            last_seen = cell.find('span', class_='timeago')['title'] if cell.find('span', class_='timeago') else None
                            row_data[header] = last_seen
                        else:
                            row_data[header] = cell.get_text(strip=True)
                
                characters.append(
                    Character(
                        character_class=row_data['Class'],
                        level=row_data['L'],
                        fame=row_data['Fame'],
                        place=row_data['Pl.'],
                        items=row_data['Equipment'],
                        stats=row_data['Stats'],
                        last_seen=row_data.get('Last seen') if row_data.get('Last seen') is not None else None
                    )
                )

    return Player(
        name=name,
        description=description,
        characters_count=int(player_info.get('Characters')) if player_info.get('Characters') is not None else None,
        skins=int(player_info.get('Skins')) if player_info.get('Skins') is not None else None,
        exaltations=int(player_info.get('Exaltations')) if player_info.get('Exaltations') is not None else None,
        fame=int(player_info.get('Fame')),
        rank=int(player_info.get('Rank')),
        account_fame=int(player_info.get('Account fame')),
        guild=player_info.get('Guild'),
        guild_rank=player_info.get('Guild Rank'),
        first_seen=player_info.get('First seen'),
        created=player_info.get('Created'),
        last_seen=player_info.get('Last seen'),
        characters=characters if characters else None
    )