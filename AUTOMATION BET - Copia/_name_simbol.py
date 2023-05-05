import sys
sys.path.append(".")
from beautifusoup_set.soup import get_soup
from soccer_stats.teams_names import Team

class Simbol:


    def __init__(self, site):
        self.site = site
        self.team = Team(site)

        self.soup = site.find("div", attrs={
            'id': 'content'
        })

        self.table = self.soup.find("table", attrs={
            'cellspacing': '0',
            'cellpadding': '1',
            'width': "100%"
        })


        self.rows = self.table.find_all("tr", attrs={
        
        })[0]


        self.row_values = self.rows.find_all('b')


        self.team_names = {
            self.team.first_team(): self.row_values[0].get_text().lower(),
            self.team.second_team(): self.row_values[-1].get_text().lower()
        }

    def get_first_team_simbol(self):
        return self.team_names[self.team.first_team()]


    def get_second_team_simbol(self):
        return self.team_names[self.team.second_team()]
