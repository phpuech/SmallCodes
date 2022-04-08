# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:51:50 2015

@author: php
"""

import matplotlib.pyplot as plt
import numpy as np

# your input data:
befores = np.random.rand(10)
afters = np.random.rand(10)

# plotting the points
plt.scatter(np.zeros(len(befores)), befores)
plt.scatter(np.ones(len(afters)), afters)

# plotting the lines
for i in range(len(befores)):
    plt.plot( [0,1], [befores[i], afters[i]], c='k')

plt.xticks([0,1], ['before', 'after'])

plt.show()