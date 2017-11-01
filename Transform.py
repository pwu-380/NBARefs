__author__ = 'Peter'

# This script 1hot encodes the ref data

import pandas as pd

READFILE = 'Crawler/data/2016-17_season_refs_complete.csv'
SAVEFILE = '2016-17_season_refs_1hot.csv'

df_raw = pd.read_csv(READFILE)

print df_raw.head()

#Creates dummys for each ref column
df_r0_dummy = pd.get_dummies(df_raw['Ref'])
df_r1_dummy = pd.get_dummies(df_raw['Ref.1'])
df_r2_dummy = pd.get_dummies(df_raw['Ref.2'])

# print ''
# print df_r0_dummy.columns
# print df_r1_dummy.columns
# print df_r2_dummy.columns

#The idea is to first concat all the dummy columns after another, to ensure all refs are captured,
#then group by columns
df_dummy_all = pd.concat([df_r0_dummy, df_r1_dummy, df_r2_dummy], axis=1)
df_dummy_all = df_dummy_all.groupby(level=0, axis=1).sum()

print df_dummy_all.head()

#Removes the old ref columns and concats the 1-hot encoded data
df_raw = df_raw.ix[:,0:8]
df_transformed = pd.concat([df_raw, df_dummy_all],axis=1)

df_transformed.to_csv(SAVEFILE)