# Plots a heat map of refs vs teams

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_team = pd.read_csv('2015-16_season_fta_total.csv')
df_refs = pd.read_csv('2015-16_season_fta_refs.csv')
df_all_data = pd.read_csv('2015-16_season_refs_1hot.csv')

# Order the refs with the highest FTA desc

df_refs = df_refs[df_refs['Refd Games'] > 40] # Drop all refs with fewer than 40 officiated games
df_refs.sort_values('FTA/Game', ascending=False, inplace=True)

print df_refs.head()

# Create matrix for heatmap

temp = []
m = []

for team in df_team.itertuples():
    for ref in df_refs.itertuples():
        df_temp = df_all_data[df_all_data[ref[3]] == 1]
        df_home = df_temp[df_temp['Hometeam'] == team[1]]
        home_sum = df_home['HFTA'].sum()
        home_count = df_home['HFTA'].count()

        df_away = df_temp[df_temp['Awayteam'] == team[1]]
        away_sum = df_away['AFTA'].sum()
        away_sum = int(round(away_sum * 1.05))           # Normalization factor for away games determined by regression
        away_count = df_away['AFTA'].count()

        temp.append((home_sum+away_sum)/(home_count+away_count))
    m.append(temp)
    temp = []

print m

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax = sns.heatmap(m,linewidths=1,linecolor='white',cmap='Spectral', vmax=40, vmin=10, xticklabels=4, yticklabels=4)
ax.set_ylabel('Teams by ranking in FTAs taken')
ax.set_xlabel('Refs by ranking in FTAs given')
fig.savefig('Charts/2016_season_fta_refvteam')

