import sys


sys.path.append('.')

from _name_simbol import Simbol



class _LastResultGameShape:
    
    """This class will represent some atribute of laste result
    game date in some determinate game...
    """
    
    _HOME = 0
    _AWAY = 1
    
    
    _WIN = '#c6ecc6'
    _DRAW = '#FFFFBF'
    _LOSE = '#ffbaba'
    


    
    def __init__(self, team_condition, site):
        self._table = site.find("table", attrs={
            'cellspacing': "0",
            'cellpadding': '1',
            'width': '100%'
        })

        self.simbol = Simbol(site)
   
        self._team_condicion = team_condition
        """[summary]

        Args:
            team_condicion ([type]): [description]
            The condicion mean that this team
            must win, draw, or lose
            
            WIN ----- GREEN
            DRAW ----- WHITE
            LOSE ------ RED
        """
        self._team_names_table_list = self._table.find_all("td", {
            'width': "40%",
            'bgcolor': self._DRAW
                        })
    
    
    
        self._team_goals_table_list = self._table.find_all("td", {
                'align': 'center', 
                'bgcolor': self._DRAW
                 })
      
        
        
        self._set_teams_lastest_result(self._team_condicion)
        
    
                            
                         
    def _set_teams_lastest_result(self, condition_game):
    
        if condition_game == 'DRAW':
           
            """When the condition the game was --DRAW-- this mean
            DRAW In the table represent the color white(a little yellow)
            """
            self._draw_recent_game_stast
            
                
    
        if condition_game == "WIN":
            
            """When the condition the game was ---WIN-- this mean
                    WIN, In the table represent the color green
            """
            self._win_recent_game_stast
           
                  
        elif condition_game == 'LOSE':
            self._lose_recent_game_stast
    
    
    
    
    @property
    def _draw_recent_game_stast(self):
        """This property
         it work every date in the game about every draw in the game, I mean
         goals, conceded goals and how many goals their goals in the draw game
        """
        for index in range(0, 2):
                if index == 0:
                    #Home teams lastest result game
    
                    
                    for pos in range(len(self._get_team_names)):
                    
                    
                        name = self._get_team_names[pos][self._HOME].strip().lower()
                        
                        if self.simbol.get_first_team_simbol() == name:
                            # home team playing at home


                            self._home_team['totals_goals'] += int(self._get_team_goals[pos][self._HOME])
                            self._home_team['goals'].append(int(self._get_team_goals[pos][self._HOME]))
                            self._home_team['totals_conceded'] += int(self._get_team_goals[pos][self._AWAY])
                            self._home_team['conceded'].append(int(self._get_team_goals[pos][self._AWAY]))
                            self._home_team['draw'] += 1
                        else:
                            name = self._get_team_names[pos][self._AWAY].strip().lower()
                            
                            if self.simbol.get_first_team_simbol() == name:
                                # home team plyaing at away
                               
                                self._home_team['away']['totals_goals'] += int(self._get_team_goals[pos][self._AWAY])
                                self._home_team['goals'].append(int(self._get_team_goals[pos][self._AWAY]))
                                self._home_team['away']['totals_conceded'] += int(self._get_team_goals[pos][self._HOME])
                                self._home_team['conceded'].append(int(self._get_team_goals[pos][self._HOME]))
                                self._home_team['away']['draw'] += 1 
                else:
                    # Away lastest result game
                    for pos in range(len(self._get_team_names)):
                        
                        name = self._get_team_names[pos][self._AWAY].strip().lower()
                
                    
                        if self.simbol.get_second_team_simbol() == name:

                            self._away_team['totals_goals'] += int(self._get_team_goals[pos][self._AWAY])
                            self._away_team['goals'].append(int(self._get_team_goals[pos][self._AWAY]))
                            self._away_team['totals_conceded'] += int(self._get_team_goals[pos][self._HOME])
                            self._away_team['conceded'].append(int(self._get_team_goals[pos][self._HOME]))
                            self._away_team['draw'] += 1
                        else:
                            name = self._get_team_names[pos][self._HOME].strip().lower()
                            
                            if self.simbol.get_second_team_simbol() == name:
                               
                                self._away_team['home']['totals_goals'] += int(self._get_team_goals[pos][self._HOME])
                                self._away_team['goals'].append(int(self._get_team_goals[pos][self._HOME]))
                                self._away_team['home']['totals_conceded'] += int(self._get_team_goals[pos][self._AWAY])
                                self._away_team['conceded'].append(int(self._get_team_goals[pos][self._AWAY]))
                                self._away_team['home']['draw'] += 1
                
    
    @property
    def _win_recent_game_stast(self):
        """[summary] This property have the purpose to work on every date
        in the recent game like, win, goals, conceded and how many game the play,
        and how many goals they scored
        """
        self._team_names_table_list = self._table.find_all("td", {
                            'width': "40%",
                            'bgcolor': self._WIN
                    })
        
        
        
        
        self._team_goals_table_list = self._table.find_all("td", {
                    'align': 'center', 
                    'bgcolor': self._WIN
                    })
        
                
    
        for pos in range(len(self._get_team_names)):
        
            
            for index in range(0, 2):
                
                
                if index == 0:
                    # home team playing at home position
                    name = self._get_team_names[pos][self._HOME].strip().lower()
                    
                    
                    if self.simbol.get_first_team_simbol() == name:
                        self._home_team['win'] += 1
                        self._home_team['totals_conceded'] += int(self._get_team_goals[pos][self._AWAY])
                        self._home_team['conceded'].append(int(self._get_team_goals[pos][self._AWAY]))
                        self._home_team['totals_goals'] += int(self._get_team_goals[pos][self._HOME])
                        self._home_team['goals'].append(int(self._get_team_goals[pos][self._HOME]))
                            
                    else:
                        # home team playing at away position
                            
                        name = self._get_team_names[pos][self._AWAY].strip().lower()

                        
                        if self.simbol.get_first_team_simbol() == name:
                            self._home_team['away']['win'] += 1
                            self._home_team['away']['totals_conceded'] += int(self._get_team_goals[pos][self._HOME])
                            self._home_team['conceded'].append(int(self._get_team_goals[pos][self._HOME]))
                            self._home_team['away']['totals_goals'] += int(self._get_team_goals[pos][self._AWAY]) 
                            self._home_team['goals'].append(int(self._get_team_goals[pos][self._AWAY]))       
                
                else:
                    # away
                    name = self._get_team_names[pos][self._AWAY].strip().lower()
                    
                    if self.simbol.get_second_team_simbol() == name:
                    
                        # away team playing at away
                        self._away_team['win'] += 1
                        self._away_team['totals_goals'] += int(self._get_team_goals[pos][self._AWAY])
                        self._away_team['goals'].append(int(self._get_team_goals[pos][self._AWAY]))
                        self._away_team['totals_conceded'] += int(self._get_team_goals[pos][self._HOME])
                        self._away_team['conceded'].append(int(self._get_team_goals[pos][self._HOME]))
                        
                    else:
                        # away team playing at home
                        name = self._get_team_names[pos][self._HOME].strip().lower()
                        
                        if self.simbol.get_second_team_simbol() == name:
                            self._away_team['home']['win'] += 1
                            self._away_team['home']['totals_goals'] += int(self._get_team_goals[pos][self._HOME])
                            self._away_team['goals'].append(int(self._get_team_goals[pos][self._HOME]))
                            self._away_team['home']['totals_conceded'] += int(self._get_team_goals[pos][self._AWAY])
                            self._away_team['conceded'].append(int(self._get_team_goals[pos][self._AWAY]))
     
    @property
    def _lose_recent_game_stast(self):
        """[summary] This property has a function to work on the date in the last
        recent game in the league, and will show you how many game the team(first or second)
        lose, how many goals they scored and how many goals they conceded
        """
        self._team_names_table_list = self._table.find_all("td", {
                'width': "40%",
                'bgcolor': self._LOSE
                                     })
    
        self._team_goals_table_list = self._table.find_all("td", {
                'align': 'center', 
                'bgcolor': self._LOSE
                            })
            
            

        for index in range(0, 2):
            if index == 0:
                #Home teams lastest result game 
                for pos in range(len(self._get_team_names)):
                
                
                    name = self._get_team_names[pos][self._HOME].strip().lower()

                    count = 0
                    if self.simbol.get_first_team_simbol() == name:
                        # home team playing at home
                      

                        self._home_team['totals_goals'] += int(self._get_team_goals[pos][self._HOME])
                        self._home_team['goals'].append(int(self._get_team_goals[pos][self._HOME]))
                        self._home_team['totals_conceded'] += int(self._get_team_goals[pos][self._AWAY])
                        self._home_team['conceded'].append(int(self._get_team_goals[pos][self._AWAY]))
                        self._home_team['lose'] += 1
                       
                    
                    else:
                        
                        name = self._get_team_names[pos][self._AWAY].strip().lower()
                        
                        if self.simbol.get_first_team_simbol()== name:
                            # home team plyaing at away
                            
                            self._home_team['away']['lose'] += 1
                            self._home_team['away']['totals_goals'] += int(self._get_team_goals[pos][self._AWAY])
                            self._home_team['goals'].append(int(self._get_team_goals[pos][self._AWAY]))
                            self._home_team['away']['totals_conceded'] += int(self._get_team_goals[pos][self._HOME])
                            self._home_team['conceded'].append(int(self._get_team_goals[pos][self._HOME]))
            else:
                # Away lastest result game
                for pos in range(len(self._get_team_names)):
                    
                    name = self._get_team_names[pos][self._AWAY].strip().lower()
            
                
                    if self.simbol.get_second_team_simbol() == name:

                        self._away_team['lose'] += 1
                        self._away_team['totals_goals'] += int(self._get_team_goals[pos][self._AWAY])
                        self._away_team['goals'].append(int(self._get_team_goals[pos][self._AWAY]))
                        self._away_team['totals_conceded'] += int(self._get_team_goals[pos][self._HOME])
                        self._away_team['conceded'].append(int(self._get_team_goals[pos][self._HOME]))
                       
                    else:
                        name = self._get_team_names[pos][self._HOME].strip().lower()
                        
                        if self.simbol.get_second_team_simbol() == name:
                
                            self._away_team['home']['lose'] += 1
                            self._away_team['home']['totals_goals'] += int(self._get_team_goals[pos][self._HOME])
                            self._away_team['goals'].append(int(self._get_team_goals[pos][self._HOME]))
                            self._away_team['home']['totals_conceded'] += int(self._get_team_goals[pos][self._AWAY])
                            self._away_team['conceded'].append(int(self._get_team_goals[pos][self._AWAY]))
        
                            
    @property
    def _get_team_names(self):
        team_names = []
        for name in self._team_names_table_list:
            value = name.get_text()

            team_names.append(value.split('-'))
            
        
        return team_names
    
    
    @property
    def _get_team_goals(self):
        teams_goals = []
        
        for goals in self._team_goals_table_list:
            value = goals.get_text()
            
            teams_goals.append(value.split('-'))
            
        return teams_goals
