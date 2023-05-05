import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

OPTIONS = Options()
OPTIONS.headless = False
SITE_URL = 'https://protipster.com'



class NavigatorProtipster:
    """This class represent each iteration with web browser
    to came to a certain page on the site protipster
    """
    NAVIGATOR = webdriver.Chrome(options=OPTIONS)
    _TIPS = '//*[@id="app-container"]/header/nav/div/div[2]/ul/li[1]'
    _tables_league = '//*[@id="app-container"]/header/nav/div/div[2]/ul/li[3]'
    _BURGER = '//*[@id="app-container"]/header/nav/div/button'


    _leagues = {
        'premierLeague': 0,
        'champoinShip': 1,
        'leagueOne': 2,
        'scottishPremierLeague': 5,
        'championsLeague': 8,
        'europaLeague': 9,
        'europaConferenceLeague': 10,
        'laLiga': 13,
        'serieA': 14,
        'bundesLiga': 15,
        'turkeySuperLiga': 16,
        'frenchLiga': 17,
        'eredivisie': 18,
        'eliteSerien': 19,
        'swedish': 20,
        'mls': 21
    }
    
    
    
    def __init__(self, league, name_team):
        self.NAVIGATOR.get(SITE_URL)
        self.click_button_xpath(self._BURGER)
        self.click_button_xpath(self._tables_league)
        
        self.access_league(league)
        self.access_games(name_team)
        
        
        #self.access_footebol_tips_page
        #self.click_on_browse_leagues
        #self.click_on_country(self._TABLES_COUNTRY['england'])
        
    
   
    def click_button_xpath(self, content):
        self.NAVIGATOR.find_element(By.XPATH, content).click()
        
    
    @property
    def click_on_browse_leagues(self):
        value = self.NAVIGATOR.find_element(By.XPATH, '//*[@id="app-container"]/div[5]/div/div[1]/div[1]/section/button')
        self.NAVIGATOR.execute_script('arguments[0].click();', value)
        

    @property
    def access_footebol_tips_page(self):
        """consist to find all the links with is associte with id 1 and
        find some expecific id that content is fotebool tips and
        access this link
        """
        FOOTEBOL_POSITION = 1
        TABLE_POSITION = 0
        table_content = self.NAVIGATOR.find_elements(By.ID, '1')
        
        table_links = table_content[TABLE_POSITION].find_elements(By.TAG_NAME, 'a')
        
        footebol_tips_link = table_links[FOOTEBOL_POSITION].get_attribute('href')

        self.NAVIGATOR.get(footebol_tips_link)
        
    def access_league(self, league_name):
        
        """consist to find all the links with is associte with id 2 and
        find some expecific id that content is league and
        access this link
        """
        TABLE_POSITION = 0
        table_content = self.NAVIGATOR.find_elements(By.ID, '2')
        
        table_links = table_content[TABLE_POSITION].find_elements(By.TAG_NAME, 'a')
        
        league = table_links[league_name].get_attribute('href')

        self.NAVIGATOR.get(league)
        
    
    def access_games(self, name_team):
        table = self.NAVIGATOR.find_element(By.ID, 'list-future')
        
        links  = table.find_elements(By.TAG_NAME, 'a')
        
        values = self._get_link_names(links)
        

        #NAME = 'tottenham hotspur'
            
        for index, names in enumerate(values):
            for name in names:
                value = name.strip().lower()
                if value == name_team:
                    self.NAVIGATOR.get(links[index].get_attribute('href'))
            
            
    def _get_link_names(self,links):
        list_names = []
        for link in links:
            list_names.append(link.text.strip())
            
            
        for index, names in enumerate(list_names):
            values = names[5:-8].split('\n')
            del values[0]
            list_names[index] = values
            
        return list_names
        