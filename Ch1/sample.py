#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:51:25 2023

@author: ethan
Description: sample
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random
#%%
for i in range(10):
    print(i, random())
plt.figure()
plt.plot(range(10), random(10))

