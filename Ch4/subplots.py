#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:16:30 2023

@author: ethanpeacock
"""
from numpy.random import random
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 101)
fig, ax = plt.subplots(2, 2)
ax[0,0].hist(random(20))
ax[0,1].plot(t, t**2, t, t**3 - t)
ax[1,0].plot(random(20), random(20), 'r*')
ax[1,1].plot(t*np.cos(10*t), t*np.sin(10*t))
fig.suptitle("Data and Functions 2")

fig = plt.gcf()
print(fig.canvas.get_supported_filetypes())
plt.savefig("greatest_figure_ever.pdf")
