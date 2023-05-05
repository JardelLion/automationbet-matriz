import sys
sys.path.append(".")


from beautifusoup_set.soup import get_soup


tips =  get_soup().find("div", 
                     {"class": "preview_bet"})


tips_recomend = tips.find("p").get_text().strip()

odds_market_recomend = tips.find("p", attrs={
    'class': "preview_odd"
}).get_text().strip()



class AcademiaTipsRecomend:
    # this class represent the most bet recomend on the site academia de aposta de angola
    
    
    
    _recomend_tips_dict = {
        'tips': tips_recomend,
        'odds': odds_market_recomend
    }

    
    
    @property
    def get_academia_tips_recomend(self):
        value = f'The tips recomend was {self._recomend_tips_dict.get("tips").upper()}'
        
        return value
    
    
    @property
    def get_academia_makert_recomend(self):
        value = f'The odds that bookmakers give us was {self._recomend_tips_dict.get("odds").upper()}'
        
        return value
    
