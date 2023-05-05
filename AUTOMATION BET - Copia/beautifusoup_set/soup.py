import sys
sys.path.append(".")

from bs4 import BeautifulSoup
from access.get_access import access


site = "gfile:///C:/Users/Jardel_Jemilson/Documents/BET/2022/04-ABRIL/DAILY%20GAMES/5/Preston%20vs%20Blackpool%20head%20to%20head%20preview%20stats%20and%20analysis,%202021-2022.html"

def get_soup():
    """This function will return a beautifulsoup object

    Returns:
        [type]: [description] object value
    """
    soup = BeautifulSoup(access(site), "html.parser")
    
    return soup
