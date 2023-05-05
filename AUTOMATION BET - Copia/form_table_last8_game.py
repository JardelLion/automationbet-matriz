from turtle import home
from _offense_defense_shape import OffenseDefenseShape
from beautifusoup_set.soup import get_soup
from soccer_stats.get_name_league import get_name

table = get_soup().find_all("td", attrs={
    'align': 'center',
    'valign': 'middle',
    'style': 'margin:6px;'
})


table_league = OffenseDefenseShape("FORM_TABLE", table)

def home_points_last8():
    value = table_league._first_team_points.get('points_goals')
    
    return value


def away_points_last8():
    value = table_league._second_team_points.get("points_goals")
    
    return value

def difference_points_last8():
    home = int(home_points_last8())
    away = int(away_points_last8())
    if home > away:
        return home - away
    elif away > home:
        return away - home

    return home - away

#print(home_points_last8())
#print(away_points_last8())
