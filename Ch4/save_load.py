#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:09:18 2023

@author: ethanpeacock
"""
import numpy as np

x = np.linspace(0, 1, 1001)
y = 3*np.sin(x)**3 - np.sin(x)

# save data to files
np.save('x_values', x)
np.save('y_values', y)
np.savetxt('x_values.dat', x)
np.savetxt('y_values.dat', y)
np.savez('xy_values', x_vals=x, y_vals=y)

# load data from files
x2 = np.load('x_values.npy')
y2 = np.loadtxt('y_values.dat')
w = np.load('xy_values.npz')

print(x2 == x)
print(y2 == y)
print(w['x_vals'] == x)
print(w['y_vals'] == y)

