#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
explore the model of the viral load (number of virons in the blood of HIV
                                     infected patient)
after the administration of antiretroviral drug

One model for the viral load predicts that the concentration V(t) of HIV in
the blodo at time t after the start of treatment will be

V(t) = A exp(-a*t) + B exp(-b*t)

The four parameters A, a, B, and b are constants that control the behavior of 
the model

A and B specify the initial viral load
a is the rate at which new cells are infected,
and b is the rate at which virons are removed from the blood


@author: ethanpeacock
"""

import matplotlib.pyplot as plt
import numpy as np

# discretize time for viral load model
time = np.linspace(0, 10, 101)

# define viral load model
def viral_load_model(t, alpha, beta, A, B):
    return A * np.exp(-alpha * t) + B * np.exp(-beta * t)

# set model parameters
A = 10**5.2
B = 0
alpha = 10**1/22
beta = 10**0

# evaluate viral model over time
viral_load = viral_load_model(time, alpha, beta, A, B)
# plot viral load model
plt.plot(time, viral_load, label="V(t) viral load model")


# read in the experimental data
hiv_data_file = "../pmls-data-master/01HIVseries/HIVseries.csv"
hiv_data = np.loadtxt(hiv_data_file, delimiter=',')

# plot experimental data
time_exp = hiv_data[:,0]
concentration = hiv_data[:,1]
plt.plot(time_exp, concentration, 'ko', \
         label="Infected Patient Records")


# add labels title and legend
plt.xlabel('days since starting antiretroviral drug')
plt.ylabel('number of virons in the blood')
plt.legend()

# print inverse of t cell infection rate alpha
print(1/alpha)