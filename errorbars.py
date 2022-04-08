# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:02:14 2015

@author: php
"""

"""
Demo of errorbar function with different ways of specifying error bars.

Errors can be specified as a constant value (as shown in `errorbar_demo.py`),
or as demonstrated in this example, they can be specified by an N x 1 or 2 x N,
where N is the number of data points.

N x 1:
    Error varies for each point, but the error values are symmetric (i.e. the
    lower and upper values are equal).

2 x N:
    Error varies for each point, and the lower and upper limits (in that order)
    are different (asymmetric case)

In addition, this example demonstrates how to use log scale with errorbar.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams.update({'font.size': 18})
#font = FontProperties()
#font.set_name('Script MT')
#font.set_family('serif')
#font.set_variant('normal')
plt.rc('font', family='sans') 


# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
# example error bar values that vary with x-position
error = 0.1 + 0.2 * x
# error bar values w/ different -/+ errors
lower_error = 0.4 * error
upper_error = error*.25
asymmetric_error = [lower_error, upper_error]

fig = plt.figure('Test',  figsize=(7, 7))
plt.errorbar(x, y,markersize=10,xerr=asymmetric_error, yerr=asymmetric_error, fmt='o', color='black')
#plt.plot(x,y,'-', color='red')
plt.title('Error plot, Old school font')
plt.xlabel('variable')
plt.ylabel('Parameter')
plt.xlim(-0.05, )
plt.ylim(-.35,)

fig.tight_layout()

plt.show()