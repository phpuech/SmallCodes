# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:18:49 2015

@author: php
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import os
import time


# where is the file
#repertoire
inputpath = '/home/php/Bureau/'
#fichier
nom = 'martineall' 
suffix = '.csv'
#noms des conditions
conditions = ['A', 'B', 'C', 'D', 'E', 'F']

# for the macro, where to find it

now = time.strftime("%c")
today =time.strftime("%Y")+time.strftime("%m")+time.strftime("%d")
heure = time.strftime("%H")+time.strftime("%M")+time.strftime("%S")
maintenant = today + "-" + heure

outputpath = inputpath+'output'+maintenant+"/"
if not os.path.exists(outputpath):
    os.makedirs(outputpath)

fichier = inputpath + nom + suffix

# nombre de bins pour distribution
df = pd.read_csv(fichier, delimiter=r"\s+",   comment='#', names=conditions, skiprows=0)
colonnes = list(df)
#input number of data points
for col in colonnes:
    valeurs = df[col]
    N=len(valeurs)
    #if avalaible, spreading and noise of the measure
    maxvalue=valeurs.max()
    minvalue= valeurs.min()
    #noise=10
    
    #print "Estimation of number of bins"
    #print "-----"
    #print "Only if data spreading and noise are taken into account"
    #print "Noise method :       ", np.round((maxvalue-minvalue)/noise, decimals=1)
    #print "-----"
    print "Only if number of data points is taken into account"
    a=np.round(np.sqrt(N), decimals=1)
    print "Square root choice : ", a
    b=np.round(1.+np.log(N)/np.log(2), decimals=1)
    print "Sturge :             ", b
    c=np.round(2.*N**(1./3), decimals=1)
    print "Rice :               ", c
    med=np.round((a+b+c)/3, decimals=0)
    print "Mean of 3 methods :  ", med
    print "-----"
    binwidth=np.round((maxvalue-minvalue)/med, decimals=1)
    print "Bin width :          ", binwidth
    
    fig=plt.figure(col, figsize=(10, 5), dpi=100)
    ax1=plt.subplot(121)
    
    plt.plot(valeurs, color='lightblue')
    plt.xlabel("# cell")
    plt.ylabel("Area")
    plt.title("Succession / "+col)
    
    ax2=plt.subplot(122)
    
    valeurs.hist(color='lightblue')#, bins=np.arange(minvalue, maxvalue + binwidth, binwidth), color='lightblue')
    plt.xlabel("Area")
    plt.ylabel("# of events")
    plt.title("Histogram / "+col)
    
#    ax2=plt.subplot(133)
#    
#    plt.boxplot(valeurs)
#    plt.xlabel("")
#    moyenne=np.mean(valeurs)
#    mediane=np.median(valeurs)
#    plt.plot(1,moyenne, 'o', color='red', label='mean')
#    plt.plot(1,mediane, 'o', color='green', label = 'median')
#    #plt.legend()
#    plt.xticks([1], ["Condition"])
#    plt.ylabel("Area")
#    plt.title("Boxplot")

    fig.tight_layout() 
    
    plotname=outputpath+nom+'-'+col+'.png'
    plt.savefig(plotname)
    #release memory
    plt.close(fig)

fig1 = plt.figure("Complete")
df.boxplot()
plt.xlabel("Condition")
plt.ylabel("Area")
plt.ylim(-0.05,)
plotname1=outputpath+nom+'-compare.png'
plt.savefig(plotname1)
plt.show()
    #release memory
plt.close(fig1)
#plt.show()
#plt.show()