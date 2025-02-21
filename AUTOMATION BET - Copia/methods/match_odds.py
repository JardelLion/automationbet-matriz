from operator import is_
import sys

sys.path.append('.')
from soccer_stats.statsProbability import Statistic
from soccer_stats.last_result_game_4Games import LastResult4Games
from soccer_stats.teams_names import Team
#from soccer_stats._contextual_averages import _ContextualAverages
from soccer_stats.points_per_game import PointsPerGame
from performance_teams import PerformanceTeam
from _last_result_most_recent_first8Games import LastResultMostRecentFirst8Games
from soccer_stats.avarage_scoring.average_scoring import ScoringStats
from soccer_stats.table_result_passed import  TableResultPassed
from soccer_stats.get_name_league import get_name
from soccer_stats.league_allowed import get_leagues



class MatchOdds:
    """This class represent the time who have more change to win the game
        based on the last 4 games in the league and the DRAW  ideia"""


    _performance = 0
    def __init__(self, site) -> None:
        self.site = site
        self.LAST4_GAMES = LastResult4Games(site)

        
        self.STASTISTIC = Statistic(site)
        #self.CONTEXTUAL = _ContextualAverages(site)

        self.PERFORMANCE = PerformanceTeam(site)

        self.points = PointsPerGame(site)

        self.SCORING_STATIST = ScoringStats(site)

        self.TABLE_RESULT_PASSED = TableResultPassed(site)

        self.last_result_most_recent_first8Games = LastResultMostRecentFirst8Games(site)

        _home_point = self.points.get_home_points_per_game()
        _away_point = self.points.get_away_points_per_game()
        _media_point = (_home_point + _away_point) / 2
        
        self.analize_probability_to_draw_performance
        
      
    def only_two_number(self, number) -> int:
        value = str(number).split('.')
        two_digit = 0
        if len(value[-1]) == 3:
            two_digit = value[-1][:-1]
            value = value[0] + "." + two_digit
        
            return float(value)

        return number
        


    def verify_diference_score_change(self, method='win'):
        if method.lower() == 'draw':
            
            if self.LAST4_GAMES.getChange_home_score > self.LAST4_GAMES.getChange_away_score:
                diference = self.LAST4_GAMES.getChange_home_score - self.LAST4_GAMES.getChange_away_score
                return diference

            elif self.LAST4_GAMES.getChange_away_score > self.LAST4_GAMES.getChange_home_score:
                diference = self.LAST4_GAMES.getChange_away_score - self.LAST4_GAMES.getChange_home_score
                return diference

           
            return self.LAST4_GAMES.getChange_home_score - self.LAST4_GAMES.getChange_away_score

        elif method.lower() == 'win':
            if self.last_result_most_recent_first8Games.get_home_change_to_score() > self.last_result_most_recent_first8Games.get_away_change_to_score():
                diference = self.last_result_most_recent_first8Games.get_home_change_to_score() - self.last_result_most_recent_first8Games.get_away_change_to_score()
                return self.only_two_number(diference)

            elif self.last_result_most_recent_first8Games.get_away_change_to_score() > self.last_result_most_recent_first8Games.get_home_change_to_score():
                diference = self.last_result_most_recent_first8Games.get_away_change_to_score() - self.last_result_most_recent_first8Games.get_home_change_to_score()
                return self.only_two_number(diference)
            return self.only_two_number((self.last_result_most_recent_first8Games.get_home_change_to_score() - self.last_result_most_recent_first8Games.get_away_change_to_score()))


    def home_score_more(self, method='win'):
        if method.lower() == 'win':
            value = self.last_result_most_recent_first8Games.get_home_change_to_score() > self.last_result_most_recent_first8Games.get_away_change_to_score()
            if value:
                number = self.last_result_most_recent_first8Games.get_home_change_to_score() - self.last_result_most_recent_first8Games.get_away_change_to_score()

                if number > 0:
                    return True

            return False

        elif method.lower() == 'draw':
            value = self.LAST4_GAMES.getChange_home_score > self.LAST4_GAMES.getChange_away_score
            

            if value:
                number = self.LAST4_GAMES.getChange_home_score - self.LAST4_GAMES.getChange_away_score

                if number > 1.40:
                    return True

            return False


    def away_score_more(self, method='win'):
        if method.lower() == 'win':
            value = self.last_result_most_recent_first8Games.get_away_change_to_score() > self.last_result_most_recent_first8Games.get_home_change_to_score()

            if value:
                number = self.last_result_most_recent_first8Games.get_away_change_to_score() - self.last_result_most_recent_first8Games.get_home_change_to_score()

                if number > 0:
                    return True

            return False

        elif method.lower() == 'draw':
            value = self.LAST4_GAMES.getChange_away_score > self.LAST4_GAMES.getChange_home_score
            
        
            if value:
                number = self.LAST4_GAMES.getChange_away_score - self.LAST4_GAMES.getChange_home_score
           
                if number > 1.40 :
                    return True


            return False
    

    @property
    def deep_analize_draw(self):

        star_level = (
            self.TABLE_RESULT_PASSED.get_league_probability_to_draw() >= 35 and
            self.TABLE_RESULT_PASSED.get_game_probability_to_draw() >= 35

            )
    
        check = (
            #int(self.CONTEXTUAL._get_overTwo) < 56 and
            self.SCORING_STATIST.get_hasChangeGoalsGame < 2.80 and
            self.SCORING_STATIST.get_averageGoalChangeGame < 2.80 and
            star_level and 
            self.TABLE_RESULT_PASSED.get_home_probability_to_draw() >= 35 and
            self.TABLE_RESULT_PASSED.get_away_probability_to_draw() >= 35
            
        )

        if check:
            return True 

        return False


    @property
    def check_draw(self):
        
        
        is_true = (
            self.away_score_more('draw') == False and
            self.home_score_more('draw') == False and
            self.verify_media_score_change < 1.66 and
            self.deep_analize_draw and
            self.analize_probability_to_draw_performance <= 16
        )

        

       
         
        
        
        if is_true:
           
            
            if self.is_league_allowed:
                
                return "The [ROBOT] Recommend enter in <<[DRAW]>> in this match"
            else:
                print('League Not Allowed (Draw)', get_name(self.site))

           


        return False
    
    @property
    def deep_analize_under1_half(self):

        fist_level = (
            self.TABLE_RESULT_PASSED.get_league_probability_to_draw() >= 35 and
            self.TABLE_RESULT_PASSED.get_game_probability_to_draw() >= 35
        )

        second_level = (
            self.TABLE_RESULT_PASSED.get_league_probability_to_draw() > 30 and
            self.TABLE_RESULT_PASSED.get_game_probability_to_draw() >= 37 and
            self.verify_diference_score_change('draw') <= 0.50
        )

        third_level = (
            self.TABLE_RESULT_PASSED.get_league_probability_to_draw() >= 34 and
            self.TABLE_RESULT_PASSED.get_game_probability_to_draw() >= 34 and
            self.TABLE_RESULT_PASSED.get_home_probability_to_draw() > 30 and
            self.TABLE_RESULT_PASSED.get_away_probability_to_draw() > 30
        )
        

        check = (
            (fist_level or second_level or third_level) and
            self.TABLE_RESULT_PASSED.get_home_probability_to_draw() > 30 and
            self.TABLE_RESULT_PASSED.get_away_probability_to_draw() > 30 and
            self.verify_diference_score_change('draw') < 1
        )
       
        
       
       

        if check:
            return True 

        return False

    @property
    def check_under1_half(self):
        
        NOT_ACCEPTABLE_LEAGUES = [
            'brazil - parabaino',
            'brazil - paulista a1',
            'zambia - super league',
            'spain - la liga 2',
            'usa - mls',
            'usa - usl championship',
            'usa - usl league one',
            'usa - nisa'
            
        ]
       
    

        is_true = (
            self.deep_analize_under1_half and
            self.analize_probability_to_draw_performance < 15 and
            (self.SCORING_STATIST.get_hasChangeGoalsGame < 2.67 and
            self.SCORING_STATIST.get_averageGoalChangeGame < 2.67)
            
        )
        
        if is_true:
    
            if self.is_league_allowed:

                if get_name(self.site) not in NOT_ACCEPTABLE_LEAGUES:

                    if self.analize_probability_to_draw_performance <= 10:
                        return "The [ROBOT] Recommend enter in <<[MAGICO  SUPER INVESTIMENT]>>in this match"

                    return "The [ROBOT] Recommend enter in <<[MAGICO] in this match"

            else:
                print('League Not Allowed (MAGICO)', get_name(self.site))
        return False


    @property
    def deep_analize_primo(self):

        fist_level = (
            self.TABLE_RESULT_PASSED.get_league_probability_to_draw() >= 23 and
            self.TABLE_RESULT_PASSED.get_game_probability_to_draw() >= 23 and
            self.TABLE_RESULT_PASSED.get_home_probability_to_draw() >= 23 and
            self.TABLE_RESULT_PASSED.get_away_probability_to_draw() >= 23 
        )


        second_level = (
            self.TABLE_RESULT_PASSED.get_league_probability_to_draw() >= 20 and
            self.TABLE_RESULT_PASSED.get_game_probability_to_draw() >= 20 and
            self.TABLE_RESULT_PASSED.get_home_probability_to_draw() >= 20 and
            self.TABLE_RESULT_PASSED.get_away_probability_to_draw() >= 20 and 

            (   self.TABLE_RESULT_PASSED.get_league_probability_to_draw() >= 27 or
                self.TABLE_RESULT_PASSED.get_game_probability_to_draw() >= 27 or
                self.TABLE_RESULT_PASSED.get_home_probability_to_draw() > 27 or
                self.TABLE_RESULT_PASSED.get_away_probability_to_draw() > 27
            )
        )
        

        check = (
            (fist_level or second_level)
        )
       
        
       
       

        if check:
            return True 

        return False

    @property
    def under_1_5_primo(self):
        
        NOT_ACCEPTABLE_LEAGUES = [
            'italy - serie c - group a',
            'italy - serie c - group c',
            'italy - serie c - group d',
            'italy - serie d - group a',
            'italy - serie d - group b',
            'italy - serie d - group c',
            'italy - serie d - group d',
            'portugal - liga portugal 2',
            'zambia - super league',
            'spain - la liga 2',
            'france - ligue 2',
            'league one',
            'argentina - primera c'
            'argentina - primera c - apertura',
            'argentina - primera c - clausura',
            'brazil - serie d',
            'england - national league',
            'usa - mls',
            'usa - usl championship',
            'usa - usl league one',
            'usa - nisa'
            
            ]
            
        check = (
            
            self.deep_analize_primo and
            self.verify_diference_score_change('draw') <= 0.50 and
            self.analize_probability_to_draw_performance < 15 and
            self.SCORING_STATIST.get_hasChangeGoalsGame < 2.40 and
            self.SCORING_STATIST.get_averageGoalChangeGame < 2.40 and
            self.check_under1_half == False

        )

        if check and get_name(self.site) not in NOT_ACCEPTABLE_LEAGUES:
            
            if self.is_league_allowed:

                return "The [ROBOT] Recommend enter in [    <<PRIMO>>     ]"
            else:
                print("League NOt Allowed (PRIMO)", get_name(self.site))

        return False


    @property
    def matriz_primo(self):
        """a mudanca principal esta na performance de 26
        E NO EXPECTED GOAL DE 2,67 PARA 2,40"""
        test = [
            
            
        ]
        
        
        NOT_ACCEPTABLE_LEAGUES = [
            'italy - serie b',
            'portugal - primeira liga', # e a mesma coisa que liga portugal
            'portugal - liga portugal',
            'portugal - liga portugal 2',
            'argentina - liga profesional',
            'italy - serie a',
            'brazil - serie a',
            'brazil - serie b',
            'argentina - primera c',
            'argentina - primera c - apertura',
            'argentina - primera c - clausura',
            'south africa - premier division',
            'south africa - first division',
            'italy - serie c - group a',
            'italy - serie c - group b',
            'italy - serie c - group c',
            'italy - serie c - group d',
            'italy - serie d - group a',
            'italy - serie d - group b',
            'italy - serie d - group c',
            'italy - serie d - group d',
            'portugal - liga portugal 2',
            'zambia - super league',
            'spain - la liga 2',
            'france - ligue 2',
            'league one',
            'france - national',
            'france - nacional',
            'scotland - championship',
            'japan - j1 league',
            'japan - j2 league',
            'japan - j3 league',
            'argentina - primera nacional',
            'south korea - k1 league',
            'south korea - k2 league',
            'south korea - k3 league',
            'south korea - k league 1',
            'south korea - k league 2',
            'south korea - k league 3',
            'brazil - serie a',
            'brazil - serie b',
            'brazil - serie d',
            'usa - mls',
            'usa - usl championship',
            'usa - usl league one',
            'usa - nisa'
            
            ]
        check = (
            
            self.deep_analize_primo and
            self.verify_diference_score_change('draw') <= 0.50 and
            self.analize_probability_to_draw_performance <= 26 and
            self.SCORING_STATIST.get_hasChangeGoalsGame < 2.40 and
            self.SCORING_STATIST.get_averageGoalChangeGame < 2.40 and
            self.check_under1_half == False and
            self.under_1_5_primo == False and 
            self.matriz_magico == False
        )

        if check and get_name(self.site) not in NOT_ACCEPTABLE_LEAGUES:
            
            
            if self.is_league_allowed:
                
                if get_name(self.site) in test:
                    return 'test[MATRIZ-PRIMO]'

                # if (get_name(self.site) in SPECIAL_LEAGUES):
                #     return "The [ROBOT] Recommend enter in [   <<TEST>>   ]"

                return "The [ROBOT] Recommend enter in [    <<MATRIZ-PRIMO>>     ]"
            else:
                print("League NOt Allowed (MATRIZ-PRIMO)", get_name(self.site))

        return False
    
    @property
    def matriz_full(self):
        """
        """
        
        
        NOT_ACCEPTABLE_LEAGUES = [
            'spain - la liga 2',
            'portugal - primeira liga',
            'portugal - liga portugal',
            'portugal - liga portugal 2',
            'portugal - segunda liga',
            'italy - serie a',
            'italy - serie c - group a',
            'scotland - championship',
            'france - national',
            'france - nacional',
            'france - ligue 2',
            'premier league',
            'italy - serie c - group b',
            'england - national league',
            'argentina - primera nacional',
            'south korea - k league 1',
            'argentina - primera c',
            'argentina - primera c - apertura',
            'argentina - primera c - clausura',
            'brazil - serie d',
            'south korea - k3 league',
            'south africa - premier division',
            'south africa - first division',
            'japan - j1 league',
            'argentina - liga profesional',
            'south korea - k league 2',
            'japan - j3 league',
            'zambia - super league',
            'italy - serie c - group a',
            'italy - serie c - group b',
            'italy - serie c - group c',
            'italy - serie c - group d',
            'italy - serie d - group a',
            'italy - serie d - group b',
            'italy - serie d - group c',
            'italy - serie d - group d',
            'usa - usl league one',
            'usa - usl championship#',
            'brazil - serie a',
            'brazil - serie b',
            'usa - mls',
            'germany - 2. bundesliga'
             
        ]
        #     'italy - serie c - group a',
        #     'italy - serie c - group c',
        #     'italy - serie c - group d',
        #     'italy - serie d - group a',
        #     'italy - serie d - group b',
        #     'italy - serie d - group c',
        #     'italy - serie d - group d',
        #     'portugal - liga portugal 2',
        #     'zambia - super league',
        #     'spain - la liga 2',
        #     'france - ligue 2',
        #     'league one',
        #     'france - national',
        #     'france - nacional',
        #     'scotland - championship',
        #     'japan - j1 league',
        #     'japan - j2 league',
        #     'argentina - primera nacional',
        #     'south korea - k3 league',
        #     'brazil - serie a',
        #     'brazil - serie b',
        #     'brazil - serie d',
        #     ]
        check = (
            
            self.deep_analize_primo and
            self.verify_diference_score_change('draw') <= 0.50 and
            self.analize_probability_to_matriz_full_performance and
            self.SCORING_STATIST.get_hasChangeGoalsGame < 2.80 and
            self.SCORING_STATIST.get_averageGoalChangeGame < 2.80 and
            self.check_under1_half == False and
            self.under_1_5_primo == False and 
            self.matriz_magico == False and
            self.matriz_primo == False
        )
        


        if check and get_name(self.site) not in NOT_ACCEPTABLE_LEAGUES:
            
            if self.is_league_allowed:

                # if (get_name(self.site) in SPECIAL_LEAGUES):
                #     return "The [ROBOT] Recommend enter in [   <<TEST>>   ]"

                return f"The [ROBOT] Recommend enter in [    <<MATRIZ-FULL({self.SCORING_STATIST.get_averageGoalChangeGame})>>     ]"
            else:
                print("League NOt Allowed (MATRIZ-FULL)", get_name(self.site))

        return False
    
    
    @property
    def matriz_full_expected_over(self):
        """
        """
        
        
        NOT_ACCEPTABLE_LEAGUES = [
            'germany - 2. bundesliga',
            'brazil - serie c',
            'league two',
            'la liga',
            'spain - la liga 2',
            'portugal - primeira liga',
            'portugal - liga portugal',
            'portugal - liga portugal 2',
            'portugal - segunda liga',
            'france - ligue 2',
            # 'italy - serie a',
            'italy - serie c - group a',
            'scotland - championship#',
            'france - national',
            'france - nacional',
            'italy - serie c - group b',
            'england - national league',
            'argentina - primera nacional',
            'south korea - k league 1',
            'argentina - primera c',
            'argentina - primera c - apertura',
            'argentina - primera c - clausura',
            'brazil - serie d',
            'south korea - k3 league',
            'south africa - premier division',
            'south africa - first division',
            'japan - j1 league',
            'argentina - liga profesional',
            'south korea - k league 2',
            'usa - mls',
            'japan - j2 league',
            'japan - j3 league',
            'zambia - super league',
            'italy - serie d - group b'
            'italy - serie c - group a',
            #'italy - serie c - group c',
            'italy - serie c - group d',
            'italy - serie d - group a',
            'italy - serie d - group b',
            'italy - serie d - group c',
            'italy - serie d - group d',
            'usa - usl league one',
            'usa - usl championship'
             
        ]
        #     'italy - serie c - group a',
        #     'italy - serie c - group c',
        #     'italy - serie c - group d',
        #     'italy - serie d - group a',
        #     'italy - serie d - group b',
        #     'italy - serie d - group c',
        #     'italy - serie d - group d',
        #     'portugal - liga portugal 2',
        #     'zambia - super league',
        #     'spain - la liga 2',
        #     'france - ligue 2',
        #     'league one',
        #     'france - national',
        #     'france - nacional',
        #     'scotland - championship',
        #     'japan - j1 league',
        #     
        #     'argentina - primera nacional',
        #     'south korea - k3 league',
        #     'brazil - serie a',
        #     'brazil - serie b',
        #     'brazil - serie d',
        #     ]
        check = (
            
            self.deep_analize_primo and
            self.verify_diference_score_change('draw') <= 2.0 and
            self.analize_probability_to_matriz_full_performance and
            self.SCORING_STATIST.get_hasChangeGoalsGame > 2.80 and
            self.SCORING_STATIST.get_averageGoalChangeGame > 2.80 and
            self.check_under1_half == False and
            self.under_1_5_primo == False and 
            self.matriz_magico == False and
            self.matriz_primo == False
        )

        if check and get_name(self.site) not in NOT_ACCEPTABLE_LEAGUES:
            
            if self.is_league_allowed:

                # if (get_name(self.site) in SPECIAL_LEAGUES):
                #     return "The [ROBOT] Recommend enter in [   <<TEST>>   ]"

                return "The [ROBOT] Recommend enter in [    <<EXPECTED OVER>>     ]"
            else:
                print("League NOt Allowed (MATRIZ-FULL-EXPECTED OVER)", get_name(self.site))

        return False
    
    
    
    @property
    def matriz_magico(self):
        test = [
            'italy - serie b'
            
        ]
       
        NOT_ACCEPTABLE_LEAGUES = [
            'italy - serie a',
            'brazil - serie a',
            'brazil - serie b',
            'argentina - primera c',
            'argentina - primera c - apertura',
            'argentina - primera c - clausura',
            'south africa - premier division',
            'south africa - first division',
            'brazil - parabaino',
            'brazil - paulista a1',
            'zambia - super league',
            'spain - la liga 2',
            'italy - serie c - group b',
            'italy - serie c - group a',
            'italy - serie c - group c',
            'italy - serie c - group d',
            'italy - serie d - group a',
            'italy - serie d - group b',
            'italy - serie d - group c',
            'italy - serie d - group d',
            'portugal - primeira liga', # e a mesma coisa que liga portugal
            'portugal - liga portugal',
            'portugal - liga portugal 2',
            'zambia - super league',
            'argentina - liga profesional',
            'league one',
            'france - national',
            'france - nacional',
            'france - ligue 2',
            'scotland - championship',
            'japan - j1 league',
            'japan - j2 league',
            'japan - j3 league',
            'argentina - primera nacional',
            'brazil - serie b',
            'brazil - serie d',
            'usa - mls',
            'usa - usl championship',
            'usa - usl league one',
            'usa - nisa',
            'south korea - k league 1',
            'south korea - k league 2',
            'south korea - k3 league',
            'argentina - primera c ',
            'argentina - primera c - Apertura',
            'argentina - primera c - Clausura',
            'south Africa - premier division',
            'south africa - first division',
            'germany - 2. bundesliga'
            
        ]
       
       

        is_true = (
            self.deep_analize_under1_half and
            self.analize_probability_to_draw_performance <=26 and
            (self.SCORING_STATIST.get_hasChangeGoalsGame < 2.40 and
                self.SCORING_STATIST.get_averageGoalChangeGame < 2.40) and
            self.check_under1_half == False
            
        )
        
        if is_true:
    
            if self.is_league_allowed:

                if get_name(self.site) not in NOT_ACCEPTABLE_LEAGUES:
                    if get_name(self.site) in test:
                        return 'test [MATRIZ-MAGICO]'
    

                    return "The [ROBOT] Recommend enter in <<[MATRIZ-MAGICO] in this match"

            else:
                print('League Not Allowed (MATRIZ-MAGICO)', get_name(self.site))
        return False
    
        
    @property
    def bothTimeToScore(self):
        NOT_ACCEPTABLE_LEAGUES = [
            # 'france - ligue 1',
            'championship',
            'bundesliga',
            'germany - 2. bundesliga',
            # 'italy - serie a',
            # #'brazil - serie a',
            'brazil - serie b',
            # 'argentina - primera c',
            # 'argentina - primera c - apertura',
            # 'argentina - primera c - clausura',
            'south africa - premier division',
            'south africa - first division',
            # #'brazil - parabaino',
            # #'brazil - paulista a1',
            'zambia - super league',
            'spain - la liga 2',
            'italy - serie c - group b',
            'italy - serie c - group a',
            'italy - serie c - group c',
            'italy - serie c - group d',
            'italy - serie d - group a',
            'italy - serie d - group b',
            'italy - serie d - group c',
            'italy - serie d - group d',
            'portugal - primeira liga', # e a mesma coisa que liga portugal
            'portugal - liga portugal',
            'portugal - liga portugal 2',
            'zambia - super league',
            # 'argentina - liga profesional',
            # 'league two',
            #'france - national',
            #'france - nacional',
            'france - ligue 2',
            # 'scotland - championship',
            'england - national league',
            # 'japan - j1 league',
            # # 'japan - j2 league',
            'japan - j3 league',
            'argentina - primera nacional',
            # 'brazil - serie b',
            # 'brazil - serie d',
            'usa - mls',
            'usa - usl championship',
            'usa - usl league one',
            'usa - nisa',
            'south korea - k league 1',
            # 'south korea - k league 2',
            'south korea - k3 league',
           
            
        ]
        home = (
           
            self.SCORING_STATIST.get_homeScoredPerMatch >= 1 and
            self.SCORING_STATIST.get_homeConcededPerMatch >= 1 and
            self.PERFORMANCE.get_home_change_conceded >= 45 and
            self.PERFORMANCE.get_home_change_score > 40 and
            self.TABLE_RESULT_PASSED.get_home_probability_to_draw() >= 10   
        )
        
        away = (
            self.SCORING_STATIST.get_awayScoredPerMatch >= 1 and
            self.SCORING_STATIST.get_awayConcededPerMatch >= 1 and
            self.PERFORMANCE.get_away_change_conceded >= 45 and
            self.PERFORMANCE.get_away_change_score > 40 and
            self.TABLE_RESULT_PASSED.get_away_probability_to_draw() >= 10
            
        )
        
        if home and away:
             if self.is_league_allowed:
    
                if get_name(self.site) not in NOT_ACCEPTABLE_LEAGUES:
                    
                    if (self.TABLE_RESULT_PASSED.get_home_probability_to_draw() > 15 or
                        self.TABLE_RESULT_PASSED.get_away_probability_to_draw() > 15 ):
                        return 'The ROBOT Recomendo enter in[BOTH TIIME TO SCORE [NO] ]'
                    
                    return "The ROBOT Recomend [BOTH TIME TO SCORE]"
    
    @property
    def asian(self):
        #home jogando em casa e fora forte
        super_to_homeStrong = (
           
            self.SCORING_STATIST.get_homeScoredPerMatch >= 2 and
            self.SCORING_STATIST.get_homeConcededPerMatch <= 0.5 and
            self.PERFORMANCE.get_home_change_score > 65 and
            self.PERFORMANCE.get_home_change_make_points > 50
             
        )
        
        super_to_awayStrong = (
            self.SCORING_STATIST.get_awayScoredPerMatch >= 2 and
            self.SCORING_STATIST.get_awayConcededPerMatch <= 0.5 and
            self.PERFORMANCE.get_away_change_score > 65 and
            self.PERFORMANCE.get_away_change_make_points > 50
            
        )
        
        
        weak_to_home = (
           
            self.SCORING_STATIST.get_homeScoredPerMatch <= 1 and
            self.SCORING_STATIST.get_homeConcededPerMatch >= 2 and
            self.PERFORMANCE.get_home_change_conceded >= 50 and
            self.PERFORMANCE.get_home_change_make_points < 40
             
        )
        
        weak_to_away = (
            self.SCORING_STATIST.get_awayScoredPerMatch <= 1 and
            self.SCORING_STATIST.get_awayConcededPerMatch >= 2 and
            self.PERFORMANCE.get_away_change_conceded >= 50 and
            self.PERFORMANCE.get_away_change_make_points < 40
            
        )
        
        if super_to_homeStrong and weak_to_away:
            return "The ROBOT Recomend enter in [ANSIAN  homeSuper]"
        
        if super_to_awayStrong and weak_to_home:
            return "The ROBOT Recomend enter in [ANSIAN awaySuper]"
        
        
        
        
        
        
        
        
        
        
       

            
        
    @property
    def verify_media_score_change(self):
        


        value = (
            self.LAST4_GAMES.getChange_home_score + self.LAST4_GAMES.getChange_away_score
        )  /2
        

        return value


    @property
    def check_draw_35(self):
        
        
       
        is_true = (
            self.analize_probability_to_draw_performance < 17 and
            self.check_under1_half == False and self.check_draw == False and
            self.TABLE_RESULT_PASSED.get_game_probability_to_draw() >= 35 and
            self.TABLE_RESULT_PASSED.get_league_probability_to_draw() > 30 and
            self.TABLE_RESULT_PASSED.get_home_probability_to_draw() > 30 and
            self.TABLE_RESULT_PASSED.get_away_probability_to_draw() > 30 and
            self.away_score_more('draw') == False and
            self.home_score_more('draw') == False and
            self.verify_media_score_change < 1.66 and
            self.SCORING_STATIST.get_hasChangeGoalsGame < 2.80 and
            self.SCORING_STATIST.get_averageGoalChangeGame < 2.80 and
            self.verify_diference_score_change('draw') < 1
            
        )
        

        
        
         
        
        
        if is_true:
            
            if self.is_league_allowed:
                    
                return "The [ROBOT] Recommend enter in <<DRAW[35]>> in this match"
            else:
                print('League Not Allowed (draw35)', get_name(self.site))


        return False
    
    
    


    @property
    def _under2__half_new(self):
        is_true = (
            self.TABLE_RESULT_PASSED.get_game_probability_to_draw() > 35 and
            self.TABLE_RESULT_PASSED.get_league_probability_to_draw() > 35 and
            self.TABLE_RESULT_PASSED.get_home_probability_to_draw() > 23 and
            self.TABLE_RESULT_PASSED.get_away_probability_to_draw() > 23 and 
            self.verify_diference_score_change('draw') < 1 and
            self.SCORING_STATIST.get_hasChangeGoalsGame < 2 and
            self.analize_probability_to_draw_performance < 32 and
            self.check_draw_35 == False and self.check_draw == False and
            self.check_under1_half == False

        )

        #message = '''ODD DEVE SER ABAIXO DE 3,10 OU SEJA NAO DEVE SER MAIOR OU IGUAL A 3,30 NO UNDER 1,5 GOALS.'''


        if is_true:
            if self.is_league_allowed:
                return f"==>>  The [ROBOT] Recommend enter in <<[UNDER 2NEW]>> in this match"
                
            else:
                print('League Not Allowed ', get_name(self.site))
          

        return False


    @property
    def analize_probability_to_matriz_full_performance(self):
        
        def performance_full_highter(performance_home, performance_away):
            if(performance_home > performance_away):
                return performance_home - performance_away
            
            elif performance_away > performance_home:
                return performance_away - performance_home
            
            else:
                return performance_home - performance_away
            
        performance_result_matriz_full = {
            'points': performance_full_highter(
                self.PERFORMANCE.get_home_change_make_points,
                self.PERFORMANCE.get_away_change_make_points),
            
            'score': performance_full_highter(
                self.PERFORMANCE.get_home_change_score,
                self.PERFORMANCE.get_away_change_score),
            
            'conceded': performance_full_highter(
                self.PERFORMANCE.get_home_change_conceded,
                self.PERFORMANCE.get_away_change_conceded
            )
            
        }
        
        
            
       
            
        is_true = (
            performance_result_matriz_full['points'] <= 33 and
            performance_result_matriz_full['score'] <= 33 and
            performance_result_matriz_full['conceded'] <= 33)
        
        if (is_true):
            return True
        
        else:
            return False
        
        

                      
    @property
    def analize_probability_to_draw_performance(self):
        performance_home_values = [
            self.PERFORMANCE.get_home_change_make_points,
            self.PERFORMANCE.get_home_change_score,
            self.PERFORMANCE.get_home_change_conceded
        ]
        
        performance_away_values = [
            self.PERFORMANCE.get_away_change_make_points,
            self.PERFORMANCE.get_away_change_score,
            self.PERFORMANCE.get_away_change_conceded
        ]
        

        performance_result = {
            'points': 0,
            'score': 0,
            'conceded': 0
        }

        def performance_check(index):
            value = 0
            if performance_home_values[index] > performance_away_values[index]:
                
                value = performance_home_values[index] - performance_away_values[index]
                    
            elif performance_away_values[index] > performance_home_values[index]:

                value = performance_away_values[index] - performance_home_values[index]
            
            else:
                value = performance_home_values[index] - performance_away_values[index]

            return value

        for index, number in enumerate(performance_home_values):
           
            if index == 0:
                performance_result['points'] = performance_check(index)
                

            elif index == 1:
                performance_result['score'] = performance_check(index)
            
            elif index == 2:
               performance_result['conceded'] = performance_check(index)
               

        total_performance_acceptable = (
            performance_result['points'] +
            performance_result['score'] +
            performance_result['conceded']
        )
       
        self._performance = total_performance_acceptable
        if total_performance_acceptable < 0:
            total_performance_acceptable = abs(total_performance_acceptable)  

        return total_performance_acceptable


    def get_performance(self):
        return self._performance


    
    def get_dateOfGame(self):

        table_date = self.site.find("table", attrs={
            'cellspacing': '0', 'cellpadding': '2',
            'width': '100%'
        })

        date = table_date.find_all('tr', attrs={'height': '24'})
        return str(date[-2].text)


    @property
    def _get_dayOfGame(self):
        day = self.get_dateOfGame().split(' ')
        return day[0].strip().lower()


    @property
    def is_league_allowed(self):
        league = get_name(self.site)

        if league in get_leagues():
            return True

        return False
