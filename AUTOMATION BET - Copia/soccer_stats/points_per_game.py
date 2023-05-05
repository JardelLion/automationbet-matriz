import sys

sys.path.append('.')


class PointsPerGame:


    def __init__(self, site):

        self.table = site.find_all('table', attrs={
        'cellspacing':'0',
        'cellpadding': '2'
        })[2]


        self.points = self.table.find_all('td', attrs={
            'align': 'center', 'width': '14%'
        })


        if len(self.points) == 0:
            self.table = site.find_all('table', attrs={
            'cellspacing':'0',
            'cellpadding': '2'
                    })[1]


            self.points = self.table.find_all('td', attrs={
            'align': 'center', 'width': '14%'
        })


    def get_home_points_per_game(self):
    
        value = float(self.points[0].get_text())
        
        return value


    def get_away_points_per_game(self):
        value = float(self.points[1].get_text())

        return value



