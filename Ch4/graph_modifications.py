#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:55:23 2023

@author: ethanpeacock
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 100)
y = np.sin(x**2)
y1 = np.sin(1/x)

ax = plt.gca()
ax.set_title("My first plot", size=24, weight='bold')
ax.set_xlabel("speed [um/s]")
ax.set_ylabel("kinetic energy")
ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)
ax.plot(x, y)
ax.plot(x, y1)
lines = ax.get_lines()       # a list of line objects
# make the first line thick, dashed, and red
plt.setp(lines[0], linestyle='--', linewidth=1, color='r')
plt.setp(lines[1], linestyle='*', linewidth=5, color='k')