import openpyxl

def get_sheet_name(sheet_name):
    return sheet_name




workbook = openpyxl.load_workbook('tecnica_analise/2023/MATRIZ.xlsx')
sheet = workbook[get_sheet_name('maio')]

question_day =  '20/5/2023' #data 10/5/2010
#str(input("Qual é o dia que se quer analisar [10/04/2023] / [all]: "))



data = []
game = []
home = []
draw = []
away = []
home_pinnacle = []
draw_pinnacle = []
away_pinnacle = []
under_1_5 = []
over_2_5 = []
under_2_5 = []
under_1_5_pinnacle = []
over_2_5_pinnacle = []
under_2_5_pinnacle = []
analise_fundamentalista = []


for number_row in range(1, 51):
    """Estamos alimentando todas as nossas listas com os valores que estao na planilha."""
    
    if sheet['a' + str(number_row)].value is not None:
        # verificando se o valore nao e None
        # adicionando os valores a nosssas listas
        
        data.append(sheet['a' + str(number_row)].value)
        game.append(sheet['b' + str(number_row)].value)
        home.append(sheet['c' + str(number_row)].value)
        draw.append(sheet['d' + str(number_row)].value)
        away.append(sheet['e' + str(number_row)].value)
        home_pinnacle.append(sheet['f' + str(number_row)].value)
        draw_pinnacle.append(sheet['g' + str(number_row)].value)
        away_pinnacle.append(sheet['h' + str(number_row)].value)
        under_1_5.append(sheet['i' + str(number_row)].value)
        over_2_5.append(sheet['j' + str(number_row)].value)
        under_2_5.append(sheet['k' + str(number_row)].value)
        under_1_5_pinnacle.append(sheet['l' + str(number_row)].value)
        over_2_5_pinnacle.append(sheet['m' + str(number_row)].value)
        under_2_5_pinnacle.append(sheet['n' + str(number_row)].value)
        analise_fundamentalista.append(sheet['o' + str(number_row)].value)
    


     
def analise_tecnica_magico(index):
    is_analise_under = (
        under_1_5[index] <= 2.85 and
        under_1_5_pinnacle[index] <= 3.09 and
        home[index] > 2.15 and
        home_pinnacle[index] > 2.15 and
        away[index] > 2.15 and
        away_pinnacle[index] > 2.15 and
        over_2_5[index] >= 2 and
        over_2_5_pinnacle[index] >= 2.09         
    )
 
   
    is_analise_over = (
        over_2_5[index] <= 1.98 and
        over_2_5_pinnacle[index] <= 2.09 and
        under_1_5[index] > 2.85 and
        under_1_5_pinnacle[index] > 3.09
    )
    
  
    
    if is_analise_under:
        return "The Robot Recomend Enter in << UNDER 2 >> [MATRIZ-MAGICO]"
    
    if is_analise_over:
        return "The Robot Recomend Enter in << OVER 2,25 >>  [MATRIZ-MAGICO]"
    else:
        return "The Robot Recomend [NOT INVEST IN THIS GAME] [MATRIZ-MAGICO]"
    
    
def analise_tecnica_primo(index):
    is_analise_under = (
        under_1_5[index] <= 2.70 and
        under_1_5_pinnacle[index] <= 2.90 and
        home[index] > 2.15 and
        home_pinnacle[index] > 2.15 and
        away[index] > 2.15 and
        away_pinnacle[index] > 2.15 and
        over_2_5[index] >= 2 and
        over_2_5_pinnacle[index] >= 2.09         
    )
 
   
    is_analise_over = (
        under_1_5[index] > 2.70 and
        under_1_5_pinnacle[index] > 2.90 and
        over_2_5[index] <= 1.98 and
        over_2_5_pinnacle[index] <= 2.09
    )
    
    is_analise_under_2 = (
        under_1_5[index] > 2.70 and
        under_1_5_pinnacle[index] > 2.90 and
        under_1_5[index] != 404 and # means that this market must be open
        under_1_5_pinnacle[index] != 404 and # means that this market must be open
        over_2_5[index] > 1.98 and
        over_2_5_pinnacle[index] > 2.09 and
        under_2_5[index] < 1.91 and
        under_2_5_pinnacle[index] < 1.91 and
        home[index] > 2.15 and
        home_pinnacle[index] > 2.15 and
        away[index] > 2.15 and
        away_pinnacle[index] > 2.15
    )
    
  
    
    if is_analise_under:
        return "The Robot Recomend Enter in << UNDER 2 >> [MATRIZ-PRIMO]"
    
    if is_analise_over:
        return "The Robot Recomend Enter in << OVER 2,25 >>  [MATRIZ-PRIMO]"
    
    if is_analise_under_2:
        return "The Robot Recomend Enter in << UNDER 2,5 >> [MATRIZ-PRIMO]"
    
    else:
        return "The Robot Recomend [NOT INVEST IN THIS GAME] [MATRIZ-PRIMO]"
    
        
    
    
    



#varrer todos os dados da analise fundamentalista
for index in range(1, len(analise_fundamentalista)):

    if question_day == 'all':
    
        if str(analise_fundamentalista[index]).lower() == 'matriz-magico':
            #do the analise tecnica baseada nas regras do magico
            print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_magico(index))
            print()
        
        elif str(analise_fundamentalista[index]).lower() == 'matriz-primo':
        # do the analise tecnica baseada nas regras do primo
            print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_primo(index))
            print()
            
            

        else:
            print('talvez haja algo erro verifica a coluna de analise fundamentalista')
            
    else:
        choosed_data = f'{data[index].day}/{data[index].month}/{data[index].year}'.strip()
        if str(analise_fundamentalista[index]).lower() == 'matriz-magico':
            #do the analise tecnica baseada nas regras do magico
            if choosed_data == question_day:
                print(choosed_data, game[index] + " || ", analise_tecnica_magico(index))
                print()
        
        elif str(analise_fundamentalista[index]).lower() == 'matriz-primo':
        # do the analise tecnica baseada nas regras do primo
            if choosed_data == question_day:
                print(f'{data[index].day}/{data[index].month}/{data[index].year}', game[index] + " || ", analise_tecnica_primo(index))
                print()
            

        else:
            print('talvez haja algo erro verifica a coluna de analise fundamentalista no excel')
            
        
            
