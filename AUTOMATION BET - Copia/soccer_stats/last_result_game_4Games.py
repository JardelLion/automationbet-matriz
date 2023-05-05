import site
import sys
sys.path.append('.')

from soccer_stats._last_result_most_recent_first4Games  import LastResultMostRecentFirst
from math import floor

class LastResult4Games:
    """This class represent every information about the 4 games most
    recent first in the  league...
    """
    
    
    def __init__(self, site):
        self.site = site
        self.last_restul_most_recent = LastResultMostRecentFirst(site)
    
    def get_average(self, values_list):
        values = values_list

        
        
        number = 0
        for value in values:
            number += int(value)
            
        return number / len(values)
        
    @property
    def all_goals(self):
        
        values = self.last_restul_most_recent.all_goals()
        
        return values
    
    
    @property
    def get_home_average_scored(self):
        
        average = self.get_average(self.last_restul_most_recent.get_home_goals_scored())
       
        return average
    
    @property 
    def get_home_average_conceded(self):
        average = self.get_average(self.last_restul_most_recent.get_home_goals_conceded())
      
        return average
    
    
    @property
    def get_away_average_scored(self):
       average = self.get_average(self.last_restul_most_recent.get_away_goals_scored())
       
       
       return average
   
   
    @property
    def get_away_average_conceded(self):
       average = self.get_average(self.last_restul_most_recent.get_away_goals_conceded())
       
       return average

    # calcuting the change to home or away score in the game
    @property
    def getChange_home_score(self):
        change = (
            self.get_home_average_scored +
            self.get_away_average_conceded
        ) / 2


        return change
   
    @property
    def getChange_away_score(self):
        
        change = (
            self.get_home_average_conceded +
            self.get_away_average_scored
        ) / 2

       


        return change
   
    @property
    def home_list_goals_scored(self):
        return self.last_restul_most_recent.first_team_goals_scored_list()
    
    
    @property
    def home_list_goals_conceded(self):
        return self.last_restul_most_recent.first_team_goals_conceded_list()
    
    
    @property
    def away_list_goals_scored(self):
        return self.last_restul_most_recent.second_team_goals_scored_list()
    
    
    @property
    def away_list_goals_conceded(self):
        return self.last_restul_most_recent.second_team_goals_conceded_list()


