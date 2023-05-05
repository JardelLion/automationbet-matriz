import sys
sys.path.append('.')
from soccer_stats.statsProbability import Statistic
from soccer_stats.last_result_game_4Games import LastResult4Games

stast = Statistic()
last4Games = LastResult4Games()

print(stast.frequency_over_goals_last4Games_home(2.5),
stast.frequency_over_goals_last4Games_away(2.5))
print(last4Games.getChange_home_score, 
last4Games.getChange_away_score)
print(stast.change_score_medianaLast4Games)
print(stast.frequency_under_goals_last4Games_away(2.5))
