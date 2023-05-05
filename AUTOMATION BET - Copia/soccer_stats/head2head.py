from ast import In
from email import message
from ssl import SOCK_STREAM
import sys
sys.path.append(".")


from soccer_stats.teams_names import Team
from soccer_stats._head2head_last_game import head2head_all_goals
from soccer_stats._head2head_last_game import head2head_get_away_goals
from soccer_stats._head2head_last_game import head2head_get_home_goals
from soccer_stats._head2head_last_game import home_average_goals_scored
from soccer_stats._head2head_last_game import away_average_goals_scored
from soccer_stats.convert_to_int import convert_to_int
from soccer_stats.get_name_league import get_name
   
    


class Head2Head:
    # This class represent the confort that happend for this two team
    
    # h2h (head 2 head)

    _market_dict = {}



    def  __init__(self, site):
        self.site = site
        self.team = Team(site)

        try:
            _tables = self.site.find_all("table", {"cellspacing":'0', 'cellpadding': '2', 
                                            'width': '100%'
                                })[6]

            if get_name(self.site) == 'serie b'.lower():
                _tables = self.site.find_all("table", {"cellspacing":'0', 'cellpadding': '2', 
                                'width': '100%'
                        })[5]
                            

            self._table = _tables.find('table', attrs={
                                'cellspacing': '0', 
                                'cellpadding': '0',
                                'width': '100%'
                            })

            self._values = self._table.find_all('td',
                        {"style": "padding-left:20px;"})
                            

            self._label_market_names = self._table.find_all("td",
                        {"align": "right"})
        except:
            pass


        self._set_market_dict

                
    @property
    def _is_equal(self):
        value = ""
        try:
            value = len(self._values) == len(self._label_market_names)
        except:
            pass
        
        return value
    @property
    def _set_market_dict(self):
        """This private method add somes key and values into the dictionaries
        """
        if self._is_equal:
            
            for index in range(len(self._values)):
                name = self._label_market_names[index].get_text().strip().lower().replace(" ", "_")
                label_name = name
                
                if '\n' in label_name:
                    label_name = name.replace("\n", "_")
                    
                self._market_dict[label_name] = self._values[index].get_text()
        
    
    
    
    @property
    def get_home_xwin(self):
        """Get the home wins, x represent how many time the home team
        win the game

        Returns:
            return an integer number
        """
        key = self.team.first_team().replace(' ','_') + "_wins"
        
        values = self._market_dict.get(key, 0)
        
        return int(values)
        
    @property
    def get_draw_x(self):
        """Get the draws games, x represent how many time the draws
        happend in the game

        Returns:
            return an integer number
        """
        key = 'draws'
        value = self._market_dict.get(key, 0)
        
        return int(value)
    
    @property
    def get_away_xwin(self):
        """Get the away wins, x represent how many time the away team
        win the game

        Returns:
            return an integer number
        """
        key = self.team.second_team().replace(" ", "_") + "_wins"
        value = self._market_dict.get(key, 0)
        
        return int(value)
    
    @property
    def get_home_xscored(self):
        """Get the home average scored in the game
        , x represent how many time that average happend in the game
       

        Returns:
            return an integer number
        """
        key = self.team.first_team().replace(" ", "_") + '_scored'
        
        value = convert_to_int(self._market_dict.get(key, 0))
        
        return value
    
    @property
    def get_away_xscored(self):
        """Get the away average scored in the game
        , x represent how many time that average happend in the game
       

        Returns:
            return an integer number
        """
        key = self.team.second_team().replace(" ", "_") + "_scored"
        value = convert_to_int(self._market_dict.get(key, 0))
        
        return value
    
    
    @property
    def get_btts_scored(self):
        """Get the stast of btts(both time scored in the game)
        Returns:
            return an string number
        """
        key ='both_teams_scored'
        value = self._market_dict.get(key, 0)
        
        return convert_to_int(value)
    
    @property
    def get_matches_over_one_half(self):
        """Get the over 1.5 that happend in the game
            
            
            Returns: return the string value
        """
        key = 'matches_over_1.5_goals'
        value = convert_to_int(self._market_dict.get(key, 0))
        
        return value
    
    
    @property
    def get_matches_over_two_half(self):
        """Get over 2.5 goals in the game between then an return as 
        string value

        Returns:
            return a string value
        """
        key = 'matches_over_2.5_goals'
        value = convert_to_int(self._market_dict.get(key, 0))
        
        return value
    
    @property
    def get_matches_over_three_half(self):
        """Get over 3.5 goals in the game between the teams in h2h

        Returns:
            return an string value
        """
        key = 'matches_over_3.5_goals'
        
        value = convert_to_int(self._market_dict.get(key, 0))
         
        return value
    
    @property
    def get_total_goals_per_match(self):
        """Get the total goals per match in h2h

        Returns:
            return a float number
        """
        key = 'total_goals_per_match'
        value = self._market_dict.get(key, 0)
        
        return float(value)
    
    
    @property
    def get_home_scored_per_match(self):
        """Get the stast home scored per match in h2h

        Returns:
            return a float number
        """
        key = self.team.first_team().replace(" ", "_") + "_goals_per_match"
        
        value = self._market_dict.get(key, 0)
        
        return float(value)
    
    
    @property
    def get_away_scored_per_match(self):
        """Get the away stast scored per match in h2h

        Returns:
            return a float number
        """
        key = self.team.second_team().replace(" ", "_") + "_goals_per_match"
        
        value = self._market_dict.get(key, 0)
        
        return float(value)
    
    @property
    def get_home_total_goals(self):
        """Get the home total goal in h2h

        Returns:
            return a integer number
        """
        key = self.team.first_team().replace(" ", "_") + "_total_goals"
        
        value = self._market_dict.get(key, 0)
        
        return int(value)
    
    @property
    def get_away_total_goals(self):
        """Get the away total goals in h2h

        Returns:
            return an integer number
        """
        key = self.team.second_team().lower().replace(" ", "_") + "_total_goals"
        
        value = self._market_dict.get(key, 0)
        
        return int(value)
    
    @property
    def home_average_scored(self):
        return home_average_goals_scored()
    
    @property
    def home_goals(self):
        return head2head_get_home_goals()

    
    
    @property
    def away_average_scored(self):
        return away_average_goals_scored()
    
    @property
    def away_goals(self):
        return head2head_get_away_goals()
    
    
    @property
    def all_goals(self):
        return head2head_all_goals()
