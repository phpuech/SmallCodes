# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:44:24 2015

Corrected PHP June 2016 for d0

@author: php
"""

"""
simple boxplot

"""


#---------------------------------------------------

# a bunch of packages for simple life
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
import pandas as pd
import os
import seaborn as sns
#from statsmodels import eval_measures


#---------------------------------------------------

# outlook for plots
#plt.rcParams.update({'font.family':'serif'})
#plt.rcParams.update({'font.size': 16})

sns.set_style("white")
sns.set_context("talk")#, font_scale=1.5)

#---------------------------------------------------

# where is the file
#repertoire
inputpath = '/home/php/Bureau/PHP-DEV/ReferencingvsCopying/'
#fichier
suffix = '.txt'
nom = 'percent' 
# for the macro, where to find it
fichier = inputpath + nom + suffix

df1 = pd.read_csv(fichier, delimiter=r"\s+",   comment='#', names=['p'], skiprows=1)
print "---------------COLONNES---------------"
print "before calculation"
print "df1"
print df1['p']
x=df1['p']
y=x
x=x-4

# test referencing vs copying in python for columns
# attention ce n'est pas la meme chose pour les dataframe
print "after calculation"
print "x=colonne-4"
print x
print "y=x avant calcul"
print y
print "df1 last"
print df1['p']
print "---------------DATAFRAMES---------------"
dfx=df1
dfcopy=df1.copy()
print "df1"
print df1
dfy=dfx
dfz=df1 #idem si on met dfx
dfx[0:3]=0
dfz=dfz-4
print "dfx reset to 0"
print dfx
print "dfy = dfx avant reset"
print dfy
print "dfz = dfz avant reset, moins 4"
print dfz
print "df1 last"
print df1
print "df copy"
print dfcopy

# fig1=plt.figure(figsize=(5, 7), dpi=100)

# sns.boxplot(df1, width=.3, color="white")
# sns.stripplot(y=df1, jitter=False, size=7, color=".3", linewidth=0)

# plt.ylabel("percent increased indentation", fontsize = 16)

# plt.show()

# fig1.tight_layout() 
