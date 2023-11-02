#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 22:46:19 2023

@author: ethan
"""
import numpy as np
rows = 3
columns = 4
p = 0.1
q = 0.3
A = np.zeros( (rows, columns) )
for m in range(rows):
    for n in range(columns):
        A[m, n] = p**m * q**n
print(A)
