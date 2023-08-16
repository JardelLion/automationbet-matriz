import openpyxl

def get_sheet_name(sheet_name):
    return sheet_name




workbook = openpyxl.load_workbook('tecnica_analise/2023/EXPECTED-OVER-2023.xlsx')
sheet = workbook[get_sheet_name('agosto')]

question_day =  '14/8/2023' #data 10/5/2010
#str(input("Qual é o dia que se quer analisar [10/04/2023] / [all]: "))



data = []
game = []
home = []
draw = []
away = []
league = []

under_1_5 = []
over_2_5 = []
under_2_5 = []

analise_fundamentalista = []


for number_row in range(1, 100):
    """Estamos alimentando todas as nossas listas com os valores que estao na planilha."""
    
    if sheet['a' + str(number_row)].value is not None:
        # verificando se o valore nao e None
        # adicionando os valores a nosssas listas
        
        data.append(sheet['a' + str(number_row)].value)
        game.append(sheet['b' + str(number_row)].value)
        home.append(sheet['c' + str(number_row)].value)
        draw.append(sheet['d' + str(number_row)].value)
        away.append(sheet['e' + str(number_row)].value)
     
       
        under_1_5.append(sheet['f' + str(number_row)].value)
        over_2_5.append(sheet['g' + str(number_row)].value)
        under_2_5.append(sheet['h' + str(number_row)].value)

        analise_fundamentalista.append(sheet['j' + str(number_row)].value)
        
        league.append(
            str(sheet['n' + str(number_row)].value).upper().strip()
            )
        
       
    


     
def analise_tecnica_expected_over(index):
    """_summary_
    analisar as odds e encontrar um padrao para o mercado over 2,5  e under 2,5

    Args:
        NOT_ACCEPTABLE_LEAGUES - ligas nao permidas para trabalhar na expected over
        ALLOWED_OVER_LEAGUE - ligas apenas permitidas para trabalhar over 2,5
 
    """
    
    NOT_ACCEPTABLE_LEAGUES = [
        'brazil - serie c',
        'league two',
        'la liga',
        'spain - la liga 2',
        'portugal - primeira liga',
        'portugal - liga portugal',
        'portugal - liga portugal 2',
        'portugal - segunda liga',
        # 'italy - serie a',
        'italy - serie c - group a',
        # 'premier league',
        'scotland - championship',
        'france - national',
        'france - nacional',
        'france - ligue 2',
        'italy - serie c - group b',
        'england - national league',
        'argentina - primera nacional',
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
        'japan - j3 league',
        'japan - j2 league',
        'usa - mls',
        
        'zambia - super league',
        'italy - serie c - group a',
        # 'italy - serie c - group c',
        'italy - serie c - group d',
        'italy - serie d - group a',
        'italy - serie d - group b',
        'italy - serie d - group c',
        'italy - serie d - group d',
        'usa - usl league one',
        'usa - nisa'
             
    ]
    
    ALLOWED_OVER_LEAGUE = [
       
        'PREMIER LEAGUE',
        'BUNDESLIGA',
        #'JAPAN - J1 LEAGUE'
       
    ]
    
    is_analise_under25BLUE = (
        under_1_5[index] < 3 and
        under_1_5[index] != 0 and
        
        league[index] not in [
            'BUNDESLIGA'
        ]
        
    
        # league[index] not in ALLOWED_OVER_LEAGUE
             
    )
    
    is_analise_under25PURPLE = (
        under_1_5[index] <= 3.55 and
        under_1_5[index] != 0 and
        league[index].upper().strip() not in ALLOWED_OVER_LEAGUE 
    
        # league[index] not in ALLOWED_OVER_LEAGUE
             
    )
 
   
    is_analise_over25GRAY = (
       
     
        under_1_5[index] >= 3.75 and
        
        league[index].upper().strip() not in [
            'PREMIER LEAGUE'
        ]
       
    )
    
    
    if league[index].upper().strip() in ['BRAZIL - SERIE A']:
        brazil_condition = (
            under_1_5[index] >= 3.10 and
            under_1_5[index] < 3.75
            )
        
        if brazil_condition:
            return "The Robot Recomend Enter in << OVER 2,25 >> [EXPECTED OVER (YELLOW)]"
            
            
    
    
    # ENTER IN UNDER 2,5 NO BLUE
    if is_analise_under25BLUE and league[index].lower() not in NOT_ACCEPTABLE_LEAGUES:
        
        return "The Robot Recomend Enter in << UNDER 2,5 >> [EXPECTED OVER (BLUE) ]"
    
    
    
    
    
    
    
    # ENTER IN UNDER 2,5 NO PURPLE
    if is_analise_under25PURPLE and league[index].lower() not in NOT_ACCEPTABLE_LEAGUES: 
        
        # if league[index].lower() in ['italy - serie a']:
                
        #     if under_1_5[index] <= 3.50:
        #         return "The Robot Recomend Enter in << UNDER 2,5 >>  [EXPECTED OVER (PURPLE) ]"
        #     else:
        #         return None
            
            
        
        if league[index].lower() in ['league one']:
            if under_1_5[index] < 3.40:
                
                return "The Robot Recomend Enter in << UNDER 2,5 >> [EXPECTED OVER (PURPLE) ]"
            
            else:
                return None    
        
        return "The Robot Recomend Enter in << UNDER 2,5 >> [EXPECTED OVER (PURPLE) ]"
    
    
    
    
    
    
    
    
    
    # enter in OVER 2,5
    if is_analise_over25GRAY and league[index].lower() not in NOT_ACCEPTABLE_LEAGUES:
        if league[index].lower() in [
            'italy - serie a',
            'premier league',
            'france - ligue 1',
            'italy - serie c - group c'
   
        ] and under_1_5[index] == 404: 
            
            return None
        
        # if league[index].lower() in ['italy - serie a']:
            
        #     if under_1_5[index] >= 3.95:
        #         return "The Robot Recomend Enter in << OVER 2,5 >>  [EXPECTED OVER (GRAY) ]"
        #     else:
        #         return None
        
        if league[index].lower() in ['league one']:
            if under_1_5[index] >= 3.90:
                
                return "The Robot Recomend Enter in << OVER 2,5 >>  [EXPECTED OVER (GRAY) ]"
            else:
                return None
            
            
        if league[index].lower() in ['bundesliga'] and over_2_5[index] == 404:
            return None
        
        return "The Robot Recomend Enter in << OVER 2,5 >>  [EXPECTED OVER (GRAY) ]"

        
    
    else:
         return None




#varrer todos os dados da analise fundamentalista
for index in range(1, len(analise_fundamentalista)):

    if question_day == 'all':
    
        if str(analise_fundamentalista[index]).lower().strip() == 'ex-over':
            #do the analise tecnica baseada nas regras do magico
            print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_expected_over(index))
            print()
        
        elif str(analise_fundamentalista[index]).lower() == 'ex-over':
        # do the analise tecnica baseada nas regras do primo
            print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_expected_over(index))
            print()
            
            

        else:
            print('talvez haja algo erro verifica a coluna de analise fundamentalista')
            
    else:
        choosed_data = f'{data[index].day}/{data[index].month}/{data[index].year}'.strip()
        if str(analise_fundamentalista[index]).lower() == 'ex-over':
            #do the analise tecnica baseada nas regras do magico
            if choosed_data == question_day:
                if analise_tecnica_expected_over(index) == None:
                    pass
                else:
                    
                    print(choosed_data, game[index] + " || ", analise_tecnica_expected_over(index))
                    print()
        
        elif str(analise_fundamentalista[index]).lower() == 'ex-over':
        # do the analise tecnica baseada nas regras do primo
            if choosed_data == question_day:
                if analise_tecnica_expected_over(index) == None:
                    pass
                else:
                    
                    print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_expected_over(index))
                    print()
            

        else:
            print('talvez haja algo erro verifica a coluna de analise fundamentalista no excel')
            
        
            
