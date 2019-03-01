# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 03:49:00 2018

@author: Gohar
"""

import pandas as pd              # Data analysis library
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
study = pd.read_csv('study.csv')
study.describe()
study.cov()

def randomSample(df, observations_number, return_type = 'mean'):
    arr =  np.empty([0,50])
    for col in df : 
        if col != 'UNS' :
          x = loopColumn(df, col, observations_number, return_type)
          arr = np.insert(arr, 0, x, 0)
    return arr[::-1]
    
    
def loopColumn(df, col, observations_number, return_type):
    arr_mean = np.array([])
    arr_var = np.array([])
    arr_val = np.array([])
    for i in range(0,50):
        arr_mean = np.append(arr_mean, round(df[col].sample(observations_number).mean(), 2))
        arr_var = np.append(arr_var, round(df[col].sample(observations_number).var(), 2))
        arr_val = np.append(arr_val, round(df[col].sample(observations_number), 2))
    
    if return_type == "mean":
        return arr_mean
    elif return_type == "var":
        return arr_var
    
    
    
    

#STG = np.array([])
#for i in range(0,49):
    #STG = np.append(STG,round(study.STG.sample(10).mean(), 2))
    
#print(np.mean(STG))
mean_of_samples_5 = randomSample(study, 5)
mean_of_samples_10 = randomSample(study, 10)
mean_of_samples_15 = randomSample(study, 15)
mean_of_samples_25 = randomSample(study, 25)

print('STG Mean : ' + str(mean_of_samples_10[0].mean()))
print('PEG Mean : ' + str(mean_of_samples_10[4].mean()))
print('\n')
print('STG Variance : ' + str(randomSample(study, 10, 'var')[0].var()))
print('PEG Variance : ' + str(randomSample(study, 10, 'var')[4].var()))

"""

#Red is the dataset mean
#Green is the mean of the samples mean
chart4, ax4 = plt.subplots()
ax4.axvline(mean_of_samples_25[0].mean(), color= 'purple', linewidth = 2)
ax4.axvline(study['STG'].mean(), color= 'red', linewidth = 2)
sns.rugplot(mean_of_samples_25[0], ax=ax4, color='red')
sns.distplot(mean_of_samples_25[0])


chart1, ax1 = plt.subplots()
ax4.axvline(mean_of_samples_5[0].mean(), color= 'green', linewidth = 2)
ax1.axvline(mean_of_samples_5[0].mean(), color= 'green', linewidth = 2)
ax1.axvline(study['STG'].mean(), color= 'red', linewidth = 2)
ax1.set(xlabel='STG')
sns.rugplot(mean_of_samples_5[0], ax=ax1, color='red')
sns.distplot(mean_of_samples_5[0])
print('Sample Means at sample size of  5 - variance : ' + str(mean_of_samples_5[0].var()))


chart2, ax2 = plt.subplots()
ax4.axvline(mean_of_samples_15[0].mean(), color= 'black', linewidth = 2)
ax2.axvline(mean_of_samples_15[0].mean(), color= 'black', linewidth = 2)
ax2.axvline(study['STG'].mean(), color= 'red', linewidth = 2)
ax2.set(xlabel='STG')
sns.rugplot(mean_of_samples_15[0], ax=ax2, color='red')
sns.distplot(mean_of_samples_15[0])
print('Sample Means at sample size of 15 - variance : ' + str(mean_of_samples_15[0].var()))


chart3, ax3 = plt.subplots()
ax4.axvline(mean_of_samples_25[0].mean(), color= 'blue', linewidth = 2)
ax3.axvline(mean_of_samples_25[0].mean(), color= 'blue', linewidth = 2)
ax3.axvline(study['STG'].mean(), color= 'red', linewidth = 2)
ax3.set(xlabel='STG')
sns.rugplot(mean_of_samples_25[0], ax=ax3, color='red')
sns.distplot(mean_of_samples_25[0])
print('Sample Means at sample size of 25 - variance : ' + str(mean_of_samples_25[0].var()))
"""







"""
chart4, ax4 = plt.subplots()
ax4.axvline(mean_of_samples_25[4].mean(), color= 'purple', linewidth = 2)
ax4.axvline(study['PEG'].mean(), color= 'red', linewidth = 2)
sns.rugplot(mean_of_samples_25[4], ax=ax4, color='red')
sns.distplot(mean_of_samples_25[4])


chart1, ax1 = plt.subplots()
ax4.axvline(mean_of_samples_5[4].mean(), color= 'green', linewidth = 2)
ax1.axvline(mean_of_samples_5[4].mean(), color= 'green', linewidth = 2)
ax1.axvline(study['PEG'].mean(), color= 'red', linewidth = 2)
ax1.set(xlabel='PEG')
sns.rugplot(mean_of_samples_5[4], ax=ax1, color='red')
sns.distplot(mean_of_samples_5[4])
print('Sample Means at sample size of  5 - variance : ' + str(mean_of_samples_5[4].var()))


chart2, ax2 = plt.subplots()
ax4.axvline(mean_of_samples_15[4].mean(), color= 'black', linewidth = 2)
ax2.axvline(mean_of_samples_15[4].mean(), color= 'black', linewidth = 2)
ax2.axvline(study['PEG'].mean(), color= 'red', linewidth = 2)
ax2.set(xlabel='PEG')
sns.rugplot(mean_of_samples_15[4], ax=ax2, color='red')
sns.distplot(mean_of_samples_15[4])
print('Sample Means at sample size of 15 - variance : ' + str(mean_of_samples_15[4].var()))


chart3, ax3 = plt.subplots()
ax4.axvline(mean_of_samples_25[4].mean(), color= 'blue', linewidth = 2)
ax3.axvline(mean_of_samples_25[4].mean(), color= 'blue', linewidth = 2)
ax3.axvline(study['PEG'].mean(), color= 'red', linewidth = 2)
ax3.set(xlabel='PEG')
sns.rugplot(mean_of_samples_25[4], ax=ax3, color='red')
sns.distplot(mean_of_samples_25[4])
print('Sample Means at sample size of 25 - variance : ' + str(mean_of_samples_25[4].var()))

"""


