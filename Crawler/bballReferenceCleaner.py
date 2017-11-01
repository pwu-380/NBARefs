#Commandline utility, prepares tables copied from BasketballReference.com for basketballCrawlerNew.py
#python -c 'import bballReferenceCleaner; bballReferenceCleaner.season_data_clean([raw file])' >
# [clean file]

import pandas as pd
import dateutil.parser as parser

DTEAM = {'celtics':'BOS',
		 'nets':'BRK',
		 'knicks':'NYK',
		 '76ers':'PHI',
		 'raptors':'TOR',
		 'bulls':'CHI',
		 'cavaliers':'CLE',
		 'pistons':'DET',
		 'pacers':'IND',
		 'bucks':'MIL',
		 'hawks':'ATL',
		 'hornets':'CHO',
		 'heat':'MIA',
		 'magic':'ORL',
		 'wizards':'WAS',
		 'nuggets':'DEN',
		 'timberwolves':'MIN',
		 'thunder':'OKC',
		 'blazers':'POR',
		 'jazz':'UTA',
		 'warriors':'GSW',
		 'clippers':'LAC',
		 'lakers':'LAL',
		 'suns':'PHO',
		 'kings':'SAC',
		 'mavericks':'DAL',
		 'rockets':'HOU',
		 'grizzlies':'MEM',
		 'pelicans':'NOP',
		 'spurs':'SAS'
		 }

HEADER = 'GameID,Date,Hometeam,Awayteam,Homescore,Awayscore'

def season_data_clean (rawfile):
    df = pd.read_csv(rawfile)
    #regex to strip all subheaders from csv file
    df = df[df.PTS.str.match('\d\d*\d')]
    
    #preparing interesting columns for transform
    dates = df.Date.values.tolist()
    hteams = df['Home/Neutral'].values.tolist()
    ateams = df['Visitor/Neutral'].values.tolist()
    hscore = df['PTS.1'].values.tolist()
    ascore = df['PTS'].values.tolist()
    
    #clean and print each line
    print HEADER
    for j in range(0,len(dates)):
        print '{0},{1},{2},{3},{4},{5}'.format(j+1,
                                               parser.parse(dates[j]).date(),
                                               abbr_team(hteams[j]),
                                               abbr_team(ateams[j]),
                                               hscore[j],ascore[j])
    
def abbr_team (team):
	#split the team name from the home city
	team = team.rsplit(None, 1)[-1]
	teamab = DTEAM[team.lower()]
	return teamab