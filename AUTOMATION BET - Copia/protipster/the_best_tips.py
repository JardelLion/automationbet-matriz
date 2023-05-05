import sys
sys.path.append('.')
from beautifusoup_set.soup import get_soup



best_tip = get_soup().find_all("span",
                           attrs={
                               'class': 'flex'
                           })


best_tips_point = best_tip[16].get_text().strip()
point_number = best_tips_point[-4:].strip()

list_tips_table = [{
    
    'high_odds_table': get_soup().find("div", attrs={
            'id': 'highOdds',
            'class': 'pt-2'
        }),

        'from_tips_table': get_soup().find("div", attrs={
            'id': 'streak',
            'class': 'pt-2'
        }),

        'team_win_table': get_soup().find("div", attrs={
            'id': 'teamToWin',
            'class': 'pt-2'
        }),

        'goal_market_table': get_soup().find("div", attrs={
            'id': 'goalMarkets',
            'class': 'pt-2'
        }),

        'bettins_tips_table': get_soup().find("div", attrs={
            'id': 'other',
            'class': 'pt-2'
        })
        
    }
]


def get_best_tips(values):
   
    for table in values:
        for key, value in table.items():
            tips_score = value.find_all("span", attrs={
                'class': 'score'
            })
            tips_recomend = value.find_all('p', attrs={
                'class': 'cursor-pointer'
            })
            
                
            if len(tips_score) == len(tips_recomend):
               for index, v in enumerate(tips_score):
                   point_score = tips_score[index].find("span", attrs={
                       'class': 'font-bold'
                   }).get_text().strip()
                   
                   if point_score == point_number:
                    print(tips_recomend[index].get_text().strip(), point_score)
            
         

get_best_tips(list_tips_table)
