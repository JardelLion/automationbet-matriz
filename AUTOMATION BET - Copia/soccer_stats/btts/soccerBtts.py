import sys
sys.path.append('.')
from soccer_stats._contextual_averages import _ContextualAverages

def bothTeamScoring():
    btts = _ContextualAverages()._get_btts
    
    return btts

