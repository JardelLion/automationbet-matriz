import sys
sys.path.append(".")
from soccer_stats.statsProbability import Statistic
from soccer_stats.avarage_scoring.average_scoring import ScoringStats
from soccer_stats.head2head import Head2Head
from performance_teams import PerformanceTeam
from soccer_stats.btts.soccerBtts import bothTeamScoring
from scoring_rate.rate import ScoringRate
from math import ceil
from _last_result_most_recent_first8Games import get_change_media, get_away_change_to_score, get_home_change_to_score


scoring_stast = ScoringStats()
scoring_rate = ScoringRate()
stast = Statistic()
head = Head2Head()
performance = PerformanceTeam()



scoring_rate_check = ceil((scoring_rate.get_has_change_scoring_rate_away + 1 +
                    scoring_rate.get_has_change_scoring_rate_home + 1 ) / 2)


class Over2_5:
    """this class represent the method over 2.5 goals"""

    
    @property 
    def check_over_method(self):

        is_true = (
            self.performance_verify and
            self.change_goals_rate_verify and
            self.btts_contextual_average_verify and
            get_change_media() > 2.80
        )
        

        if is_true or get_change_media() > 2.70 and scoring_rate_check >= 85:
            return "The [ROBOT] recomend enter in [OVER 2.5 GOALS] in this match"
        

        return False



    @property
    def performance_verify(self):
        value = ceil((performance.get_home_change_score +
                        performance.get_away_change_score) / 2) + 1

        is_performance_valueable = value >= 50

        if is_performance_valueable:
            return True
        return False


    @property
    def change_goals_rate_verify(self):
    
        is_change_goals_valueable = scoring_rate_check > 70
       
        if is_change_goals_valueable:
            return True
        return False


    @property
    def btts_contextual_average_verify(self):
    
        is_btts_predic_valueable = bothTeamScoring() >= 55
        if is_btts_predic_valueable:
            return True
        

        return False