__author__ = 'Peter'
#This file is used to the point differential distributions for different teams

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Plots multiple charts if True
MULTIPLOT = True
# Plot starting from this team number
TEAMNUM = 0
# Location of datafile
DATAFILE = '2016-17_season_refs_1hot.csv'
# Where the plot is saved
SAVEFILE = 'Charts/2017_season_pd01_BOS-MIL.png'

# Hash key for every team's string
DTEAM = {0: 'BOS',
         1: 'BRK',
         2: 'NYK',
         3: 'PHI',
         4: 'TOR',
         5: 'CHI',
         6: 'CLE',
         7: 'DET',
         8: 'IND',
         9: 'MIL',
         10: 'ATL',
         11: 'CHO',
         12: 'MIA',
         13: 'ORL',
         14: 'WAS',
         15: 'DEN',
         16: 'MIN',
         17: 'OKC',
         18: 'POR',
         19: 'UTA',
         20: 'GSW',
         21: 'LAC',
         22: 'LAL',
         23: 'PHO',
         24: 'SAC',
         25: 'DAL',
         26: 'HOU',
         27: 'MEM',
         28: 'NOP',
         29: 'SAS'
}

df_games = pd.read_csv(DATAFILE)

if MULTIPLOT:
    #Plots 10 teams in a 2x5 figure
    fig, axes = plt.subplots(2, 5, figsize=(15,6), sharex=True, sharey=True)

    for i, row in enumerate(axes):
        for j, ax in enumerate(row):
            #For each team subplot calculate the point differential when they're at home
            df_home = df_games[df_games['Hometeam']==DTEAM[TEAMNUM]][['Homescore','Awayscore']]
            s_pd = df_home['Homescore'] - df_home['Awayscore']
            s_pd = s_pd.rename('Diff')
            df_home = pd.concat([df_home,s_pd], axis=1)

            #Calculate the point differential when they're away
            df_away = df_games[df_games['Awayteam']==DTEAM[TEAMNUM]][['Homescore','Awayscore']]
            s_pd = df_away['Awayscore'] - df_away['Homescore']
            s_pd = s_pd.rename('Diff')
            df_away = pd.concat([df_away,s_pd], axis=1)

            #Plot histograms of home and away point differentials on the same subplot
            sns.distplot(df_home['Diff'], bins=9, color='blue', ax=ax)
            sns.distplot(df_away['Diff'], bins=9, color='red', ax=ax)

            ax.set_title(DTEAM[TEAMNUM])

            if i == len(axes)-1:
                ax.set_xlabel('Point Differential')
            else:
                ax.set_xlabel('')
            if j == 0:
                ax.set_ylabel('Probability Density')

            TEAMNUM += 1
else:
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,0.8,0.8])

    #Calculate the point differential when they're at home
    df_home = df_games[df_games['Hometeam']==DTEAM[TEAMNUM]][['Homescore','Awayscore']]
    s_pd = df_home['Homescore'] - df_home['Awayscore']
    s_pd = s_pd.rename('Diff')
    df_home = pd.concat([df_home,s_pd], axis=1)

    #Calculate the point differential when they're away
    df_away = df_games[df_games['Awayteam']==DTEAM[TEAMNUM]][['Homescore','Awayscore']]
    s_pd = df_away['Awayscore'] - df_away['Homescore']
    s_pd = s_pd.rename('Diff')
    df_away = pd.concat([df_away,s_pd], axis=1)

    #Plot histograms of home and away point differentials on the same plot
    sns.distplot(df_home['Diff'], bins=9, color='blue', ax=ax)
    sns.distplot(df_away['Diff'], bins=9, color='red', ax=ax)

    ax.set_title(DTEAM[TEAMNUM])
    ax.set_xlabel('Point Differential')
    ax.set_ylabel('Probability Density')

plt.savefig(SAVEFILE)