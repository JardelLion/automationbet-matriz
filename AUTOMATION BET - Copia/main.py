import sys
from soccer_stats.statsProbability import LAST_REULT_GAME
sys.path.append(".")
# the site inicial must be soccer stats

from soccer_stats.teams_names import first_team, second_team
from soccer_stats.last_result_game import LastResulGame
from soccer_stats.btts.soccerBtts import bothTeamScoring
from soccer_stats.over_one.overOneHalf import over_1_half
from soccer_stats.over_two.overTwoHalf import over_2_half
from soccer_stats.avarage_scoring.average_scoring import ScoringStats
from soccer_stats.head2head import Head2Head
from soccer_stats.statsProbability import Statistic


last_result = LastResulGame()
stast = Statistic()
avarage_scoring = ScoringStats()
head2head = Head2Head()




def last_result_stast():
    PHARSE = 'MOST RECENT IN THE LEAGUE'
    print(f'  LASTEST RESULT IN THE LEAGUE IN {last_result.home_totals_game} GAMES')
    print(f'{PHARSE:^45}')
    print(f'{first_team().upper()}         VS            {second_team().upper()}')
    
    NAMES = ['TOTALS GAME',
             'WIN',
             'DRAW',
             'LOSE',
             'GOLS',
             'CONCEDED']
    
    last_result_table = [
        [last_result.home_totals_game, last_result.away_totals_game],
        [last_result.home_totals_game_win, last_result.away_totals_game_win],
        [last_result.home_totals_game_draw, last_result.away_totals_game_draw],
        [last_result.home_totals_game_lose, last_result.away_totals_game_lose],
        [last_result.home_totals_game_goals, last_result.away_totals_game_goals],
        [last_result.home_totals_game_conceded, last_result.away_totals_game_conceded]
    ]
    
    home = 0
    away = 1
    for pos in range(len(NAMES)):
        print(f" {last_result_table[pos][home]} {NAMES[pos]:^33} {last_result_table[pos][away]:>2}")
        
  
    
def contextual_avarages():
    avarages = [
        bothTeamScoring(),
        over_1_half(),
        over_2_half() 
    ]
    
    NAMES = ['BTTS',
             'OVER 1.5', 
             'OVER 2.5']
    
    
    for index in range(len(NAMES)):
        print(f"        {NAMES[index]:<14}{avarages[index]} %")
        
       
        
def avarage_scoring_match():
    avarage_scoring_list_home = [
        avarage_scoring.get_homeScoredPerMatch,
        avarage_scoring.get_homeConcededPerMatch,
        avarage_scoring.get_hasChangeGoalsHome,
        avarage_scoring.get_leagueAverageScoringHome,
    ]
    
    avarage_scoring_list_away = [
        avarage_scoring.get_awayScoredPerMatch,
        avarage_scoring.get_awayConcededPerMatch,
        avarage_scoring.get_hasChangeGoalsAway,
        avarage_scoring.get_leagueAverageScoringAway
    ]
    
    NAMES = [
        'SCORED PER MACTH',
        'CONCEDED PER MATCH',
        'HAS CHANGE GOLS',
        'LEAGUE AVERAGE SCORING'
    ]
    
    print(f'{first_team().upper()}          Goals          {second_team().upper()}')
    print(f' HOME                                    AWAY ')
    for index in range(len(NAMES)):
        print(f'{avarage_scoring_list_home[index]:^5}  {NAMES[index]:>23}  {avarage_scoring_list_away[index]:>12}')


def head_to_head():
    pharse = 'head to head'.upper()
    print(f'{first_team().upper():<14} {pharse:<18} {second_team().upper()}')
    
    head_lists_home = [
        head2head.get_home_xwin,
        head2head.get_home_xscored,
        head2head.get_home_scored_per_match,
        head2head.get_home_total_goals            
    ]
    
    head_lists_away  = [
        head2head.get_away_xwin,
        head2head.get_away_xscored,
        head2head.get_away_scored_per_match,
        head2head.get_away_total_goals,
    ]
    
    content_list = [
        'win','scored', 'scored per match',
        'total goals'
    ]
    head_average = [
        head2head.get_btts_scored,
        head2head.get_matches_over_one_half,
        head2head.get_matches_over_two_half,
        head2head.get_matches_over_three_half,
        head2head.get_draw_x
        
    ]
    
    content_list_average = [
        'btts scored', '1.5 over',
        '2.5 over', '3.5 over',
        'draw']
    for index, value in enumerate(head_lists_home):
        print(f"{head_lists_home[index]:<14} {content_list[index].upper():<25} {head_lists_away[index]}")
    
    
    for index, value in enumerate(content_list_average):
        print(f"{head_average[index]:<14} {content_list_average[index].upper():<25} {head_average[index]}")
    
    
def line():
    line =  40 * '-'
    print(line)
    



last_result_stast()
line()
contextual_avarages()
line()
avarage_scoring_match()

line()
head_to_head()