import sys


sys.path.append('.')

from soccer_stats.get_name_league import  get_name
from math import ceil




class TableResultPassed:



    def __init__(self, site):
        
        self.table = site.find_all('table', attrs={
                'cellspacing': '0', 'cellpadding': '2'
            })[1]


        if get_name(site) in ['italy - serie b']:

            self.table = site.find_all('table', attrs={
                'cellspacing': '0', 'cellpadding': '2',
                'style':'width:100%;padding-top:22px;'
                
                })[0]

            
        

        self.game = self.table.find('tr', attrs={
            'height':'28'
        })

        if self.game is None:
            for position in range(0, 5):
                self.table = site.find_all('table', attrs={
                'cellspacing': '0', 'cellpadding': '2'
                })[position]  #4 the real position

                self.game = self.table.find('tr', attrs={
                'height':'28'})

                if self.game is None:
                    continue
                else:
                    break

            
        
        self.home_away_stastic = self.game.find_all('td', attrs={
            'align': 'center'
        })

        self.league_stastic = None
        try:
            
            self.league_stastic = self.table.find_all('tr', attrs={
                    'height':'26'
                })[2]

            
        except:
            pass

        if self.league_stastic is None:
            self.league_stastic = self.table.find_all('tr', attrs={
                    'height':'26'
                })

        



        if get_name(site) in ['italy - serie b']:
            self.league_stastic = self.table.find_all('tr', attrs={
                'height':'26'
            })[1]


        if isinstance(self.league_stastic, list):

            for value in self.league_stastic:

                self.league_points = value.find_all('td', attrs={
                    'align': 'center'
                })
        else:
            self.league_points = self.league_stastic.find_all('td', attrs={
                    'align': 'center'
                })


        
        

        self.teams = {
                'home': {
                    "gamePoints": self.home_away_stastic[0].text.strip(),
                    'win': self.home_away_stastic[1].text.strip(),
                    'draw': self.home_away_stastic[2].text.strip(),
                    'lose': self.home_away_stastic[3].text.strip(), 

                        "leagueTotal": {
                            "gamePoints": self.league_points[0].text.strip(),
                            'win': self.league_points[1].text.strip(),
                            'draw': self.league_points[2].text.strip(),
                            'lose': self.league_points[3].text.strip()
                                    }
                        },

                'away': {
                    "gamePoints": self.home_away_stastic[4].text.strip(),
                    'win': self.home_away_stastic[5].text.strip(),
                    'draw': self.home_away_stastic[6].text.strip(),
                    'lose': self.home_away_stastic[7].text.strip(), 

                        "leagueTotal": {
                            "gamePoints": self.league_points[4].text.strip(),
                            'win': self.league_points[5].text.strip(),
                            'draw': self.league_points[6].text.strip(),
                            'lose': self.league_points[7].text.strip()
                        }
                }
        }


        
        #self.show_statics()
      
       


    
                
    
    def get_home_probability_to_draw(self):
        
        home = (
            float(self.teams['home']['leagueTotal']['draw']) /
            float(self.teams['home']['leagueTotal']['gamePoints'])
        

        )

        return ceil(home * 100)

    def get_away_probability_to_draw(self):
        away = (
            float(self.teams['away']['leagueTotal']['draw']) /
            float(self.teams['away']['leagueTotal']['gamePoints'])

        )

        return ceil(away *100)



    def get_league_probability_to_draw(self):
        home = (
            float(self.teams['home']['leagueTotal']['draw']) /
            float(self.teams['home']['leagueTotal']['gamePoints'])

        )

        away = (
            float(self.teams['away']['leagueTotal']['draw']) /
            float(self.teams['away']['leagueTotal']['gamePoints'])

        )

        return ceil(((home * 100) + (away *100)) / 2)


    def get_game_probability_to_draw(self):
        home = (
            float(self.teams['home']['draw']) /
            float(self.teams['home']['gamePoints'])

        )

        away = (
            float(self.teams['away']['draw']) /
            float(self.teams['away']['gamePoints'])

        )

        return ceil(((home * 100) + (away *100)) / 2)

    def show_statics(self):
        print(f'home probability: ', self.get_home_probability_to_draw())
        print(f'away probability: ', self.get_away_probability_to_draw())
        print(f'league draw: ', self.get_league_probability_to_draw())
        print('Game Draw: ', self.get_game_probability_to_draw())


