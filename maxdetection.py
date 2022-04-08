# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:58:26 2015

@author: php
"""

# local max or min detection on a trace

import numpy as np
from scipy.signal import argrelextrema, medfilt, wiener#, savgol_filter # trop recent pas dans distro scipy
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('real.out', delimiter=r"\s+",   comment='#', names=['t', 'd','d2', 'd3','f'], skiprows=6)
print data

# sampling
seuil=100*10**(-12)
# smoothing by running mean
m=21
n=51

#x = np.random.random(n)



fig0 = plt.figure()


plt.plot(data['t'], data['f'], color='grey')

forcesmooth=pd.rolling_mean(data['f'], m)
forcesmooth2=pd.rolling_mean(forcesmooth, n)

test=medfilt(data['f'].values)
test2=wiener(data['f'].values)

# a la place de ceci il serait peut etre bon de faire un polynomial machin
# sinon on a un multiple peak detection

timesmooth=pd.rolling_mean(data['t'], m)
timesmooth2=pd.rolling_mean(timesmooth, n)


#plt.plot(data['t'],test2, color='blue')
#plt.plot(data['t'],test, color='green')
#plt.plot(timesmooth, forcesmooth, color='red')
plt.plot(timesmooth2, forcesmooth2, color='black')

#
# ici il faudrait smoother le bruit pour eviter d'avoir tous les pics

# for local maxima
#print argrelextrema(forcesmooth, np.greater)

# for local minima
#print argrelextrema(x, np.less)

y=forcesmooth2.values
x=timesmooth2.values


#x=data['t']
#print x
values=y[argrelextrema(y, np.greater)[0]]
#
#values=y[argrelextrema(y, np.greater)[0]]
positions=x[argrelextrema(y, np.greater)[0]]
#
yy=[]
xx=[]
l=len(values)
for i in np.arange(l):
    if values[i] > seuil:
        yy.append(values[i])
        xx.append(positions[i])
        

## apres il faut dire "et y superieur a x fois le bruit"
#
plt.plot(xx,yy,'o', color='green')



fig1 = plt.figure()
temps = xx - xx[0]
p=len(temps)
index=np.arange(p)
plt.scatter(index, temps, s=34)


fig2 = plt.figure() 
index2=np.arange(p-1)
ecart=[]
for i in np.arange(p-1):
    ecart.append(temps[i+1]-temps[i])

plt.scatter(index2, ecart, color='red', s=34)



plt.show()