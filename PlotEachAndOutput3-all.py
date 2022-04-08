# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 17:31:17 2015

@author: as
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

inputpath = '/home/as/Bureau/etudiants/ambroise/AFMdata/151229-cos600-mlctuc-11um-si-derriere/tsv/'
outputpath = inputpath + 'output.txt'

print "open path and saved file"
print inputpath
print outputpath

#files =[]
files = [f for f in os.listdir(inputpath) if f.endswith('.tsv')]

#print files
print "------------------------------------"
#print files

file = open(outputpath, "w")
file.write("# Data output in Pa\n")
file.write("# File  Mean    SD    Median\n")

for i in files :
    openfile=inputpath+i
    print openfile
# -------------------------------
#import datas as columns in pandas
#note delimiter type is set to tab or space or the two
    df1 = pd.read_csv(openfile, delimiter=r"\s+",  names=['0','1','2','3','4','5','6', 'E','8', '9', '10', '11', '12'], skiprows=1)
    print df1['E']
    
    plt.figure(i)

    plt.plot(df1['E'], 'ro')
    plt.plot(df1['E'], 'r')

    plt.xlim(-1,len(df1['E']+1))
    plt.ylim(-1,)
    plt.xlabel("FC number")
    plt.ylabel("Young modulus, E (Pa)")
    plt.title(i)

    mean=df1.mean(axis=0)['E']
    sd=df1.std(axis=0)['E']
    median=df1.median(axis=0)['E']

    texte="Mean = " + str(mean) + " +/- "+ str(sd) + " Pa\n" + "Median =  " + str(median) + " Pa"

    plt.text(0,50, texte)  
    
    
        
    
    print "Mean value (Pa) = ", mean
    print "Std deviation (Pa) = ", sd
    print "Median value (Pa) = ", median
    print "------------------------------------"

    plotname=openfile+'.png'
    plt.savefig(plotname)
    
    sortie=i+" "+str(mean)+" "+str(sd)+" "+str(median)+"\n"
    #print sortie
    file.write(sortie)

    
file.close()

# trace de toutes les conditions sur un seul graphe
plt.figure("All")
for i in files :
    openfile=inputpath+i
# -------------------------------
#import datas as columns in pandas
#note delimiter type is set to tab or space or the two
    df2 = pd.read_csv(openfile, delimiter=r"\s+",  names=['0','1','2','3','4','5','6', 'E','8', '9', '10', '11', '12'], skiprows=1)
    
    plt.plot(df2['E'], marker="o")

    plt.xlim(-1,11)
    plt.ylim(-1,1000)
    plt.xlabel("FC number")
    plt.ylabel("Young modulus, E (Pa)")

plotname2=inputpath+'all.png'
plt.savefig(plotname2)

plt.show()

    