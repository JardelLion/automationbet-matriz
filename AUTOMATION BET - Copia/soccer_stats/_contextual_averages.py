import sys
sys.path.append('.')

from soccer_stats.convert_to_int import convert_to_int



list_methos = [

    'Over 1.5 goals',
    'Over 2.5 goals',
    'Both teams scored'
   ]

class _ContextualAverages:
    
    # contextual avarages appear in this site in the position 4
    
    
    average = {
        'overOneHalf': '0',
        'overTwoHalf': '0',
        'bttsScored': '0',
        
        
    }

    def __init__(self, site):
        self.table_value = site.find_all('table',
         {"cellspacing": "0", 'cellpadding': "1", 'width': '100%'})

        self._set_value_list()
        self.show()
    
    

    
    
    _position_list = []
    
    
    def get_table_middle(self):
        # number 4 is the contectual avarages position in this site
        table_middle = self.table_value[4].find_all('font', {'style':"font-size:14px;"})
        
        return table_middle
    

    @property
    def _get_string_table_left(self):
        value_table_left = self.table_value[4].find_all('td', {'style': "padding-left:5px;"})
    
        return value_table_left


    def _set_value_list(self):
        for index in range(len(self._get_string_table_left)):
            if self._get_string_table_left[index].get_text() in list_methos:
                self._position_list.append(index)
        
        
    def show(self):
        
        for index in range(len(self._position_list)):
    
            table_left_string = self._get_string_table_left[self._position_list[index]].get_text().lower()

            value = self.get_table_middle()[self._position_list[index]].get_text()
            
    
           
            if table_left_string == 'over 1.5 goals':
               self.average['overOneHalf'] = convert_to_int(value)
                
            
            if table_left_string == 'over 2.5 goals':
                self.average['overTwoHalf'] = convert_to_int(value)
            
            
            if table_left_string == 'both teams scored':
                
                self.average['bttsScored'] = convert_to_int(value)
                
   
                 
            
    @property
    
    def _get_btts(self):
        return self.average['bttsScored']
    
    @property
    
    def _get_overTwo(self):
        return self.average['overTwoHalf']
    
    
    @property
    
    def _get_overOne(self):
        return self.average['overOneHalf']
            
