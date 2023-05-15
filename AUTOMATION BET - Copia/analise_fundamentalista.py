from msilib.schema import Error
import sys
from time import sleep
from os import system


sys.path.append('.')

from soccer_stats.teams_names import Team
from methods.match_odds import MatchOdds
#from backteste import create_sheet
from bs4 import BeautifulSoup
from access.get_access import access
from pathlib import Path
from soccer_stats.get_name_league import get_name
from soccer_stats.table_result_passed import TableResultPassed

#tHE PRINCIPAL AUTOMATION BET
recent_paths = Path(r'C:\Users\JBXBILLIONS\Documents\BET\2023\\5-MAIO\\20tt').glob("**\*.html")

paths = []
for path in recent_paths:
    paths.append(path)
    

league_not_allowed_draw_normal = [
        'argentina - primera nacional',
        'argentina - primera c - apertura',
        'japan - j1 league',
        'japan - j2 league',
        'japan - j3 league'
        ]

ARGETINA_NOT_ALLOWED = [
    'argentina - primera nacional',
    'france - national',
    'italy - serie d - group d',
    'portugal - liga portugal 2'
]

KOREA_NOT_ALLOWED = [
    'south korea - k league 1',
    'south korea - k league 2',
    'south korea - k3 league'

]

print("staring")
for pos, file in enumerate(paths):

    file_string = str(file).replace(' ', '%20')
    file_string = 'file:///' + file_string

    site = BeautifulSoup(access(file_string), "html.parser")
    
    
   
    
    
    team = Team(site)
    match = MatchOdds(site)

  


    game = f'{team.first_team().upper()} vs {team.second_team().upper()}'
    league = get_name(site).upper()

    print(f'                   {game} Performance: {match.get_performance()}')
   
    
    
    
    # if match.check_draw_35 and league not in ARGETINA_NOT_ALLOWED and league not in KOREA_NOT_ALLOWED:
    #     print(f"                   {game}: league: {league} {match.get_performance()}")
    #     print('==>> ', match.check_draw_35,  ' ', match.get_performance(), match.get_dateOfGame())
    #     TableResultPassed(site).show_statics()
      
    # if match.check_under1_half and league.lower() not in ARGETINA_NOT_ALLOWED:
    #     print(f'                   {game}: league: {league}')
    #     print('==>> ', match.check_under1_half,  ' ', match.get_performance(), match.get_dateOfGame())
    #     TableResultPassed(site).show_statics()
        
        
    
    if match.matriz_magico:
        print(f'                   {game}: league: {league}')
        print('==>> ', match.matriz_magico,  ' ', match.get_performance(), match.get_dateOfGame())
        TableResultPassed(site).show_statics()

    

    # if match.under_1_5_primo:
    #     print(f'                   {game}: league: {league}')
    #     print('==>> ', match.under_1_5_primo,  ' ', match.get_performance(), match.get_dateOfGame())
    #     TableResultPassed(site).show_statics()



    if match.matriz_primo:
        print(f'                   {game}: league: {league}')
        print('==>> ', match.matriz_primo,  ' ', match.get_performance(), match.get_dateOfGame())
        TableResultPassed(site).show_statics()

    
    
    
    
    # else:
        
    #     if match.check_draw and league not in league_not_allowed_draw_normal:
    #         if match.analize_probability_to_draw_performance == 16:
    #             print(f'                   {game}: league: {league}')
    #             print('==>> ', match.check_draw, ' ', match.get_performance(), match.get_dateOfGame())
    #             TableResultPassed(site).show_statics()
    
