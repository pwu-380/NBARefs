import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

TEAM = 'GSW'
REF = 'Scott Foster'
READFILE = '2014-15_season_refs_1hot.csv'
SAVEFILE = 'Charts/2015_season_epd_gsw_scottfoster'
NUM_TRIALS = 5000

df_all_data = pd.read_csv(READFILE)
df_home = df_all_data[df_all_data['Hometeam'] == TEAM]
df_away = df_all_data[df_all_data['Awayteam'] == TEAM]

num_home_games = df_home[(df_home[REF] == 1)]['Date'].count()
num_away_games = df_away[(df_away[REF] == 1)]['Date'].count()
tot_games = num_home_games + num_away_games

sum_pd_home = df_home[(df_home[REF] == 1)]['Homescore'].sum() - df_home[(df_home[REF] == 1)]['Awayscore'].sum()
sum_pd_away = df_away[(df_away[REF] == 1)]['Awayscore'].sum() - df_away[(df_away[REF] == 1)]['Homescore'].sum()
actual_mean = (sum_pd_home + sum_pd_away)/tot_games

s_pd_home = df_home['Homescore'] - df_home['Awayscore']
s_pd_away = df_away['Awayscore'] - df_away['Homescore']

pd_means = []
count = 0

for i in range(NUM_TRIALS):
    sum_pd_home = s_pd_home.sample(n=num_home_games).sum()
    sum_pd_away = s_pd_away.sample(n=num_away_games).sum()
    mean = (sum_pd_home + sum_pd_away)/tot_games
    if mean <= actual_mean:
        count += 1

    pd_means.append(mean)

print ('Actual mean: ', actual_mean)
print('The number of trials at least as extreme: ', count)
print('Percent of trials at least as extreme: ', count/float(NUM_TRIALS))

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.hist(pd_means, bins=20)
ax.set_xlabel('Mean Point Differential')
ax.set_ylabel('Frequency')
fig.savefig(SAVEFILE)

# Scott Foster
# ('Actual mean: ', 16)
# ('The number of trials at least as extreme: ', 4021)
# ('Percent of trials at least as extreme: ', 0.8042)