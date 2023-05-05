import sys
sys.path.append('.')
from beautifusoup_set.soup import get_soup

table = get_soup().find_all("section",
               attrs={
                   'class': 'fixture__widget bg-gray-widget rounded-md mb-4'
                                       })


most_recomend_tip =table[-1].find("p", attrs={
    'class': 'mb-2'
})

most_recomend_market = table[-1].find('p', attrs={
    'class': "inline-flex"
})
most_recomend_percentage = table[-1].find("span", attrs={
    'class': "font-bold"
})


tips_recomend = most_recomend_tip.get_text().strip()


tips_market = most_recomend_market.get_text().strip()

tips_percentage = most_recomend_percentage.get_text().strip()


class ProTipsterTipsRecomend:
    # this class represent the betting tip recoment in the site protipster
    
    
    _recomend_tips_dict = {
        'tips': tips_recomend,
        'market': tips_market,
        'percentage': tips_percentage
    }
    
    
    @property
    def get_proTipster_tips_recomend(self):
        value = self._recomend_tips_dict.get("tips")
        
        return value
    
    
    @property
    def get_proTipster_market_recomend(self):
        value = f'The market recomend was {self._recomend_tips_dict.get("market").upper()}'
        
        return value
    
    @property
    def get_proTipster_percentage_voted(self):
        value  = f'The percentage more VOTED was {self._recomend_tips_dict.get("percentage").upper()}'
        
        return value
    