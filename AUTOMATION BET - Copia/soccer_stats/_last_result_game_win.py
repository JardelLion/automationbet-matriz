import sys


sys.path.append('.')
from _last_resut_shape import _LastResultGameShape



class _LastResultWin(_LastResultGameShape):
    
    _home_team = {
        'win': 0,
        'totals_conceded': 0, 
        'totals_goals': 0,
        'totals_game': 0,
        
        'away': {
            'win': 0,
            'totals_conceded': 0,
            'totals_goals': 0,
            'totals_game': 0
        },
        
        'goals': [],
        'conceded': []
    }


    _away_team = {
        'win': 0, 
        'totals_conceded': 0,
        'totals_goals': 0,
        'totals_game': 0,
        
        'home': {
            'win': 0,
            'totals_conceded': 0,
            'totals_goals': 0,
            'totals_game': 0
        },
        'goals': [],
        'conceded': []
    }
    
    _team_condition = ''
    
    def __init__(self, site):
        super().__init__("WIN", site)
        
        
        
    @property
    def get_home_team_playing_home_goals(self):
        return self._home_team['totals_goals']
    
    
    @property
    def get_home_team_playing_home_win(self):
        return self._home_team['win']
    
    @property
    def get_home_team_playing_home_conceded(self):
        return self._home_team['totals_conceded']
    
    
    @property
    def get_home_team_playing_away_goals(self):
        return self._home_team['away']['totals_goals']
    
    @property
    def get_home_team_playing_away_win(self):
        return self._home_team['away']['win']
    
    
    @property
    def get_home_team_playing_away_conceded(self):
        return self._home_team['away']['totals_conceded']
    
    
    
    @property
    def get_away_team_playing_home_goals(self):
        return self._away_team['home']['totals_goals']
    
    @property
    def get_away_team_playing_home_win(self):
        return self._away_team['home']['win']
    
    @property
    def get_away_team_playing_home_conceded(self):
        return self._away_team['home']['totals_conceded']
    
    
    
    @property
    def get_away_team_playing_away_goals(self):
        return self._away_team['totals_goals']
    
    
    @property
    def get_away_team_playing_away_win(self):
        return self._away_team['win']
    
    @property
    def get_away_team_playing_away_conceded(self):
        return self._away_team['totals_conceded']
    
    
    
    
    @property
    def get_away_lists_goals_scored(self):
        return self._away_team.get('goals')
    
    @property
    def get_home_lists_goals_scored(self):
        return self._home_team.get('goals')
    
    @property
    def get_home_lists_goals_conceded(self):
        return self._home_team.get('conceded')
    
    @property
    def get_away_lists_goals_conceded(self):
        return self._away_team.get("conceded")
    
    
