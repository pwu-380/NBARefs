__author__ = 'Peter'

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Filenames/locations
READFILE = '2015-16_playoffs_refs_1hot.csv'         #Score, FTA and Refs for every game
TEAMFILE = '2015-16_playoffs_fta_total.csv'           #Total FTA by team
REFFILE = '2015-16_playoffs_fta_refs.csv'             #Avg FTA in games attended by each ref
PLTFILE = 'Charts/2016_playoffs_fta_refs.png'         #Box plot of the ref FTA averages

PLTBOX = True                                      #True if want to plot boxplot

#Reads season data
df_games = pd.read_csv(READFILE)

print df_games.head()

#Calculates the total FTA for home and away for each team
df_hfta = df_games[['Hometeam', 'HFTA']].groupby('Hometeam').sum()
df_afta = df_games[['Awayteam', 'AFTA']].groupby('Awayteam').sum()

#Calculates total FTA for each team and sorts descending
df_fta = pd.concat([df_hfta, df_afta['AFTA'], df_hfta['HFTA'] + df_afta['AFTA']], axis=1)
df_fta.columns = ['HFTA', 'AFTA', 'Total']
df_fta = df_fta.sort_values('Total', ascending=False)

print df_hfta.head()
print df_afta.head()
print df_fta.head()

df_fta.to_csv(TEAMFILE)

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax = sns.regplot(x='HFTA', y='AFTA', data=df_fta)
# ax.set_title('FTA Home vs Away')
# plt.savefig('Charts/2016_season_fta_corr')

fta_ref = []
ref_list = df_games.columns[9:]

for ref in ref_list:
    games = df_games[df_games[ref] == 1][ref].sum()
    hfta = df_games[df_games[ref] == 1]['HFTA'].sum()
    afta = df_games[df_games[ref] == 1]['AFTA'].sum()
    fta_ref.append({'Ref': ref, 'FTA/Game': (hfta+afta)/games, 'Refd Games': games})

df_fta_ref = pd.DataFrame(fta_ref)
df_fta_ref.to_csv(REFFILE)

if PLTBOX:
    fig2 = plt.figure()
    ax2 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
    ax2 = sns.boxplot(df_fta_ref['FTA/Game'])
    plt.savefig(PLTFILE)