# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:09:01 2015

@author: php
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
import pandas as pd
import os

# for test
#distribution = "gaussian"
distribution = "evans" #skewed

# d'apres Zhang 2002
def Distri(n,f):
    l=len(f)
    y=np.ones(l)
    j=0
    if n=="evans":
        for i in f:
            y[j]=np.exp(i)*np.exp(1.-np.exp(i))
            j=j+1
    if n=="gaussian":
        for i in f:
            y[j]=np.exp(-i**2)
            j=j+1
    return y

# fit function corresponding
def FitDistri(f, *p):
    l=len(f)
    y=np.ones(l)
    j=0
    for i in x:
        y[j]=(p[1]*np.exp(p[2]*(i-p[0]))*np.exp(p[3]-np.exp(p[2]*(i-p[0]))))#*p[4] #if not normalized
        j=j+1
    return y

#finding nearest
def where(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]

# fake x values for demo
linx=np.arange(-10,10,0.01)


fig1=plt.figure(figsize=(6,6), dpi=100)

# definition of plot as a grid to have the residues above the fitted curve
gs = gridspec.GridSpec(2, 1,height_ratios=[1,3])
# for axis label localization, to align the labels
labelx = -0.1


ax1=plt.subplot(gs[1])

noise = np.random.normal(0,0.1,len(linx))
noisy = noise + Distri(distribution, linx)
offset = np.random.normal(1,10,1)
x=linx+offset+noise

# faire un guess resonnable pour la position du max
yguess=np.max(noisy)
indexguess=(np.abs(noisy-yguess)).argmin()
xguess=x[indexguess]
# passer les initialguess
initialguess=[xguess,1,1,1]#, yguess] if not normalized

#le parametre critique pour ce fit est p[0] il faut un estimate pas trop delirant si le bruit est grand

fitParams, fitCovariances = curve_fit(FitDistri, x, noisy, p0=initialguess)
fitted = FitDistri(x, fitParams[0], fitParams[1], fitParams[2], fitParams[3])#, fitParams[4]) if not normalized

plt.plot(x, noisy, '.', color='grey')
#plt.plot(x, Distri(x), color='blue', alpha=0.5)
plt.plot(x, fitted, color='red', alpha=0.75, lw=2)

plt.xlim(-11,21)
plt.ylim(-0.5,1.5)
plt.xlabel("Force (UA)", fontsize = 16)
plt.ylabel("Probability (UA)", fontsize = 16)

ax2 = plt.subplot(gs[0], sharex=ax1)
# calculate residues
residus = noisy - fitted
# plot residues of fits
plt.plot(x, residus, "-", color="black", alpha=0.5)
# set the plot
plt.ylabel('Res. (UA)', fontsize = 16)
plt.ylim(-1,1)
# align y axis label
ax2.yaxis.set_label_coords(labelx, 0.5)
# remove ticks of x axis
plt.setp( ax2.get_xticklabels(), visible=False)

print initialguess
print fitParams

fig1.tight_layout() 

plt.show()