
import sys


sys.path.append('.')


class Team:

    def __init__(self, site):
        self.site = site

        self.teams_names = self.site.find("h1").get_text()
      
        
        

        
        
        '''self.table_names_teams = self.site.find('table', attrs={
            'cellspacing': '0', 'cellpadding': '2',
            'width': '100%'
        }) 

        self.teams_names = self.table_names_teams.find_all('tr', attrs={
        
        })[2].text

        
        
        if self.teams_names.lower() in 'vs':
            print('yes')
            pass
        else:
            self.teams_names = self.table_names_teams.find_all('tr', attrs={
        
        })[2].text'''

        self.position = 0

        for index in range(len(self.teams_names)):
            if self.teams_names[index] == 'v' and self.teams_names[index + 1] == 's':
                self.position = index
                break
     
    def first_team(self):
        """This function have a purpose to return the first name team

        Returns:
            [type]: return a first team name in the game string
        """
        return self.teams_names[0:self.position].strip().lower()  


    def second_team(self):
        """[summary] This function have a purpose to return the second name team

        Returns:
            [type]: return a second team name in the game string
        """
        return self.teams_names[self.position + 3:].strip().lower()
