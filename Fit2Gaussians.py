# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:19:51 2015

@author: php
"""

import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

######################################
# Setting up test data
def norm(x, mean, sd):
  norm = []
  for i in range(x.size):
    norm += [1.0/(sd*np.sqrt(2*np.pi))*np.exp(-(x[i] - mean)**2/(2*sd**2))]
  return np.array(norm)

mean1, mean2 = 0, 7
std1, std2 = 1, 1.5

x = np.linspace(-20, 20, 1000)
y_real = norm(x, mean1, std1) + norm(x, mean2, std2)
noise = np.random.normal(0,0.01,len(x))
y_real=y_real+noise
offset = np.random.normal(1,10,1)
x=x+offset+noise

######################################
# Solving
m, dm, sd1, sd2 = [5, 10, 1, 1]
p = [m, dm, sd1, sd2] # Initial guesses for leastsq
y_init = norm(x, m, sd1) + norm(x, m + dm, sd2) # For final comparison plot

def res(p, x, y):
  m, dm, sd1, sd2 = p
  m1 = m
  m2 = m1 + dm
  y_fit = norm(x, m1, sd1) + norm(x, m2, sd2)
  err = y - y_fit
  return err

plsq = leastsq(res, p, args = (x, y_real))

y_est = norm(x, plsq[0][0], plsq[0][2]) + norm(x, plsq[0][0] + plsq[0][1], plsq[0][3])
y1=norm(x, plsq[0][0], plsq[0][2])
#y1pos=norm(plsq[0][0], plsq[0][0], plsq[0][2])

y2=norm(x, plsq[0][0] + plsq[0][1], plsq[0][3])
#y2pos=norm(plsq[0][0] + plsq[0][1], plsq[0][0] + plsq[0][1], plsq[0][3])

print "Means"
print "First gaussian", np.round(plsq[0][0], decimals=2)
print "Second gaussian", np.round(plsq[0][0] + plsq[0][1], decimals=2)

fig=plt.figure('Two gaussian fit')
ax1=plt.subplot(111)
plt.plot(x,y_real, label='Real Data', color='grey', alpha=0.5)
#plt.plot(x, y_init, 'r.', label='Starting Guess')
plt.plot(x, y_est, 'r-', label='Fitted')
plt.plot(x, y1, 'b--', label='Composantes')
plt.plot(x, y2, 'b--')
plt.ylabel('Probability')
plt.xlabel('Parameter value')

plt.ylim(-0.05,0.75)
plt.xlim(-30, 30)


texte="Positions\nFirst peak : "+str(np.round(plsq[0][0], decimals=1))+"\nSecond peak : " +str(np.round(plsq[0][0]+ plsq[0][1], decimals=1))
ax1.text(10, 0.6, texte, fontsize=12) 
#plt.title(texte) 

#max1=str(np.round(plsq[0][0], decimals=1))
#max2=str(np.round(plsq[0][0]+ plsq[0][1], decimals=1))
#ax1.text(plsq[0][0], y1pos+0.05, max1)
#ax1.text(plsq[0][0]+ plsq[0][1], y2pos1+0.05, max2)

#plt.legend(frameon=False)

plt.show()