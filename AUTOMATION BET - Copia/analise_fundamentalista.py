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
recent_paths = Path(r'C:\Users\JBXBILLIONS\Documents\BET\2023\\7-JULHO\\17').glob("**\*.html")

paths = []
for path in recent_paths:
    paths.append(path)
    



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
   
    
    
    
   
        
        
    
    if match.matriz_magico:
         print(f'                   {game}: league: {league}')
         print('==>> ', match.matriz_magico,  ' ', match.get_performance(), match.get_dateOfGame())
         TableResultPassed(site).show_statics()

    

    if match.matriz_primo:
         print(f'                   {game}: league: {league}')
         print('==>> ', match.matriz_primo,  ' ', match.get_performance(), match.get_dateOfGame())
         TableResultPassed(site).show_statics()
        
    
    if match.matriz_full:
        print(f'                   {game}: league: {league}')
       
        print('==>> ', match.matriz_full,  ' ', match.get_performance())#, match.get_dateOfGame())
        TableResultPassed(site).show_statics()

