from cgitb import text
import enum
import numbers
import sys
from tkinter import S

sys.path.append(".")
from _name_simbol import Simbol
import string


HOME = 0
AWAY = 1



class LastResultMostRecentFirst:
    
    
    def __init__(self, site):
        self._list_names = []
        self._list_goals = []

       

        self._teams = {
                'first_team': {
                'goals': [],
                'conceded': []
            },
    
    
            'second_team': {
            'goals': [],
            'conceded': []
            }
}
        self.site = site.find_all("table", attrs={
            'cellspacing': '0',
            'cellpadding': '1',
            'width': '100%'
        })[2]


        

        self.simbol = Simbol(site)


        teams_names = self.site.find_all('td', attrs={
            'width': '40%'
        })
        
        #caso o teams_names retorne tamanho 0 ele ira procurar outra formacao neste caso
        # uma width de 41% 
        if len(teams_names) == 0:

            teams_names = self.site.find_all('td', attrs={
            'width': '41%'
            })

            if len(teams_names) == 0:

                teams_names = self.site.find_all('td', attrs={
                'width': '33%'
                })



        teams_goals = self.site.find_all('td', attrs={
            'width':'8%',
            'align': 'center'
        
        })

        #caso o teams_goals retorne 0 ira procurar outra formatacao
        #referente ao tamanho de 8%

       

       
        if len(teams_goals) == 0:
            all_goals = []

            
            teams_goals = self.site.find_all('td', attrs={

                'width':'9%',
                'align': 'center'
                })

            
            for index, _ in enumerate(teams_goals):
                v = teams_goals[index].find('a')

                if v is None:
                    all_goals.append(teams_goals[index])
                else:
                    all_goals.append(v.find_all('font')[0])
            
            
            teams_goals = all_goals

           
            
        
  
        
       
        for index, _ in enumerate(teams_names):


            value_split = teams_goals[index].text.strip().split(':')
           
                
            if len(value_split) == 2:
                self._list_goals.append(value_split)
                
            elif len(value_split) == 1:
                value_split = teams_goals[index].text.strip().split('-')
                self._list_goals.append(value_split)

              
            self._list_names.append(teams_names[index].text.strip().split('-'))
            #self._list_goals.append(teams_goals[index].text.strip().split('-'))
        
        
        
        
        #== get_first_team_simbol())
        for index, value in enumerate(self._list_goals):
            if index % 2 == 0:
                #print(list_names[index][HOME].lower().strip() in get_first_team_simbol())
                if self._list_names[index][HOME].lower().strip() in self.simbol.get_first_team_simbol():
                    
                    self._teams['first_team']['goals'].append(int(value[HOME]))
                   
                    self._teams['first_team']['conceded'].append(int(value[AWAY]))
            if index % 2 == 1:
                if self._list_names[index][AWAY].lower().strip() in self.simbol.get_second_team_simbol():
                    self._teams['second_team']['goals'].append(int(value[AWAY]))
                    self._teams['second_team']['conceded'].append(int(value[HOME]))

        '''def append_value_dict():
            for index, names in enumerate(list_names):
                
                if names[HOME].lower().strip() == get_first_team_simbol():
                    teams['first_team']['goals'].append(int(list_goals[index][HOME]))
                    teams['first_team']['conceded'].append(int(list_goals[index][AWAY]))
                    
                    
                elif names[AWAY].lower().strip() == get_second_team_simbol():
                    teams['second_team']['goals'].append(int(list_goals[index][AWAY]))
                    teams['second_team']['conceded'].append(int(list_goals[index][HOME]))
            '''   
        #append_value_dict()      
                
            
    def get_home_goals_scored(self):
        value = self._teams['first_team']['goals']
        
        return value

    def get_home_goals_conceded(self):
        value = self._teams['first_team']['conceded']
        
        return value



    def get_away_goals_scored(self):
        value = self._teams['second_team']['goals']
        
        return value


    def get_away_goals_conceded(self):
        value = self._teams['second_team']['conceded']
        
        return value


    def all_goals(self):
        return self._list_goals


    def first_team_goals_scored_list(self):
        value = sorted(self._teams['first_team']['goals'])
        return value

    def first_team_goals_conceded_list(self):
        value = sorted(self._teams['first_team']['conceded'])
        
        return value


    def second_team_goals_scored_list(self):
        value = sorted(self._teams['second_team']['goals'])
        
        
        return value

    def second_team_goals_conceded_list(self):
        value = sorted(self._teams['second_team']['conceded'])
        
        return value


