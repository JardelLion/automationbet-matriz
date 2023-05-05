import sys
sys.path.append(".")

from beautifusoup_set.soup import get_soup


table = get_soup().find('div', attrs={
    'class': 'grid grid-cols-1 md:grid-cols-2 gap-4 my-4'
    
})

table_list = table.find_all("div", attrs={
    'class': 'card text-lg'
})
tips_list = []

tips_dict = {
    "market": '',
    'odds': '',
    'tips': ''
}
for d in table_list:
    tips_list.append(d.find_all("p"))
    
all_tips_list = []  
for key, value_list in enumerate(tips_list):
    tips_dict['market'] = value_list[1].get_text().strip()
    tips_dict['odds'] = value_list[-1].get_text().strip()
    tips_dict['tips'] = value_list[0].get_text().strip()
    
    all_tips_list.append(tips_dict.copy())

for value_dict in all_tips_list:
    for key, value in value_dict.items():
        print(f'{key} : {value.upper()}')
        
    print()
    print()
    
    