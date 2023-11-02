#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculate how long an object is in the air when thrown from a specified height
with a range of initial speeds assuming constant acceleration due to gravity:
    0.5 * g * t**2 - v0 * t - y0 = 0

@author: ethan
"""
import numpy as np

#%% Initialize variables.
initial_speed = 0.0              # v0 = initial vertical speed of ball [m/x]
impact_time = 0.0                # t = time of impact [s] (computed in loop)

#%% Initialize parameters.
g = 9.80665                      # Gravitational acceleration [m/s^2]
initial_height = 2.0             # y0 = height ball is thrown from [m]
speed_increment = 5.0            # Speed increment for each iteration [m/s]
cutoff_time = 10.0               # Stop computing after impact time exceeds cutoff.

#%% Calculate and display impact time.  Increment initial speed each step.
#   Repeat until impact time exceeds cutoff.
while impact_time < cutoff_time:
    # Use quadratic equation to solve kinematic equation for impact time:
    impact_time = (np.sqrt(initial_speed**2 + 2 * g * initial_height) \
                   + initial_speed) / g
    print("speed= {} m/s; time={:.1f} s".format(initial_speed, impact_time))
    initial_speed += speed_increment
print("Calculation complete")