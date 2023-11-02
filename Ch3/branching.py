#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script illustrates branching.

@author: ethan
"""
import numpy as np

maxTrials = 5

for trial in range(1, maxTrials+1):
    userInput = input('Pick a number: ')
    number = float(userInput)
    if number < 0:
        print('The square root is not real.')
    else:
        print('The square root of {} is {:.4f}.' \
              .format(number, np.sqrt(number)))
    userAgain = input('Try another [y/n]? ')
    if userAgain != 'y':
        break

#%% Check to see if the loop exited normally.
if trial >= maxTrials:
    print('Sorry, only {} per customer.'.format(maxTrials))
elif userAgain == 'n':
    print('Bye!')
else:
    print('Sorry, I did not understand that.')
