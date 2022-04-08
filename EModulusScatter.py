# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:26:23 2015

@author: php
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import os
import time
#import seaborn as sns


#sns.set_style("white")
# where is the file
#repertoire
inputpath = '/home/php/Bureau/'
#fichier
nom = 'Young' 
suffix = '.csv'
#noms des conditions
conditions = ['10um', '15um', '30um', 'continuous']


fichier = inputpath + nom + suffix

df = pd.read_csv(fichier, delimiter=r"\s+",   comment='#', names=conditions, skiprows=0)

colonnes = list(df)

fig=plt.figure(nom, figsize=(7, 7), dpi=100)

i=1
for col in colonnes:
    l=len(df[col])
    x=np.ones(l)*i
    plt.scatter(x,df[col], facecolors='none', edgecolors='black')
    moyenne=np.mean(df[col])
    plt.scatter(i,moyenne, s=64,color='red', alpha=0.5)
    i=i+1

df.boxplot()

plt.ylim(0,)
plt.xlabel("Surface type, indentation @ 500nm")
plt.ylabel("Young modulus (Pa)")

fig.tight_layout() 

plt.show()
