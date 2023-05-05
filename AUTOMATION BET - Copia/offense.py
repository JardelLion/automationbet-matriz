import sys
from urllib.request import parse_http_list
sys.path.append('.')
from beautifusoup_set.soup import get_soup
from soccer_stats.teams_names import first_team, second_team
from _offense_defense_shape import OffenseDefenseShape


table = get_soup().find_all("td", attrs={
    'align': 'center',
    'valign': 'middle',
    'style': 'margin:6px;'
})

offense = OffenseDefenseShape('OFFENSE', table)


    
def home_offense_goals():
    value = offense._first_team_points.get("points_goals")
    
    return int(value)

def away_offense_goals():
    value = offense._second_team_points.get("points_goals")
    
    return int(value)

