from multiprocessing.sharedctypes import Value
import sys
sys.path.append('.')

from soccer_stats.head2head import Head2Head
from soccer_stats.statsProbability import Statistic
from scoring_rate.rate import ScoringRate
from performance_teams import PerformanceTeam
from _last_result_most_recent_first8Games import get_change_media
from math import ceil

headTohead = Head2Head()
stast = Statistic()
scoring_rate = ScoringRate()
performance = PerformanceTeam()


class Under2_5:
    """This class represent the method under 2.5 and under 3 goals in the match"""

    _head_to_head_number_games = (
        headTohead.get_draw_x +
        headTohead.get_away_xwin +
        headTohead.get_home_xwin
        )

    _scoring_rate_totals = ceil((scoring_rate.get_has_change_scoring_rate_away + 2 +
            scoring_rate.get_has_change_scoring_rate_home
        ) / 2)

    @property
    def check_under(self):
        is_true = (
            self.medianaHeadToHead_verify and
            self.medianaLast4Games_verify and
            self.performance_verify and
            self.scoring_rate_verify < 79 and
            get_change_media() < 1.50
        )
        
        if is_true :
            return "The [ROBOT] Recommend enter in [UNDER 2,5 GOALS] in this match"

        return False

    @property
    def performance_verify(self):
        value = (
            performance.get_home_change_score +
            performance.get_away_change_score
        ) / 2 <= 60

        return value


    @property
    def medianaLast4Games_verify(self):
        value = (
            stast.change_score_medianaLast4Games <= 2.25
        )

        return value

    @property
    def medianaHeadToHead_verify(self):
        value = (
            stast.get_changeScoredMediana_headTohead <= 2 and
            self._head_to_head_number_games >= 3
        )

        return value

    @property
    def scoring_rate_verify(self):
        value = self._scoring_rate_totals


        return value
