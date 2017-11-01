__author__ = 'Peter'

#This was intended to plot the distribution of FTA given by a ref against a specific team, versus teams
# in general I think

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_games = pd.read_csv('2015-16_season_refs_1hot.csv')

df_ref_games = df_games[df_games['Scott Foster'] == 1]

# fig = plt.figure()
# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# sns.distplot(df_games['Diff'], bins=9, color='blue', ax=ax)
# sns.distplot(df_ref_games['Diff'], bins=9, color='red', ax=ax)


print df_ref_games[(df_ref_games['Hometeam'] == 'GSW') | (df_ref_games['Awayteam'] == 'GSW')].ix[:,1:9]