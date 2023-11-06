import sys

sys.path.append('.')
from _name_simbol import Simbol 
from soccer_stats.statsProbability import Statistic




teams_names = []
teams_goals = []
count_draws = 0

HOME = 0
AWAY = 1

teams = {
    'home': {
        'scored': 0,
        'conceded': 0,
        'list_goals': [],
        'all_goals_games': [],
        'draw_probability': 0,
        'draw_probabilityLast6Games': 0
    },

    'away': {
        'scored': 0,
        'conceded': 0,
        'list_goals': [],
        'all_goals_games': [],
        'draw_probability': 0,
        'draw_probabilityLast6Games': 0
    }
}


class LastResultMostRecentFirst8Games:

    count_draws = 0
    def __init__(self, site):
        self.stast = Statistic(site)
        self.simbol = Simbol(site)

        self._table = site.find('table', attrs={
            'cellpadding': '1',
            'cellspacing': '0',
            'width': '100%'
        })
        
      

        self.table_names = self._table.find_all('td', attrs={
            'width': '40%'
        })
        self.table_goals = self._table.find_all('td', attrs={
            'width': '8%'
        })
        
       

 
        if len(self.table_names) == len(self.table_goals):
            
            for index, _ in enumerate(self.table_names):
                if index < 12:
                    names = self.table_names[index].get_text().strip()
                    goals = self.table_goals[index].get_text().strip()
                    
                    points = goals.split('-')
                    
                    if int(points[0]) == int(points[1]):
                        self.count_draws += 1

                    teams_names.append(names.split(' - '))
                    teams_goals.append(goals.split('-'))


        for pos, names in enumerate(teams_names):
            for index, name in enumerate(names):
                if name.lower().strip() == self.simbol.get_first_team_simbol():
                    teams['home']['scored'] += int(teams_goals[pos][index])
                    teams['home']['conceded'] += int(teams_goals[pos][index-1])
                
                elif name.lower().strip() == self.simbol.get_second_team_simbol():
                    teams['away']['scored'] += int(teams_goals[pos][index])
                    teams['away']['conceded'] += int(teams_goals[pos][index-1])


        for pos, names in enumerate(teams_names):
            if pos % 2 == 0:
                if names[HOME].lower().strip() == self.simbol.get_first_team_simbol():
                    teams['home']['list_goals'].append(teams_goals[pos])

                teams['home']['all_goals_games'].append(teams_goals[pos])

            elif pos % 2 == 1:
                if names[AWAY].lower().strip() == self.simbol.get_second_team_simbol():
                    teams['away']['list_goals'].append(teams_goals[pos])

                teams['away']['all_goals_games'].append(teams_goals[pos])
                


        self.home_scored_media = teams['home']['scored'] / 6
        self.home_conceded_media = teams['home']['conceded'] / 6

        self.away_scored_media = teams['away']['scored'] / 6
        self.away_conceded_media = teams['away']['conceded'] / 6


    def get_home_change_to_score(self):
        value = self.home_scored_media + self.away_conceded_media
        return value / 2

    def get_away_change_to_score(self):
        value = self.away_scored_media + self.home_conceded_media

        return value / 2

    def get_change_media(self):
        value = self.get_home_change_to_score() + self.get_away_change_to_score()

        return value / 2


    def get_last4Games_xdraws():
        return count_draws


    def get_frequency_last6Games_home_draw(self):
        value = teams['home']['list_goals']
        return self.stast.frequency_xdraw(value)

    def get_frequency_last6Games_away_draw(self):
        value = teams['away']['list_goals']
        return self.stast.frequency_xdraw(value)


    def _get_frequency_last6Games_home_draw_all_games(self):
        value = teams['home']['all_goals_games']
        return self.stast.frequency_xdraw(value)

    def _get_frequency_last6Games_away_draw_all_games(self):
        value = teams['away']['all_goals_games']
        return self.stast.frequency_xdraw(value)

    def get_media_frequencyLast6Games_all_games(self):
        return (self._get_frequency_last6Games_away_draw_all_games() +
                self._get_frequency_last6Games_home_draw_all_games()) / 2

    def get_media_frequencyLast6Games_home_and_away(self):
        return (self.get_frequency_last6Games_home_draw() +
                self.get_frequency_last6Games_away_draw()) / 2


