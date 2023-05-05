import sys

sys.path.append(".")

from beautifusoup_set.soup import get_soup
from _offense_defense_shape import OffenseDefenseShape

table = get_soup().find_all("td", attrs={
    'align': 'center',
    'valign': 'middle',
    'style': 'margin:6px;'
})

   
defense = OffenseDefenseShape('DEFENSE', table)


def home_defense_conceded_goals():
    value = defense._first_team_points.get("points_goals")
    
    return int(value)

def away_defense_conceded_goals():
    value = defense._second_team_points.get("points_goals")
    
    return int(value)
