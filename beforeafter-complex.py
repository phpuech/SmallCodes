# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:52:08 2015

@author: php
"""

import numpy as np
import matplotlib.pyplot as plt  
#--------------------------------
def points(x,y,n): # Plot n points symmetrically aligned about axes
    dx=0.03  # define distance between individual dots    
    m = 1-(n%2) # ensure symmetrical alignment for odd or even number of dots
    while(m<n):
        plt.scatter(x+(dx*m),y,color = 'k', marker = 'o', s=50, zorder=1)
        plt.scatter(x-(dx*m),y,color = 'k', marker = 'o', s=50, zorder=1)
        m+=2 
    return   
#--------------------------------   
def histogram(b): # count number of data points in each bin
    for col in range(0,2):
        count = np.unique(b[:,col], return_counts=True)  
        for n in range(0,np.size(count[col])):
            points(col,count[0][n], count[1][n])
    return
#-------------------------------        
def partition(a,bins): # partition continuous data into equal sized bins for plotting     
    lo = np.min(a)
    hi = np.max(a)
    rng = hi-lo
    step = rng/float(bins-1)

    for col in range (0,2):
        for row in range (0,int(np.size(a,axis=0))):
            for n in range (0,bins):
             if (a[row,col] <= (lo + (step / 2) + n * step)):
                 b[row,col] = (lo + (n * step))
                 break
    return(b)    
#--------------------------------    
def lines(b): # draw 'before' and 'after' lines between paired data points + median line
    for row in range (0,int(np.size(a,axis=0))):
        plt.plot([0,1],[b[row,0], b[row,1]], c='k',zorder=0, lw=1, alpha=0.3)
        plt.plot ([0,1],[np.median(b[:,0]),np.median(b[:,1])],c='r',zorder=2, lw=2, alpha=1)
    return
#================================    
# MAIN   
# Dummy paired continuous data (...or import from spreadsheet as a numpy array)\;    
a = np.array([
 [1.62,1.53,1.42,1.39,1.11,1.20,0.99,0.88,0.60,0.65,0.52,0.49,0.43,0.41,0.31], # before
[0.8,0.7,0.52,0.61,0.44,0.43,0.49,0.33,0.44,0.39,0.20,0.29,0.37,0.19,0.00] ]) # after

bins = 10 # choose total number of bins to categorise data into
ax=plt.axes()

a = a.transpose()
b=a # make a copy of the input data matrix to write categorised data to
b = partition(a,bins) # partition continuous data into bins
lines(b) # draw lines between mid points of each bin and draw median line
histogram(b) # draw histograms centered at mid points of each bin

# Make general tweaks to plot appearance here:
plt.xticks([0,1], ['OUT', 'IN'], fontsize=14)
plt.ylabel('stimulation threshold (mA)',fontsize=13)
plt.text(0.8,1.3,'All patients',fontsize=13)
ax.patch.set_facecolor('white') # set background colour for plot area (default = white)
ax.spines['top'].set_visible(False)   # remove default upper axis
ax.spines['right'].set_visible(False) # remove default right axis
plt.tick_params(axis='both',which='both',direction = 'out',top='off', right = 'off',labeltop='off') # remove tick marks from top & right axes
plt.xlim(-0.6,1.6)
plt.ylim(0,1.7)

plt.show()   