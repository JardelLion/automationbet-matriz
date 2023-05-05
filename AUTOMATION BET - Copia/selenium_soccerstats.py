from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

OPTIONS = Options()
OPTIONS.headless = False
SITE_URL = 'https://soccerstats.com'

_leagues = {
    'Liga_NOS': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[29]/span/a',
    'Laliga': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[16]/span/a',
    'PremierLeague': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[11]/span/a',
    'ChampionShip': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[12]/span/a',
    'LeagueOne': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[13]/span/a',
    'Ligue1': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[19]/span/a',
    'SerieA': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[24]/span/a',
    'Eliteserien': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[27]/span/a',
    "Turkey": '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[33]/span/a'
}


class SoccerStatsSelenium:
    """This class represent the selinum soccerstast site"""
    
    NAVEGATOR = webdriver.Chrome(options=OPTIONS)
    
    _teams_accessed = []

    def __init__(self, league):
        self.NAVEGATOR.get(SITE_URL)
        self.click_button_agree
        self.find_league(league)
 
    
    @property
    def click_button_agree(self):
        self.NAVEGATOR.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]').click()
    
    
    def find_league(self, league):
        self.NAVEGATOR.find_element(By.XPATH, league).click()

    
    def access_game_team(self, name_team):
        
        list_link = self.NAVEGATOR.find_elements(By.ID, 'btable')[5]

        names = list_link.find_elements(By.CLASS_NAME, 'odd')

        link_place = list_link.find_elements(By.CLASS_NAME, 'vsmall')


        teams_names = []
        for name in names:
            teams_names.append(name.text.split('\n\n\n\n'))

        HOME = 0
        AWAY = 1
        team = name_team


        for index, name in enumerate(teams_names):
            home = name[HOME][9:-5].strip()
            away = name[AWAY][0:-5].strip()

            
            if team in home:
                self._save_history_game_access(home)
                self._save_history_game_access(away)
                self.NAVEGATOR.get(link_place[index].get_attribute('href'))
                
            if team in away:
                self._save_history_game_access(home)
                self._save_history_game_access(away)
                self.NAVEGATOR.get(link_place[index].get_attribute('href'))
                

   
    def _save_history_game_access(self, team):
        self._teams_accessed.append(team)
        return self._teams_accessed


    @property
    def get_history_game_access(self):
        value = self._teams_accessed

        return value

    @property
    def go_back(self):
        self.NAVEGATOR.back()

    @property
    def get_page_content(self):
        return self.NAVEGATOR.page_source
            

#if __name__ == '__main__':
  #  m = SoccerStatsSelenium()
