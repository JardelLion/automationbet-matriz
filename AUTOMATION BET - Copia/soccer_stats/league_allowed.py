leagues = [
    {'italy':[
        'Italy - Serie A',
        'Italy - Serie B',
        'Italy - Serie C - Group A',
        'Italy - Serie C - Group B',
        'Italy - Serie C - Group C',
        'Italy - Serie D - Group A',
        'Italy - Serie D - Group B',
        'Italy - Serie D - Group C',
        'Italy - Serie D - Group D'
        
    ],

    'laliga': [
        'La Liga',
        'Spain - La Liga 2',
        # 'Spain - Tercera Div. Gr. 1',
        # 'Spain - Tercera Div. Gr. 3'
        
    ],
    'brazil': [
        'Brazil - Serie A',
        'Brazil - Serie B',
        'Brazil - Serie C',
        'Brazil - Serie D',
        'Brazil - Paulista A1',
        'Brazil - Parabaino'
    ],
    'francesa': [
        'France - Ligue 1',
        'France - Ligue 2',
        'France - National',
        'France - Nacional'
        
    ],
    'inglesa': [
        'Premier League',
        'Championship',
        'League One',
        'League Two',
        'England - National League',
        'REMOVE ADS - Enjoy an ad-free experience on SoccerSTATS.com and show your support: become a Member!'
    ],
    'argentina': [
        'Argentina - Primera Nacional',
        'Argentina - Primera C',
        'Argentina - Primera C - Apertura',
        'Argentina - Primera C - Clausura',
        'Argentina - Liga Profesional'
        
    ],
    'japao': [
        'Japan - J1 League',
        'Japan - J2 League',
        'Japan - J3 League'
    ],
    'korea': [
        'South Korea - K League 1',
        'South Korea - K League 2',
        'South Korea - K3 League'
    ],
    'alemanha': [
        'Bundesliga',
        'Germany - 2. Liga'
    ],
     'liga_portuguesa': [
         'Portugal - Primeira Liga', # e a mesma coisa que liga portugal
         'Portugal - Liga Portugal',
         'Portugal - Liga Portugal 2',
         'Portugal - Segunda Liga']
    ,
    'scotland': [
        'Scotland - Championship'
    ],

    'africa': [
        'South Africa - Premier Division',
        'South Africa - First Division'
    ],
    'zambia': ['zambia - super league'],
    'usa': [
        'USA - MLS',
        'USA - USL Championship',
        'USA - USL League One'
    ]
    
    }
]


def get_leagues():
    all_leagues = []
    for league_name in leagues:
        for _, league in league_name.items():
            for name in league:
                all_leagues.append(name.lower())

    return all_leagues



