# tests/test_parser.py
import pytest
from realmeye.parser import parse_player_data

def test_parse_player_data():
    # Sample HTML data
    sample_html = """
    <html>
        <h1>
            <span class="entity-name">KatsFan</span>
        </h1>
        <div class="row">
            <div class="col-md-5">
                <table class="summary">
                <tr>
                    <td>Characters</td>
                    <td>8</td>
                </tr>
                <tr>
                    <td>Skins</td>
                    <td>
                    <span class="numeric">40</span> (32494 <sup>th</sup>)
                    </td>
                </tr>
                <tr>
                    <td>Exaltations</td>
                    <td>
                    <span class="numeric">8</span>
                    </td>
                </tr>
                <tr>
                    <td>Fame</td>
                    <td>
                    <span class="numeric">16108</span> (7492 <sup>nd</sup>)
                    </td>
                </tr>
                <tr>
                    <td>Rank</td>
                    <td>
                    <div class="star-container">51 <div class="star star-red"></div>
                    </div>
                    </td>
                </tr>
                <tr>
                    <td>Account fame</td>
                    <td>
                    <span class="numeric">108005</span> (4348 <sup>th</sup>)
                    </td>
                </tr>
                <tr>
                    <td>Guild</td>
                    <td>
                    <a href="/guild/TowerJanitors">TowerJanitors</a>
                    </td>
                </tr>
                <tr>
                    <td>Guild Rank</td>
                    <td>Initiate</td>
                </tr>
                <tr>
                    <td>First seen</td>
                    <td>~6 years and 289 days ago</td>
                </tr>
                <tr>
                    <td>Last seen</td>
                    <td>
                    <span class="timeago" title="2024-01-18T15:15:09Z">2024-01-18 15:15:09</span> as Priest
                    </td>
                </tr>
                </table>
            </div>
            <div class="col-md-7">
                <div class="well description" id="d">
                <div class="line1 description-line">Hello!</div>
                <div class="line2 description-line">I play on Steam</div>
                <div class="line3 description-line">I took a break, came back and urgles are still annoying</div>
                </div>
            </div>
        </div>
    </html>
    """

    # Parse the sample HTML
    player = parse_player_data(sample_html)

    # Assertions
    assert player.name == "KatsFan"
    assert player.characters_count == 8
    assert player.description == ['Hello!', 'I play on Steam', 'I took a break, came back and urgles are still annoying']
    assert player.characters_count == 8
    assert player.skins == 40
    assert player.exaltations == 8
    assert player.fame == 16108
    assert player.rank == 51
    assert player.account_fame == 108005
    assert player.guild == 'TowerJanitors'
    assert player.guild_rank == 'Initiate'
    assert player.first_seen == '~6 years and 289 days ago'
    assert player.last_seen == '2024-01-18 15:15:09'
    assert player.characters == None