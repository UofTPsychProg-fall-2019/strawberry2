#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pandorable problem set 3 for PSY 1210 - Fall 2019

@author: katherineduncan

In this problem set, you'll practice your new pandas data management skills, 
continuing to work with the 2018 IAT data used in class

Note that this is a group assignment. Please work in groups of ~4. You can divvy
up the questions between you, or better yet, work together on the questions to 
overcome potential hurdles 
"""

#%% import packages 
import os
import numpy as np
import pandas as pd

#%%
# Question 1: reading and cleaning

# read in the included IAT_2018.csv file
IAT = pd.read_csv('/Users/evimyftaraj1/Documents/GitHub/lec3_files/IAT_2018.csv')

# rename and reorder the variables to the following (original name->new name):
# session_id->id  
# genderidentity->gender
# raceomb_002->race
# edu->edu
# politicalid_7->politic
# STATE -> state
# att_7->attitude 
# tblacks_0to10-> tblack
# twhites_0to10-> twhite
# labels->labels
# D_biep.White_Good_all->D_white_bias
# Mn_RT_all_3467->rt

IAT = IAT[['session_id', 'genderidentity', 'raceomb_002', 'edu', 'politicalid_7', 'STATE', 'att_7', 'tblacks_0to10', 'twhites_0to10', 'labels', 'D_biep.White_Good_all', 'Mn_RT_all_3467']]

IAT = IAT.rename(columns = {'session_id':'id'})
IAT = IAT.rename(columns = {'genderidentity':'gender'})
IAT = IAT.rename(columns = {'raceomb_002':'race'})
IAT = IAT.rename(columns = {'politicalid_7':'politic'})
IAT = IAT.rename(columns = {'STATE':'state'})
IAT = IAT.rename(columns = {'att_7':'attitude'})
IAT = IAT.rename(columns = {'tblacks_0to10':'tblack'})
IAT = IAT.rename(columns = {'twhites_0to10':'twhite'})
IAT = IAT.rename(columns = {'D_biep.White_Good_all':'D_white_bias'})
IAT = IAT.rename(columns = {'Mn_RT_all_3467':'rt'})


# remove all participants that have at least one missing value
IAT_clean = IAT.dropna(axis=0,how='any')


# check out the replace method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html
# use this to recode gender so that 1=men and 2=women (instead of '[1]' and '[2]')

IAT_clean.gender = IAT_clean.gender.replace(to_replace = '[1]', value = '1')
IAT_clean.gender = IAT_clean.gender.replace(to_replace = '[2]', value = '2')


# use this cleaned dataframe to answer the following questions

#%%
# Question 2: sorting and indexing

# use sorting and indexing to print out the following information:

# the ids of the 5 participants with the fastest reaction times


# the ids of the 5 men with the strongest white-good bias


# the ids of the 5 women in new york with the strongest white-good bias


#%%
# Question 3: loops and pivots

# check out the unique method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html
# use it to get a list of states
states = list(IAT_clean.state.unique())


# write a loop that iterates over states to calculate the median white-good
# bias per state
# store the results in a dataframe with 2 columns: state & bias

IAT_state = []
for i in states:
    if IAT_clean.state == i:
         IAT_state = list(IAT_clean.D_white_bias[IAT_clean.state == i])
         IAT_state.median()
    


# now use the pivot_table function to calculate the same statistics
state_bias=...

# make another pivot_table that calculates median bias per state, separately 
# for each race (organized by columns)
state_race_bias=...
#%%

# Question 4: merging and more merging

# add a new variable that codes for whether or not a participant identifies as 
# black/African American

# use your new variable along with the crosstab function to calculate the 
# proportion of each state's population that is black 
# *hint check out the normalization options
prop_black =...

# state_pop.xlsx contains census data from 2000 taken from http://www.censusscope.org/us/rank_race_blackafricanamerican.html
# the last column contains the proportion of residents who identify as 
# black/African American 
# read in this file and merge its contents with your prop_black table
census =...
merged =...

# use the corr method to correlate the census proportions to the sample proportions

# now merge the census data with your state_race_bias pivot table

# use the corr method again to determine whether white_good biases is correlated 
# with the proportion of the population which is black across states
# calculate and print this correlation for white and black participants





