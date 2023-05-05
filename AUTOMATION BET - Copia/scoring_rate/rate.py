import sys
sys.path.append(".")

from beautifusoup_set.soup import get_soup

SCORING_RATE_HOME = 3
SCORING_RATE_AWAY = 4 
    
class ScoringRate:
    """This class have a purpose to give you an ideia of an avarage of
    scoring rate.
    """
    
    _home = {
        "scoring_rate_home": '0',
        'conceded_rate_home': '0',
        'hasChange_scoring_rate_home': '0',
        "average_scoring_rate_home": '0'
    }
    
    _away = {
        "scoring_rate_away": '0',
        'conceded_rate_away': '0',
        'hasChange_scoring_rate_away': '0',
        'average_scoring_rate_away': '0'
    }
    
    
    
    def __init__(self):
        self._set_scoring_rate_home()
        self._set_scoring_rate_away()
       
    
    
    def _set_scoring_rate_home(self):
        table = self._get_scoring_rate_table[SCORING_RATE_HOME].find_all("td",
                                                                         {'align':"center"})
        
        for index in range(len(table)):
            if index == 0:
                # Home rate scoring
                self._home['scoring_rate_home'] = table[index].get_text()
                
            elif index == 1:
                # away rate scoring(second team)
                self._away['conceded_rate_away'] = table[index].get_text()
                
            elif index == 2:
                # averages scoring rate home team
                # has a change to scoring rate
                self._home['hasChange_scoring_rate_home'] =int(
                    
                    (
                        self._transforming_int_number(self._home.get("scoring_rate_home")) +
                        self._transforming_int_number(self._away.get("conceded_rate_away"))
                    ) / 2
                )
                
            elif index == 3:
                # averages scoring rate league
                self._home['average_scoring_rate_home'] = (
                    self._transforming_int_number(table[index].get_text())
                )
                
                
                
    def _set_scoring_rate_away(self):
    
        table = self._get_scoring_rate_table[SCORING_RATE_AWAY].find_all("td",
                                                                        {'align':"center"})
    
        for index in range(len(table)):
            if index == 0:
                # Home rate scoring
                self._home['conceded_rate_home'] = table[index].get_text()
                
            elif index == 1:
                # away rate scoring(second team)
                self._away['scoring_rate_away'] = table[index].get_text()
                
            elif index == 2:
                # averages scoring rate home team
                # has a change to scoring rate
                self._away['hasChange_scoring_rate_away'] =int(
                    
                    (
                        self._transforming_int_number(self._home.get("conceded_rate_home")) +
                        self._transforming_int_number(self._away.get("scoring_rate_away"))
                    ) / 2
                )
                
            elif index == 3:
                # average league 
                self._away['average_scoring_rate_away'] = (
                    self._transforming_int_number(table[index].get_text())
                )
            
            
    def _transforming_int_number(self, text):
        value = ''
        for pos in range(len(text)):
            if text[pos] != '%':
                value += text[pos]
                
                
        return int(value)
            
                
        
        
            
                
            
            
        
    
    
    
    @property
    def _get_scoring_rate_table(self):
        table = get_soup().find_all("table",
                            {"cellspacing": "0",
                             "cellpadding": "0",
                             "bgcolor": "#cccccc",
                             'width': "99%",
                             "style":'margin-top:5px;'})
        
        return table
    
    
    @property
    def get_has_change_scoring_rate_home(self):
        value = self._home['hasChange_scoring_rate_home']
            
        return value
    
    @property
    def get_has_change_scoring_rate_away(self):
        
        value = self._away['hasChange_scoring_rate_away']
        
        return value
    