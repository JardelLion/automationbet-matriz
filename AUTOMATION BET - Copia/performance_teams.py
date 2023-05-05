import sys
sys.path.append('.')


from soccer_stats.convert_to_int import convert_to_int


class PerformanceTeam:
    """This class represent the last performance of team 
        the chance they have to score"""

    
    def __init__(self, site):
        self.site = site
        
        self.performance_team = site.find_all('table', attrs={
        'cellspacing': '0',
        'cellpadding': '2',
        'width': '100%'
        })


        self.table_performance_team = None
        


        for index in range(5, 10):
            p = self.performance_team[index].find_all('b')
            
            if len(p) == 6:
               
                self.table_performance_team = self.performance_team[index].find_all('b')
                break
        
    
            

        self.first_team = {
            'points':self.table_performance_team[0].get_text(),
            'goal_scored': self.table_performance_team[2].get_text(),
            'goal_conceded': self.table_performance_team[4].get_text()
            }

        self.second_team = {
            'points': self.table_performance_team[1].get_text(),
            'goal_scored': self.table_performance_team[3].get_text(),
            'goal_conceded': self.table_performance_team[5].get_text()
            }

    
    @property
    def get_home_change_score(self):

        if self.first_team.get('goal_scored') == '-':
            return 0
       
        value = convert_to_int(self.first_team.get('goal_scored'))
       
        return value
    
    
    @property
    def get_home_change_conceded(self):

        if self.first_team.get('goal_conceded') == '-':
            return 0
    
        value = convert_to_int(self.first_team.get('goal_conceded'))
        
        return value
    
    @property
    def get_home_change_make_points(self):

        if self.first_team.get("points") == '-':
            return 0
       
        value = convert_to_int(self.first_team.get("points"))
        
        return value
    
    @property
    def get_away_change_score(self):

        if self.second_team.get('goal_scored') == '-':
            return 0
    
        value = convert_to_int(self.second_team.get('goal_scored'))
    
        return value
    
    @property
    def get_away_change_conceded(self):

        if self.second_team.get("goal_conceded") == '-':
            return 0
        
        value = convert_to_int(self.second_team.get("goal_conceded"))
        
        return value
    
    @property
    def get_away_change_make_points(self):
        if self.second_team.get("points") == '-':
            return 0
            
        value = convert_to_int(self.second_team.get("points"))
        
        return value