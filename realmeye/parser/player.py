from bs4 import BeautifulSoup
from realmeye.models import Player

def parse_player_data(html_data) -> Player:
    soup = BeautifulSoup(html_data, 'html.parser')
    
    name = soup.find("span", class_="entity-name").get_text()

    description = soup.find("div", class_="well description").find_all("div", class_="description-line")
    description = [line.get_text() for line in description]

    summary_table = soup.find("table", class_="summary")
    player_info = {}

    for tr in summary_table.find_all("tr"):
        key = tr.find_all("td")[0].text.strip()
        value_td = tr.find_all("td")[1]

        if value_td.find("a"):
            value = value_td.find("a").text.strip()
        elif value_td.find("span"):
            value = value_td.find("span").text.strip()
        elif value_td.find("div"):
            value = value_td.get_text(separator=" ", strip=True)
        else:
            value = value_td.text.strip()
        player_info[key] = value

    return Player(
        name=name,
        description=description,
        characters_count=int(player_info['Characters']),
        skins=int(player_info['Skins']),
        exaltations=int(player_info['Exaltations']),
        fame=int(player_info['Fame']),
        rank=int(player_info['Rank']),
        account_fame=int(player_info['Account fame']),
        guild=player_info['Guild'],
        guild_rank=player_info['Guild Rank'],
        first_seen=player_info['First seen'],
        last_seen=player_info['Last seen']
    )