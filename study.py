# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 01:10:05 2018

@author: Gohar
"""

import pandas as pd              # Data analysis library
import seaborn as sns            #DV library
import matplotlib.pyplot as plt  #DV library

study = pd.read_csv('study.csv')

chart1, ax1 = plt.subplots()
ax1.set(xlabel='STG')
sns.rugplot(study['STG'], ax=ax1, color='red')

chart1, ax2 = plt.subplots()
ax2.set(xlabel='SCG')
sns.rugplot(study['SCG'],ax=ax2, color='blue')

chart1, ax3 = plt.subplots()
ax3.set(xlabel='STR')
sns.rugplot(study['STR'],ax=ax3, color='green')

chart1, ax4 = plt.subplots()
ax4.set(xlabel='LPR')
sns.rugplot(study['LPR'],ax=ax4, color='black')

chart1, ax5 = plt.subplots()
ax5.set(xlabel='PEG')
sns.rugplot(study['PEG'],ax=ax5, color='purple')


chart1, ax6 = plt.subplots()
ax6.set(xlabel='ALL ATTR')
# Rug Plot
sns.rugplot(study['STG'], ax=ax6, color='red')
sns.rugplot(study['SCG'], ax=ax6, color='blue')
sns.rugplot(study['STR'], ax=ax6, color='green')
sns.rugplot(study['LPR'], ax=ax6, color='black')
sns.rugplot(study['PEG'], ax=ax6, color='purple')

#scatter plot
study.plot(kind="scatter", x="STG", y="SCG")
study.plot(kind="scatter", x="STG", y="STR")
study.plot(kind="scatter", x="STG", y="LPR")
study.plot(kind="scatter", x="STG", y="PEG")
study.plot(kind="scatter", x="SCG", y="STR")
study.plot(kind="scatter", x="SCG", y="LPR")
study.plot(kind="scatter", x="SCG", y="PEG")
study.plot(kind="scatter", x="STR", y="LPR")
study.plot(kind="scatter", x="STR", y="PEG")
study.plot(kind="scatter", x="LPR", y="PEG")


#Histogram

sns.distplot(study.STG)  
sns.distplot(study.SCG)
sns.distplot(study.STR)
sns.distplot(study.LPR)
sns.distplot(study.PEG) 
study.plot(kind="hist")

#Box Plot 

sns.boxplot(data=study, orient='h')


 


















        