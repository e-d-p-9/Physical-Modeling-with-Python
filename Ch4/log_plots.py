#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:45:56 2023

@author: ethanpeacock
"""
import numpy as np
import matplotlib.pyplot as plt

# define functions for plotting
def f1(x):
    return np.exp(x)

def f2(x):
    return x**3.6

# create x interval for function evaluations
start = 2
stop = 7
step = 0.01
x = np.arange(start, stop+step, step)

# evaluate functions over x interval 2 <= x <= 7
y1 = f1(x)
y2 = f2(x)

# plot both functions
plt.plot(x, y1, label="$\exp(x)$")
plt.plot(x, y2, label ="$x^{3.6}$")

# add details
plt.xlabel('x')
plt.ylabel('y')
plt.title("$\exp(x)$ vs $x^{3.6}$")
plt.legend()
plt.show()
plt.close()

# create semi log plots of functions above
plt.semilogy(x, y1, label="$\exp(x)$")
plt.semilogy(x, y2, label ="$x^{3.6}$")

# add details
plt.legend()
plt.title("semi log plot of $\exp(x)$ vs $x^{3.6}$")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.close()

# create loglog plot of functions above
plt.loglog(x, y1, label="$\exp(x)$")
plt.loglog(x, y2, label="$x^{3.6}$")

# add details
plt.legend()
plt.title("log log plot of $\exp(x)$ vs $x^{3.6}$")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.close()
