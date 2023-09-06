import openpyxl

def get_sheet_name(sheet_name):
    return sheet_name




workbook = openpyxl.load_workbook('tecnica_analise/2023/bts-asian2023.xlsx')
sheet = workbook[get_sheet_name('setembro')]

question_day =  '3/9/2023' #data 01/5/2010
#str(input("Qual é o dia que se quer analisar [10/04/2023] / [all]: "))



data = []
game = []
home = []
draw = []
away = []
league = []
btsyes = []
btsno = []


under_1_5 = []
over_2_5 = []
under_2_5 = []

over_1_5 = []
over_2 = []
under_2 = []

analise_fundamentalista = []


NOT_ACCEPTABLE_LEAGUES = [
        'france - ligue 1',
        'championship',
        'bundesliga',
        'germany - 2. bundesliga',
        'brazil - serie c',
        'league two',
        #'la liga',
        'spain - la liga 2',
        'portugal - primeira liga',
        'portugal - liga portugal',
        'portugal - liga portugal 2',
        'portugal - segunda liga',
        'italy - serie a',
        'italy - serie c - group a',
        #'premier league',
        'scotland - championship',
        'france - national',
        'france - nacional',
        'france - ligue 2',
        'italy - serie c - group b',
        'england - national league',
        #'argentina - primera nacional',
        'south korea - k league 1',
        'argentina - primera c',
        'argentina - primera c - apertura',
        'argentina - primera c - clausura',
        # 'brazil - serie a',
        'brazil - serie b',
        'brazil - serie d',
        'south korea - k3 league',
        'south africa - premier division',
        'south africa - first division',
        'japan - j1 league',
        'argentina - liga profesional',
        'south korea - k league 2',
        #'japan - j3 league',
        #'japan - j2 league',
        'usa - mls',
        'usa - usl championship',
        'zambia - super league',
        'italy - serie c - group a',
        'italy - serie c - group c',
        'italy - serie c - group d',
        'italy - serie d - group a',
        'italy - serie d - group b',
        'italy - serie d - group c',
        'italy - serie d - group d',
        'usa - usl league one',
        'usa - nisa'
             
    ]



NOT_ACCEPTABLE_LEAGUES_2 = [
        #'france - ligue 1',
        'championship',
        'bundesliga',
        'germany - 2. bundesliga',
        'brazil - serie c',
        #'league two',
        'la liga',
        'spain - la liga 2',
        'portugal - primeira liga',
        'portugal - liga portugal',
        'portugal - liga portugal 2',
        'portugal - segunda liga',
        #'italy - serie a',
        'italy - serie c - group a',
        'premier league',
        #'scotland - championship',
        #'france - national',
        #'france - nacional',
        'france - ligue 2',
        'italy - serie c - group b',
        'england - national league',
        'argentina - primera nacional',
        'south korea - k league 1',
        #'argentina - primera c',
        #'argentina - primera c - apertura',
        #'argentina - primera c - clausura',
        # 'brazil - serie a',
        'brazil - serie b',
        #'brazil - serie d',
        'south korea - k3 league',
        'south africa - premier division',
        'south africa - first division',
        #'japan - j1 league',
        #'argentina - liga profesional',
        #'south korea - k league 2',
        'japan - j3 league',
        #'japan - j2 league',
        'usa - mls',
        'usa - usl championship',
        'zambia - super league',
        'italy - serie c - group a',
        'italy - serie c - group c',
        'italy - serie c - group d',
        'italy - serie d - group a',
        'italy - serie d - group b',
        'italy - serie d - group c',
        'italy - serie d - group d',
        #'usa - usl league one',
        'usa - nisa'
             
    ]

for number_row in range(1, 200):
    """Estamos alimentando todas as nossas listas com os valores que estao na planilha."""
    
    if sheet['a' + str(number_row)].value is not None:
        # verificando se o valore nao e None
        # adicionando os valores a nosssas listas
        
        data.append(sheet['a' + str(number_row)].value)
        game.append(sheet['b' + str(number_row)].value)
        # home.append(sheet['c' + str(number_row)].value)
        # draw.append(sheet['d' + str(number_row)].value)
        # away.append(sheet['e' + str(number_row)].value)
    
    
        analise_fundamentalista.append(sheet['m' + str(number_row)].value)
        
        btsyes.append(sheet['n' + str(number_row)].value)
        btsno.append(sheet['o' + str(number_row)].value)
        
        under_1_5.append(sheet['f' + str(number_row)].value)
        over_2_5.append(sheet['g' + str(number_row)].value)
        under_2_5.append(sheet['h' + str(number_row)].value)
        
        
        
        over_1_5.append(sheet['i' + str(number_row)].value)
        over_2.append(sheet['k' + str(number_row)].value)
        under_2.append(sheet['l' + str(number_row)].value)
        
        
        
    
        
        league.append(
            str(sheet['q' + str(number_row)].value).upper().strip()
            )
        
       
     
def analise_tecnica_bts(index):
    """_summary_
    analisar as odds e encontrar um padrao para o mercado bts yes or bts no

    Args:
        NOT_ACCEPTABLE_LEAGUES - ligas nao permidas para trabalhar na bts yes e bts no 
        ALLOWED_OVER_LEAGUE - ligas apenas permitidas para trabalhar bts yes e bts no
 
    """
    
    
    
    
    is_analise_bts_NO = (
        btsyes[index] >= 1.79 and
        btsyes[index] != 0 and
        btsyes[index] != 404 
        #btsno[index] > 1.67
       
       
             
    )
    
    is_analise_bts_YES = (
        btsyes[index] <= 1.70 and
        btsyes[index] != 0 and 
        btsyes[index] != 404 and
        
        league[index].upper().strip() not in [
            'PREMIER LEAGUE',
            'USA - MLS',
            'PORTUGAL - SEGUNDA LIGA',
            'LEAGUE ONE',
            'ITALY - SERIE B',
            'JAPAN - J3 LEAGUE'
            
            
        ] 
        
             
    )
    
    is_analise_over25 = (
        under_1_5[index] >= 3.7 and
        under_1_5[index] != 404 and
        under_1_5[index] != 0
    )
    is_analise_over15 = (
        under_1_5[index] > 3 and
        under_1_5[index] < 3.7 and
         under_1_5[index] != 404 and
        under_1_5[index] != 0
    )
    
    
    is_analise_under2 = (
        under_1_5[index] < 3 and
         under_1_5[index] != 404 and
        under_1_5[index] != 0 and 
        
        league[index] not in [
            'JAPAN - J2 LEAGUE',
            'LEAGUE TWO'

        ]
    )
    
    market_accept = []
 
    if is_analise_over15 and league[index].lower().strip() not in NOT_ACCEPTABLE_LEAGUES_2:
        if over_1_5[index] >= 1.40:
            market_accept.append("The Robot Recomend Enter in << OVER 1.5 NO >>")
     
    if is_analise_over25 and league[index].lower().strip() not in NOT_ACCEPTABLE_LEAGUES_2:
        
        
        if league[index] in ['JAPAN - J2 LEAGUE']:
            if over_2[index] >= 1.40:
            
                market_accept.append("The Robot Recomend Enter in << OVER 2  NO >>")
            
        elif league[index] in ['LEAGUE ONE']:
            if over_1_5[index] >= 1.40:
            
                market_accept.append("The Robot Recomend Enter in << OVER 1,5  NO >>")
            
        
        else:
            if over_2_5[index] >= 1.40:
            
                market_accept.append("The Robot Recomend Enter in << OVER 2.5  NO >>")
      
        
    if is_analise_under2 and league[index].lower().strip() not in NOT_ACCEPTABLE_LEAGUES_2:
        if under_2[index] >= 1.40:
            
            market_accept.append("The Robot Recomend Enter in << UNDER 2 NO >>")
        
    
    if is_analise_bts_NO and league[index].lower().strip() not in NOT_ACCEPTABLE_LEAGUES:
        if btsno[index] >= 1.40:
        
            market_accept.append("The Robot Recomend Enter in << BTS NO >>")
    
    if is_analise_bts_YES and league[index].lower().strip() not in NOT_ACCEPTABLE_LEAGUES:
        if btsno[index] >= 1.40:
            market_accept.append("The Robot Recomend Enter in << BTS YES >>")
        
    if len(market_accept) != 0:
        
        return market_accept
    
    return None
    
    
    
    
def analise_tecnica_bts_(index): 
    return "The Robot Recomend Enter in << @BTS YES test >>"


def analise_tecnica_super(index):
    
    is_analise_home_super = (
        analise_fundamentalista[index].strip() == 'homesuper'
    )
    
    is_analise_away_super = (
        analise_fundamentalista[index].strip() == 'awaysuper'
    )
    
    if is_analise_home_super and league[index].lower().strip() not in NOT_ACCEPTABLE_LEAGUES:
        
        return "The Robot Recomend Enter in << homesuper test >>"
    
    if is_analise_away_super and league[index].lower().strip() not in NOT_ACCEPTABLE_LEAGUES:
        
        return "The Robot Recomend Enter in << awaysuper test >>"
        
        

#varrer todos os dados da analise fundamentalista
for index in range(1, len(analise_fundamentalista)):

    if question_day == 'all':
    
        if str(analise_fundamentalista[index]).upper().strip() == 'BTS NO':
            #do the analise tecnica baseada nas regras do bts no
            print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_bts(index))
            print()
        
            
        elif str(analise_fundamentalista[index]).upper().strip() == 'BTS':
            # do the analise tecnica baseada nas regras do bts
            print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_bts_(index))
            print()
            
        elif str(analise_fundamentalista[index]).lower().strip() in ['homesuper','awaysuper']:
            print('jfdf')
            # do the analise tecnica baseada nas regras do super
            print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_super(index))
            print()
            
            

        else:
            
            print('talvez haja algo erro verifica a coluna de analise fundamentalista')
            
    else:
        choosed_data = f'{data[index].day}/{data[index].month}/{data[index].year}'.strip()
        
        
        if str(analise_fundamentalista[index]).upper().strip() == 'BTS NO':
           
            #do the analise tecnica baseada nas regras do bts no
            
            if choosed_data == question_day:
              
                if analise_tecnica_bts(index) == None:
                    
                    pass
                else:
                
                    print(choosed_data, game[index] + " || ", analise_tecnica_bts(index))
                    print()
        
                  
        elif str(analise_fundamentalista[index]).upper().strip() == 'BTS':
            # do the analise tecnica baseada nas regras do bts
            if choosed_data == question_day:
                if analise_tecnica_bts_(index) == None:
                    pass
                else:
                    
                    print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_bts_(index))
                    print()
                    
        elif str(analise_fundamentalista[index]).lower().strip() in ['homesuper', 'awaysuper']:
            # do the analise tecnica baseada nas regras do super
           
            if choosed_data == question_day:
                if analise_tecnica_super(index) == None:
                    pass
                else:
                    
                    print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_super(index))
                    print()
            

        else:
            print('talvez haja algo erro verifica a coluna de analise fundamentalista no excel')
            
        
            

