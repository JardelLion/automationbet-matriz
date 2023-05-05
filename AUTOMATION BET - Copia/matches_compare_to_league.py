import sys

from attr import attrs
sys.path.append(".")
from beautifusoup_set.soup import get_soup
from soccer_stats.convert_to_int import convert_to_int

table = get_soup().find_all('table', attrs={
    'width': '100%' ,
    'cellpadding':'2',
    "cellspacing":'0',
    'border':'0',
    'style':'margin-top:3px'
})

home_table = table[0].find_all('tr', attrs={
    'height':'24'
})[0]

away_table =  table[1].find_all('tr', attrs={
    'height':'24'
})[0]



home_value = convert_to_int(home_table.find('td', attrs={
        'align':'center',
        'width':'45'
    }).text)




away_value = convert_to_int(away_table.find('td', attrs={
        'align':'center',
        'width':'45'
    }).text)

 
def get_homeDraw_chance():
    return home_value

def get_awayDraw_chance():
    return away_value


def get_drawChange_game():
    value = ( home_value + away_value
        
    )

    return value


