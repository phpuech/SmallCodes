# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:40:43 2015

@author: php
"""

# a bunch of packages for simple life
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
import pandas as pd
import os
import time

#---------------------------------------------------

#on recupere les dates et heures de compilation
now = time.strftime("%c")
today =time.strftime("%Y")+time.strftime("%m")+time.strftime("%d")
heure = time.strftime("%H")+time.strftime("%M")+time.strftime("%S")
maintenant = today + "-" + heure
#print now
#print "---------------------------------------------------"
#---------------------------------------------------

# outlook for plots
plt.rcParams.update({'font.size': 16})
#plt.rcParams.update({'font.family':'serif'})

#---------------------------------------------------

# where is the file
# data for processing
inputpath = '/home/php/Bureau/'
outputpath = inputpath
datasave = outputpath+"compilation-"+maintenant +'-data.txt'
#on peut aussi choisir de sauver ailleurs...
#---------------------------------------------------
# fichier de sortie des datas
file = open(datasave, "w")
file.write("# " + now+"\n")
file.write("#---------------------------------------------------\n")
# liste des fichiers au bon format
files = [f for f in os.listdir(inputpath) if f.endswith('.tsv')]
# tri par ordre alphabetique
files.sort()
# preparation du fichier de sortie, separe par des espaces
file.write("# Filename | #FC | Mean E (Pa) | SD E (Pa) | Median E (Pa)\n")
file.write("#---------------------------------------------------\n")
#-------------------------------------------------------

for fichier in files:
    localfichier=inputpath+fichier
    df = pd.read_csv(localfichier, delimiter=r"\s+", names=['0', '1','2', '3','E', '5', '6', '7'], skiprows=1)
    moyenne=np.round(df['E'].mean(), decimals=2)
    sd=np.round(df['E'].std(), decimals=2)
    mediane=np.round(df['E'].median(), decimals=2)
    npoints=len(df['E'])
    file.write(fichier+" "+str(npoints)+" "+str(moyenne)+" "+str(sd)+" "+str(mediane)+"\n")
file = open(datasave, "r")
print file.read()
file.close()