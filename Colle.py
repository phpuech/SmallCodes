# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:42:02 2015

@author: php
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
import pandas as pd
import os

x=["2C-470", "2C-555", "2C-625", "UV-470", "UV-555", "UV-625"]
xx=[0,1,2,3,4,5]
y=[10.6, 1.41, 1, 1.18, 1.01,1]
couleurs=["lightblue", "lightgreen", "pink","lightblue", "lightgreen", "pink"]

fig1=plt.figure(figsize=(6,6), dpi=100)
ax1=plt.subplot(111)

plt.bar(xx, y, color=couleurs, width=0.6)
plt.xlim(-0.25,6)
plt.ylim(0,11)
plt.xlabel("Glue-Wavelength (nm)", fontsize = 16)
xxx=[0.3, 1.3, 2.3, 3.3, 4.3, 5.3]
plt.xticks(xxx, x)
plt.ylabel("F/F0 with 40x0.75 @ 50%", fontsize = 16)

texte="2C = 2-components epoxy\nUV = UV curable optical glue"
ax1.text(2,9.5, texte, fontsize=12)

plt.axhline(y=1, color="black", ls='--', alpha=0.5)
plt.axhline(y=7, color="red", ls='--', alpha=0.5)
ax1.text(2,7.5, "Max. Ca++ signal", color="red", alpha=0.5, fontsize=12)


fig1.tight_layout() 
plt.show()