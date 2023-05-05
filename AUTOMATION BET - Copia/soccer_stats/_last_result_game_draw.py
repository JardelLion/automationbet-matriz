import sys

sys.path.append('.')
from _last_resut_shape import _LastResultGameShape


    
class _LastResultDraw(_LastResultGameShape):
    
    # This represent the team date that how many and win the game
    
    
    
    _home_team = {
        'draw': 0,
        'totals_conceded': 0, 
        'totals_goals': 0,
       
        
        'away': {
            'draw': 0,
            'totals_conceded': 0,
            'totals_goals': 0,
           
        },
        'goals': [],
        'conceded': []
    }


    _away_team = {
        'draw': 0, 
        'totals_conceded': 0,
        'totals_goals': 0,
        
        
        'home': {
            'draw': 0,
            'totals_conceded': 0,
            'totals_goals': 0,
            
        },
        'goals': [],
        'conceded': []
    }
    
    _team_condition = ''

    
    def __init__(self, site):
       super().__init__('DRAW', site)
      
        
    
        
    @property
    def get_home_team_playing_home_goals(self):
        return self._home_team['totals_goals']
    
    
    @property
    def get_home_team_playing_home_draw(self):
        return self._home_team['draw']
    
    @property
    def get_home_team_playing_home_conceded(self):
        return self._home_team['totals_conceded']
    
    
    @property
    def get_home_team_playing_away_goals(self):
        return self._home_team['away']['totals_goals']
    
    @property
    def get_home_team_playing_away_draw(self):
        return self._home_team['away']['draw']
    
    
    @property
    def get_home_team_playing_away_conceded(self):
        return self._home_team['away']['totals_conceded']
    
    
    
    @property
    def get_away_team_playing_home_goals(self):
        return self._away_team['home']['totals_goals']
    
    @property
    def get_away_team_playing_home_draw(self):
        return self._away_team['home']['draw']
    
    @property
    def get_away_team_playing_away_draw(self):
        return self._away_team['draw']
    
    @property
    def get_away_team_playing_home_conceded(self):
        return self._away_team['home']['totals_conceded']
    
    
    
    @property
    def get_away_team_playing_away_goals(self):
        return self._away_team['totals_goals']
    
    
    @property
    def get_away_team_playing_away_conceded(self):
        return self._away_team['totals_conceded']
    
    @property
    def get_away_lists_goals_scored(self):
        return self._away_team.get("goals")
    
    @property
    def get_home_lists_goals_scored(self):
        return self._home_team.get('goals')
    
    @property
    def get_home_lists_goals_conceded(self):
        return self._home_team.get("conceded")
    
    
    @property
    def get_away_lists_gols_conceded(self):
        return self._away_team.get('conceded')


