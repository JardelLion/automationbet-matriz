from operator import index
from os import W_OK
from pprint import pp
import sys

from attr import attrs
sys.path.append('.')
from beautifusoup_set.soup import get_soup

table = get_soup().find('table', attrs={
    'id': 'btable', 'cellpadding': '2',
    'cellspacing': '0', 'width': '100%'
})


tables = get_soup().find_all('tr', attrs={
    'class': 'odd', 'height': '28'
    
})
names = []
GP = []
W = []
D = []
L = []
GF = []
GA = []

for t in tables:
    name = t.find('td', attrs={
    'align': 'left'
        })
    
    points = t.find_all('td', attrs={
    'align': 'center'
        })
    

    names.append(name)
    GP.append(points[1])
    W.append(points[2])
    D.append(points[3])
    L.append(points[4])
    GF.append(points[5])
    GA.append(points[6])
   



list_names = []
list_gp = []
list_w = []
list_d = []
list_l = []
list_gf = []
list_ga = []

for index, name in enumerate(names):
    value = name.get_text().strip(),
    totals_game = GP[index].get_text().strip(),
    win = W[index].get_text().strip(), 
    lose = L[index].get_text().strip(),
    draw = D[index].get_text().strip(), 
    goal_for = GF[index].get_text().strip(), 
    goal_aganist = GA[index].get_text().strip(), 

    list_names.append(value)
    
    list_gp.append(totals_game)
    list_w.append(win)
    list_d.append(draw)
    list_l.append(lose)
    list_gf.append(goal_for)
    list_ga.append(goal_aganist)


def names_list():
    return list_names

def draws():
    return list_d

def wins():
    return list_w

def loses():
    return list_l

def goals_for():
    return list_gf

def goals_aganist():
    return list_ga


def games_number():
    return list_gp

