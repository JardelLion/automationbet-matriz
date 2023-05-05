import sys
sys.path.append(".")

from _offense_defense_shape import OffenseDefenseShape
from beautifusoup_set.soup import get_soup

table = get_soup().find_all("td", attrs={
    'align': 'center',
    'valign': 'middle',
    'style': 'margin:6px;'
})

table_league = OffenseDefenseShape("TABLE_LEAGUE", table)

def home_points():
    value = table_league._first_team_points.get('points_goals')
    
    return value


def away_points():
    value = table_league._second_team_points.get("points_goals")
    
    return value





