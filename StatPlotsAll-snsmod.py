# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 16:00:03 2015

@author: as
"""
#needed packages
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set(color_codes=True)

#set ooptions to be homogeneous with other files
sns.set(font="Open Sans")
sns.set(style="white", context="talk") 
import os

#where are my files ? 
inputpath = '/home/php/Bureau/tests/'
#filed = inputpath+'pooled.csv'
#file1 = inputpath+'603old.txt'
#file2 = inputpath+'603new.txt'
file3 = inputpath+'thy1.txt'
file4 = inputpath+'cos600continu.txt'
file5 = inputpath+'cos603continu.txt'
file6 = inputpath+'cos600stamp.txt'
file7 = inputpath+'cos603stamp.txt'

experiment = 'E on continuous and stamped fibronectin'

#import datas as columns in pandas
cas0 = pd.read_csv(file3, delimiter=r"\s+",  names=['0', 'mean','sd', 'median'], skiprows=2)
cas1 = pd.read_csv(file4, delimiter=r"\s+",  names=['0', 'mean','sd', 'median'], skiprows=2)
cas2 = pd.read_csv(file5, delimiter=r"\s+",  names=['0', 'mean','sd', 'median'], skiprows=2)
cas3 = pd.read_csv(file6, delimiter=r"\s+",  names=['0', 'mean','sd', 'median'], skiprows=2)
cas4 = pd.read_csv(file7, delimiter=r"\s+",  names=['0', 'mean','sd', 'median'], skiprows=2)
print cas0
print cas1
print cas2
print cas3
print cas4
#creation plot
fig=plt.figure("comparaison", figsize=(5.5,7))

# creation liste des datas
expdata=[cas0['median'],cas1['median'],cas2['median'], cas3['median'], cas4['median']]
print expdata
#boxplots using sns
couleurs = [sns.desaturate('blue', 0.75),sns.desaturate('red', 0.75),sns.desaturate('green', 0.75),sns.desaturate('red', 0.25), sns.desaturate('green', 0.25)]
#plt.boxplot(data)#, color=['blue', 'red', 'green', 'red', 'green'], saturation=[0,0.5,0.5,0.25,0.25])#,'green'#,'blue','orange'], widths=.5, alpha=0.5)
sns.boxplot(data=expdata, palette=couleurs)
sns.stripplot(data=expdata, size=7, jitter=True, edgecolor="black", palette=couleurs)
#scatter plot using plt
##define vectors
#x1=0*np.ones(len(expdata[0]))
#x2=1*np.ones(len(expdata[1]))
#x3=2*np.ones(len(expdata[2]))
#x4=3*np.ones(len(expdata[3]))
#x5=4*np.ones(len(expdata[4]))
#
#
#
##
###plot scatters
#plt.scatter(x1,cas0['median'], color='blue', alpha=1, s=36)
#plt.scatter(x2,cas1['median'], color='red', alpha=1, s=36)
#plt.scatter(x3,cas2['median'], color='green', alpha=1, s=36)
#plt.scatter(x4,cas3['median'], color='red', alpha=0.75, s=36)
#plt.scatter(x5,cas4['median'], color='green', alpha=0.75, s=36)


#
###separation line(s)
##plt.axvline(x=1.65, linewidth=1, color='k')
#
#
#
##axis and labels
#plt.xlim(0.6,4.6)
#plt.yscale('log')
#plt.xlabel('Indentor type & T')
plt.xticks([0,1,2,3,4], ["Thy1GFP-C", "600-C", "603-C", "600-S30", "603-S30"])
plt.ylabel('Young modulus (Pa) @ 0.5um indentation')
plt.title('Cos variants on FN substrates')
plt.ylim(0,500)

#clean output for screen and save file
fig.tight_layout()
plotname=inputpath+'/comparaison.png'
plt.savefig(plotname)


plt.show()