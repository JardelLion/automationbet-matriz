import sys
sys.path.append(".")
import sqlite3
from selenium_soccerstats import SoccerStatsSelenium
from beautifusoup_set.soup import get_soup
from teste import show


connect = sqlite3.connect("data_base\Leagues.db")

cursor = connect.cursor()


_leagues = {
    'PremierLeague': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[11]/span/a',
    'ChampionShip': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[12]/span/a',
    'LeagueOne': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[13]/span/a',
    'Laliga': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[16]/span/a',
    'Ligue1': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[19]/span/a',
    'Eredivisie': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[23]/span/a',
    'SerieA': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[24]/span/a',
    'Liga_NOS': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[29]/span/a',
    'Noruega': '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[27]/span/a',
    "Turkey": '//*[@id="headerlocal"]/div/div/div[1]/table[2]/tbody/tr/td[33]/span/a'
}

leagues_tables_soccerStast = {
    'premierLeague': _leagues.get('PremierLeague'),
    'ChampionShip': _leagues.get("ChampoinShip"),
    'LeagueOne': _leagues.get("LeagueOne"),
    "Laliga": _leagues.get('Laliga'),
    'Ligue1': _leagues.get("Ligue1"),
    'Eredivisie': _leagues.get('Eredivisie'),
    'SerieA': _leagues.get('SerieA'),
    'Liga_NOS': _leagues.get("Liga_NOS"),
    'Noruega': _leagues.get("Noruega"),
    'Turkey': _leagues.get("Turkey")
}



def get_teams_names_list(league):
    teams_names = []
    cursor.execute(f"""SELECT Team FROM {league}""")
    for name in cursor:
        teams_names.append(list(name)[0])

    return teams_names


def get_site_content():
    for key_league, xpath_league in leagues_tables_soccerStast.items():
        access = SoccerStatsSelenium(xpath_league)
        for name in get_teams_names_list(key_league):
            print(access.get_history_game_access)
            if name in access.get_history_game_access:
                continue
            else:
                access.access_game_team(name)
                soup = get_soup(access.get_page_content)
                show()

               
            
        break
            

        
    
  





# primeiramente sera pegar League data_base
# pegar uma liga

# open protipster click na liga
# pesquisar se o nome existe, se sim clicar, se nao ignorar
    # caso sim, cliclar e extrair os dados e as tips
                    # tips: the best tip and tip recommend

# open academiadas apostas
    # pesquisar se o nome esta na tabela e clicar 
                # caso sim, extrair os dados de tips
                            # tips: tips recommend

# analise the tips recommend and the best tips like
        # protipster
        # academia das apostas


# open soccerstast
    # clickar na liga
    # pesquisar o jogo caso tenha jogo
        # clicar no jogo 
            # colocar os metodos para extrair os dados
                # guardar as respostas dos metodos em um arquivo
                # guardar as tips recommend no mesmo arquivo

    
