import sys
from unicodedata import name

sys.path.append('.')


def get_name(site):

    name_league = site.find('div', attrs={
    'id': 'content'
    }).find("font")


    name_league_final_altenative = site.find('div', attrs={
        'id': 'content'
    }).find_all('div')[1].find('font') #caso nao encotre a liga ira mandar este valor
    
    
    

    name_league_second_option = site.find('div', attrs={
        'id': 'content'}).find_all('div')
    

    name_league_second_option_value = ''

    for div_position in range( 0, 6):
        """max limit the div 10, total de div sao 107 mais os dados que queremos
        extrair estar na posicao 3 para dar um pouco de tempo colocamos ate a posicao 6"""

        try:
            
            if div_position == 3:
                v = name_league_second_option[div_position].find('font', attrs={
                })

                name_league_second_option_value = str(v.text).lower().strip()

        except (UnicodeError, AttributeError):
            pass


    altenative_name_league = site.find_all('div')
    altenative_one = 13  #represent the first altenative
    altenative_two = 15  #represent the first altenative
    
    altenative_three = 12  #represent the second altenative
    altenative_four = 14   #represent the second altenative
    
    altenative_list = [
        'REMOVE ADS - Enjoy an ad-free experience, show your support: become a Member!',
        'REMOVE ADS - Enjoy an ad-free experience on SoccerSTATS.com and show your support: become a Member!',
        'remove ads - enjoy an ad-free experience and show your support: become a member!',
        'remove ads - enjoy an ad-free experience, show your support: become a member!',
        'remove ads - enjoy an ad-free experience on soccerstats.com and show your support: become a member!']

    
    value = name_league.get_text()
   

    
    if value.lower().strip() in altenative_list:

        check_altenative = altenative_name_league[altenative_one].find('font')
       
        

        if check_altenative is None:
            try:
                check_altenative = altenative_name_league[altenative_three].find('font').get_text()
                value = check_altenative.lower().strip()
                return value

            except AttributeError:

                check_altenative = altenative_name_league[altenative_four].find('font').get_text()
                value = check_altenative.lower().strip()
                return value

        if altenative_name_league[altenative_one].find('font') is not None:
            
            value = altenative_name_league[altenative_one].find('font').get_text()
            
            
        else:
            if altenative_name_league[altenative_two].find('font').get_text() is not None:
                value = altenative_name_league[altenative_two].find('font').get_text()
    
       
    if value.lower().strip() not in altenative_list:
        if len(value.lower().strip()) <= 1:
            value = name_league_second_option_value
            
    else:
        
        value = str(name_league_final_altenative.text).lower().strip()

            
    return value.lower().strip()



