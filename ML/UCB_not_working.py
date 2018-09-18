#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 19:18:25 2018

@author: rahul
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

dataset= pd.read_csv("Ads_CTR_Optimisation.csv")
N=10000
d=10

number_of_selections=[1]*d
sum_of_rewards=[0]*d
selected_ads=[]
total_reward=0
max_upperbound=0

for i in range(0,9):
    selected_ads.append(i)    
    reward= dataset.values[i,i]
    sum_of_rewards[i]+=reward
    
    total_reward+=reward
    
for n in range(10,N):
    ad=0
    max_upper_bound=0
    for i in range(0,d):
        average= sum_of_rewards[i]/number_of_selections[i]
        delta = math.sqrt(3/2 * math.log(n)/number_of_selections[i])
        upper_bound= average+delta
        if upper_bound>max_upper_bound:
            max_upper_bound=upper_bound
            ad=i
        
    selected_ads.append(ad)
    reward= dataset.values[n,ad]
    sum_of_rewards[ad]+=reward
    number_of_selections[ad]+=1
    total_reward+=reward
        
plt.hist(selected_ads)
