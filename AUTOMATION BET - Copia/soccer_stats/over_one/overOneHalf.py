import sys
sys.path.append(".")

from soccer_stats._contextual_averages import _ContextualAverages



def over_1_half():
    value = _ContextualAverages()._get_overOne
    return value
