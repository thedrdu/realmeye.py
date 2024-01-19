from realmeye.parser import parse_player_data

def test_parse_player_data_1():
    """Test case for user KatsFan."""
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

    player = parse_player_data(sample_html)

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
    assert player.created is None
    assert player.last_seen == '2024-01-18 15:15:09 as Priest'
    assert player.characters is None

def test_parse_player_data_2():
    """Test case for user Lollynick."""
    sample_html = """
    <html>
        <h1>
            <span class="entity-name">Lollynick</span>
        </h1>
        <div class="row">
            <div class="col-md-5">
            <table class="summary">
                <tr>
                <td>Characters</td>
                <td>5</td>
                </tr>
                <tr>
                <td>Skins</td>
                <td>
                    <span class="numeric">60</span> (17018 <sup>th</sup>)
                </td>
                </tr>
                <tr>
                <td>Exaltations</td>
                <td>
                    <span class="numeric">79</span>
                </td>
                </tr>
                <tr>
                <td>Fame</td>
                <td>
                    <span class="numeric">1787</span> (19790 <sup>th</sup>)
                </td>
                </tr>
                <tr>
                <td>Rank</td>
                <td>
                    <div class="star-container">56 <div class="star star-orange"></div>
                    </div>
                </td>
                </tr>
                <tr>
                <td>Account fame</td>
                <td>
                    <span class="numeric">616994</span> ( <a href="/top-players-by-account-fame/301">396 <sup>th</sup>
                    </a>)
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
                <td>Leader</td>
                </tr>
                <tr>
                <td>Created</td>
                <td>~11 years and 34 days ago</td>
                </tr>
                <tr>
                <td>Last seen</td>
                <td>hidden</td>
                </tr>
            </table>
            </div>
            <div class="col-md-7">
            <div class="well description" id="d">
                <div class="line1 description-line">gKYdTzvrUOTr8Kdh0Be0</div>
                <div class="line2 description-line"></div>
                <div class="line3 description-line"></div>
            </div>
            </div>
        </div>
    </html>
    """

    player = parse_player_data(sample_html)

    assert player.name == "Lollynick"
    assert player.characters_count == 5
    assert player.description == ['gKYdTzvrUOTr8Kdh0Be0', '', '']
    assert player.skins == 60
    assert player.exaltations == 79
    assert player.fame == 1787
    assert player.rank == 56
    assert player.account_fame == 616994
    assert player.guild == 'TowerJanitors'
    assert player.guild_rank == 'Leader'
    assert player.first_seen is None
    assert player.created == '~11 years and 34 days ago'
    assert player.last_seen == 'hidden'
    assert player.characters is None