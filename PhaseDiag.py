# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:33:18 2015

@author: php
"""

import matplotlib.pylab as plt

data = [[10, 50, "carre", "yyy"], 
        [ 15, 25, "rond", "yyn"], 
        [ 30, 30, "carre", "yyn"], 
        [ 50, 25, "rond", "yyn"],
        [5, 10, "rond", "ynn"]]

fig=plt.figure(figsize=(5, 5), dpi=100)

for item in data:
    
    if item[2] == "carre":
        forme = 's'
    elif item[2] == "rond":
        forme = 'o'     
    
    if item[3] == 'yyy':
        couleur = 'green'
    elif item[3] == 'yyn':
        couleur = 'orange'
    else:
        couleur = 'red'
        
    plt.scatter(item[0]-0.5, item[1], s=580, 
           c=couleur, 
           marker=r"$ {} $".format(item[3]), edgecolors='none' )
    plt.scatter(item[0]-0.5, item[1]+0.5, s=800, 
           c=couleur, 
           marker=forme, facecolors='none', edgecolors=couleur )

plt.xlim(-1,101)
plt.xlabel("Diameter of patterned disk (um)")
plt.ylim(-1,101)
plt.ylabel("Spacing of disks (um)")
plt.title("3A9 cells\n")#r'$xxx$'+' : stamping / adhesion / single cell\n')

fig.tight_layout()

plt.show()