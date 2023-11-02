#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 22:17:08 2023

@author: ethan
"""
import numpy as np
# perform larger calculations past 4300 for integer string conversion
import sys
sys.set_int_max_str_digits(0)
a, b, c = 2, 2, -1
while (b**2 - 4*a*c >= 0):
    x = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
    print("a = {:.4f}, x = {:.4f}".format(a, x))
    a -= 0.3
print("done!")

for ii in range(10**6):
    if ii % 10**5 == 0: print("{:.0f} percent complete".format( 100*ii/10**6 ))
