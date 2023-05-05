import sys
sys.path.append('.')

from soccer_stats.teams_names import first_team, second_team

class OffenseDefenseShape:
    
    """Class that represent the date of deffense and offense points"""
    
    _table_league = 0
    _form_table = 1
    _defense = -1
    _offense = -2
    
    
    
    
    _first_team_points = {
        'points_goals': '0' 
    }


    _second_team_points = {
       'points_goals': '0' 
    }
    
    
    
    def __init__(self, type_condition, table):
        self._type_condition = type_condition
        self._table = table
        
        
        if self._type_condition == 'OFFENSE':
            # OFFENSE CONDITION
            self._set_condition_type(self._offense)
            
            self.add_value(self.first,
                           self.second)

        
        if self._type_condition == 'DEFENSE':
            # DEFENSE CONDITION
            
            self._set_condition_type(self._defense)
            
            self.add_value(self.first,
                           self.second)
            
        
        if self._type_condition == 'TABLE_LEAGUE':
            # TABLE_LEAGUE CONDITION
            
            self._set_condition_type(self._table_league)
            
            self.add_value(self.first,
                           self.second)
            
        if self._type_condition == 'FORM_TABLE':
            # TABLE LAST 8 GAME CONDITION
            
            self._set_condition_type(self._form_table)
            
            self.add_value(self.first,
                           self.second)
            
            
            
            
    def _set_condition_type(self, condition):
        
        self.first = self._table[condition].find("tr", attrs={
                'class': 'trow7'
                 })

        self.second = self._table[condition].find("tr", attrs={
                'class': 'trow5'
                })

        
        
        
    
    def add_value(self, first_value, second_value):
        
        date_first_offense_table = first_value.find_all('td')
        date_second_offense_table = second_value.find_all('td')
       
        
        if len(date_first_offense_table) == len(date_second_offense_table):
            
            if self._verifying_name(date_first_offense_table[1].text.lower(), first_team()):
                    # first team offense
              
                self._first_team_points['points_goals'] = date_first_offense_table[-2].get_text().strip()
                
           
            if self._verifying_name(date_second_offense_table[1].text.lower(), second_team()):
                # second team offense
                self._second_team_points['points_goals'] = date_second_offense_table[-2].get_text().strip()
    
    
    def _verifying_name(self, name, team):
        names = name.split(' ')
        
        for value_name in names:
            if value_name in team.lower():
                return True

        return False
