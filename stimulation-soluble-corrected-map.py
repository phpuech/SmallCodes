# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 12:08:39 2014

@author: php
"""
# set minimaliste de packages utiles
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# aesthetics of seaborn / matplotlib plots
sns.set_style("white")

#--------------------------------
# definition d'une fonction de trace pour les courbes autres que fond et stim

def trace(x,y):
    #recuperation des noms des colonnes
    noms=y.columns.values
    #trace de tout sauf du temps en fonction du temps calcule
    for i in np.arange(0,len(y.columns)):
        if i>0:
            plt.plot(x, y[noms[i]], alpha=0.25, linewidth=1)#, color='red')
    
# -------------------------------
#recuperation des donnees d'un csv avec pandas SANS header () (sinon changer l'option en True)
fluo = pd.read_csv('iono.csv', delimiter=r"\s+", header=None)#, header=True)
# valeur de l'increment de temps par image
dt=1 # en secondes

# recuperation des noms des colonnes données dans le fichier texte
names = fluo.columns.values
#print names[1]

# -------------------------------
# ATTENTION TRES IMPORTANT
# les donnees ont deja un fond soustrait cf. fiji
# on utilise pour cela la fonction "substract background"
# attention au choix de la valeur : la noter dans le cahier
# -------------------------------


# correction du temps et mise en place de l'ecart temporel entre deux frames
temps = (fluo[names[0]]-1)*dt

# recuperation des donnees sauf du temps pour faire les calculs
subnames=names[1:]
# si la colonne i est problematique
# subnames=names[1:i-1]+names[i+1:]

# on elimine le temps et on a que la fluo
fluosub=fluo[subnames]
#print fluosub
#on recupere les valeurs initiales de la fluo
#initial=fluo[subnames[0]]
initial=fluosub.iloc[0]
#on elimine le niveau de depart
fluosubcorr=fluosub/initial
#for i in subnames:
#    fluosubcorr[i]=fluosubcorr[i]/fluosubcorr[i][0]
# on calcule les moyennes et sem des signaux
fluomean=fluosubcorr.mean(axis=1)
fluosem=fluosubcorr.std(axis=1)/sp.sqrt(len(fluosubcorr.columns)) #goes for sem

#creation de la figure tout en une
fig0 = plt.figure()

# plot des donnees originelles
plt.subplot(221)
trace(temps, fluo)
plt.xlabel('Time (sec)')
plt.title('Fluo bckgd substracted, Fiji')
plt.ylabel('Grey level')
plt.ylim(0,)

# distribution des niveaux initiaux de fluo    
plt.subplot(222)
initial.hist(alpha=0.25, color='green', grid=False)
plt.xlabel('F0 (Grey level)')
plt.xscale('log')
plt.ylabel('# cells')
plt.title('Distribution label.')    

# plot des donnees en ratio ramene a la fluo initiale : F/F0
plt.subplot(223)
trace(temps, fluosubcorr)
plt.xlabel('Time (sec)')
plt.ylabel('F/F0')
plt.title('Fluo, norm.')

# courbe moyenne et sem
plt.subplot(224)
plt.plot(temps, fluomean-fluosem, alpha=0.5, linewidth=2, color='green',ls='dashed')
plt.plot(temps, fluomean, alpha=0.5, linewidth=2, color='green')
plt.plot(temps, fluomean+fluosem, alpha=0.5, linewidth=2, color='green',ls='dashed')
plt.xlabel('Time (sec)')
plt.ylabel('F/F0')
plt.title('Mean +/- sem')
plt.ylim(0.5,)

# on recree la derniere figure pour export separe
fig1 = plt.figure(figsize=(5, 4))
plt.plot(temps, fluomean-fluosem, alpha=0.5, linewidth=2, color='green',ls='dashed')
plt.plot(temps, fluomean, alpha=0.5, linewidth=2, color='green')
plt.plot(temps, fluomean+fluosem, alpha=0.5, linewidth=2, color='green',ls='dashed')
plt.xlabel('Time (sec)')
plt.ylabel('F/F0')
plt.title('Soluble stimulation, Iono @ 10 sec')
plt.ylim(0.5,)

# on recree la derniere figure pour export separe
fig2 = plt.figure(figsize=(5, 4))
turned=fluosubcorr.transpose()
l=len(turned)
noms=l-np.arange(0,l)
#ax=sns.heatmap(turned, xticklabels=10, yticklabels=noms, cmap='jet', vmin=0, vmax=13, cbar=False)
ax=sns.heatmap(turned, xticklabels=10, yticklabels=False, cmap='viridis', vmin=1, vmax=13, cbar=False)#jet iintroduces a lot of funny errors
cbar = ax.figure.colorbar(ax.collections[0])
cbar.set_label('F/F0', rotation=270)
plt.xlabel('Time (sec)')
plt.ylabel('Individual cell')


# amelioration esthetique des deux figures
fig0.tight_layout()
fig1.tight_layout()
fig2.tight_layout()

# on affiche les figures
plt.show()