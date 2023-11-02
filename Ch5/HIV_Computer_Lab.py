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

#%% HIV
# discretize time for viral load model
time = np.linspace(0, 10, 101)

# define viral load model
def viral_load_model(t, alpha, beta, A, B):
    return A * np.exp(-alpha * t) + B * np.exp(-beta * t)

# set model parameters
A = 10**6
B = 0
alpha = 10**1/22
beta = 10**0
# alpha = 10**-0.3
# beta = 10**0
# A = 10**5.2
# B = 0

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
plt.show()
plt.close()

# print inverse of t cell infection rate alpha
print(1/alpha)

#%% Bacterial
# define growth models
def bacteria_v_t(t, r):
    return 1 - np.e**(-t/r)

def bacteria_w_t(t, r, A):
    return A * (np.e**(-t/r) - 1 + (t/r))



# TODO: create a list two lists of r remaining 1 and A remaining 1 and varying the other
r_vary = A_vary = np.linspace(0, 1, endpoint=True, num=10)
r_const = 1
A_const = 1

A = 1
r = 1
# time_step = 0.01
# time_start = 0.0001
# time_stop = 2.0 + time_step
# bacteria_time = np.arange(time_start, time_stop, time_step)

# define a a time discretization for the bacteria growth models
bacteria_time = np.linspace(0.001, 2.001, num=len(A_vary))


# evaluate w(t) for A = [0,1] r = 1
w_Ai = [bacteria_w_t(bacteria_time, r_const, A_i) for A_i in A_vary]
# evaluate w(t) for A = 1 r = [0,1]
w_ri = [bacteria_w_t(bacteria_time, r_i, A_const) for r_i in r_vary]

# index for incrementing through A values for plot labels
A_index = 0
# plot each w(t) bacteria evaluation for the varying values of A from 0 to 1
for w_i in w_Ai:
    # create label
    plt_label = "A=" + str(A_vary[A_index])
    # plot w(t) for current evaluation with A ranging from 0 to 1
    plt.plot(bacteria_time, w_i, label=plt_label)
    # increment A index to label the next plot appropriately
    A_index += 1
# show the values of A that alter the curve with legend
plt.legend()
# set title
plt.title("Norvick W(t) with varying values for A=[0,1]; r=1")
# set axis labels
plt.xlabel("time in hours")
plt.ylabel("Fraction of maximum beta-galactosidase activity")
plt.show()
plt.close()


# index for incrementing through A values for plot labels
r_index = 0
# plot each w(t) bacteria evaluation for the varying values of A from 0 to 1
for w_i in w_ri:
    # create label
    plt_label = "r=" + str(r_vary[r_index])
    # plot w(t) for current evaluation with A ranging from 0 to 1
    plt.plot(bacteria_time, w_i, label=plt_label)
    # increment r index to label the next plot appropriately
    r_index += 1
# show the values of A that alter the curve with legend
plt.legend()
# set title
plt.title("Norvick W(t) with varying values for r=[0,1]; A=1")
# set axis labels
plt.xlabel("time in hours")
plt.ylabel("Fraction of maximum beta-galactosidase activity")
plt.show()
plt.close()



# w1 = bacteria_w_t(bacteria_time, r, A)
# plt.plot(bacteria_time, w1)


# plt.title("Novick-Weiner W(t)")





