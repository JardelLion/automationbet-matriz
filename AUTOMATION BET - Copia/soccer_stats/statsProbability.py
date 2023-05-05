from re import S
import sys
sys.path.append(".")

from soccer_stats.last_result_game import LastResulGame
from soccer_stats.avarage_scoring.average_scoring import ScoringStats
from soccer_stats.last_result_game_4Games import LastResult4Games
import math




class Statistic:
    # This class represent statis made for the creator of program
    
    
    def __init__(self, site):
        self.LAST_RESULT_GAME_4GAMES = LastResult4Games(site)
        self.LAST_REULT_GAME = LastResulGame(site)
        self.SCORING_STATIST = ScoringStats(site)
    
    
    
    @property
    def get_home_predict_goal(self):
        """it take the average league goal
        and check if has change to the home team is
        bigger than average league goal
        
        if it is it will return the number goal
        if not it will return -1

        Returns:
            return a integer number
        """
        
        averague_league = self.SCORING_STATIST.get_leagueAverageScoringHome
        goals_change = self.SCORING_STATIST.get_hasChangeGoalsHome
        if goals_change > averague_league:
            
            return goals_change
        
        
        else:
            return -1
        
    @property
    def get_away_predict_goal(self):
    
        """it take the average league goal
        and check if has change to the home team is
        bigger than average league goal
        
        if it is it will return the number goal
        if not it will return -1

        Returns:
            return a integer number
        """
        
        averague_league = self.SCORING_STATIST.get_leagueAverageScoringAway
        goals_change = self.SCORING_STATIST.get_hasChangeGoalsAway
        if goals_change > averague_league:
            
            return goals_change
        
        
        else:
            return -1
        
        
    @property
    def possibility_goals_game(self):
        first_team_goals = self.SCORING_STATIST.get_hasChangeGoalsHome
        second_team_goals = self.SCORING_STATIST.get_hasChangeGoalsAway
        
        return (first_team_goals + second_team_goals) / 2
    
    
    def _frequency_goals(self, all_goals, market, over_goals=0):
        """consiste em determinar com que frequencia acontece um determinado
        resultado em percentagem

        Args:
            all_goals ([type]): [description]
            over_goals ([type]): [description]

        Returns:
            [type]: [description]
        """
        values_goals = all_goals
        
        
        frequency = 0
        if market == 'OVER':
            for goals in values_goals:
                value = int(goals[0]) + int(goals[1])
                if value > over_goals:
                    frequency += 1

        if market == 'UNDER':
            for goals in values_goals:
                value = int(goals[0]) + int(goals[1])
                if value < over_goals:
                    frequency += 1

        if market == 'DRAW':
            for goals in values_goals:
                value = int(goals[0]) == int(goals[1])
                if value:
                    frequency += 1

                
        return int(float(frequency / len(values_goals)) * 100)
    
    
    def frequency_over_goals_headTohead(self, over_goals):
        """method goals represent the method over like over 2,5 3,5 4,5"""
        return self._frequency_goals(
            self.HEAD2HEAD.all_goals, over_goals=over_goals, market='OVER')

    def frequency_over_goals_last8Games(self,over_goals):
        
        return self._frequency_goals(self.LAST_REULT_GAME.all_goals,
            over_goals=over_goals, market='OVER')
        
    
    def frequency_over_goals_last4Games(self, over_goals):
        
        return self._frequency_goals(self.LAST_RESULT_GAME_4GAMES.all_goals,
            over_goals=over_goals, market='OVER')

    def frequency_over_goals_last4Games_home(self, over_goals):
        last4_games_home = []

        for index, goals in enumerate(self.LAST_RESULT_GAME_4GAMES.all_goals):
            if index % 2 == 0:
                last4_games_home.append(goals)
            
        return self._frequency_goals(last4_games_home, over_goals=over_goals,
        market='OVER')

    def frequency_under_goals_last4Games_home(self, over_goals):
        last4_games_home = []

        for index, goals in enumerate(self.LAST_RESULT_GAME_4GAMES.all_goals):
            if index % 2 == 0:
                last4_games_home.append(goals)
            
        return self._frequency_goals(last4_games_home, over_goals=over_goals,
        market='UNDER')


    def frequency_over_goals_last4Games_away(self, over_goals):
        last4_games_away = []

        for index, goals in enumerate(self.LAST_RESULT_GAME_4GAMES.all_goals):
            if index % 2 == 1:
                last4_games_away.append(goals)

        
        return self._frequency_goals(last4_games_away, over_goals=over_goals,
                            market='OVER')


    def frequency_under_goals_last4Games_away(self, over_goals):
        last4_games_away = []

        for index, goals in enumerate(self.LAST_RESULT_GAME_4GAMES.all_goals):
            if index % 2 == 1:
                last4_games_away.append(goals)

        
        return self._frequency_goals(last4_games_away, over_goals=over_goals,
                            market='UNDER')


    def frequency_xdraw(self,games_goals):
        return self._frequency_goals(games_goals, market='DRAW')


        
        
    def mediana(self, values):
    
        '''consiste em determinar que 50% dos valores acima sao superiores e os outros
        sao inferiores a 50% '''
       
        sorted_values = sorted(values)

        mediana_position = (len(sorted_values) + 1) / 2
    
        positions = (math.ceil(mediana_position)), math.floor(mediana_position)
        
        
        return (sorted_values[positions[0]-1] + sorted_values[positions[1]-1]) / 2
    
    
    @property
    def get_mediana_home_scoredLast8Games(self):
        value = self.mediana(self.LAST_REULT_GAME.home_lists_goals_scored)
        return value
    
        
    @property
    def get_mediana_away_scoredLast8Games(self):
        value = self.mediana(self.LAST_REULT_GAME.away_lists_goals_scored)
        return value
    
    
    @property
    def get_mediana_away_concededLast8Games(self):
        value = self.mediana(self.LAST_REULT_GAME.away_lists_goals_conceded)
        
        return value
        
        
    # check every mediana in the last 4 games
    
    @property
    def get_mediana_home_scoredLast4Games(self):
        return self.mediana(self.LAST_RESULT_GAME_4GAMES.home_list_goals_scored) 
    
    @property
    def get_mediana_home_concededLast4Games(self):
        return self.mediana(self.LAST_RESULT_GAME_4GAMES.home_list_goals_conceded)
    
    @property
    def get_mediana_away_scoredLast4Games(self):
        return self.mediana(self.LAST_RESULT_GAME_4GAMES.away_list_goals_scored)
    
    
    @property
    def get_mediana_away_concededLast4Games(self):
        return self.mediana(self.LAST_RESULT_GAME_4GAMES.away_list_goals_conceded)

    @property
    def get_average_mediana_concededLast4Games(self):
        value = (
            self.get_mediana_home_concededLast4Games +
            self.get_mediana_away_concededLast4Games
         )
        
        return value

    @property
    def get_average_mediana_scoredLast4Games(self):
        value = (
            self.get_mediana_home_scoredLast4Games +
            self.get_mediana_away_scoredLast4Games
        )

        return value

    @property
    def get_average_medianaLast4Games(self):
        value = (
            self.get_average_mediana_concededLast4Games +
            self.get_average_mediana_scoredLast4Games
        ) / 2

        return value


    @property
    def _home_change_score_mediana(self):
        value = (self.get_mediana_home_scoredLast4Games +
                self.get_mediana_away_concededLast4Games
            ) / 2

        return value


    @property
    def _away_change_score_mediana(self):
        """determine the median basedo on the last 4 result in the league
        """
        value = (self.get_mediana_away_scoredLast4Games + 
            self.get_mediana_home_concededLast4Games
            ) / 2
        return value

    @property
    def change_score_medianaLast4Games(self):
        return self._away_change_score_mediana + self._home_change_score_mediana

    
    #head to head median
    @property
    def get_mediana_home_headTohead(self):
        return self.mediana(self.HEAD2HEAD.home_goals)

    @property
    def get_mediana_away_headTohead(self):
        return self.mediana(self.HEAD2HEAD.away_goals)


    # change to score based on the mediana
    @property
    def get_change_home_score_mediana_headTohead(self):
        value = (
            self.get_mediana_home_headTohead +
            self.get_mediana_away_headTohead
        ) / 2

        return value

    @property
    def get_change_away_score_mediana_headTohead(self):
        value = (
            self.get_mediana_away_headTohead +
            self.get_mediana_home_headTohead
        ) / 2

        return value

    @property
    def get_changeScoredMediana_headTohead(self):
        value = (
            self.get_change_home_score_mediana_headTohead +
            self.get_change_away_score_mediana_headTohead
        )
        
        return value
