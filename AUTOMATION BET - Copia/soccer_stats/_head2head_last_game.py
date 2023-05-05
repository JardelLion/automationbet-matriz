import sys

sys.path.append('.')

from soccer_stats.teams_names import Team

table_goals = []
table_names = []

team_ = {
        'home': {
                'totals_goals': 0,
                'conceded': 0,
                'goals': []
            },
            
            'away': {
                'totals_goals': 0,
                'conceded': 0,
                'goals': []
            }
        }


class Head2HeadLastGame:


    def __init__(self, site):
        self.site = site
        self.team = Team(site)

        self.table = site.find_all("td", attrs={
            'align': 'center',
            'valign': 'top'
        })[4]


        team_names_table = self.table.find_all('td', attrs={
            'align': 'center'
        })

        teams_goals_table = self.table.find_all('b')

        

        for values in teams_goals_table:
            table_goals.append(values.get_text().split('-'))


        for index, values in enumerate(team_names_table):
            names = values.get_text().strip()
            if index % 2 == 0:
                table_names.append(names.split(' - '))

        
    

        for index, values in enumerate(table_names):
            for pos, name in enumerate(values):
                
                if name.strip().lower() == self.team.first_team():
                    self.home_team_scored(table_goals[index][pos])
                    team_['home']['goals'].append(int(table_goals[index][pos]))
                    if pos == 1:
                        self.home_team_conceded(table_goals[index][0])
                    else:
                        self.home_team_conceded(table_goals[index][1])
                
                elif name.strip().lower() == self.team.second_team().lower():
                    
                    self.away_team_scored(table_goals[index][pos].strip())
                    team_['away']['goals'].append(int(table_goals[index][pos].strip()))
                    if pos == 1:
                        self.away_team_conceded(table_goals[index][0])
                    else:
                        self.away_team_conceded(table_goals[index][1])

    def home_team_scored(value):
        team_['home']['totals_goals'] += int(value)

    def home_team_conceded(value):
        team_['home']['conceded'] += int(value)
        
    def away_team_scored(value):
        team_['away']['totals_goals'] += int(value)
        
    def away_team_conceded(value):
        team_['away']['conceded'] += int(value)
            
                    
                    
def home_average_goals_scored():
    sum_values = 0
    
    for value in team_['home']['goals']:
        sum_values += value
        
    return sum_values / len(table_names) 


def away_average_goals_scored():
    sum_values = 0
    for value in team_['away']['goals']:
        sum_values += value
    
    return sum_values / len(table_names)


def head2head_all_goals():
    return table_goals

def head2head_get_home_goals():
    return team_['home']['goals']

def head2head_get_away_goals():
    return team_['away']['goals']


