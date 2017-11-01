import requests
from bs4 import BeautifulSoup

def getSoupFromURL(url, suppressOutput=True):
    """
    This function grabs the url and returns and returns the BeautifulSoup object
    """
    if not suppressOutput:
        print url

    try:
        r = requests.get(url)
        print r.text
    except:
        return None

    return BeautifulSoup(r.text, 'html.parser')

