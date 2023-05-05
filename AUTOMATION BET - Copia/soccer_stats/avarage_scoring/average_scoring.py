import sys
sys.path.append(".")


# home
class ScoringStats:
    
    
    home = {
        'scoredPerMatch': '0',
        'concededPerMatch': '0',
        'hasChangeHome': '0',
        'leagueAverageScoringHome': '0'
    }
    
    away = {
            'scoredPerMatch': '0',
            'concededPerMatch': '0',
            'hasChangeAway': '0',
            'leagueAverageScoringAway': '0'
    }
   

    
    def __init__(self, site):
        self.site = site
        self._set_value_dict()
        
       
    
    def _get_table_home_scoring(self):
        table = self.site.find_all('table', {'cellspacing': '0',
                                        'cellpadding': '0',
                                        'width': "99%",
                                        'style': 'margin-top:5px;'})
        
        return table 
    
    
    
    def _set_value_dict(self):
        POSITION = 2
        for pos in range(POSITION):
            table_value = self._get_table_home_scoring()[pos].find_all("td", {'align': 'center'})
            if pos == 0:
                # home scoring date
                
                for index in range(len(table_value)):
                    value = table_value[index].get_text()
    
                    if index == 0:
                        # Avarage home time goals
                        self.home['scoredPerMatch'] = value
                        
                    elif index == 1:
                        # Avarage away time conceded goals
                        self.away['concededPerMatch'] = value
            
                    elif index == 3:
                        # Avarage of league teams scoring at home
                        self.home['leagueAverageScoringHome'] = value
                        
                    else:
                        continue 
               
            elif pos == 1:
                # away scoring date
                for index in range(len(table_value)):
                
                    value = table_value[index].get_text()
                
                    if index == 0:
                        # Avarage home time goals
                        self.home['concededPerMatch'] = value
                        
                    elif index == 1:
                        # Avarage away time conceded goals
                        self.away['scoredPerMatch'] = value
                        
                        
                    elif index == 3:
                        # Avarage of league teams scoring at home
                        self.away['leagueAverageScoringAway'] = value 
                        
                    else:
                        continue
                
                    
        self._posibilityScoringHome()
        self._posibilityScoringAway()
                    
        
            

            
    def _posibilityScoringHome(self):
        value = (self.get_homeScoredPerMatch + self.get_awayConcededPerMatch) / 2
        self.home['hasChangeHome'] = value
            
    def _posibilityScoringAway(self):
        value = (self.get_awayScoredPerMatch + self.get_homeConcededPerMatch) / 2
        self.away['hasChangeAway'] = value
        
            
                    
    
    
    
    
    @property
    def get_homeScoredPerMatch(self):
        return float(self.home['scoredPerMatch'])
    
    
    @property
    def get_homeConcededPerMatch(self):
        return float(self.home['concededPerMatch'])
    
    
    @property
    def get_leagueAverageScoringHome(self):
        return float(self.home['leagueAverageScoringHome'])
    
    
    
    @property
    def get_awayScoredPerMatch(self):
        return float(self.away['scoredPerMatch'])
    
    @property
    def get_awayConcededPerMatch(self):
        return float(self.away['concededPerMatch'])
    
    
    @property
    def get_leagueAverageScoringAway(self):
        return float(self.away['leagueAverageScoringAway'])
    
    @property
    def get_hasChangeGoalsHome(self):
        return float(self.home['hasChangeHome'])
    
    @property
    def get_hasChangeGoalsAway(self):
        return float(self.away['hasChangeAway'])

    @property
    def get_hasChangeGoalsGame(self):
        value = self.get_hasChangeGoalsAway + self.get_hasChangeGoalsHome

        return value
