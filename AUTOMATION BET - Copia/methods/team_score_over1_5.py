from asyncio import FIRST_COMPLETED
from distutils.command.build_scripts import first_line_re
import sys
from turtle import home
sys.path.append('.')
from performance_teams import PerformanceTeam
from soccer_stats.head2head import Head2Head
from soccer_stats.statsProbability import Statistic
from soccer_stats.teams_names import first_team, second_team
from scoring_rate.rate import ScoringRate
from _last_result_most_recent_first8Games import get_home_change_to_score, get_away_change_to_score



stast = Statistic()
performance = PerformanceTeam()
head_to_head = Head2Head()
scoring_rate = ScoringRate()

def score_more(team):
    if team == 'home'.lower():
        if get_home_change_to_score() > get_away_change_to_score():
            return True
        return False

    elif team =='away'.lower():
        if get_away_change_to_score() > get_home_change_to_score():
            return True

        return False


def is_home():
    
    is_valueable = (
        score_more('home') and
        get_home_change_to_score() > 1.70 and
        stast.get_change_home_score_mediana_headTohead >= 1 and
        scoring_rate.get_has_change_scoring_rate_home >= 60 and
        performance.get_home_change_score > 55
       
        
    )
    

    if is_valueable:
        return True

    return False

  
def is_away():
    
    is_valueable = (
        score_more('away') and 
        get_away_change_to_score() > 1.70 and
        stast.get_change_away_score_mediana_headTohead >= 1 and
        scoring_rate.get_has_change_scoring_rate_away >= 60 and
        performance.get_away_change_score > 55
    )
    

    if is_valueable:
        return True

    return False



class TeamScoreOver1_5:
    """this class represen if the team score over 1.5 goals"""


    @property
    def check_team(self):

        if is_home():
            return f'The [ROBOT] Recommend enter in [{first_team().upper()} OVER 1,5 GOALS]'

        elif is_away():
            return f'The [ROBOT] Recommend enter in [{second_team().upper()} OVER 1,5 GOALS]'

        return False

