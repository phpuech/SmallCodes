# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 12:08:39 2014

@author: php
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.patches import ConnectionPatch
# from matplotlib.lines import Line2D
import pandas as pd
# import scikits.statsmodels.api as sm
#import scikits.statsmodels.graphics as smg
#--------------------------------
# definition d'une fonction de trace pour les courbes autres que fond et stim
def trace(x):
    for i in np.arange(1,len(x.columns)):
        plt.plot(temps, x[i], alpha=0.25, linewidth=1)#, color='red')
    
# -------------------------------
#recuperation des donnees d'un csv avec pandas
fluo = pd.read_csv('test.csv', sep=r'\s+', header=None)#, header = True)
# valeur de l'increment de temps par image
dt=1 # en secondes

print fluo
print fluo[0]
# -------------------------------
# ATTENTION TRES IMPORTANT
# les donnees ont deja un fond soustrait cf. fiji
# on utilise pour cela la fonction "substract background"
# -------------------------------



temps = (fluo[0]-1)*dt

#plot original data
fig0 = plt.figure()
# title of the entire figure

plt.subplot(221)
trace(fluo)
plt.xlabel('Time (sec)')
plt.title('Fluo bckgd substracted, Fiji')
#plt.legend(loc='upper left')
plt.ylabel('Grey level')
plt.ylim(0,2**16)

#  la normalisation doit se faire avant la moyenne !!!

# calcul de la moyenne de tout sauf temps
col=set(fluo.columns)
col.remove(0)
#col.remove(55) #si une cellule problematique
col =list(col)
fluosub=fluo[col]
print fluosub
initial=fluosub.iloc[0]
fluosub=fluosub/fluosub.iloc[0]
fluomean=fluosub.mean(axis=1)
fluosd=fluosub.std(axis=1)/sp.sqrt(len(fluosub.columns)) #goes for sem


#creation d'une figure
plt.subplot(223)
for i in np.arange(1,len(fluo.columns)):
    plt.plot(temps, fluosub[i], alpha=0.25, linewidth=1)#, color='red')
plt.xlabel('Time (sec)')
plt.ylabel('F/F0')
plt.title('Fluo, norm.')
#plt.legend(loc='lower left')
    
plt.subplot(222)
initial.hist(alpha=0.25, color='green', grid=False)
plt.xlabel('F0 (Grey level)')
plt.xscale('log')
plt.ylabel('# cells')
plt.title('Distribution label.')    
    
plt.subplot(224)
plt.plot(temps, fluomean-fluosd, alpha=0.5, linewidth=2, color='green',ls='dashed')
plt.plot(temps, fluomean, alpha=0.5, linewidth=2, color='green')
plt.plot(temps, fluomean+fluosd, alpha=0.5, linewidth=2, color='green',ls='dashed')
#plt.legend(loc='upper left')
plt.xlabel('Time (sec)')
plt.ylabel('F/F0')
plt.title('Mean +/- sem')
plt.ylim(0.5,)

# plot only of the last figure in case of need
fig1 = plt.figure(figsize=(5, 4))
plt.plot(temps, fluomean-fluosd, alpha=0.5, linewidth=2, color='green',ls='dashed')
plt.plot(temps, fluomean, alpha=0.5, linewidth=2, color='green')
plt.plot(temps, fluomean+fluosd, alpha=0.5, linewidth=2, color='green',ls='dashed')
#plt.legend(loc='upper left')
plt.xlabel('Time (sec)')
plt.ylabel('F/F0')
plt.title('Soluble stimulation, Iono @ 10 sec')
plt.ylim(0.5,)
#plt.legend(deux, 'images')
#fig.legend()

fig0.tight_layout()
fig1.tight_layout()

#figOr.tight_layout()



plt.show()