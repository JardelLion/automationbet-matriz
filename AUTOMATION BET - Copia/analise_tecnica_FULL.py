import openpyxl

def get_sheet_name(sheet_name):
    return sheet_name




workbook = openpyxl.load_workbook('tecnica_analise/2022/MATRIZ-FULL-2022.xlsx')
sheet = workbook[get_sheet_name('setembro')]

question_day =  '30/9/2022' #data 10/5/2010
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


for number_row in range(1, 300):
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
    


     
def analise_tecnica_matriz_full(index):
    """_summary_
    analisar as odds e encontrar um padrao para o mercado over 2,5 over 2,25 e under 2

    Args:
        NOT_ACCEPTABLE_LEAGUES - ligas nao permidas para trabalhar na matriz-full
        ALLOWED_OVER_LEAGUE - ligas apenas permitidas para trabalhar over 2,5 e over 2,25
 
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
        'japan - j3 league'
             
    ]
    
    ALLOWED_OVER_LEAGUE = [
        'JAPAN - J1 LEAGUE',
        'JAPAN - J2 LEAGUE',
        'FRANCE - LIGUE 2',
        'CHAMPIONSHIP',
        'LEAGUE ONE',
        'LEAGUE TWO',
        'BRAZIL - SERIE A',
        'JAPAN - J3 LEAGUE',
        'SOUTH KOREA - K LEAGUE 2',
        'BRAZIL - SERIE B',
        'USA - USL Championship',
        'USA - USL League One',
        'USA - NISA'
    ]
    
    is_analise_under = (
        under_1_5[index] <= 2.90 and
     
        # home[index] > 2.15 and
      
        # away[index] > 2.15 and
        
        over_2_5[index] >= 2 and 
        league[index] not in ALLOWED_OVER_LEAGUE
             
    )
 
   
    is_analise_over = (
        over_2_5[index] <= 2.06 and
     
        under_1_5[index] > 2.90 
       
    )
    
    IS_ANALISE_OVER_LEAGUE_SPECIAL_brasilA = (
        
        under_1_5[index] >= 2.60 and
        over_2_5[index] <= 2.45 and
        league[index] ==  'BRAZIL - SERIE A')
        
        
    IS_ANALISE_OVER_LEAGUE_SPECIAL_brasilB = (
        
        under_1_5[index] >= 2.28 and
        league[index] ==  'BRAZIL - SERIE B')
        
    
    
    
    if IS_ANALISE_OVER_LEAGUE_SPECIAL_brasilA == True:
        
        return 'The Robot Recomend Enter in << --OVER 2,25-- >>  [MATRIZ-FULL]'
     
    elif IS_ANALISE_OVER_LEAGUE_SPECIAL_brasilB == True:
        
        return 'The Robot Recomend Enter in << --OVER 2,25-- >>  [MATRIZ-FULL]' 

        
    
    
  
    
    if is_analise_under and league[index].lower() not in NOT_ACCEPTABLE_LEAGUES:
        return "The Robot Recomend Enter in << UNDER 2 >> [MATRIZ-FULL]"
    
    if is_analise_over and league[index].lower() not in NOT_ACCEPTABLE_LEAGUES:
        if league[index] in ['LEAGUE ONE',
                            'BRAZIL - SERIE A',
                            'JAPAN - J1 LEAGUE',
                            'JAPAN - J3 LEAGUE',
                            'LA LIGA',
                            'USA - USL Championship',
                            'USA - USL League One',
                            'USA - NISA']:
            
            return 'The Robot Recomend Enter in << @OVER 2,25 >>  [MATRIZ-FULL]' 
        
        return "The Robot Recomend Enter in << OVER 2,5 >>  [MATRIZ-FULL]"
    else:
         return "The Robot Recomend [NOT INVEST IN THIS GAME] [MATRIZ-FULL]"




#varrer todos os dados da analise fundamentalista
for index in range(1, len(analise_fundamentalista)):

    if question_day == 'all':
    
        if str(analise_fundamentalista[index]).lower().strip() == 'matriz-full':
            #do the analise tecnica baseada nas regras do magico
            print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_matriz_full(index))
            print()
        
        elif str(analise_fundamentalista[index]).lower() == 'matriz-full':
        # do the analise tecnica baseada nas regras do primo
            print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_matriz_full(index))
            print()
            
            

        else:
            print('talvez haja algo erro verifica a coluna de analise fundamentalista')
            
    else:
        choosed_data = f'{data[index].day}/{data[index].month}/{data[index].year}'.strip()
        if str(analise_fundamentalista[index]).lower() == 'matriz-full':
            #do the analise tecnica baseada nas regras do magico
            if choosed_data == question_day:
                print(choosed_data, game[index] + " || ", analise_tecnica_matriz_full(index))
                print()
        
        elif str(analise_fundamentalista[index]).lower() == 'matriz-full':
        # do the analise tecnica baseada nas regras do primo
            if choosed_data == question_day:
                print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_matriz_full(index))
                print()
            

        else:
            print('talvez haja algo erro verifica a coluna de analise fundamentalista no excel')
            
        
            