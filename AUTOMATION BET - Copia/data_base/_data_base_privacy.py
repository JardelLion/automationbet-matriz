import sys
sys.path.append(".")
import sqlite3
from _table_league_names import names_list, games_number, loses
from _table_league_names import wins, draws, goals_aganist, goals_for


conne  = sqlite3.connect("data_base\\League.db")
#conne = sqlite3.connect("Leagues.db")
c = conne.cursor()

league = 'Championship'

list_names = names_list()

def create_table_league(league):
    c.execute(f"""CREATE TABLE IF NOT EXISTS {league}(
    TEAM        TEXT NOT NULL,
    GP          TEXT NOT NULL,
    W           TEXT NOT NULL,
    D           TEXT NOT NULL,
    L           TEXT NOT NULL,
    GF          TEXT NOT NULL,
    GA          TEXT NOT NULL   
    )""")

  


def insert_names_on_league(league,
     names, totals_game, win, draw, lose, goal_for, goal_aganist):
    c.executemany(f"INSERT INTO {league} VALUES(?,?,?,?,?,?,?)",
                 (names, totals_game, win, draw, lose, goal_for, goal_aganist))
    conne.commit()
    print("add successufuly")

    c.close()


create_table_league(league)

insert_names_on_league(league, list_names, games_number(), wins(),
                        draws(), loses(), goals_for(), goals_aganist())

