# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:30:07 2015

@author: php
"""

## numpy is used for creating fake data
import numpy as np 
import matplotlib as mpl 

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt 

## Create data
np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)

## combine these different collections into a list    
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
#bp = ax.boxplot(data_to_plot)

# Save the figure
#fig.savefig('fig1.png', bbox_inches='tight')

## add patch_artist=True option to ax.boxplot() 
## to get fill color
#bp = ax.boxplot(data_to_plot, patch_artist=True)
bp = ax.boxplot(data_to_plot, 0,'rs',0, patch_artist=True)
## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='black', linewidth=2, alpha=0.5)
    # change fill color
    box.set( facecolor = 'white' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(ls='-',color='black', linewidth=2, alpha=0.5)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='white', linewidth=0, alpha=0.5)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='black', linewidth=2, alpha=0.5)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='black', alpha=0.5, mfc='None' )
    
## Custom x-axis labels
ax.set_yticklabels(['Sample1', 'Sample2', 'Sample3', 'Sample4'])

## Remove top axes and right axes ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()



plt.show()
fig.savefig('fig1.png', bbox_inches='tight')