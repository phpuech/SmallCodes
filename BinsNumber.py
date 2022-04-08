# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:18:49 2015

@author: php
"""

import numpy as np

# nombre de bins pour distribution

#input number of data points
N=50
#if avalaible, spreading and noise of the measure
maxvalue=100
minvalue= 0
noise=10

print "Estimation of number of bins"
print "-----"
print "Only if data spreading and noise are taken into account"
print "Noise method :       ", np.round((maxvalue-minvalue)/noise, decimals=1)
print "-----"
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
print "Bin width :          ", np.round((maxvalue-minvalue)/med, decimals=1)