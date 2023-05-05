import sys

sys.path.append('.')

# This class represent every date of two team win lose,
#goals, conceded and how many goals they play

from soccer_stats._last_result_game_draw import _LastResultDraw
from soccer_stats._last_result_game_lose import _LastResultLose
from soccer_stats._last_result_game_win import _LastResultWin


class LastResulGame:
    
    def __init__(self, site):
        self.site = site
        _draw = _LastResultDraw(site)
        _win = _LastResultWin(site)
        _lose = _LastResultLose(site)
    

    
    @property
    def home_totals_game_win(self):
        value = (
            self._win.get_home_team_playing_home_win + self._win.get_home_team_playing_away_win
            
        )
        
        return value
    
    @property
    def home_totals_game_lose(self):
        value = (
           self._lose.get_home_team_playing_home_lose +
            self._lose.get_home_team_playing_away_lose
        )
        return value
    
    @property
    def home_totals_game_draw(self):
        value = (
            self._draw.get_home_team_playing_home_draw +
            self._draw.get_home_team_playing_away_draw
        )
        return value
    
    
    @property
    def home_totals_game_goals(self):
        value = (
            self._win.get_home_team_playing_home_goals +
            self._win.get_home_team_playing_away_goals +
            
            self._draw.get_home_team_playing_home_goals +
            self._draw.get_home_team_playing_away_goals +
            
            self._lose.get_home_team_playing_home_goals + 
            self._lose.get_home_team_playing_away_goals
        )
        
        return value
    
    
    @property
    def home_totals_game_conceded(self):
        
        value = (
            self._win.get_home_team_playing_home_conceded +
            self._win.get_home_team_playing_away_conceded +
            
            self._draw.get_home_team_playing_home_conceded +
            self._draw.get_home_team_playing_away_conceded +
            
            self._lose.get_home_team_playing_home_conceded + 
            self._lose.get_home_team_playing_away_conceded
        )
         
        return value
    
    
    @property
    def home_totals_game(self):
        value = (
            self._win.get_home_team_playing_home_win +
            self._win.get_home_team_playing_away_win + 
            
            self._draw.get_home_team_playing_home_draw +
            self._draw.get_home_team_playing_away_draw + 
            
            
            self._lose.get_home_team_playing_home_lose +
            self._lose.get_home_team_playing_away_lose
        )
        
        return value
    
    @property
    def home_lists_goals_scored(self):
        values = (self._win.get_home_lists_goals_scored, 
                  self._draw.get_home_lists_goals_scored,
                  self._lose.get_home_lists_goals_scored)
        lists_goals = []
        for numbers in values:
            for number in numbers:
                lists_goals.append(number)
                
        return sorted(lists_goals)
    
    @property
    def home_lists_goals_conceded(self):
        values = (self._win.get_home_lists_goals_conceded, 
                  self._draw.get_home_lists_goals_conceded,
                  self._lose.get_home_lists_goals_conceced)
        lists_goals = []
        for numbers in values:
            for number in numbers:
                lists_goals.append(number)
                
        return sorted(lists_goals)
    
        
    
    
    @property
    def away_totals_game_win(self):
        
        value = (
            self._win.get_away_team_playing_home_win +
            self._win.get_away_team_playing_away_win
        )
        
        return value
    
    
    @property
    def away_totals_game_lose(self):
        value = (
            self._lose.get_away_team_playing_away_lose +
            self._lose.get_away_team_playing_home_lose
        )
        
        
        return value
    
    
    @property
    def away_totals_game_draw(self):
        value = (
            self._draw.get_away_team_playing_home_draw +
            self._draw.get_away_team_playing_away_draw
        )
        
        return value
    
    @property
    def away_totals_game_goals(self):
        value = (
            self._win.get_away_team_playing_away_goals +
            self._win.get_away_team_playing_home_goals +
            
            self._draw.get_away_team_playing_away_goals +
            self._draw.get_away_team_playing_home_goals +
            
            self._lose.get_away_team_playing_away_goals +
            self._lose.get_away_team_playing_home_goals
        )
        
        return value
    @property
    def away_lists_goals_scored(self):
        values = (self._win.get_away_lists_goals_scored, 
                  self._draw.get_away_lists_goals_scored,
                  self._lose.get_away_lists_goals_scored)
        lists_goals = []
        for numbers in values:
            for number in numbers:
                lists_goals.append(number)
                
        return sorted(lists_goals)
    
    @property
    def away_lists_goals_conceded(self):
        values = (self._win.get_away_lists_goals_conceded, 
                  self._draw.get_home_lists_goals_conceded,
                  self._lose.get_home_lists_goals_conceced)
        lists_goals = []
        for numbers in values:
            for number in numbers:
                lists_goals.append(number)
                
        return lists_goals #sorted(lists_goals)
                
        
    
    
    @property
    def away_totals_game_conceded(self):
        value = (
            self._win.get_away_team_playing_away_conceded +
            self._win.get_away_team_playing_home_conceded +
            
            self._draw.get_away_team_playing_away_conceded +
            self._draw.get_away_team_playing_home_conceded +
            
            self._lose.get_away_team_playing_away_conceded +
            self._lose.get_away_team_playing_home_conceded
        )
        
      
        return value
    
    
    @property
    def away_totals_game(self):
        value = (
            self._win.get_away_team_playing_home_win +
            self._win.get_away_team_playing_away_win + 
            
            self._draw.get_away_team_playing_home_draw +
            self._draw.get_away_team_playing_away_draw + 
            
            
            self._lose.get_away_team_playing_home_lose +
            self._lose.get_away_team_playing_away_lose
        )
        
        return value
    
    @property
    def all_goals(self):
        values = (self._win._get_team_goals,
                  self._lose._get_team_goals,
                  self._draw._get_team_goals)
        
        goals =[]
        for numbers in values:
            for number in numbers:
                goals.append(number)
                
        return goals
    
    
