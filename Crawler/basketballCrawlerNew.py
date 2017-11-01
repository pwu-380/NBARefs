#!/Users/Peter/Miniconda2/bin/python
#Run from commandline

import requests
import re
from bs4 import BeautifulSoup as bs
import time
#import logging

#__all__ = ['getSoupFromURL', 'getCurrentPlayerNamesAndURLS',
#           'buildPlayerDictionary', 'searchForName',
#           'savePlayerDictionary', 'loadPlayerDictionary',
#           'gameLogs']

#BASKETBALL_LOG = 'basketball.log'

#logging.basicConfig(filename=BASKETBALL_LOG,
#                    level=logging.DEBUG,
#                    )

URL = 'http://www.basketball-reference.com/boxscores/{0}.html'

BASICID = 'div_box_{0}_basic'
FTACOL = 9

NEWHEADER = 'GameID,Date,Hometeam,Awayteam,Homescore,Awayscore,HFTA,AFTA,Ref,Ref,Ref'


#Objective is to scrape box pages for Home and Away FTAs, and referees for each game
def get_season_refdata(path):
    header = True

    #Opens the season datafile --
    #CSV: GameID | Date | Hometeam | Awayteam | Homescore | Awayscore
    f = open(path, 'r')
    for line in f:
        line = line.strip()
        gid, date, hteam, ateam, hscore, ascore = line.split(',')

        if header:
            print NEWHEADER
            header = False
        else:
            #get_box_stats returns array in order of home FTA, away FTA and refs(x3)
            stats = get_box_stats(get_box_url(date, hteam), hteam.lower(), ateam.lower())
            print '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}'.format(
                  gid, date, hteam, ateam, hscore, ascore, stats[0],
                  stats[1], stats[2], stats[3], stats[4])

        time.sleep(1)	# sleeping to be kind for requests

    f.close()


def get_soup_from_url(url, suppressOutput=True):
    #This function grabs the url and returns and returns the soup
    if not suppressOutput:
        print url

    try:
        r = requests.get(url)
    except:
        return None

    return bs(r.text, 'html.parser')


def get_fta_from_soup (soup, team):
    #Finds the FTA in the soup (can change as the site changes its layout)
    id = BASICID.format(team)
    soup = soup.find('div',{'id':id})
    soup = soup.find('tfoot')
    soup = soup.select('td:nth-of-type({0})'.format(FTACOL))
    return soup[0].text


def get_box_url(date, hteam):
    #Produces the url for the detailed game page on a specific game
    s = date.replace('-','') + '0' + hteam
    boxurl = URL.format(s)
    return boxurl


def get_box_stats(url, hteam, ateam):
    #We want to get the home team FTA, away team FTA, refs
    #Soup can scrape the tables for FTAs
    soup = get_soup_from_url(url)
    hfta = get_fta_from_soup (soup, hteam)
    afta = get_fta_from_soup (soup, ateam)

    #The officials are found by regexing the page text
    s = re.search('(Officials:).*', soup.text).group()
    s = s.encode('ascii', 'ignore').decode('ascii')
    s = s.replace('Officials:','')
    refs = s.split(', ')
    return [hfta, afta, refs[0], refs[1], refs[2]]

get_season_refdata('data/2014-15_season_clean_pt2.csv')

